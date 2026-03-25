# TOSCANINI — Orchestration Protocol

**Created:** 2026-03-25
**Named for:** Arturo Toscanini — conducted from memory, demanded precision, made the orchestra play better than they thought they could.
**Purpose:** Decision interface between Prome (orchestrator) and Will (decision-maker). Prome generates proposals, Will approves or rejects. Binary only.

---

## How It Works

1. **Prome identifies work** — research gaps, system improvements, agent tasks, architecture needs
2. **Prome frames a proposal** — one decision, clearly scoped, with a reason
3. **Will decides** — Approve or Reject. Optionally one line of context on rejection.
4. **Prome executes** — spawns sub-agents, updates files, routes signals
5. **Prome logs the outcome** — what happened, did it work, what did we learn

---

## Proposal Format

```
🔵 PROPOSAL: [One line. What I want to do.]
→ [One line. Why it matters.]
COST: [Sub-agent spawn / time estimate / context cost]
[Approve] [Reject]
```

**Rules:**
- If I can't explain it in two lines, I haven't thought about it enough
- Max **5 proposals per check-in** — prioritized, most impactful first
- 🔴 prefix for urgent (threshold breach, time-sensitive, blocking other work)
- 🔵 prefix for standard
- 🟢 prefix for low-priority / nice-to-have

---

## When Proposals Happen

| Trigger | What |
|---------|------|
| **Session start** | Read QUEUE.md, present top proposals |
| **Post-scan** | After news/signal scan, batch new proposals |
| **Threshold breach** | Immediate single proposal, 🔴 prefix |
| **Agent completion** | If sub-agent surfaces a decision point, escalate |
| **Will checks in** | Present queue state, ask if ready to decide |

**NOT on heartbeat.** Heartbeats are health checks, not decision sessions. Proposals wait for active engagement.

---

## Rejection Handling

- **Bare reject** = I drop it or deprioritize. No questions asked.
- **Reject + one line** = I adjust and may re-propose with the feedback incorporated.
- **Three rejections on same theme** = I stop proposing in that area until Will raises it.

---

## Batching & Efficiency

- Group related proposals when possible ("approve this research sprint" > 5 individual file proposals)
- If a proposal requires multiple sub-agent spawns, say so upfront — Will approves the batch, not each spawn
- Track spawn count per session to avoid context/cost bloat

---

## Proposal Categories

| Category | Examples |
|----------|---------|
| **RESEARCH** | New thesis investigation, deep-dive on a signal, data pull |
| **ARCHITECTURE** | New folder structure, tracking framework, agent protocol change |
| **AGENT OPS** | Spawn an agent for a specific task, refresh stale agent, prune STATUS |
| **SYSTEM** | Protocol changes, workflow improvements, tool setup |
| **ESCALATION** | Threshold breach that changes positioning thesis, needs awareness |

---

## Execution After Approval

1. Spawn sub-agent with clear task definition + COMPLETION_SPEC instructions
2. Log to DECISIONS.md: proposal + decision + timestamp
3. When sub-agent completes: read COMPLETION block, then:
   - WILL_NEEDS → add to `WILL_QUEUE.md`
   - FOLLOW-UP → draft new proposal in `QUEUE.md`
   - GAPS → note in DECISIONS.md outcome
4. If outcome changes thesis or triggers new work: generate follow-up proposal

**Every spawn instruction must include:**
```
When finished, write a COMPLETION block per PROME/TOSCANINI/COMPLETION_SPEC.md:
STATUS: ✅ DONE | ⚠️ PARTIAL | ❌ BLOCKED
CHANGED: [files]
RESULT: [2-3 sentences]
GAPS: [what couldn't be done + why]
WILL_NEEDS: [things only Will can do, or "None"]
FOLLOW-UP: [next action needed, or "None"]
```

---

## What This Is NOT

- Not a position/trade decision framework (that stays in POSITIONS.md / Will's discretion)
- Not a replacement for direct conversation (Will can always just talk to me normally)
- Not rigid — if Will wants to riff, brainstorm, or go off-protocol, we do that
- The protocol serves us, not the other way around
