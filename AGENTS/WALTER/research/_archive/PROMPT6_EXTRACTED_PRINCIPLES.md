# Prompt 6: Emergency Dispatch — Extracted Principles for WALTER

## What Matters for Signal Routing Architecture

### 1. Hierarchical Routing with Policy Override

**Core Pattern:** Default routing → Policy-based exception handling

- **ECRF (Emergency Call Routing Function):** Geospatial point-in-polygon lookup (deterministic)
- **ESRP (Emergency Services Routing Proxy):** Policy Routing Rules (PRRs) for failover
- **PRF (Policy Routing Function):** Condition-based diversion (hurricane, overload, evacuation)

**WALTER Analog:** Standard agent routing → Toscanini override for system stress

| Emergency Dispatch | WALTER Equivalent |
|-------------------|-------------------|
| ECRF geospatial lookup | Agent capability matching |
| ESRP policy evaluation | Toscanini priority rules |
| PRR call diversion | Signal batching / queue overflow handling |
| Multi-PSAP load balancing | Cross-agent workload distribution |

---

### 2. Location-Agnostic Routing (The PEMEA Pattern)

**Problem:** Application-based emergency routing fails across borders because apps lack foreign PSAP integration.

**Solution (ETSI TS 103 478 / PEMEA):**
- Application Provider (AP) → PSAP Service Provider (PSP) via authenticated interfaces (Pa, Ps, Pr, Pp)
- Location + profile data authenticated and routed across international borders
- Stepping stone toward WebRTC emergency services

**WALTER Analog:** Cross-domain signal routing where agent "home" domain ≠ signal origin domain

**Key Insight:** Authentication and trust boundaries matter more than physical proximity for routing decisions.

---

### 3. Multi-Modal Message Handling

**NG911 Message Types:**
- Voice (SIP/TCP/TLS)
- Real-Time Text (RTT — IETF RFC 4103)
- Video streams
- Sensor telemetry (IoT)
- Advanced Mobile Location (AML)

**Critical Design:** Same SIP session carries interleaved audio + video + text. No separate channels.

**WALTER Analog:** Single signal envelope carrying multiple data types (price + narrative + source confidence)

---

### 4. Determinant Code System (MPDS)

**Medical Priority Dispatch System:**
- 36 protocols → Determinant Code (protocol + acuity + modifiers)
- Acuity levels: OMEGA/ALPHA → BRAVO → CHARLIE/DELTA → ECHO
- Response priority strictly tied to code

| Level | Trigger | Response |
|-------|---------|----------|
| OMEGA/ALPHA | Stable vitals | Cold (no lights/sirens) |
| BRAVO | Moderate emergency | Hot (lights/sirens) |
| CHARLIE/DELTA | Severe/life threat | Hot + ALS + first responder |
| ECHO | Immediate life threat | Maximum priority, closest units regardless of jurisdiction |

**WALTER Analog:** Signal severity classification → Response urgency

**Key Principle:** Pre-arrival instructions (PAIs) = Zero-minute response time. Dispatcher provides clinical guidance while units en route.

→ **WALTER:** Can we provide "pre-arrival" context to agents before full analysis completes?

---

### 5. Pathfinding Algorithms for Resource Allocation

**CAD System Algorithms:**
- **Dijkstra:** Absolute shortest path (baseline)
- **A* (A-Star):** Heuristic-guided, faster, optimal
- **Tabu Search / VRP:** Multi-unit, multi-constraint optimization

**Weighted Scoring Models:**
- Geographic proximity
- Unit capabilities (ALS, HazMat, etc.)
- Real-time status (Available, En Route, On Scene)
- Response plan requirements (not just closest unit)

**WALTER Analog:** Agent selection based on capability + availability + workload, not just domain match

---

### 6. Graceful Degradation Patterns

**NG911 Resilience:**
- Geographically diverse ESInets
- Independent power sources
- Redundant data centers (hundreds of miles apart)
- Multi-carrier SIP trunking
- Automatic PRR execution on ECRF/PSAP failure

**Key Mechanism:** If primary PSAP unreachable → automatic diversion to secondary/mutual-aid PSAPs with full payload preservation.

**WALTER Analog:** Agent failure → automatic reroute to backup with full context preservation

---

### 7. Data Standard Evolution

| Standard | Era | Format | Purpose |
|----------|-----|--------|---------|
| EIDD (2.105.1-2017) | Legacy | XML (NIEM) | Inter-CAD incident sharing |
| EIDO (NENA-STA-021.1b) | Modern | JSON (RESTful API) | Full NG911 data conveyance |
| Status Codes (1.116.2-2020) | Current | Data Dictionary | Unit status standardization |
| Incident Types (2.103.2-2019) | Current | Data Dictionary | Event classification |

**WALTER Insight:** Standards evolve from document-centric (XML) to API-centric (JSON). Plan for format migration.

---

### 8. Security: The Ransomware Threat Model

**Attack Vectors:**
- DDoS: +48% YoY on telecom sector
- Ransomware: Doubled in single year
- Insider threats, phishing, zero-days

**Mitigation:**
- Zero-trust architecture
- Multi-factor authentication on CAD
- Offline, immutable GIS/ECRF backups
- NIST Cybersecurity Framework alignment

**WALTER Analog:** Signal integrity + agent authentication + audit trails

---

### 9. IoT Integration: The ADR Pattern

**Problem:** Raw sensor data overwhelming human dispatchers.

**Solution (Additional Data Repository / RapidSOS model):**
1. Device detects emergency → transmits telemetry to cloud clearinghouse
2. Voice call initiated → PSAP queries clearinghouse by phone number
3. Telemetry displayed on CAD dashboard in real-time

**Key:** Sensor data NEVER goes directly to dispatcher. Always mediated through lookup/matching layer.

**WALTER Analog:** Raw market data → curated signal repository → agent dashboard on query

---

## What We Can Ignore

| Emergency-Specific | Why Not Needed |
|-------------------|----------------|
| Z-axis/vertical location | Financial signals don't have physical elevation |
| NFPA 1710/1720 compliance | No regulatory response time requirements |
| Pre-Arrival Instructions (PAIs) | Agents don't need step-by-step coaching |
| TTY/TDD legacy support | No backward compatibility requirements |
| Barometric pressure sensors | No physical sensor integration |

---

## Key Architectural Decisions for WALTER

1. **Policy-based routing override:** Yes — Toscanini rules as PRR equivalent
2. **Cross-domain authentication:** Yes — PEMEA pattern for agent trust
3. **Multi-modal signal envelopes:** Yes — single message, multiple data types
4. **Severity-based prioritization:** Yes — MPDS-style determinant codes
5. **Capability-weighted agent selection:** Yes — beyond simple domain matching
6. **Graceful degradation with context preservation:** Yes — PRR-style failover
7. **API-first design (JSON):** Yes — skip XML/NIEM phase
8. **Signal repository mediation:** Yes — ADR pattern for raw data

---

*Extracted from: PROMPT6_EMERGENCY_DISPATCH_MASTER.md + PROMPT6_EMERGENCY_DISPATCH_COMPASS.md*
*Date: April 6, 2026*
