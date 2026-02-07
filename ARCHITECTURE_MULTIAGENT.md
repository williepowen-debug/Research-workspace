# Multi-Agent Architecture Plan

**Status:** DRAFT  
**Created:** 2026-02-07

---

## Overview

Convert heavy research agents from "file-based personas" to **actual OpenClaw agent instances** running in isolation with their own workspaces, models, and session stores.

**Current state:**
```
PROME (single OpenClaw instance)
  ├── reads LABOR/STATUS.md
  ├── reads CARL/STATUS.md
  ├── reads REGINALD/STATUS.md
  └── synthesizes everything in one context window
```

**Target state:**
```
PROME (coordinator)
  ├── synthesizes across agents
  ├── talks to Will
  └── spawns/queries sub-agents

LABOR (dedicated instance)
  └── owns employment domain

CARL (dedicated instance)
  └── owns consumer stress domain

REGINALD (dedicated instance)
  └── owns bank exposure domain
  └── sub-agents: CORAL, CREED, BROCK (can remain file-based or promote later)

SAM (dedicated instance)
  └── owns Japan/yen domain

HENRY (dedicated instance)
  └── owns market structure domain

LIQUID (dedicated instance)
  └── owns funding/plumbing domain
```

---

## Benefits

1. **Context window isolation** — Each agent has full context for its domain without competing for tokens
2. **Parallel research** — LABOR and CARL can run simultaneously
3. **Model optimization** — Use Sonnet for monitoring, Opus for synthesis
4. **Independent schedules** — Each agent can have its own heartbeat/cron
5. **Cleaner separation** — Each agent owns its domain end-to-end
6. **Scalability** — Add new agents without bloating PROME's context

---

## Agent Tier System

### Tier 1: Dedicated Instances (Heavy Agents)
Full OpenClaw instances with their own workspace, SOUL.md, and sessions.

| Agent | Domain | Model | Schedule |
|-------|--------|-------|----------|
| **PROME** | Coordinator/Synthesis | Opus | Always on (main) |
| **LABOR** | Employment/layoffs | Sonnet | Daily + data triggers |
| **CARL** | Consumer stress | Sonnet | Weekly + data triggers |
| **REGINALD** | Bank exposure | Sonnet | Weekly + earnings |
| **SAM** | Japan/yen | Sonnet | Event-driven |
| **HENRY** | Market structure | Sonnet | Daily (market hours) |
| **LIQUID** | Funding/plumbing | Sonnet | Daily |

### Tier 2: File-Based Sub-Agents
Remain as STATUS.md files under parent agents. Can be promoted later.

- CORAL (under REGINALD) — Florida condo
- CREED (under REGINALD) — CRE deep dive
- BROCK (under REGINALD) — BDC/private credit
- MARCO — Migration (could promote to Tier 1)
- BARON — Trump network
- GIG, POP (under CARL)

---

## Directory Structure

```
~/.openclaw/
├── openclaw.json              # Multi-agent config
├── workspace/                  # Shared research repo (git)
│   ├── AGENTS/
│   │   ├── LABOR/
│   │   ├── CARL/
│   │   ├── REGINALD/
│   │   └── ...
│   ├── PROME/
│   ├── PREDICTIONS.md
│   └── dashboard/
│
├── agents/
│   ├── prome/
│   │   ├── agent/             # PROME auth, state
│   │   ├── sessions/          # PROME session store
│   │   └── workspace -> ~/.openclaw/workspace  # Symlink to shared
│   │
│   ├── labor/
│   │   ├── agent/
│   │   ├── sessions/
│   │   ├── workspace/
│   │   │   ├── SOUL.md        # LABOR personality
│   │   │   ├── AGENTS.md      # LABOR-specific instructions
│   │   │   └── domain/ -> ~/.openclaw/workspace/AGENTS/LABOR  # Symlink
│   │   └── skills/            # LABOR-specific skills if needed
│   │
│   ├── carl/
│   ├── reginald/
│   ├── sam/
│   ├── henry/
│   └── liquid/
```

