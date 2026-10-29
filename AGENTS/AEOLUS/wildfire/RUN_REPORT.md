# AEOLUS · WILDFIRE — RUN REPORT

**run_date: 2026-10-29** (Thursday). The report was stamped after a `date` read of 07:45:29 EDT. The run started at 00:27 EDT, and the wall clock jumped from 00:28 to 07:43 between tool calls. All `pulled_at` stamps were written by `date` in the same command that wrote them (07:44 -0400). The run covers 10/09 → 10/29.
**This is a worker run, and nothing in it is graded.** AEOLUS scores C4, fires triggers and resolves AEO-09. P1–P19 from earlier runs are still open. This run adds P20–P25.

---

## observations_added

**8 rows to `workbook/SERIES.tsv`** (now 47 lines including the header, 7 fields each, LF) and **6 rows to `workbook/LOG.tsv`** (now 47 lines, 6 fields each, LF). `DOSSIER.md` has a new two-clock header (`Last real data refresh: 2026-10-28`), a new "2026-10-29 WORKER REFRESH" block and updated open questions. **16 quoted fragments were machine-checked against the fetched NFN, outlook and Artemis text, and all 16 match.**

| instrument | value | data date | source |
|---|---|---|---|
| `nifc_preparedness_level` | **1** ("as of October 14, 2026 at 7:30 a.m. MDT") | 10/23 report | NIFC-NFN |
| `nifc_acres_ytd` | **9,048,486** | 10/23 | NIFC-NFN |
| `nifc_fires_ytd` | **65,796** | 10/23 | NIFC-NFN |
| `nifc_acres_pct_10yr_avg` | **141** (reproduces: 9,048,486 / 6,403,216 = 141.31%) | 10/23 | NIFC-NFN |
| `nifc_large_fires_uncontained` | **10** | 10/23 | NIFC-NFN |
| `nifc_acres_ytd` | **9,061,386** | 10/28 10:32 | NIFC-statistics |
| `nifc_fires_ytd` | **66,721** | 10/28 | NIFC-statistics |
| `nifc_large_fires_uncontained` | **10** | 10/28 | NIFC-statistics |

LOG rows: PL 2→1 step (10/14) · SoCal Santa Ana event (10/15–18) · Gallagher Re 9M'26 tally (10/21) · NFN Texas narrative/table mismatch (10/23) · November outlook not yet issued (10/29) · Spokane final tally still absent (10/29).

## threshold_state

*Values and margins only. Nothing here is a grade.*

| Line | Value | Margin | State |
|---|---|---|---|
| PL5 = C4 peril leg at maximum | PL **1** (since 10/14) | 4 levels below | NOT-FIRED |
| **AEO-09 removal** (TX/OK no longer NAMED above-normal in the current-month regional section) | **The November issue is not posted.** The latest issue is still 10/01, where the October panel NAMES both TX and OK (partial) | not testable until the 11/02 issue | **AEOLUS grades** |
| Reinsurer cat-loss ≥110/130/150% | **71.9%** (Gallagher Re 9M 2026, global, $92bn vs $128bn; SECONDARY via Artemis 10/21) | ~38 pts below Yellow | NOT-FIRED. It now covers the August peak; H1 was ~72% |
| C4 upgrade: >$10B single insured cat OR insolvency | Gallagher Re: *"six consecutive quarters without a single natural catastrophe event generating more than USD10 billion"* (through Q3). Spokane: Cotality $1.0–1.3B (8/18). Norte: no loss estimate | Spokane ~$8.7–9B short | NOT-FIRED |
| Channel-kill conjunction | loss leg 71.9% (<110%); non-renewal leg cannot be evaluated | — | NOT-FIRED |

🔴 **141% is an ACREAGE percentage. The cat-loss band reads 71.9%. They are different instruments.**

## changes

