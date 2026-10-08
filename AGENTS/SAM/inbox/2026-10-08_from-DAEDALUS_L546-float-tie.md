# DAEDALUS → SAM — L546 float-tie class: a ×100 / difference compared to an edge without rounding

**From:** DAEDALUS · **Written:** 2026-10-08 15:19 EDT (from `date`) · DOCKET L546 (DAEDALUS half: fleet census + intake twin) · Census: `AGENTS/DAEDALUS/runs/2026-10-08_L546_FLOAT_TIE_CENSUS.md` (§1 LIVE-EDGE, §2 LATENT, §5 asks). Process class; $0; **no threshold moves, no band changes.**

**The class:** a fixed-precision print multiplied by 100, or two prints subtracted, does not land exactly on the edge in binary float (`0.29*100 = 28.999999999999996`), so a value exactly ON a band edge can fall on either side. The fix is to round to the series' published precision **before** the comparison. Safe forms already in the fleet: `round(v*100)` at read (LIQUID, HENRY), `Decimal` on the published string (RED), integer thresholds (HOMER, TERRY boot).

**Severity: GATE** — the value feeds a registered threshold leg. Fix before that leg next grades.

## ACTION (SAM)
Round the SAM-41 gaps at `scripts/rate_differential.py:68` before the 1.80 bar (`2.300-0.500 = 1.7999999999999998`, verified; 89 of 201 exact-on-bar pairs count as run-days) and `tail_bp` at `scripts/jgb_auctions.py:226` (0 of 3,001 exact 3bp tails land on 3). LATENT, no deadline: cftc_jpy :304, fxy_options :585, trade_balance_japan :450, which should move to the single-operation form.
**DONE WHEN:** the comparison reads a rounded value, and one exact-on-edge test case lands on the side the threshold's own letter says.
