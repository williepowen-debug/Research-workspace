# Prompt 2 Distilled: Military Messaging — What We Keep

**Source discipline:** Military communications (USMTF, NATO STANAG 4406, MLPP, CRITIC system)
**Core question answered:** How do you enforce priority in a multi-recipient system where speed, sensitivity, and recipient role all matter independently?

---

## The Big Idea: Three Independent Axes

Military messaging's fundamental insight: **urgency, sensitivity, and recipient role are orthogonal**. A message can be any combination:

- FLASH + UNCLASSIFIED = Urgent, anyone can see it (market-wide signal, time-critical)
- ROUTINE + TOP SECRET = Can wait, restricted access (position details, not urgent)
- FLASH + CONFIDENTIAL = Urgent AND restricted (sensitive thesis, urgent timing)

This extends ESI's dual-axis (urgency vs cost) by adding **who should see it** as a fully independent dimension.

| Axis | Controls | Our Translation |
|------|----------|-----------------|
| **Precedence** | How fast it must be delivered | Signal processing priority |
| **Sensitivity** | Who can see it | Which agents receive it |
| **Recipient Role** | What they must do with it | Action required vs awareness only |

---

## Precedence Levels (Adapted)

| Level | Delivery Target | Word Limit | When To Use |
|-------|----------------|------------|-------------|
| **FLASH** | <10 min | 200 words | Stop-loss breach, margin call, liquidity trap |
| **IMMEDIATE** | <30 min | 200 words | Threshold breach, convergence signal, catalyst confirmed |
| **PRIORITY** | <3 hours | Unlimited | Research request, position review, deep analysis |
| **ROUTINE** | <6 hours | Unlimited | Background monitoring, cache refresh, periodic updates |

**The 200-word rule:** At FLASH and IMMEDIATE, enforce brevity. If you can't say it in 200 words, you don't understand it well enough yet. Don't write an essay when the building is on fire.

We don't need FLASH OVERRIDE (nuclear command authority) or CRITIC (presidential intelligence) — our system isn't deep enough to need 6 tiers. Four is right for our scale.

---

## Dual Precedence: Action vs Information Recipients

The most immediately useful pattern in the entire research corpus. Same signal, different urgency for different recipients based on what they need to DO with it.

| Recipient Type | Precedence | Obligation |
|---------------|-----------|------------|
| **Action (TO:)** | Higher | Must act on this signal. Can spawn sub-tasks. Can reply. |
| **Information (INFO:)** | Lower | Awareness only. May act within own domain, not obligated. |

**Example applied to our network:**
- HY OAS spike signal:
  - **LIQUID (action):** IMMEDIATE — assess funding impact, this is your domain
  - **BROCK, HENRY (info):** PRIORITY — be aware, may affect your work

- JOLTS inversion signal:
  - **CARL (action):** IMMEDIATE — integrate into labor transmission thesis
  - **RED, REGINALD (info):** PRIORITY — note for next sweep

This is implementable TODAY in signal file headers. Add `TO:` and `INFO:` lines with precedence.

---

## Ruthless Preemption

Higher precedence **stops** lower precedence work. Not "gets added to the queue" — actually interrupts what's in progress.

**Two rules:**
1. Higher always preempts lower. No negotiation.
2. The preempted party gets **explicit notification** — they know their work was interrupted and why.

**Our translation:** If a FLASH signal arrives while an agent is working a ROUTINE task, the ROUTINE task pauses. The agent gets a message: "Your task [X] was preempted by [FLASH signal Y]."

**Why notification matters:** Without it, agents lose track of interrupted work. The military learned this the hard way — preempted parties need to know so they can resume later.

---

## Readdressal: Agents Can Escalate

This is the "information is smart, rank is not" principle.

**Key rule:** Precedence is an attribute of the **information**, not the **sender**. A junior agent can send FLASH if the signal warrants it. A senior agent can send ROUTINE for non-urgent updates.

**Escalation pathway:**
1. Agent receives PRIORITY signal
2. Recognizes thesis-critical implications the originator missed
3. Readdresses as IMMEDIATE to other agents
4. Downstream expertise upgrades the priority

