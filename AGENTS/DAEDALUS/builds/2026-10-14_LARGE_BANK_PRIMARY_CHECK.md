# Large-bank desk: primary check of the $250B line, the name list and Q3 dates

**Written:** 2026-10-14 Wed ~20:30 ET (`date`). Research helper spawned by DAEDALUS. The only input is REGINALD's packet `inbox/2026-10-10_from-REGINALD_large-bank-desk-proposal-inputs.md`.
**Scope:** read-only. The only repo write is this file. No git state was changed.
**Tags used below:** `[P]` = primary source (regulation text, a Fed publication, an SEC filing or an issuer IR page). `[S]` = SECONDARY. `[M]` = MEMORY-UNVERIFIED. `[X]` = PROXY, my own arithmetic on primary inputs.

---

## 0. Bottom line

| Question | Answer |
|---|---|
| Is "$250B total assets" by itself the Category III line? | **No.** Category III means **≥$250B** average total consolidated assets, **OR ≥$100B plus ≥$75B** in any one of nonbank assets, weighted short-term wholesale funding or off-balance-sheet exposure. It also requires that the firm is neither a GSIB nor Category II (12 CFR 252.5(d)(1)) `[P]`. Every measure is a **four-quarter trailing average of quarterly-average balances**, not a period-end figure (12 CFR 252.2) `[P]`. |
| Does ">$250B" give the same set as "Category I–III"? | **No.** Northern Trust is **Category II at $179.3B**. Four foreign-bank IHCs are **Category III below $250B**: Barclays US, UBS Americas, RBC US and DB USA. Two firms are above $250B at period-end but were **Category IV** in the 2026 Fed list: FITB ($300.2B) and HBAN ($284.0B). |
| How many US top-tier firms are above $250B (period-end 6/30/2026)? | **16:** JPM · BAC · C · WFC · GS · MS · USB · COF · PNC · TFC · BK · SCHW · STT · AXP · FITB · HBAN. Two IHCs are also above it, both `[S]`: TD Group US ($507B) and BMO Financial Corp ($298B). |
| Which of those are missing from REGINALD's list of 10? | **BK and STT** (both Category I GSIBs), **SCHW** ($517.3B, Cat III), **AXP** ($308.2B, **Category II since Q2 2026**), **FITB** ($300.2B, moving to Cat III in Q3 2026) and **HBAN** ($284.0B). |
| Is the line stable? | **No, it is under live review.** On 9/25/2026 Reuters reported, from 4 unnamed sources, that the Fed will propose re-indexing the thresholds to nominal GDP (top line ~$960B–$1T, bottom ~$150B) `[S]`. **No proposal appears in the Fed press feed through 10/13/2026** `[P]`. The rule text is unchanged since 2019 (eCFR is current to 10/13/2026) `[P]`. |
| Does the proposed line cut through REGINALD's own cohort? | **Yes.** HBAN is in REGINALD's 14-bank MI3 cohort ("≤$250B" in the packet) but held **$284.0B** at 6/30/2026 `[P]`. The packet's perimeter split is already wrong for HBAN. |

---

## 1. Sources consulted (URL and access result)

