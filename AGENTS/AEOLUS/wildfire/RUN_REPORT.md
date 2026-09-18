# AEOLUS · WILDFIRE — RUN REPORT

**run_date: 2026-09-18** (Friday) · folder last refreshed 2026-08-27 — **22-day gap closed**
**Worker run. Nothing here is graded. AEOLUS scores C4, fires triggers and resolves AEO-09.**

---

## observations_added

**5 rows → `workbook/SERIES.tsv`** (all dated 2026-09-18, all approved instrument names, 7-field check passes on all 22 rows)
**11 rows → `workbook/LOG.tsv`** (6-field check passes on all 24 rows)
Also updated: `DOSSIER.md` (full rewrite, two-clock header → `Last real data refresh: 2026-09-18`) and `SOURCES.md` (three new verified-command blocks).

### The instrument table

| instrument | value | unit | as-of | source | Δ vs prior (8/27) |
|---|---|---|---|---|---|
| `nifc_preparedness_level` | **3** | level | 9/18 *(set 9/9 07:30 MDT)* | NIFC-NFN | 🔽 **5 → 3.** PL5 run **ENDED 9/9** after **54 days inclusive / 53 elapsed** (7/18→9/9) |
| `nifc_acres_ytd` | **8,523,213** | acres | 9/18 | NIFC-NFN | ⬆️ **+551,814** |
| `nifc_acres_pct_10yr_avg` | **146** | pct | 9/18 | NIFC-NFN | 🔽 **164 → 146 (−18 pts)** |
| `nifc_fires_ytd` | **56,289** | count | 9/18 | NIFC-NFN | ⬆️ **+4,855** (pct 127 → 126) |
| `nifc_large_fires_uncontained` | **50** | count | 9/18 | NIFC-NFN | 🔽 **−44** (from 94) |
| personnel assigned *(not a vocabulary instrument — not logged to SERIES)* | **12,315** | count | 9/18 | NIFC-statistics | 🔽 **−9,539** (from 21,854) |
| 10-yr avg YTD, **published** *(context)* | **44,745 fires · 5,823,577 acres** | — | 9/18 | NIFC-NFN | 🔑 **fields render again** — blank 8/21 & 8/27 |
| `h1_us_insured_natcat` | **~$36B US / $46bn global**, 28% below avg | USD_bn | **H1 2026** | Gallagher Re / Munich Re / Aon | **UNCHANGED — no new row appended.** Vintage now **~2.5 months** old |
| Spokane single-event insured loss | **$1.0–1.3B** | USD_bn | **8/18** | **Cotality — NOT in SOURCES.md** | 🔴 **NEW to the record; MISSED by the 8/27 run** |
| NAIC company-initiated nonrenewal rate, Western Zone | **25.1** | per 1,000 PIF | **2024** | NAIC CIPR 2026-07-31 | 🔑 vintage **2022 → 2024** |
| USDM CONUS D1–D4 *(**cited from `water/`, not pulled**)* | **56.61** | pct | **8/25** | water/workbook/SERIES.tsv | ⚠️ unchanged — **water/'s own series is 24 days stale** |

### ⚠️ Read the acreage pair together, never the ratio alone

**Absolute acres ROSE +551,814 while the ratio FELL 18 points.** Third consecutive read with that signature — and this run it is **measured, not inferred**: the published 10-yr comparator grew from an implied ~4,860,609 ac (8/27) to **5,823,577 ac** (9/18), **+962,968 acres of denominator in 22 days** against +551,814 of numerator. **The comparator is accreting faster than this year's fires. The falling percentage is not a deceleration signal on its own.**

✅ **Reproducibility:** `8,523,213 / 5,823,577 = 146.36%` and `56,289 / 44,745 = 125.80%` — both narrative percentages reproduce from the newly-rendering published averages. **DOSSIER open question #6 (derived-vs-published averages, open since 8/21) is CLOSED.**

---

## threshold_state

*Values and margins only. **NOT-FIRED / FIRED language below is a statement about the arithmetic, not a grade.***

