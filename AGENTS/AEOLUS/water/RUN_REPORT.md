# AEOLUS · WATER — worker RUN REPORT

**run_date: 2026-09-18** (worker run 13:1x–14:0x ET) · spawned by AEOLUS · **findings are PROPOSAL-ONLY — AEOLUS adjudicates.**
*Nothing below is scored, fired, resolved or routed. No source was substituted. Every failed command is reported with its exact error.*

---

## observations_added

**102 rows → `workbook/SERIES.tsv`** · **17 rows → `workbook/LOG.tsv`** · `DOSSIER.md` refreshed (new 9/18 block; two-clock header → `Last real data refresh: 2026-09-18` / `Dossier written: 2026-09-18`).

Rows written **only under instrument names already in AGENT.md's controlled vocabulary**: `powell_elev` (7) · `mead_elev` (7) · `lees_ferry_q` (17 new + 7 revision appends) · `kaub_stage` (21) · `duisburg_ruhrort_stage` (21) · `usdm_conus_*` (18) · `gatun_elev` (1) · `panama_max_draft_ft` (1) · `danube_stations_below_lkv` (1) · `rosario_stage` (1).

> ⛔ **Four instruments were measured but NOT written to `SERIES.tsv`, because no approved name exists and AGENT.md forbids inventing one.** Their figures are in `LOG.tsv` and below. **Names PROPOSED for AEOLUS's approval** (same route `gatun_elev` took on 9/11):
> `memphis_stage` (ft, `NOAA-NWPS-MEMT1`) · `stlouis_stage` (ft, `USGS-07010000-00065`) · `mead_24ms_proj_dec` (ft, `USBR-24MS-<scenario>`) · `powell_24ms_proj_min` (ft, `USBR-24MS-<scenario>`).

---

## threshold_state

*Reported as value + margin. **NOT graded** — the FIRED/NOT-FIRED column is deliberately left to AEOLUS.*

| Threshold | Current value | Margin | Note |
|---|---|---|---|
| **Mead vs Hoover 1,035 ft** *(the binding one)* | **1,038.44 ft** [9/17 · USBR 921/49] | **+3.44 ft** | 14-day OLS slope **−0.0352 ft/day**; decline resumed (was −0.013 ft/day at the 9/10 read) |
| **Powell vs ROD 3,510 ft** | **3,516.83 ft** [9/17 · USBR 919/49] | **+6.83 ft** | 14-day OLS −0.094 ft/day, **but it turned up**: 3,516.62 (9/15) → 3,516.67 → 3,516.83 |
| Powell vs min power pool 3,490 ft | 3,516.83 ft | +26.83 ft | |
| **Kaub vs NNW 25 cm** — 3 most recent COMPLETE days | 9/15 **30.723** · 9/16 **27.448** · 9/17 **24.302** | ❌ / ❌ / **✅** | unrounded daily means, n = 94/96/96 |
| **Duisburg-Ruhrort vs NNW 153 cm** — same 3 days | 9/15 **159.312** · 9/16 **160.438** · 9/17 **157.781** | ❌ / ❌ / ❌ | n = 96/96/96 |
| **C5 conjunction, 3 most recent complete days** | **not satisfied on 9/15–9/17** | — | 🔴 **but satisfied on 9/10–9/12 — see finding ②** |
| **Memphis vs `lowThreshold` −8 ft** | **−0.63 ft** [9/18 17:00Z] | **+7.37 ft** | vs 2023 analogue −12.06: **+11.43 ft**; vs 2022 −10.81: **+10.18 ft** |
| USDM CONUS D1–D4 | **59.37%** [mapDate 9/15] | — | extent plateaued; **D4 rose 1.75 → 2.02%** |
| Danube below-LKV count | **5 of 44** | unchanged vs 8/27 | 🔴 the count is misleading — see finding ⑥ |
| Rosario vs P10 ≈ 1.42 m | **2.53 m** [9/18] | +1.11 m, **73.5th pctile** | not firing, not close |
| Gatún (no band registered) | **84.47 ft** [9/17] | — | same-date 09-17: 2023 79.75 / 2024 86.25 / 2025 86.77 |
| Panama draft floor | **48.0 ft TFW**, "until further notice" | — | A-33-2026 still operative; **32 slots/day** cap (A-29) unchanged |

---

## changes

### ① 🔴 SEPTEMBER 2026 24-MONTH STUDY — published **on time** (document-dated **2026-09-15**), not late

