# TOUR-03 instrument test — US–Canada airline SEATS (fork of MARCO s32, 2026-10-14 21:06–21:10 EDT)

**Scope:** find a free primary monthly seat series for US–Canada air routes, take a dated 2025-vs-2026 read, and propose the TOUR-03 letter. No repo file was written. Downloads are in `scratchpad/t3dl/` (`fje_CA_{2023..2026}.csv`, outputs `calc_out.txt`, `gaps_out.txt`, `holes_out.txt`). Scripts are in `scratchpad/t3scripts/` (`fje_pull.py`, `fje_calc.py`, `fje_gaps.py`, `fje_holes.py`).

## 1. Source — ✅ ADOPTABLE (with a mandatory hole check)

**BTS T-100 International Segment (All Carriers)**, transtats table code **`FJE`**. The form header reads "Air Carriers : T-100 International Segment (All Carriers)". The table includes foreign carriers (CARRIER_GROUP 0: Air Canada, Jazz, Rouge, WestJet, Porter, Flair, Transat).

| Step | URL / fields | HTTP |
|---|---|---|
| Table index | `https://www.transtats.bts.gov/Tables.asp?QO_VQ=EEE` (lists FJE, FMF, GED, GEE, FJD, FMG) | 200 |
| Form GET | `https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FJE&QO_fu146_anzr=Nv4%20Pn44vr45` → "Latest Available Data: **July 2026**" | 200 |
| Form POST (same URL) | echo `__VIEWSTATE` / `__VIEWSTATEGENERATOR` / `__EVENTVALIDATION`; `__EVENTTARGET`/`__EVENTARGUMENT`/`__LASTFOCUS` = ""; `cboGeography=Canada`, `cboYear=<YYYY>`, `cboPeriod=All`, `btnDownload=Download`; field checkboxes `=on`: DEPARTURES_SCHEDULED, DEPARTURES_PERFORMED, **SEATS**, PASSENGERS, UNIQUE_CARRIER, UNIQUE_CARRIER_NAME, REGION, CARRIER_GROUP, CARRIER_GROUP_NEW, ORIGIN, ORIGIN_CITY_NAME, ORIGIN_COUNTRY, DEST, DEST_CITY_NAME, DEST_COUNTRY, YEAR, MONTH, CLASS. Browser UA plus a cookie jar; no key | 200, `application/zip`, ~2 s per year |

Returns `T_T100I_SEGMENT_ALL_CARRIER.csv`. Row counts: 2023 18,373 · 2024 19,388 · 2025 18,921 · 2026 10,231 (Jan–Jul). The Canada filter captures **both directions** (CA→US 9,743 / US→CA 9,645 rows in 2024). Measure used: **CLASS F (scheduled passenger) SEATS**. F+L (adding charters) moves every figure by ≤0.3pp; P and G are cargo. **Lag is about 2.5 months**, not 6: July 2026 was available on 10/14.

### ⚠️ The series has CARRIER-MONTH HOLES. Grading it raw is wrong.
Foreign-carrier filings are sometimes missing for a whole month and show as zero, with no error. Holes are defined as a zero month between neighbours above 5k seats; "trailing" means the newest month.

| Hole | Neighbours | Effect if graded raw |
|---|---|---|
| **2025-06 Jazz (QK)** | May 295,226 / Jul 318,536 | June-2025 BASE understated by ~307k |
| **2026-06 Air Canada mainline (AC)** | May 643,849 / Jul 575,777 | June 2026 reads −9.92%; hole-filled it is **+0.45%** |
| **2026-07 Porter PD + P3 (trailing)** | Jun 98,208 + 81,822 | July 2026 reads −4.77%; with Porter = Jun-26 it is **+0.73%** |

Genuine exits are correctly *not* flagged as holes because they stay at zero: **Lynx (Y9)** goes to zero from Mar-2024 (ceased Feb-2024 ✓); **Air Transat (TS)** winds down to 7,761 in May, 1,460 in Jun and 0 in Jul-2026 (US exit 6/30 ✓).
**Rule for any adoption:** run the hole scan on every pull. Fill interior holes with the mean of the neighbouring months and trailing holes with the prior month, **flagged**. Re-pull later vintages, because foreign filings may backfill.

## 2. Read (class F seats, all carriers, both directions; hole-filled unless marked raw)

**Winter season Nov–Mar** (the FL snowbird leg; **no holes inside these windows**):

| Basis | 2023-24 | 2024-25 | **2025-26** | 25-26 vs 24-25 | vs 23-24 |
|---|---|---|---|---|---|
| ALL | 15,197,008 | 15,061,509 | **13,399,803** | **−11.03%** | −11.83% |
| Canadian/foreign carriers | 11,098,140 | 10,921,037 | 9,317,225 | **−14.69%** | −16.05% |
| US carriers | 4,098,868 | 4,140,472 | 4,082,578 | −1.40% | −0.40% |
| **FL subset** (US airport in FL) | 3,388,029 | 3,589,522 | **2,955,345** | **−17.67%** | −12.77% |
| FL, foreign carriers | 3,276,069 | 3,497,363 | 2,877,261 | −17.73% | −12.17% |

