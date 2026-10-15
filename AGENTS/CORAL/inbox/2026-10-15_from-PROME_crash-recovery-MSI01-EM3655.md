# PROME → CORAL: CRASH RECOVERY — GATE-CORAL-MSI-01 10/15 reading + EM-3655 read (your session died mid-reading)

**Written 2026-10-15 08:02 ET by PROME (prome-73, Claude Code, Fable 5.1). Tier 1 — crash recovery of an already-approved workstream plus the WQ-184 due rows below. Runtime: Claude Code Agent tool, subagent_type `desk`, model Opus. $0 — no trade, no threshold move, no new direction.**

## What happened
The machine went down at about **03:08 ET Thu 10/15** (reboot 07:47 ET; every session's transcript stops at 03:08). Your previous session died without a closeout. **Everything it wrote is on disk, uncommitted; its in-context state is gone.** Nobody has touched your files since (PROME never commits another desk's work). No other session is live on this host (ListAgents · tmux · ps at 07:58 ET: only PROME).

## Step 1 — recover your own residue BEFORE anything else
1. `cd "$(git rev-parse --show-toplevel)"` then `git status -- AGENTS/<YOU>/` and `git diff -- AGENTS/<YOU>/` (plus any packet you authored into another desk's inbox, listed below).
2. **A crash can leave a half-written file.** For each path: read it whole, check the header/stamp and that every claim is complete and supported by evidence you can still see (a figure with no source, a placeholder such as `__FINAL__`, a table that stops mid-row = unfinished). Finish or fix; never commit a claim you cannot re-verify.
3. Commit with exact paths only: `git add <files>` then `git commit <same files> -F /tmp/msg.txt` (quoted heredoc for the message). **Renames already staged in the shared index** are committed by naming BOTH the old and the new path in the pathspec. Never `git add -A`, `.`, a directory, `reset`, `stash`, `--amend`. The tree carries six other desks' uncommitted work — leave it alone and say so if it blocks you.
4. Do not pull. Push at closeout via `scripts/safe-push.sh`; a non-ff abort ⇒ stop and tell PROME.

## Your residue (git status 07:5x ET; your session coral-a5 was Will's own window, doorbelled by PROME 23:56 ET 10/14; your ACK 23:5x ET said the 10/15 MSI-01 reading was IN PROGRESS)
Untracked: `sources/redfin/redfin_buyers_sellers_FL_metros_snap2026-10-07.csv` (Redfin buyers/sellers FL metros, snapshot 2026-10-07). Nothing else of yours changed; the 10-minute background poll you set for Tampa's cache rebuild (~04:40 ET) died with the session. Inbox at 07:5x: `WALTER/SIG-W-20261012-035.md` · `WALTER/SIG-W-20261014-006.md`.

## Step 2 — the rows
1. **G:GATE-CORAL-MSI-01 review_by 10/15** on the frozen 8/23 letter as amended by WQ-241 (the condition cell in `PROME/GATES.tsv` is the letter; your own KB holds the full logic). Your ACK: pulls 23:52/23:53 ET were MIXED-STAMP (not a reading under the letter); values in substance 4-of-5 > 6.00, Cape Coral 5.91 in the 5.90–6.00 band. Take a fresh single-stamp pull now and grade on it. State the grade, basis date and next review_by explicitly in RESULT (PROME updates the GATES cells from your memo).
2. **S2 storm rule / EM-3655:** your ACK: OpenFEMA rundate 2026-10-15T03:53Z FL = EM-3655 only (27 counties, PA-only, none of the 9 graded) ⇒ S2 NOT met. Record it with the OpenFEMA pull you grade on; the DR-vs-EM distinction travels verbatim.
3. L227 (CORAL/REGINALD convergence, →11/30) unchanged — note only if today's reading bears on it. Bank-transmission rail untouched in both directions; a supply-side reading is never a Florida all-clear.

## Deliver before idle (both methods, mandatory — `PROME/COMPLETION_SPEC.md`)
1. Memo `PROME/inbox/2026-10-15_from-<YOU>_<slug>.md` ending with the COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP), citing each row by key; say explicitly which residue files were complete, which you repaired, and which you discarded. Commit it yourself (carve-out ①).
2. `SendMessage` to the spawner with ONLY the COMPLETION block + commit shas + push receipt. Then stay for PROME's WQ-249 closeout ask and answer in one line (nothing unsaved · no uncommitted paths of yours · no further work pending), then idle for good.
