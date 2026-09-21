"""Tests for the historical feed-forward fitness reconstruction."""

from math import isclose
import sys
from pathlib import Path

import pytest

VALIDATION = Path(__file__).resolve().parents[1] / "validation"
sys.path.insert(0, str(VALIDATION))

from historical_chromosome import build_chromosome
from historical_fitness import forward, mean_squared_error


UPPER_RANGE = 5.8


def zero_chromosome():
    return build_chromosome("0" * 100, "1" * 10)


def test_zero_weights_produce_half_output():
    chromosome = zero_chromosome()

    prediction = forward(
        (1.0, 0.0),
        chromosome,
        upper_range=UPPER_RANGE,
    )

    assert prediction == pytest.approx((0.5,))


def test_zero_weights_have_xor_mse_quarter():
    chromosome = zero_chromosome()

    inputs = (
        (0.0, 0.0),
        (0.0, 1.0),
        (1.0, 0.0),
        (1.0, 1.0),
    )
    targets = (
        (0.0,),
        (1.0,),
        (1.0,),
        (0.0,),
    )

    error = mean_squared_error(
        inputs,
        targets,
        chromosome,
        upper_range=UPPER_RANGE,
    )

    assert isclose(error, 0.25)


def test_disconnected_links_are_zeroed_before_forward_pass():
    # A valid encoded weight of 1.00 is followed by nine zero weights.
    # Disconnecting that first link must make the network behave exactly like
    # the all-zero network.
    first_weight = "0001100100"  # 100 decimal -> 1.00
    weight_bits = first_weight + ("0" * 90)

    connected = build_chromosome(weight_bits, "1" + "0" * 9)
    disconnected = build_chromosome(weight_bits, "0" * 10)

    connected_prediction = forward(
        (1.0, 0.0),
        connected,
        upper_range=UPPER_RANGE,
    )
    disconnected_prediction = forward(
        (1.0, 0.0),
        disconnected,
        upper_range=UPPER_RANGE,
    )

    assert connected_prediction != pytest.approx(disconnected_prediction)
    assert disconnected_prediction == pytest.approx((0.5,))


def test_input_pattern_must_have_two_values():
    chromosome = zero_chromosome()

    with pytest.raises(ValueError, match="exactly 2 inputs"):
        forward(
            (1.0,),
            chromosome,
            upper_range=UPPER_RANGE,
        )


def test_target_pattern_must_have_one_value():
    chromosome = zero_chromosome()

    with pytest.raises(ValueError, match="one target output"):
        mean_squared_error(
            ((0.0, 0.0),),
            ((0.0, 0.0),),
            chromosome,
            upper_range=UPPER_RANGE,
        )


def test_empty_training_set_is_rejected():
    chromosome = zero_chromosome()

    with pytest.raises(ValueError, match="at least one"):
        mean_squared_error(
            (),
            (),
            chromosome,
            upper_range=UPPER_RANGE,
        )
