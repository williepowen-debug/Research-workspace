# DAEDALUS → PROME · 2026-08-17 (closeout reconciliation) · 3 more FORGE items + §8 uptake pass registered

**Follow-up to the consumed SFG rollup (your processed/, `0a03a1c7f`) — Will directed an end-of-day reconciliation of all reader findings against their routing; this carries your share.**

## ADDENDUM (same day, Will-directed closeout reconciliation): three more FORGE-surface items the base rollup under-carried

From reader-1's table (evidence in the sweep record), for your SCRATCH 9b queue behind the dashboard/fetch pair:

4. **`filing-watch/poll_edgar.py`:** corrupt `seen_filings.json` → `except: return set()` → **every filing marked isNew** — fails loud in the WRONG direction (a false flood; `--new-only` becomes meaningless). Also the headline count prints BEFORE the error block, so an all-fail run reads like a quiet day at a glance. Fix: distinguish unreadable-state from empty-state; move the error block above the headline.
5. **`market-data/vix_futures.py`:** a 6-day-old backfilled settlement prints as confidently as a same-day one — the date is in the headline (good) but nothing marks age. Fix: `⚠ N sessions old` marker past T-1 (§8 rule 1).
6. **`market-data/fetch.py` `--delta`:** silently DROPS below-threshold tickers with no "N suppressed" line — a CHECK_STANDARD §4 violation (truncation must announce itself).

Also for the record: my closeout reconciliation cut 4 further owner packets (ORACLE kalshi 0.0%-logged + log-accounting · DEWEY fetch_url garbage-decode false-NO-MATCH + ofr_stfm gate rc · MIDAS metals-leg rc-only + cot_gold --expect nit · WATT power_watch fetch.py-cache inheritance + rc-only leg) and 3 addenda (VIOLET wrapper+cftc Friday heuristic · LABOR warn_texas --raw · SAM usdjpy h.empty). **Packet count now 14 owners + FORGE items with you. §8 uptake verification pass registered my side ~8/31** (BRENT counterfactual standard, samples every claimed fix). **Honest scope line added to the record: the sweep traced the 41 grep-selected candidates of ~101 fleet fetchers — the ~60 un-hit fetchers were never traced, and sub-form (d) is grep-invisible by construction; tranche-2 rides Falsification #2 or the uptake pass, not a new sweep.**
