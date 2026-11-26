# Florida county distress counts, flooded against dry: a pre-flood baseline (pilot)
**Date:** 2026-11-26 (work 11:40 to 12:01 ET, times from `date`) | **Mode:** Cold, WALTER request REQ-DEWEY-20261123-001 (Will-approved 2026-11-23 18:24 ET in WALTER's terminal; DOCKET L1246, due 12/01), taken up in PROME prome-80's Thanksgiving assignment | **Confidence:** High on counts as published and on the HUD document read; Medium on comparability between the clerk and court series; Low on any flood attribution (not yet testable)

⚠️ **Counts only.** No parcel, address, case number, book and page, or person's name appears in this report or in any packet. Working files stayed outside the repository and the one recorded document read was deleted after reading.

## Key finding

A monthly baseline exists and is cheap to keep, but not from the county clerks in three of the four counties. Brevard's clerk index returns monthly lis pendens and HUD subordinate-mortgage totals directly. The other three counties are closed to automated counting: Seminole by a bot challenge, Marion by a login with reCAPTCHA, and Volusia by terms barring redistribution. The state court foreclosure-filing series covers all four counties, and Brevard's clerk counts track it closely: correlation 0.94 over 20 months, totals within 3%. **The falsifier already bites before the flood:** in the first half of 2026, foreclosure filings ran 25% to 52% above a year earlier in Brevard, Volusia and Seminole, against 11% in the pre-registered dry control (Marion). A later gap over Marion will not by itself show a flood effect. Brevard's flood-driven filings will also be held down by HUD's 90-day FHA foreclosure moratorium from the 2026-11-24 declaration, while Seminole and Volusia, outside it, are not.

**Brevard's HUD partial-claim mortgages** show the 2025-10-01 rule change plainly: 111.8 a month (December 2024 to September 2025), 26.0 a month (November 2025 to February 2026), 67.0 a month (March to October 2026), with the median lien rising from about $11,000 to $15,000 to $23,000. Only the post-March-2026 level is a usable pre-flood baseline.

**Step 0, the HUD lien:** the May 2026 HUD lien in the Silver Pines sample **is a partial claim**. The recorded document is titled "Subordinate Mortgage" to the Secretary of Housing and Urban Development, with "Partial Claim" printed in its footer, signed in April 2026 and prepared for a non-bank servicer's loan-modification team. HOMER's PIPELINE row ("HUD Partial Claims ENDED 2025-10-01") is wrong as worded. HUD's own Q&A says that from 2025-10-01, permanent home-retention options, which include the standalone partial claim, are limited to **once every 24 months**, except in declared disaster areas [PRIMARY: HUD, Loss Mitigation Options Questions and Answers, dated 2025-09-18]. The COVID-19 recovery options did end on 2025-09-30. So the HUD series is kept: it counts post-default workouts, not ended programmes.

## Feasibility, county by county (step 1)

| County | Role | Clerk index route | Result | What was used |
|---|---|---|---|---|
| Brevard | flooded, in DR-4956-FL | AcclaimWeb document-type search with record-date range; accuracy disclaimer only, no CAPTCHA, no account | **FEASIBLE**: one query returns a monthly total; 201 lis pendens rows = 201 distinct documents (October 2026 check) | Clerk counts, 2024-11 to 2026-11, and court filings |
| Seminole | flooded basin, outside the declaration | DuProcess web inquiry | **STOPPED**: HTTP 403 with `cf-mitigated: challenge` (Cloudflare managed challenge), 11/26 late morning; not retried | Court filings only |
| Volusia | flooded basin, outside the declaration | clerk.org official-records inquiry | **NOT ENTERED**: the access agreement limits use to personal, informational use and "expressly prohibit[s] ... publishing on-line ... or otherwise disseminating data or information accessed". This repository is public, so DEWEY did not accept it | Court filings only |
| Marion | dry control, pre-registered | BrowserView | **STOPPED**: the site's own settings file reports `freeAccessWithoutLogin: 0` (login required) and reCAPTCHA v3 configured; no account was created | Court filings only |

**Substitute source for all four:** University of Florida Shimberg Center, Florida Housing Data Clearinghouse, "Foreclosure Filings, Monthly, 2019-2026", compiled from the Office of the State Courts Administrator (OSCA) and the clerks [INSTITUTIONAL: Shimberg Center, pulled 2026-11-26]. ⚠️ **Its July, August and September 2026 rows are exact copies of April, May and June 2026** in all five counties pulled (15 of 15 cells identical). They are excluded below; the usable series ends **June 2026**.

## Control county, chosen before any count was seen (step 3)

Written to a timestamped working file at 11:45:27 ET, before any county count was viewed: **Marion**, fallback Alachua for the clerk route. Why: outside both 2026 federal declarations (DR-4956-FL flooding: Brevard, Hardee, Indian River, Martin, Okeechobee, Palm Beach, St. Lucie; DR-4955-FL Isaias: 15 Panhandle counties [PRIMARY: OpenFEMA DisasterDeclarationsSummaries, pulled 2026-11-26]); inland, with its population centred on Ocala away from the St. Johns floodplain; no November 2026 flood mention on AEOLUS, CORAL or WALTER surfaces; size between Seminole and Volusia. Known weaknesses: its eastern edge touches Lake George on the St. Johns (sparsely settled forest), and it took less of the October 2024 Milton damage than the three treated counties. Rejected: Lake (flooding on the St. Johns), Polk (borders declared Hardee), Osceola and Orange (upper St. Johns basin), the Gulf counties hit by 2024 surge, and the river counties further north. The clerk fallback (Alachua) was not needed for the court series; its counts were pulled in the same request and are shown only in the falsifier section, labelled as not pre-registered.

## Counts (step 2)

### A. Court foreclosure filings, monthly, all four counties (Shimberg / OSCA)

| Month | Brevard | Volusia | Seminole | Marion (control) |
|---|---|---|---|---|
|---|---|---|---|---|
| 2024-11 | 41 | 44 | 34 | 40 |
| 2024-12 | 51 | 27 | 25 | 34 |
| 2025-01 | 45 | 42 | 20 | 43 |
| 2025-02 | 83 | 65 | 41 | 73 |
| 2025-03 | 101 | 88 | 37 | 70 |
| 2025-04 | 103 | 89 | 38 | 77 |
| 2025-05 | 80 | 67 | 40 | 55 |
| 2025-06 | 91 | 79 | 38 | 93 |
| 2025-07 | 88 | 104 | 35 | 75 |
| 2025-08 | 88 | 91 | 51 | 79 |
| 2025-09 | 117 | 110 | 60 | 78 |
| 2025-10 | 111 | 117 | 62 | 75 |
| 2025-11 | 89 | 86 | 47 | 56 |
| 2025-12 | 87 | 125 | 57 | 69 |
| 2026-01 | 97 | 100 | 54 | 72 |
| 2026-02 | 85 | 97 | 53 | 62 |
| 2026-03 | 111 | 94 | 53 | 77 |
| 2026-04 | 131 | 119 | 56 | 93 |
| 2026-05 | 100 | 103 | 41 | 77 |
| 2026-06 | 106 | 110 | 69 | 77 |

Definition: civil foreclosure cases filed, by month, as compiled by Shimberg from OSCA and clerks; the source notes the majority are residential. Definition breaks: October to December 2024 are low in every county (Helene and Milton, court closures and the FHA disaster foreclosure moratorium); recording and reporting lags are the compiler's.

### B. Brevard clerk: lis pendens recorded, monthly, by plaintiff type

| Month | All | Lender or servicer | Association | Government | Other |
|---|---|---|---|---|---|
|---|---|---|---|---|---|
| 2024-11 | 67 | 27 | 18 | 2 | 20 |
| 2024-12 | 76 | 30 | 25 | 0 | 21 |
| 2025-01 | 68 | 26 | 13 | 1 | 28 |
| 2025-02 | 120 | 83 | 11 | 1 | 25 |
| 2025-03 | 126 | 75 | 21 | 4 | 26 |
| 2025-04 | 143 | 89 | 32 | 0 | 22 |
| 2025-05 | 113 | 64 | 18 | 1 | 30 |
| 2025-06 | 105 | 64 | 23 | 1 | 17 |
| 2025-07 | 112 | 62 | 25 | 2 | 23 |
| 2025-08 | 103 | 68 | 12 | 0 | 23 |
| 2025-09 | 134 | 94 | 20 | 2 | 18 |
| 2025-10 | 134 | 87 | 28 | 3 | 16 |
| 2025-11 | 105 | 68 | 23 | 1 | 13 |
| 2025-12 | 127 | 93 | 15 | 1 | 18 |
| 2026-01 | 132 | 88 | 14 | 1 | 29 |
| 2026-02 | 129 | 76 | 26 | 2 | 25 |
| 2026-03 | 144 | 86 | 23 | 3 | 32 |
| 2026-04 | 150 | 92 | 31 | 2 | 25 |
| 2026-05 | 129 | 79 | 22 | 1 | 27 |
| 2026-06 | 140 | 97 | 14 | 0 | 29 |
| 2026-07 | 151 | 80 | 29 | 9 | 33 |
| 2026-08 | 110 | 72 | 23 | 0 | 15 |
| 2026-09 | 107 | 74 | 15 | 2 | 16 |
| 2026-10 | 201 | 115 | 20 | 4 | 62 |
| 2026-11 | 108 | 69 | 20 | 3 | 16 |

Query: AcclaimWeb document types LIS PENDENS (LP) and (LP1), record-date range = calendar month, one row per document (checked: total = distinct documents). Plaintiff type is a keyword rule on the plaintiff's name (lender words such as bank, mortgage, servicing, loan; association words such as association, homeowners, condominium; government words such as county, city, United States), so "other" holds individuals, unrecognised LLCs and trusts. **November 2026 is partial** (index through 11/25, 17 recording days). **October 2026 (201) includes one LLC plaintiff with 33 filings**, most on a single recording day (40 lis pendens recorded 10/26); without it October is 168, still above the January to September 2026 mean of 132.4. October is pre-flood: the declared incident period began 10/31.

**Cross-check against series A, Brevard, 2024-11 to 2026-06 (20 months):** clerk lender plus association lis pendens 1,862 against court filings 1,805 (ratio 1.03), correlation 0.94; all lis pendens 2,357 (ratio 1.31). The clerk series is a fair, faster stand-in for court filings, which lag by months.

### C. Brevard clerk: mortgages recorded to HUD, monthly

| Month | All mortgages recorded | To HUD | HUD, $150k or less | HUD, over $150k | HUD, no amount | Median HUD amount, $150k or less ($) |
|---|---|---|---|---|---|---|
| 2024-11 | 1499 | 67 | 65 | 1 | 1 | 10,776 |
| 2024-12 | 1879 | 81 | 79 | 2 | 0 | 10,937 |
| 2025-01 | 1561 | 133 | 127 | 6 | 0 | 11,175 |
| 2025-02 | 1547 | 102 | 99 | 3 | 0 | 11,048 |
| 2025-03 | 1864 | 124 | 121 | 3 | 0 | 11,989 |
| 2025-04 | 2061 | 138 | 135 | 3 | 0 | 13,134 |
| 2025-05 | 2123 | 120 | 113 | 7 | 0 | 12,479 |
| 2025-06 | 1928 | 111 | 107 | 4 | 0 | 12,638 |
| 2025-07 | 2057 | 106 | 100 | 6 | 0 | 13,370 |
| 2025-08 | 1930 | 95 | 91 | 4 | 0 | 12,884 |
| 2025-09 | 1941 | 108 | 105 | 3 | 0 | 15,023 |
| 2025-10 | 2148 | 85 | 82 | 3 | 0 | 15,113 |
| 2025-11 | 1618 | 31 | 29 | 2 | 0 | 13,785 |
| 2025-12 | 2145 | 28 | 27 | 1 | 0 | 8,146 |
| 2026-01 | 1525 | 18 | 14 | 4 | 0 | 12,579 |
| 2026-02 | 1801 | 27 | 24 | 2 | 1 | 15,048 |
| 2026-03 | 2214 | 56 | 53 | 3 | 0 | 19,435 |
| 2026-04 | 2136 | 67 | 67 | 0 | 0 | 16,103 |
| 2026-05 | 2065 | 76 | 75 | 0 | 1 | 15,636 |
| 2026-06 | 2223 | 79 | 76 | 3 | 0 | 14,722 |
| 2026-07 | 2076 | 74 | 73 | 1 | 0 | 16,785 |
| 2026-08 | 1995 | 57 | 54 | 3 | 0 | 18,587 |
| 2026-09 | 1848 | 66 | 63 | 2 | 1 | 21,513 |
| 2026-10 | 1776 | 61 | 60 | 1 | 0 | 18,539 |
| 2026-11 | 1326 | 57 | 56 | 1 | 0 | 22,744 |

Query: AcclaimWeb mortgage document types (MORTGAGE, the three tax-exempt mortgage types, DEED/MORTGAGE COMBO, MODIFIED MORTGAGE), grantee matching "Housing and Urban Development" or "Secretary of Housing", one row per document. Every HUD match came back as MORTGAGE or MODIFIED MORTGAGE. Banding by recorded amount separates partial-claim-sized liens from anything reverse-mortgage-sized; the over-$150k band is 0 to 7 a month and was not read. November 2026 is partial (index through 11/25).

**The 2025-10-01 policy break is visible:** 111.8 a month from December 2024 to September 2025, then 26.0 a month from November 2025 to February 2026, then 67.0 a month from March to October 2026. The median lien rose from about $11,000 to $15,000 to $23,000. A recorded lien trails its signing by about a month (the Silver Pines document: signed in April, recorded in May). **So the HUD series measures FHA workouts under a new rule set, and only its post-March-2026 level is a usable pre-flood baseline.**

## Falsifier (step 4)

**The pre-flood trends already differ.** Foreclosure filings, first half of each year (series A):

| County | H1 2024 | H1 2025 | H1 2026 | 2025 vs 2024 | 2026 vs 2025 |
|---|---|---|---|---|---|
| Brevard | 477 | 503 | 630 | +5% | **+25%** |
| Volusia | 444 | 430 | 623 | -3% | **+45%** |
| Seminole | 264 | 214 | 326 | -19% | **+52%** |
| Marion (control) | 338 | 411 | 458 | +22% | **+11%** |
| Alachua (not pre-registered, shown for spread) | 129 | 139 | 205 | +8% | +47% |

All three treated counties were pulling away from Marion **before** the flood, and Alachua, also dry, rose as fast as Volusia. A post-flood gap over Marion is therefore not evidence of a flood effect unless it is larger than this pre-existing drift, and with one dry county the comparison has no measure of how much dry counties differ from each other. Monthly counts are small (Seminole averages about 45 a month), so single months move 20% to 30% on noise. **Minimum honest test after the flood:** compare each treated county's change against its own 2026 pre-flood path and against more than one dry county, over at least a quarter, and read the clerk lender lis pendens in Brevard as the early series.

## Counter-evidence and limits

- **The flood may not show up in foreclosures for many months, and in Brevard the measure is mechanically suppressed.** In a Presidentially-declared major disaster area (public assistance, individual assistance or both), FHA loans are under a foreclosure moratorium for 90 days from the declaration, covering new and pending foreclosures, plus an automatic 90-day servicer extension after it [PRIMARY: HUD ML 2025-06, Handbook 4000.1 III.A.2.l.ii(A)]. DR-4956-FL was declared 2026-11-24, so FHA filings in Brevard are held back to about 2027-02-22. Seminole and Volusia, outside the declaration, get no moratorium. **A lower Brevard count over the next quarter is the moratorium, not health**; the lis pendens index does not say which loans are FHA, so for that period read Brevard's association filings and the outside-declaration counties instead.
- **HUD seconds also rise for reasons unrelated to the flood:** the 24-month limit took effect 2025-10-01, so a fall in HUD subordinate mortgages after that date is a policy break, not improvement.
- **Lis pendens includes non-mortgage suits** (association liens, quiet title, contract disputes); the plaintiff split is a keyword rule, not a document read.
- **The court series is a compilation**, already shown to carry one copy error; its July to September 2026 values are unusable until it is corrected.
- **Only Brevard has a clerk series.** For Seminole and Volusia, the counties the river flood is now reaching, the only count is the lagging court series.

## Source Quality Assessment

Primary for Brevard clerk counts (the county's own index, queried directly), the HUD document (recorded image read on screen), HUD policy (HUD's Q&A PDF) and the declarations (OpenFEMA API). Institutional for series A: a university compilation of OSCA data, cross-checked against Brevard's primary clerk counts (0.94), with one demonstrated copy defect. Weakest links: the plaintiff-type keyword rule and the single dry control.

## References

- Brevard Clerk Official Records (AcclaimWeb), document-type search: https://vaclmweb1.brevardclerk.us/AcclaimWeb/search/SearchTypeDocType (queried 2026-11-26 11:4x to 11:59 ET)
- Shimberg Center, Florida Housing Data Clearinghouse, foreclosure filings: https://flhousingdata.shimberg.ufl.edu/eviction-foreclosure/results?nid=500&nid=6400&nid=5900&nid=4100&nid=100 (pulled 2026-11-26)
- HUD, Loss Mitigation Options Questions and Answers (2025-09-18): https://www.hud.gov/sites/dfiles/Housing/documents/Loss_Mitigation_Options_Qs_As.pdf
- HUD Mortgagee Letter 2025-06 (2025-01-16): https://archives.hud.gov/news/2025/2025-06hsgml.pdf
- OpenFEMA DisasterDeclarationsSummaries, DR-4955 and DR-4956: https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries
- Seminole Clerk DuProcess (refused): https://recording.seminoleclerk.org/DuProcessWebInquiry/ · Volusia Clerk inquiry (terms not accepted): https://app02.clerk.org/or_m/ · Marion Clerk BrowserView (login): https://nvweb.marioncountyclerk.org/BrowserView/
- Prior DEWEY sample: `AGENTS/DEWEY/output/2026-11-23_flood-parcels-to-lenders-silver-pines.md`

## Process Report

**Searches run:** 5 web searches; about 12 site probes; about 200 Brevard index requests (two monthly passes plus tests, one-second spacing), 3 OpenFEMA calls, 1 Shimberg pull, 1 recorded-document download. Client name `research-bot/1.0` throughout.
**Kill conditions:** (a) no desk keeps a monthly county count (HOMER, CORAL, CARL and CREED searched; only national ATTOM and 2009 to 2011 history) → run; (b) one flooded county's clerk returns monthly totals → not killed; (c) the HUD lien is a partial claim → HUD series kept.
**Data gaps:** clerk counts for Seminole, Volusia and Marion; court filings after June 2026; HUD-lien counts outside Brevard.
**Source frustrations:** Cloudflare at Seminole; login at Marion; redistribution terms at Volusia; Shimberg's duplicated quarter; the recorded document is an image with no text layer.
**Confidence:** High on counts and the HUD read; Medium on comparability; Low on attribution, by design: no post-flood month exists yet.
**If I had more time/tools:** a second dry control with a usable clerk index; OSCA's own filing tables to replace the compilation's Q3 2026; ask Shimberg to correct the duplicated quarter.
**Suggestions:** keep the series by re-running the Brevard pull monthly and re-pulling Shimberg when it corrects Q3. *(Added 2026-11-26 15:40 ET, after delivery: on Will's word the client is kept as `scripts/brevard_counts.py`; `python3 scripts/brevard_counts.py lp YYYY-MM` and `hud YYYY-MM` reproduce tables B and C. It re-ran November 2026 lis pendens at 108, matching table B.)*

**Reproduction recipe:** (1) Brevard: accept the disclaimer (`POST /AcclaimWeb/search/Disclaimer?st=/AcclaimWeb/search/SearchTypeDocType`, `disclaimer=true`), then per month `POST /AcclaimWeb/search/SearchTypeDocType?Length=6` with `DocTypes` = `99,100` (lis pendens) or `106,158,159,161,170,118` (mortgage types), `RecordDateFrom`/`RecordDateTo` = the month, then `POST /AcclaimWeb/Search/GridResults` (`page`, `size=500`) until `total` is reached; HUD = grantee (`IndirectName`) matching "HOUSING AND URBAN" or "SECRETARY OF HOUSING", banded by `Consideration`. (2) Shimberg: the results URL above; table 4 is the monthly foreclosure table. (3) Declarations: OpenFEMA `$filter=disasterNumber eq 4955` and `4956`.
