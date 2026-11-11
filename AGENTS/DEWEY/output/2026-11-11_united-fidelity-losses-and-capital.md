# United Fidelity: recognized multifamily losses and depleted capital

Date: 2026-11-11. Authority: Will's focused follow-up to CATO's population review. Mode: Thesis. Confidence: High on filing arithmetic and historical orders; UNKNOWN on specific loss trigger, subsequent remediation and property-level recovery. Entity: United Fidelity Bank, FSB, RSSD 391575; bank figures, not consolidated parent figures.

## Finding

The cash-basis explanation does not remove the economic damage: **Q3 multifamily charge-offs were $362.453 million, quarterly net loss was $246.851 million, and reported total capital fell to 7.2647% of risk-weighted assets.** Remaining multifamily loans were $2.722 billion, of which $2.143 billion were nonaccrual. The narrower investigation therefore establishes a capital problem alongside the classification change. It does not establish the specific reason for that change or the ultimate recovery. [S1, calculations]

## Losses, remaining exposure and accounting

Amounts below are $million; balance-sheet values are quarter-end, income values explicitly identified. [PRIMARY: S1]

| Measure / MDRM | June 30 | September 30 |
|---|---:|---:|
| Assets / RCFD2170 | 6,493.323 | 5,915.451 |
| Gross loans / RCFD2122 | 3,436.066 | 3,059.390 |
| Domestic multifamily loans / RCON1460 | 3,089.016 | 2,721.595 |
| Multifamily nonaccrual / RCON3501 | 0.121 | 2,143.246 |
| Loan allowance / RCFD3123 | 81.707 | 6.323 |
| Multifamily gross charge-offs, YTD / RIAD3588 | 0 | 362.453 |
| Loan provision, YTD / RIAD4230 | 0 | 287.070 |
| Net income, YTD / RIAD4340 | -2.790 | -249.641 |
| Bank equity / RCFD3210 | 652.530 | 389.667 |

The allowance reconciles exactly: **81.707 + 287.070 − 362.459 gross quarterly charge-offs + 0.005 recoveries = 6.323**. The broader $319 million provision includes $31.930 million for other amortized-cost financial assets (RIADJJ02); using the broader provision in the loan-only bridge would be wrong. Recognized losses consumed both newly provided reserves and the existing allowance. [S1]

Multifamily represents 88.96% of total reported gross loans; 78.75% of the remaining multifamily balance is nonaccrual. These are remaining reported balances after charge-offs, not an additional $2.14 billion loss estimate. Adding the charge-offs to remaining balances does not reconstruct original affected-loan principal: originations, repayments and which loans were charged down are undisclosed. The $6.323 million allowance covers the entire loan book, not a disclosed multifamily-specific reserve. [S1; calculation/limits]

TEXT4769 says the approximately $2.14 billion loans were current **before** entering nonaccrual cash-basis treatment and cash receipts can still generate interest. It does not say all remain current now, identify collateral valuations, or explain the trigger. June's explanation contained only rental-income commentary. Federal Reserve guidance permits nonaccrual before missed payments and, under conditions, cash income after partial charge-offs. This explains why the disclosures can coexist, not why this bank made the change. [S1; PRIMARY: S2, §2065.1.4–.6]

## Remaining capital capacity

| Regulatory measure | June 30 | September 30 |
|---|---:|---:|
| CET1 capital, $million / RCFAP859 | 535.135 | 262.335 |
| Tier 1 capital, $million / RCFA8274 | 640.360 | 367.726 |
| Total capital, $million / RCFA3792 | 728.416 | 402.133 |
| Risk-weighted assets, $million / RCFAA223 | 4,828.713 | 5,535.471 |
| CET1 ratio / RCFAP793 | 11.0824% | 4.7392% |
| Tier 1 ratio / RCFA7206 | 13.2615% | 6.6431% |
| Total capital ratio / RCFA7205 | 15.0851% | 7.2647% |
| Leverage ratio / RCFA7204 | 10.1619% | 5.8188% |

[S1.] Both capital depletion and higher risk-weighted assets weakened the ratios even though total assets shrank. The reported 150%-weighted delinquent/nonaccrual HFI exposure rose from $13.251 million to $2,156.486 million (RCFDS455), consistent with a material risk-weighting effect; this is not a complete RWA attribution. Tier 2 eligible allowance also fell from $61.200 million to $7.521 million (RCFA5310). Do not equate accounting equity with regulatory loss headroom. [S1]