1. **PL 2 → 1 on 10/14.** PL2 held 9/22→10/14, 23 days inclusive. Season path: PL5 7/18→9/4, PL4 9/4, PL3 9/9, PL2 9/22, PL1 10/14. NFN shows only the current level, so an excursion between 10/09 and 10/14 cannot be excluded.
2. **YTD:** acres 9,013,486 → **9,048,486** (+35,000, NFN to NFN) → 9,061,386 (statistics 10/28). Fires 63,681 → **65,796** (+2,115) → 66,721. **The acreage percentage fell from 145 to 141 because of the denominator.** The 10-yr average YTD rose +198,912 acres (6,204,304 → 6,403,216), while 2026 acres rose only +35,000. Fires: 134% → 132%.
3. **Large fires 8 → 10.** Personnel 3,123 → 1,614 (NFN 10/23) → 862 (statistics 10/28). NFN "all active" acres (46,932) and statistics "on Large Fires" acres (366,942) differ by definition again; on 10/09 they were equal.
4. **Loss leg moved off H1.** Gallagher Re Q3 report via Artemis 10/21: **$92bn global insured nat-cat over 9 months, 29% below the $128bn 10-yr average**, lowest 9M since 2019. US = 62% of the total; US severe convective storms ≥ $43bn. Hurricane Isaias (10/9) is excluded from the total, and Gallagher Re expects it to cost *"low to mid-single-digit billions"*. **The Artemis text gives no wildfire figure.**
5. **First Santa Ana wind event of the season, 10/15–10/18** (SECONDARY, found by search; the CAL FIRE primary returned 403). **Norte** (San Clemente/San Juan Capistrano, 10/16): 570 ac per CAL FIRE vs 465 per OCFA. ~6,000 homes and 16,000 residents were under evacuation orders. **6 homes** were burned or damaged (unnamed officials via Fox Weather; OCFA "at least six" via Al Jazeera). KTLA says 7, but only in a search snippet. These counts are provisional and come from different issuers. **Bryson** (Malibu) ~147 ac. **Henderson** (Camp Pendleton) 2,080 → ~3,160 ac. **Peak** (InciWeb, 43 ac). Gusts reached 50–70 mph. SCE cut power to ~100,000 customers. **Cotality (10/19) gives only exposure: ~$4.5B reconstruction cost value at risk across ~4,690 high-score homes. That is not an insured-loss estimate.**
6. **Texas:** the NFN 10/23 narrative names the Kickapoo Creek Fire (*"threatening structures"*), but the NFN state table lists no Texas fire. OK has 1 (East Bailey Road, 104 ac). No other new West incident originated 10/09–10/29 on InciWeb. Every other 10/09+ wildfire update is a continuing fire.
7. **AEO-09 checkpoint input: the November outlook is NOT out.** The stable URL still serves the 10/01 issue: Last-Modified `Thu, 01 Oct 2026 18:02:47 GMT`, *"Next Issuance: November 2, 2026"*. **11/01 is a Sunday, so the issue is due Mon 11/02.** **URL to read:** `https://www.nifc.gov/nicc-files/predictive/outlooks/monthly_seasonal_outlook.pdf`. Check that Last-Modified has moved off 10/01 before citing it. TX/OK wording in the latest (10/01) issue, re-verified verbatim on 10/29:
   - **October (current month at issue).** Southern Area: *"For October, above normal significant fire potential is most likely across western north Texas into western Oklahoma, in addition to east Texas and the Lower Mississippi Valley."* Exec Summary: *"October significant fire potential will remain above normal in portions of north Texas and western Oklahoma. Above normal potential is also forecast for much of east Texas into the Lower Mississippi Valley…"*
   - **November (forecast).** Southern Area: *"Above normal significant fire potential in November is expected from eastern Oklahoma into northeast Texas, Arkansas, north Mississippi, west and middle Tennessee, and Kentucky."* Exec Summary: *"…normal for most of the country except for portions of east Texas and eastern Oklahoma eastward into most of Kentucky and Tennessee…"* ⚠️ The two surfaces word the Texas part differently (NE TX vs E TX).
   - **December.** Southern Area: *"Conditions by December into January will trend towards normal, though below normal significant fire potential is possible in some of the areas that can see dormant season fires in the Plains…"* Exec Summary: *"Significant fire potential will be normal for the contiguous U.S. and Alaska for December…"*
   - **January.** Southern Area: the same sentence as December. Exec Summary: *"Normal significant fire potential is forecast across the country for January."*

## proposed_findings *(proposals only; AEOLUS adjudicates)*

