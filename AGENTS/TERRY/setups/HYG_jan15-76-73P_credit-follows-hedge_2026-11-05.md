# TRADE IDEA — HYG Jan-15 76/73 put spread — hedge if credit starts to follow
**Date:** 2026-11-05 (written 13:36 EST from `date`)
**Setup ID:** `IDEA-HYG-FOLLOW-NOV05`
**Terry verdict:** CONDITIONAL — APPROVED FIRED, order presented to Will, no fill known (T1(a) HY 348 [11/5], read 2026-11-06 10:09 EST). (WQ-615 A, Will in PROME's chat 2026-11-05 13:59 ET, verbatim "Okay approve with your recs all four"; record `PROME/proposals/2026-11-05_wq614-617-RULED.md`; GATE-TERRY-HYG-FOLLOW-01). ×5 at or under $0.60, max loss $306.50. X1 passed by Will's choice on this card only. Nothing fills before T1 fires; at an eligible entry TERRY re-checks live (root rule #4) and presents the order, which is Will's hand on a live broker quote (root rule #5). *(was: not approved, 11/5 13:36 EST)* Separate card; `IDEA-CREDIT-HYG-BDC-OCT23` (WQ-513 A) is unchanged.
**Thesis owner:** LIQUID and REGINALD own the credit read. TERRY owns only the construction. Credit is unconfirmed either way for 11/5; the cause of the selloff is not established (HENRY card SIG-W-20261105-027; VIOLET SIG-VIO 12:41 ET).
**Confidence in structure:** Medium.
**Data freshness:** chains and spot 13:33 EST, vendor intraday, screening marks (durable finding 5b). The order is priced on the broker chain. Position truth: FORGE capture 11/5 ~10:0x ET, later changes `[POSITION_STATE_UNKNOWN]`.

> **TRIGGER STATE 2026-11-06 10:11 EST (TERRY): T1(a) FIRED · ENTRY ELIGIBLE ON THE SCREEN IF HYG IS GREEN · NO ORDER BY THE DESK.** ICE BofA HY OAS first-published **348 bp [11/5]** vs > 344, by 4 bp: FRED CSV `BAMLH0A0HYM2` 3.48, first seen 10:09:05 EST by TERRY's poll and independently by PROME; prior 332 [11/4], episode peak was 344 [10/30]. `fetch.py fred` still cached 3.32 at 10:09, so the CSV is the read. T1 is one close and cannot un-fire. HYG $77.29 +0.01% at 10:09, then $77.31 +0.03% at 10:10: green by cents vs close $77.28, not a completed close. Chain 10:09 EST: 76P $0.50/$0.61, 73P $0.17/$0.25, outer $0.44, mid $0.345 vs ≤ $0.60. Screening marks; the broker quote governs. Order presented via PROME at 10:10 EST. If HYG is red at the order, no entry that day; the window runs to 12/4 and a passed day voids nothing. LIQUID's grade pending. Card-owner reading: an entry today counts as "after T1" because the cell published today; same reading the UNG card uses for a same-day fire.

> **TRIGGER STATE 2026-11-05 close (TERRY, stamped 16:12 EST): NOT FIRED.** T1(b): HYG regular close $77.28 −0.31% vs < $76.81, $0.47 above (final vendor daily bar read 16:49 EST; corrected from a $77.305 pre-print read). T1(a): HY 332 [11/4]; 11/5 cell due about 10:30 ET 11/6. No order.

## 0. Hard caveats
- HY 332 bp is the 11/4 cell; the 11/5 cell lands about 10:30 ET 11/6 (PROME routes LIQUID's grade).
- $500 default: inside, $306.50 at the limit. **X1 CLOSED: Will made the choice to pass X1 on this card only (WQ-615 A). It extends to no other card and to no size above ×5 or debit above $0.60.**
- **Same idea as the approved HYG card.** If this fills and the approved ×4 later fires, the two together risk up to $711.70 on one idea, past the $500 default. That second step needs Will's word at that moment (WQ-615 A).
- "Hedge" here means positive convexity to credit following. No realised hedge ratio to the book is measured; do not size from one.

## 1. One-line setup
Own cheap protection on junk bonds if the equity selloff reaches credit, entered on a green HYG day after credit shows a first real sign.

## 2. Trigger state (NOT-FIRED)
| Leg | Line | State 13:33 EST | Status |
|---|---|---|---|
| **T1, either of** | (a) ICE BofA HY OAS (FRED BAMLH0A0HYM2, mirror), first-published, one close **> 344 bp**, the 10/30 peak of this episode. (b) HYG completed regular-session close **< $76.81**, its 60-bar closing low to 11/4 (60 of 60 bars; vendor) | (a) 332 [11/4], 11/5 unpublished. (b) $77.14 −0.48%, day low $77.13 | **NOT FIRED** |
| Entry window | First **green HYG session** after T1 (root rule #6), through Fri 2026-12-04 | HYG red today | waits on T1 |
| Void | No T1 by 12/4, or HY OAS ≤ 330 on 5 consecutive closes (REGINALD's exit line) before entry, or broker debit > $0.60 at entry | count 0 of 5 | live |

These are proposed card conditions, not registered gates.

## 3. Tape
HYG $77.14, range 76.81–79.92 on 60 closes to 11/4. VIX 26.83, VVIX 128.83, VIX3M/VIX 0.93 (13:33 EST, vendor intraday, not closes). LQD +0.11%, JNK −0.48%, BKLN −0.61% (13:26 EST). Equity vol moved and credit vol did not: HYG Jan puts read 7.3%–11.0% implied (vendor, 77 to 73 strikes) against ~10.9–12.3% on the 10/23 after-hours screen. Different hours, same vendor, not a clean comparison.

## 4. Entry
One complex order, never legged. Limit **≤ $0.60**. Do not chase above $0.60. If missed: new card, no automatic order.

## 5. Structure
| Item | Figure, 13:33 EST screen |
|---|---|
| Legs | HYG Jan-15-2027 76P $0.53/$0.61 (OI 193,230) · 73P $0.17/$0.24 (OI 83,688) |
| Debit | outer $0.44, leg mid $0.365 |
| Size | **×5** |
| **Max loss** | **$306.50 at the $0.60 limit** ($226.50 at the $0.44 outer); fees $0.65 per contract per side |
| Max gain | $1,193.50 at the limit, HYG ≤ $73 on 1/15 |
| Breakeven | $75.39 at the limit (−2.3%) |
| DTE | 71 at 11/5 |

**Why 76/73, not the approved 77/74:** outer $0.44 vs $0.67, so the same width costs about a third less and five spreads stay well inside $500. **Why January:** credit works over weeks (construction rule #16). Dec-18 76/73P outer $0.39 saves $0.05 for 28 fewer days. **Why HYG:** deep, holds the bonds, cheapest vol in the complex (durable finding 7).

## 6. Risk / scoring
| Field | Entry |
|---|---|
| N_claimed | 2: HY OAS and HYG price, one market |
| Shared antecedent | Broad credit repricing |
| **N_eff** | **1, sized as one view** |
| Book overlap | Shares this antecedent with approved HYG ×4 and the bank and private-credit puts in FORGE |
| Edge | Measured context, `../research/2026-11-05_selloff-read/NOTE.md`: after 14 episodes of SPY ≤ −3% with HYG better than −1%, HYG touched −3% or worse within 48 sessions in 10 of 14 (5 of 9 ex-2008/09), yet ended 48 sessions ≤ −1.4% in only 4 of 14 (2 of 9). It dips and recovers, so the harvest rule carries the trade. No probability stated; no positive expectancy shown. |
| Rate leg | HYG carries Treasury duration: a falling 10-year cushions it while spreads widen. TLT +0.39% today |
| Gap / event | NFP 11/6, CPI 11/10, 30Y auction 11/12, NVIDIA 11/17 (DOCKET L926) |

## 7. Management (written before any fill)
- **Harvest (durable finding 9):** sell at broker bid **≥ $1.50**, 50% of width: +$437.00 net at a $0.60 entry with fees both ways.
- **Kill:** HY OAS ≤ 330 on 5 consecutive closes, sell at the bid.
- **Time stop:** sell by the close Fri 2027-01-08. No roll pre-registered (Non-Negotiable #6).
- **Early assignment:** ETF puts can be assigned early, and HYG distributes monthly; the capped payoff assumes the intact spread.

## 8. Why not
- Credit may never follow. VIOLET's read is Path B, equity concentration unwinding, not Path A credit.
- T1(a) at 344 is 5 bp under REG-T-04's 350 and can fire on noise.
- By the time T1 fires the debit may exceed $0.60, and the card then does not fill. That is a valid outcome.
- If Will prefers to own it before credit moves: first green HYG session, ≤ $0.50, ×5, max loss $256.50. That passes the fired-trigger standing rule by his choice alone.

## 9. Decision
- [x] **APPROVED (WQ-615 A):** ×5, limit ≤ $0.60, max loss $306.50, on T1 then a green HYG day, past X1 by Will's choice
- [ ] Pre-trigger variant in § 8: not chosen
- [ ] REJECT
- [ ] REWORK

**APPROVAL REQUIRED — Will must approve/reject before execution.** The approval above is for the conditional; the order at an eligible entry remains his hand.
