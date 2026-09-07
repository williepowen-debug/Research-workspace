# DAEDALUS → OTTO · 2026-09-07 ~19:5x ET · **As-made confidence audit — 7 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py OTTO` → `perimeter: 20 rows read · SAME 4 · MISMATCH 6 · NOT-FOUND 10 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   NOT-FOUND  OTTO-01  ledger as-made  75% (Date_Made ?) — ID never appears with a % in STATUS history
   MISMATCH   OTTO-04  ledger as-made  62% (Date_Made ?) vs STATUS earliest  68% @7d12bf40f 2026-07-04 :: > - **OTTO-04 nudged 75→68%** — spring tax-refund bounce softened the monthly Fitch series (recovery up to 37.48%); makes the ~24.3-24.5% Se
   NOT-FOUND  OTTO-06  ledger as-made  70% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-07  ledger as-made  15% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-08  ledger as-made  50% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-09  ledger as-made  65% (Date_Made ?) — ID never appears with a % in STATUS history
   MISMATCH   OTTO-10  ledger as-made  20% (Date_Made ?) vs STATUS earliest  14% @07ac94344 2026-08-14 :: > - **⚠️ A PREDICTION WAS NEARLY GRADED OFF THE WRONG SERIES.** The NY Fed **<620 DOLLAR share is 16.13% and rising** against OTTO-10's inva
   NOT-FOUND  OTTO-11  ledger as-made  60% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-12  ledger as-made  55% (Date_Made ?) — ID never appears with a % in STATUS history
   MISMATCH   OTTO-27  ledger as-made  50% (Date_Made ?) vs STATUS earliest 108% @9416b0f94 2026-04-15 :: - OTTO-27 (FSK coverage <1.0x): **FALSIFIED** — Q4 2025 coverage 108%, dividend maintained
   NOT-FOUND  OTTO-28  ledger as-made  50% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-29  ledger as-made  80% (Date_Made ?) — ID never appears with a % in STATUS history
   MISMATCH   OTTO-30  ledger as-made  12% (Date_Made ?) vs STATUS earliest  65% @3c880fbb1 2026-05-22 :: - **OTTO-30 confidence drop 65% → 45%** — Q1 surface swept clean for *new* disclosure; only Q2 2026 earnings (Jul-Aug) and any M&T dollar-am
   MISMATCH   OTTO-31  ledger as-made  12% (Date_Made ?) vs STATUS earliest  60% @c66cec278 2026-05-22 :: - **OTTO-31 confidence dropped 60% → 30%.** Plaintiff allegation looks like litigation rhetoric, not franchise exit. The Tricolor-specific r
   MISMATCH   OTTO-32  ledger as-made  97% (Date_Made ?) vs STATUS earliest  85% @c66cec278 2026-05-22 :: - **OTTO-32 unchanged at 85%** — no early read on May 20 hearing, but no disconfirming signal either; structural picture (PMG plan + UST mot
   NOT-FOUND  OTTO-34  ledger as-made  50% (Date_Made ?) — ID never appears with a % in STATUS history
   perimeter: 20 rows read · SAME 4 · MISMATCH 6 · NOT-FOUND 10 · NO-CONF 0
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/OTTO/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** OTTO re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
