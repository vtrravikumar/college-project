"""Run Phase 1 reproducibility experiments for the college project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np

# Allow direct execution from the repository root.
VALIDATION_DIR = Path(__file__).resolve().parent
if str(VALIDATION_DIR) not in sys.path:
    sys.path.insert(0, str(VALIDATION_DIR))

from backprop import train_backprop
from genetic_algorithm import GAConfig, encode_weights, train_genetic
from neural_network import NeuralNetwork


def xor_dataset() -> tuple[np.ndarray, np.ndarray]:
    inputs = np.array(
        [[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float
    )
    targets = np.array([[0], [1], [1], [0]], dtype=float)
    return inputs, targets


def accuracy(network: NeuralNetwork, inputs: np.ndarray, targets: np.ndarray) -> float:
    prediction = (network.forward(inputs) >= 0.5).astype(int)
    return float(np.mean(prediction == targets))


def run_xor(runs: int, seed: int) -> dict:
    inputs, targets = xor_dataset()

    bp_rng = np.random.default_rng(seed)
    bp_network = NeuralNetwork((2, 2, 2, 1), bp_rng)
    bp = train_backprop(
        bp_network,
        inputs,
        targets,
        learning_rate=2.0,
        epochs=10000,
        tolerance=1e-4,
    )

    ga_runs = []
    config = GAConfig(
        population_size=80,
        generations=500,
        crossover_probability=0.8,
        mutation_probability=0.02,
    )

    for run in range(runs):
        rng = np.random.default_rng(seed + run)
        network = NeuralNetwork((2, 2, 2, 1), rng)
        result = train_genetic(
            network,
            inputs,
            targets,
            config=config,
            rng=rng,
        )
        ga_runs.append(
            {
                "run": run + 1,
                "seed": seed + run,
                "generations": result["generations"],
                "final_mse": result["final_mse"],
                "accuracy": accuracy(network, inputs, targets),
                "converged": result["final_mse"] <= 1e-4,
                "history": result["history"],
            }
        )

    encoded = encode_weights(
        bp_network.parameter_vector(),
        minimum=-1.0,
        maximum=1.0,
        bits=8,
    )

    result = {
        "experiment": "XOR",
        "network": [2, 2, 2, 1],
        "dataset": inputs.astype(int).tolist(),
        "targets": targets.astype(int).tolist(),
        "backpropagation": {
            "epochs": bp["epochs"],
            "final_mse": bp["final_mse"],
            "accuracy": accuracy(bp_network, inputs, targets),
            "history": bp["history"],
        },
        "genetic_algorithm": {
            "runs": ga_runs,
            "summary": {
                "successful_runs": sum(r["converged"] for r in ga_runs),
                "total_runs": runs,
                "best_mse": min(r["final_mse"] for r in ga_runs),
                "mean_mse": float(np.mean([r["final_mse"] for r in ga_runs])),
                "worst_mse": max(r["final_mse"] for r in ga_runs),
            },
        },
        "encoding_smoke_test": {
            "bits_per_weight": 8,
            "encoded_weight_count": len(encoded),
            "status": "PASS",
        },
    }

    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=30)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.runs < 1:
        parser.error("--runs must be at least 1")

    results_dir = VALIDATION_DIR / "results"
    results_dir.mkdir(exist_ok=True)

    result = run_xor(args.runs, args.seed)
    output = results_dir / "xor.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    summary_output = results_dir / "phase1-xor-results.md"
    bp = result["backpropagation"]
    ga = result["genetic_algorithm"]["summary"]
    config = result["genetic_algorithm"]["configuration"]
    summary = [
        "# Phase 1 Validation — XOR Experiment",
        "",
        "This file records the outcome of the reproducibility-oriented Phase 1 validation harness. "
        "It is not a claim of byte-for-byte reproduction of the original 1998 Watcom C implementation.",
        "",
        "## Experiment",
        "",
        f"- Dataset: XOR ({len(result['dataset'])} patterns)",
        f"- Network: {result['network']}",
        f"- Validation seed: {args.seed}",
        f"- GA runs: {args.runs}",
        "",
        "## Back Propagation",
        "",
        f"- Epochs: {bp['epochs']}",
        f"- Final MSE: {bp['final_mse']:.8f}",
        f"- Accuracy: {bp['accuracy']:.1%}",
        "",
        "## Genetic Algorithm",
        "",
        f"- Population: {config['population_size']}",
        f"- Maximum generations: {config['generations']}",
        f"- Crossover probability: {config['crossover_probability']}",
        f"- Mutation probability: {config['mutation_probability']}",
        f"- Successful runs: {ga['successful_runs']}/{ga['total_runs']}",
        f"- Best MSE: {ga['best_mse']:.8f}",
        f"- Mean MSE: {ga['mean_mse']:.8f}",
        f"- Worst MSE: {ga['worst_mse']:.8f}",
        "",
        "## Encoding Smoke Test",
        "",
        f"- Bits per weight: {result['encoding_smoke_test']['bits_per_weight']}",
        f"- Encoded weight count: {result['encoding_smoke_test']['encoded_weight_count']}",
        f"- Status: {result['encoding_smoke_test']['status']}",
        "",
        "## Interpretation",
        "",
        "These results document the current Phase 1 Python reconstruction. Exact comparison with the original project requires verification of the archived C source and its encoding and GA conventions.",
        "",
        "The complete machine-readable run record, including per-run histories, is stored in xor.json.",
        "",
    ]
    summary_output.write_text("\n".join(summary), encoding="utf-8")

    bp = result["backpropagation"]
    ga = result["genetic_algorithm"]["summary"]

    print("=" * 56)
    print("COLLEGE PROJECT VALIDATION — PHASE 1")
    print("=" * 56)
    print("Experiment: XOR")
    print("Network:    2-2-2-1")
    print()
    print(f"Back Propagation MSE : {bp['final_mse']:.8f}")
    print(f"Back Propagation acc : {bp['accuracy']:.1%}")
    print()
    print(f"GA runs              : {ga['total_runs']}")
    print(f"GA successful runs   : {ga['successful_runs']}/{ga['total_runs']}")
    print(f"GA best MSE          : {ga['best_mse']:.8f}")
    print(f"GA mean MSE          : {ga['mean_mse']:.8f}")
    print(f"GA worst MSE         : {ga['worst_mse']:.8f}")
    print()
    print(f"Results              : {output}")
    print("=" * 56)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
