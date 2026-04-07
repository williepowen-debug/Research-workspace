# Prompt 8: Open Output Systems — Alternatives to Point-to-Point Messaging

**Sources:** Wikipedia (Blackboard Systems), Confluent (Event-Driven MAS Patterns), Medium/Petelin (Blackboard + MCP), DHS (COP for Emergency Responders), Canadian Army Journal, ODNI ICD 501/209, Ambush (Cognitive Load in Combat Systems), MAG Aerospace (COP Benefits)
**Date:** 2026-04-07

---

## The Problem We're Solving

Current system: agents write signals to each other's `inbox/` directories. WALTER decides who gets what. Information lives in silos — to see what CARL received, you read CARL's inbox. To see what REGINALD got, you read REGINALD's inbox. There's no single place to see everything.

Question from Will: Is there a better model where agent outputs are "out in the open"?

---

## Six Models Examined

### 1. Common Operating Picture (COP) — Military / Emergency Management

**What it is:** A single identical display of relevant operational information shared by more than one command. Not a message system — a continuously-updated shared view of reality.

**How it works:**
- One display, many viewers
- Updated by designated producers (intelligence staff, liaison officers)
- Consumers don't receive messages — they look at the picture
- The picture is organized spatially and hierarchically by domain
- Everyone sees the same information but focuses on their sector

**Why it succeeds:**
- Eliminates the "I didn't get that message" problem
- Forces information producers to synthesize (you can't put raw data on a COP — it would be illegible)
- Creates shared context without explicit coordination
- Natural convergence detection: when multiple indicators light up in the same area, everyone sees it

**Why it fails:**
- Hurricane Katrina: FEMA had a COP system (HSIN). Almost nobody used it. Agencies didn't know it existed, had no training, and the portal was hard to find. The tool existed but the adoption didn't.
- Cognitive overload: combat systems that "technically display all necessary information but practically overwhelm operators during critical moments." The COP becomes noise if not aggressively curated.
- Requires a dedicated maintainer. A COP that nobody updates is worse than no COP — it creates false confidence in stale information.

**Key design principle:** A COP is not a feed — it's a curated summary. Someone (WALTER, in our case) owns it, maintains it, and is accountable for its accuracy. The difference between a COP and a data dump is editorial judgment.

**Applicability to us:** HIGH. A single document that WALTER maintains showing "here's what's happening right now across all domains" — organized by domain (labor, credit, energy, Japan, etc.), timestamped, with precedence indicators. Agents read it at boot. Will reads it anytime.

---

### 2. Blackboard Pattern — AI / Software Architecture

**What it is:** A shared knowledge repository ("blackboard") where specialist agents post findings and read each other's work. No direct agent-to-agent communication — all interaction happens through the shared surface.

**The metaphor:** Experts gathered around a physical blackboard. Each watches for opportunities to contribute their expertise. When one expert writes something, others see it and may be triggered to add their own analysis.

**Three components:**
1. **Blackboard** — structured global memory with all data, hypotheses, partial solutions
2. **Knowledge Sources** — specialized agents that read from and write to the blackboard
3. **Control Component** — decides which agent acts next, based on current blackboard state

**How agents interact:**
- Agents don't know about each other — only about the blackboard schema
- Agents can join or leave without disrupting the system
- Coordination is implicit: Agent A writes a finding → Agent B sees it and is triggered to analyze → Agent B writes result → Agent C picks it up
- All history is preserved — complete audit trail

**Comparison to inbox model:**

| Aspect | Blackboard | Point-to-Point Inbox |
|--------|-----------|---------------------|
| Coupling | Decoupled via shared schema | Tightly coupled: sender must know recipient |
| Broadcast | One write reaches all interested agents | Must copy to N inboxes |
| History | Complete audit trail | Lost after consumption |
| Context | Agents see full problem state | Agents only know what was sent to them |
| Scalability | Adding agent = permission setup only | Adding agent = new routing rules |
| Discovery | Agents find relevant information themselves | Only see what was explicitly routed |

**Why it succeeds:**
- Handles complex, ill-defined problems through modular contribution
- Supports opportunistic reasoning — agents contribute when they can, not when directed
- Natural convergence: multiple agents writing to the same area of the blackboard makes the convergence visible

**Why it fails:**
- Requires agents to understand and respect the shared schema. If agents write arbitrary data, coordination breaks.
- The control component is critical — without it, agents may thrash (repeatedly reading the same state without progress) or starve (never getting triggered)
- Performance degrades if the blackboard grows unbounded — needs curation/compaction

**Real-world uses:** RADARSAT-1 Mission Control, Adobe Acrobat OCR, military C4ISR systems, game AI.

**Applicability to us:** HIGH but with constraints. Our agents are ephemeral sessions — they can't "watch" the blackboard in real-time. They read it once at boot. This means the blackboard model works for boot-time context loading but NOT for real-time triggering. The control component (WALTER or Prome) still needs to notify agents of urgent items.

---

### 3. Intelligence Community Dissemination — "Discover Broadly, Retrieve Selectively"

**What it is:** The IC shifted from "need to know" (withhold unless proven necessary) to "responsible sharing" (provide unless specific risk proven). Information is treated as a national asset, not property of the originating office.

**Three modes of information flow:**
1. **Discovery** — Learn that information exists without seeing content. Metadata exposure. "I can see there's a signal about CRE stress, but I haven't read it yet."
2. **Dissemination** — Information pushed to authorized personnel. Routine distribution.
3. **Retrieval** — Requester pulls content after discovery. On-demand access.

**Tearlines — same intelligence at multiple levels:**

| Level | Content | Audience |
|-------|---------|----------|
| Full version | Sources, methods, timing, raw data | Originator + cleared analysts |
| Tearline | Analytic conclusion, confidence, action required | Broader cleared audience |
| Sanitized | Generic assessment, no sources | Widest distribution |

**Key insight for us:** The three-mode model maps directly:
- **Discovery** = signal metadata visible on a shared surface (COP/blackboard). Every agent can see WHAT exists.
- **Dissemination** = WALTER pushes urgent signals to specific agents via inbox notifications
- **Retrieval** = agents pull full signal content from a shared location when they need it

This hybrid is the most practical: metadata is open, full content is retrievable, urgent items are pushed.

---

### 4. Event-Driven Patterns — Confluent/Kafka

Four patterns for multi-agent coordination without point-to-point messaging:

**a) Orchestrator-Worker:** Central orchestrator distributes tasks via shared topic. Workers auto-rebalance. Immutable log enables replay.

