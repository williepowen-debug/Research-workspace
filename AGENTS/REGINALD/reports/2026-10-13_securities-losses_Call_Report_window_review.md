# Bank securities losses and the Q3 disclosure window

**As of:** October 13, 2026 evening ET. REGINALD review of Will's supplied side-LLM report. Primary verification scope: the relevant FDIC QBP page, current filing-deadline notice and capital provision; preserved Treasury observations; existing June30 bank-level AOCI cohort. The entire QBP and a new national bank screen were not reviewed.

The report identifies a useful duration-risk channel alongside our credit work. Its aggregate securities figures check out. Its proposed October30 shock, 95-bank count and named-bank rankings remain unproved. The investment question is how new marks affect tangible equity, earnings, funding and capital relative to expectations. An unrealized-loss screen alone cannot answer that question.

## Claims and their financial bases

| Supplied claim | Finding | Investment implication |
|---|---|---|
| Q2 unrealized losses $326.7B: AFS $109.8B, HTM $216.9B | Verified at FDIC QBP printed p4, PDF p7. Total +$1.6B QoQ, −$68.6B/17.4% YoY; respective loss/cost ratios 5.5%, 2.9%, 10.5%. | These are quarter-end market/book gaps for non-equity securities, not new earnings expense or a regulatory-capital deduction. FDIC's footnote distinguishes this calculation from AOCI. |
| October30 reveals the Q3 losses | Qualified. Most September30 filers are due Friday October30; certain banks with more than one foreign office receive five additional days, to Wednesday November4. | Filing deadline is not simultaneous public availability. Earnings can disclose marks earlier. Q3 balances stop September30; October yield moves belong to Q4 or later commentary. Our November7 retrieval still checks completeness/amendments. |
| Short rates rose about60bp in30days | Instrument/window unspecified. Official preserved data show August31→September30: 2Y +54bp, 5Y +60bp, 10Y +54bp. | Roughly consistent with selected tenors, but short-rate change alone cannot revalue a bank's Treasury/MBS book. Curve shape, duration, hedges, runoff and MBS convexity matter. |
| About95 of4,295 banks suffer >20% equity impairment | Unverified calculation. A secondary reference links an All-In passage at49:27; original transcript/model not retrieved. | Need total existing loss versus incremental shock, equity denominator, taxes, bank/holdco identity, date, security duration and hedge treatment before reproducing or using it. This is not an established failure count. |
| Size shares, median ratios, Schwab67%, BAC$84B/35%, WFC21%, stock correction | Not independently established here on comparable dates/entities/bases. | Preserve as leads, not inputs. Price declines do not establish attribution or unpriced loss. Existing September29 attribution and October12 KRE studies already address part of this question. |

