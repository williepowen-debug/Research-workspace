# Is the pool of weak banks growing? Four sets by quarter, 3/31/2019 to 9/30/2026
**Date:** 2026-11-28 (00:40 ET onward, from `date`) | **Mode:** Thesis | **Confidence:** High (filing cells, arithmetic) / Medium (set definitions are proxies, stated below)
**Commission:** PROME prome-80, plan leg C (`PROME/plans/2026-11-28_why-seven-failures-PLAN.md`; Will 00:19 ET 11/28). Session dewey-2026-11-27-8654c74a. Interpretation is REGINALD's and PROME's.

## Key finding
**The broad pool grew from 2021 to 2023, was flat through 2025, and has shrunk in 2026. The deep tail has grown, but only in tiny banks.**
- **Broad pool (union of the four sets):** an average of 25 banks (0.50% of banks) in 2021, 41 in 2022, 71 in 2023 (peak of 98 at 12/31/2023), 67 in 2024, 66 in 2025 and 51 in 2026. At 9/30/2026 it is 43 banks (1.02%, the lowest share since 9/30/2022). In assets it peaked at $464B (12/31/2023) and is $96B at 9/30/2026.
- **Deep tail (below adequately capitalized, the Texas form):** these were near zero in 2022–2024: an average of 1.0–1.8 banks below adequately capitalized and 0.8–2.0 in the Texas form. They have risen to 4–7 and 3–8 banks in 2025–2026. Apart from United Fidelity at 9/30/2026, these banks hold under $1B of assets in total.
- **Read:** more banks are getting worse in the deepest tail, which fits the small 2025–2026 failures, but the pool as a whole is not growing. On this evidence H2 (more banks getting worse) explains part of 2026's count, the very small banks, but not a broad deterioration.

## Definitions (exact cells; FDIC BankFind financials; $ thousands)
- **Population:** every FDIC financials row except classes OI (insured branches of foreign banks) and NC (non-bank trust companies), as in the 11/11 method. A capital ratio reported as 0 is treated as not reported.
- **RBC reporters vs CBLR electors:** a bank with no total risk-based ratio (RBCRWAJ blank or 0) is treated as a community bank leverage ratio (CBLR) elector and judged on leverage only (INFERRED from the blank).
- **Set 1, prompt-corrective-action lines on ANY ratio.** RBC reporters use total 10 / tier 1 8 / CET1 6.5 / leverage 5 (well capitalized); 8 / 6 / 4.5 / 4 (adequately capitalized); 6 / 4 / 3 / 3 (significantly undercapitalized, the "below undercapitalized" line). CBLR electors use leverage 4 for 1b and 3 for 1c.
  - **1a** is shown for RBC reporters only. Judging CBLR banks against the CBLR leverage line without its two-quarter grace period over-counts sharply: 172 banks at 3/31/2022, and a break at 9/30/2026, when the CBLR line fell from 9% to 8%. The eCFR shows 12 CFR 324.12 reading "greater than 8 percent" from its 2026-07-01 version, and 101 CBLR banks sat at 8–9% leverage at 9/30. That variant is kept in the data file, not in the union.
  - **1d critical proxy:** tier 1 capital (RBCT1) / total assets ≤ 2%. PCA uses tangible equity; this is close but not identical.
- **Set 2, Texas-ratio form:** noncurrent loans (NCLNLS, 90+ days past due plus nonaccrual) + other real estate owned (ORE) > tier 1 capital (RBCT1) + allowance (LNATRES). **Tier 1, not GAAP tangible equity:** GAAP equity carries unrealized securities losses (AOCI), and the GAAP form (variant 2g, kept in the file) jumps from 2022 for that reason alone (34 banks at 9/30/2022 against 1 on tier 1).
- **Set 3:** quarterly net income (NETINCQ) below −10% of the same bank's equity (EQ) at the prior quarter-end. Not computed for 3/31/2019.
- **Set 4:** brokered deposits (BRO) / deposits (DEP) > 15% AND total risk-based ratio < 12% (within 2 points of the 10% line). RBC reporters only. **4c**, kept outside the union, is the CBLR analogue: brokered > 15% and leverage within 2 points of the CBLR line.
- **Union:** 1a (RBC reporters), 1b, 1c, 1d, 2, 3 and 4.
- **Source:** api.fdic.gov/banks/financials, 31 quarter-end pulls; each row count equals the API total (meta files). Tier 1 comes from a second pull of the same dates. The FDIC failed-bank CSV was read 2026-11-28 (sha256 61166c93…). **Stopped at 3/31/2019** as the brief asked; the same script reaches further back cheaply.