**Filename trap, stated first because it is what a scraper hits:** `SEP26.pdf` → **HTTP 404**. The Most Probable is **split into two scenario files**, exactly as August was:
`SEP26_6.pdf` (6 maf WY2027 Powell release, 812,259 B) · `SEP26_7.pdf` (7 maf, 959,222 B), at `usbr.gov/lc/region/g4000/24mo/2026/`. UC mirrors `24Month_09_6.pdf` / `24Month_09_7.pdf` are byte-size-identical. `AUG26.pdf` also 404s — **the unsuffixed name has existed for neither month.**
Two further traps confirmed: `uc/water/crsp/studies/**24Month_09.pdf**` returns HTTP 200 and is the **September *2025*** study (the UC month-numbered files are not year-keyed); and `lc/region/g4000/**24mo.pdf**` — the "current" link — is 819,439 B, byte-size-identical to `JUL26.pdf`, title line *"July 2026 Most Probable 24-Month Study"*. **It is now four weeks stale, worse than the six days recorded on 8/27.**

**Alignment verified before any projected cell was read** (method per SOURCES.md): both elevation columns extract as 36 bare values, Sep-2025 → Aug-2028; matched month-by-month against `921/csv/49.csv` and `919/csv/49.csv` — **12 of 12 historical month-ends agree to within 0.02 ft** in every scenario file.

**MEAD — full month-by-month path, end-of-month (ft). The 6 maf and 7 maf Most Probable runs are IDENTICAL through Apr-2027 and diverge from May-2027.**

| Scenario | Sep-26 | Oct-26 | Nov-26 | **Dec-26** | Jan-27 | Feb-27 | Mar-27 | Apr-27 | May-27 | Jun-27 | Jul-27 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Sept MP 6 maf** | 1038.40 | 1035.16 | **1034.88** | **1034.18** | 1033.98 | 1033.37 | 1026.94 | 1019.05 | 1012.55 | 1008.13 | 1007.38 |
| **Sept MP 7 maf** | 1038.40 | 1035.16 | **1034.88** | **1034.18** | 1033.98 | 1033.37 | 1026.94 | 1019.05 | 1016.49 | 1015.54 | 1018.11 |
| **Sept Prob. Min** | 1038.36 | 1034.83 | 1034.23 | **1033.58** | 1033.23 | 1032.72 | 1025.67 | 1016.96 | 1009.66 | 1004.47 | 1003.28 |
| *Aug MP 6 maf (benchmark)* | 1038.80 | 1037.88 | 1035.56 | *1034.74* | 1034.36 | 1033.57 | 1026.72 | 1018.28 | 1011.16 | 1006.46 | 1005.63 |

- **December 2026 delta vs the August study's 1,034.74 ft: −0.56 ft (→ 1,034.18 ft).**
- **PATH read, not endpoint (L-36): the projected minimum over the CY2026 window is 1,034.18 ft — and it falls AT the 12/31 endpoint this month, so path-min == endpoint.** *(Stated explicitly because in August they differed and grading on the endpoint overstated the buffer 2.4×.)*
- **The first month-end at/below 1,035 ft moves EARLIER by one month: December → NOVEMBER 2026** (1,034.88). **October 2026 is projected at 1,035.16 — 0.16 ft above the line.**
- Probable Minimum crosses in **October** (1,034.83).
- **No bias adjustment applied.** Whether the n=6 **+2.19 ft** *August-study* under-projection bias (KB-097/099) transfers to a **September** study is AEOLUS's call. *(SOURCES.md's own caveat: the bias is discretionary-conservation-driven and the 2027-28 Guidelines just replaced the framework that produced it.)*

**POWELL vs 3,510 ft — and a contradiction inside the study, reported not resolved.**

| Scenario | WY2027 minimum (Oct-26→Sep-27) | 24-month-horizon minimum | Ever below 3,510? |
|---|---|---|---|
| **Sept MP 6 maf** | **3,511.43** (Feb-2027) | **3,511.43** (Feb-2027) | **No** — closest +1.43 ft |
| **Sept MP 7 maf** | **3,511.43** (Feb-2027) | **3,510.00** (Feb-2028), 3,510.10 (Mar-2028) | **No** — *touches* exactly |
| **Sept Prob. Min** | **3,483.31** (Sep-2027) | 3,475.21 (Feb-2028) | **Yes — Jan-2027 (3,509.00)**; through min power pool 3,490 at Sep-2027 |

Sept MP 6 maf monthly path: Sep-26 3514.98 · Oct 3515.05 · Nov 3514.64 · Dec 3513.51 · Jan-27 3512.26 · **Feb-27 3511.43** · Mar 3511.57 · Apr 3513.99 · May 3527.85 · Jun 3542.40 · Jul 3541.26 · Aug 3535.88 · Sep-27 3533.32.

