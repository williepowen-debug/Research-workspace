# POLLY METHODOLOGY SKELETON v0.2

**Purpose:** Governs analytical methodology, evidence logging, hypothesis management, and session protocols for POLLY (Insurance Stress Monitor) within the CARL multi-agent ecosystem.

**Parent Agent:** CARL (Consumer Aggregate Risk Ledger)
**Domain:** Insurance Stress, P&C Markets, Health Coverage, Consumer Protection Gaps
**Core Signal:** Consumer financial vulnerability through insurance stress — "The safety net fraying"

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable methodology.*

### About This System

A **session** is one continuous LLM interaction window—from opening until context exhaustion or explicit close. Sessions are numbered sequentially (e.g., POLLY 1, POLLY 2, POLLY 3). At session end, handoff documents transfer context to the next session.

**Storage:** Log entries (ML, FL, FLOW, VX) are maintained in a workbook (POLLY_WORKBOOK.xlsx). The workbook and handoff documents are saved locally and uploaded to project files for future sessions.

**Two Skeletons:**
- **Methodology skeleton** (this document): Governs *how* to operate—principles, protocols, templates
- **Domain skeleton** (POLLY_DOMAIN_SKELETON.md): Defines *what* POLLY monitors—entities, vectors, glossary, thresholds

Load both at session start.

### Current Thesis

**INSURANCE STRESS THESIS:** Insurance is both INDICATOR and AMPLIFIER of consumer financial stress. As indicator: when consumers can't afford premiums or reduce coverage, it signals strain not yet visible in credit metrics. As amplifier: underinsured consumers are one incident away from financial catastrophe. The insurance market faces unprecedented pressure (climate, medical costs, inflation), transmitting directly to consumer vulnerability.

**Confidence:** 65% | **Status:** UNCERTAIN — thesis logically sound, multiple confirming signals

**Invalidation Criteria:**
- Premium increases moderate to below income growth for 2+ quarters
- Policy lapse rates decline while coverage levels increase
- Carrier exits reverse; capacity returns to stressed markets
- Health coverage rates improve across income segments

### Log Decision Tree

When you have new information, determine where it belongs:

```
IS IT ABOUT CURRENT/PAST STATE (what IS or WAS true)?
├─ YES → ML (Master Log)
│        Example: "FL Citizens enrollment hit 1.4 million policies"
│
└─ NO → DOES IT HAVE A FUTURE DATE (something to watch for)?
        ├─ YES → FL (Future Log)
        │        Example: "Hurricane season begins June 1"
        │        CRITICAL: FL entries RETIRE when date passes
        │
        └─ NO → IS IT A STRUCTURAL RELATIONSHIP (if X, then Y)?
                ├─ YES → FLOW (Cascade Map)
                │        Example: "Premium increase → coverage reduction → protection gap"
                │
                └─ NO → Probably ML, or doesn't need logging
```

### Entry Creation Essentials

Every log entry MUST have:
1. **Unique ID** following format: `[LOG]-POLLY-[##]`
2. **Timestamp** of when observation was made (not when logged)
3. **Source** with retrieval date
4. **Interpretation** (what it means, not just what it is)
5. **Cross-references** to related entries
6. **Hypothesis tagging** (which hypotheses does this support/contradict?)
7. **Geographic scope** (national, state-specific, regional)

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
| Devil's Advocate | 0, 3, 7 | Challenge Insurance Stress thesis |
| Handoff | 0, 4, 5 | Explicit knowledge transfer |
| State Vector | 0, 6 | Report to CARL |
| Regional Focus | 0, 2 | Deep dive on FL, CA, or other priority state |

### Critical Warnings

**DO NOT:**
- Delete or overwrite existing entries (correct with preserved history)
- Log current observations in FL (FL is for FUTURE triggers only)
- Record confidence scores without reasoning
- End sessions without handoff documentation
- Suppress contradictory evidence
- Ignore geographic specificity (national averages can mask regional crises)
- Report to CARL without noting regional concentrations

