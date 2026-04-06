# ESI Triage Principles — Extracted for Financial Signal Routing

**Source:** Prompt 1 Research — Emergency Severity Index (ESI) Triage Systems  
**Date:** 2026-04-06  
**Status:** Ready for inbox/messaging system design

---

## Core Architectural Pattern: Dual-Axis Classification

**ESI Innovation:** Separate "how critical?" (acuity) from "what resources?" (cost)

| Medical (ESI) | Financial (Our System) |
|---------------|------------------------|
| Levels 1-2: Acuity ("how sick?") | **Urgency Axis:** Time to execution |
| Levels 3-5: Resource prediction | **Cost Axis:** Processing complexity |

**Key Insight:** These are fundamentally different questions. Conflating them causes misallocation.

---

## The Four Decision Points — Financial Translation

### Decision Point A: System-Critical?
**ESI:** Requires immediate life-saving intervention?  
**Financial:** Margin call, stop-loss breach, liquidity trap, correlation breakdown

**Criteria (adapted):**
- Position approaching stop-loss
- Margin utilization > threshold
- Liquidity dry-up in held positions
- Correlation spike threatening hedges
- System-level risk limit breach

**Action:** Immediate execution, bypass all queues

---

### Decision Point B: High-Risk / Thesis-Critical?
**ESI:** High-risk situation? New confusion? Severe distress?  
**Financial:** Thesis-confirming signal? Convergence event? Threshold breach?

**Criteria (adapted):**
- Threshold breach (HY OAS, CCC OAS, VIX, etc.)
- Convergence signal (multiple agents flag same risk)
- Time-sensitive catalyst (earnings, Fed meeting, claims)
- New information confirming/rejecting core thesis

**Action:** <10 min processing, priority queue

---

### Decision Point C: Resource Prediction
**ESI:** How many resources needed? (0/1/≥2)  
**Financial:** Processing complexity estimation

| ESI Level | Resource Count | Financial Equivalent | Processing Lane |
|-----------|---------------|---------------------|-----------------|
| Level 5 | 0 resources | Simple threshold alert | Automated bypass |
| Level 4 | 1 resource | Single data source, simple model | Fast-track |
| Level 3 | ≥2 resources | Multi-source, complex model, human review | Standard queue |

**Resource Definition (what counts as "cost"):**
- Data lookups (FRED, yfinance, EDGAR)
- Model recalculations (correlation, VaR, stress tests)
- Human approvals (position changes, size adjustments)
- Agent spawns (sub-agent research tasks)
- API calls (external data sources)

