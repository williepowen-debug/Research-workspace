# SAM METHODOLOGY ADAPTATION NOTES

**Purpose:** Documents how SAM (Samurai) agent interprets and adapts the CARL Methodology Skeleton v0.2 for macro/sovereign analysis.

**Created:** 2026-01-20
**Base Methodology:** CARL_METHODOLOGY_SKELETON_v0.2.md

---

## Overview

The CARL Methodology Skeleton was designed for consumer financial stress analysis. SAM operates in a different domain (Japan sovereign, global macro, CLO transmission) with different characteristics:

| Characteristic | CARL (Consumer) | SAM (Macro/Sovereign) |
|----------------|-----------------|----------------------|
| **Data cadence** | Quarterly releases | Real-time markets |
| **Crisis speed** | Weeks to months | Hours to days |
| **Actor count** | Many diffuse consumers | Few large institutions |
| **Thesis structure** | Binary (Front-Loading vs Soft Landing) | Multiple equilibria (5 scenarios) |
| **Coordination** | Internal subordinates | External peer agents |

This document specifies SAM's adaptations to methodology principles.

---

## 1. Hypothesis Management: Scenario Trees vs Binary

### Methodology Standard (§3)

The methodology skeleton assumes binary competing hypotheses:
- Primary thesis with invalidation criteria
- At least one competing hypothesis

### SAM Adaptation

SAM uses a **probability-weighted scenario tree** instead of binary hypotheses. This is appropriate because:

1. **Multiple equilibria are possible in macro**: Japan can land in fundamentally different stable states (soft landing, controlled devaluation, fiscal crisis, etc.) — these aren't competing explanations of the same data but genuinely different future paths.

2. **Scenarios are mutually exclusive**: Unlike hypotheses (which explain the same observations), scenarios describe different future states. Only one will occur.

3. **Probability weighting enables nuance**: Rather than "thesis confidence 88%", SAM can express "32% controlled chaos, 28% panic, 12% soft landing, etc."

### Implementation

```yaml
# Standard methodology format (binary)
primary_thesis:
  statement: "Front-Loading Paradigm"
  confidence: 88%
  competing_hypothesis: "Soft Landing"

# SAM adaptation (scenario tree)
scenario_tree:
  A_soft_landing: 12%
  B_controlled_chaos: 32%
  C_acute_panic: 28%
  D1_austerity: 9%
  D2_monetary_dominance: 8%
  # Remaining probability = mixed/uncertain outcomes
```

### Compliance Notes

- **Invalidation criteria still apply**: Each scenario has conditions that would eliminate it from consideration
- **Diagnostic value still applies**: Evidence is evaluated by how much it shifts scenario probabilities
- **Devil's Advocate still applies**: Periodic sessions should argue for low-probability scenarios

---

## 2. Log System: FL/ML Separation in Real-Time Markets

### Methodology Standard (§2)

- ML = Current/past state observations
- FL = Future-dated catalysts, RETIRED when date passes

### SAM Adaptation

In real-time markets, the FL/ML distinction requires additional nuance:

**FL Entries for SAM:**
- Scheduled events (BOJ meetings, auctions, data releases)
- Political deadlines (elections, coalition votes)
- Regulatory implementation dates (ESR June 2026)

**NOT FL (Goes to ML):**
- Threshold approaches ("30Y JGB approaching 4.00%") — this is current state
- Market conditions ("Auction weakness") — this is current state
- Pattern observations ("Resembles 2022 UK Gilt Crisis") — this is analysis

**Retirement Protocol:**
Event passes → Document outcome in ML → Mark FL as RETIRED with ML pointer

Example:
```yaml
# FL-JPN-062 (created before event)
event: "BOJ Decision Jan 23-24"
expected_impact: "Fork in road"
status: "ACTIVE"

# FL-JPN-062 (after event)
status: "RETIRED"
outcome: "BOJ held rates, signaled April hike"
outcome_documented_in: "ML-JPN-140"
```

---

## 3. Session Types: Adding Crisis Mode

### Methodology Standard (§4)

Five session types: Update, Analysis, Reconciliation, Devil's Advocate, Handoff

### SAM Adaptation

SAM adds a **Crisis** session type for active market stress:

| Session Type | SAM Context | Monitoring Cadence |
|--------------|-------------|-------------------|
| **Update** | Normal operations | Daily/Weekly |
| **Analysis** | Deep dive on specific flow | As needed |
| **Crisis** | Active market stress | HOURLY |
| **Reconciliation** | Cross-reference audit | Weekly |
| **Devil's Advocate** | Challenge scenarios | Monthly |
| **Handoff** | Session transfer | End of session |

