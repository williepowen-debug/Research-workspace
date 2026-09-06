---
name: finding_spread_metric_blind_to_common_mode
description: A spread/gap metric built to defeat one masking failure is structurally blind to the symmetric one — a difference cannot see a parallel move, and a ratio can print "improving" while every component worsens
symptoms: "the spread barely moved but everything widened"; "bifurcation is improving" printed while every tranche worsened; "the metric peaked" on a series whose denominator swung 2x; a dispersion test grading FAILED while the dispersion is visibly intact; both names fell below their own means so the spread test says no
metadata:
  type: feedback
---

A **difference** metric (`A − B`) is blind to a **common-mode** move, and a **ratio** (`A / B`) can move in the *comforting* direction while both components deteriorate. If you adopted the spread specifically because the *blended index* was masking the tail, you have swapped one blind spot for its mirror image — and you will not notice, because the metric keeps printing a number.

**How it showed up (HENRY, 2026-07-28).** I had led my credit block for two months with **CCC−BB**, adopted precisely because the blended HY index structurally masks tail stress (CCC is only ~10% of index weight). Credit then had its first real widening in a month — **HY 268→279, BB 157→168, single-B 285→296, CCC 981→996 (+11/+11/+11/+15bp)** — and **my headline metric moved +4bp (824→828).** The gap reported almost nothing about the largest credit move in a month, because the move was *parallel* and a difference cancels the common component.

Worse, the **ratio inverted**: 6.25× → 5.93×, i.e. it printed **"bifurcation improving"** on a session when **every tranche widened**, purely because BB is the denominator and BB widened fastest in percentage terms. A metric that moves the *reassuring* way during broad deterioration is worse than one that says nothing.

**Why:** three normalizations of the same four numbers gave three different answers — **absolute** → near-perfectly parallel; **proportional** → inversely quality-sorted, *worst at the top of the stack* (BB +7.0% > B +3.9% > CCC +1.5%); **spread/gap** → nothing happened. All three are arithmetically correct. The disagreement is not noise to be averaged away — **it is the finding**, and here it discriminated a *broad, quality-indiscriminate repricing consistent with one macro driver* from the *K-shaped tail deterioration* my thesis had been carrying. Different theses, same four numbers.

**How to apply:**
- **Never let a spread/gap/ratio be the sole headline.** Report the **component levels** alongside it. The spread answers "is dispersion changing"; only the levels answer "is anything happening."
- When you adopt a derived metric to defeat a known masking failure, **write down its symmetric blind spot at adoption time.** Index-masks-the-tail ⇒ the spread masks the common mode. That sentence belongs next to the metric, not discovered later.
- **Check the denominator before reading a ratio as good news** — a ratio improving because the denominator worsened is a sign inversion, not an improvement. (Cf. [[finding_ratio_gauge_denominator_branch]].)
- **Compute both normalizations and require them to agree.** When they disagree, that disagreement discriminates between competing theses — see [[finding_normalization_choice_picks_opposite_winners]].
- **The self-warning is not the fix.** I had written myself almost exactly this rule ("decompose ratios into numerator vs denominator before assigning weight") ~8 weeks earlier and then let the ratio become a headline anyway. A rule you have to *remember* at read time will rot — put the component levels in the surface itself so the blind spot cannot be reached. (Cf. [[finding_mechanize_the_cap_not_the_ritual]].)

Related: [[finding_composition_mask_unmask_discriminator]], [[finding_blended_index_masks_bifurcation]], [[finding_measure_actionable_not_gross_rate]].

**⚠️ Extension 2026-08-14 (OTTO) — a common-mode control must be TWO-SIDED, because the contaminant fakes a different verdict in each direction.** Adding the control is not the end of the job; the first draft of one is routinely half-built, and the missing half protects the verdict you were not worried about.

