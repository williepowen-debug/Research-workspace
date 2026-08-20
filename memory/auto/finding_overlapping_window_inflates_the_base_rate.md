---
name: finding_overlapping_window_inflates_the_base_rate
description: "A rolling-window statistic sampled faster than its window shares most of its data with its neighbour — dispersion survives this, but the EXCEEDANCE COUNT over-counts by roughly the overlap factor, so a threshold base-rated on it looks far better calibrated than it is"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 140e8d6d-b26c-42d3-a5f8-3870c6804f67
  modified: 2026-08-20T13:04:15.765Z
---

When someone hands you a **rolling** statistic — a 4-week rolling sum sampled weekly, a 30-day moving average sampled daily, a trailing-12 sampled monthly — the observation count they quote is **not** a count of independent draws. A 4-week sum sampled weekly shares **75% of its data with its neighbour**: 1,128 weekly periods contain only **~281 non-overlapping 4-week blocks**, not 1,125 independent ones.

**Why this is easy to miss: it corrupts one statistic and leaves the other one fine.**

- **Dispersion survives.** σ, percentiles, and the shape of the distribution are consistent estimates off the overlapping series (with reduced effective sample). A σ table computed this way is usable as sent — which is exactly why nothing looks wrong.
- **The exceedance count does not.** One genuine extreme *episode* produces **up to N consecutive breaches** for an N-period window. A naive count reads that as N events. So the firing rate is inflated by roughly the overlap factor.

**And the error has a direction.** It makes the threshold look **more frequently exercised — i.e. better calibrated — than it is**, so a bar advertised as "fires ~X times per decade" is actually looser than advertised. For any trigger meant to detect a rare adverse event, that is the dangerous direction: the bar passes review on a firing rate that was never real.

**The fix is a procedure, not a caveat.** Before setting any threshold on a rolling series, get exceedance counts computed **both ways** — all overlapping observations **and** de-clustered episodes (collapse consecutive breaches into one event) — and set the bar against the de-clustered number. If the two counts differ by ~the window length, the overlap is doing all the work.

**Two companions that travel with this:**
- **Check the skew before assuming a symmetric bar is admissible.** If mean ≠ median, or one tail sits further from the median than the other, then at any *k* the two sides of a ±kσ bar have **different** exceedance rates. Quote the two sides as separate numbers with separate base rates. (Found the same session: a flow series whose fat tail was on the selling side — good for a detector aimed at the sell side, fatal to a symmetric spec.)
- **Centre the bar on the series' own centre, never on zero,** when the series has a structural drift. A zero-centred bar on a structurally-positive series fires one direction constantly and the other almost never, and reports that structural property as signal.

Found 2026-08-20 (BOND↔SAM), setting a foreign-flow threshold off a correctly-computed σ table. The dispersion answer was right and the ask was answered well; the overlap only bites at the step *after* it. Sibling of [[finding_base_rate_the_instrument_before_its_event_table]] (base-rate before reading events) and [[finding_base_rate_the_threshold_before_building_it]] — this is the n+1: **base-rating is not enough if the base rate itself is computed on overlapping windows.** Related: [[finding_ranked_head_sample_is_not_the_population]], [[finding_unnamed_instrument_makes_a_threshold_a_family]].

**Why:** an inflated firing rate is invisible at review — every number in the table is individually correct, and the defect lives in the counting convention, not in any value.

**How to apply:** when base-rating any threshold, first ask *"is the underlying series a rolling window sampled faster than the window?"* If yes, de-cluster before counting, and set the bar against the de-clustered count. State the effective n, not the raw n.
