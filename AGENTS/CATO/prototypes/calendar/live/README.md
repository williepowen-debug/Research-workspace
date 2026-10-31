# Live read-only research calendar

Will approved the bounded live reader and chose “Keep this layout for the live read-only version” on October 31, 2026. Open Agent Launcher → Calendar → Open Calendar, or from the Git root:

```sh
python3 -B AGENTS/CATO/prototypes/calendar/live/app.py --open-browser
python3 -B AGENTS/CATO/prototypes/calendar/live/app.py --check
```

Keep the service window open; Ctrl+C stops it. Reopen the launcher to load its new tab. The browser waits for Windows/WSL localhost forwarding before opening. No model calls, source writes, reminders or agent starts occur. The server binds only loopback, validates Host/Origin, exposes only GET routes and serves source text only from the calendar's allowlist. Source checking can use `--pause` to keep its window visible.

The accepted Week/Day/details layout now reads local files on demand. Previous/next week, Today, owner filters and literal search narrow the view. Housekeeping is off; Unclassified is on. Long cards are visually shortened; details retain full titles, source excerpts, file hashes, current-source links and caveats. Uncertain dates, windows, undated and earlier records remain separate. Past records are not automatically marked completed. Counts are source records, not unique economic events or launch recommendations.

## Sources and limits

- HENRY's NEXT 30 DAYS table: explicit verification window binds inferred years. Out-of-window or unsupported dates remain uncertain; prose beyond the table and recurring rules are not expanded. Exact times stay exact; multiple/non-clock times are not invented. Source refresh deadline produces a stale warning.
- PROME's `spawn_list.open` version 1 export: open obligations with full owner/state/notes; captured source hash and rows must match. Raw date cells preserve windows; an export's range end is not silently turned into an event date. Export errors are unavailable, never an empty success. No operational boot or spawn command runs.
- GATES: LIVE and FIRED-UNEXECUTED records at the leading review_by date. A review date is not a gate-fire forecast; terminal states are excluded. Unknown states/malformed rows are reported.
- Catalyst registry: parse the literal SUMMONS_LEDGERS mapping without executing prome_gate. At delivery this includes LABOR, VULCAN, VIOLET, CYPHER, GIBBS and ISHM, supporting their two existing schemas and explicit date classes. Other desk calendars are outside coverage.
- The preview's one TERRY card supplies dated context only, never current holdings. Reviewed preview joins/classifications are reused only while every cited excerpt remains present and represented primary rows remain current. Changed context is visibly withheld. Unknown docket categories remain visible; no keyword classifier silently hides work. Similar records outside reviewed joins remain separate.

Source coverage lists loaded/unavailable files, parser limitations and counts. File hashes/excerpts describe the captured read. Reads are sequential, not a global repository transaction; each covered source is reread for change detection. Missing sources remove their affected records and disclose incomplete coverage. A failed HTTP refresh retains the last view with a failure warning. Views older than 15 minutes prompt refresh. Reading a file does not refresh its evidence; the calendar does not fetch GitHub or verify live external dates. HENRY's stated refresh deadline is assessed; other sources retain their own caveats without an invented freshness certification.

This version does not implement Month view, launch preparation/preflight, personal-calendar integration, reminders or scheduling. Live source contents can still be wrong. Independent acceptance and ordinary-use benefit remain unmeasured; evidence below is author work.

## Checks

```sh
cd AGENTS/CATO/prototypes/calendar/live
python3 -B -m unittest test_reader -q
# From Git root, with native Windows Chrome and loopback access:
python3 -B AGENTS/CATO/prototypes/calendar/live/test_browser.py
```

`fixtures.json` preserves real October 31 source rows for both catalyst schemas, economic window and gate reading. Tests cover windows, invalid dates, uncertain timing, stale evidence, missing/malformed inputs, nonexecuting registry parsing, source-hash mismatch, moved dates, terminal gate annotations, changed reviewed context and path escape. Browser checks use captured live input and simulated changes/failures: desktop and narrow layout, filters, source escaping, moved event, retained failed-refresh view, unavailable/stale warnings and read-only HTTP boundaries. `browser-checks.json` and screenshots are author evidence, not a live data feed. Native launcher checks also verify opening Calendar leaves the dispatch queue/history unchanged.
