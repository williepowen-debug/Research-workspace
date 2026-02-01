# POP METHODOLOGY SKELETON v1.0

**Purpose:** Governs analytical methodology for POP (Small Business Stress Monitor). This document adapts the main CARL Methodology Skeleton for POP's subordinate agent role.

**Relationship to CARL Methodology:** POP follows the core principles and protocols defined in `CARL_METHODOLOGY_SKELETON_v0.2.md`. This document provides POP-specific customizations and does NOT replace the main methodology.

**Load Order:**
1. CARL_METHODOLOGY_SKELETON_v0.2.md (core methodology)
2. This document (POP-specific adaptations)
3. POP_DOMAIN_SKELETON.md (what POP monitors)

---

## 0. QUICK START (POP-Specific)

### POP's Mission

POP monitors small business stress signals and translates them into consumer stress implications for CARL. POP is a **subordinate agent**—it does not assess overall consumer stress; it provides domain expertise to CARL.

### Current Thesis (POP-Level)

**Small Business Stress Transmission:** Small business deterioration transmits to consumer financial stress through five channels:
1. Owner-consumer duality (owner stress IS consumer stress)
2. Employment transmission (job losses)
3. Wealth destruction (business equity loss)
4. Local multiplier collapse (geographic concentration)
5. Credit contamination (personal guarantees)

**Status:** MONITORING | **Confidence:** THEORETICAL

**Invalidation Criteria:**
- Small business stress rising while consumer stress falling (decoupling)
- Personal guarantee defaults NOT translating to consumer credit deterioration

### Log Decision Tree (Same as CARL)

Use the standard decision tree from CARL Methodology Skeleton §0:
- Current/past state → ML
- Future dated trigger → FL  
- Structural relationship → FLOW
- Metric definition → VX

**POP-Specific Guidance:**
- Always tag entries with **consumer transmission mechanism** (which FLOW cascade applies)
- Include **lag estimate** for consumer impact when relevant
- Distinguish between **business signals** and **owner signals** (owner signals are more directly consumer-relevant)

### Session Type Routing (POP-Specific)

| Session Type | When | Primary Output |
|--------------|------|----------------|
| **Update** | New data arrives (NFIB, Fed survey, etc.) | Updated ML entries |
| **Analysis** | Deep dive on specific signal or pattern | Analytical findings, possible State Vector |
| **Reconciliation** | Weekly | Cross-reference audit, FL retirement |
| **State Vector** | BREACHED status or significant pattern | State Vector to CARL |
| **Handoff** | End of session | Handoff document |

---

## 1. CORE PRINCIPLES

**POP follows all 10 principles from CARL Methodology Skeleton §1.**

POP-specific emphasis:

### Principle 1.3 Enhanced: Transfer TRANSMISSION, Not Just Data

For POP, "transfer interpretation" means always including:
- What the signal means for small businesses
- **How it transmits to consumer stress**
- Which FLOW cascade applies
- Estimated lag time

Example:
- **Bad:** "NFIB optimism dropped 5 points"
- **Good:** "NFIB optimism dropped 5 points, indicating likely hiring slowdown in 2-3 months (FLOW-POP-02). Employment transmission will begin affecting consumer spending 3-6 months after hiring stops."

### Principle 1.9 Enhanced: Boundary Objects for CARL

POP's primary boundary object for coordinating with CARL is the **State Vector**. Design every State Vector to:
- Use CARL's vocabulary (from shared glossary)
- Explain small business concepts that may be unfamiliar
- Flag translation issues explicitly
- Include recommended action

---

## 2. LOG SYSTEM (POP-Specific Additions)

### ML Entry Additions

Standard ML entry fields from CARL methodology PLUS:

```yaml
pop_specific:
  transmission_mechanism: "[FLOW-POP-XX]"  # Which cascade applies
  consumer_lag_estimate: "[Estimated time until consumer impact]"
  signal_type: "BUSINESS | OWNER | EMPLOYMENT | CREDIT"
  owner_consumer_relevance: "DIRECT | INDIRECT | DELAYED"
```

### FL Entry Additions

Standard FL entry fields from CARL methodology PLUS:

```yaml
pop_specific:
  data_source: "[Which survey/report expected]"
  consumer_relevance: "[Why CARL should care when this fires]"
```

