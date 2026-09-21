"""3-bit decoder reconstruction experiment.

Historical report evidence verified from the original scanned pages:
- network: 3-2-2-3
- not fully connected
- chromosome length: 170
- population: 25
- generations: 1900
- crossover: 0.5
- mutation: 0.01
- weight range: -12 to +12
- zero-weight links: 2, 6, 10
- training patterns: 011->011, 101->101, 110->110

Surviving C evidence establishes 10 bits per weight for the recovered GA
implementation. A 3-2-2-3 network has 16 possible weighted links, hence
160 weight bits. The scanned report confirms a 170-bit chromosome. The
remaining 10 bits are therefore unresolved; 170 is not explained by simply
appending all 16 connectivity bits.

This experiment uses the exact training patterns visible in the scan. It is a
modern seeded reconstruction, not the original 1998 random run.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"validation"))
from historical_ga_training import train_historical_ga

INPUTS=(
    (0.0,1.0,1.0),
    (1.0,0.0,1.0),
    (1.0,1.0,0.0),
)
TARGETS=INPUTS

# Scanned report: links 2, 6 and 10 have zero weights.
CONNECTIVITY=list("1"*16)
for link in (2,6,10):
    CONNECTIVITY[link-1]="0"
CONNECTIVITY="".join(CONNECTIVITY)

PARAMS=dict(
    population_size=25,
    generations=1900,
    crossover_probability=0.5,
    mutation_probability=0.01,
    upper_range=12.0,
    success_threshold=0.05,
)

def run():
    result=train_historical_ga(
        np.random.default_rng(1998),
        INPUTS,
        TARGETS,
        **PARAMS,
        connectivity_bits=CONNECTIVITY,
        layer_sizes=(3,2,2,3),
        chromosome_bits=160,
        evolve_connectivity=False,
    )
    return {
        "experiment":"3-bit decoder",
        "interpretation":"160 weight bits + separate 16-bit connectivity",
        "reported_chromosome_length":170,
        "weight_bits":160,
        "connectivity_bits":16,
        "status":"success" if result.success else "not_converged",
        "seed":1998,
        "population_size":25,
        "generations_requested":1900,
        "generations_completed":result.generations_completed,
        "crossover_probability":0.5,
        "mutation_probability":0.01,
        "reported_weight_range":[-12,12],
        "initial_best_fitness":result.initial_best_fitness,
        "best_fitness":result.best_fitness,
        "connectivity_target":CONNECTIVITY,
        "zero_weight_links_reported":[2,6,10],
        "training_data":"011->011, 101->101, 110->110",
        "chromosome_note":"The scanned report confirms 170. With 16 links and surviving 10-bit weight fields, the recovered weight representation is 160 bits. Appending the 16 connectivity bits would give 176, not 170; the extra 10-bit discrepancy remains unresolved."
    }

if __name__=="__main__":
    record=run()
    print(json.dumps(record,indent=2))
    out=ROOT/"results"/"decoder_historical_seed1998.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
