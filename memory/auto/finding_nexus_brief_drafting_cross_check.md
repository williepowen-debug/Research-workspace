---
name: finding-nexus-brief-drafting-cross-check
description: "Drafting a NEXUS_BRIEF is a cross-check pass, not a solo template-fill — diff shared facts against peer briefs and mine them for latent edges"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 62d42722-ab26-4fe0-ad3c-54dadfdf7594
---

When an agent drafts/refreshes its `NEXUS_BRIEF.md` (fleet rollout, schema R3+amd7), the highest-value moves are NOT filling the template solo — they are (1) **cross-checking load-bearing shared facts against peer agents' briefs**, and (2) **mining peer briefs for latent edges into your own domain**.

Validated VIOLET 2026-06-08 standing up its brief:

- **(1) Drift surfaced as peer disagreement.** VIOLET's state files had May CPI on 6/12; SAM and BRENT both had 6/10 (correct, BLS-verified). The standardized format made the peer-vs-peer mismatch visible at a glance — the disagreement *was* the verification trigger. VIOLET also had NFP consensus 88k vs BRENT's 80k (BRENT right). The brief format catches drift that idiosyncratic STATUS files hide. This is NEXUS's Type-B comparison value working *in reverse* — at draft time, for the author, not just for NEXUS.
- **(2) The loud edge crowds out the quiet real one.** VIOLET integrated BRENT's tension immediately (BRENT's brief *names* VIOLET's vol node → unmissable) but initially under-used SAM's brief, missing that SAM's yen-carry-unwind-into-BOJ is a vol event in VIOLET's own domain (the Aug-2024 carry-unwind analog was already in VIOLET's research queue). The edge that names you is louder than the edge you must infer; budget a deliberate pass for the quiet ones.

**Why:** the brief's stated purpose is cross-agent comparison (Type B). That same comparability pays off at *authoring* time — peer briefs are a free fact-check and edge-discovery surface. Treating the draft as a solo template-fill wastes it, and ships drift the format was designed to catch.

**How to apply:** after a solo first pass, read 2-3 peer briefs whose domains touch yours: (a) diff every shared date/number/level against your own state files — any divergence → verify against the primary source, don't assume your copy is right; (b) scan their SENDING/WAITING-FOR tables for edges that transmit into your domain and add the reciprocal. Applies to all remaining Tier-1 rollout agents. Related: [[finding_independent_convergence_validates_schema]], [[finding_subagent_prefire_date_verification]], [[finding_shared_antecedent_independence_test]], [[feedback_verify_counts_before_propagating]].
