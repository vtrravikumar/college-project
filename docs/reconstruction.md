# Reconstruction Plan

## Purpose

This document defines the Phase 1 reconstruction of the 1998 college project:

**ANALYSIS OF ARTIFICIAL NEURAL NETWORK — USING BACK PROPAGATION & GENETIC ALGORITHM**

The objective is to recreate the original project in a modern programming language while preserving its original theory, experimental intent, and documented conclusions.

This is **not** a modernization of the research at this stage. Modern research context and any new hypotheses belong to a later phase.

## Phase 1 boundary

Phase 1 is complete when we have:

1. A faithful, readable reconstruction of the original project manuscript.
2. A modern implementation of the algorithms and experiments described by the manuscript.
3. Reproduced application experiments, using the same problem definitions where they can be established.
4. A comparison between the historical reported results and the modern reconstruction.
5. Runtime measurements on modern hardware, clearly separated from algorithmic performance.
6. Documentation of discrepancies, assumptions, and unresolved historical details.
7. A reproducible codebase and results suitable for reference from the finished book.

The complete modern source code does not need to be printed in the book. It can remain in this repository and be referenced from the book.

## Evidence hierarchy

The reconstruction uses three evidence sources:

### 1. Original report — primary specification

The report is the primary source for:

- project objectives
- terminology
- problem definitions
- methodology
- algorithms as described in prose
- experimental setup
- applications
- reported results
- conclusions

The current manuscript states that the project evolves feed-forward neural networks using a genetic algorithm, represents candidate solutions as concatenated link weights, evaluates fitness using mean squared error, and applies reproduction, crossover and mutation over generations.

### 2. Surviving Watcom C source — implementation evidence

The archived source is retained under:

`archive/original-code/Code-01.pdf`
`archive/original-code/Code-02.pdf`
`archive/original-code/Code-03.pdf`

The source is useful for recovering implementation flow, parameter names, data structures and operations that may not be fully explained by the prose.

However, the surviving source was recovered from old material and may contain extraction/transcription errors. It must therefore be visually verified against the source pages before an implementation detail is treated as authoritative.

### 3. Modern Python implementation — reproducible reconstruction

The Python implementation is evidence of what we have actually reproduced.

It must not be described as the original implementation or as a byte-for-byte translation of the Watcom C program.

Where historical evidence is incomplete, the modern implementation will document the chosen interpretation.

## Reconstruction matrix

| Area | Evidence from report | Evidence from old source | Reconstruction status | Confidence |
|---|---|---|---|---|
| Project objective | GA-based evolution of feed-forward ANN | To be reviewed | Established | High |
| Problem domain | Boolean functions and robot arm movement | To be reviewed | Established | High |
| Neural-network representation | Link weights/connectivity | To be reviewed | Partially established | Medium |
| Fitness | Mean squared error / summed error in reported experiments | To be reviewed | Established | Medium-High |
| GA population | Population of candidate strings | To be reviewed | Established | High |
| Selection/reproduction | Fitter strings survive | To be reviewed | Established | High |
| Crossover | GA crossover operation | To be reviewed | Established | High |
| Mutation | GA mutation operation | To be reviewed | Established | High |
| Enhanced encoding | Explicitly identified by project | To be recovered | Pending | Medium |
| Binary weight representation | Described in methodology | To be verified | Pending exact convention | Medium |
| Connectivity evolution | Described as part of network design | To be verified | Pending | Medium |
| Back Propagation baseline | Used for comparison | To be reviewed | Partially established | Medium |
| XOR | Reported Boolean-function experiment; scan confirms 100-bit chromosome and 25/1400/0.9/0.04 parameters | Surviving C is consistent with 10 links × 10 bits | Modern harness exists; historical reported values documented | High |
| 3-bit parity | Scan confirms 3-2-2-1, 132-bit chromosome, 12-link connectivity, training table and 57/21 sec timings | Surviving C gives 10-bit weight fields | Modern reconstruction completed; 120-bit separate-connectivity and hypothetical 132-bit combined interpretations tested | High for source facts; Medium for encoding interpretation |
| Decoder | Scan confirms 3-2-2-3, 170-bit chromosome, three training patterns, 16-link table and 84/70 sec timings | Surviving C gives 10-bit weight fields | Modern reconstruction completed; 170-bit encoding remains unresolved | High for source facts; Low-Medium for encoding interpretation |
| Robot inverse kinematics | Scans confirm 2-4-2, seven training patterns, 16 links, 128-bit chromosome and 0.000208 summed error | Surviving C establishes 10-bit weight fields, but robot-specific encoding is not recovered | Reported solution numerically verified; 128-bit encoding remains unresolved | High for source facts; High for reported-result verification |
| GA parameter values | Verified against original scans for parity, decoder and robot | Partially verified where surviving source applies | Major application parameters documented | High |
| Historical execution time | Report contains BP/GA timings for parity, decoder and robot | Not required for algorithm reconstruction | Historical timings documented; modern timing still pending | High for reported values |
| Historical hardware | Not established in current evidence | Not established | Pending | Unknown |

