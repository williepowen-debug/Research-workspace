# Prompt 6 Distilled: Emergency Dispatch — What We Keep

**Source discipline:** 911/NG911 emergency dispatch (NENA i3, MPDS triage, CAD systems)
**Core question answered:** How do you route distress signals to the right responder, triage severity under time pressure, and keep the system running when components fail?

---

## The Big Idea: Policy-Based Routing with Graceful Degradation

Emergency dispatch solves the same problem we have: incoming signals must reach the right agent, fast, with the right priority — and the system can't go down. The key architectural move is separating **default routing** (deterministic, rule-based) from **policy override** (condition-based exception handling).

| Dispatch Component | Function | Our Translation |
|-------------------|----------|-----------------|
| **ECRF** (Emergency Call Routing Function) | Geospatial lookup → which PSAP gets this call | Domain routing table → which agent gets this signal |
| **ESRP** (Emergency Services Routing Proxy) | Policy evaluation, forwarding | WALTER's routing logic |
| **PRF** (Policy Routing Function) | Condition-based diversion when normal routing fails | Safety net overrides, MINIMIZE protocol |

The PRF is the most important concept: when a PSAP goes down or is overloaded, the system doesn't just fail — it automatically diverts calls to backup centers with full context preserved. This is exactly what we need for agent unavailability or overload.

---

## Four Patterns to Implement

### 1. Determinant Code Classification (MPDS)

Medical dispatch uses a structured code: protocol number + severity letter + sub-determinant. 1,828 possible codes, each mapped to a pre-configured response. No ambiguity about what resource to send.

**Our adaptation:**

| MPDS Level | Response | WALTER Precedence | Action |
|-----------|----------|-------------------|--------|
| ECHO | Maximum — closest units regardless of jurisdiction | FLASH | All relevant agents + Will immediately |
| DELTA/CHARLIE | ALS hot response | IMMEDIATE | Primary agent, INFO to chain |
| BRAVO | Hot or cold per local policy | PRIORITY | Primary agent, standard processing |
| ALPHA | BLS cold response | ROUTINE | Archive + COP entry, agent pulls at boot |
| OMEGA | Non-emergency, may divert | Below threshold | Filter — may not even enter archive |

**Key insight from MPDS:** BRAVO is deceptive — alphabetically low but operationally hot. Moderate-seeming signals can require urgent response. WALTER must classify on content, not on first impression.

### 2. Pre-Arrival Context (Zero-Minute Response)

While ambulances are en route, dispatchers provide callers with step-by-step instructions (CPR coaching, tourniquet application). This is "zero-minute response time" — useful work before the full resource arrives.

**Our adaptation:** When WALTER routes an IMMEDIATE signal to an agent, the push notification includes enough context that the agent can begin processing BEFORE reading the full signal:

```
Signal: SIG-W-20260407-005
Precedence: IMMEDIATE
Pre-arrival context: HY OAS widened 28bps single session. This crosses the 25bps safety net threshold.
Your channel (LIQUID) should: assess funding stress implications, check SOFR/repo overnight.
Full signal: AGENTS/WALTER/signals/SIG-W-20260407-005.md
```

The agent knows what to do before reading the full analysis. This is especially valuable when signal files are long.

### 3. Capability-Weighted Agent Selection

CAD systems don't just send the closest unit — they evaluate capability tags, real-time status, estimated response time, and response plan requirements. A HazMat incident needs a HazMat unit, not just the nearest engine.

**Our adaptation:** WALTER's routing table includes agent capability profiles, not just domain assignments:

| Agent | Domain | Capabilities | Current Load |
|-------|--------|-------------|-------------|
| REGINALD | Banking | CRE, earnings, CMBS, funding, NDFI | 🔴 Heavy (earnings season) |
| LIQUID | Credit | HY OAS, spreads, funding, repo | 🟡 Normal |
| BROCK | Private Credit | Gating, NAV, PIK, redemptions | 🟠 Elevated |

