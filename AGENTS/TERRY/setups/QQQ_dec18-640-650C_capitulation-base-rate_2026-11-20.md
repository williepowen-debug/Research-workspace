# TRADE IDEA — QQQ Dec-18 640/650 call spread — the first panic close with the vol curve inverted
**Date:** 2026-11-20 (written 11:3x EST; figures stamped from `date` and the pulls)
**Setup ID:** `IDEA-QQQ-CAPIT-NOV20`
**Thesis owner:** none. No desk holds a bullish view. The evidence is TERRY's own tape base rate (chart/tape/vol is TERRY's lane); HENRY owns the dealer levels and gives no direction (11/19: "a volatility-timing statement, not a direction").
**Thesis reference:** `../research/2026-11-20_wake-L831-L929/NOTE.md` § 3.
> **RULING 2026-11-23, recorded 12:1x EST (TERRY, PROME packet 6df81509fa): CLOSED — WQ-724 RULED, DECLINED (Will 2026-11-23 12:03 ET, verbatim "WQ-724 (TERRY's QQQ bounce bet): declined."; record `PROME/proposals/2026-11-23_wq732-follow-up-RULED.md`). Never filled, $0, no order.** On its own terms the card could not have entered by the time of the ruling: the credit filter needed an HY cell ≤ 350 and the 11/20 cell printed 376 (FRED BAMLH0A0HYM2, pulled 12:09 EST); the entry needed a red QQQ session at ≤ $635 and QQQ was $651.07, +7.00% (vendor 12:09 EST). The bounce the card was built for came on a session it could not enter. CAL-0009 (the 11/20 trigger forecast) stays graded as it was. Note `../research/2026-11-23_will-rulings-paper-book-print/NOTE.md` § 1.
**Terry verdict:** CLOSED — WQ-724 RULED, DECLINED (Will 2026-11-23 12:03 ET); never filled, $0 (was: CONDITIONAL — **NOT-FIRED, NOT approved.** Will decides at fire (root rule #5; USER.md "Trade ideas loosened", 2026-10-20). A fire is not an approval.)
**Confidence in trade structure:** Low. **Edge:** Small (RISK_SCORING § 2: "watch / tiny only").
**TERRY's lean:** decline unless Will wants a defined contrarian ticket; ×1 is the most I would take.
**Data freshness:** spot and VIX 11:22–11:25 ET vendor intraday (VIX bars about 15 minutes delayed); chain 11:24 ET vendor, SCREENING marks (durable finding 5b): the order is priced on the broker chain. Position truth: FORGE 11/18 13:21 ET capture; later changes `[POSITION_STATE_UNKNOWN]`.

## 0. Missing inputs / hard caveats
- [x] Live price checked (11:22 ET) · [x] chain checked (vendor screen 11:24 ET) · [ ] broker quote at entry
- [x] Position truth: FORGE 11/18 shows Will's own short-dated QQQ puts (Nov-18 655P, Nov-19 648P, no card, D-103): the opposite view, his hand; later state unknown.
- [x] Catalysts checked: Thanksgiving Thu 11/26 closed, Fri 11/27 half day; FOMC decision Wed 12/9 (REGINALD 11/19) inside the hold; Nvidia 10-Q pending (VULCAN).
- **$500 default: inside, $451.30 at the limit. X1 CLOSED: any fill goes past X1 by Will's choice on this card, never pre-approved.**
- **Opposes the book's credit card:** `IDEA-HYG-FOLLOW-NOV05` (HYG puts, APPROVED FIRED, fill Will's hand) pays if credit follows; this card loses in that case. Together they are a partial offset on one driver (the HY path), not two views.

## 1. One-line setup
Buy a defined-risk 20-session bounce in QQQ after the first red close where VIX is over 30 and the vol curve is inverted, because that state has historically marked short-term panic more often than the start of a crash.

## 2. Trigger state (NOT-FIRED)
| Leg | Line | State at 11:22–11:25 ET | Status |
|---|---|---|---|
| **T1 — panic close** | today's 16:00 closes: Cboe VIX close **> 30**, VIX3M/VIX close **< 0.95**, QQQ close **red** vs $645.04 [11/19] | VIX 30.31, ratio 0.932 (11:08 ET bars); QQQ $627.32 −2.75% | **NOT FIRED** until the closes print (the tested form is the close) |
| **Credit filter** | REGINALD's **REG-T-04 has FAILED**: an HY OAS first-published cell ≤ 350 bp for 11/20 (publishes about Mon 11/23) or 11/23 (about Tue 11/24). Added 11:3x ET on LIQUID's 11/20 packet (REG-T-04 completing on the 11/23 cell about 55%, LIQUID's projection): the sample's losers were the credit-led cases, so the card enters only if credit does not confirm. A risk filter, **not tested** in the base rate (pre-2023 HY is not reachable here). | 352 [11/19] = 1 of 3 | waits on the HY prints |
| **Entry window** | first **red QQQ session** after T1 and the credit filter (root rule #6: calls on red days), through Wed 11/25, live at order time | — | waits on T1 and the filter |
| **No chase** | QQQ ≤ **$635.00** at order time and broker complex debit ≤ **$4.50** | screen outer $4.41 | moment properties, graded at order time |
| **Void before entry** | REG-T-04 **fires** (HY OAS first-published > 350 bp on three consecutive sessions: 11/19, 11/20 and 11/23 cells), or no qualifying red session by 11/25 | — | — |

**Why the close, not now:** the base rate was measured on closes. Firing on today's intraday read would be calling a description of the moment a trigger (`finding_gate_pass_is_not_evidence_it_found_the_best_reason`); waiting for the close costs part of the median first-week bounce (+2.9% at +5 sessions) and buys a condition that was not true when I wrote it.

## 3. Tape (11:22–11:25 ET, vendor, intraday)
| Item | Read |
|---|---|
| QQQ | $627.32, −2.75% vs $645.04 [11/19 close]; 8.0% under its 200-day 682.01 (200 of 200 bars to 11/19) |
| S&P 500 | 7,084.58, 9.39% under its 7,818.93 close [10/6] (251 daily bars); intraday under HENRY's 7,100 (HEN-64 needs a close) |
| Breadth | RSP −0.05%, IWM −0.96%, KRE +0.33%: tech-led, equal weight flat |
| Vol | VIX 30.31 / VIX3M 28.24 = 0.932 inverted; QQQ Dec ATM IV about 36% (11:24 screen) vs about 28% on 11/5 |
| Credit | HY OAS 352 [11/19, FRED], fifth straight rise from 320 [11/12]; HYG $76.49 −0.05%; bank credit absent (REGINALD 11/19) |
| Dealers | HENRY 11/19: short gamma, trough 7,100–7,200, about 40% of it expires today; after expiry, moves need more news |

## 4. Entry
One complex order, limit **≤ $4.50**, on the first red QQQ session 11/23–11/25 after T1 and the credit filter, QQQ ≤ $635.00. Strikes stay at 640/650. Above $4.50 or QQQ above $635: no order. If missed: no card (a re-strike is a new card).

## 5. Structure
| Item | Figure, 11:24 ET vendor screen |
|---|---|
| Legs | QQQ Dec-18-2026 **640C** $18.31/$18.49 (OI 3,728) · **650C** $14.08/$14.11 (OI 14,446) |
| Debit | outer $4.41, mid $4.31 |
| Size | **×1** |
| **Max loss** | **$451.30 at the limit** ($450.00 + $1.30 fees, 0.65/contract/side) |
| Max gain | $1,000 − $451.30 = **$548.70** at QQQ ≥ $650 on 12/18 |
| Breakeven | **$644.50** at the limit (+2.7% from $627.32) |
| Payoff | 1.22 : 1 |
| DTE | 28 at 11/20; 12/18 is exactly 20 sessions after 11/20 |

**Why a spread:** Dec implied about 34–36% at these strikes; an outright 640C is about $18.40 ($1,840), far past the default. **Why 640/650:** the long strike is +2.0% from spot and the short +3.6%, inside the sample's +20-session median (+6.0%), so the full payoff needs only a median-or-worse outcome. Alternatives: 630/650C outer $9.90 (past the default at ×1); 645/655C outer $4.40 with breakeven +3.5% (worse odds on the same view).

## 6. Risk / scoring
### 6a. Effective-N
| Field | Entry |
|---|---|
| N_claimed | 2: the panic base rate · dealer short gamma expiring today |
| Shared antecedent | the same panic state; the gamma point is a vol-timing statement with no direction (HENRY) |
| **N_eff** | **1**, sized as one view |
| Book | Opposes Will's own short-dated QQQ puts (his hand) and the HYG put card (credit-follows). If both cards filled, a credit-led continuation pays HYG and loses here. |

- **Edge (measured today, one specification):** first red QQQ close with VIX close > 30 and VIX3M/VIX < 0.95, 17 episodes 2007–2026 (5,121 daily bars from 2006-07-17): QQQ **+20 sessions median +6.0%, up 76%; ≥ +3.6% in 11 of 17; negative in 4 of 17** (worst −16.5%, 2008-09). Base, all days: +2.0%, up 67%. Sample EV at this structure: about 11/17 × $548.70 − 6/17 × $451.30 ≈ **+$196 per card**, before the caveats.
- **Caveats on the edge (they decide the lean):** n=17, built today; QQQ data start 2006, so the 2000–2002 tech unwind (the nearest analog to an AI-concentration unwind) is not in it; the losers are the credit-led cases (2008-09, 2020-02) and credit is widening today; HY history before 2023 is not reachable, so I could not condition on it; the 11/5 study found the opposite at +10 sessions after single −5% QQQ days (median −4.2%, 11 episodes), a different condition.
- **Kelly reference:** not computed; edge confidence is low, so the size is the default floor, ×1.
- **Invalidation:** after entry, HY OAS first-published > 350 bp on three consecutive later sessions (REG-T-04's shape, re-run from the entry day) → sell at the broker bid. Before entry, REG-T-04 firing voids the card.
- **Gap/event risk:** FOMC 12/9 inside the hold; a holiday week with thin volume (HENRY's caveat).
- **Liquidity:** OI 3,728 and 14,446; vendor spreads $0.03–0.18. Acceptable on the screen; broker quote decides.
- **Execution block:** T1 met at today's closes; REG-T-04 failed on the 11/20 or 11/23 HY cell; a red session by 11/25; QQQ ≤ $635; broker debit ≤ $4.50; Will's approval.

## 7. Management (written before any fill)
- **Harvest (durable finding 9):** sell at broker bid **≥ $8.00** (+$347.40 net at $4.50, fees both sides).
- **Thesis break:** HY first-published > 350 on three consecutive sessions after entry → sell at the bid.
- **Time stop:** sell by the close **Fri 2026-12-11** (15 sessions after 11/20; the sample's +15 count is also 11 of 17 at ≥ +3.6%). No roll, no add pre-approved (Non-Negotiable #6; construction rule #23).
- Review: at each HY first print (REGINALD's count) and at 12/9.

## 8. Why not
No owner view; a small, post-hoc sample; the regime most like today's (a tech-concentration unwind with credit widening) is either missing from the sample or among its losers. Payoff 1.22 : 1 needs the hit rate to hold well above 45%. The clean answer can be no.

## 8b. Trigger forecast (WQ-493 A)
- **Trigger event:** on Fri 2026-11-20, the Cboe VIX regular close is > 30, the VIX3M/VIX close ratio is < 0.95, and QQQ closes below $645.04.
- **Deadline:** 2026-11-20 16:15 ET (Cboe index closes).
- **Resolution basis:** Cboe VIX and VIX3M daily closes and the QQQ daily close (vendor daily bars, re-pulled after 16:15 ET; FRED VIXCLS as a cross-check for VIX).
- **Probability:** **0.50, subjective** (VIX 30.31 at 11:08 ET sits on the line; the ratio and QQQ legs are far from their lines).

## 9. Decision
- [ ] APPROVE at fire: ×1, limit ≤ $4.50, max loss $451.30, past X1 by Will's choice
- [ ] REJECT
- [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution.**
