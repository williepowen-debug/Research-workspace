---
name: finding_option_marks_need_live_chain
description: Option position marks carried forward in state files go phantom — pull the live chain (last/bid/ask) at every decision point; sanity-check vs moneyness/DTE
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4a62efbc-b8af-4e4f-967f-71c66d99d9f4
---

Option marks in STATUS/SCRATCH files decay much faster than underlying prices and can be wrong by orders of magnitude. BRENT Jun 9 2026: CF $130C Jun 18 carried as "~$8 ≈ $800" [INFER] while the live chain showed $0.10 last / $0.00 bid — CF stock was $108.58, a 20%-OTM call with 7 sessions left *cannot* mark $8. A sell-vs-hold deliberation with Will ran on the phantom number (advisor caught it Jun 12).

**Why:** Rule 4 ("prices must be live") gets applied to underlyings but not derivatives; an [INFER] tag on a mark feels like adequate hedging but doesn't stop the number from driving a decision. Options add moneyness/theta decay on top of price drift, so a stale mark isn't just off — it can be structurally impossible.

**How to apply:** Before any position decision (sell/hold/roll/expire) on an option: (1) pull the live chain — last, bid, ask, OI; (2) sanity-check the mark against moneyness and DTE (deep-OTM + short-dated ⇒ near-zero; if the carried mark violates this arithmetic, it's phantom); (3) a zero bid means the position may be unsellable — disposition options collapse to "ride it." Never deliberate EV on an [INFER]'d option mark. Related: [[feedback_position_cost_basis_not_authoritative]], [[feedback_pull_live_primary_not_dashboard]].
