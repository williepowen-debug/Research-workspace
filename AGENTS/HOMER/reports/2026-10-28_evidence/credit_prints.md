# HOMER credit/housing prints — retrieval 2026-10-28 (~22:50 ET)

Retrieval helper output. Nothing written to the repo. Downloads: `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-HOMER/3b7684a0-0372-42eb-b6ae-02767433240c/scratchpad/dl_creditprints/`.
Legend: **PRIMARY** = issuer document, or the issuer's own wire release · **SECONDARY** = third party · **DERIVED** = arithmetic by this helper and not published by the issuer.
Every source below was checked as a 2026 document (dateline or PDF metadata). 2025 look-alike pages turned up in search and were rejected.

---

## 1. ICE First Look: SEPTEMBER 2026 data — PRIMARY (ICE release on Business Wire)

- **Published:** 2026-10-27, 09:00 EDT, Business Wire. Data as of 2026-09-30.
- **URL (wire, issuer):** https://www.businesswire.com/news/home/20261027946724/en/
- **Text read from:** the full mirror at https://www.financialcontent.com/article/bizwire-2026-10-27-ice-first-look-september-delinquencies-track-seasonal-norms-as-foreclosure-pipeline-shifts-toward-recent-vintages
- **Issuer page (same narrative, no table):** https://mortgagetech.ice.com/resources/data-reports/first-look-at-september-2026-mortgage-data. Its page header wrongly says "August 2026"; the body is September.

| Metric (Sep-2026) | Value | MoM | YoY | Basis/caveat |
|---|---|---|---|---|
| National DQ rate (30+ days, not in FC) | **3.66%** | +3.50% (relative; "+12 bps" in the text) | +7.02% (relative) | 34 bps below Sep-2019 |
| FC pre-sale inventory rate | **0.55%** | +1.54% | +35.53% | Aug was 0.54% |
| 30+ DPD or in FC (count) | **2,331,000** | +76,000 | +233,000 | |
| 30+ DPD, not in FC | **2,027,000** | +71,000 | +151,000 | |
| **90+ DPD, not in FC** | **579,000** | +5,000 | +102,000 | Serious DQ share 1.04% vs the 2017-19 September average of 1.06%. Serious DQ is +21% YoY and −5% from the February peak |
| **FC pre-sale inventory** | **303,000** | +5,000 | +82,000 (text: +37% YoY, "highest since early 2019") | |
| **FC starts** | **40,000** | +8.20% | **−2.92%** (text: "down 3%") | ⚠️ The YoY turned negative. Aug starts were +29% YoY |
| **FC sales** | **8,200** | +5.35% | **+14.50%** | |
| Prepayment SMM | 0.59% | −6.96% (−4 bps) | −19.91% | Lowest since Feb-2025; 6th straight monthly decline from March's 1.06% |
| 30-day DQ | count not given | — | +5% YoY | narrative only |
| Cures | **NOT PUBLISHED** in the First Look | | | Cure-rate band basis = ICE Mortgage Monitor (not yet out) |
| FHA | "Serious FHA delinquencies have declined 10% since February" | | | No VA figure |
| Vintage | Loans originated 2022 or later = 43% of starts and 49% of completed sales. More than three quarters of active FCs have been delinquent for under 18 months. FC aging is at a 15-year low | | | |

**States (non-current = DQ plus FC, as % of active loans):** Top: LA 8.70%, MS 8.61%, IN 6.49%, AL 6.45%, AR 6.07%. Bottom: OR 2.51%, CA 2.39%, MT 2.28%, WA 2.26%, ID 2.10%. Top by 90+: MS 2.50%, LA 2.38%, AL 1.91%, IN 1.67%, AR 1.66%.
⚠️ **The two 12-month-change lists look inverted as printed.** The "Top 5 by 12-mo change" list is the *smallest* changes (NY −0.70%, ID 3.26%, ND 3.97%, NJ 3.99%, SD 4.07%). The "Bottom 5" list is the *largest* (HI 38.62%, CO 22.21%, KY 20.77%, NC 17.47%, OH 16.96%). This is the issuer's labelling, quoted as published. FL does not appear in any list.

