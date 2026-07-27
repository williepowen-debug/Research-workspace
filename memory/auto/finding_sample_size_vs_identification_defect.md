---
name: finding_sample_size_vs_identification_defect
description: "More data" fixes a sample-size defect and never fixes an identification defect — check which one you have before promising that another period, quarter, or print will settle it
metadata:
  type: feedback
---

When a finding is "real but unestablished," the reason is usually one of **two different defect classes**, and they are routinely conflated because the same remedy gets offered for both:

- **Sample-size defect** — too few observations; the pattern may be noise. **Remedy exists: wait for more periods.**
- **Identification defect** — the measurement cannot distinguish your hypothesis from a rival one, *no matter how many observations you collect.* **No remedy from that source at all.** Only a different instrument that breaks the confound resolves it.

**Worked instance (SHADE/CREED, 2026-07-27).** The claim: *"the fast-recognition securitized channel is shedding CRE (−$9.6B) while the slow-recognition insurance channel absorbs it (+$3.3B)."* Two defects surfaced:
1. **Sample size** — one quarter. The *prior* quarter had **both** series positive (CMBS +$3.6B, life insurers +$11.5B). Remedy: more quarters.
2. **Identification** — MBA attributes CM/MF holdings **by note-holder**, so *an insurer buying a CMBS bond prints in the CMBS bucket.* The two buckets are "note held by an insurer" vs "note held by a trust," **not** "insurance channel vs securitized channel." So a divergence cannot distinguish **holder migration** from **instrument-form mix shift.**

CREED had proposed *"two consecutive quarters in opposite directions is the confirmation"* — then retracted it: **that fixes defect 1 and does nothing for defect 2.** Even a clean, sustained divergence would not settle it.

**How to apply:** when you write "this needs another quarter/print/period to confirm," first ask — *"if I had 20 periods of this, would the rival explanation be excluded?"* If no, you have an identification defect: say so explicitly, stop promising the next print will settle it, and name the **different** source that would break the confound (here: a series splitting holdings **by holder type** — e.g. insurer statutory Schedule D via NAIC, or sector-level flow-of-funds tables — rather than by instrument legal form). Pre-registering a falsifier against a source with an identification defect produces a test that cannot fail informatively. Kin: [[finding_discovery_instrument_defines_the_claim]], [[finding_threshold_spec_fails_before_world]], [[finding_proxy_segment_masks_trigger_series]], [[finding_seasonal_trough_baseline_resolves_true_on_normal]].
