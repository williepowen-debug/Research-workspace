# PROME → HOMER: CRASH RECOVERY (WQ-436) — your thesis clarifications, workbook refresh and PROME packet are on disk, uncommitted

**Written 2026-10-15 08:33 ET by PROME (prome-73, Claude Code). Authority: Will, 2026-10-15 08:31 ET, verbatim "okay approved both" on WQ-436 (record `PROME/proposals/2026-10-15_wq436-437-RULED.md`). Runtime: Claude Code Agent tool, subagent_type `desk`, model Opus. $0 — no trade, no threshold move, no new direction.**

## What happened
The machine went down at about **03:08 ET Thu 10/15** (reboot 07:47 ET; every session's transcript stops at 03:08). Your previous session (Will-launched homer-02, a Will-directed catch-up) died without a closeout. **Everything it wrote is on disk, uncommitted; its in-context state is gone.** Nobody has touched your files (PROME never commits another desk's work). No other session of yours is live (ListAgents · tmux · ps at 08:31 ET).

## Step 1 — recover your own residue
1. `cd "$(git rev-parse --show-toplevel)"` then `git status -- AGENTS/HOMER/` and `git diff -- AGENTS/HOMER/`.
2. **A crash can leave a half-written file.** Read each changed file whole; check headers/stamps and that every claim is complete and supported by evidence you can still see (a figure with no source, a placeholder, a table that stops mid-row = unfinished). Finish or fix; never commit a claim you cannot re-verify. Your own last log rows or pickup notes are claims to CHECK at the artifact, not a list of what exists — two desks this morning found their committed logs claimed write-backs that never reached disk.
3. Commit with exact paths only: `git add <files>` then `git commit <same files> -F /tmp/msg.txt` (quoted heredoc; subject ≤100 chars). Never `git add -A`, `.`, a directory, `reset`, `stash`, `--amend`. The tree carries other desks' uncommitted work — leave it alone and say so if it blocks you. Do not pull. Push at closeout via `scripts/safe-push.sh`; a non-ff abort ⇒ stop and tell PROME.

## Your residue (git status 07:5x ET — 10 paths + 1 packet)
Modified: `STATUS.md` · `registry/corrections_receipts.tsv` · `thesis/THESIS.md` (§7 between-grade clarifications, §8 convergence handle BUILT 10/15 — "no kill level moved") · `workbook/BUILDER.tsv` · `KB_LIVE.tsv` · `MULTIFAMILY.tsv` · `PIPELINE.tsv` · `PRICING.tsv` · `RATES.tsv` · `STATE_HSG.tsv`.
Packet YOU authored, untracked — verify, then commit (carve-out ①): `PROME/inbox/2026-10-15_from-HOMER_R3-verdicts-by-name-and-THESIS-KILL-gate-summary-qualifiers.md` (written 00:02 ET). PROME consumes it only after your commit: item 1 (the three WATCH_FOR re-wordings → WALTER's lane) and item 2 (the two GATES-summary qualifiers "pre-sale" and "serious" — a C1 wording clarification PROME verifies at your committed THESIS §7; review_by 11/20 unchanged).
Check specifically: THESIS §7/§8 are complete (no truncated table); every workbook TSV has its header vintage line updated to what you actually refreshed; `STATUS.md` names this recovery.

## Step 2 — scope
Nothing of yours is due today (GATE-HOMER-THESIS-KILL review_by 11/20; the 11/20 grade cannot return FALSIFIED/PARTIAL on the core legs per your own §7). Finish only what your dead session had in scope. **Inbox: 33 pending (14 top-level · 19 WALTER)** — drain what you can inside a short session, log per `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md`, and name the remainder with counts in GAPS; a full drain is not required by this spawn.

## Deliver before idle (both methods, mandatory — `PROME/COMPLETION_SPEC.md`)
1. Memo `PROME/inbox/2026-10-15_from-HOMER_<slug>.md` ending with the COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP); say which residue files were complete, which you repaired, which you discarded. Commit it yourself (carve-out ①).
2. `SendMessage` to the spawner with ONLY the COMPLETION block + commit shas + push receipt. Then stay for PROME's WQ-249 closeout ask and answer in one line (nothing unsaved · no uncommitted paths of yours · no further work pending), then idle for good.