**Monthly 2026 vs 2025:** Jan −14.23 · Feb −8.42 · Mar −12.18 · Apr −3.80 · May −3.42 · Jun **+0.45*** (raw −9.92) · Jul **+0.73*** (raw −4.77). FL subset: Jan −21.41 · Feb −13.69 · Mar −18.55 · Apr −13.42 · May −8.70 · Jun −1.69* · Jul −13.14*. (\* = rests on an imputed cell.)
**Apr–Jul:** ALL −1.43% vs 2025 / −6.24% vs 2024 · foreign carriers −4.24% · **US carriers +3.42%** · FL −10.20%. **Jan–Jul:** ALL −5.75% vs 2025, −8.76% vs 2024. **Calendar 2025 vs 2024:** −5.58% (2025 is itself a reduced base).

**Carrier families, winter 25-26 vs 24-25 (FL subset in brackets):**
| Family | All routes | FL |
|---|---|---|
| Air Canada (AC + QK + RV) | −11.1% | −12.3% |
| WestJet (WS) | −18.7% | −26.2% |
| Porter (PD + P3) | −7.0% | −7.7% |
| Flair | −55.9% | −52.0% |
| Transat | −33.3% | −35.7% |

US carriers held flat in winter and **grew +3.4%** in Apr–Jul: US airlines are partly backfilling summer seats, but not the winter or FL seats.

**Anchors (direction / order of magnitude only):**
- WestJet Apr–Jul seats **−18.5%** vs the trade-press "summer-2026 −32% ASM": same direction, smaller magnitude. ASM is not seats; the −32% is unverified.
- Transat to zero by July and Lynx to zero from March 2024 match the announced events.
- Passengers (T-100) Jan–May 2026 YoY −10.9 / −8.7 / −8.3 / −2.4 / +0.1 run the same sign as, and ~5pp less negative than, StatCan's Canadian-resident air return trips. T-100 also counts US residents and connecting traffic.

## 3. Proposed TOUR-03 letter (for MARCO to adopt or amend — not graded here)

> **TOUR-03 instrument (proposed 2026-10-14): BTS T-100 International Segment (All Carriers, transtats `FJE`), CLASS F seats, US↔Canada both directions, all carriers, hole-checked (zero carrier-months between non-zero neighbours filled and flagged), graded on the WINTER SEASON Nov–Mar with the FL subset (US airport in FL) as the thesis leg. "Restoration to 2025 levels" = winter 2026-27 total seats ≥ winter 2024-25 (15,061,509; FL 3,589,522), the last season scheduled before the boycott took hold. Holds (prediction correct) if winter 2026-27 is below that level on the total AND FL bases; FAILS if either is at or above it. Resolver: the first FJE pull carrying March 2027 (~mid-June 2027, est.), re-checked on the next vintage for backfilled holes. Read as of data month March 2026 (winter 25-26): total −11.03%, FL −17.67% vs 24-25 ⇒ not restored.** Monthly prints are a watch, not the grade: summer-2026 months sit ≈ flat vs 2025 hole-filled (Jun +0.45%, Jul +0.73%, both on imputed cells), against a 2025 summer that was already −7% to −12% vs 2024.

⚠️ **Why the season basis and not "2025" as a calendar year:** calendar-2025 is itself −5.58% vs 2024 and its summer was boycott-cut, so "≥ the same month of 2025" is a low bar that summer 2026 already roughly meets (within imputation error). A month-matched letter would put TOUR-03 at risk on the summer leg, which is not the channel the row was written for. MARCO should choose the basis explicitly. A summer-month basis would make the current read "borderline / restored within error" rather than "not restored".

## Summary
| Item | Value |
|---|---|
| Source verdict | **ADOPTABLE** — BTS T-100 Intl Segment All Carriers (`FJE`), free, scripted POST, SEATS by carrier and route; **hole check mandatory** (3 holes found: QK Jun-25, AC Jun-26, Porter Jul-26) |
| Newest month | **July 2026** (pulled 2026-10-14; Porter missing in July = trailing hole) |
| 2026 vs 2025 seats | Winter 25-26 vs 24-25: **−11.03% all / −17.67% FL**; Jan–Jul −5.75%; Apr–Jul −1.43% (US carriers +3.42%, foreign −4.24%); Jun +0.45%* / Jul +0.73%* hole-filled (raw −9.92 / −4.77) |
| Proposed letter | Winter 2026-27 (Nov–Mar) class F seats, total AND FL, vs winter 2024-25 (15.06M / 3.59M); ≥ on either = FAILS; resolver = first FJE pull with Mar-2027 (~Jun 2027 est.). Current read (data month Mar-2026): not restored |