Confidence describes confidence in the **historical claim**, not confidence that the OCR/source extraction is error-free.

## Reconstruction rules

### Rule 1 — Preserve the original theory

The manuscript should retain the original technical argument and terminology during Phase 1.

We may correct obvious transcription/OCR errors, but we should not silently replace the 1998 methodology with a modern algorithm.

### Rule 2 — Reconstruct the algorithm, not the syntax

The new implementation will reproduce the algorithmic behaviour of the original project in modern Python.

We do not need to reproduce:

- Watcom-specific syntax
- old memory-management techniques
- compiler-specific constructs
- original user-interface code

unless those details affect the algorithmic result.

### Rule 3 — Use the old source as a clue

When the report describes an operation incompletely, the surviving C source can provide implementation clues.

When the report and source disagree, record the discrepancy rather than silently choosing one.

### Rule 4 — Do not invent missing parameters

If a parameter cannot be established from the report or sufficiently verified source, mark it as unresolved and document the assumption used by the reconstruction.

### Rule 5 — Preserve randomness explicitly

Genetic algorithms are stochastic. Modern experiments must record:

- random seed
- population size
- number of generations
- crossover parameters
- mutation parameters
- encoding parameters
- network architecture
- fitness definition

Repeated runs should be used where appropriate.

### Rule 6 — Compare outcomes, not just decimal equality

The first objective is to reproduce the original experimental behaviour and conclusions.

Numerical differences may arise from:

- random initialization
- random-number generators
- floating-point behaviour
- implementation details
- parameter interpretation
- hardware

A numerical mismatch is therefore an observation to investigate, not automatically a reconstruction failure.

## Historical result vs reproduced result

Every completed experiment should distinguish:

### Historical result

What the original report states.

### Reproduced result

What the modern implementation produces.

### Interpretation

Why the results are equal, approximately equal, or different, where the evidence permits an explanation.

Example structure:

| Attribute | Historical project | Modern reconstruction |
|---|---|---|
| Algorithm | As documented | Reconstructed |
| Network | As documented | Equivalent reconstruction |
| Dataset | Original | Same |
| Parameters | Reported values | Reconstructed values |
| Result | Reported result | Measured result |
| Runtime | If available | Measured |
| Hardware | If available | Modern hardware |
| Difference | — | Explained where possible |

## Hardware and runtime

Execution time is part of the reconstruction record but is **not** treated as a direct measure of algorithmic quality.

The original experiments were performed with computing resources available in the late 1990s. The modern implementation will run on contemporary hardware. For small networks, the same algorithm may execute dramatically faster today.

We therefore record runtime as historical/engineering context:

- historical runtime, if documented or reliably measured from surviving evidence
- historical hardware, if documented
- modern runtime
- modern hardware/software environment

We will not manufacture a 1998 runtime or hardware specification where the evidence does not support it.

The comparison should answer:

> How much faster does the same reconstructed workload execute today?

It should not be interpreted as:

> How much better is the algorithm?

## Current validation harness

The existing `validation/` implementation is the beginning of the reconstruction, not its final historical interpretation.

It currently provides:

- feed-forward neural network
- mean squared error
- Back Propagation baseline
- Genetic Algorithm optimisation
- binary encoding/decoding utilities
- XOR validation
- repeated seeded GA runs
- persisted JSON and Markdown results
- automated tests and GitHub Actions validation

The current GA implementation intentionally uses a real-valued chromosome for its baseline. Binary chromosome evolution will only be introduced after the original encoding convention is sufficiently verified.

## Phase 1 experiment sequence

1. Establish the exact project methodology from the manuscript.
2. Inspect and verify the old C source where it can resolve implementation questions.
3. Complete the reconstruction matrix.
4. Reconstruct the first Boolean-function experiment.
5. Compare its historical and modern results.
6. Measure modern execution time.
7. Add remaining documented Boolean-function experiments.
8. Reconstruct the robot arm experiment if the report contains sufficient information.
9. Run the full documented comparison between GA and Back Propagation.
10. Freeze the Phase 1 implementation and results.
11. Integrate the application, experiment and result sections into the manuscript.
12. Publish the reproducible implementation in this repository and reference it from the book.

## Phase 1 exit condition

The project should be considered reconstructed when the modern implementation can demonstrate the original project's central claim under the documented experimental conditions, with any material differences explicitly recorded.

At that point the historical project can be preserved as a completed reconstruction.

## Later phase — not part of this reconstruction

Only after Phase 1 is complete will we investigate:

- how the 1998 approach relates to modern neuroevolution
- neural architecture search
- evolutionary optimisation of topology
- hybrid evolutionary/gradient methods
- unanswered questions from the original work
- experiments that could be meaningful on modern hardware

Those investigations will be treated as a new research/evolution phase and will not be mixed into the historical reconstruction.
