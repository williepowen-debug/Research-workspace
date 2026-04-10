# Git Protocol for Agent Workspace

**Effective:** April 10, 2026
**Purpose:** Prevent cron job commits from blocking Claude Code agent pushes

---

## Core Rule

**Agents commit their own work. Prome does not auto-commit.**

---

## Background

The problem: Prome's cron jobs (HERMES AM Delivery, STATUS.md auto-refresh) were creating git commits that conflicted with Claude Code agents' uncommitted work. This caused push failures and forced agents to handle complex rebases.

The solution: Remove all auto-commits from Prome. Agents commit when ready.

---

## Agent Responsibilities

Each agent (CARL, REGINALD, SAM, BRENT, etc.) must:

1. **Stage only their own files**
   ```bash
   git add AGENTS/<AGENT_NAME>/
   ```

2. **Commit with descriptive message**
   ```bash
   git commit -m "<AGENT_NAME>: Brief description of changes"
   ```

3. **Pull before pushing**
   ```bash
   git pull --rebase
   ```

4. **Push their commit**
   ```bash
   git push
   ```

---

## What NOT to Commit

These files should NOT be committed by agents:

| File/Directory | Why | What To Do |
|----------------|-----|------------|
| `FORGE/tools/market-data/.cache/*` | Auto-generated market data | Leave uncommitted |
| `FORGE/tools/news-sweep/.cache/*` | Auto-generated news data | Leave uncommitted |
| `**/__pycache__/*` | Compiled Python | Leave uncommitted |
| `HEARTBEAT.md` (if Prome updated) | Prome's file | Let Prome handle |
| `PROME/STATUS.md` (if cron updated) | Auto-refresh | Let Prome handle |

---

## Handling Conflicts

If `git pull --rebase` fails:

1. **Check what's conflicting**
   ```bash
   git status
   ```

2. **If cache files conflict**
   ```bash
   git checkout -- FORGE/tools/market-data/.cache/
   git rebase --continue
   ```

3. **If another agent's files conflict**
   - Stop and ask that agent to commit their work
   - Do NOT stash or modify another agent's files

4. **If truly stuck**
   - Ask Will for guidance
   - Document the blocker in MEMORY.md

---

## Prome's Role

Prome will:
- ✅ Fetch market data (local only, no commits)
- ✅ Run news sweeps (local only, no commits)
- ✅ Send Telegram alerts
- ✅ Spawn agents when needed
- ❌ **NO auto-commits to git**

---

## Spawnable vs Persistent Agents

| Agent | Type | Git Workflow |
|-------|------|--------------|
| LABOR | Persistent (Telegram) | Self-commit |
| CARL | Persistent (Claude Code) | Self-commit |
| REGINALD | Persistent (Claude Code) | Self-commit |
| LIQUID | Persistent (Telegram) | Self-commit |
| BROCK | Persistent (Telegram) | Self-commit |
| BRENT | Persistent (Telegram) | Self-commit |
| SAM | Persistent (Claude Code) | Self-commit |
| RED | Persistent (Claude Code) | Self-commit |
| HERMES | Persistent (Telegram) | Self-commit |
| HENRY | Spawnable | Prome spawns, agent commits |
| HAWK | Spawnable | Prome spawns, agent commits |
| MARCO | Spawnable | Prome spawns, agent commits |
| ZHAO | Spawnable | Prome spawns, agent commits |
| OTTO | Spawnable | Prome spawns, agent commits |
| NEXUS | Spawnable | Prome spawns, agent commits |
| SHADE | Spawnable | Prome spawns, agent commits |

---

## Emergency: If Prome Accidentally Commits

If Prome creates a commit that blocks an agent:

1. Agent documents the conflict
2. Will decides: revert Prome's commit OR agent handles rebase
3. Document lesson in MEMORY.md

---

*Last updated: 2026-04-10 by Prome*
