# AEOLUS · WATER — live dossier

**As-of: 2026-11-05 (11/05 worker freight-evidence pass, block below; tasked subset: Rhine six-station stage and discharge · WSV forecast · CBS · Contargo notices · heating oil · operational search · Powell inflow attribution · Yangtze retry, failed) · 2026-10-29 (10/29 worker dark-window pass, block below; tasked subset: Rhine 6c scan 10/19→10/28 + NNW + WSV forecast + Contargo + Kaub/Duisburg Q · Mead/Powell/Lees Ferry + Powell inflow driver (owed #5) · Colorado agreement + *Nevada v. Burgum* docket + MWD 10/27 · Gatún + ACP advisories · Memphis · USDM · USDA barge. NOT re-pulled: Yangtze, Danube, Paraná, St. Louis, Vicksburg/Cairo, CBS, heating oil, Maxau/Worms/Mainz/Emmerich, 24-Month Study) · 2026-10-21 (10/21 worker dark-window pass; tasked subset: Rhine 6c scan + NNW + WSV forecast + Contargo · Mead/Powell/Lees Ferry + October 24MS · Memphis · USDA barge · USDM · Gatún + ACP advisories. NOT re-pulled: Yangtze, Danube, Paraná, St. Louis, Vicksburg/Cairo, CBS, heating oil, Maxau/Worms/Mainz/Emmerich, Q series) · 2026-10-10 (10/10 block, AEOLUS directly) · 2026-10-09 worker pass below** *(worker pass 10/9, tasked subset: Rhine C5 legs + WSV forecast · Contargo · Mead/Powell/Lees Ferry · Colorado policy clock + Oct 24-MS · Panama (A-37/A-38, Gatún) · Danube LKV · Memphis + USDA barge. NOT re-pulled this pass: USDM, Yangtze, Paraná, St. Louis, Vicksburg/Cairo, CBS, heating oil, Maxau/Worms/Mainz/Emmerich. The 10/9 block below SUPERSEDES the 9/28 block for the instruments it covers.)* *(Prior as-of line, kept: As-of 2026-09-28 — DARK-WINDOW worker pass 9/28 — every instrument re-pulled at its primary except snowpack (seasonally empty); Mississippi Vicksburg (VCKM6) / Cairo (CIRI2) NWPS IDs RESOLVED from the NWPS listing, not yet registered. The 9/28 block below SUPERSEDES the 9/18 block where they overlap; older blocks are history — read the section dates.)* *(Prior as-of line, kept: As-of 2026-09-18 *(FULL worker pass 9/18 — every instrument in this folder re-pulled at its primary except snowpack (seasonally empty) and the Yangtze (not tasked). Section blocks below dated 8/27 or 9/11 are SUPERSEDED by the 9/18 block unless they say otherwise — read the section dates).* All figures primary (USBR 24-Month Study / USBR hydrodata / USGS NWIS / WSV-PEGELONLINE / NOAA-NWPS / ACP / OVF / UNL-FICH / USDM API).)*

> **Last real data refresh: 2026-11-05**  ·  **Dossier written: 2026-11-05**

### 🔴 11/05 AEOLUS DIRECT PASS (no worker)
**① Rhine FIRED the 40/180 key on complete days 11/02–04:** Kaub 19.104 / 18.010 / 22.260, Duisburg 168.979 / 161.427 / 154.427 (KB-237). **② Colorado:** milestone YELLOW on the letter 11/02; Powell 3,535.89, Mead 1,039.29 [11/04]; second inflow pulse 53,324 cfs [11/04]; no PI motion (KB-238). **③ Others:** Memphis −4.179 [11/04], Rosario 4.04 m, Danube above LKV at five gauges, Gatún 87.08 [11/04], USDM D1–D4 43.98% [11/03] (KB-241). ⚠️ Yangtze not refreshed: site timed out.
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*

### 🔴 11/05 WORKER PASS: does the Rhine low water reach freight? The free record goes dark at 10/30

> **Worker run, PROPOSAL-ONLY. Nothing is scored, fired or resolved here.** Detail: `RUN_REPORT.md` (11/05). `workbook/SERIES.tsv` +92 rows, `workbook/LOG.tsv` +30 rows. Pulls 11:54–12:01 ET 11/05.

**Answer as far as the sources go:** gauge state is severe and getting worse. Surcharges are at the top of Contargo's table, but they are set by the gauge, so they are not independent evidence. Reduced loads are reported for the Upper Rhine through 10/30. **No source of any kind describes cargo on 11/02–11/05**, and no plant or refinery warning dated since 10/28 was found.

| Class | What exists | Latest date covered | Basis |
|---|---|---|---|
| **Gauge state** | Kaub 18–22 cm, Duisburg 154–169 cm, Emmerich 7 cm, Köln 69 cm | 11/04 (11/05 partial) | PRIMARY, WSV, Contargo table |
| **Price or surcharge** | Contargo Kaub €1,075 / Ruhrort €335 per 20′. Hapag-Lloyd table ends at Kaub 25, so 18–22 is "individual agreement" | 11/05 | PRIMARY for Contargo; SECONDARY for Hapag (its page returned 403) |
| **Price, market** | Tanker: Lower Rhine unchanged 10/26–30, Basel up, Frankfurt and Karlsruhe eased. No €/t. CBS 2026-Q3 **not printed** | 10/30 | SECONDARY trade |
| **Reduced load** | "by Thursday loads to Upper Rhine destinations were limited, depending on barge size" (Kaub 52 then 41 cm, above today) | 10/30 | SECONDARY trade, no tonnage |
| **Demonstrated halt or cargo loss** | Nothing dated since 10/28. Before it: "most barges stayed near the ARA, or went no further than Duisburg and Cologne" (10/16 post); MSG 14 ships for 3 (10/02) | 10/21 | SECONDARY, context only |
| **Downstream supply** | Swiss diesel stock release 45,000 m³, 10/23–11/22. Trigger stated as pipeline delays from rain in southern France, with Rhine low water as the months-long background | live to 11/22 | PRIMARY, mixed cause |

**Contargo, page table 05.11.2026, verbatim:** *"Wir müssen Sie darauf hinweisen, dass für Pegelstände kleiner gleich 30 cm in Emmerich, 180 cm in Duisburg-Ruhrort, 105 cm in Köln und 80 cm in Kaub unsere Transportverpflichtung endet. Dennoch versuchen wir alles uns Mögliche, um Ihre Container zu transportieren."* All four gauges are inside those lines (2 / 153 / 69 / 18). This is standing text keyed to the gauge. The obligation ended; service did not stop. No suspension text is on the page.

**Named-company search since 10/28:** BASF's Q3 release (10/28) has no mention of Niedrigwasser, Rhein or Logistik and raises the outlook; it covers the quarter to 9/30 and the call was not read. Covestro, thyssenkrupp, Shell Rheinland, Evonik, Lanxess, GKM and Karlsruhe coal: **searched, nothing found. That is a result, not proof of no impact.** Whether Covestro's August force majeure at Dormagen was lifted is unknown. WSV and GDWS notices: none found, ELWIS NfB only partly read.

**Discharge, daily means (m³/s), complete days:**

| | 10/29 | 10/30 | 10/31 | 11/01 | 11/02 | 11/03 | 11/04 |
|---|---|---|---|---|---|---|---|
| Maxau | 410 | 372 | 386 | 395 | 396 | 405 | 411 |
| Worms | 502 | 472 | 441 | 437 | 440 | 445 | 445 |
| Mainz | 623 | 574 | 535 | 502 | 492 | 500 | 495 |
| Kaub | 661 | 612 | 573 | 536 | 518 | 513 | 531 |
| Duisburg | 954 | 903 | 853 | 795 | 739 | 706 | 677 |
| Emmerich | 1,016 | 945 | 898 | 836 | 785 | 739 | 703 |

**No discharge history exists in the long-series files** (stage only), and WSV characteristic values for Q came back empty, so the 2018 and 2022 discharge comparison cannot be made. Stage on the same dates, 11/02–04: Kaub 19.1 / 18.0 / 22.3 against 2018 58.9 / 55.6 / 55.3 and 2022 131.1 / 125.9 / 124.2; Duisburg 169.0 / 161.4 / 154.4 against 189.9 / 185.1 / 188.1 and 286.9 / 278.1 / 275.4. The datum caveat applies. This is a same-date low, not a 2026 low: 2026 stands at Kaub −4.8 [10/01], Duisburg 121.4 [9/29]. Discharge is above the 10/19 values (Kaub 491.5, Duisburg 607). **WSV forecast, init 11/05 07:00:** Kaub 16 on 11/07, then estimate 5–8 by 11/08–09; Duisburg 150–155; Emmerich 1–3. Instantaneous points. Emmerich's published NNW of −1 is already undercut (SERIES −21.8 on 9/27).

**Powell second pulse, a storm pulse (evidenced):** dam releases flat while unregulated gauges jumped together 11/01–03, and press reports heavy rain in the Four Corners. Gauge sum 11/03 51,437 cfs: San Juan near Bluff 58%, Colorado near Cisco 30%, Green 9%. Navajo stored its share (inflow 52,053 cfs on 11/02, release 250). **Not a clean recession:** Cisco is down to 6,710 from 17,700, but Bluff fell to 20,800 on 11/04 and rebounded to about 31,000 on 11/05; the cause is not established. No USBR data newer than 11/04 at 12:01 ET: Powell 3,535.89 (+25.89 vs 3,510), Mead 1,039.29 (+4.29 vs 1,035). Inflow 53,324 is the 5th-highest October–November day since 1963. Do not extrapolate the rate.

**Others:** fastenergy read, confounded, seven states in SERIES. Yangtze retry failed (curl rc 28, 45 s). No source substituted.

### 🔴 10/29 WORKER PASS (dark window 10/21 → 10/29) — the Rhine joint-below run BROKE on 10/23; a record October storm lifted Powell 9.3 ft in a week; Arizona and CAP have moved to join *Nevada v. Burgum* (no PI motion)

> **Worker run, PROPOSAL-ONLY. Nothing is scored, fired or resolved here.** Detail: `RUN_REPORT.md` (10/29). Observations: `workbook/SERIES.tsv` +91 rows, `workbook/LOG.tsv` +12 rows. Pulls 00:19–00:25 ET 10/29.

**① RHINE C5 legs** — unrounded daily means by LOCAL calendar day; complete = n ≥ 90. **10/25 (CEST→CET) is a 25-hour day, n = 100; all 100 readings averaged** (time-weighted); the 96-reading and UTC-day alternatives land on the same side of both lines. NNW re-read 10/29: Kaub 25.0 [occ 2018-10-22] / Duisburg 153.0 [occ 2018-10-23], `validFrom` null — **not republished**.

| Date | Kaub mean (n) | Duisburg mean (n) | both ≤? |
|---|---|---|---|
| 10/19 | 12.885 (96) | 137.323 (96) | yes |
| 10/20 | 19.240 (96) | 138.385 (96) | yes |
| 10/21 | 15.146 (96) | 138.844 (96) | yes |
| 10/22 | 19.062 (96) | 144.708 (96) | yes |
| 10/23 | **25.854** (96) | 146.625 (96) | **no — Kaub +0.854** |
| 10/24 | 23.844 (96) | **159.333** (96) | **no — Duisburg +6.333** |
| 10/25 | 31.280 (100) | 188.030 (100) | no — both |
| 10/26 | 54.167 (96) | 208.156 (96) | no — both |
| 10/27 | 56.625 (96) | 234.844 (96) | no — both |
| 10/28 | 57.156 (96) | 233.833 (96) | no — both |
| *10/29* | *59.591 (22) INCOMPLETE* | *220.727 (22) INCOMPLETE* | *skipped* |

10/19–10/21 reproduce the stored rows to 3 dp. **3-day windows:** 10/19–21 and 10/20–22 have both legs at/below on all 3 days; **the first failing window is 10/21–23** (Kaub leg only, by 0.854 cm, inside the datum caveat); the first to fail by more than a few cm is 10/22–24 (Duisburg +6.333); every window from 10/23–25 on fails on both legs. **Most recent 3 complete days (10/26–28): both legs above on all 3.** Last joint-below complete day: **10/22**. Max 15-min readings: Kaub **61** (10/28), Duisburg **243** (10/27). Discharge (daily means): Kaub 491 → **682 m³/s**, Duisburg 607 → **1,047 m³/s** (10/19 → 10/28). **WSV forecast (init 10/28 07:00 CET):** Kaub peaks 60, then falls to 44 by 10/30 07:00; the *estimate* reaches **25 at 11/01 01:00 → 23**; Duisburg falls 237 → 212 → *estimate* **189** (11/01 07:00). Instantaneous points, not daily means. **Contargo (28.10):** Kaub 56/55 → row 60–51 cm **€550/20′** (from €1,075); Ruhrort 227/240 is above the top printed row (180 cm), so no Duisburg € row applies. Days 10/22–26 are not on the page.

**② Colorado** — **Powell 3,530.09 [10/27]** (+20.09 vs 3,510), +9.32 ft since 10/20 (+1.33 ft/day); ≥3,520 on every day 10/16–10/27 (12 consecutive days) — state only. **Mead 1,038.29 [10/27]** (+3.29 vs 1,035); window minimum 1,037.16 [10/22]; +1.11 ft over 7 days. No day was at/below either line. **Driver (owed #5, answered at primaries): a storm INFLOW event, not releases or DROA.** Powell inflow (USBR 919/29) went from 8,696 cfs (10/20) to a peak of **63,368 cfs (10/22)**, the second-highest October–November day since 1963. Storage rose **+537,840 af in 7 days**, the largest 7-day Sep–Nov gain in the series. Sources: San Juan near Bluff (to 33,800 cfs) and the Colorado near Cisco (to 12,800). Glen Canyon release stayed flat at ~6,550 cfs, Flaming Gorge release flat at ~2,165 cfs, and Navajo stored its upper-San-Juan peak (44,238 cfs inflow, ~263 cfs release). **Mead's rise has two drivers, split not computed:** Grand Canyon tributary inflow (gauge near Grand Canyon 7,460 → 23,800 cfs; Little Colorado; Virgin) and a cut in Hoover release (9,474 → 5,278 cfs). The pulse is receding, so **do not extrapolate the rate**.

**③ Colorado regime** — **Lower Basin implementing agreement: NO evidence of execution** (detail and tiers in RUN_REPORT §3). MWD's 10/27 agendas had **no approval item**. The only related item was a closed-session "deciding whether to initiate litigation; 1 potential case" (IW-tagged); its result is not posted. No Arizona special session or §45-106 resolution was found (SECONDARY). ***Nevada v. Burgum* (ECF 15–42):** **Arizona moved to intervene as plaintiff 10/16** (ECF 15), seeking remand **without** vacatur. **CAWCD (CAP) moved to intervene 10/27** (ECF 35); it seeks remand conditioned on the 760 kaf Lower Basin split, plus an injunction against action under the ROD **after 2028**. The federal answer is now due **12/10** (ECF 34). **No preliminary-injunction or TRO motion through ECF 42** (last known filing 10/27).

**④ Quick refreshes** — Gatún **86.56 ft [10/27]** (same date 2023 79.63 / 2024 87.47 / 2025 87.92); no ACP advisory after A-39 (10/21). Memphis UTC-day mean **−1.709 ft [10/28]**, down from 3.532 [10/21]; margin vs −8 is +6.291 (observed level only). USDM CONUS D1–D4 **50.67% [valid 10/20]** (−3.06 pp); D4 1.19. USDA St. Louis **592.19% = $23.63/t [10/20]**, the fourth weekly decline; 73.9th percentile of the same week (n = 23).

### ⬇️ ROTATED 2026-11-05: the 10/21, 10/10 and 10/9 passes → `../archive/WATER_DOSSIER_ARCHIVE_2026-11-05_10-9-to-10-21-passes.md`, verbatim.

## ROTATED 2026-10-10 — older passes and the standing sections
Verbatim → `../archive/WATER_DOSSIER_ARCHIVE_2026-10-10_9-28-pass-to-sec5.md` (crc in its banner). **Grep it; never re-derive from memory.** It holds: the 9/28 dark-window pass · 9/11 drain refresh · 9/18 full pass (September 24MS, Rhine window) · §1 drought (USDM split geography, "same dataset, opposite verdicts") · §2 Colorado system (Powell↔Mead coupling **measured**, the base-rate contamination note, the hydropower leg, the **Final-EIS shortage matrix**, the unmodelled inflow term, "**El Niño does NOT refill the Colorado**") · §3 river navigation (8/13 six-station Rhine read, the WSV forecast instrument, the 8/13 trigger re-spec, **other watched rivers** with their reference levels) · §4 snowpack/groundwater · §5 water as an AI-siting constraint.
**Standing facts a worker needs without opening it:** Powell↔Mead are ONE coupled system — never two witnesses · El Niño gives no reliable Upper-Colorado snowpack lift · Rhine graded on unrounded means only · Danube LKVs reset in 2026 (OVF) · Paraná reference = Rosario trailing-year percentile (no published plane) · St. Louis has no reference plane (no adjective).

## STANDING RULES (hot pointer — added 2026-10-21, DAEDALUS refresh item 6; text unchanged, source in archive)

⛔ **NO MISSISSIPPI THRESHOLD MAY BE GRADED** (AEOLUS, 2026-09-18) until the measurement basis is a structural column rather than a `notes` string. Three surfaces report on three silently different bases (Memphis instantaneous latest · Memphis `stageflow/observed` daily mean · St. Louis 08:00 spot). Carry the band as an **OBSERVED LEVEL ONLY**. Full text, verbatim: `archive/WATER_DOSSIER_ARCHIVE_2026-10-10_9-28-pass-to-sec5.md` lines 121–132 + the 9/18 addendum.

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
