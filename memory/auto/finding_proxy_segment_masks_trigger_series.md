---
name: finding_proxy_segment_masks_trigger_series
description: "When the real series is unreachable, an adjacent-segment proxy can be methodologically impeccable and still produce the OPPOSITE verdict — IG (Baa-Aaa) said 'credit didn't reprice' in Mar-2023 while HY OAS moved +125bps. Grade the series the trigger actually fires on, or label the verdict as proxy-scoped."
metadata: 
  node_type: memory
  type: finding
  originSessionId: bd8279ea-4bcb-44d7-a76b-0ad3a0a4cbd7
---

**The pattern (2026-07-16, DEWEY prompt 07b):** with ICE BofA HY OAS blocked by FRED's rolling-3yr licence cap, an agent substituted Moody's **Baa−Aaa** as a credit proxy and concluded *"neither channel repriced"* in the Mar-2023 SVB episode (+8bps vs COVID's +115bps). The proxy work was excellent — it was benchmark-free precisely to strip out the Treasury-rally artifact that fooled the naive Baa−10Y read (+43bps, of which Aaa−10Y was +35). But the verdict was **wrong**: recovered **HY OAS went 397 → 522 = +125bps**, moving *Mar-9, concurrent with the run*. IG OAS peaked at just 164. **Both measures were accurate.** The error was calling "credit" what was only **IG** — and the trigger under study (X1) fires on **HY**.

**Why:** a proxy inherits its own segment's behaviour, and segments decouple exactly in the regimes worth studying. IG and HY are the same asset class and usually co-move — which is what makes the substitution feel safe — but in a bifurcated tape the spread between them *is* the signal. Rigor on the proxy (correct decomposition, artifact removal) raises confidence in a number that is answering a **different question**, so methodological quality actively launders the segment error. Note the failure was asymmetric and one-directional: the proxy could only *understate*. Sibling: [[finding_composition_mask_unmask_discriminator]] (entity-controlled denominator masks a headline) — same shape, different lever: here the *analyst's own substitution* does the masking.

**How to apply:** name the series the decision/trigger actually keys on **before** choosing a proxy. If the real series is unreachable, either (a) label the verdict **proxy-scoped** ("IG did not reprice" ≠ "credit did not reprice") and cap confidence, or (b) go get the real series — the wall may be soft ([[finding_declared_data_wall_needs_fleet_memory_check]]; here a Wayback archive endpoint recovered 1996→2023 in minutes and flipped the verdict). Never let a proxy's rigor transfer to a claim about the segment it isn't measuring. Related: [[finding_blended_index_masks_bifurcation]], [[finding_number_carries_threshold_unit_source]].
