# TRADE IDEA — RSP Dec-18 220/230 call spread — red-day call on the breadth thesis
**Date:** 2026-11-05 (written 13:36 EST from `date`)
**Setup ID:** `IDEA-RSP-DEC-NOV05`
**Terry verdict:** CLOSED — PASSED, WQ-616 RULED B (Will in PROME's chat 2026-11-05 13:59 ET, verbatim "Okay approve with your recs all four"; record `PROME/proposals/2026-11-05_wq614-617-RULED.md`). Never approved, never filled, $0. `IDEA-RSP-OCT20` and its ≤ $4.90 limit are unchanged. Any later use needs a fresh card. *(was: CONDITIONAL — FIRED on its own legs at the 13:33 EST screen, not approved; TERRY leaned wait.)* Separate card; `IDEA-RSP-OCT20` (WQ-591 A, GATE-TERRY-RSP-01) is unchanged and its ≤ $4.90 limit does not move.
**Thesis owner:** HENRY, L616 breadth study (10/31), `AGENTS/HENRY/STATUS.md` § MARKET BREADTH. HENRY has not reviewed these strikes.
**Confidence in structure:** Low.
**Data freshness:** spot and chain 13:33 EST, vendor intraday, screening marks (durable finding 5b). The 220C printed DIRINC. Position truth: FORGE capture 11/5 ~10:0x ET, later changes `[POSITION_STATE_UNKNOWN]`.

## 0. Hard caveats
- New strikes and a new expiry are a new deployment, not the approved card.
- $500 default: inside, $376.30. **X1 CLOSED: any fill goes past X1 by Will's choice on this card, never pre-approved.**
- Credit is unconfirmed for 11/5 and the cause of the selloff is not established. Dealer gamma is negative (HENRY 12:39 ET): moves are amplified both ways.

## 1. One-line setup
Buy a defined-risk rebound in equal-weight stocks, the least damaged index, on a red day, with today's relative strength intact.

## 2. Trigger state (FIRED on screening marks)
| Leg | Line | State 13:33 EST | Status |
|---|---|---|---|
| Red RSP session | live read at order time (root rule #6) | $217.20 −2.75% | MET |
| Floor | RSP ≥ $215 | $217.20 | MET |
| Breadth | RSP/SPY price ratio > 0.280497871, the approved card's frozen line | 0.2950 intraday | MET |
| Debit | broker complex debit ≤ $3.75 | outer $3.75, mid $3.525 (vendor) | MET at the edge; broker quote unverified |

The legs copy the approved card except the debit cap. Proposed card conditions, not registered gates. Good for today's session only; another day needs a re-price.

## 3. Tape
RSP $217.20, 200 closes to 11/4 average $208.12, closing high $223.33. SPX 7,381.54, 0.8% above its 200-day 7,320.35 (200 of 200 bars; vendor). VIX3M/VIX 0.93, front inverted, graded at the close by VIOLET.

## 4. Entry
One complex order, limit **≤ $3.75**. Do not chase. If missed: no order.

## 5. Structure
| Item | Figure, 13:33 EST screen |
|---|---|
| Legs | RSP Dec-18-2026 220C $4.10/$4.40 (OI 1,570) · 230C $0.65/$0.80 (OI 4,647) |
| Size | **×1** |
| **Max loss** | **$376.30** = $375.00 + $1.30 fees |
| Max gain | $623.70 at RSP ≥ $230 on 12/18 (a level above the 200-bar closing high) |
| Breakeven | $223.76 (+3.0%), about the 11/4 close $223.65 |
| DTE | 43 at 11/5 |

**Why not the approved Jan 215/225C:** outer $6.25 vs its ≤ $4.90. Why not Jan 220/230C: the 230C quotes $0.90/$1.85, outer $4.50. Alternatives: IWM Dec-18 275/285C outer $4.25, max loss $426.30, BE $279.26, no thesis owner. RSP shares avoid the vol premium: 54 shares to a $208.02 stop risks $495.72 before gaps, $11,729 of notional, stop executed by hand. Shown, not proposed.

## 6. Risk / scoring
| Field | Entry |
|---|---|
| N_claimed / N_eff | 2 / 1: breadth and rebound share one antecedent, equities stabilising |
| Book overlap | Opposes the bank and private-credit puts; ratio unmeasured. Shares the rebound antecedent with `IDEA-QQQ-200D-NOV05` |
| Edge | **Against, on the measured sample.** RSP after SPY ≤ −3% with HYG better than −1%, 14 episodes: +20 sessions median −6.0%, up 21%. Fragile to the cut: see `../research/2026-11-05_selloff-read/NOTE.md`. No positive expectancy shown. |
| Gap / event | NFP 11/6, CPI 11/10, NVIDIA 11/17 (DOCKET L926) |

## 7. Management (written before any fill)
- **Harvest (durable finding 9):** sell at broker bid **≥ $6.00**: +$222.40 net at $3.75.
- **Invalidation:** RSP completed close < $208.02 (the approved card's line) or HY OAS first-published > 344 bp, or HENRY retracts: sell the spread.
- **Time stop:** sell by the close Fri 2026-12-11. No roll, no add pre-approved.

## 8. Why not
Calm credit on a day this large has not been a good sign (NOTE). Breadth can stay relatively strong while RSP falls in dollars. This pays little unless RSP recovers all of today's loss by mid-December.

## 9. Decision
- [ ] Approve today only: not chosen
- [x] **PASSED (WQ-616 B)**
- [ ] REWORK

**APPROVAL REQUIRED — Will must approve/reject before execution.**