### Domain-Specific Caution: Regional Variation

Insurance markets are highly localized. Always:
- Note geographic scope of data
- Distinguish national trends from regional crises
- Track priority states separately (FL, CA, LA, TX)
- Remember: national stability can mask regional catastrophe

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

*Defines the four-log structure and when to use each. For detailed field definitions, see POLLY_DOMAIN_SKELETON.md.*

### Overview

| Log | Question Answered | Persistence | Update Frequency |
|-----|-------------------|-------------|------------------|
| **VX** (Vector Registry) | What are we measuring? | Permanent | Rarely (structural) |
| **ML** (Master Log) | What do we know right now? | Permanent | As observations arrive |
| **FL** (Future Log) | What should we watch for? | Until date passes | As catalysts identified |
| **FLOW** (Cascade Map) | If X breaks, what breaks next? | Until relationship changes | As mechanisms understood |

### 2.1 ML (Master Log)

**Purpose:** Documents current-state observations about insurance market conditions.

**When to Use:**
- Recording premium change data
- Documenting carrier market exits or non-renewal announcements
- Capturing regulatory actions or rate filings
- Logging coverage gap evidence

**ID Format:** `ML-POLLY-[##]` (e.g., ML-POLLY-01, ML-POLLY-02)

**Key Fields:** Timestamp, ID, Vectors, Segment, Geography, Description, Analysis, Source, Status, Confidence, Cross-Links, Invalidation Criteria

**Special Field: Geography**
Every ML entry should note geographic scope:
- `NATIONAL` — US-wide data
- `[STATE]` — State-specific (e.g., FL, CA)
- `REGIONAL` — Multi-state region
- `LOCAL` — Sub-state geography

### 2.2 FL (Future Log)

**Purpose:** Tracks dated future triggers—events that COULD change system state when they occur.

**When to Use:**
- Upcoming carrier earnings
- Rate filing decisions expected
- Regulatory deadlines
- Hurricane/catastrophe season dates
- Policy change effective dates (ACA, Medicaid)

**ID Format:** `FL-POLLY-[##]` (e.g., FL-POLLY-01, FL-POLLY-02)

**Critical Discipline:** FL entries MUST be RETIRED when their date passes, regardless of whether the catalyst fired. Outcomes are documented in ML.

### 2.3 FLOW (Cascade Map)

**Purpose:** Documents transmission pathways—how insurance stress propagates.

**When to Use:**
- Mapping causal chains (e.g., premium spike → coverage reduction → protection gap)
- Documenting transmission to CARL (insurance stress → credit stress)
- Identifying regional cascade patterns

**ID Format:** `FLOW-POLLY-[##]` (e.g., FLOW-POLLY-01, FLOW-POLLY-02)

**Pre-defined FLOW entries in Domain Skeleton:**
- FLOW-POLLY-01: Premium Affordability Cascade
- FLOW-POLLY-02: Coverage Gap Cascade
- FLOW-POLLY-03: Market Failure Cascade
- FLOW-POLLY-04: Health Coverage Cascade
- FLOW-POLLY-05: Polly-to-CARL Transmission

### 2.4 VX (Vector Registry)

**Purpose:** Defines the metrics being tracked, their thresholds, and current status.

**ID Format:** `VX-POLLY-[#.##]` (e.g., VX-POLLY-1.01, VX-POLLY-3.02)

**Vector Categories (from Domain Skeleton):**
- VX-POLLY-1.xx: Homeowners Insurance
- VX-POLLY-2.xx: Auto Insurance
- VX-POLLY-3.xx: Health Insurance
- VX-POLLY-4.xx: Market Stress

**Status Values:**
- **NORMAL** — Below threshold, no concern
- **ELEVATED** — Approaching threshold, watch closely
- **CRITICAL** — At or near threshold, high concern
- **BREACHED** — Tripwire crossed, immediate attention required

### FL vs. ML Decision Guide (POLLY-Specific)

