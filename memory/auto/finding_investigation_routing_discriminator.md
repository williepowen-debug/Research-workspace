---
name: finding_investigation_routing_discriminator
description: "route signal-investigation by \"do I need the answer THIS session to make a routing call?\" — yes→inline verify, no→assign a dedicated research agent; a paywalled headline is an investigation POINTER not route-or-kill"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ca7de837-e262-43d3-b725-e07d4c42cceb
---

Will-directed (WALTER, 2026-06-27; codified CHECKLIST v0.22). When a signal needs *investigation* — recover paywalled content, build out data, verify framing — split two cases with one litmus: **"Do I need the answer THIS session to make a routing call?"**

- **Yes (blocking same-session framing-check)** → spawn an inline verify-research sub-agent (cheap, fast, keeps the call moving).
- **No (topic-investigation / data-building)** → **assign a dedicated research agent** (e.g. WALTER→DEWEY via a scoped `/deep-research` prompt + a tracking-ledger row); route the cited result on return. Keep the router/coordinator's own context for sensing + routing, NOT research execution.

Corollary — **a paywalled / headline-only posting is an investigation POINTER, not a route-or-kill binary**: sense → recognize the topic → trigger investigation depth → recover content + pull primary data, rather than killing on inaccessibility or relaying the headline as if it were a verified signal.

**Why:** research run in the router's context bloats it, and a cited deep-research output beats a quick verify; relaying a paywalled headline as a routed signal launders an unverified claim, while killing it loses a real lead.

**How to apply:** any triaging/coordinating agent (WALTER, PROME) — before researching yourself, run the litmus; default depth-research to a dedicated agent. Worked examples 2026-06-27: flood-insurance SIG-030 (inline verify — borderline) vs the housing-distress paywalled foreclosure headlines (assigned as a DEWEY deep-research prompt). Related: [[feedback_walter_autonomous_verify]], [[feedback_route_to_domain_agent]], [[finding_private_by_construction_unverifiable]].