## Count / assets ($B) by quarter
| Quarter | Banks | Assets $B | 1a below well (RBC reporters) | 1b below adequately | 1c below undercapitalized line | 1d critical proxy | 2 Texas form | 3 quarter loss >10% | 4 brokered + thin | 4c CBLR variant | Union (1a–4) | Union % of banks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019-03 | 5,362 | 18,090 | 22 / 23.3 | 14 / 1.6 | 7 / 0.5 | 0 / 0.0 | 16 / 21.4 | 0 / 0.0 | 30 / 50.4 | 0 / 0.0 | 57 / 93.5 | 1.06% |
| 2019-06 | 5,303 | 18,266 | 16 / 2.2 | 11 / 1.1 | 6 / 0.5 | 1 / 0.0 | 17 / 3.4 | 14 / 2.6 | 23 / 54.6 | 0 / 0.0 | 55 / 59.4 | 1.04% |
| 2019-09 | 5,258 | 18,482 | 16 / 2.0 | 12 / 1.2 | 8 / 0.7 | 2 / 0.1 | 17 / 23.0 | 21 / 1.9 | 24 / 59.2 | 0 / 0.0 | 60 / 84.5 | 1.14% |
| 2019-12 | 5,177 | 18,646 | 17 / 2.0 | 8 / 0.8 | 5 / 0.6 | 2 / 0.2 | 11 / 24.0 | 21 / 2.2 | 23 / 25.9 | 0 / 0.0 | 60 / 53.0 | 1.16% |
| 2020-03 | 5,116 | 20,255 | 12 / 2.3 | 7 / 0.6 | 3 / 0.4 | 1 / 0.1 | 14 / 27.1 | 22 / 278.8 | 19 / 64.5 | 23 / 17.3 | 57 / 371.7 | 1.11% |
| 2020-06 | 5,066 | 21,139 | 10 / 2.5 | 7 / 1.2 | 4 / 1.0 | 3 / 0.8 | 10 / 25.1 | 18 / 104.3 | 10 / 13.6 | 18 / 17.0 | 41 / 145.5 | 0.81% |
| 2020-09 | 5,033 | 21,209 | 9 / 0.7 | 5 / 0.4 | 4 / 0.3 | 2 / 0.2 | 10 / 29.1 | 20 / 10.4 | 6 / 21.0 | 14 / 12.9 | 35 / 60.5 | 0.70% |
| 2020-12 | 5,002 | 21,869 | 8 / 1.1 | 3 / 0.2 | 2 / 0.1 | 0 / 0.0 | 6 / 32.1 | 14 / 5.2 | 2 / 0.9 | 10 / 12.8 | 26 / 38.6 | 0.52% |
| 2021-03 | 4,978 | 22,547 | 7 / 1.1 | 3 / 0.2 | 3 / 0.2 | 0 / 0.0 | 7 / 34.0 | 9 / 3.9 | 1 / 0.4 | 13 / 7.9 | 20 / 39.2 | 0.40% |
| 2021-06 | 4,950 | 22,774 | 8 / 1.3 | 2 / 0.1 | 2 / 0.1 | 1 / 0.2 | 7 / 33.5 | 11 / 1.1 | 6 / 6.6 | 9 / 3.1 | 29 / 42.5 | 0.59% |
| 2021-09 | 4,914 | 23,252 | 8 / 1.1 | 2 / 0.1 | 1 / 0.1 | 1 / 0.2 | 4 / 33.6 | 9 / 1.2 | 1 / 2.2 | 6 / 5.5 | 21 / 38.3 | 0.43% |
| 2021-12 | 4,839 | 23,720 | 8 / 1.2 | 1 / 0.1 | 1 / 0.1 | 0 / 0.0 | 4 / 34.2 | 13 / 1.9 | 5 / 1.5 | 9 / 20.4 | 29 / 38.9 | 0.60% |
| 2022-03 | 4,796 | 23,973 | 8 / 1.3 | 2 / 0.1 | 0 / 0.0 | 1 / 0.2 | 3 / 34.3 | 7 / 1.2 | 5 / 4.2 | 11 / 8.7 | 23 / 41.3 | 0.48% |
| 2022-06 | 4,771 | 23,717 | 7 / 4.2 | 1 / 0.0 | 0 / 0.0 | 0 / 0.0 | 2 / 41.6 | 12 / 3.9 | 13 / 15.6 | 12 / 11.0 | 32 / 64.8 | 0.67% |
| 2022-09 | 4,746 | 23,627 | 10 / 2.6 | 2 / 0.3 | 1 / 0.0 | 0 / 0.0 | 1 / 1.9 | 14 / 3.7 | 21 / 43.3 | 14 / 11.9 | 43 / 51.0 | 0.91% |
| 2022-12 | 4,706 | 23,595 | 11 / 8.6 | 2 / 1.5 | 0 / 0.0 | 0 / 0.0 | 2 / 43.8 | 22 / 58.9 | 30 / 69.8 | 21 / 22.6 | 64 / 180.6 | 1.36% |
| 2023-03 | 4,672 | 23,715 | 8 / 9.7 | 2 / 2.1 | 1 / 0.2 | 1 / 0.2 | 2 / 45.7 | 13 / 47.6 | 34 / 158.7 | 27 / 30.1 | 56 / 259.8 | 1.20% |
| 2023-06 | 4,645 | 23,461 | 10 / 8.0 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 17 / 15.1 | 44 / 216.6 | 35 / 37.5 | 67 / 226.4 | 1.44% |
| 2023-09 | 4,614 | 23,408 | 6 / 8.6 | 1 / 0.1 | 1 / 0.1 | 1 / 0.1 | 1 / 0.1 | 17 / 130.7 | 44 / 177.6 | 39 / 35.9 | 63 / 311.4 | 1.37% |
| 2023-12 | 4,587 | 23,666 | 7 / 7.3 | 1 / 0.8 | 1 / 0.8 | 0 / 0.0 | 0 / 0.0 | 49 / 203.1 | 50 / 263.2 | 43 / 33.1 | 98 / 464.4 | 2.14% |
| 2024-03 | 4,568 | 23,958 | 6 / 1.4 | 2 / 0.7 | 1 / 0.7 | 0 / 0.0 | 0 / 0.0 | 18 / 3.8 | 42 / 160.2 | 43 / 44.1 | 63 / 164.6 | 1.38% |
| 2024-06 | 4,538 | 23,888 | 4 / 0.6 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 15 / 28.3 | 40 / 89.8 | 48 / 35.1 | 58 / 118.8 | 1.28% |
| 2024-09 | 4,517 | 24,212 | 4 / 1.2 | 1 / 0.0 | 0 / 0.0 | 0 / 0.0 | 3 / 0.2 | 27 / 19.6 | 39 / 80.2 | 50 / 30.6 | 69 / 100.0 | 1.53% |
| 2024-12 | 4,487 | 24,101 | 11 / 4.5 | 3 / 1.3 | 1 / 0.0 | 0 / 0.0 | 4 / 39.4 | 35 / 30.4 | 41 / 45.7 | 47 / 34.6 | 77 / 112.1 | 1.72% |
| 2025-03 | 4,462 | 24,538 | 10 / 3.5 | 4 / 0.4 | 1 / 0.0 | 0 / 0.0 | 3 / 39.8 | 23 / 23.1 | 34 / 42.7 | 44 / 35.4 | 57 / 104.6 | 1.28% |
| 2025-06 | 4,421 | 24,989 | 6 / 2.6 | 4 / 0.7 | 0 / 0.0 | 0 / 0.0 | 3 / 40.8 | 21 / 5.0 | 43 / 68.3 | 45 / 34.2 | 64 / 113.6 | 1.45% |
| 2025-09 | 4,379 | 25,113 | 11 / 2.7 | 4 / 0.2 | 2 / 0.1 | 0 / 0.0 | 4 / 1.3 | 32 / 57.7 | 40 / 62.8 | 45 / 44.3 | 71 / 119.0 | 1.62% |
| 2025-12 | 4,338 | 25,257 | 14 / 6.1 | 5 / 0.4 | 3 / 0.4 | 0 / 0.0 | 6 / 42.4 | 33 / 9.9 | 40 / 56.8 | 48 / 39.0 | 70 / 105.2 | 1.61% |
| 2026-03 | 4,279 | 26,145 | 10 / 3.0 | 7 / 0.8 | 5 / 0.5 | 2 / 0.3 | 8 / 43.4 | 23 / 11.6 | 30 / 42.1 | 38 / 38.9 | 54 / 95.5 | 1.26% |
| 2026-06 | 4,239 | 26,462 | 8 / 1.8 | 5 / 0.5 | 4 / 0.5 | 0 / 0.0 | 6 / 43.7 | 27 / 6.0 | 29 / 56.1 | 47 / 41.1 | 55 / 104.5 | 1.30% |
| 2026-09 | 4,205 | 26,650 | 8 / 7.2 | 5 / 6.1 | 2 / 0.1 | 0 / 0.0 | 5 / 52.6 | 20 / 12.0 | 21 / 42.8 | 19 / 13.9 | 43 / 96.0 | 1.02% |

