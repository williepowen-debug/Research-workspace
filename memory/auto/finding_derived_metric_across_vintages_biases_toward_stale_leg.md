---
name: finding_derived_metric_across_vintages_biases_toward_stale_leg
description: "A metric combining two legs of different vintages is biased toward the stale leg's regime — and the delta from fixing it is a BASIS CHANGE, never a threshold trigger"
symptoms: "spread/ratio/bound looks wrong but every leg checks out; the common-factor number changed and no market moved; min-across-legs; argmin picked the laggy series; one leg's as-of is older than the others; bound set by the leg that publishes slowest; residual attributed to the wrong leg"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b9d57092-feed-4612-8068-07dc7bb89182
  modified: 2026-08-04T15:15:24.416Z
---

A derived metric built from two data legs (spread, ratio, margin, gap) whose legs carry **different as-of dates** is not a measurement of now — it is biased in the direction of whatever regime the **stale leg** was drawn from, and the bias **grows the more the market trends**.

WATT 2026-08-04: `power_watch.py` reported the PJM spark spread as **+$43.86/MWh** by pairing a **deliv-7/22** power print with **8/4** gas. Same-vintage on-peak: **+$29.84/MWh** — a **~47% overstatement**, because the stale power leg came from a hotter regime. The instrument *printed a vintage-mismatch warning*, which had been read for weeks as a caveat rather than as an invalidation.

**Why:** the source lagged silently. The EIA ICE biweekly file's publication lag had grown to ~13 days; it still returned HTTP 200 and parsed cleanly. Nothing announces that a leg has gone stale enough to invalidate the derived number. See [[finding_partitioned_source_returns_stale_window_at_200]], [[finding_plausible_stale_value_evades_review]].

**The second-order trap is the expensive one.** Once corrected, the tempting move is to score the drop (+$51.95 → +$29.84, ~43%) against a registered *"compresses 50%"* trigger. That would be wrong twice over: the old figure was ICE peak-period OTC and the new one DM2 RT on-peak — **different products, not two points in one series.** A threshold measured across a basis change is not a measurement. Related: [[finding_normalization_choice_picks_opposite_winners]], [[finding_cross_entity_comparison_needs_same_perimeter]], [[finding_threshold_level_is_a_measurement_not_a_constant]].

**How to apply:**
1. Before reading any derived metric, **check the two legs' as-of dates**. If they differ materially, the number is not current — recompute same-vintage or refuse to print it.
2. When a fix changes a level, ask **"did the world move, or did my basis move?"** before scoring it against any trigger. A basis change must never fire a threshold.
3. Write the **basis onto the threshold spec** ("compresses 50% *measured on one consistent basis across 3+ sessions*"), so a future reader cannot silently compare across instruments.
4. If you have published the biased level to other agents, **send a publisher-side correction** — the stale figure is now load-bearing in someone else's file ([[finding_retired_threshold_has_no_publisher]]).

---

## Extension 2026-09-01 (BOND) — the SELECTION form: an extremum-across-legs estimator is set by the leg with the SHORTEST COVERAGE

The instance above is **contamination** — a stale leg drags a two-leg metric toward its own regime. There is a second, harder-to-see form where **every leg is individually correct and current-as-published**, and the estimator is still wrong.

**An estimator that SELECTS across legs — `min`, `max`, an argmin bound, "the common component is at most X" — does not average the vintage problem away. It concentrates it.** A leg whose endpoint stops earlier has, mechanically, had less time to move, so it produces a smaller delta — so **`min`-across-legs preferentially SELECTS the least-covered leg.** The bound then describes a publication calendar rather than a market, and **it moves when no data moves at all.**

**BOND 2026-09-01**, DM sovereign long-end cross-section (US/EA/UK/JP 10Y at four issuer primaries). The min-across-legs bound on the common factor printed **+8.2bp** — taken from the **UK** leg, which stopped **5 days early** (BoE publishes through 8/27; 8/31 was a UK bank holiday). Japan's implied *idiosyncratic residual* was **+3.2bp** with that leg in the set and **0.0bp** with it dropped. **The entire "Japan-specific" component was manufactured by a bank holiday.**

**Why it evades every check that catches the contamination form.** Each leg's value is right, current, and from its own primary. A freshness check on any single series passes. A vintage-mismatch warning of the kind that saved the WATT case never fires, because no leg is *stale* — they are merely **unequally covered**, which is a property of the SET, not of any member. Related: [[finding_instrument_cadence_cannot_resolve_the_claims_window]], [[finding_spread_metric_blind_to_common_mode]], [[finding_silent_blank_evades_review]].

🔴 **The bias has a fixed sign and it points at whatever you are grading.** A short-covered leg *shrinks* the bound, which *inflates* the residual attributed to the leg under test — so the error runs toward "this leg is idiosyncratic/special," which is usually the interesting-finding direction and therefore the one least likely to be challenged. In the BOND case it pushed toward the exact hypothesis a peer desk's verdict was about to be scored on. [[finding_measurement_bias_sign_is_fixed_harm_direction_is_not]], [[finding_confounds_align_with_the_prior_you_brought]].

**How to apply (in addition to 1–4 above):**
5. **Quote a cross-leg bound ONLY off a matched endpoint set.** If the legs cannot be matched, truncate the whole window to the laggiest leg and say so — never mix endpoints to keep a leg in.
6. **Print the per-leg lag beside the estimator, always.** A bound without its coverage table is not reviewable.
7. **Run the drop-one test.** Recompute the bound without the shortest-covered leg; if the answer moves materially, the bound was reporting a calendar. This is one line and it is the whole diagnostic.
8. **Report RANK and MEDIAN beside any min/max bound, never the bound alone** — rank is robust to unequal coverage in a way an extremum is not, and when bound and rank disagree the disagreement *is* the finding.
