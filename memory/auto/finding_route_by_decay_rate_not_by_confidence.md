---
name: finding_route_by_decay_rate_not_by_confidence
description: "A desk built to not-be-wrong will be right and late. Sort inbound by how fast its value DECAYS, not by how confident you are — a stated caveat is what makes fast routing safe."
symptoms: "correct but shipped after the move; we were right and it did not matter; held for confirmation and missed the session; you cannot position on a refusal"
metadata:
  node_type: memory
  type: finding
  modified: 2026-08-31T23:21:45.000Z
---

A verification-first desk optimises for **not being wrong**, which systematically converts tradeable items into accurate post-mortems.

**Worked instance (WALTER, 2026-07-31 → validated 2026-08-02).** 7/31 produced a great deal of correct *"unconfirmed / claim-only / not established"*. The one genuinely actionable item — the LTA split (hyperscalers contractually insulated while the exposed buyer and the seller take the hit) — shipped at 23:59Z on 7/3–7/9 data, **six hours after the session that had already traded it closed** (AMZN +15.32 / AAPL −7.35 / MU −5.90). **You cannot position on a refusal.**

**Validated on its first live test, 8/02.** `SIG-W-20260802-005` (US yen intervention) shipped FT-sourced with *"no official confirmation"* as its **stated central caveat** — Bessent's official statement resolved it **~1 hour later**, and `SIG-W-20260802-011` shipped the resolution as its own signal. Holding for confirmation would have delivered both an hour later with zero gain; because the caveat was **written into the packet**, the confirmation **closed a loop instead of exposing a miss**.

**Why:** value decay and confidence are independent axes, and only one of them has a clock. An item whose value decays (a tradeable mechanism) loses everything while you verify; an item whose value is durable (a correction, a guard) loses nothing. Sorting by confidence therefore delays exactly the items that cannot afford it.

**How to apply:** **sort inbound by DECAY RATE, not confidence.** Route decaying items **faster at lower confidence**, with the uncertainty **stated in the packet** — a written caveat is a repair instruction, and it is what makes fast routing safe. Let durable items wait for the check. Never treat "we were right" as the score when the horizon had already passed.

Related: [[finding_imperfect_level_to_the_right_owner_beats_a_perfect_one_to_nobody]] · [[feedback_single_source_liveevent_is_a_lead]] · [[finding_market_ignoring_is_not_market_refuting]] · [[finding_deferral_rule_hides_its_own_cost]]
