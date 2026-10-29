# HOMER — California lane baseline (research helper draft)

Built 2026-10-28 ~23:30 ET. Draft for HOMER review. **Not a ledger write.** Nothing in the repo was edited.
Raw downloads are in `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-HOMER/3b7684a0-0372-42eb-b6ae-02767433240c/scratchpad/ca/`.

Labels: **PRIMARY** = the issuer's own page or file. **SECONDARY** = press, advocacy or search-engine summary. **DERIVED** = HOMER-side arithmetic or ordering on a primary table; the issuer did not publish it.
Every figure's publication year was checked against the issuer page. The search engine kept returning 2025 lookalikes (C.A.R. Sept-2025, Case-Shiller Aug-2025, ICE Feb-2025 fire data). Those were rejected unless a row says it is history.

## Boundary reminder
- **AEOLUS owns** wildfire peril, insurer losses, rate filings, the FAIR Plan, and the Sustainable Insurance Strategy (SIS). Those appear below only as **pointers**.
- **HOMER owns** the housing-credit consequence: delinquency, forbearance, foreclosure, prices and sales.
- **No Florida-style "statewide → another desk" rule applies to CA.** No desk is named for CA statewide housing figures, so HOMER can publish them. Confirm this with PROME/ROSTER if a CORAL-like owner exists.

---

## 1. C.A.R. monthly sales & price report — September 2026

**Source:** https://www.car.org/aboutus/mediacenter/newsreleases/2026releases/sept2026sales. **PRIMARY.** Released **2026-10-19**, not mid-month. curl-reachable: **YES** (HTTP 200, plain HTML). Cadence: monthly, about the 3rd week of the following month. Also referenced: infographic at car.org/Global/Infographics/2026-09-Sales-and-Price and the data hub https://www.car.org/marketdata/data/housingdata (curl 200).

| Metric (existing SFR, Sept 2026) | Value | MoM | YoY | Note |
|---|---|---|---|---|
| Sales, SAAR | **260,410** | −3.4% (Aug 269,620) | −6.5% (Sep-25 278,540) | Below 300K for the **48th consecutive month** (C.A.R.) |
| YTD sales | — | — | +0.8% | C.A.R. |
| Statewide median price | **$899,720** | −0.2% (Aug $901,420) | +1.7% (Sep-25 $884,390 r) | Sep-25 value is revised ("r") |
| Condo/townhome median | $640,000 | 0.0% | −1.5% | Sales −7.5% YoY |
| Unsold Inventory Index | **3.7 months** | flat vs Aug 3.7 | Sep-25 3.6 | Statewide only. County UII is not in the release |
| Active listings | — | +2.7% | +0.5% | First annual increase in 8 months |
| Median days to sell | 29 | — | Sep-25 32 | |
| Sales-to-list ratio | 98.8% | — | Sep-25 98.2% | |
| Median $/sq ft | $434 | — | Sep-25 $427 | |
| 30Y FRM (C.A.R. calc from PMMS) | 6.86% avg Sept | Aug 6.67% | Sep-25 6.35% | Rate surface is HOMER's RATES.tsv. This is only C.A.R.'s monthly average |

**Regional and county medians (existing SFR, Sept 2026, county sales NSA):**

| Area | Median Sep-26 | Aug-26 | Sep-25 | Price MoM | Price YoY | Sales MoM | Sales YoY |
|---|---|---|---|---|---|---|---|
| Los Angeles **Metro Area** (C.A.R. region) | $855,000 | $850,000 | $830,000 | +0.6% | +3.0% | +1.5% | −8.0% |
| Los Angeles **County** | $994,670 | $946,950 | $983,230 | +5.0% | +1.2% | +5.4% | −10.9% |
| San Francisco Bay Area | $1,325,000 | $1,272,000 | $1,300,000 | +4.2% | +1.9% | +4.9% | −3.1% |
| San Diego County | $1,050,000 | $1,090,000 | $990,000 | −3.7% | +6.1% | −6.0% | −12.2% |
| Inland Empire | $601,030 | $600,000 | $591,010 | +0.2% | +1.7% | −2.9% | −10.2% |
|  ↳ Riverside County | $620,000 | $632,990 | $624,000 | −2.1% | −0.6% | −6.4% | −12.7% |
|  ↳ San Bernardino County | $531,090 | $522,370 | $500,030 | +1.7% | +6.2% | +3.5% | −6.0% |
| Southern California | $895,000 | $900,000 | $869,250 | −0.6% | +3.0% | −0.2% | −9.1% |
| Central Valley | $500,000 | $500,000 | $499,900 r | 0.0% | 0.0% | −3.4% | −2.5% |
| Fresno County | $429,450 | $430,000 | $445,000 | −0.1% | −3.5% | −10.0% | −10.5% |
| Kern County (Bakersfield) | $420,000 | $400,500 | $405,000 | +4.9% | +3.7% | −6.3% | −3.6% |

