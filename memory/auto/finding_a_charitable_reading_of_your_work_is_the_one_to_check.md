---
name: finding_a_charitable_reading_of_your_work_is_the_one_to_check
description: When a reviewer explains your discrepancy in a way that credits you with sound method, that explanation is the least likely to be checked and the most costly to accept — verify it exactly as hard as an accusation.
metadata:
  type: feedback
---

A peer reconciling my base-rate table counted **2** observations above a cut where I had reported **1**, and wrote: *"I assume you excluded the observation under test from its own base rate, which is the right method — flagging only so the two counts don't read as a discrepancy later."*

**I hadn't.** The value was **14.5959×**; my cut was **14.6**; and **14.6 was the rounded display figure of that same observation.** I had printed a number at one decimal place, typed the printed number back in as a threshold, and the unrounded datum fell the other side of it. **The count was right by accident and the method I was being credited with was one I never applied.**

**Why this class is dangerous:** an accusation gets checked — being wrong is costly, so you verify. **A charitable explanation gets accepted**, because it costs nothing and confirms your competence. So the reading most likely to enter the record unverified is the flattering one. Here it would have hardened into "REGINALD applied leave-one-out" in a peer's registry, on a desk making a live threshold decision.

**The underlying arithmetic trap is worth its own line: a rounded display value is not the number.** Print at 1dp, reuse the printed figure as a cut, and you silently exclude the very observation you rounded.

**How to apply:**
- **When a reviewer supplies a reason for your result that you did not supply, go and check whether it's true.** Especially when it flatters. "I assume you did X, which is right" is a claim about your work that only you can verify.
- **Correct it even when the conclusion is unchanged.** Mine survived (99.4th percentile either way) — but the *method* attributed to me was wrong, and a peer had already banked it. **A number right by accident is a defect, because the accident is not repeatable.**
- **Never type a printed figure back in as a threshold.** Cut on the unrounded value, or state the cut to more precision than the display.
- **State both framings when an observation is in its own base rate**: including-the-test (2/166) and leave-one-out (1/165). The second is correct for "is this unusual?"; showing both makes the method visible instead of assumed.
- Related: [[finding_asymmetric_rigor_counterparty_claims]] (the inward-pointing sibling — verify the number that makes you RETRACT) · [[finding_number_carries_threshold_unit_source]] · [[finding_loadbearing_number_must_be_reproducible]] · [[finding_apparent_confabulation_is_often_a_baseline_mismatch]].
