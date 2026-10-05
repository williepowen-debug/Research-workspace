# Prompt 5 Distilled: Intelligence Community Dissemination — What We Keep

**Source discipline:** U.S. Intelligence Community (ICD 501, 502, 503; ODNI Foreign Disclosure; CAPCO framework)
**Core question answered:** How do you shift from "information belongs to whoever created it" to "information is a shared asset" — while maintaining control over sensitive content?

---

## The Big Idea: Discover Broadly, Retrieve Selectively, Push Where Appropriate

The IC's post-9/11 paradigm shift is the single most relevant model for our COP architecture. The old model ("need to know") = our current inbox system, where agents only see what's explicitly routed to them. The new model ("responsible sharing") = the COP, where information is presumed available unless there's a specific reason to restrict it.

| Era | IC Principle | Our Current System | COP Target |
|-----|-------------|-------------------|------------|
| Pre-9/11 | Need to know | Agents see only their inbox | — |
| Post-9/11 | Responsible sharing | — | Agents see COP + full archive |

**The denial standard matters:** Under ICD 501, withholding information requires "specific, articulable risks" — not vague concerns. In our system: the default is that every signal is visible on the COP and in the archive. WALTER only restricts access if there's a concrete reason (e.g., signal contains position-specific details that could cause premature action).

---

## Three-Mode Information Flow

This is the architecture for Layers 1-3 of the COP hybrid model:

| Mode | IC Definition | Our Implementation |
|------|-------------|-------------------|
| **Discovery** | Learn information exists via metadata | COP.md — domain, timestamp, precedence, one-line summary |
| **Retrieval** | Pull full content on demand | signals/ archive — full signal with sources, confidence, analysis |
| **Dissemination** | Push to authorized personnel | Push notifications — inbox pings for FLASH/IMMEDIATE only |

**The key insight:** Discovery and Retrieval are PULL operations — agents decide what to read. Only Dissemination is PUSH. This means most signals never generate inbox traffic. They exist in the COP and archive, and agents find them when they need them.

This solves the scaling problem: adding a new agent doesn't require updating routing rules for every signal type. The new agent reads the COP at boot and discovers what's relevant to their domain.

---

## Tearline Versioning: Same Signal, Multiple Detail Levels

The IC produces the same intelligence at multiple classification levels. The most operationally useful pattern for us:

| Level | Content | Who Reads It | Where It Lives |
|-------|---------|-------------|---------------|
| **Summary** | One-line assessment, precedence, domain tag | Everyone (COP scan) | COP.md |
| **Tearline** | Analytic conclusion, confidence score, action required | Domain agents | Signal header block |
| **Full version** | Raw sources, methodology, cross-references, data tables | Originating agent + deep analysts | Signal body |

**Why this matters:** Will scanning the COP shouldn't need to read a 500-word signal about CMBS maturity walls to know "REGINALD: CMBS refinancing wave $76.6B in Q2, IMMEDIATE." The summary is enough. If he wants detail, he reads the full signal.

**Implementation:** Every signal file has three scannable sections:
1. YAML header (metadata — machine-readable)
2. Summary paragraph (tearline — human-scannable)
3. Full body (deep content — read on demand)

This is already sketched in the Signal Format Spec. Tearlines make it mandatory, not optional.

---

## Dissemination Controls as Routing Constraints

| IC Control | Meaning | Our Equivalent | When to Use |
|-----------|---------|---------------|-------------|
| **ORCON** | Originator controls forwarding | Signal stays with receiving agent — no readdressal without WALTER approval | Sensitive position info, pre-approval trade signals |
| **REL TO** | Releasable to listed partners only | Route only to named agents | Domain-specific signals (e.g., CRE signals → REGINALD only) |
| **DISPLAY ONLY** | Show without copy transfer | Agent can reference but not reproduce in their STATUS | Will's private journal entries, draft thesis |

We don't need NOFORN, IMCON, or PROPIN — those are IC-specific. But the principle of **enforceable routing constraints as signal metadata** is directly applicable. The routing table already has domain assignments; dissemination controls make those assignments machine-enforceable, not just guidelines.

---

## Audit as Enabler, Not Burden

The IC's core bargain: **broader access is acceptable if and only if access is logged and reviewable.**

**Our translation:** Opening up the signal archive and COP to all agents is safe because:
- Every signal has a creation timestamp and author
- The route_log records who received push notifications and when
- Agent STATUS files record what signals were processed
- Git history provides an immutable audit trail

Without audit capability, open access creates risk. With it, open access creates value. This is why the Signal Registry (Draft A) includes logging fields — they're not bureaucracy, they're the mechanism that makes openness safe.

---

## The Watchlist Pattern

IC analysts create "saved searches" — persistent subscriptions that automatically flag matching intelligence.

**Our translation:** Each agent's boot sequence includes domain-specific scan criteria:
- REGINALD watches for: CRE, bank earnings, CMBS, funding stress
- CARL watches for: labor, consumer credit, delinquency, gas price
- SAM watches for: BOJ, yen, JGB, carry trade

These aren't routing rules WALTER maintains — they're agent-side filters applied to the COP and archive. The agent scans the COP, matches against their watchlist, and pulls relevant signals. This inverts the routing burden: instead of WALTER deciding who gets what, agents decide what they need.

**Combined with push:** WALTER still pushes FLASH/IMMEDIATE. But for PRIORITY/ROUTINE, the agent-side watchlist handles discovery. This is "discover broadly, retrieve selectively" in practice.

---

## Failure Modes That Will Bite Us

### 1. The "Responsible Sharing" Overcorrection
The IC's pendulum swung too far — WikiLeaks happened because access expanded faster than audit capability.
**Our risk:** Making everything visible on the COP before we have the logging infrastructure to track who read what.
**Fix:** Start with COP + archive visible to all. Add route_log tracking for push notifications. Full access logging can come later (Git history covers the gap).

### 2. Tearline Quality Degrades
If summaries are sloppy, agents read the full signal anyway — defeating the purpose.
**Our risk:** WALTER writes vague one-liners on the COP ("credit signal — see archive").
**Fix:** Tearline summaries must include: domain, precedence, what changed, and quantified impact. "REGINALD: CMBS Q2 maturity wall $76.6B hard maturity, no extensions available. IMMEDIATE." Not "CMBS update, see signal."

### 3. Discovery Without Context
Agents discover a signal exists but lack context to know if they should read it.
**Our risk:** COP entry says "LABOR: JOLTS update" — is this routine or thesis-changing?
**Fix:** Precedence indicator on every COP entry. Agents can skip ROUTINE entries outside their domain. IMMEDIATE/FLASH entries always include enough context to judge relevance.

---

## What We Don't Need From IC Dissemination

- Classification levels (UNCLASSIFIED through TOP SECRET//SCI) — no security clearance hierarchy
- CAPCO portion marking (paragraph-level classification) — too granular for our signal format
- Foreign Disclosure Officer (FDRO) role and ICD 403 process — no foreign partners
- FISA intercept restrictions and court-ordered controls — no legal compliance layer
- Zero Trust architecture and continuous monitoring (ICD 503) — no network security layer
- ABAC (Attribute-Based Access Control) systems — file permissions suffice
- Sensitive Review Board dispute resolution — Will arbitrates disputes directly
- UEBA behavioral anomaly detection — agent behavior is visible in STATUS files

---

*Distilled from PROMPT5_IC_DISSEMINATION_MASTER.md + PROMPT5_IC_DISSEMINATION_SUPPLEMENT.md | April 7, 2026*