**b) Hierarchical Agent:** Recursive orchestration layers. Topics become "logical swimlanes." Agents join/leave sibling groups without disruption.

**c) Blackboard (Event Log):** Shared knowledge via append-only event log. "Each worker agent simply produces and consumes events to collaborate." No explicit connections.

**d) Market-Based:** Decentralized agents bid/negotiate through market topics. Eliminates quadratic connections.

**Common thread:** All four use the immutable log as single source of truth. Coordination happens through events, not directed messages. History is preserved. Agents are independently deployable.

**Applicability to us:** The file system IS our event log. Signals written to a shared directory are append-only, timestamped, and readable by anyone. We don't need Kafka — we need the PATTERN from Kafka applied to flat files.

---

### 5. Wire Service Model — AP/Reuters

**What it is:** Stories go on the wire. Every subscribing desk sees everything. Editors pull what's relevant to their beat. The wire doesn't route — it publishes.

**Key properties:**
- Standardized format (inverted pyramid: critical info first, details later)
- No routing by the wire service — pure publish
- Consumers self-select based on their domain expertise
- Wire provides the facts; editorial judgment happens at the desk

**Why it works:** Consumers know their beat. A foreign desk editor doesn't need AP to tell them a story about Iran is relevant — they recognize it themselves.

**Why it fails for us:** Our agents are not persistent subscribers. They don't continuously watch a feed. They boot, do work, and end. A wire model requires continuous consumption, which we can't do.

**What we can borrow:** The format discipline. Every signal written in standardized structure with critical information first. Agents reading the shared surface can quickly scan and self-select.

---

### 6. Cognitive Load Research — What Kills Shared Displays

**The core problem:** "The very attempt to be comprehensive in communication results in a decreased likelihood that truly relevant and critical information will be identified, understood, and acted upon."

**Failure modes:**
- Everything looks equally important → nothing looks important
- Operators spend mental effort understanding the INTERFACE rather than the CONTENT
- Routine notifications mask urgent warnings during high-tempo operations
- "Dozens of separate displays requiring extensive visual scanning"

