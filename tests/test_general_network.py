"""Focused tests for generalised reported network sizes."""
import sys
from pathlib import Path
VALIDATION=Path(__file__).resolve().parents[1]/"validation"; sys.path.insert(0,str(VALIDATION))
from historical_chromosome import connection_layout,build_chromosome
from historical_fitness import forward,mean_squared_error

def test_parity_has_twelve_links_and_120_weight_bits():
    assert len(connection_layout((3,2,2,1)))==12
    c=build_chromosome("0"*120,"111011110111")
    assert len(c.weight_chunks)==12

def test_general_forward_accepts_three_inputs():
    c=build_chromosome("0"*120,"111011110111")
    assert forward((0,1,0),c,layer_sizes=(3,2,2,1),upper_range=12.0)==(0.5,)

def test_general_mse_accepts_eight_parity_patterns():
    c=build_chromosome("0"*120,"111011110111")
    inputs=tuple(tuple((n>>i)&1 for i in (2,1,0)) for n in range(8))
    targets=tuple(((sum(row)%2),) for row in inputs)
    assert mean_squared_error(inputs,targets,c,layer_sizes=(3,2,2,1),upper_range=12.0)==0.25
