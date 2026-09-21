"""Historical GA generation-step reconstruction.

This is a modern Python reimplementation of the generation() behaviour
evidenced by Code-01.pdf. It is not a translation of the original C.

The surviving listing shows:
- two parents selected from oldpop;
- two offspring produced by crossover + mutation;
- both offspring evaluated;
- the offspring with lower fitness/error is retained;
- the retained offspring replaces oldpop[store];
- newpop is then copied from oldpop.

The statistics() listing strongly indicates that store is the index of the
maximum-fitness (worst-error) member. The OCR around that assignment is
damaged, so the index interpretation is documented as an evidence-based
reconstruction rather than claimed as a byte-for-byte recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from historical_ga_operators import (
    crossover_and_mutate,
    roulette_select_index,
)


@dataclass(frozen=True)
class HistoricalGenerationResult:
    """Result of one reconstructed historical generation."""

    old_population: np.ndarray
    new_population: np.ndarray
    parent_indices: tuple[int, int]
    survivor_index: int
    survivor_fitness: float
    crossover_site: int
    did_crossover: bool


def worst_fitness_index(fitness: np.ndarray) -> int:
    """Return the index of the maximum raw fitness value."""
    values = np.asarray(fitness, dtype=float)
    if values.ndim != 1 or len(values) == 0:
        raise ValueError("fitness must be a non-empty one-dimensional array")
    if not np.all(np.isfinite(values)):
        raise ValueError("fitness must contain finite values")
    return int(np.argmax(values))


def generate_one_step(
    rng: np.random.Generator,
    old_population: np.ndarray,
    fitness: np.ndarray,
    *,
    crossover_probability: float,
    mutation_probability: float,
    evaluate: Callable[[np.ndarray], float],
) -> HistoricalGenerationResult:
    """Reconstruct one historical generation step."""
    population = np.asarray(old_population, dtype=np.uint8)
    values = np.asarray(fitness, dtype=float)

    if population.ndim != 2 or population.shape[0] < 2 or population.shape[1] == 0:
        raise ValueError("old_population must contain at least two non-empty chromosomes")
    if np.any((population != 0) & (population != 1)):
        raise ValueError("old_population must be binary")
    if values.shape != (population.shape[0],):
        raise ValueError("fitness must match population size")
    if not np.all(np.isfinite(values)) or np.any(values < 0):
        raise ValueError("fitness must contain finite non-negative values")

    mate1 = roulette_select_index(rng, values)
    mate2 = roulette_select_index(rng, values)

    child1, child2, site, did_crossover = crossover_and_mutate(
        rng,
        population[mate1],
        population[mate2],
        crossover_probability,
        mutation_probability,
    )

    fitness1 = float(evaluate(child1))
    fitness2 = float(evaluate(child2))

    if not np.isfinite(fitness1) or not np.isfinite(fitness2):
        raise ValueError("child fitness must be finite")

    if fitness1 < fitness2:
        survivor = child1
        survivor_fitness = fitness1
    else:
        survivor = child2
        survivor_fitness = fitness2

    store = worst_fitness_index(values)
    updated_old = population.copy()
    updated_old[store] = survivor
    updated_new = updated_old.copy()

    return HistoricalGenerationResult(
        old_population=updated_old,
        new_population=updated_new,
        parent_indices=(mate1, mate2),
        survivor_index=store,
        survivor_fitness=survivor_fitness,
        crossover_site=site,
        did_crossover=did_crossover,
    )
