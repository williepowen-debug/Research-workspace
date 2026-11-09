# ORACLE — Scheduled Runs Registry

**Rule:** any change to the routine (script, cron line, slots) updates this file in the same pass. Pattern source: `AGENTS/BRENT/SCHEDULED_RUNS.md` (BRENT's are cloud routines; ORACLE's is local and free — WQ-527 covered local only, a cloud routine would be a separate spend ask).

## Live routine (1) — installed 2026-10-28 21:1x ET by ORACLE (WQ-527 C option A; Will 2026-10-28 20:59 ET verbatim "527 C approve, 528 A approve"; DOCKET L847)

| What | Where | Schedule | Box |
|---|---|---|---|
| Pulls-only daily read, sync-first since 2026-11-09 (Contract 2): `polymarket.py pull --log` → `kalshi.py pull --log` → `tools/disruption_supply_spread.py` → receipt row → path-scoped local commit | `tools/daily_pull.sh` | user crontab: `15 10,13,16,19,22 * * 1-5` (box TZ America/New_York) | **Both boxes.** Laptop `WilliePOwen` installed 10/28. Desktop `DESKTOP-BC6EF81`: receipts from 11/02 show it running (crontab itself not read from this box) |

**Cron line (exact):**
```
15 10,13,16,19,22 * * 1-5 /bin/bash /home/willi/Research-workspace/AGENTS/ORACLE/tools/daily_pull.sh >> /home/willi/.local/state/oracle_daily_pull.log 2>&1
```

## Contract

