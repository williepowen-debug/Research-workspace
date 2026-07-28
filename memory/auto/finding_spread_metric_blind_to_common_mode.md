---
name: finding_spread_metric_blind_to_common_mode
description: A spread/gap metric built to defeat one masking failure is structurally blind to the symmetric one — a difference cannot see a parallel move, and a ratio can print "improving" while every component worsens
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
