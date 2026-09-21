"""Verify the reported 1998 robot inverse-kinematics solution.

The scanned source pages establish a 2-4-2 network, seven training patterns,
16 numbered links, a 128-bit chromosome, and the reported optimal weights.

This phase deliberately verifies the published solution rather than inventing
an encoding or attempting to reproduce the original GA random run. The source
does not preserve enough evidence to establish the historical 128-bit
encoding algorithm.

The report's prose says links 4, 8, 11 and 16 are zero, but the scanned
weight table and the 16-bit connectivity string show links 4, 8 and 16 as
zero while link 11 has weight -1.5. This discrepancy is preserved explicitly.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]

LAYER_SIZES = (2, 4, 2)

INPUTS = np.array(
    [
        [8.40739, 2.9386],
        [8.25326, 3.28037],
        [8.0309, 3.70669],
        [7.69392, 4.24922],
        [7.14987, 4.9518],
        [6.19551, 5.86087],
        [4.33232, 6.92405],
    ],
    dtype=float,
)

TARGETS = np.array(
    [
        [0.174533, 0.290889],
        [0.19635, 0.32725],
        [0.2244, 0.374],
        [0.2618, 0.436333],
        [0.31416, 0.5236],
        [0.3927, 0.6545],
        [0.5236, 0.872667],
    ],
    dtype=float,
)

# Link numbering in the scanned diagram is:
#   links 1-8  : 2 input nodes -> 4 hidden nodes
#   links 9-16 : 4 hidden nodes -> 2 output nodes
REPORTED_WEIGHTS = np.array(
    [
        -1.11,
        0.39,
        -0.37,
        0.00,
        1.00,
        -0.73,
        0.60,
        0.00,
        0.57,
        0.63,
        -1.50,
        -1.42,
        0.03,
        0.95,
        -0.78,
        0.00,
    ],
    dtype=float,
)

REPORTED_CONNECTIVITY = "1110111011111110"
REPORTED_SUMMED_ERROR = 0.000208


def sigmoid(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, -500.0, 500.0)
    return 1.0 / (1.0 + np.exp(-clipped))


def forward(inputs: np.ndarray, weights: np.ndarray) -> np.ndarray:
    w1 = weights[:8].reshape(2, 4)
    w2 = weights[8:].reshape(4, 2)
    hidden = sigmoid(inputs @ w1)
    return sigmoid(hidden @ w2)


def main() -> None:
    outputs = forward(INPUTS, REPORTED_WEIGHTS)
    squared_error = float(np.sum((outputs - TARGETS) ** 2))

    # The report calls the value "Summed Error". Dividing the reproduced
    # squared error by 7 patterns * 4 nodes gives 0.00020773..., which
    # rounds to the reported 0.000208. We record this as a numerical match,
    # not as proof of the original error-normalisation implementation.
    normalized_error = squared_error / (len(INPUTS) * 4)

    zero_weight_links = [
        index + 1
        for index, weight in enumerate(REPORTED_WEIGHTS)
        if weight == 0.0
    ]
    zero_connectivity_links = [
        index + 1
        for index, bit in enumerate(REPORTED_CONNECTIVITY)
        if bit == "0"
    ]

    record = {
        "experiment": "Robot inverse kinematics",
        "phase": "reported_solution_verification",
        "architecture": list(LAYER_SIZES),
        "training_patterns": len(INPUTS),
        "chromosome_length_reported": 128,
        "links": 16,
        "reported_connectivity": REPORTED_CONNECTIVITY,
        "reported_weights": REPORTED_WEIGHTS.tolist(),
        "reported_zero_weight_links": [4, 8, 11, 16],
        "zero_weight_links_from_table": zero_weight_links,
        "zero_connectivity_links_from_string": zero_connectivity_links,
        "population_size": 30,
        "generations": 500,
        "crossover_probability": 0.4,
        "mutation_probability": 0.01,
        "reported_weight_range": [-1.5, 1.5],
        "reported_summed_error": REPORTED_SUMMED_ERROR,
        "reproduced_squared_error": squared_error,
        "reproduced_normalized_error": normalized_error,
        "rounded_normalized_error": round(normalized_error, 6),
        "matches_reported_error_to_6dp": round(normalized_error, 6)
        == REPORTED_SUMMED_ERROR,
        "encoding_status": (
            "Unresolved. 128 bits for 16 links implies 8 bits/link, "
            "but the surviving C implementation establishes a 10-bit "
            "weight field for the recovered GA module. No historical "
            "robot-specific encoder has been recovered."
        ),
        "source_discrepancy": (
            "The scanned prose says links 4, 8, 11 and 16 are zero. "
            "The scanned weight table gives link 11 = -1.50, while the "
            "16-bit connectivity string has zero bits at links 4, 8 and 16. "
            "The discrepancy is preserved rather than corrected."
        ),
        "historical_status_note": (
            "Modern Python verification of the scanned 1998 solution; "
            "not a reproduction of the original GA random run."
        ),
    }

    print(json.dumps(record, indent=2))

    output = ROOT / "results" / "robot_historical_verification.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
