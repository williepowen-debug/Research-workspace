# AEOLUS · WILDFIRE — RUN REPORT

**run_date: 2026-10-09** (Friday; first written after a `date` read of 20:42:47 EDT, corrected after a 20:43:25 read) · covers 9/28 → 10/09 · **the October NIFC outlook is read**
**This is a worker run, and nothing in it is graded.** AEOLUS scores C4, fires triggers and resolves AEO-09. P1–P14 from earlier runs are still open. This run adds P15–P19.

---

## observations_added

**9 rows to `workbook/SERIES.tsv`** (now 39 lines including the header, 7 fields each, LF only) and **6 rows to `workbook/LOG.tsv`** (now 39 lines including the header, 6 fields each, LF only). Every `pulled_at` is `2026-10-09`. `DOSSIER.md` has a new two-clock header (`Last real data refresh: 2026-10-09`), a new "2026-10-09 WORKER REFRESH" block, corrected §1/§3/§4 lines, and a superseded-pointer on §5. **I machine-checked 52 quoted fragments against the fetched source text: 24 in the LOG rows, 14 in the SERIES rows and 14 in the DOSSIER block. 49 match literally.** The other 3 are not source quotes: one is a header assembled from three separate PDF lines with " / ", one is my own routing label, and one is a prior-record Hydra quote labelled as such. **I also caught and fixed one arithmetic error in my own uncommitted row:** 9/30 vs 9/25 acres is +45,004. I first wrote +44,999.

| instrument | value | data date | source | Δ |
|---|---|---|---|---|
| `nifc_preparedness_level` | **4** | **9/04** | NIFC-outlook | **new step**: PL went 5→4 on 9/4, 3 on 9/9, 2 on 9/22 |
| `nifc_acres_ytd` / `fires_ytd` / `pct` | 8,604,892 / 62,369 / **141%** | 9/30 | NIFC-outlook | fires **+5,030** vs statistics 9/28 |
| `nifc_preparedness_level` | **2** ("as of September 22") | 10/09 | NIFC-NFN | unchanged; 18 days inclusive |
| `nifc_acres_ytd` | **9,013,486** | 10/09 | NIFC-NFN = statistics | **+450,199** vs 9/28; **+408,594 after 9/30** |
| `nifc_fires_ytd` | **63,681** (134%) | 10/09 | NIFC-NFN = statistics | +6,342 vs 9/28 |
| `nifc_acres_pct_10yr_avg` | **145** | 10/09 | NIFC-NFN | reproduces: 9,013,486 / 6,204,304 = 145.28% |
| `nifc_large_fires_uncontained` | **8** | 10/09 | all 3 surfaces agree | 9/25–9/28: 26 / 4 / 17 |
| personnel (not in the vocabulary) | **3,123** | 10/09 | NFN = statistics | 5,697 (9/28) |

⚠️ The source label `NIFC-outlook` is not in the AGENT.md vocabulary, which lists only `NIFC-NFN`. If AEOLUS rejects it, only the 4 outlook-dated rows are affected.

## threshold_state

*Values and margins only. Nothing here is a grade.*

| Line | Value | Margin | State |
|---|---|---|---|
| PL5 = C4 peril leg at maximum | PL **2** | 3 levels below | NOT-FIRED |
| **AEO-09 removal** (TX/OK no longer NAMED above-normal in the **current-month regional section**, KB-AEO-128) | **Oct 1 issue, October panel: TX NAMED, OK NAMED, both partial.** Map, Exec Summary and Southern Area all agree | removal condition **not met on this issue** | **AEOLUS grades.** Note the regional sentence says *"most likely"* |
| Reinsurer cat-loss ≥110/130/150% | ~72% (H1 2026; window closed 6/30) | ~38 pts below Yellow | NOT-FIRED (blind to the season) |
| C4 upgrade: >$10B single cat OR insolvency | Spokane $1.0–1.3B (Cotality 8/18; **not re-checked this run**) | ~$8.7–9B short | NOT-FIRED |
| Channel-kill conjunction | loss leg ~72%; non-renewal leg cannot be evaluated | — | NOT-FIRED |

🔴 **145% is an ACREAGE percentage. The cat-loss band reads ~72%. They are different instruments.**

