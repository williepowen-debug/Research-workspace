# NCLH Q3 10-Q read and funding re-run — 2026-11-05

**Verdict: the funding leg is clean through 2027 on this test, and November 17 should pass, though no document can certify that until the date. What is left of the bear read is ticket pricing, deposits and leverage, not liquidity.** Working model, not truth.

Primary: NCLH 10-Q for 9/30/26, acc 0001104659-26-120217, filed 2026-10-29, read at sec.gov 2026-11-05. Also read: Q2 10-Q (acc 0001104659-26-089657), Q3 FY25 10-Q (acc 0001104659-25-106057), October 15 Amendment 3 Ex-10.1 and 8-K (acc 0001104659-26-116254). Arithmetic: `model.py`, `calculations.json`. USD millions unless marked.

## What the 10-Q added

| Line | Reported | Grade against the watchlist | So what |
|---|---|---|---|
| **D1 liquidity 9/30** | ~$1.4B actual = cash 256.5 + ~$1.1B revolver availability (6/30 ~$1.5B; 9/30/25 ~$1.8B) | **CONFIRMS** (bar ≥ ~$1.3B) | The release's $2.1B was pro forma. Availability plus the October steps reconciles: 1.1B + 380 + 315 ≈ 1.8B |
| **D2 notes** | Issue price, redemption premium and extinguishment loss are not stated in the 10-Q (text search 11/5). Revolver repayment reads **$380.0M**, against ~$376.3M in the 10/15 8-K | **STILL OPEN** to the Q4 print or 10-K | Difference 3.7 preserved, not reconciled. This re-run uses 380.0 |
| **D3 9M OCF** | 1,706.4, +4.64% | **CONFIRMS**, with a quality note | Of the +75.7, working capital is +51.9 (accrued expenses alone swing +127.1) and cash earnings +23.8 |
| **D4 deposits** | Balance −0.16% YoY; 9M line −36.6 vs +13.9 | **BREAKS stands, direction better than the 10/29 read said** | The YoY cash gap narrowed from −226.1 at H1 to −50.5 at 9M. But ticket revenue fell 104.3 in Q3, so about 59% of the 175.7 improvement is less revenue being released from deposits, not more booked. Refundable share of contract liabilities **45%** vs 40% at 9/30/25 and 6/30/26. Card-processor reserves: none required |
| **D5 2027 exchangeables** | 192.0 + 24.1 = **216.2 outstanding at 9/30**, current; company expects to repay in cash or refinance before maturity | Condition 1 of the spring is live | See November 17 below |
| **D6 covenants** | "In compliance" at 9/30. Waiver sentences are the same boilerplate as Q2. **New:** Amendment 3 "modified certain existing financial covenant definitions and the related collateral" | **BREAKS on the letter ("any amendment"); no stress in the arithmetic** | See covenant section |
| **D7 maturities** | Rem-2026 238.6 · 2027 1,105.7 · 2028 1,346.1 · 2029 1,370.0 · 2030 4,134.3 · 2031 1,875.1 · after 5,428.2 · total 15,498.0 | **CONFIRMS** | 2028 still carries the 525 because the redemption is an October event. 2030 rose 184.7 since June, in line with more revolver use in Q3. Pro forma: 2028 ~821 · 2030 ~3,754 · 2031 ~2,825 |
| **D8 ratings** | Moody's B1 / B3 · S&P B+ / B+ / BB revolver | **CONFIRMS** | Unchanged from Q2 |
| **D9 capex** | Rem-2026 $1.1B · 2027 $3.1B · 2028 $1.8B; export credit $0.6B / $2.0B / $1.3B | **CONFIRMS on timing** | 2027 +$0.2B and rem-2026 −$0.2B: the same $4.2B moved later. Contract minimums $19.42B vs $18.65B, +$773M, mostly after 2031 |
| **B3 2027 interest** | Not in the 10-Q (text search 11/5) | **STILL OPEN** | Needs the call transcript. Quartr is not available to this desk |
| **Canada (PROME 9/22 ask)** | Named only inside the North America region. About 84% of revenue is U.S.-sourced; no other single country exceeds 10% | **ANSWERED AS A BOUND:** below 10% of revenue | Alaska and itinerary dependence are not measured here |
| **New: ship sales** | Oceania Insignia sale agreed October 2026, closing September 2027, price not stated. Oceania Sirena sold September 2026, leased back to spring 2028; ships proceeds 105.0 | Context | Small so far. Logged under a combination theme |

