# Q3 bank population: larger-band trigger off quarter to quarter; smaller-bank move concentrated

**Date:** 2026-11-11 | **Mode:** Thesis | **Request:** REQ-DEWEY-20261022-003R / DOCKET L1119 | **Authority:** Will's instruction to investigate remaining obtainable evidence. **Confidence:** High on retrieved filing cells and arithmetic; Medium on cross-era comparison; UNKNOWN on the exact EagleBank bridge and United Fidelity's underlying reason for its accounting/status change.

## Key finding

**The six-bank sample does not describe the whole $10–100 billion band.** In the complete Q3 extraction, that band's coverage improves from **115.97% to 116.76%**, while its problem-loan share edges down from **1.164% to 1.163%**. The original quarter-over-quarter trigger is **OFF**. The year-over-year trigger remains **ON**, extending the original G1 episode from 10 to 11 quarters through 2026Q3. [S1/S2; unchanged original trigger definition]

The **$1–10 billion band deteriorates**: coverage falls from 150.78% to 126.72%, and problem loans rise from 0.866% to 1.031% of loans. But **United Fidelity Bank accounts for 69.1% of the dollar increase in that band's noncurrent loans**. Its filing says approximately $2.14 billion of multifamily loans were current before being placed on nonaccrual cash-basis accounting. The filing also reports substantial multifamily charge-offs. **Do not describe the entire reported nonaccrual jump as newly missed payments, or dismiss it as harmless accounting.** Excluding that bank at both dates, smaller-bank coverage still falls, from 150.41% to 143.53%, and the problem-loan share rises from 0.867% to 0.912%. [S1/S2/S4]

This completes the **full-population Q3 band and contemporaneous-placement leg**, using all 4,267 reporters marked filed in the September 30 panel. It does **not** solve the exact EagleBank reconciliation or overturn the original finding that declining coverage alone had no useful standalone predictive contribution at the requested horizon.

## 1. Complete current population and unchanged group definitions

The reporting panel contains 4,268 institutions; 4,267 were marked filed and all 4,267 were retrieved, with no missing or duplicate RSSDs. The sole unfiled reporter is Paxos, an uninsured national trust bank excluded from the insured-bank comparison. Each raw file's hash, financial-row reporting date and bank identifier, and extracted values passed validation. Retrieval window: **November 11, 20:00:04–22:02:15 UTC**. Filings may subsequently be amended. [S1/S5]

All amounts underpinning the calculations are $thousands. Coverage=allowance/noncurrent loans; noncurrent=nonaccrual plus 90+ days still accruing. Problem-loan share=noncurrent/gross loans. Ratios are sums over banks, not average-bank ratios. G1 is nominal $10–100 billion; G1x excludes card specialists (>25% of gross loans in cards); G1r uses the original fixed 2026Q2-dollar deflator reference; G2 is $1–10 billion. OI/NC are excluded as before. Membership changes each quarter. [S1–S3; `research/2026-11-11_003R-population/METHOD.md`]

| Group | Banks Q2→Q3 | Coverage Q2→Q3 | Problem-loan share Q2→Q3 | Annualized quarterly NCO Q2→Q3 | Annualized quarterly provisions Q2→Q3 | QoQ / YoY trigger |
|---|---:|---:|---:|---:|---:|---|
| G1 | 126 → 124 | 115.97% → 116.76% | 1.164% → 1.163% | 0.362% → 0.330% | 0.331% → 0.369% | OFF / ON |
| G1x | 122 → 120 | 100.26% → 100.22% | 1.149% → 1.147% | 0.239% → 0.219% | 0.204% → 0.248% | OFF / ON |
| G1r | 126 → 123 | 115.97% → 116.71% | 1.164% → 1.164% | 0.362% → 0.330% | 0.331% → 0.370% | OFF / ON |
| G2 | 890 → 889 | 150.78% → 126.72% | 0.866% → 1.031% | 0.296% → 0.406% | 0.388% → 0.453% | ON / ON |

[S1/S2, DEWEY calculation.] Both components must move in the specified direction, using unrounded values. G1x coverage falls slightly, but its problem-loan share also falls, so the quarterly conjunction is OFF. The September 2025 baselines and every aggregate numerator/denominator are saved in `population-calculations.json`.

Current quarterly flows are Q3 FFIEC YTD minus June FDIC YTD, by certificate. Every current group member has a complete flow/loan pair. Provisions use **RIADJJ33**, which matches FDIC ELNATR, not loan-only RIAD4230. June's original counts and rates reproduce. These de-cumulated flows are not a direct retrieval of FDIC's still-unavailable Q3 quarterly fields; merger accounting and reporting revisions remain comparability limits. The stock-ratio triggers do not depend on this flow calculation. [S1/S2]

## 2. United Fidelity concentration and the sensitivity check

