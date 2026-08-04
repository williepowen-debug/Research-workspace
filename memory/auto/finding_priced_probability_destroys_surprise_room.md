---
name: finding_priced_probability_destroys_surprise_room
description: "A 'hawkish-of-priced' style bet pays on SURPRISE, so rising market-implied probability SHRINKS its edge. News that the mechanism is working can be bearish for the trade — compute unpriced remainder, not the level."
metadata:
  node_type: memory
  type: finding
---

A position framed as **"X-of-priced"** (hawkish-of-priced, hot-of-consensus, beat-the-whisper) pays on the **gap between outcome and expectation**, not on the outcome. So the arithmetic runs opposite to intuition: **evidence that your mechanism is working, once it reaches the price, DESTROYS your edge.**

**The trap:** you identify a real causal channel ("US Treasury is publicly pressuring Japan to hike"), confirm it is firing, and log it as *up-risk*. But if the pressure is absorbed into **pricing**, the surprise room you were paid for is gone. The mechanism can be live, correct, and adverse simultaneously.

**Worked case (SAM 2026-08-04).** Route 1 of the carry-convexity frame was "BOJ hawkish-of-priced." Bessent publicly conditioned further FX support on Japanese *policy* — a genuine new channel onto the largest in-window catalyst. SAM recorded it as **up-risk**, caveated as un-sourced. Sourcing it inverted the sign: Sep BOJ pricing had moved **~23% → ~39.7%**, so unpriced surprise room fell **~77% → ~60%**. Compounding it, SAM's own confirmed prior (CH-004) was that a *fully-priced* hike had already been delivered **without** unwinding carry. Net: neutral-to-negative for the trade. A second anchor (oil) was moving down at the same time, so what had been logged as "two anchors offsetting" was really **two anchors moving the same way** — and that read had survived only because one of them was unmeasured.

**Disciplines:**
1. **Track the UNPRICED REMAINDER, not the level.** `unpriced = 100 − cumulative`. That is the quantity the bet owns. If your source publishes cumulative probabilities, **difference them** for the per-meeting marginal — and verify the basis, because cumulative-vs-per-meeting is a silent factor-of-two class of error.
2. **Before logging a channel as up-risk, ask: does this reach the PRICE?** A mechanism that moves the market moves your edge *against* you. One that changes the outcome without being priced is what pays.
3. **"Could not source it" is grounds to withhold a DIRECTION, not to assert one with a caveat.** A caveated direction still propagates as a direction. The offsetting/aggregate read that depends on an unmeasured leg is not a finding — it is a placeholder wearing a finding's clothes.
4. **Re-derive the aggregate when any leg gets measured.** Two anchors "offsetting" can silently become two anchors compounding.

**Generalizes to:** earnings-vs-whisper, CPI-vs-consensus, election-odds-vs-narrative, any "market is underpricing X" thesis. The moment the market agrees with you, re-price your own edge — agreement is the thing you were being paid to not have.

Related: [[finding_threshold_level_is_a_measurement_not_a_constant]] · [[finding_escalation_line_needs_delta_not_level]] · [[finding_confidence_priced_against_thesis_not_letter]] · [[finding_offrepo_routine_prompt_rot]]
