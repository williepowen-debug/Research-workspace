# Message Routing & Communication System Research Prompts

## Prompt 1: Emergency Severity Index (ESI) Triage Systems

**Research Agent:** Domain expert in medical triage systems

**Task:** Conduct deep research into the Emergency Severity Index (ESI) and other medical triage protocols. Extract principles applicable to financial signal routing systems.

**Research Questions:**
1. What is the complete ESI algorithm? How do triage nurses determine levels 1-5?
2. What is the difference between "acuity" (levels 1-2) and "resource needs" (levels 3-5)? How is resource need predicted?
3. What are the error rates and failure modes of ESI? When does it break down?
4. How does ESI handle "fast track" patients who bypass normal queues?
5. What are the Canadian CTAS, Australian ATS, and UK MTS systems? How do they differ from ESI?
6. What is the "triage drift" phenomenon and how is it mitigated?

**Deliverables:**
- Summary of ESI algorithm with decision tree
- Comparison table: ESI vs CTAS vs ATS vs MTS
- Key principles applicable to financial signal routing
- Warning: what NOT to copy from medical triage

**Sources:** AHRQ ESI Handbook, peer-reviewed triage studies, emergency medicine journals

---

## Prompt 2: Military Message Precedence & Routing

**Research Agent:** Domain expert in military communications

**Task:** Investigate military message handling systems (USMTF, NATO APP-11, DOD Message Handling System). Extract routing and precedence principles.

**Research Questions:**
1. What are the standard precedence levels (FLASH, IMMEDIATE, PRIORITY, ROUTINE)? What are the delivery time requirements for each?
2. How does military messaging handle "precedence override" — when a higher priority message arrives?
3. What is the difference between "precedence" (speed) and "classification" (security)? How do they interact?
4. How are messages routed by "action addressee" vs "information addressee"?
5. What is the "need to know" principle and how is it enforced?
6. How does military messaging handle receipt confirmation and non-repudiation?
7. What are the failure modes? What happens when networks are degraded?

**Deliverables:**
- Precedence level definitions with time standards
- Routing decision matrix (precedence × classification × recipient role)
- Principles for financial signal routing
- Comparison: military need-to-know vs financial need-to-act

**Sources:** DOD Message Handling System docs, NATO STANAG 4406, FM 6-02.40

---

## Prompt 3: Air Traffic Control Message Systems

**Research Agent:** Domain expert in aviation systems

**Task:** Research air traffic control communication protocols (ICAO PANS-ATM, ARTS, flight strips). Extract principles for real-time state management.

**Research Questions:**
1. What is the "flight strip" system? How do controllers visually scan and prioritize?
2. How does ATC handle "conflict detection" — identifying when two aircraft need attention?
3. What are the standard message types (clearance, instruction, advisory, request)?
4. How does ATC handle handoffs between controllers? What information transfers?
5. What is the "sterile cockpit" rule and how does it relate to distraction management?
6. How do emergency declarations (MAYDAY, PAN-PAN) override normal traffic?
7. What is the "sweatbox" training and how does it test controller decision-making?

**Deliverables:**
- Flight strip data elements and visual layout principles
- Conflict detection algorithms applicable to signal clustering
- Handoff protocols for agent-to-agent transfer
- Principles for managing cognitive load

**Sources:** ICAO Doc 4444, FAA Order 7110.65, NASA ATC research

---

## Prompt 4: Publish-Subscribe Message Brokers

**Research Agent:** Domain expert in distributed systems

**Task:** Investigate modern message broker architectures (Kafka, RabbitMQ, NATS). Extract patterns for durable, scalable routing.

**Research Questions:**
1. What is the "topic" vs "queue" distinction? When to use each?
2. How do "consumer groups" enable load balancing across multiple consumers?
3. What is "durable subscription" — can consumers replay missed messages?
4. How do brokers handle "backpressure" when consumers are slow?
5. What are the tradeoffs: at-least-once vs exactly-once delivery?
6. How do "dead letter queues" handle failed processing?
7. What is "event sourcing" and how does it relate to audit trails?

**Deliverables:**
- Architecture patterns: topic-based vs content-based routing
- Consumer group load balancing strategies
- Durability and replay mechanisms
- Failure handling patterns applicable to agent systems

**Sources:** Kafka documentation, NATS JetStream, RabbitMQ tutorials, Martin Kleppmann's "Designing Data-Intensive Applications"

---

## Prompt 5: Intelligence Community Dissemination Controls

**Research Agent:** Domain expert in intelligence processes

**Task:** Research IC directives 501, 502, 503 (Discovery, Dissemination, Retrieval). Extract principles for controlled information sharing.

**Research Questions:**
1. What is "responsible sharing" vs "need to know"? How has the IC shifted toward "need to share"?
2. What are "dissemination controls" (ORCON, NOFORN, REL TO, etc.)?
3. How does the IC handle "tearline" reports — versions with different classification levels?
4. What is "discovery" — making information findable without pushing it?
5. How are "watchlists" and "subscriptions" used for automated routing?
6. What are the audit requirements for information access?
7. How does the IC handle "foreign disclosure" — sharing with allies?

**Deliverables:**
- Dissemination control taxonomy
- Discovery vs push models
- Tearline concept applied to signal detail levels
- Audit and accountability principles

**Sources:** ICD 501, 502, 503; Intelligence Community Directive documents

---

## Prompt 6: Scientific Collaboration Alert Systems

**Research Agent:** Domain expert in scientific computing

**Task:** Research CERN ATLAS TDAQ, LIGO alert system, ZTF broker. Extract patterns for real-time scientific data distribution.

**Research Questions:**
1. What is the CERN ATLAS "trigger system"? How does it filter 40 MHz of data to 1 kHz?
2. What are "trigger levels" (L1, L2, EF) and how do they cascade?
3. How does LIGO handle gravitational wave alerts? What is the "graceDB" system?
4. What is the ZTF (Zwicky Transient Facility) alert distribution system?
5. How do these systems handle "false alarm" vs "real event" discrimination?
6. What are "circulars" and how do they enable community follow-up?
7. How is latency minimized from detection to alert?

**Deliverables:**
- Multi-level trigger architectures
- False positive management strategies
- Community alert distribution patterns
- Latency optimization techniques

**Sources:** CERN ATLAS TDAQ papers, LIGO alert documentation, ZTF technical papers

---

## Synthesis Prompt: Cross-Domain Principles

**Research Agent:** Systems synthesis expert

**Task:** After reviewing outputs from Prompts 1-6, synthesize cross-domain principles for financial signal routing.

**Synthesis Questions:**
1. What principles appear across multiple domains (medical, military, ATC, etc.)?
2. What are the universal tradeoffs: speed vs accuracy, completeness vs timeliness?
3. What failure modes are common across all systems?
4. What is the "meta" for message routing? What are the invariant patterns?
5. How do these systems handle "overload" — too many messages?
6. What human-in-the-loop patterns are most effective?
7. What should a financial signal routing system copy vs avoid?

**Deliverables:**
- Cross-domain principle matrix
- Universal failure modes and mitigations
- Recommendations for WALTER architecture
- Open questions requiring further research

---

## Research Standards

For each prompt:
- Cite primary sources (official docs, peer-reviewed papers)
- Note confidence level for each claim
- Flag speculation vs established fact
- Include specific examples, not just generalities
- Note when domain-specific details may NOT apply to financial signals