The total ratio is below the ordinary 8% adequately-capitalized threshold in 12 CFR 6.4; below 8% meets that rule's numerical undercapitalized test. This is a filing-to-rule comparison, not evidence of a newly issued OCC notice. At unchanged RWA, reaching 8% would require **$40.705 million more eligible total capital**. CET1 exceeds 4.5% by only **$13.239 million** on the same fixed-denominator basis. Neither figure is a recapitalization forecast or safe further-loss budget: capital eligibility, taxes, earnings and RWA can change. [PRIMARY: S3; S1 calculations]

The October 31, 2023 OCC consent order imposed higher minimums: CET1 8%, leverage 9%, Tier 1 10%, total 12%. September's reported ratios are below all four. It addressed credit review, allowance methodology and other deficiencies; the bank neither admitted nor denied the findings. Article IV(8) permits the supervisor to require a disposition plan upon specified failures and written direction; it does not itself announce a sale or liquidation. I found no termination in targeted searches, but the live search endpoint failed, so later modification/current enforcement status remains unverified. The order is context, not proof that examiners directed these 2026 losses. [PRIMARY: S4, pp.2–6]

## Ownership, counterevidence and unresolved cause

The Federal Reserve's June 2024 agreement identifies the chain Pedcor Financial LLC → Pedcor Financial Bancorp → Fidelity Federal Bancorp → United Fidelity Bank. It required prior approval for specified parent distributions and debt actions. Parent support therefore cannot simply be assumed; the agreement does not quantify available fresh capital. [PRIMARY: S5]

Pedcor's own banking page describes affordable-housing finance and services to Pedcor affiliates. That establishes a business connection, **not** that the impaired loans are affiliate loans or that a particular sponsor/geography caused the losses. No loan-level mapping was established. [PRIMARY: S6]

Counterevidence matters: residual book equity and CET1 remain positive; cash interest may continue; nonaccrual balances are not total-loss estimates. Nevertheless, actual charge-offs, quarterly losses and capital deterioration rule out treating this as an inconsequential label change. The cause, collateral valuations, guarantees, expected recoveries, post-quarter capital actions and affected properties remain UNKNOWN. [S1; bounded source review]

## Sources and reproduction

- **S1 PRIMARY:** FFIEC Call Reports, June/September 2026, RSSD391575, retrieved November11. [CDR public portal](https://cdr.ffiec.gov/public/). Full parsed rows: `research/2026-11-11_united-fidelity/20260630-rows.json` and `20260930-rows.json`; derived checks: `calculations.json`. Original June SDF: `research/2026-11-11_003R-population/ufb-20260630.sdf.gz`; September member `391575.sdf.gz` in that directory's `call-reports-sdf.tar.gz`. Original population manifest preserves hashes. Financial units are $thousands. Parse semicolon-delimited SDF; code=value at columns 2/3; quarterly income=September YTD minus June YTD. September inspected cells last updated October30. Subsequent amendments possible.
- **S2 PRIMARY:** [Federal Reserve nonaccrual guidance](https://www.federalreserve.gov/publications/files/bhc-2065-2093.pdf).
- **S3 PRIMARY:** [OCC published capital rule, p.62042](https://www.occ.gov/news-issuances/federal-register/2014/78fr62018.pdf). Current [12 CFR6.4 text](https://www.law.cornell.edu/cfr/text/12/6.4) corroborated the thresholds; direct eCFR retrieval failed.
- **S4 PRIMARY:** [OCC order2023-031](https://www.occ.gov/static/enforcement-actions/ea2023-031.pdf).
- **S5 PRIMARY:** [Federal Reserve agreement24-014](https://www.federalreserve.gov/newsevents/pressreleases/files/enf20240625a1.pdf).
- **S6 PRIMARY:** [Pedcor banking](https://www.pedcorcompanies.com/our-services/banking/).

## Delivery and process report

REGINALD: capital/filing follow-up reference. GIBBS and CREED: remaining multifamily exposure and explicit missing property mapping. TERRY: tradeability read requested; no instrument, position or execution proposed. PROME: focused follow-up complete within public evidence; prioritization belongs to Will. WALTER: log research output and audit pointers. Reference: Will-directed UFB follow-up to003R, not a new broad-study commission.

Method: saved primary filings plus targeted official/company-source searches; no population redownload, fan-out, paid access or external contact. Reconciled allowance and quarterly income; checked capital codes and denominator, historical enforcement terms, and counterevidence. The specific-cause question remains unanswered rather than inferred. No new watcher or research program. EagleBank exact reconciliation and Plaza recovery economics remain separately unresolved and unchanged. CATO's review informed scope, not a substitute for this filing check. No downstream consumption or completed TERRY read claimed.
