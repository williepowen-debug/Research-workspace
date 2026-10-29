# CARL-DR-1: Bread Q3 modification tables; Capital One still pending

**Date:** 2026-10-28 | **Mode:** Thesis | **Commission:** existing CARL-DR-1 / DOCKET L567, deliver by November 13. **Status:** Bread Q3 delivered (Synchrony Q3 delivered 10/25); Capital One Q3 pending filing. **Confidence:** High on disclosed amounts and arithmetic; class-wide causal delinquency effect NOT COMPUTABLE.

## Key finding

Bread's recent modified-card cohort had **$251 million classified current at September 30, 2026**, versus $264 million at June 30. That equals **139.20 basis points of its $18,031 million credit-card book**, down from the June scale comparison of 148.25 basis points. This is a changing, selected cohort's size, **not measured hidden delinquency, a causal effect, or a ceiling on masking**. Capital One's latest 10-Q in the SEC submissions feed is still the June-quarter filing (filed July 28), retrieved 2026-10-29 02:09 UTC. [PRIMARY: Bread Financial Q3 10-Q, filed October 27, Note 2, pp.36–39](https://www.sec.gov/Archives/edgar/data/1101215/000110121526000092/bfh-20260930.htm); dated SEC checks below.

## Evidence

All dollar amounts are **millions**. Credit-card loans only: Bread's "other loans" (installment and split-pay, $819M at September 30) are outside the modification tables and the denominator. Q2 is April–June, Q3 July–September. The performance table is a trailing-12-month cohort of loans still in a program on the stated date. It does not follow the same borrowers through time. [PRIMARY: Q3 Note 2, p.39; Q2 comparison from `research/2026-10-12_cards/BFH-Q2-2026-tables.json`, Bread June-quarter 10-Q.]

| Metric and basis | June 30 / Q2 2026 | September 30 / Q3 2026 |
|---|---:|---:|
| Quarter's modifications still in program at period end | 89 (0.5% of card loans) | 90 (0.5%); Q3-2025: 100 (0.6%) |
| Year-to-date modifications still in program at period end | 196 (six months, 1.1%) | 251 (nine months, 1.4%); 9M-2025: 258 (1.5%) |
| Weighted-average interest-rate reduction, quarter | 23.5 percentage points | 23.9 percentage points |
| Recent still-program cohort: current | 264 | 251 |
| Same cohort: 30–59 / 60–89 / 90+ days delinquent | 21 / 17 / 23 | 20 / 18 / 20 |
| Same cohort: total 30+ days delinquent | 61 | 58 |
| Same cohort: total | 325 | 309 |
| Credit-card loans denominator | 17,808 | 18,031 |
| Current cohort / card book, derived basis points | 148.25 | **139.20** |
| Subsequent default within 12 months of modification, balance | 26 (six months) | 14 (quarter); 29 (nine months) |

The scale ratio is `current card cohort / credit-card loans × 10,000`, the same formula and denominator line as the October 12 Q2 report. **Basis note, which also applies to Q2:** the cohort is at amortized cost, while the "Credit card loans" line is carrying value. Carrying value includes unbilled interest and fees ($404M across card and other loans at September 30). The filing gives no card-only amortized-cost total. The ratio is therefore a slightly understated scale marker, consistent across both quarters. [PRIMARY: Q3 Note 2, p.36 loans table and footnote 2; p.39 cohort table.]

**Bread's modification amounts are not enrollment flows.** The 90/251 rows are September-30 balances of modifications made in the past three or nine months that are still in a program. They include accrued interest and fees. Synchrony's comparable rows use enrollment-date balances, so the two issuers' "quarter" rows are not the same measure. Do not pool them. [PRIMARY: Q3 Note 2, p.39 footnote 1.]

