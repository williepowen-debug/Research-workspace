# OPERATIONS.md — How This System Works

*Central reference for operating the PROME research network. Updated: 2026-02-07*

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         WILL                                 │
│                      (Telegram)                              │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    PROME (Opus)                              │
│              Coordinator / Synthesizer                       │
│                                                              │
│  • Talks to Will                                            │
│  • Spawns research agents                                   │
│  • Routes proposals for approval                            │
│  • Maintains dashboard                                       │
└─────────────────────────┬───────────────────────────────────┘
                          │ spawns
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              RESEARCH AGENTS (Sonnet)                        │
│                                                              │
│  LABOR    CARL    HENRY    SAM    REGINALD    LIQUID   MARCO │
│    │        │       │       │        │          │        │   │
│    └────────┴───────┴───────┴────────┴──────────┴────────┘   │
│                          │                                    │
│              Each has own workspace + STATUS.md               │
│              Can't message out, spawn, or schedule            │
└─────────────────────────────────────────────────────────────┘
```

---

## Agents Roster

| Agent | Model | Domain | Daily Check-in |
|-------|-------|--------|----------------|
| **PROME** | Opus 4.5 | Coordination | — |
| **LABOR** | Sonnet 4.5 | Employment | 8:00 AM ET |
| **CARL** | Sonnet 4.5 | Consumer Credit | 8:15 AM ET |
| **MARCO** | Sonnet 4.5 | Migration | 8:30 AM ET |
| **HENRY** | Sonnet 4.5 | Market Structure | Not scheduled |
| **SAM** | Sonnet 4.5 | Japan/BOJ | Not scheduled |
| **REGINALD** | Sonnet 4.5 | Regional Banks | Not scheduled |
| **LIQUID** | Sonnet 4.5 | Funding/Plumbing | Not scheduled |

---

## How to Spawn an Agent

### One-Shot (Quick Task)
```
sessions_spawn(agentId="labor", task="Summarize current claims status")
```
Agent wakes → does task → reports back → session ends.

### Ongoing Session (Multi-Turn)
```
sessions_spawn(agentId="labor", task="...", cleanup="keep")
```
Agent wakes → does task → reports back → session stays open.

Then send follow-ups:
```
sessions_send(sessionKey="agent:labor:subagent:...", message="Follow-up question")
```

### Check Active Sessions
```
sessions_list(kinds=["subagent"])
```

---

## Daily Check-In System

### Schedule (Weekdays Only)

| Time (ET) | Time (UTC) | Agent | Cron Expression |
|-----------|------------|-------|-----------------|
| 8:00 AM | 13:00 | LABOR | `0 13 * * 1-5` |
| 8:15 AM | 13:15 | CARL | `15 13 * * 1-5` |
| 8:30 AM | 13:30 | MARCO | `30 13 * * 1-5` |

### Flow

```
1. Cron fires → PROME wakes
2. PROME spawns agent with check-in prompt
3. Agent reviews its STATUS.md
4. Agent reports findings
5. If action needed → PROME sends proposal to Will
6. Will taps [Approve] or [Reject]
7. On approve → PROME executes the action
8. Logged to PROPOSALS.md and transcripts/
```

### Proposal Format (Telegram)

```
🔔 **LABOR Proposal**

**Trigger:** Daily check-in
**Action:** Update STATUS.md with latest claims data

**Rationale:** Claims at 231K, watching for 250K threshold

