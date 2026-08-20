---
name: finding_distance_to_a_threshold_is_a_claim_about_its_basis
description: "Publishing how far a metric sits from a registered trigger asserts the grading basis, not just the price; read the row's value_basis and sustain_unit before quoting a distance."
metadata:
  type: feedback
---

**A "we are X% away" figure is a claim about the GRADING BASIS as much as about the level, and the basis is usually a column you did not read.**

**Bought 2026-08-19, by WALTER, against the single number it had just told the operator to watch.** `REG-T-02` is `WAL-PRICE < 78`, sustain 1. WALTER pulled an intraday quote, computed **2.00% away**, published it to STATUS and to Will as *"the closest live thing on the board… it fires on one print."* At closeout it re-pulled post-close and found **WAL closed $80.40 = 3.08% away.** The registry row it had already opened that session carried, two columns over:

- `value_basis: regular-session close, unadjusted, per-share`
- `sustain_unit: consecutive daily closes`

**Intraday prints do not grade that trigger at all.** The distance was not merely stale — it was computed on an instrument the gate does not read.

**The compounding error: a TREND built across mixed bases.** WALTER also published *"it tightened at EVERY reading"* — 5.5% → 4.23% → 3.53% → 2.79% → 2.00% — a series mixing two prior closes with three intraday reads. **The actual close came in WIDER than two of the intraday points underneath the trend.** The narrower, gradeable, still-true statement was `8/18 close 4.23% → 8/19 close 3.08%`. **A monotone sequence assembled from different bases is not a trend; it is a sampling artifact that happens to point somewhere.**

**Why this is not just "quote closes":**
- The failure is **directional and flattering** — an intraday extreme is by construction at least as close to the trigger as the close, so a mixed-basis distance is **biased toward looking more urgent than it is.** Nobody re-checks a number that is already alarming.
- It is **self-inflicted by partial reading.** The row was open. `trigger_id`, `metric`, `threshold_op` and `threshold_value` were read; `value_basis` and `sustain_unit` were not. **Reading the first four columns of a threshold row feels like reading the row.**
- WALTER had flagged **the same registry-basis-vs-tool class in three RED triggers hours earlier** (`RED-FT-03/04` settlement-vs-daily-bar, `FT-06` VIXCLS-vs-`^VIX`) and then committed it itself. **Diagnosing a class does not immunise you against it.**

**Do this:** before publishing any distance-to-trigger, read the row's `value_basis`, `sustain_unit` and `exit_condition`. Quote the distance **on the basis that grades**, name that basis in the same sentence, and if you only have an off-basis read say so rather than converting it. **Check the exit too** — a trigger between its fire and exit levels (WAL sat $1.50 under a `≥81.90 × 3 closes` exit) is in a different state from one simply "approaching."

Related: [[finding_registry_names_a_concept_tool_resolves_an_instrument]] · [[finding_unnamed_instrument_makes_a_threshold_a_family]] · [[finding_exact_level_authenticates_a_wrong_direction]] · [[finding_number_carries_threshold_unit_source]] · [[finding_standing_guard_is_a_false_negative_risk]] · [[finding_prereg_verdict_boundary_must_be_a_number]]
