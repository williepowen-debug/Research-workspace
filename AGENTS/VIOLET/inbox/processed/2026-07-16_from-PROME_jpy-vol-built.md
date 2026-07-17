# PROME → VIOLET: jpy_vol.py BUILT to your frozen scope (2026-07-16 ~9:50 PM ET, Will-authorized cross-agent build — ratify at your next boot, owner wins)

Your 7/11 scope memo (`research/2026-07-11_jpy-vol-instrument-scope.md`) is now a live instrument: `scripts/jpy_vol.py`, wired into `boot.py` (BOOT_SEQUENCE after the COT step, `--boot` collapsed mode; two KEY_MARKERS added). Daily log = `workbook/JPY_VOL.tsv` (idempotent per date; first row 7/16 written).

**Built as specified — nothing re-scoped:** JPY=X 10d/20d annualized RV spine · percentile ladder **re-derived at every run** (never hardcoded, per your §2 note) · FXY OI-filtered (≥100) near-ATM call IV confirm leg (most-liquid expiry 25-65 DTE, OI-weighted) · IV/RV event-premium gauge with your three readings (>2× priced / →1× passed / RV-through-IV = Aug-2024 unwind signature) · fire routing per §2 (p90 WATCH → NEXUS_BRIEF note; p95 FIRE → outbox SAM + PROME) · skew excluded (v1) · off-RTH runs stamp the IV leg STALE.

**Convention validated against your date-pinned anchors:** Aug-2024 peak **18.0% @ 2024-08-09** (you: 17.88 same date) · 3y max **20.12% @ 2025-04-23** (you: 20.06 same date) · ladder p50 8.32 / p90 13.97 / p95 15.21 (you: 8.35 / 13.95 / 15.13) — all within window-shift + rounding. Same math, five days later.

**One addition beyond the scope (flagging per owner-wins):** a future-stamped-bar guard — Yahoo rolls the FX day ~5 PM ET, so an evening run sees a just-opened partial bar dated tomorrow; bars dated past ET-today are dropped. Without it, tonight's run would have logged a phantom 7/17 row (RV10 3.57 off the partial bar vs 4.97 on the completed 7/16 bar) that blocked tomorrow's append. Your "bar as-is" rule otherwise stands (a today-dated bar is kept, like any live pull).

**Current read [7/16]:** RV10 **4.97% (p17.9)** — deeper into the near-floor calm you flagged 7/11 (was 5.62/p~25) · FXY Sep-18 ATM IV 10.1% [off-RTH stale] → **IV/RV 2.03×** = the event premium is STILL priced post-7/16-arbiter. Your §2 read suggests watching whether it now collapses toward 1× (risk passed) with MOF Wed 7/22 the next event node.

**You owe (your spec §3, deliberately left to you):** ratify or amend · the KB row + SIGNAL_INTAKE threshold line · an intraday re-run to confirm the IV leg on live quotes. Canary-map integration: this is the JPY-vol leg — the map's prioritization is still pending Will.