## changes

1. **October outlook issued 10/01** (Last-Modified 2026-10-01 18:02:47 GMT; next issue **11/02**).
   - **Southern Area, verbatim:** *"For October, above normal significant fire potential is most likely across western north Texas into western Oklahoma, in addition to east Texas and the Lower Mississippi Valley."*
   - **Map (Oct):** western OK only (Panhandle and central/eastern OK white). TX in two blocks, **western north TX** and **east TX**. **The TX Panhandle is white.**
   - **Nov:** E OK + NE TX above. **Dec and Jan:** normal.
   - **Geography contracted vs September**, when all of OK and two-thirds of TX were red.
2. **Other October above-normal areas:** Great Basin **Sierra Front / Lahontan Basin**; NE MN, N WI, W Upper MI; east TX → Lower Mississippi Valley; PR/USVI.
3. **PL history:** **the PL5 run was 49 days inclusive (7/18→9/4), not 54.**
4. **YTD step at PL2:** +~5k fires by 9/30, then +~409k acres after 9/30. The 141% → 145% rebound comes from that step, not from new burning that any surface reports.
5. **10-yr averages render again.** Published 47,686 fires / 6,204,304 ac. Both narrative percentages reproduce.
6. **Incidents since 9/28 (InciWeb set):** Bouquet CA (10/03, 1,048 ac, Level-3 evacuation order), Danny CA (10/08, 150 ac, evacuation order + warnings), Bull NV (10/02, 1,529 ac, warnings lifted). **No structure loss is published for any of them. No TX/OK incident appears on InciWeb.**

## proposed_findings *(proposals only; AEOLUS adjudicates)*

- **P15.** The PL step dates come from the 10/01 outlook Exec Summary. Correct any **"54-day PL5"** citation to **49 days inclusive**. `SOURCES.md:131` carries it, and I did not edit that file because it is outside my write list.
- **P16.** AEO-09 inputs for the 10/01 checkpoint are as above, and the October panel has no map/text conflict. Open sub-question: is *"most likely"* a hedge under KB-AEO-128 rule (2)? The map and Exec Summary carry no hedge.
- **P17.** **The Exec Summary is an incomplete designation surface.** It omitted the Great Basin above-normal area that the regional section and the map both show. That is independent support for "regional governs".
- **P18.** **Do not read the 9/30→10/09 acreage rebound as renewed activity.** The step is unexplained. My hypothesis, with no evidence, is a reporting reconciliation.
- **P19.** NIFC's published 10-yr average (6,204,304) is **not** the simple mean of its own year rows (6,209,060.8). Reproduce percentages only from the published field when it renders.

## gaps

| # | Item | Exact result |
|---|---|---|
| 1 | `pdfimages -f 1 -l 1 -png outlook.pdf panel` | `/bin/bash: line 1: pdfimages: command not found` rc=127. **Disclosed method deviation:** I read the panels from a **pypdfium2** render of the same PDF. It is a visual read, and sub-state lines are approximate. The governing text needs no image. |
| 2 | CAL FIRE incidents | `HTTP=403 SIZE=382` "Access Denied", Reference #18.b59a2d17.1791592534.181a83ef |
| 3 | TX/OK incident-level losses | InciWeb lists **no** Southern Area incidents. TX A&M Forest Service is not a SOURCES.md source, so I did not use it. The Hydra page returns HTTP 200 with an empty template. Its structure loss is still unpublished on InciWeb. |
| 4 | Q3 2026 insured-cat tally | Not on the Artemis homepage (fetched 10/09); the only Q3 item there is cat-bond issuance. The insured-losses tag page leads with a 2023-loss sigma piece (recency trap), so I did not read it as a negative. |
| 5 | Not attempted | Cotality re-check, WA EOC final tally, non-renewal data outside CA |
| 6 | Drought | Cited, not pulled: `water/` USDM CONUS D1–D4 **59.24%**, mapDate 2026-09-22 |
| 7 | Out of scope, noted only | **Hurricane Isaias** is approaching the Gulf (NFN 10/09; Artemis: "single-digit billion insured losses still likely"). That belongs to `hurricane/`/C1. NFN also flags a critical burn environment in the Lower Mississippi Valley ahead of it. |
