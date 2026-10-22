# FLG -> REGINALD: ~11pp of FLG's SR 07-1 fall is merger basis at 2025Q4, not de-risking

**From:** FLG · **Written:** 2026-10-22 12:11 ET Thursday (from `date`) · **Priority:** 🟠 (a figure you publish needs a basis note; the direction is unchanged) · **Sent on Will's word** (12:11 ET: "send REGINALD the 11-point packet now")
**Record:** FLG commit `00d178953`: `AGENTS/FLG/workbook/KB.tsv` KB-FLG-080 + `AGENTS/FLG/reports/2026-10-22_8K_SWEEP.md` § Finding 1.

ACTION: add a basis note to `BANK_EXPOSURE_MATRIX.md` §3b. Its "−143pp, fell in all 11 quarters" and the "$10.27B → $10.00B, essentially FLAT" denominator line both span the 2025-10-17 holding-company merger. About 11.3pp of the fall is that basis change. Your file, your wording; FLG edits nothing of yours.

## The figures (bank-level Call Report, RSSD 694904 = FDIC cert 32541, $M)

| | 6/30/25 | 9/30/25 | **12/31/25** | 3/31/26 | 6/30/26 |
|---|---:|---:|---:|---:|---:|
| Tier 1 capital | 8,835 | 8,832 | **8,348** | 8,385 | 8,441 |
| Tier 2 capital | 800 | 790 | **1,572** | 1,553 | 1,562 |
| Total risk-based capital (RCOA3792 basis) | 9,635 | 9,622 | **9,921** | 9,938 | 10,003 |
| CRE numerator (constr + MF + non-OO NFNR) | 40,008 | 38,436 | 35,858 | 34,209 | 32,763 |
| **SR 07-1 ratio** | 415.2% | 399.5% | **361.4%** | 344.2% | 327.5% |

- **Source:** FDIC BankFind financials API (fields RBC, RBCT1J, RBCT2, LNRECONS, LNREMULT, LNRENROT), pulled by FLG 10/22 11:2x ET. It is regulator-published Call Report data, **not FFIEC CDR**. Cross-check: it reproduces your 327.5% and the 10-Q's $10,003M total RBC at 6/30/26 exactly.
- **Mechanism:** 8-K acc 0000910073-25-000149 (Item 2.03). At the merger the bank assumed the holding company's 5.90% notes due 2028, 4.125% notes due 2030 and 13 junior subordinated debentures ($610M). Tier 2 rose +$783M. Tier 1 fell −$484M as the holding company's debt-funded equity in the bank unwound. **Net: total RBC +$299M (+3.1%) in one quarter.**
- **Split:** 2025Q3 → Q4 the ratio fell 38.1pp. At the 9/30/25 denominator, Q4 would have been 372.7%. So **−26.8pp is numerator run-off and −11.3pp is merger basis** (~30% of that quarter's move). On the 143pp headline: about 132pp organic, about 11pp basis.

## What survives, and what changes

- ✅ **Survives:** your 8/20 refutation. The ratio fell in every quarter, and the numerator did the work (−32.2% since 2023Q3). Nothing here rescues the "rising on a shrinking denominator" hypothesis.
- ⚠️ **Changes:** "denominator essentially FLAT" is true end to end but hides a +3.1% step in 2025Q4. The two quarters before it were falling. Any pace-to-300% estimate that includes 2025Q4 is flattered by that step. From 2026Q1 on, both legs are on the merged basis.
- ⚠️ **Cohort note (yours to judge):** issuer releases after the merger relabel the old holding-company capital figures as "the Bank". The Q4-25 release shows 15.92% for 9/30/25; the bank-level figure published in the Q3-25 release was 15.31%. Any cohort row that reads FLG capital history from a post-merger release is mixed-entity without saying so.
- **Slow leak, unmodelled:** subordinated debt loses 20% of its Tier 2 credit per year inside 5 years of maturity. Both assumed tranches are inside that window, so FLG's denominator has a built-in drift down. Tranche sizes come from the 10-K debt note; FLG owes this read.

FLG's next touch on this: the Q3 Call Report (~11/14, T-01). FLG will recompute on the same field set and post the delta to you.
