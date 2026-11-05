# TERRY -> PROME: live selloff construction read, 2026-11-05 13:33 EST marks

**Answers:** Will's word in PROME's window 13:25 ET, verbatim "open BROCK and launch TERRY". **Evidence:** `AGENTS/TERRY/research/2026-11-05_selloff-read/NOTE.md`; marks `chains_final.txt` beside it. **Basis:** vendor intraday, screening marks, not closes, no broker quote. No order, no gate or level change, no expiry reminder. **Book:** FORGE capture 11/5 ~10:0x ET, cash $28,218.18 (62.93%) plus pending +$3,953.67; Robinhood $2,349.37 [≤11:06 ET]; later changes `[POSITION_STATE_UNKNOWN]`.

**Limits carried:** credit is unconfirmed for 11/5 (HY 332 [11/4] pre-dates today, HYG −0.48%); the cause is not established.

## 1. Approved cards: none eligible
| Row keys | State 13:33 EST | Block |
|---|---|---|
| `IDEA-RSP-OCT20` · WQ-591 A · GATE-TERRY-RSP-01 | NOT-FIRED. Red $217.20 −2.75%, above $215, ratio 0.2950 | Debit only: outer $6.25, mid $5.375, vs ≤ $4.90. Rough: mid reaches $4.90 near RSP $215.7, outer near $214.7, under the floor. Closest of the four |
| `IDEA-CREDIT-HYG-BDC-OCT23` · WQ-513 A | NOT-FIRED. HY 332 [11/4], run 0 of 3, needs > 350 ×3 | Trigger and red HYG. Price is no block: outer $0.67 vs ≤ $1.00. Last run start for the 11/13 window is the 11/9 close |
| `IDEA-ORCL-PUTSPREAD-OCT23` · WQ-514 A · WQ-518 A | NOT-FIRED. DTCC 300 [11/3] vs 350, no newer read found | Four blocks: T1, T2 ($114.94 < $120), debit outer $6.35 vs ≤ $4.40 and past $5.00 no-chase, FQ2 date. Red too |
| `IDEA-UNG-SSW-OCT31` · WQ-573 · WQ-606 A · GATE-TERRY-UNG-01 | NOT-FIRED. GFS `.anl` +0.057 [11/5 12Z], ECMWF +0.660 [11/5 00Z] | Trigger and green $9.31 +0.43%. Price fits: outer $0.47 vs ≤ $0.50 |

## 2. New cards, none approved
| Row key | Label, trigger state | Structure | Max loss / gain | $500 default / X1 |
|---|---|---|---|---|
| `IDEA-HYG-FOLLOW-NOV05` | **NOT-FIRED.** HY first-published > 344 bp on one close (332 [11/4]) or HYG close < $76.81 ($77.14), then first green HYG day, by 12/4 | HYG Jan-15 76/73P ×5, limit ≤ $0.60 (outer $0.44) | $306.50 / $1,193.50, BE $75.39 | inside / past X1 only by Will's choice |
| `IDEA-RSP-DEC-NOV05` | **FIRED on its legs, TERRY leans wait.** Red, ≥ $215, ratio intact, outer $3.75 at the limit; broker unverified; today only | RSP Dec-18 220/230C ×1, limit ≤ $3.75 | $376.30 / $623.70, BE $223.76 | inside / past X1 only by Will's choice |
| `IDEA-QQQ-200D-NOV05` | **NOT-FIRED.** Live VIX3M/VIX ≥ 1.00 on a red QQQ day by 11/20 (0.93 now) | QQQ Dec-18 670/680C ×1, limit ≤ $4.90 (outer $4.67) | $491.30 / $508.70, BE $674.91 | inside / past X1 only by Will's choice |

⚠️ The two calls are one rebound idea, up to $867.60 together. The hedge plus the approved HYG ×4 is one credit idea, up to $711.70 together. Both pairs pass $500 per idea, Will's choice only. The same line, HY > 344 bp, arms the hedge and kills both calls.

**Recommendation:** the hedge is the best of the three. Calm credit is not an all-clear, and HYG vol has not moved. Pre-approve it on its trigger. Pass on calls today; let QQQ wait for its trigger.

## 3. Evidence that changes the read
Big down days with credit calm did worse than days when credit fell too. SPY ≤ −3%, HYG better than −1%, 14 episodes: +20 sessions median −5.0%, 21% up (ex-2008/09, n = 9: −3.0%, 33%). With HYG ≤ −1%, 28 episodes: +1.9%, 68% up. Any day: +1.5%, 67%.
⚠️ The −5.0% is not a forecast. At a −2.5% cut it is +1.0%, 51% up, n = 37. What holds at all five cuts tested: calm credit trails both comparisons at +20 sessions. Waiting for the curve to normalise helps (ex-2008/09, n = 8: +0.1%, 50% up) and is still under any-day. HYG after the 14: −3% or worse within 48 sessions in 10 of 14, but ending ≤ −1.4% in only 4 of 14, so the hedge lives on its harvest rule.

## ACTION
1. PROME registers WQ rows for `IDEA-HYG-FOLLOW-NOV05`, `IDEA-RSP-DEC-NOV05` and `IDEA-QQQ-200D-NOV05` before showing them to Will.
2. PROME names the desk that reads GFS 18Z and ECMWF 12Z for `IDEA-UNG-SSW-OCT31`. AEOLUS STATUS 12:37 ET says neither was read.
3. PROME routes the 11/5 HY cell to TERRY when LIQUID grades it. WALTER closed 11:54 ET, so its close pass is not running.

OP-SCALE contest follows by a separate packet before Saturday 11/7. TERRY stays open.

**APPROVAL REQUIRED — Will must approve/reject before execution.**
