# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

A multi-agent financial research operation tracking systemic risk transmission. Goal: detect stress early enough to position ahead of consensus. The operator is Will (Eastern timezone).

## How The System Works

Two platforms share this git repo:

- **OpenClaw (VPS):** Prome (chief of staff / coordinator) runs here, assigns decision work, manages state/decision rails, and communicates with Will via Telegram. WALTER owns signal/news routing. You don't run here.
- **Claude Code (local):** CARL, REGINALD, SAM, and RED run here as independent sessions. You are NOT spawned by Prome. You communicate with Prome and each other via inbox/outbox files.

Coordination is file-based. Write to `AGENTS/<NAME>/outbox/` to request Prome action. Read `AGENTS/<NAME>/inbox/` for incoming signals. Prome checks these and routes accordingly.

**Operating model:** Prome is chief of staff, not the universal analyst. Prome owns prioritization, decision rails, state files, operational tasking, and Will-facing synthesis. **WALTER owns signal/news routing**: ingest, filter, dedupe, archive, and route incoming market intelligence. Domain agents own domain evidence and judgment. If Prome sends a task packet, treat it as the current coordination layer unless it conflicts with Will or higher-priority instructions.

**Transmission chain:** LABOR → CARL → REGINALD → market repricing. HENRY (velocity), LIQUID (amplification), SAM (Japan, parallel trigger), HAWK → BRENT (oil/energy).

**Active agents:** PROME, CARL\*, REGINALD\*, OZK\*, CORAL\*, SAM\*, RED\*, LABOR, BROCK, LIQUID, HENRY, HAWK, BRENT, NEXUS. Tier 2 (spawned as needed): ZHAO, HANS, MARCO, BARON, SHADE, HERMES, DARWIN, OTTO, ORACLE. (\* = Claude Code)

*OZK spun out from REGINALD on 2026-04-24 (promoted from REGINALD/OZK/ to AGENTS/OZK/ as a peer agent). WAL is the next candidate for promotion when ready.*
*CORAL (Florida) spun out from REGINALD on 2026-06-19 (promoted from REGINALD/sub-agents/CORAL/ to AGENTS/CORAL/ as a peer agent). CORAL is the comprehensive whole-Florida agent (real estate, insurance, FL banks, migration, tourism, state fiscal/property-tax, labor, coastal/climate — 10 pillars; see AGENTS/CORAL/COVERAGE.md). Overlap with MARCO on FL migration/tourism is intentional — reconcile shared metrics to one number, don't silo. Florida is a top-priority geography for Will.*

Agent state lives at `AGENTS/<NAME>/STATUS.md`. Trade execution at `FORGE/STATUS.md`.

## Critical Rules

1. **Read before editing.** Never call Edit without reading the file in the same turn.
2. **Subagents own their files.** Don't edit a file another agent is updating. Wait for it to finish.
3. **Agent data can be hallucinated.** Verify against SEC filings before trading. (PSEC PIK was 8.6%, not 35%.)
4. **Prices must be live.** Never cite prices from STATUS files.
5. **Trade proposals → Will approves.** Never execute without [Approve].
6. **Puts on green days, calls on red days.** Note when breaking and why.
7. **Roll duration, don't trim size.** Trimming = thesis broken. Rolling = timeline uncertain.
8. **Mechanical before creative.** Rolls, trims, expiries BEFORE new research threads.
9. **Deploy agents then wait.** If you spawn for a decision, wait for outputs.
10. **Close the proposal loop.** Proposal → decision → execution → record in originating agent's STATUS.md.
11. **trash > rm.** Always use trash for deletions.

## Key Directories

| Path | Purpose |
|------|---------|
| AGENTS/ | All agent domains, STATUS files, knowledge bases |
| FORGE/ | Trade execution — positions, P/L, per-trade folders (KRE/, WAL/, OZK/) |
| FORGE/timing/ | Thesis timing research, convergence timeline, 44-file research corpus |
| FORGE/tools/market-data/ | Live data CLI: `python3 fetch.py price KRE`, `python3 dashboard.py` |
| memory/ | Daily session notes (YYYY-MM-DD.md) |
| PROME/ | Coordinator state (SCRATCH, STATUS, FLEET_SCAN, ORCHESTRAL_LAYER_DESIGN, AUTONOMY) |
| WILL/ | Will's journal, ideas, trading journal |
| docs/ | OPERATIONS.md, ARCHITECTURE.md |

## Git Protocol

Agents share one working directory and branch. **GitHub is the single source of truth.** All agents pull at session start and **commit locally** at session end. **Pushing is Will-coordinated — not an automatic session-end step:** the shared branch means a per-agent closeout push races other agents' unpushed commits and dirty trees. Commit your work locally so it's preserved; it goes to origin when Will opens a coordinated push window.

