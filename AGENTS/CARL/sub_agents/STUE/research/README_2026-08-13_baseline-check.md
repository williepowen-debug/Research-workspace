# Baseline check, 2026-08-13 — source data + how to reproduce

**Why these files are here:** the 8/13 session's three thesis-adverse findings all rest on arithmetic off these two primaries. **A finding that reverses a domain's headline has to be reproducible by someone who does not trust it.**

| File | Source | Pulled |
|---|---|---|
| `FSA_PortfoliobyLoanStatus_pulled-2026-08-13.xls` | `studentaid.gov/sites/default/files/fsawg/datacenter/library/PortfoliobyLoanStatus.xls` | 2026-08-13 |
| `NYFed_HHD_C_Report_2026Q2_pulled-2026-08-13.xlsx` | `newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/HHD_C_Report_2026Q2.xlsx` | 2026-08-13 |

**Retrieval:** both hosts **403 WebFetch**; both serve fine to `curl` with a browser User-Agent. NY Fed's path is deterministic (`HHD_C_Report_<YYYY>Q<N>.xlsx`) — **poll it, don't watch for a media advisory.**

## The three numbers and where they live

1. **90+ balance share** — NY Fed **Page 12 Data**, `STUDENT LOAN` column. 26:Q2 = **10.60%**; 2015–19 mean **11.12%**; 31 consecutive quarters >10% (12:Q3–20:Q1).
2. **Flow into 90+** — NY Fed **Page 14 Data** (30+ is Page 13), `STUDENT LOAN`. 26:Q2 = **7.83%**; pre-pandemic 2015–19 mean 9.51%, range 8.59–10.27%.
   ⚠️ **Page 28** (by age, 4Q moving sum) gives **7.44%** for the same concept — it tracked Page 14 within ±0.01pp for five quarters then diverged +0.39pp in 26:Q2 alone. **Cite Page 14. Register S4.**
3. **Defaulted borrowers** — FSA **`Federally Managed` tab**, column **`Cumulative in Default`** (official definition on the `LoanStatusDefinitions` tab: *loans more than 360 days delinquent*). FY2026 Q2 = quarter ending **2026-03-31** = **9.00M / $220.3B**. Pre-pandemic peak FY2020 Q2 = **7.90M / $171.5B**.
   ⚠️ **PERIMETER TRAP:** the `Direct Loan` tab is a **different, smaller population** (7.20M now, 5.80M peak). The widely-repeated "defaults nearly doubled from ~5M" compares a **Direct Loan** baseline to a **Federally Managed** numerator. **Always read both tabs before quoting a ratio.**

**Trend method:** OLS on FY2016 Q4 – FY2020 Q2 (n=15, the clean pre-COVID window), slope **+0.119M/qtr**, extrapolated 24 quarters to FY2026 Q2 ⇒ counterfactual **10.7M** vs actual **9.0M** = **−16.2%**.

**Retention:** keep until the FY2026 Q3 FSA print (~Sep 2026) resolves open question #16, then re-evaluate under the >60d retirement sweep. **Do not archive before #16 grades** — these are the comparison base.

---

## PM ADDITION — the #17 answer (exposure adjustment)

| File | Source | Pulled |
|---|---|---|
| `FSA_DLPortfoliobyDelinquencyStatus_pulled-2026-08-13.xls` | `…/library/DLPortfoliobyDelinquencyStatus.xls` | 2026-08-13 |
| `FSA_DLPortfoliobyRepaymentPlan_pulled-2026-08-13.xls` | `…/library/DLPortfoliobyRepaymentPlan.xls` | 2026-08-13 (**pulled, UNEXAMINED — it is the instrument for open question #18**) |

**Exposure shares** — `FSA_PortfoliobyLoanStatus…xls`, **`Federally Managed`** tab. Dollar columns are paired `($, recipients)` from col index 2: In-School · Grace · **Repayment** · Deferment · **Forbearance** · Cumulative-in-Default · Other. Share = status ÷ sum of the seven.
- 2015–19 avg: **repayment 53.8%**, forbearance 10.0% · FY2026 Q2: **repayment 38.5%**, forbearance 29.5%.

**Exposure-adjusted delinquency** — `FSA_DLPortfoliobyDelinquencyStatus…xls`, **`FedManagedPortbyDelinquencyStat`** tab. Dollar columns from index 2: Current · 31-90 · 91-180 · 181-270 · 271-360 · Transferring-to-Default.
- **in-repayment base** = sum of all six · **90+** = last four ÷ base.
- 2015–19 avg **7.97%** → FY2026 Q2 **10.95%** = **1.37×**.

**Independent cross-check:** FSA exposure share applied to the NY Fed headline ⇒ 20.55% → 26.82% = **1.31×**.
⚠️ **Fiscal-quarter mapping matters:** FSA FY Q1 ends Dec (prior calendar year), Q2 = Mar, Q3 = Jun, Q4 = Sep. **FY2026 Q2 = calendar 2026 Q1.** Applied, not assumed.

⚠️ **Two caveats that ride with any quote of this finding:** the in-repayment base **excludes** the defaulted stock (which grew 5.2M→9.0M just before the reading, making the result *conservative*), and **selection into forbearance is uncontrolled** (open question #18 — the main threat).
