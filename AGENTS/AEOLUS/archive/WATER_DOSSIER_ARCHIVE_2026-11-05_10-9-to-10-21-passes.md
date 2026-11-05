# Water DOSSIER archive: the 10/21, 10/10 and 10/9 passes, rotated 2026-11-05, verbatim

crc32 of the body below: 3329494395

---
### 🔴 10/21 WORKER PASS (dark window 10/10 → 10/21) — Rhine below both NNW lines on every complete day; October 24-Month Study is out; Powell back above 3,520

> **Worker run, PROPOSAL-ONLY. Nothing is scored, fired or resolved here.** Detail: `RUN_REPORT.md` (10/21). Observations: `workbook/SERIES.tsv` +96 rows, `workbook/LOG.tsv` +7 rows. Pulls 22:19–22:24 ET 10/21.

**① RHINE C5 legs** — unrounded daily means, **local CEST calendar day** (all readings carry +02:00; CET switch is 10/25), complete = n ≥ 90/96; frozen NNW Kaub **25** / Duisburg **153** (live API re-read 10/21: 25.0 occ 2018-10-22 / 153.0 occ 2018-10-23, `validFrom` null — **not republished**).

| Date | Kaub mean (n) | Duisburg mean (n) | both ≤? |
|---|---|---|---|
| 10/10 | 7.823 (96) | 145.156 (96) | yes |
| 10/11 | 15.042 (96) | 147.573 (96) | yes |
| 10/12 | 18.906 (96) | 141.812 (96) | yes |
| 10/13 | **19.719** (96) | 143.260 (96) | yes |
| 10/14 | 15.042 (96) | 146.573 (96) | yes |
| 10/15 | 12.677 (96) | 146.958 (96) | yes |
| 10/16 | 9.052 (96) | 142.698 (96) | yes |
| 10/17 | 10.053 (95) | 145.427 (96) | yes |
| 10/18 | 8.781 (96) | 144.260 (96) | yes |
| 10/19 | 12.885 (96) | 137.323 (96) | yes |
| 10/20 | 19.240 (96) | 138.385 (96) | yes |
| 10/21 | 15.146 (96) | 138.844 (96) | yes |
| *10/22* | *18.611 (18) INCOMPLETE* | *144.333 (18) INCOMPLETE* | *skipped* |

10/8 and 10/9 recomputed in the same pull reproduce the stored rows to 3 dp. **No complete day with either leg above its line; all 12 three-day windows 10/8–10/10 … 10/19–10/21 have both legs at/below on all 3 days** — a COUNT, not a grade. Closest approach: Kaub 19.719 (10/13, −5.281 to 25); Duisburg 147.573 (10/11, −5.427 to 153); one instantaneous Duisburg reading of 155 on 10/17 (daily mean 145.427). **WSV forecast (init 10/21 07:00 CEST):** forecast to 10/23 07:00 — Kaub 17 → 20 → 18, Duisburg 136 → 144; *estimate* to 10/25 05:00 — Kaub 25 at 10/24 15:00 → 30; Duisburg 153 at 10/24 15:00 → 160. ⚠️ Instantaneous points, estimate class past 10/23 07:00 — not a daily mean. **Contargo** (table dated 21.10): Kaub 21 / 18 → row 'ab 40 cm' **€1,075/20′**; Ruhrort 138 / 136 → row 140–131 cm **€675/20′** — both unchanged since 10/8.

**② Colorado** — Mead **1,037.18 ft [10/20]** (+2.18 vs 1,035); window high 1,037.71 (10/11), falling 10/12–10/19, flat 10/19–10/20. Powell **3,520.77 [10/20]** (+10.77 vs 3,510); window low 3,518.88 (10/11); **at/above 3,520 on 10/16–10/20 (5 consecutive days)** — state only. Lees Ferry flat 6,540–6,650 cfs 10/9–10/20 (10/10–10/11 missing in NWIS), so **release is not the driver of Powell's rise**; inflow driver NOT verified (hypothesis: Flaming Gorge DROA water and/or October inflow). **October 2026 24-Month Study PUBLISHED** (dated 10/15; run processed 10/8): official = **6 maf** run (`24Month_10_6.pdf`). EOM columns match all 12 USBR actuals Oct-25 → Sep-26 to 0.00 ft. **Mead:** Oct-26 1,035.29 · Nov 1,033.97 · Dec **1,034.52** · 12-month min **1,007.73 (Jul-2027)**. **Powell:** 12-month min **3,516.28 (Feb-2027)**; no end-of-month value below 3,510 in the 24 months. 7 maf alternative: Mead 12-mo min 1,015.68 (May-2027); Powell 24-mo min 3,510.69 (Mar-2028). vs September 6 maf: Mead Dec-26 1,034.18 → 1,034.52; Powell Feb-27 3,511.43 → 3,516.28. ⚠️ End-of-month values only — AEO-10's "at any point" basis is not settled by an EOM table. ⚠️ `lc/region/g4000/24mo.pdf` still serves the JULY study.

