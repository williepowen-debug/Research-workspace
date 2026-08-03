---
name: finding_per_share_figures_break_across_splits
description: Per-share figures spanning a stock split cannot be summed or compared; the RATIO to same-year EPS is split-invariant and is the portable unit
metadata:
  type: reference
---

**Any per-share series that crosses a stock split is not additive and not comparable across the split date — but a RATIO of two same-year per-share figures is, because the split cancels.** When assembling per-share effects across years, carry the **percentage**, not the dollar.

**Worked case (DEWEY DR-2, 2026-08-02, all [PRIMARY] 10-K disclosures):** disclosed EPS effects of hyperscaler useful-life changes.
- GOOGL Jan-2021 change: **+$2.98/diluted share** — against reported diluted EPS of **$112.20**. Both **pre-split** (Alphabet 20:1, July 2022).
- AMZN Jan-2020 change: **+$3.98/diluted share** — against reported diluted EPS of **$41.83**. Both **pre-split** (Amazon 20:1, June 2022).
- GOOGL Jan-2023 change: **+$0.24** against **$5.80**; META Jan-2025: **+$1.00** against **$23.49**. Post-split.

Summing the dollar column ($2.98 + $0.24 …) produces a meaningless number dominated by the pre-split entries — **$2.98 is ≈$0.149 in post-split terms, a 20× overstatement.** But **2.7% (2.98/112.20) and 4.1% (0.24/5.80) are directly comparable**, because numerator and denominator come from the same filing and the split cancels.

**How to apply:** before combining per-share figures across years, check for a split in the interval. Then either (a) split-adjust every figure to one basis, or preferably (b) **convert to a ratio against a same-year per-share denominator** and work in percentages. The ratio needs no adjustment and cannot be silently corrupted by a split you did not know about — which is the real hazard, since splits are rarely mentioned in the note you are reading.

**Generalizes beyond splits** to any per-unit figure whose denominator is redefined mid-series: per-share after a split/reverse-split, per-capita after a population rebasing, per-unit after a contract-size change. **Same-period ratios survive a denominator change; levels do not.**

Related: [[finding_number_carries_threshold_unit_source]], [[finding_relabeled_number_viral_stat]], [[finding_threshold_level_is_a_measurement_not_a_constant]], [[finding_rebased_metric_check_made_date]], [[finding_normalization_choice_picks_opposite_winners]].
