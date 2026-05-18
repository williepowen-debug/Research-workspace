# TOSCANINI — Orchestration Protocol

**Created:** 2026-03-25
**Named for:** Arturo Toscanini — conducted from memory, demanded precision, made the orchestra play better than they thought they could.
**Purpose:** Decision interface between Prome (orchestrator) and Will (decision-maker). Prome generates proposals, Will decides: Approve, Pause, or Reject.

---

## How It Works

1. **Prome identifies work** — research gaps, system improvements, agent tasks, architecture needs
2. **Prome frames a proposal** — one decision, clearly scoped, with a reason
3. **Will decides** — Approve, Pause, or Reject. Optionally one line of context.
4. **Prome executes** — spawns sub-agents, updates files, routes signals
5. **Prome logs the outcome** — what happened, did it work, what did we learn

---

## Proposal Format

```
🔵 PROPOSAL: [One line. What I want to do.]
→ [One line. Why it matters.]
COST: [Sub-agent spawn / time estimate / context cost]
CONVICTION: [High / Med / Low — Prome's confidence this produces value]
[Approve] [Pause] [Reject]
```

**Rules:**
- If I can't explain it in two lines, I haven't thought about it enough
- Max **5 proposals per batch** — after 5, checkpoint (report outcomes) before presenting more
- Max **3 concurrent sub-agent spawns** — prevents context/cost bloat, keeps outputs manageable
- 🔴 prefix for urgent (threshold breach, time-sensitive, blocking other work)
- 🔵 prefix for standard
- 🟢 prefix for low-priority / nice-to-have
- ⏰ **Time-sensitive tag** — append to any proposal with a closing window. Prome gets ONE nudge ("this has a window closing at X") if Will hasn't responded. One nudge only, then wait.
- **One spawn, one clear objective.** Each proposal must be achievable within a single sub-agent lifespan (~3-8 min, ~50K tokens). If a task has two distinct goals, split it into two proposals. Bundling causes the agent to run out of steam on the second objective. (Lesson: REGINALD P-002 bundled inbox processing + EARNINGS_PREP upgrade → inbox got done, prep didn't move.)

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

## Decision Handling

- **Approve** = Execute. Log to DECISIONS.md. Spawn if needed (max 2 concurrent).
- **Pause** = Good idea, wrong moment. Stays in QUEUE.md. Re-present when context changes or at next check-in. NOT a rejection — no penalty to the topic.
- **Bare reject** = I drop it or deprioritize. No questions asked.
- **Reject + one line** = I adjust and may re-propose with the feedback incorporated.
- **Three rejections on same *topic*** = I stop proposing on that specific topic until Will raises it. (Topic-specific, NOT category-level. Rejecting a DARWIN refresh ≠ rejecting all agent ops.)
- **Silence** = Wait. Batch pending proposals for next check-in. Nothing auto-proceeds.

---

## Batching & Efficiency

- Group related proposals when possible ("approve this research sprint" > 5 individual file proposals)
- If a proposal requires multiple sub-agent spawns, say so upfront — Will approves the batch, not each spawn
- Track spawn count per session to avoid context/cost bloat
- **Checkpoint flow:** Present up to 5 → Will decides → Prome executes (max 3 concurrent) → checkpoint (report outcomes) → next batch if any
- **Proposal expiry:** No auto-expiry timer. If Will doesn't act, Prome re-presents at next check-in if still relevant, drops if not.
- **Follow-up spawns within an approved workstream are pre-authorized.** If Will approves "spawn HAWK with 7 signals" and HAWK's completion says "need second pass to update scenario probs," Prome spawns without re-proposing. New *direction* still needs a proposal.

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

**Completion check rule:** Before EVERY response to Will during active spawns, Prome runs `subagents list`. Any completed agents get reported FIRST, before addressing Will's message. No exceptions. This prevents completions from getting buried in conversation flow.

**Every spawn instruction must include:**
```
When finished:
1. Write a COMPLETION block to `AGENTS/{your-agent-name}/LAST_COMPLETION.md` (overwrite):
STATUS: ✅ DONE | ⚠️ PARTIAL | ❌ BLOCKED
CHANGED: [files]
RESULT: [2-3 sentences. Must include at least one number.]
GAPS: [what couldn't be done + why]
WILL_NEEDS: [things only Will can do, or "None"]
FOLLOW-UP: [next action needed, or "None"]

2. Also include the same COMPLETION block at the end of your task output.
```

**Backup scan:** At checkpoints and session end, Prome scans `AGENTS/*/LAST_COMPLETION.md` for any results that were missed via system messages.

---

## Check-In Flow (step by step)

When Will starts a session or checks in, Prome runs this sequence:

```
1. BOOT        → Read SCRATCH, STATUS, QUEUE, LESSONS, today's memory
2. SCORE       → Run HUNTING.md scoring across all candidate work (internal, don't show math)
3. TRIAGE      → Scan Prome inbox for cross-agent signals that change priorities
4. RE-RANK     → Update QUEUE.md with scored/ranked proposals
5. PRESENT     → Show Will top 5 proposals with [Approve] [Pause] [Reject] buttons
6. DECIDE      → Will acts on proposals
7. EXECUTE     → Spawn agents (max 2 concurrent), do Tier 1 work
8. CHECKPOINT  → Report outcomes when spawns complete
9. NEXT BATCH  → Present next 5 if any remain
10. CLOSE      → Session Report + SCRATCH handoff
```

**Steps 1-4 happen before Will sees anything.** Will's first interaction is step 5 — a clean, ranked list ready to decide on.

**If Will wants to skip the queue** and talk about something else, that's fine. The protocol serves us, not the other way around. Queue holds until next check-in.

---

## Session Report

At session end (or before `/clear` / `/new`), Prome delivers a short report:

```
## SESSION REPORT — [date, time]
TIER 1 ACTIONS: [what was done in background, bullet list]
PROPOSALS DECIDED: [which proposals moved, outcomes]
QUEUE STATE: [what's pending for next session]
HUNTING: [active directives, any suggested changes]
OPEN THREADS: [anything unfinished that carries forward]
```

This replaces individual FYI pings. One clean summary instead of mid-session noise.

---

## What This Is NOT

- Not a position/trade decision framework (that stays in POSITIONS.md / Will's discretion)
- Not a replacement for direct conversation (Will can always just talk to me normally)
- Not rigid — if Will wants to riff, brainstorm, or go off-protocol, we do that
- The protocol serves us, not the other way around
