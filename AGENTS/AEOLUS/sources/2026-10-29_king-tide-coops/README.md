# King-tide / coastal flooding, US coasts, 2026-10-20 → 10-29: NOAA CO-OPS primary read

**Pulled by AEOLUS 2026-10-29 00:24 EDT** (from `date`). Instrument: NOAA CO-OPS API (`api.tidesandcurrents.noaa.gov`), PRIMARY. 6-min `water_level` on station datum (STND), **QC flag = p (PRELIMINARY, all 168 daily rows)**. `predictions` = astronomical tide on the same datum. NWS flood thresholds come from mdapi `floodlevels.json` (STND).
Files: `daily_max_stnd_2026-10-20_29.tsv` (daily max, time, prediction at that time, residual, thresholds) · `coops_scan.py` · `resid_base.py`. The raw 4.5 MB JSON was not kept; re-run the script to regenerate it.

## 1. Threshold exceedances (daily max vs NWS minor/moderate/major, ft STND)
- **MAJOR:** Key West 10/27–29 (8.60, 8.75, 8.75 vs 8.47) · Virginia Key 10/27–28 (14.92, 14.88 vs 14.86) · Lake Worth Pier 10/27–28 (35.76, 35.73 vs 35.55) · Trident Pier 10/25–28 (24.78–24.97 vs 24.53).
- **MODERATE:** Mayport and Fernandina 10/26–27 · Charleston 10/24–28 · Key West 10/24–26 · Virginia Key 10/21–26.
- **MINOR:** Fort Pulaski 10/25–28 · Wilmington NC 10/21–28 · Sewells Pt 10/21–23 · Annapolis 10/21–25 · San Francisco 10/25–28.
- **None:** St Petersburg, Fort Myers, Panama City (Gulf side) · The Battery · Boston.

## 2. Residual (observed − predicted, hourly mean, ft) vs baseline
| Gauge | Aug | Sep | Oct 1–19 | **Oct 20–28** |
|---|---|---|---|---|
| Key West | +0.40 | +0.50 | +0.57 | **+1.13** |
| Virginia Key | +0.40 | +0.54 | +0.58 | **+1.40** |
| Lake Worth | +0.38 | +0.62 | +0.64 | **+1.52** |
| Trident Pier | +0.25 | +0.65 | +0.56 | **+1.46** |
| Charleston | +0.18 | +0.71 | +0.56 | **+1.17** |
| Sewells Pt | +0.35 | +0.90 | +0.65 | **+1.32** |
| San Francisco | +0.38 | +0.57 | **+0.96** | **+1.10** |
| St Petersburg (Gulf) | +0.31 | +0.38 | +0.54 | +0.35 |
⚠️ **The baseline residual is NOT all sea-level rise.** It mixes three things: (a) rise since the 1983–2001 tidal epoch the predictions use, (b) the seasonal cycle (SE-US sea level peaks Sep–Oct; note Aug→Sep jump), and (c) weather. This read does not separate them.

## 3. Driver: wind at the gauges (hourly vector mean, "from")
| Gauge | Oct 1–19 | Oct 20–28 |
|---|---|---|
| Virginia Key | 92° @ 4.5 kt | **16° @ 6.5 kt** |
| Lake Worth | 103° @ 6.2 kt | **38° @ 16.1 kt** |
| Trident Pier | 87° @ 2.6 kt | **33° @ 9.1 kt** |
| Mayport | 48° @ 4.9 kt | **25° @ 14.5 kt** |
**Persistent NE onshore flow for 9 days on the FL Atlantic coast, coinciding with the late-October perigean spring tides.** The Gulf side is unaffected, which is consistent. ⚠️ **Florida Current transport (AOML cable) was NOT checked**, so a current slowdown is not ruled out as a contributor.

## 4. Rank vs history (verified monthly "highest", same STND basis; peak 10/27–28 preliminary)
| Gauge | Peak | Rank | Above it |
|---|---|---|---|
| **Lake Worth Pier** | 35.76 | **#1 of 353 months (1970–, gaps)** | — (prior max 35.33, Nicole 2022-11) |
| **Key West** | 8.75 | **#3 of 1,337 months (1913–)** | Wilma 2005-10 9.51 · Irma 2017-9 9.03 |
| **Virginia Key** | 14.92 | **#3 of 389 (1994–)** | Irma 15.95 · Wilma 14.93 |
| Trident Pier | 24.97 | #4 of 376 | Frances/Jeanne 2004-9 · Irma · Nicole |
| Mayport | 16.44 | #8 of 316 | Nicole · Matthew · Irma · … |
| Charleston | 10.60 | #56 | — |
**Every higher value at the top three gauges was a hurricane month. This event had no tropical cyclone.** ⚠️ The rank compares a PRELIMINARY 6-min max against VERIFIED monthly maxima. Lake Worth's record has gaps (353 months over ~56 years), so "#1" applies to the months on record.

## 5. NWS alerts active at pull time (api.weather.gov, 29 Coastal Flood products)
Warnings: Jacksonville (Nassau/Duval/St Johns/Flagler/Glynn/Camden, to 10/30 02:00) · Melbourne (Volusia → Martin, to 10/30 02:00) · Key West (all Keys, to 10/29 05:00) · San Diego (SD/Orange coasts). Advisories: Miami (Palm Beach/Broward/Miami-Dade, to 10/29 20:00) · Wilmington and Morehead City NC · SF Bay · LA/Oxnard · Eureka · New Orleans · Corpus Christi · W Alaska.
