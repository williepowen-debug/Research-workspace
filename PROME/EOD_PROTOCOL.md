# EOD/AM Agent Protocol

*The daily research cycle. Run AM (market open) and EOD (market close).*

**Last Updated:** 2026-02-27

---

## The Chain

```
DISCOVER → LOG → CORRECT → QUANTIFY → SYNTHESIZE → INFER → CHALLENGE
```

### Step 1: DISCOVER (Agent EOD/AM Scan)

Spawn 6 core agents in parallel. Each searches their domain for new information and reports back.

**Agents:** HENRY, REGINALD, LABOR, LIQUID, SAM, BROCK

**Prompt template (EOD):**
```
EOD Analysis — [DATE]. Market just closed.

Your job: Search for what happened today in [DOMAIN]. 

Key context: [2-3 sentences of today's major events from Prome's view]

Tasks:
1. Web search for today's action in your domain — what's NEW?
2. What changed vs your prior STATUS.md? Explicitly state deltas.
3. Any cross-domain signals you noticed?
4. Update your STATUS.md with today's data
5. Report findings — concise brief (3-5 paragraphs). Start with "[AGENT] EOD BRIEF — [DATE]"

IMPORTANT: Don't just summarize headlines. Tell me what CHANGED and what it means for our thesis.
```

**Prompt template (AM):**
```
AM Scan — [DATE]. Market opening.

Your job: What happened overnight and pre-market in [DOMAIN]?

Tasks:
1. Web search for overnight developments, pre-market moves, international action
2. Any data releases this morning? What's expected?
3. What should we watch today specifically?
4. Update STATUS.md if warranted
5. Brief (2-3 paragraphs). Start with "[AGENT] AM BRIEF — [DATE]"
```

**Notes:**
- Give REGINALD a WIDE lens ("any bank/CRE/regulatory/credit news") not narrow ("why did WAL drop")
- Give each agent 2-3 sentences of context so they know the day's theme
- Agents report directly to chat AND update STATUS.md

---

### Step 2: LOG (Agents Update Files)

After discovery briefs come in, spawn a second round if needed:
- Each agent ensures STATUS.md captures ALL findings
- Cross-agent signals are routed (e.g., BROCK findings → REGINALD inbox)
- Only needed if agents missed logging something in Step 1

---

### Step 3: CORRECT (Prome's Meta-Question)

**This is the highest-leverage step. Only Prome (or Will) can do this.**

After reading all briefs, ask: **"What does each agent have wrong or incomplete given what the OTHER agents found?"**

Look for:
- Agent A found something that changes Agent B's assessment, but B doesn't know
- An agent is anchored on an old framework when new data invalidates it
- Two agents found the same signal from different angles but neither connected them
- An agent's status level (🟢🟡🟠🔴) is stale given today's information

---

### Step 4: QUANTIFY (Cross-Agent Corrections)

Spawn targeted corrections to each agent with blind spots. **Require quantified reactions:**

```
CROSS-AGENT SIGNAL — From Prome (orchestrator).

[Describe the insight they're missing and why it matters]

Respond with:
1. Your honest reaction — does this change anything?
2. If yes, what specifically shifts (probability, timing, severity)?
3. A number: how much does this move your conviction? (X% → Y%)
4. Update STATUS.md if warranted

Keep it concise — 2-3 paragraphs max.
```

**The number is mandatory.** "Interesting, noted" is not acceptable. Force the delta.

---

### Step 5: SYNTHESIZE (Prome's Brief)

Read all agent briefs + reactions. Deliver unified analysis:

- What happened today (facts)
- Cross-agent connections (where the edge is)
- Position implications (what it means for FORGE)
- Signal assessment table (each vector's status + change today)

---

### Step 6: INFER (Go Deeper)

After synthesis, ask: **"What patterns, themes, or inferences are hidden? What's more important than we're giving it credit for?"**

Look for:
- Self-reinforcing loops (A causes B causes more A)
- Timing convergences (multiple catalysts clustering)
- Magnitude underestimates (stacked risks that multiply, not add)
- Structural shifts disguised as cyclical events
- Things that are "obvious" but nobody's positioned for

---

### Step 7: CHALLENGE (RED Team)

Spawn RED agent with the updated thesis:

```
RED TEAM — [DATE]. Here is our current thesis and today's updates:

[Summary of synthesis + inferences]

Our current conviction: [X%]
Key positions: [list]

Your job: Attack this. What are we wrong about? What are we overweighting? 
Where is confirmation bias strongest? Give me your honest probability 
assessment and the single strongest argument against our position.
```

**Run RED at least 2x/week, not necessarily daily.** Save it for when conviction is rising (that's when bias is highest).

---

## Scheduling

| Run | Time (ET) | Agents | Steps |
|-----|-----------|--------|-------|
| **AM** | ~8:30 (after claims/data) | All 6 | 1-5 (skip 6-7 most days) |
| **EOD** | ~4:15 (after close) | All 6 | 1-6 (add 7 on Tue/Thu) |

**Cost estimate:** ~$3-5 per full run (6 agents × ~$0.50-0.75 each). Discovery + correction rounds = ~$6-10 per full cycle.

---

## Delivery

**Option A (Daily routine):** Agents update files silently, Prome delivers one consolidated brief.
**Option B (Deep dive):** Agents report here individually + Prome synthesizes. More messages, more detail.
**Option C (Full cycle):** Agents report + Prome synthesizes + corrections + reactions. Tonight's format. Use for major days.

Default to **A** for normal days, **B** for volatile days, **C** when multiple signals fire.

---

## Auto-Delivery Fix

HENRY and LABOR reports didn't auto-deliver on Feb 27. Workaround:
- If a report doesn't arrive within 3 minutes of spawn, check `subagents list`
- If status = done but no message, pull from agent's STATUS.md directly
- Investigate OpenClaw `sessions.visibility` setting for cross-agent history access

---

## Key Lessons (Feb 27 First Run)

1. **Wide prompts > narrow prompts** — REGINALD missed MFS because asked "why did WAL drop" instead of "what happened in banking"
2. **Cross-agent corrections are the highest-value step** — every agent moved when shown what others found
3. **Quantified reactions prevent hand-waving** — "55% → 68%" is actionable, "noted" is not
4. **Will's meta-questions are irreplaceable** — "what are we getting wrong?" and "what's hidden?" can't be automated
5. **The chain compounds** — each step builds on the last. Skipping steps degrades the whole thing
