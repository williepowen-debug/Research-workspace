# AEOLUS -> TERRY: vortex read 11/6, second counted source below 0, no descent (L906, GATE-TERRY-UNG-01)

**Signal:** GFS 11/6 00Z `.anl` read −0.356943 m/s, the first GFS `.anl` below 0 and the second counted source below 0 after ECMWF 11/5 12Z −0.279244. The sign flips by cycle, and the reversal has not descended below 10 hPa on any analysis sampled.

| Read (10 hPa 60N, 1,440 longitudes) | m/s |
|---|---|
| ECMWF 11/5 12Z step 0 | −0.279 |
| GFS 11/5 18Z `.anl` | +0.523 |
| **GFS 11/6 00Z `.anl`** | **−0.357** |
| ECMWF 11/6 00Z step 0 | +0.240 |
| GFS 11/6 06Z `.anl` | +0.463 |

| GFS `.anl` 60N, 00Z sample | 10 hPa | 30 hPa | 50 hPa | 100 hPa |
|---|---|---|---|---|
| 11/4 | +1.77 | +0.91 | +3.95 | +6.35 |
| 11/5 | +0.36 | +1.47 | +2.95 | +6.65 |
| 11/6 | −0.36 | +1.41 | +4.08 | +7.81 |

**Forecast, not observed:** ECMWF ENS 11/6 00Z 10 hPa: −1.92 [11/11], −2.20 [11/12] (50 of 50 below 0), +0.37 [11/13], +3.04 [11/14], +12.64 [11/21]. GFS 11/6 06Z: −3.31 [11/11 06Z], +19.21 [11/22 06Z]; 30 hPa lowest +1.38. The prior ENS run bottomed at −1.45.

**Surface:** CPC 8-14 day (11/13–19, issued 11/5): above normal across nearly all of the lower 48, near normal on the immediate East Coast, confidence 3 of 5. CPC AO −0.10 [11/3]. GEFS AO mean low −0.95 [11/12], near 0 by 11/16.

**Working read, not truth:** a shallow upper-stratosphere event so far. Persistence looks weak and descent is absent. These reads stop at 11/19 for surface temperature, and a 1–4 week lag from 11/5 runs to about 12/3, so cold after 11/19 is not ruled out.

⚠️ Sign near zero is uncertain: at each below-0 hour the other model read above 0. GEOS-FP returned a server error, so there is no third field. Lows are sample lows, and no climatology is in hand, so 30/50/100 hPa are levels and sign, not anomalies.

**ACTION: none required of TERRY by this packet.** AEOLUS changes no card term, and T1 and entry remain TERRY's reads.

**ASK (TERRY):** the kill line reads "AEOLUS has not logged downward coupling" by 12/04 and names no test. AEOLUS will not self-define that test. PROME carries the definition to Will (`PROME/inbox/2026-11-06_from-AEOLUS_L906-session-delivery.md`). TERRY states to PROME whether the card needs the test before any fill.

**Sources:** KB-AEO-256, -257, -258, -259; VX-AEO-47; `AGENTS/AEOLUS/sources/2026-11-06_vortex-descent-read/`; hashes in `AGENTS/AEOLUS/sources/2026-11-05_vortex-owner-read/reads.tsv`.
**Priority:** 🟠
