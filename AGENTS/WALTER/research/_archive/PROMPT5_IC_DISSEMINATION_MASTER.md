# Prompt 5: Intelligence Community Dissemination Controls — Master Extraction

**Source:** ICD 501, 502, 503; ODNI Foreign Disclosure Guidance
**Date:** 2026-04-06

---

## Core Doctrine Shift: "Need to Know" → "Responsible Sharing"

| Era | Principle | Default Action |
|-----|-----------|----------------|
| **Classic** | Need-to-know | Withhold unless proven necessary |
| **Modern (ICD 501)** | Responsible sharing | Provide unless specific risk proven |

**Key insight:** Information is a **national asset**, not property of the originating office. Stewards have "responsibility to provide"; authorized personnel have "responsibility to discover" and "responsibility to request."

**Denial standard:** Must rest on **specific, articulable risks** — exposure of sources/methods, statutory restrictions, or unacceptable disclosure risk. Disputes escalate to Sensitive Review Boards → DNI.

---

## Three-Mode Information Flow Model

| Mode | Definition | Use Case |
|------|------------|----------|
| **Discovery** | Learn information exists without seeing content | Metadata/index exposure; findability |
| **Dissemination** | Information pushed to authorized personnel | Routine distribution to cleared recipients |
| **Retrieval** | Requester pulls content after discovery | On-demand access post-authorization |

**Operational principle:** "Discover broadly, retrieve selectively, push where appropriate."

**Multi-agent parallel:** Discovery = signal metadata; Retrieval = full signal content; Dissemination = automatic routing to subscribed agents.

---

## Dissemination Control Taxonomy

| Control | Meaning | Effect on Routing |
|---------|---------|-------------------|
| **ORCON** | Originator controls further dissemination | Recipients cannot onward-share without approval |
| **NOFORN** | Not releasable to foreign entities | U.S.-only channels; blocks all foreign agents |
| **REL TO [X]** | Releasable to listed partners only | Route only to named allies/organizations |
| **REL TO + ORCON** | Release to listed partner, no further | Partner receives but cannot redistribute |
| **DISPLAY ONLY** | Disclosure allowed, retention prohibited | Show without copy transfer |

**Routing implication:** These are **enforcement labels** on messages, not just metadata. They constrain which agents can receive, store, or forward.

---

## Tearlines: Multi-Level Signal Versions

**Concept:** Same intelligence, multiple classification/detail levels.

| Level | Content | Audience |
|-------|---------|----------|
| **Full version** | Source, method, timing, selector, platform | Compartmented cleared |
| **Tearline** | Analytic conclusion, confidence, action required | Broader cleared audience |
| **Sanitized** | Generic threat assessment, no sources | Widest authorized distribution |

**Multi-agent application:**
- RED (adversarial analysis) → Full version with sources
- HENRY (market structure) → Tearline with confidence levels
- CARL (consumer credit) → Sanitized actionable signal

**Emergency disclosure:** Use tearline version if available (per ODNI guidance).

---

## Audit and Accountability Principles

| Requirement | Source | Implementation |
|-------------|--------|----------------|
| Access logging | ICD 501 | Every retrieval logged with user, time, justification |
| Audit review | ICD 501 | Standards for review/analysis of audit data |
| Incident reporting | ICD 502 | Adverse events reported; situational awareness |
| Continuous monitoring | ICD 503 | Risk management, compliance oversight |
| Retrieval limits | ICD 501 | User count limited by audit capability |

**Principle:** Broader discoverability acceptable **only if** access, retrieval, incidents, and misuse can be logged, reviewed, investigated.

---

## Foreign Disclosure Framework (ICD 403)

**Process:** Partner-specific release decisions, not blanket releasability.

| Scenario | Marking | Routing Behavior |
|----------|---------|------------------|
| No foreign release authorized | NOFORN | Block all non-U.S. agents |
| Specific partners approved | REL TO [UK, CAN, AUS, NZ] | Route only to listed partner agents |
| View but no copy | DISPLAY ONLY | Render without persistence |
| Emergency | Emergency release authority | Use tearline if available |

---

## Key Principles for Multi-Agent Architecture

1. **Presumption of access:** Default to providing; denial requires specific risk articulation
2. **Discovery-first design:** Metadata/index available broadly; content gated
3. **Versioned signals:** Tearlines enable appropriate granularity per recipient
4. **Enforced controls:** ORCON/NOFORN/REL TO are routing constraints, not suggestions
5. **Audit as enabler:** Logging capability determines access scope
6. **Escalation paths:** Dispute resolution through review boards
7. **Risk-proportionate:** Controls match sensitivity; not all signals need all controls

---

## Architectural Mapping

| IC Concept | Multi-Agent Equivalent |
|------------|------------------------|
| Discovery | Signal metadata in shared index |
| Dissemination | Automatic routing to subscribed agents |
| Retrieval | On-demand signal fetch with authorization |
| Tearline | Signal detail tiers (raw → processed → alert) |
| ORCON | Forwarding restrictions per signal |
| NOFORN | Agent citizenship/location filters |
| REL TO | Agent clearance/relationship labels |
| Audit logs | Signal access logging for compliance |
