---
name: finding_base_rate_the_threshold_before_building_it
description: "Before registering a threshold, compute its base rate AND its separation between the states it must distinguish — a LEVEL bar is usually a descriptor, and 'don't build it' is a legitimate, common answer."
metadata:
  type: feedback
---

**"Register a threshold" is a hypothesis, not a task. Test it before you build it, and be willing to conclude that it should not exist.**

Two numbers decide it: the **unconditional base rate** (how often is this condition true at all?) and the **separation** (how much more often is it true in the state you are trying to detect than outside it?). **A trigger with low separation is a description of the world wearing threshold clothing** — when it fires it tells the recipient nothing.

**Incident (LABOR, 2026-08-07).** One pass base-rated six candidate thresholds against 36 years of monthly data. Three results:

- **Level bars were never triggers.** Two live escalation thresholds keyed to an unemployment *level* — one at 4.7%, one at 5.0% — were true in **65%** and **58%** of all months since 1990, separating the target state by only **+12.9pp** and **+13.8pp**. The *change* form of the identical series separated **+50.7pp**. **The series was never the problem; the LEVEL construction was.** Replacements built on a drawdown separated **+53 to +63pp** at base rates of 8-12%.
- **Two of three requested thresholds were killed by measurement.** One would have keyed on a series that *lags* the one already triggering (peak correlation at +1 month; a signal unique to it was a false positive ~9 times in 10). The other keyed on a series whose declines separate the target state by **+0.0pp** at one bar and **−4.0pp** at another — *it fires more often outside the state it was meant to detect.*
- **The same measurement prevented a scoring error.** The largest single sector loss in that month's data sat at the 5.7th percentile of its own history and was the obvious candidate to escalate a tracked vector. Because that series carries no information about the target state, **scoring it would have imported noise** — so the vector was held. **An unusual level is not a signal; only a level that discriminates is.**

**How to apply:**
1. **Compute base rate + separation before shipping any threshold.** Under ~20pp separation, it is a descriptor. Do not ship it.
2. **Prefer deltas and drawdowns to levels** unless the level *is* the decision boundary (a stop, a covenant, a margin call). Levels drift with regime; changes do not ([[finding_escalation_line_needs_delta_not_level]]).
3. **Record the NO with its numbers.** A killed threshold is a permanent saving, and the written record stops the same idea being re-proposed next quarter by someone reading the same suggestive print.
4. **Base-rate conjunctions JOINTLY, never by multiplying legs.** A compound measured 8.2% against a naive product that was nowhere near it ([[finding_compound_gate_jointly_unsatisfiable]]).
5. **Check every new spec against the live print: if it fires the day you wrote it, suspect yourself.** Not firing today is weak evidence you did not reverse-engineer it from the data in front of you.
6. **When a discredited gauge is still what the audience watches, demote rather than delete** — keep publishing it, move the trigger elsewhere, and say plainly that it no longer fires anything.
7. **Never re-point a LIVE prediction onto a replacement gauge you just built, in the direction that makes it fire.** Fix the instrument for the future; let the open call resolve on the letter it was written with ([[finding_confidence_priced_against_thesis_not_letter]], [[finding_claim_outlives_its_discredited_instrument]]).

Related: [[finding_threshold_spec_fails_before_world]] · [[finding_base_rate_the_instrument_before_its_event_table]] · [[finding_inherited_default_threshold_is_a_silent_decision]] · [[finding_threshold_level_is_a_measurement_not_a_constant]] · [[finding_ratio_gauge_denominator_branch]]
