# CodexWriter — Export

> **Role:** Optional Extension — Phase 5
> **Type:** Publisher / Builder
> **Position:** Phase 5 of the 5-phase pipeline, after Gate 5 approval. Converts the finalized manuscript into publishable output formats.

---

## Purpose

Export takes the finalized manuscript and produces output in publishable formats. The default format is a formatted Markdown manuscript. Additional formats (DOCX, PDF, ePub) are extension capabilities.

Export is the final step in the pipeline. Once the manuscript is exported, the creative work is complete. The author may continue to revise, but the exported version is the snapshot that was approved at Gate 5.

---

## Inputs

- **Finalized manuscript:** All chapter drafts, approved after prose editing and reader simulation.
- **Story state:** For metadata (title, author, project ID, book ID).
- **Templates:** For output formatting, if applicable.
- **Export configuration:** Target format(s), styling preferences, metadata.

---

## Outputs

- **Mark다운 manuscript:** A compiled Markdown file with all chapters in order, plus front matter (title, author, table of contents).
- **DOCX (extension):** A formatted Word document, if the DOCX export capability is implemented.
- **PDF (extension):** A formatted PDF, if the PDF export capability is implemented.
- **ePub (extension):** An ePub file, if the ePub export capability is implemented.

---

## Workflow

### Step 1: Verify Manuscript Readiness

Check that:
- All chapters are drafted and approved.
- Continuity is clean (no open critical or high findings).
- Reader simulation has been completed.
- The author has approved Gate 5.

If any of these are not true, flag the issue and do not proceed.

### Step 2: Compile the Manuscript

Assemble all chapters in canonical order:

- Read each chapter's draft from the project directory.
- Concatenate in sequence order.
- Add front matter: title, author, project ID, word count, generation date.
- Add a table of contents (chapter titles and sequence numbers).

The Markdown manuscript is the default output. It should be clean, readable, and ready for further formatting if needed.

### Step 3: Apply Formatting (if applicable)

If the export includes formatted output (DOCX, PDF, ePub):

- Apply the project's style preferences (font, spacing, chapter headings, scene breaks).
- Generate the formatted file.
- Verify the output is readable and correctly formatted.

### Step 4: Generate Metadata

Include metadata in the export:
- Title
- Author
- Project ID / Book ID
- Word count
- Generation date
- Version (e.g., "Alpha Export 1")

### Step 5: Deliver the Export

Report completion to the orchestrator with:
- What formats were produced
- File paths
- Word count
- Any formatting notes or issues

---

## Error Handling

| Error | Response |
|---|---|
| Manuscript not ready | "Export requires all chapters to be drafted, approved, continuity-clean, and reader-simulated. Here is the current status: [status]. Do you want to proceed anyway, or complete the remaining steps first?" |
| Gate 5 not approved | "Export requires Gate 5 approval. The author must approve the final manuscript before export can proceed." |
| Format not implemented | "The requested format ([format]) is not yet implemented. The Markdown manuscript is available. Do you want to use that, or implement the requested format first?" |

---

## Portability

- Markdown output is universal — any host can compile it.
- DOCX, PDF, and ePub generation require additional tooling (python-docx, weasyprint, ePub libraries). These are extensions, not core functionality.
- The export skill is designed to be the last step in the pipeline, after all creative work is complete.

---

## File Outputs

- `export/manuscript.md` — compiled Markdown manuscript.
- `export/manuscript.docx` (if implemented)
- `export/manuscript.pdf` (if implemented)
- `export/manuscript.epub` (if implemented)

---

## Evaluation

An export implementation is successful when:

1. It compiles all chapters in correct order with front matter.
2. The Markdown manuscript is clean and readable.
3. Formatted outputs (if implemented) are correctly formatted and readable.
4. It verifies manuscript readiness before exporting.
5. It produces a snapshot that matches what the author approved at Gate 5.
