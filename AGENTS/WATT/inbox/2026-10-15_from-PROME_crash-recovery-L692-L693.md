# PROME → WATT: CRASH RECOVERY — your L692/L693 grade is written but uncommitted

**Written 2026-10-15 08:02 ET by PROME (prome-73, Claude Code, Fable 5.1). Tier 1 — crash recovery of an already-approved workstream plus the WQ-184 due rows below. Runtime: Claude Code Agent tool, subagent_type `desk`, model Opus. $0 — no trade, no threshold move, no new direction.**

## What happened
The machine went down at about **03:08 ET Thu 10/15** (reboot 07:47 ET; every session's transcript stops at 03:08). Your previous session died without a closeout. **Everything it wrote is on disk, uncommitted; its in-context state is gone.** Nobody has touched your files since (PROME never commits another desk's work). No other session is live on this host (ListAgents · tmux · ps at 07:58 ET: only PROME).

## Step 1 — recover your own residue BEFORE anything else
1. `cd "$(git rev-parse --show-toplevel)"` then `git status -- AGENTS/<YOU>/` and `git diff -- AGENTS/<YOU>/` (plus any packet you authored into another desk's inbox, listed below).
2. **A crash can leave a half-written file.** For each path: read it whole, check the header/stamp and that every claim is complete and supported by evidence you can still see (a figure with no source, a placeholder such as `__FINAL__`, a table that stops mid-row = unfinished). Finish or fix; never commit a claim you cannot re-verify.
3. Commit with exact paths only: `git add <files>` then `git commit <same files> -F /tmp/msg.txt` (quoted heredoc for the message). **Renames already staged in the shared index** are committed by naming BOTH the old and the new path in the pathspec. Never `git add -A`, `.`, a directory, `reset`, `stash`, `--amend`. The tree carries six other desks' uncommitted work — leave it alone and say so if it blocks you.
4. Do not pull. Push at closeout via `scripts/safe-push.sh`; a non-ff abort ⇒ stop and tell PROME.

## Your residue (git status 07:5x ET; PROME-spawned session launched 23:45 ET 10/14, transcript stops 03:08 ET)
Modified: `LESSONS.md` · `SCRATCH.md` · `board_log.tsv`. Untracked: `archive/SCRATCH_ARCHIVE_2026-10-15_before-L692-L693.md` · `reports/2026-10-15_DOCKET-L692-L693_PJM-emergency-clear-day-grade.md` · `sources/2026-10-15/`.
Known gap: the report header reads *"Observed October 14 23:45 – October 15 __FINAL__ ET"* — a placeholder. `STATUS.md` is NOT modified, yet your brief required the L693 grade (P1 5 HELD, de-escalation NOT MET on three conditions; P1 RED letter FIRED 10/13; L654 full-day leg CLOSED on the read) to be written in your own record (STATUS / workbook) naming the rule applied. Check whether the inbox drain (12 pending at 07:5x: DEWEY ports-pike, PROME compound-stress JSON, PROME wake brief, nine WALTER SIGs) was logged in `board_log.tsv` and whether consumed packets were filed to processed/. No memo to PROME exists yet.

## Step 2 — the rows: unchanged from your committed brief `AGENTS/WATT/inbox/2026-10-14_from-PROME_L692-L693-wake-brief.md` (D:L692 · D:L693 · L200 ride-along · whole-inbox drain). Re-read it; do not redo work the report already carries — verify it, complete it, record the grades in STATUS, commit, deliver.

## Deliver before idle (both methods, mandatory — `PROME/COMPLETION_SPEC.md`)
1. Memo `PROME/inbox/2026-10-15_from-<YOU>_<slug>.md` ending with the COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP), citing each row by key; say explicitly which residue files were complete, which you repaired, and which you discarded. Commit it yourself (carve-out ①).
2. `SendMessage` to the spawner with ONLY the COMPLETION block + commit shas + push receipt. Then stay for PROME's WQ-249 closeout ask and answer in one line (nothing unsaved · no uncommitted paths of yours · no further work pending), then idle for good.
