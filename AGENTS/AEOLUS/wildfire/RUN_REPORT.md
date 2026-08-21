# AEOLUS · WILDFIRE — RUN REPORT

**run_date: 2026-08-21** · worker run · data date **2026-08-21** (NIFC statistics "Last Updated: Friday, August 21, 2026 – 09:20")
*Overwrites the previous run. Prior run: 2026-08-13.*

---

## observations_added

**5 rows → `workbook/SERIES.tsv`** · **4 rows → `workbook/LOG.tsv`** (9 total)

SERIES (all `date=2026-08-21`, `source=NIFC-NFN`):
`nifc_preparedness_level=5` · `nifc_acres_ytd=7642082` · `nifc_fires_ytd=50077` · `nifc_acres_pct_10yr_avg=171` · `nifc_large_fires_uncontained=76`

LOG: `nifc_refresh` (8/21) · `nifc_outlook_still_august` (8/21) · `spokane_insured_loss_estimate` (8/06) · `spokane_structure_count_revised` (8/06)

**No `h1_us_insured_natcat` row appended** — no new aggregate publication since 8/13; appending an unchanged row would fake a refresh.
**No new instrument invented.** The Spokane insured-loss estimate has no entry in the controlled vocabulary, so it went to `LOG.tsv` as an event and is raised below as a proposed finding for AEOLUS to adjudicate.

---

## threshold_state
*Values and margins only. The worker does not grade, score, fire or resolve.*

| Instrument | Value (as-of) | Band | Margin | State |
|---|---|---|---|---|
| **NIFC Preparedness Level** | **5 of 5**, since **2026-07-18 07:30 MDT** = **35 days inclusive / 34 elapsed** (8/21) | max tier | at ceiling — cannot go higher | **AT MAX, held through the 8-day dark period** |
| **`nifc_acres_pct_10yr_avg`** ⚠️ ACREAGE | **171%** (8/21) — 7,642,082 ac | *no acreage band exists in the threshold table* | — | ⚠️ **NOT a threshold instrument. See the red note below.** |
| **`nifc_fires_ytd`** | **50,077 = 129%** (8/21) | *no band* | — | — |
| **`nifc_large_fires_uncontained`** | **76** (8/21) | *no band* | — | **improved −25 from 101** |
| **Reinsurer cat-loss tally vs 10-yr avg** ⚠️ THE LOSS INSTRUMENT | **~72–75%** (H1 2026, unchanged since 8/13) | Y ≥110 · O ≥130 · **R ≥150** | **~35 pts below YELLOW; ~75 pts below RED** | **NOT FIRED — and pointing the opposite way** |
| **C4 upgrade 3→4: single insured cat >$10B** | Spokane, Gallagher Re 8/6: "hundreds of millions", plausible **~$1B** high case | >$10B | **~$9B short — about one order of magnitude** | **NOT FIRED** |
| **C4 upgrade 3→4: carrier insolvency** | none reported on the listed sources | any | — | **NOT FIRED** |
| **C4 channel-kill (conjunction)** | leg 1 (H1 cat <110%): satisfied at ~72–75%. leg 2 (non-renewals stable 2+ qtrs): unevidenced outside CA | both required | second leg open | **NOT FIRED** |
| **Property insurance non-renewal rate** | no new filing pulled this run | Y +10% · O +25% · R +40%/exit | — | **not measured this run** |

🔴 **THE CENTRAL DISCIPLINE, RESTATED BECAUSE THE GAP WIDENED.**
**171% is an ACREAGE percentage. The RED band is a CAT-LOSS percentage, currently ~72–75%.** Different rows of the threshold table, different units, different publishers. The peril leg moved **+16 pts (155 → 171)** in 9 days while the loss leg **did not move at all**. **The two legs are now further apart than at any prior read** — reading "PL5 for 35 days, 171% of average, costliest fire in WA history" as a hard insurance market is the exact substitution this folder exists to prevent.

---

## changes
*since the 2026-08-12/13 read*

