"""End-to-end historical-style GA training loop.

Modern Python reconstruction.  Defaults preserve the recovered 2-2-2-1,
100-bit weight chromosome with separate connectivity.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
import numpy as np
from historical_chromosome import build_chromosome, connection_layout
from historical_fitness import mean_squared_error, DEFAULT_LAYER_SIZES
from historical_ga_generation import generate_one_step

@dataclass(frozen=True)
class HistoricalTrainingResult:
    best_chromosome: np.ndarray
    best_fitness: float
    generations_completed: int
    success: bool
    initial_best_fitness: float
    best_fitness_history: tuple[float,...]

def train_historical_ga(
    rng: np.random.Generator,
    inputs: tuple[Sequence[float],...],
    targets: tuple[Sequence[float],...],
    *,
    population_size:int, generations:int, crossover_probability:float,
    mutation_probability:float, upper_range:float,
    connectivity_bits:str="1"*10, success_threshold:float=0.05,
    layer_sizes:Sequence[int]=DEFAULT_LAYER_SIZES,
    chromosome_bits:int|None=None,
    evolve_connectivity:bool=False,
) -> HistoricalTrainingResult:
    links=sum(layer_sizes[i]*layer_sizes[i+1] for i in range(3))
    if len(connectivity_bits)!=links: raise ValueError(f"connectivity_bits must contain exactly {links} bits")
    weight_bits=links*10
    if chromosome_bits is None: chromosome_bits=weight_bits + (links if evolve_connectivity else 0)
    expected=weight_bits + (links if evolve_connectivity else 0)
    if chromosome_bits!=expected: raise ValueError(f"chromosome_bits must be {expected} for this representation")
    population=rng.integers(0,2,size=(population_size,chromosome_bits),dtype=np.uint8)
    def evaluate(chromosome):
        bits="".join(str(int(b)) for b in chromosome[:weight_bits])
        conn=connectivity_bits if not evolve_connectivity else "".join(str(int(b)) for b in chromosome[weight_bits:])
        return mean_squared_error(inputs,targets,build_chromosome(bits,conn),layer_sizes=layer_sizes,upper_range=upper_range)
    fitness=np.array([evaluate(c) for c in population])
    best_i=int(np.argmin(fitness)); best=population[best_i].copy(); best_fit=float(fitness[best_i]); initial=best_fit; history=[best_fit]
    if best_fit<success_threshold:
        return HistoricalTrainingResult(best,best_fit,0,True,initial,tuple(history))
    completed=0
    for _ in range(generations):
        result=generate_one_step(rng,population,fitness,crossover_probability=crossover_probability,mutation_probability=mutation_probability,evaluate=evaluate)
        population=result.new_population
        fitness=np.array([evaluate(c) for c in population])
        i=int(np.argmin(fitness)); current=float(fitness[i])
        if current<best_fit: best_fit=current; best=population[i].copy()
        history.append(best_fit); completed+=1
        if best_fit<success_threshold: break
    return HistoricalTrainingResult(best,best_fit,completed,best_fit<success_threshold,initial,tuple(history))
