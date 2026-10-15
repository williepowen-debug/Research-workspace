# PROME → LABOR: CRASH RECOVERY + L625 claims grade (08:30 ET today) + L626 residue

**Written 2026-10-15 08:02 ET by PROME (prome-73, Claude Code, Fable 5.1). Tier 1 — crash recovery of an already-approved workstream plus the WQ-184 due rows below. Runtime: Claude Code Agent tool, subagent_type `desk`, model Opus. $0 — no trade, no threshold move, no new direction.**

## What happened
The machine went down at about **03:08 ET Thu 10/15** (reboot 07:47 ET; every session's transcript stops at 03:08). Your previous session died without a closeout. **Everything it wrote is on disk, uncommitted; its in-context state is gone.** Nobody has touched your files since (PROME never commits another desk's work). No other session is live on this host (ListAgents · tmux · ps at 07:58 ET: only PROME).

## Step 1 — recover your own residue BEFORE anything else
1. `cd "$(git rev-parse --show-toplevel)"` then `git status -- AGENTS/<YOU>/` and `git diff -- AGENTS/<YOU>/` (plus any packet you authored into another desk's inbox, listed below).
2. **A crash can leave a half-written file.** For each path: read it whole, check the header/stamp and that every claim is complete and supported by evidence you can still see (a figure with no source, a placeholder such as `__FINAL__`, a table that stops mid-row = unfinished). Finish or fix; never commit a claim you cannot re-verify.
3. Commit with exact paths only: `git add <files>` then `git commit <same files> -F /tmp/msg.txt` (quoted heredoc for the message). **Renames already staged in the shared index** are committed by naming BOTH the old and the new path in the pathspec. Never `git add -A`, `.`, a directory, `reset`, `stash`, `--amend`. The tree carries six other desks' uncommitted work — leave it alone and say so if it blocks you.
4. Do not pull. Push at closeout via `scripts/safe-push.sh`; a non-ff abort ⇒ stop and tell PROME.

## Your residue (git status at 07:5x ET — 21 paths; your session labor-89 was Will's own window, doorbelled by PROME 23:47 ET 10/14)
Modified: `BUILD_DEBT.md` · `STATUS.md` (pickup items 1 ✅ NFP card moved, 2 re-parked, 2a deferred-needs-Will, 9 ✅ JOLTS openings NO BAND decided, AHE real-wage line) · `board_log.tsv` · `domain/sources/2026-10-02_NFP_SEP_GRADE_SYNTHESIS.md` · `registry/corrections_receipts.tsv` · `workbook/KB.tsv` · `workbook/PUBLISHED.tsv`.
Staged renames (in the shared index): `docket/GRADING_CARD_20261002_NFP.md → docket/graded/…` · 10 `inbox/WALTER/SIG-W-*.md → inbox/WALTER/processed/` (-20261008-025, -033, -20261010-005, -20261012-018, -033, -044, -20261014-001, -007, -008, -023) · 3 `inbox/2026-10-08_from-DAEDALUS_*`, `2026-10-14_from-DAEDALUS_brief-pin-wiring.md → inbox/processed/`.
Packets YOU authored, untracked — commit them (carve-out ①): `AGENTS/RED/inbox/2026-10-14_from-LABOR_nfp-card-moved-to-graded.md` · `AGENTS/TERRY/inbox/2026-10-14_from-LABOR_nfp-card-moved-to-graded.md` · `AGENTS/REGINALD/inbox/2026-10-14_from-LABOR_jolts-openings-band-decision.md`.
Still pending in your inbox: `inbox/2026-10-14_to-LABOR_sdl01-flip-and-pop-control-ask.md` (MARCO's SDL-01 question — answer only if you hold the figure).

## Step 2 — the registered rows (DOCKET quotes verbatim)
1. **D:L625 (TODAY, 08:30 ET):** *"LABOR WAKE — initial claims w/e Oct 10 + continuing claims w/e Oct 3, 08:30 ET (card FROZEN 10/8: AGENTS/LABOR/docket/GRADING_CARD_20261015_claims.md); grade at the DOL primary on the as-published vintage; the 10/8 print was 197K band B, MA 198,000 (mechanical), CC 1,716,000; v13 at 1 and v7 at 2 after their 4-of-4 completions (score 26/75); ⚠️ no registered rule moves either vector back UP short of a 230K+ print or the 250K MA trigger."* You are launched minutes before the print: recover first (Step 1), then grade at the DOL primary once published (your reader guard L-33/L-24: bare curl → DOL PDF). Waiting the few minutes to 08:30 is fine; do not wait beyond ~09:15 for a late release — report ARMED and PROME re-wakes. Freeze the next card (10/22) in this session per your C2a recurring-print trigger.
2. **D:L626 (10/13, self-directed C2 step):** your STATUS diff shows most of it done (items 1, 9) — finish what is open, record what stays parked with a fold-by, and name item 2a's Will-gated `CLAUDE.md` edits in WILL_NEEDS (PROME routes them).
3. Context: CPI 10/14 (headline +0.6% m/m / 3.7% y/y, core +0.3% / 2.6%) is in SIG-W-20261014-023 (already in your processed/). PPI prints 08:30 today too — note only if it bears on your rows.

## Deliver before idle (both methods, mandatory — `PROME/COMPLETION_SPEC.md`)
1. Memo `PROME/inbox/2026-10-15_from-<YOU>_<slug>.md` ending with the COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP), citing each row by key; say explicitly which residue files were complete, which you repaired, and which you discarded. Commit it yourself (carve-out ①).
2. `SendMessage` to the spawner with ONLY the COMPLETION block + commit shas + push receipt. Then stay for PROME's WQ-249 closeout ask and answer in one line (nothing unsaved · no uncommitted paths of yours · no further work pending), then idle for good.
