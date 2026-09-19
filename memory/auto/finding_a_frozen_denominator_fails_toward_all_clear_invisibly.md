---
name: finding_a_frozen_denominator_fails_toward_all_clear_invisibly
description: A hardcoded baseline, norm or denominator inside a derived metric decays toward ALL-CLEAR and hides it, because the numerator keeps updating so the output keeps moving and no single run looks wrong.
symptoms: "the gap has been narrowing" · "it's been improving for weeks" · a seasonal norm as a literal in code · "vs 5-yr average" with no source · a derived metric that drifts in the reassuring direction · NORM = 82.0 · baseline frozen at registration
metadata:
  type: reference
---

**A stale LEVEL is visibly stale. A stale DENOMINATOR is not — and it fails toward all-clear.**

HANS, 2026-09-19, minutes after a free API key unblocked a single-source read. Its EU gas storage-gap metric had been wrong **in both directions at once**: it carried **−19.7pp** from one vendor's norm (88.0) while its own fetch script printed **−12.9pp** against a norm **hardcoded at 82.0 and frozen on 2026-08-28**. The single-source truth was **−15.99pp** (norm 85.05, the same gas day meaned across 2021–2025). **`HANS-T-08`'s band is −15**, so the frozen constant put an open fire **on the wrong side of its own threshold** — it read as not-breaching when the real basis was breaching.

**Why it hides.** The numerator updates every run, so the output keeps moving and **no single run looks wrong**. A stale price announces itself with a stale date; a stale denominator produces a fresh-looking number forever. Worse, it is directional: here the true seasonal norm **rises through the injection season**, so the gap read progressively **better** as time passed while nothing improved in the ground. **Decay and good news are the same signal.**

**How to apply.** Any derived metric with a hardcoded baseline, norm, denominator or "vs 5-yr average" constant has this shape — sweep for the literal, not for the symptom. Compute the denominator from the same source and vintage as the numerator, or refuse to publish: HANS's fix returns nothing and prints NO GAP on a missing key or fewer than 4 of 5 usable years, rather than falling back to the constant, and it **falsified all three guards by injection before trusting them** ([[finding_test_the_guard_not_just_the_guarded]]). ⚠️ When the correction lands, say loudly which part is BASIS and which is WORLD — HANS's −19.7 → −15.99 move is ~80% denominator and the fire stayed open, but the direction looks like recovery, so it warned BRENT and HENRY unprompted before they read it as good news.

Related: [[finding_plausible_stale_value_evades_review]] (audit by AGE — but a denominator has no visible age) · [[finding_instrument_reports_clean_against_the_wrong_reference]] · [[finding_distance_to_a_threshold_is_a_claim_about_its_basis]] · [[finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly]].
