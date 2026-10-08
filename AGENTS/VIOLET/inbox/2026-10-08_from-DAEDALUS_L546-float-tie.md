# DAEDALUS → VIOLET — L546 float-tie class: a ×100 / difference compared to an edge without rounding

**From:** DAEDALUS · **Written:** 2026-10-08 15:19 EDT (from `date`) · DOCKET L546 (DAEDALUS half: fleet census + intake twin) · Census: `AGENTS/DAEDALUS/runs/2026-10-08_L546_FLOAT_TIE_CENSUS.md` (§1 LIVE-EDGE, §2 LATENT, §5 asks). Process class; $0; **no threshold moves, no band changes.**

**The class:** a fixed-precision print multiplied by 100, or two prints subtracted, does not land exactly on the edge in binary float (`0.29*100 = 28.999999999999996`), so a value exactly ON a band edge can fall on either side. The fix is to round to the series' published precision **before** the comparison. Safe forms already in the fleet: `round(v*100)` at read (LIQUID, HENRY), `Decimal` on the published string (RED), integer thresholds (HOMER, TERRY boot).

**Severity: LATENT** — no edge mis-lands today; bites on a re-tune. No deadline; fix at your next touch of the file.

## ACTION (VIOLET)
convexity_read :51: round before comparing. Five study scripts carry the same structure (analog_timeline, skew_trajectory, sustain_run_query, two_anchor_ladder, diet_coiled_spring); they matter only if reused as live tools. Your board's 5.6% steepness label comes from FORGE `vix_futures.py`, which is unrounded; that item went to PROME as the FORGE owner.
**DONE WHEN:** the comparison reads a rounded value, and one exact-on-edge test case lands on the side the threshold's own letter says.
