# COMMON BLOCK — Thursday 2026-10-08 wakes (PROME `prome-fc`, laptop `WilliePOwen`, written 08:1x ET)

Every desk brief in this directory begins with the COMPLETION_SPEC preamble and then carries this block verbatim by reference. Read it once.

## Authority and facts
- Spawn class: Tier 1, WQ-184 due-row wake under **WQ-389** (Will 2026-10-07 23:20 ET, verbatim *"wake all eight tomorrow morning"*), condition re-established 2026-10-08 08:07 ET (Will in-session, verbatim *"We are on lap top. Everything should be closed and you can spawn"*). C6 class: every wake is on a due dated row.
- Preflight: ListAgents 08:10 ET = this PROME (`prome-fc`) + `walter-71` (Will's own WALTER window, busy); `session_bridge.py` 07:56 ET = two Claude processes on this host (PROME, WALTER), no Codex; desktop CLOSED on Will's word. You are the only writer of your desk directory.
- Eight desks run in parallel on this box: VULCAN · LABOR · BROCK · NEXUS · HENRY · OSPREY · LIQUID · DAEDALUS. Do not route signals around WALTER; do not grade another desk's row.
- $0 capital. No trade proposal, threshold move, score change or new direction unless the task's evidence forces one — then name the item that forced it. Trade construction = TERRY; position truth is off-repo (`FORGE/STATUS.md` is the stale mirror).

## Rules that bite
- **Prices live:** `python3 FORGE/tools/market-data/fetch.py price <TICKER>` / `fetch.py fred <SERIES>` (cache-busted CSV for FRED first-published cells), never STATUS or HEARTBEAT marks. Every figure keeps its date and basis. Pre-market reads are vendor reads, not closes.
- **Clock:** run `date` in the same command as any stamp you write; never type a clock from narrative.
- **L0 drain = the WHOLE inbox, every sender** — top-level packets AND the `inbox/WALTER/` lane — each logged per `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md`. Caveats travel verbatim.
- **Git (root CLAUDE.md Git Protocol):** touch only `AGENTS/<NAME>/`, packets you author into other agents' inboxes (carve-out ①), auto-memory files you author (carve-out ③). `cd "$(git rev-parse --show-toplevel)"` for every git command. Exact paths: `git add <files>` then `git commit <same paths> -F /tmp/msg.txt` (quoted heredoc `<<'EOF'`). Never `git add -A` / `git add .` / a directory add / `git reset` / `--amend` / `git stash`. Subject ≤100 chars.
- **Concurrency:** seven other desks commit and push now, so `bash scripts/safe-push.sh` may abort non-ff — routine. Recovery: `git fetch origin && git diff --name-only "$(git merge-base HEAD origin/master)..origin/master"` against `git status --porcelain`; with NO overlap run `git pull --rebase --autostash`, then re-push; up to three tries. Any overlap, or a rebase conflict ⇒ stop, keep your commit local, report the sha to PROME. Never force. The receipt is the literal line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).`
- A session that would WAIT hours for a scheduled print closes out and reports the armed state; PROME re-spawns at the print.
- Closeout per your own desk protocol: orphan check (`bash scripts/orphan_check.sh <NAME>`), consumer check if you superseded a figure others cite, claim check, memory-index check if you wrote an auto-memory, read-cap re-measure if your protocol asks.

## Deliver before idle (both mandatory)
1. A dated memo at `PROME/inbox/2026-10-08_from-<NAME>_<slug>.md` ending with the COMPLETION block from `PROME/COMPLETION_SPEC.md` (≤10 lines: STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP), citing each row key graded, committed by you (carve-out ①) with the explicit path and recipient-named subject.
2. `SendMessage` to `prome-fc` containing ONLY the COMPLETION block + your commit shas + the push receipt line. Not the full report.
Deliver as your final action before idling. Then stay available for PROME's WQ-249 closeout ask and answer it in one line (nothing unsaved · no uncommitted paths of yours · no further work pending), then idle for good.
