# Prompt 1 Distilled: ESI Triage — What We Keep

**Source discipline:** Emergency medicine (Emergency Severity Index, CTAS, MTS)
**Core question answered:** How do you classify incoming signals on two axes simultaneously — urgency AND processing cost — without conflating them?

---

## The Big Idea: Dual-Axis Classification

ESI's key innovation is that "how urgent is this?" and "how expensive is this to process?" are **different questions**. Conflating them causes misallocation — an urgent but simple signal gets the same treatment as an urgent and complex one.

| Axis | What It Measures | Our Translation |
|------|-----------------|-----------------|
| **Urgency** (ESI Levels 1-2) | How time-critical? | How fast must WALTER route this? |
| **Resource Cost** (ESI Levels 3-5) | How many resources to process? | How many agents/lookups/spawns needed? |

A margin call is urgent but cheap (route immediately, zero analysis needed). A multi-agent convergence assessment is urgent AND expensive. A routine cache refresh is neither. Classify on both axes independently.

---

## The Four Decision Points (Adapted)

Triage nurses walk a decision tree. WALTER should too:

### Decision A: System-Critical?
Does this require immediate action to prevent portfolio damage?
- Stop-loss breach, margin call, liquidity trap, correlation breakdown
- **Action:** Bypass all queues. Route immediately.

### Decision B: Thesis-Critical?
Does this materially confirm or threaten the core thesis?
- Threshold breach (HY OAS, CCC OAS, VIX), convergence signal, time-sensitive catalyst
- **Action:** Priority queue, <10 min processing target.

### Decision C: Resource Estimation
How many resources does this need?

| Resources | Processing Lane | Example |
|-----------|----------------|---------|
| 0 | Automated bypass | Simple threshold alert, cache refresh |
| 1 | Fast-track | Single data source lookup, one agent |
| 2+ | Standard queue | Multi-agent synthesis, deep research, human review |

**What counts as a resource:** Data lookups (FRED, yfinance, EDGAR), model recalculations, human approvals, agent spawns, API calls.
**What doesn't count:** Cache reads, simple arithmetic, formatting.

### Decision D: Safety Net Override
After initial classification, always check for override conditions:
- VIX spike > threshold
- HY OAS sudden widening
- Correlation breakdown (normally uncorrelated assets moving together)
- Liquidity dry-up (bid-ask widening)

If triggered: **force upgrade to Decision B level** regardless of initial classification.

---

## Failure Modes That Will Bite Us

### 1. The "Medium Priority" Black Hole
ESI's biggest failure: 60% of patients cluster at Level 3 — undifferentiated middle.

**Our risk:** Everything becomes "medium priority" and nothing gets fast-tracked or deprioritized.
**Fix:** If >50% of signals land in one category, the classification criteria aren't discriminating enough. Add sub-levels or sharpen thresholds. Force distribution.

### 2. Triage Drift
In busy ERs, triage becomes a function of how crowded the ER is, not how sick the patient is. Nurses unconsciously downtriage during surges.

**Our risk:** During high-volatility regimes, everything looks urgent. WALTER starts treating routine monitoring as critical.
**Fix:** Classification thresholds must be **invariant to system load**. A signal is Level 2 based on what it IS, not how many other signals arrived that day.

### 3. Static Classification
ESI assesses once at intake. But patients deteriorate.

**Our risk:** A signal classified as ROUTINE at intake becomes urgent as market conditions evolve.
**Fix:** Mandatory re-triage intervals. Unprocessed signals re-evaluated every N minutes. Canadian CTAS model: re-assess at defined intervals based on initial severity.

### 4. Subjective Bias
ESI error rates are highest at the Level 2/3 boundary — exactly where human judgment fills gaps between clear criteria.

**Our risk:** "Conviction" weights and gut-feel overrides contaminate classification.
**Fix:** Algorithmic, feature-based classification. Minimize places where subjective judgment determines routing.

---

## Patterns to Implement

| Pattern | What It Does | Expected Impact |
|---------|-------------|-----------------|
| **Fast-track bypass** | Simple signals (0-1 resources) skip main queue | 70% wait reduction in ESI studies |
| **Safety net override** | Post-classification check for stress indicators | Catches signals that initially look benign but aren't |
| **Mandatory re-triage** | Re-evaluate unprocessed signals on interval | Prevents stale signals from sitting in queue |
| **Forced distribution** | If >50% cluster in one level, sharpen criteria | Prevents "everything is medium" collapse |
| **Feature-driven queuing** | Route directly from signal features, skip explicit classification step | 30-60% efficiency gain vs classify-then-prioritize |
| **Classification audits** | Compare initial classification vs actual outcome | 63% → 90% accuracy improvement in ESI |

---

## What We Don't Need From ESI

- Medical-specific triage criteria (vital signs, presenting complaints)
- Comparison between ESI, CTAS, ATS, MTS systems
- Inter-rater reliability statistics
- Specific ML accuracy benchmarks (we'll develop our own)
- Pediatric/geriatric triage modifications

---

## The 5-Level System (Starting Point)

| Level | Name | Criteria | Processing Target |
|-------|------|----------|-------------------|
| **1** | Critical | System-threatening, immediate action required | Immediate |
| **2** | Urgent | Thesis-critical, time-sensitive | <10 min |
| **3** | Standard | Complex, multi-resource, multi-agent | <60 min |
| **4** | Fast-Track | Simple, single resource | <15 min |
| **5** | Automated | Zero resources, fully automated | Immediate |

Note: Levels 4-5 are fast-tracked PAST Level 3. A simple threshold check shouldn't wait behind a complex synthesis task just because the synthesis was submitted first.

---

*Distilled from ESI_TRIAGE_EXTRACTED_PRINCIPLES.md | April 6, 2026*
