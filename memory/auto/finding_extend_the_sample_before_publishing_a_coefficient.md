---
name: finding_extend_the_sample_before_publishing_a_coefficient
description: A cross-sectional coefficient computed on a cohort assembled for a different question can clear significance and vanish on extension — double n before publishing, and if it halves the finding was the frame.
metadata:
  type: feedback
---

Testing whether a bank selloff sorted on private-credit exposure, a **pre-existing 14-name cohort** — built months earlier to screen *hidden CRE* — gave Spearman **rho −0.559**, past the n=14 critical value (~0.53), with the three worst returns ranking #1/#2/#3 on exposure. A clean, publishable-looking mechanism.

**It died on extension.** 26 names: **−0.255** (crit ~0.39). The 12 money-center names alone: **−0.014**. Dropping the single highest-exposure name: −0.174. The n=14 result was an artifact of *which fourteen*.

**Why this one gets past you:** the cohort was **not** selected on the outcome, and re-using a defined, pre-committed cohort is the standard defence against cherry-picking. **It feels like the disciplined choice.** But a cohort assembled for question A is a *biased frame* for question B whenever the selection variable correlates with the new test variable — here, "banks I screen for hidden CRE" over-weights concentrated mid-cap lenders, exactly the tail that drives an NDFI rank.

**How to apply:**
- **Extend the sample once before publishing any cross-sectional coefficient.** Survives a doubling of n → a finding. Halves → it was the frame. This is cheap and it is the whole control.
- **Always print n and the critical value beside rho.** A bare "−0.559" hides that it is one name away from nothing.
- **Report every variable tested, not the best one.** Testing k variables and quoting the winner needs a higher bar; say how many you ran.
- **Run the obvious confound explicitly** (here: prior run-up vs drawdown, rho −0.024 — "what rallied most fell most" was dead, which is what made the null trustworthy rather than lazy).
- **A null that survives extension is a real result** and is worth publishing as one — it closed a trade-card question that a false positive would have opened.
- Related: [[finding_ranked_head_sample_is_not_the_population]] (the head-sampling sibling) · [[finding_cohort_too_small_to_move_the_index]] · [[finding_base_rate_the_threshold_before_building_it]] · [[finding_crosscheck_with_free_parameter_validates_nothing]] · [[finding_overlapping_window_inflates_the_base_rate]].