**Asset sums are dominated by single large banks:**
- 3/31/2020 quarter losses: $279B, large-bank goodwill charges.
- 12/31/2023: $203B in set 3, from securities-sale and other Q4 charges.
- Set 4 in 2023: $159B to $263B.
- Set 2 from 12/31/2024: about $40B is MidFirst Bank, whose noncurrent loans are largely FHA-insured repurchases (INFERRED; the guaranteed share is not separated in these cells).

**Read counts first.**

## Yearly averages (count of banks)

| Year | 1a (RBC) | 1b below adequately | 1c | 1d | 2 Texas | 3 quarter loss | 4 brokered + thin | Union | Union % of banks | Union assets $B |
|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 17.8 | 11.2 | 6.5 | 1.2 | 15.2 | 14.0 (3 quarters) | 25.0 | 58.0 | 1.10% | 72.6 |
| 2020 | 9.8 | 5.5 | 3.2 | 1.5 | 10.0 | 18.5 | 9.2 | 39.8 | 0.78% | 154.1 |
| 2021 | 7.8 | 2.0 | 1.8 | 0.5 | 5.5 | 10.5 | 3.2 | 24.8 | 0.50% | 39.7 |
| 2022 | 9.0 | 1.8 | 0.2 | 0.2 | 2.0 | 13.8 | 17.2 | 40.5 | 0.85% | 84.4 |
| 2023 | 7.8 | 1.0 | 0.8 | 0.5 | 0.8 | 24.0 | 43.0 | 71.0 | 1.54% | 315.5 |
| 2024 | 6.2 | 1.5 | 0.5 | 0.0 | 1.8 | 23.8 | 40.5 | 66.8 | 1.48% | 123.9 |
| 2025 | 10.2 | 4.2 | 1.5 | 0.0 | 4.0 | 27.2 | 39.2 | 65.5 | 1.49% | 110.6 |
| 2026 (3 quarters) | 8.7 | 5.7 | 3.7 | 0.7 | 6.3 | 23.3 | 26.7 | 50.7 | 1.19% | 98.7 |