Breadth (C.A.R. text): 33 of 53 counties had YoY median gains, 3 were flat, 17 declined. 19 counties had YoY sales gains and 33 had declines.

**Caveats**
- These are medians on existing detached SFR closings from a survey of more than 90 associations. They are **composition-sensitive** (C.A.R. says so itself) and are not a repeat-sales index. Use Case-Shiller (§2) for value change.
- County sales are NSA. The statewide SAAR is SA.
- C.A.R. revises the prior year ("r").
- **"Los Angeles Metro Area" and "Los Angeles County" are different rows.** Say which one you cite.
- C.A.R. is a trade association with a policy position: car.org carries a "YES ON PROP 37" banner (see §7). Its narrative is advocacy-adjacent, but the data tables are standard.

---

## 2. S&P Cotality Case-Shiller — August 2026 (released 2026-10-27)

**Source:** https://press.spglobal.com/2026-10-27-S-P-Cotality-Case-Shiller-Index-Reports-Annual-Gain-in-August-2026. **PRIMARY.** curl-reachable: **YES** (HTTP 200). Cadence: monthly, last Tuesday, about a 2-month lag. Revisable for the prior **24 months**.

| Metro | Aug-26 level | MoM NSA | MoM SA | Jul/Jun NSA | **YoY (NSA)** |
|---|---|---|---|---|---|
| Los Angeles | 447.44 | **−0.80%** | +0.18% | −0.49% | **+1.36%** |
| San Francisco | 366.01 | **−0.68%** | +0.46% | −0.67% | **+3.37%** |
| San Diego | 449.12 | **−0.12%** | +0.73% | −0.14% | **+2.29%** |
| Composite-20 | 348.97 | −0.40% | +0.27% | −0.01% | +2.65% |
| U.S. National | 336.74 | −0.15% | +0.28% | +0.10% | +2.09% |

**Caveats**
- NSA monthly declines are seasonal. All three CA metros rose on an SA basis. Do not report the NSA MoM as a price decline without the SA figure beside it.
- The release puts CPI at +3.4% YoY, so all three CA metros are **negative in real terms**. That is derived context; the release says it only for the national index.
- The commentary quote in the release says "S&P CoreLogic", a legacy brand name. The index is the same.
- Case-Shiller covers metro-wide MSAs. It does not isolate burn zones.

---

## 3. ATTOM — California foreclosure

### 3a. Monthly: August 2026 (latest; released 2026-09-17)
- Report: https://www.attomdata.com/news/market-trends/foreclosures/august-2026-foreclosure-market-report/. **PRIMARY.** curl: **YES**.
- State table PDF: https://www.attomdata.com/wp-content/uploads/2026/09/Foreclosure-by-State-Aug-2026.pdf. **PRIMARY.** curl: **YES**. The filename pattern is irregular: July is `Foreclosure-by-State-July-2026.pdf`, August is `-Aug-2026.pdf`, and both sit in the `/2026/09/` folder. Discover the file from the report page; don't guess it.