| # | Source | URL | Result | Used for |
|---|---|---|---|---|
| 1 | eCFR web UI, 12 CFR 252.5 | ecfr.gov/current/title-12/.../section-252.5 | **FAILED.** 302 redirect to unblock.federalregister.gov (bot wall) | — |
| 2 | eCFR Versioner API: 252.5, 252.2, 238.10 | `ecfr.gov/api/versioner/v1/full/2026-10-13/title-12.xml?part=252&section=252.5` (and the same for 252.2 and part 238 §238.10) | **OK, HTTP 200** (needs a compression header). Title 12 is "up to date as of 2026-10-13". 252.5 text is identical on 10/01 and 10/13 | Threshold text `[P]` |
| 3 | eCFR part 252 version history | `.../api/versioner/v1/versions/title-12.json?part=252` | OK | Shows 252.5 has had no amendment since [84 FR 59099, Nov 1 2019]. Part 252 amendments dated 2026-10-02 touch only stress-test sections (252.14/.16/.42/.44/.54/.57 and App. A/B) |
| 4 | **FFIEC NIC "Holding Companies > $10B"** | https://www.ffiec.gov/npw/Institution/TopHoldings | **FAILED, HTTP 403**: page titled "CAPTCHA Error \| FFIEC" (WebFetch and curl). `?asOfDate=20260630` and `/npw/FinancialReport/FinancialDataDownload` also return 403 | **Not used.** No Y-9C figure in this report comes from NIC |
| 5 | Fed, 2026 Stress Test Results (6/24/2026), **Table 3** | https://www.federalreserve.gov/publications/files/2026-dfast-results-20260624.pdf | OK. Table 3 read with pdfminer at the coordinate level, pp. 8–9: 32 firms × "Risk Based Category" | Category per firm `[P]` |
| 6 | Fed press-release RSS | https://www.federalreserve.gov/feeds/press_all.xml | OK. Holds the last 20 items, 9/10–10/13/2026 | Shows no tailoring-threshold proposal. Stress-test final rule issued 9/30/2026 |
| 7 | Fed "Large Financial Institutions" page | federalreserve.gov/supervisionreg/large-financial-institutions.htm | **404** (guessed URL) | — |
| 8 | Fed Large Commercial Banks release (LBR), as of **6/30/2026** | https://www.federalreserve.gov/releases/lbr/current/default.htm | OK | **Bank-level** consolidated assets and bank RSSD IDs, including IHC subsidiary banks `[P]` |
| 9 | SEC XBRL frames, `us-gaap:Assets` CY2025Q3I → CY2026Q2I | `data.sec.gov/api/xbrl/frames/us-gaap/Assets/USD/CY2026Q2I.json` etc. | OK | Period-end total assets from 10-Q/10-K for every SEC filer `[P]` |
| 10 | SEC submissions JSON, 17 issuers | `data.sec.gov/submissions/CIK##########.json` | OK, fetched ~20:20 ET 10/14 | Which issuers have filed a Q3 Item 2.02 8-K `[P]` |
| 11 | Q3 2026 earnings 8-K exhibits: JPM, WFC, C, GS, BAC, MS, STT | sec.gov/Archives/edgar/data/… (accession numbers in §4) | OK | Total assets at 9/30/2026 `[P]` |
| 12 | 10-Qs for 6/30/2026: USB, FITB, HBAN, COF, PNC, TFC, AXP, SCHW | sec.gov/Archives/... `*-20260630.htm` | OK | Issuers' own category statements `[P]` |
| 13 | USB Q2-26 earnings supplement; HBAN Q2-26 EX-99.2 | sec.gov/Archives/edgar/data/36104/000003610426000039/a2q26earningssupplement.htm ; .../49196/000004919626000060/hban20260630_8kex992.htm | OK | Quarterly-average total assets, used for the `[X]` four-quarter proxy |
| 14 | Reuters via Spokesman-Review, 9/25/2026 | https://www.spokesman.com/stories/2026/sep/25/us-fed-plans-to-raise-bank-oversight-thresholds-so/ | OK | Indexing plan `[S]` |
| 15 | Cleveland Fed Economic Commentary 2026-07 (4/13/2026) | https://www.clevelandfed.org/publications/economic-commentary/2026/ec-202607-effect-of-size-thresholds-on-large-banks-2019-tailoring-framework | OK. No firm list | Context only |
| 16 | Wikipedia "List of largest banks in the United States" (cites FFIEC NIC, 6/30/2026) | https://en.wikipedia.org/wiki/List_of_largest_banks_in_the_United_States | OK | **IHC totals `[S]`.** Its figures for US BHCs match the SEC frames to the $1B, which is a cross-check |
| 17 | Issuer IR pages: PNC, BNY, Truist, Fifth Third, USB (PDF) | investor.pnc.com/…/detail/696 ; bny.com/…/130449.html ; ir.truist.com/2025-05-01-… ; ir.53.com/…/2025/… ; s203.q4cdn.com/711684571/…2026.pdf | OK | Q3 dates `[P]` |
| 18 | Capital One IR; Schwab IR (aboutschwab.com) | investor.capitalone.com/news-releases ; aboutschwab.com/investor-relations | **403** (WebFetch and curl) | COF date seen only through the search-indexed issuer page plus a wire mirror. SCHW date is `[S]` |
| 19 | Northern Trust PR; Nasdaq copy of the COF PR | northerntrust.com/…/2026/… ; nasdaq.com/press-release/… | **Timeout** | Dates taken from the search index of the issuer PR |
| 20 | Quartr MCP | — | **Unavailable** (re-authentication required) | — |
| 21 | OFR Bank Systemic Risk Monitor | financialresearch.gov/bank-systemic-risk-monitor/ | Page loads; no download URL surfaced | Not used (FR Y-15 indicators therefore unverified) |

