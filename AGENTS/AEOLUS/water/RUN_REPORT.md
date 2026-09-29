# AEOLUS · WATER — worker RUN REPORT

**run_date: 2026-09-28** (worker run 19:59–20:09 ET; report written 20:08 ET per `date`) · spawned by AEOLUS · **findings are PROPOSAL-ONLY — AEOLUS adjudicates.**
*Nothing below is scored, fired, resolved or routed. No source was substituted. Every failed command is reported with its exact error. No git operations.*
*(Supersedes the 9/18 `RUN_REPORT.md`; `RUN_REPORT_ADDENDUM.md` (9/18) left untouched.)*

---

## observations_added

**120 rows → `workbook/SERIES.tsv`** (510 → 630 lines) · **14 rows → `workbook/LOG.tsv`** · `DOSSIER.md`: new 9/28 block at top + two-clock header → `Last real data refresh: 2026-09-28` / `Dossier written: 2026-09-28`.
All `pulled_at` stamps = `2026-09-28 20:06 ET` (SERIES) / `20:06`–`20:08 ET` (LOG). I took each one from `datetime.now()` inside the write command, and the script asserted that no stamp was later than the wall clock. I re-checked them after writing: 120/120 rows have 7 fields and 14/14 LOG rows have 6.

| Instrument (approved names only) | Rows | Span |
|---|---|---|
| `kaub_stage` / `duisburg_ruhrort_stage` | 11 / 12 | 9/18–9/28 (+1 Duisburg **9/15 revision append**) |
| `mead_elev` / `powell_elev` | 10 / 10 | 9/18–9/27 |
| `lees_ferry_q` | 27 | 10 new (9/18–9/27) + **17 revision appends** (9/01–9/17) |
| `memphis_stage` | 10 | 9/18, 9/19, 9/21–9/28 (9/20 skipped, n=20) |
| `stlouis_stage` | 10 | 9/19–9/28 |
| `gatun_elev` | 10 | 9/18–9/27 |
| `usdm_conus_*` | 6 | mapDate 9/22 |
| `panama_max_draft_ft` · `danube_stations_below_lkv` · `rosario_stage` | 1 · 1 · 1 | 9/28 |
| Yangtze (`yichang_/hankou_/datong_` stage+q, `three_gorges_level`) | 7 | 9/29 07:00 CST |
| `maxau/worms/mainz_stage` (9/28) · `emmerich_stage` (9/27) | 4 | |

⛔ **I measured Vicksburg and Cairo but did not write them to SERIES, because no approved name exists for either. Proposed names: `vicksburg_stage` and `cairo_stage`.** The figures are in LOG and below.
⚠️ **I edited one of my own LOG rows about 1 minute after writing it.** The Colorado row said Lees Ferry was "~7,650–7,840 cfs during the Powell rise". The actual range across 9/16–9/24 was 7,650–8,220. That row was never read or relied on before the fix. Nothing written by anyone else was touched.

---

## threshold_state

*This table gives value and margin only. **The FIRED/NOT-FIRED verdict is AEOLUS's call.***

