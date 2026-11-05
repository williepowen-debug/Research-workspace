# Path A F2 audit: result

**Run:** 2026-11-05, finished 10:44 ET (VIOLET, Claude Code, Opus 5.5). Spec frozen before outcomes at commit cc62521ac. Script `run_audit.py`; tables `cells.tsv`, `episodes.tsv`. Raw ICE series not committed.

## Verdict

**1. F2 is NOT RUNNABLE, which resolves to NO GATE.** The primary cell has 3 post-2018 episodes against the frozen floor of 5. Under KB-VIO-217/260 that is no gate, never F2-waived. Variants cannot rescue it (SPEC rule 1).

**2. The inherited ~70% did not replicate.** Pooled hit rate 42.1% (8 of 19) on the frozen +50% definition, under the frozen 50% bar. On the literal TRADE.md wording, a spike over 10 points, it is **31.6% (6 of 19)**. That implies a false-positive rate of 58-68%, against the inherited 25-30%.

**3. There is a real signal, of a different kind from the one the thesis states.** It roughly doubles the odds of a spike. It does not make a spike likely.

| Hit definition, 100bp cell, t+10 to t+30 | Pooled | Base rate | Lift | p | Pre-2018 | Post-2018 |
|---|---:|---:|---:|---:|---:|---:|
| +50% (frozen primary) | 8/19, 42.1% | 21.4% | 1.97x | 0.030 | 7/16, 43.8% vs 16.7%, p 0.007 | 1/3 vs 33.1%, p 0.704 |
| Over 10 points (POST-FREEZE, TRADE.md:185) | 6/19, 31.6% | 13.7% | 2.31x | 0.037 | 5/16, 31.2% vs 9.6%, p 0.014 | 1/3 vs 23.9%, p 0.547 |
| VIX close at or above 30 | 5/19, 26.3% | 6.8% | 3.84x | 0.007 | 4/16, 25.0% vs 5.0%, p 0.007 | 1/3 vs 11.3%, p 0.303 |
| +15% | 12/19, 63.2% | 65.0% | 0.97x | 0.666 | 11/16 vs 61.2% | 1/3 vs 74.5% |

**Read:** the +15% row is the warning. A loose definition gives a respectable-looking 63%, and it equals the 65% base rate, so it carries no information. How the inherited 70% was defined is unknown, so this shows how such a figure can arise, not that it did.

## Why post-2018 cannot answer

- **The bar moved.** A 50% VIX rise from a sub-20 base is twice as common after 2018: 33.1% vs 16.7% of eligible days. This matches KB-VIO-211.
- **VIX got there first in the large shocks.** On the first +100bp day: 2/27/2020 VIX 39.16, 3/7/2022 VIX 36.45, 4/3/2025 VIX 30.02. All three fail the VIX<20 gate, so credit led none of them. This agrees with the April lag study.
- **The 3 eligible episodes:** 11/16/2018 hit (18.14 to 36.07), 1/9/2019 miss, 6/3/2019 miss.

## Other frozen findings

- **Curve filter does almost nothing:** it removes 1 of 20 episodes (3/28/2023), and the hit rate moves from 40.0% to 42.1%. The inherited drop to a 15-20% false-positive rate has no support here.
- **50bp cell has no edge at +50%:** 13/52, 25.0% vs 21.4%, p 0.311. Its VIX>=30 rate is higher: 9/52, 17.3% vs 6.8%, p 0.008.
- **Onset reading matters:** with VIX<20 at the trough instead of the signal day, the rate falls to 25.0% (8/32), p 0.382.
- **Lookback:** 42 days 46.2% (6/13), 126 days 30.8% (8/26).

## The live episode, excluded from all tallies

- On the 63-day definition the low is 260bp [8/28], so HY 340bp [11/03] is +80bp. On the thesis watch base it is +72bp from 268bp [9/22]. Both are under 100bp. The 63-day trigger is 360bp.
- It entered the 75bp cell on **10/22 at VIX 19.03**. Its t+10 to t+30 window is about 11/05 to 12/07. VIX 21.15 [11/02] fell before that window and does not count.
- Over-10-points needs a VIX close at or above 29.03; +50% needs 28.55. 75bp-cell history: 7/25 (28.0%) against a 13.7% base, post-freeze cell, and 1/3 after 2018.

## Limits

- **Superset:** credit origin and cross-sector were not tested, nor the "no Fed QE backstop" check in TRADE.md. Those filters may lift the rate; this audit cannot say.
- **Clustering:** 19 episodes sit in about 5 credit cycles, so independence is overstated and every p here is too generous.
- **Post-freeze cell:** the over-10-points cells were added after outcomes were seen, because I found TRADE.md:185 late. Frozen cells reproduced byte-identical after the addition.
- **Series:** 1996-2023 comes from one archived FRED snapshot, authenticated on 26 overlap days and thesis marks. Later ICE restatements before 2023-11 cannot be checked.
- **No outside reader:** primary count recomputed by a separate code path, and 4 episodes checked by hand.

## Recommendation, needs Will's word

1. Withdraw "~70%" and the 25-30% false-positive figure from the thesis and TRADE.md. Replace them with: 6 of 19 (32%) against a 14% base, unreplicated after 2018.
2. Keep Path A as a mechanism and WATCH, with no gate and no sizing derived from it. Withdraw the dormant Lag Trade's 1-2% sizing template. Its "HY OAS x 7.6 + 158 = implied VIX" target also has no defined units.
3. Optional: register the live 75bp episode as a dated prediction, so VIOLET has one open test. Rule proposed: VIX close at or above 29.03 by about 12/07.