[✅ Approve] [❌ Reject]
```

---

## Dashboard

**URL:** http://100.86.70.6:8080 (Tailscale required)

### Tabs
1. **Overview** — Position, transmission chain, agent status, predictions
2. **Sub-Agents** — Agent network, recent activity, active sessions
3. **Data** — FRED, BLS, Treasury, SEC filings

### Features
- Hero status card (system-wide RED/ORANGE/YELLOW/GREEN)
- Countdown timers for catalysts
- Sub-agent activity log (auto-refreshes 30 sec)
- Alert badge in header

### API Endpoints
- `/api/agents` — Agent status from STATUS.md files
- `/api/prices` — Live market data
- `/api/subagents` — Sub-agent activity log
- `/api/alerts` — Alert history

### Logging Sub-Agent Activity
```bash
curl "http://localhost:8080/api/subagents/log?agent=labor&task=...&status=completed&result=..."
```

---

## Transcripts

**Location:** `transcripts/[agent]/YYYY-MM-DD_HH-MM_[task].md`

Every sub-agent interaction should be saved as readable markdown:
- Task given
- Agent's thinking
- Response
- Tool usage
- Cost

**Git tracked** — push after sessions for audit trail.

---

## File Structure

```
workspace/
├── AGENTS.md           # Boot instructions
├── SOUL.md             # Prome's personality
├── USER.md             # About Will
├── MEMORY.md           # Long-term memory
├── OPERATIONS.md       # THIS FILE
├── PROPOSALS.md        # Agent action queue
├── PREDICTIONS.md      # Cross-agent predictions
├── CALENDAR.md         # Upcoming events
├── PROME/
│   └── STATUS.md       # Prome's dashboard
├── AGENTS/
│   ├── LABOR/
│   │   ├── STATUS.md
│   │   └── INBOX.md      # Signals from Prome
│   ├── CARL/
│   │   ├── STATUS.md
│   │   └── INBOX.md
│   ├── HENRY/
│   │   ├── STATUS.md
│   │   └── INBOX.md
│   ├── SAM/
│   │   ├── STATUS.md
│   │   └── INBOX.md
│   ├── REGINALD/
│   │   ├── STATUS.md
│   │   └── INBOX.md
│   ├── LIQUID/
│   │   ├── STATUS.md
│   │   └── INBOX.md
│   ├── HAWK/
│   │   ├── STATUS.md
│   │   └── INBOX.md
│   └── MARCO/
│       ├── STATUS.md
│       └── INBOX.md
├── transcripts/        # Saved agent conversations
├── dashboard/          # Web dashboard
└── memory/             # Daily session notes
```

---

## Signal Routing (Inbox System)

**Full protocol:** `docs/SIGNAL_ROUTING.md`

### How It Works

```
Will sends signal → Prome filters & routes → Agent INBOX.md → Agent processes
```

**Prome's job:** Sort signals to the right agent. Don't decide *where* in STATUS.md — just get it to the right house.

**Agent's job:** On session start, check INBOX.md and decide: INTEGRATE, UPDATE, ARCHIVE, or DISCARD.

### Agent Boot Sequence (Updated)

Every agent session should start:

1. **Read INBOX.md** — Process any signals from Prome
2. Read STATUS.md — Current state
3. Do assigned task
4. Update STATUS.md if needed
5. Clear processed inbox entries

### Inbox Locations

Each agent has `AGENTS/[NAME]/INBOX.md`

### Cross-Agent Signals

Some signals touch multiple agents. Prome routes to PRIMARY and notes secondaries:

| Signal Type | Primary | Secondary |
|-------------|---------|-----------|
| Employment | LABOR | CARL, REGINALD |
| Consumer credit | CARL | REGINALD |
| BOJ/Japan | SAM | LIQUID, HENRY |
| Fed policy | LIQUID | HENRY, REGINALD |
| Geopolitical | HAWK | SAM, LIQUID |
| Market structure | HENRY | LIQUID |
| Bank stress | REGINALD | CARL |

---

## Key Commands

### Spawn Agent
```
sessions_spawn(agentId="...", task="...", cleanup="keep")
```

### Send Follow-Up
```
sessions_send(sessionKey="...", message="...")
```

### List Sessions
```
sessions_list(kinds=["subagent"])
```

### Check Cron Jobs
```
cron(action="list")
```

### Add Cron Job
```
cron(action="add", job={...})
```

### Update Dashboard Log
```
curl "http://localhost:8080/api/subagents/log?agent=...&task=...&status=..."
```

---

## Cost Model

| Agent Type | Model | Approximate Cost |
|------------|-------|------------------|
| PROME (coordinator) | Opus 4.5 | $$$ |
| Research agents | Sonnet 4.5 | $ |

**Strategy:** Heavy research on cheap Sonnet, synthesis on smart Opus.

Typical sub-agent task: $0.02-0.05
Long research session: $0.10-0.20

---

## Adding a New Agent

1. Create workspace:
```bash
mkdir -p ~/.openclaw/agents/[name]/workspace
cd ~/.openclaw/agents/[name]/workspace
ln -s ~/.openclaw/workspace/AGENTS/[NAME] domain
ln -s ~/.openclaw/workspace repo
```

2. Create SOUL.md and AGENTS.md (use existing agent as template)

3. Patch config:
```
gateway(action="config.patch", raw="{...}")
```

4. Add to allowAgents list and agentToAgent.allow

5. Optional: Add daily check-in cron

---

## Troubleshooting

### Agent Not Responding
- Check `sessions_list()` for active sessions
- Check transcript file for errors
- Try one-shot spawn to test

### Dashboard Not Loading
```bash
systemctl --user status dashboard
systemctl --user restart dashboard
```

### Cron Not Firing
```
cron(action="list")
```
Check `nextRunAtMs` timestamp.

### Proposal Buttons Not Working
Callback data comes through as user message — PROME handles routing.

---

*This file is the operating manual. Update when procedures change.*
