---
name: finding_count_measures_intake_not_domain
description: "A coverage/cluster COUNT measures your own intake, not the world — so a governance trigger keyed to a count will misdiagnose a collection gap as a taxonomy or domain problem. You can audit what you killed; you cannot audit what you never saw."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0eefedce-1876-483e-8cea-dbcf5083422f
  modified: 2026-07-27T14:14:10.855Z
---

Any metric of the form *"how many signals do we have on X"* is a measurement of **your own collection and classification**, not of the domain. When a governance rule fires off such a count, its first-order reading is usually wrong.

Worked instance (WALTER, 2026-07-27): the `AI_INFRA_CAPEX` cluster hit its 40-signal soft cap, triggering a two-limb revisit test. **Limb (a) — fragmentation, the only limb about whether the cluster had stopped being one theme — did NOT fire** (4 populated angles, not >5). **Limb (b) — "any original angle with <2 signals in 60 days" — DID fire**, on two angles. Read at face value that says *split the cluster.*

The actual cause was collection, established earlier by the domain owner pushing back:
- **TrendForce (the standard source for that angle): 0 hits across all 764 archive rows. Ever.**
- **Micron's quarterly beat: never entered the router at all — not filtered out, never seen.**
- The router's **filter was audited clean** — 6 relevant kills out of 270, all 6 correct.
- Some in-scope signals had been **misfiled into a different cluster**, so the count under-read the domain twice over.

The domain owner's line is the whole finding: ***"Your cluster count is measuring your taxonomy, not my domain."***

**The load-bearing asymmetry:** you can audit what you **killed** — kills are logged, reviewable, and their rate is measurable. You **cannot** audit what you **never saw**. A collection gap is invisible from the inside and produces no error, no alert, and no artifact. In this case all three known instances surfaced only because a recipient pushed back or the operator sent a screenshot.

**How to apply:**
1. When a count-based trigger fires, ask **"is this bucket empty in the WORLD, or empty in my INTAKE?"** before touching taxonomy, thresholds, or structure.
2. Prefer **collection fixes over structural fixes** — restructuring to accommodate a gap encodes the gap permanently.
3. Distrust caps and counts as governance instruments; a count that fires for collection reasons will keep sending you the wrong way. Prefer a qualitative review trigger.
4. Treat **recipient push-back as a coverage-audit signal**, not a complaint — it is one of the only channels through which invisible gaps become visible.
5. Look for a **directional pattern** in the misses. Here it was specific and repeatable: financing and supply/credit were reliably caught; **demand-side capex guidance, ROI and input-cost were reliably missed** — three instances on three axes.

Related: [[finding_never_received_is_not_doesnt_hold]] · [[finding_coverage_gap_needs_all_surface_check]] · [[finding_discovery_tool_wrong_slice_false_zero]] · [[finding_passive_surface_rot_push_not_dashboard]] · [[finding_magnitude_ranked_discovery_blind_to_deep_slow]]