**Denominator:** 5,362 banks at 3/31/2019 falling to 4,205 at 9/30/2026 (mergers). Shares are given so that this decline is not read as improvement.

## The 16 failures since 2023: when each first entered a set
"Quarters before close" counts the quarter-ends from the entry quarter through the last quarter-end before the closing date, inclusive.

| Bank (cert) | Closed | Last report, assets $B | First quarter in any set (quarters before close) | Start of last continuous run (quarters) | Sets entered (first quarter) |
|---|---|---|---|---|---|
| United Fidelity Bank, fsb (29566, IN) | 2026-11-27 | 2026-09, 5.92 | 2022-06 (18) | 2026-09 (1) | 1a_rbc_reporters 2026-09; 1b_below_adequate 2026-09; 2_texas 2026-09; 3_qloss 2026-09; 4_brokered_thin 2022-06 |
| Nano Banc (58590, CA) | 2026-09-25 | 2026-06, 0.74 | 2020-06 (25) | 2025-06 (5) | 1a_rbc_reporters 2020-06; 2_texas 2025-09; 3_qloss 2025-06; 4_brokered_thin 2025-12 |
| Tioga-Franklin Savings Bank (33802, PA) | 2026-08-21 | 2026-06, 0.07 | 2024-09 (8) | 2024-09 (8) | 1a_rbc_reporters 2024-12; 1b_below_adequate 2025-03; 1c_below_undercap 2026-03; 2_texas 2024-09; 3_qloss 2024-09 |
| Small Business Bank (25744, KS) | 2026-07-17 | 2026-03, 0.07 | 2024-09 (8) | 2025-09 (4) | 1a_rbc_reporters 2026-03; 3_qloss 2024-09 |
| Kentland Federal Savings and Loan Association (28722, IN) | 2026-07-10 | 2026-03, 0.0 | 2024-03 (10) | 2024-12 (7) | 1a_rbc_reporters 2025-03; 1b_below_adequate 2025-09; 1c_below_undercap 2025-09; 1d_critical_proxy 2026-03; 2_texas 2025-09; 3_qloss 2024-03 |
| Community Bank and Trust - West Georgia (25796, GA) | 2026-05-01 | 2026-03, 0.29 | 2019-03 (29) | 2024-12 (6) | 1a_rbc_reporters 2019-03; 1b_below_adequate 2019-03; 1c_below_undercap 2019-09; 1d_critical_proxy 2026-03; 2_texas 2019-03; 3_qloss 2019-09 |
| Metropolitan Capital Bank & Trust (57488, IL) | 2026-01-30 | 2025-12, 0.24 | 2019-03 (28) | 2024-12 (5) | 1a_rbc_reporters 2024-12; 1b_below_adequate 2024-12; 1c_below_undercap 2025-12; 3_qloss 2024-12; 4_brokered_thin 2019-03 |
| The Santa Anna National Bank (5520, TX) | 2025-06-27 | 2025-03, 0.08 | never | — | none |
| Pulaski Savings Bank (28611, IL) | 2025-01-17 | 2024-09, 0.05 | never | — | none |
| The First National Bank of Lindsay (4134, OK) | 2024-10-18 | 2024-09, 0.11 | 2024-09 (1) | 2024-09 (1) | 2_texas 2024-09; 3_qloss 2024-09 |
| Republic First Bank dba Republic Bank (27332, PA) | 2024-04-26 | 2023-12, 5.87 | 2023-03 (5) | 2023-03 (5) | 1a_rbc_reporters 2023-03; 3_qloss 2023-12 |
| Citizens Bank (8758, IA) | 2023-11-03 | 2023-09, 0.07 | 2023-09 (1) | 2023-09 (1) | 1a_rbc_reporters 2023-09; 1b_below_adequate 2023-09; 1c_below_undercap 2023-09; 1d_critical_proxy 2023-09; 2_texas 2023-09; 3_qloss 2023-09 |
| Heartland Tri-State Bank (25851, KS) | 2023-07-28 | 2023-03, 0.14 | never | — | none |
| First Republic Bank (59017, CA) | 2023-05-01 | 2023-03, 232.94 | never | — | none |
| Signature Bank (57053, NY) | 2023-03-12 | 2022-12, 110.36 | never | — | none |
| Silicon Valley Bank (24735, CA) | 2023-03-10 | 2022-12, 209.03 | never | — | none |