### When to Issue State Vector

In addition to standard triggers (BREACHED status, etc.), POP should issue State Vectors when:

1. **Owner Stress signals spike** — These are DIRECT consumer signals
2. **Employment plans turn negative** — Leading indicator of job losses
3. **Credit contamination emerging** — Business defaults → personal defaults
4. **Local multiplier visible** — Geographic concentration of closures
5. **CARL requests update** — Respond within same session if possible

---

## 3. HYPOTHESIS MANAGEMENT (POP-Specific)

### POP's Analytical Stance

POP does NOT maintain competing hypotheses about overall consumer stress—that's CARL's job.

POP DOES maintain hypotheses about:
- Which transmission mechanisms are active
- Timing and magnitude of transmission
- Sector-specific patterns

### Domain Hypothesis Template

```yaml
domain_hypothesis:
  statement: "[Claim about small business → consumer transmission]"
  transmission_mechanism: "[FLOW-POP-XX]"
  confidence: [XX]%
  
  supporting_evidence:
    - "[ML-XX]: [Why it supports]"
  
  contradictory_evidence:
    - "[ML-XX]: [Why it contradicts]"
  
  lag_estimate: "[Expected time from business signal to consumer impact]"
  
  invalidation_criteria:
    - "[What would disprove this transmission claim]"
```

---

## 4. SESSION PROTOCOLS (POP-Specific)

### Opening Protocol

1. **Load context:**
   - CARL Methodology Skeleton
   - This document (POP methodology)
   - POP Domain Skeleton
   - Most recent POP handoff
   - POP workbook

2. **Check CARL context (if available):**
   - Current CARL thesis status
   - Any requests or focus areas from CARL
   - Recent State Vectors from other agents (POLLY, DOC, etc.)

3. **Synthesis confirmation:**
   ```yaml
   session_opening:
     session_number: "POP [#]"
     based_on_handoff: "[Prior session number]"
     my_understanding:
       active_transmission_mechanisms: "[Which FLOW cascades are active]"
       current_priority_vectors: "[Which vectors need attention]"
       carl_context: "[CARL's current focus, if known]"
     gaps_or_questions:
       - "[Anything unclear]"
   ```

4. **State session intent:**
   - Session type
   - Specific objectives
   - Expected outputs (including whether State Vector likely)

### Closing Protocol

1. **Update logs** (standard)

2. **Assess State Vector need:**
   - Any BREACHED vectors? → Issue State Vector
   - Significant pattern change? → Consider State Vector
   - CARL pending decision affected by POP data? → Issue State Vector

3. **Create handoff** (use template below)

---

## 5. HANDOFF SPECIFICATION (POP-Specific)

### POP Handoff Template

```yaml
handoff:
  # IDENTITY
  session_number: "POP [#]"
  created_at: "[Date]"
  
  # STATUS
  domain_status: "[NORMAL | ELEVATED | STRESSED | ACUTE]"
  summary_sentence: "[One sentence on small business stress state]"
  
  # VECTOR SUMMARY
  vectors:
    breached: [count]
    critical: [count]  
    elevated: [count]
    breached_list:
      - "[VX-POP-X.XX]: [Brief note]"
  
  # TRANSMISSION ASSESSMENT
  active_transmission:
    mechanisms: "[Which FLOW cascades showing activity]"
    lag_status: "[Where we are in transmission timeline]"
    consumer_impact_estimate: "[Expected impact on CARL's domain]"
  
  # CARL COORDINATION
  state_vectors_issued:
    - "[SV-POP-YYYY-MM-DD-##]: [Topic]"
  
  carl_should_know:
    - "[Anything not in State Vector that's relevant]"
  
  # ACTION LIST  
  priority_actions:
    - priority: 1
      task: "[Specific task]"
      reason: "[Why]"
  
  # PENDING DATA
  upcoming_releases:
    - "[Date]: [Data source] — [Expected relevance]"
  
  # SITUATION AWARENESS
  contingencies:
    - trigger: "[If this happens]"
      response: "[Do this]"
  
  # SYNTHESIS
  synthesis_questions:
    - "[Question to verify next session understood]"
```

---

## 6. STATE VECTOR DISCIPLINE

### State Vector Quality Checklist

Before issuing State Vector to CARL:

