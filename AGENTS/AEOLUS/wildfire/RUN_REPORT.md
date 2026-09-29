# AEOLUS · WILDFIRE — RUN REPORT

**run_date: 2026-09-28** (Monday; written 20:04 EDT) · covers the AEOLUS dark window 9/18 → 9/28
**This is a worker run and nothing in it is graded. AEOLUS scores C4, fires triggers and resolves AEO-09.** The 9/18 proposals P1–P10 are still open. This run adds evidence under P1, P3 and P7 and adds P11–P14.

---

## observations_added

**8 rows went to `workbook/SERIES.tsv`** (30 rows total, 7 fields on every row) and **8 rows to `workbook/LOG.tsv`** (33 rows total, 6 fields on every row). `DOSSIER.md` got a new two-clock header reading `Last real data refresh: 2026-09-28` and a "2026-09-28 WORKER REFRESH" block. The §3, §4 and §5 summary lines that were still carrying 9/18 figures were also updated. Every `pulled_at` value is `2026-09-28`, and `date` was run before each write.

| instrument | value | data date | source | Δ vs 9/18 |
|---|---|---|---|---|
| `nifc_preparedness_level` | **2** ("as of September 22, 2026 at 7:30 a.m. MDT") | 9/28 fetch | NIFC-NFN | 🔽 **3 → 2 on 9/22.** PL3 held from 9/9 to 9/22 (14 days counting both ends). |
| `nifc_acres_ytd` | **8,559,888** | 9/25 | NIFC-NFN | +36,675 |
| `nifc_fires_ytd` | **57,087** | 9/25 | NIFC-NFN | +798 |
| `nifc_acres_pct_10yr_avg` | **145** (from the narrative) | 9/25 | NIFC-NFN | 146 → 145. ⚠️ Cannot be reproduced (P12) |
| `nifc_large_fires_uncontained` | **26** (from the narrative) | 9/25 | NIFC-NFN | 50 → 26. ⚠️ **The basis changed** (P11) |
| `nifc_acres_ytd` | **8,563,287** | 9/28 07:55 | NIFC-statistics | +3,399 vs 9/25 |
| `nifc_fires_ytd` | **57,339** | 9/28 07:55 | NIFC-statistics | +252 vs 9/25 |
| `nifc_large_fires_uncontained` | **17** ("Being Suppressed") | 9/28 07:55 | NIFC-statistics | — |
| personnel (not in the vocabulary, so not in SERIES) | **6,824** (NFN, 9/25) · **5,697** (statistics page, 9/28) | — | — | 9/18: 12,315 |
| `h1_us_insured_natcat` | unchanged at ~$36B US / $46bn global, 28% below average | H1 2026 | — | **No new row. The data is now about 3 months old.** |

⚠️ **Source label:** the three 9/28 rows use `source = NIFC-statistics`, which is the SOURCES.md "NIFC statistics" page. The AGENT.md vocabulary lists only `NIFC-NFN`. AEOLUS may reject the label. If so, only these three rows are affected.

---

## threshold_state

*This section gives values and margins only. "NOT-FIRED" here describes the arithmetic. It is not a grade.*

