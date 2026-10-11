# FHLB hub: source list

*Built 2026-10-10 (Sat ~20:3x ET). Each row says where a primary document lives so any figure in the hub can be re-pulled. PDFs in this folder are **local-only** (gitignored here, per the repo's "bank primary source materials — local only" convention). On another machine, re-download from the URL.*

**SEC EDGAR fetch:** `curl -H 'User-Agent: REGINALD research willie@research.local' https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-without-dashes>/<primary-doc>`. WebFetch gets a 403 on sec.gov. Verify the returned filer NAME before using a CIK (LESSONS: CIK 1325878 is **Topeka**, not Des Moines).

## FHLB System (Office of Finance, the System's fiscal agent)

| Document | As of | Published | URL | Local file |
|---|---|---|---|---|
| Combined Financial Report Q2 2026 (Table 3 advances by borrower type; Table 5 top-10) | 6/30/26 | 2026-08-13 | `https://cdn.fhlb-of.com/files/2026/2026Q2CFR.pdf` | `2026_2026Q2CFR.pdf` |
| Combined Financial Report Q1 2026 | 3/31/26 | 2026-05-14 | `https://cdn.fhlb-of.com/files/2026/2026Q1CFR.pdf` | `2026_2026Q1CFR.pdf` |
| Combined Financial Report FY2025 | 12/31/25 | 2026-03-24 | `https://cdn.fhlb-of.com/files/2025/2025Q4CFR.pdf` | `2025_2025Q4CFR.pdf` |
| Combined Financial Report Q2 2025 | 6/30/25 | 2025 | (`cdn.fhlb-of.com/files/2025/2025Q2CFR.pdf`, path inferred from the local filename) | `2025_2025Q2CFR.pdf` |
| Combined Operating Highlights Q2 2026 (advances $810.7B; total assets $1,436.6B) | 6/30/26 | 2026-07-30 | `https://cdn.fhlb-of.com/files/2026/2026Q2FHLBCombinedOperatingHighlights.pdf` | `2026_2026Q2FHLBCombinedOperatingHighlights.pdf` |
| Combined Operating Highlights Q1 2026 | 3/31/26 | 2026 | (`…/2026/2026Q1FHLBCombinedOperatingHighlights.pdf`, path inferred) | `2026_2026Q1FHLBCombinedOperatingHighlights.pdf` |
| Monthly consolidated-obligation debt file (feeds the Q3 nowcast) | through 9/30/26 | monthly | `https://cdn.fhlb-of.com/files/Debt%20Statistics/fhlbanalystdata.xlsx` | not stored. Re-pull at each month-end |

## FHLBank and member SEC filings (read directly 2026-10-10)

| Filer (CIK) | Form | Period | Accession | Used for |
|---|---|---|---|---|
| Athene Holding (1527469) | 10-K | FY2025 | 0001527469-26-000013 | FHLB funding agreements $23.3B; capacity $66.4B max / $30.7B collateral-constrained incl. outstanding; "investment spread strategy" |
| Athene Holding (1527469) | 10-Q | Q1 2026 | 0001527469-26-000028 | $28.2B; capacity $68.2B / $31.4B |
| Athene Holding (1527469) | 10-Q | Q2 2026 | 0001527469-26-000056 | $27.7B; capacity $70.1B / $33.8B |
| FHLBank Des Moines (1325814) | 10-K | FY2025 | 0001628280-26-016325 | top five; Athene 21%; insurers $50.9B of $110.2B; Section 10(e) language |
| FHLBank Des Moines (1325814) | 10-Q | Q2 2026 | 0001628280-26-054726 | Athene $27,695M = 22%; WFC $22,000M; insurers $57.1B of $125.0B; top five 51% |
| FHLBank San Francisco (1316944) | 10-K | FY2025 | 0001316944-26-000049 | ≥10% borrowers: WAL $4,800M = 13% (YE25), JPMorgan $9,315M = 20% (YE24); no ≥10% stockholder YE25; total assets $73.3B |
| FHLBank Chicago (1331451) | 10-Q | Q2 2026 | 0001331451-26-000148 | total assets $163.2B; advances $71.1B (from $61.1B) |
| FHLBank Indianapolis (1331754) | 10-K | FY2025 | 0001331754-26-000058 | top five; Delaware Life $3,338M = 8%; insurers 34% |
| FHLBank Indianapolis (1331754) | 10-Q | Q2 2026 | 0001331754-26-000161 | Delaware Life $4,963M = 12% (#2); insurers 36%; standby letters of credit $1,331M |
| All 11 FHLBanks | XBRL companyfacts | 12/31/25–6/30/26 | `https://data.sec.gov/api/xbrl/companyfacts/CIK<10-digit>.json` | district table in `../reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md` §2 (CIK list in its §method) |

## Regulators, GAO, Council, state law

| Document | Date | URL | Local file |
|---|---|---|---|
| FHFA Advisory Bulletin AB 2024-03, *FHLBank Member Credit Risk Management* (active 10/10/26) | 2024-09-27 | `https://www.fhfa.gov/advisory-bulletin/ab-2024-03` | `ab2024-03.pdf` |
| FHFA Advisory Bulletin AB 2013-09 (insurer-member collateral; state law controls insurer resolution) | 2013-12-23 | `https://www.fhfa.gov/advisory-bulletin/ab-2013-09` | not stored |
| FHFA rescinded-bulletins list (checked: AB 2024-03 not on it) | checked 2026-10-10 | `https://www.fhfa.gov/advisory-bulletin/rescinded` | not stored |
| Council of FHLBanks letter to FHFA Director Pulte (asks to revise AB 2024-03) | 2026-04-10 (posted 4/14) | `fhlbanks.com` (letter pp. 13–14 of the posted submission) | `council_letter_20260410.pdf` |
| GAO-26-107373, *Federal Home Loan Banks: Role During Financial Stress and Members' Borrowing Trends and Outcomes* | 2025-12 (released 12/17) | `https://www.gao.gov/products/gao-26-107373` | `gao-26-107373.pdf` |
| FHFA-OIG Annual Plan FY2025 | — | `https://www.fhfaoig.gov/sites/default/files/FY2025AnnualPlan.pdf` | `FY2025AnnualPlan.pdf` |
| FHFA-OIG Annual Plan FY2026 | 2025-09-29 | fhfaoig.gov | `FY2026AnnualPlan.pdf` |
| FHFA-OIG FY2026 Management & Performance Challenges ("member credit risk … abated") | — | fhfaoig.gov | `FY2026ManagementAndPerformanceChallenges.pdf` |
| FHFA-OIG EVL-2025-005 (FHLBanks faced challenges obtaining timely supervisory information) | 2025-09-18 | fhfaoig.gov | `EVL-2025-005.pdf` |
| FHFA-OIG AUD-2013-006 (insurer lending) | 2013 | fhfaoig.gov | `AUD-2013-006.pdf` |
| Iowa Code §507C.5 (FHLB stay limits in insurer receivership) | 2024 / 2025 / 2026 editions | `https://www.legis.iowa.gov/docs/code/2026/507C.5.pdf` | `iowa507C5_2024.pdf` · `_2025` · `_2026` |

## Delaware Life / Group 1001 (helper-verified 2026-10-10; full ledger in `../verification/`)

| Document | Date | Where |
|---|---|---|
| AM Best release (Group 1001 L/A outlook → Negative; 42% affiliated) | 2026-07-31 | `news.ambest.com/pr/PressContent.aspx?altsrc=2&refnum=37618` |
| Delaware Life affiliated-investments update (S&P outlook; remediation plan) | 2026-09-11 | `delawarelife.com/content/affiliated-investments-reduction-plan-update` |
| Delaware Life 2025 audited statutory statements (Note 2 subpoenas; Note 19 FHLB capacity $3,432,768K) | 2026 | company site (`cdn.bfldr.com/…/Report_-_Independent_Auditors_-_2025.pdf`) |
| Class actions: Rosner v. Delaware Life 1:26-cv-26388 · Kalinsky v. Delaware Life 0:26-cv-62823 (S.D. Fla.) | filed 2026-09-16 · 2026-10-07 | `courtlistener.com/docket/74800082/` · `/74930247/` |
| Bloomberg, Mark Walter's insurers ramped up FHLB borrowing (secondary; page 403, read via search index) | 2026-09-02 | `bloomberg.com/news/articles/2026-09-02/mark-walter-s-insurers-ramped-up-borrowing-from-fhlb-while-lending-to-affiliates` |
| Bloomberg via ClaimsJournal (restatement first reported; S&P outlook) | 2026-07-22 | `claimsjournal.com/news/national/2026/07/22/338938.htm` |

## The draft under review

| File | Note |
|---|---|
| `FHLB_Risk_Research_Report_Reconciled.docx` | Will's input, received 2026-10-10. Committed (18 KB) |
| `FHLB_Risk_Research_Report_Reconciled_TEXT.md` | Text extract for grep/diff |
