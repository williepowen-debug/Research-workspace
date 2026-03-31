# CARL SYSTEM CONTEXT FOR METHODOLOGY RESEARCH

**Purpose:** This document provides grounding context for methodology research. It enables the methodology project to understand *what we're building methodology for* without loading the full CARL project.

**Last Updated:** 2026-01-19

---

## WHAT CARL IS

CARL (Consumer Aggregate Risk Ledger) is a multi-agent LLM system designed to monitor and predict US consumer financial stress. The core thesis—called the **Front-Loading Paradigm**—is that consumer financial deterioration *leads* rather than *lags* broader banking and credit crises. Consumers are breaking first; traditional economic indicators will recognize it later.

CARL is the primary agent focused on consumer stress. Planned subordinate agents include:
- **POLLY** — Insurance stress (P&C, health)
- **DOC** — Healthcare cost stress
- **NICK** — Shadow credit / non-bank lending
- **POP** — Small business stress
- **GIG** — Gig economy saturation

These agents report to CARL through standardized **State Vectors**—structured summaries of domain status, key metrics, confidence levels, and emerging concerns.

---

## THE LOG SYSTEM ARCHITECTURE

CARL maintains four distinct logs. Understanding their relationships is essential—methodology must support all four.

### VX (Vector Registry)
**Question answered:** "What are we measuring?"

Defines the 19 stress metrics with thresholds and tripwires. Structural—rarely changes. Example:

```
VX-CARL-1.04: Subprime Auto 60+ DQ
  Threshold: 7.0%
  Current: 6.65% (ALL-TIME HIGH since 1994)
  Status: BREACHED
```

### ML (Master Log)
**Question answered:** "What do we know right now?"

Documents current-state observations. Updated as new data arrives. Rarely retired. Each entry links to relevant vectors, includes confidence scores, analysis, sources, and invalidation criteria.

ID format: `ML-[DOMAIN]-[##]` (e.g., ML-CR-04 for Credit domain entry 4)

### FL (Future Log / Catalyst Log)
**Question answered:** "What should we watch for, and when?"

Tracks dated future triggers—events that could change system state. **Critical discipline:** FL entries are RETIRED when their date passes, regardless of whether the catalyst fired. Outcomes get documented in ML.

This distinction caused early confusion. We had 34 FL entries, 19 of which were actually current-state observations (belonged in ML). Cleanup reduced to 10 focused future triggers.

ID format: `FL-[DOMAIN]-[##]` (e.g., FL-EI-01 for Employment/Income catalyst 1)

### FLOW (Cascade Map)
**Question answered:** "If X breaks, what breaks next?"

Documents transmission pathways—how stress propagates across vectors and domains. Not date-driven; mechanism-driven. Persists as long as the structural relationship holds.

Example: FLOW-CARL-01 "Grand Unification" traces: Inflation squeeze → Income insufficiency → Credit exhaustion → Collateral default → Banking transmission

---

## KEY DOMAIN CONCEPTS

These terms carry meaning beyond their definitions. Preserving them transfers tacit understanding.

### Front-Loading Paradigm
The traditional sequence (recession → unemployment → consumer stress) has **inverted**. Consumers are breaking FIRST due to inflation squeeze, debt traps, and rate shock. The "soft landing" narrative is contradicted by granular data showing synchronized stress across all consumer credit verticals simultaneously.

### Zombie Borrower
A borrower making only minimum payments—technically current but functionally insolvent. At 22%+ APR, minimum payments cover almost no principal. These borrowers will transition to default 6-12 months after exhausting liquidity buffers. The minimum payment rate hitting a 12-year high is a leading indicator; the delinquency wave follows.

### Cockroach Thesis
"When you see one cockroach, there are probably more." Applied to subprime auto lender failures. Tricolor (criminal charges Dec 2025) followed by PrimaLend (Ch.11 Oct 2025) validated the thesis—visible failures indicate broader hidden deterioration.

### K-Shape Bifurcation
Economic divergence where upper-income households maintain spending while lower-income households deteriorate. **This masks aggregate stress.** Top 10% now represent 49.2% of consumer spending. Aggregate "flattening" in delinquency data often hides continued deterioration in lower segments. Headline numbers can look stable while the foundation crumbles.

### Super-Lien (HOA)
HOA assessment liens that take priority over first mortgages. If HOA forecloses, mortgage lender's collateral is impaired. Creates hidden transmission from consumer (HOA) stress to bank (mortgage) losses. Florida SIRS deadline passed Dec 31, 2025—foreclosure wave building.

---

## CURRENT SYSTEM STATUS (as of Jan 2026)

**Phase:** Stage 2 → Stage 3 transition (Credit Exhaustion → Collateral Default)

**Vector Summary:**
- 7 vectors BREACHED (tripwire crossed)
- 9 vectors CRITICAL (approaching threshold)
- 3 vectors ELEVATED
- 19 total vectors tracked

