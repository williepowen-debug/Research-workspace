# CARL-DR-1: Synchrony Q3 modification tables; two issuers still pending

**Date:** 2026-10-25 | **Mode:** Thesis | **Commission:** existing CARL-DR-1 / DOCKET L567, deliver by November 13. **Status:** Synchrony Q3 delivered; Capital One and Bread Q3 pending filing. **Confidence:** High on disclosed amounts and arithmetic; class-wide causal delinquency effect NOT COMPUTABLE.

## Key finding

Synchrony's recent modified-card cohort had **$948 million classified current at September 30, 2026**, versus $971 million at June 30. That equals **99.24 basis points of its $95.526 billion card book**, down from the June scale comparison of 103.04 basis points. This is a changing, selected cohort's size, **not measured hidden delinquency, a causal effect, or a ceiling on masking**. Capital One and Bread still showed June-quarter 10-Qs as their latest in SEC submissions retrieved October 25. [PRIMARY: Synchrony Q3 10-Q, filed October 22, Note 4, pp.45/49–50](https://www.sec.gov/Archives/edgar/data/1601712/000160171226000043/syf-20260930.htm); dated SEC checks below.

## Evidence

All dollar amounts are **millions**. Card products only: commercial credit and installment loans are excluded. Q2 is April–June; Q3 is July–September. Period-end cohorts cover loans modified in the previous 12 months and still in a program at the stated balance-sheet date; they are not the same borrowers tracked through time. [PRIMARY: same Note 4; Q2 comparison from the retained tables and the July 23 10-Q cited below.]

| Metric and basis | June 30 / Q2 2026 | September 30 / Q3 2026 |
|---|---:|---:|
| Quarter's modified-card enrollment balances | 537 = 341 long-term + 196 short-term | 555 = 364 + 191 |
| Year-to-date modified-card enrollment balances | 1,153 (six months) | 1,708 (nine months) |
| Recent still-program cohort: current | 971 = 915 + 56 | 948 = 890 + 58 |
| Same cohort: 30–89 days delinquent | 156 = 127 + 29 | 169 = 138 + 31 |
| Same cohort: 90+ days delinquent | 132 = 100 + 32 | 125 = 94 + 31 |
| Same cohort: total 30+ days delinquent | 288 | 294 |
| Same cohort: total, derived | 1,259 | 1,242 |
| Total card-book denominator | 94,233 | 95,526 |
| Current cohort / card book, derived basis points | 103.04 | 99.24 |
| Long-term modified-card payment-default/charge-off amount, quarter | 88 | 84 |

The scale ratio is `current card cohort / total card receivables × 10,000`. The total modified-loan row in Q3 shows **$956 million current**, but includes $8 million of commercial credit; using it would change the numerator's product perimeter. The card-only numerator is $948 million. [PRIMARY: Synchrony Q3 Note 4, performance table p.50; book denominator at opening Note 4.]

**Keep three measurement bases separate.** Modification-period amounts use enrollment-date balances. The performance table covers the trailing-12-month cohort still in programs at September 30. The issuer's footnote also gives September-end balances of $914 million long-term and $120 million short-term for modifications made during the nine months; these are across loan classes and are neither the enrollment flows nor the card-only trailing cohort. They are not added to any row above. [PRIMARY: Q3 Note 4, p.49.]

Current status requires full minimum-payment catch-up or re-aging after three consecutive monthly program payments. Long-term programs reduced weighted-average interest rates by **97% relative**, not 97 percentage points. Short-term programs forgave $10 million in Q3 and $188 million over nine months for successful exits; 62% of short-term loans modified within the preceding 12 months had completed payments and exited during the nine months. These program measures are not untreated-cohort comparisons. [PRIMARY: Q3 Note 4, pp.49–50.]

**Default-window warning:** Q3 reports $84 million for the quarter and $188 million for nine months; the retained Q2 table reports $166 million for six months. Nine-month minus six-month is $22 million, not the separately reported $84 million quarter. Each disclosure selects enrollments from the 12 months preceding its own balance-sheet date. The filings do not provide a bridge for this difference. Use the disclosed quarter directly; do not manufacture it by subtraction or infer improved borrower outcomes from the mismatch. These are amounts, not default rates. [PRIMARY: Q3 p.50; retained Q2 table 69.]

## What remains unanswered

This Note 4 disclosure supplies no matched untreated counterfactual or complete loan-level status/payment history establishing how much delinquency was prevented solely by relief. Older programs, exits, temporary assistance and re-aging overlap remain outside a complete causal map. Allowances estimate lifetime expected losses, including modified loans, separately from delinquency classification. A current classification therefore does not establish delayed accounting loss recognition. No newly observed counterfactual resolves CARL's causal test in these tables. [PRIMARY: Q3 Note 4, allowance discussion and modification tables; CARL's October 12 methods instructions.]

The three-issuer refresh remains PARTIAL. [SEC Capital One submissions](https://data.sec.gov/submissions/CIK0000927628.json) and [Bread submissions](https://data.sec.gov/submissions/CIK0001101215.json) had no September 30, 2026 10-Q in the recent-filings arrays at this pull; latest filings remained July 28, reporting June 30. This states the checked feeds at the saved retrieval time, not a future filing-date forecast. CARL alone owns the combined class-wide 50-basis-point test. No confirm, miss or ceiling follows from this update.

## Counter-evidence

The current cohort is smaller in dollars while the card book is larger, and reported quarter default amounts are lower than Q2. Both argue against reading every relief-program balance as concealed deterioration. Conversely, selected rolling cohorts and incomplete relief coverage mean those changes cannot refute masking. Actual payments before re-aging matter; successful program exits remove borrowers from the still-program table. No cross-issuer pooling or causal attribution is justified.

## Source quality, reproduction and process report

**Primary source:** Q3 filing above, accession `0001601712-26-000043`, report date September 30, filed October 22. **Q2 comparison:** [Synchrony June-quarter 10-Q, July 23](https://www.sec.gov/Archives/edgar/data/1601712/000160171226000033/syf-20260630.htm), tables already preserved at `research/2026-10-12_cards/SYF-Q2-2026-tables.json`; original three-issuer analysis is `output/2026-10-12_carl-dr1-cards-q2-fdm.md`.

**Saved evidence:** `research/2026-10-25_catchup/` contains all three raw SEC submissions responses, the full SYF Q3 HTML, derived searchable text, and `sec_check.json` with source URLs, UTC retrieval times and SHA256 hashes. Reproduce the filing check with `scripts/edgar_fetch.py <CIK> --type 10-Q --limit 2`; fetch the exact Q3 document using `scripts/edgar_doc.py text 1601712 0001601712-26-000043 --doc syf-20260930.htm`. Read Note 4's full tables, not keyword hits alone.

**Work:** three issuer feed checks and one full filing pull, existing primary-pull tools; no web searches or subagents. **Source frustration:** sandbox DNS initially failed; the same SEC fetch succeeded with technical network approval. Contact address sent only to SEC hosts under WQ-488 EMAIL A. **Gaps:** two Q3 filings unpublished in the checked feeds; causal counterfactual and overlap map unavailable. **Confidence:** high on table readings, not a causal test. **Next:** complete COF/BFH after filing and deliver the consolidated existing commission by November 13; no new collection or research programme proposed.
