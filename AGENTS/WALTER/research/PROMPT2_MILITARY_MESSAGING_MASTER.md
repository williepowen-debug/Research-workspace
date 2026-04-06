# Military Messaging Systems — Master Extraction (Prompt 2)

**Sources:** 3 LLM outputs (2 PDFs + 1 Markdown)  
**Date:** 2026-04-06  
**Status:** Comprehensive reference for inbox/messaging system design

---

## 1. Core Architectural Principle: Dual-Axis Independence

**Fundamental Insight:** Precedence (urgency) and Classification (sensitivity) are completely orthogonal dimensions.

| Dimension | Governs | Controls | Example Combinations |
|-----------|---------|----------|---------------------|
| **Precedence** | Speed of delivery | How fast message must be handled | FLASH UNCLASSIFIED (urgent, public) |
| **Classification** | Access authorization | Who can see the message | ROUTINE TOP SECRET (sensitive, can wait) |

**Critical Rule:** These axes do not imply each other. A message can be any combination of urgency × sensitivity.

---

## 2. Precedence Hierarchy (Six Tiers)

| Level | Prosign | Delivery Objective | Authorization | Use Case | Financial Equivalent |
|-------|---------|-------------------|---------------|----------|---------------------|
| **Flash Override / ECP** | Y | **< 3 minutes** | National Command Authority (President, SecDef, CJCS) | Nuclear C2, national survival | System halt, circuit breaker, catastrophic loss |
| **CRITIC** | WW | **≤ 10 minutes** | Intelligence community, NSA-controlled | President's immediate attention | Thesis-destroying event confirmed |
| **FLASH** | Z | **< 10 minutes** | MACOM commanders, combat units | Initial enemy contact, imminent attack | Stop-loss breach, liquidity trap, margin call |
| **IMMEDIATE** | O | **≤ 30 minutes** | MACOM-level, staff officers | Force movements, grave disasters | Threshold breach, convergence signal |
| **PRIORITY** | P | **≤ 3 hours** | Division heads and above | Situation reports, troop movements | Research request, position review |
| **ROUTINE** | R | **≤ 6 hours** | Broadly authorized | Periodic reports, logistics | Background monitoring, cache refresh |
| **DEFERRED** | — | No fixed ceiling | Bulk transfers | Non-urgent admin | Batch jobs, analytics |

**Key Details:**
- Prosign Z (FLASH) resembles lightning bolt — visual urgency
- Prosign O = "Operational Immediate" (original full title)
- **200-word limit** on FLASH/IMMEDIATE — enforces brevity at high urgency
- Time measured from filing at originator to availability at destination

---

## 3. Preemption Mechanics: Ruthless Priority Enforcement

### Legacy Circuit-Switched Systems (Hard Preemption)
- Higher precedence **disconnects** active lower-priority calls
- Preempted parties receive distinctive **preemption tone**
- Flash Override cannot be preempted by anything
- Flash can only be preempted by Flash Override

### Modern Store-and-Forward Systems (Soft Preemption)
Active preemption yields diminishing returns (messages transfer in milliseconds). Instead, four complementary mechanisms:

| Mechanism | How It Works | Financial Equivalent |
|-----------|-------------|---------------------|
| **Priority Queuing** | Higher precedence always dequeues first | FLASH signals processed before ROUTINE |
| **Permanent Associations** | Dedicated connections reserved for FLASH/OVERRIDE | Keep TCP connections open for critical signals |
| **DiffServ Packet Marking** | DSCP in IP header; WRED drops low-priority first | QoS tagging for signal packets |
| **Capacity Reservation** | Refuse lower-precedence before max capacity | Reserve compute for critical signals |

**WRED (Weighted Random Early Drop):**
- Monitors queue depth
- Selectively drops lower-precedence packets before buffer full
- TCP interprets drops as congestion, throttles low-priority streams
- High-priority packets bypass WRED, get near-zero queuing delay

