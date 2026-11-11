# Q3 bank coverage in historical context; EagleBank's exact bridge remains unproved

**Date:** 2026-11-11 | **Mode:** Thesis | **Request:** REQ-DEWEY-20261022-003R, continuation | **Confidence:** High on source rows and arithmetic; Medium on cross-era comparison; UNKNOWN on EagleBank's unexplained schedule difference. **State:** PARTIAL overall; six-bank historical-placement leg delivered.

## Key finding

**EagleBank's Q3 allowance coverage of noncurrent loans sits near the 11th percentile against the June 2026 comparison population, versus about the 18th percentile for its Q2 value.** Valley moved from about the 31st to the 27th percentile on that same fixed comparison. This completes the six banks' Q3 placement against the original historical snapshots. It is **not** a Q3 contemporaneous peer ranking, a new predictive test, or a failure probability.

EagleBank's company and regulatory-capital numbers tie more closely than the earlier rounded bridge showed, but an exact bridge to its past-due/nonaccrual schedule remains unproved. The full-universe Q3 aggregate trigger remains uncomputed: Q3 is absent from the actual FFIEC bulk selector, not merely missing from FDIC search.

## 1. Six-bank placement on unchanged snapshot dates

Coverage = loan allowance / (nonaccrual + 90+ days past due and still accruing). The six Q3 ratios come from the twelve fresh FFIEC bank filings documented in `output/2026-11-11_003R-six-bank-refresh-partial.md`. The comparison populations were freshly retrieved from FDIC for December 2006, June 2008 and June 2026. Eligible banks have assets at least $1 billion, gross loans at least 10% of assets, positive noncurrent loans, and a reported allowance. Percentile is the percentage with a **strictly lower** ratio.

| Original six banks | Q3 coverage | Q3 value vs Dec 2006 | Q3 value vs Jun 2008 | Q2 value vs Jun 2026 | Q3 value vs Jun 2026 |
|---|---:|---:|---:|---:|---:|
| SouthState | 199.66% | 44.5 | 76.8 | 53.2 | 51.0 |
| Valley | 109.75% | 22.2 | 55.4 | 30.6 | 26.7 |
| Huntington | 148.59% | 32.6 | 66.9 | 40.6 | 37.8 |
| EagleBank | 67.20% | 10.9 | 32.6 | 18.2 | 10.8 |
| BankUnited | 50.92% | 7.1 | 22.0 | 7.8 | 7.2 |
| Zions | 204.28% | 45.3 | 77.4 | 55.2 | 52.1 |
| **Valid comparison ratios, n** | | **622** | **659** | **1,016** | **1,016** |

[PRIMARY: FDIC BankFind and FFIEC CDR; derived by DEWEY, retrieved November 11. Evidence and exact numerators: `research/2026-11-11_003R-continuation/placement-calculations.json`.]

**Small correction to the original placement calculation.** The October report's counts—623, 661 and 1,023—include 1, 2 and 7 foreign-bank branches with positive noncurrent loans but **missing allowances**. Its published percentiles are consistent with counting these undefined ratios in the denominator, while excluding them from the lower-ratio numerator. The new table excludes them from both. The saved calculation retains the old-denominator result for direct comparison; the old Q2 table is reproduced within 0.1 percentile point at its printed precision. This is a denominator repair in **Table 4 placement only**. It does not recalculate or overturn the separate episode hit rates or bank-loss regressions.

## 2. EagleBank: narrower arithmetic, stronger limits

All amounts below are **$ thousands**. Bank = EagleBank, RSSD 2652092; company = Eagle Bancorp.

| Source field | June 30 | September 30 |
|---|---:|---:|
| Company 10-Q nonperforming loans, HFS excluded | 111,124 | 166,021 |
| Bank RC-R II 5.c, RCONS449 | 111,124 | 166,021 |
| Bank RC-R II 4.c, RCONS423, HFS delinquent/nonaccrual exposure category | 25,656 | 13,534 |
| Arithmetic sum of those two RC-R cells | 136,780 | 179,555 |
| Bank RC-N 9, RCON1403, total nonaccrual | 136,915 | 179,722 |
| **Arithmetic difference: RC-N less the two RC-R cells** | **135** | **167** |
| Bank RC-N Memo 5, RCONC226, HFS nonaccrual | **0** | **0** |

The company HFI figure matches a bank regulatory-capital cell **exactly at both dates**. The earlier $191K/$201K arithmetic used rounded company HFS disclosures of $25.6M/$13.5M. Using the exact RC-R HFS-category amounts narrows the differences to $135K/$167K, but **does not prove a like-for-like reconciliation**.

