---
name: confidence-priced-against-thesis-not-letter
description: "A prediction's confidence gets priced against the thesis you MEANT, but it resolves on the letter you WROTE — if the letter is weaker, it fires in worlds where the thesis is wrong and banks a meaningless CONFIRMED; test by asking what the letter does if the thesis is false"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7af368f3-8e51-4dd5-8151-9208a3303ecc
  modified: 2026-07-27T20:31:05.494Z
---

You price a prediction's confidence by thinking about the **thesis** ("does the compounding redemption queue persist?"), then write a **trigger** that is operationally convenient. Those two drift apart, and nothing in the normal review loop compares them — you re-read the trigger for *measurability*, never for *strength*. When the letter is materially weaker than the thesis, the trigger fires in worlds where the thesis is plainly wrong, and you bank a CONFIRMED that means nothing.

**Why:** BROCK's BRK-30 was priced at 65% against "the queue persists," but its letter fired on **<100% satisfaction at any ONE of five funds** — a bar so low that 5 of 5 already cleared it at registration, and a fund going 10%→6% demand (a large improvement) would still fire it. It would have resolved CONFIRMED in a substantially *clearing* market. The re-spec built to test the actual thesis priced at **45%**. Same world, same evidence, **20 points apart** — that spread *is* the gap, made visible only because both were written down.

The tell that it is systemic rather than one sloppy row: the **same day**, in the same domain, a second trigger (a redemption register's "≥2 vehicles gated simultaneously") turned out to fire **7-fold on day one**. Two triggers, same channel, mis-specified in the **same direction** — too easy to fire. That is a habit in how you write triggers where you already believe the thesis, not bad luck.

**How to apply:**
- At registration, run the **inversion test**: *describe a world where my thesis is FALSE. Does the trigger still fire?* If yes, the letter is too weak — tighten it or say plainly that it is a weak proxy and price it accordingly.
- Check the **direction of the skew across your book**. Triggers written on a channel you're already convinced about skew easy-to-fire; count them. n≥2 in one channel is a pattern to fix at the authoring step, not a coincidence.
- When you find the gap in an **open** prediction, do **not** re-base it — a re-based metric imports the premise that forced the re-date, and the replacement is often already true at the original Made_Date (see [[finding_rebased_metric_check_made_date]], [[finding_threshold_level_is_a_measurement_not_a_constant]]). Let it resolve on its letter and register a **separate companion** that tests the spirit. Running both is the point: a fired letter plus a no-call companion is **not a contradiction, it is the diagnosis** — "the trigger fired but the thesis did not advance."
- Beware the primitive itself. A ratio whose denominator is the quantity you care about carries no independent information, and may blend a behavioural signal with a **policy choice** (satisfaction = offer ÷ demand mixes investor behaviour with the manager's cap decision). Measure the behaviour; carry policy as a separate labelled leg. See [[finding_ratio_gauge_denominator_branch]], [[finding_composition_mask_unmask_discriminator]].

Distinct from [[feedback_forward_discovery_prediction_spirit]] (letter satisfied by data that pre-dates the prediction) and [[finding_threshold_spec_fails_before_world]] (spec unmeasurable). Here the letter is perfectly measurable and genuinely satisfied — it is just a **much smaller claim** than the confidence was priced against. Related: [[finding_threshold_vs_mechanism]].