---

## 2. The tailoring thresholds (12 CFR 252.5, Regulation YY; SLHC mirror 12 CFR 238.10, Regulation LL)

Rule text verbatim in substance from the eCFR API, current to 2026-10-13 `[P]`. Source rule: 84 FR 59032/59099 (Nov 1, 2019). SLHC version: 84 FR 59077.

| Category | Test (US BHC or US IHC; all values are averages per 252.2) | Citation |
|---|---|---|
| **Scope** | A US BHC with **≥$100B** average total consolidated assets must determine its category at least quarterly. IHCs and FBOs: Categories II–IV only. | 252.5(a)(1)–(3) |
| **I** | A "global systemically important BHC" identified under **12 CFR 217.402** (the GSIB method). Size is not the test. | 252.5(b) |
| **II** | **≥$700B** average total consolidated assets, **OR** (**≥$75B** average **cross-jurisdictional activity** AND **≥$100B** assets). Must not be a GSIB. | 252.5(c)(1) |
| **III** | **≥$250B** average total consolidated assets, **OR** (**≥$100B** assets AND **≥$75B** in at least one of: average total **nonbank assets** · average **weighted short-term wholesale funding** · average **off-balance-sheet exposure**). Must be neither a GSIB nor Category II. | 252.5(d)(1) |
| **IV** | **≥$100B** average total consolidated assets and none of the categories above. | 252.5(e)(1) |
| **Step-down (hysteresis)** | A firm stays in a category until it is below **every** trigger for **each of the four most recent calendar quarters**. For example, Category III ends only when assets are under $250B AND all three $75B indicators are under $75B, quarter by quarter, four times running. | 252.5(c)(2), (d)(2), (e)(2) |

How each measure is defined (12 CFR 252.2) `[P]`:

| Measure | Definition and source report |
|---|---|
| Total consolidated assets (BHC/IHC) | The **average of daily (or Wednesday) balances for the quarter, as reported on the FR Y-9C**, i.e. average balances, not the period-end balance sheet. |
| "Average …" (all measures) | The average over the **four most recent calendar quarters**, or fewer if fewer have been reported. |
| Cross-jurisdictional activity · weighted short-term wholesale funding | As reported on the **FR Y-15**. |
| Off-balance-sheet exposure | FR Y-15 total exposure **minus** total consolidated assets for the same quarter. |
| Total nonbank assets | As reported on the **FR Y-9LP**. |
| FBO | Uses **combined US assets** from the FR Y-7Q in place of total consolidated assets. |

⚠️ **The Fed's own plain-English summary drops the $100B floor.** Figure 3 of the 2026 stress-test results PDF describes Category III as "$250 billion or more in total assets **or** $75 billion or more in weighted short-term wholesale funding, nonbank assets, or off-balance-sheet exposure." The rule text requires ≥$100B as well. Quote the CFR, not the summary.

**Proposals and their status (2025–2026):**

| Item | Status as of 2026-10-14 | Source |
|---|---|---|
| Re-index the $100B / $250B / $700B thresholds to nominal GDP (top line → ~$960B–$1T; some $100B requirements → ~$150B; a TD Cowen note reportedly puts $250B → $375B) | **REPORTED, NOT PROPOSED.** Reuters (9/25/2026, 4 unnamed sources) says a proposal is "expected later this year". Bowman floated GDP indexing in January 2026. The Fed declined comment. Nothing in the Fed press RSS from 9/10 to 10/13 | Spokesman-Review/Reuters `[S]`; Fed RSS `[P]`. The $375B figure comes from a search summary only and was **not opened at source** |
| Congressional bills to raise or index the thresholds (H.R. 6553, S. 5452) | **UNVERIFIED.** Seen only in a search-result summary; not checked on congress.gov | `[S]` |
| Capital re-proposal (the Basel III "endgame" successor): revised standardized approach for Cat III/IV, expanded risk-based approach for Cat I/II, **AOCI recognition for Cat III/IV with a 5-year transition** | **PROPOSED 3/19/2026** (joint FDIC/FRB/OCC). No final rule seen. This is the "AOCI / Basel endgame" row on REGINALD's calendar | Truist 10-Q for 6/30/2026 `[P]` |
| Stress-test transparency / volatility-reduction rule | **FINAL 9/30/2026**; eCFR amendments effective 10/02/2026. Separately, SCBs were held at 2025 levels until 2027 (Fed, 2/4/2026) | Fed RSS `[P]`; DFAST 2026 text `[P]` |

