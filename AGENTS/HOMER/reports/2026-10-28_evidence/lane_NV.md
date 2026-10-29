# HOMER — Nevada / Las Vegas coverage lane: source map + baseline

Built 2026-10-28 (~23:30 ET) by a research helper. Nothing in the repository was edited. Raw pulls are in `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-HOMER/3b7684a0-0372-42eb-b6ae-02767433240c/scratchpad/nv/`.
Labels: **PRIMARY** = the issuer's own file or release. **SECONDARY** = press coverage of the issuer. **DERIVED** = arithmetic done here, not published by anyone.
"curl" = whether a plain `curl -L -A 'Mozilla/5.0'` from this box returned the file or page, tested 2026-10-28.

## 0. Retire the stale row

HOMER's old row read "NV Sale Fallthrough 19% (2025, LV Review-Journal), CC 14.53%". **Both halves are mislabelled.**

| Old figure | What it actually is | Current replacement |
|---|---|---|
| Fallthrough 19% | Redfin's **press-release** basis (not seasonally adjusted), December 2025: Las Vegas 19%, up 3.5 points YoY. The Review-Journal only relayed it. | Redfin **dataset** basis (seasonally adjusted): **18.58%, September 2026**. Redfin's current dataset puts December 2025 at **16.58%**, not 19%. The two Redfin bases do not match each other (see §2). |
| CC 14.53% | NY Fed state file, Nevada, **Q4-2024** (it is not a 2025 value): percent of credit-card balance 90+ days delinquent. | **16.28%, Q4-2025**, ranked #1 of 51 (states plus DC) (§5) |

## 1. Las Vegas REALTORS (LVR, formerly GLVAR) monthly statistics: PRIMARY

- **Source:** the monthly stats PDF, `https://members.lasvegasrealtor.com/statistics/pdf/YYYY-MM-GLVAR-Housing-Stats%28t3govm4R8h4%29.pdf`. The token `t3govm4R8h4` was the same for 2026-06, -07, -08 and -09. It changes between years (2022 used a different one).
- **curl:** the **PDF works (200)**. `www.lasvegasrealtor.com` returns **429** to both curl and WebFetch, so the press-release page cannot be pulled; use the PDF.
- **Cadence:** monthly, about the 6th day of the following month. September 2026 data came out **Tue 2026-10-06** (Fox5 and News3LV stories, both dated 2026-10-06).
- **Coverage:** the GLVAR MLS (Clark, Nye, Lincoln and White Pine counties). It **excludes most new-home sales** (builders), so read it alongside §7.

### September 2026 (PDF, PRIMARY)

| Metric | SFH | MoM | YoY | Condo/TH | MoM | YoY |
|---|---|---|---|---|---|---|
| Median sold price | **$470,000** | −1.1% | +0.0% | **$290,000** | −3.3% | −1.4% |
| Units sold | **1,745** | −3.2% | −7.4% | **424** | −5.6% | −12.6% |
| Average sold price | $597,526 | −6.5% | −3.2% | $300,319 | −1.0% | −2.1% |
| Available **without offers** | **7,995** | +5.3% | +6.6% | **2,796** | +3.0% | +7.3% |
| All available listings | 9,984 | +2.4% | +4.4% | 3,337 | +1.2% | +4.8% |
| New listings | 3,120 | −3.6% | −1.3% | 868 | −2.3% | −1.9% |
| Sold within 30 days | 53.4% (Sep-25: 50.2%) | | | 47.2% (Sep-25: 46.4%) | | |
| Sold after 121+ days | 6.4% (Sep-25: 7.4%) | | | 10.8% (Sep-25: 12.0%) | | |
| Dollar value of sales | $1,042.7M | −6.5% | −10.3% | $127.3M | −9.5% | −14.4% |

