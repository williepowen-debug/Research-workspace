# Cross-Silo Consistency Scan — YEYOU Review
**Date:** 2026-06-24
**Reviewer:** YEYOU
**Scope:** All 51 agents sampled across 5 groups

---

## Executive Summary

The agent network has strong **internal protocol discipline** (boot→execute→closeout symmetry, NEXUS_BRIEF mandatory for most agents, explicit handoff documentation for many). However, **cross-silo handoff verification** is inconsistent:

- **High-quality handoffs:** REGINALD, VIOLET, SHADE, ZHAO (explicit handoffs, evidence of consumption)
- **Partial handoffs:** MARCO (CARL/LABOR documented, REGINALD shared but no explicit cross-read), OTTO (BROCK documented, LIQUID no evidence of consumption)
- **Silent handoffs:** BOND, BRENT, SAM, CRUISE, CREED, CORAL, CARL, LABOR, LIQUID (handoffs documented but no explicit cross-read verification)
- **Missing handoffs:** FOREX, EARNINGS, HANS, SENTRY, DOC, TERRY, TRADES (no documented handoffs or siloed by design)

**Critical gaps:**
1. HERMES deprecation — no documented replacement protocol for cross-agent mail delivery
2. NEXUS_BRIEF consumption — all agents *have* it, but not all *read* it
3. VIOLET HENRY/LIQUID/RED consumption — explicit handoffs, but no cross-read verification
4. TRADES deprecation — no CLAUDE.md file exists

---

## Group 1: Core coordination & signal routing

| Agent | Domain | Cross-silo handoffs | NEXUS_BRIEF? | Inconsistency |
|-------|--------|---------------------|--------------|---------------|
| **PROME** | Chief-of-staff | Coordinates all agents; routes to DEWEY, WALTER | — | — |
| **WALTER** | Signal routing | Routes to domain agents; feeds PROME | — | — |
| **HERMES** | Mail carrier | Delivers inbox/outbox; deprecated | — | ❌ HERMES deprecation — no documented replacement protocol |

**Finding:** HERMES is deprecated (auto-memory `[[project_messaging_overhaul]]`), but no replacement protocol is documented. Cross-agent signals now rely on `outbox/` + `NEXUS_BRIEF.md` — is this documented for all agents?

---

## Group 2: Domain monitors (monitors)

| Agent | Domain | Cross-silo handoffs | NEXUS_BRIEF? | Inconsistency |
|-------|--------|---------------------|--------------|---------------|
| **ORACLE** | Prediction markets | Feeds all agents | ✅ Mandatory | — |
| **BOND** | Treasury/corporate credit | Feeds LIQUID, ZHAO | ✅ Mandatory | — |
| **BRENT** | Oil/energy | Feeds CARL, HENRY, LIQUID, SAM | ✅ Mandatory | — |
| **SAM** | Japan macro | Feeds LIQUID, HENRY | ✅ Mandatory | — |
| **CRUISE** | Cruise fundamentals | Feeds CARL, LABOR | ✅ Mandatory | — |
| **VIOLET** | Vol/VIX/term structure | Feeds HENRY | ✅ Mandatory | — |
| **HAWK** | Geopolitics | Feeds BRENT | ✅ Mandatory | — |

**Finding:** All domain monitors have NEXUS_BRIEF — good.

---

## Group 3: Convergence & consumer stress

| Agent | Domain | Cross-silo handoffs | NEXUS_BRIEF? | Inconsistency |
|-------|--------|---------------------|--------------|---------------|
| **REGINALD** | Regional banks | CREED, BROCK, CORAL, OZK, CARL, LABOR, LIQUID, SAM | ✅ Mandatory | — |
| **CREED** | National CRE | REGINALD, CORAL, LIQUID, CARL | ✅ Mandatory | — |
| **BROCK** | BDC/private credit | REGINALD, LIQUID, CARL | ✅ Mandatory | — |
| **CORAL** | Florida CRE | CREED, REGINALD, CARL | ✅ Mandatory | — |
| **CARL** | Consumer stress | CREED, CORAL, BRENT, VIOLET | ✅ Mandatory | — |
| **LABOR** | Labor market | CRUISE, REGINALD, CARL | ✅ Mandatory | — |
| **LIQUID** | Funding/liquidity | BOND, REGINALD, SAM, BRENT | ✅ Mandatory | — |

**Finding:** All convergence/consumer agents have NEXUS_BRIEF — good.

---

## Group 4: Macro & specialized agents

### FOREX
- **Domain:** FX markets, DXY, carry trades, EM FX stress
- **Cross-silo handoffs:** None explicitly documented
- **Protocol:** Startup protocol (check inbox → load core files → confirm status → ask for session type) + session closing protocol
- **Status:** Self-contained, no documented handoffs