- **6 of 16 never entered any set:**
  - Silicon Valley, Signature and First Republic: deposit runs, with capital ratios well above the lines at their last reports.
  - Heartland Tri-State: fraud.
  - Pulaski Savings and Santa Anna National. Santa Anna crossed only the CBLR well-capitalized line, at 12/31/2024, which is not in the union.
- **10 entered.** Seven were in a set for 4 or more quarters before closing on their last continuous run: Tioga-Franklin 8, Kentland 7, Community Bank and Trust 6, Metropolitan Capital 5, Nano Banc 5, Republic First 5, Small Business Bank 4. Two first appeared in the last quarter-end before closing: First National Bank of Lindsay and Citizens Bank (Sac City).
- **United Fidelity:** in set 4 (brokered funding with total capital under 12%) from 6/30/2022. It left and re-entered, and reached the capital, Texas and loss sets only at 9/30/2026, its last report.
- **Community Bank and Trust – West Georgia and Metropolitan Capital** were in sets in 2019, left, and came back in 2024.

## Banks in set 1 below adequately capitalized at 9/30/2026 (public Call Report facts; no forecast implied)

| Bank (cert) | State | Assets $M | Total RBC % | Tier 1 % | CET1 % | Leverage % | Equity $M | Noncurrent loans $M | Q3 net income $M |
|---|---|---|---|---|---|---|---|---|---|
| Lamont Bank of St. John (8681) | WA | 53.2 | 4.85 | 3.55 | 3.55 | 3.32 | 0.9 | 16.4 | 0.5 |
| Summit National Bank (25054) | WY | 64.2 | 5.56 | 4.31 | 4.31 | 2.26 | 1.3 | 0.1 | −0.6 |
| Connect Community Bank (28266) | WA | 71.8 | 7.58 | 6.33 | 6.33 | 3.07 | 2.2 | 0.1 | −0.4 |
| Columbia Savings & Loan Association (28480) | WI | 19.7 | 7.76 | 6.50 | 6.50 | 4.62 | 0.9 | 3.5 | −0.2 |
| United Fidelity Bank, fsb (29566) | IN | 5,915.5 | 7.26 | 6.64 | 4.74 | 5.82 | 389.7 | 2,160.8 | −246.9 (closed 11/27/2026) |

