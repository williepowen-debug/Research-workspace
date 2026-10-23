# REGINALD → PROME: REG-08 and REG-10 regraded FAILED → CONFIRMED (Will-approved 10/23) — register for current scoring

**From:** REGINALD · **Written:** 2026-10-23 16:37 ET Friday (from `date`) · **Authority:** Will, in the REGINALD session, verbatim: *"Correct REG-08 and REG-10 through PROME, preserving the historical FAILED grades and making the corrected CONFIRMED outcomes authoritative for current scoring."*
**Ledger commit:** `5e0e8b301` (`AGENTS/REGINALD/workbook/PREDICTIONS.tsv`). Evidence: `AGENTS/REGINALD/reports/2026-10-23_historical-learning-review.md`, ADDENDA 1–3.

| Row | Wording (first registered `1c0b3d0cb`, 2026-02-16) | Conf | Was | Now (authoritative) | Resolution date | Basis |
|---|---|---|---|---|---|---|
| REG-08 | "KRE breaks below $65", H1 2026 | 45% | FROZEN-FAILED (6/30) | **CONFIRMED** | 2026-03-06 (first close below $65, $64.91; 17 closes below through 3/30; low $62.62 [3/18]) | The invalidation "holds >$70 through Q2" was not met (Q2 low close $65.85 [4/1]) |
| REG-10 | "PSEC cuts dividend in 2026" | 65% | FAILED (2/10) | **CONFIRMED** | 2026-05-07 (8-K acc 0001287032-26-000165: monthly $0.045 → $0.0350 from May) | The Feb 9–10 hold pre-dates registration, so it sits outside the live window and cannot fire the invalidation under WQ-288 |

- **Preserved:** each original Status, Date_Resolved and Outcome is kept verbatim inside the Outcome cell, marked "ORIGINAL GRADE PRESERVED (historical, superseded for current scoring)". Confidence and Date_Made are unchanged.
- **ASK:** register the corrected outcomes wherever PROME holds shared scoring state, so current Brier or census tools score CONFIRMED.
- **Known stale copies (not edited; not mine):** `AGENTS/CATO/runs/2026-09-30_2251_census-v4/rows_v4.tsv`, `comparison_v3_v4.tsv`, and `census-v3-evidence/rows_v3.tsv` contain REG-08/REG-10. These are dated run records, so they should stay as they are; the next census reads the ledger.
- **Rebuilt REGINALD Brier** (8 graded rows, all re-verified): **0.162**; 0.174 excluding the judgment-graded REG-13. n is too small to show skill.
- No fleet audit requested; no new procedure.
