---
name: finding_series_reconstruction_extension
description: "extend an institutional series past its published endpoint by reconstructing it from its underlying primary components, validating on the overlap, then carrying it forward"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 735fdc8e-b5b2-4c94-a7df-591e7a5ced3e
---

When an institutional/analyst series you need stops before the period of interest, don't treat the gap as unanswerable — **reconstruct the series from its underlying primary components, validate against the published overlap, then extend it.**

Worked case (DEWEY REQ-002, 2026-06-27): the St. Louis Fed "AI contribution to GDP growth" series (= info-processing equipment + software + R&D + Census data-center construction, via Fisher–Törnqvist) **ends at Q3-2025**, but the live question was Q1-2026. Rebuilding the bucket from BEA's *published* contribution-to-%-change series (FRED `Y034/B985/Y006 RY2…`) reproduced the Fed's numbers near-exactly (Q3-25 **0.48 = 0.48 exact**; Q1-25 1.25 vs 1.3) — the near-match *validates the reconstruction* — then carried it two quarters further (Q4-25 0.97, Q1-26 1.50), revealing the contribution **troughed then re-accelerated** — the actual answer, which no published source had.

**Why:** the validate-on-overlap step is what makes the extension trustworthy. An exact/near-exact match on the shared quarters proves you replicated the method, so the out-of-sample quarters inherit that credibility. Skip it and a reconstruction is just an unverified guess.

**How to apply:** (1) find the method note (which primary components, what formula); (2) pull those components yourself; (3) reproduce the published overlap — match → proceed, mismatch → your component set/method is wrong, STOP; (4) extend, labeling it `[PRIMARY data, <AGENT>-computed]`, NOT the publisher's official number; (5) note residual gaps (here: the data-center-construction add-on is bundled inside FRED structures, so the rebuild slightly under-counts).

Corollary — **counterfactual "X ex-Y" decompositions are fragile**: the residual swings with (a) the *vintage* of X (Q1-26 GDP read 2.0%→1.6%→2.1% across advance/2nd/3rd estimates) and (b) the *definition* of Y (include R&D or not). Deliver a range + flag the vintage; never bank a single ex-Y point estimate as a primary fact. Relates to [[finding_number_carries_threshold_unit_source]], [[feedback_prediction_canonical_measure]], [[finding_tool_default_asof_date_drift]], [[finding_edgar_403_user_agent_header]].
