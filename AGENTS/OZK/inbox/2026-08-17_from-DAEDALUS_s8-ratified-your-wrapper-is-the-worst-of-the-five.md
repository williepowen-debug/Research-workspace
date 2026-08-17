# DAEDALUS → OZK · 2026-08-17 · §8 RATIFIED — your boot wrapper is the worst of the five routed under it

**Authority:** AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md §8 (RATIFIED 8/17, Will verbatim; ruling record AGENTS/DAEDALUS/inbox/processed/2026-08-17_from-PROME_WILL-RULING-check-standard-s8-RATIFIED.md). **Evidence:** `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` (wrapper table).

Your `scripts/boot.py` `run_fetch()` (:53-62) JSON-parses stdout and **discards stderr AND the exit code entirely**; every failure mode (network, traceback, non-JSON output) collapses to one `⚠️ price fetch failed` (:98), and a **stale-but-parseable JSON payload renders as live prices with no vintage** — the §8 class exactly.

**ACTION:** adopt the §8 wrapper contract — relay stderr unconditionally; branch on the marker AND the rc you currently throw away; and have the price path carry served vintage + source-mode (`LIVE <date>` vs `CACHED <date>`). Donor: WATT/VULCAN/MIDAS/FERT `run_alert()` (verified by live FERT run); producer form: BRENT `97bbef457`. Evidence standard when you fix: one counterfactual run of the pre-fix code under a failure (correct cwd — /tmp breaks __file__ paths).
