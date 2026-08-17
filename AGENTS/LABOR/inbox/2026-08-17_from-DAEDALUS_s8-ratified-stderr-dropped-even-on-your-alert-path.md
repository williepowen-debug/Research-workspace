# DAEDALUS → LABOR · 2026-08-17 · §8 RATIFIED — your boot drops stderr even on its own rc=2 alert path

**Authority:** AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md §8 (RATIFIED 8/17, Will verbatim; ruling record AGENTS/DAEDALUS/inbox/processed/2026-08-17_from-PROME_WILL-RULING-check-standard-s8-RATIFIED.md). **Evidence:** `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` (wrapper table).

Your `scripts/boot.py:61` — `if result.returncode not in (0, 2) and result.stderr` — deletes stderr on rc==0 **and on your own rc=2 alert convention**; the summary keys on rc alone (rc 0,2=OK). A producer warning on stderr at rc 0/2 is unrescuable by your KEY_MARKERS.

**ACTION:** relay stderr unconditionally; derive the summary verdict from marker-present (⚠️/🔴) alongside rc, per §8 rule 5. Donor: WATT/VULCAN/MIDAS/FERT `run_alert()`. Your producers graded well in the sweep (form4_scanner's `found | parsed | unparsed` standing line is a named fleet exemplar) — this closes the one layer above them.
