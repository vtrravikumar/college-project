"""First end-to-end XOR run for the 1998 college-project reconstruction.

This is a modern Python experiment based on the historical report/source
evidence. It is not a reproduction of the original random run.

The documented XOR parameters recovered so far are:
- population: 25
- generations: 1400
- crossover probability: 0.9
- mutation probability: 0.04
- reported weight range: approximately -5.58 to +5.8

The surviving C decoder uses the upper range and a scale of 100. Because the
original encode() implementation and value.dat are unavailable, this run uses
the explicitly documented C-observed decoder reconstruction with upper_range
5.8. The reported lower bound is therefore recorded as source context rather
than silently forced into the decoder.

Run from the repository root:

    PYTHONPATH=validation python experiments/xor_historical.py

The seed is explicit so the run is reproducible.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validation"))

from historical_ga_training import train_historical_ga


INPUTS = (
    (0.0, 0.0),
    (0.0, 1.0),
    (1.0, 0.0),
    (1.0, 1.0),
)
TARGETS = ((0.0,), (1.0,), (1.0,), (0.0,))
SEED = 1998


def main() -> None:
    result = train_historical_ga(
        np.random.default_rng(SEED),
        INPUTS,
        TARGETS,
        population_size=25,
        generations=1400,
        crossover_probability=0.9,
        mutation_probability=0.04,
        upper_range=5.8,
        connectivity_bits="1" * 10,
        success_threshold=0.05,
    )

    record = {
        "experiment": "XOR",
        "status": "success" if result.success else "not_converged",
        "seed": SEED,
        "population_size": 25,
        "generations_requested": 1400,
        "generations_completed": result.generations_completed,
        "crossover_probability": 0.9,
        "mutation_probability": 0.04,
        "reported_weight_range": [-5.58, 5.8],
        "decoder_upper_range_used": 5.8,
        "success_threshold": 0.05,
        "initial_best_fitness": result.initial_best_fitness,
        "best_fitness": result.best_fitness,
        "best_chromosome": "".join(str(int(bit)) for bit in result.best_chromosome),
        "historical_status_note": (
            "Modern seeded reconstruction; not the original 1998 random run."
        ),
    }

    print(json.dumps(record, indent=2))

    output = ROOT / "results" / "xor_historical_seed1998.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
