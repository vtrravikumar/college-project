"""Historical chromosome structure for the 1998 neural-network GA reconstruction.

This module defines the chromosome layout evidenced by the surviving Code-01
source and the report. It is a modern Python reconstruction, not historical
source code.

For the documented 2-2-2-1 network there are 10 possible links:
- 4 input -> hidden-1
- 4 hidden-1 -> hidden-2
- 2 hidden-2 -> output

Code-01 uses CHROMLEN=10 and CONCN=10. A 100-bit weight chromosome is therefore
ten 10-bit weight fields. Connectivity is stored separately as ten bits.

The exact historical link ordering is not independently recovered from the
available source. The ordering used here is a documented reconstruction:
weights/connectivity are grouped layer-by-layer, with source node order before
destination node order. It must remain explicit so it can be changed if a
clearer source scan is recovered.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from historical_encoding import (
    DEFAULT_WEIGHT_BITS,
    bits_to_integer,
    decode_connectivity,
    decode_weight_c_observed,
)


DEFAULT_CONNECTION_LAYOUT = (
    ("input", 0, "hidden1", 0),
    ("input", 0, "hidden1", 1),
    ("input", 1, "hidden1", 0),
    ("input", 1, "hidden1", 1),
    ("hidden1", 0, "hidden2", 0),
    ("hidden1", 0, "hidden2", 1),
    ("hidden1", 1, "hidden2", 0),
    ("hidden1", 1, "hidden2", 1),
    ("hidden2", 0, "output", 0),
    ("hidden2", 1, "output", 0),
)


@dataclass(frozen=True)
class HistoricalChromosome:
    """Separate historical-style weight and connectivity chromosomes."""

    weight_bits: str
    connectivity_bits: str

    def __post_init__(self) -> None:
        if len(self.weight_bits) != 10 * DEFAULT_WEIGHT_BITS:
            raise ValueError(
                "the documented 2-2-2-1 chromosome requires 100 weight bits"
            )
        if len(self.connectivity_bits) != len(DEFAULT_CONNECTION_LAYOUT):
            raise ValueError("connectivity must contain 10 link bits")
        if any(bit not in "01" for bit in self.weight_bits):
            raise ValueError("weight_bits must contain only '0' and '1'")
        if any(bit not in "01" for bit in self.connectivity_bits):
            raise ValueError("connectivity_bits must contain only '0' and '1'")

    @property
    def weight_chunks(self) -> tuple[str, ...]:
        """Return the ten fixed-width 10-bit weight fields."""
        return tuple(
            self.weight_bits[i : i + DEFAULT_WEIGHT_BITS]
            for i in range(0, len(self.weight_bits), DEFAULT_WEIGHT_BITS)
        )

    @property
    def encoded_weights(self) -> tuple[int, ...]:
        """Return the ten raw binary-decoded weight integers."""
        return tuple(bits_to_integer(chunk) for chunk in self.weight_chunks)

    @property
    def connectivity(self) -> tuple[int, ...]:
        """Return the ten separate link-presence bits."""
        return decode_connectivity(self.connectivity_bits)

    def decode_weights(
        self, *, upper_range: float, scale: int = 100
    ) -> tuple[float, ...]:
        """Decode all ten weights using the observed Code-01 decoder."""
        return tuple(
            decode_weight_c_observed(
                chunk, upper_range=upper_range, scale=scale
            )
            for chunk in self.weight_chunks
        )

    def active_weights(
        self, *, upper_range: float, scale: int = 100
    ) -> tuple[float, ...]:
        """Apply separate connectivity bits to decoded weights.

        A zero connectivity bit produces a zero effective link weight, matching
        the role of gbit[] in Code-01's finalweights().
        """
        decoded = self.decode_weights(upper_range=upper_range, scale=scale)
        return tuple(
            weight if connected else 0.0
            for weight, connected in zip(decoded, self.connectivity)
        )


def build_chromosome(
    weight_bits: str,
    connectivity_bits: str | Iterable[int],
) -> HistoricalChromosome:
    """Construct and validate the separate historical chromosome fields."""
    if isinstance(connectivity_bits, str):
        encoded_connectivity = connectivity_bits
    else:
        values = tuple(connectivity_bits)
        if any(bit not in (0, 1) for bit in values):
            raise ValueError("connectivity bits must contain only 0 or 1")
        encoded_connectivity = "".join(str(bit) for bit in values)

    return HistoricalChromosome(
        weight_bits=weight_bits,
        connectivity_bits=encoded_connectivity,
    )
