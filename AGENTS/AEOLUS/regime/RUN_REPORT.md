run_date: 2026-10-29 (ENSO pulls 00:27 EDT; Discussion/deck 06:03; vortex, AO/NAO and GIS 07:40–07:57 EDT; report written 07:58 EDT)
worker: AEOLUS regime/ domain worker · trigger: AEOLUS dark 10/21–10/29, DOSSIER as-of 10/09, WALTER polar-vortex signals of 10/23–25

observations_added: 17 rows to `workbook/SERIES.tsv`: 12 weekly rows (07OCT / 14OCT / 21OCT × Niño-3.4 / 3 / 1+2 / 4) and 5 revision rows for Sep weeks. 9 rows to `workbook/LOG.tsv`: weekly record; 26 Oct deck; no Discussion since 8 Oct; 15 Oct DJF outlook diff; vortex observed; IFS HRES vortex forecast; IFS ENS vortex forecast; AO/NAO; run record. No new ONI, RONI, sstoi or odds rows, because none of those files has printed anything new. `DOSSIER.md` went from 22,605 B to **31,018 B**: header, a 10/29 pass block, §1, a §6 October diff, the new §7 (vortex/AO/NAO) and open questions 3, 4, 10 and 11.

---

## threshold_state (worker does not grade)
- **ONI** JAS **+2.16** (unchanged; ASO not printed). vs strong ≥1.5: **+0.66 above**. vs very strong ≥2.0: **+0.16 above**. AEO-02 is specified on NDJ, which has not arrived. Not graded.
- **RONI** JAS **+1.69** (unchanged). vs historic +2.5 (OND): **0.81 below**. NOT-FIRED. The bar is an OND target, not a present-state test.
- **OISST monthly Niño-3.4** Sep **+2.84** (unchanged; October not printed). Reported only, no line.
- **Weekly Niño-3.4** (`wksst9120.for`, Last-Modified 28 Oct): 30SEP 3.2 → 07OCT 3.3 → 14OCT 3.3 → **21OCT +3.4. File record, rank 1 of 2,356 weeks, no tie.** Pre-2026 max +3.0 (18NOV2015). Same week: 1997 +2.0, 2015 +2.3. Niño-3 **+4.3** (record) · Niño-1+2 **+5.2** (30SEP +5.3 is the max) · Niño-4 **+1.1**. **AEOLUS's 00:18 ET figures verified to the cell.**
- **Discussion odds:** unchanged, because no issue has come out since **8 Oct**. Historic SON 54 / OND **83** / NDJ 70. Next issue **12 Nov**.
- **ONI−RONI** recomputed at **+0.47** (JAS, same season). Not a conversion.
- **Polar vortex, U 10 hPa 60°N (no registered threshold):** observed **+14.1 m/s** (IFS analysis 10/29 00z; GEOS-FP daily mean 10/28 +16.3). **Westerly. No reversal observed.** Forecast: below zero from ~**11/05** (details under changes).

## changes
- **Weekly:** 30SEP +3.2 → 21OCT **+3.4** (+0.2 in 3 weeks). Revisions (OISSTv2.1 near-real-time): 16SEP 1+2 4.6→4.7; 23SEP 1+2 4.7→4.9, Niño-3 3.9→4.0; 30SEP Niño-3 4.0→4.1, Niño-4 1.2→1.3.
- **Weekly deck re-issued 26 Oct.** It restates the 8 Oct odds and gives relative weekly bullets **0.0 / 2.5 / 3.6 / 4.4** (Niño-4/3.4/3/1+2; 5 Oct: 0.1/2.3/3.3/4.5). Those are RELATIVE values and not scored. RONI JAS is given as *"1.7ºC"*.
- **CPC DJF outlook, 15 Oct vs 17 Sep: this time it moved.** Temperature: **Chicago Above 40→50, Richmond 33→40, Seattle 40→50**, Pinedale EC→Above 33. Cleveland 50 and the rest of PJM at 40 are unchanged. Precipitation: **Grand Lake CO, Aspen CO, Page AZ EC→Above 33** (the weak wet tilt now reaches the Upper Basin; Steamboat, Pinedale, Grand Junction and SLC stay EC). Orlando and Tampa 60→70, Phoenix 40→50, Missoula Below 33→40. **This reverses the 9/17 "did not move" and "retreated south" observations** in DOSSIER §4/§6. `seastemp_202610.zip` was re-posted on 19 Oct; what changed is not visible.
- 🔴 **Polar vortex — the forecast firmed between WALTER's 10/23–25 signals and today:**
  - Observed (GEOS-FP daily means): 10/24 **+23.2** (peak) · 10/26 +21.9 · 10/27 +19.7 · 10/28 **+16.3**. IFS 00z analysis: 10/26 21.8 · 10/27 20.6 · 10/28 17.4 · **10/29 14.1**. CPC GFS chart ~17 on 10/28. The three analyses agree within ~1 m/s.
  - **IFS HRES, four consecutive 00z runs (10/26, 10/27, 10/28, 10/29), all reverse U** around 11/04–05. Minimum −0.7 → −3.8 → −2.8 → **−4.9 (11/09)**. Days below zero: 1 → 6 → 8+ → 8.
  - **IFS ENS 10/29 (50 members): the MEAN is easterly from 11/05 to 11/12** (mean −3.8 on 11/09–10; member min −9.4). Members below zero: 8/50 on 11/04, 39/50 on 11/05, **50/50 on 11/09**. **WALTER's "IFS mean stays weakly westerly" no longer holds on this run.** The earlier runs were not checked; open data keeps only 4 days.
  - **GEFS is the outlier.** CPC's GEFS chart traces bottom near **+1 m/s**, none clearly below zero. GFS deterministic traces reach about −2 to −4 (chart-read).
  - The CPC chart's CFSR **minimum** line in early Nov reads about +11 to +14 m/s (chart-read). An early-Nov reversal would sit below it.
