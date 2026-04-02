# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

A multi-agent financial research operation tracking systemic risk transmission. Goal: detect stress early enough to position ahead of consensus. The operator is Will (Eastern timezone).

## How The System Works

Two platforms share this git repo:

- **OpenClaw (VPS):** Prome (coordinator) runs here, spawns sub-agents, manages signals, communicates with Will via Telegram. You don't run here.
- **Claude Code (local):** CARL, REGINALD, SAM, and RED run here as independent sessions. You are NOT spawned by Prome. You communicate with Prome and each other via inbox/outbox files.

Coordination is file-based. Write to `AGENTS/<NAME>/outbox/` to request Prome action. Read `AGENTS/<NAME>/inbox/` for incoming signals. Prome checks these and routes accordingly.

**Transmission chain:** LABOR → CARL → REGINALD → market repricing. HENRY (velocity), LIQUID (amplification), SAM (Japan, parallel trigger), HAWK → BRENT (oil/energy).

**Active agents:** PROME, CARL\*, REGINALD\*, SAM\*, RED\*, LABOR, BROCK, LIQUID, HENRY, HAWK, BRENT, NEXUS. Tier 2 (spawned as needed): ZHAO, HANS, MARCO, BARON, SHADE, HERMES, DARWIN, OTTO, ORACLE. (\* = Claude Code)

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

Agents share one working directory and branch.

> **`git add` ONLY files inside your own `AGENTS/<NAME>/` directory.** Never `git add .` or `git add -A`. If you need to commit a shared file (HEARTBEAT, FORGE, etc.), flag it to Prome — don't commit it yourself.

**Before committing:**
1. `git reset HEAD` — clear staging area
2. `git add AGENTS/<YOUR_NAME>/` — stage only your files
3. `git diff --cached --stat` — verify nothing unexpected
4. If unexpected files: `git restore --staged <file>`

**Before pulling:**
1. Stash your files: `git stash push -- AGENTS/<YOUR_NAME>/`
2. Pull, then pop: `git stash pop`
3. Never resolve merge conflicts in another agent's files — flag to Prome

**Never:** force push, commit outside your directory without instruction, resolve another agent's conflicts.

## Tools

- Python venv at `.venv/`
- pdfminer.six: `from pdfminer.high_level import extract_text`
- Market data: `python3 FORGE/tools/market-data/dashboard.py` (see README.md there)
- Dashboard: `systemctl --user status dashboard`

## Reference

**Status key:** 🟢 none | 🟡 monitoring | 🟠 elevated | 🔴 active/critical

**Cost model:** Heavy research on Sonnet, synthesis on Opus. Typical sub-agent: $0.02-0.05. Long research: $0.10-0.20.