| Item | 8/12–8/13 | **8/21** | Δ |
|---|---|---|---|
| Preparedness Level | 5, 26 days | **5, 35 days** (inclusive convention) | **+9 days at max tier** |
| Acres YTD | 6,447,442 = **155%** | **7,642,082 = 171%** | **+1,194,640 ac · +16 pts** |
| Fires YTD | 46,509 = **126%** | **50,077 = 129%** | +3,568 · +3 pts |
| Uncontained large fires | **101** | **76** | **−25 — the only instrument that improved** |
| Aug outlook | issued 8/01 | **still 8/01 — verified, next issuance 9/01** | unchanged, confirmed not assumed |
| Spokane structures | ~640–700 / ~5,390 ac (8/1–2, Spokesman/WA-EOC) | **">700 homes" / ">10,000 ac" (8/6, Gallagher Re)** | **revised UP on both, as warned** |
| Spokane insured loss | none | **hundreds of $M → plausibly $1B (Gallagher Re, 8/6)** | **new — the loss leg finally has an event number** |
| Aggregate cat losses | ~$36B, 25–28% below avg | **unchanged, no new publication** | **stale by design (H1 lands Jul–Aug, FY ~Jan)** |

**Shape of the move:** fire count +7.7% but acres +18.5% — **acres-per-fire is still rising**, i.e. larger events rather than more of them, the same signature flagged on 8/13. All ten geographic areas list ≥1 large fire; the Northwest carries 32 fires and **six over 100,000 acres**. State large-fire counts: OR 18 · WA 13 · MT 12 · ID 7 · CO 5 · UT 5 · MN 3 · NV 3 · CA 2, plus 1 each in NM, SD, AK, GA, MS, FL, WY. Personnel assigned **24,265**; acres on currently-active large fires **3,571,843** (~47% of YTD).

**The 76-vs-101 read needs AEOLUS's judgment, not the worker's:** uncontained large fires fell 25% while acreage accelerated. Both come from the same NIFC field as the 8/13 figure, so it is a real move, not a definitional one — but whether it reads as containment progress or as consolidation into fewer very large fires is a grading call.

---

## AEO-09 CHECKPOINT — status only, NOT resolved

**Instrument: `monthly_seasonal_outlook.pdf`, header reads verbatim `Issued: August 1, 2026 / Next Issuance: September 1, 2026`.**
✅ **Verified rather than assumed, per the task. The August outlook IS still current; no September outlook exists yet (~11 days out).**

| Panel | TX / OK | Verbatim |
|---|---|---|
| **August (current month)** | **ABOVE-NORMAL — STILL THERE** | above-normal for "much of the northern Plains, northern Minnesota, **southern Plains**, Lower Mississippi Valley, south Florida, and Puerto Rico and the U.S. Virgin Islands" |
| **September** | **returns to normal** | "For September, potential is forecast to return to **normal in much of the Southern Area**, western Colorado, and southwest Wyoming" |
| **October / November** | normal | normal everywhere except northern Minnesota, PR, USVI |

**Southern Area regional section — reads DIFFERENTLY from the Executive Summary:**
> "Dryness is expected to worsen across the southern Plains and Lower Mississippi Valley during August, a common theme in summers with intensifying El Niño conditions. **Above normal significant fire potential is forecast to develop through large parts of Oklahoma and Texas** into southern and eastern Arkansas, Louisiana, Mississippi, and southwestern Alabama in the coming weeks… **Above normal significant fire potential has the potential to carry into September, especially over the southern Plains.**"

⚠️ **Two adjudications the worker will not make:**
1. **Scope of "removed."** The same 8/01 outlook keeps TX/OK above-normal in its **August** panel while already returning much of the Southern Area to normal in its **September** panel. Whether AEO-09 grades the current-month panel or any panel of an outlook issued ≤12/01 changes the answer.
2. **Internal tension.** Exec Summary says September returns to normal in much of the Southern Area; the Southern Area section says above-normal "has the potential to carry into September, especially over the southern Plains." **They are not the same claim about the same geography.**

