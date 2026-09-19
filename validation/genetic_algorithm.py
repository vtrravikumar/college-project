"""Genetic algorithm weight optimiser."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from neural_network import NeuralNetwork


@dataclass(frozen=True)
class GAConfig:
    population_size: int = 80
    generations: int = 300
    crossover_probability: float = 0.8
    mutation_probability: float = 0.02
    weight_min: float = -1.0
    weight_max: float = 1.0


def encode_weights(
    weights: np.ndarray,
    *,
    minimum: float,
    maximum: float,
    bits: int,
) -> np.ndarray:
    """Encode real-valued weights as fixed-width binary strings."""
    if bits < 2:
        raise ValueError("bits must be at least 2")
    if minimum >= maximum:
        raise ValueError("minimum must be less than maximum")

    values = np.clip(np.asarray(weights), minimum, maximum)
    levels = (1 << bits) - 1
    integers = np.rint((values - minimum) / (maximum - minimum) * levels).astype(int)
    return ((integers[:, None] >> np.arange(bits - 1, -1, -1)) & 1).astype(np.uint8)


def decode_weights(
    bits: np.ndarray,
    *,
    minimum: float,
    maximum: float,
) -> np.ndarray:
    """Decode fixed-width binary strings back to real-valued weights."""
    bits = np.asarray(bits, dtype=np.uint8)
    if bits.ndim != 2:
        raise ValueError("bits must be a two-dimensional array")
    width = bits.shape[1]
    levels = (1 << width) - 1
    integers = bits @ (1 << np.arange(width - 1, -1, -1))
    return minimum + (integers / levels) * (maximum - minimum)


def _initial_population(
    rng: np.random.Generator,
    population_size: int,
    parameter_count: int,
    minimum: float,
    maximum: float,
) -> np.ndarray:
    return rng.uniform(
        minimum, maximum, size=(population_size, parameter_count)
    )


def _select(
    rng: np.random.Generator,
    population: np.ndarray,
    losses: np.ndarray,
) -> np.ndarray:
    # Tournament selection: lower MSE is fitter.
    selected = np.empty_like(population)
    for i in range(len(population)):
        a, b = rng.integers(0, len(population), size=2)
        selected[i] = population[a] if losses[a] <= losses[b] else population[b]
    return selected


def _crossover(
    rng: np.random.Generator,
    parents: np.ndarray,
    probability: float,
) -> np.ndarray:
    children = parents.copy()
    for i in range(0, len(children) - 1, 2):
        if rng.random() < probability:
            point = int(rng.integers(1, children.shape[1]))
            left = children[i, point:].copy()
            children[i, point:] = children[i + 1, point:]
            children[i + 1, point:] = left
    return children


def _mutate(
    rng: np.random.Generator,
    population: np.ndarray,
    probability: float,
    minimum: float,
    maximum: float,
) -> None:
    mask = rng.random(population.shape) < probability
    population += mask * rng.normal(0.0, 0.15, size=population.shape)
    np.clip(population, minimum, maximum, out=population)


def train_genetic(
    network: NeuralNetwork,
    inputs: np.ndarray,
    targets: np.ndarray,
    *,
    config: GAConfig = GAConfig(),
    rng: np.random.Generator,
) -> dict:
    """Optimise the network's weights with a real-valued GA.

    The 1998 report describes binary encoding, so Phase 1 keeps the encoder
    available as a separately testable component while using real-valued
    chromosomes for a stable baseline. Binary chromosome evolution will be
    introduced once the original code's encoding convention is verified.
    """
    parameter_count = len(network.parameter_vector())
    population = _initial_population(
        rng,
        config.population_size,
        parameter_count,
        config.weight_min,
        config.weight_max,
    )

    best_loss = float("inf")
    best_vector = None
    history: list[float] = []

    for generation in range(1, config.generations + 1):
        losses = np.empty(len(population))
        for i, vector in enumerate(population):
            network.set_parameter_vector(vector)
            losses[i] = network.mse(inputs, targets)

        best_index = int(np.argmin(losses))
        if losses[best_index] < best_loss:
            best_loss = float(losses[best_index])
            best_vector = population[best_index].copy()

        history.append(best_loss)

        if best_loss <= 1e-4:
            break

        parents = _select(rng, population, losses)
        children = _crossover(rng, parents, config.crossover_probability)
        _mutate(
            rng,
            children,
            config.mutation_probability,
            config.weight_min,
            config.weight_max,
        )

        # Elitism preserves the best solution found so far.
        children[0] = best_vector
        population = children

    network.set_parameter_vector(best_vector)
    return {
        "generations": generation,
        "final_mse": best_loss,
        "history": history,
        "best_weights": best_vector.tolist(),
    }
