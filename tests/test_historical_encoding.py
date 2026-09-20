"""Tests for the historically evidenced GA encoding."""

import sys
from pathlib import Path

import pytest

VALIDATION = Path(__file__).resolve().parents[1] / "validation"
sys.path.insert(0, str(VALIDATION))

from historical_encoding import (
    bits_to_integer,
    decode_connectivity,
    decode_weight_c_observed,
    encode_connectivity,
    encode_scaled_weight,
    encode_weight_c_observed,
    integer_to_bits,
)


def test_report_discretisation_example() -> None:
    # The report prints 11111101; the 1998 C program stores it in a
    # fixed-width 10-bit chromosome chunk, hence the leading zero here.
    assert encode_scaled_weight(2.63) == "0100000111"
    assert bits_to_integer("0100000111") == 263


def test_fixed_width_integer_encoding() -> None:
    assert integer_to_bits(0, width=10) == "0000000000"
    assert integer_to_bits(1023, width=10) == "1111111111"


def test_integer_overflow_is_rejected() -> None:
    with pytest.raises(ValueError):
        integer_to_bits(1024, width=10)


def test_c_observed_positive_weight_round_trip() -> None:
    bits = encode_weight_c_observed(2.63, upper_range=4.5)
    assert bits == "0100000111"
    assert decode_weight_c_observed(bits, upper_range=4.5) == pytest.approx(2.63)


def test_c_observed_negative_weight_round_trip() -> None:
    bits = encode_weight_c_observed(-2.63, upper_range=4.5)
    assert bits == "1011001001"
    assert decode_weight_c_observed(bits, upper_range=4.5) == pytest.approx(-2.63)


def test_connectivity_is_separate_from_weights() -> None:
    connectivity = encode_connectivity([1, 0, 1, 1, 0])
    assert connectivity == "10110"
    assert decode_connectivity(connectivity) == (1, 0, 1, 1, 0)


def test_signed_encoder_rejects_out_of_range_weight() -> None:
    with pytest.raises(ValueError):
        encode_weight_c_observed(-4.6, upper_range=4.5)


def test_signed_encoder_detects_ten_bit_overflow() -> None:
    with pytest.raises(ValueError):
        encode_weight_c_observed(-5.8, upper_range=5.8)
