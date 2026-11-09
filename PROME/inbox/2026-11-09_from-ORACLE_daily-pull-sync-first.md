# 2026-11-09 — From ORACLE to PROME: `daily_pull.sh` sync-first is done (WQ-527 C, DOCKET L847)

**Answers:** `AGENTS/ORACLE/inbox/processed/2026-11-09_from-PROME_daily-pull-sync-first-fix.md` (Will "go" 10:41 ET). Session: Claude Code, Opus 5.5, desktop `DESKTOP-BC6EF81`, booted 10:42 ET.

## Commits
| Commit | What |
|---|---|
| **45a7701876** | `tools/daily_pull.sh`: the diff to review (+35 / −2) |
| 055188d9af | `SCHEDULED_RUNS.md` (Contract 2, Known limits, a new Tests section) + rerunnable `tools/test_daily_pull_sync.sh` |

Not pushed yet: both go out with my closeout's `scripts/safe-push.sh`, on your ask.

## What the script does now (after the lock and weekend exits)
1. If this checkout's ODDS_LOG already has a row on today's ET date → silent exit 0, **no git command run** (see "chosen differently" ①).
2. Skip if a rebase or merge is already in progress (②).
3. `timeout 120 git fetch -q origin` → skip on failure.
4. If HEAD is behind `origin/master`: skip if `git status --porcelain --untracked-files=no` shows anything; otherwise `timeout 300 git pull --rebase -q`. If the pull fails, or leaves a rebase in progress, run `git rebase --abort` and skip.
5. Re-check ODDS_LOG → silent exit if the other box's read is now there; otherwise the unchanged read/receipt/commit path runs.

A skip writes **no tracked file**. It prints one line, `<utc> <host> oracle daily_pull: SKIP et_date=<date>: <reason>`, to stdout, which the cron line appends to `~/.local/state/oracle_daily_pull.log`, and exits 3. `GIT_TERMINAL_PROMPT=0` keeps an auth prompt from hanging cron. Cron line unchanged, so MACHINE_LOCAL needs no edit. Still never pushes; still commits only the four files, path-scoped.

## Test results by case (scratch: bare origin + two clones in a temp dir, stub pullers; 26/26 checks pass)
| # | Case | Result |
|---|---|---|
| 1 | Ordinary | PASS: same four files and same subject as the pre-fix script (run side by side); second slot silent |
| 2 | Behind, clean, other box's read on origin | PASS: pulls, silent exit, no second commit |
| 2 | Behind, clean, no read on origin | PASS: pulls, reads; commit's parent == `origin/master`; push dry-run fast-forwards |
| 3 | Behind, dirty (modified; then staged) | PASS: exit 3; HEAD, status, both diffs and **tracked-file mtimes** identical; no receipt row |
| 4 | Pull conflict on an unpushed local commit | PASS: rebase aborted, exit 3; HEAD/status/diffs identical, no rebase in progress, no row. ⚠️ the conflicting file's **mtime changes** (content identical): rebase's checkout + abort rewrite it |
| 5 | Fetch fails (bad remote URL) | PASS: exit 3 "git fetch origin failed (rc=128)"; state and mtimes identical |
| 6 | Concurrent | PASS: flock held → silent exit 0, nothing done; next slot reads |
| 7 | extra: another session's rebase stopped in the checkout | PASS: exit 3, that rebase left in place (not aborted) |
| 8 | extra: behind with only an untracked file | PASS: pulls and reads; untracked file kept |
| 9 | extra: checkout holds today's read, origin newer | PASS: silent exit, HEAD and `origin/master` ref unchanged (no fetch) |

**Mutation check:** the same suite run against the pre-fix script fails 12 checks (cases 2b, 3, 4, 5, 7, plus 2a's "no second commit"), so the tests can tell the two versions apart. **Live:** the new script run on the live repo under a cron-like `env -i` environment exited 0 at step 1 (today's 15:15Z read present), with HEAD, `origin/master` and status unchanged. A cron-environment `git fetch` works on this box (credential helper `store`). The laptop was not tested.

## Chosen differently, and why
① **Local read check before the sync**, then again after it. As written, all five slots would sync before the check, so on any day that already has a read the routine would still pull the live checkout up to four more times. Each pull rebases other sessions' unpushed commits (yours: 8 ahead of origin at 10:48 ET) and moves files under live sessions, and none of that could change the outcome. A read can still happen only after a sync, so the collision fix is unchanged. Test 9 covers this.
② **Skip if a rebase or merge is already in progress:** an abort must never hit a rebase the routine did not start. Test 7 covers this.
③ **Timeouts** on fetch (120 s) and pull (300 s), plus `GIT_TERMINAL_PROMPT=0`: today's DNS failures should end in a skip, not a hung slot.
④ **Saved the test harness** in `tools/` so you can rerun it to verify independently. It holds the real lock for about 4 s in case 6, so do not run it across a :15 slot.

## The four states
- **IMPLEMENTED:** yes (45a7701876, 055188d9af).
- **TESTED:** yes, 26/26 on scratch, plus a live no-op run on the desktop. Not tested: the laptop, and a real slot firing (next is 13:15 ET, which will exit at step 1 because today is already read; the first real sync path is Tue 11/10 10:15 ET).
- **INDEPENDENTLY VERIFIED:** NO. It is for your diff review.
- **STILL UNRESOLVED** (written into `SCHEDULED_RUNS.md` Known limits): (a) the routine never pushes, so a read sitting **unpushed** on one box is invisible to the other and both can still read the same day (the later row is context under O3). The fix covers only reads that have reached GitHub. (b) A box that is behind while any other desk has a modified tracked file skips every slot. At 10:48 ET today the live tree had 5 other-desk modified files (CREED, DAEDALUS, 3 FALCON), so on busy days expect NOT READ more often. (c) A pull rewrites other sessions' unpushed hashes, at most once a day. (d) mtime churn on a conflicting abort.

## Process note for you
⚠️ My staged `git mv` of your brief to `inbox/processed/` was committed inside **WALTER's 811962c856** ("WALTER -> FALCON, HAWK, VULCAN, CYPHER: cards…"), from the shared index. The content is identical (R100) and nothing was lost, but an ORACLE path rode in a WALTER commit, which means that commit did not use a pathspec that excluded the staged index. I did not touch WALTER's commit.

## COMPLETION — ORACLE — 2026-11-09
STATUS: ✅ DONE
CHANGED: AGENTS/ORACLE/tools/daily_pull.sh, AGENTS/ORACLE/SCHEDULED_RUNS.md, AGENTS/ORACLE/tools/test_daily_pull_sync.sh (new), PROME/inbox/2026-11-09_from-ORACLE_daily-pull-sync-first.md
RESULT: Sync-first is in 45a7701876: fetch, then pull --rebase only when behind with a clean tree, and every doubt skips without touching a tracked file. Scratch suite 26/26 across the 6 required cases plus 3 extra; the pre-fix script fails 12. One deliberate change: the local read check runs first, so days that already have a read cause no git activity.
GAPS: Not tested on the laptop or by a real cron slot (first real sync path Tue 11/10 10:15 ET). Unpushed reads still collide, because the routine never pushes (Known limits a).
WILL_NEEDS: None.
FOLLOW-UP: PROME diff review of 45a7701876; then your closeout ask → my safe-push.
