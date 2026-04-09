# GIG METHODOLOGY SKELETON v0.2

**Purpose:** Governs analytical methodology, evidence logging, hypothesis management, and session protocols for GIG (Gig Economy Saturation Monitor) within the CARL multi-agent ecosystem.

**Parent Agent:** CARL (Consumer Aggregate Risk Ledger)
**Domain:** Gig Economy Saturation, Platform Labor Markets, Worker Financial Stress
**Core Signal:** Consumer income fragility and gig worker financial stress — "Cracks forming underneath the ice"

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable methodology.*

### About This System

A **session** is one continuous LLM interaction window—from opening until context exhaustion or explicit close. Sessions are numbered sequentially (e.g., GIG 1, GIG 2, GIG 3). At session end, handoff documents transfer context to the next session.

**Storage:** Log entries (ML, FL, FLOW, VX) are maintained in a workbook (GIG_WORKBOOK.xlsx). The workbook and handoff documents are saved locally and uploaded to project files for future sessions.

**Two Skeletons:**
- **Methodology skeleton** (this document): Governs *how* to operate—principles, protocols, templates
- **Domain skeleton** (GIG_DOMAIN_SKELETON.md): Defines *what* GIG monitors—entities, vectors, glossary, thresholds

Load both at session start.

### Current Thesis

**GIG SATURATION THESIS:** The gig economy has shifted from opportunity to trap—simultaneously serving as both symptom (workers flee to gig when traditional employment fails) and cause (saturated platforms compress earnings, accelerating financial stress). Gig worker stress is a LEADING indicator of broader labor market and consumer financial deterioration.

**Confidence:** 65% | **Status:** UNCERTAIN — thesis plausible, evidence accumulating, needs validation

