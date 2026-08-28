# AEOLUS · WILDFIRE — RUN REPORT

**run_date: 2026-08-27** · worker run · data date **2026-08-27** (NIFC NFN "Last Updated: August 27, 2026")
*Overwrites the previous run. Prior run: 2026-08-21.*

---

## observations_added

**5 rows → `workbook/SERIES.tsv`** · **4 rows → `workbook/LOG.tsv`** (9 total)

SERIES (all `date=2026-08-27`, `source=NIFC-NFN`):
`nifc_preparedness_level=5` · `nifc_acres_ytd=7971399` · `nifc_fires_ytd=51434` · `nifc_acres_pct_10yr_avg=164` · `nifc_large_fires_uncontained=94`

LOG: `nifc_refresh` (8/27) · `nifc_outlook_still_august` (8/27) · `spokane_loss_estimate_no_update` (8/27) · `nonrenewal_gap_partially_closed` (8/27)

**No `h1_us_insured_natcat` row appended** — no new aggregate publication since the H1 print; appending an unchanged row would fake a refresh.
**No new instrument invented.** The non-renewal-rate finding (§ below) has no entry in the controlled vocabulary, so it went to `LOG.tsv` as a sourced event and is raised as a proposed finding for AEOLUS to adjudicate and, if wanted, formally add to the vocabulary.

---

## threshold_state
*Values and margins only. The worker does not grade, score, fire or resolve.*

| Instrument | Value (as-of) | Band | Margin | State |
|---|---|---|---|---|
| **NIFC Preparedness Level** | **5 of 5**, since **2026-07-18 07:30 MDT** = **41 days inclusive / 40 elapsed** (8/27) | max tier | at ceiling | **AT MAX, entire season to date** |
| **`nifc_acres_pct_10yr_avg`** ⚠️ ACREAGE | **164%** (8/27) — 7,971,399 ac | *no acreage band exists* | — | ⚠️ **NOT a threshold instrument.** Pct FELL from 171% while absolute acres ROSE — denominator-growth effect, not deceleration (see changes). |
| **`nifc_fires_ytd`** | **51,434 = 127%** (8/27) | *no band* | — | same denominator-growth effect |
| **`nifc_large_fires_uncontained`** | **94** (8/27) | *no band* | — | 🔴 **worsened +18 from 76 — reverses the 8/21 improvement** |
| **Reinsurer cat-loss tally vs 10-yr avg** ⚠️ THE LOSS INSTRUMENT | **~72–75%** (H1 2026, unchanged since 8/13; corroborated by an independent republication this run) | Y ≥110 · O ≥130 · **R ≥150** | **~35 pts below YELLOW; ~75 pts below RED** | **NOT FIRED — still pointing the opposite way** |
| **C4 upgrade 3→4: single insured cat >$10B** | Spokane, Gallagher Re 8/6 (unrevised): "hundreds of millions", plausible **~$1B** high case | >$10B | **~$9B short** | **NOT FIRED** |
| **C4 upgrade 3→4: carrier insolvency** | none reported | any | — | **NOT FIRED** |
| **C4 channel-kill (conjunction)** | leg 1 (H1 cat <110%): satisfied ~72–75%. leg 2 (non-renewals stable 2+ qtrs): **now has a national/regional rate instrument, but its newest observation is 2022** | both required | second leg's evidentiary currency is AEOLUS's call | **NOT FIRED** |
| **Property insurance non-renewal rate** | **NEW — national 1.04%, SW region 1.28%, NW region 0.67%, all 2018-2022 avg (FIO/NAIC)** | Y +10%YoY · O +25% · R +40%/exit | *no YoY series exists yet to grade against a % change band — this is a level, not yet a trend* | **band not gradable from this cut; see §non-renewal below** |

🔴 **THE CENTRAL DISCIPLINE, RESTATED.**
**164% is an ACREAGE percentage. The RED band is a CAT-LOSS percentage, currently ~72–75%.** Different rows of the threshold table, different units, different publishers. The peril leg's acreage % actually **eased** this run (171%→164%) while the large-fire count **worsened** (76→94) — the two peril sub-instruments moved in **opposite directions from each other**, on top of the peril/loss divergence that was already the standing finding. **Read no single figure as summarizing "the fire season" — three separate instruments (acreage %, large-fire count, loss %) each say something different this run.**

---

## changes
*since the 2026-08-21 read*