| Threshold | Value [date · basis] | Margin | Note |
|---|---|---|---|
| **Mead vs Hoover 1,035 ft** | **1,037.79 ft** [9/27 · USBR 921/49] | **+2.79 ft** | lowest daily value since 9/10; the 14-day trend (least-squares slope) is **−0.0683 ft/day** (was −0.0352 at the 9/17 read) |
| Mead exit ≥1,045 × 5 days | max since 9/10 = 1,038.78 (9/13) | — | **0 days ≥1,045** |
| **Powell vs ROD 3,510 ft** (realised daily) | **3,517.64 ft** [9/27 · USBR 919/49] | **+7.64 ft** | low 3,516.62 (9/15); high 3,517.77 (9/24); falling 3 days since |
| Powell exit ≥3,520 × 5 days | max since 9/10 = 3,517.77 (9/24) | — | **0 days ≥3,520** |
| **Kaub vs NNW 25 cm** — 3 most recent complete days | 9/26 **−0.844** · 9/27 **−0.604** · 9/28 **1.537** (n 96/96/95) | −25.844 / −25.604 / −23.463 | these are unrounded daily means |
| **Duisburg-Ruhrort vs NNW 153 cm** — same 3 days | 9/26 **130.344** · 9/27 **126.104** · 9/28 **123.031** (n 96/96/96) | −22.656 / −26.896 / −29.969 | |
| **C5 conjunction, 3 most recent complete days** | **both legs at/below NNW on 9/26, 9/27 and 9/28** | — | The joint run has lasted **11 complete days (9/18–9/28)**. See `dark_window_scan` |
| **Memphis vs `lowThreshold` −8 ft** | daily mean **+9.553 ft** [9/28, UTC day, n=23] · instantaneous 10.32 @ 23:00Z | +17.55 | trough since 8/19 still **−4.678 [9/14]**, which was +3.32 vs −8 / +6.13 vs 2022's −10.81 / +7.38 vs 2023's −12.06 |
| USDM CONUS D1–D4 | **59.24%** [mapDate 9/22] | −0.13 pp vs 59.37 | D4 **2.11%** (+0.09) |
| Gatún (no band registered) | **84.74 ft** [9/27 · ACP CSV] | — | same date in prior years: 2023 **79.99** / 2024 86.16 / 2025 86.80 |
| Panama Neopanamax draft | **49.0 ft** effective 9/28 (A-36-2026) | — | up from 48.0 ft (A-33). **SLOTS** go from 32 to **33/day** for booking dates from 10/15. No new **TRANSITS** figure yet (the September summary is not out) |
| Panama TRANSITS vs ≤32/≤27/≤22 | latest is still **33.19/day (Aug)** [A-34] | +1.19 vs ≤32 | |
| Danube below-LKV flag | **23 of 44** [9/28] | was 5 on 9/18 | 19 after removing the documented placeholder dates (see changes ⑥) |
| Rosario vs P10 1.44 m | **2.81 m** [9/28] | +1.37 m | 88th percentile of the trailing 366 days |

---

## dark_window_scan

**Rhine C5 (frozen NNW Kaub ≤25 / Duisburg ≤153), every day 9/13–9/28**
- **Method:** PEGELONLINE `W/measurements.json?start=P31D`, pulled at 20:00 ET. Kaub returned 2,973 rows and Duisburg 2,976, both covering 2026-08-29 02:00 → 2026-09-29 01:45 CEST.
- **Daily mean:** unrounded, over the local CEST calendar day. A day counts as complete at n ≥ 90 of 96.
- **Reproduction check:** this method reproduces every 9/18-run value to 3 decimals, with one exception: Duisburg 9/15 is now **159.292, revised from 159.312**. The n is 96 in both pulls, so a raw reading changed. A revision row was appended.
- **9/28 is COMPLETE.** The brief expected it would not be, but the German day closed at 18:00 EDT, before this run started.

| Date | Kaub mean | n | Duisburg mean | n | Both ≤? |
|---|---|---|---|---|---|
| 9/13 | 25.292 | 96 | 147.729 | 96 | no — Kaub +0.292 |
| 9/14 | 31.083 | 96 | 160.823 | 96 | no |
| 9/15 | 30.723 | 94 | 159.292 *(rev.)* | 96 | no |
| 9/16 | 27.448 | 96 | 160.438 | 96 | no |
| 9/17 | 24.302 | 96 | 157.781 | 96 | no — Kaub only |
| **9/18** | **23.000** | 96 | **151.594** | 96 | **YES** |
| **9/19** | **21.719** | 96 | **147.531** | 96 | **YES** |
| **9/20** | **18.427** | 96 | **146.490** | 96 | **YES** |
| **9/21** | **15.625** | 96 | **147.896** | 96 | **YES** |
| **9/22** | **12.625** | 96 | **142.875** | 96 | **YES** |
| **9/23** | **11.344** | 96 | **138.625** | 96 | **YES** |
| **9/24** | **5.760** | 96 | **135.531** | 96 | **YES** |
| **9/25** | **2.427** | 96 | **134.073** | 96 | **YES** |
| **9/26** | **−0.844** | 96 | **130.344** | 96 | **YES** |
| **9/27** | **−0.604** | 96 | **126.104** | 96 | **YES** |
| **9/28** | **1.537** | 95 | **123.031** | 96 | **YES** |
| 9/29 | 1.250 | 8 | 121.000 | 8 | incomplete — skipped |

