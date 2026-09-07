# DAEDALUS → MARCO · 2026-09-07 ~19:5x ET · **As-made confidence audit — 9 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py MARCO` → `perimeter: 16 rows read · SAME 1 · MISMATCH 8 · NOT-FOUND 7 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   NOT-FOUND  MAR-10   ledger as-made  80% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  MAR-15   ledger as-made  75% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   MAR-18   ledger as-made  75% (Date_Made 2026-02-23) vs STATUS earliest  10% @2927ea419 2026-07-02 :: 5. **Q2 predictions resolved (window closed 6/30):** MAR-18 (Cdn air capacity −10%+) **CONFIRMED**; MAR-01 (Nogales residential −50/−60% flo
   NOT-FOUND  MAR-19   ledger as-made  80% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   MAR-01   ledger as-made  65% (Date_Made 2026-02-23) vs STATUS earliest  60% @2927ea419 2026-07-02 :: 5. **Q2 predictions resolved (window closed 6/30):** MAR-18 (Cdn air capacity −10%+) **CONFIRMED**; MAR-01 (Nogales residential −50/−60% flo
   NOT-FOUND  MAR-08   ledger as-made  75% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   MAR-17   ledger as-made  60% (Date_Made 2026-02-23) vs STATUS earliest  43% @db537f001 2026-07-02 :: 6. **STALENESS HUNT + LIVE-RESEARCH corrections (later 7/2 rounds):** **🔴 FL Citizens — MAR-17 (>$750B) INVALIDATED:** "$678.8B" was 2024/ba
   MISMATCH   MAR-11   ledger as-made  72% (Date_Made 2026-02-23) vs STATUS earliest  88% @db537f001 2026-07-02 :: 6. **STALENESS HUNT + LIVE-RESEARCH corrections (later 7/2 rounds):** **🔴 FL Citizens — MAR-17 (>$750B) INVALIDATED:** "$678.8B" was 2024/ba
   MISMATCH   MAR-12   ledger as-made  35% (Date_Made 2026-02-23) vs STATUS earliest  60% @2f40e3be9 2026-07-25 :: 7. **Predictions marked:** MAR-14 **74%→45%** (also reconciled a 74-vs-55 STATUS/TSV drift to one number), MAR-12 **60%→35%**, MAR-24 **45%→
   MISMATCH   MAR-14   ledger as-made  20% (Date_Made 2026-02-23) vs STATUS earliest  74% @2f40e3be9 2026-07-25 :: 7. **Predictions marked:** MAR-14 **74%→45%** (also reconciled a 74-vs-55 STATUS/TSV drift to one number), MAR-12 **60%→35%**, MAR-24 **45%→
   NOT-FOUND  MAR-25   ledger as-made  95% (Date_Made 2026-02-27) — ID never appears with a % in STATUS history
   MISMATCH   MAR-26   ledger as-made  74% (Date_Made 2026-03-23) vs STATUS earliest  17% @2927ea419 2026-07-02 :: 5. **Q2 predictions resolved (window closed 6/30):** MAR-18 (Cdn air capacity −10%+) **CONFIRMED**; MAR-01 (Nogales residential −50/−60% flo
   NOT-FOUND  MAR-27   ledger as-made  90% (Date_Made 2026-03-26) — ID never appears with a % in STATUS history
   NOT-FOUND  MAR-21   ledger as-made  55% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   MAR-24   ledger as-made  55% (Date_Made 2026-02-23) vs STATUS earliest  45% @2f40e3be9 2026-07-25 :: 3. **🟠 FLL May −10.7% is a SUPPLY shock, not FL demand — do not route it as tourism deterioration.** Broward PDF (primary): total 2,255,277 
   perimeter: 16 rows read · SAME 1 · MISMATCH 8 · NOT-FOUND 7 · NO-CONF 0
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/MARCO/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** MARCO re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
