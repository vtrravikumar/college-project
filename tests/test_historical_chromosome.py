"""Tests for the historical chromosome structure."""

import sys
from pathlib import Path

import pytest

VALIDATION = Path(__file__).resolve().parents[1] / "validation"
sys.path.insert(0, str(VALIDATION))

from historical_chromosome import DEFAULT_CONNECTION_LAYOUT, build_chromosome


def test_documented_2_2_2_1_layout_has_ten_links():
    assert len(DEFAULT_CONNECTION_LAYOUT) == 10
    assert DEFAULT_CONNECTION_LAYOUT[:4] == (
        ("input", 0, "hidden1", 0),
        ("input", 0, "hidden1", 1),
        ("input", 1, "hidden1", 0),
        ("input", 1, "hidden1", 1),
    )
    assert DEFAULT_CONNECTION_LAYOUT[4:8] == (
        ("hidden1", 0, "hidden2", 0),
        ("hidden1", 0, "hidden2", 1),
        ("hidden1", 1, "hidden2", 0),
        ("hidden1", 1, "hidden2", 1),
    )
    assert DEFAULT_CONNECTION_LAYOUT[8:] == (
        ("hidden2", 0, "output", 0),
        ("hidden2", 1, "output", 0),
    )


def test_100_bit_weight_chromosome_splits_into_ten_10_bit_fields():
    chromosome = build_chromosome(
        "0000000001" * 10,
        "1010101010",
    )

    assert len(chromosome.weight_chunks) == 10
    assert chromosome.weight_chunks == ("0000000001",) * 10
    assert chromosome.encoded_weights == (1,) * 10


def test_connectivity_is_separate_from_weight_chromosome():
    chromosome = build_chromosome(
        "0000000001" * 10,
        [1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    )

    assert len(chromosome.weight_bits) == 100
    assert chromosome.connectivity == (1, 0, 1, 1, 0, 0, 1, 0, 1, 0)


def test_zero_connectivity_zeroes_effective_weight():
    # 100 -> 1.00 with the observed C decoder.
    chromosome = build_chromosome(
        "0001100100" * 10,
        "1010101010",
    )

    effective = chromosome.active_weights(upper_range=4.5)

    assert effective == (1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0)


def test_invalid_weight_chromosome_length_is_rejected():
    with pytest.raises(ValueError):
        build_chromosome("0" * 90, "1010101010")


def test_invalid_connectivity_length_is_rejected():
    with pytest.raises(ValueError):
        build_chromosome("0" * 100, "10101")
