# WQ-537 cohort instrument — who is drawing down (first observation frozen 2026-10-29 09:31 ET fetch, before the 11/10 CPI)

## Instrument chosen: Fed Distributional Financial Accounts (DFA), deposits per household by income group

| Field | Value |
|---|---|
| Publisher / file | Federal Reserve Board, DFA, `dfa-income-levels-detail.csv` inside https://www.federalreserve.gov/releases/z1/dataviz/download/zips/dfa.zip (fetched 2026-10-29 09:31 ET, $0; zip sha256 e7f35451dc4d…; member files dated 2026-09-15; DFA page "Last Update: September 18, 2026") |
| Saved | `source/dfa-income-levels-detail.csv`, `source/dfa-data-definitions.txt`, hashes in `source/SHA256SUMS.txt` |
| Columns used | `Deposits`, `Consumer credit`, `Household count` ($ millions, nominal, end of quarter) by income percentile group (pct00to20 … pct99to100) |
| Statistic | **Deposits per household, YoY %, bottom 40% of income minus top 20%** (gap in pp), computed within one vintage. Companion: deposits ÷ consumer credit per group (buffer coverage) |
| Latest quarter | 2026:Q2 (Z.1 2026:Q2 release 2026-09-11) |
| Next print | **2026:Q3, with Z.1 on Thu 2026-12-10 12:00 ET** (federalreserve.gov/releases/z1, read 2026-10-29: *"The next Z.1 release will be Thursday, December 10, 2026, at 12:00 noon."*) |

### First observation (vintage 2026-09-11/18, nominal)

| Group | Deposits/HH Q2-25 | Q1-26 | **Q2-26** | YoY | QoQ | Deposits ÷ consumer credit Q2-25 → Q2-26 |
|---|---|---|---|---|---|---|
| Bottom 40% income | $25,511 | $25,914 | **$25,799** | **+1.13%** | −0.44% | 1.371 → 1.356 |
| Bottom 20% only | $17,643 | $17,607 | $17,618 | −0.14% | +0.06% | 1.349 → 1.319 |
| Middle 40–80% | $62,281 | $64,319 | $63,738 | +2.34% | −0.90% | 1.504 → 1.505 |
| Top 20% | $336,047 | $350,332 | $346,261 | **+3.04%** | −1.16% | 5.157 → 5.200 |
| **Gap, bottom 40 minus top 20** | | | | **−1.91 pp** | | |

Read: in the Fed's allocation, bottom-40 deposits grew more slowly than top-20 deposits over the year to Q2 2026, and bottom-40 deposit coverage of consumer credit slipped while top-20 coverage rose. Nominal; not deflated. This predates September's saving-rate drop, so it is a baseline, not evidence about September.

### ⚠️ Caveats that travel with every figure above

1. **Model allocation, not observation.** The DFA page: SCF balance sheets are interpolated "between SCF surveys" and forecast "for each quarter beyond the most recent survey year"; shares are then applied to Financial Accounts aggregates. The 2026 cohort split is therefore a model, not an observation of who drew down. It can describe; it cannot establish.
2. **Re-basing risk at the 12/10 print.** SCF 2025 was released 2026-10-09; if the December DFA brings it in, history may be revised. Rule: compare Q3-26 only to Q2-26 and Q3-25 **of the same vintage**, and record the old Q2 figures above as superseded, never as a change.
3. Deposits only (checking, savings, time). Money-market funds sit in a separate column and are excluded on purpose (a top-heavy asset).

## Candidates considered and why not chosen

| Candidate | Verdict |
|---|---|
| NY Fed Household Debt and Credit, Q3 2026 | **Release date UNVERIFIED**: no media advisory found 2026-10-29 (NY Fed HHDC page and search); Q3 2025 came out 2025-11-05 with a 10/31 advisory. Measures debt and delinquency by age, not buffers, so it is a cross-check for CRL-32, not its cohort instrument. CARL's docket row for 11/05 stays labelled UNVERIFIED. |
| Card-issuer Q3 payment-rate disclosures | **Not in CARL's Q3 reads** (SYF/COF/ALLY Q3 reads carry NCO and delinquency only, KB-537). Monthly trust payment rates exist in SEC 10-D filings (e.g. COMET; KB-CARL-209 for the February format) at $0, but they describe one issuer's trust pool, not an income cohort. Not frozen; owed only if CRL-32 fires. |
| Bank-panel balances by income (PNC Consumer Health Check 10/13; BofA Institute Consumer Checkpoint) | **Observed, but no numbers in the published text**: PNC says balances "remain well above pre-pandemic norms for all income groups" and gives figures only as charts; BofA's October Checkpoint quotes no median balances. Reading numbers off a chart is not a frozen observation. Qualitative counter-evidence, carried as such. |
| PHAN's BNPL series | **Neither house is a grading series** for CRL-32: both are annual surveys with no print inside the window. Where cited as context the letter uses **Fed SHED 26%** (probability panel, n≈13,000), not LendingTree 47% (opt-in online), because the panel is the better-sampled measure of a population share; both stay carried with basis labels (STATUS BNPL row, KB-581). |

## Cost of better data (if Will wants an observed cohort split)

An observed monthly series of balances by income exists only inside bank and fintech panels (BofA, JPMorgan Chase Institute, PNC, Earnest-type card panels). Public releases give charts, not tables. Getting the numbers would mean a paid data licence (vendor pricing not checked, a spend decision) or manual chart digitising with stated error. Neither is proposed here.