**Key Principle:** "Ruthless preemption" — no guarantees for lower precedence in presence of higher.

---

## 4. Dual Precedence: Different Speed for Different Recipients

**Military Innovation:** Same message, different precedence for action vs. information addressees.

| Recipient Type | Header Field | Precedence Example | Obligation |
|----------------|-------------|-------------------|------------|
| **Action (TO:)** | MMHS-Primary-Precedence | IMMEDIATE | Must act, can originate reply |
| **Information (INFO:)** | MMHS-Copy-Precedence | PRIORITY | Awareness only; may act locally |

**Example:** Message marked "P R" (Priority/Routine)
- Action addressees: 3 hours
- Information addressees: 6 hours

**Financial Translation:**
- HY OAS spike signal
  - **LIQUID (action):** IMMEDIATE — assess funding impact
  - **BROCK, HENRY (information):** PRIORITY — awareness for positioning

---

## 5. Special Addressing Mechanisms

### Book Messages
- Multiple addresses, each unaware of others
- Relay stations strip addresses before forwarding
- **Financial:** Blind carbon copy with compartmentalized distribution

### Address Indicating Groups (AIG)
- Single designator represents 16+ address combinations
- Increases handling speed
- **Financial:** "CREDIT_CHAIN" = LIQUID + BROCK + SHADE + REGINALD

### General Messages
- Predefined wide distribution (ALCOM, NAVOP)
- Sequential numbering
- **Financial:** Daily briefing, threshold alerts broadcast

### Negative Routing (XMT)
- Exclude specific addressees from collective distributions
- **Financial:** Restricted lists exclude specific traders/desks

---

## 6. Message Readdressal: Controlled Escalation

**Principle:** Recipients can readdress with same, higher, or lower precedence.

| Original Role | Can Readdress To | Precedence Change |
|--------------|------------------|-------------------|
| Action (TO:) | Action or Information | Higher, lower, or same |
| Information (INFO:) | Information only | Higher, lower, or same |

**Key Insight:** Downstream parties who recognize urgency the originator missed can **escalate**.

**Financial Application:**
- Agent receives PRIORITY signal
- Recognizes thesis-critical implications
- Readdresses as IMMEDIATE to other agents
- **Escalation pathway:** Low → Medium → High based on domain expertise

---

## 7. Classification vs. Precedence: Orthogonal Application

| Scenario | Classification | Precedence | Meaning |
|----------|---------------|------------|---------|
| ROUTINE CONFIDENTIAL | Protect from unauthorized | Can wait 6 hours | Sensitive but not urgent |
| FLASH UNCLASSIFIED | Can be read by anyone | Deliver in 10 minutes | Urgent but not sensitive |
| FLASH TOP SECRET | Restricted access | Deliver in 10 minutes | Urgent AND sensitive |

**Financial Translation:**
| Scenario | Sensitivity | Precedence | Meaning |
|----------|-------------|------------|---------|
| ROUTINE PRIVATE | Position details hidden | Background | Internal only, not urgent |
| IMMEDIATE PUBLIC | Market-wide signal | Urgent | Broadcast, time-critical |
| FLASH CONFIDENTIAL | Limited agent access | Immediate | Sensitive thesis, urgent timing |

---

## 8. Need-to-Know: Compartmentalized Routing

**Two-Gate Test:**
1. Appropriate clearance level
2. Demonstrated need for specific information

**Both required.** Clearance alone is insufficient.

### Enforcement Mechanisms

| Mechanism | Military | Financial |
|-----------|----------|-----------|
| **Routing Guides** | Signal officers dictate staff distribution | Role-based routing rules |
| **Subject Indicator Codes (SICs)** | 3-character topic codes | Signal type tags (macro, single-name, risk) |
| **Authorization Letters** | Signed by directors, verified by security | Compliance-approved distribution lists |
| **Compartmentalization** | SCI codewords (TALENT KEYHOLE, GAMMA) | Desk-level information barriers |
| **Special Access Programs** | Dedicated channels, separate from GENSER/SCI | Deal-team restricted lists |

