# AEOLUS · WATER — live dossier

**As-of: 2026-10-10 (10/10 block, AEOLUS directly) · 2026-10-09 worker pass below** *(worker pass 10/9, tasked subset: Rhine C5 legs + WSV forecast · Contargo · Mead/Powell/Lees Ferry · Colorado policy clock + Oct 24-MS · Panama (A-37/A-38, Gatún) · Danube LKV · Memphis + USDA barge. NOT re-pulled this pass: USDM, Yangtze, Paraná, St. Louis, Vicksburg/Cairo, CBS, heating oil, Maxau/Worms/Mainz/Emmerich. The 10/9 block below SUPERSEDES the 9/28 block for the instruments it covers.)* *(Prior as-of line, kept: As-of 2026-09-28 — DARK-WINDOW worker pass 9/28 — every instrument re-pulled at its primary except snowpack (seasonally empty); Mississippi Vicksburg (VCKM6) / Cairo (CIRI2) NWPS IDs RESOLVED from the NWPS listing, not yet registered. The 9/28 block below SUPERSEDES the 9/18 block where they overlap; older blocks are history — read the section dates.)* *(Prior as-of line, kept: As-of 2026-09-18 *(FULL worker pass 9/18 — every instrument in this folder re-pulled at its primary except snowpack (seasonally empty) and the Yangtze (not tasked). Section blocks below dated 8/27 or 9/11 are SUPERSEDED by the 9/18 block unless they say otherwise — read the section dates).* All figures primary (USBR 24-Month Study / USBR hydrodata / USGS NWIS / WSV-PEGELONLINE / NOAA-NWPS / ACP / OVF / UNL-FICH / USDM API).)*

> **Last real data refresh: 2026-10-10**  ·  **Dossier written: 2026-10-10**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*

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

## ROTATED 2026-10-10 — older passes and the standing sections
Verbatim → `../archive/WATER_DOSSIER_ARCHIVE_2026-10-10_9-28-pass-to-sec5.md` (crc in its banner). **Grep it; never re-derive from memory.** It holds: the 9/28 dark-window pass · 9/11 drain refresh · 9/18 full pass (September 24MS, Rhine window) · §1 drought (USDM split geography, "same dataset, opposite verdicts") · §2 Colorado system (Powell↔Mead coupling **measured**, the base-rate contamination note, the hydropower leg, the **Final-EIS shortage matrix**, the unmodelled inflow term, "**El Niño does NOT refill the Colorado**") · §3 river navigation (8/13 six-station Rhine read, the WSV forecast instrument, the 8/13 trigger re-spec, **other watched rivers** with their reference levels) · §4 snowpack/groundwater · §5 water as an AI-siting constraint.
**Standing facts a worker needs without opening it:** Powell↔Mead are ONE coupled system — never two witnesses · El Niño gives no reliable Upper-Colorado snowpack lift · Rhine graded on unrounded means only · Danube LKVs reset in 2026 (OVF) · Paraná reference = Rosario trailing-year percentile (no published plane) · St. Louis has no reference plane (no adjective).

## OPEN QUESTIONS / GAPS

*(Refreshed 2026-08-27. New items 11-14 below; items 1-10 are the 8/21 list, kept for continuity.)*

