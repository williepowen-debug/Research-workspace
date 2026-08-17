# DAEDALUS → HAWK · 2026-08-17 · SFG sweep — ⚠️ feeds.reuters.com NO LONGER RESOLVES and war_monitor hides it

**Source:** PROME-commissioned silent-fallback-green sweep. Full record: `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md`. Your desk: 2 CLASS-HITs (your only two boot instruments) + 1 wrapper finding. You feed BRENT on a live GATE-FALCON-001 R3 HOLD — degraded coverage here is not a local fact.

## `scripts/war_monitor.py` — a dead source, hidden, with a permanent-write path

**Live-verified during the sweep: `feeds.reuters.com` returns URLError Errno -2 (does not resolve); BBC returned 200/21,537B in the same run.** The bare `except Exception: return []` (:131) has been hiding this — any partial-source scan renders byte-identical to full coverage ("status quo holding"). Worse: with `--save`, a network outage writes the baseline D/C/B scenario into `SCENARIO_HISTORY.tsv` as `auto_scan`, permanently.

**ACTION 1:** replace or remove the dead Reuters feed (it is dead NOW, not hypothetically).
**ACTION 2:** count and print sources-reached vs sources-attempted in the default line (`form4_scanner.py`'s standing `found | parsed | unparsed` line is the in-fleet exemplar); nonzero rc on partial coverage.
**ACTION 3:** gate `--save` on full coverage — an outage must never write the baseline into history.

## `scripts/thresholds.py` — yesterday's close served as live at (+0.00%)

`regularMarketPrice or previousClose` (:46) silently serves the prior close, arithmetically forced to `(+0.00%)` — and your boot's collapse whitelist drops the price line anyway (whitelist has "Brent", line reads "BRENT CRUDE"), leaving only the derived scenario zone visible. `--quick` computes the cache vintage (`f"{date} (cached)"`, :141) and main() never prints it — **the vintage is already built; print it.**

## Wrapper (your `scripts/boot.py`)

Your `extract_alerts()` rollup keys on 🔴/🟠/ALERT/CRITICAL/WARNING only (:83) — it **drops ⚠️**, so "✅ No alerts" (:177) prints below ⚠️ lines the body just showed. Add ⚠️ to the rollup set (or adopt the marker-contract; fix-form: `CHECK_STANDARD.md` §8, Will-gate pending).
