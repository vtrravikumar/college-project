"""3-bit parity reconstruction experiment.

The report records chromosome length 132 for a 3-2-2-1 network. Surviving C
evidence supports 10 bits per weight and therefore 120 weight bits for 12 links.
Connectivity is separately described. Both interpretations are deliberately
run without deciding which was historical.
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
TARGETS=tuple(((sum(row)%2),) for row in INPUTS)
CONNECTIVITY="111011110111"
PARAMS=dict(population_size=30,generations=1000,crossover_probability=0.5,mutation_probability=0.09,upper_range=12.0,success_threshold=0.05)

def run():
    records=[]
    for label,combined in (("A_120_weight_bits_separate_connectivity",False),("B_132_combined_weight_and_connectivity",True)):
        result=train_historical_ga(np.random.default_rng(1998),INPUTS,TARGETS,**PARAMS,connectivity_bits=CONNECTIVITY,layer_sizes=(3,2,2,1),chromosome_bits=132 if combined else 120,evolve_connectivity=combined)
        records.append({"interpretation":label,"reported_chromosome_length":132,"weight_bits":120,"connectivity_bits":12,"status":"success" if result.success else "not_converged","seed":1998,"best_fitness":result.best_fitness,"initial_best_fitness":result.initial_best_fitness,"generations_completed":result.generations_completed,"connectivity_target":CONNECTIVITY,"hypothesis_note":"B is hypothetical; no surviving source proves a combined 132-bit chromosome." if combined else "A follows the surviving 10-bit weight-field evidence with connectivity stored separately."})
    return records

if __name__=="__main__":
    records=run()
    print(json.dumps(records,indent=2))
    out=ROOT/"results"/"parity_historical_seed1998.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(records,indent=2)+"\n",encoding="utf-8")
