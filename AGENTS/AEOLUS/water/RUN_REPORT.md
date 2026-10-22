# AEOLUS · WATER — worker RUN REPORT

**run_date: 2026-10-21** (worker run 22:19–22:26 ET per `date`) · spawned for AEOLUS (dark-window catch-up, 5 tasked items) · **findings are PROPOSAL-ONLY — AEOLUS adjudicates.**
*Nothing below is scored, fired, resolved or routed. No source was substituted. No git operations. Supersedes the 10/9 `RUN_REPORT.md`.*

---

## observations_added

**96 rows → `workbook/SERIES.tsv`** (790 → 886 lines after the repair) · **7 rows → `workbook/LOG.tsv`** (138 → 145) · `DOSSIER.md`: new 10/21 block at top; header → `Last real data refresh: 2026-10-21`.

| instrument | rows | dates |
|---|---|---|
| kaub_stage / duisburg_ruhrort_stage | 12 + 12 | 10/10–10/21 (all complete, local CEST day) |
| contargo_lws_kaub_20ft / _duisburg_20ft | 2 + 2 | 10/20, 10/21 (departure dates) |
| powell_elev / mead_elev | 11 + 11 | 10/10–10/20 |
| lees_ferry_q | 10 | 10/9, 10/12–10/20 (10/10–10/11 not in NWIS return) |
| memphis_stage | 12 | 10/10–10/21 (UTC day, n ≥ 22) |
| usda_barge_rate_pct | 7 | week 10/13, all origins |
| usdm_conus_* | 6 | valid 10/13 |
| gatun_elev | 11 | 10/10–10/20 |

Stamps: SERIES `2026-10-21 22:24 ET`, LOG `2026-10-21 22:25 ET`, each taken from `date` in the same command as the write. ⚠️ The stamp is the WRITE time; the pulls ran 22:19–22:23 ET, so stamps are up to ~5 min later than the actual pull (none later than the wall clock). SERIES: every non-blank line has 7 fields; LOG: every line has 6; both LF-only (0 CR).

**REPAIR (item 4, AEOLUS-directed):** the 2026-10-10 `rosario_stage` record split across physical lines 789–790 (two 6-field lines) is now ONE 7-field record. Value 3.22 m, pulled_at `2026-10-10 11:46 ET` and notes text unchanged; the 5 trailing empty fields were dropped. Logged in LOG.tsv (`series_tsv_row_repair`). ⚠️ Not repaired: **line 252 is a blank line** (1 empty field), pre-existing and outside the directed scope; `csv.DictReader` skips it. So "every line has 7 fields" holds for every NON-BLANK line only.

## threshold_state

*FIRED / NOT-FIRED is AEOLUS's call. Worker reports value + margin only; the column below says NOT GRADED.*

| instrument | value | margin | state |
|---|---|---|---|
| Rhine Kaub ≤25 cm (NNW, frozen) | 15.146 cm [10/21 mean, n=96]; window max 19.719 [10/13] | −9.854 (10/21); −5.281 at the window max | NOT GRADED |
| Rhine Duisburg-Ruhrort ≤153 cm (NNW, frozen) | 138.844 cm [10/21 mean, n=96]; window max 147.573 [10/11] | −14.156 (10/21); −5.427 at the window max | NOT GRADED |
| Rhine joint 3-complete-day windows | **12 of 12** windows (10/8–10/10 through 10/19–10/21) have both legs at/below on all 3 days | first complete day with either leg above its line: **none** | NOT GRADED |
| Mead vs Hoover 1,035 | 1,037.18 ft [10/20]; window min 1,037.18 [10/19 and 10/20] | +2.18 | NOT GRADED |
| Mead exit ≥1,045 ×5 | 1,037.18 | −7.82 | NOT GRADED |
| Powell vs 3,510 | 3,520.77 ft [10/20]; window min 3,518.88 [10/11] | +10.77 (+8.88 at the min) | NOT GRADED |
| Powell exit ≥3,520 ×5 days | 3,520.02 / 3,520.31 / 3,520.55 / 3,520.71 / 3,520.77 on **10/16–10/20 = 5 consecutive days** | +0.02 to +0.77 | NOT GRADED (AEOLUS grades) |
| Oct 24MS (6 maf, official) Mead | Dec-2026 EOM 1,034.52; 12-mo min **1,007.73 (Jul-2027)** | −0.48 / −27.27 vs 1,035 | NOT GRADED (end-of-month table only) |
| Oct 24MS (6 maf) Powell | 12-mo min **3,516.28 (Feb-2027)** | +6.28 vs 3,510 | NOT GRADED |
| Memphis vs lowThreshold −8 ft | 3.532 ft [10/21 UTC-day mean, n=24] | +11.532 (vs 2022 −10.81: +14.342; vs 2023 −12.06: +15.592) | NOT GRADED |
| Panama transits bands ≤32/≤27/≤22 | Sep 32.63/day (A-38, already recorded); Oct not published | +0.63 vs ≤32 (September) | NOT GRADED |
| USDM CONUS D1–D4 | 53.73% [valid 10/13] | −1.48 pp vs 55.21 [10/6] | NOT GRADED |

