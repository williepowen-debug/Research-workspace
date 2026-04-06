# Air Traffic Control Systems — Master Extraction (Prompt 3)

**Sources:** LLM research on ICAO Doc 4444, FAA Order 7110.65, EUROCONTROL Guidelines  
**Date:** 2026-04-06  
**Status:** Comprehensive reference for real-time state management and agent coordination

---

## 1. Core Architectural Principle: Spatial State Externalization

**Flight Strip System:** A physical/electronic card encoding full current and planned state of a single flight.

**Triple Function:**
1. **Legal record** — audit trail of clearances issued
2. **Cognitive offload** — working memory externalized
3. **Shared state** — visible to all controllers in sector

**Financial Translation:** Every signal gets a "strip" — shared state representation visible to all agents.

---

## 2. Flight Strip Data Architecture (24 Fields)

| Block | Field | Financial Analog |
|-------|-------|------------------|
| 1 | Mode 3/A beacon code | Signal ID / hash |
| 2 | Aircraft count + type | Signal category (macro, single-name, risk) |
| 3 | Aircraft identification | Signal name/ticker |
| 4 | Reduced separation flags | Special handling indicators |
| 5 | Controlling sector number | **Current "owner" agent** |
| 6 | Filed airspeed | Expected processing time |
| 7 | Reported flight level | Current status (↑ climbing, ↓ descending) |
| 8 | Cleared flight level | Target state |
| 9 | Requested flight level | Original intent |
| 10-13 | Position + time reporting | State history, timestamps |
| 14-17 | Future positions | Projected state, planning horizon |
| 18-19 | Departure/Destination | Source system, target action |
| 20 | Indicators/toggles | Route display, annotations |
| 21 | Coordination indicators | **Inter-agent communication flags** |
| 22 | Annotations | Free-form notes |
| 23 | Clearance restrictions | Conditional actions |
| 24 | Strip number / total | Queue position |

**Key Principle:** Schema adapted to operational context while maintaining core field invariance.

---

## 3. Visual Layout Principles

**Spatial Encoding:**
- **Vertical position** = priority order (altitude in ATC)
- **Bay assignment** = phase-of-flight categorization
- **Holder color** = flight category (green departures, blue arrivals)
- **Physical manipulation** = state transition signal
- **Strip annotations** = standardized micro-language

**Scanning Pattern:** Cyclic sweeps from top to bottom — matches temporal order of required actions.

**Financial Translation:**
- Vertical position = urgency (FLASH at top, ROUTINE at bottom)
- Bay = processing phase (intake, analysis, action, complete)
- Color = signal type (credit, labor, energy, etc.)
- Manipulation = moving strip = state change

---

## 4. Conflict Detection: Three-Zone Model

| Zone | Name | Action | Financial Equivalent |
|------|------|--------|---------------------|
| 1 | **No Problem Area** | Passive monitoring | Green — no action needed |
| 2 | **Possible Problem Area** | Track closely | Yellow — watch, no action yet |
| 3 | **Do Something Area** | Trajectory modification | Red — intervention required |

**STCA (Short-Term Conflict Alert):**
- Look-ahead: 2 minutes (optimal: 60 seconds)
- Warning: 50-90 seconds before violation
- **No resolution suggestion** — identifies conflict, doesn't prescribe fix
- Nuisance alert rate is first-class constraint

**NASA Finding:** Controllers respond to alerts only **56% of the time** — alert predictive value and nuisance rate are coupled.

**Financial Translation:**
- 2-minute look-ahead for signal conflicts
- Alert when signals contradict or overlap
- Don't auto-resolve — flag for agent attention
- Calibrate to minimize false alerts

---

## 5. ATC Message Taxonomy

| Type | Authority | Requires Readback | Financial Equivalent |
|------|-----------|-------------------|---------------------|
| **Clearance** | Legal permission, creates accountability | **Yes** | Position entry, trade execution |
| **Instruction** | Directive to perform maneuver | **Yes** | Agent task assignment |
| **Advisory/Information** | Non-directive, "EXPECT" | No | Market data, context |
| **Request** | ATC requesting info | No | Agent query |

**Conditional Clearance Format (4 parts):**
1. Identification
2. The condition
3. The clearance
4. Brief reiteration of condition

**Financial Translation:** Conditional orders must include condition, action, and condition restatement.

---

## 6. Handoff Protocols: Agent-to-Agent State Transfer

### ICAO Four-Stage Transfer Dialogue

| Stage | Name | Description | Financial Equivalent |
|-------|------|-------------|---------------------|
| **1** | **Notification** | T-ATCU notifies A-ATCU of flight | Signal arrives in inbox |
| **2** | **Coordination** | Propose conditions (level, speed, heading) | Negotiate handoff parameters |
| **3** | **Acceptance** | A-ATCU accepts or counter-proposes | Accept or negotiate handoff |
| **4** | **Transfer** | Responsibility shifts at Transfer Point | Agent assumes ownership |

