---
name: feedback_dont_bank_unpassed_forecast
description: "Don't log a not-yet-passed bill / unrealized forecast as a resolved structural fact — it can reverse"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 10fb8061-e4c1-4ca0-a435-fe09515a4aff
---

A forecast or pending legislative action is not a resolved fact until it clears. MARCO banked the $71.7B ICE/CBP reconciliation bill as a near-certain "structural enforcement lock, funded and unconstrained through term" across STATUS + thesis (v2.0–v2.2) — then it **missed its Jun 1 2026 deadline** and the Senate parliamentarian struck the core enforcement provisions under the Byrd rule. The thesis had to walk back from 🔴 locked to 🟠 contested (v2.3).

**Why:** banking a forecast as fact contaminates everything downstream — dashboards, conviction levels, kill-conditions all inherit a certainty that doesn't exist yet. Catalysts on a calendar (votes, rulings, prints) carry execution risk until the event resolves.

**How to apply:** keep pending catalysts in the *forward docket* (dated, with branch logic), NOT in the confirmed/structural column, until they actually resolve. When a forecast does feed the thesis, separate the irreversible piece from the contingent piece — for MARCO the 2.2M self-deportation *stock* loss was irreversible (real spine) while the funding *flow* was contingent (the part that reversed). Mirror discipline to [[feedback_yoy_baseeffect_use_multiyear_stack]] (read the clean metric, not the contaminated one) — same family: don't let a contaminated/contingent layer masquerade as the robust core.
