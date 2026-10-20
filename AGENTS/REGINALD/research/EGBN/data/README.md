# EGBN data extracts

**Snapshot captured October20,2026.** Original row dates and source conventions are preserved. These files are extracts of existing desk data, not newly fetched bank or market observations.

- `workbook/`: EGBN-referencing rows from16 shared REGINALD tables, including six EGBN workout rows, cohort histories, knowledge-base entries, predictions, vectors and historical market activity. A row can mention multiple banks; retaining it does not make all its values EGBN-only. Whole rows, headers and source preambles are preserved.
- `market-technicals/`: EGBN rows from six dated market CSVs. Old prices, options and positioning are historical observations, not current quotes or broker positions.
- The original shared ledgers remain authoritative. Every source path, source hash, selected row count and copied-file hash is recorded in [INVENTORY.json](../INVENTORY.json). TSV selections also record original line numbers.
- Frozen prediction rows have been copied without alteration; this does not reopen, regrade or change them. Historical cohort files retain their own definitions and vintages.

Run `.venv/bin/python3 AGENTS/REGINALD/research/EGBN/verify_inventory.py` from the repository root to verify the snapshot and detect changes in originals. No automatic refresh is installed.
