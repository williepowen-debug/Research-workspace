# AEOLUS · WILDFIRE — verified primary sources

**Commands below were run and returned the stated values on 2026-08-13** unless marked otherwise.

---

## PERIL LEG

### NIFC National Fire News — preparedness level, active fires, YTD acres ✅ verified 8/13, 8/21, 8/27
`https://www.nifc.gov/fire-information/nfn`
**Verified return (8/12 report):** PL **5**, **101** uncontained large fires, **6,447,442** acres YTD, **46,509** fires = **126%** and **155%** of 10-yr averages respectively.
**Verified return (9/18 report):** PL **3** ("as of September 9, 2026 at 7:30 a.m. MDT" — PL5 run ENDED 9/9), **50** uncontained large fires, **8,523,213** acres YTD = **146%**, **56,289** fires = **126%**, personnel **"over 12,000"** in narrative. 🔑 **The 10-yr-average fields RENDER AGAIN this run** (blank on 8/21 and 8/27): published **10-year average Year-to-Date 2016-2025 = 44,745 fires / 5,823,577 acres**, and both narrative pcts reproduce exactly from them. ⚠️ **Two active-acreage fields differ by definition:** NFN "Acres from all active fires" = 1,292,408 vs statistics-page "Acres Burned on Large Fires" = 2,523,653.
⚠️ **The statistics page gives EXACT personnel where NFN rounds** — statistics: **12,315**; NFN narrative: "over 12,000". Prefer the statistics page for personnel. Statistics page "Last Updated: Friday, September 18, 2026 - 08:37".
⚠️ **The NFN page shows only the CURRENT preparedness level, never the step history.** Whether PL went 5→4→3 or 5→3 is not answerable from this source; the NIFC Preparedness Levels page / IMSR archive would be needed and **neither is in this file** — do not reconstruct one.
**Verified return (8/27 report):** PL **5** (set 7/18/26 07:30 MDT), **94** uncontained large fires (label = "Total number of large fires" / "Current Active Large Fires"), **7,971,399** acres YTD = **164%**, **51,434** fires = **127%**, **21,854** personnel. Field labels confirmed present: "Number of new large fires" (7), "Total number of large fires" (94), "Fires contained" (1). ⚠️ **10-yr-average fields still render BLANK in served HTML** — pct figures are narrative-derived, not from a labeled field (unchanged from 8/21).

### NIFC statistics (the numeric series)
`https://www.nifc.gov/fire-information/statistics`

### 🔑 National Significant Wildland Fire Potential Outlook — the forward instrument
`https://www.nifc.gov/nicc-files/predictive/outlooks/monthly_seasonal_outlook.pdf`
**Issued ~the 1st of each month; next issuance stated in the header.** This is the **only forward-looking primary** here and the one that resolves **AEO-09**.
⚠️ **The URL is stable but the CONTENT is replaced monthly** — the file is not versioned. **Record the issue date with any figure you take from it**, or you will cite a superseded outlook from a live-looking URL (`finding_dated_stamp_is_a_trigger_not_a_shield`).
✅ **Verified 2026-09-18: the SEPTEMBER issuance EXISTS.** Header: *"Issued: September 1, 2026 / Next Issuance: October 1, 2026 / Outlook Period – September through December 2026."*
🔑 **THE MAP PANELS ARE EXTRACTABLE — pdfminer text alone is NOT enough for AEO-09.** The four monthly panels are images on page 1 and carry designations the narrative does not (e.g. far-west TX normal in September while every text surface says "southern Plains"). Verified working:
```
curl -sSL -o outlook.pdf "https://www.nifc.gov/nicc-files/predictive/outlooks/monthly_seasonal_outlook.pdf"
python3 -c "from pdfminer.high_level import extract_text; open('outlook.txt','w').write(extract_text('outlook.pdf'))"
pdfimages -f 1 -l 1 -png outlook.pdf panel      # panel-001=month1 ... panel-004=month4
```
**Regional sections are the AEO-09 grading surface** — find them with `grep -n "^Southern Area" outlook.txt` (9/01 issue: line 811).
**Verified (Aug-1 issuance):** above-normal potential across the western/north-central US, **newly expanding into TX, OK and the Lower Mississippi Valley.**

### Drought — the fuel-state driver → **`../water/SOURCES.md` § 1 is the canonical home**

⚠️ **MOVED 2026-08-13 (Will-directed). Do not re-add the pull commands here.**

