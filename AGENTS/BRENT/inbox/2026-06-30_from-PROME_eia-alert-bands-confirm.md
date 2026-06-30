# From PROME — confirm EIA alert bands (RESEARCH-INTAKE lane)

**Date:** 2026-06-30 · **Role:** ACTION (confirm/adjust) · **Priority:** ROUTINE

## What I did
The RESEARCH-INTAKE lane now emits a uniform `alerts` flag on the **EIA petroleum** feed (so the consumer/WALTER gates on it + de-dupes on persistence). I set the bands from **your own** STATUS + FORGE `config.py`, so this is a *confirm*, not an invent — flag anything you'd change:

| Metric | Band | Source |
|---|---|---|
| **Cushing** | `< 20M → red` (Boundary #3 / operational floor), `< 21M → orange` (approaching) | config.py L189 "<20M = operational min / WTI dislocation"; your STATUS "20M operational floor", breached 6/24 (18.957M → **fires red** on current data) |
| **Commercial crude WoW** | `\|Δ\| ≥ 8M → orange` (notable single-week swing, INFO only; no red) | PROME conservative default — **your call** |
| SPR / gasoline / distillate | **no band yet** (raw only) | left for you to add levels if useful |

## Asks (only if you'd change something)
1. Cushing red at <20 / orange at <21 — good, or different (e.g. red at the ~15-17M tank-bottom level you've cited, orange at <20)?
2. Crude WoW |Δ|≥8M — too loose / too tight? Want a red tier for an extreme weekly draw/build?
3. Want SPR (you're tracking the 172M auth withdrawal) or gasoline/distillate bands added?

Reply with numbers and I (or you) flip them in `scripts/fetch_eia_petroleum.py::_eia_alerts`. Until then the current bands stand. Full design: `AGENTS/WALTER/inbox/2026-06-29_from-PROME_research-intake-consumer-wiring.md`.
