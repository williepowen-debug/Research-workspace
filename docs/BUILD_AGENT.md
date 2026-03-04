# BUILD_AGENT.md — Agent Creation Playbook

*Follow this checklist every time. No skipping steps.*

---

## Prerequisites

- Agent name (lowercase for id, UPPERCASE for display)
- Domain definition (one sentence)
- Parent agent (if sub-agent) or standalone
- Central workspace folder exists at `AGENTS/<NAME>/` (or `AGENTS/<PARENT>/sub-agents/<NAME>/`)

---

## Step 1: Create Directories

```bash
mkdir -p ~/.openclaw/agents/<name>/workspace
mkdir -p ~/.openclaw/agents/<name>/agent
```

## Step 2: Create Symlinks

```bash
# Domain — points to central workspace folder
ln -sf ~/.openclaw/workspace/AGENTS/<NAME> ~/.openclaw/agents/<name>/workspace/domain
# For sub-agents:
# ln -sf ~/.openclaw/workspace/AGENTS/<PARENT>/sub-agents/<NAME> ~/.openclaw/agents/<name>/workspace/domain

# Repo — points to main workspace
ln -sf ~/.openclaw/workspace ~/.openclaw/agents/<name>/workspace/repo
```

## Step 3: Create CLAUDE.md

Use `AGENTS/CLAUDE_TEMPLATE.md` as the base. Every agent MUST have:

| Section | Required | Notes |
|---------|----------|-------|
| Identity | ✅ | Name, domain, role in network, parent (if sub-agent) |
| Spawn Protocol | ✅ | 6-step: INBOX → STATUS → execute → write → OUTBOX → update STATUS |
| Domain Scope | ✅ | What you own + what you DON'T own (with agent names) |
| OUTBOX rules | ✅ | Signal format, HERMES delivery note |
| Workbook rules | ✅ | ML/VX/FLOW/FL table with "when to log" tests |
| FILES table | ✅ | All files the agent touches |
| Cross-Agent Signals | Optional | Routing table (who sends to whom, under what conditions) |
| Key Thresholds | Optional | Top 3-5 critical thresholds |

**File must be named `CLAUDE.md`** (not AGENTS.md — standardize going forward).

## Step 4: Create INBOX.md + OUTBOX.md

```bash
# In agent workspace (not central workspace)
~/.openclaw/agents/<name>/workspace/INBOX.md
~/.openclaw/agents/<name>/workspace/OUTBOX.md
```

Standard headers (see any existing agent for format).

## Step 5: Ensure Domain Files Exist

At minimum the domain folder needs:

| File/Folder | Required | Purpose |
|-------------|----------|---------|
| `STATUS.md` | ✅ | Live state, dashboard, thesis. Under 250 lines. |
| `workbook/ML.tsv` | ✅ | Memo log — timestamped evidence |
| `workbook/VX.tsv` | ✅ | Vectors — tracked indicators with thresholds |
| `workbook/FLOW.tsv` | Recommended | Transmission pathways |
| `workbook/PREDICTIONS.tsv` | Recommended | Falsifiable forecasts with confidence + resolution |
| `sources/` | Recommended | Archived research documents |

If workbook files don't exist, create them with headers:
```
# ML.tsv
Entry_ID\tDate\tCategory\tTitle\tSummary\tSource\tDiagnostic_Value\tVector_Link\tTags

# VX.tsv
Vector_ID\tName\tCategory\tCurrent_Value\tYellow\tOrange\tRed\tStatus\tConfidence\tLast_Updated\tSource\tNotes

# PREDICTIONS.tsv
Pred_ID\tDate_Made\tPrediction\tConfidence\tTimeframe\tStatus\tDate_Resolved\tOutcome\tNotes
```

**Note:** FL.tsv is deprecated. Do not create it for new agents. Existing FL.tsv files will be migrated to PREDICTIONS.tsv over time.

## Step 6: Register with OpenClaw

```bash
openclaw agents add <name> \
  --workspace ~/.openclaw/agents/<name>/workspace \
  --agent-dir ~/.openclaw/agents/<name>/agent \
  --model anthropic/claude-sonnet-4-6 \
  --non-interactive
```

Default model: `claude-sonnet-4-6` (cheap, fast). Use `claude-opus-4-6` only for synthesis agents (NEXUS, RED).

## Step 7: Add to Prome's Spawn Allowlist

Edit `~/.openclaw/openclaw.json` → `agents.list` → find `prome` → `subagents.allowAgents` → append agent id.

## Step 8: Add to HERMES Routing Table

Edit `~/.openclaw/agents/hermes/workspace/CLAUDE.md` → Agent Directory table → add row.

## Step 9: Add to AGENTS_DIRECTORY.md

Edit `~/.openclaw/workspace/AGENTS_DIRECTORY.md` → appropriate section → add row.

## Step 10: Verify

```bash
# Can Prome spawn it?
openclaw agents list  # should show agent

# Files in place?
ls ~/.openclaw/agents/<name>/workspace/  # CLAUDE.md, INBOX.md, OUTBOX.md, domain/, repo/
ls ~/.openclaw/agents/<name>/workspace/domain/  # STATUS.md, workbook/
```

## Step 11: Test Spawn

Spawn with a simple orientation task to verify the agent can read its files and respond coherently.

---

## Anti-Patterns

- ❌ Don't name the instruction file AGENTS.md (use CLAUDE.md)
- ❌ Don't put INBOX/OUTBOX in the central workspace (goes in agent workspace)
- ❌ Don't create agents without workbook TSV files
- ❌ Don't skip HERMES + AGENTS_DIRECTORY updates
- ❌ Don't use opus for routine domain agents (cost)
- ❌ Don't let STATUS.md exceed 250 lines (archive old content)

---

*Last updated: 2026-03-04*
