"""Back-propagation training for the validation harness."""

from __future__ import annotations

import numpy as np

from neural_network import NeuralNetwork


def train_backprop(
    network: NeuralNetwork,
    inputs: np.ndarray,
    targets: np.ndarray,
    *,
    learning_rate: float = 1.0,
    epochs: int = 5000,
    tolerance: float = 1e-4,
) -> dict:
    """Train a network using batch gradient descent and sigmoid units.

    This is a modern, explicit reconstruction used as a validation baseline.
    It is not presented as a byte-for-byte reproduction of the 1998 program.
    """
    history: list[float] = []

    for epoch in range(1, epochs + 1):
        activations = [inputs]
        pre_activations = []

        activation = inputs
        for weights in network.weights:
            with_bias = np.concatenate(
                [activation, np.ones((activation.shape[0], 1))], axis=1
            )
            z = with_bias @ weights
            activation = network.sigmoid(z)
            pre_activations.append(z)
            activations.append(activation)

        error = activations[-1] - targets
        mse = float(np.mean(error**2))
        history.append(mse)

        if mse <= tolerance:
            return {"epochs": epoch, "final_mse": mse, "history": history}

        deltas = [None] * len(network.weights)
        deltas[-1] = error * network.sigmoid_derivative(activations[-1])

        for layer in range(len(network.weights) - 2, -1, -1):
            downstream = deltas[layer + 1] @ network.weights[layer + 1].T
            downstream = downstream[:, : network.layer_sizes[layer + 1]]
            deltas[layer] = downstream * network.sigmoid_derivative(
                activations[layer + 1]
            )

        batch_size = len(inputs)
        for layer, weights in enumerate(network.weights):
            a = np.concatenate(
                [activations[layer], np.ones((batch_size, 1))], axis=1
            )
            gradient = (a.T @ deltas[layer]) / batch_size
            weights -= learning_rate * gradient

    return {"epochs": epochs, "final_mse": history[-1], "history": history}