| CA, Aug 2026 | Value | Source |
|---|---|---|
| Total foreclosure filings | **4,450** | State PDF |
| Rate | **1 in every 3,291 housing units**. Rank **15** of 50+DC (1 = worst) | State PDF |
| MoM / YoY | **−2.69% / +8.33%** | State PDF |
| Foreclosure starts | **2,565**, **#3** state after FL 3,189 and TX 3,126 | Report text |
| REOs (completed foreclosures) | **589**, **#2** state after TX 1,835 | Report text |
| U.S. reference | 40,277 filings, 1 in 3,569 HU, +0.93% MoM, +12.83% YoY. Starts 25,894 (+7% YoY). REO 5,794 (+42% YoY) | State PDF / text |

- **The September 2026 / Q3-2026 report is NOT out as of 10/28.** The ATTOM news feed through 10/26 lists no foreclosure report after August. Guessed URLs for a September or Q3 report returned 404, but they were guesses, not proof of absence. In 2025 the Q3 report ran in mid-October, so **this one is late**: re-check at boot.
- No CA metro figures appear in the August monthly text. Riverside, Stockton and Fresno metro rates are **not published in ATTOM's free monthly surfaces** that I found.

### 3b. Mid-year 2026 (H1; released 2026-07-16)
- https://www.attomdata.com/news/market-trends/foreclosures/2026-mid-year-foreclosure-market-report/. **PRIMARY.** curl: **YES**. The state table is in the HTML.

| CA, H1 2026 (Jan–Jun) | Value |
|---|---|
| Foreclosure filings | **21,543** |
| Rate | **0.15% of housing units (1 in 680)**. Rate rank **18** |
| Change vs H1-2025 / vs H1-2024 | **+12.79% / +13.31%** |
| Foreclosure starts | **16,040**, #3 state |
| REOs | **2,644**, #2 state |
| U.S. reference | 227,548 filings, 0.16% (1 in 632), +21.26% YoY |

- **Metro, Q2-2026:** **Bakersfield, CA = 1 in every 616 housing units, #4 worst** of 110 metros with population ≥500K, behind Lakeland, Columbia SC and Cape Coral. **PRIMARY** (mid-year page).
- **Riverside/San Bernardino, Stockton, Fresno:** no published H1 or Q2 rate found in free ATTOM text. ATTOM's metro tables are usually behind the paid data product, so this is a coverage gap.
- **Basis caveat (same discipline as the FL rows):** monthly, quarterly, H1 and annual rates are different bases and are not comparable. CA has **no band** yet; any CA band would be a Will-gated design.
- CA is a **non-judicial** state. ICE's table marks it with no judicial asterisk. Starts convert to REO faster than in judicial states, which helps explain CA's high REO rank alongside a mid-pack filing rate. That last point is an interpretation, not ATTOM's statement.

---

## 4. Wildfire-affected mortgage performance (LA Jan-2025 fires) and 2026 fires

### 4a. Performance data
| Item | Value | As-of | Source | Label |
|---|---|---|---|---|
| Serious DQ (90+) share in LA fire-affected ZIPs | "**more than double its pre-fire level**" more than a year after the fires. Foreclosure rates "have remained stable" | published **2026-08-13** | Cotality, "The delinquent costs of wildfire", https://www.cotality.com/insights/articles/foreclosures-after-wildfire (curl **YES**) | PRIMARY (Cotality), but **no numeric level is published in the text**; the chart is an image. Path: 30-day DQ jumped ~6% in the first month after the fires; 60-day reached 4% of mortgages at month 2 |
| ICE fire-zone DQ/forbearance | **No 2026 ICE update found.** The Oct-2026 Mortgage Monitor (data 2026-08-31) contains no fire, CA or forbearance content (text search of the PDF: 0 hits) | — | https://mortgagetech.ice.com/publicdocs/mortgage/ICE_Mortgage_Monitor_Oct._2026.pdf (curl YES) | gap |
| ICE history (2025 only) | ~680 missed the Jan-2025 payment. Feb-2025 DQ: Palisades region **23.9%**, Eaton/Altadena **16.7%** (as summarized in the press) | Feb 2025 | ICE Feb/Mar-2025 Mortgage Monitor; Bloomberg 2025-02-21 | **History only, 2025**. The DQ percentages are a SECONDARY summary; verify in the ICE Mar-2025 PDF before citing |
| CalAssist Mortgage Fund disbursed | **$54M to 1,575 households**; 76% of funds went to Eaton-fire homes. Up to $100K / 12 months, non-repayable. Fund size $125M | as of **2026-09-14** | Governor release 2026-09-17, https://www.gov.ca.gov/2026/09/17/governor-newsom-delivers-on-pledge-to-provide-new-financing-options-for-eaton-and-palisades-survivors/ | PRIMARY. curl **NO** (403); WebFetch OK |
| Insurance claims, LA fires | ~42,000 claims, >40,000 at least partly paid, **$23.7B**. >13,000 involve smoke damage | as of March 2026 (CDI via Governor 2026-09-15) | gov.ca.gov | **AEOLUS-owned**, pointer only |

