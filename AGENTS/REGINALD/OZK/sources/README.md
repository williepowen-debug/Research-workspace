# OZK — Sources

Raw inputs from external research, primary filings, and multi-LLM research runs. This is the evidence locker — nothing here should be edited after creation.

---

## File Instructions

**What belongs here:**
- Primary data extracts (FDIC API, FFIEC Call Reports, 10-K sections)
- Multi-LLM research outputs (V1–V4 pattern: same prompt run through 4 models)
- External thesis documents (Temple 8, etc.)
- Raw CSV/data pulls

**Naming convention:**
- Primary data: `[SOURCE]_[DESCRIPTION].md` (e.g. `FDIC_API_CALL_REPORT_DATA.md`)
- Multi-LLM runs: `OZK_[TOPIC]_V[1-4].md` (e.g. `OZK_GFC_TRACK_RECORD_V3.md`)
- External research: `[AUTHOR/PLATFORM]_[TOPIC].md`

**Rules:**
- **Never edit source files after creation.** They're the record of what we received. If a source is wrong, note the correction in KB.tsv or THESIS.md — don't alter the original.
- **V1–V4 files** are the same prompt sent to four different LLMs. Cross-model convergence = high confidence. Unique findings from one model = flag for verification.
- **.docx files** exist because some LLM outputs came in that format. Keep as-is.

**Relationship to KB.tsv:** Key facts get extracted from sources into KB.tsv as individual rows with `[KB-OZK-NNN]` IDs and source citations pointing back here. Sources are the raw material; KB is the refined product.

---

## Source Categories

**Primary filings:** 10K extract, FDIC API data, FFIEC Call Report (CSV), RC-R capital data, QBP geographic analysis
**Multi-LLM research:** NDFI deep research (4 models), GFC track record (4 models), construction maturity (3 models), interest reserve model (4 models)
**External:** Temple 8 short thesis, IQHQ RaDD research, insider scan, FORGE trade status

---

*KB → `../workbook/KB.tsv` | Research (our analysis) → `../research/` | Thesis → `../THESIS.md`*
