# OZK — Historical

Primary-source extracts from OZK quarterly Management Comments PDFs. **Live reference data** — actively used for multi-quarter trajectory analysis (e.g., `research/threads/RESG_MIX_DETERIORATION.md` 6Q view).

---

## File Instructions

**What belongs here:**
- Per-quarter extracts from OZK Management Comments PDFs (one file per quarter)
- Naming: `Q<N>_<YY>_extract.md` (e.g., `Q1_25_extract.md`)
- Each extract distills the PDF into a consistent section structure: RESG portfolio detail, credit quality, reserves/ACL, NIM, CIB verticals, capital, mgmt commentary verbatim
- Source PDF path in the first line so we can re-run extracts if methodology changes

**What does NOT belong here:**
- Completed audits / executed plans → `../archive/`
- Research analyses (e.g., RESG migration math) → `../research/` or `../research/threads/`
- Raw PDFs themselves → `../raw/`
- Current-quarter extract-in-progress → top level until the analysis is published

**Rule:** Append, don't rewrite. Each quarter's extract is frozen once created — new prints get new files. If the extraction methodology changes, annotate the change in a separate file rather than backfilling.

---

## Current Contents (as of 2026-04-23)

| File | Period | Source |
|------|--------|--------|
| `Q4_24_extract.md` | Q4 2024 (quarter ending 12/31/2024) | Q4_2024_mgmt_comments.pdf |
| `Q1_25_extract.md` | Q1 2025 | Q1_2025_mgmt_comments.pdf |
| `Q2_25_extract.md` | Q2 2025 | Q2_2025_mgmt_comments.pdf |
| `Q3_25_extract.md` | Q3 2025 | Q3_2025_mgmt_comments.pdf |
| `Q4_25_extract.md` | Q4 2025 | Q4_2025_mgmt_comments.pdf |

**Next expected additions:** `Q1_26_extract.md` — the Apr 22 Management Comments PDF is currently in `../raw/`; extract when Q2 26 starts becoming relevant for trajectory work.

---

*This directory feeds multi-quarter analyses. Keep the schema consistent across files so downstream consumers (RESG_MIX_DETERIORATION, future trajectory work) can diff cleanly quarter-over-quarter.*
