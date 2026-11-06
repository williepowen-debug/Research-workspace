# Vortex persistence and descent read, 2026-11-06 (DOCKET L906, GATE-TERRY-UNG-01)

Observation only. No score, band, gate or card term moves from this folder.

| File | What it holds |
|---|---|
| `gfs_u60N_profile_10-30-50-100hPa.txt` | GFS 0.25 zonal-mean U at exact 60N, 10/30/50/100 hPa: 00Z `.anl` 10/29 to 11/6, 06Z `.anl` 11/6, then the 11/6 06Z forecast to f384. NOMADS, 1,440 longitudes |
| `ecmwf_oper_u60N_profile_20261106_00z.txt` | ECMWF IFS HRES 11/6 00Z, 10/50/100 hPa, to +240h. 30 hPa is not in the open-data index, so the 30 hPa read is GFS only |
| `ecmwf_ens_u10_60N_20261106_00z.txt` | ECMWF ENS 11/6 00Z, 10 hPa 60N, 50 perturbed members |
| `cpc_gefs_ao_forecast_init_20261105.txt` | CPC GEFS Arctic Oscillation forecast, init 11/5, 31 members |
| `prof.py` `oper.py` `ens.py` | The decoders. They need eccodes, installed per `regime/SOURCES.md` |

Limits: the analysis lows are lows of the sample (00Z each day plus 11/6 06Z), not of every cycle. No climatology is in hand, so the 30/50/100 hPa levels are read as levels and sign, not as anomalies. GEOS-FP returned a server error on the 11/5 to 11/6 request, so there is no third field.