The September 2026 FFIEC 041 form, page 67, explicitly excludes residential mortgage, high-volatility CRE and sovereign exposures from the RC-R 4.c/5.c categories when delinquent or nonaccrual. They are therefore not automatically equal to RC-N's total population. Separately, RC-N's explicit HFS nonaccrual memo is **zero at both dates**, despite the issuer's HFS disclosure and RC-R figures. That reporting tension must remain visible. Neither its cause nor the $135K/$167K difference is explained by a disclosed loan-level bridge. Do not assign it to fees, principal-versus-amortized-cost accounting, rounding, parent consolidation, or error without evidence.

**Disposition:** HFS treatment explains much of the reported company-versus-bank ratio difference, and the company HFI figure is found within the bank's own filing. The exact RC-N bridge remains UNKNOWN. No allegation of misstatement follows.

## 3. Full-band source dependency, checked rather than inferred

- FDIC's Q3 `REPDTE:20260930` query still returns zero rows. That is a limitation of this endpoint, not absence of individual Q3 filings.
- A normal GET and product-selection postback on the FFIEC bulk page succeeded using curl. Selecting **Call Reports — Single Period** returned **June 30, 2026 as the newest option; September 30 was absent**. The options, timestamp and response hash are saved in `bulk-availability.json`.
- FFIEC's documented bulk schedule begins 45 calendar days after quarter-end (November 14 for Q3). This is not a guaranteed release date. Individual retrieval remains possible; its published API guideline is approximately 2,500 downloads per hour, with 1.5-second spacing recommended. A complete 4,267-filer assembly would be a substantial separate extraction pass, not six-bank evidence extrapolated into a band.

**Still owed under the same commission:** the full-population Q3 aggregate trigger, current-Q3 population comparison, and any exact EagleBank reconciliation the source can establish. This pass delivers the fixed-history six-bank placement and documents the remaining source distinctions. It does not mark 003R resolved, invoke the unavailable-Q3 clause, create a watcher, or reset the original deadline.

## Counter-evidence and limits

The original study found no useful standalone predictive contribution from falling coverage at the requested horizon. Low placement alone does not change that. CECL changed reserve accounting in 2020; the pre-2020 columns can overstate today's cushion. BankUnited and Huntington's noncurrent totals include substantial government-guaranteed balances in the prior study; those adjustments are not refreshed here. Issuer mix and a few large loans can dominate individual ratios. The June 2026 comparison population is intentionally held fixed and is **not today's Q3 distribution**.

## References, reproduction and process report

- [FDIC financials API](https://api.fdic.gov/banks/financials): saved `fdic-20061231.json`, `fdic-20080630.json`, `fdic-20260630.json` plus exact URL/time/hash metadata under `research/2026-11-11_003R-continuation/`. Apply the eligibility and strict-less-than formulas in §1; `placement-calculations.json` saves each lower count and both denominator conventions.
- FFIEC CDR SDF source rows and hashes: `egbn-regulatory-bridge-rows.json`; retrieved in this session's preceding November 11 live pull. Additional SEC table extracts: `EGBN-0001050441-26-000096-tables.json` and `EGBN-0001050441-26-000113-tables.json`.
- [FFIEC 041 September 2026 form](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC041_202609_f.pdf), pages 50 and 67; [current-form index](https://www.ffiec.gov/resources/reporting-forms/ffiec041).
- [Bulk selector](https://cdr.ffiec.gov/Public/PWS/DownloadBulkData.aspx), [publication timing](https://www.cdr.ffiec.gov/Public/HelpFiles/WelcomeAdditionalInfo.htm), and [PWS API specification](https://cdr.ffiec.gov/public/Files/SIS611_-_Retrieve_Public_Data_via_Web_Service.pdf), §3.1; accessed November 11.

Work: three historical FDIC population pulls, two full SEC filings, regulator form/dictionary checks, and an actual bulk-product selection. No sub-agents. Python requests returned 403 on the bulk page; normal curl GET/postback worked. The precise RC-R cells narrowed arithmetic but did not solve the scope mismatch; no unsupported explanation was selected. Further full-population work remains registered under 003R.

## Recipient actions

- REGINALD: Consume the fixed-history placement and the RC-N/RC-R limits. Keep exact EagleBank reconciliation unresolved.
- GIBBS, CREED, WAL, OZK, FLG and RED: Use the stated comparison dates and complete-case denominators when citing this placement.
- TERRY: Retain these limits alongside the earlier tradeability packet. This is no new predictive signal or trade instruction.
- PROME and WALTER: Record this leg as delivered. Keep 003R PARTIAL and preserve its existing scope and overdue history.

**Do-not-relay-as:** a current-Q3 peer ranking, probability of failure, exact EagleBank bridge, evidence of misstatement, absence of individual Q3 data, or a completed full-band rerun.