United Fidelity Bank, FSB: certificate 29566, RSSD 391575. This is an **as-filed contribution check prompted by the large aggregate move**, not a newly registered exclusion rule.

| Primary item ($thousands unless stated) | June 30 | September 30 |
|---|---:|---:|
| Gross loans, RCFD2122 | 3,436,066 | 3,059,390 |
| Nonaccrual, RCFD1403 | 16,211 | 2,159,092 |
| 90+ days accruing, RCFD1407 | 480 | 1,704 |
| Total noncurrent | 16,691 | 2,160,796 |
| Allowance, RCFD3123 | 81,707 | 6,323 |
| YTD net charge-offs, RIAD4635−4605 | 139 | 362,593 |
| YTD broad credit-loss provisions, RIADJJ33 | 0 | 319,000 |

The **fresh November 11 retrieval of June's FFIEC filing reproduces the FDIC baseline**, so this comparison is not explained by a June amendment missing from the FDIC feed. September's RCON3501 records **$2.143246 billion of domestic multifamily nonaccrual loans**. RCN total, multifamily detail and regulatory-capital delinquent/nonaccrual exposures corroborate the scale within the filing. RIAD3588 separately reports **$362.453 million YTD domestic multifamily charge-offs**. [S4]

Crucially, explanatory field **TEXT4769** says the roughly $2.14 billion portfolio was current before entering nonaccrual cash-basis treatment; cash receipts are recognized as interest income and may continue contributing income. That is the bank's explanation, not an independent loan-level audit. The filing does not establish that every affected borrower newly missed payment, why the treatment changed, or future recoveries. Charge-offs remain reported losses; the explanation does not erase them. [S4]

The band's total noncurrent increase is **$3.102326 billion**; United Fidelity contributes **$2.144105 billion**, or 69.1%. Excluding it from both quarterly groups gives:

| G2 excluding United Fidelity, diagnostic only | Q2 | Q3 |
|---|---:|---:|
| Banks | 889 | 888 |
| Coverage | 150.41% | 143.53% |
| Problem-loan share | 0.867% | 0.912% |
| Annualized NCO rate | 0.297% | 0.325% |
| Annualized provision rate | 0.389% | 0.382% |

The quarterly stock-ratio trigger remains ON without United Fidelity, but the change is much smaller; the provision rate declines in this sensitivity. Holding G2's **874 common banks** fixed also retains the headline direction: coverage 150.46%→126.78%, problem-loan share 0.873%→1.030%. Thus membership changes alone do not explain the as-filed deterioration. These are post-hoc diagnostics, not replacements for the canonical groups or a new predictive test. [S1/S2; `g2-sensitivity.json`, `g2-contribution-check.json`]

## 3. Historical band placement

Fresh 146-quarter coverage series reproduce the original June percentiles. Q3 values are compared with the **unchanged 1990Q1–2026Q2 benchmark**, excluding Q3 itself. Percentile=percentage of observations strictly lower. This updates descriptive placement, not the historical episode regressions.

| Q3 group | Coverage | Percentile vs 1990–2026Q2 (n=146) | vs 1990–2019 (n=120) | vs 2020–2026Q2 (n=26) |
|---|---:|---:|---:|---:|
| G1 | 116.76% | 41.1 | 48.3 | 7.7 |
| G1x | 100.22% | 45.2 | 54.2 | 3.8 |
| G1r | 116.71% | 48.6 | 55.0 | 19.2 |
| G2 | 126.72% | 39.0 | 47.5 | 0.0 |

[S1–S3.] G2's as-filed value is below every observation in the 26-quarter post-2020 benchmark. **That comparison includes the United Fidelity concentration and accounting-status qualification above.** The pre-2020 columns cross the CECL accounting break and cannot be read as like-for-like loss cushions. Aggregate group ratios are not directly comparable to a single bank's risk.

## 4. Original six banks against the actual Q3 population

The Q3 comparison contains **1,012 eligible insured banks**: assets ≥ $1 billion, loans ≥ 10% of assets, positive noncurrent loans and a reported allowance. Missing allowances are excluded, never treated as zero. All six Q3 ratios reproduce the earlier individual pulls. These are current-quarter descriptive percentiles, replacing neither the fixed-June historical comparison nor its explicitly dated values.

| Bank | Q3 coverage | Banks strictly lower / valid population | Q3 percentile |
|---|---:|---:|---:|
| SouthState | 199.66% | 512 / 1012 | 50.6 |
| Valley | 109.75% | 271 / 1012 | 26.8 |
| Huntington | 148.59% | 401 / 1012 | 39.6 |
| EagleBank | 67.20% | 125 / 1012 | 12.4 |
| BankUnited | 50.92% | 74 / 1012 | 7.3 |
| Zions | 204.28% | 523 / 1012 | 51.7 |