**Crisis Session Protocol:**
1. Load skeleton + handoff + real-time data
2. Check all RED/ORANGE thresholds against current values
3. Evaluate four-signal confirmation protocol
4. Update scenario probabilities if evidence warrants
5. Determine if escalation to coordinating agents needed
6. Brief handoff if context nearing exhaustion

**RED CHECK Protocol (Add to UPDATE Sessions):**

Allocate 10 minutes at end of UPDATE sessions for counter-thesis review:

1. **Review Stabilization Signals** (3 min)
   - Check current JGB yields vs. peaks
   - Note any buyer return signals
   - Log to `RED/COUNTER_EVIDENCE_LOG.md`

2. **Assess Soft Landing Probability** (4 min)
   - Has any CH-SAM-01 requirement been met or advanced?
   - Has any requirement been invalidated?
   - Update scenario probability if warranted

3. **Log Counter-Evidence** (3 min)
   - Document evidence supporting counter-thesis
   - Tag ML entry with COUNTER_SIGNAL
   - Note in session handoff

See `C:/Projects/SAM/RED/SAM_COUNTER_THESIS.md` for full framework.

**Trigger for Crisis Mode:**
- Any threshold at RED status
- Any FLOW cascade confirmed active
- Any coordinating agent signals systemic stress
- Market dislocation (auction failures, circuit breakers, etc.)

---

## 4. Thresholds: Color-Coded Escalation

### Methodology Standard

The methodology skeleton uses status values: NORMAL | ELEVATED | CRITICAL | BREACHED

### SAM Adaptation

SAM uses color-coded thresholds with explicit escalation protocols:

| Color | Meaning | Action |
|-------|---------|--------|
| 🟢 GREEN | Normal | Periodic monitoring |
| 🟡 YELLOW | Watch | Daily monitoring, prepare contingencies |
| 🟠 ORANGE | Alert | 24-hour watch, alert coordinating agents |
| 🔴 RED | Critical | Continuous monitoring, crisis protocols |

**Mapping to Methodology:**
- GREEN = NORMAL
- YELLOW = ELEVATED
- ORANGE = CRITICAL
- RED = BREACHED

---

## 5. Multi-Agent Coordination: Peer Model

### Methodology Standard (§6)

The methodology assumes hierarchical coordination (CARL as parent, subordinate agents report via State Vectors).

### SAM Adaptation

SAM operates in a **peer coordination model** with other domain agents:

| Agent | Relationship | Data Flow |
|-------|--------------|-----------|
| **LIQUID** | Peer | Bidirectional (funding ↔ Japan flows) |
| **REGINALD** | Peer | Bidirectional (bank stress ↔ CLO contagion) |
| **MASTER** | Coordinator | SAM reports scenarios; MASTER synthesizes |
| **OTTO** | Peer | Limited (CLO overlap only) |

**State Vector Exchange:**

SAM sends to LIQUID:
```yaml
state_vector:
  from_agent: "SAM"
  to_agent: "LIQUID"
  domain: "Japan Sovereign"
  key_metric: "Japan repatriation pressure"
  status: "CRITICAL"
  interpretation: "GPIF/Lifer rotation may trigger $60-100B UST selling"
  recommended_action: "WATCH for UST auction weakness, SOFR spike"
```

LIQUID sends to SAM:
```yaml
state_vector:
  from_agent: "LIQUID"
  to_agent: "SAM"
  domain: "US Funding"
  key_metric: "SOFR-IORB spread"
  status: "NORMAL"
  interpretation: "Funding markets stable despite RRP depletion"
  recommended_action: "Continue monitoring; no immediate stress"
```

---

## 6. Confidence Scoring: Decomposed Dimensions

### Methodology Standard (§3.3)

Confidence is a single percentage with reasoning.

### SAM Adaptation

SAM decomposes confidence into three dimensions:

| Dimension | Meaning | Example |
|-----------|---------|---------|
| **Pattern** | Confidence the mechanism is correctly identified | "97% - Impossible Trilemma architecture confirmed" |
| **Timing** | Confidence in when the event occurs | "82% - Jan 23-27 window is critical" |
| **Magnitude** | Confidence in the severity | "90% - Major market impact likely" |

This allows more precise communication:
- "Pattern 97%, Timing 82%, Magnitude 90%" is more actionable than "Confidence 90%"
- Different dimensions may move independently (pattern confirmed but timing uncertain)

**Reporting Format:**
```yaml
thesis_confidence:
  pattern: "97%"
  timing: "82%"
  magnitude: "90%"
  reasoning: |
    Pattern: JGB crisis confirms trilemma mechanism
    Timing: BOJ Jan 23 is clear catalyst window
    Magnitude: 30Y ATH demonstrates market dysfunction
```

