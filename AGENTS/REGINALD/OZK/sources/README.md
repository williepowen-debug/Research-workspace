# OZK — Sources

Primary-source extracts only. This is the evidence locker for data pulled directly from regulatory filings, FDIC/FFIEC APIs, and official OZK 10-K/10-Q text.

**Raw LLM research outputs live in `../raw/llm_outputs/`** (moved Apr 23 restructure Phase 2). **Raw PDFs live in `../raw/`.**

---

## What belongs here

- 10-K / 10-Q section extracts (e.g. `10K_Q4_2025_EXTRACT.md`)
- FDIC API pulls (`FDIC_API_CALL_REPORT_DATA.md`)
- FDIC Quarterly Banking Profile extracts (`FDIC_QBP_Q4_2025.md`, `FDIC_QBP_Q4_GEOGRAPHIC_ANALYSIS.md`)
- FFIEC Call Report raw CSVs (`FFIEC_CALL_REPORT_Q4_2025_RAW.csv`, `FFIEC_RC-R_Q4_2025.csv`)
- Broker / position snapshots (`FORGE_TRADE_STATUS.md`)
- Insider filing scans (`INSIDER_SCAN_OZK.md`)

## What does NOT belong here

- Raw LLM research outputs → `../raw/llm_outputs/`
- Raw OZK PDFs (Mgmt Comments, Financial Supplement, transcript) → `../raw/`
- Quarterly Mgmt Comments extracts for multi-quarter trajectory analysis → `../historical/`
- Dead audit/restructure artifacts → `../archive/`

## Rules

- **Never edit source files after creation.** They're the record of what we received.
- If a source is wrong or superseded, note the correction in `../workbook/KB.tsv` — don't alter the original.

## Relationship to KB

Key facts get extracted into `../workbook/KB.tsv` as individual rows with `[KB-OZK-NNN]` IDs and citations pointing back here. Sources are the raw material; KB is the refined product.

---

*KB → `../workbook/KB.tsv` | Analysis → `../research/` | Thesis → `../THESIS.md` | Raw LLM outputs → `../raw/llm_outputs/` | Raw PDFs → `../raw/`*
