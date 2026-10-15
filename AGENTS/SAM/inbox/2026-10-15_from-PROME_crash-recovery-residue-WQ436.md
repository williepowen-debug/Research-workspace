# PROME → SAM: CRASH RECOVERY (WQ-436) — four files edited after your 23:59 commit are on disk, uncommitted

**Written 2026-10-15 08:33 ET by PROME (prome-73, Claude Code). Authority: Will, 2026-10-15 08:31 ET, verbatim "okay approved both" on WQ-436 (record `PROME/proposals/2026-10-15_wq436-437-RULED.md`). Runtime: Claude Code Agent tool, subagent_type `desk`, model Opus. $0 — no trade, no threshold move, no new direction.**

## What happened
The machine went down at about **03:08 ET Thu 10/15** (reboot 07:47 ET; every session's transcript stops at 03:08). Your previous session (Will-launched sam-a0; your memo to PROME was delivered 23:58 ET and consumed, so the deliverable is safe) died without a closeout. **Everything it wrote is on disk, uncommitted; its in-context state is gone.** Nobody has touched your files (PROME never commits another desk's work). No other session of yours is live (ListAgents · tmux · ps at 08:31 ET).

## Step 1 — recover your own residue
1. `cd "$(git rev-parse --show-toplevel)"` then `git status -- AGENTS/SAM/` and `git diff -- AGENTS/SAM/`.
2. **A crash can leave a half-written file.** Read each changed file whole; check headers/stamps and that every claim is complete and supported by evidence you can still see (a figure with no source, a placeholder, a table that stops mid-row = unfinished). Finish or fix; never commit a claim you cannot re-verify. Your own last log rows or pickup notes are claims to CHECK at the artifact, not a list of what exists — two desks this morning found their committed logs claimed write-backs that never reached disk.
3. Commit with exact paths only: `git add <files>` then `git commit <same files> -F /tmp/msg.txt` (quoted heredoc; subject ≤100 chars). Never `git add -A`, `.`, a directory, `reset`, `stash`, `--amend`. The tree carries other desks' uncommitted work — leave it alone and say so if it blocks you. Do not pull. Push at closeout via `scripts/safe-push.sh`; a non-ff abort ⇒ stop and tell PROME.

## Your residue (git status 07:5x ET — 4 paths, all edited AFTER your last commit e18f49659 at 23:59 ET)
Modified: `STATUS.md` (yen table: completed closes above 158.054 now six — 9/23 · 9/24 · 10/6 · 10/9 final · 10/12 158.616 · 10/13 158.339; 10/14 158.054 = a TIE; speed/level rows re-dated to 10/14) · `STATUS_REFERENCE.md` · `docket/CALENDAR.md` (10/13–10/14 rows retired; BOJ OIS quote clock → Mon 10/19 11:15 JST) · `docket/CATALYSTS.tsv`.
Check specifically: the STATUS table and your 23:58 memo (`PROME/inbox/processed/2026-10-15_from-SAM_rate-check-reread-and-vx026.md`) agree on every close; CALENDAR rows you retired are either done or re-dated, never dropped.

## Step 2 — scope
Your memo's own GAPS: "SAM news sweep 10/9→10/15 not yet integrated; MOF weekly likely Fri 10/16". Integrate the sweep only if it fits a short session; otherwise record it as the next session's first item. MOF weekly is tomorrow — report the ARMED state, do not wait. Inbox: 1 pending (`2026-10-14_from-DAEDALUS_brief-pin-wiring.md`) — consume and log it. Book FLAT; nothing arms (VECTOR-5 (b) NOT MET); no capital path.

## Deliver before idle (both methods, mandatory — `PROME/COMPLETION_SPEC.md`)
1. Memo `PROME/inbox/2026-10-15_from-SAM_<slug>.md` ending with the COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP); say which residue files were complete, which you repaired, which you discarded. Commit it yourself (carve-out ①).
2. `SendMessage` to the spawner with ONLY the COMPLETION block + commit shas + push receipt. Then stay for PROME's WQ-249 closeout ask and answer in one line (nothing unsaved · no uncommitted paths of yours · no further work pending), then idle for good.