**NOT resources (routine, don't count):**
- Cache reads
- Simple arithmetic
- Formatting/output

---

### Decision Point D: Vital Sign Safety Net
**ESI:** Danger zone vitals trigger uptriage consideration  
**Financial:** Post-classification override for market stress

**Override triggers (always check after initial classification):**
- VIX spike > threshold
- HY OAS sudden widening
- Correlation breakdown (normally uncorrelated assets)
- Liquidity dry-up (bid-ask spread widening)
- Flash crash indicators

**Action:** Uptrage to Level 2 regardless of initial classification

---

## Critical Failure Modes to Avoid

### 1. The Level 3 "Black Hole"
**ESI Problem:** 60% of patients cluster at Level 3 — undifferentiated middle  
**Our Risk:** Everything becomes "medium priority"

**Mitigation:**
- Force distribution with strict criteria
- If >50% of signals land in one category, add discriminating criteria
- Consider splitting Level 3 into 3a/3b/3c

---

### 2. Triage Drift
**ESI Problem:** Classification becomes function of ED load, not patient condition  
**Our Risk:** High-volatility regime = everything urgent

**Mitigation:**
- Classification thresholds invariant to system state
- No "load-based" priority adjustments
- Machine learning models that operate independently of environmental context (+16pp accuracy)

---

### 3. Subjective Assessment Bias
**ESI Problem:** Racial/gender bias strongest where human judgment fills gaps  
**Our Risk:** "Conviction" weights, gut feel overrides

**Mitigation:**
- Protocolized pathways eliminate bias
- Minimize subjective classification
- Algorithmic, feature-based assignment

---

### 4. Static Classification
**ESI Problem:** Point-in-time assessment, patients deteriorate  
**Our Risk:** Signal becomes stale, market conditions change

**Mitigation:**
- Mandatory re-triage at defined intervals (CTAS model)
- Re-evaluate unprocessed signals every N minutes
- Time-decay function for signal relevance

---

## Actionable Design Principles

### DO Implement

| Principle | ESI Source | Financial Application |
|-----------|-----------|----------------------|
| **Fast-track bypass** | Level 4-5 patients → >70% wait reduction | Simple signals skip main queue |
| **Vital sign safety net** | Decision Point D | Post-classification override for vol spikes |
| **Mandatory re-triage** | CTAS time intervals | Re-evaluate stale signals |
| **Daily audits** | Triage accuracy 63% → 90% | Compare classification vs. actual P&L |
| **Feature-driven queuing** | Skip classify-then-prioritize | Direct queue assignment from features (+30-60% efficiency) |
| **Impact × urgency matrix** | ITIL adaptation | Portfolio exposure × time decay |

### DON'T Implement

| Anti-Pattern | ESI Lesson | Our Avoidance |
|--------------|-----------|---------------|
| Subjective severity | Bias at Level 2/3 boundary | No "conviction" weights |
| Level 3 clustering | 60% undifferentiated middle | Force distribution |
| Classification = disposition | L1 discharged, L5 admitted | Priority ≠ importance |
| Environmental contamination | 50% uptriage during crowding | Thresholds invariant to load |
| Strict priority without starvation | Low-priority queues starved | Aging/escalation mechanisms |
| One scheme for all types | MTS "unwell adult" failure | Separate logic by signal type |

---

## Recommended 5-Level System

| Level | Name | Criteria | Processing Target | Example |
|-------|------|----------|-------------------|---------|
| **1** | Critical | System-threatening, immediate action | Immediate | Margin call, stop breach |
| **2** | Urgent | Thesis-critical, time-sensitive | <10 min | HY OAS threshold breach, convergence signal |
| **3** | Standard | Complex, multi-resource | <60 min | Deep research request, multi-agent synthesis |
| **4** | Fast-Track | Simple, single resource | <15 min | Single threshold alert, routine rebalancing |
| **5** | Automated | Zero resources, fully automated | Immediate | Cache refresh, simple calculation |

**Fast-Track Eligibility:** Level 4-5 signals bypass main queue → 70% wait reduction

---

## Implementation Checklist

- [ ] Define Decision Point A criteria (system-critical thresholds)
- [ ] Define Decision Point B criteria (thesis-critical signals)
- [ ] Define resource counting rules (what counts as "cost")
- [ ] Define Decision Point D overrides (vital sign safety net)
- [ ] Implement fast-track bypass for Level 4-5
- [ ] Implement mandatory re-triage intervals
- [ ] Build audit logging (classification vs. outcome)
- [ ] Ensure thresholds invariant to system load
- [ ] Design separate flowcharts for signal types (macro, single-name, risk, regulatory)
- [ ] Add aging/escalation to prevent starvation

---

## Key Metrics to Track

| Metric | ESI Benchmark | Our Target |
|--------|--------------|------------|
| Mistriage rate | 32.2% | <20% |
| Inter-rater reliability (κ) | 0.791 | >0.80 |
| Level 3 clustering | 60% | <40% |
| Fast-track eligibility | 30-60% | 30-50% |
| Audit accuracy improvement | 63% → 90% | Baseline → +20pp |

---

## References

- ESI Version 4 Handbook (AHRQ)
- CTAS Implementation Guidelines
- MTS Presentational Flowcharts
- "Triage drift" research (overcrowding effects)
- Machine learning triage studies (+16pp accuracy)

---

**Next Steps:**
1. Review against Prompt 2 (military messaging) for additional principles
2. Draft formal specification document
3. Prototype routing logic