[S1; `q3-placements.json`.] EagleBank's current-Q3 percentile is 12.4, versus 10.8 when its same Q3 ratio was compared with June's distribution. Those are different benchmark populations, not a revision to the same percentile. Government-guaranteed exposures, loan mix and issuer/bank definition differences remain important; earlier Huntington/BankUnited guarantee adjustments are not refreshed here. No percentile is a failure probability.

## 5. Completion boundary and counter-evidence

**Delivered:** the full filed-panel assembly, all four group triggers, historical-band comparison and current-Q3 six-bank placement. **Still UNKNOWN:** the exact EagleBank RC-N versus RC-R/issuer bridge. The earlier $135K/$167K differences and zero HFS-nonaccrual memo remain unexplained; do not assign fees, rounding, parent consolidation or misstatement. The old approximate Valley 131%→117% relay remains unreproduced and must not be revived. See `output/2026-11-11_003R-source-and-definition-check.md`.

The original study's lack of standalone predictive lift remains the relevant counter-evidence. G1's QoQ result now provides direct evidence against extrapolating six falling bank ratios into a worsening larger-band aggregate. G2's concentration and explicit cash-basis explanation constrain a broad stress narrative. None of this establishes benign credit quality, future loss severity, or a trade.

## Sources and evidence archive

All derived artifacts below are under `research/2026-11-11_003R-population/`.

- **S1 PRIMARY, FFIEC CDR:** [Public data site](https://cdr.ffiec.gov/public/), [API specification](https://cdr.ffiec.gov/public/Files/SIS611_-_Retrieve_Public_Data_via_Web_Service.pdf). `panel.json`, `retrieval-summary.json`, `manifest.jsonl.gz`, `call-reports-sdf.tar.gz`, `current-bank-rows.tsv`, and final validation JSON preserve reporter identity, full source, timestamps, hashes and chosen MDRMs. All 4,267 sources passed checks; no missing financial fields in the selected groups. Archive receipt records member/hash verification.
- **S2 PRIMARY, FDIC BankFind:** [Financials API](https://api.fdic.gov/banks/financials). Whole-date June 2026/September 2025 and preceding-quarter baselines, Q3 zero-row availability response, and current institution classifications are saved with exact query and retrieval metadata. `history-json.tar.gz` plus `history/retrieval.jsonl` preserve 146 quarters / 188,337 bank-quarter observations; historical hashes, dates and counts passed. The baseline scan excludes OI/NC as in the original study.
- **S3 PRIMARY, FRED:** [GDPDEF](https://fred.stlouisfed.org/series/GDPDEF), retrieved November 11 via existing `scripts/fred_pull.py`; `gdpdef-history.csv`. Fixed denominator 133.411; Q3 deflator 134.127. No change to the original real-band reference.
- **S4 PRIMARY, United Fidelity:** Q3 source member `391575.sdf.gz`; fresh June source `ufb-20260630.sdf.gz` and `ufb-june-fresh-check.json`; exact cells and explanatory text in `ufb-core-rows.json`, `ufb-rcn-rows.json`, `ufb-explanation-and-chargeoffs.json`. Q3 cells last updated October 30. Commentary is issuer-supplied, not independently audited here.
- **S5 PRIMARY scope checks:** [OCC Paxos conversion approval](https://www.occ.gov/news-issuances/news-releases/2025/nr-occ-2025-125e.pdf); NIC records for new uninsured trust reporters linked in `new-trust-exclusions.json`. The sole unfiled reporter is excluded by scope, not assumed immaterial from unknown asset size.

`METHOD.md` gives the complete reproduction recipe; calculation JSON saves underlying sums, complete-case counts, memberships and percentile lower counts. No ephemeral scratch path is a report dependency.

## Process report and recipient actions

The individual-report route took about two hours because the bulk selector still lacked Q3 and the FDIC endpoint returned no Q3 rows. The source was not hung. Sequential retrieval respected the published pacing guidance. A separate historical refresh reproduced the original benchmarks. Full-set integrity checks passed. The large G2 move triggered a contribution/sensitivity check, a fresh June United Fidelity pull, and a read of its explanatory text; this changed the interpretation materially. Targeted web searches did not establish the underlying reason for United Fidelity's treatment change; third-party reproductions were not used as the numerical spine. No subagents, new production helper, watcher, paid source or external contact.

**REGINALD:** consume the completed population leg and the United Fidelity as-filed concentration/explanatory qualification; preserve the UNKNOWN mechanism and EagleBank bridge. **GIBBS, CREED, WAL, OZK, FLG and RED:** use the full-band divergence and concentration caveat; do not relay this as uniform bank deterioration. **TERRY:** descriptive evidence only, no trade construction proposed. **PROME:** mark the population/historical/current-placement residual delivered; exact EagleBank reconciliation remains UNKNOWN under the existing commission, with no invented deadline or watcher. **WALTER:** log the research continuation and verify recipient pointers. Delivery does not establish consumption.