**Design patterns that work:**
1. **Progressive disclosure** — Basic status visible immediately, details on demand. "Reveal information as situations develop rather than initially overwhelming."
2. **Spatial clustering** — Related information grouped together, reducing visual search
3. **Priority-based presentation:**
   - Safety-critical alerts: highest priority, distinctive characteristics
   - Mission-critical alerts: compete based on tactical importance
   - Informational alerts: queue for low-workload periods
4. **Intelligent alerting** — Adapts to operator state and context, reduces nuisance alerts

**Key lesson for us:** An open-output system that shows everything equally will FAIL. It must be structured with clear visual hierarchy: what's FLASH, what's IMMEDIATE, what's background. The default view should show only what changed since last check. Details available on drill-down.

---

## Synthesis: What Model Fits Our System?

### Constraints

1. **Agents are ephemeral sessions** — they boot, work, and end. No continuous polling.
2. **File-based infrastructure** — no databases, no message brokers, no APIs. Git repo + flat files.
3. **Two platforms** — OpenClaw (VPS) and Claude Code (local). Must work across both.
4. **15+ active agents** — routing table can't be rebuilt for every new agent.
5. **Will needs visibility** — must be able to see everything, quickly, without reading 15 inboxes.
6. **Urgency still matters** — FLASH signals can't wait for next agent boot.

### The Hybrid: COP + Discovery/Retrieval + Push Notification

**Layer 1: The COP (Shared Surface)**
`AGENTS/WALTER/COP.md` — A single, curated document WALTER maintains.
- Organized by domain (Labor, Credit, Energy, Japan, Market Structure, Positions)
- Each domain section: current state, recent signals (last 48h), active concerns
- Timestamped entries so agents can see "what's new since my last session"
- Visual hierarchy: 🔴 FLASH/IMMEDIATE items at top, ROUTINE at bottom
- Updated every time WALTER processes new information
- **This is what Will reads.** This is what agents load at boot for context.

**Layer 2: The Signal Archive (Retrieval)**
`AGENTS/WALTER/signals/` — All signals WALTER produces live here as individual files.
- Standard format per Signal Format Spec
- One file per signal, not per recipient
- Tagged with metadata (domain, precedence, relevant agents, confidence)
- Agents can browse, search, or read any signal they want
- Complete audit trail — nothing is deleted, only aged out
- **This is the "open output" — everything visible, nothing siloed**

**Layer 3: Push Notifications (Dissemination)**
For FLASH and IMMEDIATE signals only, WALTER still writes a lightweight pointer to agent inboxes:
```
# WALTER NOTIFICATION — 2026-04-07T14:30:00Z
Signal: SIG-W-20260407-003
Precedence: IMMEDIATE
Summary: HY OAS widened 28bps in single session — safety net triggered
Full signal: AGENTS/WALTER/signals/SIG-W-20260407-003.md
Action required: Assess funding stress implications
```
One paragraph, not a full signal. Points to the archive. Only for urgent items.

PRIORITY and ROUTINE signals? They live in the COP and the archive. Agents discover them at boot. No inbox spam.

### What This Solves

| Problem | Current System | Hybrid Model |
|---------|---------------|-------------|
| "Where do I see everything?" | Read 15 inboxes | Read COP.md |
| Signal duplication | Same file copied to 5 inboxes | One file in signals/, pointers for urgent |
| Agent can't find cross-domain signal | Only sees own inbox | Browse full signals/ archive |
| Convergence detection | Manual cross-referencing | Visible on COP when domains cluster |
| Cognitive overload | N/A (no shared view exists) | COP is curated, not a data dump |
| FLASH still reaches agents | Yes (inbox) | Yes (push notification to inbox) |
| Audit trail | Scattered across inboxes | Complete in signals/ + route_log |

---

## Open Questions

1. **COP update frequency:** Every signal? Or batched (e.g., every 2 hours during market hours)?
2. **COP size management:** As entries accumulate, how do we archive/rotate? Rolling 48h window?
3. **Agent buy-in:** Do existing agents need to change their boot sequence to read COP.md?
4. **Cross-platform sync:** OpenClaw agents and Claude Code agents both need to read the COP. Git pull timing matters.
5. **Who curates the COP?** WALTER owns it, but during sessions where WALTER isn't active, does it go stale? Does Prome have a backup role?

---

*Prompt 8 — Open Output Systems Research*
*Date: April 7, 2026*
