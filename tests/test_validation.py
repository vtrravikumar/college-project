import sys
from pathlib import Path

import numpy as np

VALIDATION = Path(__file__).resolve().parents[1] / "validation"
sys.path.insert(0, str(VALIDATION))

from genetic_algorithm import decode_weights, encode_weights
from neural_network import NeuralNetwork
from validate_project import xor_dataset


def test_xor_dataset_is_complete():
    inputs, targets = xor_dataset()

    assert inputs.tolist() == [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert targets.ravel().tolist() == [0, 1, 1, 0]


def test_weight_binary_round_trip():
    values = np.array([-1.0, -0.25, 0.0, 0.5, 1.0])
    encoded = encode_weights(values, minimum=-1.0, maximum=1.0, bits=8)
    decoded = decode_weights(encoded, minimum=-1.0, maximum=1.0)

    assert encoded.shape == (5, 8)
    np.testing.assert_allclose(decoded, values, atol=1 / 127)


def test_network_forward_shape():
    network = NeuralNetwork((2, 2, 2, 1), np.random.default_rng(42))
    inputs, _ = xor_dataset()

    output = network.forward(inputs)

    assert output.shape == (4, 1)
    assert np.all(output >= 0.0)
    assert np.all(output <= 1.0)
