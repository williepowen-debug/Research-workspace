---
name: feedback_register_the_call_even_when_you_expect_to_lose_it
description: "Register the falsifiable call even when you expect to lose it — a wrong prediction with an honestly-stated price is an ASSET, and the calibration record is the only thing that turns individual sessions into collaboration and learning over time"
metadata:
  node_type: memory
  type: feedback
---

**Will, 2026-08-21:** *"even if the predictions are wrong its still important. Over time it will help us collaborate and learn."*

**The prediction canon is almost entirely one-directional.** `FORGE/PREDICTION_DISCIPLINE.md` carries 20+ registration rules and every one of them is a brake: base-rate before freezing · check the gate can fire · *"don't build it" is a real answer* · confidence priced against the letter, not the thesis. All correct. **But taken alone they only ever push in the direction of registering FEWER things, and nothing in the canon names the cost of that.** This memory is the counterweight, and it comes from the operator.

**Why it matters — the arithmetic, from BOND's own book (2026-08-21).** 15 resolved predictions, 9 FALSE / 6 TRUE. Bucketed by stated confidence:

| stated | n | hit-rate |
|---|---|---|
| 30–49% | 4 | 25% |
| **50–69%** | **11** | **27%** |
| 70–89% | 3 | 100% |

**The 50–69% band is the finding: 11 calls, ~6 expected hits if calibrated, 3 actual.** That is systematic overconfidence, it is large, it is actionable *(price the next one ~20pp lower than instinct)* — **and it did not exist until it was computed, because it is a property of the SET, not of any row.** Every single one of the 9 "wrong" predictions is load-bearing in it. **A desk that had registered only its confident calls would have a book of 3 rows, all TRUE, and would know nothing about itself.**

The same session produced the smaller version of the same point: two consecutive auction predictions both landed on the wrong side of a benign print, and *that pairing* — not either row — is what surfaced a possible directional bias in how this desk prices auction demand.

**Why the failure mode is invisible from inside.** Under-registration never announces itself. There is no alarm for a prediction not made, no stale row, no rc=1 — the book simply stays small and every remaining row looks fine. **An error-correction culture drifts into an error-AVOIDANCE culture without any step where that decision is visibly taken.** The tell to watch for: a heavily-caveated session with a nearly-empty prediction book during a week dense with catalysts. *(BOND: the book was EMPTY 8/15→8/18, with two frozen tests running and nothing in the live regime falsifiable on a desk-authored instrument.)*

**How to apply:**
1. **Adjust the PRICE, never the decision to register.** Uncertain is not a reason to withhold — it is the information. "I think 35%" is a publishable prediction; "I'm not sure enough to say" is not a position, it is an absence.
2. **A FALSE at 35% is a WELL-CALIBRATED prediction, not a miss.** Score the book, not the row. Only the aggregate can be right or wrong about you.
3. **Deliberately fill the empty ends of your own curve.** High-confidence structural calls and sub-40% long-shots are the two bands that stay empty by default, and they are the two that most constrain the fit.
4. **Register PRE-PRINT, always.** A prediction is only honest before the event; afterward it is a description. This is what makes the record usable by *other desks* — the collaboration half of Will's sentence.
5. **The brakes in `PREDICTION_DISCIPLINE.md` govern HOW to specify a call, not WHETHER to make one.** *"Don't build it"* is a real answer about an **unfireable gate** — never about an uncomfortable one.

**The asymmetry that settles it:** a badly-*specified* prediction is a defect that costs a session to fix. A prediction never *made* costs a permanent hole in the calibration record that no later work can fill, because the moment it could have been registered honestly has passed.

Related: [[finding_base_rate_the_threshold_before_building_it]] · [[finding_confidence_priced_against_thesis_not_letter]] · [[finding_calibration_discount_regime_conditional]] · [[finding_compound_gate_jointly_unsatisfiable]]
