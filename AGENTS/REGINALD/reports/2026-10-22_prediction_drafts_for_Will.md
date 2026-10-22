# REGINALD — three prediction drafts for Will's approval (2026-10-22, ~13:3x ET)

**Why now:** DAEDALUS's review found REGINALD had 4 OPEN predictions, only 1 of them made since July, in the middle of earnings season. Each draft below follows `FORGE/PREDICTION_DISCIPLINE.md`: named instrument and carrying filing, frozen baseline value + date, a base rate, MECE verdict branches with a NO-VERDICT band, and an IMMOVABLE or CHOSEN resolve-by. **Drafts only:** nothing is encoded in `workbook/PREDICTIONS.tsv` until Will approves, and PROME registers any approved row (REG-27 precedent, WQ-454). Probabilities are REGINALD's first marks.

---

## D1 — EGBN: the Q4 criticized maturities stay on the bank's books ("extend, not exit")

| Field | Draft |
|---|---|
| **Claim** | Of the 4 criticized loans >$10M that mature in 4Q26, **at least 3 are still bank-held at 12/31/2026** (held for investment, held for sale, nonaccrual or foreclosed property). The 4: DC apartments $42.685M (matures 10/27), Montgomery mixed-use $27.722M (10/27), Prince George's apartments $56.000M (12/21), DC apartments $20.474M (12/30). Baseline = Q3 deck slide 20, acc 0001050441-26-000110, 9/30/2026 |
| **Instrument** | EGBN Q4-2026 earnings deck criticized/classified >$10M and nonaccrual >$5M tables. Fallback: 2026 10-K loan footnotes. Loans are matched by collateral + location + balance (`research/EGBN/data/loan_level/`, track IDs L02 · L05 · L11 · L16) |
| **Branches (MECE)** | Let h = loans shown still held, x = loans shown exited (paid off, refinanced away or sold), u = unknown. **TRUE** if h ≥ 3 · **FALSE** if x ≥ 2 · **NO-VERDICT** otherwise (u large enough that neither is established). Absence from a table counts as u, never as x |
| **Base rate** | Of the identifiable Q2-list loans whose maturities have passed, **3 were held** (Prince George's extended twice, Montgomery storage extended, the Fairfax $18.5M office loan matured 2/28/2026 and still held) and **1 exited** (DC $35.4M, paid off). ≈75% held per loan. Independent binomial P(h ≥ 3 of 4) = 74% |
| **Mark** | **65%**. Shaded down from 74% because outcomes are correlated (one bank's policy), and the DC $42.7M at 61% LTV on a fresh 8/17/2026 appraisal is the likeliest clean refinance |
| **Resolve_By** | **2027-03-16, IMMOVABLE:** latest SEC 10-K deadline for EGBN's filer class (75 days after 12/31 if accelerated; 60 days if large accelerated, i.e. 2027-03-01, whichever applies, verified at encoding). Graded first at the Q4 release |
| **What it tests** | The mechanism behind the 10/22 work: whether banks meet weak maturities by extending rather than collecting. TRUE supports "recognition is managed, not avoided". FALSE (outside money taking these loans out) is real contrary evidence for the bear read on EGBN |

## D2 — Cohort: Q4 charge-offs rise at most of the six Q3-read banks (the appraisal-refresh test)

| Field | Draft |
|---|---|
| **Claim** | **At least 4 of these 6 banks report Q4-2026 annualized net charge-offs ABOVE their Q3-2026 rate:** SSB 0.09% · VLY 0.28% · HBAN 0.31% · EGBN 0.25% · BKU 0.11% · ZION 0.02% (Q3 values as printed, release basis, read 10/22) |
| **Instrument** | Each bank's Q4-2026 8-K EX-99.1 "net charge-offs as a percentage of average loans (annualized)" as printed, compared at printed precision. Equal = not above (half-open). Fallback carrying filing: the 10-K |
| **Branches (MECE)** | Let r = banks whose Q4 rate prints above Q3, n = banks with no Q4 print by Resolve_By. **TRUE** if r ≥ 4 · **FALSE** if r + n ≤ 3 · **NO-VERDICT** otherwise |
| **Base rate** | In 8 recent quarter-to-quarter transitions at SSB and HBAN (Q3-25 → Q3-26, printed series), the NCO rate rose 4 times, fell 3 and was flat once: **≈50%**. ZION/EGBN/BKU/VLY show the same coin-flip character in Q2 → Q3 (3 of 6 rose). Binomial at p = 0.5: **P(r ≥ 4 of 6) = 34%** |
| **Mark** | **45%**. Lifted above the 34% base rate by the 10/22 finding that maturities trigger re-appraisals (Eagle's deck s18 policy) and FLG's 10-Q statement that its H1 CRE charge-offs were "primarily driven by appraisals received", with ~$525M of EGBN maturities alone landing in 4Q26. Lifted only 11 points, because 2 of the 6 (EGBN, BKU) are mid-cleanup or flat, and Q4 seasonality is not established |
| **Resolve_By** | **2027-03-16, IMMOVABLE** (latest 10-K deadline among the six; verify each filer class at encoding) |
| **What it tests** | The corrected 12:3x ET implication: recognition is not simply deferred to 2027, because appraisal refreshes force write-downs in Q4–Q1. FALSE at r ≤ 3 says the deferral reading was closer to right |

## D3 — VLY: the problem-loan stock keeps building in Q4

| Field | Draft |
|---|---|
| **Claim** | **Valley's total non-accrual loans at 12/31/2026 are ≥ $511.4M** (the 9/30/2026 level) |
| **Instrument** | VLY Q4-2026 8-K EX-99.1 asset-quality table, "Total non-accrual loans" ($K, as printed). Baseline **$511,390K [9/30/2026]**, acc 0000714310-26-000045. Fallback: 10-K |
| **Branches (MECE)** | **TRUE** if printed ≥ 511,390 · **FALSE** if < 511,390 · **NO-VERDICT** if VLY changes the line's definition in the Q4 release (a restated 9/30 comparative is then used as the baseline and noted) or prints no table by Resolve_By |
| **Base rate** | VLY non-accrual by quarter-end: 421.5 → 433.9 → 432.6 → 462.6 → 511.4 ($M, Q3-25 → Q3-26, VLY Q3 release table). **Rose in 3 of the last 4 quarters** (≈75%) |
| **Mark** | **60%**. Shaded below the 75% run rate because the Q3 jump was one $30.1M construction loan that VLY calls well secured. A payoff or sale of that one loan alone could push Q4 under the bar |
| **Resolve_By** | **2027-03-01, IMMOVABLE** (VLY is a large accelerated filer: 60-day 10-K deadline; verify at encoding) |
| **What it tests** | Valley's early flag: problem CRE rising for two straight quarters while quantitative CRE reserves are released. It pairs with the DEWEY deposit-mix and run-speed inputs (VLY loan-to-deposit 96.3%) |

---

## Housekeeping done with these drafts
- `registry/PREDICTION_RESOLVE_BY.tsv` anchors corrected the same day. The 12:3x ET version used EXPECTED_EVENT, which the HOT canon rule forbids. REG-27 is now IMMOVABLE (SSB Q2-2027 10-Q deadline, 2027-08-09); REG-01/03/06 are CHOSEN decision dates with their missing-report rule stated.
- On approval each row goes into `workbook/PREDICTIONS.tsv` (10 columns, appended, pinned rows untouched) and the sidecar in the same commit, and PROME is packeted for the shared registration.