---

## 7. Flows vs Cascades

### Methodology Standard

The methodology references "FLOW" entries for cascade maps.

### SAM Adaptation

SAM distinguishes between:

**FLOW entries:** Named cascade pathways (structural relationships)
- FLOW-JPN-1.06: Fiscal Doom Loop
- FLOW-JPN-3.01: CLO Nuclear Transmission

**Cascade status:** Real-time activation state
- LATENT: Pathway exists but not active
- ARMED: Trigger approaching
- ACTIVE: Cascade in progress
- EXHAUSTED: Cascade completed or invalidated

**Example:**
```yaml
flow: "FLOW-JPN-3.01"
name: "CLO Nuclear Transmission"
status: "ARMED"  # Not yet active, but trigger (CLO 180bps) approaching
distance_to_trigger: "25bps"
```

---

## 8. Handoff Structure: I-PASS Adapted

### Methodology Standard (§5)

I-PASS adapted handoff with thesis status, current state, action list, situation awareness, synthesis.

### SAM Adaptation

SAM handoff follows I-PASS structure with additions:

| Component | Standard | SAM Addition |
|-----------|----------|--------------|
| **I** - Status | Thesis status | + Scenario probabilities with trends |
| **P** - Summary | Current state | + Active flows status |
| **A** - Actions | Priority tasks | + Monitoring schedule (hourly/daily/weekly) |
| **S** - Awareness | Contingencies | + Four-signal confirmation status |
| **S** - Synthesis | Mental model | + Cross-agent coordination status |

---

## 9. Diagnostic Value in Macro Context

### Methodology Standard (§3.4)

Evidence tagged as HIGH/MEDIUM/LOW/ZERO based on how well it discriminates between hypotheses.

### SAM Adaptation

In scenario tree context, diagnostic value measures **probability shift**:

| Diagnostic Value | Definition | Example |
|------------------|------------|---------|
| **HIGH** | Shifts one or more scenarios by >10% | "20Y auction failure" — D scenarios +10% |
| **MEDIUM** | Shifts scenarios by 5-10% | "30Y approaches 4.00%" — C +5% |
| **LOW** | Shifts scenarios by <5% | "Political rhetoric continues" |
| **ZERO** | Consistent with all scenarios | "Market volatility elevated" |

---

## 10. Time Sensitivity

### Methodology Standard

Assumes sessions can be spaced by days or weeks.

### SAM Adaptation

During crisis periods, SAM requires compressed operations:

| Phase | Session Frequency | Handoff Cadence |
|-------|------------------|-----------------|
| **Normal** | 1-2x per week | Weekly |
| **Elevated** | Daily | Daily |
| **Crisis** | Multiple per day | Each session |
| **Emergency** | Continuous | Rolling updates |

**Context Management:**
- During crisis, load minimal context (§0 Quick Start + key thresholds only)
- Full skeleton load only for Analysis or Handoff sessions
- Crisis sessions focus on thresholds, flows, and four-signal protocol

---

## Summary: SAM Methodology Compliance

| Methodology Section | SAM Compliance | Adaptation |
|--------------------|----------------|------------|
| §1 Core Principles | ✅ Full | None |
| §2 Log System | ✅ Full | Additional FL/ML guidance for real-time |
| §3 Hypothesis Management | 🔄 Adapted | Scenario tree vs binary |
| §4 Session Protocols | 🔄 Adapted | Crisis session type added |
| §5 Handoff Specification | ✅ Full | Enhanced with scenario probabilities |
| §6 Multi-Agent Coordination | 🔄 Adapted | Peer model vs hierarchical |
| §7 Bias Mitigation | ✅ Full | None |

**Legend:** ✅ Full compliance | 🔄 Adapted with documented rationale

---

## Rationale for Adaptations

All adaptations are justified by domain requirements:

1. **Scenario trees** are standard in macro analysis (IMF, central banks use this approach)
2. **Decomposed confidence** enables better communication of epistemic state
3. **Peer coordination** reflects the actual multi-domain structure
4. **Crisis mode** is necessary for real-time market monitoring
5. **Color-coded thresholds** improve rapid assessment during stress

None of the adaptations violate core methodology principles:
- Disprove, Don't Confirm ✅ (applies to each scenario)
- Externalize Before the Break ✅ (enhanced handoff structure)
- Immutability Preserves Trust ✅ (unchanged)
- Intent Enables Autonomy ✅ (scenario framework provides intent)

---

*End of SAM Methodology Adaptation Notes*