Drought was originally filed in this folder because it was the instrument I was using for fire that session. **That was a misfiling: drought is not wildfire's instrument.** It is the shared upstream input to **four** channels — **C2** crops, **C4** fire fuel state, **C5** river navigation, **C6** reservoir inflow. Keeping it under one consumer made it invisible to the other three and allowed the same dataset to produce different reads in two places.

**Current state (valid 8/11): CONUS D1–D4 `50.38%`, D0–D4 `73.62%`, every tier up WoW.**

🔑 **The fire-specific discipline, which stays here:** a national drought number is **not** a fire signal. **Pull the state/county cut and confirm the geography overlaps the fire exposure.** On 8/13 the deterioration was in **OK / TX Panhandle**, which firmed the fire outlook — while **crops in the corn belt independently refused to confirm.** Same dataset, opposite verdicts, decided entirely by geography.

---

## INSURED-LOSS LEG

### 🔴 THE SERIES THAT NO LONGER EXISTS (L-05)
**NOAA NCEI's Billion-Dollar Weather and Climate Disasters database was DISCONTINUED (Jul 2025)**, stewardship moved to Climate Central. **Do not cite it and do not expect it to return.** A government series can vanish — this channel therefore runs on **private** tallies with a redundant feed.

### Replacements (use these)
| Source | What it gives |
|---|---|
| **Gallagher Re** / **Munich Re** / **Aon** cat reports | H1 and full-year insured nat-cat tallies vs 10-yr average — **the RED-band instrument** |
| **Artemis.bm** | reinsurance ROL, renewal pricing, cat-bond issuance |
| **Climate Central** | the NCEI successor for event-loss framing |
| **CA DOI** / **CA FAIR Plan** | non-renewal rates, residual-pool enrollment, assessments |
| State insurance departments (WA, CO, OR, TX) | non-renewal + carrier-exit filings in newly-repricing states |

### 🔑 Non-renewal rate — NATIONAL + REGIONAL, verified 2026-08-27
**US Treasury FIO, "Analyses of U.S. Homeowners Insurance Markets, 2018-2022: Climate-Related Risks and Other Factors" (Jan 2025)** — built on the NAIC/FIO PCMI Data Call (80% of HO-3/HO-5 policies nationwide by premium).
```
curl -sL -A "Mozilla/5.0" -o fio_report.pdf "https://home.treasury.gov/system/files/311/Analyses_of_US_Homeowners_Insurance_Markets_2018-2022_Climate-Related_Risks_and_Other_Factors_0.pdf"
python3 -c "from pdfminer.high_level import extract_text; open('fio_report.txt','w').write(extract_text('fio_report.pdf'))"
grep -n -i "nonrenewal rate" fio_report.txt
```
**Verified return (8/27):** ~3.4MB PDF, extracts cleanly with pdfminer.six. **Definition (p.7, verbatim): "Nonrenewal Rate = Count of Nonrenewals in Reporting Year / Policies in Force at End of Reporting Year."** National avg 2018-2022 = **1.04%** (rose to 1.20% by 2022). By national climate-risk (TLCR) quintile: Highest-Risk **1.61%** vs Lowest-Risk **0.90%**; Highest-Risk rose 1.10%→2.37%, 2018→2022. Southwest region (CA/AZ/NV/CO/NM/UT) **1.28%** avg, Highest-Risk category **1.92%**. Northwest region (WA/OR/ID/MT/WY/AK) **0.67%** avg, Highest-Risk **0.86%**. **Full detail → `workbook/LOG.tsv` 2026-08-27 `nonrenewal_gap_partially_closed`.**
⚠️ **Vintage ceiling: data ends 2022, published Jan 2025. No 2023/2024/2025/2026 coverage** — the report's own limitations section says so. **No WA-state-specific cut** (regional only). **TX excluded from nonrenewal calc entirely** (insurer data gap, per report footnote).
### 🔑 Non-renewal — FRESHER VINTAGE FOUND 2026-09-18 (NAIC MCAS, data through **2024**)
**NAIC Center for Insurance Policy and Research, "Examining Homeowner Property Insurance Market Dynamics — An Assessment of Countrywide State-Level Data From 2018 to 2024", FINAL RESEARCH REPORT dated 2026-07-31.** Supersedes the FIO/PCMI report as the *freshest* non-renewal instrument (FIO stays the only one that names its member states).
⚠️ **`curl` returns HTTP 403 on both `content.naic.org` URLs — bot-protected.** Do NOT conclude the document is gone. Retrieve with **WebFetch**, which saves the 9.2 MB PDF to disk, then extract locally:
```
# WebFetch https://content.naic.org/sites/default/files/mcas-homeowners-property-insurance-market-dynamics-report.pdf
# -> saves to the tool-results dir; then:
python3 -c "from pdfminer.high_level import extract_text; open('naic_ho.txt','w').write(extract_text('<saved>.pdf'))"
grep -n -i "nonrenewal" naic_ho.txt
```
**Verified return (9/18):** 93,040 chars, clean extract. **Denominator (verbatim): "we normalize the nonrenewal data by the total number of policies in force to get a ratio of company-initiated nonrenewals per 1,000 policies in force."** 2024 rates per 1,000 PIF — Western **25.1**, Southeast **22.0**, Midwest **14.2**, Northeast **11.7**; national total **2,019,799** nonrenewals; all four reproduce from the published counts and sum to the stated national total.
⚠️ **Vintage ceiling: ends 2024, and MCAS is ANNUAL — it cannot answer a "stable 2+ quarters" question.** ⚠️ **Zone-level ONLY — no state figures anywhere in the text, and the zone STATE MEMBERSHIP is not stated in the report.** Excludes Puerto Rico, North Dakota, and New York (NY files no MCAS data).
⚠️ **Never compute a delta between the FIO 1.04% and the NAIC per-1,000 figures** — different data calls, different universes; the delta would measure the instrument.