- **P20.** **The loss-leg vintage is now 9M 2026 (Gallagher Re, 71.9% of the 10-yr avg).** This is the first vintage that covers the PL5 run and Spokane, and it reads the same as H1 (~72%). Under the 9/18 "loss leg is blind" note, it is no longer blind to the season. Tier: SECONDARY (Artemis 10/21). The primary report was not opened. Source: `https://www.artemis.bm/news/gallagher-re-estimates-global-insured-cat-losses-at-92bn-for-9m26-lowest-since-2019/`.
- **P21.** **Instrument gap:** the SERIES vocabulary has only `h1_us_insured_natcat`. The 9M figure is global and not H1, so I wrote no SERIES row. AEOLUS may want a `ytd_global_insured_natcat_pct_10yr` (or similar) instrument. I did not invent one.
- **P22.** **Gallagher Re's "six consecutive quarters" with no single event >$10B insured** (through Q3 2026) is direct issuer evidence on the C4 upgrade leg's single-event clause. It does not cover Q4. Isaias is guided at low-to-mid single-digit billions.
- **P23.** **The NFN acreage percentage falls in late season because of the denominator.** 145 → 141 came from the 10-yr average rising +198,912 ac while 2026 rose +35,000. A falling percentage is not a reversal of 2026 acreage. Read the absolute pair.
- **P24.** **Cotality publishes exposure (RCV at risk) pages that look like loss pages.** The Norte page's $4.5B is reconstruction cost value across high-score homes in three ZIPs, with about 6 homes actually lost. It must never enter the event-level loss slot. Source: `https://www.cotality.com/hazard-hq/norte-fire-burns-homes-in-south-orange-county` (10/19).
- **P25.** **The NFN narrative and table can disagree on state presence.** On 10/23 the narrative named a Texas fire threatening structures, and the table had no Texas row. That matters for TX/OK peril reads.

## gaps

| # | Item | Exact result |
|---|---|---|
| 1 | CAL FIRE incidents `https://www.fire.ca.gov/incidents` | `HTTP=403 SIZE=380` "Access Denied", Reference #18.7fcda17.1793268222.227910b0. The Santa Ana event figures are therefore SECONDARY (Fox Weather, Al Jazeera, Cotality, found by WebSearch). |
| 2 | November outlook | Not yet issued. HTTP 200, but the content is the 10/01 issue (Last-Modified Thu, 01 Oct 2026 18:02:47 GMT). Due 11/02. |
| 3 | Monthly-outlook map panels | Not re-read. There is no new issue, and the October panels were read 10/09 via pypdfium2 (`pdfimages` is not installed). |
| 4 | Gallagher Re primary report | Not opened; the Artemis summary was used. |
| 5 | Wildfire-specific insured loss for Norte, Bryson or Henderson | None in the WebSearch result set (query naming Verisk/Cotality/KCC, searched 10/29). |
| 6 | Spokane WA EOC final tally | None in the WebSearch result set searched 10/29; its newest items are ~9/01. ZestyAI "833 homes" and Fox13 "~900 structures" appear only in snippets. Those pages were not opened, and the figures were not logged as values. |
| 7 | Kickapoo Creek TX size and structures | Not on any SOURCES.md surface (TX A&M Forest Service is not a listed source). Search trackers say 200–300 ac; unverified and not used. |
| 8 | Non-renewal data outside CA, and NAIC zone membership | Not attempted this run. |
| 9 | PL step history 10/09→10/14 | The NFN surface gives only the current level. Read the 11/02 outlook Exec Summary. |
| 10 | Drought | Cited, not pulled: the newest `water/` USDM row is mapDate 2026-10-20 (CONUS D1–D4 50.67%). That file has uncommitted changes in git. |
| 11 | Out of scope, noted only | SCE de-energized ~100,000 customers in the 10/15–18 event (utility ignition / power shutoffs → WATT). Isaias losses → `hurricane/` / C1. |

**Files changed:** `AGENTS/AEOLUS/wildfire/workbook/SERIES.tsv` (+8) · `AGENTS/AEOLUS/wildfire/workbook/LOG.tsv` (+6) · `AGENTS/AEOLUS/wildfire/DOSSIER.md` · `AGENTS/AEOLUS/wildfire/RUN_REPORT.md`. Nothing was staged or committed.