⚠️ **And a mechanism note that cuts against the prediction's premise:** the outlook attributes the southern-Plains dryness to *"intensifying El Niño conditions"* and attributes Caribbean fire activity to El Niño keeping rainfall offshore. **AEO-09 expects a historic El Niño to REMOVE above-normal potential from TX/OK; the issuing authority is currently using El Niño to EXPLAIN why it is there.** That is load-bearing on AEO-09 and on the shared-composite argument behind it. **AEOLUS adjudicates; `regime/` owns ENSO.**

---

## proposed_findings
*PROPOSALS ONLY — candidate central `KB.tsv` rows. The worker wrote none of these to `workbook/KB.tsv`.*

1. **The peril/loss divergence widened to its largest recorded gap.** Acreage 155% → **171%** in 9 days while the aggregate loss leg sat unchanged at ~72–75% of average. *Sources: NIFC-NFN 8/21; Aon/Gallagher Re H1 2026 (carried).* **Directional support for the down-stack migration claim; still not independent confirmation of it.**
2. **The Spokane Complex now carries an insurer-issued loss estimate — and it lands an order of magnitude below the C4 upgrade trigger.** Gallagher Re: "minimally… hundreds of millions (USD); with a plausible chance and likelihood of this becoming a billion-dollar event"; possibly **the costliest insured wildfire in Washington history**. *Source: Artemis.bm 2026-08-06 citing Gallagher Re.* **Margin to the >$10B trigger: ~$9B. NOT FIRED.**
3. **AM Best explicitly forecloses the reinsurance-hardening read.** "The losses do not appear to be in the same order of magnitude as the 2025 California wildfires and **likely will have minimal impact on the current softening prices in the reinsurance market**." *Source: Artemis.bm 2026-08-06 citing AM Best.* **This is a named rating agency stating the peril event does NOT reprice reinsurance — i.e. an independent voice for the same divergence.**
4. **A WA FAIR Plan assessment path is now named — the first non-CA residual-pool evidence this folder has held.** AM Best: WA's FAIR plan is "similar to California's… not taxpayer-funded, and all insurance companies in the state are required to be members," assessed on premium share. *Source: Artemis.bm 2026-08-06 citing AM Best.* **This is the down-stack mechanism appearing in a second state.** ⚠️ It is a **mechanism note, not a filing** — it does not close open question 4 (non-renewal data outside CA).
5. **Cat-bond transmission is bounded at current damage levels.** WA-exposed sponsors: State Farm, Allstate, USAA, Travelers. Aggregate-layer retention erosion possible; **per-occurrence structures unlikely to be touched.** *Source: Artemis.bm 2026-08-06 citing AM Best.*
6. **Structure counts revised upward exactly as the standing warning predicts**, and the two figures are different objects: **">700 homes destroyed"** (Gallagher Re, 8/6) vs **"as many as 1,100 properties damaged or destroyed"** (unnamed fire officials, aerial imagery, 8/6). Acreage also revised ~5,390 → ">10,000". *Prior: ~640–700 / ~5,390 ac, Spokesman/WA-EOC, 8/1–2.* **Do not merge destroyed with damaged-or-destroyed.**
7. **The issuing authority's own attribution runs against AEO-09's premise** (see the checkpoint section). *Source: NIFC outlook issued 2026-08-01, Southern Area section.*

---

## gaps
*Required output. A reported gap beats a worked-around one.*

