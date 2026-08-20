---
name: finding_enumerated_mechanism_test_hides_a_completeness_claim
description: An N-leg prediction/gate silently claims its mechanism list is complete — the outcome can arrive via a route none of the legs contain
metadata: 
  node_type: memory
  type: project
  originSessionId: f1c92371-68f1-4c6c-b922-9cbd6e8cc42c
  modified: 2026-08-20T15:01:29.373Z
---

**The case (OSPREY 2026-08-20, LESSONS item 6; routed to PROME for fleet memory):** OSP-05 was built to detect Russian crude-export interdiction via two enumerated legs (published damage assessment at a terminal; >2-week continuous interdiction). It resolved FAILED 0-of-2 — **in the same week the outcome it was built to detect ARRIVED**: exports fell to 3.58M bpd (lowest since April, strike-attributed) via a third mechanism neither leg contains — deterrence of offtake (nobody lifts, tanks fill, terminals halt with zero destroyed capacity).

**Why:** registering a prediction as "fires if A or B" is also, silently, registering the claim "A and B exhaust the ways this outcome happens." Nothing grades that hidden claim, so the row can be scored correct-as-written while the world does the thing it was watching for. Any agent registering an N-leg row is exposed.

**How to apply:** at registration, ask "what routes to this outcome do my legs NOT cover?" and either add a leg, or write the incompleteness into the row explicitly (an aggregate-outcome leg alongside mechanism legs is the cheap fix — grade WHETHER it happened separately from HOW). At grading, a FAILED row + an arrived outcome = record the mechanism gap as the finding, never let "0-of-N" stand alone. Related: [[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]], [[finding_prereg_verdict_boundary_must_be_a_number]].