| Observation Type | Correct Log | Example |
|------------------|-------------|---------|
| Premium increase data released | ML | "Auto insurance CPI up 22% YoY" |
| Carrier announces market exit | ML | "State Farm stops new CA homeowners" |
| Hurricane season start | FL | "Atlantic hurricane season begins June 1" |
| Rate filing decision expected | FL | "CA DOI ruling on Allstate filing expected March" |
| Carrier earnings upcoming | FL | "Allstate Q4 earnings Jan 31" |
| Causal mechanism | FLOW | "Market exit → last resort growth → regional stress" |

---

## 3. HYPOTHESIS MANAGEMENT

*Governs how hypotheses are tracked, evaluated, and revised.*

### 3.1 Primary Thesis Structure

```yaml
primary_thesis:
  name: "Insurance Stress Thesis"
  statement: |
    Insurance is both INDICATOR (consumers cutting coverage signals stress)
    and AMPLIFIER (underinsurance converts incidents into catastrophes).
    Market pressure from climate, inflation, and medical costs transmits
    directly to consumer financial vulnerability.
  
  confidence: 65%
  status: UNCERTAIN
  
  key_supporting_evidence:
    - "[ML-POLLY-XX]: [Evidence with reasoning]"
  
  key_contradictory_evidence:
    - "[ML-POLLY-XX]: [Evidence with reasoning]"
  
  invalidation_criteria:
    - condition: "Premium increases moderate below income growth 2+ quarters"
      confidence_impact: "-25%"
    - condition: "Policy lapse rates decline + coverage increases"
      confidence_impact: "-20%"
    - condition: "Carrier exits reverse; capacity returns"
      confidence_impact: "-20%"
    - condition: "Health coverage rates improve across segments"
      confidence_impact: "-15%"
  
  last_evaluated: "[Date]"
```

### 3.2 Competing Hypotheses

**Market Rationalization Hypothesis:**
- Statement: "Insurance repricing reflects accurate risk; consumers and markets will adapt"
- Current Assessment: "Partially valid but ignores affordability constraints"
- Key evidence needed: Adaptation patterns, coverage maintenance despite increases

**Government Backstop Hypothesis:**
- Statement: "State/federal programs will prevent coverage collapse"
- Current Assessment: "Limited evidence of adequate capacity"
- Key evidence needed: Backstop program capacity vs. projected need

### 3.3 Diagnostic Value Tagging

When logging evidence, assess its diagnostic value:

| Diagnostic Value | Meaning | POLLY Example |
|------------------|---------|---------------|
| **HIGH** | Discriminates between hypotheses | "Consumers dropping coverage despite no incident" |
| **MEDIUM** | Somewhat favors one hypothesis | "Premium increases accelerating" |
| **LOW** | Consistent with all hypotheses | "Insurance industry exists" |
| **ZERO** | Equally predicted by all | "Carriers file rate changes" |

---

## 4. SESSION PROTOCOLS

### 4.1 Session Types

**Update Session**
- *Purpose:* Ingest new data from carriers, regulators, industry sources
- *Trigger:* Earnings releases, rate filings, industry reports
- *Output:* Updated ML/FL entries, VX status changes
- *Duration:* Short

**Analysis Session**
- *Purpose:* Deep dive on specific pattern or mechanism
- *Trigger:* Major carrier announcement, threshold approached, CARL request
- *Output:* Analytical findings, FLOW updates, hypothesis confidence changes
- *Duration:* Medium-Long

**Regional Focus Session**
- *Purpose:* Deep dive on specific state/region (FL, CA, etc.)
- *Trigger:* Regional catalyst, state-specific data release
- *Output:* Regional assessment, state-level vector updates
- *Duration:* Medium

**Reconciliation Session**
- *Purpose:* Cross-reference audit, FL retirement, consistency check
- *Trigger:* Monthly, post-earnings-season
- *Output:* Corrected entries, retired FL items, updated cross-refs
- *Duration:* Medium

