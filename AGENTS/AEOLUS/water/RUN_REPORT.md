# AEOLUS · WATER — worker RUN REPORT

**run_date: 2026-10-09** (worker run 20:32–20:42 ET per `date`) · spawned by AEOLUS (tasked subset, 7 items) · **findings are PROPOSAL-ONLY — AEOLUS adjudicates.**
*Nothing below is scored, fired, resolved or routed. No source was substituted. No git operations. Supersedes the 9/28 `RUN_REPORT.md`.*

---

## observations_added

**93 rows → `workbook/SERIES.tsv`** (681 → 774 lines) · **10 rows → `workbook/LOG.tsv`** (123 → 133) · `DOSSIER.md`: new 10/9 block at top; header → `Last real data refresh: 2026-10-09`.
All stamps `2026-10-09 20:40 ET` (SERIES) / `20:41 ET` (LOG), taken from `datetime.now()` in the write script, which checked that no stamp was later than the clock. Every SERIES row has 7 fields and every LOG row has 6. Both files are LF-only (0 CR before and after). The one non-7-field line in SERIES is the blank line 252, which was already there.

| Instrument | Rows | Span |
|---|---|---|
| `kaub_stage` / `duisburg_ruhrort_stage` | 2 / 2 | 10/8, 10/9 (10/5–10/7 already stored; recomputed, identical to 3 dp) |
| `mead_elev` / `powell_elev` | 10 / 10 | 9/28–10/8, minus dates already stored (Mead 10/7, Powell 10/6). The 9/28–10/5 rows are **backfill**: before this run, those values existed only in the notes of the 10/8 scan row |
| `lees_ferry_q` | 11 | 9/28–10/8 (9/25–9/27 re-pulled: no revision) |
| `memphis_stage` | 9 | 9/29–10/5, 10/8, 10/9 (10/6 and 10/7 skipped, n=21) |
| `gatun_elev` | 11 | 9/28–10/8 |
| `panama_transits` | 1 | Sep 2026 |
| `danube_stations_below_lkv` | 1 | 10/9 |
| `contargo_lws_kaub_20ft` / `_duisburg_20ft` | 11 / 11 | 9/29–10/9. 10/8–10/9 were read directly. 9/29–10/7 are mapped from Contargo's own level-history table against the schedule as printed 10/9 (stated in each row's notes) |
| `usda_barge_rate_pct` | 14 | weeks of 9/29 and 10/6 × 7 origins |

⚠️ **Self-correction:** about one minute after writing the Panama LOG row, I corrected it. It said Gatún was "rising 10 of 11 days". The true count is 9 rises and 2 flat days (10/5, 10/6). Nobody had read the row before the fix.

---

## threshold_state

*Value and margin only. **FIRED / NOT-FIRED is AEOLUS's call.***

| Threshold | Value [date · basis] | Margin | Note |
|---|---|---|---|
| **Kaub vs NNW 25 cm**: 3 most recent complete days | 10/7 **1.323** · 10/8 **0.990** · 10/9 **7.583** (n 96/96/96) | −23.677 / −24.010 / −17.417 | unrounded CEST-day means |
| **Duisburg-Ruhrort vs NNW 153 cm**: same days | 10/7 **129.979** · 10/8 **138.333** · 10/9 **140.396** | −23.021 / −14.667 / −12.604 | |
| C5 joint run (count) | both legs at/below NNW on **every complete day 9/18 → 10/9 (22 days)** | — | 3-day joint windows in 10/5–10/9: 3 |
| WSV forecast, init 10/9 07:00 | Kaub 5 → 12 (10/11 07:00); Duisburg 138 → **154** (instantaneous, 10/10 19:00–10/11 01:00) → 152 | Duisburg forecast **+1 above 153** at its peak | `estimate` to 10/13: Kaub reaches **25** at 10/12 21:00. Duisburg 147–148 |
| **Mead vs Hoover 1,035** | **1,037.61 ft** [10/8 · USBR 921/49] | **+2.61** | window low; −0.08 ft/day over 10/4→10/8; 0 days ≥1,045 |
| **Powell vs 3,510** (realised) | **3,519.03 ft** [10/8 · USBR 919/49] | **+9.03** | peak 3,519.04 (10/6, 10/7); 0 days ≥3,520 |
| Memphis vs lowThreshold −8 | **6.570 ft** [10/9 daily mean, UTC day, n=22] | +14.57 | lowest complete day since 9/28 = 3.630 (10/8); trough still −4.678 [9/14] |
| Panama TRANSITS vs ≤32 / ≤27 / ≤22 | **32.63/day** [Sep 2026 · A-38-2026] | **+0.63 vs ≤32** | Aug 33.19. DRAFT 49.0 ft (A-36). SLOTS 33/day from 10/15 |
| Gatún (no band) | **85.23 ft** [10/8 · ACP CSV] | — | same date: 2023 79.92 / 2024 86.15 / 2025 86.88 |
| Danube below-LKV flag | **23 / 44** [10/9] | unchanged count | the **reference** moved (see changes) |
| C6 implementation milestone | Guidelines §3: **effective only on executed implementing + parallel agreements** | — | no primary shows execution; see proposed findings |

