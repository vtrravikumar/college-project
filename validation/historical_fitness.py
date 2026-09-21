"""Historical feed-forward fitness reconstruction for the 1998 GA.

This is a modern Python reimplementation of the behaviour evidenced by
Code-01 and the report. It is not a transcription of historical Python.

The surviving Code-01 forward() routine shows a 2-2-2-1 sigmoid network with
no bias terms. The ten links are ordered layer-by-layer, matching the
documented reconstruction in historical_chromosome.py:

    4 input -> hidden1
    4 hidden1 -> hidden2
    2 hidden2 -> output

The report describes GA fitness for weight optimisation as the error obtained
by feed-forwarding the training patterns, with the surviving C source dividing
the accumulated squared error by NODE3 * NCLS. For the documented 2-2-2-1
case this is the mean squared error over the four patterns and one output.

This module deliberately does not implement GA survivor/replacement logic;
that part of generation() remains uncertain in the OCR-derived source.
"""

from __future__ import annotations

from math import exp
from typing import Iterable, Sequence

from historical_chromosome import HistoricalChromosome


INPUT_NODES = 2
HIDDEN1_NODES = 2
HIDDEN2_NODES = 2
OUTPUT_NODES = 1
PATTERN_COUNT = 4


def sigmoid(value: float) -> float:
    """Return the sigmoid used by the historical forward propagation."""
    # The historical C expression is 1/(1+exp(-net)).
    return 1.0 / (1.0 + exp(-value))


def active_weight_matrices(
    chromosome: HistoricalChromosome,
    *,
    upper_range: float,
    scale: int = 100,
) -> tuple[list[list[float]], list[list[float]], list[list[float]]]:
    """Map the ten effective chromosome weights to the three network layers."""
    weights = chromosome.active_weights(
        upper_range=upper_range,
        scale=scale,
    )

    hidden1 = [
        [weights[0], weights[1]],
        [weights[2], weights[3]],
    ]
    hidden2 = [
        [weights[4], weights[5]],
        [weights[6], weights[7]],
    ]
    output = [[weights[8]], [weights[9]]]

    return hidden1, hidden2, output


def forward(
    inputs: Sequence[float],
    chromosome: HistoricalChromosome,
    *,
    upper_range: float,
    scale: int = 100,
) -> tuple[float, ...]:
    """Run one pattern through the historical 2-2-2-1 network.

    No bias terms are used because the surviving Code-01 forward() source
    accumulates only weight * activation products.
    """
    if len(inputs) != INPUT_NODES:
        raise ValueError("the historical network requires exactly 2 inputs")

    hidden1, hidden2, output = active_weight_matrices(
        chromosome,
        upper_range=upper_range,
        scale=scale,
    )

    layer1 = [
        sigmoid(sum(float(inputs[j]) * hidden1[j][i] for j in range(INPUT_NODES)))
        for i in range(HIDDEN1_NODES)
    ]
    layer2 = [
        sigmoid(
            sum(layer1[j] * hidden2[j][i] for j in range(HIDDEN1_NODES))
        )
        for i in range(HIDDEN2_NODES)
    ]
    result = [
        sigmoid(
            sum(layer2[j] * output[j][i] for j in range(HIDDEN2_NODES))
        )
        for i in range(OUTPUT_NODES)
    ]
    return tuple(result)


def mean_squared_error(
    inputs: Iterable[Sequence[float]],
    targets: Iterable[Sequence[float]],
    chromosome: HistoricalChromosome,
    *,
    upper_range: float,
    scale: int = 100,
) -> float:
    """Evaluate the chromosome using historical-style feed-forward MSE."""
    input_rows = tuple(inputs)
    target_rows = tuple(targets)

    if len(input_rows) != len(target_rows):
        raise ValueError("inputs and targets must contain the same number of rows")
    if not input_rows:
        raise ValueError("at least one training pattern is required")

    squared_error = 0.0
    output_count = 0

    for pattern, target in zip(input_rows, target_rows):
        prediction = forward(
            pattern,
            chromosome,
            upper_range=upper_range,
            scale=scale,
        )
        if len(target) != OUTPUT_NODES:
            raise ValueError("the historical network requires one target output")
        squared_error += sum(
            (prediction[i] - float(target[i])) ** 2
            for i in range(OUTPUT_NODES)
        )
        output_count += OUTPUT_NODES

    return squared_error / output_count
