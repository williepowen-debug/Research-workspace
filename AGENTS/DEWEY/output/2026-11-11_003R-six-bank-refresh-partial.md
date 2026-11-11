# Q3 reserve-coverage rerun: six banks verified; full-band work remains open

> **Same-day continuation:** `output/2026-11-11_003R-historical-placement-and-bridge.md` delivers the historical-placement leg and narrows the EagleBank arithmetic with exact RC-R cells. RC-N/RC-R definitions differ and the HFS nonaccrual memo is zero; exact reconciliation remains unproved. Full-population Q3 work remains open. The earlier rounded bridge below is not an exact reconciliation.

**Date:** 2026-11-11 | **Mode:** Thesis | **Request:** REQ-DEWEY-20261022-003R | **State:** PARTIAL | **Confidence:** High on retrieved Call Report totals; Medium on the company/bank reconciliation; no updated full-universe result.

## Key finding

**The original six-bank pattern persists in Q3 on a consistent bank-level basis:** noncurrent loans and their share of loans rose at all six banks, while allowance coverage fell at all six. This verifies the descriptive pattern, not its predictive value. REGINALD's October 30 decision to give the coverage decline zero standalone predictive weight is not re-graded here.

The full historical-band/placement rerun remains unfinished. FDIC BankFind returned zero Q3 rows, while FFIEC lists **4,267 filing institutions out of 4,268 panel members**. Individual filings are available; “Q3 data unavailable” would be false. The existing FDIC-based full-universe computation has not been replaced with a newly assembled FFIEC universe.

## Fresh six-bank evidence

Source: twelve fresh FFIEC CDR `RetrieveFacsimile` SDF responses, June 30 and September 30, 2026, retrieved November 11. Bank-level, not parent-company data. Raw input rows, RSSDs, dates and response hashes are saved in `research/2026-11-11_003R/six-bank-primary-rows.json`.

Definition unchanged from REQ-003: **noncurrent = nonaccrual + 90+ days past due while accruing**; coverage = loan allowance / noncurrent. MDRMs: 1403 + 1407, 3123, and gross loans 2122. Use consolidated RCFD when reported, otherwise RCON; do not mix HBAN's domestic and consolidated loan denominators. Dollar figures below are **$ millions**; ratios are calculated from $thousands.

| Bank | Noncurrent June → September | Coverage June → September | Noncurrent / loans June → September |
|---|---:|---:|---:|
| SouthState | 274.411 → 294.964 | 213.79% → 199.66% | 0.535% → 0.563% |
| Valley | 478.695 → 528.722 | 123.27% → 109.75% | 0.912% → 0.994% |
| Huntington | 2,026.598 → 2,168.632 | 160.30% → 148.59% | 1.060% → 1.124% |
| EagleBank | 136.915 → 179.722 | 88.48% → 67.20% | 2.052% → 2.733% |
| BankUnited | 403.707 → 434.951 | 53.88% → 50.92% | 1.687% → 1.826% |
| Zions | 295.451 → 316.207 | 224.15% → 204.28% | 0.472% → 0.506% |

This is the **original six**, not a claim that all regional banks deteriorated. REGINALD's broader issuer-read cohort had counterexamples; its October 30 report records 7 of 10 worsening, with Amerant, Customers and First Citizens moving the other way. That owner result was read, not independently refreshed here. No new rank, threshold, score or trade is assigned.

## Two definition reconciliations

**EagleBank:** REGINALD's November 6 filing read identified held-for-sale nonaccrual loans as the main denominator difference. DEWEY independently retrieved Eagle Bancorp's Q2 and Q3 10-Qs and verified the nonperforming-assets table footnotes. The issuer excludes **$25.6M at June 30 and $13.5M at September 30** of nonaccrual loans held for sale. It reports nonperforming loans of **$111.124M and $166.021M**, and coverage of **109% and 73%**. Compare bank Call Report nonaccrual of $136.915M and $179.722M.

The bridges using the rounded HFS disclosures leave **$0.191M and $0.201M**, respectively. The major difference is therefore explained, but an **exact dollar-for-dollar bridge remains unresolved**. These residuals exceed the $0.05M rounding interval of a one-decimal-million disclosure; do not declare rounding alone the explanation. Do not silently replace the bank denominator with the issuer's held-for-investment denominator. Saved SEC excerpts and hashes: `research/2026-11-11_003R/EGBN-*.json`.

