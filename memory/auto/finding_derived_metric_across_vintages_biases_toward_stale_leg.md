---
name: finding_derived_metric_across_vintages_biases_toward_stale_leg
description: "A metric combining two legs of different vintages is biased toward the stale leg's regime — and the delta from fixing it is a BASIS CHANGE, never a threshold trigger"
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
