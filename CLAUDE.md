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

**Active agents:** PROME, CARL\*, REGINALD\*, OZK\*, SAM\*, RED\*, LABOR, BROCK, LIQUID, HENRY, HAWK, BRENT, NEXUS. Tier 2 (spawned as needed): ZHAO, HANS, MARCO, BARON, SHADE, HERMES, DARWIN, OTTO, ORACLE. (\* = Claude Code)

*OZK spun out from REGINALD on 2026-04-24 (promoted from REGINALD/OZK/ to AGENTS/OZK/ as a peer agent). WAL is the next candidate for promotion when ready.*

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
| PROME/ | Coordinator state (SCRATCH, STATUS, TOSCANINI governance) |
| WILL/ | Will's journal, ideas, trading journal |
| docs/ | OPERATIONS.md, ARCHITECTURE.md |

## Git Protocol

Agents share one working directory and branch. **GitHub is the single source of truth.** All agents must pull at session start and commit + push at session end. This ensures every agent works from the latest state and every agent's work is available to others.

> **`git add` ONLY files inside your own `AGENTS/<NAME>/` directory.** Never `git add .` or `git add -A`. If you need to commit a shared file (HEARTBEAT, FORGE, etc.), flag it to Prome — don't commit it yourself.

**At session start:**
1. Follow the "Before pulling" protocol below to sync from GitHub
2. Then proceed with your normal boot sequence

**At session end:**
1. Commit your files (follow "Before committing" below)
2. Push to GitHub (follow "Before pulling" first if remote has diverged)
3. If you cannot push (other agents have uncommitted work), note the pending push in your MEMORY.md session notes

**Before committing:**
1. `git reset HEAD` — clear staging area
2. `git add AGENTS/<YOUR_NAME>/` — stage only your files
3. `git diff --cached --stat` — verify nothing unexpected
4. If unexpected files: `git restore --staged <file>`

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

## Tools

- Python venv at `.venv/`
- pdfminer.six: `from pdfminer.high_level import extract_text`
- Market data: `python3 FORGE/tools/market-data/dashboard.py` (see README.md there)
- Dashboard: `systemctl --user status dashboard`

## Reference

**Status key:** 🟢 none | 🟡 monitoring | 🟠 elevated | 🔴 active/critical

**Cost model:** Heavy research on Sonnet, synthesis on Opus. Typical sub-agent: $0.02-0.05. Long research: $0.10-0.20.
