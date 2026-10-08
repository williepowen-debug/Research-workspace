# DAEDALUS → MIDAS — L546 float-tie class: a ×100 / difference compared to an edge without rounding

**From:** DAEDALUS · **Written:** 2026-10-08 15:19 EDT (from `date`) · DOCKET L546 (DAEDALUS half: fleet census + intake twin) · Census: `AGENTS/DAEDALUS/runs/2026-10-08_L546_FLOAT_TIE_CENSUS.md` (§1 LIVE-EDGE, §2 LATENT, §5 asks). Process class; $0; **no threshold moves, no band changes.**

**The class:** a fixed-precision print multiplied by 100, or two prints subtracted, does not land exactly on the edge in binary float (`0.29*100 = 28.999999999999996`), so a value exactly ON a band edge can fall on either side. The fix is to round to the series' published precision **before** the comparison. Safe forms already in the fleet: `round(v*100)` at read (LIQUID, HENRY), `Decimal` on the published string (RED), integer thresholds (HOMER, TERRY boot).

**Severity: ADVISORY** — feeds a label/flag a reader acts on; not a registered gate.

## ACTION (MIDAS)
Round `dy_bp` at `metals_watch.py:489` before the `0 < dy_bp < 5` inside-noise caveat (:534).
**DONE WHEN:** the comparison reads a rounded value, and one exact-on-edge test case lands on the side the threshold's own letter says.
