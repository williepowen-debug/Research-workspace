# Rhine long series: C5 →5 base rate (AEOLUS, 2026-10-31)

**What:** 15-minute stage (W, cm) at Kaub and Duisburg-Ruhrort, 2000-01-01 01:00 to 2026-10-31 14:15 local time (MEZ/MESZ). Pulled from WSV PEGELONLINE's bulk raw-data route at 09:28 ET on 2026-10-31. The route is the "Zeitreihen-Download" modal on `/gast/pegeltabelle`, driven directly. It is a POST to `/gast/download/prepare`, which returns JSON `downloadUrl`, followed by a GET of the zip. The command is `pull_wsv_long_series.sh` in this folder.
- Zip sha256 `f60356dec1375b208f288d58cd1ed4a08ebb6bf7d017d26965e30711f268ed71`, 7,195,546 B. It holds 940,853 readings per station.
- The zip was not committed because it is 7.2 MB. Re-pull it with the script. A later pull will not be byte-identical, because the end date moves and raw data can be revised.
- Licence: DL-DE->Zero-2.0. Quality: `unchecked` raw data (WSV's own label).
- `rhine_daily_means_2000-2026.csv` is derived by `base_rate.py`. Each row is an unrounded local-calendar-day mean plus the count of readings that day.

**Validation against the registered REST-derived values:** 15 day-pairs from 2026 were compared (9/10–12, 9/26–28, 10/10, 10/21–28). 27 of 30 values match to 3 dp. Three differ by 0.010–0.020 cm (Kaub 9/28 +0.015; Duisburg 10/21 +0.010 and 10/22 −0.020), which is consistent with raw-data revision of a single reading. No grade changes. The pre-2026 part reproduces both published record lows on their published dates: Kaub is 25.281 on 2018-10-22 against NNW 25, and Duisburg is 152.969 on 2018-10-23 against NNW 153.

**Result (registered rule: both legs at or below the line on 3 consecutive complete days, unrounded means):**

| Pair (Kaub / Duisburg, cm) | Windows 2000–2025 | Years with ≥1 window (of 26) | 2026 windows |
|---|---|---|---|
| **25 / 153: NNW record lows (REGISTERED)** | **0** | **0** | 43 |
| 30 / 160 | 1 | 1 (2018) | 58 |
| 35 / 170 | 19 | 2 (2018, 2022) | 68 |
| **40 / 180** | 31 | **3 (2003, 2018, 2022)** | 71 |
| 50 / 190 | 53 | 4 (+2011) | 79 |
| 65 / 201: MNW | 111 | 6 | 85 |
| 77 / 227: GlW | 255 | 11 | 102 |

The 3-year result for 40/180 holds for any Kaub line from 38 to 45 and any Duisburg line from 178 to 190. It falls to 2 years (2003 drops out) at Kaub ≤36 or Duisburg ≤176. KB-AEO-230.