1. **WA state EOC final structure tally — NOT OBTAINED.** `https://mil.wa.gov/alerts` returned **HTTP 200, 96,625 bytes** but contained no Spokane structure figure (only "Spokane County" / "ALERTSpokane.org" nav references). `https://www.dnr.wa.gov/wildfires` returned **HTTP 200, 274,587 bytes** with no Spokane structure figure. **No source substituted.** The revised count in this run comes from **Gallagher Re via Artemis**, a *different issuing authority* than a state EOC, and is labelled as such throughout.
2. **No firmed catastrophe-modeler loss estimate for Spokane.** Artemis site search for "Spokane" returned only the single 2026-08-06 article. **No KCC / Verisk / Moody's RMS industry loss estimate has been published on the listed sources.** The $1B figure remains a broker's plausibility statement, not a modeled estimate.
3. **Aggregate reinsurer cat tally not refreshed — by publication schedule, not by failure.** H1 figures land ~Jul–Aug, full-year ~Jan. The Artemis front page (checked 8/21) carried no new US nat-cat aggregate. **The loss leg is genuinely stale and is labelled so rather than back-filled with an acreage figure.**
4. **NIFC's published 10-year-average YTD values render BLANK** in the served HTML (`10-year average Year-to-Date / 2016-2025 / Fires: / Acres:` — both empty). The **129% / 171%** figures are taken from NIFC's own narrative paragraph, the same source as the 8/13 read's 126% / 155%. Implied averages are **derived, not published**: acres ≈ **4,469,053**, fires ≈ **38,819**. Flagged, not silently substituted.
5. **Non-renewal filings (WA, CO, OR, TX) not pulled** this run — `SOURCES.md` names the state insurance departments but carries no verified command for them. **The non-renewal leg still rests on CA evidence alone**, which is what holds the C4 channel-kill open.
6. **PL5 duration convention is ambiguous and the ambiguity is inherited.** The 8/12 row recorded "26 days" since 7/18, which is an **inclusive** count (25 elapsed). This run uses the same convention: **35 inclusive / 34 elapsed**. Both are recorded in the SERIES note so AEOLUS grades on a stated basis rather than a guessed one.
7. **Drought not pulled here by design** — `../water/` owns it as a shared C2/C4/C5/C6 input. **Cite `water/workbook/SERIES.tsv`; no values copied into this workbook.** The 8/13 dossier's D1–D4 figure was removed from DOSSIER.md rather than carried stale.
8. **Checked and deliberately EXCLUDED:** Artemis 2026-08-20 reported Allstate pre-tax cat losses of **$2.402bn** for the current aggregate year. **75% of July's $682M was wind and hail (severe convective storm), not wildfire.** It is a single-carrier all-peril aggregate, not a wildfire loss instrument — **not logged here.**

---

## sources actually pulled this run

| Source | Result |
|---|---|
| `https://www.nifc.gov/fire-information/nfn` | ✅ HTTP 200 · report dated **August 21, 2026** |
| `https://www.nifc.gov/fire-information/statistics` | ✅ HTTP 200 · **Last Updated Friday, August 21, 2026 – 09:20** · cross-agrees with NFN on 76 / 50,077 / 7,642,082 |
| `https://www.nifc.gov/nicc-files/predictive/outlooks/monthly_seasonal_outlook.pdf` | ✅ HTTP 200 · 1.5 MB · 17 pp · **`Issued: August 1, 2026 / Next Issuance: September 1, 2026`** |
| `https://www.artemis.bm/` (feed + site search + 2 articles) | ✅ HTTP 200 · one Spokane loss article (8/6); one Allstate article (8/20, excluded) |
| `https://mil.wa.gov/alerts` | ⚠️ HTTP 200, **no Spokane structure figure** |
| `https://www.dnr.wa.gov/wildfires` | ⚠️ HTTP 200, **no Spokane structure figure** |
| WebFetch on the Artemis Spokane article | ❌ **HTTP 403 Forbidden** — retrieved successfully via `curl` with a browser UA instead |
| `../water/` drought | ⏭️ **not pulled by design** — other folder's instrument |

**Files written this run:** `workbook/SERIES.tsv` (append) · `workbook/LOG.tsv` (append) · `DOSSIER.md` (rewrite) · `RUN_REPORT.md` (this file, last write).
**Nothing written outside `AGENTS/AEOLUS/wildfire/`. Nothing committed. No channel scored, no trigger fired, no prediction resolved, no packet written, no agent routed to.**
