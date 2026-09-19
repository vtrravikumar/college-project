# Project Validation

This directory contains a reproducibility-oriented Python implementation of the
1998 college project described in the report:

> Analysis of Artificial Neural Network Using Back Propagation & Genetic Algorithm

The first phase validates the core ideas without claiming to reproduce the
original Watcom C implementation byte-for-byte.

## Phase 1

- feed-forward neural network
- mean squared error
- back-propagation training
- genetic-algorithm weight optimisation
- binary weight encoding/decoding
- XOR experiment
- repeated seeded GA runs
- JSON result output

The original report is the source of truth. Where the report does not provide
enough information to reconstruct an experiment exactly, the implementation
uses an explicit documented assumption rather than silently inventing details.

## Run

From the repository root:

```bash
python validation/validate_project.py
```

Optional:

```bash
python validation/validate_project.py --runs 30 --seed 42
```

Results are written to `validation/results/xor.json`.

## Scope

This is deliberately incremental. Three-bit parity, decoder validation,
connectivity optimisation, and robot inverse kinematics will be added only
after the relevant source material has been recovered and verified.
