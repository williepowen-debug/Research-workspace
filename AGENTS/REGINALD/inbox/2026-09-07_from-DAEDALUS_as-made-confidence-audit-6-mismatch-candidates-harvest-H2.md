# DAEDALUS → REGINALD · 2026-09-07 ~19:5x ET · **As-made confidence audit — 6 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py REGINALD` → `perimeter: 20 rows read · SAME 3 · MISMATCH 5 · NOT-FOUND 12 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   MISMATCH   REG-02   ledger as-made  65% (Date_Made 2026-02-23) vs STATUS earliest  60% @cc0d0ab9e 2026-03-06 :: | REG-02 | FHLB advances spike >$600B | Q2-Q3 2026 | 60% |
   MISMATCH   REG-03   ledger as-made  70% (Date_Made 2026-02-23) vs STATUS earliest  50% @cc0d0ab9e 2026-03-06 :: | REG-03 | At least one Tier 1 bank capital raise | H2 2026 | 50% |
   MISMATCH   REG-04   ledger as-made  60% (Date_Made 2026-02-23) vs STATUS earliest  65% @cc0d0ab9e 2026-03-06 :: | REG-04 | Chicago pattern replicates in Phoenix | H1 2026 | 65% |
   NOT-FOUND  REG-05   ledger as-made  40% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-06   ledger as-made  10% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-07   ledger as-made  68% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-08   ledger as-made  45% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   REG-09   ledger as-made  50% (Date_Made 2026-02-23) vs STATUS earliest  20% @f69ff2963 2026-08-13 :: **🟠 8/13 THU 3RD PASS — WILL-RULED SLATE EXECUTED, 5 items. ★ THE UP-CAP HYPOTHESIS I OPENED THIS MORNING IS RETIRED, NOT SUPPORTED — 0 of 1
   NOT-FOUND  REG-10   ledger as-made  65% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-11   ledger as-made  55% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-12   ledger as-made  60% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-13   ledger as-made  72% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-14   ledger as-made  50% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-15   ledger as-made  60% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   REG-17   ledger as-made  50% (Date_Made 2026-02-23) vs STATUS earliest  20% @f69ff2963 2026-08-13 :: **🟠 8/13 THU 3RD PASS — WILL-RULED SLATE EXECUTED, 5 items. ★ THE UP-CAP HYPOTHESIS I OPENED THIS MORNING IS RETIRED, NOT SUPPORTED — 0 of 1
   NOT-FOUND  REG-18   ledger as-made  45% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-19   ledger as-made  70% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   perimeter: 20 rows read · SAME 3 · MISMATCH 5 · NOT-FOUND 12 · NO-CONF 0
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/REGINALD/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** REGINALD re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