**Devil's Advocate Session**
- *Purpose:* Systematically challenge Insurance Stress thesis
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
- *Trigger:* Significant developments, regional crisis, monthly minimum
- *Output:* Formal State Vector per §6.2
- *Duration:* Short

### 4.2 Opening Protocol

Every session should begin with:

1. **Load Context**
   - This methodology skeleton
   - POLLY_DOMAIN_SKELETON.md
   - Most recent handoff
   - POLLY_WORKBOOK (or relevant log entries)

2. **Synthesis Confirmation**
   ```yaml
   session_opening:
     session_number: "POLLY [#]"
     based_on_handoff: "[Prior session number]"
     my_understanding:
       thesis_status: "[Current thesis status]"
       current_priority: "[What should be focused on]"
       key_context: "[Critical context carried forward]"
       regional_alerts: "[Any state-specific concerns]"
     gaps_or_questions:
       - "[Anything unclear]"
     confirmed: [true | false]
   ```

3. **Session Intent**
   - State session type
   - Identify specific objectives
   - Note geographic focus if applicable

### 4.3 Closing Protocol

Every session should end with:

1. **Log Updates** — All observations logged, FL retired if needed
2. **Handoff Creation** — Follow template in §5
3. **CARL Notification** — If significant, prepare State Vector

---

## 5. HANDOFF SPECIFICATION

### 5.1 I-PASS Adapted Structure

| Component | POLLY Adaptation |
|-----------|------------------|
| **I** — Illness Severity | Thesis Status (one word) |
| **P** — Patient Summary | Current insurance stress state, phase, confidence |
| **A** — Action List | Priority tasks for next session |
| **S** — Situation Awareness | Invalidation watch + contingencies + regional alerts |
| **S** — Synthesis by Receiver | Questions for next session |

### 5.2 Required Handoff Fields

```yaml
handoff:
  session_number: "POLLY [#]"
  created_at: "[Date]"
  
  # THESIS STATUS
  thesis_status: "[VALIDATED | CONTESTED | UNCERTAIN | INVALIDATED]"
  urgency: "[ROUTINE | ELEVATED | CRITICAL]"
  summary_sentence: "[One sentence on current state]"
  
  # CURRENT STATE
  current_state:
    phase: "[Stable | Premium Pressure | Coverage Erosion | Protection Collapse]"
    thesis_confidence: [XX]%
    thesis_confidence_reasoning: "[Why this level]"
    key_developments:
      - "[Recent significant observation]"
    vector_summary:
      breached: [count]
      critical: [count]
      elevated: [count]
    regional_status:
      florida: "[Status]"
      california: "[Status]"
      other_alerts: "[Any other state concerns]"
  
  # ACTION LIST
  priority_actions:
    - priority: 1
      task: "[Specific task]"
      reason: "[Why important]"
  
  # SITUATION AWARENESS
  contingencies:
    - trigger: "[If this happens]"
      response: "[Do this]"
  
  seasonal_awareness:
    hurricane_season: "[Active? Key dates?]"
    wildfire_season: "[Active? Key dates?]"
    enrollment_periods: "[ACA open enrollment, etc.]"
  
  approaching_invalidation:
    - "[Any invalidation criteria getting close]"
  
  # CARL REPORTING
  carl_update_needed: [true | false]
  carl_update_reason: "[Why/why not]"
  
  # DOC COORDINATION (health coverage overlap)
  doc_coordination_needed: [true | false]
  doc_coordination_topic: "[If yes, what topic]"
  
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

POLLY is a subordinate agent to CARL. POLLY monitors insurance stress and reports consumer financial vulnerability signals to CARL via State Vectors.

**When to Report to CARL:**
- Any POLLY vector moves to BREACHED
- Major carrier announces significant market exit
- State last-resort insurer shows rapid enrollment growth
- Multiple vectors move to CRITICAL simultaneously
- Regional crisis emerges (FL, CA, etc.)
- Monthly minimum (even if "no significant change")

### 6.2 State Vector Specification (POLLY → CARL)

```yaml
state_vector:
  # IDENTITY
  id: "SV-POLLY-[YYYY-MM-DD]-[##]"
  from_agent: "POLLY"
  to_agent: "CARL"
  timestamp: "[ISO timestamp]"
  
  # SYNTACTIC (shared vocabulary)
  domain: "Insurance Stress"
  primary_metric: "[Most concerning vector]"
  value: "[Current value/status]"
  status: "[NORMAL | ELEVATED | CRITICAL | BREACHED]"
  
  # SEMANTIC (POLLY's interpretation)
  interpretation: |
    [What this means for consumer financial vulnerability]
    [Insurance as indicator vs. amplifier in this case]
    [Geographic concentration if applicable]
  
  confidence: [XX]%
  confidence_reasoning: "[Why this confidence]"
  
  translation_flags:
    - "[Insurance concepts that need explanation]"
    - "[Regional vs. national distinction]"
  
  # PRAGMATIC (recommended action)
  recommended_action: "[IGNORE | WATCH | INCORPORATE | ESCALATE]"
  action_rationale: "[Why this recommendation]"
  
  transmission_to_carl:
    vectors_affected: ["[CARL vectors this impacts]"]
    flow_activated: "[Any FLOW-POLLY-05 transmission signs]"
    lag_estimate: "[Expected time until CARL vectors show impact]"
    incident_dependency: "[Does transmission require incident to occur?]"
  
  # GEOGRAPHIC ALERT (if applicable)
  regional_alert:
    present: [true | false]
    region: "[If true, which state/region]"
    severity: "[Concern level]"
  
  # VALIDITY
  sources: ["[Key sources]"]
  next_update: "[When POLLY will report again]"