> 🔴 **THE AMBIGUITY, FLAGGED NOT RESOLVED.** The September study states verbatim: *"The August 2026 24-Month Study projected the October 1, 2026 Lake Powell elevation to be less than 3,540 feet and **Lake Powell's elevation is projected to decline below 3,510 feet during WY2027**,"* and on that basis invokes §5.1.C.2 (Low Elevation Infrastructure Protection Range; WY2027 release **6.00–7.00 maf**). **But the August study's own Most Probable tables also do not go below 3,510 in WY2027** (6 maf min 3,511.70 Feb-2027; 7 maf 3,510.00 Feb-2028). The determination may rest on **within-month minima**, on the **Probable Minimum** run (August MIN *does* cross: Dec-2026 3,510.74 → Jan-2027 3,507.94), or on a test defined in the 2027-2028 Operating Guidelines, **which this worker has not read.** ⇒ **Do not grade the C6 Powell 3,510 row off the end-of-month Most Probable column until the basis is settled.**

**Narrative changes worth a decision-maker's attention:**
- **August unregulated inflow to Powell came in at 0.001 maf ≈ 0% of the 1991-2020 average** — against the August study's own one-month-ahead forecast of **0.070 maf = 19%**. September forecast 0.15 maf = 43%. Apr–Jul 1.14 maf = 18% (unchanged). WY2026 **3.52 maf = 37%** (August: 3.58 maf = 37%). DROA Flaming Gorge release still modelled at 1.00 maf.
- **Mexico treaty footnote replaced.** August carried *"provisional modeling assumptions … successor Minute to Minute 323 … currently under development … subject to change until a new Minute is entered into force."* September: **that footnote is gone (grep count 0)** and the body names **IBWC Minute No. 334** as governing (2 mentions; **0** in August). The plain reading is that a successor Minute entered into force between 8/21 and 9/15 — **NOT verified at IBWC by this worker; verify before use.**
- CY2026 diversions: CAP **0.963 → 0.985 maf**, MWD 0.789 → 0.788, Nevada/SNWP 0.201 unchanged.

### ② 🔴 RHINE — a 3-day joint-below window **opened and closed inside AEOLUS's dark period**

Unrounded daily means of 15-min observations; **a day with < 90 of 96 readings is skipped, not counted as a miss.**

| Date | Kaub mean (≤ 25 cm) | n | Duisburg mean (≤ 153 cm) | n | Both below |
|---|---|---|---|---|---|
| 2026-09-09 | 25.854 ❌ | 96 | 157.490 ❌ | 96 | no |
| **2026-09-10** | **21.531 ✅** | 96 | **152.906 ✅** | 96 | **YES** |
| **2026-09-11** | **21.844 ✅** | 96 | **149.146 ✅** | 96 | **YES** |
| **2026-09-12** | **20.635 ✅** | 96 | **145.073 ✅** | 96 | **YES** |
| 2026-09-13 | 25.292 ❌ | 96 | 147.729 ✅ | 96 | no |
| 2026-09-14 | 31.083 ❌ | 96 | 160.823 ❌ | 96 | no |
| **2026-09-15** | **30.723 ❌** | **94** | **159.312 ❌** | 96 | no |
| **2026-09-16** | **27.448 ❌** | 96 | **160.438 ❌** | 96 | no |
| **2026-09-17** | **24.302 ✅** | 96 | **157.781 ❌** | 96 | no |
| *2026-09-18* | *23.100 ✅* | *80* | *151.863 ✅* | *80* | *INCOMPLETE — skipped* |

- **On today's read the conjunction FAILS**: the 3 most recent complete days are **9/15, 9/16, 9/17**.
- 🔴 **On a read taken 9/13 it would have been SATISFIED**: 9/10–9/12, three consecutive complete days, both legs at/below NNW, all six readings n=96. Run length exactly 3, bounded by 9/09 (Duisburg above) and 9/13 (Kaub above). **AEOLUS was dark 9/11 → 9/18.**
- 2026-08-19 was a separate **isolated** joint-below day (Kaub 13.906 / Duisburg 135.885). Longest consecutive run in the whole 31-day retention window: **3 days.** *(The retired 10-consecutive-day clause would not have fired either.)*
- **NOT GRADED, NOT DECLARED FIRED OR UNFIRED.** AEOLUS decides whether a satisfied-but-unobserved window counts. The structural point is generic: **a current-state persistence test cannot see a window that opens and closes between reads.**
- ⚠️ **Method note:** a `P10D` pull made 9/18 showed 9/08 as `n=16, INCOMPLETE`; the `P31D` pull shows 9/08 as `n=96, complete`. **The "incomplete" day was an artifact of where the query window started.** Always grade completeness from a window that fully contains the day.
- **This reverses the 8/27 read** ("recovered; Duisburg at a folder-record high"). Duisburg *did* set a new folder-record high — **203.656 cm on 9/02**, superseding 194.146 — then fell **58.6 cm in ten days**.