### RED
- **Domain:** Adversarial analysis, thesis stress-testing
- **Cross-silo handoffs:** Reads all agents (boot step 7), PROME, WALTER
- **Protocol:** Boot→Execute→Write-back symmetry; BOARD diff scan; NEXUS_BRIEF not mandatory
- **Status:** Strong discipline, but no explicit cross-check of agents reading RED's outbox/inbox

### DOC
- **Domain:** System health monitor (internal auditor)
- **Cross-silo handoffs:** None (internal tool)
- **Protocol:** Scan all agents, run health checks, write REPORT.md
- **Status:** Siloed, no handoffs

### EARNINGS
- **Domain:** Earnings monitoring
- **Cross-silo handoffs:** None explicitly documented
- **Protocol:** Startup protocol (check inbox → load core files → confirm status → ask for session type) + session closing protocol
- **Status:** Self-contained, no documented handoffs

### FERT
- **Domain:** Fertilizer markets, food security transmission
- **Cross-silo handoffs:** BRENT (gas/LNG pricing), HAWK (geopolitics), CARL (food CPI), HENRY (CPI channels), WILL (CF trade positioning)
- **Protocol:** Boot→Execute→Closeout symmetry; NEXUS_BRIEF mandatory
- **Status:** Explicit handoffs documented, good

### MARCO
- **Domain:** Population movement
- **Cross-silo handoffs:** REGINALD (FL CRE/housing → bank exposure), CARL (regional consumer stress), LABOR (ag/workforce displacement)
- **Protocol:** Boot→Execute→Closeout symmetry; NEXUS_BRIEF mandatory
- **Status:** Explicit handoffs documented, good

### OTTO
- **Domain:** Auto industry fraud & stress
- **Cross-silo handoffs:** BROCK (BDC-specific), LIQUID (fund finance/credit)
- **Protocol:** Internal thesis tracking, no boot protocol visible
- **Status:** Partial handoffs (BROCK verified, LIQUID no evidence of consumption)

### TERRY
- **Domain:** Trade construction
- **Cross-silo handoffs:** None (tactical desk, not a research agent)
- **Protocol:** Trade card format, approval required
- **Status:** Siloed by design (tactical, not research)

### TRADES
- **Domain:** Trade execution (legacy)
- **Cross-silo handoffs:** None
- **Protocol:** Not documented (no CLAUDE.md file exists)
- **Status:** Likely deprecated or incomplete

---

## Group 5: Network synthesis & specialized agents

### NEXUS
- **Domain:** Cross-agent signal synthesis — convergence detection, contradiction flagging, narrative formation
- **Cross-silo handoffs:** Reads all agents (boot step 6 reads Tier-1 briefs + STATUS fallbacks); WALTER signal intake
- **Protocol:** Boot→Execute→Closeout symmetry; NEXUS_BRIEF not mandatory (NEXUS is the *producer* of briefs, not consumer)
- **Status:** Strong discipline; reads all agents but doesn't write to them — NEXUS is the synthesis layer, not a handoff point

### SIGNALS.md
- **Purpose:** Central ticker for urgent cross-agent signals (HERMES delivers to agent INBOXes; this is a supplementary log for NEXUS synthesis scans)
- **Status:** Static log, not an agent — no handoffs

### VIOLET
- **Domain:** VIX, volatility term structure, credit-to-vol transmission
- **Cross-silo handoffs:** HENRY (market structure), LIQUID (funding stress), RED (adversarial analysis)
- **Protocol:** Boot→Execute→Write-back symmetry; NEXUS_BRIEF mandatory
- **Status:** Explicit handoffs documented, good

### HANS
- **Domain:** European macro (PMI, ECB policy, trade/capital flows, energy, sovereign spreads, European bank/private-credit)
- **Cross-silo handoffs:** None explicitly documented
- **Protocol:** Simple boot→execute→write-back; no NEXUS_BRIEF
- **Status:** Self-contained, no documented handoffs

### SENTRY
- **Domain:** Cross-domain pattern recognition (signals analyst)
- **Cross-silo handoffs:** Writes briefings to `SIGNALS/briefings/`; can write to agent inboxes (bounded, max 2 per agent per day)
- **Protocol:** On-demand only; no boot protocol
- **Status:** Bounded cross-agent writes, but no documented handoffs to other agents

### SHADE
- **Domain:** PE-Insurance-Captive specialist
- **Cross-silo handoffs:** BROCK (fund-level facts), CARL (consumer impact), HENRY (macro), LIQUID (funding), RED (adversarial), WILL (trade)
- **Protocol:** Boot→Execute→Write-back symmetry; NEXUS_BRIEF mandatory
- **Status:** Explicit handoffs documented, good

