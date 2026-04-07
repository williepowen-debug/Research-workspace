# Prompt 8 Distilled: Open Output Systems — What We Keep

**Source discipline:** Military COP doctrine, Blackboard Pattern (AI), IC dissemination, event-driven architecture (Kafka), wire services (AP/Reuters), cognitive load research
**Core question answered:** Is there a better model than point-to-point inboxes where agent outputs are "out in the open" — and what kills shared displays in practice?

---

## The Big Idea: The COP Is Curated, Not Comprehensive

Six models were examined. All of them confirm the same thing: **shared visibility beats siloed messaging.** But every model that failed — FEMA's HSIN during Katrina, overloaded combat displays, noisy wire feeds — failed for the same reason: they showed everything equally and expected consumers to sort it out.

A COP that shows everything is a data dump. A COP that shows the right things with clear hierarchy is the most powerful coordination tool available.

**WALTER = the editor, not the wire.** AP puts everything on the wire. The newspaper editor decides what makes the front page. WALTER's job is editorial judgment: what matters right now, what changed, what's converging, what can wait.

---

## The Three-Layer Architecture (Confirmed)

The research across all six models converges on the same hybrid that emerged in the Prompt 5 distillation and last session's discussion with Will:

| Layer | What | Where | Who Reads It |
|-------|------|-------|-------------|
| **1. COP** | Curated current picture, ~15 lines | `COP.md` at repo root | Everyone. Will first. Agents at boot. |
| **2. Signal Archive** | Every signal WALTER produces, full detail | `AGENTS/WALTER/signals/` | Agents who want detail. On demand. |
| **3. Push Notifications** | FLASH/IMMEDIATE pings only | Telegram to Will + agent inbox pointers | Will immediately. Agents next session. |

**Layer 1 is the product.** Layers 2 and 3 support it. If WALTER only delivers one thing, it's the COP.

---

## What Makes a COP Work (From Military + Emergency Management)

### It must be maintained by a single owner
A COP with no maintainer goes stale. Stale COP is worse than no COP — it creates false confidence. WALTER owns COP.md. Nobody else edits it. WALTER updates it every session.

### It must be organized by domain, not by time
Chronological feeds (newest first) force readers to reconstruct the picture themselves. Domain-organized views (labor, credit, energy, Japan, positions) let readers jump to what they care about and ignore the rest.

### It must show hierarchy
FLASH items at the top, visually distinct. ROUTINE at the bottom or omitted. If everything looks the same, nothing stands out. The COP from the earlier discussion had this right: FLASH/IMMEDIATE → ELEVATED → MONITORING → No change.

### It must be scannable in 30 seconds
If you can't get the picture in half a minute, the COP is too long. Military COPs are one screen. Ours should be one screenful of terminal output.

---

## The Blackboard Pattern: What Applies, What Doesn't

The Blackboard Pattern (from AI research) is the most architecturally similar to what we're building: specialist agents post findings to a shared surface, read each other's work, and are triggered to contribute when something relevant appears.

**What applies:**
- Agents don't need to know about each other — only about the shared surface (COP + archive)
- Agents can join or leave without disrupting the system
- All history preserved — complete audit trail
- Convergence is naturally visible when multiple agents write to the same area

**What doesn't apply:**
- Blackboard agents watch the board in real-time and react. Our agents are ephemeral — they boot, read once, work, end. No continuous watching.
- The "control component" (who acts next based on board state) assumes a persistent scheduler. We have Will deciding which agent to boot next.

**Bottom line:** We get the Blackboard's coordination benefits at boot time, but not its real-time reactivity. That's fine — our decisions operate on hours and days, not milliseconds.

---

## What Kills Shared Displays (Cognitive Load Research)

This is the cautionary section. Every shared display failure in the research came from one of four causes:

### 1. Everything looks equally important
If every COP entry is the same format, same font, same indentation — the reader's eye has no anchor. The FLASH item about Kharg Island looks the same as the routine JOLTS monitoring note.
**Fix:** Visual hierarchy. Status indicators (🔴🟠🟡) and precedence labels (FLASH, IMMEDIATE, etc.) at the start of every entry.

### 2. Operators spend effort understanding the INTERFACE, not the CONTENT
If the COP format changes between sessions, or uses inconsistent terminology, or requires learning a schema — readers waste cognition on the container instead of the content.
**Fix:** Identical format every time. Same sections, same order, same conventions. Agents and Will should be able to read the COP on autopilot so all their attention goes to what's new.

### 3. Routine notifications mask urgent warnings
During high-tempo operations, the volume of routine updates drowns urgent items. This is the alert fatigue problem from ATC (Prompt 3).
**Fix:** The COP has sections by severity. FLASH/IMMEDIATE always at the top, always visible, even if the MONITORING section is 10 lines long. During crisis periods (MINIMIZE), the COP may OMIT routine items entirely.

### 4. Too many separate displays
Combat operators facing "dozens of separate displays requiring extensive visual scanning" had degraded performance. Consolidation beats distribution.
**Fix:** One COP. Not one per domain, not one per agent, not one per thesis. One file, one view, one scan. The entire point is consolidation.

---

## The Wire Service Lesson: Format Discipline

AP/Reuters write in inverted pyramid: most critical information first, details later. Editors can cut from the bottom without losing the lead.

**Our application:** Every COP entry follows the same micro-format:
```
• DOMAIN: What happened/what's true. Quantified. [Date]
```

Examples:
```
• BRENT: Kharg Island struck — 90% Iran exports at risk. Trump deadline 8PM tonight. [Apr 7]
• CARL+BRENT: Gas $4.12 breakpoint + oil surge = consumer squeeze accelerating. [Apr 7]
• LIQUID: HY OAS 316, tightening. Strongest counter-signal — credit NOT confirming stress. [Apr 7]
```

Lead with the domain. State the fact. Quantify. Date it. One line. If an agent or Will wants more, they go to the signal archive.

---

## Open Questions Resolved

| Question from Prompt 8 | Resolution |
|------------------------|------------|
| Where does COP live? | `COP.md` at repo root. WALTER maintains and commits it. |
| Update frequency? | Every WALTER session. Static between sessions. |
| Size management? | Rolling window — only current state + last 48h changes. Historical signals in archive. |
| Agent buy-in? | Add "read COP.md at boot" to agent protocols. Simple. |
| Cross-platform sync? | Git pull brings COP to both platforms. Same as all other files. |
| Who curates when WALTER is offline? | Nobody. COP is static between sessions. Will is the real-time awareness layer. Prome could update in a reduced capacity if needed. |

---

## What We Don't Need From Open Output Systems

- Kafka/NATS/RabbitMQ infrastructure — files and markdown
- Blackboard real-time watchers and control components — agents are ephemeral
- Wire service subscription management — agents just read a file
- Combat system display rendering — we have a terminal, not a tactical display
- FEMA HSIN portal design — we don't have an adoption problem, we have 1 user + ~10 agents
- Market-based bidding/negotiation patterns — too complex for our scale
- WebRTC/SIP multimedia sessions — text files only

---

## The Realistic WALTER Workflow (Confirmed)

1. WALTER boots
2. Reads all agent STATUS files + FORGE + recent signals
3. Detects changes, threshold crossings, convergence
4. Updates COP.md — curated, hierarchical, scannable in 30 seconds
5. Writes any new signals to signals/
6. Pings Will on Telegram if anything is FLASH-level
7. Done

That's the whole system. Everything else is refinement.

---

*Distilled from PROMPT8_OPEN_OUTPUT_SYSTEMS_MASTER.md | April 7, 2026*
