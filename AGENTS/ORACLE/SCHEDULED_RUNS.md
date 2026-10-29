# ORACLE — Scheduled Runs Registry

**Rule:** any change to the routine (script, cron line, slots) updates this file in the same pass. Pattern source: `AGENTS/BRENT/SCHEDULED_RUNS.md` (BRENT's are cloud routines; ORACLE's is local and free — WQ-527 covered local only, a cloud routine would be a separate spend ask).

## Live routine (1) — installed 2026-10-28 21:1x ET by ORACLE (WQ-527 C option A; Will 2026-10-28 20:59 ET verbatim "527 C approve, 528 A approve"; DOCKET L847)

| What | Where | Schedule | Box |
|---|---|---|---|
| Pulls-only daily read: `polymarket.py pull --log` → `kalshi.py pull --log` → `tools/disruption_supply_spread.py` → receipt row → path-scoped local commit | `tools/daily_pull.sh` | user crontab: `15 10,13,16,19,22 * * 1-5` (box TZ America/New_York) | **LAPTOP `WilliePOwen` only.** Desktop: install the same crontab line at the next switch (not done) |

**Cron line (exact):**
```
15 10,13,16,19,22 * * 1-5 /bin/bash /home/willi/Research-workspace/AGENTS/ORACLE/tools/daily_pull.sh >> /home/willi/.local/state/oracle_daily_pull.log 2>&1
```

## Contract

1. **Pulls, never grades.** No edit to STATUS, VX, KB, the `V5_*` ledgers or `watchlist.tsv`. A live ORACLE session grades the logged rows. Routine pulls are ORACLE's own live pulls, so they count as reads under letter O3/O5 (letter §9.5).
2. **One read per ET weekday.** Each slot exits silently if ODDS_LOG already has a row on today's ET date (session or earlier slot). A slot whose Polymarket pull appends 0 rows records `FAIL` ("NO READ") and the next slot retries.
3. **Receipt:** one row per attempt in `workbook/ROUTINE_RUNS.tsv` (run_ts_utc, et_date, host, status OK/PARTIAL/FAIL, rc and row counts per step, spread or error note).
4. **Commits** only `ODDS_LOG.tsv`, `KALSHI_ODDS_LOG.tsv`, `DISRUPTION_SUPPLY_SPREAD.tsv`, `ROUTINE_RUNS.tsv`, path-scoped, locally; **never pushes** (the next closeout's safe-push carries it).
5. **Ran-check:** `python3 tools/routine_check.py` at every boot (CLAUDE.md step 2b) — lists every weekday since install as READ / NOT READ / PENDING; rc=1 on any NOT READ.

## Known limits

- **Runs only while WSL is up.** WSL stops its VM when no terminal or session is open, and cron does not catch up. Five slots (10:15–22:15 ET) cover any day Will opens the box; a day the box stays shut is a `NOT READ` in the ran-check. Not fixed: a Windows Task Scheduler trigger would wake WSL, but that is a Windows-side change for Will to decide.
- **Per box.** A machine switch leaves the other box's cron (if any) idle; the receipt's `host` column shows which box read.
- Holiday pulls happen (weekday rule); letter O3 treats them as context.

## Tests run at install (2026-10-28, scratch git copy, not the live repo)

- Live repo, read already taken → silent exit, nothing written.
- Scratch: double-log guard active → `FAIL` row "NO READ: polymarket logged 0 rows" (caught a v1 bug that recorded this as `OK`).
- Scratch, guard window zeroed → `OK`, PM 58 rows, Kalshi 11, spread +36.0pp, committed path-scoped.
- Third run same day → silent skip, no new row.
- `routine_check.py` with install date set to 10/20 → flags 10/20, 10/22, 10/23, 10/26, 10/27 NOT READ (the known gap), reads 10/21's 22:22 ET pull as 10/21, rc=1.