- **Total sales:** 2,169 units (DERIVED: 1,745 + 424, which matches the press figure).
- **SFH all-time high median:** $490,000, set May and June 2026 (press, SECONDARY). September's $470,000 is 4.1% below it (DERIVED).
- **Months of supply:** "5 months", up from about 4 a year earlier (press, SECONDARY). DERIVED check: 10,791 listings without offers ÷ 2,169 sales = 4.98. SFH alone is 4.58; condo/TH alone is 6.59 (DERIVED).
- **Cash share:** **23.5%** (Sep-25: 23.0%). **Distressed share** (short sales + foreclosures): **1.1%** (Sep-25: 0.5%). Both come from the LVR press release via [Fox5, 2026-10-06](https://www.fox5vegas.com/2026/10/06/las-vegas-realtors-report-fewer-homes-selling-interest-rates-rise/) (SECONDARY). Neither appears in the stats PDF. Cash share and distressed share **are in the press release only**, and that release cannot be curled.
- ⚠️ **Year check:** the KTNV and Review-Journal "$470,000 September median" stories are **September 2025**. That month happens to have the same median, so a 2025 story is easy to mistake for this one. Rejected.

## 2. Pending-sale fallthrough (cancellations): Redfin: PRIMARY dataset

- **File:** `https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_html_public_dashboards/contract_cancellations.csv.gz` (linked from [Redfin Data Center](https://www.redfin.com/news/data-center/home-purchase-cancellations/)).
- **curl:** **YES (200).** S3 Last-Modified was 2026-10-22. The **next update is Tue 2026-11-17** (stated on the Data Center page).
- **Series:** `PERCENT_PENDINGS_FALLEN_THROUGH`, `FREQUENCY="monthly"`, `REGION_NAME="Las Vegas, NV metro area"`. Monthly values are **seasonally adjusted**; weekly ("four_weeks") values are not. The data goes back to 2012 and is "subject to revision."

| Month (2026) | Las Vegas | YoY (pts) | National | Las Vegas rank of 50 |
|---|---|---|---|---|
| Sep | **18.58%** | **+2.66** | **14.54%** | **#3** (behind Jacksonville 19.88%, Tampa 18.76%; tied with Orlando 18.58%) |
| Aug | 18.68% | +2.77 | 14.22% | |
| Jul | 17.74% | +2.36 | 14.14% | |
| Jun | 17.33% | +0.82 | 13.69% | |
| Jan–May | 15.76–16.61% | about 0 | | |

- **Reading:** Las Vegas was flat YoY through May. YoY has been rising since June and was +2.7 points in August–September. September 2026 is Las Vegas's highest reading since **June 2022 (22.51%)**, excluding the March 2020 COVID spike (41.2%).
- ⚠️ **Two Redfin bases that do not reconcile:** press releases quote **not seasonally adjusted** rates and counts. For example, Las Vegas December 2025 was 19% in the press release but 16.58% in the dataset. National December 2025 was 16.3% in the press release but 13.55% in the dataset. National July 2026 cancellations were 47,189 in the press release (via First Trust) but 46,243 in the dataset. **Use the dataset only and never mix the two bases.**

## 3. S&P Cotality Case-Shiller Las Vegas: PRIMARY via FRED

- **Files:** `https://fred.stlouisfed.org/graph/fredgraph.csv?id=LVXRNSA` (not seasonally adjusted) and `id=LVXRSA` (seasonally adjusted). **curl: YES, but only without a browser user-agent.** The `-A 'Mozilla/5.0'` call returned code 000; plain curl worked.
- **Cadence:** monthly, on the last Tuesday of the month, with about a two-month lag. August data came out 2026-10-27. **September data is due about Tue 2026-11-24.**

| | NSA | SA |
|---|---|---|
| Aug-2026 index level | **298.55** | 295.07 |
| MoM | −0.56% | −0.33% (DERIVED) |
| YoY | −1.29% | −1.26% (DERIVED) |
| All-time peak | 305.90 (May-2025) | 305.18 (Feb-2025) |
| Drawdown from peak | **−2.41%** (DERIVED) | −3.31% (DERIVED) |

- **Context (DERIVED):** the 2006 bubble peak was 234.78 (Aug-2006) and the trough was 89.87 (Mar-2012). The current peak is about 30% above the 2006 peak in nominal terms.
- **Revision:** Case-Shiller revises recent months, so store each reading with its vintage.

## 4. ATTOM foreclosure rates (Nevada and Las Vegas): PRIMARY

- **Source:** monthly reports at `attomdata.com/news/market-trends/foreclosures/<month>-2026-foreclosure-market-report/`; the mid-year report is at `.../2026-mid-year-foreclosure-market-report/`.
- **curl:** **YES (200)** for the report pages and for `https://www.attomdata.com/feed/` (RSS, the best way to detect new releases).
- **Units:** "1 in X housing units with a filing" (monthly or quarterly), or "% of housing units" (half-year or annual).

| Period | Nevada | Las Vegas MSA | National | Published |
|---|---|---|---|---|
| Aug-2026 (monthly) | **1 in 1,920, #2** (South Carolina #1 at 1 in 1,547) | not in the top 5 metros | 1 in 3,569 | 2026-09-17 |
| Jul-2026 (monthly) | **1 in 1,703, #1** | **1 in 1,394, #3** of metros with population ≥200K | 1 in 3,603 | 2026-08-27 |
| Jun-2026 (monthly) | 1 in 2,508, #4 | n/a | 1 in 3,656 | 2026-07-16 |
| Q2-2026 (quarterly) | 1 in 871, #5 | n/a | n/a | 2026-07-16 |
| **H1-2026** | **0.22%, 1 in 452, #6**; 2,935 properties; +6.38% vs H1-2025; +17.64% vs H1-2024 | not in the H1 text | 0.16%, 1 in 632; 227,548 properties; +21.26% | 2026-07-16 |
| Q2-2026 foreclosure timeline | **1,507 days** (5th longest) | | | 2026-07-16 |

- ⚠️ **The September / Q3-2026 report is NOT out yet.** As of 2026-10-28 the RSS feed shows no Q3 foreclosure report, and the guessed URLs return 404. It is expected late October or early November. Its Q3 Nevada rank is the next reading.
- ⚠️ **Basis discipline (same rule as Florida):** monthly, quarterly, H1 and annual rates are different bases and must not be compared with each other. Nevada's very long foreclosure timeline (1,507 days) means REO completions lag starts heavily.

## 5. NY Fed Household Debt and Credit (CCP/Equifax): Nevada, PRIMARY

Two files cover Nevada. They have different cadences, and only one of them has a state-level credit-card series.

**(a) Annual state file:** `https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/area_report_by_year.xlsx`. **curl: YES.** It is titled "State Level Household Debt Statistics 2003-2025" and was published **February 2026**. It holds **Q4 values only**, for all 50 states plus DC. Sheets used: `creditcard_delinq` = "Percent of Credit Card Debt Balance 90+ Days Delinquent"; `mortgage_delinq` = "Percent of Mortgage Debt Balance 90+ Days Delinquent" (excludes HELOC). The panel is a 5% sample.

| Q4 | NV credit card 90+ (% of balance) | US | FL | NV mortgage 90+ | US |
|---|---|---|---|---|---|
| 2023 | 12.95% | 9.66% | 11.68% | 0.63% | 0.58% |
| 2024 | **14.53%** (the old row) | 11.24% | 13.49% | 0.69% | 0.71% |
| **2025** | **16.28%, #1 of 51** | 12.36% | 14.94% (#2) | 0.86% (#28) | 0.94% |

The next annual update is expected about February 2027.

**(b) Quarterly report data:** `.../data/xls/HHD_C_Report_2026Q2.xlsx`. **curl: YES.** It was published **2026-08-11** (the Q2-2026 report). Nevada is one of 11 "select states" (AZ, CA, FL, IL, MI, NJ, **NV**, NY, OH, PA, TX). **This file has no Nevada credit-card series.** It does have:

| Sheet | 25Q2 | 25Q3 | 25Q4 | 26Q1 | **26Q2** | All US 26Q2 |
|---|---|---|---|---|---|---|
| Page 36: % of **mortgage** debt 90+ days late | 0.73 | 0.99 | 0.74 | 1.38 | **1.94** (highest of the 11 states; Florida 1.62) | **0.99** |
| Page 35: % of **all** balances 90+ days late | 2.91 | 3.05 | 2.93 | 3.34 | **3.94** | 3.31 |
| Page 38: quarterly transition into 90+ (all debt) | 2.70 | 3.37 | 3.70 | 3.59 | **3.59** | n/a |
| Page 37: quarterly transition into 30+ (all debt) | 5.69 | 5.77 | 5.89 | 5.45 | **4.79** | n/a |
| Page 39: % of consumers with a new foreclosure | 0.01 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |
| Page 40: % of consumers with a new bankruptcy | 0.08 | 0.08 | 0.07 | 0.07 | **0.09** (highest of the 11) | 0.05 |

- ⚠️ **Sampling noise:** Nevada is a small state in a 5% panel. Its mortgage 90+ series moved 0.74 → 1.38 → 1.94 in two quarters; Arizona moved 0.36 → 1.37 → 0.96 over a similar window. **Treat a single-quarter Nevada move as an observation, not a trend**, until it holds for two prints. The **NV mortgage 1.94% vs national 0.99%** reading is the most striking number in this lane and the noisiest.
- **The quarterly and annual files are different series and must not be spliced.** The annual file's own note says state totals "may not match" the quarterly report. Its Q4-2025 Nevada mortgage reading was **0.86%**; the quarterly file's 25Q4 Nevada reading was **0.74%**.
- ⚠️ **Scoring-model break (HOMER docket row 8):** the Q2-2026 workbook footnote reads "Credit Score: **VantageScore 4.0 (2026Q1+); Equifax Riskscore 3.0 (prior)**" (Page 7, mortgage originations by score). Page 9 (auto) still says Riskscore 3.0. The break affects **credit-score-banded series** (originations by score, any score-tier cut). **The delinquency-status series above are not score-banded**, and this workbook flags no break on them. Still, any 2026Q1 step change should be checked against the break before it is read as stress.
- **Next release:** Q3-2026 is expected in **early November 2026**. Q3-2025 came out 2025-11-05; the media advisory usually appears about a week earlier, and none was posted as of 2026-10-28. The file name will be `HHD_C_Report_2026Q3.xlsx`. That URL currently returns an HTML 404 page with HTTP status 200, so **check the content-type, not the status code.**

## 6. ICE mortgage performance (Nevada)

- **ICE First Look**, September 2026 data, published **2026-10-27**. PDF: `https://s2.q4cdn.com/154085107/files/doc_news/ICE-First-Look-September-Delinquencies-Track-Seasonal-Norms-as-Foreclosure-Pipeline-Shifts-Toward-Recent-Vintages-2026.pdf`. **curl: YES.** Release list (JSON): `ir.theice.com/feed/PressRelease.svc/GetPressReleaseList?...` (curl: YES). The `ir.theice.com` HTML page returns 403.
- **Nevada is NOT in the September, August or July First Look.** The release prints only the top and bottom 5 states for non-current %, 90+ %, and 12-month change. There is no full state table.
- **Last time Nevada appeared:** February 2026 data, among the 5 states with the largest 12-month rise in non-current share: **+12.96% YoY** (relative change, not points). In January 2026 data it was +11.66% (SECONDARY via search; the PDFs were not re-pulled).
- **Full-state non-current rates** are in the ICE **Mortgage Monitor** (monthly, `icemortgagetechnology.com/resources/data-reports`; that page returned 200 to curl). Mortgage Monitor state tables are irregular. **There is no reliable monthly Nevada non-current figure from ICE.**
- **FHA share and FHA delinquency for Nevada: not pulled.** Candidate sources are the MBA National Delinquency Survey state tables (quarterly, subscription) and HUD's FHA Single Family Loan Performance Trends (monthly, national). **Gap: Nevada FHA DQ has no free primary source identified.**

## 7. Nevada stress context, October 2026 (context only: LABOR and MARCO own these domains)

| Item | Value | Period / published | Source | Label | curl |
|---|---|---|---|---|---|
| Apartment List metro rent (Las Vegas-Henderson-Paradise) | **$1,409**; **−2.35% YoY**; −0.06% MoM (US: $1,384, +0.06% YoY) | Oct-2026 file (`..._2026_10.csv`) | [Apartment List](https://www.apartmentlist.com/research/category/data-rent-estimates) Summary CSV | PRIMARY | **YES** (ctfassets CSV links on the page) |
| Apartment List vacancy index, LV metro | **7.52%** (Oct-25: 7.07%; US: 6.96%) | Oct-2026 | Vacancy_Index CSV | PRIMARY | YES |
| Apartment List concession rate, LV metro | **54.65% of listings** (Oct-25: 38.22%; US: 31.95%) | Oct-2026 | Concession_Rates CSV | PRIMARY | YES |
| Third-party multifamily vacancy | about 10.8%; asking rent $1,473 (−2.25% YoY) | Q2-2026 | Lee & Associates | SECONDARY broker report | not tested |
| Nevada unemployment (SA) | **4.7%** (Aug: 4.8%). Las Vegas MSA (NSA) 4.8%, down 0.9 points YoY | Sep-2026, released 2026-10-20 | DETR via Fox5/News3LV | SECONDARY | detr.nv.gov returns **403** |
| LV visitor volume | about 3.2M, +2.7% YoY (Jul-2026); YTD 22.75M, +0.5% | Jul-2026 (Sep-2026 not found) | LVCVA via Fox5 | SECONDARY | lvcva.com returns **403** |
| New homes (Home Builders Research) | no 2026 September figure found. Latest seen: Jan-2026, 790 net sales (−19% YoY), 643 permits (−39%) | Jan-2026 | HBR via the Review-Journal | SECONDARY | reviewjournal.com returns **403** |

SHA-256 of the Apartment List Oct-2026 files: Summary `73dd2ae6…466b`; Vacancy `ed5734c9…6306`; Concessions `186cb94d…3e46`.
**The concession rate is the strongest Las Vegas rental-stress tell:** 54.65% is 22.7 points above the US (DERIVED) and up 16.4 points YoY (DERIVED).

## 8. Recommended recurring sources

| # | Series | Source / file | Cadence | Next | curl | Class |
|---|---|---|---|---|---|---|
| 1 | LVR SFH and condo median, sales, listings without offers | members.lasvegasrealtor.com stats PDF (token URL) | Monthly, about the 6th | about 2026-11-05 (Oct data) | YES (PDF) | PRIMARY |
| 1b | LVR cash share and distressed share | LVR press release (via Fox5/News3LV) | Monthly | same | NO (429) | SECONDARY |
| 2 | Las Vegas pending-sale fallthrough (SA) and rank | Redfin `contract_cancellations.csv.gz` | Monthly | **2026-11-17** | YES | PRIMARY |
| 3 | Case-Shiller Las Vegas (LVXRNSA/LVXRSA) | FRED CSV | Monthly, last Tuesday | about 2026-11-24 (Sep data) | YES (no browser user-agent) | PRIMARY (via FRED) |
| 4 | Nevada and Las Vegas foreclosure rate and rank | ATTOM monthly, quarterly, mid-year, year-end; RSS feed | Monthly, mid-month | Q3/Sep report imminent | YES | PRIMARY |
| 5a | Nevada mortgage 90+, all-debt 90+, transition rates, bankruptcies | NY Fed `HHD_C_Report_YYYYQn.xlsx` (Pages 35–40) | Quarterly | **early Nov 2026 (Q3)** | YES | PRIMARY |
| 5b | **Nevada credit-card 90+ (% of balance)**: the charter's "CC 90+ DQ" | NY Fed `area_report_by_year.xlsx` | **Annual (Q4 values only)** | about Feb 2027 | YES | PRIMARY |
| 6 | Nevada non-current (only when it enters the top/bottom 5) | ICE First Look PDF (q4cdn) + IR JSON feed | Monthly, about the 4th week | late Nov 2026 | YES | PRIMARY |
| 7 | Las Vegas rent, vacancy, concessions | Apartment List CSVs (ctfassets) | Monthly, about month-end | late Nov 2026 | YES | PRIMARY |

**Charter correction to propose:** the charter's "CC 90+ DQ" signal is **annual** at state level, not quarterly. The quarterly NY Fed report gives Nevada mortgage and all-debt 90+ rates but **no Nevada credit-card series**.
