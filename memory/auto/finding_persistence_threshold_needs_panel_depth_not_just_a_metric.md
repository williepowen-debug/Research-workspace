---
name: finding_persistence_threshold_needs_panel_depth_not_just_a_metric
description: "A threshold spanning N consecutive periods cannot fire on a panel whose units are observed fewer than N consecutive times — the metric exists, the base rate is computable, and '0 of N fired' reads as a calibrated negative when it is a structural impossibility"
symptoms: "zero fires since registration, threshold never trips, 0 of 9 vehicles, consecutive-quarter rule never satisfied, panel looks fully populated, most units have one or two observations, in-sample threshold, design statistic not a base rate"
metadata:
  node_type: memory
  type: finding
---

**A persistence threshold has two requirements, and everyone checks only the first:** the panel must carry the *metric*, and each unit must be observed *at least as many consecutive times as the threshold spans.* When depth < span, the rule is **untrippable by the panel's shape**, not by the world's behaviour — and it produces the most convincing possible negative.

**Worked case (BROCK, 2026-09-03, WQ-158).** A redemption-gate register carried *"≥3 consecutive sub-100% satisfaction quarters"* across **9 vehicles**, reported as **"0 of 9 fired."** An external reviewer (via PROME) correctly flagged the *levels* as in-sample design statistics. The denominator audit found something worse:

- Of 9 vehicles, **2 cannot produce the metric at all** (one has no redemption mechanism; one is restricted multi-year with no cap/request structure).
- **3 more have no measured cell** — their value is derivable only by *assuming* the fund filled exactly to its cap.
- The honest panel is **6 measured cells across 4 vehicles.**
- 🔑 **Exactly ONE vehicle had ever been observed 3 consecutive quarters, and it reached 3 on the day of the audit.** Its own sub-100% run was **2**.

⇒ **A 3-consecutive rule was being graded against a panel that had never observed 3 consecutive quarters anywhere.** Zero fires was guaranteed at registration.

**Why it survives every audit.** The panel *is* populated — 9 rows, real vehicles, real percentages. Row-counting passes. Field validation passes. You can even compute a base rate per the discipline in [[finding_base_rate_the_threshold_before_building_it]] and get a sane-looking number, because the base rate is computed on *cells*, while the threshold consumes *runs*. **Nothing in the instrument reports the depth-per-unit distribution**, which is the only statistic that decides gradeability. Cf. [[finding_banded_threshold_with_no_metric_surface_is_untrippable]] — there the metric surface is absent; **here it is present and shallow**, which is far more convincing.

**The reporting harm is the real cost.** *"0 of 9"* is read by every downstream consumer as *the world is not doing this.* It actually means *this panel cannot see it.* An impossibility and a calibrated negative are indistinguishable from the output alone — the same shape as [[finding_option_menu_omitting_the_owners_choice_reads_as_silence]].

**Checks, cheapest first:**
1. **Before registering any N-period persistence rule, print the per-unit consecutive-observation histogram.** If `max(depth) < N`, the rule is inert — say so on the register rather than reporting zero fires.
2. **Separate "measured" from "derivable-by-assumption" cells.** A cell computed as `cap ÷ requests` assumes fill-to-cap; that is an assumption wearing a measurement's clothes.
3. **Check that the measure is commensurable across units.** In the worked case one panel mixed dollars-accepted÷dollars-requested, a ratio of two rounded share-percentages against a *prior*-period base, and two press figures — four different measurements under one threshold ([[finding_cross_entity_comparison_needs_same_perimeter]]).
4. **When the panel cannot grade the level, do not re-place the level off the same panel.** Find an out-of-sample referent or declare the rule inert. Re-placing off the panel that could not grade it just re-derives the design statistic.
