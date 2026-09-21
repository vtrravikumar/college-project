"""End-to-end historical-style GA training loop.

This is a modern Python reconstruction of the GA training flow evidenced by
Code-01. It is not historical Python and does not claim byte-for-byte
equivalence to the C program.

The loop combines the reconstructed:
- binary chromosome/population
- historical-style fitness evaluation
- roulette selection
- crossover and mutation
- two-child lower-error survivor
- replacement of the current worst member

For weight optimisation, connectivity is supplied separately and remains
fixed while the 100-bit weight chromosome evolves, matching the report's
separate treatment of weights and connections.

The random initialisation is necessarily a modern reproducible choice because
the original random stream/initial population cannot be recovered exactly.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from historical_chromosome import build_chromosome
from historical_fitness import mean_squared_error
from historical_ga_generation import generate_one_step


@dataclass(frozen=True)
class HistoricalTrainingResult:
    best_chromosome: np.ndarray
    best_fitness: float
    generations_completed: int
    success: bool
    initial_best_fitness: float
    best_fitness_history: tuple[float, ...]


def _fitness_function(
    chromosome_bits: np.ndarray,
    connectivity_bits: str,
    inputs: tuple[Sequence[float], ...],
    targets: tuple[Sequence[float], ...],
    *,
    upper_range: float,
) -> float:
    chromosome = build_chromosome(
        "".join(str(int(bit)) for bit in chromosome_bits),
        connectivity_bits,
    )
    return mean_squared_error(
        inputs,
        targets,
        chromosome,
        upper_range=upper_range,
    )


def train_historical_ga(
    rng: np.random.Generator,
    inputs: tuple[Sequence[float], ...],
    targets: tuple[Sequence[float], ...],
    *,
    population_size: int,
    generations: int,
    crossover_probability: float,
    mutation_probability: float,
    upper_range: float,
    connectivity_bits: str = "1" * 10,
    success_threshold: float = 0.05,
) -> HistoricalTrainingResult:
    """Run the reconstructed binary GA until success or max generations."""
    if population_size < 2:
        raise ValueError("population_size must be at least 2")
    if generations < 0:
        raise ValueError("generations must be non-negative")
    if len(connectivity_bits) != 10 or any(bit not in "01" for bit in connectivity_bits):
        raise ValueError("connectivity_bits must contain exactly 10 binary values")

    population = rng.integers(
        0, 2, size=(population_size, 100), dtype=np.uint8
    )

    def evaluate(chromosome: np.ndarray) -> float:
        return _fitness_function(
            chromosome,
            connectivity_bits,
            inputs,
            targets,
            upper_range=upper_range,
        )

    fitness = np.array([evaluate(chromosome) for chromosome in population])
    best_index = int(np.argmin(fitness))
    best_chromosome = population[best_index].copy()
    best_fitness = float(fitness[best_index])
    initial_best = best_fitness
    history = [best_fitness]

    if best_fitness < success_threshold:
        return HistoricalTrainingResult(
            best_chromosome=best_chromosome,
            best_fitness=best_fitness,
            generations_completed=0,
            success=True,
            initial_best_fitness=initial_best,
            best_fitness_history=tuple(history),
        )

    completed = 0
    for _ in range(generations):
        result = generate_one_step(
            rng,
            population,
            fitness,
            crossover_probability=crossover_probability,
            mutation_probability=mutation_probability,
            evaluate=evaluate,
        )
        population = result.new_population
        fitness = np.array([evaluate(chromosome) for chromosome in population])

        current_best_index = int(np.argmin(fitness))
        current_best = float(fitness[current_best_index])
        if current_best < best_fitness:
            best_fitness = current_best
            best_chromosome = population[current_best_index].copy()
        history.append(best_fitness)
        completed += 1

        if best_fitness < success_threshold:
            break

    return HistoricalTrainingResult(
        best_chromosome=best_chromosome,
        best_fitness=best_fitness,
        generations_completed=completed,
        success=best_fitness < success_threshold,
        initial_best_fitness=initial_best,
        best_fitness_history=tuple(history),
    )
