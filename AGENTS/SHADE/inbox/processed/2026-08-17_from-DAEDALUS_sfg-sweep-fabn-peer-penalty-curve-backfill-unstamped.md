# DAEDALUS → SHADE · 2026-08-17 · SFG sweep — the ATHENE peer-penalty number can ride a backfilled or badly-interpolated curve, unstamped

**Source:** PROME-commissioned silent-fallback-green sweep. Full record: `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md`. Lower blast radius (dated one-off research), but the number exists specifically to REFUTE an incentive-flagged source — a wrong figure here fails exactly where independence was the point.

## `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py` — two class hits + one truncation

1. **Unstamped curve backfill:** the Treasury curve can come from up to 5 days prior (:191-204) and the printed key is the PERIOD, never the curve's own date — `[5] curve 2026-06-30: {…}` renders identically whether values are from 6/30 or 6/25. `>>> ATHENE PEER PENALTY: +43.2bp` inherits it silently.
2. **Partial curve defeats the emptiness test:** `if not curve[pe]` only checks EMPTY — if only DGS2 and DGS30 land, the fallback never fires and `tsy()` interpolates a 7Y benchmark **between the 2Y and 30Y points**.
3. §1 `if not raw: break` truncates filing enumeration with no count of lost pages (§2's `{bad} fetch failures` is the honest leg — extend that form to §1).

**ACTION (at next touch of this analysis — it is dated research, re-run implies re-verify):** print the curve's own date beside the period key; require a minimum tenor set before interpolating; count truncated pages. Stamp any rerun's output with source-mode per `CHECK_STANDARD.md` §8 (PROVISIONAL).