### CA DOI — a WORKING page (the 8/27 404 was a different path)
`https://www.insurance.ca.gov/01-consumers/140-catastrophes/MandatoryOneYearMoratoriumNonRenewals.cfm` ✅ **fetched live 2026-09-18.**
Gives moratorium mechanics + the dated declaration list (most recent **2026-08-06 Gann Fire**). ⚠️ **Publishes NO rate or policy-count statistic with a denominator** — it is a mechanism source, not a metric source.
🔑 **Use it as a CENSORING flag:** a Governor's emergency declaration freezes non-renewals for one year in the named ZIP codes, so CA's measured non-renewal rate is **suppressed hardest exactly where fires are worst.** A benign CA/Western print is therefore ambiguous between a calm market and a censored one.

⚠️ **PROPOSED, NOT ADMITTED — Cotality (Hazard HQ):** `https://www.cotality.com/hazard-hq/cotality-analysis-21b-in-spokane-wildfire-exposure` carries a **$1B–$1.3B** Spokane insured-loss estimate (issued 2026-08-18) and an aerial-imagery structure analysis. **It is NOT an approved source.** A worker may report it as a proposal; **only AEOLUS may admit it here or log its figures as fact.**

⚠️ **Failed on 2026-08-27:** `insurance.ca.gov/01-consumers/140-catastrophes/WildfireInsuranceInformation.cfm` → 404. `cfpnet.com/about-us/newsroom/policy-in-force-data/` → 404. Neither yielded a working command for a CA-specific or more-current (2023+) cut.

⚠️ **These are commercial publishers on their own schedule.** H1 figures land ~Jul–Aug; full-year ~Jan. **Between publications the loss leg is genuinely stale and should be labelled so** — do not substitute an acreage figure to fill the gap. That substitution is the exact error this folder's README is built to prevent.

---

## EVENT-LEVEL

- **InciWeb** `https://inciweb.wildfire.gov` — individual incident status
- **State EOCs** — structure-loss counts. ⚠️ **Early structure counts are provisional and revise upward for days.** Record the count *with its as-of date and its issuing authority*; a county fire chief's estimate and a state EOC tally are different objects.
- **CAL FIRE** `https://www.fire.ca.gov/incidents` — CA incidents + statewide YTD

---

## KNOWN TRAPS