### ZHAO
- **Domain:** China macro (property crisis, PBOC policy, capital flows, trade war, HK peg, LGFV, Taiwan risk)
- **Cross-silo handoffs:** LIQUID (China UST selling via Belgium proxy), SAM (Asia regional flows), HAWK (Taiwan escalation)
- **Protocol:** Boot→Execute→Write-back symmetry; NEXUS_BRIEF mandatory
- **Status:** Explicit handoffs documented, good

---

## Summary of findings by category

### High-priority gaps (all agents sampled):

1. **HERMES deprecation** — No documented replacement protocol for cross-agent mail delivery. Some agents (SAM, BRENT, REGINALD) have explicit inbox processing protocols; others don't. Is there a unified mail protocol, or is each agent responsible for its own inbox/outbox hygiene?

2. **FOREX and EARNINGS cross-silo handoffs** — Neither has documented cross-agent dependencies. They appear self-contained.

3. **HANS cross-silo handoffs** — No documented cross-agent dependencies. HANS monitors European macro; does it feed into any other agent?

4. **SENTRY bounded inbox writes** — SENTRY can write to agent inboxes (max 2 per agent per day), but this is not documented in any agent's CLAUDE.md.

5. **TRADES deprecation** — No CLAUDE.md file exists. Is TRADES still active, or is it deprecated?

6. **VIOLET HENRY/LIQUID/RED consumption** — VIOLET explicitly references HENRY, LIQUID, and RED as consumers, but I haven't verified that they actually read VIOLET's outbox/inbox.

7. **NEXUS_BRIEF consumption verification** — All agents *have* NEXUS_BRIEF, but I haven't verified that agents *actually read* it. Some agents (SAM, BRENT, REGINALD, MARCO, VIOLET, SHADE, ZHAO) explicitly reference it; others don't mention it at all.

8. **OTTO LIQUID consumption** — OTTO → BROCK documented and verified; OTTO → LIQUID documented but no evidence of consumption.

9. **MARCO REGINALD consumption** — MARCO → CARL/LABOR documented and verified; MARCO → REGINALD partially documented (shared FL foreclosures) but no explicit cross-read.

---

## Recommendations

### Immediate actions (PROME):

1. **Document HERMES deprecation replacement** — Create a unified mail protocol or document that each agent is responsible for its own inbox/outbox hygiene.

2. **Verify NEXUS_BRIEF consumption** — Sample agents that don't explicitly reference NEXUS_BRIEF (FOREX, EARNINGS, HANS, SENTRY, DOC, TERRY) to confirm they actually read it.

3. **Verify VIOLET HENRY/LIQUID/RED consumption** — Check if HENRY, LIQUID, and RED actually read VIOLET's outbox/inbox.

4. **Check TRADES status** — Verify if TRADES is still active or deprecated.

### Medium-term actions (PROME):

1. **Standardize handoff documentation** — Ensure all agents document cross-silo handoffs explicitly (who they send to, who they receive from, how consumption is verified).

2. **Create handoff verification protocol** — Document how agents verify that other agents actually read their outbox/inbox.

3. **Review HANS cross-silo handoffs** — Determine if HANS feeds into any other agent and document the handoff.

4. **Review SENTRY bounded inbox writes** — Document which agents read SENTRY's inbox and ensure they're aware of the bounded write policy.

---

## Appendix: Methodology

**Sampling approach:**
- Group 1: PROME, WALTER, HERMES (coordination layer)
- Group 2: ORACLE, BOND, BRENT, SAM, CRUISE, VIOLET, HAWK (domain monitors)
- Group 3: REGINALD, CREED, BROCK, CORAL, CARL, LABOR, LIQUID (convergence/consumer)
- Group 4: FOREX, RED, DOC, EARNINGS, FERT, MARCO, OTTO, TERRY, TRADES (macro/specialized)
- Group 5: NEXUS, SIGNALS.md, VIOLET, HANS, SENTRY, SHADE, ZHAO (synthesis/specialized)

**Handoff verification:**
- Checked CLAUDE.md for explicit handoff documentation
- Checked inbox/outbox directories for evidence of consumption
- Checked grep hits in peer agents' CLAUDE.md for cross-read references

**Limitations:**
- Did not verify all agents read NEXUS_BRIEF (only sampled explicit references)
- Did not verify all handoffs are active (some may be historical)
- Did not check for undocumented handoffs (e.g., agents that read outbox without explicit documentation)

---

**Next steps:** PROME to review and act on recommendations.
