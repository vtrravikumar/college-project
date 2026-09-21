"""Tests for the end-to-end historical-style GA training loop."""

import sys
from pathlib import Path

import numpy as np
import pytest

VALIDATION = Path(__file__).resolve().parents[1] / "validation"
sys.path.insert(0, str(VALIDATION))

from historical_ga_training import train_historical_ga


XOR_INPUTS = (
    (0.0, 0.0),
    (0.0, 1.0),
    (1.0, 0.0),
    (1.0, 1.0),
)
XOR_TARGETS = ((0.0,), (1.0,), (1.0,), (0.0,))


def test_training_is_reproducible_for_a_fixed_seed():
    kwargs = dict(
        inputs=XOR_INPUTS,
        targets=XOR_TARGETS,
        population_size=6,
        generations=2,
        crossover_probability=0.4,
        mutation_probability=0.01,
        upper_range=5.8,
    )

    first = train_historical_ga(np.random.default_rng(123), **kwargs)
    second = train_historical_ga(np.random.default_rng(123), **kwargs)

    np.testing.assert_array_equal(first.best_chromosome, second.best_chromosome)
    assert first.best_fitness == pytest.approx(second.best_fitness)
    assert first.best_fitness_history == second.best_fitness_history


def test_training_returns_a_valid_100_bit_best_chromosome():
    result = train_historical_ga(
        np.random.default_rng(7),
        XOR_INPUTS,
        XOR_TARGETS,
        population_size=5,
        generations=1,
        crossover_probability=0.4,
        mutation_probability=0.01,
        upper_range=5.8,
    )

    assert result.best_chromosome.shape == (100,)
    assert set(np.unique(result.best_chromosome)) <= {0, 1}
    assert result.generations_completed == 1
    assert result.best_fitness >= 0.0


def test_training_rejects_invalid_connectivity():
    with pytest.raises(ValueError, match="exactly 10"):
        train_historical_ga(
            np.random.default_rng(1),
            XOR_INPUTS,
            XOR_TARGETS,
            population_size=5,
            generations=1,
            crossover_probability=0.4,
            mutation_probability=0.01,
            upper_range=5.8,
            connectivity_bits="101",
        )