| Item | 8/21 | **8/27** | Δ |
|---|---|---|---|
| Preparedness Level | 5, 35 days inclusive | **5, 41 days inclusive** | **+6 days at max tier** |
| Acres YTD | 7,642,082 = **171%** | **7,971,399 = 164%** | **+329,317 ac, but −7 pts** — the to-date 10-yr-avg denominator grew faster than the numerator (implied avg 8/21 ≈4.47M → 8/27 ≈4.86M ac) |
| Fires YTD | 50,077 = **129%** | **51,434 = 127%** | +1,357 · −2 pts, same denominator effect |
| Uncontained large fires | **76** | **94** | 🔴 **+18 — reverses the 8/21 improvement**; 7 new large fires reported 8/26, 1 contained |
| Personnel assigned | 24,265 | **21,854** | **−2,411** despite MORE large fires — AEOLUS's call whether this is demobilization or reallocation |
| Aug outlook | issued 8/01 | **still 8/01 — re-verified via direct PDF text extraction, next issuance 9/01 (~5 days out)** | unchanged, confirmed not assumed |
| Spokane insured loss | hundreds of $M → plausibly $1B (Gallagher Re, 8/6) | **UNCHANGED — checked, no newer estimate found** | no move |
| Aggregate cat losses | ~$36B US / ~$47B global, 25–28% below avg | **UNCHANGED — one independent corroborating republication found ($46bn global H1, 28% below avg), no new post-H1 print** | no move |
| Non-renewal rate | no metric surface existed | **NEW: national + SW + NW regional rates sourced (FIO/NAIC, 2018-2022 vintage)** | gap partially closed — see below |

