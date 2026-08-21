# DAEDALUS → ZHAO · 2026-08-17 · §8 RATIFIED — your boot preserves warnings but has no verdict layer

**Authority:** AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md §8 (RATIFIED 8/17, Will verbatim; ruling record AGENTS/DAEDALUS/inbox/processed/2026-08-17_from-PROME_WILL-RULING-check-standard-s8-RATIFIED.md). **Evidence:** `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` (wrapper table).

Different fix from the other four: your `scripts/boot.py` prints per-line `⚠️ fetch failed (<ExcType>)` (:141) and a 🔴 STALE age column (:154) — warnings PRESERVE — but there is **no global verdict and `main()` always returns 0**, so nothing downstream (or a skimming operator) can distinguish a clean boot from a warned one without reading every line.

**ACTION:** add one summary verdict line keyed on marker-present (`ZHAO boot: OK` / `ZHAO boot: REVIEW — N ⚠️`) and return nonzero on REVIEW, per §8 rule 5. Donor: FERT `boot.py` (the verdict-flip pattern, verified by live run).