## changes

1. **Rhine dark window 10/10–10/21 (6c scan)** — calendar day = **local CEST day** (PEGELONLINE timestamps all carry +02:00; this matches the "local CEST day" basis the 10/9 rows use; the CET switch is 10/25). All 12 days complete (n = 95–96); **10/21 is a COMPLETE day on this basis** (the pull at 22:19 ET = 04:19 CEST 10/22), and the incomplete day is **10/22** (n=18: Kaub 18.611 / Duisburg 144.333), not used.
   Kaub UNROUNDED: 10/10 7.823 · 10/11 15.042 · 10/12 18.906 · 10/13 19.719 · 10/14 15.042 · 10/15 12.677 · 10/16 9.052 · 10/17 10.053 (n=95) · 10/18 8.781 · 10/19 12.885 · 10/20 19.240 · 10/21 15.146.
   Duisburg UNROUNDED: 10/10 145.156 · 10/11 147.573 · 10/12 141.812 · 10/13 143.260 · 10/14 146.573 · 10/15 146.958 · 10/16 142.698 · 10/17 145.427 · 10/18 144.260 · 10/19 137.323 · 10/20 138.385 · 10/21 138.844.
   **Both legs at/below on every complete day; no first day above either line exists in the window.** The only reading above a line was one instantaneous Duisburg 155 cm on 10/17 (that day's mean 145.427). 10/8 (0.990 / 138.333) and 10/9 (7.583 / 140.396) recomputed in the same pull and reproduce the stored rows to 3 dp. 10/10 complete (7.823 / 145.156) supersedes the 10/10 LOG incomplete read (n=68: 6.912 / 144.412).
   **NNW re-read 10/21:** Kaub NNW 25.0 (occurrence 2018-10-22), Duisburg NNW 153.0 (occurrence 2018-10-23), `validFrom` = null for both → **not republished**. GlW Kaub 77.0 / Duisburg 227.0, `validFrom` 2023-01-01, unchanged.
   **WSV forecast (init 10/21 07:00 CEST):** forecast class to 10/23 07:00 — Kaub 17 → 20 (10/22 13:00–19:00) → 18; Duisburg 136 → 144–145. Estimate class 10/23 09:00 → 10/25 05:00 — Kaub reaches 25 at 10/24 15:00, 26 at 17:00, 30 by 10/25 03:00; Duisburg 153 at 10/24 15:00, 154 at 19:00, 160 by 10/25 03:00. ⚠️ Instantaneous points, estimate class, not daily means.
   **Contargo** (DE table dated 21.10.2026): 20.10 Kaub 21 / Ruhrort 138; 21.10 Kaub 18 / Ruhrort 136 → Kaub row 'ab 40 cm' **€1,075/20′** (€1,280/40′); Duisburg row 140–131 cm **€675/20′** (€780/40′). Both unchanged since 10/8.
2. **Colorado** — Mead 1,037.60 [10/9] → 1,037.71 [10/11] → **1,037.18 [10/19, 10/20]**: −0.53 ft over 10/11–10/20 (~−0.06 ft/day). Powell 3,518.97 [10/9] → 3,518.88 [10/11] → **3,520.77 [10/20]**: +1.89 ft. **Driver check:** Lees Ferry flat at 6,540–6,650 cfs throughout (10/1 7,100 then ~6,600), so **Glen Canyon release did not change**; the Powell rise is an inflow-side move that this run did NOT verify at a daily instrument. HYPOTHESIS only: Flaming Gorge Drought Response Operations water (the October 24MS assumes 1.00 maf by Apr-2027) and/or October inflow (24MS forecast 0.400 maf, 88% of average).
   **October 2026 24-Month Study — PUBLISHED.** Title date **October 15, 2026**; official run = **6 maf** Powell release (`https://www.usbr.gov/uc/water/crsp/studies/24Month_10_6.pdf`, Model Run ID 3338, processed 10/8/2026 12:58 PM); alternative 7 maf run `24Month_10_7.pdf` (Run 3341, processed 10/8/2026 11:38 AM). Found via the registered UC index command at 22:19 ET 10/21. Anchor method: the Mead and Powell end-of-month columns match all 12 USBR 921/919 actuals Oct-2025 → Sep-2026 **exactly (0.00 ft)** before any projected cell was read.
   - 6 maf Mead EOM: Oct-26 1,035.29 · Nov 1,033.97 · Dec 1,034.52 · Jan-27 1,034.33 · Feb 1,033.64 · Mar 1,027.24 · Apr 1,019.35 · May 1,012.87 · Jun 1,008.47 · **Jul 1,007.73 (12-mo min)** · Aug 1,010.01 · Sep 1,010.85.
   - 6 maf Powell EOM: Oct-26 3,519.23 · Nov 3,519.44 · Dec 3,518.29 · Jan-27 3,517.00 · **Feb 3,516.28 (12-mo and 24-mo min)** · Mar 3,516.53 · Apr 3,519.97 · May 3,533.28 · Jun 3,548.86.
   - 7 maf: Mead 12-mo min 1,015.68 (May-2027); Powell 12-mo min 3,516.28 (Feb-2027), 24-mo min 3,510.69 (Mar-2028).
   - vs September 6 maf study: Mead Dec-26 1,034.18 → 1,034.52 (+0.34); Mead Jul-27 1,007.38 → 1,007.73 (+0.35); Powell Feb-27 3,511.43 → 3,516.28 (+4.85).
   - ⚠️ The LC copy `https://www.usbr.gov/lc/region/g4000/24mo.pdf` still serves the **JULY 2026** study (title line checked); the LC archive name `24mo/2026/OCT26.pdf` returned **HTTP 404**. The UC copy is the October study.
3. **Mississippi** — Memphis UTC-day means: 10/10 8.848 · 10/11 **9.551** (window peak) · 10/12 8.990 · 10/13 7.820 · 10/14 6.356 · 10/15 5.389 · 10/16 5.267 · 10/17 5.778 · 10/18 6.203 · 10/19 5.613 · 10/20 4.510 · **10/21 3.532** (window low; n = 23–24 each). 10/8 (3.630) and 10/9 (6.570) reproduce the stored rows. Latest instantaneous 3.01 ft (10/22 01:00Z). USDA barge, week 10/13: **St. Louis 673.4375% = $26.87/t** (723.21% on 10/6); Twin Cities 852 · Mid-Miss 839 · Lower Illinois 825 · Cincinnati 793.75 · Lower Ohio 793.75 · Cairo-Memphis 567.1875. St. Louis rank: 78.3rd percentile of the same calendar week (n=23; was 69.6 on 10/6), 93.8th of all weeks (n=1,182). Same week: 2022 2,653.1 · 2023 641.7 · 2024 682.9 · 2025 501.4.
4. **USDM** — CONUS valid 10/13: None 25.46 · D0–D4 74.54 · D1–D4 **53.73** · D2–D4 30.33 · D3–D4 9.79 · D4 **1.30**. vs 10/6: D1–D4 −1.48 pp (extent easing), D4 +0.15 (intensity up at the top). Total (US+PR) D1–D4 45.05 — not the CONUS row.
5. **Panama** — Gatún 85.24 [10/10] → **86.20 [10/20]** (+0.94 vs 85.26 [10/9]; rising 9 of 10 days); same date 2023 79.62 / 2024 87.35 / 2025 87.08. **New: A-39-2026 (dated 10/21)**: Last-Minute Reservation service reinstated at the Panamax Locks effective immediately, citing water-saving measures and close-to-average recent watershed rain; Super-category swap/substitution rules from bookings dated 2027-01-03. **No draft or slot-cap change stated**; the ACP says the watershed water deficit persists. September transits 32.63/day (A-38) already recorded; the October Monthly Ops summary is not published (normally the following month).

## proposed_findings

*Proposals only, with sources. AEOLUS adjudicates.*

- **P1 (C5, Rhine):** The dark window 10/10–10/21 adds 12 complete days with both legs at/below NNW; with 10/8–10/9 that is 14 consecutive complete days (and the 10/9 report's 22-day run from 9/18). No exit day exists in the window. The WSV *estimate* has both legs crossing their lines around 10/24 15:00 (instantaneous). — PEGELONLINE W + WV, pulled 2026-10-21 22:19 ET.
- **P2 (C6, AEO-10):** The October 24MS (official 6 maf run) prints Mead end-of-month **below 1,035 from Nov-2026** (1,033.97) and **Dec-2026 1,034.52**, with a 12-month minimum of 1,007.73 in Jul-2027. Realised Mead is 1,037.18 [10/20] and falling about 0.06 ft/day; the study's Oct-26 EOM is 1,035.29. — `24Month_10_6.pdf` (dated 10/15/2026, run 3338) + USBR 921/49.
- **P3 (C6 leg 3):** Powell printed ≥3,520 on 5 consecutive days (10/16–10/20) with Glen release unchanged; the October 24MS Most Probable has **no end-of-month Powell value below 3,510** in 24 months (min 3,516.28 Feb-2027), unlike the August study (which projected a fall below 3,510 in WY2027). The driver of the realised rise is unverified (hypothesis: DROA water). — USBR 919/49, USGS 09380000, `24Month_10_6.pdf`.
- **P4 (C5, Mississippi):** Memphis fell 6.0 ft from 9.551 [10/11] to 3.532 [10/21] on daily means, still +11.5 ft above −8. The St. Louis barge rate fell for a third week (673.44%), but its same-week rank ROSE (69.6 → 78.3) because same-week history is lower in mid-October. — NWPS MEMT1 stageflow/observed; USDA AMS deqi-uken.
- **P5 (Panama):** A-39-2026 eases a booking rule (Last-Minute Reservation back at Panamax) — this is a loosening of a water-saving measure, not a draft or slot change. Gatún +0.94 ft in 11 days. — ACP A-39-2026; ACP Gatún CSV.
- **P6 (SOURCES hygiene, for AEOLUS):** ① `SOURCES.md` §4 should name the UC study URLs `24Month_MM_6.pdf`/`_7.pdf` for October (the index command finds them, the LC `24mo.pdf` copy is 3 months stale). ② The Memphis hourly command `.../gauges/MEMT1/stageflow/observed` is in `RUN_REPORT_ADDENDUM.md` but not in `SOURCES.md`; this run used it from there. ③ In the SOURCES PDF recipe, `python3 -I` (isolated mode) cannot import pdfminer; `.venv/bin/python` works. The worker does not edit SOURCES.md.

## gaps

- **USDM valid 10/20:** not released at pull time (22:22 ET Wed 10/21; release is Thursday). The API returned only 10/13 and 10/6 maps for 10/6–10/21.
- **Panama October transits:** not published (Monthly Ops for October expected in November). September is already recorded.
- **Lees Ferry 10/10 and 10/11:** absent from the NWIS dv return (other days present, provisional "P"). Not a command failure.
- **Powell inflow driver:** not verified — no daily Powell inflow instrument is registered in `SOURCES.md`; not substituted.
- **24MS on the LC host:** `https://www.usbr.gov/lc/region/g4000/24mo/2026/OCT26.pdf` → **HTTP 404** (196 B HTML); `24mo.pdf` → HTTP 200 but the **July 2026** study. The October study was read from the UC host instead (same issuer, registered index).
- **First PDF extraction attempt** with `python3 -I` produced empty text files (pdfminer not importable in isolated mode, stderr suppressed); re-run with `/home/willi/Research-workspace/.venv/bin/python` succeeded.
- **Not tasked / not pulled this run:** Yangtze, Danube (OVF), Paraná (UNL-FICH), St. Louis, Vicksburg/Cairo, CBS 85817NED, heating oil, Maxau/Worms/Mainz/Emmerich stage, all Rhine discharge (Q) series, Powell storage, snowpack (seasonally empty).
- **SERIES.tsv line 252** (blank line) left as found — outside the directed repair.