> **`git add` ONLY files inside your own `AGENTS/<NAME>/` directory.** Never `git add .` or `git add -A`. If you need to commit a shared file (HEARTBEAT, FORGE, etc.), flag it to Prome — don't commit it yourself.

**At session start:**
1. Follow the "Before pulling" protocol below to sync from GitHub
2. Then proceed with your normal boot sequence

**At session end:**
1. Commit your files locally (follow "Before committing" below).
2. **Do NOT push by default.** Pushing is Will-coordinated — push only inside a window Will has opened. A session-end push races other agents' unpushed commits / dirty trees on the shared branch. (When Will opens a push, one agent's push sweeps everyone's committed-but-unpushed work — see auto-memory `finding_push_train_pattern`.)
3. Note any pending push in your session notes so the next coordinated push window sweeps it.

**Before committing:** (pathspec pattern — avoids the shared-`.git/index` race; see auto-memory `finding_pathspec_commit_race_safety`, incident `8ac5bf71` Jun 4 2026)
1. **For modified files:** `git commit AGENTS/<YOUR_NAME>/<file> -m "..."` — path-scoped commit, no separate staging step.
2. **For new untracked files:** atomic `git add <specific files> && git commit <same specific files> -m "..."` — explicit paths only, **never `git add AGENTS/<YOUR_NAME>/` as a directory** (sweeps in unintended files).
3. **Optional sanity check** between add and commit on new-file flows: `git diff --cached --stat`.
4. **Never `git reset HEAD`** — shared `.git/index` makes it a global unstage that races against other agents' concurrent stages.
5. **Pre-commit sanity check (mandatory):** before committing, run `git status -- AGENTS/<YOUR_NAME>/`. Confirm: no dangling deletions (bash-`mv` residue), no unstaged new files you meant to include, nothing staged outside your own dir. 5-second guard against the `git mv`-vs-`bash mv` residue class (auto-memory `git_mv_for_inbox_processing`) and the cross-dir-leak class. *(Validated 2026-06-26: on first use this caught 53 foreign pre-staged files mid-race + surfaced a months-old display-copy desync.)*

**Before pulling:**
1. `git status` — check for uncommitted changes **OUTSIDE** your directory
2. If you see modifications in other agents' directories: **STOP. Do not pull.** Other agents' uncommitted work will be lost. Choose one:
   - **Option A:** Flag to Will and wait for instruction
   - **Option B (if Will unavailable):** Commit your work locally and defer the push. Note in your MEMORY.md session notes that a push is pending. Push next session when the working directory is cleaner.
3. If working directory is clean outside your files: proceed with stash/pull/pop
4. `git stash push -- AGENTS/<YOUR_NAME>/` — stash only your files
5. `git pull --rebase`
6. `git stash pop`
7. If stash pop fails: `git stash drop` is OK **only if YOUR files are already committed.** Never drop a stash containing other agents' work.
8. Never resolve merge conflicts in another agent's files — flag to Prome

**Never:** force push, commit outside your directory without instruction, resolve another agent's conflicts, pull when other agents have uncommitted local changes.

## Data Hygiene

Closeout discipline, fleet-wide (ratified 2026-06-26 after a 5-agent architecture review; see `PROME/cluster/2026-06-26_fleet_arch_compare.md`).

- **Ledger staleness — STATUS is canonical truth.** TSV workbook ledgers (KB/VX/FLOW/etc.) silently drift behind STATUS — a *universal* fleet failure mode. Keep each ledger in one of two states, never the silent-rot middle: **(a) FROZEN** — dead ledger, prepend a banner `FROZEN <date> — not maintained; STATUS is canonical, do not cite rows as current`, and stop maintaining it; or **(b) LIVE with a boot-time mtime staleness alert** (surface "X.tsv stale Nd" at boot, not at closeout).
- **Research/sources retirement (closeout step):** a file that is *>60 days old AND not boot-read AND not referenced by a live doc* → `git mv` to `archive/`. Prevents research-graveyard accumulation.
- **Out of scope (do not build):** outbox-kill / new cross-agent send protocols / inbox boot-auto-triage. File-based messaging is slated for replacement (auto-memory `messaging_overhaul`) — interim is only "stop writing dead outbox files"; route messaging redesign to that effort.

## Tools

- Python venv at `.venv/`
- pdfminer.six: `from pdfminer.high_level import extract_text`
- Market data: `python3 FORGE/tools/market-data/dashboard.py` (see README.md there)
- Dashboard: `systemctl --user status dashboard`

## Reference

**Status key:** 🟢 none | 🟡 monitoring | 🟠 elevated | 🔴 active/critical

**Cost model:** Heavy research on Sonnet, synthesis on Opus. Typical sub-agent: $0.02-0.05. Long research: $0.10-0.20.