**Silent Transfer of Control (STOC):**
- No verbal coordination needed when:
  - Updated flight plan correlated in both systems
  - Aircraft identified
  - Separation ≥ minimum
  - Instant voice comms available as fallback

**Critical Rule:** Once handoff initiated, neither controller may alter flight path without approval until Transfer Point passed.

### Position-to-Position Handover (HOTO)

**Core Principles:**
- Handover only in "clean" situations (no active emergency)
- Relieving controller arrives early; relieved stays until SA confirmed
- Checklist prevents omissions
- No handover during sector configuration change

**Information Package:**
- Current traffic situation
- Pending conflicts and planned resolutions
- Special conditions (weather, equipment, abnormal procedures)
- Coordination in progress
- Special handling requirements

**Rotation Types (Risk Ranked):**
| Type | Risk |
|------|------|
| New-to-Hot-to-Cold | Medium |
| New-to-Cold-to-Hot | Medium |
| **Two-controller swap** | **Highest** — no continuity |

**Financial Translation:**
- Handoff only when signal in stable state
- Outgoing agent briefs incoming on context
- Checklist for handoff completeness
- Avoid simultaneous agent replacement

---

## 7. Sterile Cockpit Rule: Distraction Architecture

**FAR 121.542:** No non-essential activities during critical phases (taxi, takeoff, landing, below 10,000 ft).

**ATC Analog:** "Sterile sector" during high-workload phases — social conversation halts, non-operational comms deferred.

**Handover Protocol:** Only in "clean situations" — don't transfer during high cognitive demand.

**Financial Translation:**
- Identify high-cognitive-load processing windows
- Suppress non-critical interrupts during them
- Categorize all messages by urgency before delivery
- Build interrupt deferral as explicit feature

---

## 8. Emergency Override Architecture

### Two-Level Emergency Hierarchy

| Level | Call | Priority | Use Case |
|-------|------|----------|----------|
| **MAYDAY** | "Mayday Mayday Mayday" | **Absolute priority** — all other traffic yields | Grave and imminent danger |
| **PAN-PAN** | "Pan-Pan Pan-Pan Pan-Pan" | Priority over all except distress | Urgent but no immediate danger |

**MAYDAY Actions:**
1. Acknowledge: "[Callsign] ROGER MAYDAY at [time]Z"
2. Emergency aircraft receives absolute priority
3. Clear airspace ahead
4. Notify supervisor and adjacent sectors
5. Coordinate emergency services

**Dynamic Status:** Can upgrade (PAN-PAN → MAYDAY) or downgrade (MAYDAY → PAN-PAN) as situation evolves.

**Financial Translation:**
- Two-level emergency: System-critical vs. Urgent
- Emergency signals preempt all normal traffic
- Explicit acknowledgment format
- Support real-time upgrade/downgrade

---

## 9. Sweatbox Training: Simulation-Driven Learning

**What:** Closed-loop simulation where instructor controls aircraft according to trainee instructions.

**Tests:**
- Traffic picture construction
- Sequence management
- Conflict anticipation
- Recovery under workload
- Instruction precision
- Spatial awareness

**Vector Drills:** Constrained optimization puzzles — "chess puzzles" with specific scenario geometry.

**Pause and Recover:** Freezing scenario time to assess complex situations before continuing.

**Financial Translation:**
- Scenario-based agent training
- Constrained optimization drills
- Pause mechanism when complexity exceeds safe processing

---

## 10. Cognitive Load Architecture

### Endsley's Three-Level SA Model

| Level | Name | Description |
|-------|------|-------------|
| **1** | **Perception** | Extract raw state (positions, altitudes, speeds) |
| **2** | **Comprehension** | Integrate into coherent "traffic picture" |
| **3** | **Projection** | Extrapolate forward to anticipate conflicts |

**Controller Mental Model:** Dynamic, visuo-spatial, four-dimensional (lateral, vertical, speed, time).

### Workload-Performance Relationship

**Curvilinear:** Performance degrades at both extremes — too low (vigilance failure) and too high (overload).

**Goal:** Keep agents operating in productive mid-range.

### Cognitive Load Management Strategies

| Strategy | Description | Financial Analog |
|----------|-------------|------------------|
| **Cognitive externalization** | Strip management encodes state | Persistent state store; write-through caching |
| **Chunking** | Group aircraft into flows | Batch processing; topic aggregation |
| **Anticipatory planning** | Scan 15-20 min ahead | Look-ahead probes; predictive detection |
| **Task delegation** | Executive handles comms; planner handles data | Role separation; agent specialization |
| **Task shedding** | Defer lower-priority under load | Priority-based queue with service tiers |
| **Standardized phraseology** | Reduces linguistic overhead | Typed message schemas; structured formats |
| **Position scanning pattern** | Cyclic, predictable scan | Round-robin polling; no-starvation scheduler |

### Planner-Executive Role Division

| Role | Responsibility |
|------|---------------|
| **Executive (R-side)** | Radio communications, issues clearances — tactical |
| **Planner (D-side)** | Flight data, coordination, thinks 10-20 min ahead — strategic |