```

### 6.3 Cross-References to CARL

Key CARL vectors POLLY should monitor for transmission effects:
- **VX-CARL-1.03** — Credit Card Delinquency (uninsured losses → credit use)
- **VX-CARL-2.xx** — Housing vectors (insurance affects mortgage/property)
- Consumer spending vectors (premium burden reduces discretionary)

### 6.4 Coordination with DOC

Health insurance overlaps with DOC (Healthcare Cost) domain. Coordinate when:
- Health coverage changes affect medical cost exposure
- Medical debt transmission mechanisms activate
- ACA/Medicaid policy changes affect both domains

Protocol: Share relevant State Vectors; note coordination in handoffs.

---

## 7. BIAS MITIGATION

### 7.1 Devil's Advocate Protocol

**When to Invoke:** Monthly, or when Insurance Stress thesis confidence >80%

**Process for POLLY:**
1. Argue that insurance markets ARE rationalizing appropriately
2. Identify strongest evidence for "Market Rationalization" hypothesis
3. Ask: "What would I expect to see if insurance stress were temporary repricing?"
4. Document findings regardless of outcome

### 7.2 Fresh Eyes Protocol

**When to Invoke:** Quarterly

**Process:**
1. Load only VX definitions and raw data
2. Do NOT load prior ML entries or interpretations
3. Ask: "What does this data suggest about insurance market health?"
4. Compare to established thesis

### 7.3 POLLY-Specific Bias Risks

| Bias Risk | Why POLLY is Vulnerable | Countermeasure |
|-----------|------------------------|----------------|
| **Catastrophe recency** | Recent disasters vivid; long-term trends forgotten | Use multi-year data, not just recent events |
| **Regional overgeneralization** | FL/CA crises may not represent national picture | Always note geographic scope |
| **Industry narrative** | Carriers emphasize losses to justify rates | Cross-reference with consumer data |
| **Affordability assumption** | Assume premium = unaffordable without evidence | Require income-relative data |

---

## APPENDIX A: POLLY ENTRY TEMPLATES

### A.1 ML Entry Template

```yaml
ml_entry:
  id: "ML-POLLY-[##]"
  timestamp: "[When observation made]"
  created_by: "POLLY [session #]"
  
  vectors: "[VX-POLLY IDs affected]"
  segment: "[Homeowners | Auto | Health | Market]"
  geography: "[NATIONAL | STATE | REGIONAL | LOCAL]"
  state: "[If state-specific, which state]"
  
  description: |
    [What was observed — factual]
  
  analysis: |
    [What this means — interpretation]
    [Indicator vs. amplifier function]
  
  data_quote: "[Key data point or quote]"
  source: "[Source and date]"
  
  status: "[ACTIVE | ELEVATED | WATCH]"
  confidence: [0.XX]
  
  hypothesis_impact:
    insurance_stress_thesis: "[CONSISTENT | INCONSISTENT | NEUTRAL]"
    diagnostic_value: "[HIGH | MEDIUM | LOW | ZERO]"
  
  cross_links: "[Related entries]"
  carl_relevance: "[How this affects CARL assessment]"
  transmission_mechanism: "[If amplifier, what's the pathway?]"
  invalidation_criteria: "[What would make this obsolete]"