A credit stress signal could route to LIQUID (domain match) or REGINALD (if it's bank-specific CRE). The routing decision considers both domain fit AND current load. During earnings week, REGINALD is overloaded — route non-critical credit signals to LIQUID instead.

### 4. Automatic Failover with Context Preservation

When a PSAP goes down, the PRF diverts calls to backup centers. The critical requirement: **full payload preservation**. The backup center receives the same location data, caller info, and multimedia — not a degraded version.

**Our adaptation:** If WALTER routes a signal to an agent that isn't available (no active session, or agent STATUS shows 🔴 overloaded):

1. Route to backup agent (per routing table backup assignments)
2. Full signal preserved — not a summary, the actual signal
3. Original routing logged — so when the primary agent returns, they see what was rerouted
4. Prome notified if no backup available — escalation path

---

## The Alternative Response Pathway

The most innovative pattern in modern dispatch: not every call needs police/fire/EMS. Eugene's CAHOOTS program handles 12% of calls with civilian crisis teams, with only 1.3% requiring police backup. Seattle's nurse navigator redirects 40% of transferred calls away from emergency response entirely.

**Our translation:** Not every signal needs a dedicated agent. Some signals are:
- **Routine monitoring updates** → COP entry only, no agent action
- **Cross-domain context** → INFO to multiple agents, no single owner
- **Will-only** → Goes to Telegram briefing, no agent routing needed
- **Below threshold** → Filtered, logged in kill log, never routed

WALTER should be comfortable NOT routing a signal. The filter's job is to protect agent attention, not to maximize throughput.

---

## Failure Modes That Will Bite Us

### 1. The Intrado Catastrophe (Counter Overflow)
A single software counter hit its maximum, blocking 11 million people from 911 for 6 hours. One variable, catastrophic failure.
**Our risk:** Any single-point-of-failure in WALTER's processing (e.g., a corrupted COP.md, a full disk, a broken signal ID counter).
**Fix:** COP.md is regenerable from the signal archive. Signal IDs use date-based format (no counter overflow possible). The signals/ directory is the authoritative source; COP.md is a derived view.

### 2. The 23 Million Misroute Problem
Legacy 911 routed based on cell tower location, not caller location — routing on the wrong attribute.
**Our risk:** Routing based on signal topic keywords rather than actual content analysis. A signal mentioning "credit" goes to LIQUID when it's really about consumer credit (CARL's domain).
**Fix:** Classification must consider the full signal, not just keywords. The three-gate filter in the Filter Spec addresses this — Gate 1 (relevance), Gate 2 (domain routing), Gate 3 (precedence) are sequential checks on different dimensions.

### 3. PSAP Consolidation Trap
Consolidating 7,485 PSAPs down to 5,748 improved efficiency but created larger single points of failure.
**Our risk:** WALTER as single point of failure for all signal routing. If WALTER's session ends mid-processing, signals are lost.
**Fix:** Signals are written to the archive BEFORE routing. If WALTER crashes, the signal exists in the archive. Next WALTER session (or Prome) can process unrouted signals. The archive is the safety net, not WALTER's session state.

---

## What We Don't Need From Emergency Dispatch

- Geospatial routing, ECRF point-in-polygon, PIDF-LO location format — no geographic dimension
- Z-axis vertical location, barometric pressure, floor-level precision — no physical space
- NFPA 1710/1720 response time standards — no regulatory compliance
- Pre-Arrival Instructions (CPR coaching) — agents don't need clinical scripts
- SIP/TLS/TCP protocol stack — no network protocol layer
- Real-Time Text (RTT), video-to-911, multimedia routing — single format (markdown files)
- AML (Advanced Mobile Location), eCall vehicle telemetry — no device integration
- ShotSpotter/gunshot detection, smart building sensors — no IoT feeds
- Dijkstra/A* pathfinding algorithms — no geographic routing optimization
- EIDD/EIDO/NIEM data standard details — our format spec serves this purpose

---

*Distilled from PROMPT6_EMERGENCY_DISPATCH_MASTER.md + PROMPT6_EMERGENCY_DISPATCH_COMPASS.md + PROMPT6_EXTRACTED_PRINCIPLES.md | April 7, 2026*
