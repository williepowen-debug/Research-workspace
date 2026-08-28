---
name: finding_conditional_swap_needs_base_rate_at_registration
description: "A conditional spec-swap (if X then use leg Y) must base-rate leg Y at REGISTRATION of the conditional, not at activation — otherwise Y falls into the amendment-inherits-certificate defect the moment X fires."
metadata: 
  node_type: memory
  symptoms: 
    - "the row registers ex-ante with an 'if F2 reads X then swap to butterfly leg Y' clause"
    - "a base_rate_review.py --agent NAME check reads clean because the alternative leg's text is not yet in the row's active cells"
    - the trigger goes live and the primary check queues under time pressure just as the swap is about to activate
  type: feedback
  originSessionId: 51a69186-72b3-4cbb-8978-f4ac3edeb36b
  modified: 2026-08-28T20:03:55.387Z
---

**The finding (2026-08-28, RED S38h audit of CHG-051's amendment-inherits-certificate class, live on FT-11):** a conditional spec-swap of the form *"if X reads Y, then swap trigger leg from A to B"* leaves leg B **un-base-rated** by construction, because `base_rate_review.py` and equivalents read the row's ACTIVE legs — B sits in the CONDITIONAL cell, not the active-legs cell, and is invisible to the check until it swaps in. At activation the deadline is measured in sessions and the base-rate calculation is deferred by pressure, which is how leg B silently inherits leg A's construction certificate when it has none.

**Why:** the amendment-inherits-certificate class (NEXUS ML-203, 2026-08-28 §6.2) attacks amendments that inherit the ORIGINAL row's base rate without re-verification. A conditional swap is that class shifted one step upstream: the amendment is PRE-REGISTERED as text but the leg it swaps IN is un-base-rated. Both instances of the class are silent-by-design: the row reads clean AND the tool reads clean, because neither is looking at the leg that will decide the outcome.

**How to apply:** at ANY registration of a conditional spec-swap (`if X then use leg Y`), base-rate leg Y against the conditional's own instrument and window BEFORE the row lands. Record the base rate in the row's Notes or a companion cell, and re-verify at activation only as a sanity check, never as the first read. If leg Y's base rate is not computable at registration (e.g., leg Y depends on data that doesn't yet exist), either (a) defer the whole conditional until the base rate IS computable, or (b) accept the row as APPARATUS-INCOMPLETE and mark it so a consumer never treats it as a registered check.

**Live instance:** RED-FT-11 v1.1 conditional (butterfly leg `2*DGS20−DGS10−DGS30` swap under BOND F2 read post-9/9). Registered S36c 2026-08-27, audited S38h 2026-08-28 — butterfly leg has NO base rate registered. Row updated with the v1.1 obligation. Base-rating is owed BEFORE BOND F2 activates it, not at activation.

**Related:** [[finding_prereg_verdict_boundary_must_be_a_number]] (a trigger that registers a direction but not a magnitude is only half pre-registered — same "hole in the row" shape) · ML-RED-203 (NEXUS charge, edit-axis staleness parent class) · ML-RED-183/184 (audit-inherits-granularity, sibling — a check inherits the granularity of its own unit of analysis).