**Shape of the move:** the acreage-% deceleration is **not a real slowdown signal** — it is a seasonally-accreting comparator effect (the "10-yr average" is itself a to-date cumulative figure that grows through the season, so a percentage can fall even as the raw acreage keeps climbing). The more informative move this run is the **large-fire count reversing from improvement (−25) to deterioration (+18)** on the same underlying NIFC field, alongside a **personnel drawdown** in the opposite direction. Geographic lead: Oregon and Washington now tied at 16 large fires each, Montana at 12 — full 10-area breakdown was not re-pulled this run (only the page's own narrative on leaders and new fires).

---

## AEO-09 CHECKPOINT — status only, NOT resolved

**Instrument: `monthly_seasonal_outlook.pdf`, re-fetched and text-extracted directly (pdfminer) 8/27. Header reads verbatim `Issued: August 1, 2026 / Next Issuance: September 1, 2026`.**
✅ **Re-verified, not assumed. Still the August outlook; no September outlook exists yet (~5 days out).** The Executive Summary text is unchanged from the 8/21 read (it cites a static "as of July 31" figure baked into the Aug-1 document — 165%/128% — which is a different, frozen number from the live NFN page's rolling 164%/127%; do not conflate the two).

No new adjudication inputs beyond what the 8/21 report already flagged (scope-of-"removed" ambiguity; Exec Summary vs. Southern Area tension; El Niño cited as the mechanism FOR the above-normal TX/OK potential that AEO-09 expects El Niño to remove). Unrefreshed this run — `regime/` owns ENSO state.

---

## proposed_findings
*PROPOSALS ONLY — candidate central `KB.tsv` rows. The worker wrote none of these to `workbook/KB.tsv`.*

1. **The large-fire-count improvement reported on 8/21 reversed.** Uncontained large fires rose from 76 to 94 (+18, +24%) in 6 days, with personnel assigned falling 2,411 over the same window. *Source: NIFC-NFN 8/27.* **Whether this is genuine deterioration or a reporting-field artifact (e.g. reclassification) is AEOLUS's call — the field label and source are identical across both reads, so it reads as a real move.**
2. **The acreage-percentage "improvement" (171%→164%) is very likely a comparator-denominator artifact, not a deceleration.** Absolute acres still rose +329,317 in 6 days; the implied 10-yr-average denominator itself grew ~9% over the same window (4.47M→4.86M ac), consistent with a cumulative to-date average that mechanically rises through the season. **Recommend AEOLUS treat the acreage % as directionally noisy near mid-late season and weight the raw acreage delta and the large-fire count more heavily.**
3. **The Spokane/aggregate loss leg is confirmed stable, not merely unrefreshed.** An independent republication of the Gallagher Re H1 global figure ($46bn/28% below avg) corroborates the dossier's carried $47B/~$36B figures via a different outlet, and a direct Artemis re-check found no new Spokane article since 8/6. *Sources: Artemis.bm (checked, none new) + Reinsurance News/Business Insurance republication.* **This strengthens confidence that the loss leg is genuinely flat, not just stale-by-schedule.**
4. **🔑 A national + regional non-renewal-rate instrument now exists, partially closing the standing channel-kill gap.** US Treasury FIO / NAIC PCMI Data Call: national avg 2018-2022 = **1.04%**, rising to 1.20% by 2022; national Highest-Risk climate quintile **1.61%** (more than doubled 2018→2022, 1.10%→2.37%); Southwest region (CA-dominant) **1.28%** (+23.5% vs national); Northwest region (WA/OR-dominant) **0.67%** (−35% vs national). *Source: home.treasury.gov FIO report, Jan 2025, verified pull command in `SOURCES.md`.* **Load-bearing caveat: the data ends in 2022 and cannot speak to 2023-2026 — AEOLUS must decide whether this closes only the definitional gap (what instrument exists) or also the evidentiary one (what it currently reads).**
5. **Tension worth flagging, not resolving: the Northwest's 2018-2022 non-renewal baseline (0.67%, below national) sits under the region carrying 2026's heaviest live peril load (OR/WA tied at 16 large fires).** The dataset predates the current season by construction; this is a reason to seek a fresher NW-specific cut, not evidence the peril/insurance link is weak there.

---

## gaps
*Required output. A reported gap beats a worked-around one.*

1. **No newer Spokane insured-loss estimate — checked, not found.** Artemis.bm wildfire-tag feed and a targeted site search for "Spokane wildfire" both returned only the 2026-08-06 article. No KCC/Verisk/Moody's RMS modeled figure located.
2. **WA state EOC final structure tally — not re-attempted this run** (checked 8/21, negative; not re-pulled 8/27 given no indication of a pending update).
3. **CA DOI wildfire-insurance page failed: `https://www.insurance.ca.gov/01-consumers/140-catastrophes/WildfireInsuranceInformation.cfm` → HTTP 404.**
4. **CA FAIR Plan policy-in-force page failed: `https://www.cfpnet.com/about-us/newsroom/policy-in-force-data/` → HTTP 404.** No source substituted; a CA FAIR-Plan policy-count-growth figure surfaced via general web search only (not a direct primary fetch with a reproducible command) and was **deliberately not logged as fact** — reported here as an unclosed lead instead.
5. **Non-renewal rate — CLOSED at the national/regional/2018-2022 level, STILL OPEN at the state-specific/current level.** No WA-state-specific cut exists in the FIO source (WA is bundled into "Northwest" with OR/ID/MT/WY/AK). No 2023-2026 observation exists in any source found this run. Texas is excluded from the FIO nonrenewal calculation entirely (insurer data gap, per the report's own footnote).
6. **Geographic 10-area large-fire breakdown not re-pulled** — only the page's stated leaders (OR 16, WA 16, MT 12) and new-fire narrative were captured this run, not the full state-by-state table carried in the 8/21 dossier.
7. **Drought not pulled here by design** — `../water/` owns it as a shared C2/C4/C5/C6 input. No values copied into this workbook.
8. **10-year-average YTD fields still render BLANK** on the NIFC page (confirmed again 8/27, unchanged from 8/21). Percentages taken from NIFC's narrative paragraph; implied averages remain derived, not published.

---

## sources actually pulled this run

| Source | Result |
|---|---|
| `https://www.nifc.gov/fire-information/nfn` | ✅ fetched · report dated **August 27, 2026**, "Last Updated: August 27, 2026" |
| `https://www.nifc.gov/nicc-files/predictive/outlooks/monthly_seasonal_outlook.pdf` | ✅ fetched (60MB timeout on WebFetch's markdown pass; recovered via direct download + pdfminer.six text extraction) · confirmed **`Issued: August 1, 2026 / Next Issuance: September 1, 2026`** |
| `https://www.artemis.bm/news/tag/wildfire/` + site search | ✅ fetched · no Spokane article newer than 8/6 |
| WebSearch: Gallagher Re/Aon/Munich Re Aug 2026 natcat update | ✅ returned H1 global corroboration ($46bn/28% below avg) + Midwest derecho note (different peril, excluded) |
| `https://home.treasury.gov/system/files/311/Analyses_of_US_Homeowners_Insurance_Markets_2018-2022_Climate-Related_Risks_and_Other_Factors_0.pdf` | ✅ fetched directly (curl + pdfminer.six, ~3.4MB) · **exact command now in `SOURCES.md`** · national/regional nonrenewal rates extracted |
| `https://www.insurance.ca.gov/01-consumers/140-catastrophes/WildfireInsuranceInformation.cfm` | ❌ **HTTP 404** |
| `https://www.cfpnet.com/about-us/newsroom/policy-in-force-data/` | ❌ **HTTP 404** |
| `https://www.fio.treasury.gov/reports/...` | ❌ **DNS resolution failure (`getaddrinfo ENOTFOUND`)** — wrong host; the correct host is `home.treasury.gov` (used above) |
| `../water/` drought | ⏭️ **not pulled by design** — other folder's instrument |

**Files written this run:** `workbook/SERIES.tsv` (append) · `workbook/LOG.tsv` (append) · `SOURCES.md` (edit — added the FIO non-renewal command + NIFC 8/27 verification note) · `DOSSIER.md` (edit — refreshed peril/loss sections, added new §6 non-renewal finding) · `RUN_REPORT.md` (this file, last write).
**Nothing written outside `AGENTS/AEOLUS/wildfire/`. Nothing committed. No channel scored, no trigger fired, no prediction resolved, no packet written, no agent routed to.**
