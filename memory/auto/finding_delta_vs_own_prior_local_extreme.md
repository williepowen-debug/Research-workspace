---
name: finding_delta_vs_own_prior_local_extreme
description: "a Δ measured against your OWN last reading misleads if that prior was a local extreme — contextualize a short-window delta against the medium-term trajectory before calling a reversal/regime-change"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 89b1ddd3-1f8e-45a5-8f53-0546435a41f6
---

A short-window delta (Δ1d/Δ7d) is computed against a baseline — and when that baseline is your *own previous state-file reading*, the delta silently inherits whatever distortion was in that prior point. If the prior reading happened to sit at a local peak/trough, the next delta will overstate the move and read as a reversal when it's really just mean-reversion of an overshoot.

ORACLE 2026-06-27: "Fed hike in 2026" printed 51.5%, **Δ7d −14** against my 6/22 STATUS reading of 61.5%. Read in isolation that looks like a dovish reversal of my prior #1 "hawkish-turn confirmed" signal. The CLOB `history` trajectory showed the truth: hike-2026 spiked to a ~66% peak ~6/20 (right after the 6/17 FOMC dots) and my 6/22 reading was *near that peak*; the 30-day trend was still **+21** (up). So the −14 was a pullback within an uptrend, not a pivot. No-cuts-2026 (the durable axis) held 80% (+13/30d). Calling a "reversal" off the 7d delta alone would have been wrong.

**How to apply:** before declaring a reversal/regime-change off a Δ vs your last reading, pull the trajectory (sparkline / Δ30d / Δ90d) and ask "was my prior baseline a local extreme?" If the short-window delta and the medium-term trend disagree in sign, trust the trajectory and frame it as overshoot-cooling, not a pivot — and pick a *level* tripwire on the durable series (here: no-cuts <70%) rather than chasing the noisy delta. Sibling of [[finding_divergence_requires_fresh_likeforlike_baseline]] (that one = stale *thesis* baseline; this one = your own prior reading being an extreme) and [[finding_suspect_fresh_pull_over_curated_record]]. Generalizes to any agent tracking deltas vs a last STATUS reading — prices, spreads, OAS, odds, macro prints.