### ③ 🔴 The 9/30 C5 base-rate obligation is **plausibly meetable** — the 8/27 "unreachable" finding was scoped to one endpoint

- **The REST wall is REAL, and now confirmed at n=6 window sizes instead of 4:** `P45D`, `P60D`, `P90D`, `P150D` and `P365D` all return the **identical 3,049 rows** starting `2026-08-18T01:15`. Explicit date ranges for Oct-2024 and Oct-2018 return **zero rows**. A retention wall, not a query limit. **That part of the 8/27 finding stands.**
- **But it is a property of the `measurements.json` endpoint, not of WSV.** PEGELONLINE's own help page (`pegelonline.wsv.de/gast/hilfe`) states verbatim:
  > *"PEGELONLINE bietet die Möglichkeit, historische Wasserstandsdaten und Abflusswerte **seit dem 1. Januar 2000** herunterzuladen. Bei den heruntergeladenen Daten handelt es sich um **ungeprüfte Rohdaten**."*
  (Historical stage **and discharge** downloadable since 1 Jan 2000 — as **unverified raw data**, which may contain outliers and measurement errors.) `/webservices/files` repeats it.
- **And the file archive is already deeper than 31 days:** `/webservices/files/Wasserstand+Rohdaten/RHEIN/1d26e504-7f9e-480a-b52c-5932be6549ab` (**KAUB**) lists **91 daily files, 20.06.2026 → 18.09.2026**, each offering `down.csv` / `down.txt` / `down.zrxp`. **Duisburg-Ruhrort uuid: `c0f51e35-d0e8-4318-afaf-c5fcbc29f4c1`.**
- **What I could NOT do (route unresolved, not absent):** dates outside that 91-day listing return **HTTP 404** on the same path pattern (tested `22.10.2018`, `15.10.2022`, `01.11.2018`, `01.01.2000`), and the back-to-2000 bulk download is a **JavaScript-driven zip builder** on `/gast/pegeltabelle` whose only form is `<form name="filterForm" method="GET" action="/gast/pegeltabelle">` — no download endpoint exposed to `curl`.
- **No secondary substituted.** ⇒ **Same class as L-35 (Gatún): a method failure recorded as a publication absence.** The 8/27 wording *"GENUINELY UNREACHABLE — confirmed four ways, so the 9/30 obligation cannot be met as written"* should be narrowed to the REST endpoint.

### ④ **GlW verified at the issuing authority — and it IS a navigation reference** *(Task 5 answered)*

| | **GlW** | `validFrom` | **TuGLW** | **NNW** |
|---|---|---|---|---|
| **Kaub** | **77.0 cm** ✅ *(candidate CORRECT)* | **2023-01-01** | 190 cm | 25.0 cm (2018-10-22) |
| **Duisburg-Ruhrort** | **227.0 cm** ✅ *(candidate CORRECT)* | **2023-01-01** | 280 cm | 153.0 cm (2018-10-23) |

- **Both carried candidate values are correct at the primary.** Validity period: the current determination carries `validFrom 2023-01-01`; GlW is periodically redetermined and `validFrom` is the field that dates it (re-check it, not the number, at each pass).
- **Is it a navigation-reference plane, as opposed to another record-low statistic? YES — and WSV says so structurally, not just by name.** The companion value is longnamed **`TuGLW` = *"verkehrsgesicherte Fahrrinnentiefe unter GlW (Tiefe unter GlW)"*** — the **traffic-secured fairway DEPTH beneath GlW**. WSV defines the maintained navigable channel *as a depth measured down from GlW*. ⚠️ **TuGLW is therefore a DEPTH, not a stage** — it currently sits in this folder's tables in a row of stage values, where it reads as one.
- **Definition and derivation** (WSV/BfG documentation; the API gives only the gloss *"Pegelkennwert: GLW gleichwertiger Wasserstand"*): GlW is the stage **equalled or undercut on average 20 ice-free days per year**. It is obtained by first computing the equivalent discharge **GlQ** from ~100 years of daily mean discharge at the gauge, then converting GlQ to a stage using measured water-surface elevations at discharges near GlQ. It sets planned fairway depth per Rhine reach. ⇒ **a duration-curve navigation plane, categorically different in kind from NNW.**
- 🔴 **Bonus, and it validates the current trigger's method:** PEGELONLINE's definitions page gives **`NNW` = *"niedrigster bekannter **Tagesmittelwert** des Wasserstandes"*** — the lowest known **daily mean**. **Grading unrounded daily means against NNW is like-for-like**, which the trigger already does correctly.
- ⚠️ Kaub also publishes **`NW` = 25.0 cm** *"Niedrigster Tageswasserstand"*, timespan 2010-11-01→2020-10-31, same occurrence date 2018-10-22. **Same number, different scope — NW and NNW are not two independent witnesses.**
- ⚠️ **Datum caveat unchanged and still live:** Kaub's `gaugeZero` is 67.669 m ü. NHN with `validFrom` **2019-11-01** — *after* its 2018 record. Duisburg's is 16.106 m, same 2019-11-01. The API still does not state whether historic values were re-referenced.

