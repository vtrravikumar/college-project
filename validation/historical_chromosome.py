"""Historical-style chromosome reconstruction for the 1998 neural-network GA.

Modern Python reimplementation, not historical Python.  The default remains
the recovered 2-2-2-1 case (10 links, 100 weight bits).  The representation is
now parameterised so other reported networks can be tested without changing
the historical defaults.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Sequence
from historical_encoding import DEFAULT_WEIGHT_BITS, bits_to_integer, decode_connectivity, decode_weight_c_observed

def connection_layout(layer_sizes: Sequence[int]) -> tuple[tuple[str,int,str,int], ...]:
    if len(layer_sizes) != 4:
        raise ValueError("layer_sizes must contain input, hidden1, hidden2, output")
    names = ("input", "hidden1", "hidden2", "output")
    links=[]
    for layer in range(3):
        for src in range(layer_sizes[layer]):
            for dst in range(layer_sizes[layer+1]):
                links.append((names[layer], src, names[layer+1], dst))
    return tuple(links)

DEFAULT_CONNECTION_LAYOUT = connection_layout((2,2,2,1))

@dataclass(frozen=True)
class HistoricalChromosome:
    weight_bits: str
    connectivity_bits: str
    link_count: int = len(DEFAULT_CONNECTION_LAYOUT)

    def __post_init__(self):
        expected=self.link_count*DEFAULT_WEIGHT_BITS
        if len(self.weight_bits) != expected:
            raise ValueError(f"weight_bits must contain exactly {expected} bits")
        if len(self.connectivity_bits) != self.link_count:
            raise ValueError(f"connectivity must contain exactly {self.link_count} link bits")
        if any(b not in "01" for b in self.weight_bits+self.connectivity_bits):
            raise ValueError("chromosome fields must contain only '0' and '1'")

    @property
    def weight_chunks(self):
        return tuple(self.weight_bits[i:i+DEFAULT_WEIGHT_BITS] for i in range(0,len(self.weight_bits),DEFAULT_WEIGHT_BITS))

    @property
    def encoded_weights(self):
        return tuple(bits_to_integer(c) for c in self.weight_chunks)

    @property
    def connectivity(self):
        return decode_connectivity(self.connectivity_bits)

    def decode_weights(self, *, upper_range: float, scale: int = 100):
        return tuple(decode_weight_c_observed(c, upper_range=upper_range, scale=scale) for c in self.weight_chunks)

    def active_weights(self, *, upper_range: float, scale: int = 100):
        return tuple(w if connected else 0.0 for w, connected in zip(self.decode_weights(upper_range=upper_range, scale=scale), self.connectivity))

def build_chromosome(weight_bits: str, connectivity_bits: str | Iterable[int], *, link_count: int | None = None) -> HistoricalChromosome:
    if isinstance(connectivity_bits, str):
        encoded=connectivity_bits
    else:
        values=tuple(connectivity_bits)
        if any(v not in (0,1) for v in values):
            raise ValueError("connectivity bits must contain only 0 or 1")
        encoded="".join(str(v) for v in values)
    count=len(encoded) if link_count is None else link_count
    return HistoricalChromosome(weight_bits, encoded, count)