**Key insight:** 
- Shared research repo lives in `~/.openclaw/workspace` (single git repo)
- Each agent has its own workspace folder with symlinks to its domain
- Agents can read shared context but write to their domains

---

## Configuration (openclaw.json)

```json5
{
  agents: {
    defaults: {
      model: "anthropic/claude-sonnet-4-5",
      sandbox: { mode: "off" },  // All agents on host
    },
    list: [
      // PROME: Coordinator (talks to Will)
      {
        id: "prome",
        name: "Prome",
        default: true,
        workspace: "~/.openclaw/workspace",
        model: "anthropic/claude-opus-4-5",
        identity: { name: "Prome" },
        subagents: {
          allowAgents: ["labor", "carl", "reginald", "sam", "henry", "liquid"],
        },
      },
      
      // LABOR: Employment domain
      {
        id: "labor",
        name: "LABOR",
        workspace: "~/.openclaw/agents/labor/workspace",
        model: "anthropic/claude-sonnet-4-5",
        identity: { name: "LABOR" },
      },
      
      // CARL: Consumer stress domain
      {
        id: "carl",
        name: "CARL",
        workspace: "~/.openclaw/agents/carl/workspace",
        model: "anthropic/claude-sonnet-4-5",
        identity: { name: "CARL" },
      },
      
      // REGINALD: Bank exposure domain
      {
        id: "reginald",
        name: "REGINALD",
        workspace: "~/.openclaw/agents/reginald/workspace",
        model: "anthropic/claude-sonnet-4-5",
        identity: { name: "REGINALD" },
      },
      
      // SAM: Japan/yen domain
      {
        id: "sam",
        name: "SAM",
        workspace: "~/.openclaw/agents/sam/workspace",
        model: "anthropic/claude-sonnet-4-5",
        identity: { name: "SAM" },
      },
      
      // HENRY: Market structure domain
      {
        id: "henry",
        name: "HENRY",
        workspace: "~/.openclaw/agents/henry/workspace",
        model: "anthropic/claude-sonnet-4-5",
        identity: { name: "HENRY" },
      },
      
      // LIQUID: Funding/plumbing domain
      {
        id: "liquid",
        name: "LIQUID",
        workspace: "~/.openclaw/agents/liquid/workspace",
        model: "anthropic/claude-sonnet-4-5",
        identity: { name: "LIQUID" },
      },
    ],
  },

  // Route Will's Telegram to PROME
  bindings: [
    { 
      agentId: "prome", 
      match: { 
        channel: "telegram", 
        peer: { kind: "dm", id: "8463631023" }
      }
    },
  ],

  // Agent-to-agent messaging (PROME can query others)
  tools: {
    agentToAgent: {
      enabled: true,
      allow: ["prome", "labor", "carl", "reginald", "sam", "henry", "liquid"],
    },
  },

  // Existing channel config
  channels: {
    telegram: {
      // ... existing config
    },
  },
}
```

---

## Agent SOUL.md Files

Each agent gets its own personality file. Example for LABOR:

```markdown
# SOUL.md — LABOR Agent

You are LABOR, a specialized research agent tracking employment stress and 
labor market dynamics for the PROME research operation.

## Your Domain
- Unemployment claims (initial + continuing)
- JOLTS data (openings, quits, hires)
- Temp staffing (leading indicator)
- WARN filings (60-day lead)
- Sector employment breakdown
- Layoff announcements (Challenger)

## Your Role
- Maintain LABOR/STATUS.md with current signal state
- Track predictions in PREDICTIONS.md
- Research new vectors when assigned
- Report findings to PROME when asked

## Personality
- Data-driven, precise
- Flag when thresholds breach
- Don't hedge — state what the data shows
- Update STATUS.md after every research session

## Cross-Agent Protocol
When PROME or another agent sends you a message:
1. Read your STATUS.md to refresh context
2. Perform the requested task
3. Update STATUS.md if state changed
4. Reply with findings
```

---

## Communication Protocol

