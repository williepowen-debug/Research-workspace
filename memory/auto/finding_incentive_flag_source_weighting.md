---
name: finding_incentive_flag_source_weighting
description: "down-weight incentivized sources (attorney/regulator/broker/mgmt), up-weight realized hard-to-game metrics (NCO/call-reports/per-capita/deposits/core-CPI)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2deb9ef6-cca2-4435-981b-c119a048b089
---

When weighting a two-sided domain signal, score each cited source by its incentive before scoring the claim. **DOWN-weight** volume-incentivized sources (bankruptcy/plaintiff attorneys → "tidal wave"), politically-incentivized (regulators/OIR → "thriving market"), placement-incentivized (broker/reinsurance commentary), structurally-optimistic (bank/corporate mgmt → "no loss expected"). **UP-weight** realized, hard-to-game metrics: NCOs, FDIC call reports, per-capita-normalized counts (e.g. AOUSC bankruptcy), deposit flows, BLS core-CPI components.

**Why:** both alarmist AND complacent framings cluster around incentivized sources, and the verified-transmission data lags the framing in BOTH directions — so the honest read is almost always "framing ahead of the realized data."

**How to apply:** before logging a domain signal's strength, tag every cited source's incentive and re-weight; a claim resting only on incentivized sources is ≤0.55 pending a realized-metric confirm. Pair with the single-diagnostic discipline (name the one hard metric that would confirm/falsify). Surfaced from the Will-commissioned S-FL distress deep-research (RED chunk-C, KB-RED-052), which deflated a viral "tidal wave" to ~70/30 normalization on exactly this rubric. Related: [[feedback_litigation_allegation_weighting]], [[finding_threshold_vs_mechanism]], [[feedback_corrected_framing_calibration]].
