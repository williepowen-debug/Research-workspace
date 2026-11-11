# CARL-DR-1: Capital One Q3 modification tables and the three-issuer card refresh

**Date:** 2026-11-04 | **Mode:** Thesis | **Commission:** existing CARL-DR-1 / DOCKET L567, deliver by November 13. **Status:** three-issuer Q3 card refresh COMPLETE (Synchrony 10/25, Bread 10/28, Capital One here). **Confidence:** High on disclosed amounts and arithmetic; Low on why the Capital One cohort moved (the filing gives no reason); class-wide causal delinquency effect NOT COMPUTABLE.

## Key finding

**The recent modified-card cohort at Capital One deteriorated sharply in one quarter, and the filing does not say why.** Delinquent balances in its domestic card cohort rose from **$645 million at June 30 to $993 million at September 30 (+54.0%)**, while delinquent balances in the whole domestic card book rose 11.1%. In the same quarter of 2025 the two moved together (+8.8% and +8.9%). The delinquent share of the cohort is **25.2%, against 15.7–18.0% at each of the five prior period-ends**. Synchrony and Bread show no matching move. This is one quarter at one issuer. It is **not measured hidden delinquency, a causal effect, or a ceiling on masking**, and the whole-book delinquency rate is lower than a year ago. [PRIMARY: Capital One Q3 10-Q, filed November 3, Note 4, Table 4.1 and modification Tables 4.7–4.10, pp.96–102](https://www.sec.gov/Archives/edgar/data/927628/000092762826000152/cof-20260930.htm)

The scale ratio CARL asked for is **113.31 basis points at Capital One (June 119.27)**: $3,041 million current on a $268,376 million card book. ⚠️ That fall is not a benign reading on its own: the current balance fell while delinquent balances rose and the cohort total increased from $3,896 million to $4,104 million. These changing rolling groups do not establish same-account migration. **Causal-language correction, November 11:** the earlier claim that migration mainly caused the fall is withdrawn; see `output/2026-11-11_capital-one-discover-cause-addendum.md`.

## Evidence

All dollar amounts are **millions**, card only. Capital One personal loans are excluded from numerators and denominators, as in the October 12 report. Capital One figures include international cards unless marked domestic.

### Three issuers, June 30 and September 30, 2026

| Metric and basis | Capital One Jun | Capital One Sep | Synchrony Jun | Synchrony Sep | Bread Jun | Bread Sep |
|---|---:|---:|---:|---:|---:|---:|
| Cohort: current | 3,182 | **3,041** | 971 | 948 | 264 | 251 |
| Cohort: 30+ days delinquent | 714 | **1,063** | 288 | 294 | 61 | 58 |
| Cohort: 90+ days delinquent | 333 | **463** | 132 | 125 | 23 | 20 |
| Cohort: total | 3,896 | **4,104** | 1,259 | 1,242 | 325 | 309 |
| Delinquent share of cohort, derived | 18.3% | **25.9%** | 22.9% | 23.7% | 18.8% | 18.8% |
| Card-book denominator | 266,789 | 268,376 | 94,233 | 95,526 | 17,808 | 18,031 |
| Current cohort / card book, derived bp | 119.27 | **113.31** | 103.04 | 99.24 | 148.25 | 139.20 |

**Do not pool these issuers.** Measurement bases differ, and the prior reports' warnings stand: Capital One's cohort is amortized cost on a rolling 12-month basis, Synchrony's period amounts use enrollment-date balances, and Bread's are period-end balances. The denominators are also not one basis. [PRIMARY: Capital One as above; Synchrony and Bread per `output/2026-10-25_carl-dr1-syf-q3-fdm.md` and `output/2026-10-28_carl-dr1-bfh-q3-fdm.md`.]

### Capital One domestic card, by period-end

| Period-end | Cohort current | 30–59 | 60–89 | 90+ | Cohort delinquent | Cohort total | Delinquent share | Book 30+ rate, derived |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jun 30, 2025 ⚠️ | 3,423 | 200 | 141 | 297 | 638 | 4,061 | 15.7% | 3.60% |
| Sep 30, 2025 ⚠️ | 3,343 | 228 | 160 | 306 | 694 | 4,037 | 17.2% | 3.89% |
| Dec 31, 2025 ⚠️ | 3,250 | 221 | 164 | 328 | 713 | 3,963 | 18.0% | 3.99% |
| Mar 31, 2026 ⚠️ | 3,140 | 194 | 149 | 304 | 647 | 3,787 | 17.1% | 3.70% |
| Jun 30, 2026 | 3,098 | 210 | 147 | 288 | 645 | 3,743 | 17.2% | 3.39% |
| **Sep 30, 2026** | **2,955** | **350** | **225** | **418** | **993** | **3,948** | **25.2%** | 3.74% |

⚠️ These rows may hold loans modified before Discover closed on May 18, 2025. The September 2025 filing footnote puts that at $2.1 billion of the rolling table, and the rolling window should have excluded them by the June 2026 row. **Only the last two rows are clearly free of that effect, so the prior-year comparison is one imperfect observation.** [PRIMARY: Q3 10-Q Table 4.9 footnote 2; the five earlier rows from the filings listed under Reproduction.]

Every delinquency bucket moved: 30–59 days +66.7%, 60–89 days +53.1%, 90+ days +45.1%. The cohort accounts for **35.8% of the quarter's rise in domestic delinquent dollars** ($348 million of $971 million), against 6.9% a year earlier. Cohort delinquent balances are still small against the book: 38.16 basis points of domestic card loans, up from 24.90.

### Capital One modification and default flows

| Measure | Q2-25 | Q3-25 | Q1-26 | Q2-26 | Q3-26 |
|---|---:|---:|---:|---:|---:|
| Domestic loans modified in the quarter | 1,027 | 1,164 | 1,103 | 1,008 | **1,365** |
| % of domestic class | 0.41% | 0.46% | 0.43% | 0.39% | **0.52%** |
| International modified | 58 | 57 | 72 | 69 | 70 |
| Domestic subsequent defaults | 191 | 165 | 163 | 152 | **230** |
| International subsequent defaults | 23 | 23 | 24 | 26 | 26 |

Q3 domestic modifications rose 35.4% on Q2 and 17.3% on the year. Subsequent defaults rose 51.3% and 39.4%. A subsequent default is 90+ days delinquent, charged off, or moved to nonaccrual. The weighted-average rate cut on domestic modifications was 15.95 percentage points (Q2 15.42). Comparison rows are as originally filed. [PRIMARY: Q3 10-Q Tables 4.7, 4.8, 4.10; earlier filings as listed.]

**Do not subtract year-to-date modification rows.** Nine months ($3,143M) less six months ($2,001M) is $1,142M, not the disclosed quarter's $1,365M. The same gap existed in 2025 ($956M against $1,164M). The filing gives no bridge. Use the disclosed quarter directly.

## What remains unanswered

- **Why the cohort moved.** The filing does not explain it. A full text search of the filing found no stated program, definition or reporting change for these tables. A third-party copy of the Q3 call (2,685 lines) has zero matches for modification, hardship, forbearance, workout or re-aging, read untruncated. Absence from that copy is not proof it was never discussed. [UNVERIFIED: third-party transcript copy, retrieved 2026-11-04.]
- **Perimeter note.** Domestic Card has included Brex and the legacy corporate card since Q2 2026 (Q3 10-Q MD&A). June and September both carry that, so it does not by itself explain the June-to-September move. Whether Brex balances sit in this cohort is not stated.
- **Competing explanations the data cannot separate:** failed plans among recently modified borrowers; more borrowers entering programs already delinquent (the Q3 flow rose, and the tables do not show delinquency at entry); or Discover program, servicing or reporting mix. Each is a possibility, not a finding.
- **Class-wide effect.** No filing gives a matched untreated counterfactual or loan-level payment history, and temporary relief and re-aging overlap the cohorts by undisclosed amounts. **No newly published counterfactual evidence appears in this filing.** CARL alone owns the combined 50-basis-point test. No confirm, miss or ceiling follows from this report.

## Counter-evidence

- **Against reading this as broad consumer stress:** Capital One's domestic book rate of 3.74% is down 15 basis points on the year. On the Q3 call the CFO called the 35 basis point quarterly rise "in line with normal seasonality" and said charge-offs benefited from improving delinquencies and recoveries. The Credit Card segment's net charge-off rate fell 60 basis points on the year to 4.01%, and the allowance fell on a Domestic Card net release "due to favorable credit performance". [PRIMARY for the 4.01% and the allowance: Q3 10-Q MD&A. UNVERIFIED third-party transcript copy for the CFO's words.] ⚠️ Management also said delinquencies have lately moved with seasonality "as opposed to beating it", which ends a run of outperformance rather than reversing it.
- **Against reading it as class-wide:** Synchrony's delinquent share rose only from 22.9% to 23.7%, Bread's was flat at 18.8%, and Synchrony's default amount fell (88 to 84).
- **Against dismissing it:** the rise exceeds the book's, hits all three buckets, and arrives with higher modification and default flows. Management's seasonality remark describes the whole book, not this cohort.

## Source quality, reproduction and process report

**Primary source:** Capital One Q3 10-Q, accession `0000927628-26-000152`, filed November 3 (accepted 21:13 UTC), full document read directly from SEC. Tables tie: each row's buckets sum to its delinquent total and each row's current plus delinquent sums to its total, asserted in the build. **Earlier rows:** 10-Qs `0000927628-25-000247`, `0000927628-25-000276`, `0000927628-26-000048`; 10-K `0000927628-26-000024`; June 2026 from the retained `research/2026-10-12_cards/COF-Q2-2026-tables.json`.

**Saved evidence:** `research/2026-11-04_cards/COF-Q3-2026-tables.json` holds every value, source URL, byte count, SHA-256, retrieval time and the derived figures. The Q3 derived text and submissions feed sit beside it. Full filing HTML was not committed (6–9 MB each): reproduce from the URLs and hashes, reading Note 4's tables in full. Find the tables by their numbered captions, not by column headers.

**Work:** one issuer feed, five full filing pulls, one web search, two transcript fetches (one failed); no sub-agents. **Caught before writing:** Table 4.10 (defaults) has modification-type columns and reads like Table 4.7; its $230M is not a modification flow. A search summary labelled 3.99% as the year-ago rate; 3.99% is December 31, 2025, and the September 30, 2025 rate is 3.89%. An early transcript search was truncated at 10 hits and was re-run in full before the negative claim was written. **Gaps:** no primary call transcript; no reason for the move. **Confidence:** high on table readings, low on cause, none on causal effect. **If I had more:** a Capital One master-trust or supplement breakdown of legacy Discover versus legacy Capital One modified balances, if one exists; not searched here.

**Do not relay as:** hidden delinquency, a class-wide card signal, a Capital One credit break, or evidence of misstatement. Do not pool the three issuers. Do not call the 113.31 basis point fall an improvement.

**L567 state:** the three-issuer Q3 refresh is delivered. CARL owns what follows. No new collection is proposed.
