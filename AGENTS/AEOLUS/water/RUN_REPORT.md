# AEOLUS · WATER — worker RUN REPORT

**run_date: 2026-10-29** (worker run: pulls 00:18–00:26 ET; files written 00:27–07:39 ET, per `date`) · spawned for AEOLUS (dark window 10/21 22:30 ET → 10/29; 5 tasked items) · **findings are PROPOSAL-ONLY. AEOLUS adjudicates them.**
*Nothing below is scored, fired, resolved or routed. No source was substituted. No git operations were run. This report supersedes the 10/21 `RUN_REPORT.md`.*

---

## observations_added

**91 rows → `workbook/SERIES.tsv`** (886 → 977 lines) · **12 rows → `workbook/LOG.tsv`** (145 → 157). Both files were checked: LF endings, 0 CR, 7 / 6 fields on every appended row, and no duplicate `(date, instrument)` pairs. `DOSSIER.md`: new 10/29 block at the top; header → `Last real data refresh: 2026-10-28`.

| instrument | rows | dates |
|---|---|---|
| kaub_stage / duisburg_ruhrort_stage | 7 + 7 | 10/22–10/28 (10/19–21 already stored; reproduced to 3 dp) |
| kaub_q / duisburg_ruhrort_q | 10 + 10 | 10/19–10/28 (first Q rows in this folder) |
| contargo_lws_kaub_20ft | 2 | 10/27, 10/28 (Duisburg not written: level above the printed schedule) |
| powell_elev / mead_elev | 7 + 7 | 10/21–10/27 |
| powell_storage | 8 | 10/20–10/27 |
| lees_ferry_q | 6 | 10/21–10/26 (NWIS ends 10/26) |
| usdm_conus_* | 6 | valid 10/20 |
| usda_barge_rate_pct | 7 | 10/20 (7 origins) |
| memphis_stage | 7 | 10/22–10/28 (UTC day) |
| gatun_elev | 7 | 10/21–10/27 |

## threshold_state (state + margin only; NOT graded)

### 1. Rhine C5 →5 — dark-window scan 10/19 → 10/28
Basis: unrounded daily means by LOCAL calendar day (CEST to 10/24, CET from 10/26). Complete = n ≥ 90. **10/25 is a 25-hour day (00:00 CEST → 24:00 CET), n = 100, with all 100 readings averaged** (equal 15-min weights, so the mean is time-weighted). Two alternatives give the same side of both lines: dropping the repeated 02:00–02:45 hour (n = 96; Kaub 31.500 / Duisburg 188.542) and the UTC day (n = 96; 32.438 / 190.010).

| Date | Kaub mean (n) | vs 25 | Duisburg mean (n) | vs 153 | both ≤? |
|---|---|---|---|---|---|
| 10/19 | 12.885 (96) | −12.115 | 137.323 (96) | −15.677 | yes |
| 10/20 | 19.240 (96) | −5.760 | 138.385 (96) | −14.615 | yes |
| 10/21 | 15.146 (96) | −9.854 | 138.844 (96) | −14.156 | yes |
| 10/22 | 19.062 (96) | −5.938 | 144.708 (96) | −8.292 | yes |
| 10/23 | **25.854** (96) | **+0.854** | 146.625 (96) | −6.375 | **no (Kaub)** |
| 10/24 | 23.844 (96) | −1.156 | **159.333** (96) | **+6.333** | **no (Duisburg)** |
| 10/25 | 31.280 (100) | +6.280 | 188.030 (100) | +35.030 | no (both) |
| 10/26 | 54.167 (96) | +29.167 | 208.156 (96) | +55.156 | no (both) |
| 10/27 | 56.625 (96) | +31.625 | 234.844 (96) | +81.844 | no (both) |
| 10/28 | 57.156 (96) | +32.156 | 233.833 (96) | +80.833 | no (both) |
| 10/29 | 59.591 (22) | — | 220.727 (22) | — | INCOMPLETE, skipped |

**Window test (every 3 consecutive complete days):**

| Window | Kaub legs | Duisburg legs | Result |
|---|---|---|---|
| 10/19–21 | ✓✓✓ | ✓✓✓ | both legs all 3 days |
| 10/20–22 | ✓✓✓ | ✓✓✓ | both legs all 3 days |
| **10/21–23** | ✓✓✗ | ✓✓✓ | **FIRST FAILING WINDOW** (Kaub 10/23, +0.854 cm) |
| 10/22–24 | ✓✗✓ | ✓✓✗ | fails; the first window that fails by more than a few cm (Duisburg +6.333) |
| 10/23–25 | ✗✓✗ | ✓✗✗ | fails |
| 10/24–26 | ✓✗✗ | ✗✗✗ | fails |
| 10/25–27 | ✗✗✗ | ✗✗✗ | fails |
| **10/26–28 (3 most recent)** | ✗✗✗ | ✗✗✗ | **both legs above on all 3 days** |

