# Phase 1 Results & Evidence

## Purpose

This document is the working evidence record for the Phase 1 reconstruction of the 1998 college project:

**ANALYSIS OF ARTIFICIAL NEURAL NETWORK — USING BACK PROPAGATION & GENETIC ALGORITHM**

It separates:
1. what is confirmed from the original scanned report;
2. what is supported by the surviving Watcom C source;
3. what the modern Python reconstruction actually reproduces;
4. what remains unresolved.

The modern Python implementation is **not** presented as the original 1998 source.

---

## Experiment 1 — XOR

### Source-verified historical facts

- Network: 2–2–2–1
- Fully connected
- Chromosome length: **100**
- Population: **25**
- Generations: **1400**
- Crossover probability: **0.9**
- Mutation probability: **0.04**
- Weight range: approximately **−5.58 to +5.8**
- Ten network links are present.

The 100-bit chromosome is consistent with the surviving 10-bit weight field:

**10 links × 10 bits = 100 bits**

### Modern validation status

The CI Phase 1 harness currently runs a seeded XOR validation with seed 42 and 3 GA runs. It is a **modern reconstruction harness**, not a reproduction of the original 1998 GA run.

Current validation:
- BP final MSE: **0.12549697**
- BP accuracy: **50.0%**
- GA best MSE: **0.24494425**
- Successful GA runs: **0/3**

These values should not be presented as the historical 1998 results.

---

## Experiment 2 — Three-bit parity

### Source-verified historical facts

- Network: **3–2–2–1**
- Not fully connected
- Chromosome length: **132**
- Population: **30**
- Generations: **1000**
- Crossover probability: **0.9**
- Mutation probability: **0.09**
- Weight range: **−12 to +12**
- Optimal connectivity: 111011110111
- Twelve link weights are listed.
- Zero-weight links: **4 and 9**
- Training set contains all eight 3-bit patterns.
- Reported training time: BP **57 sec**, GA **21 sec**

### Encoding evidence

The architecture has 12 possible links.

The surviving C implementation establishes a 10-bit weight field:

**12 × 10 = 120 weight bits**

The report's confirmed chromosome length is **132 bits**.

The difference is exactly **12**, which equals the number of connectivity bits.

Therefore, **120 weight bits + 12 connectivity bits is strongly consistent with the reported chromosome length**.

However, the surviving C implementation stores connectivity separately in gbit[]. The exact historical internal arrangement of the 132 bits is therefore not proven.

### Modern reconstruction

Two modern interpretations were tested with seed 1998:

| Interpretation | Weight bits | Connectivity | Final best MSE | Status |
|---|---:|---:|---:|---|
| Separate connectivity | 120 | Fixed 12 bits | **0.249886** | Not converged |
| Hypothetical combined chromosome | 120 | 12 bits in 132-bit chromosome | **0.250000** | Not converged |

Both completed all 1000 generations.

These experiments document modern reconstruction behaviour; they do not prove that the original 1998 GA failed to converge.

---

## Experiment 3 — Decoder

### Source-verified historical facts

- Network: **3–2–2–3**
- Not fully connected
- Chromosome length: **170**
- Population: **25**
- Generations: **1900**
- Crossover probability: **0.5**
- Mutation probability: **0.01**
- Weight range: **−12 to +12**
- Training patterns: 011 → 011, 101 → 101, 110 → 110
- Sixteen link weights are listed.
- Zero-weight links: **2, 6 and 10**
- Reported training time: BP **84 sec**, GA **70 sec**

### Encoding evidence

The architecture has 16 possible links.

Using the 10-bit weight field established by the surviving C implementation:

**16 × 10 = 160 weight bits**

If all 16 connectivity bits were appended:

**160 + 16 = 176 bits**

The report nevertheless confirms **170 bits**.

Therefore the decoder chromosome length remains **unresolved**. The difference from the recovered 160-bit weight representation is exactly 10 bits, but there is currently no source evidence establishing what those additional bits represent.

### Modern reconstruction

The modern experiment uses the three training patterns recovered from the scan.

Parameters:
- seed: 1998
- population: 25
- generations: 1900
- crossover: 0.5
- mutation: 0.01
- upper range: 12
- fixed connectivity: 1011101110111111