### Distribution Limiters

| Designator | Meaning | Financial Equivalent |
|-----------|---------|---------------------|
| **EXDIS** | Exclusive Distribution — named circle only | Specific recipient list |
| **NODIS** | No Distribution — only indicated persons | Eyes only |
| **LIMDIS** | Limited Distribution — protective measures | Restricted list with compliance oversight |

---

## 9. Five-Layer Receipt Architecture

| Layer | Confirms | Mechanism | Financial Equivalent |
|-------|----------|-----------|---------------------|
| **1. Transmission Receipt** | Reached next relay point | Prosign "R" | Signal reached router/gateway |
| **2. Delivery Receipt** | Arrived at destination center | MTA auto-generated | Signal arrived at agent inbox |
| **3. Read Receipt** | Recipient accessed message | User Agent P7 layer | Agent opened/read signal |
| **4. Acknowledgment (AKNLDG)** | Explicit reply required | Per ACP 121 Section 335 | Agent confirms receipt |
| **5. Compliance Confirmation** | Intent to execute | WILCO ("Will Comply") | Agent commits to action |

**Non-Repudiation:** DoD PKI infrastructure — CAC cards sign messages, cryptographically verifiable proof of origin.

---

## 10. Degraded Communications: Graduated Response

### MINIMIZE
- Drastically reduces message volume
- Only designated senior commanders may impose/cancel
- Message switches process only above specified precedence threshold
- **Financial:** During market stress, defer non-critical traffic

### EMCON (Emission Control)
- Graduated scale from unrestricted to full radio silence
- **EMCON Full/Delta:** All emissions prohibited except pre-authorized
- Can receive but cannot transmit (including acknowledgments)
- **Financial:** Read-only mode during system degradation

### BEADWINDOW
- Alerts for Essential Element of Friendly Information (EEFI) disclosure
- Numbered codes (BEADWINDOW 1 = position disclosure)
- **Rule:** Not used if calling attention would be more damaging

### DDIL Framework
- **D**enied, **D**egraded, **I**ntermittent, **L**imited
- Conceptual model for contested communications

### PACE Plans
- **P**rimary, **A**lternate, **C**ontingency, **E**mergency
- Layered fallbacks when infrastructure fails

### Fallback Hierarchy
When digital fails:
1. HF radio (BLOS alternative to SATCOM)
2. Wire/landline
3. Physical couriers
4. Visual communications (flashing light, semaphore, flaghoist)

**Doctrine:** Messenger/courier is "a primary means of communication."

---

## 11. Routing Decision Matrix

| Decision Factor | Determines | Mechanism | Override |
|----------------|------------|-----------|----------|
| **Classification** | Which network carries message | Network access control (NIPRNet/SIPRNet/JWICS) | Hard constraint — cannot override |
| **Precedence** | Speed on selected network | Queue priority, preemption, DiffServ, capacity reservation | MINIMIZE may raise minimum threshold |
| **Recipient Role** | Delivery time per recipient | Dual precedence (Primary/Copy) | Action always receives at primary precedence |
| **Compartment** | Which addresses may receive | Routing indicators, Compartmented Address Book | Cross-domain solutions for gateway |
| **Distribution Limiter** | Who within org may view | Authorization letters, routing guides | Commander authority only |
| **EMCON State** | Whether transmission permitted | Emission control policy | Communication windows; commander authority |

---

## 12. Extractable Principles for Financial Signal Routing

### DO Implement

