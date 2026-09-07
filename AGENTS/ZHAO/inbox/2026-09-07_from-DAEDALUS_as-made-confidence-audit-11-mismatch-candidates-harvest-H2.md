# DAEDALUS → ZHAO · 2026-09-07 ~19:5x ET · **As-made confidence audit — 11 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py ZHAO` → `perimeter: 17 rows read · SAME 8 · MISMATCH 9 · NOT-FOUND 0 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   MISMATCH   ZHA-01   ledger as-made  18% (Date_Made 2026-03-03) vs STATUS earliest  70% @0d0ead00a 2026-03-09 :: | ZHA-01 | USD/CNY breaks 7.30 | 70% → **55%** ↓ | ~~2-4 weeks~~ 6-10 weeks | OPEN | DXY <100 sustained 10 sessions + PBOC stops gold buys |
   MISMATCH   ZHA-03   ledger as-made  25% (Date_Made 2026-03-06) vs STATUS earliest  65% @0d0ead00a 2026-03-09 :: | ZHA-03 | Belgium TIC >$500B | 65% | Q1-Q2 2026 | OPEN | Growth decelerates <15% YoY for 2 prints |
   MISMATCH   ZHA-04   ledger as-made  42% (Date_Made 2026-03-06) vs STATUS earliest  65% @0d0ead00a 2026-03-09 :: | ZHA-04 | China official <$650B | 65% | Q2-Q3 2026 | OPEN | NFP relief → may slip to Q3. Watch DXY. |
   MISMATCH   ZHA-06   ledger as-made  72% (Date_Made 2026-03-06) vs STATUS earliest  60% @0d0ead00a 2026-03-09 :: | ZHA-06 | >250 small banks consolidated in 2026 | 60% | 2026 | OPEN | Policy reversal on mergers |
   MISMATCH   ZHA-10   ledger as-made  40% (Date_Made 2026-03-09) vs STATUS earliest  45% @77f56870c 2026-03-22 :: | ZHA-10 | Yuan oil settlement via Hormuz >$5B cumulative | 45% | Q3 2026 | OPEN | Ceasefire reopens Hormuz to all traffic → yuan channel co
   MISMATCH   ZHA-11   ledger as-made  68% (Date_Made 2026-07-09) vs STATUS earliest  65% @c4c0bc33a 2026-07-09 :: | ZHA-11 | China NOT the 30Y 7/9 indirect-bid (77.74%) driver | 65% | OPEN — pre-registered 7/9, indirect test only (TIC has no maturity bre
   MISMATCH   ZHA-12   ledger as-made  80% (Date_Made 2026-07-16) vs STATUS earliest   4% @adeac0f72 2026-07-16 :: **(a) BoK branch — DECISION ALREADY PRINTED, this is now integration + a forward falsifiable consequence (ZHA-12, KB-ZHAO-093/094).** BoK hi
   MISMATCH   ZHA-15   ledger as-made  18% (Date_Made 2026-07-16) vs STATUS earliest  55% @9283ddbe0 2026-07-16 :: | ZHA-15 | Politburo late-Jul meeting signals STIMULUS branch (concrete new fiscal measure) | 55% | OPEN — pre-registered, date TBC |
   MISMATCH   ZHA-16   ledger as-made  45% (Date_Made 2026-09-02) vs STATUS earliest  35% @d757fb63b 2026-09-02 :: | 🆕 **ZHA-16** | **Xi–Trump summit (9/24) produces branch A — an official output extending the reciprocal-tariff suspension beyond 2026-11-1
   perimeter: 17 rows read · SAME 8 · MISMATCH 9 · NOT-FOUND 0 · NO-CONF 0
ASMADE-AUDIT 1: >=1 MISMATCH candidate — candidates, owner verifies at the named blob
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/ZHAO/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** ZHAO re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