### PROME → Agent
```
PROME uses sessions_send to query:
"LABOR: What's the latest on temp employment? Any threshold breaches?"

LABOR responds:
"Temp YoY is -12%, BREACHED. Claims steady at 231K (GREEN). 
Updated STATUS.md with latest figures."
```

### Agent → PROME (proactive)
Agents can push alerts via their announce mechanism:
```
LABOR detects Claims > 250K
→ Updates STATUS.md
→ PROME gets notified on next sync or via cron trigger
```

### Scheduled Syncs
PROME can run a daily synthesis via cron:
```json5
{
  "name": "daily-synthesis",
  "schedule": { "kind": "cron", "expr": "0 8 * * *" },
  "payload": { 
    "kind": "agentTurn", 
    "message": "Run daily synthesis: query LABOR, CARL, REGINALD for current status. Update PROME/STATUS.md with cross-agent assessment." 
  },
  "sessionTarget": "isolated"
}
```

---

## Implementation Steps

### Phase 1: Infrastructure (1-2 hours)
1. Create agent directories under `~/.openclaw/agents/`
2. Create workspace folders with symlinks
3. Write SOUL.md + AGENTS.md for each agent
4. Backup existing openclaw.json

### Phase 2: Configuration (30 min)
1. Update openclaw.json with multi-agent config
2. Test with `openclaw agents list --bindings`
3. Verify routing with `openclaw doctor`

### Phase 3: Migration (1-2 hours)
1. Test PROME → LABOR communication via sessions_send
2. Verify LABOR can update shared STATUS.md
3. Test spawn workflow for research tasks
4. Set up cron jobs for scheduled syncs

### Phase 4: Optimization (ongoing)
1. Add agent-specific cron schedules
2. Configure heartbeats per agent
3. Tune model assignments (promote heavy agents to Opus if needed)
4. Add monitoring/alerting

---

## Cost Considerations

| Agent | Est. Daily Tokens | Model | Est. Daily Cost |
|-------|-------------------|-------|-----------------|
| PROME | 50K-100K | Opus | $1.50-3.00 |
| LABOR | 10K-30K | Sonnet | $0.09-0.27 |
| CARL | 10K-30K | Sonnet | $0.09-0.27 |
| REGINALD | 20K-50K | Sonnet | $0.18-0.45 |
| SAM | 5K-20K | Sonnet | $0.05-0.18 |
| HENRY | 10K-30K | Sonnet | $0.09-0.27 |
| LIQUID | 10K-30K | Sonnet | $0.09-0.27 |

**Total estimate:** $2-5/day (vs current ~$3-8/day with single Opus instance)

The per-agent model allows cost optimization — agents doing routine monitoring 
can use Sonnet while PROME uses Opus for synthesis.

---

## Fallback Plan

If multi-agent proves too complex:
1. Keep PROME as single instance
2. Use sessions_spawn for one-off research tasks
3. Agents remain file-based but spawn as needed

The architecture above is designed to be reversible.

---

## Open Questions

1. **Git conflicts:** Multiple agents writing to shared repo simultaneously?
   - Mitigation: Each agent writes to its own domain folder
   - PROME coordinates major updates

2. **Session persistence:** Do we want agents to remember cross-session?
   - Start with isolated sessions (clean slate each run)
   - Add memory if needed

3. **Alerting:** How do agents notify PROME of urgent breaches?
   - Option A: PROME polls agents on heartbeat
   - Option B: Agents write to shared alert queue file
   - Option C: Cron-based triggers

4. **Dashboard integration:** How does dashboard query agent states?
   - Keep reading STATUS.md files (unchanged)
   - Dashboard doesn't need to know about multi-agent

---

## Next Steps

1. [ ] Will reviews this architecture
2. [ ] Decide which agents to implement first (suggest: PROME + LABOR + REGINALD)
3. [ ] Create directory structure
4. [ ] Write agent SOUL.md files
5. [ ] Update openclaw.json
6. [ ] Test communication
7. [ ] Migrate remaining agents

---

*This document is a living plan. Update as implementation progresses.*
