"""Binary GA operators reconstructed from the surviving 1998 Code-01 listing.

This is a modern Python implementation of the documented/source-evidenced
operators. It is not a translation of the original C program.

Source evidence:
- selection is described as roulette-wheel selection;
- crossover chooses a site with garand(0, lchrom-1);
- mutation flips a gene when flip(pmutation) succeeds;
- flip(probability) uses a uniform random draw against the supplied
  probability.

The historical source has OCR damage in the population-replacement portion of
generation(). That replacement logic is therefore intentionally not included
here yet.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class BinaryIndividual:
    """A binary chromosome with an associated fitness value."""

    chromosome: np.ndarray
    fitness: float


def random_binary_chromosome(
    rng: np.random.Generator, length: int
) -> np.ndarray:
    """Create one binary chromosome of the requested length."""
    if length <= 0:
        raise ValueError("length must be positive")
    return rng.integers(0, 2, size=length, dtype=np.uint8)


def random_binary_population(
    rng: np.random.Generator, population_size: int, chromosome_length: int
) -> np.ndarray:
    """Create a binary population."""
    if population_size <= 0:
        raise ValueError("population_size must be positive")
    return np.vstack(
        [
            random_binary_chromosome(rng, chromosome_length)
            for _ in range(population_size)
        ]
    )


def roulette_select_index(
    rng: np.random.Generator,
    fitness: np.ndarray,
) -> int:
    """Select an individual by roulette wheel.

    The surviving Code-01 selection routine accumulates the raw fitness
    values and selects against that cumulative total. Because objectfn()
    returns an error value, this creates a source-level inconsistency with
    the report's statement that lower error is fitter. We preserve the
    surviving routine here rather than silently correcting it.

    A zero total cannot define a roulette wheel and is rejected.
    """
    values = np.asarray(fitness, dtype=float)
    if values.ndim != 1 or len(values) == 0:
        raise ValueError("fitness must be a non-empty one-dimensional array")
    if not np.all(np.isfinite(values)) or np.any(values < 0):
        raise ValueError("fitness must contain finite non-negative values")

    total = values.sum()
    if total <= 0:
        raise ValueError("fitness total must be positive")

    probabilities = values / total
    return int(rng.choice(len(values), p=probabilities))


def mutate_bits(
    rng: np.random.Generator,
    chromosome: np.ndarray,
    probability: float,
) -> np.ndarray:
    """Flip each gene independently with the supplied mutation probability."""
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must be between 0 and 1")

    result = np.asarray(chromosome, dtype=np.uint8).copy()
    if result.ndim != 1 or np.any((result != 0) & (result != 1)):
        raise ValueError("chromosome must be a one-dimensional binary array")

    mask = rng.random(result.shape) < probability
    result[mask] = 1 - result[mask]
    return result


def crossover_and_mutate(
    rng: np.random.Generator,
    parent1: np.ndarray,
    parent2: np.ndarray,
    crossover_probability: float,
    mutation_probability: float,
) -> tuple[np.ndarray, np.ndarray, int, bool]:
    """Apply one-point crossover followed by per-gene mutation.

    The surviving C listing chooses a crossover site in [0, lchrom-1].
    When crossover does not occur it uses lchrom-1 as the site. We preserve
    that observable convention while treating the selected site as the
    boundary between the two parent segments.
    """
    if not 0.0 <= crossover_probability <= 1.0:
        raise ValueError("crossover_probability must be between 0 and 1")

    a = np.asarray(parent1, dtype=np.uint8)
    b = np.asarray(parent2, dtype=np.uint8)
    if a.ndim != 1 or b.ndim != 1 or len(a) != len(b) or len(a) == 0:
        raise ValueError("parents must be non-empty one-dimensional arrays of equal length")
    if np.any((a != 0) & (a != 1)) or np.any((b != 0) & (b != 1)):
        raise ValueError("parents must be binary")

    did_crossover = bool(rng.random() < crossover_probability)
    site = int(rng.integers(0, len(a))) if did_crossover else len(a) - 1

    child1 = np.concatenate((a[:site], b[site:]))
    child2 = np.concatenate((b[:site], a[site:]))

    child1 = mutate_bits(rng, child1, mutation_probability)
    child2 = mutate_bits(rng, child2, mutation_probability)

    return child1, child2, site, did_crossover
