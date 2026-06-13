---
name: finding-re-derivation-surfaces-concept-failure
description: "when re-marking a stale level-anchored framework, RE-DERIVE the math at the new spot — concept failures hide inside numerical updates that a re-mark would miss. VIOLET 6/12/26 ladder"
metadata: 
  node_type: memory
  type: finding
  originSessionId: f004662b-fd16-4eb6-83f3-b971763eebd8
---

When a level-anchored framework gets stale-marked because its computing-spot moved (e.g., a ladder, a budget zone, a kill-line, a retest-budget), the *minimum* response is "re-mark the numbers." That is often insufficient.

**Rule:** RE-DERIVE the framework's logic at the new anchor, don't just re-quote the numbers at the new spot. The concept may not survive the transit.

**Reason:** A framework's *qualitative* clauses ("near-spent," "budget zone," "comfortably outside," "modal retest") are bound to the spot they were written from. When spot moves materially, the *quantitative* distance changes — but the *qualitative* meaning of the same VIX level can change category. What was a modal touch from spot 22 ("budget zone 24-25 = +8-12% retest") becomes an unaffordable tail event from spot 19 (+24-31% from entry). The historical touch-probability didn't change; only the cost-from-entry did. Re-marking the numbers preserves the words "budget zone" with their original implied risk-grade — silently mis-pricing the framework.

**How to apply:**
- Any framework with spot-conditioned language (ladders, budget zones, kill-lines, retest budgets) carries an implicit "this is valid IF spot is near [X]" condition. Make that condition explicit at write time.
- When a stale-mark trigger fires, the response is RE-DERIVATION, not just numerical refresh. Check whether each qualitative clause survives at the new anchor. Some will (e.g., raw historical population stats); some won't (e.g., "near-spent," "comfortably outside").
- Surface the *concept failure* explicitly — don't just update the numbers and move on. The re-derivation often surfaces a finding bigger than the numbers (in VIOLET's case: a fundamental retest-budget asymmetry between near-peak and deflated entries, which became a branch-weight rotation inside the live thesis).

**Origin:** VIOLET 6/12/26 — KB-VIO-099 ladder re-derivation. KB-VIO-089's "23 near-spent / 24-25 retest budget zone / 26 no longer comfortably outside" was registered 6/10 at spot 22.22. Spot fell to 19.44 (settle) / 19.04 (tick) overnight. The re-derivation revealed: raw historical rates (11/9/9/8 of 19) stand unchanged, BUT the "retest budget" *concept* doesn't translate from a near-peak entry to a sub-20 entry — what was modal retest becomes tail event. Surfaced a strategic rotation in the thesis (fade economics hurt, coiled-spring strengthened) that a pure numerical re-mark would have missed.

**Sibling rules:**
- [[finding_number_carries_threshold_unit_source]] — anchor / unit / source travel with the number; this is the *concept* corollary
- [[feedback_yoy_baseeffect_use_multiyear_stack]] — base-effect class: same metric, different anchor, different meaning
- [[finding_threshold_vs_mechanism]] — "mechanism intact / threshold stuck" is a different concept-vs-numbers split
- [[finding_catalyst_path_decoupling]] — level trigger ≠ path trigger; same family of anchor-multiplicity issues