### ⑤ 🔴 MISSISSIPPI — Memphis fell **13.10 ft in 21 days** as the autumn window opened

- **Memphis (MEMT1): −0.63 ft @ 2026-09-18T17:00Z**, against **12.47 ft @ 2026-08-28T01:00Z**. `lowThreshold` = **−8 ft** (unchanged). `flood.lowWaters.historic` re-pulled: **26 entries, unchanged** — deepest **2023-10-17 −12.06 ft** *(flagged "Preliminary")*, **2022-10-21 −10.81**, 1988-07-10 −10.70, 2012-09-19 −9.80. **The 1988 row still carries NOAA's stale *"LOWEST STAGE ON RECORD *****"* statement and is still not quotable.**
- ⚠️ **This is a single instantaneous reading, not a daily mean.** SOURCES.md registers only the point-in-time gauge endpoint for Memphis; **no daily-mean or observed-series command is registered, so no slope is computed here.** *(Registering one would let the Mississippi band be graded the way the Rhine band is.)*
- **St. Louis (USGS 07010000, param 00065) — carried with NO adjective, no reference plane found:** 9/01 **3.00** · 9/05 0.27 · 9/09 **−1.22** · 9/12 0.39 · 9/14 **3.65** · 9/16 0.58 · 9/18 **3.22** ft. **Large swings both ways — not a monotonic fall**, unlike the 8/27 note ("falling fast, 8.15 → 4.27 in 4 days").
- **Vicksburg and Cairo remain UNRESOLVED. No ID was guessed.**

### ⑥ 🔴 DANUBE — the below-LKV count is flat at 5, **and that conceals five fresh all-time records**

**5 of 44 stations carry `LKV_viszony = −1` — identical to 8/27.** It reads as "stable". It is not.