### 4b. Forbearance / moratorium clock (events that convert to DQ/FC)
| Instrument | Terms | Status / date | Source |
|---|---|---|---|
| **AB 238** (2025) Mortgage Forbearance Act | Up to 12 months in 90-day increments. No lump-sum demand, no late fees, no foreclosure during forbearance. Request deadline = end of emergency + 6 months **or 2027-01-07**, whichever is first | In force | LA County DCBA, https://dcba.lacounty.gov/forbearanceact/ (curl YES). That page has **not** been updated for AB 1847 |
| Voluntary lender extension | **>160 institutions** committed up to **90 additional days**, subject to investor (GSE) approval | Announced **2026-02-05** | DCBA page; Spectrum News 2026-02-05 (SECONDARY) |
| **AB 1847** (Harabedian) | Extends AB 238 one more year for LA-fire survivors. Max forbearance **12 → 24 months**. Servicer must offer deferral of missed payments **to loan end** unless investor/servicing guidelines prohibit it. Request deadline **2029-01-07** (bill analysis; SECONDARY) | **Signed 2026-09-15** (Governor release, PRIMARY). The urgency clause was removed by floor amendment (Assembly analysis, SECONDARY) ⇒ **probably effective 2027-01-01**. That date is an inference; confirm on leginfo | gov.ca.gov 2026-09-15 (curl NO); leginfo (curl NO, WebFetch 403) |
| **AB 1842** (Harabedian) | Makes disaster mortgage-forbearance protections **permanent** for future declared disasters | **Signed 2026-09-15** | gov.ca.gov 2026-09-15 |
| FHA foreclosure moratorium, LA County | Automatic 90 days from the 2025-01-08 PDMDA, extended by ML 2025-07 **through 2025-07-07** | **No later extension found.** Treat it as expired unless HUD shows otherwise | HUD FHA INFO 2025-12 / ML 2025-07 (2025) |
| GSE disaster forbearance | Standard Fannie/Freddie disaster forbearance runs up to 12 months, then a workout. **No 2026 LA-specific GSE expiry date found** | — | gap |

**Conversion-window read (DERIVED, label it):** the earliest AB 238 forbearances started Jan-2025, ran 12 months to about Jan-2026, and the voluntary 90-day extension added from Feb-2026 takes them to about **Q2-2026**. AB 1847 likely takes effect **2027-01-01**. So borrowers who were not on a voluntary extension may sit in a **gap from roughly Q2-2026 to 2027**, where repayment, DQ or foreclosure can occur. Cotality's "serious DQ more than double pre-fire, foreclosures stable" (8/13/2026) is consistent with this, but nothing proves it. A borrower-count series to test it is **not public**.