Primary sources: [FDIC Q2 2026 QBP](https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-second-quarter-2026.pdf), [FDIC current Q3 filing notice](https://www.fdic.gov/news/financial-institution-letters/2026/consolidated-reports-condition-and-income-third-quarter), [Treasury 2026 daily nominal curve CSV](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&_format=csv). Podcast navigation: [All-In at49:27](https://www.youtube.com/watch?v=ZJKs08oU1zg&t=2967s), found through [a secondary episode reference](https://www.abetternewspaper.com/editions/69322fa5-f365-4909-b98b-737532741ce3). That reference is not independent financial verification.

## Recognition and capital

AFS interest-rate marks generally reduce GAAP equity through AOCI after tax. The existing June30 AOCI cohort records opt-out for all14 selected bank subsidiaries. The applicable [capital provision](https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-217/subpart-C/section-217.22), b(2), permits eligible institutions to exclude specified AOCI components from CET1. A GAAP book-value loss therefore need not immediately reduce reported CET1. Bank and listed-parent capital must remain separate.

An AFS sale at the already-marked value moves the recognized loss into earnings; it does not create the same GAAP equity loss a second time. At an opted-out institution, realization can remove the capital benefit of the prior exclusion. Reconcile earnings, AOCI reclassification and the capital adjustment rather than adding all three as economic losses.

HTM interest-rate fair-value gaps generally remain outside reported GAAP equity until realization, but credit losses can be recognized without a sale. Legacy losses transferred from AFS to HTM can also remain in AOCI. “HTM losses do not affect capital until sold” is consequently too broad. Securities losses can impair earning power, collateral liquidity and funding economics even without forced sales; “unrealized” does not mean economically costless.

The [March19 capital proposal](https://www.fdic.gov/news/financial-institution-letters/2026/regulatory-capital-rule-regulatory-capital-and-standardized) proposed AOCI inclusion for Category III/IV with a transition. It is not a basis for treating every regional bank's Q3 mark as a current capital deduction. Rule state, category and effective date require verification at the relevant entity.

## Reuse of the existing AOCI study

`reports/2026-09-24_cohort_AOCI_exposure.md` and `workbook/AOCI_COHORT_2026Q2.tsv` already identify the channel. Their June30 data and September22 scenario remain frozen; the table below is a separately dated mechanical sensitivity, not a revision of those expectations.

| Treasury tenor | June30 yield | September30 yield | Q3 change |
|---|---:|---:|---:|
| 2Y | 4.14% | 4.88% | +74bp |
| 5Y | 4.19% | 5.09% | +90bp |
| 10Y | 4.44% | 5.29% | +85bp |

Actual quarter-end rates came from BOND's preserved official CSV, captured October7; this is a direct read of the original observations, not reliance on BOND's conclusions. No fresh October13 official curve was retrieved here.

For scale only, apply assumed modified duration3–5 years to June30 AFS fair value, an assumed parallel90bp shock and25% fully usable tax benefit: after-tax mark = FV × duration ×0.009 ×0.75. Hold securities, hedges, shares and other balance-sheet items fixed; omit convexity, runoff, trading, basis changes and issuer-specific taxes. These simplifying assumptions prevent interpretation as an AOCI forecast.

| Bank subsidiary | June30 AFS fair value $M | Additional after-tax mark sensitivity $M |
|---|---:|---:|
| OZK | 4,235.075 | 85.76–142.93 |
| WAL | 18,846.464 | 381.64–636.07 |
| EGBN | 904.184 | 18.31–30.52 |
| VLY | 4,292.148 | 86.92–144.86 |

WAL has the largest AFS dollar sensitivity of these four on this fixed-book assumption. EGBN's named-credit workouts remain the more decision-sensitive earnings question; OZK's cash exits and retained financing remain central. Neither comparative statement is a valuation forecast. Map actual subsidiary marks to parent equity, hedges and shares before estimating a parent TBV effect. Existing AOCI is already in GAAP equity; subtracting the entire AFS market/book gap again double-counts it. Any HTM economic-book adjustment needs a separate, clearly labeled basis.

As a reasonableness check, an unhedged duration5 portfolio facing60bp loses about3% before tax. An incremental loss exceeding20% of equity would require securities exceeding6.67× that equity denominator, or8.89× with25% tax relief. Existing losses, longer duration or leverage can change that arithmetic. It illustrates why the 95-bank model inputs matter; it does not reproduce that screen.

## Evidence that can change the judgment

Use the existing Q3 reads, beginning with WAL, and the planned November7 retrieval. Record:

1. Actual AOCI/TBV changes and AFS/HTM cost-versus-fair-value disclosures, reconciled to hedges, sales, transfers, runoff and taxes. A small mark despite the curve move is contrary evidence to an unhedged-duration hypothesis.
2. Deposit changes, uninsured/rate-sensitive composition, deposit cost and replacement borrowing. Deposit loss combined with security sales, expensive funding or weaker liquidity would strengthen the stress-transmission mechanism; stable funding and usable liquidity weaken the forced-sale mechanism.
3. New securities expense versus prior AOCI, and new credit expense versus prior allowance, kept separate. Reconcile realized cash and retained exposure through the existing21-row workout bridge.
4. Parent earnings capacity, tangible capital and matched regulatory numerator/RWA. Price revised sustainable returns and funding costs against dated expectations; a lower P/TBV ratio alone does not establish unpriced credit loss. Current comparable consensus remains a gap.

**Conclusion-changing conditions:** unexpectedly durable deposits, effective hedges or limited mark losses weaken the rate-stress mechanism. Marks plus costly funding replacement or forced realization strengthen it. A credible earnings/capital bridge and an expectations gap are still necessary for a valuation conclusion. No new bank-wide “20%” trading threshold, national screen, standing monitor or scored forecast is introduced.

Future sessions should retain the supplied report as a hypothesis, recover the podcast calculation if available and append Q3 actuals without rewriting the September24 or October13 expectations. Source identities, dates, arithmetic and retrieval failures are preserved in `domain/sources/2026-10-13_securities-losses-review-receipt.json`.