- **Three-day windows in 9/13–9/28 where both legs hold on every day: NINE.** They run 9/18-20, 9/19-21, 9/20-22, 9/21-23, 9/22-24, 9/23-25, 9/24-26, 9/25-27 and 9/26-28. All nine sit inside **one unbroken 11-day joint run from 9/18 to 9/28**, which is still open at the latest complete day. It started the day after the last 9/18 read (9/15–9/17).
- **Earlier window, still in the retained data:** 9/10–9/12 (21.531/152.906 · 21.844/149.146 · 20.635/145.073), bounded by 9/09 and 9/13. The gap between the two runs was 5 days (9/13–9/17).
- **NNW re-read at this grading:** Kaub still **25.0** (occurrence 2018-10-22) and Duisburg still **153.0** (occurrence 2018-10-23). **WSV has NOT republished NNW,** even though Kaub's daily mean has gone as low as −0.844, so the frozen and live values still agree. GlW is 77 / 227 (validFrom 2023-01-01); MNW is 65 / 201.
- **WSV forecast** (25 points per station, horizon 9/28 07:00 → 9/30 07:00 CEST): Kaub 2 → 0 → −1 → **−2**; Duisburg 123 → **121**, flat. There is no rebound anywhere in the horizon.
- **Discharge (Q), daily means:**
  - Kaub 534.3 m³/s (9/18) → 433.5 (9/26) → 445.3 (9/28).
  - Duisburg 665.4 → 552.9 (9/28).
  - ⚠️ Q is derived from stage through a rating curve. It is **not an independent check of the gauge sensor**; the two stations falling together over 235 km is the stronger argument against a sensor fault.
- **Kaub datum caveat is still open.** Kaub's gauge zero is 67.669 m NHN, validFrom 2019-11-01, which is after the 2018 NNW. So the ~25 cm exceedance is approximate.

**Mead / Powell, every day 9/10–9/27** (USBR 49 CSVs; the latest printed row is 9/27)

| Date | Mead | vs 1,035 | Powell | vs 3,510 |
|---|---|---|---|---|
| 9/10 | 1,038.72 | +3.72 | 3,517.24 | +7.24 |
| 9/11 | 1,038.65 | +3.65 | 3,517.13 | +7.13 |
| 9/12 | 1,038.67 | +3.67 | 3,517.01 | +7.01 |
| 9/13 | 1,038.78 | +3.78 | 3,516.87 | +6.87 |
| 9/14 | 1,038.72 | +3.72 | 3,516.74 | +6.74 |
| 9/15 | 1,038.66 | +3.66 | **3,516.62** (min) | +6.62 |
| 9/16 | 1,038.50 | +3.50 | 3,516.67 | +6.67 |
| 9/17 | 1,038.44 | +3.44 | 3,516.83 | +6.83 |
| 9/18 | 1,038.38 | +3.38 | 3,516.84 | +6.84 |
| 9/19 | 1,038.32 | +3.32 | 3,516.99 | +6.99 |
| 9/20 | 1,038.22 | +3.22 | 3,517.21 | +7.21 |
| 9/21 | 1,038.19 | +3.19 | 3,517.41 | +7.41 |
| 9/22 | 1,038.14 | +3.14 | 3,517.56 | +7.56 |
| 9/23 | 1,038.06 | +3.06 | 3,517.69 | +7.69 |
| 9/24 | 1,038.01 | +3.01 | 3,517.77 (max) | +7.77 |
| 9/25 | 1,037.92 | +2.92 | 3,517.75 | +7.75 |
| 9/26 | 1,037.88 | +2.88 | 3,517.71 | +7.71 |
| 9/27 | **1,037.79** (min) | **+2.79** | 3,517.64 | +7.64 |

- **Mead** has not been at or below 1,035 on any day, and has not reached 1,045 on any day.
- **Powell** has not been at or below 3,510 on any day, and has not reached 3,520 on any day.
- **Exit counters:** 0 of 5 for both.

---

## changes

① **Rhine.** Since the last read (9/15–9/17, with only Kaub below on 9/17), both legs have been below on every complete day from 9/18 to 9/28.
- Kaub fell 23.844 cm, from 23.000 to −0.844 (9/26), then went to 1.537 (9/28).
- Duisburg fell 28.6 cm, from 151.594 to 123.031, with no down-day reversals after 9/21.
- The other Rhine gauges (daily means, not trigger stations): Maxau 283.198 · Worms −23.469 · Mainz 100.917 (9/28); Emmerich −21.781 (9/27).

