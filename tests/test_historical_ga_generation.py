"""Tests for the historical GA generation reconstruction."""

import sys
from pathlib import Path

import numpy as np

VALIDATION = Path(__file__).resolve().parents[1] / "validation"
sys.path.insert(0, str(VALIDATION))

from historical_ga_generation import generate_one_step, worst_fitness_index


def test_worst_fitness_index_identifies_maximum_error():
    fitness = np.array([0.20, 0.03, 0.80, 0.10])
    assert worst_fitness_index(fitness) == 2


def test_generation_replaces_worst_member_with_fitter_child():
    population = np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=np.uint8,
    )
    # The surviving selection routine uses raw fitness as roulette weights.
    # With seed 25 this fixture selects the first (zero) chromosome twice.
    # This deliberately preserves the source-level selection semantics rather
    # than assuming that lower error receives a higher roulette probability.
    fitness = np.array([0.20, 0.30, 0.50])

    def evaluate(chromosome):
        return float(np.sum(chromosome))

    # With crossover disabled, the historical operator uses the last
    # crossover site. Mutation is also disabled, so the selected parent
    # chromosomes are copied unchanged.
    result = generate_one_step(
        np.random.default_rng(25),
        population,
        fitness,
        crossover_probability=0.0,
        mutation_probability=0.0,
        evaluate=evaluate,
    )

    assert result.parent_indices == (0, 0)
    assert result.survivor_index == 2
    assert result.survivor_fitness == 0.0
    np.testing.assert_array_equal(result.old_population[2], [0, 0, 0, 0])
    np.testing.assert_array_equal(result.new_population, result.old_population)


def test_generation_selects_lower_error_child():
    population = np.array(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
        ],
        dtype=np.uint8,
    )
    fitness = np.array([0.10, 0.90])

    def evaluate(chromosome):
        # Prefer chromosomes with fewer one-bits.
        return float(np.sum(chromosome))

    result = generate_one_step(
        np.random.default_rng(7),
        population,
        fitness,
        crossover_probability=1.0,
        mutation_probability=0.0,
        evaluate=evaluate,
    )

    assert result.survivor_fitness <= 4.0
    assert result.survivor_index == 1


def test_generation_preserves_population_size_and_binary_values():
    population = np.array(
        [
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 1],
        ],
        dtype=np.uint8,
    )
    fitness = np.array([0.2, 0.4, 0.8])

    result = generate_one_step(
        np.random.default_rng(11),
        population,
        fitness,
        crossover_probability=0.5,
        mutation_probability=0.1,
        evaluate=lambda chromosome: float(np.sum(chromosome)),
    )

    assert result.old_population.shape == population.shape
    assert result.new_population.shape == population.shape
    assert set(np.unique(result.old_population)) <= {0, 1}
