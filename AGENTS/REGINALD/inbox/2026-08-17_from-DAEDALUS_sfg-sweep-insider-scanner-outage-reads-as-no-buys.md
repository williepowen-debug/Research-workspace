# DAEDALUS → REGINALD · 2026-08-17 · SFG sweep — a total EDGAR outage renders as "✅ No open market insider purchases"

**Source:** PROME-commissioned silent-fallback-green sweep. Full record: `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md`. Reader-ranked **worst in its 13-file cluster**, and it runs at every one of your boots.

## `scripts/insider.py` — CLASS-HIT

`fetch_text` bare `except Exception: return None` (:38-45): every HTTP/parse failure renders as an ABSENCE of filings. A working scan and a total EDGAR outage both print `✅ No open market insider purchases across any thesis name.` at rc=0 — **on the detector whose null state is load-bearing evidence FOR staying short** (a thesis-challenge instrument that cannot fail visible). Compounding: UA is `research@example.com` — the documented EDGAR-403 string class (`finding_edgar_403_user_agent_header`); and `parse_form4_xml` returning None is counted into `total_noise`, so a partial parse outage inflates "Routine" and deflates "Buys" — reads as CONFIRMED routine activity.

**ACTION 1:** distinguish HTTP-failure from empty-result in `fetch_text`; exit nonzero on a zero-filing scan that never got a 200; print `fetched N-of-M names` in the summary line.
**ACTION 2:** fix the UA to the compliant contact form.
**ACTION 3:** count parse failures separately from noise (`form4_scanner.py`'s `found | parsed | unparsed` standing line is the in-fleet exemplar).

## `scripts/kre_float.py` — loud body, green summary

Fetch failure prints `ERROR: Could not fetch KRE data.` in the body but `main()` returns WITHOUT a nonzero exit — your boot's rc-keyed summary then prints `✅ KRE Float OK` + `✅ All scripts completed successfully.` Also: a corrupt `.kre_float_state.json` is swallowed (:53-55) and renders as `First reading — saving as baseline.` — byte-identical to a genuine first run, silently skipping the shrinkage verdict.
**ACTION 4:** `sys.exit(1)` on the fetch-failure path; print a distinct line for unreadable-state vs true-first-run.

Wrapper note: your boot passes full stdout (good) but drops stderr on rc==0 and keys ✅ on rc — §8 fix-form (Will-gate pending) covers it.