## Covenant: what the amendment changed

The contract's redline shows the change to **Total Capitalization**. The old open-ended add-back for intangible impairments and non-cash exchangeable-note charges is gone. In its place is a fixed dollar add-back to equity: **$7,409.0M through 2028, $6,350.6M in 2029, $5,292.2M from 2030.** The collateral list adds Norwegian Epic and Pride of America and removes Norwegian Star.

| Net funded debt / capitalization, 9/30/26 (my arithmetic, ESTIMATE) | Carrying debt | Principal |
|---|---:|---:|
| With the $7,409.0M add-back | **0.584** | 0.591 |
| Without it | 0.825 | 0.829 |
| Contract limit, 9/30 and 12/31/26 | 0.80 | 0.80 |
| Add-back needed to pass | ~559 | ~661 |

So the test passes only because of the add-back, but it needs a small part of it: about $0.6B of $7.4B. The limit steps down to 0.70 by 9/30/28. ⚠️ The old add-back's dollar value is unknown, so I cannot say whether the swap loosened or tightened the test. Whether a 9/30 certificate used the new or old definition is also not established. The company states compliance either way.

## November 17 revolver test

The revolver matures that day only if the 2027 exchangeables are still unrefinanced **and** Free Liquidity is below $800M.

| Free Liquidity estimate (ESTIMATE) | $M |
|---|---:|
| After the October deal, excluding the conditional 315 layer | ~1,731 |
| Less the **whole** of Q4's net need, as if it all landed by 11/17 | ~413 |
| Deliberately harsh floor | **~1,318** |
| Margin over 800 | **~518** |

⚠️ Expected to pass, not certified. Inputs are a rounded "$1.1 billion", October cash flows are unknown, and redemption premium and fees are unquantified. Drawability assumes the ordinary draw conditions hold. No public document appears on the date, so L715 grades on later evidence: an 8-K if it sprang, or the 10-K.

## Funding model re-run

Same method and endpoint (12/31/27) as 9/19 and 10/14; the method reproduces the 9/19 flat and +2% rows. Uses before operating cash: 3,449.8. Opening room: cash 256.5, revolver 1,480, plus 315 conditional.

| OCF path per year | OCF to 12/31/27 | Left, excluding the 315 | Left, with the 315 |
|---|---:|---:|---:|
| +2% | 2,599 | **886** | 1,201 |
| Flat | 2,473 | **760** | 1,075 |
| −5% | 2,165 | **452** | 767 |
| −10% | 1,867 | **154** | 469 |
| −15% | 1,580 | **−134** | 181 |

**Breakeven −12.7% a year excluding the 315 (10/14: about −14% to −16%), −18.3% with it.** If the ~$175M 2027 interest step-up is not earned back: −9.6%. Cash flow is tracking +4.64% through nine months, so the company sits well above all three, and the like-for-like cushion has narrowed a little.

⚠️ **Limits unchanged:** endpoint test, not a low-point schedule. Cruise cash is seasonal, so interim liquidity runs lower than these figures. FY27 other capex of 400 is my assumption. No refinancing, asset sales or equity are assumed, which is conservative. The 2027 repayments are funded in the model, including the 216.2 exchangeables.

## Capital-access ladder

NCLH 9/30: (256.5 + ~1,100) / 15,498.0 = **8.75%** (June 9.81%; RCL 9/30 32.58%). Pro forma for October about 13.2%, with the conditional 315. Same formula as KB-CRU-152.

## What this does to the desk

- **`VX-CRU-05` held at RED(4); no band letter forces a move.** The band has no cell for a raised guide with a negative yield and rising leverage. Bands are Will's, so the re-spec goes to him through PROME.
- **Recommendation: NCLH conviction 3 → 2.** Of the row's five listed weakeners, two have plainly happened (guide raise, improved funding, the latter at a higher cost), two partly (operating turnaround; deposits and occupancy), and lower leverage has not. The row stays WATCH 3 / NO CARD until Will rules.