- **The run broke.** The last complete day with both legs at/below was **10/22**. The first failing window, 10/21–23, fails on one leg only, by **0.854 cm**. That is inside the charter's unresolved gaugeZero datum caveat (Kaub gaugeZero `validFrom` 2019-11-01, after the 2018 record). The failure is unambiguous from the 10/22–24 window on (Duisburg +6.3 cm) and across both legs from 10/23–25.
- **First instantaneous readings above the lines:** Kaub 26 at 10/22 23:45 CEST; Duisburg 154 at 10/24 06:45 CEST (last ≤153 at 06:30).
- **Max 15-min readings, 10/19 → 10/29 05:15 CET:** Kaub **61 cm** (10/28 19:15 CET); Duisburg **243 cm** (10/27 21:00 CET). Over 10/19–10/22 the maxima were Kaub 26 and Duisburg 146.
- **NNW not republished:** Kaub NNW 25.0 (occ 2018-10-22) and Duisburg NNW 153.0 (occ 2018-10-23), both with `validFrom` null. GlW is unchanged at 77 / 227.
- **Discharge (daily means, m³/s):**

| | 10/19 | 10/20 | 10/21 | 10/22 | 10/23 | 10/24 | 10/25 | 10/26 | 10/27 | 10/28 |
|---|---|---|---|---|---|---|---|---|---|---|
| Kaub | 491.5 | 518.4 | 501.2 | 517.5 | 546.3 | 537.8 | 569.5 | 669.1 | 680.0 | 682.4 |
| Duisburg | 607.3 | 611.5 | 613.5 (n = 95) | 636.8 | 644.7 | 697.9 | 824.8 | 918.9 | 1,051.6 | 1,046.6 |

- **WSV forecast (init 10/28 07:00 CET; instantaneous points; forecast class to 10/30 07:00, then estimate to 11/01 07:00):** Kaub rises 55 → 60 (10/28 23:00), then falls to 44 (10/30 07:00); the *estimate* reaches **25 at 11/01 01:00** and **23 at 07:00**. Duisburg goes 237 → 212 (10/30 07:00), then the *estimate* falls to **189** (11/01 07:00). If the estimate verifies, Kaub would be back at its line around 11/01 while Duisburg stays about 36 cm above its own.
- **Contargo:** the page table is dated 28.10 and shows only 27.10 and 28.10. Kaub was 56 / 55 cm, which falls in the 60–51 cm row: **€550 per 20′** (€645 per 40′), down from €1,075 on 10/21. Ruhrort was 227 / 240 cm, above the top printed Duisburg row (180–171), so no € row applies. The page also prints tier numbers in brackets (Ruhrort "(3)", Kaub "(6)"); these were not mapped. **No data for 10/22–10/26** is recoverable from this page.

### 2. Colorado — realised levels (USBR 919/49, 921/49; USGS 09380000)

| Date | Powell ft | vs 3,510 | Mead ft | vs 1,035 | Lees Ferry cfs |
|---|---|---|---|---|---|
| 10/20 | 3,520.77 | +10.77 | 1,037.18 | +2.18 | 6,570 |
| 10/21 | 3,521.76 | +11.76 | 1,037.19 | +2.19 | 6,640 |
| 10/22 | 3,523.59 | +13.59 | **1,037.16** | **+2.16 (window min)** | 6,570 |
| 10/23 | 3,525.00 | +15.00 | 1,037.22 | +2.22 | 6,480 |
| 10/24 | 3,526.10 | +16.10 | 1,037.71 | +2.71 | 6,470 |
| 10/25 | 3,527.51 | +17.51 | 1,038.03 | +3.03 | 6,510 |
| 10/26 | 3,528.66 | +18.66 | 1,038.18 | +3.18 | 6,480 |
| 10/27 | **3,530.09** | **+20.09** | **1,038.29** | **+3.29** | (NWIS ends 10/26) |

- **No Mead day at/below 1,035.00. No Powell day at/below 3,510.00.**
- **Trend:** Powell rose +9.32 ft over 10/20 → 10/27, or **+1.33 ft/day**. Daily steps were +0.99 / +1.83 / +1.41 / +1.10 / +1.41 / +1.15 / +1.43. Mead rose +1.11 ft over 7 days (**+0.159 ft/day**), flat through 10/23 and then +0.27 ft/day.
- **Exit-rule states (state only):** Powell has been ≥3,520 on 12 consecutive days (10/16–10/27). Mead is not ≥1,045 on any day.
- **Driver checked, not extrapolated:** the rise comes from a storm inflow pulse that is already receding (see ②). Releases did not change upward: Glen Canyon is flat and Hoover was cut.

