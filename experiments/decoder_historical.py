"""3-bit decoder reconstruction experiment.

Historical report evidence:
- network: 3-2-2-3
- not fully connected
- chromosome length: 170 (reported)
- population: 25
- generations: 1900
- crossover: 0.5
- mutation: 0.01
- weight range: -12 to +12
- reported zero-weight links: 2, 6, 10

Surviving C evidence establishes 10 bits per weight for the recovered GA
implementation. A 3-2-2-3 network has 16 possible weighted links, hence
160 weight bits. Connectivity is separately described in the report/source
model. The reported 170 therefore remains unresolved.

The training table was not recoverable from OCR beyond its heading. The
experiment below uses the minimal source-consistent interpretation of a
3-bit decoder: all eight 3-bit input patterns map to themselves at the
three outputs. This is explicitly a reconstruction assumption, not recovered
historical training data.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"validation"))
from historical_ga_training import train_historical_ga

INPUTS=tuple(tuple((n>>i)&1 for i in (2,1,0)) for n in range(8))
TARGETS=INPUTS

# Report says links 2, 6 and 10 have zero weights; use 1-based link numbering.
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
        "training_data_assumption":"Eight 3-bit input patterns mapped to identical 3-bit outputs; historical training table was not recoverable from OCR.",
        "chromosome_note":"170 is preserved as reported. With 16 links and surviving 10-bit weight fields, the reconstructed weight chromosome is 160 bits; the extra 10 bits remain unexplained."
    }

if __name__=="__main__":
    record=run()
    print(json.dumps(record,indent=2))
    out=ROOT/"results"/"decoder_historical_seed1998.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