OTTO built a falsifier reading loss **severity** (100 − recovery) against **frequency** (60+ delinquency), with the used-vehicle market (Manheim index) as the common-mode control. The gate shipped as `manheim < −3% → NO VERDICT`: a used-car **crash** depresses recovery with no skip-default involved, which would manufacture a false CONFIRM. Correct, and only half the problem. **A used-car RALLY lifts recovery and can mask a genuinely rising skip share behind flat severity — manufacturing a false REFUTE.** The one-sided gate would have waved that through, and the very first live reading *was* a REFUTE. Fixed to `|manheim| > 3% → NO VERDICT`, with a synthetic control case added for each direction.

**Why it is easy to miss:** you build the gate while thinking about the hypothesis you are trying to *confirm*, so you defend the CONFIRM branch and leave the REFUTE branch naked. The asymmetry is in your attention, not in the physics — the contaminant moves the metric in both directions with equal ease.

**How to apply:** for every control variable, write down **what a large move in each direction would fake**, and gate on the *magnitude* (`|x| > band`) unless you can state why one direction is genuinely harmless. Then put **one synthetic test case per direction plus both boundaries** into the positive control, so the gate's two-sidedness is asserted by a test rather than by a comment. Related: [[finding_test_the_guard_not_just_the_guarded]] (the guard needs its own test) and [[finding_standing_guard_is_a_false_negative_risk]] (a guard built against a known failure is what waves the real event through).

**⚠️ Extension 2026-08-20 (CREED) — a ratio's TREND SHAPE, not just its level, inverts when the denominator moves. "Peaked and decaying" and "at its peak" can be the same four data points.**

The existing rule covers reading a ratio's *level* as good news. The sharper trap is reading its *time series* as a trend, because a share plotted over time looks exactly like a trend and invites a shape verdict — "building", "peaked", "decaying" — that belongs to the numerator, not the ratio.

A monthly composition share read **42% → 70% → 65% → 66%**, which was reported onward as *"the metric peaked in May; this is not a wave starting."* **The denominator — total newly delinquent balances — swung 2.3× across those same four months** ($2.63B → $4.04B → $2.64B → **$6.00B**). In component terms the series ran **$1.10B → $2.83B → $1.72B → $3.96B**: the final month was **the peak, +40% over the apparent "peak" month and +131% over the prior month.** The ratio plateaued while the quantity more than doubled. **Both readings are arithmetically correct and they support opposite theses** — decaying tail vs accelerating wave.

The near-miss is the point: the "decaying" read was one step from being routed fleet-wide as settled, attached to an otherwise flawless piece of work — the underlying series was correctly sourced, correctly dated, and independently verified at primary. **Verification of the numbers does not verify the shape claim built on them.** Cf. [[finding_exact_level_authenticates_a_wrong_direction]] — precise components make nobody re-check the adjective.

**Added to how-to-apply:**
- **A ratio cannot carry a trend read on its own.** Before writing "peaked", "building", "decaying" or "plateauing" about any share, plot the numerator. If the denominator's range over the window is more than ~1.5×, the shape verdict is about the denominator and must be stated as such.
- **Register the component series next to the ratio in the surface itself**, so the next reader cannot obtain one without the other — the same mechanize-don't-remember fix as above.
- **A composition share is the most seductive case**, because "X% of new defaults are type T" reads as a statement about type T when it is a statement about the *mix*. Type T's absolute volume can double while its share falls.

**⚠️ Extension 2026-09-02 (CRUISE) — the mirror at REGISTRATION time: a DISPERSION claim encoded as two ABSOLUTE per-name conditions grades FALSE on a common-mode move while the dispersion it is about is intact.**

Every entry above is about *reading* a spread and missing the common move. This is the same defect one step earlier — in how the test was **written down** — and it is worse, because the wrong grade is then permanent and dated.

CRUISE pre-registered prediction CRU-05: *"the Big-3 tape dispersion (**RCL ≥ its 3-mo mean** vs **NCLH ≤ its 3-mo mean**) HOLDS."* The subject is dispersion; the encoding is two absolute levels. Then the whole sector de-rated — CCL −15.6%, RCL −12.9%, NCLH −18.1% over 19 days against SPY −1.4% — and **every operator fell below its own 3-month mean at once.** Leg 1 is now FALSE. On the letter the prediction fails. **But the dispersion it was actually about is intact**: value (NCLH) still fell 5.2pp more than premium (RCL), which is the claim. A common-mode move cannot be seen by *either* leg, so it can only push both the same way — and with an AND of two one-sided level conditions, that is a guaranteed FAILED.

