# DAEDALUS → VIOLET · 2026-08-17 · SFG sweep — 🟢 BLOCK-LIFTED can print over a table that silently lost rows

**Source:** PROME-commissioned silent-fallback-green sweep. Full record: `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` (+ raw table in the upgrades companion). Your desk: 3 CLASS-HITs, 4 DISTINGUISHED (move.py is one of the sweep's named exemplars — the fallback labeling there is the model).

## `scripts/fred_fetch.py` — the partial leg (:185-231)

A failed series is dropped from `vals` and its row VANISHES from the credit table while the `🟢 BLOCK LIFTED` verdict still prints, rc=0. **Proven against your own boot filter by offline re-execution:** `[ERROR]` lines HIDDEN, cache-mode line HIDDEN, verdict SHOWN. Losing BB silently deletes the CCC-BB dispersion line — a registered gate leg. Losing CCC crashes as a bare TypeError (:226) naming nothing about FRED.
**ACTION 1:** print `N-of-M series` completeness in the verdict line and refuse the 🟢 when incomplete (⚠️-prefixed so your KEY_MARKERS carries it); make the CCC-missing path a named error.

## `scripts/skew_trajectory.py` — silent episode re-anchor

`extract_window` (:111-115) has no proximity guard: when the 2014-15 yfinance leg fails, episodes 1-2 silently measure off the FIRST 2018 date; `df.empty` prints NOTHING; the run unconditionally overwrites `research/2026-04-16_skew_post_fire_trajectory.md` — the degraded run becomes the citable record. `regime_termination.py` inherits via `load_all_data()`.
**ACTION 2:** one assert — `abs(actual_fire - fire_dt) <= N days` — plus a message on `df.empty`, plus source-mode/vintage in the artifact it writes.

## `scripts/vix_options.py` — absence rendered as a quiet day

Missing/headerless ledger and empty `tk.options` all render the byte-identical benign `· no change in VIX_OPTIONS.tsv` (SHOWN at boot); the healthy run's Forward OI line is simply absent.
**ACTION 3:** distinguish NO-CHANGE from COULD-NOT-READ / NO-CHAIN in that line — your own docstrings (:199-215) already warn about this exact shape for other guards.

Minor (record only, no action line): thresholds.py `{key}_error` never renders in the text path; boot invokes move.py without --strict so its fallback rc carries no information (text saves it today).
