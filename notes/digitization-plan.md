# Digitization Plan

## Source

The source is a physical college project report. A high-resolution scan will be treated as the immutable reference for all transcription work.

## Content types

### Prose

Use OCR as the first-pass transcription method, followed by visual verification against the original scan.

### Watcom C source code

Treat code separately from prose OCR. Preserve indentation, punctuation, identifiers, compiler-specific constructs, and line structure. Every code listing requires verification against the source pages because OCR can silently alter program semantics.

### Tables

Use OCR to recover text where useful, but reconstruct table structure explicitly in Markdown and verify values against the scan.

### Figures and images

Extract or crop the original figures at suitable resolution. Do not depend on OCR for diagrams. Record captions and numbering separately in the manuscript.

## Fidelity rule

The first manuscript pass should reproduce the original technical content faithfully. Modernization, rewriting, commentary, or retrospective interpretation should be kept separate from the primary transcription unless explicitly decided later.

## Proposed processing pipeline

```text
scan PDF
  → page images
  → image preprocessing
  → OCR / code extraction
  → structured Markdown
  → visual fidelity review
  → VTR Press validation
```

## First validation sample

Before processing the entire report, capture a representative sample containing:

- title / front matter
- normal prose
- headings and subheadings
- at least one table
- at least one figure or diagram
- at least one Watcom C listing
- references

The sample will be used to validate the tooling and manuscript conventions.
