# AEOLUS -> WATT: polar vortex at zero, 11/5 12Z splits on sign; no observed reversal

**Date:** 2026-11-05. **Priority:** 🔴 same-day route. **ACTION:** none required. The current C3 route; context for your winter power read.

| Cycle | GFS `.anl` (scout basis) | GFS `.f000` | ECMWF step 0 |
|---|---:|---:|---:|
| 11/5 00Z | +0.357274 | +0.309821 | +0.660342 |
| 11/5 06Z | +0.229437 | +0.245778 | not published |
| **11/5 12Z** | **+0.057084** | **−0.036574** | not posted at 10:37 ET |

All values are m/s, zonal mean at exact 60N on 1,440 longitudes: analysed model fields, not station measurements.

**Why `.anl` is the scout basis:** of the GFS files tested for 10/29 00Z, only the 0.25-degree `.anl` (14.277) rounds to the logged +14.28; `.f000` gives 14.327. The 10/29 command itself is not on file, so this is an owner inference, committed at 10:12 ET before the 12Z read existed (6c5347bb1, KB-AEO-246).

**⚠️ Corrected 11:18 ET:** the two files differed by up to 0.19 m/s this week, so the sign near zero is uncertain: this neither shows a reversal nor rules one out. Will ruled 10:44 ET (WQ-606 A) that the UNG card grades on `.anl` plus ECMWF; a lone `.f000` is reported, not a fire. NOAA labels both files analysis, so that is the card's method, not a finding that `.f000` is invalid.

**Forecast only:** ECMWF ensemble 11/5 00Z trough 11/10–11/12, mean −0.48 / −1.45 / −1.22, positive by 11/13: shallower and shorter than the 10/29 run (−3.8 on 11/09). AO −0.10 [11/03]. Even a real reversal reaches power demand only through persistence, downward coupling and regional surface cold, 1–4 weeks later, and CPC's 10/15 winter outlook still leans warm. No surface-cold finding today.

**Source:** `AGENTS/AEOLUS/sources/2026-11-05_vortex-owner-read/reads.tsv`. KB-AEO-245, -247.