**Principle:** Parallel processing of tactical and strategic tasks requires separated resources.

**Financial Translation:**
- Separate agents for immediate execution vs. strategic planning
- Tactical agent: handles trades, alerts
- Strategic agent: research, synthesis, forecasting

---

## 11. Integration with Previous Prompts

### ESI Triage (Prompt 1) + ATC

| ESI | ATC | Combined |
|-----|-----|----------|
| 5-level triage | 3-zone conflict model | **Zone-based triage:** No Problem / Monitor / Act |
| Decision Point D (vital signs) | STCA alerts | **Automated safety net** with override capability |
| Resource prediction | Strip data fields | **State encoding** with resource estimation |
| Fast-track bypass | Bay assignment | **Spatial routing** by phase and priority |

### Military Messaging (Prompt 2) + ATC

| Military | ATC | Combined |
|----------|-----|----------|
| Precedence levels | Strip priority order | **Vertical position = precedence** |
| Dual precedence (action/info) | Executive/Planner roles | **Primary/secondary agent distinction** |
| Handoff protocols | 4-stage transfer dialogue | **Standardized agent handoff** |
| Emergency override | MAYDAY/PAN-PAN | **Two-level emergency with dynamic status** |
| Graduated degradation | Sterile sector | **Protected processing windows** |

---

## 12. Recommended Combined Architecture

### Signal "Flight Strip" Schema

```
SIGNAL STRIP FIELDS:
├── Identity
│   ├── Signal ID (hash)
│   ├── Name/ticker
│   └── Category (macro, single-name, risk, etc.)
├── State
│   ├── Current status (intake, analysis, action, complete)
│   ├── Owner agent (controlling sector)
│   └── History (timestamped state transitions)
├── Planning
│   ├── Target state
│   ├── Projected timeline
│   └── Dependencies
├── Coordination
│   ├── Inter-agent flags
│   ├── Handoff status
│   └── Special handling indicators
└── Metadata
    ├── Source system
    ├── Precedence level
    ├── Sensitivity classification
    └── Annotations
```

### Three-Zone Alert Model

| Zone | Color | Action | Example |
|------|-------|--------|---------|
| **No Problem** | Green | Passive monitoring | Routine market data |
| **Possible Problem** | Yellow | Track closely | Threshold approaching |
| **Do Something** | Red | Intervention required | Threshold breached, conflict detected |

### Four-Stage Agent Handoff

1. **Notification** — Signal arrives, potential receivers alerted
2. **Coordination** — Negotiate handoff parameters
3. **Acceptance** — Receiving agent accepts responsibility
4. **Transfer** — Ownership shifts at defined point

### Sterile Processing Windows

- Identify high-cognitive-load phases
- Suppress non-critical interrupts
- Explicit interrupt deferral mechanism
- Handoff only in "clean" situations

### Emergency Hierarchy

| Level | Trigger | Response |
|-------|---------|----------|
| **MAYDAY** | System-critical threat | Absolute priority, all resources |
| **PAN-PAN** | Urgent but not immediate | Priority over routine, not over MAYDAY |

---

## 13. Implementation Checklist

- [ ] Define signal strip schema (24 fields)
- [ ] Implement spatial board layout (vertical = precedence, bays = phase)
- [ ] Build three-zone alert system (green/yellow/red)
- [ ] Calibrate look-ahead time (2 minutes optimal)
- [ ] Implement four-stage handoff protocol
- [ ] Create silent handoff conditions
- [ ] Build handover checklist
- [ ] Implement sterile processing windows
- [ ] Create two-level emergency hierarchy
- [ ] Build dynamic status upgrade/downgrade
- [ ] Implement cognitive externalization (persistent state)
- [ ] Create Planner/Executive role separation
- [ ] Build task shedding mechanism
- [ ] Implement standardized message schemas
- [ ] Create round-robin scanning pattern

---

## 14. Key Metrics to Track

| Metric | ATC Benchmark | Our Target |
|--------|--------------|------------|
| Conflict alert response rate | 56% (NASA) | >80% (higher trust through calibration) |
| Look-ahead time | 2 minutes | 2-5 minutes (financial context) |
| Handoff completion time | Seconds | <1 minute |
| Sterile window violations | — | <1% |
| Emergency acknowledgment time | Immediate | <30 seconds |
| Cognitive load (self-reported) | Mid-range optimal | Keep in productive band |

---

## References

- ICAO Doc 4444 (PANS-ATM), 16th Ed.
- FAA Order JO 7110.65
- EUROCONTROL Coordination & Transfer of Control Guidelines (Ed. 2.0, 2023)
- EUROCONTROL STCA Guidelines
- NASA TM-20120016737 (ATCAM)
- NASA Cognitive Model of ATC
- FAR 121.542 (Sterile Cockpit)
- Endsley's Situation Awareness Theory

---

**Next Steps:**
1. Review against Prompts 4-7 (Pub-Sub, Intel Community, Emergency Dispatch, Scientific Teams)
2. Draft unified architecture document combining all domains
3. Prototype signal strip system with handoff protocols
