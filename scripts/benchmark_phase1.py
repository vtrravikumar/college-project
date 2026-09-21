"""Benchmark the modern Phase 1 experiment workloads.

This measures wall-clock time for the current Python reconstruction on the
machine where the script is executed. It is explicitly a modern runtime
measurement, not a reconstruction of the 1998 hardware/runtime.
"""

from __future__ import annotations

import json
import platform
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKLOADS = [
    ("parity", [sys.executable, "experiments/parity_historical.py"]),
    ("decoder", [sys.executable, "experiments/decoder_historical.py"]),
    ("robot_verification", [sys.executable, "experiments/robot_historical.py"]),
]


def main() -> None:
    records = []
    for name, command in WORKLOADS:
        started = time.perf_counter()
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        elapsed = time.perf_counter() - started
        records.append(
            {
                "workload": name,
                "elapsed_seconds": elapsed,
                "return_code": completed.returncode,
            }
        )

    result = {
        "benchmark": "Phase 1 modern reconstruction workloads",
        "historical_status": "modern_runtime_only",
        "python": platform.python_version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "records": records,
    }

    output = ROOT / "results" / "phase1_modern_runtime.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