---

## 3. Firms with ≥$100B in total assets

Period-end total assets at **6/30/2026**, plus **9/30/2026** where the firm has already reported. Ranked by 6/30/2026.

Column keys:
- **Cat:** category from the Fed 2026 stress-test results, Table 3 `[P-D]`, updated where the issuer's own 6/30/2026 10-Q says otherwise `[P-Q]`.
- **Bank RSSD:** the lead subsidiary bank's ID from the Fed LBR at 6/30/2026 `[P]`. **Holding-company RSSDs are not shown** because NIC was unreachable, and none are filled from memory (REGINALD's VLY/CIK lesson).
- **4Q proxy:** the average of four period-end balances, Q3-25 to Q2-26 `[X]`, unless marked "qtr-avg" (the average of four quarterly-average balances from the issuer's own release, which is closer to the rule).

| # | Holding company | Type | Bank RSSD (lead bank, $B at 6/30) | Total assets 6/30/26 ($B) | 9/30/26 ($B) | Cat | 4Q proxy ($B) | Asset source |
|---|---|---|---|---|---|---|---|---|
| 1 | JPMorgan Chase & Co. | BHC | 852218 (4,091.3) | **5,015.1** | **5,091.5** | I | 4,725.2 | 10-Q XBRL `[P]`; 9/30 from Q3 supplement `[P]` |
| 2 | Bank of America Corp. | BHC | 480228 (2,654.6) | **3,499.2** | **3,427.7** | I | 3,452.7 | 10-Q XBRL; Q3 EX-99.3 `[P]` |
| 3 | Citigroup Inc. | BHC | 476810 (1,976.2) | **2,895** | **2,941** | I | — | Q3 release, "EOP assets ($B)" 2Q26/3Q26 columns `[P]`. Citi's 2026 10-Q XBRL has no `Assets` fact (anomaly). NIC via Wikipedia shows 2,894 `[S]` |
| 4 | Wells Fargo & Co. | BHC | 451965 (1,907.9) | **2,282.2** | **2,253.3** | I | 2,174.9 | 10-Q XBRL; Q3 EX-99.2 `[P]` |
| 5 | Goldman Sachs Group | BHC | 2182786 (758.8) | **2,127.7** | **2,182** | I | 1,951.3 | 10-Q XBRL; Q3 release balance sheet ($B) `[P]` |
| 6 | Morgan Stanley | BHC | 1456501 (419.3) + 2489805 (250.4) | **1,675.1** | **1,692.3** | I | 1,510.4 | 10-Q XBRL; Q3 supplement `[P]` |
| 7 | U.S. Bancorp | BHC | 504713 (705.6) | **725.9** | 10/15 | III | **686.6 qtr-avg** | 10-Q XBRL; Q2 supplement averages `[P]`. ⚠️ $13B below the **$700B Category II** line on the qtr-avg basis; period-end is already above it |
| 8 | Capital One Financial | BHC | 112837 (662.2) | **673.8** | 10/20 | III (10-Q confirms) | 671.9 | 10-Q XBRL `[P]`. The Discover acquisition is already in the base ($661.9B at 9/30/2025). Closing date `[M]` |
| 9 | PNC Financial Services | BHC | 817824 (609.8) | **616.0** | 10/15 | III | 590.4 | 10-Q XBRL `[P]` |
| 10 | Truist Financial | BHC | 852320 (548.3) | **556.0** | 10/16 | III (10-Q confirms) | 549.1 | 10-Q XBRL `[P]` |
| 11 | Bank of New York Mellon (BNY) | BHC | 541101 (425.1) | **525.0** | 10/15 | I | 503.5 | 10-Q XBRL `[P]` |
| 12 | Charles Schwab Corp. | **SLHC** | not in LBR (savings-association banks) | **517.3** | 10/15 `[S]` | III (10-Q confirms) | 491.7 | 10-Q XBRL `[P]` |
| 13 | TD Group US Holdings LLC | **IHC** | 497404 TD Bank NA (342.8) | **507** `[S]` | — | III | — | Wikipedia/NIC `[S]`; bank-level `[P]` |
| 14 | State Street Corp. | BHC | 35301 (412.6) | **418.4** | **403.3** | I | 386.9 | 10-Q XBRL; Q3 EX-99.2 `[P]` |
| 15 | American Express Co. | BHC | 1394676 (213.9) | **308.2** | 10/23 | **II** `[P-Q]` (DFAST table: III) | 303.7 | 10-Q: "became a Category II firm during the second quarter of 2026" because cross-jurisdictional activity >$75B (four-quarter average to 3/31/2026) `[P]` |
| 16 | Fifth Third Bancorp | BHC | 723112 (299.2) | **300.2** | 10/19 | IV → **III transition begins Q3-26** `[P-Q]` | 256.1 | 10-Q: "In the third quarter of 2026, the Bancorp will begin the transition from Category IV to Category III" `[P]`. Assets jumped from $214B to $297B between Q4-25 and Q1-26; the deal identity (Comerica) is `[M]` |
| 17 | BMO Financial Corp. | **IHC** | 75633 BMO Bank NA (255.0) | **298** `[S]` | — | III | — | `[S]`; bank-level `[P]` |
| 18 | Huntington Bancshares | BHC | 12311 (283.1) | **284.0** | 10/22 | IV | **244.2 qtr-avg** | 10-Q XBRL; Q2 EX-99.2 averages `[P]`. Q3-25 ($209.7B average) drops out of the window next quarter, so Q3-26 data will **likely cross $250B** `[X]` projection. The 10-Q makes no category statement. Deal identity (Cadence) `[M]` |
| — | *the $250B line falls here* | | | | | | | |
| 19 | HSBC North America Holdings | **IHC** | 413208 HSBC Bank USA (173.1) | **243** `[S]` | — | IV | — | `[S]`. HSBC USA Inc. (an SEC filer and subsidiary of the IHC): $180.7B `[P]` |
| 20 | First Citizens BancShares | BHC | 491224 (236.3) | **236.8** | — | IV | 234.0 | `[P]` |
| 21 | Barclays US LLC | **IHC** | 2980209 Barclays Bank DE (43.5) | **234** `[S]` | — | **III** | — | `[S]`. **Cat III below $250B**, i.e. via a $75B risk indicator |
| 22 | Citizens Financial Group | BHC | 3303298 (232.5) | **233.8** | — | IV | 227.7 | `[P]` |
| 23 | M&T Bank Corp. | BHC | 501105 (218.8) | **219.3** | — | IV | 214.7 | `[P]` |
| 24 | UBS Americas Holding LLC | **IHC** | 3212149 UBS Bank USA (124.4) | **214** `[S]` | — | **III** | — | `[S]`. Cat III below $250B |
| 25 | RBC US Group Holdings LLC | **IHC** | 63069 City National (99.1) | **204** `[S]` | — | **III** | — | `[S]`. Cat III below $250B |
| 26 | Ally Financial | BHC | 3284070 (188.2) | **199.8** | — | IV | 196.2 | `[P]` |
| 27 | KeyCorp | BHC | 280110 (188.6) | **191.3** | — | IV | 187.9 | `[P]` |
| 28 | Northern Trust Corp. | BHC | 210434 (178.6) | **179.3** | 10/21 | **II** | 175.3 | `[P]`. **Category II at $179B** (cross-jurisdictional activity) |
| 29 | Santander Holdings USA | **IHC** | 722777 Santander Bank NA (104.0) | **164.5** | — | IV | 166.3 | 10-Q XBRL `[P]` |
| 30 | Regions Financial | BHC | 233031 (159.8) | **161.3** | — | IV | 160.2 | `[P]` |
| 31 | DB USA Corp. | **IHC** | 214807 DB Trust Co Americas (40.5) | **130** `[S]` | — | **III** | — | `[S]`. Cat III below $250B |
| 32 | Pinnacle Financial Partners (new CIK 2082866) | BHC | 2925666 (128.8) | **129.1** | — | not in the 2026 list | 103.2 (n=3) | `[P]`. Crossed $100B after its merger (partner Synovus `[M]`), so it is **Category IV-bound** `[X]` |
| 33 | Synchrony Financial | **SLHC** | — | **121.9** | — | IV | 119.9 | `[P]` |

**At or near $100B and not covered by tailoring:**

| Firm | Assets ($B, 6/30/26) | Why it is excluded |
|---|---|---|
| USAA | 244 `[S]` | Insurance-engaged SLHC; absent from the Fed stress-test list. Covered-SLHC exclusion inferred, **definition not fetched** |
| Interactive Brokers | 247.3 `[P]` | Not a BHC or SLHC (broker-dealer) `[M]` |
| Ameriprise | 197.9 `[P]` | Insurance-engaged SLHC; absent from the stress-test list. Inferred |
| Mizuho Americas | 90 `[S]` | Below $100B |
| BNP Paribas USA | 84 `[S]` | Below $100B |
| MUFG Americas | not found | Absent from the stress-test list |
| Western Alliance · Raymond James · Zions | 98.7 / 94.2 / 89.0 `[P]` | Below $100B |

**Category sets (2026 stress-test Table 3 `[P]` plus issuer 10-Q updates):**

| Category | Firms |
|---|---|
| **I (8 US GSIBs)** | JPM, BAC, C, WFC, GS, MS, BK, STT |
| **II** | NTRS; **AXP since Q2-26** |
| **III, US top-tier** | USB, COF, PNC, TFC, SCHW; **FITB transitioning from Q3-26** |
| **III, IHCs** | TD, BMO, Barclays US, UBS Americas, RBC US, DB USA |
| **IV** | Ally, Citizens, Fifth Third*, First Citizens, HSBC NA, Huntington, KeyCorp, M&T, Regions, Santander, Synchrony (*transitioning) |

---

## 4. Q3 2026 earnings dates for the firms above $250B

Status as of 2026-10-14 ~20:25 ET. "Reported" means an Item 2.02 8-K is on EDGAR.

| Firm | Q3 date | Status | Source |
|---|---|---|---|
| JPM | Tue 10/13 | **REPORTED** | 8-K 0001628280-26-065582 `[P]` |
| WFC | Tue 10/13 | **REPORTED** | 8-K 0000072971-26-000318 `[P]` |
| C | Tue 10/13 | **REPORTED** | 8-K 0001104659-26-115323 `[P]` |
| GS | Tue 10/13 | **REPORTED** | 8-K 0000886982-26-000529 `[P]` |
| BAC | Wed 10/14 | **REPORTED** | 8-K 0000070858-26-000481 `[P]` |
| MS | Wed 10/14 | **REPORTED** | 8-K 0000895421-26-000288 `[P]` |
| STT | Wed 10/14 | **REPORTED** | 8-K 0000093751-26-000592 (Item 2.02 "On October 14, 2026…") `[P]` |
| PNC | **Thu 10/15**, ~06:30 ET; call 10:00 ET | upcoming (this week) | Issuer PR, 9/3/2026 `[P]` |
| USB | **Thu 10/15**, pre-open; call 08:00 CT | upcoming | Issuer PR PDF, 10/1/2026 `[P]` |
| BK (BNY) | **Thu 10/15**, ~06:30 ET; call 11:00 ET | upcoming | Issuer PR, 10/31/2025 (2026 schedule) `[P]` |
| SCHW | **Thu 10/15**, pre-open (8:30 ET call) | upcoming, **date `[S]`** | MarketBeat (marked "estimated"). Issuer IR returned 403 |
| TFC | **Fri 10/16**, pre-open; call 08:00 ET | upcoming | Issuer 2026 schedule (5/1/2025) `[P]`; 9/18/2026 call PR via mirrors |
| FITB | **Mon 10/19**, ~06:30 ET; call 09:00 ET | upcoming (next week) | Issuer IR, 8/12/2025 `[P]`. The older 11/2024 schedule said Thu 10/22 and is superseded |
| COF | **Tue 10/20**, ~16:05 ET; call 17:00 ET | upcoming | Issuer IR page as shown in the search index, plus wire copy (tmcnet, 9/24/2026). Direct fetch 403 |
| NTRS (Cat II, <$250B) | **Wed 10/21**; call 08:00 CT | upcoming | Issuer PR (search index; fetch timed out) |
| HBAN | **Thu 10/22**, pre-open; call 09:00 ET | upcoming | Issuer PR, 9/30/2026, via mirrors (placera, finviz) |
| AXP | **Fri 10/23**; release ~07:00 ET, call 08:30 ET | upcoming | Issuer BusinessWire PR, 9/22/2026 (search index) |
| IHCs (TD, BMO, Barclays US, …) | — | No standalone earnings. The IHC's own data is the FR Y-9C, filed ~40–45 days after quarter-end (and NIC is blocked to automated access) | — |

As of tonight, 7 of the 16 US firms above $250B have printed. Four more print tomorrow (PNC, USB, BK, SCHW), then TFC on 10/16. The rest come 10/19 to 10/23.

---

## 5. Fleet overlap (read-only grep)

Files grepped: `AGENTS/*/STATUS.md`, `AGENTS/*/CLAUDE.md`, BROCK's BRK-31 frozen frame and REGINALD's `NDFI_COHORT.tsv`.

| Agent | What it holds on the large banks | Nature |
|---|---|---|
| **BROCK** | BRK-31 frozen frame: JPM · WFC · C (plus 8 regionals) for a private-credit/NDFI reserve **build** or a named private-credit counterparty in Q3/Q4 prints. STATUS 10/14: "JPM/WFC/C release reads show no qualifying fire; attribution INSUFFICIENT" | One-lens prediction coverage. The new desk consumes it and does not grade it |
| **REGINALD** | `NDFI_COHORT.tsv` "large" sample at **bank level** (6/30/2026, RC-C Memo 10): JPM, BAC, C, WFC, PNC, USB, TFC, KEY, RF, FITB, FHN, CFR. STATUS uses BAC/MS/JPM as price comparators. **HBAN, MTB and CFG are in the 14-bank MI3 cohort** | Data asset plus comparator. **HBAN sits above the proposed line** |
| **NEXUS** | STATUS logs the big-bank Q3 read: BAC NCOs $1.349B; MS revenue $20.338B; JPM/WFC/C reserve builds $539M / $46M / $369M with no private-credit attribution | Synthesis consumer |
| **LIQUID** · **WALTER** | BAC lower NCOs and WFC lower NPAs / LCR improvement as funding context. WALTER routed BAC/MS issuer Q3 counterevidence | Routing / consumption |
| **CARL** | COF / SYF / ALLY / AXP monthly card-credit metrics (COF card 30+ 3.57% in August). Routes bank-level consumer stress to REGINALD | Consumer-credit lens on COF and AXP |
| **SENTRY** | FITB on the Tier-1 bank-puts list; PNC in the Tier-2 peer cluster | Signal watchlist |
| **TERRY** | An HBAN 16P management row (expiry 10/16) | Position (trade construction) |
| **SHADE** | Truist and Fifth Third as counterparties that paused (n=2); bank items routed to REGINALD | Context |
| **OTTO** | Bank-loss table: JPM $170M · Fifth Third $178M · Barclays $150M · Regions $68M | Credit-event context |
| **HANS** | European banks (Barclays, Deutsche) "as it transmits to U.S." | Parent-level overlap with the Barclays US and DB USA IHCs |
| **OZK** · **VULCAN** | Citi as lender on an OZK credit; GS/JPM in an AI-capex credit basket | Incidental |
| False positives | OSPREY "GS" = Ukrainian General Staff; CRUISE "Truist" = equity analyst; HOMER "Wells Fargo" = NAHB/WF HMI data series; ORACLE "Goldman" = a worked example | Ignore |

**Summary:** no agent owns large-bank fundamentals. Coverage is incidental:
- BROCK: JPM/WFC/C through the private-credit lens only.
- REGINALD: a bank-level NDFI snapshot plus price comparators.
- CARL: COF and AXP through the card-credit lens.
- NEXUS, LIQUID and WALTER: consumers of the release reads.

**No one covers BK, STT or SCHW. No one covers GS or MS as subjects, or the custody/IHC set.**

---

## 6. UNVERIFIED items and limits

1. **No FR Y-9C figure is used.** FFIEC NIC returned HTTP 403 with a CAPTCHA page on every endpoint tried. For SEC filers, holding-company totals are 10-Q/10-K GAAP period-end figures `[P]`. These match the NIC figures quoted on Wikipedia to the $1B for every US BHC checked. IHC totals (TD, BMO, HSBC NA, Barclays US, UBS Americas, RBC US, DB USA) are **SECONDARY**, taken from Wikipedia's citation of NIC at 6/30/2026. Holding-company RSSD IDs are **not given**; the RSSDs shown are lead-bank IDs from the Fed LBR.
2. **Tailoring uses four-quarter averages of quarterly-average balances (Y-9C / Y-15 / Y-9LP), not period-end.** Only USB (686.6) and HBAN (244.2) were computed on a quarterly-average basis, from the issuers' own releases. Every other "4Q proxy" averages period-end balances `[X]`.
3. **The risk indicators** (cross-jurisdictional activity, weighted short-term wholesale funding, nonbank assets, off-balance-sheet exposure) were **not checked**: no FR Y-15 access. The category column rests on the Fed's 2026 Table 3, whose data vintage is probably through ~Q4-25 (not stated), plus the issuers' 10-Q updates. Categories can move every quarter: AXP moved to II in Q2-26, FITB moves to III in Q3-26, HBAN is likely next.
4. **The indexing proposal is SECONDARY and unproposed.** The level figures (~$150B; ~$960B–$1T; $375B per a TD Cowen note) come from press reports. The $375B figure and the bills H.R. 6553 / S. 5452 come from search summaries only. The Fed press RSS covers only 9/10–10/13; the Reuters piece of 9/25 says no proposal had been issued before then.
5. **Capital re-proposal (3/19/2026):** the status comes from Truist's 10-Q of 6/30/2026. No final rule appears in the Fed RSS window. The Federal Register citation was not fetched.
6. **Citi at 6/30/2026** is the rounded comparative in the Q3 release ($2,895B). The XBRL company-facts for Citi's 2026 10-Qs lack `us-gaap:Assets`, which is unexplained. The **GS** 9/30 figure is the rounded $B balance sheet in its release.
7. **Earnings dates:**
   - SCHW is `[S]` (a calendar estimate; issuer IR returned 403).
   - COF, NTRS, HBAN and AXP come from issuer press releases seen through the search index or mirrors, not fetched directly.
   - PNC, USB, BNY, TFC and FITB were fetched at the issuer.
8. **Deal identities are `[M]`:** FITB–Comerica, HBAN–Cadence, PNFP–Synovus and the COF–Discover closing date. The asset step-changes themselves are primary.
9. **Exclusions are inferred, not checked:**
   - USAA and Ameriprise (insurance-engaged SLHCs) and IBKR (not a holding company subject to tailoring) are excluded by inference from their absence in the Fed stress-test list. The covered-SLHC definition in 12 CFR 238.2 was not fetched.
   - MUFG Americas' status was not found.
10. **Quartr MCP** needed re-authentication and was not used. The **OFR** Bank Systemic Risk Monitor exposed no download link.
11. **The grep is limited** to STATUS/CLAUDE files plus the two named files. Ledgers, research folders and inboxes elsewhere were not scanned.
12. **Process disclosure:** SEC EDGAR requests used the User-Agent string already in REGINALD's scripts (`REGINALD-Research <operator email>`, as SEC requires). No other external service received it.

---

## 7. What this means for the perimeter (facts for DAEDALUS's proposal; not a ruling)

| Option | Name set at 6/30/2026 | Note |
|---|---|---|
| A. ">$250B total assets" (REGINALD's draft line) | 16 US: JPM BAC C WFC GS MS USB COF PNC TFC BK SCHW STT AXP FITB HBAN (+ TD and BMO IHCs `[S]`) | Not a regulatory category. It takes **HBAN out of REGINALD's MI3 cohort** and moves if the Fed re-indexes |
| B. "US top-tier Category I–III" | JPM BAC C WFC GS MS BK STT · NTRS AXP · USB COF PNC TFC SCHW FITB(transitioning) = 16; HBAN joins on likely Q3-26 crossing | Tracks the regulatory regime (SCB, annual stress test, LCR/NSFR). It moves quarterly and needs Y-15 data that is not reachable today |
| C. A named list frozen at charter, re-cut quarterly | Any of the above | Avoids silent drift when the categories or the thresholds move |

REGINALD's 10 names omit **two Category I GSIBs (BK, STT)**, Schwab, AXP (now Category II) and FITB/HBAN. Whichever line is chosen, **HBAN, and FITB if any boundary is drawn near $250B, need an explicit owner call** between REGINALD and the new desk before Q3 prints (FITB 10/19, HBAN 10/22).