### 3. Colorado regime — Lower Basin implementing agreement + *Nevada v. Burgum*

**Agreement (Guidelines §3/§5.9): NO evidence of execution at 10/29.**

| Claim | Tier | Source |
|---|---|---|
| The MWD 10/27 meetings (Special Joint Exec/Board 12:00; Imported Water Subcommittee 10:00) had **no action item to approve or execute a Lower Basin agreement** | PRIMARY | mwdh2o.legistar.com MeetingDetail ID 1456563 and 1455916, plus the agenda PDFs (`View.ashx?M=A&ID=1456563…`, `…ID=1455916…`) |
| MWD 10/27 item 8-1 was a closed-session *"anticipated litigation — deciding whether to initiate litigation; 1 potential case"* (Gov. Code §54956.9(d)(4)). The subject was added 10/19 and tagged (IW). IW also heard oral reports titled "Development of Colorado River Operating Guidelines" and "Report on the Colorado River Board Meeting" | PRIMARY | same |
| **The result of the 10/27 closed session is UNKNOWN.** Legistar action history shows a blank mover, result and vote for every 10/27 item, and the minutes are not posted. The agenda does not name the case | PRIMARY (absence) | Legistar HistoryDetail pages |
| The next MWD board meeting is the Special Joint Exec/Board on 11/10; its agenda is not yet posted | PRIMARY | Legistar calendar |
| CAWCD's 10/27 complaint in intervention describes the 760 / 440 / 50 kaf reductions as "in accordance with a Lower Basin implementing agreement", and says that "absent a consensus agreement" the Secretary apportions. It does **not** say the agreement has been executed | PRIMARY | ECF 35-7 |
| Federal Register: **0** Reclamation documents published since 2026-10-01 | PRIMARY | federalregister.gov API |
| DOI news, page 1 (read 10/29): no Colorado River item | PRIMARY (absence) | doi.gov/news |
| No report of execution in web searches. Arizona joined the Nevada suit on 10/16; ADWR's Buschatzke is quoted as preserving "a path forward to achieving a collaborative outcome" | SECONDARY | thenevadaindependent.com/article/drawing-a-line-in-the-sand-arizona-joins-nevadas-lawsuit-over-colorado-river-cuts · newsfromthestates.com/article/arizona-joins-nevada-lawsuit-over-colorado-river-cuts |
| A Hobbs special session to approve a Lower Basin deal was planned (KJZZ, 9/5). **No source found that it was called or held. No Arizona concurrent resolution under A.R.S. §45-106 was found.** HCR 2038 (February 2026 regular session) backs a SEVEN-state consensus; it is not the §45-106 instrument, and its final status was not confirmed | SECONDARY | kjzz.org/politics/2026-09-05/arizona-republican-lawmakers-request-more-frequent-briefings-on-colorado-river · azleg.gov/legtext/57leg/2R/bills/HCR2038H.htm |

