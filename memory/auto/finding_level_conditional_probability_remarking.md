---
name: finding_level_conditional_probability_remarking
description: "A forward probability attached to a price level/range silently re-marks itself as spot moves; ask what spot was when it was computed, and split range-composites into per-level ladders"
metadata: 
  node_type: memory
  type: project
  originSessionId: d0ed3529-f5bf-45a4-a0c3-0fa721d71c54
---

**Finding:** A forward probability attached to a price range ("60-70% chance X touches 23-26 by August") is a *function of spot*, not a static fact — it silently re-marks itself every time the tape moves, and a range-composite hides WHICH end is doing the moving. VIOLET 2026-06-10: a touch-probability filed at 4:10 PM (VIX tick 21.86) straddled the 4:15 settle (22.22); by evening the range's bottom rung (23) had become near-mechanical (+3.5% away, prediction mostly "spent") while the top (26) stayed a 2-in-6 shot — the composite was simultaneously becoming more "true" and less meaningful, and nothing in the files flagged it. Caught by an operator provenance question ("is this recent work, and do you still support it?"), not by the agent or the verification layer.

**Why:** Two kinds of numbers age completely differently: historical base rates (6/6, 5/6, 3/6, 2/6 episodes reached each level) are permanent facts, safe to cite forever; forward probabilities derived from them are spot-conditional and decay/invert as spot approaches the levels. Blending a ladder into one range-composite is legitimate shorthand at filing time but becomes wrong as the world moves, because under-specified claims can't show which component moved.

**How to apply:** (1) When filing any probability attached to price/rate levels, record the spot it was computed from and a Stale_By/re-mark trigger. (2) Prefer per-level ladders over range composites — each rung re-marks transparently. (3) When consuming someone else's level-probability, first ask what spot was when it was computed; if spot has since entered or approached the range, demand a re-mark before relying on it. (4) Small-n ladders are ordinal, not cardinal (95% lower bound on a 6/6 is ~61%) — use them to locate which rung a decision sits on, don't polish the digits. Applies identically to SAM's event probabilities, RED's scenario weights, BRENT/HAWK price-level risk marks. Canonical instance: VIOLET KB-VIO-087 (filed composite 4:10 PM → refined to ladder 6:15 PM same day). Related: [[finding_catalyst_vs_consequence_conflation]] (probabilities carry their decomposition), [[finding_threshold_vs_mechanism]].