**Revision of August priors:** none shown.
DERIVED cross-check: Sep values minus the published MoM changes reproduce the priors. 90+ is 579K − 5K = 574K, and FC inventory is 303K − 5K = 298K, both matching the August priors. Starts 40,000 / 1.082 ≈ 37.0K and sales 8,200 / 1.0535 ≈ 7.78K are consistent with Aug 37K and 7.8K.
**Pipeline (90+ plus FC, HOMER's sum basis): 579K + 303K = 882K — DERIVED.** This crosses the 850K level of the 90+/FC Pipeline row. HOMER grades it; this helper does not. Aug on the same basis was 574K + 298K = 872K (DERIVED).

---

## 2. Freddie Mac Monthly Volume Summary: SEPTEMBER 2026 — PRIMARY

- **URL:** https://www.freddiemac.com/investors/financials/pdf/0926mvs.pdf
- **Published:** 2026-10-26. PDF CreationDate 2026-10-26 09:12 −04:00; server Last-Modified Mon 26 Oct 2026 15:15 GMT. Title "Freddie Mac MVS September 2026".

| Metric | Sep-2026 | Aug-2026 | Note |
|---|---|---|---|
| **Multifamily DQ rate** (Table 6; UPB basis, 60+ days past due or in FC; loans in compliant forbearance excluded) | **0.58%** | 0.64% (**unrevised**: the Sep highlights say "decreased from 0.64% in August to 0.58%"; the Aug MVS printed 0.64%) | First MoM decline since Apr-2026 |
| Single-family serious DQ (90+ or in FC, loan count) | **0.61%** | 0.60% | |

Table 6 multifamily series as printed (Sep-25 → Sep-26): 0.51, 0.48, 0.48, 0.44, 0.43, 0.42, 0.43, 0.43, 0.47, 0.51, 0.60, 0.64, **0.58**. The SF total series runs 0.57 → 0.61.
⚠️ Per HOMER's open GSE-band defect, the headline can move on modifications. Modified loans are not counted delinquent while under 2 payments past due on the modified terms (Table 6 notes). The MVS carries no provision figure to pair with this reading.

---

## 3. Fannie Mae Monthly Summary: SEPTEMBER 2026 — **NOT FOUND (apparently not yet released)**

- PR Newswire's Fannie Mae feed (https://www.prnewswire.com/news/fannie-mae/, fetched about 22:48 ET 10/28) lists August 2026 as the newest summary. No September 2026 release appears.
- The pattern URL `https://www.fanniemae.com/media/document/pdf/093026.pdf` returns **404**. The existing `083126.pdf` and `073126.pdf` return **403**, which is a bot block on files that exist. The 404 therefore suggests the September file is absent, not merely blocked.
- fanniemae.com newsroom and monthly-summary pages return 403 to both curl and WebFetch.
- WebSearch ("Fannie Mae September 2026 Monthly Summary", plus a PR Newswire variant) found nothing for 2026. For timing: the 2025 September summary came out 2025-10-27.
- Re-check from 10/29. Priors for context: MF SDQ Aug 0.57%, Jul revised 0.62%.

---

## 4. Apartment List National Rent Report: OCTOBER 2026 data — PRIMARY

- **URL:** https://www.apartmentlist.com/research/national-rent-data
- **Published:** 2026-10-28, by Chris Salviati and Rob Warnock. Page headline: "Headline Market Update: November 2026". This is the October-data report; the September-data report carried the "October 2026" headline.

| Metric (Oct-2026) | Value | Note |
|---|---|---|
| National median rent | **$1,384** | |
| MoM | **−0.3%** | Second straight monthly decline (Sep −0.1%) |
| YoY | **+0.1%** | "first time in over three years" positive. The Sep report showed −0.4% |
| Vacancy index | **7%** (text). The vacancy CSV national row gives 0.06961 for Oct, 0.07005 for Sep and 0.07073 for Aug | Peaked at 7.3% in Feb; still above the 2017-19 average of 6.4% |
| Time on market | **36 days** (Key Stats) | ⚠️ Internal inconsistency: a section header in the same report says "34 days" |
| Concession rate | **32%** of multifamily properties offering concessions worth at least one month free. The CSV national row gives 0.3195 for Oct, 0.313 for Sep and 0.3101 for Aug | Measured as a share of PROPERTIES, not listings. Series starts Jan-2025. Concessions are not netted out of the rent estimates |

**City-level rent-estimate data file (October posted: YES):**
- Data page: https://www.apartmentlist.com/research/category/data-rent-estimates (page shows an update date of 2026-10-28)
- **Historic Rent Estimates (Jan 2017 – present):** https://assets.ctfassets.net/jeox55pd4d8n/22URKuUw4Fjzg4cODP5YBf/e2ca9fa8c46588a7ee139301984b108a/Apartment_List_Rent_Estimates_2026_10.csv
  - **Latest month column = `2026_10`.** The file has 3,688 lines.
  - SHA-256 of the copy downloaded 22:50 ET: `bc25bf0f7d354e6272c761dae3952d1be350925b1d146eab5f19891d3c0d4d25`. `rent_breadth.py` records its own hash, so this one is for reference only.
  - Nothing was computed from it.
- Other files on the same page, all with `_2026_10` suffixes:
  - Summary: `.../1AKraZTVV2s9LpEgLFmFXT/.../Apartment_List_Rent_Estimates_Summary_2026_10.csv`
  - MoM growth: `.../Apartment_List_Rent_Growth_MoM_2026_10.csv`
  - YoY growth: `.../Apartment_List_Rent_Growth_YoY_2026_10.csv`
  - Vacancy: `.../Apartment_List_Vacancy_Index_2026_10.csv`
  - Time on market: `.../Apartment_List_Time_On_Market_2026_10.csv`
  - Concessions: `.../Apartment_List_Concession_Rates_2026_10.csv`

---

## 5. ATTOM foreclosure reports: Sep-2026 monthly / Q3-2026 — **NOT FOUND (not yet released)**

- The ATTOM foreclosures archive (https://www.attomdata.com/news/category/market-trends/foreclosures/, via WebFetch) lists **August 2026 (published 2026-09-17)** as the newest market report. There is no September or Q3 report.
- Guessed slugs returned **404**: `q3-2026-foreclosure-market-report`, `september-2026-foreclosure-market-report`, `q3-2026-us-foreclosure-market-report`. The August report URL returned 200 as a control, so the 404s are real.
- WebSearch, including one restricted to prnewswire.com, found ATTOM wire releases through August 2026 (PR Newswire, 09-17) and an ATTOM affordability release dated 10-22. No foreclosure release was found for September or Q3.
- **Q3 starts (national), filings, REO, FL metro rates and top states: all NOT FOUND.**
- Context already published (PRIMARY, ATTOM): Jul-2026 starts 26,648 (+10% YoY), REO 4,764 (+23% YoY); Aug-2026 starts 25,894 (+7% YoY), 40,277 properties with filings (+13% YoY).
- ⚠️ Do not treat the "Q3 2026 Vacancy and Zombie Foreclosure Report" (ATTOM, 2026-08-27; 259,666 properties in the foreclosure process, 8,482 zombies) as Q3 foreclosure activity. It is a snapshot of properties in process, not STARTS, and does not grade the national STARTS band.
- ⚠️ Partial-quarter sums of the monthly starts are DERIVED and must not stand in for ATTOM's printed Q3 starts. This file computes none.

---

## 6. Builder earnings, Q3-2026 (8-K Ex 99.1) — PRIMARY

### PulteGroup (PHM): Q3 ended 2026-09-30, released 2026-10-22
URL: https://www.sec.gov/Archives/edgar/data/0000822416/000082241626000041/ex991earningspr9302026.htm

| Metric | Q3-26 | Q3-25 | Note |
|---|---|---|---|
| Home sale GM (GAAP) | **24.8%** | 26.2% | Includes $26M (~70 bps) of land impairments. Q2-26 was 25.0% |
| GM excluding impairments | ~25.5% **DERIVED** (24.8 + ~0.7) | — | PHM does not publish an "adjusted GM" line |
| Net new orders | **6,208** (−6%) | 6,638 | Order value $3.5B vs $3.6B (table: $3,498.6M vs $3,639.7M) |
| Florida orders | 1,823 | 1,721 | ≈ +5.9% **DERIVED**. FL backlog 3,097 vs 2,694 |
| Closings | 6,876 (−9%) | 7,529 | |
| ASP, closings | **$561K (−1%)** | $564K | |
| Backlog | 10,298 units (+4%), $6.4B (+3%) | 9,888 / $6.2B | |
| SG&A % | 10.3% | 9.4% | |
| Mortgage capture | 85% (table: 84.6%) | 84% (84.4%) | |
| Avg community count | 1,077 (+7%) | | |
| Cancellation rate | **NOT DISCLOSED** in the release | | |
| Incentives % of price | **NOT DISCLOSED** in the release | | |
| Guidance | **None in the release** | | The CEO cites "rapid increase in interest rates". Outlook was given on the 10/22 call, which was not retrieved |

### NVR: Q3 ended 2026-09-30, released 2026-10-22
URL: https://www.sec.gov/Archives/edgar/data/0000906163/000090616326000099/q32026ex991_earningsrelease.htm

| Metric | Q3-26 | Q3-25 | Note |
|---|---|---|---|
| Homebuilding gross profit margin | **18.3%** | 21.0% | Hit by higher lot costs, "pricing pressure due to continued affordability challenges and weak consumer sentiment", and ~$24.8M of contract land deposit impairments. No adjusted figure published |
| New orders | **4,391 (−7%)** | 4,735 | |
| ASP, new orders | **$442,100 (−5%)** | | |
| **Cancellation rate** | **21%** | 19% | |
| Settlements | 5,268 (−7%), ASP $445,900 (−2%) | 5,639 | |
| Backlog | 10,121 units (+10%), $4.59B (+4%) | | |
| Mortgage closed-loan production | $1.38B (−10%) | | |
| Net income | $248.6M (−27%), EPS $89.45 | $342.7M | |
| Guidance | NVR gives none | | |

### Meritage (MTH): Q3 ended 2026-09-30, released 2026-10-28 (8-K filed 10/28)
URL: https://www.sec.gov/Archives/edgar/data/833079/000083307926000133/mth20260930earningsrelease.htm

| Metric | Q3-26 | Q3-25 | Note |
|---|---|---|---|
| Home closing GM (GAAP) | **17.4%** | 19.1% | −170 bps. Driven by "higher lot and incentive costs" |
| Adjusted home closing GM | **17.9%** | 20.1% | Excludes $6.6M impairments and a $0.6M net walk-away credit. ⚠️ The CEO quote says "$6.0 million" (net of the credit); the bullet uses the gross components |
| Orders | **3,083 (−15%)** | 3,636 | Absorption pace −21% (3.0 net sales per community per month); avg community count +7% |
| ASP, orders | **$383K (−2%)** | $389K | Attributed to "higher utilization of incentives and related costs including rate buy-downs, as well as geographic mix" |
| ASP, closings | $365K (−4%) | $380K | Same incentive/buydown attribution |
| Closings | 3,187 (−14%) | 3,685 | Backlog conversion "nearly 190%" |
| Backlog | 1,611 units (−5%), $637.2M | 1,699 / $670.0M | |
| SG&A % | 11.0% | 10.8% | |
| Land spend | $329M (about −40% YoY) | | |
| Cancellation rate | **NOT DISCLOSED** in the release | | |
| Incentives % of price | **NOT QUANTIFIED**: direction only | | |
| Guidance | **None in the release**. Management expects conditions to "continue to be unpredictable over the next several quarters" | | Call is 10/29 at 08:00 PT |

### Century Communities (CCS): Q3 ended 2026-09-30, released 2026-10-28 (8-K filed 10/28)
URL: https://www.sec.gov/Archives/edgar/data/1576940/000157694026000069/ccs-20261028xex99_1.htm

| Metric | Q3-26 | Q3-25 | Note |
|---|---|---|---|
| Homebuilding GM (GAAP) | **15.0%** | 17.9% | Includes $19.6M (2.3%) of inventory impairment |
| GM excluding impairment | 17.3% | 18.3% | Issuer non-GAAP |
| Adjusted GM (excluding interest, impairment and PPA) | **19.3%** | 20.1% | Issuer non-GAAP |
| Net new contracts | **2,284 (−4.3%)** | 2,386 | Texas +21.0%; West −20.5%; Southeast −22.2% |
| ASP, deliveries | **$345.0K (−10.2%)** | $384.2K | |
| Deliveries | 2,442 (−1.8%) | 2,486 | |
| Backlog | 1,106 homes, $414.0M | | |
| SG&A % | 14.1% | | |
| **Guidance change** | **FY-26 deliveries cut to 9,350–9,650** (includes ~100 from HistoryMaker in Q4); home sales revenue **$3.3–3.4B** | Prior (Q2 release, 2026-07-22): 9,750–10,500 homes, $3.5–3.8B | Lowered on "increased mortgage rates". HistoryMaker Homes (DFW) assets acquired 2026-10-07 |
| Cancellation rate / incentives % | **NOT DISCLOSED** in the release | | |

### Taylor Morrison (TMHC) and Tri Pointe (TPH): no Q3-2026 release (from EDGAR)
- **TMHC:** no 8-K since 10/10. It filed **Form 15-12G on 2026-08-04** (deregistration).
- **TPH:** filed **Form 15-12G on 2026-05-26**. Its last 8-K and 10-Q were on 2026-08-13.
- INFERENCE, not verified: both are likely no longer SEC reporters, for example after a take-private or acquisition. Confirm before dropping them from the docket.
- Source: https://data.sec.gov/submissions/CIK0001562476.json and CIK0001561680.json

---

## 7. Trepp: late-October Q3 recap with MF figures — **NOT FOUND**
- WebSearch ("Trepp CMBS delinquency multifamily October 2026") found no Trepp Q3-2026 recap published in late October.
- Only SECONDARY items for earlier months turned up (CRE Daily, on Trepp August-2026 MF delinquency across books). They are outside the window and were not used.
- The October Trepp report is due around 11/2, per the brief.

---

## NOT FOUND list
| Item | What was tried |
|---|---|
| **Fannie Mae Monthly Summary, Sep-2026** (MF SDQ, SF SDQ) | PR Newswire Fannie feed (newest is Aug-2026); `093026.pdf` returns 404 (existing files return 403); fanniemae.com returns 403; two WebSearches. Probably not yet released |
| **ATTOM Sep-2026 monthly and Q3-2026 foreclosure report** (Q3 starts, filings, REO, FL metros, top states) | ATTOM archive via WebFetch (newest Aug, 09-17); 3 slug guesses return 404 against a 200 control; WebSearch, including a prnewswire.com-restricted search. Not yet released |
| ICE September cure figures; ICE VA figures; ICE 30-day count | Not in the First Look release (cures belong to the Mortgage Monitor) |
| PHM / MTH / CCS cancellation rates; incentive % of price for all four builders | Not in the 8-K Ex 99.1 text (only NVR discloses cancellations). Transcripts/10-Qs not retrieved |
| PHM Q4 / FY guidance | Not in the release; given on the call (not retrieved) |
| Taylor Morrison and Tri Pointe Q3-2026 | Not reporting: Form 15-12G deregistrations (TMHC 2026-08-04, TPH 2026-05-26) |
| Trepp late-October Q3 recap with MF | WebSearch; nothing in the window |
