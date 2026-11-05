# Live selloff construction read, 2026-11-05 13:33 EST

Will's word in PROME's window 13:25 ET, verbatim "open BROCK and launch TERRY". Marks: `chains_final.txt`, vendor intraday, screening marks, not closes, no broker quote. Study: `study_v2.py`, `study_v2_output.txt`. Tape 13:33 EST: SPX 7,381.54, SPY $736.33 −3.98%, QQQ $651.85 −5.80%, RSP $217.20 −2.75%, HYG $77.14 −0.48%, VIX 26.83, VIX3M 25.02, VVIX 128.83.

No order, no gate or level change. Credit is unconfirmed for 11/5: HY 332 [11/4] pre-dates today. The cause is not established.

## Approved cards
| Card key | Trigger | Colour | Broker-side debit screen | Verdict |
|---|---|---|---|---|
| `IDEA-RSP-OCT20` WQ-591 A, GATE-TERRY-RSP-01 | Red, ≥ $215, ratio 0.2950 > 0.2805: met | red, right side | 215C 7.60/9.00, 225C 2.75/3.10: outer $6.25, mid $5.375, vs ≤ $4.90 | **NOT ELIGIBLE, debit.** Rough, 11:08 to 13:33: mid moves $0.31 and outer $0.53 per $1 of RSP, so mid reaches $4.90 near RSP $215.7 and outer near $214.7, under the $215 floor. A moment property; vol can move it either way |
| `IDEA-CREDIT-HYG-BDC-OCT23` WQ-513 A | HY > 350 ×3: 332 [11/4], 0 of 3 | red, wrong side | 77P .86/.93, 74P .26/.30: outer $0.67, inside ≤ $1.00 | **NOT ELIGIBLE, trigger and colour.** Price is not the block. Last run start for the 11/13 window is the 11/9 close. X1 would be Will's choice at that moment |
| `IDEA-ORCL-PUTSPREAD-OCT23` WQ-514 A | CDS ≥ 350: DTCC 300 [11/3], no newer read found; T2 ≥ $120: $114.94 fails | red, wrong side | 115P 11.20/11.55, 100P 5.20/5.45: outer $6.35 vs ≤ $4.40, past the $5.00 no-chase | **NOT ELIGIBLE, four separate blocks** incl. FQ2 date, not re-checked, moot. Gap closed from the equity side |
| `IDEA-UNG-SSW-OCT31` WQ-573, GATE-TERRY-UNG-01 | Vortex < 0: not fired; GFS `.anl` +0.057 [11/5 12Z], ECMWF +0.660 [00Z] | green $9.31 +0.43%, wrong side | 10C .94/.97, 12C .50/.51: outer $0.47, inside ≤ $0.50 | **NOT ELIGIBLE, trigger and colour.** ECMWF 12Z and GFS 18Z unread per AEOLUS STATUS 12:37 ET |

## Study: big down days with credit calm (daily closes, HYG from 2007, cut off 11/4)
Episodes: SPY close-to-close ≤ cut, first day in a 10-session gap. Forward = total return. HYG condition = HYG day return better than −1%. Today is intraday and not a sample point.

| Sample | n | +5 sessions | +20 sessions | +29 sessions |
|---|---:|---|---|---|
| SPY ≤ −3%, HYG calm | 14 | +0.6%, 64% up | **−5.0%, 21% up** | −2.2%, 29% up |
| same, ex-2008/09 | 9 | +0.7%, 67% | −3.0%, 33% | −0.9%, 44% |
| SPY ≤ −3%, HYG ≤ −1% | 28 | +1.5%, 61% | +1.9%, 68% | +3.5%, 71% |
| SPY ≤ −2.5%, HYG calm | 37 | +0.6%, 54% | +1.0%, 51% | −0.1%, 49% |
| SPY ≤ −3.5%, HYG calm | 7 | +1.4%, 86% | −3.9%, 29% | −1.7%, 43% |
| Any day | 5,979 / 5,970 | | +1.5%, 67% | +2.0%, 68% |
| Patient: first red SPY close with VIX3M/VIX ≥ 1, ex-2008/09 | 8 of 9 | +1.2%, 62% | +0.1%, 50% | +1.5%, 62% |

**What holds:** at all five cuts tested, calm-credit episodes trail both the credit-with-it episodes and the any-day baseline at +20 sessions. Calm credit is not an all-clear. **What does not hold:** the −5.0% figure. It is one cut of a small sample, and moving the cut by 0.5 point flips the sign. Do not cite it as a forecast. Five of the 14 are 2008–09. HYG early history was thin. A plausible reason is selection (a first leg vs a washout), not tested.

RSP, same 14: +20 sessions median −6.0%, 21% up. QQQ ≤ −5% days, 11 episodes: +10 sessions median −4.2%, 18% up, +20 sessions −2.2%, 45% up.

HYG price after the 14: worst point within 48 sessions ≤ −3% in 10 of 14 (5 of 9 ex-2008/09); 48-session end ≤ −1.4% in 4 of 14 (2 of 9), median end +1.0%. It dips and recovers, so a put spread needs its harvest rule.

## New cards
| Key | Label | Structure | Max loss | $500 / X1 |
|---|---|---|---|---|
| `IDEA-HYG-FOLLOW-NOV05` | NOT-FIRED | HYG Jan-15 76/73P ×5 ≤ $0.60 | $306.50 | inside / past X1 his choice |
| `IDEA-RSP-DEC-NOV05` | FIRED on its legs, TERRY leans wait | RSP Dec-18 220/230C ×1 ≤ $3.75 | $376.30 | inside / past X1 his choice |
| `IDEA-QQQ-200D-NOV05` | NOT-FIRED | QQQ Dec-18 670/680C ×1 ≤ $4.90 | $491.30 | inside / past X1 his choice |

The same line, HY first-published > 344 bp, arms the hedge and kills both calls.

Bars: SPY 6,000, QQQ 6,000, RSP 5,918, HYG 4,926, VIX 6,002, VIX3M 5,110 returned; bars after 11/4 excluded. SPX/QQQ/RSP 200-day and HYG 60-bar stats each on full counts. `study_v1.py` is the first pass, kept for the trail.
