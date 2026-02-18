# SKILLS.md — Operational Principles

*What actually works for this research operation.*

---

## 1. Context Hygiene (Critical)

**Why:** LLMs degrade 39% in multi-turn conversations. We fight this actively.

- **Clear/compact regularly** — Don't let sessions run forever
- **Ground truth in files** — STATUS.md > conversation memory
- **Boot sequence is sacred** — Read files fresh each session
- **Subagents for complex work** — Fresh context beats polluted context

**Anti-pattern:** Relying on "I remember from earlier" — I don't reliably.

---

## 2. Signal Processing

**When Will sends market signals (screenshots, links, data):**

1. **Triage** — Which agent owns this? (LABOR/CARL/HENRY/etc.)
2. **Extract** — Pull the key data points
3. **Log** — Update relevant STATUS.md
4. **Save** — Images to `SIGNALS/images/YYYY-MM-DD/`
5. **Assess** — Does this change anything? Alert if threshold hit.

**Template response:**
```
Logged to [AGENT].
- [Key point 1]
- [Key point 2]
Impact: [None / Confirms thesis / New signal / Alert]
```

---

## 3. Subagent Strategy

**Use subagents when:**
- Task takes >10 minutes
- Need adversarial analysis (RED)
- Domain-specific deep dive
- Parallel research across topics
- Context is already polluted

**How:**
```
sessions_spawn(agentId="red", task="...", cleanup="keep")
```

**One task per spawn.** Don't overload.

**Check back:** `sessions_history(sessionKey="...")`

**Anti-pattern:** Keeping everything in main session until it degrades.

---

## 4. Research Synthesis

**When asked for analysis or briefing:**

1. **Read current state** — Agent STATUS.md files first
2. **Identify gaps** — What's stale? What's missing?
3. **Cross-reference** — How do domains connect?
4. **Synthesize** — What's the integrated picture?
5. **Confidence** — State uncertainty explicitly

**Quality bar:** "Would this hold up to RED team challenge?"

---

## 5. Plan Mode

**Trigger:** Any task with 3+ steps or architectural decisions.

**Process:**
1. Write plan before executing
2. Check in with Will if ambiguous
3. Execute step by step
4. Verify each step worked
5. Document results

**When things go sideways:** STOP. Re-plan. Don't push through.

**Anti-pattern:** Diving into execution without thinking.

---

## 6. Verification Before Done

- **Never assume it worked** — Check the output
- **For file edits** — Re-read to confirm
- **For searches** — Verify results make sense
- **For analysis** — Ask "what could be wrong here?"

**Question:** "Would a staff engineer approve this?"

---

## 7. Self-Improvement Loop

**After ANY correction from Will:**

1. Identify the pattern (not just the instance)
2. Write a rule that prevents recurrence
3. Add to `LESSONS.md` (create if needed)
4. Review lessons periodically

**Format:**
```markdown
## [Date] — [Category]
**Mistake:** [What happened]
**Pattern:** [Why it happened]
**Rule:** [How to prevent]
```

---

## 8. Briefing Generation

**When Will asks for a "briefing" (audio format):**

- **Length:** 15-20 min default (~2,500-3,500 words)
- **Structure:** Hook → Foundation → Current → Mechanics → Implications → Close
- **Style:** Conversational, no tables, explain jargon
- **Numbers:** Speak naturally ("about twelve percent" not "12.34%")
- **Save to:** `AGENTS/[AGENT]/briefings/[AGENT]_Briefing_YYYY-MM-DD.md`

---

## 9. Position Monitoring

**For active trades:**

1. Know the thesis, strikes, expiry, max loss
2. Track key thresholds (break-even, profit targets)
3. Monitor related signals (earnings, catalysts)
4. Alert on significant moves
5. Know falsification criteria

**Dashboard:** http://100.86.70.6:8080

---

## 10. Proposals & Approvals

**For agent-proposed actions:**

1. Format clearly with context
2. Include [Approve] [Reject] buttons where supported
3. Wait for explicit approval
4. Log decisions to relevant files

**Never execute trades or external actions without approval.**

---

## Core Principles

| Principle | Meaning |
|-----------|---------|
| **Files > Memory** | Write it down or lose it |
| **Fresh > Stale** | Clear context beats long context |
| **Explicit > Implicit** | State assumptions, don't assume shared understanding |
| **Verify > Trust** | Check that it worked |
| **Simple > Clever** | Obvious solutions beat elegant complexity |

---

## Anti-Patterns to Avoid

1. **"I remember..."** — No you don't. Read the file.
2. **Long monologues** — Be concise unless asked for depth.
3. **Hedging everything** — Have opinions, state confidence.
4. **Pushing through errors** — Stop, re-plan, ask if stuck.
5. **Skipping verification** — Always confirm it worked.
6. **Over-engineering** — Simple fix > elegant architecture.

---

*Last updated: 2026-02-18*
*Review and iterate as we learn what works.*