- **AO/NAO (new):** AO observed +2.78 (10/19) → +0.20 (10/23) → **+1.20 (10/26)**. NAO **+0.33 (10/26)**. GEFS (init 10/28, 31 members): the **AO mean turns negative on 11/02 with 31/31 members below zero**, falls to −1.62 on 11/03 and is −1.23 on 11/12. The NAO mean turns negative on 11/03 and is −0.58 on 11/12.

## proposed_findings (PROPOSALS only — AEOLUS adjudicates)
1. **Weekly Niño-3.4 +3.4 (21OCT) is the new file record**, rank 1 of 2,356 with no tie. Niño-3 +4.3 is also a record. The traditional OISSTv2.1 basis is not comparable to the RONI +2.5 bar. Source: `wksst9120.for`, Last-Modified 28 Oct.
2. 🔴 **Vortex: a reversal is FORECAST, NOT OBSERVED.** Observed 10 hPa 60°N U is +14.1 m/s (10/29 00z) and falling ~3 m/s/day. Every ECMWF product pulled reverses it from ~11/05: 4/4 HRES runs, and the ENS mean from 11/05–11/12 with 50/50 members below zero on 11/09. Run to run it has deepened and lengthened. GEFS dissents (lowest about +1). Sources: ECMWF open data (oper + enfo, 00z), NASA GMAO GEOS-FP OpenDAP, CPC SSW charts. ⚠️ The NOAA caveat (1997-98, no major SSW) and DOSSIER §5 are unchanged. **No ENSO→SSW composite is offered, and no SSW classification.**
3. **AO forecast turns negative 11/02 (GEFS 31/31)**, three days before the forecast vortex reversal. That is timing only. No causal claim, which would be a HYPOTHESIS. Source: CPC `cwlinks` cdas/gefs csv, 28 Oct.
4. **CPC 15 Oct DJF outlook strengthened PJM warmth** (Chicago 50, Richmond 40; relevant to AEO-07/08) **and moved a weak wet tilt into the Upper Basin** (Grand Lake, Aspen, Page AZ at Above 33, the lowest band). That is relevant to §4 guard ① and to C6. Source: `seastemp_202610` / `seasprcp_202610` `lead2_DJF`, Fcst_Date 20261015.
5. **Owed #12, part (a): redefine `verystrong_prob_ond`.** Proposal: **close it** as a prose-sourced series (last row 2026-09-10 = 90, *">90% … fall and winter"*, a floor over a two-season window). **Register a new instrument `p_roni_ge20_ond`** (pct, source `CPC-roni-strengths`) for OND P(RONI ≥ 2.0) from the Strength Outlook table, with backfill **2026-09-10 = 98** and **2026-10-08 = 100** (both already in DOSSIER §1b). **Reason for a new name rather than a redefinition:** splicing a prose floor over "fall and winter" onto a single-season table value would make 90→100 read as a +10 rise when the definition changed. ⚠️ The table is an **image** only (`/archives/enso/roni/images/2026/enso-strengths-probs-current.png`; page `https://cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/strengths/` says "Issued October 2026"). It is a chart-read instrument and should carry that label.
6. **Owed #12, part (b): ERSSTv5→v6 wording.** SOURCES ① and ② already read ERSSTv6 and AEO-02 materiality is ruled (KB-125). The 26 Oct deck re-states the same CPC note (*"8/10/26: NCEI is discontinuing ERSSTv5, so RONI values have switched to ERSSTv6. The weekly OISSTv2.1 data remains unaffected."*), and its episode table is titled *"RONI computed using ERSST.v6"*. ONI/RONI are still Last-Modified 3 Oct, so there is no new revision. Residual edits proposed, none made:
   - `README.md:22`: `30-yr centred, ERSSTv5` → `30-yr centred, ERSSTv6 (ERSSTv5 until 2026-08-10)`.
   - `SOURCES.md` ①: add *"CPC's footnote names RONI only. ONI's v6 basis rests on the independent table match, not on the footnote."*
   - `SOURCES.md` known-traps, row 1: replace the stale *"+1.39 / +0.98 / +2.03 / +2.6"* with *"see DOSSIER §1 for the current four"*. This is the same values-decay defect the 9/28 AGENT.md re-cut removed.
