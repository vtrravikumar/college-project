# College Project — Digitization & Technical Book

This repository contains the digitization work for an original college project report, with the long-term goal of producing a professional technical book using [VTR Press](https://github.com/vtrravikumar/vtr-press).

## Objective

Preserve the original college project faithfully while converting the physical report into a structured Markdown manuscript suitable for modern publishing.

The source report contains:

- prose and technical documentation
- Watcom C source code
- tables
- diagrams and other images
- references and supporting material

## Digitization principle

The physical report / master scan is the source of truth. OCR and automated processing are used to reduce manual work, but technical content, source code, tables, captions, and figures must be verified against the original pages.

The initial objective is **faithful digitization**, not modernization or rewriting of the original technical content.

## Planned workflow

```text
Physical report
      ↓
High-resolution scan
      ↓
Page preprocessing
      ↓
OCR / extraction
      ↓
Structure and cleanup
      ↓
Manual fidelity review
      ↓
manuscript.md
      ↓
VTR Press
      ↓
Technical book PDF / EPUB
```

## Repository structure

```text
college-project/
├── manuscript.md             # Main book manuscript
├── metadata.yaml              # Book and author metadata
├── README.md
├── .gitignore
│
├── source/                    # Source material policy documented separately
├── ocr/                       # OCR output and intermediate text
├── images/                    # Extracted / cleaned figures
├── tables/                    # Reconstructed tables where useful
├── notes/                     # Digitization and editorial notes
├── scripts/                   # Reproducible digitization tooling
└── tests/                     # Tests for scripts and validation
```

## Authors

The original report has three authors. Multi-author publishing support in VTR Press is tracked as a **v2.1 requirement** and this project will serve as a practical test case for that capability.

Author names will be recorded from the original report rather than inferred.

## Source files and Git

The original physical scan will be treated as the immutable source. Large scans and other binary intermediates should not be committed until the storage approach is decided. Reproducible scripts, manuscript content, metadata, notes, and appropriately sized source assets belong in Git.

## Status

**Phase 0 — Repository setup**

The repository is initialized and ready for the first representative scan. The next step is to scan a small sample of pages and use them to validate the OCR and document-reconstruction workflow before processing the full report.