### 4c. 2026 California fires with a housing-credit tail
| Fire | Emergency declared | Insurance moratorium (pointer; AEOLUS) | Housing-credit follow-up found |
|---|---|---|---|
| Gifford Fire (Kern, Santa Barbara, SLO, Ventura) | 2025-12-23 | CDI one-year moratorium from 2025-12-23: ~147K–150K policies, 29 ZIPs (CDI release dated **2026-01-09**, https://www.insurance.ca.gov/0400-news/0100-press-releases/2025/release002-2026.cfm, curl YES) | none found |
| **Gann Fire** (Calaveras, San Joaquin, Amador, Tuolumne, Stanislaus) | **2026-08-06** | CDI moratorium **2026-08-14**: >64,000 policyholders (https://www.insurance.ca.gov/0400-news/0102-alerts/2026/Commissioner-Lara-protects-more-than-64.cfm, curl YES) | none found. Watch the Stockton (San Joaquin) and Modesto (Stanislaus) metros |
- CDI states that its moratoria protected more than 1.2M homeowners in 2025.

---

## 5. Uninsured / underinsured ↔ mortgage linkage
| Item | Finding | Label |
|---|---|---|
| Force-placed (lender-placed) insurance volumes in CA, 2026 | **No 2026 dataset found.** No CFPB, CA DOI or servicer disclosure quantifying CA force-placement was located. Broker blogs (oldharbor.com 2026-10-07, others) only describe the mechanics: escrow, RESPA Reg X §1024.37 45-day notice, cost 2–10× market | gap. SECONDARY only |
| Candidate primary sources to watch | Servicer 10-Q/10-K (MR. COOPER/RITM/PFSI) commentary on lender-placed premiums. CFPB complaint database (product "Mortgage", issue "escrow/insurance", state CA). CDI annual "Residential Property Insurance" data call | to-build |
| **CA FAIR Plan policies in force** | **698,307 total PIF** (dwelling + commercial) as of **Sept 2026 (FYE 2026)**, +8% vs Sept 2025, +157% vs Sept 2022. Total exposure **$773B** (+11% YoY) | **AEOLUS-owned, pointer only.** PRIMARY: https://www.cfpnet.com/key-statistics-data/ (curl YES). ZIP/county PIF PDFs dated 2026-10-20 at cfpnet.com/wp-content/uploads/2026/10/ |
- **Housing consequence HOMER needs from AEOLUS:** whether FAIR-only (fire-only) coverage meets GSE hazard-insurance eligibility, and a ZIP-level FAIR share joined to a ZIP-level DQ series. HOMER has no ZIP-level DQ source; that is the core gap.

---

## 6. ICE state non-current rate, California
- Source: ICE Mortgage Monitor, **October 2026** edition (data as of **2026-08-31**), Appendix "Non-current loans by state" (an image table on p.20). https://mortgagetech.ice.com/publicdocs/mortgage/ICE_Mortgage_Monitor_Oct._2026.pdf. **PRIMARY.** curl: **YES** (PDF, 2.3 MB). Cadence: monthly, about the first Monday. The table is an image, so read it visually; pdfminer cannot extract it.

| CA, Aug-31-2026 | Value |
|---|---|
| DQ % (30+, excluding FC) | **2.1%** |
| FC inventory % | **0.3%** |
| **Non-current %** | **2.4%** |
| YoY change in NC % (relative) | **+6.4%** |
| National | DQ 3.5%, FC 0.5%, NC 4.1%, YoY +6.8% |

- **DERIVED:** CA ranks about **48th of 51** (50 states + DC, 1 = highest NC) by the table's ordering. Only WA, MT and ID are lower. CA has one of the lowest non-current rates in the U.S.
- The ICE **First Look** (Sept-2026 data, released 2026-10-27, https://mortgagetech.ice.com/resources/data-reports/first-look-at-september-2026-mortgage-data, curl YES) shows only top/bottom-5 states, and CA is not among them. National DQ was 3.66%. The Sept-2026 state appendix arrives with the **November Mortgage Monitor** (~early Nov).
- **FHA share for CA: NOT FOUND** in a public source. ICE does not split state by product in the free report. Options: MBA NDS state-by-product (paid), or a HUD FHA SF portfolio snapshot (data by state; unverified). Gap.

---

## 7. CA housing / mortgage policy 2026 (dates and status only)
| Item | Date | Status | Source |
|---|---|---|---|
| AB 1847: LA-fire forbearance 24 months, request deadline 2029-01-07 | signed 2026-09-15 | enacted; effective date probably 2027-01-01 (inferred) | gov.ca.gov (PRIMARY); bill analysis (SECONDARY) |
| AB 1842: permanent disaster forbearance framework | signed 2026-09-15 | enacted | gov.ca.gov |
| AB 1795: insurers pay smoke testing/remediation; ALE not cut until home is remediated | signed 2026-09-15 | enacted (**AEOLUS**) | gov.ca.gov |
| AB 1642: lead/asbestos smoke cleaning standards | signed 2026-09-15 | enacted | gov.ca.gov |
| Disaster Rebuilding Assistance Program: $100M (rate buydowns, loan-loss guarantees for construction lenders) | announced 2026-09-17 | live | gov.ca.gov |
| SB 547: extends the non-renewal moratorium law to some commercial/other property | effective 2026-01-01 | enacted (**AEOLUS**) | search summary, SECONDARY |
| CDI moratoria: Gifford (from 2025-12-23), Gann (2026-08-14) | see §4c | active one-year windows | CDI (PRIMARY) |
| Sustainable Insurance Strategy | Verisk wildfire cat model reviewed 2025; first SIS filings approved Dec-2025 (Mercury, CSAA). **No 2026 milestone confirmed** | **AEOLUS-owned** | CDI 2025 (pointer) |
| **Prop 37**: Middle-Class Home Ownership Loan Program (state borrowing for middle-income buyers of new homes) | ballot **2026-11-03** | pending vote. C.A.R. supports it (banner on car.org) | car.org; SoS voter guide (SECONDARY) |

---

## Reachability summary
| Host | curl | Notes |
|---|---|---|
| car.org | YES | |
| press.spglobal.com | YES | |
| attomdata.com (pages + PDFs) | YES | PDF filenames irregular |
| mortgagetech.ice.com (pages + publicdocs PDFs) | YES | State tables are images |
| cotality.com | YES | Charts are images, no numbers in text |
| cfpnet.com | YES | AEOLUS |
| insurance.ca.gov | YES | |
| dcba.lacounty.gov | YES | stale vs AB 1847 |
| gov.ca.gov | **NO** (403) | WebFetch works |
| leginfo.legislature.ca.gov | **NO** (403 curl and WebFetch) | use bill-analysis PDFs or the Governor release |

## Open gaps (ranked by decision value)
1. **Fire-zone DQ/forbearance numbers for 2026.** Only Cotality's qualitative "more than double pre-fire" exists. Ask whether ICE or Cotality publish a ZIP series. The forbearance-gap window (§4b, derived) makes this the CA lane's key unknown.
2. ATTOM CA **metro** rates (Riverside-SB, Stockton, Fresno). Only Bakersfield Q2 is public.
3. CA **FHA share** / FHA DQ by state.
4. Force-placed insurance volumes in CA. No public series.
5. AB 1847 effective date and request deadline should be confirmed from statute text (leginfo is blocked).
6. ATTOM Sept/Q3-2026 report is overdue versus the 2025 timing.

## Recommended recurring sources
| Source | Cadence | Next expected | Use |
|---|---|---|---|
| C.A.R. sales & price release | Monthly, ~3rd week | Oct-2026 data ~mid/late Nov | Statewide/regional medians, SAAR, UII |
| S&P Cotality Case-Shiller (LA/SF/SD) | Monthly, last Tue | Sep-2026 data on 2026-11-24 (expected) | Repeat-sales value; NSA+SA |
| ATTOM monthly + state PDF | Monthly, ~mid-month | Sept/Q3-2026: overdue, check now | CA filings, starts, REO, rate rank |
| ATTOM year-end (Jan) + mid-year (Jul) | Semiannual | YE-2026 ~mid-Jan 2027 | CA annual rate (basis for any future band) |
| ICE Mortgage Monitor appendix | Monthly, ~1st Mon | Nov edition (Sept data) early Nov | CA DQ/FC/NC % (image table) |
| ICE First Look | Monthly, ~4th week | Oct data ~late Nov | National context; CA only if top/bottom-5 |
| Cotality wildfire / mortgage insights | Ad hoc | — | Fire-zone DQ (qualitative) |
| Governor + CDI press pages | Event-driven | — | Forbearance laws, CalAssist counts, moratoria (CDI = AEOLUS) |
| CA FAIR Plan key statistics | Quarterly | Dec-2026 quarter ~Jan 2027 | **AEOLUS** pointer only |
| LA County DCBA forbearance page | Event-driven | — | Request deadlines (currently stale) |