Result:
- initial best MSE: **0.29745285**
- final best MSE: **0.21826769**
- generations completed: **1900**
- status: **not converged**

This is a modern seeded reconstruction, not a reproduction of the original random sequence.

---

## Experiment 4 — Robot inverse kinematics

### Source-verified historical facts

- Network: **2–4–2**
- Inputs: x, y
- Outputs: θ1, θ2
- Sixteen numbered links
- Seven training patterns
- Chromosome length: **128**
- Population: **30**
- Generations: **500**
- Crossover probability: **0.4**
- Mutation probability: **0.01**
- Weight range: **−1.5 to +1.5**
- Reported summed error: **0.000208**

The scanned weight table gives:

-1.11, 0.39, -0.37, 0.00, 1.00, -0.73, 0.60, 0.00,
0.57, 0.63, -1.50, -1.42, 0.03, 0.95, -0.78, 0.00

The training table contains seven (x, y, θ1, θ2) patterns.

### Encoding evidence

There are 16 links and the report gives a 128-bit chromosome.

**16 × 8 = 128**

This is consistent with an 8-bit-per-link representation.

However, the surviving C implementation establishes a 10-bit weight field for the recovered GA module. No robot-specific historical encoder has been recovered.

Therefore the **128-bit encoding remains unresolved**.

### Reported-result verification

The exact scanned weights were applied to the scanned 2–4–2 training data using the reconstructed sigmoid network.

- squared error: **0.0058164466**
- normalized error: **0.0002077302**
- rounded normalized error: **0.000208**

This matches the report's stated **0.000208**.

This is a **verification of the reported solution**, not a reproduction of the original 500-generation GA random run.

### Source discrepancy

The scanned prose says links **4, 8, 11 and 16** have zero weights.

The scanned weight table shows:
- link 4 = 0.00
- link 8 = 0.00
- link 11 = **−1.50**
- link 16 = 0.00

The scanned connectivity string also has zeroes at links 4, 8 and 16.

This discrepancy is preserved rather than silently corrected.

---

## Cross-experiment encoding evidence

| Experiment | Architecture | Links | Reported chromosome | Recovered weight bits | Observation |
|---|---|---:|---:|---:|---|
| XOR | 2–2–2–1 | 10 | **100** | 100 | Exact match |
| Three-bit parity | 3–2–2–1 | 12 | **132** | 120 | +12 = connectivity count |
| Decoder | 3–2–2–3 | 16 | **170** | 160 | +10 unresolved |
| Robot | 2–4–2 | 16 | **128** | 160 under surviving C convention | 128 is consistent with 8 bits/link |

The evidence does **not** support a single universal chromosome-length rule across all four reported applications.

The safest Phase 1 conclusion is that the project used an enhanced encoding scheme whose exact historical implementation is incompletely preserved in the surviving source.

---

## What Phase 1 has established

### Confirmed

- The original report's four application experiments have been identified.
- Their network architectures have been verified from the scans.
- Historical GA parameters have been recovered for parity, decoder and robot.
- Training data has been recovered for all three of those experiments.
- Historical optimal weight tables have been recovered for parity, decoder and robot.
- Historical connectivity strings have been recovered.
- Historical BP/GA timing figures have been recovered.
- The robot's reported **0.000208** result is numerically reproducible from the scanned solution.

### Still unresolved

- Exact historical chromosome encoding for parity.
- Exact historical chromosome encoding for decoder.
- Exact historical chromosome encoding for robot.
- Full original random-number sequence and initial populations.
- Historical execution hardware.
- Whether the surviving C source represents all application-specific encoding variants.
- Complete historical GA/Back Propagation implementation correspondence.

### Important methodological boundary

A modern reconstruction result is not evidence that the original program produced the same random trajectory.

Where the exact historical implementation cannot be recovered, the project records the discrepancy rather than tuning the modern implementation until it matches the report.

---

## Phase 1 next steps

1. Freeze the source-verified historical experiment data.
2. Measure modern execution time for the reproducible Python workloads.
3. Complete the historical-vs-modern comparison.
4. Update the manuscript's **APPLICATIONS AND RESULTS** section from this evidence record.
5. Review the manuscript for remaining OCR/transcription discrepancies.
6. Run a final CI validation.
7. Freeze the Phase 1 reconstruction before considering modern research extensions.
