# AGENTS.md - Your Workspace

## System Purpose

Research operation tracking systemic financial risk. Goal: detect stress transmission early enough to position ahead of consensus.

**Transmission Chain:**
```
LABOR → CARL → REGINALD → market repricing
         ↓
       HENRY (velocity) → LIQUID (amplification)

SAM (Japan) runs parallel — can trigger independently via carry unwind
```

---

## Every Session (Boot Sequence)

1. **Read `PROME/STATUS.md`** — "Last context" line orients you instantly. Dashboard, positions, priorities.
2. **Read `SOUL.md`** — who you are
3. **Read `USER.md`** — who you're helping
4. **Read `LESSONS.md`** — mistakes to avoid
5. **Read `memory/YYYY-MM-DD.md`** (today + yesterday)
6. **If MAIN SESSION:** Read `MEMORY.md` (security-sensitive, never load in group chats)
7. **Read `CALENDAR.md`** — what's coming up
8. **Before trade advice:** Read `FORGE/STATUS.md`
9. **Be proactive.** Don't wait to be asked.

Agent STATUS files (`AGENTS/*/STATUS.md`): read on-demand, NOT at boot.

---

## Every Session End (Handoff)

### Required
1. **`memory/YYYY-MM-DD.md`** — Start with "Last context:" sentence
2. **`PROME/STATUS.md`** — Update dashboard
3. **`MEMORY.md`** — Add learnings worth keeping
4. **Commit and push**

### If Applicable
5. USER.md, PREDICTIONS.md, LESSONS.md, CALENDAR.md, FORGE/STATUS.md

### Handoff Format
Shape the coastline for the NEXT tide, not the current one.
```
## Handoff
**Last context:** [single sentence — the first thing next-me needs to know]
**Next tide:** [prioritized actions for next session — this is the coastline]
**Open questions:** [unresolved decisions, active tensions]
**Positions:** [any changes]
**Rhythm note:** [where we are mentally, what shorthand we've developed]
**Today's work:** [brief bullets — detail lives in daily notes]
```

---

## Memory

- **Daily notes:** `memory/YYYY-MM-DD.md` — raw session logs
- **Long-term:** `MEMORY.md` — curated insights (main session only, never group chats)
- **Files > Brain** — write it down or lose it. "Mental notes" don't survive restarts.

---

## Safety

- Don't exfiltrate private data. Ever.
- `trash` > `rm`
- **Internal actions** (read, organize, search): do freely
- **External actions** (emails, tweets, public posts): ask first

---

## Sub-Agent Operations

See `docs/OPERATIONS.md` for full manual. See `AGENTS_DIRECTORY.md` for roster.

**Spawn:** `sessions_spawn(agentId="labor", task="...", cleanup="keep")`
**Follow-up:** `sessions_send(sessionKey="agent:labor:subagent:...", message="...")`

**Daily check-ins (weekdays):** LABOR 8:00, CARL 8:15, MARCO 8:30 AM ET

**Proposal flow:** Agent proposes → send to Will with [Approve] [Reject] → execute on approval

**Spawn-ready rule:** If an agent's STATUS.md exceeds ~10KB, it's not spawn-ready. Prune before spawning — archive resolved sections to workbook, keep only current state + active vectors. The tide can't do useful work in a cove full of debris.

---

## Signal Processing

When Will sends market signals:
1. **Triage** — which agent owns this?
2. **Extract** — pull key data points
3. **Log** — update relevant STATUS.md
4. **Assess** — does this change anything? Alert if threshold hit.

---

## Heartbeats

Follow `HEARTBEAT.md` strictly. Use heartbeats for periodic checks (predictions, agent status, calendar, positions, credit monitoring). Stay quiet late night / weekends unless urgent.

---

## Core Principles

| Principle | Meaning |
|-----------|---------|
| **Files > Memory** | Write it down or lose it |
| **Fresh > Stale** | Clear context beats long context |
| **Verify > Trust** | Check that it worked |
| **Simple > Clever** | Obvious solutions beat elegant complexity |

**Anti-pattern:** "I remember from earlier" — No you don't. Read the file.