```

### A.2 FL Entry Template

```yaml
fl_entry:
  id: "FL-POLLY-[##]"
  timestamp: "[When created]"
  created_by: "POLLY [session #]"
  
  catalyst: "[What to watch for]"
  trigger_date: "[When]"
  
  vectors: "[VX-POLLY IDs affected]"
  segment: "[Segment]"
  geography: "[Geographic scope]"
  
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
    outcome_ml: "[ML-POLLY-XX documenting outcome]"
```

---

## APPENDIX B: SEASONAL CALENDAR

*Key dates for POLLY monitoring — recurring annually*

### Catastrophe Season
| Event | Dates | Relevance |
|-------|-------|-----------|
| Atlantic Hurricane Season | June 1 - Nov 30 | FL, Gulf Coast, Southeast P&C exposure |
| Peak Hurricane Risk | Aug 15 - Oct 15 | Highest probability of major storms |
| CA Wildfire Season | May - October | CA homeowners exposure |
| TX/Midwest Severe Weather | March - June | Hail, tornado exposure |

### Enrollment Periods
| Event | Dates | Relevance |
|-------|-------|-----------|
| ACA Open Enrollment | Nov 1 - Jan 15 (typical) | Health coverage access |
| Medicare Open Enrollment | Oct 15 - Dec 7 | Senior coverage choices |

### Reporting Cycles
| Source | Frequency | Typical Release |
|--------|-----------|-----------------|
| Carrier Earnings | Quarterly | ~4-6 weeks after quarter end |
| KFF Employer Survey | Annual | September |
| III Industry Data | Quarterly/Annual | Varies |
| State Insurance Reports | Varies | Check state DOI |

---

## APPENDIX C: CHECKLISTS

### C.1 Session Opening Checklist

- [ ] Loaded POLLY methodology skeleton
- [ ] Loaded POLLY domain skeleton
- [ ] Loaded most recent handoff
- [ ] Loaded POLLY workbook
- [ ] Written synthesis confirmation
- [ ] Identified session type and objectives
- [ ] Noted any regional focus

### C.2 Session Closing Checklist

- [ ] All new observations logged to ML (with geography)
- [ ] FL entries checked — retired any past dates
- [ ] Cross-references updated
- [ ] Hypothesis confidence updated if warranted (with reasoning)
- [ ] Handoff created with all required fields
- [ ] Regional status noted (FL, CA, other)
- [ ] Assessed: Does CARL need a State Vector update?
- [ ] Assessed: Does DOC need coordination on health coverage?

### C.3 State Vector Checklist (before sending to CARL)

- [ ] All three layers included (syntactic, semantic, pragmatic)
- [ ] Interpretation distinguishes indicator vs. amplifier function
- [ ] Geographic scope clearly noted
- [ ] Transmission mechanism explained (including incident dependency)
- [ ] CARL vector cross-references included
- [ ] Lag estimate provided
- [ ] Regional alert flagged if applicable
- [ ] Confidence reasoning documented

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 0.2 | 2026-01-20 | Initial POLLY methodology based on CARL methodology v0.2 |

---

*End of POLLY Methodology Skeleton*