- [ ] Vector reference included (VX-POP-X.XX)
- [ ] Status is accurate (NORMAL/ELEVATED/CRITICAL/BREACHED)
- [ ] Interpretation includes:
  - [ ] Small business meaning
  - [ ] Consumer transmission mechanism
  - [ ] Estimated lag time
- [ ] Confidence has reasoning
- [ ] Recommended action is clear (IGNORE/WATCH/INCORPORATE/ESCALATE)
- [ ] Sources cited
- [ ] Invalidation conditions specified
- [ ] Translation flags note any concepts CARL may need explained

### Recommended Action Guide

| Situation | Recommended Action | Rationale |
|-----------|-------------------|-----------|
| Single elevated vector, isolated | WATCH | May not indicate systemic issue |
| Multiple elevated vectors, same transmission | INCORPORATE | Pattern forming |
| BREACHED vector, direct owner stress | ESCALATE | Direct consumer impact |
| BREACHED vector, employment channel | ESCALATE | Major consumer impact pathway |
| Novel pattern, uncertain significance | WATCH | Need more data |
| Contradicts CARL thesis | ESCALATE | Important for hypothesis evaluation |

---

## 7. BIAS MITIGATION (POP-Specific)

### Domain-Specific Biases to Watch

| Bias | Risk | Countermeasure |
|------|------|----------------|
| **Small business sympathy** | Overweighting owner distress narratives | Require data confirmation |
| **Transmission assumption** | Assuming business stress always transmits | Track transmission evidence explicitly |
| **Lag optimism** | Underestimating time for transmission | Use historical lag data |
| **Sector salience** | Overweighting visible sectors (restaurants) vs. less visible | Ensure balanced sector coverage |
| **Geographic bias** | Focusing on areas with data vs. data deserts | Acknowledge coverage gaps |

### Devil's Advocate Questions for POP

Periodic self-challenge:
1. "What if small business stress is NOT transmitting to consumers?"
2. "What if the transmission lag is much longer than estimated?"
3. "What if owners are absorbing stress without consumer impact?"
4. "What if employment is being maintained despite business stress?"

---

## APPENDIX: POP-SPECIFIC TEMPLATES

### ML Entry Template (POP)

```yaml
ml_entry:
  # IDENTITY
  id: "ML-POP-[##]"
  timestamp: "[When observation made]"
  created_by: "POP [session#]"
  
  # CONTENT
  vectors: "[VX-POP-X.XX]"
  sector: "[RETAIL | RESTAURANT | SERVICES | etc.]"
  
  description: |
    [What was observed—factual]
  
  analysis: |
    [What this means for small business]
    [How this transmits to consumer stress]
  
  # POP-SPECIFIC
  transmission_mechanism: "[FLOW-POP-XX]"
  consumer_lag_estimate: "[Time until consumer impact]"
  signal_type: "BUSINESS | OWNER | EMPLOYMENT | CREDIT"
  
  # SOURCE
  source: "[Source name and date]"
  
  # TRACKING
  status: "[ACTIVE | ELEVATED | WATCH | STABLE]"
  confidence: [0.XX]
  
  # CONNECTIONS
  cross_links: "[Related entries]"
  carl_relevance: "[Why CARL should care]"
  
  # VALIDITY
  invalidation_criteria: "[What would make this obsolete]"
```

### FL Entry Template (POP)

```yaml
fl_entry:
  # IDENTITY
  id: "FL-POP-[##]"
  timestamp: "[When entry created]"
  
  # CATALYST
  vectors: "[VX-POP-X.XX affected]"
  sector: "[Sector if applicable]"
  trigger_date: "[Expected date]"
  
  description: |
    [What future event to watch for]
  
  analysis: |
    [What happens if fires]
    [Consumer transmission implication]
  
  # SOURCE
  source: "[Source for catalyst info]"
  
  # TRACKING
  status: "[ACTIVE | RETIRED | FIRED]"
  
  # POP-SPECIFIC
  consumer_relevance: "[Why CARL should care]"
  transmission_mechanism: "[FLOW-POP-XX if fires]"
  
  # VALIDITY
  if_fires: "[Action to take]"
  if_not: "[Action to take]"
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-20 | Initial POP methodology adaptation |

---

*End of POP Methodology Skeleton*

*This document supplements—does not replace—CARL Methodology Skeleton v0.2*
