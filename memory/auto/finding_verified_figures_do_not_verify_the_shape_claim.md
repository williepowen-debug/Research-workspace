---
name: finding_verified_figures_do_not_verify_the_shape_claim
description: Verifying every figure never verifies the SHAPE claim laid across them — name the denominator before writing "peaked"/"rising"/"plateaued"
metadata:
  type: feedback
---

**Verification of the numbers does not verify the shape claim built on them.** A *shape claim* is a verdict about the SERIES rather than about any figure: **"peaked", "rising", "plateaued", "not a wave starting", "the trend has turned", "decaying"**. Every input can be correctly sourced, correctly dated, correctly framed — and confirmed at primary by the domain owner — while the shape verdict laid over them is **exactly backwards**, because no per-figure check ever looked at it.

**Why:** a per-figure verification certifies its OBJECT, not the claim assembled from several objects. The sibling of [[finding_verification_zero_is_ambiguous]] (*a check certifies its SCOPE, not your capability*). **And the failure is invisible rather than careless — a share plotted over time looks exactly like a trend and invites a shape verdict. The chart shape and the risk shape are different objects that render identically.**

**How to apply:** before writing any shape word, run **three** questions.
1. **Is the series a RATIO or a QUANTITY? If a ratio, NAME THE DENOMINATOR AND CHECK WHETHER IT MOVED.** A share can plateau while the thing it measures doubles.
2. **Does the same shape hold on the underlying QUANTITY?** If you can't answer, **don't write the shape word** — report the levels and say the shape is ungraded.
3. **🆕 DOES YOUR DELTA CLEAR THE INSTRUMENT'S OWN NOISE?** Compute the series' stdev over a comparable span **before** the delta earns a shape word. A two-point comparison across a noisy series manufactures shapes in whichever direction the endpoints happen to fall — **and it will do so twice, in opposite directions, without either read looking wrong at the time.**

**Bought 2026-08-20 (WALTER, corrected by CREED, the trigger's owner, at the primaries).** `SIG-W-20260819-021` published *"the metric PEAKED IN MAY — 70 → 65 → 66 — this is not a wave starting."* Every share figure and every date was correct; CREED re-read all four Trepp PDFs and confirmed so. **But the denominator moved 2.3×** ($2.62B → $6.00B newly-delinquent), so **in dollars the peak was JULY at $3.96B — +40% vs May, +131% vs June.** Backwards on the measure carrying the risk.

⚠️ **The propagation asymmetry is what makes this expensive: the shape word is the QUOTABLE part.** It led the entry-point handoff, it is in the BOARD **filename** (unrenameable — delivered handoffs and `delivery_log` rows cite the path), and it travelled further than any figure in the signal. **The most memorable sentence gets the least verification and the widest distribution. Invert that.**

**Companion, same day, same desk:** *correction confers no credit on what comes next* — [[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]. **The instrument you flee to deserves the audit you gave the one you left**, and being right about the last number is a terrible prior for the next one.

Related: [[finding_normalization_choice_picks_opposite_winners]] · [[finding_level_without_a_reference_has_two_failure_modes]] · [[finding_rising_stock_flat_inflow_means_slower_outflow]] · [[finding_cross_entity_comparison_needs_same_perimeter]]


---

**EXTENDED 2026-08-20 PM (CREED, on its own surface this time — the shape trap is not only about ratios).** CREED's S8a vector (VNQ vs SPY trailing-3mo relative) carried **two** shape claims in three weeks — 7/27 *"+2.04pp, 12pp away AND RECEDING"* and 8/20 *"−0.34pp, DECAYING, direction reversed."* **Both were withdrawn.** Neither involved a moving denominator; the series is a plain difference of two returns. **The defect was NOISE:** 10-session stdev **2.01pp**, full-sample **4.70pp**, against a like-for-like move of **−1.55pp** — *inside one stdev* — which also concealed a round trip (low −4.30pp, then eight consecutive sessions back up). **A quantity with no denominator problem still cannot carry a two-point trend read.**

⚠️ **AND THE SHARPER HALF — A ROBUSTNESS CHECK CERTIFIES ONLY THE DIMENSION IT TESTED.** The 8/20 session **did** test robustness: *"negative on BOTH bases, so the sign is robust to basis choice."* **That check ran, passed, and was TRUE.** It simply wasn't the binding constraint — **nobody tested the WINDOW START**, and moving it ±9 sessions swung the same reading **−0.78pp → +2.80pp, crossing zero six times.** A *passing* robustness check is more dangerous than none, because it discharges the felt obligation to keep looking. **Before resting on a robustness result, name the dimensions you did NOT vary.** Direct sibling of [[finding_verification_zero_is_ambiguous]] in its positive form: **a check that PASSES also certifies only its scope.**

**Third consequence, same session:** the same measurement was described as *"12pp away"* from its band — safe-sounding — while the band had been **breached 78 days earlier** and the series' stdev (4.70pp) put the reading **~2.1 sigma** from it. **A distance is not a margin until you price it in the instrument's own volatility.** See [[finding_distance_to_a_threshold_is_a_claim_about_its_basis]] and [[finding_base_rate_the_threshold_before_building_it]].
