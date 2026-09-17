# Digitization Scripts

This directory will contain reproducible tooling for converting the scanned college project report into structured manuscript material.

Planned components:

- `pdf_to_pages.py` — render source PDF pages to images
- `preprocess.py` — image cleanup / deskew / contrast preparation
- `ocr.py` — OCR text extraction
- `extract_images.py` — identify or extract figures where practical
- `assemble.py` — assemble reviewed material into manuscript structures
- `validate.py` — basic manuscript checks before handing to VTR Press

The actual implementation will be chosen after testing a representative scan. Avoid over-engineering the pipeline before the source pages are available.
