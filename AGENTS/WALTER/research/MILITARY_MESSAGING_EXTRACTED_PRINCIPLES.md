# Military Messaging Principles — Extracted for Financial Signal Routing

**Source:** Prompt 2 Research — Military Message Precedence & Routing Systems  
**Date:** 2026-04-06  
**Status:** Ready for inbox/messaging system design

---

## Core Architectural Pattern: Dual-Axis Independence

**Military Innovation:** Precedence (urgency) and Classification (access) are **completely orthogonal**

| Dimension | Governs | Controls |
|-----------|---------|----------|
| **Precedence** | Urgency / Speed | How fast the message must be delivered |
| **Classification** | Sensitivity / Access | Who is authorized to see the message |

**Key Insight:** These axes do not imply each other. A FLASH UNCLASSIFIED message demands speed but not secrecy. A ROUTINE TOP SECRET message demands secrecy but can wait.

**Financial Translation:**
| Dimension | Governs | Controls |
|-----------|---------|----------|
| **Precedence** | Time to execution | How fast the signal must be processed |
| **Sensitivity** | Information access | Which agents/users can see the signal |

---

## The Precedence Hierarchy — Financial Translation

| Level | Prosign | Delivery Requirement | Financial Equivalent | Use Case |
|-------|---------|---------------------|----------------------|----------|
| **FLASH OVERRIDE** | W/Y | Immediate — preempts all | System halt / circuit breaker | Margin call, catastrophic loss imminent |
| **CRITIC** | — | ≤10 minutes | Presidential-level alert | Thesis-destroying event confirmed |
| **FLASH** | Z | ≤10 minutes | Critical execution | Stop-loss breach, liquidity trap |
| **IMMEDIATE** | O | ≤30 minutes | Urgent action | Threshold breach, convergence signal |
| **PRIORITY** | P | ≤3 hours | Standard priority | Research request, position review |
| **ROUTINE** | R | ≤6 hours | Background processing | Cache refresh, routine monitoring |

**Note:** The prosign Z (FLASH) resembles a lightning bolt — visual urgency at a glance.

---

## Preemption Mechanics: Ruthless Priority Enforcement

**Military Principle:** Higher precedence traffic **preempts** lower precedence without negotiation.

### Two Preemption Types

| Type | Mechanism | Financial Equivalent |
|------|-----------|---------------------|
| **Station-based** | Higher call terminates lower call at endpoint | Agent reassigned from low-priority to high-priority task |
| **Trunk-based** | Bandwidth reallocated mid-stream | Compute/resources redirected from routine to urgent signals |

**Key Rule:** Preempted parties receive **explicit notification** — they know their work was interrupted.

**Financial Application:**
- FLASH signal arrives → routine signal processing halts
- Agent working on ROUTINE task → reassigned to IMMEDIATE
- Compute resources reallocated from batch jobs to real-time risk
- **Notification:** "Your task [X] was preempted by higher priority signal [Y]"

---

## Dual Precedence: Different Urgency for Different Recipients

**Military Principle:** Same message, different precedence for action vs. information addressees.

| Addressee Type | Precedence | Obligation |
|----------------|-----------|------------|
| **Action (TO:)** | IMMEDIATE | Must respond, can originate reply |
| **Information (INFO:)** | PRIORITY | Awareness only; may take local action |

**Financial Translation:**
| Recipient | Precedence | Obligation |
|-----------|-----------|------------|
| **Primary Agent** | IMMEDIATE | Must act on signal, can spawn sub-tasks |
| **Secondary Agents** | PRIORITY | Awareness; may act within their domain |

**Example:**
- HY OAS spike signal
  - **LIQUID (primary):** IMMEDIATE — assess funding impact
  - **BROCK, HENRY (secondary):** PRIORITY — awareness for positioning

---

## Special Addressing Mechanisms

### Book Messages
- Multiple addresses, each unaware of others
- Relay stations strip addresses before forwarding
- **Financial:** Signal routed to agents without revealing full distribution list

### Address Indicating Groups (AIG)
- Single designator represents 16+ address combinations
- Increases handling speed
- **Financial:** "CREDIT_CHAIN" designator = LIQUID + BROCK + SHADE + REGINALD

### General Messages
- Predefined wide distribution (ALCOM, NAVOP)
- Sequential numbering
- **Financial:** Daily briefing, threshold alerts broadcast

---

## Message Readdressal: Controlled Escalation

**Military Principle:** Recipients can readdress with same, higher, or lower precedence.

| Original Addressee | Can Readdress To | Precedence Change |
|-------------------|------------------|-------------------|
| Action (TO:) | Action or Information | Higher, lower, or same |
| Information (INFO:) | Information only | Higher, lower, or same |

**Key Insight:** Downstream parties who recognize urgency the originator missed can **escalate**.

**Financial Application:**
- Agent receives PRIORITY signal
- Recognizes thesis-critical implications
- Readdresses as IMMEDIATE to other agents
- **Escalation pathway:** Low → Medium → High based on domain expertise

---

## Ten Requirements for Precedence & Preemption (JHU/APL Framework)

| # | Requirement | Financial Implementation |
|---|-------------|-------------------------|
| 1 | **User Selection** | Users indicate signal importance via precedence level |
| 2 | **Content Importance** | Precedence reflects information content, not source |
| 3 | **Rank Ordering** | Multiple precedence levels strictly rank-ordered |
| 4 | **Level Authentication** | System authenticates user access to given precedence level |
| 5 | **Preemption** | Lower precedence preempted under resource overload |
| 6 | **QoS** | Transport service supports application-level performance |
| 7 | **Maximum Goodput** | System maximizes goodput under all scenarios |
| 8 | **Precedence Authorization** | Sender's access pre-authorized; recipient's precedence bestowed at receipt |
| 9 | **Commander's Intent** | Autonomous operations can locally modify policies |
| 10 | **Service Accounting** | Precedence service accountable, traceable, robust |

