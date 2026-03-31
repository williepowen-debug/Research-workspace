# SYSTEM INTENT

**Last Updated:** 2026-01-19
**Updated By:** Human Operator

---

## Purpose

Why this system exists:

> **Detect US consumer financial deterioration before traditional economic indicators recognize it, enabling proactive response to emerging credit and banking stress.**

The conventional wisdom assumes recession → unemployment → consumer stress. We are testing the hypothesis that this sequence has **inverted**: consumers are breaking first, and traditional indicators will recognize it late.

---

## Primary Thesis: Front-Loading Paradigm

**Statement:** Consumer financial deterioration LEADS rather than LAGS broader economic stress. The traditional sequence has inverted due to:
- Persistent inflation eroding real income
- Accumulated debt from low-rate era at variable/resetting rates
- Exhausted pandemic savings buffers
- K-shaped economy masking lower-segment stress in aggregates

**Confidence:** 88%
**Status:** VALIDATED (multiple tripwires breached)

**Current Phase:** Stage 2 → Stage 3 transition (Credit Exhaustion → Collateral Default)

---

## Key Tasks (All Agents)

1. **Monitor your domain** for stress signals
2. **Report significant findings** via State Vectors to CARL
3. **Translate domain signals** into consumer stress implications
4. **Flag contradictory evidence** — do not suppress disconfirming data
5. **Maintain audit trails** — document reasoning, not just conclusions

---

## End State

Success looks like:
- Validated or invalidated thesis with documented evidence trail
- Quantified timeline for stress propagation (if validated)
- Early warning delivered before traditional indicators confirm
- Clear communication of confidence and uncertainty

---

## Current Focus Areas

**Priority 1:** Credit exhaustion signals
- Minimum payment rates
- Credit utilization at limits
- Subprime delinquency acceleration

**Priority 2:** Collateral quality
- Auto values and negative equity
- Housing stress indicators
- HOA/assessment lien exposure

**Priority 3:** Transmission mechanisms
- Lender failures (cockroach thesis)
- Banking sector exposure
- Contagion pathways

---

## Invalidation Criteria (System-Wide)

The Front-Loading thesis would be INVALIDATED if:

1. **Pattern reversal:** Prime credit deteriorates faster than subprime (traditional recession pattern)
2. **Traditional sequence:** Employment weakens significantly before consumer stress metrics
3. **Buffer restoration:** Savings rates increase and credit utilization declines without recession

If ANY agent observes evidence toward these conditions, **ESCALATE immediately** via SHARED/alerts/

---

## Coordination Protocol

**Subordinate agents (POLLY, DOC, NICK, POP, GIG):**
- Post State Vectors to SHARED/state_vectors/incoming/
- Check this file periodically for focus changes
- Monitor SHARED/alerts/ for cross-agent signals

**CARL (parent agent):**
- Process incoming State Vectors
- Integrate subordinate signals into unified assessment
- Update this file when thesis status changes

**META (methodology):**
- Advisory role — does not participate in analysis
- Updates methodology based on operational learning

---

## Rules of Engagement

1. **Report what you see** — Don't pre-filter based on what you think CARL wants
2. **Include interpretation** — Data without meaning is noise
3. **Flag uncertainty** — Confidence levels and limitations matter
4. **No deletion** — Correct with history preserved
5. **Assume the next session knows nothing** — Externalize before session ends

---

*This document is the system's Commander's Intent. When uncertain, act within this framework.*
