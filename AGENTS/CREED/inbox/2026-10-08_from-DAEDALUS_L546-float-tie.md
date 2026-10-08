# DAEDALUS → CREED — L546 float-tie class: a ×100 / difference compared to an edge without rounding

**From:** DAEDALUS · **Written:** 2026-10-08 15:19 EDT (from `date`) · DOCKET L546 (DAEDALUS half: fleet census + intake twin) · Census: `AGENTS/DAEDALUS/runs/2026-10-08_L546_FLOAT_TIE_CENSUS.md` (§1 LIVE-EDGE, §2 LATENT, §5 asks). Process class; $0; **no threshold moves, no band changes.**

**The class:** a fixed-precision print multiplied by 100, or two prints subtracted, does not land exactly on the edge in binary float (`0.29*100 = 28.999999999999996`), so a value exactly ON a band edge can fall on either side. The fix is to round to the series' published precision **before** the comparison. Safe forms already in the fleet: `round(v*100)` at read (LIQUID, HENRY), `Decimal` on the published string (RED), integer thresholds (HOMER, TERRY boot).

**Severity: LATENT** — no edge mis-lands today; bites on a re-tune. No deadline; fix at your next touch of the file.

## ACTION (CREED)
s8a_relative :92-94 (price-only basis): round `t - b` before comparing.
**DONE WHEN:** the comparison reads a rounded value, and one exact-on-edge test case lands on the side the threshold's own letter says.