**Constraint:** INFO recipients can only readdress to other INFO recipients. ACTION recipients can readdress to either.

This matters because the originating agent often doesn't know how significant the signal is to other domains. LABOR sends a PRIORITY employment signal; CARL recognizes it confirms a cascade and escalates to IMMEDIATE.

---

## Address Indicating Groups (AIGs)

Single designator = multiple agents. Saves routing overhead and ensures consistent distribution.

| Designator | Agents | Use Case |
|-----------|--------|----------|
| `CREDIT_CHAIN` | LIQUID + BROCK + SHADE + REGINALD | Credit stress signals |
| `ENERGY_CHAIN` | HAWK + BRENT | Oil/energy signals |
| `FULL_NETWORK` | All active agents | System-wide alerts |
| `THESIS_CORE` | CARL + REGINALD + SAM | Core thesis updates |

Define these once, reference by name in routing. When group membership changes, update the definition, not every signal.

---

## Five-Layer Receipt Architecture

Military messaging tracks five distinct confirmations. We don't need all five, but the concept of layered acknowledgment is valuable.

| Layer | Military | Our Version | Do We Need It? |
|-------|----------|-------------|----------------|
| 1. Transmission | Reached relay point | Signal file written to inbox | Yes (implicit — file exists) |
| 2. Delivery | Arrived at destination | Agent session started, inbox scanned | Yes |
| 3. Read | Recipient opened it | Agent read the signal file | Nice to have |
| 4. Acknowledgment | Explicit "received" | Agent confirms in STATUS.md or outbox | Yes, for FLASH/IMMEDIATE |
| 5. Compliance | "Will comply" (WILCO) | Agent commits to action | Yes, for action addressees |

**Minimum viable:** For FLASH and IMMEDIATE signals, require explicit acknowledgment. For PRIORITY and ROUTINE, delivery confirmation is sufficient.

---

## Graduated Degradation

Military has multiple degradation levels — not just "normal" and "broken."

| Level | What Happens | Our Equivalent |
|-------|-------------|----------------|
| **Normal** | All traffic flows | Standard operations |
| **MINIMIZE** | Only traffic above specified precedence processes | High-vol regime: defer ROUTINE, process PRIORITY+ only |
| **EMCON (partial)** | Can receive but limit transmission | Agents read signals but defer new analysis |
| **EMCON (full)** | Receive only, no output | Read-only mode during system crisis |

**Why this matters:** Our network doesn't have a protocol for "too many signals." During a market event, every agent fires signals simultaneously. Without MINIMIZE, WALTER drowns. With it, WALTER says "MINIMIZE in effect — PRIORITY and above only" and defers the rest.

---

## Failure Modes to Avoid

| Anti-Pattern | What Goes Wrong | Our Fix |
|-------------|----------------|---------|
| Precedence = agent seniority | Senior agents always get priority regardless of signal content | Precedence belongs to the signal, not the sender |
| Single precedence for all recipients | Everyone gets the same urgency | Dual precedence: action vs info |
| No preemption | Lower priority blocks higher | Ruthless preemption with notification |
| No degradation protocol | System chokes during surges | MINIMIZE levels, graduated response |
| Unlimited message length at high urgency | Critical signals buried in prose | 200-word cap on FLASH/IMMEDIATE |

---

## What We Don't Need From Military Messaging

- Prosign codes (Z, O, P, R) — use plain English labels
- DiffServ/WRED packet-level QoS — we don't have a network layer
- DSCP marking and TCP connection management — file-based system
- DoD PKI / CAC card non-repudiation — no cryptographic signing needed
- DDIL framework (Denied, Degraded, Intermittent, Limited) — too granular
- HF radio / physical courier fallbacks — no physical layer
- Book messages (blind distribution) — unnecessary complexity at our scale
- Negative routing (XMT exclusion) — not enough agents to need exclusion lists

---

*Distilled from MILITARY_MESSAGING_EXTRACTED_PRINCIPLES.md + PROMPT2_MILITARY_MESSAGING_MASTER.md | April 6, 2026*
