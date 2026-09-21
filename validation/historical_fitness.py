"""Historical feed-forward fitness reconstruction.

Modern Python reimplementation of the feed-forward/MSE behaviour evidenced by
the surviving C source.  Defaults preserve the recovered 2-2-2-1 network.
"""
from __future__ import annotations
from math import exp
from typing import Iterable, Sequence
from historical_chromosome import HistoricalChromosome, connection_layout

DEFAULT_LAYER_SIZES=(2,2,2,1)

def sigmoid(value: float) -> float:
    return 1.0/(1.0+exp(-value))

def active_weight_matrices(chromosome: HistoricalChromosome, *, layer_sizes: Sequence[int]=DEFAULT_LAYER_SIZES, upper_range: float, scale: int=100):
    expected_links=sum(layer_sizes[i]*layer_sizes[i+1] for i in range(3))
    if chromosome.link_count != expected_links:
        raise ValueError("chromosome link count does not match layer_sizes")
    weights=chromosome.active_weights(upper_range=upper_range, scale=scale)
    matrices=[]; offset=0
    for i in range(3):
        rows,cols=layer_sizes[i],layer_sizes[i+1]
        matrices.append([list(weights[offset+r*cols:offset+(r+1)*cols]) for r in range(rows)])
        offset += rows*cols
    return tuple(matrices)

def forward(inputs: Sequence[float], chromosome: HistoricalChromosome, *, layer_sizes: Sequence[int]=DEFAULT_LAYER_SIZES, upper_range: float, scale: int=100):
    if len(layer_sizes)!=4:
        raise ValueError("layer_sizes must contain input, hidden1, hidden2, output")
    if len(inputs)!=layer_sizes[0]:
        raise ValueError(f"network requires exactly {layer_sizes[0]} inputs")
    matrices=active_weight_matrices(chromosome, layer_sizes=layer_sizes, upper_range=upper_range, scale=scale)
    activation=[float(x) for x in inputs]
    for matrix in matrices:
        cols=len(matrix[0])
        activation=[sigmoid(sum(activation[r]*matrix[r][c] for r in range(len(matrix)))) for c in range(cols)]
    return tuple(activation)

def mean_squared_error(inputs: Iterable[Sequence[float]], targets: Iterable[Sequence[float]], chromosome: HistoricalChromosome, *, layer_sizes: Sequence[int]=DEFAULT_LAYER_SIZES, upper_range: float, scale: int=100):
    rows=tuple(inputs); expected=tuple(targets)
    if len(rows)!=len(expected): raise ValueError("inputs and targets must contain the same number of rows")
    if not rows: raise ValueError("at least one training pattern is required")
    output_count=layer_sizes[-1]; error=0.0
    for pattern,target in zip(rows,expected):
        prediction=forward(pattern, chromosome, layer_sizes=layer_sizes, upper_range=upper_range, scale=scale)
        if len(target)!=output_count: raise ValueError("network requires one target output" if output_count == 1 else f"network requires {output_count} target outputs")
        error += sum((prediction[i]-float(target[i]))**2 for i in range(output_count))
    return error/(len(rows)*output_count)