② **Mead** fell 0.65 ft from 9/17 (1,038.44 → 1,037.79) and the trend steepened from −0.035 to −0.068 ft/day. **Powell** turned up after 9/15 (+1.15 ft to 9/24) and has fallen 0.13 ft since then.
- **What drove it:** Lees Ferry (Glen Canyon's release) ran 7,650–7,840 cfs from 9/16 to 9/22, then 8,070–8,220 from 9/23. Powell rose while releases were flat or rising, so the extra water must have come in as inflow. **That is my inference; I pulled no Powell inflow series, because none is registered.**
- **Lees Ferry vs normal:** the 9/18–9/27 mean was 7,940 cfs (n=10), which is **−20.65%** against the 2018–25 same-window mean of 10,006.8 (n=80). The 9/18 read was −23.32% for 9/04–17. That is a different window, and the seasonal baseline is falling, so the change is not like-for-like.

③ **Panama.** A-36-2026 (dated 9/28) is a loosening:
- **Draft limit raised from 48.0 to 49.0 ft, effective immediately.**
- **SLOTS:** Neopanamax goes from 9 to 10 per day, taking the total from 32 to **33/day**, for booking dates from 10/15.
- From 9/29 there is no per-customer slot limit, and customers can book consecutive dates.
- ACP's stated basis: *"the most recent precipitation levels recorded in September in the Canal watershed and the effectiveness of the water-saving measures … and based on the current and projected level of Gatun Lake"*.
- Gatún rose from 84.47 (9/17) to 84.74 (9/27). It fell on only two days in that span (9/21 −0.01, 9/25 −0.02).

④ **Mississippi.**
- **Memphis:** the daily mean fell to a secondary dip of −2.028 on 9/23, then rose **11.58 ft in 5 days** to +9.553 on 9/28.
- **St. Louis** (08:00 observation): 3.22 (9/18) → 16.15 (9/27) → 15.94 (9/28).
- **Cause not investigated** — none asserted.

⑤ **USDM.** Drought extent has been flat at about 59% for four maps (58.59 → 59.37 → 59.24), while intensity edged up (D4 at 2.11). State D1–D4 cut, 9/15 → 9/22:

| State | 9/15 | 9/22 | Change |
|---|---|---|---|
| **TN** | 17.37 | **48.07** | **+30.70 pp** |
| MS | 67.67 | 76.02 | +8.35 |
| LA | 80.33 | 85.63 | +5.30 |
| AR | 88.69 | 92.24 | +3.55 |
| TX | 81.01 | 84.20 | +3.19 |
| MO | 32.40 | 34.14 | +1.74 |
| OK | 99.82 | 99.82 | flat; **D4 16.59 → 20.79** |
| IA | 6.79 | 2.10 | −4.69 |
| NE | 60.32 | 56.62 | −3.70 |
| CO | 88.21 | 85.72 | −2.49; D4 15.21 → 13.37 |

⑥ **Danube.** The number of stations flagged below their lowest-ever level (LKV) rose from **5 to 23 of 44**.
- It is **19** after removing Deggendorf, Apatin, Ilok Most and Novo Selo, whose LKV dates are the documented 1799/1884/1894 placeholders. It is 18 if Bogojevo's LKV date (1953-12-31 23:00) is also a placeholder; that is not verified.
- **Hungarian reach, Nagybajcs (km 1801) → Duna Mohács (km 1447):** 13 stations read below LKVs dated 1992 or 2018 — for example Budapest 28 vs 33, Mohács 0 vs 50, Ercsi −97 vs −93.
- **Moving-reference effect:** five stations carry 2026 LKVs and read +1 — Adony and Dunaföldvár (reset 9/08; they were 8/01 and 8/19 in the 9/18 dossier), Dombori (9/09), Baja (9/10) and Paks (8/02).
- **Upper Danube**, also below: Hofkirchen 144 vs 166 (it was +5 on 9/18), Pfelling 213 vs 226, Kienstock 104 vs 112, Devín 53 vs 63.

⑦ **Paraná (Rosario):** 2.53 m (9/18) → **2.81 m** (9/28). The percentile rose from 73.5th to 88.0th; the trailing window's minimum is 1.08, P10 1.44 and median 2.30.

⑧ **Yangtze** (first read since 8/21; no reference plane, so no adjective). Readings at 07:00 CST 9/29, compared with 8/13:

| Station | Level | Flow |
|---|---|---|
| Yichang | 44.43 → **41.31 m** | 17,800 → **9,970 m³/s** |
| Hankou | 20.61 → **16.28 m** | 27,600 → **15,500** |
| Datong | 10.06 → **7.08 m** | 31,100 → **19,800** |
| Three Gorges reservoir | 157.30 → **166.46 m** | outflow 8,790 |

⑨ **Two source revisions.**
- **Lees Ferry:** USGS moved every 9/01–9/17 value down by 60–70 cfs (15 of 17 by exactly −70). This is the second downward revision in a month, and all values are still provisional ("P").
- **Duisburg 9/15:** −0.020 cm.

---

## proposed_findings

*These are proposals with sources; AEOLUS adjudicates.*

| # | Proposal | Source |
|---|---|---|
| **P-1** | **The Rhine C5 conjunction has held on every complete day from 9/18 to 9/28 (11 days), including the 3 most recent complete days (9/26–9/28).** There are nine qualifying 3-day windows. This run started on the first day after AEOLUS's last read, while the desk was dark. Kaub's daily mean went below the gauge zero (−0.844 on 9/26), about 26 cm under its 2018 record. | WSV PEGELONLINE P31D, n per day in table |
| **P-2** | **The live NNW has not been republished** (still 25/153, 2018 occurrence dates), so the frozen and live trigger values currently agree. I have no evidence for **why** WSV has not rewritten it. *Hypothesis only:* NNW may be computed from checked data and lag the raw feed. | `W.json?includeCharacteristicValues=true` |
| **P-3** | **Panama moved to loosening:** draft 49.0 ft (+1.0) and SLOTS 33/day, on ACP's stated basis of September rain plus Gatún's current and projected level. Gatún is 84.74 ft, 4.75 ft above the 2023 same-date analogue. | A-36-2026 (URL in gaps table); ACP Gatún CSV |
| **P-4** | **Mead's decline has steepened** (−0.068 ft/day over 14 days; low 1,037.79 on 9/27, +2.79 ft). Powell's 9/16–9/24 rise came while releases were flat or up, which implies an inflow pulse (inference). Powell has turned down for 3 days. | USBR 921/49, 919/49; USGS 09380000 |
| **P-5** | **Memphis did not hold its lows.** The trough stays at −4.678 (9/14), and the river has since risen 11.6 ft on daily means to +9.553. **Basis issue:** the stored series uses **UTC** calendar days, which no row said until this run. On the gauge's local day (CST6CDT) the trough is 9/13 at −4.587, and daily means differ by up to 0.6 ft. Choosing which day boundary is canonical is AEOLUS's call. | NWPS MEMT1 `/stageflow/observed` (706 hourly obs, 8/30 → 9/28 23Z) |
| **P-6** | **The Danube below-LKV count jumped from 5 to 23 of 44 (19 without placeholder dates).** The whole Hungarian reach is below its 1992/2018 LKVs, while five 2026-reset stations read +1 because their reference moved. | OVF ArcGIS LKV_folyok |
| **P-7** | **USDM extent is flat at about 59% but moving between regions:** Tennessee +30.7 pp in one week, and Oklahoma's D4 is up to 20.79, while Iowa, Nebraska and Colorado ease. | USDM StateStatistics (FIPS 47/40/19/31/08) |
| **P-8** | **The 24-Month Study filenames do not carry a year.** `24Month_10.pdf` on the UC index is the **October 2025** study. A check that counts the October slot on the index as published would give a false positive. **The October 2026 study is not published.** | UC index + title line of `24Month_10.pdf` |
| **P-9** | **Mississippi Vicksburg = NWPS `VCKM6`** (10.91 ft, lowThreshold 0.8 ft, no historic low-water list). **Cairo = `CIRI2`**, which NWS files as the Ohio River at Cairo (27 ft, lowThreshold 10.3). I found both in the NWPS gauge listing on the same primary; I did not guess them. They need registration and names. | `api.water.noaa.gov/nwps/v1/gauges?bbox…` (193 gauges) |
| **P-10** | **The WSV file-service listing did not roll.** Its start is still 20.06.2026 (102 dates now against 91 on 9/18). *Hypothesis:* the file service accumulates, so the summer-2026 event data is preservable there after the REST endpoint's ~31-day retention drops it. | file-service listing, HTTP 200 49,258 B |
| **P-11** | **Lees Ferry has had a second provisional revision (−60 to −70 cfs).** Every Lees Ferry level carried from 9/18 reads high. | USGS NWIS dv |

---

## gaps

**Each failure is reported as it happened; none was worked around. No source was substituted.**

| # | What | Command | Result |
|---|---|---|---|
| **G-1** | Lees Ferry, first attempts | `curl "https://waterservices.usgs.gov/nwis/dv/?format=json&sites=09380000&parameterCd=00060&startDT=2026-09-01&endDT=2026-09-28"` ×3 at 20:01 ET | **HTTP 503, 1,204 B** each time (HTML "Error report" body). A retry at 20:02 returned HTTP 200 and 4,520 B of JSON that parsed, so this is resolved. The 2018–25 history pull returned 200 and 193,327 B. |
| **G-2** | October 2026 24-Month Study | `.../lc/region/g4000/24mo/2026/{OCT26_6,OCT26_7,OCT26,OCT26_MIN,OCT26_MAX}.pdf` | **HTTP 404, 196 B** on all five. This is expected mid-October; it is not a data absence. The UC index's `24Month_10.pdf` is October **2025** (see P-8). |
| **G-3** | September Probable MAXIMUM | `.../24mo/2026/SEP26_MAX.pdf` | **Still HTTP 404, 196 B.** The index still links `SEP26_MIN` only. |
| **G-4** | LC "current" 24mo | `curl -sL https://www.usbr.gov/lc/region/g4000/24mo.pdf` | HTTP 200, 819,439 B, but the title line reads **"July 2026 Most Probable"**, two months stale. Never use this URL as "current". |
| **G-5** | Federal Register notice of the ROD | FR API: `"Lake Powell"`, `"Colorado River" "Record of Decision"`, `"Post-2026"`, pub ≥ 2026-07-15; plus `reclamation-bureau` + `"Colorado River"` ≥ 7/01 | **No ROD notice found.** Hits: the 7/31 EPA EIS Notice of Availability (`federalregister.gov/documents/2026/07/31/2026-15536/…`), a 7/17 FWS razorback-sucker rule, a 7/02 GCDAMP nominations notice, and unrelated FWS/BLM items. **Scope:** this covers API text search only, and FR indexing may lag. `usbr.gov/ColoradoRiverBasin/` and `/post2026/` have nothing newer than the 8/21 ROD and guidelines; `decision-doc/` lists the same 4 PDFs. |
| **G-6** | WSV multi-year series (the 9/30 C5 re-scope) | file-service listing only | **I did not attempt the back-to-2000 bulk route** (a JavaScript zip builder on `/gast/pegeltabelle`). **The route is still unresolved, 2 days before the 9/30 deadline.** |
| **G-7** | Incomplete days (skipped, not counted) | — | Memphis 9/20 (n=20/24, UTC); Emmerich 9/28 (n=56/96); Kaub and Duisburg 9/29 (n=8); Kaub 8/29 and Duisburg 8/29 (n=88, the window edge). |
| **G-8** | Powell inflow | — | **Not pulled; no source is registered in SOURCES.md.** The "inflow pulse" in P-4 is an inference from storage change against a flat release. |
| **G-9** | Panama September Monthly Ops Summary | advisory index (HTTP 200, 767,689 B) | Not yet published; the latest monthly is A-34 (August). No September TRANSITS figure exists yet. |
| **G-10** | Danube reading time | — | The OVF `Vizallas` field has **no timestamp**, so the reading's vintage is unknown. |
| **G-11** | Yangtze timestamp basis | — | `tm` decodes to 2026-09-28T23:00Z (07:00 CST 9/29). **Not verified** that `tm` is true UTC epoch rather than local time encoded as epoch. |
| **G-12** | Snowpack | — | Seasonally near zero Jun–Sep. Correctly empty; not a gap. |

**For AEOLUS (not gaps):**
- **AGENT.md changed during this run.** Its THRESHOLDS and OPEN QUESTIONS were re-cut 9/28; it now shows as modified in the working tree, and I did not touch it. I followed the spawn prompt, which matches the re-cut.
- **DOSSIER.md is now about 86 KB**; rotation is AEOLUS's call.
- **Rows written by earlier runs were not modified.** All corrections are append-only revision rows.

**Source URLs used this run:**
- A-36: `https://pancanal.com/wp-content/uploads/2026/04/ADV-36-2026-Increase-in-the-Number-of-Neopanamax-Booking-Slots-Draft-Adjustment-and-Transit-Reservation-System.pdf`
- Colorado River basin page: `https://www.usbr.gov/ColoradoRiverBasin/post2026/`
- UC 24-Month Study index: `https://www.usbr.gov/uc/water/crsp/studies/index.html`