| Principle | Military Source | Financial Application |
|-----------|----------------|----------------------|
| **Dual-dimension tagging** | Precedence × Classification orthogonal | Urgency × Sensitivity as separate axes |
| **Capacity reservation** | Refuse lower-precedence before max capacity | Guarantee delivery of margin calls during stress |
| **Dual-recipient tiers** | Action vs. Information with dual precedence | PM gets IMMEDIATE, CRO gets PRIORITY for same signal |
| **Graduated degradation** | MINIMIZE → EMCON → full silence | Defer analytics during crisis, preserve execution capacity |
| **Five-layer receipts** | Transmission → Delivery → Read → AKNLDG → WILCO | Delivery, read, ack, compliance confirmation |
| **Word limits at high precedence** | 200-word limit FLASH/IMMEDIATE | Enforce brevity for urgent signals |
| **Permanent associations** | Dedicated connections for FLASH/OVERRIDE | Keep channels open for critical signals |
| **DiffServ + WRED** | DSCP marking, selective drop | QoS tagging, throttle low-priority automatically |
| **Readdressal with escalation** | Downstream parties can upgrade | Agents can escalate based on domain expertise |

### DON'T Implement

| Anti-Pattern | Military Lesson | Our Avoidance |
|--------------|----------------|---------------|
| Precedence = person rank | Attribute of information, not sender | Junior agent can send FLASH if warranted |
| Single precedence for all | Different recipients, different urgency | Primary vs. secondary agent distinction |
| Binary up/down states | Graduated degradation (MINIMIZE levels) | Multi-level stress response, not just on/off |
| No receipt confirmation | Five-layer architecture | Full non-repudiation trail |
| Unlimited message size | Word limits at high precedence | Enforce brevity for urgent signals |

---

## 13. Comparison: Military Need-to-Know vs. Financial Need-to-Act

| Dimension | Military | Financial |
|-----------|----------|-----------|
| **Access gate** | Clearance + demonstrated need | Role authorization + responsibility for subject |
| **Default posture** | Deny unless explicitly granted | Deny unless on authorized distribution |
| **Enforcement** | Routing guides, SICs, SSO verification | Entitlement systems, RBAC, Chinese walls |
| **Compartmentalization** | SCI codewords, SAPs | Desk barriers, deal-team restricted lists |
| **Negative routing** | XMT prosign excludes addresses | Restricted lists exclude conflicted parties |
| **Distribution limiters** | EXDIS/NODIS/LIMDIS | Eyes only, restricted lists, compliance flags |
| **Audit trail** | Tamper-evident logs, DTG tracking | Regulatory audit (MiFID II), timestamped logs |
| **Override authority** | Commander, SSO | Compliance officer, legal |
| **Temporal dimension** | Persists across duty assignment | Transaction-bounded, expires when position closes |
| **Failure consequence** | National security damage | Insider trading, regulatory sanction, reputational damage |

**Key Parallel:** Both implement **positive access control with negative exceptions** — default is denial, access requires explicit authorization, collective distributions narrowed by exemption lists.

**Key Divergence:** Military need-to-know is duty-persistent; financial need-to-act is transaction-scoped and self-extinguishing.

---

## 14. Integration with ESI Triage (Prompt 1)

| ESI Principle | Military Principle | Combined Implementation |
|---------------|-------------------|------------------------|
| Dual-axis (urgency vs resources) | Dual-axis (precedence vs classification) | **Three-axis:** Urgency + Cost + Sensitivity |
| 5 levels (1-5) | 6 levels (ROUTINE to FLASH OVERRIDE) | **Consolidated 6 levels** with preemption |
| Decision Point A (life-saving) | FLASH OVERRIDE / CRITIC | System-critical signals preempt everything |
| Decision Point D (vital signs) | CRITIC system | Automatic escalation for thesis-critical events |
| Fast-track bypass | Book messages / AIG | Simple signals skip queue; complex routed to specialists |
| Mandatory re-triage | Readdressal | Signals re-evaluated; can be escalated |
| Resource prediction | Capacity reservation | Reserve compute for high-precedence traffic |

---

## 15. Recommended Combined Architecture

### Three-Axis Classification

