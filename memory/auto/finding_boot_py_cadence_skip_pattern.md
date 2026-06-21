---
name: finding_boot_py_cadence_skip_pattern
description: "For monthly/low-frequency-data agents, the mature boot.py pattern is SAM/BRENT run-at-boot-defensively + mtime cadence-skip on fetchers — NOT a read-only/--pull opt-in split"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 1b2802f1-daef-492f-ba41-2fb9be496059
---

When building a `scripts/boot.py` for a **low-frequency-data agent** (MARCO, LABOR, CARL, REGINALD — monthly/quarterly government releases, not live ticks), copy the SAM/BRENT architecture, don't invent a gentler one.

**The mature pattern (SAM/BRENT):** run *every* fetcher at boot, every boot, by default — made safe by (1) per-script **timeout**, (2) **non-fatal** failure (captured as ❌ FAIL in a summary table, never halts the sweep), (3) **collapsed output** (only alert-marker lines unless `--verbose`), (4) priority ordering. There is NO read-only-vs-fetch mode split.

**The one adaptation for monthly data:** generalize the **cadence-skip** SAM uses for its single weekly item (`_has_today_row`) to ALL fetchers, keyed on the **output file's mtime** — skip the fetch if the output was refreshed within the cadence window (e.g. quarterly fetcher → skip if <85d, weekly → skip if <6d). This keeps boots fast in the common case and auto-fetches exactly when a new print is actually due. Running fetchers at boot also keeps them **exercised** — breakage shows as FAIL immediately instead of rotting (the disused-tool failure mode).

**Anti-pattern I started toward and rejected:** a binary `--pull` flag (read-only by default, opt-in fetch). It adds a decision point and diverges from the proven pattern; mtime-cadence-skip solves the only real concern (re-pulling unchanged monthly data) without it.

**Two build sub-lessons:**
- The **predictions-due free-text Timeframe parser** (resolving "Q2 2026" / "H2 2026" / "FY 2026" / "Mar-May 2026" / "Through Q2" → an end-date) must **fail LOUD** — print UNPARSEABLE rows rather than silently skip (a skipped prediction is the failure mode the scan exists to kill). Unit-test it: I caught a regex eating the first two digits of the year as a day-of-month (`Dec 2026 → Dec 20`) only because the test asserted exact dates.
- A MARCO-style agent's boot.py earns its keep on the **awareness layer** (catalyst countdown + predictions/expected-signals due-scan + STATUS/VX staleness), not data refresh — it would have auto-surfaced an overdue NFP print that was caught by hand.

**Refinement (LIQUID 2026-06-20, `scripts/boot.py`):** the mtime-cadence-skip adaptation presupposes the boot.py **writes output files** (MARCO/LABOR append TSVs with an mtime to key on). A **read-only** boot.py — pull → classify → print, no persisted output — has no output mtime to skip on, so cadence-skip is N/A; it relies on the **upstream fetch-layer TTL cache** (FORGE `fetch.py` caches FRED/yfinance, re-runs were ~0.4s) for re-pull cost and ships a fail-loud **`--selftest`** (validate the data files' schema + dates + the fetch import, exit 0/1) as the applicable hardening instead. Match the hardening to the boot.py's shape: append-style → mtime cadence-skip; read-only → upstream cache + `--selftest`. Parser sub-lesson extends too: require the WHOLE timeframe word be a month (`\b(word)\b ∈ months`), else a 3-letter-prefix regex silently false-matches `Junk`→Jun / `Maybe`→May into a wrong-but-parsed date (worse than UNPARSEABLE). And an adversarial code+wiring verify pass after the build earned its keep — caught a headline metric (CCC-BB pin) silently vanishing on a sub-fetch failure, and a self-imposed doc twin-rule (CALENDAR↔CATALYSTS) already violated; one reviewer "stale doc" finding was a false positive, so verify ground truth before acting on a review finding.

Validated MARCO 2026-06-08 (commit `e5f721ef`); LABOR built the same kit in parallel the same day (independent convergence → pattern is fleet-transferable); LIQUID 2026-06-20 built a read-only variant (commits `5ac00f34`→`b52a3333`). Related: [[finding_boot_closeout_hardening_recipe]], [[finding_boot_predictions_scan]], [[finding_subagent_pre_fire_date_verification]].