| Band / trigger | Value | Margin | State |
|---|---|---|---|
| Reinsurer cat-loss tally ≥110/130/**150%** of the 10-yr average | **~72%** (H1 2026). The measurement window closed 6/30. | ~38 pts below Yellow, ~78 pts below Red | **NOT-FIRED.** The data covers a window that ended before the fire season. |
| C4 upgrade: carrier insolvency OR a single insured cat above **$10B** | Spokane: **$1.0–1.3B** (Cotality, estimate dated 8/18; page last updated 8/24; unchanged). No insolvency found. | ~$8.7–9.0B short | **NOT-FIRED** |
| C4 channel-kill: H1 cat below 110% AND non-renewals stable for 2+ quarters | Loss leg ~72% (meets it). Non-renewal leg cannot be evaluated because the series is annual and ends in 2024. | Leg 2 unevaluable | **NOT-FIRED** |
| Non-renewal rate +10/+25/+40% YoY | No new data. NAIC Western Zone 2024 = 25.1 per 1,000 is still the latest. | — | **Not gradeable** (the P4 blockers are unchanged) |

🔴 **145% is an acreage percentage. The cat-loss band reads ~72%.** Both legs are now low, but they are not converging. The peril leg is cooling. The loss leg is frozen on a window that ended before the fires started. **The first loss data that can cover this fire season is a Q3 tally, expected about mid-October.**

---

## changes

1. **The Preparedness Level fell from 3 to 2 on 9/22 at 07:30 MDT.** This is the only change the NFN page shows. It displays only the current level, so it cannot rule out a brief move away and back between 9/18 and 9/22.
2. **The peril leg kept cooling:**
   - acreage ratio 146% → 145%, and fire-count ratio 126% → 125%
   - personnel 12,315 → 6,824 (9/25) → 5,697 (9/28)
   - NFN "Acres from all active fires" 1,292,408 → 7,616
   - the NFN narrative now reads *"Most fires report minimal to moderate fire behavior."*
   - Absolute acres grew only **+36,675 in 7 days**, compared with +551,814 over the 22 days before 9/18.
3. **Southern Plains:** on the 9/25 NFN table, TX and OK have **1 large fire each out of 4 listed**. On 9/18 they had 10 of 50. New TX fires between 9/26 and 9/27 are all 2,125 acres or smaller.
4. **NFN is now a weekly page.** It states *"This report is currently updated on Fridays."* The next report is expected 10/2. The statistics page updates daily from the IMSR (NIFC's daily Incident Management Situation Report).
5. **Outlook: not re-issued.** It is still the 9/01 issue. The HTTP Last-Modified date is 2026-09-01 18:29:32 GMT, and the PDF ModDate is D:20260901122327-06'00'. The October issue is due 10/01.
6. **Loss leg: nothing moved.** No Q3 or 9-month 2026 tally exists, and none can, because Q3 has not ended. The Cotality Spokane estimate is unchanged. I also found **Swiss Re's H1 2026 figure of $42bn** ("lowest first-half since 2020", Artemis 2026-08-11), which this folder did not previously record.

### New large incidents in the gap (item 2)

| Incident | Origin | Size / containment | WUI / structures | Source |
|---|---|---|---|---|
| **Hydra Fire**, Bosque Co. TX | **9/14** 16:10, just before the window, and missing from the 9/18 record | 933 ac, 100% | **The city of Meridian was evacuated** (9/15 update), and the order was later lifted. *"The nursing home in Meridian remains evacuated."* 9/23 update: ***"Structures lost: Undetermined at this time"*** | InciWeb |
| Rafter 4B, Schleicher Co. TX | 9/26 12:28 | 2,125 ac (NFN 9/25 table: 2,100), 75%; cause: human | *"A pipeline and structures were threatened"*. No losses reported | InciWeb / NFN |
| Grover Bend, Knox Co. TX | 9/26 | 321 ac, 100% | none reported | InciWeb |
| Seven Oaks, Crockett Co. TX | 9/27 | 250 ac, 50% | none reported | InciWeb |
| Stone Bridge, near Wilburton OK | not stated | 130 ac, 60% | none reported | NFN 9/25 |
| Dome Fire, Yosemite CA | 9/15 | 5,215 ac, 30%; cause: abandoned campfire | *"There are no imminent threats to infrastructure"* | InciWeb |

**No new large incident with a published count of destroyed structures turned up in the InciWeb incidents I checked (20 recently updated pages, fetched 9/28).** This is a statement about that set only. CAL FIRE could not be reached (see gaps).

### AEO-09 input (item 3). Not a verdict.

The outlook is still the **9/01 issue**. I re-read the text, and it matches the 9/18 record word for word:
- **September, Southern Area section (the governing surface):** *"An expansive area of above-normal significant fire potential is expected across Texas, Oklahoma, Arkansas, Louisiana, Mississippi, and southwestern Alabama for the month ahead. These conditions may very well continue into October and November in portions of the region, but confidence is low as to where conditions will remain driest."*
- **October, Executive Summary:** *"For October, significant fire potential will be normal for most of the country except for northern Minnesota, northern Wisconsin, western Upper Michigan, Puerto Rico, and the U.S. Virgin Islands, which will remain above normal."*
- **Map:** I did **not re-extract** the panels this run because `pdfimages` is not installed (see gaps). The file has not changed since 9/01, so the 9/18 map reading still applies: September has TX two-thirds red with the far west normal, and OK entirely red. October has TX and OK normal.
- **Map versus text is unchanged:** for October, the map shows TX/OK normal while the Southern Area text only hedges ("may very well continue ... confidence is low"). Whether that counts as a disagreement is AEOLUS's call. **The October issue (due 10/01) will be the first one where October is the current-month panel.**

---

## proposed_findings *(proposals only; AEOLUS adjudicates)*

**New evidence under earlier proposals**
- **P1 (the loss leg is blind):** there is still no post-H1 tally. The first possible Q3 2026 aggregate is expected about mid-October. A fourth H1 issuer figure (Swiss Re $42bn) is consistent with the others.
- **P3 (Spokane structure counts):** the Cotality page was last updated 8/24 and still shows "5,256 properties with damage; 42 classified as destroyed" alongside $1.0–1.3B. I found no WA EOC final tally, which makes this the fourth run in a row without one.
- **P7 (publish the pair, not the ratio):** see P12. The ratio cannot be reproduced this run, which is a stronger reason to always publish the absolute figures.

**P11. The large-fire instrument has no stable basis.** On 9/25 the NFN narrative says **26**, but the NFN table field "Total number of large fires" says **4** on the same page. On 9/28 the statistics page's "Being Suppressed" field says **17**. The historical series already mixes fields: the 8/21 row used the statistics field, while the 8/27 and 9/18 rows used the NFN table field. **Proposal:** AEOLUS fixes one field for `nifc_large_fires_uncontained`. The statistics page's "Total Number of Large Fires Being Suppressed" is the only one that updates daily. Until then, the 50 → 26 → 17 path should not be read as a clean trend. *Why the table shows 4 is not evidenced. My hypothesis is that it lists a subset of the IMSR large fires.*

**P12. The 9/18 closure of open question #6 did not hold.** The 10-yr-average fields are **blank again** on 9/25, and the narrative **145% / 125% cannot be reproduced** from the ten year-rows on the page:
- The mean of those rows gives **142.67% / 124.47%**.
- The 9/18 published average gives 146.99%.
- 145% implies a denominator of about 5.90M acres, and I do not know NIFC's averaging method.

**Proposal:** treat NFN acreage percentages as narrative-only (not reproducible) unless the average fields render on that day. The absolute acreage is the reliable figure.

**P13. A search-engine summary attached the wrong year to 2025 loss figures.** WebSearch stated *"Aon reported ... $12 billion for Q3 2026 ... nine-month $114 billion ... Gallagher Re $105 billion."* I fetched the underlying Artemis article. It is dated **16 October 2025** and covers **Q3 and nine months of 2025**. **Q3 2026 has not closed yet, so no such 2026 figure can exist.** None of it was logged. **Proposal:** a loss figure found only through search must be checked against the publisher's own dated page before it enters the record. This is the loss-leg version of the `fused_true_facts_false_premise` failure mode.

**P14. The WUI risk in the southern Plains has shown up in this dataset as an evacuation, with no confirmed structure loss.** Hydra (Meridian, TX) evacuated a whole town on 9/15, and the issuing authority still reported "Structures lost: Undetermined" on 9/23. **Proposal:** record it as an evacuation event only. **Do not treat it as a loss** until Texas A&M Forest Service publishes a count.

---

## gaps *(required output: failures are reported, not worked around)*

| # | Item | Attempt | Exact result |
|---|---|---|---|
| 1 | **CAL FIRE incidents** | `curl -sSL -A "Mozilla/5.0" "https://www.fire.ca.gov/incidents"` | **`HTTP=403 SIZE=380`**, body *"Access Denied … You don't have permission to access "http://www.fire.ca.gov/incidents" on this server. Reference #18.569cc17.1790640096.40ef3091"* (Akamai edge block). Not worked around. |
| 2 | **Outlook map panels** | `pdfimages -f 1 -l 1 -png outlook.pdf panel` (from SOURCES.md) | `which pdfimages` returns nothing, so **poppler-utils is not installed on this box**. The 9/18 map reading stands because the file is unchanged (Last-Modified is 9/01). |
| 3 | pdfminer on system python | `python3 -c "from pdfminer.high_level import extract_text; …"` | `ModuleNotFoundError: No module named 'pdfminer'`. **It works under `/home/willi/Research-workspace/.venv/bin/python3`.** SOURCES.md should name the venv interpreter. |
| 4 | **Preparedness Level step history, 9/18–9/22** | — | NFN shows only the current level. The PL page and IMSR archive are not in SOURCES.md and were not used. |
| 5 | **NFN 10-yr-average fields** | NFN fetch, HTTP 200 | The "10-year average Year-to-Date 2016-2025 / Fires: / Acres:" fields are blank. The narrative percentages cannot be reproduced (P12). |
| 6 | **Q3 / 9-month 2026 cat tally** | Artemis insured-losses listing (newest item 9/24) and wildfire listing (newest item 8/06) | **Nothing appears in those two listings as of 9/28.** Q3 has not ended, so this is expected. |
| 7 | **WA state EOC final Spokane tally** | No SOURCES.md command exists | Not located. This is the fourth run in a row. |
| 8 | **Non-renewal data outside CA (open question #3)** | Not attempted this run | The item 1–5 scope took priority. It is still open. |
| 9 | **Drought** | Cited, not pulled (shared-input rule) | From `water/workbook/SERIES.tsv`: CONUS D1–D4 **59.37%**, mapDate **2026-09-15**, pulled by water/ on 9/18. The data is 13 days old at water/, which owns it. |
