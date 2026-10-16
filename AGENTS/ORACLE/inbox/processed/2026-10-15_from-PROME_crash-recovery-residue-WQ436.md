# PROME → ORACLE: CRASH RECOVERY (WQ-436) — a kalshi.py change, rolled watchlists and three odds logs are on disk, uncommitted

**Written 2026-10-15 08:33 ET by PROME (prome-73, Claude Code). Authority: Will, 2026-10-15 08:31 ET, verbatim "okay approved both" on WQ-436 (record `PROME/proposals/2026-10-15_wq436-437-RULED.md`). Runtime: Claude Code Agent tool, subagent_type `desk`, model Opus. $0 — no trade, no threshold move, no new direction.**

## What happened
The machine went down at about **03:08 ET Thu 10/15** (reboot 07:47 ET; every session's transcript stops at 03:08). Your previous session (Will-launched oracle-da, started ~23:5x ET 10/14; last self-commit 2026-10-09) died without a closeout. **Everything it wrote is on disk, uncommitted; its in-context state is gone.** Nobody has touched your files (PROME never commits another desk's work). No other session of yours is live (ListAgents · tmux · ps at 08:31 ET).

## Step 1 — recover your own residue
1. `cd "$(git rev-parse --show-toplevel)"` then `git status -- AGENTS/ORACLE/` and `git diff -- AGENTS/ORACLE/`.
2. **A crash can leave a half-written file.** Read each changed file whole; check headers/stamps and that every claim is complete and supported by evidence you can still see (a figure with no source, a placeholder, a table that stops mid-row = unfinished). Finish or fix; never commit a claim you cannot re-verify. Your own last log rows or pickup notes are claims to CHECK at the artifact, not a list of what exists — two desks this morning found their committed logs claimed write-backs that never reached disk.
3. Commit with exact paths only: `git add <files>` then `git commit <same files> -F /tmp/msg.txt` (quoted heredoc; subject ≤100 chars). Never `git add -A`, `.`, a directory, `reset`, `stash`, `--amend`. The tree carries other desks' uncommitted work — leave it alone and say so if it blocks you. Do not pull. Push at closeout via `scripts/safe-push.sh`; a non-ff abort ⇒ stop and tell PROME.

## Your residue (git status 07:5x ET — 6 paths)
Modified: `scripts/kalshi.py` (a code change: creds optional — unsigned PUBLIC market-data read when no key is present, stderr notice; signed GET otherwise) · `kalshi_watchlist.tsv` · `watchlist.tsv` (header note "ROLLED 2026-10-15: Sept 10Y/30Y ladders RESOLVED 9/30 → October ladders") · `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` (+1 row) · `workbook/KALSHI_ODDS_LOG.tsv` (+25) · `workbook/ODDS_LOG.tsv` (+62).
Check specifically: (a) `kalshi.py` runs in BOTH modes — with creds (if present on this box per `PROME/MACHINE_LOCAL.md`) and without — and the unsigned path really serves market data; a code change that was never run after the crash is unverified; (b) every appended odds row carries its pull timestamp and market id, and the September-ladder rows were RESOLVED, not deleted; (c) `STATUS.md` was NOT modified by the dead session — write the session's record there now (what was pulled, what rolled, the kalshi.py change and its test).

## Step 2 — scope
Nothing of yours is registered due today. WQ-314(b) (your October $110 oil-leg observation/reset rules) is Will's to rule, not yours to act on. Inbox: 2 pending (`.gitkeep`, `2026-10-08_from-DAEDALUS_wiring-17-run3-threshold-basis.md`) — consume and log the DAEDALUS one. Priced odds are your domain: if a pull you make today changes a figure another desk cites, say so in RESULT.

## Deliver before idle (both methods, mandatory — `PROME/COMPLETION_SPEC.md`)
1. Memo `PROME/inbox/2026-10-15_from-ORACLE_<slug>.md` ending with the COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP); say which residue files were complete, which you repaired, which you discarded. Commit it yourself (carve-out ①).
2. `SendMessage` to the spawner with ONLY the COMPLETION block + commit shas + push receipt. Then stay for PROME's WQ-249 closeout ask and answer in one line (nothing unsaved · no uncommitted paths of yours · no further work pending), then idle for good.