| Band (AEOLUS's, cited from `../CLAUDE.md`) | Instrument value | Margin | State |
|---|---|---|---|
| **Reinsurer cat-loss tally vs 10-yr avg** — Y ≥110% · O ≥130% · **R ≥150%** | **~72%** (H1 2026, "28% below the 10-year average") | **~38 pts below YELLOW; ~78 pts below RED** | **NOT-FIRED — and pointing the opposite way.** ⚠️ **Measured on a window that CLOSED 2026-06-30** |
| **C4 upgrade 3 → 4:** carrier insolvency **OR** single **>$10B** insured cat | Spokane **$1.0–1.3B** (Cotality 8/18) / "hundreds of millions… plausibly $1B" (Gallagher Re 8/6). No insolvency reported | **~$8.7–9.0B short** | **NOT-FIRED.** The higher estimate narrows the gap but **does not change the order of magnitude** |
| **C4 channel-kill:** H1 cat <110% **AND** non-renewals stable 2+ quarters | loss leg ~72% **satisfies**; non-renewal leg **cannot be evaluated** (annual series, ends 2024) | conjunction unsatisfied on leg 2 | **NOT-FIRED** |
| **Property non-renewal rate** — Y +10% YoY · O +25% · R +40%/carrier exit | NAIC Western Zone **8.0 → 25.1 per 1,000 (2022→2024)**; all zones **+96% to +216% since 2018** | see caveats — **wrong periodicity, wrong vintage, unknown zone membership** | ⚠️ **NOT GRADEABLE. See the three blockers below.** |

🔴 **146% IS AN ACREAGE PERCENTAGE. THE CAT-LOSS BAND READS ~72%.** Different rows of the threshold table, different units. This run the temptation runs the *other* way from usual — the peril leg cooled on five of six fields, which invites reading convergence. **It is not convergence:** one leg is decaying (and partly for denominator reasons), the other is **frozen on a window that ended before the fires**. A real convergence read waits for the **Q3 tally (~Oct)**.

---

## changes

**1. 🔽 The peril leg cooled on every field except absolute acres.** PL **5 → 3** (9/9, ending a 54-day-inclusive PL5 run); uncontained large fires **94 → 50**; personnel **21,854 → 12,315**; acreage ratio **164% → 146%**. Absolute acres **+551,814** and absolute fires **+4,855**.

**2. 🔑 The September outlook is ISSUED (9/01) — the 9/01 AEO-09 checkpoint the last two runs were waiting on is now live.** Full grading inputs below. *(It was the #2 open question on 8/27.)*

**3. ➡️ The southern Plains converted from forecast to fire.** TX **6** and OK **4** large fires — **10 of the nation's 50**, where the Southern Area had no entry in the 8/27 geographic read.

**4. 🔴 The loss leg did not move at all.** No Q3/post-H1 aggregate from Gallagher Re, Munich Re, Aon or Swiss Re. **The RED-band instrument still reads a window that closed 2026-06-30 — before Spokane and before the entire August peak.**

**5. 🔴 A second, higher Spokane loss estimate exists and the 8/27 run missed it** (Cotality, **$1–1.3B**, issued **8/18**).

**6. 🔑 The non-renewal vintage advanced 2022 → 2024** (NAIC CIPR MCAS report, 2026-07-31).

**7. 🔴 Spokane structure counts are now THREE irreconcilable objects** — Gallagher Re ">700 homes" (8/6), **NIFC "over 800 structures" (9/01)**, Cotality "**42** classified as destroyed" out of 5,256 damaged (8/24).

---

## 🔴 AEO-09 — GRADING INPUT ONLY. NO VERDICT. AEOLUS RESOLVES.

**Outlook issue date, verbatim header:** *"Issued: September 1, 2026 / Next Issuance: October 1, 2026 / Outlook Period – September through December 2026."* **The October issue does not yet exist.**
**Rule applied as handed over, not re-adjudicated:** read the **current-month** panel; where map and regional narrative disagree, **the regional section governs.**

### Current-month panel = SEPTEMBER

**Southern Area regional narrative — the GOVERNING surface, verbatim:**
> *"Confidence is higher in drought continuing to worsen over most of the southern Plains and Lower Mississippi Valley during September. Some areas received beneficial rainfall in late August, but the return of dry and unusually hot weather will likely mean any relief is temporary.* **An expansive area of above-normal significant fire potential is expected across Texas, Oklahoma, Arkansas, Louisiana, Mississippi, and southwestern Alabama for the month ahead.** *These conditions may very well continue into October and November in portions of the region, but confidence is low as to where conditions will remain driest. Fuel concerns are abundant, ranging from the recent curing of fine fuels to drought and beetle kill, along with tornado, ice storm, and hurricane damage."*

**Executive Summary, verbatim:**
> *"From the current and past weather, as well as forecast conditions, September significant fire potential will remain above normal in most of the Northwest, far northern California, central and southern Idaho, northern Nevada, and northern Utah.* **Above normal potential is also forecast for much of the southern Plains into the Lower Mississippi Valley**, *South Florida, northern Minnesota, northern Wisconsin, western Upper Michigan, Puerto Rico, and the U.S. Virgin Islands."*

**MAP panel (September 2026), read from the page-1 image extracted with `pdfimages`:**
- **Oklahoma: ENTIRELY red / Above**, Panhandle included.
- **Texas: red across the central and eastern ~two-thirds**, south to the Rio Grande Valley — **far-west TX (Trans-Pecos/El Paso) and part of the western Panhandle are WHITE / Normal.**
- Also red: Pacific Northwest block, N Minnesota / N Wisconsin, South Florida, Puerto Rico.

| | TX above-normal? | OK above-normal? |
|---|---|---|
| **Regional narrative (governs)** | **YES** — named explicitly | **YES** — named explicitly |
| **Executive Summary** | YES ("southern Plains") | YES ("southern Plains") |
| **Map panel** | **PARTIALLY** — two-thirds red, far west normal | **YES — entirely** |

✅ **NO map/text disagreement in the current-month panel.** Map and regional section both designate TX and OK above-normal for September. **The governing rule is not load-bearing this month.**

⚠️ **One nuance only the map carries, and it is a definitional question for AEOLUS, not a data question:** **Texas is only PARTLY above-normal.** If "removed for TEXAS" means *any part of TX*, September fails removal; if it means *whole-state*, far-west TX was already normal on 9/01.

### Out-month panels — here the disagreement IS real

| Panel | Map | Exec Summary | Southern Area section |
|---|---|---|---|
| **October** | **TX/OK NORMAL** (red only N Minnesota, N Wisconsin, W Upper Michigan, PR/USVI) | **agrees**: *"For October, significant fire potential will be normal for most of the country except for northern Minnesota, northern Wisconsin, western Upper Michigan, Puerto Rico, and the U.S. Virgin Islands."* | 🔴 **hedges the other way**: *"These conditions may very well continue into October and November in portions of the region, but confidence is low as to where conditions will remain driest."* |
| **November** | CONUS normal; PR/USVI above | **agrees** | as above |
| **December** | CONUS normal; PR/USVI above | *"Significant fire potential will be normal for the contiguous U.S. and Alaska for November and December but will remain above normal for Puerto Rico and the U.S. Virgin Islands."* | — |

🔴 **The OCTOBER panel is a genuine map/text disagreement — the exact case the governing rule was written for.** Flagged, **not adjudicated.** Note its character: the regional section offers a **low-confidence hedge** ("may very well… but confidence is low"), **not a competing designation.** Whether a hedge counts as the regional section "disagreeing" is **AEOLUS's call**, and it decides whether an October read is *removal* or *not-yet-removal*.

### The ENSO tension is NOT resolved — it is stronger *(`regime/` owns ENSO; cited, not adopted)*

> *"El Niño continues to rapidly strengthen in the equatorial Pacific Ocean. Central Tropical Pacific sea surface temperature anomalies are more than 1.5 C above average, the threshold for a strong El Niño, and are nearing the 2 C threshold for a very strong El Niño… The CPC forecasts El Niño to persist through the fall and winter, with 100% confidence, with a greater than 95% chance of a very strong El Niño by November… most of the models used by the CPC and internationally show this El Niño to be the strongest on record."*

⚠️ **The 8/13 load-bearing tension persists and has grown: the outlook uses El Niño to EXPLAIN above-normal fire potential in the very region where AEO-09 expects El Niño to REMOVE it.** The counter-mechanism AEO-09 needs is in the same section — *"El Niño's influence… setting the stage for what will likely be a very wet end to the year over much of the Southern Area"* — but it arrives with its own hedge: *"confidence is low in whether heightened late summer fire activity will bleed into the more traditional fall fire season in October and November."*

### Physical state has moved AGAINST removal since 8/27
**TX 6 + OK 4 = 10 of 50 national large fires.** Outlook, verbatim: *"Much of Texas and Oklahoma received less than 20% of normal rainfall for August"*; *"Rapid drought onset was observed in the southern Plains and Lower Mississippi Valley"*; extreme-to-exceptional drought *"most widespread across central Oregon, the eastern Great Basin, central Rockies, Texas Panhandle, and western Oklahoma."*

---

## proposed_findings *(PROPOSALS — AEOLUS adjudicates every one)*

**P1 — The loss leg's problem is no longer "soft", it is "blind."** H1 2026 measures a window that **closed 2026-06-30**. It contains no Spokane, no August peak, no part of the PL5 run. **It is not evidence that this fire season was cheap; it is not evidence about this fire season at all.** Every prior read framed the divergence as *peril high / losses low*. The honest 9/18 framing is *peril cooling / losses unmeasured*. **The Q3 tally (~Oct) is the first vintage that can speak to it** and is this folder's highest-value pending item.

**P2 — The 8/27 "only insured-loss figure" claim was false when written, and the failure is scope, not diligence.** Cotality published **$1–1.3B on 8/18**, nine days before the 8/27 check concluded none existed. The check searched **Artemis only**; the conclusion was **stated at world scope**. *(`finding_scan_keyed_on_naming_reads_local_form_as_absence`.)* **Proposed guard: a negative finding states the set that was searched, in the finding itself.**

**P3 — Spokane structure counts do not reconcile and must not be averaged.** ">700 homes" (Gallagher Re 8/6) vs **"over 800 structures" (NIFC 9/01)** vs **"42 classified as destroyed"** of 5,256 damaged (Cotality 8/24) — a **~17–19×** spread on "destroyed." Different objects, methods and possibly perimeters. ⚠️ **Note the counter-intuitive direction: Cotality is the LOW outlier on destroyed structures yet carries the HIGHEST loss estimate** — so the loss estimate is **not a simple function of its own destroyed-count**, which matters before either number is cited. **NIFC's "over 800" is the upward revision `SOURCES.md` warned about, and it comes from a source this folder already owns.**

**P4 — The non-renewal leg has a better instrument and is still not gradeable. Three blockers, all structural:** ① **MCAS is ANNUAL and ends 2024** — a *"stable 2+ quarters"* test **cannot be run on it at any vintage**; ② **no state cut exists** (zone-level only — "state-level" in the title describes the data *source*, not the granularity); ③ **zone membership is not stated in the report**, so **the Western 25.1 cannot be mapped onto the fire geography** until AEOLUS confirms it from an NAIC primary. **Proposal: log the definition and the series, but do NOT retire the non-renewal gap.**

**P5 — 🔴 California's non-renewal rate is CENSORED BY LAW, which makes a benign print uninformative.** A Governor's emergency declaration freezes non-renewals for one year in named ZIP codes (CA DOI primary, verified live 9/18; most recent **2026-08-06 Gann Fire**, active to **2027-08-06**). **The suppression is strongest exactly where fires are worst.** AEOLUS's band is a **CHANGE** band, so a moratorium mechanically holds the measured change down. **A reading at-or-below band in CA is consistent with BOTH a calm market AND a suppressed one — the instrument cannot separate them, and a benign print must not be counted as the channel-kill leg satisfied.**

**P6 — Never delta the FIO figure against the NAIC figure.** FIO/PCMI (80% of HO-3/HO-5 by premium, 2018-2022) and NAIC/MCAS (state-reported, 2018-2024, excl. PR/ND/NY) are **different collections over different universes.** `1.04%` vs a worker-computed `1.955%` would **measure the instrument change, not the market.** **The MCAS 2022→2024 series is internally consistent and is the only usable trend.**

**P7 — Always publish the acreage pair, never the ratio.** Third consecutive read where **absolute acres rose while the ratio fell**. With the published comparator now visible, the mechanism is confirmed arithmetically: **+962,968 acres of denominator vs +551,814 of numerator in 22 days.**

**P8 — Secondary coverage of the NAIC report is inverted; quote the report.** Press summaries render the trend as *"96% in the Southeast to 216% in the West."* The report says: *"The most significant increases have occurred in the **Northeast and Southeast** Zones during this period at **147% and 216%**, respectively."*

**P9 — Source-admission request (AEOLUS-only decision): Cotality.** It produced the **only quantified Spokane loss range** and an independent structure analysis, and it is **not in `SOURCES.md`.** Reported as a proposal; **no Cotality figure has been logged as fact.** AEOLUS decides admission.

**P10 — Owner-side gap, flagged not fixed: `water/`'s USDM series is 24 days stale** (newest observation **8/25**). The shared-input rule was observed — **no USDM pull, no USDM row written here.** But the fuel-state context for this fire read is stale **at the owner**. *(Independent corroboration from a source wildfire/ does own: the NIFC 9/01 outlook states "nearly 57% of the country in drought as of August 25", consistent with water/'s 56.61%.)*

---

## gaps *(a required output — a reported gap beats a worked-around one)*

| # | Item | Exact command / attempt | Exact result |
|---|---|---|---|
| 1 | **NAIC report via curl** | `curl -sL -A "Mozilla/5.0" -o naic_ho.pdf "https://content.naic.org/sites/default/files/mcas-homeowners-property-insurance-market-dynamics-report.pdf"` | **`HTTP=403 SIZE=5735 TYPE=text/html`** — served an HTML block page named `.pdf`. Same 403 on `content.naic.org/industry/mcas/homeowners-insurance-report`. **Recovered via WebFetch**, which saved the real 9.2 MB PDF to disk; extracted locally with pdfminer (93,040 chars, clean). **Not a substitution — same document, same publisher, different transport.** Recorded in `SOURCES.md`. |
| 2 | **NAIC zone → state membership** | `grep -n -E "Texas\|California\|Washington\|Oregon\|Colorado" naic_ho.txt` | **ZERO matches. No US state name appears anywhere in the report text.** Zone membership is **not recoverable from this source** and the worker **does not supply it from memory**. **Blocks any geographic mapping of the 25.1 figure.** |
| 3 | **Q3 / post-H1 2026 aggregate cat tally** | Artemis.bm + Reinsurance News searched for Gallagher Re / Munich Re / Aon / Swiss Re Q3 2026 | **None exists.** Latest published remains H1 2026. **Not a pull failure — a genuine absence, and the central finding of the loss leg (P1).** |
| 4 | **Artemis wildfire-tag listing** | WebFetch `https://www.artemis.bm/news/tag/wildfires/` | Returned a page whose lead article was dated **2018-11-14**; **no 2026 Spokane item surfaced.** ⚠️ **This is how the 8/18 Cotality estimate stayed invisible on 8/27 — the tag listing is an unreliable recency surface.** Do not treat an empty Artemis tag page as a negative. |
| 5 | **WA state EOC FINAL Spokane structure tally** | not located | ❌ **Third consecutive run with no final EOC tally.** The three published counts still do not reconcile (P3). |
| 6 | **CA-specific non-renewal RATE with a denominator** | CA DOI moratorium page fetched successfully | Page is live but **publishes no rate or policy-count statistic with a denominator.** A *"2.8 million policies non-renewed 2020-2025 in fire-prone ZIP codes"* figure appeared in **secondary search summary only, with no denominator and no primary fetch — NOT logged as fact.** |
| 7 | **NIFC preparedness-level STEP history** | — | The NFN page shows **only the current level.** Whether PL went 5→4→3 or 5→3 is **not answerable** from any source in `SOURCES.md`. **Not worked around.** |
| 8 | **`water/` USDM currency** | cited, not pulled (shared-input rule) | Newest water/ observation **2026-08-25 — 24 days stale.** Owner-side; flagged, not fixed. |

---

## contradictions with DOSSIER.md — flagged loudly, not silently overwritten

**① `DOSSIER.md` §3 and §4 were carrying `171%` as the live acreage figure.** 171% was the **8/21** value, superseded by **164% on 8/27**. The 8/27 run updated the **§1 table** and left **both summary sections** on the old number — so a reader of the summary got a figure two vintages behind the body. **Now 146% throughout.** *(`finding_summary_section_merges_what_the_body_separates` — the abstract is where a correction lands last.)*

**② `DOSSIER.md` §2 + the 8/27 LOG row asserted the Gallagher Re estimate "remains the only insured-loss figure for this event."** **False when written** — Cotality had published **$1–1.3B on 8/18** (P2). Both surfaces corrected; the old claim is preserved in the new LOG row so the error stays visible rather than being erased.

**③ `DOSSIER.md` §1 recorded the 10-yr-average fields as rendering BLANK** *(noted 8/21 and confirmed 8/27)*. **They render this run.** Not a contradiction in the data — a **change in the source's behaviour** — but it retires standing open question #6, and any future blank should now be read as **intermittent**, not permanent.

**④ Framing carried forward from 8/13–8/27 — "physical peril elevated, insured losses below average" — no longer describes the peril side.** PL is **3**, uncontained large fires halved, personnel down 44%. The *insurance* half of the divergence claim stands; the *peril* half has cooled. **AEOLUS owns whether the C4 score moves. The worker only reports that the inputs behind the 8/13 score of 3 🟠 ↗ have changed on both legs since it was set.**