**Critical Distinction (Req 8):** Precedence is an attribute of the **information**, not the **person**.

---

## Classification vs. Precedence: Orthogonal Application

| Scenario | Classification | Precedence | Meaning |
|----------|---------------|------------|---------|
| ROUTINE CONFIDENTIAL | Protect from unauthorized access | Can wait 6 hours | Sensitive but not urgent |
| FLASH UNCLASSIFIED | Can be read by anyone with valid address | Deliver in 10 minutes | Urgent but not sensitive |
| FLASH TOP SECRET | Restricted access | Deliver in 10 minutes | Urgent AND sensitive |

**Financial Translation:**
| Scenario | Sensitivity | Precedence | Meaning |
|----------|-------------|------------|---------|
| ROUTINE PRIVATE | Position details hidden | Background processing | Internal only, not urgent |
| IMMEDIATE PUBLIC | Market-wide signal | Urgent action | Broadcast, time-critical |
| FLASH CONFIDENTIAL | Limited agent access | Immediate execution | Sensitive thesis, urgent timing |

---

## Key Principles for Financial Signal Routing

### DO Implement

| Principle | Military Source | Financial Application |
|-----------|----------------|----------------------|
| **Ruthless preemption** | MLPP — lower traffic halted for higher | FLASH signal stops all routine processing |
| **Explicit notification** | Preemption tone | Agents know when their task was interrupted |
| **Dual precedence** | Action vs. Information addressees | Primary agent gets IMMEDIATE, secondary gets PRIORITY |
| **Readdressal with escalation** | Downstream parties can escalate | Agents can upgrade signal based on domain expertise |
| **AIG designators** | 16+ addresses in one code | "CREDIT_CHAIN" = multiple agents |
| **Book messages** | Blind distribution | Signal routed without revealing full recipient list |
| **Precedence authorization** | Attribute of information, not person | Junior agent can send FLASH if signal warrants |

### DON'T Implement

| Anti-Pattern | Military Lesson | Our Avoidance |
|--------------|----------------|---------------|
| Precedence = person rank | Precedence is information attribute, not sender rank | Junior agent can send FLASH; senior can send ROUTINE |
| Single precedence for all | Different recipients get different precedence | Primary vs. secondary agent distinction |
| No preemption | Lower traffic blocks higher | Ruthless preemption with notification |
| No readdressal | System prevents escalation | Allow controlled escalation pathway |

---

## Integration with ESI Triage Principles

| ESI Principle | Military Principle | Combined Implementation |
|---------------|-------------------|------------------------|
| Dual-axis (urgency vs resources) | Dual-axis (precedence vs classification) | **Three-axis:** Urgency + Cost + Sensitivity |
| 5 levels (1-5) | 6 levels (ROUTINE to FLASH OVERRIDE) | **Consolidated 5 levels** with preemption |
| Decision Point A (life-saving) | FLASH OVERRIDE | System-critical signals preempt everything |
| Decision Point D (vital signs) | CRITIC system | Automatic escalation for thesis-critical events |
| Fast-track bypass | Book messages / AIG | Simple signals skip queue; complex signals routed to specialists |
| Mandatory re-triage | Readdressal | Signals re-evaluated at intervals; can be escalated |

---

## Recommended Combined System: 3-Axis Classification

| Axis | Levels | Controls |
|------|--------|----------|
| **Urgency (Precedence)** | FLASH / IMMEDIATE / PRIORITY / ROUTINE | When signal is processed |
| **Cost (Resources)** | 0 / 1 / ≥2 resources | Which processing lane |
| **Sensitivity** | PUBLIC / INTERNAL / CONFIDENTIAL | Who can see the signal |

**Example Signal Classification:**
- HY OAS spike: **IMMEDIATE** + **1 resource** + **PUBLIC**
- Position sizing change: **PRIORITY** + **≥2 resources** + **CONFIDENTIAL**
- Margin call: **FLASH** + **0 resources** + **INTERNAL**

---

## Implementation Checklist

- [ ] Define 4 precedence levels with time targets
- [ ] Implement ruthless preemption with explicit notification
- [ ] Build dual-precedence routing (primary vs secondary agents)
- [ ] Create AIG-style designators for common agent groups
- [ ] Enable controlled readdressal/escalation
- [ ] Separate sensitivity axis from urgency axis
- [ ] Authenticate precedence access (attribute of info, not person)
- [ ] Build service accounting/audit trail
- [ ] Test preemption under load

---

## Key Metrics to Track

| Metric | Military Benchmark | Our Target |
|--------|-------------------|------------|
| FLASH delivery time | ≤10 minutes | ≤5 minutes (faster than military) |
| Preemption notification | 100% | 100% |
| Readdressal success rate | — | >95% |
| Precedence authorization errors | — | <1% |

---

## References

- ACP 121 (Allied Communications Publication)
- USMTF (U.S. Message Text Format)
- STANAG 4406 (NATO interoperability)
- Defense Message System (DMS)
- CRITIC system (NSCID No. 7, DCID 7/1)
- JHU/APL Ten Requirements for P&P in Packet Networks

---

**Next Steps:**
1. Review against Prompt 3+ (ATC, Pub-Sub, Intel Community)
2. Draft formal 3-axis specification
3. Prototype routing logic with preemption
