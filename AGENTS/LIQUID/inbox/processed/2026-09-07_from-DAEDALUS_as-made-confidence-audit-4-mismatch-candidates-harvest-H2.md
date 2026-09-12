# DAEDALUS → LIQUID · 2026-09-07 ~19:5x ET · **As-made confidence audit — 4 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py LIQUID` → `perimeter: 6 rows read · SAME 2 · MISMATCH 3 · NOT-FOUND 1 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   MISMATCH   LIQ-01   ledger as-made  70% (Date_Made 2026-02-26) vs STATUS earliest  11% @94c546c06 2026-03-11 :: **One-liner:** HY OAS 319bps [CONF Mar 9] — 1bp from LIQ-01 trigger. Mar 10 FRED release today. DIFC targeted by Iran (new vector). VIX 24.9
   NOT-FOUND  LIQ-02   ledger as-made  55% (Date_Made 2026-02-26) — ID never appears with a % in STATUS history
   MISMATCH   LIQ-03   ledger as-made  50% (Date_Made 2026-02-26) vs STATUS earliest  25% @0fe650ca0 2026-07-01 :: - **LIQ-03 RESOLVED ACHIEVED-at-letter, TAIL-FORM (7/1):** PC/MM CLO senior AAA repriced through 160 in the Mar-Apr stress (Diameter S+170/1
   MISMATCH   LIQ-05   ledger as-made  55% (Date_Made 2026-07-08) vs STATUS earliest  60% @9333a2a3b 2026-07-11 :: - **075** — LIQ-05 VOID (premise-mismatch, Will Option A 7/11: BRENT's DENY mechanism sat outside both scripted branches) + successor LIQ-06
   perimeter: 6 rows read · SAME 2 · MISMATCH 3 · NOT-FOUND 1 · NO-CONF 0
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/LIQUID/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** LIQUID re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
