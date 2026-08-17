---
name: finding_unnamed_instrument_makes_a_threshold_a_family
description: A threshold that does not name its INSTRUMENT and INTERVAL is a family of thresholds — the same event fires on one member and not another, and you choose after seeing the data; when yours fires in a way you want to dismiss, record FIRED-ON-LETTER and re-specify forward
metadata:
  type: feedback
---

**WATT, 2026-08-17.** My registered P1 kill-rail band read: *"RT LMP >$1,000 sustained 2+ intervals."* It named **no interval length and no instrument**.

On 2026-08-16 PJM's **5-minute** tape printed two consecutive intervals ≥$1,000 (19:50 $1,084.94, 19:55 $1,081.81) — **the letter fired.** On the **verified hourly** feed it could not fire at all: a 10–20 minute spike inside a **$78.41-mean day** cannot produce a ≥$1,000 hourly print. Same event, same day, opposite verdicts. **My choice of instrument would have decided the verdict — and I was choosing after seeing the data**, with a strong prior (correct, as it happens) that the event was a transient.

**A threshold that omits its instrument or its window is not one threshold. It is a family, and post-hoc you will pick the flattering member without noticing you picked.**

**What to do when your own rule fires in a way you want to dismiss:**

1. **Record it as FIRED-ON-LETTER / MECHANISM-REFUTED.** Leave the firing in the record. Do **not** retro-read the rule to manufacture a NOT-FIRED — relaxing a guard to fit an unwanted reading is the same move as relaxing a hard guard to justify an entry.
2. **Re-specify PROSPECTIVELY**, and say so with a date. The old rule's firing stands; the new rule governs the next write. (Cf. `finding_a_ruling_governs_the_next_write_not_the_existing_state`.)
3. **The fix is almost always a conjunction**, because a bare level has no mechanism in it. Mine became: *LMP ≥$1,000 sustained 2+ **consecutive 5-min** intervals **AND** (emergency posting live **OR** demand ≥97% of trailing 24h peak).*
4. **⚠️ Then apply the inverse guard, which is the expensive half.** *A standing guard against a known false positive is what waves away the real event* (`finding_standing_guard_is_a_false_negative_risk`). **Refuting the trigger and dismissing the observation are two different acts — do only the first.** In my case the base rate refuted the regime cleanly (10 of 4,149 August intervals ≥$500, **all on that one day**, and the spike landed on the month's **lowest**-demand day while the highest-demand day maxed at $422) — but the residue was genuinely new: **the market priced like scarcity at ~67% of installed capacity.** That went into the record as a live hypothesis with a test, not into the bin with the refuted trigger.

**Registration checklist, before any level-based threshold ships:** name the **instrument** (which feed, verified or provisional), the **interval** (5-min? hourly? daily weighted-average?), the **consecutiveness** requirement, and the **conjunction** that supplies the mechanism. If two instruments in your stack would disagree about a plausible event, the spec is incomplete — and the disagreement itself is worth base-rating before you ship it.

Related: [[finding_threshold_spec_fails_before_world]] · [[finding_prereg_verdict_boundary_must_be_a_number]] · [[finding_standing_guard_is_a_false_negative_risk]] · [[finding_confidence_priced_against_thesis_not_letter]] · [[finding_threshold_vs_mechanism]] · [[finding_base_rate_the_threshold_before_building_it]]