**③ Mississippi** — Memphis daily means (UTC day, n ≥ 22): 8.848 [10/10] → peak **9.551 [10/11]** → **3.532 [10/21]** (lowest complete day in the window; falling ~1 ft/day 10/19–10/21). Margin vs `lowThreshold` −8: +11.532. Trough of record in this folder still −4.678 [9/14]. **USDA St. Louis 673.44% = $26.87/t [10/13]**, third weekly decline (834.69 → 758.93 → 723.21 → 673.44); 78.3rd pct of same calendar week (n=23), 93.8th all weeks.

**④ Drought** — USDM CONUS D1–D4 **53.73% [valid 10/13]** (10/6 55.21, −1.48 pp); D4 1.15 → **1.30**. Valid-10/20 map not released at pull (Thursday release).

**⑤ Panama** — Gatún **86.20 ft [10/20]**, +0.94 vs 85.26 [10/9]; same date 2023 79.62 / 2024 87.35 / 2025 87.08. **A-39-2026 (10/21):** Last-Minute Reservation service reinstated at the Panamax Locks; no DRAFT or SLOT-cap change stated; ACP says the watershed deficit persists. October transits not published yet (Monthly Ops due November); September = 32.63/day (A-38, 10/9 block).

### 🔴 10/10 — AEOLUS directly (no worker): Rhine forecast cut, Colorado agreement unsigned + litigation, Panama dry-season base rate

| Item | Read | Source |
|---|---|---|
| **Rhine (C5 →5)** | Still FIRED on 10/7–9. **WSV 10/10 run CUT the rise:** Duisburg peaks **150** (10/11) < 153; Kaub **13** by 10/12 07:00 — no exit in horizon. 10/10 incomplete (n=68): Kaub 6.912 / Duisburg 144.412 | PEGELONLINE W/WV · KB-193 |
| **Mead / Powell** | **1,037.60 / 3,518.97 [10/9]** · October 24MS **not out** at 16:25Z 10/10 | USBR 921/919 · KB-193/202 |
| **Colorado agreements** | Lower Basin implementing agreement **NOT executed** on any primary; **Arizona legislature must approve** (A.R.S. §45-106); **Jan 1, 2027** deadline (secondary); MWD board item **10/27**. 1.25 maf CY2027 cut proceeds (USBR 9/15). **Nevada v. Burgum** (D. Nev. 2:26-cv-02665, filed 8/24) seeks vacatur | dated search 10/10 · KB-202/203 |
| **Two Mead consultation lines** | ROD §10.7 **1,000 ft** vs Guidelines §5.3.A.4 **1,010 ft** — C6 leg 2 re-key proposed | KB-204 |
| **Panama** | Gatún **85.26 ft [10/9]**, rising · strong-El-Niño Oct→Jan–Apr drop median **−3.1 ft** (worst −4.5) → ~82.1 ft (worst ~80.8 vs 2024 low 80.17) | ACP CSV · KB-201 |
| **Paraná / Yangtze** | Rosario **3.22 m [10/10]** = trailing-year MAX · Yangtze **NOT read** (cjh.com.cn timed out 90 s; no substitute) | UNL-FICH · water LOG |
| **USDM (drought)** | CONUS D1–D4 **55.21%** [valid 10/6] (9/29 59.38) · D4 1.15 | USDM API · KB-183 |

### 🔴 10/9 WORKER PASS — the Rhine is still jointly below both NNW levels on every complete day through 10/9, but WSV now forecasts a rise; the 2027-28 Guidelines carry no 10/01 effective date

> **Worker run, PROPOSAL-ONLY. Nothing is scored, fired or resolved here.** Detail + failed commands: `RUN_REPORT.md` (10/9). Observations: `workbook/SERIES.tsv` +93 rows, `workbook/LOG.tsv` +10 rows.

**① RHINE C5 legs** — unrounded daily means, local CEST day, complete = n ≥ 90/96; frozen NNW Kaub **25** / Duisburg **153** (live API re-read 10/9: still 25.0 [occ 2018-10-22] / 153.0 [occ 2018-10-23], **not republished**).

