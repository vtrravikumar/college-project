"""Historical binary encoding used by the 1998 neural-network GA reconstruction.

This module is a documentary Python reimplementation of the encoding evidence
available from the report and surviving Code-01 source.

It is intentionally separate from the modern GA implementation. It does not
claim to be the original 1998 Python (none existed).

Evidence captured here:
- the report describes discretisation by scaling real weights by a power of
  ten and converting the resulting integer to binary;
- the report gives 2.63 -> 263 -> 11111101 as an explicit example;
- the surviving C decoder uses fixed-width binary chunks and divides the
  decoded integer by 100;
- the surviving C decoder maps values above the upper range back through
  upper_range - value;
- connectivity is represented separately as one bit per possible link.

The original C encode() body and value.dat are unavailable. Therefore the
C-observed encoder below is deliberately documented as an inference from the
surviving decoder, not as a verified transcription of encode().
"""

from __future__ import annotations

from typing import Iterable


DEFAULT_WEIGHT_BITS = 10
DEFAULT_SCALE = 100


def integer_to_bits(value: int, *, width: int) -> str:
    """Return a non-negative integer as a fixed-width MSB-first bit string."""
    if width <= 0:
        raise ValueError("width must be positive")
    if value < 0:
        raise ValueError("value must be non-negative")
    if value >= (1 << width):
        raise ValueError(
            f"value {value} does not fit in {width} bits "
            f"(maximum {(1 << width) - 1})"
        )
    return format(value, f"0{width}b")


def bits_to_integer(bits: str | Iterable[int]) -> int:
    """Decode an MSB-first binary string using the C decoder's convention."""
    if isinstance(bits, str):
        if not bits:
            raise ValueError("bits must not be empty")
        if any(bit not in "01" for bit in bits):
            raise ValueError("bits must contain only '0' and '1'")
        return int(bits, 2)

    values = list(bits)
    if not values:
        raise ValueError("bits must not be empty")
    if any(bit not in (0, 1) for bit in values):
        raise ValueError("bits must contain only 0 or 1")
    return sum(bit << (len(values) - 1 - i) for i, bit in enumerate(values))


def encode_scaled_weight(
    weight: float,
    *,
    bits: int = DEFAULT_WEIGHT_BITS,
    scale: int = DEFAULT_SCALE,
) -> str:
    """Encode the report's explicit positive-weight discretisation example.

    This operation performs only the documented discretisation step:
    real weight -> scaled integer -> fixed-width binary.

    It intentionally does not apply a signed/excess transformation. The
    report's published example is 2.63 -> 263 -> 11111101.
    """
    if scale <= 0:
        raise ValueError("scale must be positive")
    scaled = round(weight * scale)
    if scaled < 0:
        raise ValueError(
            "encode_scaled_weight only represents the non-negative "
            "discretisation step; signed mapping remains historically unresolved"
        )
    return integer_to_bits(scaled, width=bits)


def decode_weight_c_observed(
    bits: str | Iterable[int],
    *,
    upper_range: float,
    scale: int = DEFAULT_SCALE,
) -> float:
    """Decode a weight using the surviving C source's observed rule.

    Code-01 performs:
        decoded = binary_integer / 100.0
        if decoded > urange:
            decoded = urange - decoded

    This function reproduces that rule without claiming that the missing
    original encode() implementation has been recovered.
    """
    if upper_range <= 0:
        raise ValueError("upper_range must be positive")
    if scale <= 0:
        raise ValueError("scale must be positive")

    value = bits_to_integer(bits) / scale
    if value > upper_range:
        value = upper_range - value
    return value


def encode_weight_c_observed(
    weight: float,
    *,
    upper_range: float,
    bits: int = DEFAULT_WEIGHT_BITS,
    scale: int = DEFAULT_SCALE,
) -> str:
    """Infer an encoder compatible with the surviving C decoder.

    For non-negative weights the encoded value is weight * scale.
    For negative weights, the inverse of upper_range - decoded is used:
    encoded_value = (upper_range - weight) * scale

    This is explicitly an inferred reconstruction. The original C
    encode() implementation is missing, so this function must not be
    described as a verified transcription.
    """
    if upper_range <= 0:
        raise ValueError("upper_range must be positive")
    if scale <= 0:
        raise ValueError("scale must be positive")
    if not -upper_range <= weight <= upper_range:
        raise ValueError(
            f"weight {weight} is outside the historical range "
            f"[-{upper_range}, {upper_range}]"
        )

    if weight >= 0:
        encoded = round(weight * scale)
    else:
        encoded = round((upper_range - weight) * scale)

    return integer_to_bits(encoded, width=bits)


def encode_connectivity(bits: Iterable[int]) -> str:
    """Encode link presence/absence as the separate connectivity string."""
    values = list(bits)
    if not values:
        raise ValueError("connectivity must not be empty")
    if any(bit not in (0, 1) for bit in values):
        raise ValueError("connectivity bits must contain only 0 or 1")
    return "".join(str(bit) for bit in values)


def decode_connectivity(bits: str | Iterable[int]) -> tuple[int, ...]:
    """Decode the separate connectivity string."""
    if isinstance(bits, str):
        if not bits:
            raise ValueError("connectivity must not be empty")
        if any(bit not in "01" for bit in bits):
            raise ValueError("connectivity must contain only '0' and '1'")
        return tuple(int(bit) for bit in bits)

    values = tuple(bits)
    if not values:
        raise ValueError("connectivity must not be empty")
    if any(bit not in (0, 1) for bit in values):
        raise ValueError("connectivity bits must contain only 0 or 1")
    return values
