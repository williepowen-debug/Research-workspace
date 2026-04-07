# Prompt 3 Distilled: Air Traffic Control — What We Keep

**Source discipline:** ATC communications (ICAO Doc 4444, FAA 7110.65, EUROCONTROL)
**Core question answered:** How do you manage shared state across handoffs, detect conflicts between signals, and protect cognitive capacity under load?

---

## The Big Idea: Externalized State

ATC's flight strip is a card encoding the full current and planned state of a single tracked object — visible to all controllers, annotated in real time, physically moved to signal state changes.

The strip serves three functions simultaneously:
1. **Legal record** — audit trail of what was decided
2. **Cognitive offload** — working memory written down, not held in someone's head
3. **Shared state** — everyone sees the same picture

**Our translation:** Every routed signal should have a persistent, scannable state record that any agent can read. Not buried in prose inside STATUS.md — structured, consistent, at-a-glance. This is what the Signal Registry Draft A is building toward, and what the signal header block in the Format Spec starts to provide.

The key insight isn't the 24 fields on a flight strip. It's that **if state lives only inside an agent's session, it's lost when the session ends.** Externalize it.

---

## Three-Zone Conflict Detection

ATC doesn't just track individual aircraft — it detects when two of them are about to conflict. WALTER should detect when two signals contradict or when a new signal conflicts with an existing position.

| Zone | Color | Agent System Meaning | Action |
|------|-------|---------------------|--------|
| **No Problem** | Green | Signal consistent with thesis and positions | Monitor passively |
| **Possible Problem** | Yellow | Signal tension — doesn't confirm but doesn't break thesis | Track closely, flag for next sweep |
| **Do Something** | Red | Signal directly contradicts thesis or threatens position | Intervention required |

**Critical design rule from ATC:** The alert system identifies the conflict but **does NOT prescribe the fix**. It says "these two things are in tension" and lets the controller (agent) decide what to do. Over-prescriptive alerts reduce trust and response rates.

---

## Alert Fatigue: The 56% Problem

NASA found that ATC controllers only respond to conflict alerts **56% of the time**. Why? Because alert predictive value and nuisance rate are coupled — too many false alarms train people to ignore all alarms.

**Direct warning for WALTER:** If we route too many signals, agents stop reading them. Every signal that arrives and turns out to be noise makes the next real signal less likely to get attention.

**Mitigations:**
- Calibrate signal thresholds to minimize false alerts — better to miss a marginal signal than to cry wolf
- The confidence score (0.0–1.0) in the Format Spec exists for this reason — agents can filter by their own tolerance
- Track false positive rate over time. If a signal type routinely fires without consequence, tighten the threshold or downgrade its default precedence
- Fewer, higher-quality signals > many low-quality signals

---

## Four-Stage Agent Handoff

When a signal passes from one agent's domain to another, ATC uses a four-stage protocol to prevent orphaned work or lost context:

| Stage | ATC Term | Agent Translation |
|-------|----------|-------------------|
| **1. Notification** | Transferring controller alerts receiving controller | Signal arrives in recipient inbox |
| **2. Coordination** | Propose handoff conditions (altitude, speed, heading) | Originating agent specifies what's needed: "Assess funding impact, respond by EOD" |
| **3. Acceptance** | Receiving controller accepts or counter-proposes | Receiving agent acknowledges and commits (or pushes back: "Need more context") |
| **4. Transfer** | Responsibility shifts at defined point | Receiving agent owns it. Originating agent stops working on it. |

**Silent Transfer:** When conditions are standard and both agents have full context, skip stages 2-3. The signal arrives, the agent picks it up, no negotiation needed. This should be the default for ROUTINE/PRIORITY signals with clear routing.

**When full handoff matters:** Complex signals, cross-domain analysis, anything where the receiving agent might not have enough context. The four stages prevent the "I thought you were handling it" failure mode.

**Key rule from ATC:** Once handoff is initiated, **neither agent may alter the signal** without the other's approval until transfer is complete. No silent edits mid-handoff.

