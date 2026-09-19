# College Project — Digitization & Technical Book

This repository contains the digitization and reconstruction of the original college project report, with the long-term goal of producing a professional technical book using VTR Press.

## Objective

Preserve the original college project faithfully while recreating its experiments in a modern programming language.

The Phase 1 objective is **historical reconstruction, not modernization**:

- preserve the original theory and manuscript
- recover the algorithmic intent from the report and surviving Watcom C source
- implement the algorithms in modern Python
- reproduce the documented applications and experiments
- compare historical and reproduced results
- record runtime and hardware context
- document uncertainty and discrepancies explicitly

Modern research extensions will be considered only after Phase 1 is complete.

## Digitization principle

The physical report / master scan is the source of truth. OCR and automated processing are used to reduce manual work, but technical content, source code, tables, captions, and figures must be verified against the original pages.

The surviving Watcom C source is treated as implementation evidence. Because extraction/transcription errors may exist, it is not assumed to be authoritative until verified against the source pages.

## Phase 1 workflow

```text
Original report / scan
        ↓
Faithful manuscript
        ↓
Algorithm & experiment reconstruction
        ↓
Old C source as implementation evidence
        ↓
Modern Python implementation
        ↓
Reproduced applications and results
        ↓
Historical vs modern comparison
        ↓
Completed technical book
```

## Repository structure

```text
college-project/
├── archive/
│   ├── manuscripts/
│   └── original-code/          # Surviving Watcom C source PDFs
├── source/
│   └── report/                 # Original report scans
├── manuscript_printready.md
├── metadata.yaml
├── docs/
│   └── reconstruction.md       # Phase 1 reconstruction methodology
├── validation/                 # Modern reconstruction and validation code
├── tests/
├── digitization/
├── notes/
└── README.md
```

## Authors

The original report has three authors. Multi-author publishing support in VTR Press is tracked as a **v2.1 requirement** and this project serves as a practical test case for that capability.

Author names are recorded from the original report rather than inferred.

## Phase 1 status

**Manuscript:** substantially reconstructed; fidelity review continues.

**Theory:** documented in the manuscript; reconstruction matrix established.

**Code:** modern validation harness exists; historical algorithm reconstruction continues.

**Experiments:** XOR validation is the initial experiment. Additional documented applications remain to be reconstructed.

**Results:** validation results are persisted in `validation/results/`; historical-vs-modern comparison remains in progress.

See `docs/reconstruction.md` for the reconstruction rules, evidence hierarchy, experiment sequence, and Phase 1 exit condition.

## Phase 2 — future

After Phase 1 is frozen, the project may investigate the relationship between the 1998 work and modern neuroevolution, neural architecture search, evolutionary optimisation, and any unanswered research questions identified during reconstruction.