1. **Pulls, never grades.** No edit to STATUS, VX, KB, the `V5_*` ledgers or `watchlist.tsv`. A live ORACLE session grades the logged rows. Routine pulls are ORACLE's own live pulls, so they count as reads under letter O3/O5 (letter §9.5).
2. **One read per ET weekday, judged after syncing with GitHub (sync-first, 2026-11-09, 45a7701876; PROME brief `inbox/processed/2026-11-09_from-PROME_daily-pull-sync-first-fix.md`, Will "go" 10:41 ET).** Each slot exits silently if this checkout's ODDS_LOG already has a row on today's ET date, with no git activity. Otherwise, from the repo root: skip if a rebase or merge is already in progress; `git fetch origin` (skip if it fails); if behind `origin/master`, skip when any tracked file is modified or staged, else `git pull --rebase` (if it fails or stops: `git rebase --abort`, skip); then re-check ODDS_LOG and exit silently if the other box's read is now there. **A skipped slot writes no tracked file** (no `ROUTINE_RUNS.tsv` row): it prints one `SKIP et_date=… : <reason>` line to the cron log `~/.local/state/oracle_daily_pull.log` and exits 3; the next slot retries, and the ran-check reports a day left unread as NOT READ. A slot whose Polymarket pull appends 0 rows records `FAIL` ("NO READ") and the next slot retries.
3. **Receipt:** one row per attempt in `workbook/ROUTINE_RUNS.tsv` (run_ts_utc, et_date, host, status OK/PARTIAL/FAIL, rc and row counts per step, spread or error note).
4. **Commits** only `ODDS_LOG.tsv`, `KALSHI_ODDS_LOG.tsv`, `DISRUPTION_SUPPLY_SPREAD.tsv`, `ROUTINE_RUNS.tsv`, path-scoped, locally; **never pushes** (the next closeout's safe-push carries it).
5. **Ran-check:** `python3 tools/routine_check.py` at every boot (CLAUDE.md step 2b) — lists every weekday since install as READ / NOT READ / PENDING; rc=1 on any NOT READ.

## Known limits

- **Runs only while WSL is up.** WSL stops its VM when no terminal or session is open, and cron does not catch up. Five slots (10:15–22:15 ET) cover any day Will opens the box; a day the box stays shut is a `NOT READ` in the ran-check. Not fixed: a Windows Task Scheduler trigger would wake WSL, but that is a Windows-side change for Will to decide.
- **Per box.** A machine switch leaves the other box's cron idle only if that box is off. The receipt's `host` column shows which box read.
- **Two boxes up on one day collide: fixed by sync-first, 2026-11-09, 45a7701876** (Contract 2), for the case where the other box's read has reached GitHub. History: each box judged "already read today" from its own checkout. On 11/02 the desktop read at 10:15 ET and the laptop, 299 commits behind, read again at 19:15 ET; its local commit later stopped the shared rebase on 11/04 (resolved in d8e2dae040). On 11/09 the desktop, 203 commits behind after the laptop weekend, committed 2ff376f4cd onto the 11/06 base, conflicting with the laptop's 11/07 and 11/08 rows; PROME merged on Will's word and the 11/09 rows were re-applied as 166f9c649e. The first pull of the ET date stays the read (O3); a later row is context.
- **Still open after sync-first:** (a) the routine never pushes, so a read sitting unpushed on one box is invisible to the other; both can still read the same day, and the later row is context under O3. (b) A box that is behind while any other desk has a modified tracked file skips every slot; on a busy day that leaves the date NOT READ for a live session to take. (c) When it pulls, `--rebase` rewrites the hashes of other sessions' unpushed commits; at most once a day, because a box holding today's read does not sync. This is expected, not rare: BRENT's cloud routines push to origin during the day, so the box Will is using can be behind while live desks hold unpushed local commits on a clean tree. The day's first slot with no read then rebases under those live sessions. Desks citing those hashes verify by subject (root Git Protocol), the same effect as any desk's boot pull. (PROME review, 2026-11-09.) (d) A conflicting pull is aborted with content and HEAD restored, but the conflicting files' mtimes change.
- Holiday pulls happen (weekday rule); letter O3 treats them as context.

## Tests run at install (2026-10-28, scratch git copy, not the live repo)

- Live repo, read already taken → silent exit, nothing written.
- Scratch: double-log guard active → `FAIL` row "NO READ: polymarket logged 0 rows" (caught a v1 bug that recorded this as `OK`).
- Scratch, guard window zeroed → `OK`, PM 58 rows, Kalshi 11, spread +36.0pp, committed path-scoped.
- Third run same day → silent skip, no new row.
- `routine_check.py` with install date set to 10/20 → flags 10/20, 10/22, 10/23, 10/26, 10/27 NOT READ (the known gap), reads 10/21's 22:22 ET pull as 10/21, rc=1.

## Tests run for sync-first (2026-11-09, scratch git copy, not the live repo)

Rerunnable: `bash tools/test_daily_pull_sync.sh` (bare "origin" plus two clones in a temp dir, stub pullers with no market calls; rc 0 = all pass; it holds the lock briefly, so do not run it across a :15 slot). Result 2026-11-09 on `DESKTOP-BC6EF81`: **26 of 26 checks pass in 9 cases** (PROME reran it at 10:49:59 ET: 26/0, rc 0; PROME accepted the diff, a rerun of this suite, not independent verification). Run against the pre-fix script, 12 checks fail, so the tests can tell the two apart.

1. Up to date, no read today → reads and commits the same four files, same subject, as the old script; a second slot exits silently.
2. Behind and clean, origin holds the other box's read → pulls, exits silently, no second commit. Behind and clean, no read on origin → pulls, reads, commit sits directly on `origin/master` (push dry-run fast-forwards).
3. Behind and dirty (modified, then staged) → exit 3 with the reason; HEAD, status, diffs and tracked-file mtimes identical.
4. Unpushed local commit conflicts with origin → rebase aborted, exit 3; HEAD, status and diffs identical, no rebase in progress, no receipt row. The conflicting file's mtime changes (Known limits d).
5. Unreachable remote URL → exit 3 "git fetch origin failed"; state and mtimes identical.
6. Lock held → silent exit 0, nothing done; the next slot reads.
7. Another session's rebase already stopped in the checkout → exit 3, the rebase is left in place.
8. Behind with only an untracked file → pulls and reads; untracked file kept.
9. Checkout already holds today's read and origin is newer → silent exit with no fetch (HEAD and `origin/master` ref unchanged).

Live repo, 2026-11-09 before commit 45a7701876, cron-like bare environment (`env -i`): read already taken → exit 0, HEAD, `origin/master` and status unchanged. A cron-environment `git fetch` succeeds on this box (credential helper `store`).
