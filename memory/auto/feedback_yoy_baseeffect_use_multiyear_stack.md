---
name: feedback_yoy_baseeffect_use_multiyear_stack
description: "When a YoY series laps a structural break, the headline reverses on base-effect while the level keeps falling — read a multi-year stack, not YoY"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9fcd5ce0-889c-46d4-a139-0e39923a5b11
---

When a year-over-year series laps the start of a structural break, the headline YoY will reverse (e.g. flip positive) on base-effect even while the absolute level keeps deteriorating. The recovery is the comparison base easing, not the phenomenon reversing.

**Concrete case (MARCO, 2026-05):** the Canadian travel boycott began Feb 2025. By April 2026 Canadian US-return trips printed +1.4% YoY — which at the top level got read as "softening." But the 2-yr stack vs pre-break 2024 was −30% and *worsening* (−28% March → −30% April). Sentiment (Nanos) was 82% boycott-helpful — no easing at all. The MARCO TOURISM sub-agent had held the right metric (2-yr stack) since the prior session; the top-level synthesis partly lost it by watching the headline. Forced a v2.1→v2.2 thesis correction (re-promoting the channel from "softened" to "structural").

**Why:** base-effect contamination is invisible if you only watch YoY. It produces false reversals exactly at the moments a thesis is most load-bearing (one year after the break).

**How to apply:** for any metric tracked across a regime change (boycott, policy shock, layoff wave, rate shock), anchor to a fixed pre-break baseline and report a multi-year stack alongside YoY. Treat a YoY sign-flip as suspect until the stack confirms it. At the synthesis layer, trust the sub-agent/owner's clean metric over the convenient headline. Mirror of the produce mechanism-vs-thermometer discipline ([[feedback_verify_existence_external_primaries]] is the adjacent lesson: verify the clean signal before promoting OR demoting a channel).