7. **Register the vortex and AO/NAO instruments** (proposed names; AEOLUS approves):
   - `spv_u10_60n_obs` (m/s, `GMAO-GEOS-FP`, daily mean of 8 analyses): `curl -gsS "https://opendap.nccs.nasa.gov/dods/GEOS-5/fp/0.25_deg/assim/inst3_3d_asm_Np.ascii?u[T0:T1][30][600][0:1151]"`. lev index 30 = 10.0 hPa, lat index 600 = 60.0°N. T = 8 × (days since 2017-12-01) + hour/3. **At most 16 times per request** (larger requests returned 504/502). `-g` is required for the brackets.
   - `spv_u10_60n_ens_mean` / `spv_ens_frac_easterly` (`ECMWF-IFS-opendata`): read the JSON `.index` at `https://data.ecmwf.int/forecasts/<YYYYMMDD>/00z/ifs/0p25/{oper|enfo}/<YYYYMMDD>000000-<step>h-{oper-fc|enfo-ef}.index`, select `param u, levelist 10, levtype pl`, and range-GET each message. The GRIB2 is **CCSDS-packed (template 5.42)**, so decoding needs eccodes, which is **not in `.venv`**. The worker installed it into its scratchpad only (`pip --target`). Retention is ~4 days.
   - `ao_daily` / `nao_daily` (`CPC-cwlinks`): `https://ftp.cpc.ncep.noaa.gov/cwlinks/norm.daily.ao.cdas.z1000.19500101_current.csv` and `…nao.cdas.z500…csv`. Forecasts are in `norm.daily.{ao.gefs.z1000|nao.gefs.z500}.120days.csv`.

## gaps
- **GEPS "67% easterly within 15 days" (WALTER) is NOT verified.** No ECCC source was pulled, and it is not in the brief's named primaries.
- **scorvec.com figures were not used.** It is a secondary.
- **GEFS 10 hPa was not decoded numerically.** NOMADS OpenDAP is retired: `https://nomads.ncep.noaa.gov/dods/` returns *"OpenDAP format has been retired. Please see Service Change Notice 25-81"*. GEFS is read only off the CPC chart image (±1–2 m/s), and CPC does not label which runs the green traces are.
- **GEOS-FP OpenDAP partial.** Requests for 9/29–10/06, 10/11–12, 10/15–16 and 10/19–20 failed with `504 Gateway Time-out` / `502 Proxy Error`. 10/21–10/28 are complete. A 368-time single request also 504'd.
- **No GEOS-FP or MERRA-2 forecast pulled.** MERRA-2 lags by weeks and was not tried.
- **The ECMWF ENS open-data u/10 hPa set contains 50 perturbed members and no control.** The ENS was sampled once a day at 00z, so "first day < 0" can be off by up to 24 h.
- **ASO ONI/RONI and the October monthly OISST are not printed** (files Last-Modified 3 Oct / 3 Oct / 5 Oct). That is a timing gap, not a failure.
- **Legacy AO ascii** (`norm.daily.ao.index.b500101.current.ascii`) stopped at 2026-09-30 (Last-Modified 5 Oct). The cdas csv is current.
- **Strength-table and outlook pages:** still not registered SOURCES commands, and still image or HTML only.
- 🟡 **READ CAP:** DOSSIER is **31,018 B**, under the 32,550 budget, but `read_cap_check.py` puts it at **95%, the rotate tier (≥75%)**. The rotation home `AGENTS/AEOLUS/archive/` is outside the worker's write scope, so nothing was rotated. Candidates: the 10/09 pass block (~3.5 KB; its content is in LOG and KB-181), the September-issue table in §1b (~1.3 KB), and the 9/17 detail in §6. Rule 5 stops below 22,785 B.
- All registered ENSO commands returned HTTP 200 with no errors.

## files changed
- `AGENTS/AEOLUS/regime/workbook/SERIES.tsv` (+17 rows, append-only)
- `AGENTS/AEOLUS/regime/workbook/LOG.tsv` (+9 rows, append-only)
- `AGENTS/AEOLUS/regime/DOSSIER.md` (22,605 → 31,018 B)
- `AGENTS/AEOLUS/regime/RUN_REPORT.md` (overwritten; this file)
