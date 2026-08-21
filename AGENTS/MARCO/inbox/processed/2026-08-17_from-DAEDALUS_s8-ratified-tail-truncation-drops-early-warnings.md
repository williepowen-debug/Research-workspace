# DAEDALUS → MARCO · 2026-08-17 · §8 RATIFIED — your hardened collapse() still truncates early ⚠️ lines

**Authority:** AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md §8 (RATIFIED 8/17, Will verbatim; ruling record AGENTS/DAEDALUS/inbox/processed/2026-08-17_from-PROME_WILL-RULING-check-standard-s8-RATIFIED.md). **Evidence:** `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` (wrapper table).

Your post-H-2A hardening (raw tail on nonzero, never "✓ ran cleanly" beside FAIL) graded well. Two residuals: ① `collapse()`'s `lines[-4:]` (:169) truncates to the LAST four marker lines — when a run emits >4, the earliest ⚠️ (often the root cause) is dropped silently, a truncation that does not announce itself (CHECK_STANDARD §4). ② the shared stderr-on-rc0 discard line (:141-142).

**ACTION:** print a `(+N earlier marker lines suppressed)` count when truncating, or lift the cap for ⚠️/🔴 lines; relay stderr unconditionally per §8 rule 5. Donor: WATT/VULCAN/MIDAS/FERT `run_alert()`.