---

## changes

1. **Rhine:** Duisburg rose 129.979 (10/7) → 140.396 (10/9). Kaub 0.990 → 7.583. Discharge rose at both: Kaub Q 441.5 → 469.1, Duisburg 579.3 → 619.6 m³/s; Q is rating-derived from stage, so it is not an independent check. On 10/8 at 05:00, Kaub was at **−2** in Contargo's table.
2. **Contargo:** the Duisburg row eased from €800 to **€675** per full 20′ (the 140–131 cm row) on 10/3 and again 10/7–10/9. Kaub stays €1,075.
3. **Glen Canyon release** (Lees Ferry) stepped down on 10/01, from ~8,200 to ~6,600 cfs. The step size (−19.3%) is inside the 2018–25 seasonal range; the level (−26.09% vs those years' same window) is low. Powell's rise stalled at 3,519.04. Mead resumed its decline.
4. **Panama:** September transits came in at 32.63/day, down 0.56 from August. A-37 (LoTSA 2027) changes no draft or slot cap. Gatún rose +0.49 ft in 11 days.
5. **Danube:** OVF rewrote the LKVs (the record-low reference levels) at the Hungarian reach to values dated Aug–Sep 2026. Budapest LKV went from 33 to 0 and Mohács from 50 to −29. 14 stations now sit below their **2026** record lows.
6. **Memphis** peaked at 11.300 (9/30), fell to 3.630 (10/8), then turned up. **The St. Louis barge rate fell two weeks running**: 834.69 → 758.93 → 723.21%. Its same-week rank went from 87.0 to 69.6.

---

## proposed_findings  *(PROPOSALS — AEOLUS adjudicates)*

- **P-1 · The C6 milestone row's "fail to take effect 10/01" leg has no 10/01 anchor in the text.** Guidelines §3 makes effectiveness conditional on executed agreements, and §5.3.A.3 is where "the Secretary shall determine" applies. Source: `2027-2028OperatingGuidelines_Final.pdf` §3, §5.3.A.3, §5.9. **Whether the agreements were executed is UNKNOWN from the registered primaries.**
- **P-2 · WSV forecasts a C5 leg exit.** Duisburg's instantaneous forecast peaks at 154 (10/10 evening), and the Kaub estimate reaches 25 by 10/12 21:00. Daily means are not forecast. Kaub is running above its forecast. Source: PEGELONLINE `WV`.
- **P-3 · Danube LKV rewrite.** This is the second observed instance of OVF moving the LKV reference. It is posted with a lag: the 9/08 Budapest record of 0 was not in the 9/28 response (HYPOTHESIS: OVF publishes LKVs in batches). If true, a flag count taken at any read is computed against a stale reference.
- **P-4 · The Lees Ferry 10/01 step-down is seasonal-sized.** Do not read it as a new cut without the release schedule.
- **P-5 · Contargo vs WSV:** for Ruhrort on 10/11, Contargo forecasts 171 and WSV ~152. The two issuers disagree by 19 cm, and the cause is not reconciled.

---

## gaps

- **Not tasked, not pulled:** USDM, Yangtze, Paraná, St. Louis/Vicksburg/Cairo, CBS, heating oil, Maxau/Worms/Mainz/Emmerich, snowpack (seasonally empty).
- **Lower Basin implementing agreements:** no registered primary covers this. State-agency sites (ADWR/CAP/MWD/SNWA) were not checked, and I made no substitution.
- **USBR `/post2026/` with `-A 'Mozilla/5.0'`:** `Recv failure: Connection reset by peer` (curl rc 56, HTTP 000). The same request with no UA, or with a full browser UA, returned 200. This is a method failure. The registered Contargo command still uses the short UA and worked.
- **USBR newsroom** (`/newsroom/`, `/newsroom/search?topic=Colorado River`): HTTP 200, but no dated items appear in the server HTML. It looks JS-rendered and was not read. `doi.gov/pressreleases` returned 404; `doi.gov/news` worked.
- **October 2026 24-Month Study:** not published (OCT26_* all 404). **SEP26_MAX** still 404.
- **USDA same-week median:** the 9/28 value of 512.5 is not reproduced. I get 533.3 including 2026, or 521.2 for prior years only. The percentile method does reproduce.
- **Memphis 10/6 and 10/7:** skipped (n=21 < 22).
- **Contargo 9/29–10/7 € rows:** these are mapped onto the 10/9 schedule. Whether that schedule was in force on those dates is not confirmed.