| Axis | Levels | Controls |
|------|--------|----------|
| **Urgency (Precedence)** | FLASH OVERRIDE / FLASH / IMMEDIATE / PRIORITY / ROUTINE / DEFERRED | When signal is processed |
| **Cost (Resources)** | 0 / 1 / ≥2 resources | Which processing lane |
| **Sensitivity** | PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED | Who can see the signal |

### Six-Level Precedence with Time Targets

| Level | Delivery Target | Word Limit | Financial Use Case |
|-------|----------------|------------|-------------------|
| **FLASH OVERRIDE** | < 3 minutes | 50 words | System halt, catastrophic loss |
| **FLASH** | < 10 minutes | 200 words | Margin call, stop-loss breach |
| **IMMEDIATE** | ≤ 30 minutes | 200 words | Threshold breach, convergence |
| **PRIORITY** | ≤ 3 hours | Unlimited | Research request, position review |
| **ROUTINE** | ≤ 6 hours | Unlimited | Background monitoring |
| **DEFERRED** | No ceiling | Unlimited | Batch jobs, analytics |

### Key Mechanisms

1. **Ruthless Preemption** — FLASH stops ROUTINE processing
2. **Dual Precedence** — Primary agents get higher precedence than secondary
3. **Capacity Reservation** — Refuse ROUTINE before max capacity to reserve headroom
4. **Permanent Associations** — Keep connections open for FLASH/OVERRIDE
5. **DiffServ + WRED** — Network-layer QoS with automatic throttling
6. **Five-Layer Receipts** — Full non-repudiation trail
7. **Graduated Degradation** — MINIMIZE levels during stress
8. **Readdressal with Escalation** — Agents can upgrade signals
9. **AIG Designators** — Single code for common agent groups
10. **Word Limits** — Enforce brevity at high precedence

---

## 16. Implementation Checklist

- [ ] Define 6 precedence levels with time targets
- [ ] Implement ruthless preemption with explicit notification
- [ ] Build dual-precedence routing (primary vs secondary agents)
- [ ] Create AIG-style designators for common agent groups
- [ ] Enable controlled readdressal/escalation
- [ ] Separate sensitivity axis from urgency axis
- [ ] Implement word limits at FLASH/IMMEDIATE (200 words)
- [ ] Build capacity reservation (refuse lower-precedence before max)
- [ ] Implement DiffServ + WRED for network-layer QoS
- [ ] Create permanent associations for FLASH/OVERRIDE
- [ ] Build five-layer receipt architecture
- [ ] Implement graduated degradation (MINIMIZE levels)
- [ ] Authenticate precedence access (attribute of info, not person)
- [ ] Build service accounting/audit trail
- [ ] Test preemption under load

---

## 17. Key Metrics to Track

| Metric | Military Benchmark | Our Target |
|--------|-------------------|------------|
| FLASH delivery time | < 10 minutes | < 5 minutes |
| FLASH OVERRIDE delivery | < 3 minutes | < 2 minutes |
| Preemption notification | 100% | 100% |
| Readdressal success rate | — | > 95% |
| Capacity reservation headroom | — | 20% for FLASH/OVERRIDE |
| Word limit compliance | — | 100% at FLASH/IMMEDIATE |

---

## References

- ACP 121 (Allied Communications Publication)
- ACP 126/127 (Tape Relay Procedures)
- ACP 142 (P_Mul Reliable Multicast)
- STANAG 4406 (NATO Military Message Handling)
- MIL-STD-6040 (Message Text Formatting)
- JP 6-0 (Joint Communications)
- AR 25-11 (Army Communications)
- DoD Directive O-5100.19 (CRITIC system)
- NSCID No. 7 / DCID 7/1 (Intelligence reporting)
- Isode M-Switch engineering guidance
- IETF RFC 1274/1275 (DiffServ)

---

**Next Steps:**
1. Review against Prompt 3+ (ATC, Pub-Sub, Intel Community, Emergency Dispatch, Scientific Teams)
2. Draft formal 3-axis specification document
3. Prototype routing logic with preemption and capacity reservation