**Key Breaches:**
- Subprime auto 60+ DQ at all-time high (6.65%, tracking since 1994)
- Minimum payment rate at 12-year high
- Student loan conditional delinquency at 31% (highest ever)
- Hardship 401k withdrawals at all-time high (4.8%)

**Thesis Validation Status:** VALIDATED — Multiple tripwires breached, pattern confidence 92%

---

## WHAT THE METHODOLOGY MUST SUPPORT

The methodology skeleton will govern all agents. It must address:

### 1. Session Continuity Problem
Each LLM session starts with zero tacit knowledge. Handoffs capture explicit knowledge but lose analytical intuition, pattern recognition, and "feel" for the domain. The methodology needs to define what gets externalized and how.

### 2. Evidence Evaluation
How do we assess diagnostic value of evidence? Which observations actually discriminate between hypotheses vs. which are consistent with everything? (Heuer's inconsistency principle applies here.)

### 3. Competing Hypotheses
Currently CARL tracks the Front-Loading thesis with invalidation criteria, but doesn't formally track competing hypotheses (e.g., "Soft Landing" scenario). Methodology should require explicit alternative hypothesis tracking.

### 4. Multi-Agent Coordination
When POLLY reports insurance stress to CARL, what information transfers? How do we avoid information loss at agent boundaries? What makes a good State Vector?

### 5. Bias Mitigation
How do we prevent anchoring on early assessments? Confirmation bias toward the Front-Loading thesis? The methodology needs structured countermeasures.

### 6. Audit Trail Integrity
ML entries should be immutable once created? How do we handle corrections? What versioning discipline applies?

### 7. Confidence Calibration
Current confidence scores are somewhat ad hoc. Methodology should define how confidence is calculated, what triggers updates, how to prevent overconfidence.

---

## ARTIFACTS AND DATA STRUCTURES

### Domain Skeleton (CARL_DOMAIN_SKELETON_v1_2.md)
~2,500 lines. Defines:
- Entity types (consumer segments, credit products, expense categories)
- All 19 vectors with thresholds and tripwires
- Named FLOW cascades
- Data sources
- Glossary
- Invalidation framework

### Workbook (CARL_MLFLFLOWVX_S6.xlsx)
Four sheets:
- CONS ML: 17 entries (current state observations)
- CONS FL: 10 entries (future catalysts)
- CONS FLOW: 10 entries (cascade pathways)
- VECTORS: 22 entries (metric definitions)

### Session Handoffs
Markdown documents capturing session accomplishments, decisions made, open questions, and priorities for next session. Enable continuity across sessions.

---

## PAIN POINTS THE METHODOLOGY SHOULD ADDRESS

These emerged from actual CARL operations:

1. **FL/ML Confusion** — Early sessions mixed current-state observations with future catalysts. Took explicit cleanup to separate. Methodology should make the distinction unmistakable.

2. **Cross-Reference Drift** — Cross-links between entries became stale as IDs changed. Need reconciliation discipline.

3. **Confidence Reasoning Lost** — We record confidence scores but not the reasoning. Next session doesn't know *why* confidence is 88%.

4. **Tacit Knowledge Evaporates** — Each session develops intuitions that don't survive to the next session. The "feel" for when something is significant gets lost.

5. **Overwhelming Context** — Full skeleton + workbook + handoff can exceed useful context. Need to identify minimum viable context for different session types.

6. **No Devil's Advocate** — Easy to confirm the Front-Loading thesis; nothing systematically challenges it.

---

## SUCCESS CRITERIA FOR METHODOLOGY

The methodology skeleton succeeds if:

1. A new session can achieve analytical competence faster (reduced ramp-up)
2. Confidence reasoning persists across sessions
3. Competing hypotheses get fair evaluation
4. Multi-agent communication preserves essential information
5. Audit trails enable reconstruction of analytical path
6. Bias has structural countermeasures, not just awareness

---

## HOW TO USE THIS DOCUMENT

When researching a methodology framework (e.g., Military C2, Boundary Objects):

1. **Ground the concepts:** "How would X apply to CARL's situation?"
2. **Test against pain points:** "Does this framework address FL/ML confusion? Confidence reasoning loss?"
3. **Check against data structures:** "What would this require adding to ML entries? To handoffs?"
4. **Consider multi-agent:** "How does this scale when POLLY and DOC exist?"

The goal is methodology that *fits* CARL—not abstract best practices that sound good but don't integrate.

---

## LINKS TO FULL MATERIALS

When deeper context is needed, return to CARL project for:
- Full domain skeleton (CARL_DOMAIN_SKELETON_v1_2.md)
- Current workbook (CARL_MLFLFLOWVX_S6.xlsx)
- Latest session handoff

This bridge document is a summary, not a replacement.

---

*Document version: 1.0*
*Created: 2026-01-19*
*For use in: Methodology Research Project*
