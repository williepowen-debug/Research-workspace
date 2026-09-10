# DAEDALUS → SAM · 2026-09-07 ~19:5x ET · **As-made confidence audit — 16 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py SAM` → `perimeter: 34 rows read · SAME 8 · MISMATCH 15 · NOT-FOUND 11 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   MISMATCH   SAM-28   ledger as-made  40% (Date_Made 2026-06-22) vs STATUS earliest   2% @cf2b9479c 2026-07-02 :: **(3) NFP June +57K vs 113K consensus** (revisions **−74K**; U-3 4.2% = participation artifact, 61.5%; AHE +3.5% YoY; Challenger 45.8K cooli
   MISMATCH   SAM-29   ledger as-made  65% (Date_Made 2026-06-22) vs STATUS earliest  85% @a0ce790b1 2026-06-29 :: - **CFTC −146,104 / 81.2% (Jun-23): FIRST COVER off the 83.4% top** (+4,028 WoW; longs −3,677, shorts −7,705; OI 520,825→431,030). Still dee
   MISMATCH   SAM-30   ledger as-made  30% (Date_Made 2026-06-22) vs STATUS earliest  85% @a0ce790b1 2026-06-29 :: - **CFTC −146,104 / 81.2% (Jun-23): FIRST COVER off the 83.4% top** (+4,028 WoW; longs −3,677, shorts −7,705; OI 520,825→431,030). Still dee
   MISMATCH   SAM-31   ledger as-made  35% (Date_Made 2026-06-22) vs STATUS earliest   2% @cf2b9479c 2026-07-02 :: **(3) NFP June +57K vs 113K consensus** (revisions **−74K**; U-3 4.2% = participation artifact, 61.5%; AHE +3.5% YoY; Challenger 45.8K cooli
   MISMATCH   SAM-38   ledger as-made  55% (Date_Made 2026-07-29) vs STATUS earliest  85% @f27fc1961 2026-07-31 :: **BRANCH C FIRED (the ~55% modal call) — SAM-38 RESOLVED CONFIRMED; SAM-34 RESOLVED CONFIRMED (hold @85%).** Primary sources: statement `k26
   MISMATCH   SAM-24   ledger as-made  85% (Date_Made 2026-05-12) vs STATUS earliest  72% @ee4479afb 2026-06-16 :: **Predictions resolved (see PREDICTIONS.tsv):** SAM-21 (June hike) ✅ **CONFIRMED** · SAM-24 (25bp not 50bp) ✅ **CONFIRMED** · SAM-23 (MOF in
   MISMATCH   SAM-26   ledger as-made  70% (Date_Made 2026-05-21) vs STATUS earliest   4% @3b493ea00 2026-05-26 :: 3. **JGB 30Y back below 4.0% (3.931%, -7bp).** Driver: oil collapse + dovish CPI, NOT BOJ super-long operation or insurer return. **SAM-26 (
   MISMATCH   SAM-25   ledger as-made  40% (Date_Made 2026-05-21) vs STATUS earliest 200% @3851059ee 2026-05-26 :: **SAM-25 (any Big 3 <200% @40%) — TECHNICALLY TRUE on Nippon 195% but FAILED IN SPIRIT.** Exact threshold-vs-mechanism trap logged in MEMORY
   MISMATCH   SAM-32   ledger as-made  72% (Date_Made 2026-06-30) vs STATUS earliest  85% @27ab67130 2026-07-01 :: **Forward catalysts** (full docket → `docket/CALENDAR.md`): Thu Jul 2 JGB 10Y auction · Fri Jul 3 CFTC (Jun-30 data) · **Jul 7 JGB 30Y / Jul
   MISMATCH   SAM-08   ledger as-made  85% (Date_Made 2026-02-15) vs STATUS earliest  70% @bc7bdb1f1 2026-05-31 :: - **Why 70%, not 88%:** earned discount — failed TWICE being too-hawkish on the Takaichi 0.75% ceiling (SAM-08, SAM-20), which remains live;
   NOT-FOUND  SAM-14   ledger as-made  60% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-15   ledger as-made  80% (Date_Made 2026-03-20) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-17   ledger as-made  65% (Date_Made 2026-04-13) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-18   ledger as-made  55% (Date_Made 2026-04-13) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-19   ledger as-made  75% (Date_Made 2026-04-13) — ID never appears with a % in STATUS history
   MISMATCH   SAM-20   ledger as-made  60% (Date_Made 2026-04-13) vs STATUS earliest  70% @bc7bdb1f1 2026-05-31 :: - **Why 70%, not 88%:** earned discount — failed TWICE being too-hawkish on the Takaichi 0.75% ceiling (SAM-08, SAM-20), which remains live;
   MISMATCH   SAM-22   ledger as-made  65% (Date_Made 2026-04-24) vs STATUS earliest  25% @2d8659eb5 2026-08-07 :: **Calibration note:** this is the third member of the over-confidence cluster (SAM-08 @90%, SAM-20 @60%) — **but in the opposite direction**
   NOT-FOUND  SAM-04   ledger as-made  60% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-05   ledger as-made  70% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-06   ledger as-made  75% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-07   ledger as-made  48% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-13   ledger as-made  55% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-16   ledger as-made  70% (Date_Made 2026-04-13) — ID never appears with a % in STATUS history
   MISMATCH   SAM-27   ledger as-made  75% (Date_Made 2026-05-21) vs STATUS earliest  74% @3b493ea00 2026-05-26 :: 1. **April CPI DOVISH MISS (May 22).** Core 1.4% vs 1.7% consensus / 1.8% prior — 30bp undershoot, 3rd month below 2% target. Core-core 1.9%
   MISMATCH   SAM-36   ledger as-made  50% (Date_Made 2026-07-10) vs STATUS earliest  85% @a749cb999 2026-07-11 :: **Live anchor state (trued-up Sat 7/11; newest print = Jul-7 data [rel Fri 7/10 3:30 PM ET]):** CFTC **−123,778 = 68.8% of cycle peak** (COV
   MISMATCH   SAM-37   ledger as-made  55% (Date_Made 2026-07-17) vs STATUS earliest  85% @e16b5466f 2026-07-17 :: **Pre-registered SAM-37 verdict map** (graded mechanically at Phase 2 vs the frozen lines): base −123,778/68.8%; **RE-FIRE ≤−153K/85% [SAM-3
   perimeter: 34 rows read · SAME 8 · MISMATCH 15 · NOT-FOUND 11 · NO-CONF 0
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/SAM/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** SAM re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
