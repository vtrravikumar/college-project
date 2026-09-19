# Historical C Reconstruction

This directory contains reconstructed C source derived from the surviving 1998 project code listings.

## Purpose

These files are **historical document artifacts**, not build targets.

The objective is to preserve the structure, terminology, identifiers, constants, routines, and programming style of the surviving source as faithfully as the available evidence permits.

The C source is also used as a reference when reconstructing the project behaviour in modern Python.

## Evidence hierarchy

1. Surviving scanned code PDFs in `archive/original-code/`
2. OCR manuscript in `archive/manuscripts/manuscript-full-run-111-pages.md`
3. Project report in `source/report/`

The OCR manuscript is searchable and useful for reconstruction, but it contains recognition errors. Therefore:

- no claim is made that these files compile;
- OCR uncertainties are marked rather than silently corrected;
- source-page markers are retained;
- where an exact token cannot yet be established from the scan, the uncertainty is documented.

## Compiler

The original compiler has **not been established from the available report/code evidence**. These files therefore do not identify Watcom C as the historical compiler.

## Reconstruction status

- GA source: initial historical transcription/reconstruction
- Back Propagation source: pending
- Counter Propagation source: pending
- Scan-level verification of uncertain OCR tokens: pending

See the individual source README files for details.
