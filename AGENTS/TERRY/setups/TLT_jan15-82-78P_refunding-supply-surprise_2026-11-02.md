# TRADE CARD — TLT — refunding supply surprise, January 82/78 put spread
**Date:** 2026-11-02
**Setup ID:** `IDEA-TLT-QRA-NOV02`
**Thesis owners:** NEXUS (term-premium decomposition); BOND (Treasury supply and posture).
**Thesis reference:** NEXUS packet dated October 31, `../inbox/processed/2026-10-31_from-NEXUS_term-premium-and-refunding.md`; BOND November 2 update, `AGENTS/BOND/STATUS.md` and `analysis/2026-11-02_update/`.
**Terry verdict:** CONDITIONAL — NOT-FIRED; new proposal, NOT APPROVED.
**Prepared:** 2026-11-02T10:27:55-05:00.
**Confidence in trade structure:** Medium; confidence that the required surprise occurs: Low.

> **TRIGGER STATE 2026-11-04 20:45 EST (TERRY): NOT-FIRED on intent; rec on WQ-592 CHANGED from A to B (decline).** TBAC's recommended November 2026–January 2027 table (home.treasury.gov TBACRecommendedFinancingTableByRefundingQuarter-11042026.pdf, sha256 0d7e2b68c2ba1e1c…) shows November 10Y $42B and 30Y $25B, equal to August and May, and provisional February 42/25. ⚠️ It is a recommendation and "illustrative"; Treasury's own statement is unread and BOND owns the record. ⛔ **Card letter defect, TERRY's:** T1 compares with the "preceding same-tenor scheduled auction". October's 10Y and 30Y were $39B and $22B reopenings, so the routine new-issue step reads +$3B and would satisfy T1 with no supply surprise. The intended comparison is new issue against prior new issue. Not re-lettered here: a fire-day re-letter is not TERRY's to make. BOND's owner guard was never met, so no entry was possible. No order.

## 0. Risk and missing inputs
| Field | Figures / consequence |
|---|---|
| Default | **$500/card. X1 CLOSED / DON'T-SIZE.** Candidate ×2 only at debit ≤ $1.45; maximum loss **$292.60** including $2.60 assumed opening fees. Current deployment **0 / $0**. Will decides this card and any choice against X1; larger size is never pre-approved. |
| Position truth | `[POSITION_STATE_UNKNOWN]`. BOND's dated November 2 record says its duration sleeve is flat after October 30. That is not current broker truth. Do not treat this as a hedge or revive a held line. |
| Quote basis | Required `fetch.py price TLT` at 10:26 EST: **$81.86, +0.02%, GREEN**. Date-only equity payload; retrieval bracket begins 10:26:10 EST. Chain fetch 10:26:11 local, spot_asof 10:26. Individual option bid/ask times/delay flags unavailable; vendor screening, broker price required. |
| Gaps | Broker complex quote, exact fees, live Greeks, IV rank and current book unknown. Two 90-day chart pulls returned **0 bars per ticker** on DNS failure; daily/weekly trend, range and relative-return statistics withheld. Proposed dollar rails below are risk choices, not claimed technical support/resistance. |

## 1. One-line setup
Buy a small amount of long-bond downside **only if Wednesday's Treasury financing plan actually raises long-end coupon auction sizes** and BOND supplies a fresh supporting posture. This does not bet against the recorded base case before the announcement.

## 2. Evidence, catalyst and trigger state
| Input | Dated owner evidence | Implication |
|---|---|---|
| Mechanism | NEXUS October 31 packet: October 8–23 10Y yield −22 bp; ACM term premium −24.6 bp, expected-rate path −0.1 bp. Model can revise. | Supply-sensitive duration compensation can reverse without a Fed change; no yield target inferred. |
| Counterevidence | TERRY October 31 packet/report: Treasury August 5 guidance kept coupon sizes unchanged for several quarters; Citi forecast a $3 billion cut per 20Y/30Y auction. BOND November 2: auctions clearing, long-end dealer stock down $0.580 billion in the October 21 week. | The earlier refusal remains right **unless the new event overturns its premise**. No immediate short recommendation. |
| Standing posture | BOND November 2: prior paired position kill MET-REC, sleeve FLAT, WQ-280 no-add stands. | This is a new conditional deployment requiring Will, not an add, roll or automatic BOND re-arm. |
| This week's catalysts | November 4 refunding; JOLTS November 3, ISM services November 4, Challenger November 5, payrolls November 6. HEARTBEAT Thresholds / operator brief calendar. BOND owns the refunding read. | Labor surprises and haven demand can overwhelm supply. Next week's November 10/12 auctions are follow-through, not a reason to buy before T1. |
| **T1, proposed card condition** | BOND records from Treasury's November 4 primary QRA a **≥ $1 billion increase in either 10Y or 30Y coupon auction size**, compared with the preceding same-tenor scheduled auction, by November 5 close. Net borrowing, bills, maturity changes or removal of guidance alone do not qualify. | **NOT-FIRED:** event is ahead. This is a TERRY proposal, not a registered fleet threshold or a change to BOND's bars. |
| Independent owner guard | BOND's resulting read must explicitly support fresh duration-short construction and identify how its standing kill/no-add restrictions apply to a new card. | Currently absent. T1 alone supplies no waiver. |