**Default-window warning (same pattern as Synchrony on 10/25):** Q3 reports $14M for the quarter and $29M for nine months. The Q2 table reported $26M for six months. Nine months minus six months is $3M, not the separately reported $14M quarter. Each disclosure selects modifications from the 12 months before its own balance-sheet date, and the filing gives no bridge. Use the disclosed quarter directly and do not build one by subtraction. These are balances, not default rates. The count of defaulted modifications is 6,764 for Q3-2026, against 7,124 for Q3-2025. [PRIMARY: Q3 Note 2, p.39.]

**Re-aging, a separate and overlapping practice:** re-aged accounts were **2.8%** of total card-and-other loans for Q3-2026 (2.9% for Q3-2025) and 3.1% for nine months (3.2%). Re-aging returns a delinquent balance to current after qualifying payments. It overlaps modification and relief in an amount the filing does not state, so it cannot be added to the cohort ratio. Bread also runs temporary consumer-relief programs outside the modification tables, under which "accounts receiving relief may not advance to the next delinquency cycle, including charge-off, in the same time frame." [PRIMARY: Q3 Note 2, pp.37 and 38.]

**Portfolio context (not part of the leg):** the delinquency rate was 5.57% at September 30 (5.75% at December 31, 2025). The net principal loss rate was 6.40% for Q3-2026 (7.39% for Q3-2025). [PRIMARY: Q3 Note 2, pp.37–38.]

## What remains unanswered

Note 2 provides no matched untreated counterfactual and no loan-level status or payment history that would show how much delinquency relief alone prevented. Temporary relief programs, re-aging and exits sit outside or overlap the disclosed cohort in amounts the filing does not state. Allowances estimate lifetime losses on modified loans separately from delinquency status (Note 3), so a current classification does not show delayed loss recognition. **No newly published counterfactual or loan-level evidence appears in this filing** (CARL's October 12 ASK).

The three-issuer refresh remains PARTIAL: Synchrony and Bread are delivered. [Capital One's submissions feed](https://data.sec.gov/submissions/CIK0000927628.json), retrieved 2026-10-29 02:09 UTC, lists its latest 10-Q as the June 30 report (accession 0000927628-26-000089, filed July 28). That describes the feed at retrieval, not a forecast of a filing date. CARL alone owns the combined class-wide 50-basis-point test. No confirm, miss or ceiling follows from this update.

## Counter-evidence

Both directions apply:
- **Against reading relief as concealed deterioration:** the current cohort fell ($264M to $251M) while the card book grew, delinquent cohort balances fell ($61M to $58M), 90+ balances fell ($23M to $20M), and the portfolio net loss rate is about a point lower year on year.
- **Against reading the fall as improvement:** selected rolling cohorts, successful exits, temporary relief outside the table and re-aging can all shrink the cohort without any change in borrower capacity. These tables cannot refute masking either.

No cross-issuer pooling or causal attribution is justified.

## Source quality, reproduction and process report

**Primary source:** Bread Q3 10-Q, accession `0001101215-26-000092`, report date September 30, filed October 27, read in full from SEC. **Q2 comparison:** the retained June-quarter tables at `research/2026-10-12_cards/BFH-Q2-2026-tables.json`, re-read 10/28 to confirm the June row (264 current + 61 delinquent = 325). The December 31, 2025 row also totals 325 (253 + 72). The two match by coincidence, not by a misread.

**Saved evidence:** `research/2026-10-28_cards/` holds the full BFH Q3 HTML, the derived text, both submissions responses and `BFH-Q3-2026-tables.json`, which carries the extracted values, source URLs, UTC retrieval time and SHA256 hashes. Reproduce the filing check with `scripts/edgar_fetch.py 1101215 --type 10-Q --limit 2`, then fetch the document and read Note 2's full tables, not keyword hits alone.

**Work:** two issuer feed checks and one full filing pull with existing primary-pull tools; no web searches or sub-agents. **Gaps:** Capital One Q3 not yet filed; causal counterfactual and overlap map unavailable. **Confidence:** high on table readings; this is not a causal test. **Next:** read Capital One once it files and deliver the consolidated three-issuer refresh by November 13. No new collection is proposed.
