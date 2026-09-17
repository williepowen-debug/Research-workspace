---
name: finding_one_percentile_rule_is_several_rules_across_strata
description: "A percentile threshold applied across strata is not one rule — it is several rules wearing one name, because a percentile is a statement about a DISTRIBUTION'S SHAPE and the shapes differ. Measure the bite per stratum before adopting it, and never base-rate it pooled."
symptoms:
  - "we replaced the min with a 15th percentile so it's better calibrated"
  - "the new threshold is looser across the board"
  - "same rule, applied per category"
  - "I'll base-rate the new gate on the pooled sample"
  - "it barely changed anything at that tenor"
  - "one consistent percentile cutoff for every bucket"
metadata:
  type: finding
---

**A percentile is a claim about the SHAPE of a distribution, not a level.** Apply one percentile rule across strata whose distributions have different shapes and you have quietly authored several different rules and given them one name.

**BOND, 2026-08-27.** A ruled recalibration replaced a trailing-12 **min**-based indirect bar with a **15th-percentile** bar, the stated point being a looser, better-calibrated trigger. Measured at adoption, the new bar sat above the old min by:

| stratum | bite |
|---|---:|
| 2Y | **+4.84pp** |
| 7Y | +0.82pp |
| 5Y | **+0.24pp** |

**At the 5Y it is barely a change at all** — that tenor's trailing-12 distribution is bunched hard against its own bottom, so the 15th percentile and the minimum nearly coincide. The same sentence produced a materially looser gate at one stratum and a cosmetic one at another.

**⇒ THE BASE-RATING MUST REPORT HIT-RATE AND SEPARATION PER STRATUM. A pooled figure averages several rules and describes none of them.**

## Two halves worth separating

**(a) The uneven bite was invisible in the spec and appeared only on computing the numbers.** Nothing in the written rule hinted that one stratum would barely move. **Adopting a recalibration without measuring its bite per stratum is adopting an unknown** — the spec reads uniform precisely because a percentile *sounds* uniform.

**(b) It surfaced because the adoption's COUNTERFACTUAL was computed rather than asserted** — *"would this have fired on the prints I missed?"* That same check caught a second figure already written into the draft from memory. **Compute the counterfactual; it audits the rule and the author at once.**

⚠️ **Generalises past percentiles to any distribution-relative threshold** — z-scores, IQR fences, "top decile," rank cutoffs. Each is a shape claim, and shape varies by stratum.