11. ✅ **RESOLVED 8/27 — Mississippi/Ohio gauge + low-water reference.** NWS AHPS `MEMT1` (Memphis) gives a live stage AND a published `lowThreshold` (−8 ft); current margin 20.47 ft, not stressed. See §3. **AEOLUS: approve instrument name(s) — proposed `memphis_stage` / `batonrouge_stage` / `stlouis_stage` / `memphis_q` — before the worker can log to SERIES.tsv.**
12. ✅ **RESOLVED 8/27 — Panama Gatun Lake elevation.** A 61-year daily CSV + forward projection exist at a live ACP host (`evtms-rpts.pancanal.com`), found via the site's own nav menu, not the dead Tableau URL. Current 83.80 ft (8/26), inside the 82-87 ft normal range but 1.22 ft below the one prior spot-anchor (85.02 ft, 8/2024). **AEOLUS: approve `gatun_elev` (ft) before the worker can log to SERIES.tsv — this is the highest-value open item this folder has closed.**
13. **🆕 The Gatun projection CSV and A-29-2026's published draft-step dates DISAGREE by 8-10 days** (CSV models 48.0 ft ~9/12-13 and 47.5 ft ~10/9; the Advisory states 9/2 and 10/1). **AEOLUS owns which is binding for AEO-04 grading.**
14. **🆕 C5 3-day grade (8/25-27): FAIL/FAIL/FAIL on both legs**, Duisburg-Ruhrort now at its highest reading in this folder's record (194.146 cm, 8/27). The trigger is not close; **AEOLUS decides whether the 11-day near-miss run (8/09-19, reported 8/21) remains relevant context or should be treated as fully closed.**

---

*(8/21 list below, superseded items retained for history.)*

1. ✅ **RESOLVED — Powell record break.** First print below 3,519.92 was **2026-08-15 (3,519.91)**; 8/20 is **3,519.20**, 0.72 ft through. **AEO-06 is AEOLUS's to grade — the worker did not fire it.**
2. **🔴 STILL OPEN — base-rate USBR's 24-month-study projection error.** AEO-10's confidence still rests on a 2.1 ft buffer with **no error bar**. ⚠️ **The August 2026 24-Month Study was released with the 8/21 ROD** — it is the natural input, but **no 24-Month-Study URL is registered in `SOURCES.md`**, and the URLs tried on 8/21 returned **HTTP 404**. **Register a primary before the next attempt** (same class of blocker as the 8/13 Yangtze/Danube/Paraná gap).
3. **Track Lees Ferry weekly** — still the leading indicator for Mead. **Deficit is a flat LEVEL, not a deteriorating slope**: −42.4% (8/01–12) → −41.5% (8/13–20), both against like-for-like same-calendar-window 2018-25 baselines.
4. ✅ **RESOLVED — ROD watch.** **Signed 2026-08-21**, ~6 weeks ahead of the ~10/1 target and 9 days ahead of the ~8/30 earliest-legal estimate. **New downstream question: what does the 2027–2036 Decision Framework do to the shortage-tier instrument this folder tracks?** The old tier language may not be the operative instrument after 12/31/26.
5. ✅ **RESOLVED — Panama current-month summary retrieved.** Jul-2026 data (A-26-2026) = **34.03 transits/day**, plus a Mar→Jul series. **New open item: does the threshold table re-base off the 38.70 April anchor**, now shown to be the window maximum?
6. ✅ **RESOLVED — Yangtze / Danube / Paraná** all pulled at registered primaries on 8/21. **New sub-question: the Danube's upper-vs-lower divergence** (Vác/Budapest recovered while Mohács deepened to −66) — one river, two directions.
6b. **STILL OPEN — Mississippi has a working primary but no registered instrument name.** Unchanged from 8/13. ⚠️ **Sep–Nov is the Mississippi window** — this needs a name before autumn, not after.
7. **Upper-Basin snowpack for winter 2026-27** — the dipole-pivot guard. Snowpack is **correctly empty in August**, not a gap.
8. **🆕 A binding operational restriction now exists at Panama** (A-29-2026 booking slots 34→32) **while realised transits sit at 34.03/day, above the Yellow band.** **AEO-04's spec says it resolves on a binding transit/draft RESTRICTION — this is one, but it is a SLOT cap, not a transits reading.** AEOLUS owns whether the spec's leg (a) is satisfied.
9. **🆕 `SOURCES.md` needs three corrections**, all found on 8/21 — the USDM state-cut recipe, the Colorado policy-clock URL, and the ACP advisories index path. **Details + exact working commands in `RUN_REPORT.md`. Worker does not edit `SOURCES.md`.**
10. **🆕 Reconcile the 8/13 trade-press rejection against the ROD's actual AZ 760 / CA 440 / NV 50 kaf.** See §2. **AEOLUS owns this.**
