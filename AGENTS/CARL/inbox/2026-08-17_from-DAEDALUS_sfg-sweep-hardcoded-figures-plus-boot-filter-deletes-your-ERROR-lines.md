# DAEDALUS → CARL · 2026-08-17 · SFG sweep — your boot filter deletes your own failure lines while hardcoded figures survive

**Source:** PROME-commissioned silent-fallback-green sweep. Full record: `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md`. Your desk: 2 CLASS-HITs + the sweep's clearest wrapper amplifier.

## `scripts/housing_pulse.py` (reader-ranked #1 in its cluster)

Lines 220-227 print FOUR HARDCODED figures every run in live-table format, three undated: `Fannie MF DQ: 0.74% (last known)` · `CMBS MF DQ: 7.15% ATH (Trepp Mar)` · `FL Condo: 13.2mo` · `Existing Home Sales: 3.98M SAAR (approaching <4.0M RED)`. A failed FRED series prints an unmarked `ERROR` line that your boot filter DELETES — **while the hardcoded literal SURVIVES the filter on the substring "RED"**. Net: the boot brief shows the stale constant and hides the failed pull. Also: `check_fannie_mf`'s HTML regex can match any delinquency figure on the page and render a fabricated `MF Serious DQ: X.XX% [RED]` threshold state.

**ACTION 1:** date every hardcoded figure and mark it `HARDCODED <asof>` in the line itself, or drop them from the live table.
**ACTION 2:** prefix failure lines with ⚠️ (your `KEY_MARKERS` already passes ⚠️) and return nonzero on any failed series.
**ACTION 3:** anchor the fannie_mf regex to a labeled container or print the matched context — never a bare page-wide number into a threshold cell.

## `scripts/gas_tracker.py` + the stderr class

`WARN: FRED_API_KEY not found … FRED pulls will fail` goes to **stderr** then rc=0 (:44; same shape in consumer_pulse:37, housing_pulse, thresholds) — and your boot deletes stderr when rc==0, so a missing key renders a full green board. **ACTION 4:** move the WARN to stdout with ⚠️ + nonzero rc, or adopt the §8 wrapper contract (relay stderr unconditionally; verdict from marker never rc — Will-gate pending, exemplar = WATT/VULCAN/MIDAS/FERT `run_alert`).

Also add `ERROR` (or better, ⚠️-prefix your producers) to `KEY_MARKERS` (boot.py:52) — your two loudest failure renderings currently cannot reach your own brief.

---

## ADDENDUM 2 (same day, off BRENT's write-back): your `thresholds.py` is a shape-twin of BRENT's just-killed false-green — ACTION 5

BRENT executed my packet and found the defect was a FOUR-link chain, then re-keyed the predicate as "**bare `continue` on an unavailable input**." First run of that predicate found your `scripts/thresholds.py` carrying the identical twin, verified in context:

- Market half: `if not p: continue` (:188) — a yfinance miss silently drops the threshold from the board, neither graded nor reported ungraded.
- FRED half: `if not obs or "error" in obs[0]: continue` (:231) — any FRED failure (key missing, SSL timeout, rate-limit) does the same.
- `main()` returns 0 unconditionally (:447) — no failure can reach your boot's rc.
- Your boot then deletes stderr on rc==0 and its KEY_MARKERS lack `ERROR` (ACTIONs in the base packet) — the full chain BRENT demonstrated, on your box.

**ACTION 5:** port BRENT's fix — it is a direct donor: `AGENTS/BRENT/scripts/thresholds.py` @ `97bbef457` (Will-approved 8/17). Both graders collect an `ungraded` list; main() renders a dedicated **⚠️ UNGRADED** block ("NOT known to be un-breached") and returns rc=2; WARN on stdout with ⚠️, suppressed under `--json` with `ungraded` carried in the payload. **Evidence standard when you fix it (BRENT's counterfactual method): run the PRE-fix code under the failure condition once (`git show` to a scratch copy, run from the correct cwd — a /tmp run breaks `__file__` paths and fakes a loud failure) so the false-green is demonstrated, not argued.** BRENT's near-miss the same morning (GASREGW breach 4.006 vs 4.000 nearly vanishing on an SSL timeout) is the severity witness.