---

## Sterile Cockpit: Protected Processing Windows

FAA rule: No non-essential activities during critical phases (takeoff, landing, below 10,000 ft). ATC applies the same principle — "sterile sector" during high workload.

**Our translation:** When an agent is doing deep work (synthesis, complex analysis, catalyst processing), suppress non-critical interrupts.

**Implementation:**
- WALTER checks agent load before routing. If agent is processing a FLASH or IMMEDIATE signal, defer ROUTINE delivery.
- Agents can declare "sterile" in their STATUS.md — WALTER holds non-critical signals until the window closes.
- Handoffs only in "clean" situations — don't transfer a complex signal to an agent mid-crisis.
- This interacts with the MINIMIZE protocol: MINIMIZE-2 effectively creates a network-wide sterile window.

---

## Message Taxonomy

ATC distinguishes four message types by authority level. This maps to how WALTER frames signals:

| ATC Type | Authority | Requires Confirmation | Our Equivalent |
|----------|-----------|----------------------|----------------|
| **Clearance** | Legal permission, creates accountability | Yes (readback) | Trade execution approval, position entry |
| **Instruction** | Directive to perform action | Yes (readback) | Task assignment: "Assess X, report by Y" |
| **Advisory** | Non-directive, informational | No | Context signals, market data, background |
| **Request** | Asking for information | No | Query to agent: "What's your current read on X?" |

**Conditional format (from ATC):** When a signal includes a conditional action, use four parts:
1. What signal this is about
2. The condition
3. The action if condition met
4. Restatement of condition

Example: "SIG-W-20260407-003 — IF HY OAS crosses 450bps THEN reduce KRE position size — trigger: HY OAS > 450bps"

---

## Planner/Executive Split

ATC separates two roles at every sector:

| Role | Responsibility | Time Horizon |
|------|---------------|-------------|
| **Executive (R-side)** | Radio comms, issues clearances, handles live traffic | Right now — tactical |
| **Planner (D-side)** | Flight data, coordination, conflict anticipation | 10-20 minutes ahead — strategic |

**Our translation:** This is already roughly how the network works. REGINALD/CARL/SAM are "planners" building the thesis picture. FORGE is the "executive" handling live positions. WALTER is a third role — the "coordinator" managing the flow between them.

The principle to keep: **don't make the same agent do tactical and strategic work simultaneously.** If an agent is synthesizing a deep research question, don't interrupt it with a routine data update. The Planner/Executive split is really another argument for the sterile cockpit concept and for the MINIMIZE protocol.

---

## Cognitive Load: The Curvilinear Warning

ATC research shows performance degrades at **both** extremes — too much load (overload, errors) AND too little (vigilance failure, missed signals).

**Our risk on the low end:** During quiet markets, agents get fewer signals. Monitoring becomes passive. A slow-developing stress signal gets missed because nobody is actively scanning.

**Mitigations:**
- Mandatory periodic sweeps even during quiet periods (RED's network sweep serves this function)
- Re-triage intervals for queued signals — forces re-examination
- WALTER should have a "minimum signal rate" check — if an agent hasn't received anything in X days, verify the pipeline is working, not that the world went quiet

---

## What We Don't Need From ATC

- Flight strip 24-field schema (too granular — our Format Spec header serves this purpose)
- Visual layout principles (bay assignment, holder colors, strip manipulation) — we don't have a visual board
- STCA algorithm specifics (2-minute look-ahead, geometric conflict detection) — our conflicts are thematic, not spatial
- Sweatbox training methodology — no simulation environment
- EUROCONTROL/ICAO/FAA specific standards and references
- Endsley's three-level SA theory (Perception → Comprehension → Projection) — keep the practical takeaway, drop the academic framework
- Emergency override details (MAYDAY/PAN-PAN) — already covered better by military messaging's FLASH precedence

---

*Distilled from PROMPT3_ATC_MASTER.md | April 7, 2026*