| Trap | Guard |
|---|---|
| Acreage % of average read as the cat-loss band | **Different instruments.** 155% acres ≠ 150% losses. See README. |
| Two "official" acreage totals disagreeing | NIFC's own YTD vs other federal tallies diverge; **state which one and its date**. |
| Monthly outlook PDF at a stable URL | **Content is replaced, not versioned. Stamp the issue date.** |
| One destructive season = climate trend | Attribution is mine to adjudicate; **one event is insufficient** and I should say so. |
| **Stating a negative at WORLD SCOPE after searching ONE set** | 🔴 **THE 8/27 DEFECT, ADMITTED 9/18 (KB-AEO-129).** I wrote that Gallagher Re's was *"the only insured-loss figure for this event"* — **Cotality had published $1.0–1.3B nine days earlier.** The check searched **Artemis only**; the claim was stated at world scope. **GUARD: a negative finding must name the set that was searched, inside the finding.** "No such figure exists" is never writable; *"no such figure appears in \<named set\>, searched \<date\>"* is. |
| Treating an empty **Artemis tag listing** as a real-world absence | 🔴 **It is an unreliable recency surface** — `artemis.bm/news/tag/wildfires/` returned a page whose LEAD article was dated **2018-11-14**. This is the mechanism that hid the Cotality estimate for 22 days. **Never read an empty tag page as a negative.** |
| Averaging the Spokane structure counts | 🔴 **THREE IRRECONCILABLE OBJECTS, ~17–19× apart:** ">700 homes" (Gallagher Re 8/6) · **"over 800 structures" (NIFC 9/01)** · "**42** classified as destroyed" of 5,256 damaged (Cotality 8/24). Different objects, methods, perimeters. **Never average; always name the object.** ⚠️ Counter-intuitive: **Cotality is the LOW outlier on destroyed structures yet carries the HIGHEST loss estimate** — the loss figure is not a function of its own destroyed-count. |
| Reading a benign **California** non-renewal print as a calm market | 🔴 **CA non-renewals are CENSORED BY LAW** — a Governor's emergency declaration freezes them for one year in named ZIPs (most recent **2026-08-06 Gann Fire**, active to **2027-08-06**), **and the suppression is strongest exactly where fires are worst.** My band is a CHANGE band, so the freeze mechanically holds the change down. **A benign CA print is consistent with BOTH a calm and a suppressed market and MUST NOT satisfy the channel-kill leg.** KB-AEO-130. |
| Deltaing the **FIO** figure against the **NAIC** figure | **Different collections, different universes.** FIO/PCMI = 80% of HO-3/HO-5 by premium, 2018-2022. NAIC/MCAS = state-reported, 2018-2024, excl. PR/ND/NY. A 1.04% vs 1.955% comparison **measures the instrument change, not the market.** Only the MCAS 2022→2024 series is internally consistent. |
| Quoting the NAIC zone increases from press coverage | **Secondary coverage is INVERTED.** Press renders it *"96% in the Southeast to 216% in the West."* The report says: *"The most significant increases have occurred in the **Northeast and Southeast** Zones ... at **147% and 216%**, respectively."* **Quote the report.** |

---

## 🔑 EVENT-LEVEL INSURED LOSS — Cotality ADMITTED 2026-09-18 (AEOLUS ruling, KB-AEO-129/131)

**Admitted as a VENDOR CAT-MODELLING ESTIMATE — a distinct class from an issuer market tally.** It produced the only quantified Spokane loss range and an independent structure analysis, and its absence from this file is why the 8/27 negative went unchallenged.

| Class | Example | May it enter the cat-loss band? |
|---|---|---|
| **Issuer market TALLY** (Gallagher Re, Munich Re, Aon, Swiss Re H1/Q3) | $46bn global H1'26 = ~72% of the 10-yr avg | ✅ **yes — this is the band's instrument** |
| **Vendor cat-model ESTIMATE** (Cotality, Moody's RMS, Verisk) | Spokane **$1.0–1.3B**, 8/18 | ⚠️ **event-level input only — NEVER the aggregate band** |
| **Modelled SCENARIO** (Swiss Re FL, 9/16) | $300bn+ Cat-5 Miami/Tampa | ⛔ **never — it is not a loss that occurred** |
| **Survey of EXPECTATIONS** (Moody's Jan-27 renewal, 9/16) | −7.5% to −15%, 86% expect declines | ⛔ **never — an expectation is not a transacted print** |

> 🔴 **THE LOSS LEG IS BLIND, NOT SOFT.** The band's instrument still reads **H1 2026 — a window that CLOSED 2026-06-30**, before Spokane, before the August peak, before any part of the 54-day PL5 run. **~72% is not evidence the season was cheap; it is not evidence about the season at all.** The **Gallagher Re Q3 tally (~October)** is the first vintage that can speak to it and is this folder's highest-value pending item.

