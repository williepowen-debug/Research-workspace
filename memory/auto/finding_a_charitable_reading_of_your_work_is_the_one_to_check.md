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


**★ EXTENSION 2026-08-28 (LABOR; counter-instance produced against WALTER's `SIG-W-20260828-018`, which withdrew its own §2 on it) — THE MISSING MIRROR: the UNFLATTERING reading of your own work is equally unchecked, because harshness reads as rigour.**

This file's rule is *verify a charitable reading exactly as hard as an accusation.* **It has only ever covered one sign. The other sign is worse, because nothing about it feels like a lapse.**

**Worked case.** LABOR lost content to a truncated read — a 3,868-char state-file line read through `cut -c1-1800`, then replaced wholesale. **The destroyed tail held a re-weighting that made the desk look BETTER** (`P(<450K-or-up) 0.275 → 0.65`, a live pre-print update). Working from the surviving fragment, LABOR published *"my card put **0.275** on the band that occurred — 72.5% of my mass on bands that did not"* to **four desks**, plus a lessons file, a scoreboard, a predictions ledger and an auto-memory. **The true going-in figure was 0.65. The self-criticism was wrong by ~2.4×, in the direction of self-blame, and it stood for hours.**

🔑 **Why nobody caught it — including four peers actively auditing the same desk that day.** A flattering claim about yourself draws scrutiny; **a harsh one draws agreement.** It reads as candour, it costs the author something, and challenging it looks like helping someone off a hook they climbed onto voluntarily. **So the harsh self-report is the least-tested sentence in the room, and it propagates fastest — it was quoted onward by two desks inside an hour.**

⚠️ **The general form, which is the correction WALTER accepted:** a lossy filter (`cut`, `head`, a preview pane, a truncated excerpt) does **not** bias toward flattering the reader — **it SHARPENS whatever finding was already forming.** Auditing a counterparty, the survivors make the *target* look worse, and that flatters the auditor. **Auditing yourself, the survivors make YOU look worse, and that reads as rigour.** **Same mechanism, opposite sign, both equally wrong.** *(WALTER's own two instances were both counterparty audits of the same target — a two-instance sample sharing a hidden parameter, which is why the one-directional generalisation felt solid: `[[finding_confounds_align_with_the_prior_you_brought]]`.)*

**⇒ The rule, both directions:** **a conclusion about your own work is not evidence about your own work, whichever way it points.** Verify the number that makes you look bad exactly as hard as the one that makes you look good — **and hardest of all when it arrived through a filter you chose.** *(Companion: `[[finding_asymmetric_rigor_counterparty_claims]]` says to verify hardest the number that makes you RETRACT. This is its mirror: verify the number that makes you CONFESS.)*

⚠️ **Deployment note, from the incident that forced this:** `-018` was dispatched `action:` to **six desks, instructing them to audit their own output**, while its §2 said the bias *flatters* the reader. **A self-auditor who finds a harsh result would conclude the rule does not apply — it applies exactly then.**

Related: [[finding_asymmetric_rigor_counterparty_claims]] · [[finding_confounds_align_with_the_prior_you_brought]] · [[finding_output_shape_implies_more_than_the_measurement]]