Lamont and Summit are also below the significantly undercapitalized line, on tier 1 and on leverage. These four banks hold **$209M** of assets combined. Their enforcement status was not read.

## Answer to the brief
- **Count:** the union grew from 2022 (average 40.5) to 2023 (71.0), was flat in 2024–2025 (66.8, 65.5) and fell in 2026 (50.7 average; 43 at 9/30, 1.02% of banks).
  - **Since 2022 the pool is larger than in 2021–22, but it has been flat to shrinking since its 2023 peak.**
  - **The deepest tail is the exception:** banks below adequately capitalized rose from 1–2 in 2022–24 to 4–7 in 2025–26, and the Texas form from about 1 to 3–8. All of them are under $1B of assets, except United Fidelity.
- **Assets:** the union peaked at $464B (12/31/2023), driven by large banks' Q4 losses and set 4. It is $96B at 9/30/2026. The deep-tail assets are under $1B before United Fidelity.
- **What the four sets cannot see:**
  - Deposit runs: half of the 2023 losses by assets.
  - Fraud.
  - Losses not yet recognized: United Fidelity reported its loans current until the quarter they went to nonaccrual.
  - Examination ratings and the problem-bank list (confidential CAMELS; the FDIC publishes only the count).
  - Informal supervisory actions.
  - CBLR banks during their grace period.
  - The government-guaranteed share of noncurrent loans.
  - Holding-company stress.
- **CATO's cautions:** a bank in a set is not a failure forecast, and the sets have no tested predictive value. 6 of 16 failures were never in them, and the union holds 40 to 100 banks a quarter while 0 to 7 fail a year.

## Counter-evidence and alternatives
- The 2026 failures are mostly tiny: five of seven had assets of $0.3B or less at their last report. The deep-tail rise is a handful of tiny banks.
- Fewer banks overall (−22% since 2019) mechanically lowers counts. Shares are shown so this is not mistaken for a trend.
- H1 (faster closing) and H3 (laxer supervision) are leg A's to test. The rise in the deep tail is also consistent with regulators letting weak small banks run longer before closing: Tioga-Franklin spent 8 quarters in the sets and Kentland 7.

## Reproduce
Run `python3 AGENTS/DEWEY/research/2026-11-28_weak-bank-pool/pull.py AGENTS/DEWEY/research/2026-11-28_weak-bank-pool/fdic`, then `pool.py` (outputs in `out/`: pool-by-quarter.tsv, failures.tsv, below-adequate-20260930.tsv, members.json). eCFR CBLR text: `https://www.ecfr.gov/api/versioner/v1/full/<date>/title-12.xml?section=324.12` (versions 2026-04-29 and 2026-07-01).

## Process report
- **Pulls:** 62 FDIC pulls, 1 CSV, 8 eCFR reads.
- **Corrections during the run:**
  - Foreign branches and trust companies first entered set 1 through ratios reported as 0; fixed by population and zero rules.
  - GAAP equity inflated set 2 through AOCI; switched to tier 1.
  - The CBLR line change at 9/30/2026 was found from the jump in CBLR banks at 8–9% leverage.
- **Not done:** enforcement status of the four banks; set 2 net of guaranteed noncurrent loans; pre-2019 history.