## 3. Entry and tape
After both T1 and the owner guard, use the first **GREEN TLT session** through **November 6**, TLT between **$80.50 and $82.50**, and broker complex debit **≤ $1.45**. Root rule #6: puts on green days; no exception. Today colour qualifies at the recorded pull, but the event and owner guard do not. If the move has already taken TLT below $80.50, if the quote is above $1.45, or if no qualifying session occurs by November 6, no entry; card lapses unused. No pre-event order or recurring retry permission.

## 4. Structure and live-tool screen
Buy Jan-15-2027 **82P**, sell **78P**, **×2** intact complex spreads. Expiry is 74 calendar days from November 2; view is the refunding and ensuing auctions, with a November 20 time stop. Real delta near spot avoids a deep crash lottery; selling 78 reduces premium and caps the payoff.

| Leg | Bid / ask | Width / mid | OI / volume | IV |
|---|---:|---:|---:|---:|
| Buy 82P | $1.91 / $1.95 | 2.07% | 34,600 / 41 | 12.70% |
| Sell 78P | $0.54 / $0.56 | 3.64% | 25,972 / 28 | 13.14% |

Required chain tool, **November 2 10:26:11 local**; no named-leg defects. Outer purchase **$1.41**, liquidation **$1.35**, leg-mid **$1.38**; .06 round trip / 1.38 = **4.35%**. Last trades at 09:53 / 09:48 are not quote timestamps. Raw tool stdout retained inside `../research/2026-11-02_WQ590-week-ideas/TLT_jan15_chain.txt.receipt.json`.

## 5. Independence and sizing
| Field | Assessment |
|---|---|
| N_claimed / N_eff | **2 / 1**: term-premium mechanism and supply surprise share one antecedent, higher compensation required to absorb Treasury duration. Size as one view. |
| Book relationship | An equity selloff can help existing puts while **hurting this card through a Treasury haven rally**. No diversification credit or assumed hedge ratio. Current combined exposure unknown. |
| Edge / Kelly | Event-contingent mechanism, positive option expectancy unproved. No Kelly size or calibrated profit probability. |
| Candidate | ×2 at ≤1.45 = $290 premium + $2.60 fees = **$292.60**, **1.1704R** using STATUS's $250 unit. Fits $500 default; X1 remains CLOSED. |
| Screen economics | At 1.41, ×2 loss $284.60. At the 1.45 limit, terminal maximum gain **$507.40**, before closing costs, and fee-inclusive terminal breakeven **$80.537**. These are payoff arithmetic, not targets or expected returns. |
| Alternatives | TBT shares have leveraged daily-reset/path risk; naked long 82P costs $391.30 for ×2 at this screen versus $284.60 for the vertical. No futures or short shares. |

## 6. Management written before any fill
| Rail | Rule for this prospective new position |
|---|---|
| Harvest | Sell **all ×2** at executable complex bid **≥ $2.50**; at a 1.45 entry, net profit **$204.80** after assumed $2.60 fees each way. No further price move needed to activate a profit rule. |
| Kill | Exit all on **TLT completed close ≥ $84.00**, BOND retraction/owner guard failing, or executable complex bid **≤ $0.70**. At exactly .70, limit-entry loss is $155.20 after round-trip fees; gaps can lose $292.60. |
| Time stop | Close the whole prospective line by **November 20 close**, regardless of P/L. No expiry drift. |
| Roll / add / review | None pre-approved. Review at BOND's existing QRA/auction reads or a material owner change; no new monitor or held-line sell/roll prompt. A different strike or later trade needs a new card/Will decision. |

## 7. Why not
The supply outlook on file leans the opposite way. A smaller refunding, unchanged sizes, clean auctions, weak employment or an equity liquidation/haven bid can defeat this card. A term-premium decomposition is a revisable model and does not identify a mispriced option. The liquid screen makes this feasible **if** the premise changes; it supplies no reason to front-run the announcement.

## 8. Trigger forecast, WQ-493 A
| Field | Pre-outcome registration |
|---|---|
| Event | BOND records the T1 ≥$1 billion 10Y/30Y same-tenor size increase from the November 4 QRA. |
| Deadline | November 5, 2026, 16:00 ET. |
| Resolver | Treasury primary QRA size table and BOND's dated QRA read under existing L859; compare the preceding same-tenor scheduled size. Unavailable source is unresolved, not a guessed no. |
| Probability | **0.15, subjective TERRY**; guidance and the recorded Citi cut forecast weigh against it. `CAL-0004`. This predicts T1, not an affordable entry or profit. No model calibration or new sizing authority. |

## 9. Decision route
PROME registers a separate Will decision before presenting an approve/reject ask. WQ-590 authorizes construction only. Recommend consideration as a conditional **after** the supply and owner guards; **wait now**. Fees/deliverable (standard 100 shares assumed), assignment and broker handling must be confirmed; early assignment can create cash/share obligations despite the capped intact-spread payoff.

**APPROVAL REQUIRED — Will must approve/reject before execution.**