**Five stations now carry an `LKVIdopont` in August or September 2026** — i.e. they *reset their all-time low during this drought*: **Adony** km1598.11 (**2026-08-01**) · **Paks** km1531.3 (**2026-08-02**) · **Dunaföldvár** km1560.6 (**2026-08-19**) · **Dombori** km1506.8 (**2026-08-19**) · **Baja** km1478.7 (**2026-09-10 — inside AEOLUS's dark window**).

> ⚠️ **INSTRUMENT CAVEAT: `LKV` is a MOVING reference.** When a station sets a new all-time low, OVF updates `LKV` to that value and the station's flag flips **back to +1**, because it is now at/above the *new* record. **The below-LKV count therefore understates severity precisely during a record-setting event, and a flat count can conceal fresh records. Grade the `LKVIdopont` column, not only the flag.**

Of the 5 flagged, **3 are the known null-date sentinels** (Apatin & Novo Selo `1799-12-31`, Ilok Most `1884-12-31`). **Genuinely below a real LKV: 2.**

| Station | km | Level | LKV | Margin | LKV set | vs 8/27 |
|---|---|---|---|---|---|---|
| **Pfelling** | 2305.5 | 222 | 226 | **−4** | 2018-08-22 | **unchanged — Pfelling has NOT reversed** |
| **Duna Mohács** | 1446.9 | 14 | 50 | **−36** | 2018-10-26 | was 43 / −7 → **deteriorated 29 cm** |
| *Hofkirchen* | 2256.86 | 171 | 166 | **+5** | 2003-08-27 | was −2 → **recovered** |

### ⑦ PANAMA — one new advisory, and it is a **loosening**

**A-35-2026, dated September 16, 2026**, *"Clarification on Consecutive Booking Dates Limitation in the Panamax Locks Across Different Booking Periods"* — the **only** advisory published after A-34-2026 (9/10). Effective immediately the consecutive-transit-date booking restriction **no longer applies** when slots are awarded through *different* booking periods; **exclusively Panamax locks**; all other A-28-2026 rules stand.
⇒ **The water-stress measures are UNCHANGED: Neopanamax maximum authorised draft stays 48.0 ft TFW "until further notice" (A-33, 9/4), and the 32 BOOKING SLOTS/day cap (A-29) stays in force, binding on booking dates from 9/15.**
⚠️ **SLOTS ≠ TRANSITS and they collide at 32.** The 32 is a **slot** cap. August 2026 realised **oceangoing transits** were **33.19/day** (A-34-2026).
**Gatún Lake: 84.47 ft [9/17]**, +0.43 ft vs 9/10, rising 6 of the last 7 days. **Same-date 09-17 comparison: 2023 79.75 · 2024 86.25 · 2025 86.77 · 2026 84.47** — 4.72 ft above the 2023 drought analogue, 1.78 below 2024, 2.30 below 2025. Series 1965-01-01 → 2026-09-17, **22,540 rows**.
*(Archive scanned via the singular-URL server-rendered index: 1,011 PDF anchors; A-30 … A-35 are the only 2026 advisories numbered ≥ 30.)*

### ⑧ LEES FERRY — the deficit % fell, **and it is a denominator artifact, not an improvement**

- **7,910 cfs [9/17].** Window 9/04–9/17 mean **7,840.0 cfs (n=14)** vs the **2018-25 same-calendar-window pooled mean 10,224.6 cfs = −23.32%.**
- 🔴 **DO NOT read that as an 18-point improvement on the −41% carried since 8/26.** The 2026 numerator barely moved (8/13–26 mean **7,804.3** → 9/04–17 mean **7,840.0**, **+0.5%**). The **baseline** fell **13,411.6 → 10,224.6 cfs (−23.8%)** because Glen Canyon releases drop seasonally into September in normal years too. **The deficit percentage is not comparable across calendar windows — the denominator has a strong seasonal shape.**
- **Verdict on the brief's question: it is a LEVEL, not a worsening slope** — the same verdict as 8/26. Per-year same-window baselines: 2018 11,621 · 2019 11,901 · 2020 10,474 · 2021 10,498 · 2022 9,466 · 2023 8,521 · 2024 9,595 · 2025 9,721.
- **Method reproduced exactly:** recomputing the 8/13–26 baseline today returns **13,411.6 cfs**, matching DOSSIER to the decimal.

### ⑨ USDM — **the acceleration broke; the geography migrated into the Mississippi basin**

**CONUS D1–D4** (`areaOfInterest = CONUS`, not `Total`): 8/18 **52.70** → 8/25 **56.61** (+3.91pp) → 9/01 **59.05** (+2.44) → 9/08 **58.59** (**−0.46**) → 9/15 **59.37** (+0.78).
⇒ **The 8/27 read *"a FOURTH straight week up and the acceleration itself accelerating"* no longer holds.** 9/08 was the **first weekly decline since 7/28**; extent has **plateaued near 59%**.
**Intensity did NOT plateau:** D2–D4 31.59 → **33.82** · D3–D4 11.76 → **12.54** · **D4 1.75 → 2.02%**. `Total` (US+PR) 9/15 D1–D4 = **49.77** — a **9.60 pp** gap vs CONUS.

**State cut, D1–D4, 8/25 → 9/15:** **TX 57.36 → 81.01 (+23.65pp)** · **MS 45.70 → 67.67 (+21.97)** · **MO 14.79 → 32.40 (+17.61)** · **TN 0.91 → 17.37 (+16.46)** · CA 13.90 → 22.32 (+8.42) · KS +5.64 · AR 84.90 → 88.69 (+3.79) · LA +2.44 · NM +1.60 — against **IA 19.64 → 6.79 (−12.85)** · **NE 67.43 → 60.32 (−7.11)** · CO −2.13; saturated OK 99.82, UT 100.00, AZ 77.16 flat.
⇒ 🔴 **CORRECTED 2026-09-18 (AEOLUS adjudication). Superseded wording, kept verbatim so the over-read is visible: *"the deterioration migrated out of the southern Plains into the lower Mississippi / mid-South … while the corn belt improved."* **IT DID NOT MIGRATE — IT SPREAD.** The southern Plains did not improve: **Texas is the single largest deterioration in the table at +23.65pp (57.36 → 81.01)** and **Oklahoma is saturated at 99.82%**. What happened is that the **lower Mississippi / mid-South JOINED them** (MS +21.97, MO +17.61, TN +16.46, AR +3.79, LA +2.44), while **IA (−12.85) and NE (−7.11) improved**. **Why the distinction is load-bearing and not pedantry:** the persistent TX/OK reading is what corroborates the wildfire desk's finding that both states stayed above-normal with 10 of the nation's 50 large fires now there. **"Migration" implies the southern Plains released, which would have broken that C4 link.** The numbers were right; the sentence over-read them.** The lower Mississippi is the same basin whose Memphis stage fell to a **−4.678 ft daily-mean trough on 9/14** (see the ADDENDUM — the 13.10 ft / −0.63 ft figures on this page are superseded). C5 (rivers) and C2 (crops) still point in **opposite directions off one dataset.**

### ⑩ PARANÁ — **2.53 m [9/18], 73.5th percentile**, down from 91.5th (8/27) and 99th (8/13)

Δ +0.08 on the day; cross-checked against the 366-record station history (same 2.53). Trailing-366-day distribution recomputed today: min **1.08** · P05 1.35 · **P10 1.42** · P25 1.82 · median 2.27 · P75 2.54 · max 3.03. **Far above the P10 working low-water reference. Not firing, not close.** The published **5.00 m "ALERT" is a FLOOD level**, not a low-water one. ⚠️ The one-year base remains **short** — 2020/21 reporting has Rosario near 0.08 m, lowest since 1944. Neighbours: Santa Fe 2.65 · San Lorenzo 2.62 · Diamante 2.85 · Villa Constitución 1.96 · Corrientes 4.00.

---

## proposed_findings

**All PROPOSALS. AEOLUS adjudicates; the worker neither scored, fired, resolved nor routed anything.**

| # | Proposed finding | Basis |
|---|---|---|
| **P-1** | **Sept 24MS moves Mead's first sub-1,035 month-end from December to NOVEMBER 2026 and lowers the Dec endpoint 0.56 ft to 1,034.18 ft; path-min == endpoint this month.** | `SEP26_6/_7.pdf`, alignment 12/12 ≤0.02 ft |
| **P-2** | **The Powell 3,510 ft threshold row cannot be graded from the end-of-month Most Probable column — the study's narrative and its own tables disagree, and the statutory basis is unread.** | narrative p.1 vs tables, both scenarios, both months |
| **P-3** | **A registered C5 conjunction was satisfied on 9/10–9/12 and had closed before this read. A current-state persistence test is blind to windows that open and close between reads.** | 6 complete days, n=96 each |
| **P-4** | **The 9/30 C5 base-rate obligation should be reopened: WSV publishes raw stage/discharge back to 2000-01-01 in writing; only the REST endpoint has a 31-day wall, and the file archive is already 91 days deep.** | WSV help page verbatim + 91-file listing |
| **P-5** | **GlW is confirmed as a duration-curve NAVIGATION reference (20 ice-free days/yr, via GlQ) and both candidate values are correct — Kaub 77, Duisburg 227, validFrom 2023-01-01. A GlW-keyed trigger is defensible in kind; it still needs base-rating.** | characteristicValues + WSV/BfG definition |
| **P-6** | **`TuGLW` is a fairway DEPTH beneath GlW, not a stage — it is mislabelled by adjacency in this folder's tables.** | WSV longname, verbatim |
| **P-7** | **USDM: the acceleration narrative is spent — extent plateaued ~59%, intensity still deepening (D4 → 2.02%), and the geography moved into the lower Mississippi basin.** | CONUS + 16-state series |
| **P-8** | **The Danube below-LKV count is a structurally biased severity gauge during a record-setting event; five stations reset their LKV in Aug/Sep 2026, one (Baja) on 9/10.** | `LKVIdopont` column, 44 features |
| **P-9** | **Lees Ferry's deficit percentage is not comparable across calendar windows; the −41% → −23% move is entirely denominator. The flow is flat.** | numerator +0.5%, denominator −23.8% |
| **P-10** | **USGS revised every 2026 Lees Ferry daily value down ~100 cfs; DOSSIER's −41.06% for 8/13–26 recomputes to −41.81%, and any pre-9/18 Lees Ferry level is ~100 cfs high.** | 34 of 35 rows moved exactly −100 |
| **P-11** | **The September Probable MAXIMUM is not published while the Minimum is — an asymmetric envelope, confirmed against the issuer's own index, not merely a failed filename guess.** | UC index min/max href scan |
| **P-12** | **Panama's water-stress posture is unchanged and Gatún is recovering (84.47 ft, +4.72 ft vs the 2023 analogue); A-35 is a booking loosening.** | A-35 verbatim + 22,540-row CSV |
| **P-13** | **Four instruments need approved `SERIES.tsv` names before they can be recorded: `memphis_stage`, `stlouis_stage`, `mead_24ms_proj_dec`, `powell_24ms_proj_min`.** | AGENT.md no-invented-names limit |
| **P-14** | **`SOURCES.md` §1's state-granularity recipe is dead while the working one lives only in `DOSSIER.md` — two live instructions, and the dead one is in the file workers are told to copy from.** | both run verbatim today |

**Contradicts something already in `DOSSIER.md` — flagged loudly, not silently overwritten:** P-3 (reverses the 8/27 "Rhine recovered" read) · P-4 (narrows the 8/27 "genuinely unreachable" finding) · P-7 (retires the 8/27 "fourth straight accelerating week") · P-8 (Pfelling did **not** reverse; the 8/27 "genuine REVERSAL" framing needs re-reading now that the flat count is explained) · P-9/P-10 (the −41.06% figure) · P-14.

---

## gaps

**Reported, never worked around. No source was substituted anywhere in this run.**

| # | What | Exact command | Exact result |
|---|---|---|---|
| **G-1** | **September Probable MAXIMUM 24-Month Study** | `curl -sL "https://www.usbr.gov/lc/region/g4000/24mo/2026/SEP26_MAX.pdf"` *(also `SEP26_MAX_6.pdf`, `SEP26_MAXP.pdf`, `.../uc/water/crsp/studies/24Month_09_max.pdf`, `24Month_09_MAX.pdf`)* | **HTTP 404, 196 B** on all five. Corroborated structurally: the UC index's only min/max hrefs are `SEP26_MIN.pdf` and `AUG26_MAX.pdf`. **Retry path: re-probe + re-scan the index next pass.** |
| **G-2** | **`SEP26.pdf` / `AUG26.pdf` (unsuffixed Most Probable)** | `curl -sL ".../24mo/2026/SEP26.pdf"` | **HTTP 404, 196 B.** Not a gap in the data — the files are `SEP26_6.pdf` / `SEP26_7.pdf`. **SOURCES.md's `/24mo/YYYY/MONYY.pdf` pattern does not hold for split months.** |
| **G-3** | **`SOURCES.md` §1 state/county drought granularity** | `curl -s -H "Accept: application/json" "https://usdmdataservices.unl.edu/api/USStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=CO&startdate=8/18/2026&enddate=9/15/2026&statisticsType=1"` | Body: **`"-area of interest not recognized.\r\n"`**. Same for `aoi=OK`, `aoi=40`. **Worked around ONLY by using the recipe already recorded in `DOSSIER.md` §1** (`StateStatistics` + 2-digit FIPS) — the same primary, a different documented endpoint. That recipe **additionally requires `Accept: application/json`**; without it the response is non-JSON. |
| **G-4** | **WSV multi-year series back to 2000** | `curl ".../files/Wasserstand+Rohdaten/RHEIN/1d26e504…/22.10.2018"` *(also 15.10.2022, 01.11.2018, 01.01.2000)* | **HTTP 404, 6,160 B** on all four. The listing covers **20.06.2026 → 18.09.2026 only (91 files)**. Bulk route is a JS zip builder on `/gast/pegeltabelle`; only form is `method="GET" action="/gast/pegeltabelle"`. **Route unresolved — NOT absent** (see ③). |
| **G-5** | **Mississippi Vicksburg / Cairo** | — | **Still unresolved. No ID guessed, no alternative site used.** |
| **G-6** | **Memphis daily means / observed series** | — | **No series endpoint is registered in `SOURCES.md`** — only the point-in-time gauge call. Memphis is therefore an instantaneous reading and **cannot be graded the way the Rhine legs are.** |
| **G-7** | **USGS NWIS transient failures** | `waterservices.usgs.gov/nwis/dv/?…sites=09380000…` | **HTTP 503** on first attempt; a later 200 returned a **truncated body (1,062 B, JSON cut mid-token)**. ⚠️ **A 200 from this host is not proof of a complete body — check the byte count.** Resolved by retry-with-size-guard; final pull 237,092 B. |
| **G-8** | **`elwis.de` / `bafg.de` GlW pages** | two constructed URLs | **404** — **URLs I constructed, so this is a fact about my guess, not about the publishers.** GlW was instead answered from the WSV primary (`characteristicValues` + `/gast/hilfe`) plus WSV/BfG documentation. |
| **G-9** | **Yangtze / snowpack** | — | **Not tasked this run** (Yangtze); snowpack is **seasonally near-zero Jun–Sep and correctly empty, not a gap.** |

### Housekeeping notes for AEOLUS (not gaps)

- **`DOSSIER.md` is now 76,652 B.** It was already ~70 KB before this run and is not a boot-read-whole surface, but it is well past the 32,550 B read-cap constant and my block grew it. **Rotation is AEOLUS's call.**
- **`workbook/SERIES.tsv` has a pre-existing blank line at line 252** (not introduced by this run; untouched — restructuring another layer's file is outside a worker's scope).
- **Duplicate `(date, instrument)` keys exist and are intentional** — the 8/25 and 8/26 `lees_ferry_q` revision appends, per AGENT.md's never-overwrite rule.
- **All 17 new `LOG.tsv` rows and 102 new `SERIES.tsv` rows validated at 6 and 7 tab-separated fields respectively.**
- **No git operations performed** — AEOLUS handles git, per the spawn brief.