**Invalidation Criteria:**
- Per-worker earnings rise sustainably for 2+ consecutive quarters
- Active worker counts decline while platform revenue grows (healthy equilibrium)
- Multi-apping rates decline significantly (workers don't need multiple platforms)
- Traditional employment recovery absorbs gig-dependent workers

### Log Decision Tree

When you have new information, determine where it belongs:

```
IS IT ABOUT CURRENT/PAST STATE (what IS or WAS true)?
├─ YES → ML (Master Log)
│        Example: "Uber reported 20% decline in driver incentives Q4"
│
└─ NO → DOES IT HAVE A FUTURE DATE (something to watch for)?
        ├─ YES → FL (Future Log)
        │        Example: "DoorDash earnings call Feb 15 — watch driver metrics"
        │        CRITICAL: FL entries RETIRE when date passes
        │
        └─ NO → IS IT A STRUCTURAL RELATIONSHIP (if X, then Y)?
                ├─ YES → FLOW (Cascade Map)
                │        Example: "Earnings compression → multi-apping increase"
                │
                └─ NO → Probably ML, or doesn't need logging
```

### Entry Creation Essentials

Every log entry MUST have:
1. **Unique ID** following format: `[LOG]-[DOMAIN]-[##]`
2. **Timestamp** of when observation was made (not when logged)
3. **Source** with retrieval date
4. **Interpretation** (what it means, not just what it is)
5. **Cross-references** to related entries
6. **Hypothesis tagging** (which hypotheses does this support/contradict?)

### Handoff Creation Essentials

Before ending any session:
1. **Status** — One word: VALIDATED | CONTESTED | UNCERTAIN | INVALIDATED
2. **Summary** — Current phase, key developments, confidence level
3. **Action List** — Priority tasks for next session
4. **Contingencies** — "If X happens, do Y" statements
5. **Key Mental Model** — What matters most and why (interpretation, not just data)

### Session Type Routing

| Session Type | Load Sections | Purpose |
|--------------|---------------|---------|
| Update | 0, 2 | Ingest new data, update logs |
| Analysis | 0, 2, 3 | Deep dive on specific question |
| Reconciliation | 0, 2, 7 | Cross-reference audit, cleanup |
| Devil's Advocate | 0, 3, 7 | Challenge Gig Saturation thesis |
| Handoff | 0, 4, 5 | Explicit knowledge transfer |
| State Vector | 0, 6 | Report to CARL |

### Critical Warnings

**DO NOT:**
- Delete or overwrite existing entries (correct with preserved history)
- Log current observations in FL (FL is for FUTURE triggers only)
- Record confidence scores without reasoning
- End sessions without handoff documentation
- Suppress contradictory evidence
- Report to CARL without documented State Vector

---

## 1. CORE PRINCIPLES

*Universal principles governing all agents. Derived from intelligence analysis, knowledge management, military C2, healthcare handoffs, laboratory practice, and coordination theory.*

### 1.1 Disprove, Don't Confirm
Seek contradictory evidence actively. Surviving hypotheses are those with the LEAST contradictory evidence, not the most supporting evidence. *(Source: Heuer/ACH)*

### 1.2 Externalize Before the Break
Session-local understanding must become explicit documentation before session ends. Assume the next session has zero tacit knowledge of your analytical path. *(Source: Nonaka/SECI, Hospital Handoffs)*

### 1.3 Transfer Interpretation, Not Just Data
Raw facts without assessment impose cognitive load and invite misunderstanding. Always include what the observation MEANS, not just what it IS. *(Source: Hospital Handoffs)*

### 1.4 Immutability Preserves Trust
Never delete, only correct with preserved history. Audit trails enable reconstruction of analytical paths. Errors are information—preserve them. *(Source: Lab Notebooks/ALCOA+)*

### 1.5 Intent Enables Autonomy
Clear thesis + invalidation criteria allows sessions to act appropriately without explicit instruction. When uncertain, act within the framework of stated intent. *(Source: Military C2/Commander's Intent)*

### 1.6 Pre-Commit Contingencies
Define "if X, then Y" responses before they're needed. Pre-commitment reduces decision time under pressure and prevents motivated reasoning in the moment. *(Source: Hospital Handoffs, Military C2)*

### 1.7 Diagnostic Value Over Volume
Evidence consistent with all hypotheses has zero diagnostic value. Prioritize evidence that discriminates between competing hypotheses. More evidence ≠ better analysis. *(Source: Heuer/ACH)*

### 1.8 Structure Reduces Cognitive Load
Predictable formats free mental capacity for actual comprehension. Use templates consistently. Deviate only with explicit justification. *(Source: Hospital Handoffs)*

### 1.9 Boundary Objects Enable Coordination
Shared artifacts (logs, State Vectors, handoffs) allow coordination without requiring consensus on meaning. Maintain common structure while allowing local interpretation. *(Source: Boundary Objects)*

### 1.10 Acknowledge What's Lost
Some tacit knowledge resists externalization. Design for partial transfer, not perfection. Accept that each session starts with degraded context and plan accordingly. *(Source: Nonaka/SECI)*

---

## 2. LOG SYSTEM ARCHITECTURE

*Defines the four-log structure and when to use each. For detailed field definitions, see GIG_DOMAIN_SKELETON.md.*

### Overview

| Log | Question Answered | Persistence | Update Frequency |
|-----|-------------------|-------------|------------------|
| **VX** (Vector Registry) | What are we measuring? | Permanent | Rarely (structural) |
| **ML** (Master Log) | What do we know right now? | Permanent | As observations arrive |
| **FL** (Future Log) | What should we watch for? | Until date passes | As catalysts identified |
| **FLOW** (Cascade Map) | If X breaks, what breaks next? | Until relationship changes | As mechanisms understood |

### 2.1 ML (Master Log)

**Purpose:** Documents current-state observations about gig economy conditions.

**When to Use:**
- Recording platform earnings data, active worker counts
- Documenting driver forum sentiment shifts
- Capturing analyst reports or news developments
- Logging pattern recognition (e.g., "multi-apping mentions increasing")

**ID Format:** `ML-GIG-[##]` (e.g., ML-GIG-01, ML-GIG-02)

**Key Fields:** Timestamp, ID, Vectors, Platform/Segment, Description, Analysis, Source, Status, Confidence, Cross-Links, Invalidation Criteria

**Lifecycle:** ML entries are rarely retired. Update with corrections (preserving history) rather than deleting.

### 2.2 FL (Future Log)

**Purpose:** Tracks dated future triggers—events that COULD change system state when they occur.

**When to Use:**
- Upcoming earnings calls (UBER, LYFT, DASH quarterly reports)
- Scheduled policy changes (minimum wage laws, IC classification rulings)
- Platform announcements or product launches
- Labor action dates (strikes, protests)

**ID Format:** `FL-GIG-[##]` (e.g., FL-GIG-01, FL-GIG-02)

**Critical Discipline:** FL entries MUST be RETIRED when their date passes, regardless of whether the catalyst fired. Outcomes are documented in ML.

**Retirement Protocol:**
1. Date passes
2. Document outcome: Did catalyst fire or not?
3. Create ML entry recording the outcome
4. Mark FL entry as RETIRED with pointer to ML outcome
5. Do NOT delete the original FL entry

### 2.3 FLOW (Cascade Map)

**Purpose:** Documents transmission pathways—how gig economy stress propagates.

**When to Use:**
- Mapping causal chains (e.g., earnings compression → multi-apping → burnout)
- Documenting cross-domain transmission (gig stress → auto loan stress → CARL)
- Identifying feedback loops (saturation doom loop)

**ID Format:** `FLOW-GIG-[##]` (e.g., FLOW-GIG-01, FLOW-GIG-02)

**Pre-defined FLOW entries in Domain Skeleton:**
- FLOW-GIG-01: Saturation Doom Loop
- FLOW-GIG-02: Vehicle Asset Cascade
- FLOW-GIG-03: Platform Rationalization Cascade
- FLOW-GIG-04: Gig-to-CARL Transmission

**Lifecycle:** FLOW entries persist as long as the structural relationship holds. They are NOT date-driven.

### 2.4 VX (Vector Registry)

**Purpose:** Defines the metrics being tracked, their thresholds, and current status.

**ID Format:** `VX-GIG-[#.##]` (e.g., VX-GIG-1.01, VX-GIG-2.03)

**Vector Categories (from Domain Skeleton):**
- VX-GIG-1.xx: Earnings & Compensation
- VX-GIG-2.xx: Supply & Saturation
- VX-GIG-3.xx: Financial Stress
- VX-GIG-4.xx: Platform Health

**Status Values:**
- **NORMAL** — Below threshold, no concern
- **ELEVATED** — Approaching threshold, watch closely
- **CRITICAL** — At or near threshold, high concern
- **BREACHED** — Tripwire crossed, immediate attention required

### FL vs. ML Decision Guide (GIG-Specific)

| Observation Type | Correct Log | Example |
|------------------|-------------|---------|
| Platform earnings report data | ML | "Uber Q4: driver incentives down 15% YoY" |
| Forum sentiment observation | ML | "r/uberdrivers posts increasingly negative" |
| Upcoming earnings call | FL | "DASH Q4 earnings Feb 15" |
| Policy ruling expected | FL | "CA AB5 enforcement ruling expected March" |
| Platform fee structure change | ML | "DoorDash raised take rate to 28%" |
| Causal mechanism | FLOW | "Take rate increase → worker exit → service quality decline" |

---

## 3. HYPOTHESIS MANAGEMENT

*Governs how hypotheses are tracked, evaluated, and revised.*

### 3.1 Primary Thesis Structure

```yaml
primary_thesis:
  name: "Gig Saturation Thesis"
  statement: |
    The gig economy has shifted from opportunity to trap. Gig work is both
    SYMPTOM (workers flee to gig when traditional employment fails) and CAUSE
    (saturated platforms compress earnings, accelerating financial stress).
    Gig worker stress is a LEADING indicator of broader deterioration.
  
  confidence: 65%
  status: UNCERTAIN
  
  key_supporting_evidence:
    - "[ML-GIG-XX]: [Evidence with reasoning]"
  
  key_contradictory_evidence:
    - "[ML-GIG-XX]: [Evidence with reasoning]"
  
  invalidation_criteria:
    - condition: "Per-worker earnings rise sustainably 2+ quarters"
      confidence_impact: "-30%"
    - condition: "Active count declines while revenue grows (equilibrium)"
      confidence_impact: "-25%"
    - condition: "Multi-apping rates decline significantly"
      confidence_impact: "-20%"
    - condition: "Traditional employment absorbs gig-dependent workers"
      confidence_impact: "-25%"
  
  last_evaluated: "[Date]"
```

### 3.2 Competing Hypotheses

**Healthy Flexibility Hypothesis:**
- Statement: "Gig work remains voluntary supplemental income; workers can exit to traditional jobs"
- Current Assessment: "Weakening — evidence of involuntary gig dependence increasing"
- Key evidence needed: Voluntary churn data, exit surveys showing choice not desperation

**Platform Rationalization Hypothesis:**
- Statement: "Platforms will reduce worker supply through deactivation, restoring earnings"
- Current Assessment: "Possible but creates different stress (unemployment)"
- Key evidence needed: Deactivation rates, post-deactivation employment outcomes

### 3.3 Diagnostic Value Tagging

When logging evidence, assess its diagnostic value:

| Diagnostic Value | Meaning | GIG Example |
|------------------|---------|-------------|
| **HIGH** | Discriminates between hypotheses | "Workers exiting gig return to unemployment, not traditional jobs" |
| **MEDIUM** | Somewhat favors one hypothesis | "Earnings declining" |
| **LOW** | Consistent with all hypotheses | "Platform reports growing revenue" |
| **ZERO** | Equally predicted by all | "Gig economy continues to exist" |

---

## 4. SESSION PROTOCOLS

### 4.1 Session Types

**Update Session**
- *Purpose:* Ingest new data from earnings reports, forums, news
- *Trigger:* Quarterly earnings season, significant news, scheduled check-in
- *Output:* Updated ML/FL entries, VX status changes
- *Duration:* Short

**Analysis Session**
- *Purpose:* Deep dive on specific pattern or mechanism
- *Trigger:* Anomaly detected, threshold approached, CARL request
- *Output:* Analytical findings, FLOW updates, hypothesis confidence changes
- *Duration:* Medium-Long

**Reconciliation Session**
- *Purpose:* Cross-reference audit, FL retirement, consistency check
- *Trigger:* Monthly, post-earnings-season
- *Output:* Corrected entries, retired FL items, updated cross-refs
- *Duration:* Medium

**Devil's Advocate Session**
- *Purpose:* Systematically challenge Gig Saturation thesis
- *Trigger:* Monthly, or when confidence >80%
- *Output:* Stress-test results, competing hypothesis updates
- *Duration:* Medium

**Handoff Session**
- *Purpose:* Explicit knowledge transfer focus
- *Trigger:* End of major analytical arc, before extended break
- *Output:* Comprehensive handoff document
- *Duration:* Short-Medium

**State Vector Session**
- *Purpose:* Prepare report for CARL
- *Trigger:* Significant developments, CARL request, monthly minimum
- *Output:* Formal State Vector per §6.2
- *Duration:* Short

### 4.2 Opening Protocol

Every session should begin with:

1. **Load Context**
   - This methodology skeleton
   - GIG_DOMAIN_SKELETON.md
   - Most recent handoff
   - GIG_WORKBOOK (or relevant log entries)

2. **Synthesis Confirmation**
   ```yaml
   session_opening:
     session_number: "GIG [#]"
     based_on_handoff: "[Prior session number]"
     my_understanding:
       thesis_status: "[Current thesis status]"
       current_priority: "[What should be focused on]"
       key_context: "[Critical context carried forward]"
     gaps_or_questions:
       - "[Anything unclear]"
     confirmed: [true | false]
   ```

3. **Session Intent**
   - State session type
   - Identify specific objectives
   - Note any constraints

### 4.3 Closing Protocol

Every session should end with:

1. **Log Updates** — All observations logged, FL retired if needed
2. **Handoff Creation** — Follow template in §5
3. **CARL Notification** — If significant, prepare State Vector

---

## 5. HANDOFF SPECIFICATION

### 5.1 I-PASS Adapted Structure

| Component | GIG Adaptation |
|-----------|----------------|
| **I** — Illness Severity | Thesis Status (one word) |
| **P** — Patient Summary | Current gig economy state, phase, confidence |
| **A** — Action List | Priority tasks for next session |
| **S** — Situation Awareness | Invalidation watch + contingencies |
| **S** — Synthesis by Receiver | Questions for next session |

### 5.2 Required Handoff Fields

```yaml
handoff:
  session_number: "GIG [#]"
  created_at: "[Date]"
  
  # THESIS STATUS
  thesis_status: "[VALIDATED | CONTESTED | UNCERTAIN | INVALIDATED]"
  urgency: "[ROUTINE | ELEVATED | CRITICAL]"
  summary_sentence: "[One sentence on current state]"
  
  # CURRENT STATE
  current_state:
    phase: "[Expansion | Saturation | Compression | Distress]"
    thesis_confidence: [XX]%
    thesis_confidence_reasoning: "[Why this level]"
    key_developments:
      - "[Recent significant observation]"
    vector_summary:
      breached: [count]
      critical: [count]
      elevated: [count]
  
  # ACTION LIST
  priority_actions:
    - priority: 1
      task: "[Specific task]"
      reason: "[Why important]"
  
  # SITUATION AWARENESS
  contingencies:
    - trigger: "[If this happens]"
      response: "[Do this]"
  
  approaching_invalidation:
    - "[Any invalidation criteria getting close]"
  
  # CARL REPORTING
  carl_update_needed: [true | false]
  carl_update_reason: "[Why/why not]"
  
  # SYNTHESIS
  key_mental_model:
    what_matters_most: "[Single most important thing]"
    biggest_uncertainty: "[Primary unknown]"
  
  synthesis_questions:
    - "[Question to verify understanding]"
```

---

## 6. MULTI-AGENT COORDINATION

### 6.1 Reporting Relationship

GIG is a subordinate agent to CARL. GIG monitors gig economy saturation and reports consumer income fragility signals to CARL via State Vectors.

**When to Report to CARL:**
- Any GIG vector moves to BREACHED
- Multiple vectors move to CRITICAL
- New cascade pathway identified affecting consumer stress
- Evidence of significant gig-to-consumer-credit transmission
- Monthly minimum (even if "no significant change")

### 6.2 State Vector Specification (GIG → CARL)

```yaml
state_vector:
  # IDENTITY
  id: "SV-GIG-[YYYY-MM-DD]-[##]"
  from_agent: "GIG"
  to_agent: "CARL"
  timestamp: "[ISO timestamp]"
  
  # SYNTACTIC (shared vocabulary)
  domain: "Gig Economy Saturation"
  primary_metric: "[Most concerning vector]"
  value: "[Current value/status]"
  status: "[NORMAL | ELEVATED | CRITICAL | BREACHED]"
  
  # SEMANTIC (GIG's interpretation)
  interpretation: |
    [What this means for consumer financial stress]
    [How this relates to CARL's thesis]
  
  confidence: [XX]%
  confidence_reasoning: "[Why this confidence]"
  
  translation_flags:
    - "[Areas where meaning may not transfer cleanly]"
    - "[Gig-specific context CARL should know]"
  
  # PRAGMATIC (recommended action)
  recommended_action: "[IGNORE | WATCH | INCORPORATE | ESCALATE]"
  action_rationale: "[Why this recommendation]"
  
  transmission_to_carl:
    vectors_affected: ["[CARL vectors this impacts]"]
    flow_activated: "[Any FLOW-GIG-04 transmission signs]"
    lag_estimate: "[Expected time until CARL vectors show impact]"
  
  # VALIDITY
  sources: ["[Key sources for this report]"]
  next_update: "[When GIG will report again]"
```

### 6.3 Cross-References to CARL

Key CARL vectors GIG should monitor for transmission effects:
- **VX-CARL-1.04** — Subprime Auto 60+ DQ (gig worker vehicle stress)
- **VX-CARL-1.02** — Minimum Payment Rate (gig workers bridging with credit)
- Employment/Income vectors (gig as alternative to traditional employment)

When GIG observes stress that should transmit to these CARL vectors, note in State Vector.

---

## 7. BIAS MITIGATION

### 7.1 Devil's Advocate Protocol

**When to Invoke:** Monthly, or when Gig Saturation thesis confidence >80%

**Process for GIG:**
1. Argue that gig economy IS healthy — workers have options, earnings are sustainable
2. Identify strongest evidence for "Healthy Flexibility" hypothesis
3. Ask: "What would I expect to see if gig work were truly voluntary and sustainable?"
4. Document findings regardless of outcome

### 7.2 Fresh Eyes Protocol

**When to Invoke:** Quarterly

**Process:**
1. Load only VX definitions and raw platform data
2. Do NOT load prior ML entries or interpretations
3. Ask: "What does this data suggest about gig economy health?"
4. Compare to established thesis

### 7.3 GIG-Specific Bias Risks

| Bias Risk | Why GIG is Vulnerable | Countermeasure |
|-----------|----------------------|----------------|
| **Negativity bias** | Forum data skews negative (complaints > praise) | Weight forum sentiment against hard metrics |
| **Platform narrative** | Platforms spin data positively in earnings | Cross-reference with driver-reported data |
| **Anecdote weighting** | Vivid driver stories feel representative | Require statistical corroboration |
| **Confirmation** | Saturation thesis is intuitive/appealing | Active Devil's Advocate on "Healthy Flexibility" |

---

## APPENDIX A: GIG ENTRY TEMPLATES

### A.1 ML Entry Template

```yaml
ml_entry:
  id: "ML-GIG-[##]"
  timestamp: "[When observation made]"
  created_by: "GIG [session #]"
  
  vectors: "[VX-GIG IDs affected]"
  platform: "[UBER | LYFT | DASH | CART | UPWK | FVRR | MULTI | SECTOR]"
  segment: "[Rideshare | Delivery | Freelance | Task | General]"
  
  description: |
    [What was observed — factual]
  
  analysis: |
    [What this means — interpretation]
  
  data_quote: "[Key data point or quote]"
  source: "[Source and date]"
  
  status: "[ACTIVE | ELEVATED | WATCH]"
  confidence: [0.XX]
  
  hypothesis_impact:
    saturation_thesis: "[CONSISTENT | INCONSISTENT | NEUTRAL]"
    diagnostic_value: "[HIGH | MEDIUM | LOW | ZERO]"
  
  cross_links: "[Related entries]"
  carl_relevance: "[How this affects CARL assessment]"
  invalidation_criteria: "[What would make this obsolete]"
```

### A.2 FL Entry Template

```yaml
fl_entry:
  id: "FL-GIG-[##]"
  timestamp: "[When created]"
  created_by: "GIG [session #]"
  
  catalyst: "[What to watch for]"
  trigger_date: "[When]"
  
  vectors: "[VX-GIG IDs affected]"
  platform: "[Platform or SECTOR]"
  
  if_fires: |
    [What happens if catalyst fires]
  
  if_not: |
    [What it means if catalyst doesn't fire]
  
  monitoring: "[How to track]"
  source: "[Source for catalyst info]"
  cross_links: "[Related entries]"
  
  # RETIREMENT (when date passes)
  status: "[ACTIVE | RETIRED]"
  retirement:
    outcome: "[FIRED | DID_NOT_FIRE | PARTIAL]"
    outcome_ml: "[ML-GIG-XX documenting outcome]"
```

---

## APPENDIX B: EARNINGS CALENDAR

*Key dates for GIG monitoring — update each quarter*

### Q4 2025 / Q1 2026 Earnings Season (VERIFIED)

| Company | Ticker | Date | Time | Key Metrics to Watch |
|---------|--------|------|------|---------------------|
| Uber | UBER | **Feb 4, 2026** | 5am PT / 8am ET | Active drivers, incentive spend, take rate |
| Lyft | LYFT | **Feb 11, 2026** | After Close | Active drivers, rides/driver, driver earnings |
| Upwork | UPWK | **Feb 18, 2026** | After Close | Active freelancers, GSV/freelancer |
| DoorDash | DASH | **Feb 18, 2026** | After Close | Dashers, orders/dasher, dasher pay |
| Instacart | CART | **~Feb 20-24, 2026** | After Close (TBC) | Shoppers, orders/shopper |
| Fiverr | FVRR | **Feb 25, 2026** | Before Open | Active sellers, revenue/seller |

*Dates verified Jan 2026. Instacart date estimated based on patterns; confirm closer to date.*

### Other Key Dates

| Event | Date | Relevance |
|-------|------|-----------|
| BLS Employment Report | First Friday monthly | Traditional employment context |
| Gridwise Monthly Report | ~15th monthly | Driver earnings data |

---

## APPENDIX C: CHECKLISTS

### C.1 Session Opening Checklist

- [ ] Loaded GIG methodology skeleton
- [ ] Loaded GIG domain skeleton
- [ ] Loaded most recent handoff
- [ ] Loaded GIG workbook
- [ ] Written synthesis confirmation
- [ ] Identified session type and objectives

### C.2 Session Closing Checklist

- [ ] All new observations logged to ML
- [ ] FL entries checked — retired any past dates
- [ ] Cross-references updated
- [ ] Hypothesis confidence updated if warranted (with reasoning)
- [ ] Handoff created with all required fields
- [ ] Assessed: Does CARL need a State Vector update?

### C.3 State Vector Checklist (before sending to CARL)

- [ ] All three layers included (syntactic, semantic, pragmatic)
- [ ] Interpretation explains GIG → consumer stress transmission
- [ ] CARL vector cross-references included
- [ ] Recommended action justified
- [ ] Confidence reasoning documented

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 0.2 | 2026-01-20 | Initial GIG methodology based on CARL methodology v0.2 |

---

*End of GIG Methodology Skeleton*
