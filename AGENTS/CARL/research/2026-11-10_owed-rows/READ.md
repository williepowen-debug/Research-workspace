# CARL: rows still owed 11/10, worked on PROME prome-07's message (Will's word 11:18 ET)

Written 2026-11-10 11:22 ET. Order as PROME asked: (1) NFIB and DOC docket rows, (2) Liberty Street post, (3) research retirement. Logging is not scoring: no score, band, threshold, gate letter, card or prediction moved. $0.

## 1a. NFIB October Small Business Optimism (docket row 11/10, CARL/POP; V11 context)

⚠️ **SECONDARY ONLY.** nfib.com returns HTTP 403 to this machine (curl with browser UA and web fetch, 11/10 ~11:25 ET), so the NFIB release was not read. Figures from two secondary pages dated 2026-11-10, both citing the NFIB release:

| Item | October 2026 | Source |
|---|---|---|
| Optimism Index | **97.8** (September 97.9, −0.1) | FX.co (Sept value); Academic Capital (level) |
| Long-run average | 98.0 ("53-year average") | Academic Capital |
| Uncertainty Index | **84, down 6**, "lowest since December 2025" | Academic Capital |
| Single most important problem | labor quality 25%; taxes 21% (second place, highest since May 2021); inflation share not given | Academic Capital |
| Prices | "A net 37% of owners planned to raise selling prices" (wording as published) | Academic Capital |
| Unfilled job openings | 36% | Academic Capital |
| Earnings trends, credit access, loan rate | **not obtained** | neither page |

**Read:** flat, a hair below the long-run average, uncertainty lower. Nothing here moves V11 (score 3, driven by Sub-V filings and owner income). The earnings and credit-access lines, the ones that bear on V11, were not obtained; POP owns the deeper read. Row closed as read-at-secondary.

## 1b. DOC monthly refresh on CPI day (docket row 11/10, CARL/DOC)

Parent read by CARL, no DOC spawn (BLS API v1, pulled 2026-11-10 ~11:25 ET). October 2025 is unpublished, so no official October YoY exists; interpolated figures use the geometric mean of Sep and Nov 2025 and are labelled, not BLS.

| Series | Oct 2026 | m/m | Interpolated YoY | Sep official YoY |
|---|---|---|---|---|
| Medical care (CUUR0000SAM) | 595.467 | +0.31% NSA; +0.34% SA | **+1.8%** | +1.5% |
| Medical services (SAM2) | 657.090 | +0.26% | +2.8% | +2.5% |
| Medical commodities (SAM1) | 404.929 | +0.52% | −2.9% | −3.3% |
| Hospital and related services (SEMD) | 111.493 | +0.70% | **+5.8%** | +5.4% |
| Professional services (SEMC) | 459.457 | +0.43% | +3.7% | |
| Health insurance (SEME) | 133.634 | −1.85% | −9.4% | |

Written to DOC: `sub_agents/DOC/workbook/VX.tsv` VX-DOC-1.01 and 1.02 (values, dated); `sub_agents/DOC/STATUS.md` dashboard row and a dated parent-read line. Hospital prices stay the hot leg (interpolated +5.8%, above the >5% elevated line, already WATCH). Medical costs remain context, not score. **DOC-P10 is NOT graded today:** per TEAM 11/06 it grades at the Q3 second estimate (BEA, docket row 11/25). Health insurance CPI uses BLS's retained-earnings method and lags; not read as a premium signal.

## 2. NY Fed Liberty Street post, 2026-11-10

"A Look at the Wider Divide in Credit Card Delinquency by Income", Lee, Mangrum, Scally, Sinha, van der Klaauw, https://libertystreeteconomics.newyorkfed.org/2026/11/a-look-at-the-wider-divide-in-credit-card-delinquency-by-income/ (text via web fetch). Chart data file pulled by CARL (HTTP 200, saved `research/2026-11-09_HHDC_prep/raw/LSE_2026_scally-hhdc2026q3.xlsx`, sha256 1ff6e90b98c815fe…).

**Chart 1, card flow into 90+ (4-quarter sum) by zip-code income quartile (Q1 lowest):**

| Quarter | Q1 | Q2 | Q3 | Q4 | Q1 / Q4 | Q1 − Q4 |
|---|---|---|---|---|---|---|
| 2019Q4 | 7.99 | 6.00 | 4.68 | 3.57 | 2.24× | 4.42 pp |
| 2022Q4 | 6.92 | 4.86 | 3.71 | 2.52 | 2.75× | 4.40 pp |
| 2024Q4 (peak, every quartile) | 10.92 | 8.17 | 6.94 | 4.65 | 2.35× | 6.27 pp |
| 2026Q2 | 10.64 | 8.18 | 6.40 | 4.56 | 2.33× | 6.08 pp |
| **2026Q3** | **10.33** | **7.84** | **6.30** | **4.40** | **2.35×** | **5.93 pp** |

Other charts: new cards to the lowest-income quartile 24.3% of all new cards in 2026Q3 (elevated 2020–22 per the post); median origination score 699 (2017–19 average) → 688 (2020–22 average), 703 at 2025Q4. Chart 4 (loan-level, total 7.129 at 2026Q3, NOT the Page 14 basis of 6.87): the 2020–22 vintage's contribution fell 2.869 (2024Q4) → 1.799; the 2023–25 vintage's rose 1.317 → 2.613. Post's attribution: macro conditions "likely the main contributing factor"; looser pandemic underwriting contributed through the 2020–22 vintage; "may prove to be more of a pandemic-era echo"; "absent macroeconomic shocks … will likely continue to see signs of improvement".

**Does it change the cohort or scope finding?** It does not change the 10/12 scope finding; it sharpens it in both directions.
- **Supports concentration:** lowest-income zip quartile runs at 2.35× the highest and 5.93 pp above it, above pre-pandemic levels in every quartile.
- **Against "bottom still deteriorating" on cards:** all four quartiles have fallen since the 2024Q4 peak, the lowest quartile most in points (−0.59 pp vs −0.25 pp). In relative terms the gap is near pre-pandemic (2.35× vs 2.24× at 2019Q4); it "widened" in percentage points.
- **Competing mechanism:** a vintage/underwriting echo explains part of the card-delinquency rise without the thesis's multi-vector cost squeeze. Staged to RED (`handoff_RED/COUNTER_LOG.md`, 2026-11-10 entry), unadjudicated.
- **Caveats that travel:** zip-code income, not household income (an area measure; a low-income household in a high-income zip is in Q4). The 2023–25 vintage's rising share is partly mechanical seasoning as it grows. Chart 4 is loan-level and must never substitute for Page 14 in any CARL grade.

## 3. Research retirement sweep (closeout step 13c, carried NOT RUN at 11:2x)

Candidates: tracked files in `research/` and `domain/sources/` last committed before 2026-09-11. Three found, same set as 11/09:

| File | Last commit | Live reference found | Disposition |
|---|---|---|---|
| `domain/sources/SYF_COF_Q1_2026.md` | 2026-04-29 | CRL-12 (OPEN) in PREDICTIONS.tsv | RETAINED |
| `domain/sources/ally/RECLASSIFICATION_AUDIT_FY2025.md` | 2026-07-10 | KB-CARL-223 (ACTIVE); `handoff_RED/COUNTER_LOG.md` | RETAINED |
| `domain/sources/2026-05_NYFed_HHDC_2026Q1_condensed_brief.md` | 2026-07-12 | KB-CARL-326/327/328 (ACTIVE) | RETAINED |

Retirement-sweep JSONs and PROME processed packets were not counted as live references (index/record surfaces). 0 moved. Sweep complete for this session.