***Nevada v. Burgum*, D. Nev. 2:26-cv-02665-GMN-NJK — every entry after ECF 14** (PRIMARY: CourtListener RECAP docket https://www.courtlistener.com/docket/74688268/state-of-nevada-v-burgum/; page refreshed 10/28 10:48; "Date of Last Known Filing: Oct. 27, 2026"; entries 15–42 are contiguously numbered):

| ECF | Date | Entry |
|---|---|---|
| **15** | 10/16 | **State of Arizona MOTION to Intervene** (as plaintiff) + memorandum; responses due 10/30. Arizona asks for **remand WITHOUT vacatur**, leaving the 2027-28 Guidelines in place; Nevada asks for vacatur. PDF: storage.courtlistener.com/recap/gov.uscourts.nvd.184047/gov.uscourts.nvd.184047.15.0.pdf |
| 16–22 | 10/16 | Arizona pro hac vice petitions (Costa, Dubin, Hammer, Klobas, Ratner, Sadeghi, Wall) |
| 23 | 10/20 | Minute order deferring ECF 19 (signature defect; cure by 10/27) |
| 24–29 | 10/20 (entered 10/21) | Pro hac vice granted for ECF 16, 17, 18, 20, 21, 22 |
| 30 | 10/21 | Summons returned executed on all four federal defendants (SNWA) |
| 31 | 10/21 | Notice of corrected image, ECF 19 |
| 32 | 10/23 | Federal defendants' unopposed motion to extend time to answer (first request) |
| 33 | 10/23 (entered 10/26) | ECF 19 pro hac vice granted |
| **34** | 10/26 | Magistrate Judge Koppe grants ECF 32. **Federal responsive pleading due 2026-12-10** |
| **35** | 10/27 | **Central Arizona Water Conservation District (CAP) MOTION to Intervene** (as plaintiff); responses due 11/10. ECF 35-7 complaint in intervention seeks declaratory relief, plus remand of the 2027-28 Guidelines *"so long as"* they implement the Lower Basin Alternative (Arizona reduction capped at 760 kaf for WY 2027-28), plus an **injunction against action under the Final EIS/ROD *after 2028*** |
| 36–42 | 10/27 | CAWCD pro hac vice petitions |

- **NO preliminary-injunction or TRO motion appears anywhere in ECF 1–42** (a text search of the docket page for "injunct" / "restraining" finds only the complaints' prayers). Per ECF 35, the court had not ruled on Arizona's intervention as of 10/27.
- ⚠️ RECAP is not a PACER mirror; filings after the 10/28 refresh are unknown. PACER was not searched.

### 4. Quick refreshes
| Instrument | Value | Prior | Note |
|---|---|---|---|
| **Gatún** (ACP CSV) | **86.56 ft [10/27]** | 86.20 [10/20] | Same date: 2023 79.63 / 2024 87.47 / 2025 87.92 |
| ACP advisories | **none after A-39-2026 (10/21)** | — | Singular archive index fetched 10/29 00:25 ET; web search also finds no A-40. No DRAFT or SLOTS change. October TRANSITS not yet published (last: September 32.63/day) |
| **Memphis** MEMT1, UTC-day mean (observed level only, no grade) | **−1.709 ft [10/28]** (n = 24) | 3.532 [10/21] | Daily means 2.711 / 2.087 / 1.390 / 0.319 / −0.947 / −1.668 / −1.709 for 10/22–28, flattening; latest obs −1.81 (10/29 03Z). Margin vs `lowThreshold` −8: +6.291. Folder trough still −4.678 [9/14] |
| **USDM** CONUS D1–D4 | **50.67% [valid 10/20]** | 53.73 [10/13] | −3.06 pp; D2–D4 28.68; D3–D4 9.37; D4 **1.19** (from 1.30). Valid-10/27 map is released Thursday 10/29 (after the pull) |
| **USDA barge**, St. Louis | **592.19% = $23.63/t [10/20]** | 673.44 [10/13] | Fourth weekly decline; 73.9th percentile of the same calendar week (n = 23), 90.4th of all weeks (n = 1,183). Same week: 2022 1,818.8 / 2023 577.9 / 2024 753.6 / 2025 493.1. Week of 10/27 not yet published |

## changes (since the 10/21 read)
- **Rhine:** the jointly-below run that held on every complete day from 9/18 ended after **10/22**. Kaub went from 15.1 (10/21) to 57.2 cm (10/28), and Duisburg from 138.8 to 233.8 cm. Discharge rose +36% at Kaub and +71% at Duisburg (10/19 → 10/28). The WSV *estimate* has Kaub falling back to ~23–25 cm by 11/01. Contargo's Kaub surcharge fell from €1,075 to €550 per 20′.
- **Powell:** 3,520.77 → **3,530.09** (+9.32 ft) on a record October inflow pulse.
- **Mead:** 1,037.18 → **1,038.29** (+1.11 ft) from tributary inflow plus the Hoover release cut.
- **Colorado litigation:** two Arizona parties are now moving to intervene against the ROD. The answer deadline moved to 12/10. There is still no PI motion.
- **Panama:** Gatún +0.36 ft. **Memphis:** −5.24 ft (3.53 → −1.71). **USDM:** −3.06 pp. **St. Louis barge:** −81.25 points.

## proposed_findings (PROPOSALS — AEOLUS adjudicates)
1. **Rhine C5 →5 historical window closed.** Both legs were at/below on every complete day from 9/18 through **10/22**. The first 3-day window to fail is **10/21–23**, decided by Kaub at +0.854 cm, which is inside the datum caveat. The robust break is 10/22–24 (Duisburg +6.3 cm), and every window from 10/23–25 on fails on both legs. The 3 most recent complete days (10/26–28) are both-above. *Source: PEGELONLINE W measurements P31D (pulled 10/29 00:19 ET); `water/workbook/SERIES.tsv` 10/19–10/28; LOG 2026-10-23.* Proposed for AEOLUS's grade: the sub-cm margin on the first failing day matters if the exit date is recorded.
2. **Owed #5 answered: Powell's late-October rise is a storm inflow event.** It is not driven by Glen Canyon releases (flat) or Flaming Gorge DROA (release flat ~2,165 cfs). Peak inflow was **63,368 cfs (10/22)**, the second-highest Oct–Nov day since 1963. The **+537,840 af** 7-day storage gain (10/20–27) is the largest Sep–Nov 7-day gain in the 919/17 series. The pulse came from the San Juan below Navajo and the Colorado above Cisco. *Sources: USBR UC hydrodata 919/29, 919/42, 919/17, 917/42, 920/29, 920/42, meta.csv; USGS NWIS 09379500, 09180500, 09315000.* ⚠️ Provisional data. The pre-10/21 slow rise (10/12–20) is still only partly explained, and whether the ~2,165 cfs Flaming Gorge release is DROA-designated was not checked.
3. **Two Arizona plaintiffs have moved to intervene against the ROD in *Nevada v. Burgum*:** Arizona (ECF 15, 10/16; remand without vacatur) and CAWCD (ECF 35, 10/27; conditional remand plus an injunction after 2028). There is **no PI motion through ECF 42**, and the federal answer is due 12/10. *Source: CourtListener RECAP docket 74688268 and the ECF 15 / 35 / 35-7 PDFs.* This bears on the C6 milestone band's Orange PI leg (not met on this record) and on the likelihood of agreement execution (AEOLUS's call).
4. **Lower Basin implementing agreement: no execution found.** MWD 10/27 had no approval item and held a closed session on whether to initiate litigation (outcome unknown). No Arizona §45-106 resolution or special session was found. *Primary sources: MWD Legistar; ECF 35-7; FR API. Secondary: Nevada Independent, KJZZ.* Yellow opens 11/02 under the 10/10 re-key.

## gaps (what failed or could not be verified)
| Item | Exact failure / limit |
|---|---|
| USBR newsroom | `curl https://www.usbr.gov/newsroom/news-releases` → exit code 56, HTTP 000 (`/newsroom/` the same); `news-release/5410` → HTTP 500; WebFetch `https://www.usbr.gov/newsroom/` → "HTTP 500 Internal Server Error". **No Reclamation release was read.** |
| ADWR news (`https://www.azwater.gov/news`) | curl → HTTP 403; WebFetch → "HTTP 403 Forbidden" |
| Arizona legislature special session / §45-106 resolution | Not found in searches; azleg special-session listing not parsed (`?SessionID=133` returned 200 but was not read) |
| MWD 10/27 closed-session outcome | Legistar results blank, minutes not posted |
| CourtListener API | `/api/rest/v4/…` → HTTP 401 "Authentication credentials were not provided." The HTML docket page was used instead (200). Internet Archive docket.xml → 404. ECF 16–30 PDFs → 404 (not in RECAP); docket text read instead |
| Contargo 10/22–10/26 | Not on the page; the page carries only the two most recent dates |
| Lees Ferry 10/27 | Not yet in the NWIS dv return |
| Mead inflow | `reservoir_data/921/csv/29.csv` returns an HTML error page (no Mead inflow datatype) |
| USBR hydrodata directory listings (`reservoir_data/919/` etc.) | HTTP 403. Site names were resolved from `reservoir_data/meta.csv` instead (917 = Flaming Gorge, 920 = Navajo; 914 = Morrow Point, not used) |
| USDM valid 10/27; USDA week of 10/27; October ACP Monthly Ops | Not yet released at pull time |
| Upstream gauge gaps | NWIS dv: Green River 09315000 has no 10/25 value; San Juan 09379500 has no 10/23; Little Colorado 09402000 has no 10/22–10/23 |
| Precipitation cause of the Colorado storm | Not investigated |
| NOT tasked / not pulled | Yangtze, Danube, Paraná, St. Louis, Vicksburg/Cairo, CBS, heating oil, Maxau/Worms/Mainz/Emmerich, 24-Month Study (November study not checked) |
| Instrument names not available | Powell inflow, Navajo/Flaming Gorge release, tributary flows and Hoover release went to LOG.tsv only. They are not SERIES instruments; AEOLUS approval is needed to add them |

## files changed
- `AGENTS/AEOLUS/water/workbook/SERIES.tsv` (+91 rows, appended)
- `AGENTS/AEOLUS/water/workbook/LOG.tsv` (+12 rows, appended)
- `AGENTS/AEOLUS/water/DOSSIER.md` (as-of line, two-clock header, new 10/29 block)
- `AGENTS/AEOLUS/water/RUN_REPORT.md` (overwritten; this file)