| Date | Kaub mean (n) | Duisburg mean (n) | both ≤? |
|---|---|---|---|
| 10/5 | 6.260 (96) | 130.833 (96) | yes |
| 10/6 | 1.583 (96) | 130.885 (96) | yes |
| 10/7 | 1.323 (96) | 129.979 (96) | yes |
| 10/8 | **0.990** (96) | **138.333** (96) | yes |
| 10/9 | **7.583** (96) | **140.396** (96) | yes |
| *10/10* | *8.727 (11) INCOMPLETE* | *142.091 (11) INCOMPLETE* | *skipped* |

10/5–10/7 reproduce the 10/8-scan rows to 3 dp. **Every complete day 9/18 → 10/9 (22 days) has both legs at/below** — a COUNT, not a grade. **WSV forecast (init 10/9 07:00, to 10/11 07:00):** Kaub 5 → **12**; Duisburg 138 → **peak 154 (instantaneous, 10/10 19:00 – 10/11 01:00)** → 152. **WSV `estimate` (10/11 09:00 → 10/13 07:00):** Kaub 13 → **25 by 10/12 21:00**; Duisburg 152 → 147 → 148. ⚠️ Forecast points are instantaneous, not daily means. Kaub actual ran **4–6 cm above** the 10/9 forecast all afternoon. Contargo's own forecast for Ruhrort (154 / **171** / 157 for 10/10–12) **disagrees** with WSV's ~152 for 10/11 — unreconciled.

**② Contargo** — Kaub row **'ab 40 cm' €1,075/20′** unchanged; **Duisburg eased to the 140–131 cm row, €675/20′** (Ruhrort 133 on 10/8, 140 on 10/9), from €800 on 9/27–28. Statements unchanged: obligation ends (DE page); suspension still **conditional** (EN page) — no statement that services are suspended.

**③ Colorado** — Mead **1,037.61 ft [10/8]**, +2.61 vs 1,035, window low; −0.08 ft/day over 10/4–10/8. Powell **3,519.03 [10/8]**, +9.03 vs 3,510, first decline since 9/27 (peak 3,519.04). **Lees Ferry stepped down 10/01**: ~8,200 → **~6,600 cfs** (10/2–10/8 mean 6,608.6 = **−26.09%** vs 2018-25 same window) — but a late-Sep → early-Oct step is **seasonal** (negative in 6 of 8 years, −22.8% to +17.7%; 2026 −19.3%). Driver not verified. **October 24-Month Study NOT published** (all OCT26 names 404). 🔑 **The 2027-28 Operating Guidelines §3 make effectiveness conditional on executed implementing + parallel agreements — there is NO 10/01 effective date in the text.** No primary found showing those agreements executed (USBR pages: nothing after 8/21; FR: 0 Reclamation documents since 8/1; DOI news: nothing after 8/21). State-agency primaries not registered, not checked.

**④ Panama** — **A-38-2026 (10/9): September TRANSITS 32.63/day** (979; high 37 / low 28) vs Aug 33.19 — **+0.63 vs the ≤32 transit band**. ARRIVALS 31.5. **SLOTS** used/available as printed: Neopanamax 134/125 (107.20%), auctioned 291/339 (85.84%). **A-37-2026 (10/5)**: LoTSA 2027 + cancellation-fee change — no DRAFT or SLOT-cap change. DRAFT still **49.0 ft** (A-36). Gatún **85.23 ft [10/8]** (+0.49 vs 9/27); same date 2023 **79.92** / 2024 86.15 / 2025 86.88.

**⑤ Danube** — **23 of 44** below `LKV_viszony` (19 excluding sentinels) — same count as 9/28, **but OVF rewrote the reference**: 14 stations now sit below LKVs **dated Aug–Sep 2026** (e.g. Budapest −2 vs LKV 0 [2026-09-08]; Mohács −35 vs −29 [2026-09-11]); 9/28's LKVs were 2018-dated (Budapest 33, Mohács 50). Moving-reference register entry 1 in action. Reading time field `Idopont` exists (10/9 17:00Z at 22 stations).

**⑥ Mississippi** — Memphis daily means (UTC day) rose to **11.300 [9/30]**, fell to **3.630 [10/8]** (10/6–10/7 skipped, n=21), 6.570 [10/9]. Trough still −4.678 [9/14]. **USDA St. Louis barge rate 723.21% = $28.86/t [10/6]**, down 2 weeks from 834.69; **69.6th pct of the same calendar week** (n=23), 95.6th all weeks.

