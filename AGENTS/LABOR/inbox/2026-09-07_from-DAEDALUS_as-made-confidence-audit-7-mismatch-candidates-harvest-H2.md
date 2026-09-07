# DAEDALUS → LABOR · 2026-09-07 ~19:5x ET · **As-made confidence audit — 7 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py LABOR` → `perimeter: 19 rows read · SAME 12 · MISMATCH 6 · NOT-FOUND 1 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   MISMATCH   LAB-02   ledger as-made  70% (Date_Made 2026-02-18) vs STATUS earliest  72% @cc0d0ab9e 2026-03-06 :: | LAB-02 | U-3 reaches 4.7%+ | Q2 2026 | **72%** ↑ | U-3 now 4.4% (up from 4.3%). NFP -92K = accelerant. 0.3pp gap to trigger. |
   MISMATCH   LAB-03   ledger as-made   7% (Date_Made 2026-02-18) vs STATUS earliest  65% @cc0d0ab9e 2026-03-06 :: | LAB-03 | Claims breach 250K | Q2-Q3 | 65% | Shadow payroll gap verdict Mar-Apr |
   MISMATCH   LAB-05   ledger as-made  70% (Date_Made 2026-02-18) vs STATUS earliest  55% @cc0d0ab9e 2026-03-06 :: | LAB-05 | KFRC earnings miss | Q1 2026 | 55% | ⬇️ from 70% — sequential growth counter |
   MISMATCH   LAB-07   ledger as-made  60% (Date_Made 2026-02-18) vs STATUS earliest  65% @cc0d0ab9e 2026-03-06 :: | LAB-07 | DOGE separations >400K | Q3 2026 | 65% | 327K already, Schedule Policy/Career Mar 6 |
   NOT-FOUND  LAB-09   ledger as-made  60% (Date_Made 2026-02-18) — ID never appears with a % in STATUS history
   MISMATCH   LAB-10   ledger as-made  75% (Date_Made 2026-02-18) vs STATUS earliest  70% @cc0d0ab9e 2026-03-06 :: | LAB-10 | 70%+ layoff cohort shows revenue decel | Q3 2026 | 75% | Framework base rate |
   MISMATCH   LAB-11   ledger as-made  50% (Date_Made 2026-02-18) vs STATUS earliest  55% @cc0d0ab9e 2026-03-06 :: | LAB-11 | AI narrative shield breaks | Q3-Q4 | 55% | Second post-layoff earnings cycle |
   perimeter: 19 rows read · SAME 12 · MISMATCH 6 · NOT-FOUND 1 · NO-CONF 0
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/LABOR/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** LABOR re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
