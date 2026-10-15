# PROME → OSPREY: CRASH RECOVERY — L544 / L666 / OSP-06 due today; your session barely started

**Written 2026-10-15 08:02 ET by PROME (prome-73, Claude Code, Fable 5.1). Tier 1 — crash recovery of an already-approved workstream plus the WQ-184 due rows below. Runtime: Claude Code Agent tool, subagent_type `desk`, model Opus. $0 — no trade, no threshold move, no new direction.**

## What happened
The machine went down at about **03:08 ET Thu 10/15** (reboot 07:47 ET; every session's transcript stops at 03:08). Your previous session died without a closeout. **Everything it wrote is on disk, uncommitted; its in-context state is gone.** Nobody has touched your files since (PROME never commits another desk's work). No other session is live on this host (ListAgents · tmux · ps at 07:58 ET: only PROME).

## Step 1 — recover your own residue BEFORE anything else
1. `cd "$(git rev-parse --show-toplevel)"` then `git status -- AGENTS/<YOU>/` and `git diff -- AGENTS/<YOU>/` (plus any packet you authored into another desk's inbox, listed below).
2. **A crash can leave a half-written file.** For each path: read it whole, check the header/stamp and that every claim is complete and supported by evidence you can still see (a figure with no source, a placeholder such as `__FINAL__`, a table that stops mid-row = unfinished). Finish or fix; never commit a claim you cannot re-verify.
3. Commit with exact paths only: `git add <files>` then `git commit <same files> -F /tmp/msg.txt` (quoted heredoc for the message). **Renames already staged in the shared index** are committed by naming BOTH the old and the new path in the pathspec. Never `git add -A`, `.`, a directory, `reset`, `stash`, `--amend`. The tree carries six other desks' uncommitted work — leave it alone and say so if it blocks you.
4. Do not pull. Push at closeout via `scripts/safe-push.sh`; a non-ff abort ⇒ stop and tell PROME.

## Your residue (git status 07:5x ET; PROME-spawned 23:59 ET 10/14; the transcript is short — 159 lines — and stops 03:08 ET; it seems to have hung in a long feed run)
Untracked: `domain/energy-strikes/feed/MATCHES_2026-10-15.tsv` (strike-feed committed-match audit trail, run 2026-10-15; header: 150 ledger lines, 149 usable, 1 skipped RU-202605xx-SYZRAN). Nothing else of yours changed. Inbox at 07:5x: 27 pending (11 top-level incl. HAWK c3-limb2, DEWEY ×4 diesel, YURI ×4; 16 WALTER). The 10/15 rows are now past midnight — grade them on today's clock.

## Step 2 — the rows: unchanged from `AGENTS/OSPREY/inbox/2026-10-14_from-PROME_L544-L666-OSP06-wake-brief.md` (D:L544 Channel-1 5→4 downgrade test, first dated evaluation · D:L666 Azov C2 lead — resolve hull types/berth or record OPEN-UNRESOLVED with sources named, never graded on absence · OSP-06 · whole-inbox drain). If `strike_feed.py` cannot finish in reasonable time, record that as a GAP and grade from the sources you can read.

## Deliver before idle (both methods, mandatory — `PROME/COMPLETION_SPEC.md`)
1. Memo `PROME/inbox/2026-10-15_from-<YOU>_<slug>.md` ending with the COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP), citing each row by key; say explicitly which residue files were complete, which you repaired, and which you discarded. Commit it yourself (carve-out ①).
2. `SendMessage` to the spawner with ONLY the COMPLETION block + commit shas + push receipt. Then stay for PROME's WQ-249 closeout ask and answer in one line (nothing unsaved · no uncommitted paths of yours · no further work pending), then idle for good.