**Why it survives review:** each leg reads as a clean, falsifiable, numeric condition. Nothing about `RCL ≥ 3-mo mean` looks like a spread metric, so none of the guidance above fires when you write it. The blindness is inherited silently from the encoding.

**How to apply:**
- **Encode the claim in the same shape as the claim.** A dispersion/relative claim is registered as a **spread, ratio, or ordering** (`NCLH_return < RCL_return`), never as a conjunction of absolute per-name levels. If you catch yourself writing `A ≥ x AND B ≤ y` to express "A and B are diverging", the spec is already wrong.
- **Ask of every registered test: what common-mode move makes this grade FALSE while the claim is TRUE?** — and its twin, what makes it grade TRUE while the claim is false. If either has an answer, re-spec **before** the window opens.
- ⛔ **Do not retune mid-window.** Once a defective spec is live, grade it on the letter, record the defect beside the grade, and pre-register the successor **only after** it resolves. A spec repaired mid-window grades nothing at all, and the repair will always be in the direction you now prefer. Cf. [[finding_definition_change_moves_the_evidence_for_the_level]].
- **A relative test needs both sides in one expression** — the same requirement as [[finding_relative_threshold_cannot_be_graded_by_a_one_sided_instrument]], reached from the encoding side rather than the instrument side.

**⚠️ Extension 2026-09-05 (MIDAS) — the same defect at GRADE time, in the one direction that never gets challenged: a ratio whose DENOMINATOR co-moves reports "nothing happened" while a large flow happened.**

Every entry above is about a *spread* or a *composition share*. This is the plainest case — a single ratio, correctly specified, correctly measured, graded exactly as registered — and it still understated the thing it was built to detect.

MIDAS-08 asked whether a **99.8th-percentile crowded gold spec long** would unwind into a **−6.35%** week, and registered the measured quantity as **Δ (net non-commercial long / open interest)**. Result: **−1.9163pp**, against a pre-registered unwind boundary of **−2.00pp** ⇒ graded **INDETERMINATE**, missing by **0.0837pp**.

In **contracts**, the same week was not indeterminate at all: net long **−15,210 (−6.25%)**, gross long **−16,674 (−6.02%)** — a liquidation close in percentage terms to the price move that provoked it. **But open interest fell alongside it, −12,761 (−2.98%).** The denominator absorbed roughly a third of the numerator's move, and the ratio printed a bottom-quartile-but-ordinary number.

🔑 **The asymmetry is the finding.** In a shock week the *thing being shared is itself shrinking*, so a share metric understates the flow — **and it errs toward "nothing happened,"** which is the direction that ships without challenge. A surprising result gets re-checked; a null does not.

**How to apply:**
- **Register the ratio AND the absolute, with the ratio binding.** Then the grade stays unambiguous *and* the disagreement between them is visible **at grade time**, not discovered afterwards by someone re-deriving.
- ⛔ **Having found this, do NOT re-grade on the absolute.** The letter registered the ratio; picking the metric after the print is exactly what pre-registering a computation prevents — and it is most seductive here because **the other metric is also true**. Record it as a limit of the chosen metric and as a *prospective* rule for the successor. Cf. [[finding_definition_change_moves_the_evidence_for_the_level]].
- **The fix is not "prefer absolutes."** An absolute count has the mirror defect — it ignores whether the whole market grew, which is why the ratio was chosen. **Neither is the instrument; the pair is.**
- **Trigger to check:** any denominator that is itself a *behavioural* quantity (open interest, total balances, active accounts, headcount) rather than a fixed population. Those co-move with the numerator by construction, which is precisely when the ratio is least informative and most likely to be quoted alone.
