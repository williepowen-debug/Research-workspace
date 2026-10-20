# USO — structure, positioning and technical research

Owner: BRENT. Established October 20, 2026 on Will's direct request for a USO-focused subfolder to track structural, technical and related metrics. This extends the existing USO research; supersedes: none. On Will's follow-up request, the original investigation and all supporting files now live inside this folder. The former report path contains a forwarding link.

## Start here

- [FINDINGS.md](FINDINGS.md): consolidated findings and follow-up analysis from the October 20 discussion.

- [TRACKER.md](TRACKER.md): dated assessment, missing evidence and research questions.
- [observations.tsv](observations.tsv): dated numerical observations, units, source coverage and limitations. This is the maintained numerical series for this folder; summaries link here rather than maintaining another current-value table.
- [Initial short-interest investigation](research-2026-10-20-short-interest/REPORT.md): methodology, primary FINRA row/hash receipts, issuer data and denominator conflicts. Historical report, not a live dashboard.
- [TRADE.md](../TRADE.md): position/approval references; broker/Will remains position truth. TERRY owns trade construction and grading.

## Coverage and source map

| Area | Metrics to examine | Source / coverage | Interpretation limits |
|---|---|---|---|
| Reported short positions | Shares short; report-to-report change; matched-date short percentage; days to cover | [FINRA files](https://www.finra.org/finra-data/browse-catalog/equity-short-interest/files) and [publication calendar](https://www.finra.org/filing-reporting/regulatory-filing-systems/short-interest) | Settlement snapshots, not current estimates. Net changes cannot identify gross covering/new shorts or motives. Days to cover is a volume ratio. |
| Securities lending | Shares on loan; new loans/returns; lendable supply; utilization; annual borrow fee | [IBKR proxy](https://chartexchange.com/symbol/nyse-uso/borrow-fee/); broader [securities-finance datasets](https://www.spglobal.com/market-intelligence/en/solutions/products/securities-finance) if accessible | One broker is not the whole market. Supply changes confound availability/utilization. Shares borrowed need not have been sold short. No broad authenticated USO loan series currently available. |
| Fund structure | Shares outstanding; creations/redemptions; premium/discount; holdings and roll schedule; creation restrictions | [Issuer](https://www.uscfinvestments.com/uso), [holdings](https://www.uscfinvestments.com/holdings/uso), [resources](https://www.uscfinvestments.com/resources/uso), current filings | Match numerator/denominator dates. A daily redemption is not proof of short covering. Creation capacity may change. |
| Trading activity | Short-marked volume/share of covered volume; total volume relative to history | FINRA daily files; source/venue-specific redistributors | [Short volume is not short interest](https://www.finra.org/investors/insights/short-interest); never accumulate it into an outstanding-position estimate. |
| Technical behavior | USO versus actual futures basket/NAV; relative volume; trend and realized volatility | Timestamped market data, issuer holdings and NAV | Match contracts, rolls, split adjustments and observation times. Price/volume patterns do not identify a trader. No chart study completed at setup. |
| Options | Volume and next-day open-interest changes by strike/expiry; implied volatility; skew; spreads | Authenticated option chains; [OCC/OIC data guide](https://www.optionseducation.org/referencelibrary/market-data) | Buying versus selling and opening versus closing matter. Put/call counts alone do not establish direction or dealer hedge exposure. No current chain adopted at setup. |
| Settlement stress | Fails to deliver and threshold-list status | [SEC fails data](https://www.sec.gov/data-research/sec-markets-data/fails-deliver-data), exchange lists | Lagged; fails can arise from long or short sales and do not prove naked shorting. No current USO assessment completed. |

## Observation conventions

`as_of` is the underlying settlement date or source observation clock, not the date a page was opened. `recorded_on` is the research date. CONF_PRIMARY means directly recovered primary observation; REPORTED_SECONDARY means a vendor observation, not independently authenticated at its upstream source. Neither means live. Unit `percent_annual` is an annualized percentage, not a daily cost; `percent_of_covered_volume` excludes unobserved venues.

Keep historical snapshots dated. UNKNOWN belongs in the tracker, never a numerical zero. A float ratio needs a justified denominator from the same date. Compare the same provider/coverage over time; a source switch is not a market change. Preserve source revisions with their vintage. Exact extracts link to existing receipts; new observations include a source and coverage caveat.

Refresh during authorized BRENT USO reviews and when relevant releases are actually available. This folder establishes manual research tracking; no scheduled job, release-day session, numerical trading trigger or autonomous alert was installed. Existing trading/threshold authority remains at its canonical owner.