**Valley:** the original 123.3% was the June **bank allowance / noncurrent** ratio, now reproduced as 123.27%. June bank **nonaccrual-only** coverage is 127.55%, falling to 113.47% in September; parent figures in REGINALD's November 6 10-Q read are $590.600M and $580.800M of allowance against $462.629M and $511.390M of nonaccrual, or 127.66% and 113.57%. The bank allowance is $0.528M lower at each date. **The old approximately 131% → 117% relay is not reproduced on any of those definitions and must not be cited as a reconciled company series.** Parent figures here are attributed to REGINALD's filing read; the bank figures were freshly pulled by DEWEY.

## What remains, and why this is not a completed rerun

| Required leg | Disposition |
|---|---|
| Does the original six-bank pattern persist? | Answered from twelve fresh bank filings above. |
| Explain EGBN 88.5% versus 109% | Main difference independently verified: HFS exclusions. Exact residual remains open. |
| Treat the old VLY relay explicitly | Answered: retain separate valid definitions; old approximate relay not reproduced. |
| Q3 historical-percentile placement and full-band trigger | **Not computed.** The six-bank sample cannot substitute for the original full population. |

FDIC query and raw zero-row response are saved alongside the two FFIEC panel/filers responses. FFIEC's published help says bulk Call Report files begin **45 calendar days after quarter-end**—November 14 for September 30. Its bulk page observed November 11 still showed a Call update of October 15. That is a publication schedule and observed page state, **not proof that no individual-file assembly is possible or a guaranteed release date**. No bulk Q3 file was retrieved in this pass. Preserve the original commission and overdue history; do not close it or invoke its unavailable-Q3 rule merely because BankFind is empty. Next existing-work step is a validated full-population Q3 extract, followed by the original definitions and comparison populations. No watcher, collector or new study has been created.

## Counter-evidence and limits

- Coverage declines did not independently predict losses in the original historical study; six fresh descriptive observations do not overturn that result.
- Noncurrent totals can include government-guaranteed loans. The original report identified substantial guarantee effects at BankUnited and Huntington; those adjustments are not refreshed here. These are the original unadjusted definitions, not estimates of unprotected loss exposure.
- CECL changed reserve accounting in 2020. Cross-era levels remain non-comparable without the original caveats; no historical failure probability is attached to the fresh ratios.
- Bank and parent scopes differ; EagleBank's residual is explicitly unresolved. Nonaccrual balances are not realized losses.

## References and process report

- [FFIEC CDR](https://cdr.ffiec.gov/public/): `https://ffieccdr.azure-api.us/public/RetrieveFacsimile`, `RetrievePanelOfReporters`, `RetrieveFilersSinceDate`; authenticated read-only pulls, November 11. Reused `AGENTS/REGINALD/scripts/mi3_cohort_screen.py` retrieval/parser functions without running its workbook writer or editing owner files.
- [FDIC financials API](https://api.fdic.gov/banks/financials): REPDTE 20260930, limit 10000; exact URL and timestamp in `research/2026-11-11_003R/retrieval.json`.
- [FFIEC publication timing](https://www.cdr.ffiec.gov/Public/HelpFiles/WelcomeAdditionalInfo.htm) and [bulk page](https://cdr.ffiec.gov/Public/PWS/DownloadBulkData.aspx), accessed November 11.
- Eagle Bancorp SEC accessions `0001050441-26-000096` and `0001050441-26-000113`; exact document URLs and source hashes in the saved evidence.
- `AGENTS/REGINALD/reports/2026-10-30_L801/REPORT.md`, `AGENTS/REGINALD/reports/2026-11-01_Q3-call-report_VLY-EGBN-HBAN/REPORT.md`, and `AGENTS/REGINALD/reports/2026-11-06_VLY-EGBN_10Q_reads.md` read for existing work and corrections.

One targeted web search on bulk retrieval, primary filing pulls and direct API reads; no sub-agents. Two EGBN filings were retrieved twice to capture the exact HFS footnotes after an initial phrase search missed the abbreviation. No source-access cost. The useful new result is six-bank verification and narrower reconciliation; the full-population computation and exact EGBN residual remain unfinished.

**Do-not-relay-as:** 003R completed, all regional banks worsening, Q3 reports unavailable, falling coverage predicting losses, exact EGBN reconciliation completed, or an authenticated 131% → 117% Valley series.

## Recipient actions

- REGINALD: REGINALD consumes the six-bank refresh and the explicit EGBN and VLY definition limits.
- GIBBS: GIBBS retains this report as information. No new research assignment is created.
- CREED: CREED retains this report as information. No new research assignment is created.
- WAL: WAL retains this report as information. No new research assignment is created.
- OZK: OZK retains this report as information. No new research assignment is created.
- FLG: FLG retains this report as information. No new research assignment is created.
- RED: RED retains this report as information. No new research assignment is created.
- TERRY: TERRY assesses tradeability within the existing evidence limits. No coverage-based predictive claim or trade is authorized.
