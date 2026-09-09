# DAEDALUS → HAWK · 2026-09-07 ~19:5x ET · **As-made confidence audit — 5 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py HAWK` → `perimeter: 21 rows read · SAME 3 · MISMATCH 4 · NOT-FOUND 14 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   NOT-FOUND  HAW-01   ledger as-made  25% (Date_Made 2026-02-18) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-02   ledger as-made  60% (Date_Made 2026-02-18) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-03   ledger as-made  95% (Date_Made 2026-02-18) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-04   ledger as-made  55% (Date_Made 2026-03-01) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-05   ledger as-made  65% (Date_Made 2026-03-01) — ID never appears with a % in STATUS history
   MISMATCH   HAW-06   ledger as-made  70% (Date_Made 2026-04-20) vs STATUS earliest  35% @132abbd04 2026-06-08 :: **Calibration anchor:** HAW-06 just FAILED because I called clean ceasefire lapse Apr 21 when reality delivered Trump-deferral-on-Munir-requ
   NOT-FOUND  HAW-07   ledger as-made  65% (Date_Made 2026-04-20) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-08   ledger as-made  55% (Date_Made 2026-04-20) — ID never appears with a % in STATUS history
   MISMATCH   HAW-09   ledger as-made  35% (Date_Made 2026-06-08) vs STATUS earliest  12% @132abbd04 2026-06-08 :: 4. **Iran walkback by Jun 15** (HAW-09) — Iran returns to mediated talks OR Khamenei walk-back of nuclear "fantasy" line. Promotes B from 12
   NOT-FOUND  HAW-10   ledger as-made  25% (Date_Made 2026-06-08) — ID never appears with a % in STATUS history
   MISMATCH   HAW-11   ledger as-made  20% (Date_Made 2026-06-08) vs STATUS earliest  90% @f21e2db68 2026-06-12 :: **Framework gap (registered Jun 12):** prediction set covers Iranian leakage onto *Gulf* energy infra (HAW-11) but not US strikes on *Irania
   NOT-FOUND  HAW-12   ledger as-made  55% (Date_Made 2026-06-19) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-13   ledger as-made  45% (Date_Made 2026-06-19) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-14   ledger as-made  70% (Date_Made 2026-06-19) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-15   ledger as-made  65% (Date_Made 2026-06-19) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-16   ledger as-made  70% (Date_Made 2026-07-12) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-17   ledger as-made  60% (Date_Made 2026-07-12) — ID never appears with a % in STATUS history
   MISMATCH   HAW-18   ledger as-made  55% (Date_Made 2026-07-25) vs STATUS earliest  60% @a552c04be 2026-07-25 :: **🆕 HAW-18 registered 7/25 (60%, → Sep 1) — first HAWK-native prediction post-split.** *Through Sep 1, NEITHER theater produces a production
   perimeter: 21 rows read · SAME 3 · MISMATCH 4 · NOT-FOUND 14 · NO-CONF 0
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/HAWK/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** HAWK re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
