"""Small feed-forward neural network used by the validation harness."""

from __future__ import annotations

import numpy as np


class NeuralNetwork:
    """Dense feed-forward network with sigmoid hidden/output units."""

    def __init__(self, layer_sizes: tuple[int, ...], rng: np.random.Generator):
        if len(layer_sizes) < 2:
            raise ValueError("A network needs at least input and output layers.")
        self.layer_sizes = layer_sizes
        self.weights = [
            rng.uniform(-1.0, 1.0, size=(left + 1, right))
            for left, right in zip(layer_sizes[:-1], layer_sizes[1:])
        ]

    @staticmethod
    def sigmoid(x: np.ndarray) -> np.ndarray:
        x = np.clip(x, -60.0, 60.0)
        return 1.0 / (1.0 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(output: np.ndarray) -> np.ndarray:
        return output * (1.0 - output)

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        activation = np.asarray(inputs, dtype=float)
        for weights in self.weights:
            activation_with_bias = np.concatenate(
                [activation, np.ones((activation.shape[0], 1))], axis=1
            )
            activation = self.sigmoid(activation_with_bias @ weights)
        return activation

    def mse(self, inputs: np.ndarray, targets: np.ndarray) -> float:
        prediction = self.forward(inputs)
        return float(np.mean((prediction - targets) ** 2))

    def parameter_vector(self) -> np.ndarray:
        return np.concatenate([weights.ravel() for weights in self.weights])

    def set_parameter_vector(self, vector: np.ndarray) -> None:
        offset = 0
        for weights in self.weights:
            size = weights.size
            weights[:] = vector[offset : offset + size].reshape(weights.shape)
            offset += size
        if offset != len(vector):
            raise ValueError("Parameter vector length does not match network.")
