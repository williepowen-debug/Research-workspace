# CARL RED TEAM CHARTER

**Created:** 2026-01-21 | **Session:** CARL 005
**Purpose:** Institutionalize systematic challenge to the Front-Loading Paradigm thesis

---

## Mission

The Red Team function exists to **actively seek disconfirming evidence** and **stress-test CARL's thesis**. All agents in the CARL system are designed to find stress. The Red Team is designed to find **resilience, recovery, and reasons we might be wrong**.

---

## Why This Exists

From CARL 005 vulnerability analysis:

> "This is arguably our BIGGEST vulnerability. We have structural bias toward finding stress. We haven't systematically sought disconfirming evidence. Confidence has only increased, never decreased."

Without structured opposition, CARL risks:
- Confirmation bias (seeing what we expect)
- Overconfidence in magnitude estimates
- Missing recovery signals
- Failing to update when evidence contradicts

---

## Folder Structure

```
RED_TEAM/
├── RED_TEAM_CHARTER.md          # This document
├── COUNTER_EVIDENCE_LOG.md      # Running log of disconfirming signals
├── vulnerability_analyses/       # Deep dives on thesis weak points
├── counter_evidence/            # Documented recovery signals
├── competing_hypotheses/        # Alternative explanations
└── session_logs/                # Devil's Advocate session records
```

---

## Operating Principles

### 1. Active Seeking
Don't wait for disconfirming evidence to appear — actively search for it each session.

**Minimum 15 minutes per UPDATE session** should be spent asking:
- What positive signals exist?
- What data contradicts our thesis?
- What would the "Soft Landing" thesis point to?

### 2. Weight Hard Data
Prioritize hard data (DQ rates, bankruptcy filings, reported earnings) over soft data (surveys, sentiment) when evidence conflicts.

### 3. Disaggregate
Don't accept aggregate "stress" — break down by:
- Credit tier (prime vs. subprime)
- Geography (regional variations)
- Demographic (cohort differences)

Containment scenarios require granular analysis.

### 4. Document Everything
Every piece of counter-evidence gets logged, even if ultimately dismissed. Future sessions need the audit trail.

### 5. Confidence Adjustments Go Both Ways
If evidence supports thesis → confidence can increase
If evidence contradicts thesis → **confidence MUST decrease**

We have never decreased confidence. That's a red flag.

---

## Session Types

### DEVIL'S ADVOCATE Session
A dedicated session type (per boot doc) focused entirely on challenging the thesis.

**Minimum frequency:** Every 4-5 regular sessions
**Duration:** Full session
**Output:** Vulnerability analysis + confidence recommendation

### Red Team Check (within UPDATE sessions)
15-minute structured check within regular UPDATE sessions.

**Questions to ask:**
1. What positive signals emerged this session?
2. What data points favor the competing hypothesis?
3. Should confidence be adjusted downward?
4. Are we missing something?

---

## Competing Hypotheses to Track

### Primary: "Soft Landing" Thesis
**Claim:** Consumer stress is transitory; Fed cuts will normalize conditions.
**Status:** STRONGLY CONTRADICTED (<10% confidence) — but we should actively test this

**What would support Soft Landing:**
- Credit card DQ falls below 10% for 2 quarters
- Real wage growth exceeds inflation for 3+ months
- Savings rate recovers to >7%
- Minimum payment rate declines
- Fed cuts + DQ stabilization

### Secondary: "Subprime Containment" Thesis
**Claim:** Stress is real but contained to subprime; not systemic
**Status:** PLAUSIBLE (30% probability) — identified in CARL 005 vulnerability analysis

**What would support Containment:**
- Prime borrower default share stays <30%
- Bank NCOs rise but absorbed without credit crunch
- Unemployment stays below 5%
- Credit card DQ plateaus below ATH
- Major banks maintain dividends/buybacks

---

## Counter-Evidence Categories

Track signals in these categories:

| Category | Description | Example |
|----------|-------------|---------|
| **RESILIENCE** | Consumer strength signals | Savings rate increase, DQ decline |
| **RECOVERY** | Improving trends | BNPL late rates declining |
| **CONTAINMENT** | Stress limited to segments | Prime holding while subprime stressed |
| **POLICY** | Intervention that helps | Rate cuts, stimulus, forbearance |
| **POSITIVE BIFURCATION** | Regional/segment improvement | FL insurance recovery |

---

## Integration with CARL System

### Boot Doc Updates
If Red Team analysis recommends confidence adjustment, update:
- CURRENT STATE section (confidence scores)
- Add note explaining adjustment reason

### Handoff Protocol
Every handoff should include:
- Red Team findings (if any)
- Counter-evidence noted
- Confidence adjustment (if any)

### State Vector Protocol
Subordinate agents should include "positive signals" section in state vectors (currently only POLLY does this with FL recovery).

---

## Current Vulnerabilities (from CARL 005)

| Rank | Vulnerability | Assessment | Notes |
|------|---------------|------------|-------|
| 1 | Confirmation Bias | HIGH | Structural; all agents seek stress |
| 2 | Magnitude (Containment) | MODERATE-HIGH | May not be systemic |
| 3 | Policy Intervention | MODERATE-HIGH | Wild card |
| 4 | Timing | MODERATE | Could be off 6-12 months |
| 5 | Transmission | MODERATE | Not proven at scale |

---

## Files in This System

### Vulnerability Analyses
- `RT-VA-001_THESIS_VULNERABILITY_ANALYSIS.md` — Initial comprehensive analysis (CARL 005)

### Counter-Evidence Log
- `COUNTER_EVIDENCE_LOG.md` — Running log of all disconfirming signals

### Competing Hypotheses
- `CH-001_SOFT_LANDING.md` — Primary competing hypothesis
- `CH-002_SUBPRIME_CONTAINMENT.md` — Secondary competing hypothesis

---

*Charter established: CARL 005 (2026-01-21)*
