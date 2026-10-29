# AEOLUS · REGIME — live dossier

**As-of: 2026-10-29**, ENSO figures CPC primary; vortex figures at NASA GMAO / ECMWF / CPC primaries (§7). Consolidated from KB-AEO-016/021/038/045/046/053/054/111 + VX-19/20.

> **Last real data refresh: 2026-10-21**  ·  **Dossier written: 2026-10-29**
> *(Data date = the newest ENSO OBSERVATION: weekly week-centred 21OCT2026. The §7 vortex/AO/NAO analyses run to 10/29 00z, but that is a NEW, unregistered family; the ENSO date was chosen as the conservative, loud-failing one.)*
>
> **2026-10-29 — worker pass (AEOLUS dark 10/21–10/29).**
> 1. **Weekly Niño-3.4 (`wksst`) +3.4 at week ctr 21OCT — new file record, rank 1 of 2,356 weeks, no tie** (07OCT +3.3 · 14OCT +3.3; pre-2026 max +3.0, 18NOV2015). Same week in 1997 +2.0, 2015 +2.3. Niño-3 +4.3 (record), Niño-1+2 +5.2 (flat 3 weeks, 30SEP +5.3 is the max), Niño-4 +1.1. Five Sep weekly cells revised by 0.1–0.2 (SERIES). AEOLUS's 00:18 ET read verified to the cell.
> 2. **ONI / RONI / sstoi unchanged** — files still Last-Modified 3 Oct / 3 Oct / 5 Oct. **ASO and October are not printed.** ONI JAS +2.16, RONI JAS +1.69, Sep Niño-3.4 +2.84, ONI−RONI +0.47 (recomputed, same season).
> 3. **No CPC Discussion since 8 Oct** — `ensodisc.shtml` still reads *"8 October 2026"*, next *"12 November 2026"*. The weekly deck re-issued **26 Oct** (restates the 8 Oct odds; relative weekly bullets 0.0/2.5/3.6/4.4, not scored; RONI JAS *"1.7ºC"*; CFSv2 plume issued 26 Oct).
> 4. **CPC 15 Oct DJF outlook diffed against 17 Sep (§6):** the PJM/NW temperature signal **strengthened** at 3 of 8 points and the weak wet tilt **reached the Upper Basin** (Grand Lake, Aspen, Page AZ: EC → Above 33%). This **reverses the 9/17 "did not move" observation**.
> 5. 🔴 **NEW §7 — polar vortex: a reversal is FORECAST, NOT OBSERVED.** Observed 10 hPa 60°N zonal-mean U on 10/29 00z: **+14.1 m/s (IFS analysis)**, falling ~3 m/s/day from a ~+22 peak on 10/24–26. **All four ECMWF HRES 00z runs 10/26–10/29 take it below zero on 4–5 Nov** (min −0.7 to −4.9). **The 10/29 ECMWF ENS mean is easterly 11/05–11/12, and 50/50 members are below zero on 11/09.** That is firmer than WALTER's 10/23–25 relay (*"IFS/GEFS means stay weakly westerly"*). AO observed +1.20 (10/26). The GEFS AO mean is negative from 11/02, with 31/31 members below zero that day.
>
> **2026-10-09 worker pass → archive piece 1** (key facts in KB-AEO-181).
>
> **Prior passes:** 10/09 → `archive/REGIME_DOSSIER_ARCHIVE_2026-10-29_10-09-pass-sep-table-sec6-closedQs.md` · 9/28 · 9/18 · 8/21 · 8/27 → `archive/REGIME_DOSSIER_ARCHIVE_2026-10-21_prior-passes-and-sec2.md` (grep, never boot-read).
> ⚠️ **Known-bad: `wksst8110.for`** — reconstructed from memory once, got a dead file ending 27JAN2021. `SOURCES.md` had the right one (`wksst9120.for`) all along.
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `regime/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C1 · C2 · C3 · C5 · C6 (root: owns the ENSO indices)

---

## 1. STATE — four instruments, all correct, none interchangeable

**Re-pulled 2026-10-29: only the weekly moved (through 21OCT). ONI/RONI JAS (3 Oct) and Sep OISST (5 Oct) are unchanged; ASO and October not yet printed.**

| Instrument | Value | As-of | Basis | Reads |
|---|---|---|---|---|
| **ONI** (official level) | **+2.16** | **JAS 2026** | ERSSTv6, 30-yr centred | MJJ +1.39 → JJA +1.80 → **JAS +2.16**. Above strong 1.5 by **+0.66** and very strong 2.0 by **+0.16**. **Highest JAS in the file** (1997 +1.79, 2015 +1.73); 9 of 920 seasons are higher |
| **RONI** (dynamical) | **+1.69** | **JAS 2026** | ERSSTv6, 1991-2020 | JJA +1.36 → **JAS +1.69**. **0.81 below** the +2.5 historic bar. Above 2023-24's RONI peak (1.42). **2nd-highest JAS: 1997 JAS +1.84 is higher** |
| **OISST monthly** (trend, traditional) | **+2.84** | **Sep 2026** | OISST, 1991-2020 fixed | Jun +1.55 → Jul +2.03 → Aug +2.52 → **Sep +2.84** |
| **Weekly** (fast trend, traditional) | **+3.4** | **week ctr 21OCT 2026** | OISSTv2.1, 1991-2020 | 16SEP 3.0 → 23SEP 3.1 → 30SEP 3.2 → 07OCT 3.3 → 14OCT 3.3 → **21OCT 3.4, the file record (rank 1 of 2,356 weeks, no tie)**. Same week in 1997 +2.0, 2015 +2.3 |
| Niño-1+2 | **+4.69** monthly (Sep) / **+5.2** weekly (21OCT) | Sep / 21OCT 2026 | | *the number that gets misquoted as "3.4"*. Weekly 30SEP +5.3 (file max) then flat at 5.2 for three weeks; 23SEP revised 4.7 → 4.9 |
| Niño-4 | **+0.95** monthly (Sep) / **+1.1** weekly (21OCT) | Sep / 21OCT 2026 | | still the weakest region (30SEP revised 1.2 → 1.3, 07OCT 1.3) |
| *Relative monthly Niño-3.4* — **NOT a registered instrument** | *+2.1* | *Sep 2026* | *OISSTv2.1, minus tropical mean 20°N–20°S, re-scaled, 1991-2020* | *The Discussion's quoted figure (Fig. 2). Niño-3 +3.0 · Niño-1+2 +3.9 · Niño-4 ~0.0 (read off the chart). **~0.6–0.8 below traditional, by construction***|
| *Relative weekly* (deck bullet) — **NOT a registered instrument** | *+2.5* | *~21OCT (deck 26 Oct)* | *OISSTv2.1 relative (chart title "Relative SST Anomalies")* | *Niño-4 0.0 · Niño-3 3.6 · Niño-1+2 4.4 (5 Oct deck: 2.3 / 0.1 / 3.3 / 4.5). Never cite for anything scored (KB-088 ruling stands)* |

⚠️ **Four simultaneously-true REGISTERED numbers for "the ENSO state" as of 2026-10-29: +2.16 (ONI, JAS) · +1.69 (RONI, JAS) · +2.84 (OISST monthly, Sep) · +3.4 (weekly, 21OCT).** CPC's prose quotes a **fifth (+2.1, relative monthly, Sep)** and the deck a **sixth (+2.5, relative weekly)**. Name the instrument beside the number, every time.

**CPC forward odds (8 Oct 2026 Discussion, verbatim):**
- Synopsis: *"El Niño continues to strengthen, with a **strong-to-very strong El Niño likely through January-March 2027 (remaining greater than an 83% chance)**."*
- *"Chances remain high for a historic event that would exceed the strength of previous El Niño events dating back to 1950 (+2.5°C or more for a 3-month RONI value): the chance is **54% for September-November, 83% for October-December, and 70% for November-January**."* 🔴 **OND RAISED 75 → 83.**
- 🔴 **The headline changed kind. Do not read 90 → 83 as a fall.** The 9/10 headline was *">90% chance of a very strong event"* (RONI ≥2.0, fall/winter). The 10/8 headline is ≥1.5 held **through JFM**: 83 = JFM P(≥1.5) = 37+46 in the Strength table, which sums to exactly 83 against the prose's "greater than". **The prose no longer gives a very-strong figure at all.**
- Alert status: **El Niño Advisory** (unchanged). **Next discussion: 12 November 2026.** ✅ **Confirmed 2026-10-29: no Discussion issued since 8 Oct** (page still dated 8 Oct; deck 26 Oct says the odds statements *"are updated once a month (2nd Thursday)"*; the Strength Outlook reads *"Updated: 8 October 2026"*).

### 1b. THE FORWARD CURVE — CPC's own RONI forecast (both tables now **"Issued October 2026"**, RONI, 1991-2020 base; September issue kept below for comparison)

| Season | P(RONI ≥ 2.0) Oct (Sep) | P(RONI ≥ 1.5) Oct | RONI 5th | 25th | **median** Oct (Sep) | 75th | 95th |
|---|---|---|---|---|---|---|---|
| SON 2026 | **100** (97) | 100 | 2.18 | 2.35 | **2.47** (2.43) | 2.59 | 2.76 |
| **OND 2026** | **100** (98) | 100 | 2.25 | **2.54** | **2.74** (2.67) | 2.94 | 3.23 |
| NDJ 2026-27 | **96** (93) | 100 | 2.00 | 2.39 | **2.65** (2.57) | 2.92 | 3.31 |
| DJF 2026-27 | **81** (75) | 97 | 1.58 | 2.04 | **2.36** (2.27) | 2.68 | 3.14 |
| JFM 2027 | **46** (39) | **83** | 1.13 | 1.59 | **1.90** (1.82) | 2.22 | 2.67 |
| FMA 2027 | 6 (5) | 38 | 0.66 | 1.05 | 1.33 (1.26) | 1.60 | 2.00 |
| MAM 2027 | 0 (0) | 5 | 0.23 | 0.58 | 0.83 (0.79) | 1.08 | 1.43 |
| AMJ 2027 | 0 (0) | 0 | −0.22 | 0.14 | 0.40 (0.38) | 0.66 | 1.02 |
| MJJ 2027 | 0 (new) | 0 | −0.68 | −0.26 | 0.03 (new) | 0.32 | 0.74 |

⇒ **Peak still OND; every season moved up 0.02–0.09.** The OND 25th percentile (**2.54**) is now **above** 2.5 (Sep: 2.44). Observed RONI JAS **1.69** must rise **+0.78 in two seasons** to meet the SON median. ASO dropped out of the October table.

**September issue table → rotated verbatim 2026-10-29 (archive piece 2).** Sep OND median 2.67 / 25th 2.44 / P(≥2.0) 98%; the October table above supersedes it.

---

## 2. 🔑 THE ONI↔RONI RECONCILIATION — tables ROTATED 2026-10-21

**The decadal-offset and peak-event tables (re-derived on ERSSTv6 9/18, reproduce 8/13 exactly) → `archive/REGIME_DOSSIER_ARCHIVE_2026-10-21_prior-passes-and-sec2.md` §2.** Live carry: ONI−RONI offset is NOT a constant (grew every decade; 2020s mean +0.44; JAS 2026 +0.47); RONI record = 1982-83 +2.40; 2015-16 ONI peak +2.59 / 1997-98 +2.37. ⚠️ ONI and RONI answer different questions — never present one as a correction of the other, never convert at a fixed offset. Teleconnections key to RONI (CPC framing); channel signs not yet re-derived on RONI (open Q2).

---

## 3. PER-CHANNEL SIGN TABLE — what the regime sets

| Channel | Sign | Confidence | Basis |
|---|---|---|---|
| **C1** hurricane | **SUPPRESS** ↓ | **HIGH** — mechanism now visible in storm-level forecasts (NHC names *"strong upper-level winds and dry air"* on AL92) | shear |
| **C2** crops | ambiguous | **LOW** — currently **refusing to confirm** (corn 61 / soy 62 G/E, 6 pts above my band) | drought geography is southern Plains, not the corn belt |
| **C3** winter demand | **MEAN down** ↓ · **PEAK: no sign** | mean HIGH · **peak REFUSED** | n=2 very-strong analogues, **split 1-1** |
| **C4** fire | southern-Plains fire risk should **abate** by late autumn | MED | the wet-south signal — **AEO-09 tests it** |
| **C5** Panama | drought risk ↑ | MED | El Niño → Panama hydrology |
| **C5** Rhine | **NO SIGN — separate basin** | — | ⚠️ **European basin. Never weld to the ENSO root.** |
| **C6** Colorado | **NOT relief** | MED | see §4 |

**Independence accounting:** C1 + C2 + C3 + C5-Panama + C6 share **ONE** root. **Count it once.** C5-Rhine is independent.

---

## 4. ⚠️ TWO GUARDS AGAINST INTUITIVE-BUT-WRONG READS

**① A record El Niño does NOT refill the Colorado.** The reliable wet signal is the **Southwest / Lower Basin**; **Powell's inflow is UPPER Basin**, near the ENSO precipitation **dipole pivot** where the signal is weak and sign-ambiguous. **The wet anomaly lands downstream of the reservoir that needs it.** Full treatment → `../water/DOSSIER.md`.

> ✅ **TESTED AGAINST THE LIVE 9/17 OUTLOOK, NOT REPEATED — AND IT HOLDS.** DJF 2026-27 precipitation probabilities, read at the CPC primary as GIS polygons (`lead3_DJF_prcp`, Fcst_Date 20260917):
> | Upper Basin point | DJF precip category |
> |---|---|
> | Grand Lake CO (Colorado hdwtrs) · Steamboat Spgs/Yampa · Aspen · Pinedale WY (Green R hdwtrs) · Vernal/Uinta · Flaming Gorge · Grand Junction · Moab · **Page AZ / Lake Powell** · Salt Lake City | **Equal Chances (33%) — NO tilt, either direction** |
> | Gunnison CO · Durango CO (San Juan) — the southernmost sub-basins only | Above 33% (weak) |
> | *contrast:* coastal CA, Tucson | **Above 50%** |
> | *contrast:* Phoenix | Above 40% |
> | *contrast:* **Great Falls MT / Missoula MT (N Rockies)** | **BELOW 40% / Below 33% — dry tilt** |
> ⇒ **The wet signal is south and coastal; the Northern Rockies are dry; and Powell's inflow zone sits between them in Equal Chances at 10 of 12 headwaters points tested.** Exactly the geometry this guard describes.
> 🔄 *(2026-10-29: the 15 Oct issuance moves it back north. See §6 "15 OCT ISSUANCE". The paragraph below describes 9/17 only.)*
> ⚠️ **AND IT MOVED THE WRONG WAY FOR RELIEF:** the single change from the 8/20 issuance is **Aspen CO dropping OFF its weak Above-normal tilt into Equal Chances** — the wet tilt retreated *southward, away from* the Upper Basin, while historic-event odds rose 69→75%. **Evidence strengthened, not weakened.**

**② The northern tier goes MILDER, not colder — I got this backwards once and shipped it.** On 8/3 I told MARCO a very-strong El Niño gives an "active/cold Northern-tier winter." **CPC says the inverse:** storm track shifts **SOUTH**, the North goes **milder and less stormy**. I reasoned validly from an unchecked premise, produced a confident coherent wrong finding, and **MARCO logged it as a valued counterweight to its own thesis** — the worst place for a wrong finding to sit. Found by accident 9 days later, pulling the same primary for an unrelated question (**L-13**).

> **The rule that came out of it: when a packet's CONCLUSION turns on a directional climate premise, pull the primary for THAT premise in the same session. It is one fetch. And a well-argued packet deserves MORE premise-scrutiny than a hedged one, because its polish suppresses the reader's own checking.**

---

## 5. THE RELIABILITY PROBLEM — now governing (L-14 → L-17)

Composites are built mostly from **weak and moderate** events. I hit the degradation **three times in one afternoon** on 8/12, at an amplitude *below* the current forecast:

1. **PJM winter peak** — n=2 very-strong analogues, split 1-1; **both of PJM's highest winter peaks came in *non*-strong-El-Niño winters.**
2. **PNW snowpack** — UW: WA snowpack "fared pretty well" in all three very-strong events (1984/1998/2016), against the composite's dry signal.
3. **Polar vortex** — NOAA's own caveat that **1997-98 produced no major SSW.**

⇒ **With CPC now at 83% for OND (8 Oct; 75% on 9/10, 69% on 8/13) for an out-of-sample event, the analogue set trends to n=0 and every composite becomes an extrapolation.** **The composite still gives the mean sign; it does not give the tail, and at extreme amplitude it may not give the mean either.**

**The only non-extrapolated substitute is a season-specific forecast** → **CPC DJF 2026-27 outlook.** ✅ **FETCHED 2026-09-18 — see §6.** The PUBLIC-AND-UNFETCHED status is closed.

⚠️ **But it does not retire L-14, and the prior pass already established why:** CPC states it *"strongly utilized"* ENSO composites in building this outlook **because of the magnitude of the event** (logged 8/21). **A season-specific outlook is not composite-independent — L-14 constrains this product rather than being retired by it.**

---

## 6. ✅ THE CPC DJF 2026-27 OUTLOOK — FETCHED 2026-09-18 (the standing open item, closed)

**9/17 issuance detail (PJM footprint 40% above-normal, Cleveland 50%, Richmond/Roanoke 33%; identical to 8/20 at all 8 points) → rotated verbatim 2026-10-29 (archive piece 3).** The 15 Oct diff below carries the comparison.

### 🔄 15 OCT ISSUANCE vs 17 SEP — it DID move this time (worker 2026-10-29)

`seastemp_202610.zip` / `seasprcp_202610.zip`, layers `lead2_DJF_temp` / `lead2_DJF_prcp`, **`Fcst_Date` 20261015**, `Valid_Seas` "DJF 2026-2027". Point-in-polygon at the same 26 points; the reader reproduces every 9/17 value in this section.

| Point | Temp 9/17 → 10/15 | Precip 9/17 → 10/15 |
|---|---|---|
| **Chicago (ComEd)** | Above 40 → **Above 50** | EC → EC |
| **Richmond VA** | Above 33 → **Above 40** | Above 50 → Above 50 |
| **Seattle** | Above 40 → **Above 50** | EC → EC |
| Pinedale WY | EC → **Above 33** | EC → EC |
| **Grand Lake CO · Aspen CO · Page AZ (Powell)** | EC → EC | **EC → Above 33** |
| Orlando · Tampa | Normal 33 → Normal 33 | **Above 60 → Above 70** |
| Missoula MT | Above 40 → Above 40 | **Below 33 → Below 40** |
| Phoenix | EC → EC | **Above 40 → Above 50** |
| Cleveland 50 · DC/Phila/Pitt/Columbus/Newark 40 · Miami · Steamboat · Grand Jct · SLC · Gunnison · Durango · LA · Tucson · Great Falls | unchanged | unchanged |

⇒ **Two changes against what this section said on 9/17.** ① The PJM warm signal **strengthened** (Chicago 50, Richmond 40); the rest of the footprint is unchanged. ② **The weak wet tilt moved NORTH INTO the Upper Basin** (Grand Lake, Aspen, Page AZ, all in the lowest 33–40% band). That **reverses** the 9/17 "retreated southward" note under §4 guard ①. Steamboat, Pinedale, Grand Junction and SLC stay EC on precip, so 6 of 10 headwaters points carry a weak wet tilt or none. ⚠️ `seastemp_202610.zip` is **Last-Modified 19 Oct**, 4 days after its `Fcst_Date`; `seasprcp` is 15 Oct. The worker cannot see what the re-post changed. **Worker does not grade guard ①. AEOLUS adjudicates.**

---

## 7. 🆕 TELECONNECTIONS — STRATOSPHERIC POLAR VORTEX · AO · NAO (first read 2026-10-29)

⛔ **No registered instrument yet. Values are in LOG only, and names and commands are PROPOSED (RUN_REPORT 10/29).** These primaries were named in AEOLUS's spawn prompt. They are **not** a substitution for a registered source.
**Metric:** zonal-mean zonal wind **U at 10 hPa, 60°N**. A reversal means daily-mean U < 0. **The worker does not classify an SSW.** Definitions (daily mean vs 00z, Nov–Mar window) are AEOLUS's call.

### OBSERVED (analyses) — 🟢 still WESTERLY, no reversal

| Date | GEOS-FP daily mean | IFS analysis 00z | CPC GFS chart |
|---|---|---|---|
| 10/24 | **+23.2** (peak) | — | ~+23 |
| 10/26 | +21.9 | +21.8 | ~+21 |
| 10/27 | +19.7 | +20.6 | ~+19 |
| 10/28 | +16.3 | +17.4 | ~+17 (DOY 301) |
| 10/29 | — | **+14.1** | — |

Three independent analyses agree within ~1 m/s. U is **falling ~3 m/s per day** from the 10/24 peak. CPC chart CFSR climatology, chart-read and approximate: 10/28 mean ~22, 10th percentile ~13.

### FORECAST — 🔴 a reversal is forecast by every ECMWF product pulled

| Product (00z) | First day < 0 | Minimum | Back above 0 |
|---|---|---|---|
| IFS HRES 10/26 | 11/05 | −0.7 (11/05) | 11/06 |
| IFS HRES 10/27 | 11/04 | −3.8 (11/06) | 11/10 |
| IFS HRES 10/28 | 11/05 | −2.8 (11/11) | after 11/12 |
| **IFS HRES 10/29** | **11/05** | **−4.9 (11/09)** | 11/13 |
| **IFS ENS 10/29 (50 mem.)** | mean **11/05** (−0.7, 39/50 < 0) | mean **−3.8** (11/09–10); member min −9.4 | mean ≈0 on 11/13 |
| CPC chart: GFS runs | ~11/05 | ~−2 to −4 (11/08–10) | ~11/11 |
| CPC chart: GEFS traces | none clearly < 0 | ~+1 | — |

⇒ **Run to run, the deterministic signal has deepened (−0.7 → −4.9) and lengthened (1 → 8 days).** On ENS 10/29, **50/50 members** go easterly on at least one day, and 49–50/50 on 11/08–11/09. **GEFS is the outlier:** its chart traces bottom out near +1 m/s. ⚠️ Early-November U < 0 would sit **below the CPC chart's CFSR minimum line** for those dates (~+11 to +14, chart-read; the climatology period is not printed). ⚠️ **Not verified:** WALTER's *"GEPS 67% easterly within 15 days"* (no ECCC pull) and the scorvec.com figures (secondary, not used).
⚠️ **README §5 / DOSSIER §5 caveat still applies:** NOAA notes **1997-98 produced no major SSW.** No ENSO→vortex composite is quoted here.

### AO / NAO — CPC daily (`ftp.cpc.ncep.noaa.gov/cwlinks/`, cdas csv, Last-Modified 28 Oct)

| | Observed latest | Recent path | GEFS 10/28 init (31 mem.) |
|---|---|---|---|
| **AO** | **+1.20 (10/26)** | +2.78 (10/19) → +0.20 (10/23) → +1.20 | mean +0.98 (10/31) → **−0.87 (11/02, 31/31 < 0)** → −1.62 (11/03) → −1.23 (11/12, 81% < 0) |
| **NAO** | **+0.33 (10/26)** | +1.58 (10/18) → −0.79 (10/23) → +0.33 | mean +0.89 (11/01) → −0.22 (11/03, 74% < 0) → −0.58 (11/12, 84% < 0) |

⚠️ The legacy `norm.daily.ao.index.b500101.current.ascii` stopped at 9/30 (Last-Modified 5 Oct). **Use the `cdas` csv.** The forecast AO turns negative on 11/02, three days **before** the forecast vortex reversal. The worker draws no causal link either way.

---

## OPEN QUESTIONS

1. *(closed DJF-outlook item → archive piece 4)*
2. **Should channel signs be re-derived against RONI rather than ONI?** (§2). Real work, not a one-line fix, **still not done.** The two reads at the current season, side by side, never averaged:
   - *(JJA-era side-by-side reads → archive piece 5; current reads are in the 2026-10-09 update below and §1)*
   - *(10/09 ONI/RONI JAS update → archive piece 7; the same figures are in §1)*
3. **Track the ONI−RONI offset as OND approaches** — current **+0.47** (JAS). Not a conversion factor. *(Full note → archive piece 8.)*
4. 🔴 **The ERSSTv5 → v6 basis change (2026-08-10) needs an AEOLUS ruling.** *(10/29 status: `SOURCES.md` ①/② now read ERSSTv6 and AEO-02 materiality is ruled (KB-AEO-125). The residual v5 wording is at `README.md` line 22 and in the stale SOURCES known-traps values. Proposed text is in RUN_REPORT 10/29. Superseded sentence: "`SOURCES.md` documents ONI and RONI as ERSSTv5".)* **Both files are v6.** §2's tables reproduce exactly, so nothing derived here breaks — **but `AEO-02 resolves on ONI`, and the instrument it resolves on changed basis mid-prediction.** Worker reports; **AEOLUS grades.** Also: `SOURCES.md` ①/② need their basis line corrected.
5. *(✅ RELATIVE-vs-TRADITIONAL resolution — ADOPTED as KB-AEO-181 → archive piece 6)*
6. **AEO-02** resolves on ONI in NDJ — state in STATUS; worker does not resolve. *(→ archive piece 10)*
7. **AEO-07 / AEO-08 (PJM DJF)** — measurement only, not graded: see §6, the 15 Oct issue (PJM warmth STRENGTHENED). *(The stale 'unchanged from 8/20' wording → archive piece 9.)*
8. **AEO-09** (`../wildfire/`) remains the cheapest live test of composite reliability: does the wet-south signal verify **where it is strongest**? If not, L-14 governs and the C1 suppression leg — same composite machinery — downgrades with it.
9. **NEW — no registered source for MJO / PDO / IOD / SOI.** `SOURCES.md` carries no numeric pull for any of them and the weekly deck carries no extractable figure. Only qualitative CPC text exists (*"the traditional and equatorial Southern Oscillation indices remained negative"*, 9/10). **The IOD has no CPC product at all** — its operational index is Australian BoM, outside the "CPC primaries only" rule. **Nothing was substituted.** AEOLUS's call whether to register them.
10. **NEW 10/29 — `verystrong_prob_ond` has no source since 8 Oct.** The prose stopped stating a very-strong figure. The number now exists only in the Strength Outlook, which is an **image** (`/archives/enso/roni/images/2026/enso-strengths-probs-current.png`, page "Issued October 2026"). OND P(RONI ≥ 2.0): Sep issue 98, Oct issue 100. The redefinition is proposed in RUN_REPORT 10/29. **AEOLUS rules.**
11. **NEW 10/29 — stratosphere and AO/NAO have no registered instrument** (§7). Values are in LOG only. Proposed names and commands are in RUN_REPORT 10/29.
