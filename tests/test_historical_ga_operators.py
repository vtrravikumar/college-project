"""Tests for the historical binary GA operators."""

import sys
from pathlib import Path

import numpy as np
import pytest

VALIDATION = Path(__file__).resolve().parents[1] / "validation"
sys.path.insert(0, str(VALIDATION))

from historical_ga_operators import (
    crossover_and_mutate,
    mutate_bits,
    random_binary_population,
    roulette_select_index,
)


def test_binary_population_has_requested_shape_and_values():
    population = random_binary_population(
        np.random.default_rng(42), population_size=7, chromosome_length=100
    )
    assert population.shape == (7, 100)
    assert set(np.unique(population)) <= {0, 1}


def test_mutation_probability_zero_preserves_chromosome():
    chromosome = np.array([0, 1, 0, 1], dtype=np.uint8)
    result = mutate_bits(np.random.default_rng(42), chromosome, 0.0)
    np.testing.assert_array_equal(result, chromosome)


def test_mutation_probability_one_flips_every_gene():
    chromosome = np.array([0, 1, 0, 1], dtype=np.uint8)
    result = mutate_bits(np.random.default_rng(42), chromosome, 1.0)
    np.testing.assert_array_equal(result, [1, 0, 1, 0])


def test_crossover_without_mutation_preserves_parent_genes():
    parent1 = np.array([0, 0, 0, 0], dtype=np.uint8)
    parent2 = np.array([1, 1, 1, 1], dtype=np.uint8)

    child1, child2, site, did = crossover_and_mutate(
        np.random.default_rng(42),
        parent1,
        parent2,
        crossover_probability=1.0,
        mutation_probability=0.0,
    )

    assert did is True
    assert 0 <= site < 4
    assert set(child1) <= {0, 1}
    assert set(child2) <= {0, 1}


def test_crossover_probability_zero_uses_last_site():
    parent1 = np.array([0, 0, 0, 0], dtype=np.uint8)
    parent2 = np.array([1, 1, 1, 1], dtype=np.uint8)

    child1, child2, site, did = crossover_and_mutate(
        np.random.default_rng(42),
        parent1,
        parent2,
        crossover_probability=0.0,
        mutation_probability=0.0,
    )

    assert did is False
    assert site == 3
    np.testing.assert_array_equal(child1, [0, 0, 0, 1])
    np.testing.assert_array_equal(child2, [1, 1, 1, 0])


def test_roulette_selection_matches_raw_historical_fitness():
    rng = np.random.default_rng(42)
    fitness = np.array([0.01, 1.0, 1.0])
    selections = [roulette_select_index(rng, fitness) for _ in range(1000)]
    assert selections.count(0) < selections.count(1)
    assert selections.count(0) < selections.count(2)


def test_invalid_mutation_probability_is_rejected():
    with pytest.raises(ValueError):
        mutate_bits(np.random.default_rng(42), np.array([0, 1]), 1.1)
