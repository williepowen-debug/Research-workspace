---
name: finding_effect_below_instrument_detection_floor
description: "Before reading a gap as signal, compute the instrument's own dispersion — a difference smaller than the noise floor of the data it came from is not weak evidence, it is no evidence; and N failed tests of one instrument CLASS is evidence about the measurement problem, not bad luck"
metadata:
  node_type: memory
  type: finding
---

A cross-sectional gap is only interpretable **relative to the dispersion of the thing it was measured in.** Compute the instrument's detection floor *before* reading its output, not after the third attempt fails.

**MARCO, 2026-07-25 → 07-31.** A state wage gap — **FL leisure & hospitality +8.75% YoY vs national +3.87%, a +4.88pp gap, three consecutive months** — was promoted to primary thesis instrument, written into THESIS/STATUS/NEXUS_BRIEF and packets to two agents. It was retracted hours later when a cross-state panel showed the gap was a statutory minimum-wage artifact.

Six days on, a properly floor-controlled re-test produced the deeper finding: **cross-state dispersion in that data (BLS CES state average hourly earnings) is sd ≈ 5–6pp, giving a minimum detectable difference of ~6pp.** The +4.88pp headline sat **below the noise floor of the very series it came from.** It was never distinguishable from ordinary cross-state heterogeneity — *independent of* the confound that got the blame. The confound story was true but was not the deepest problem, and finding a true confound felt like a complete diagnosis, which stopped the inquiry one level early.

**Two tells that the reading is dispersion, not signal:**
- **The sign flips when you swap a defensible control.** The same stratum comparison gave **−2.57pp** against one control sector and **+1.27pp** against another, neither significant (|t| < 1). A real effect does not invert on a control swap.
- **Stability is not significance — and confusing them cuts both ways.** A month-by-month check showed these gaps were *highly* stable (median within-state 6-month swing 3.2pp, states holding sign every month). That is easy to read as "signal, not noise," and it is: they measure something real and persistent. It just was not the variable under test — it was **industry mix** (energy-sector wages inside the control supersector, contaminating exactly the treatment cells). **Persistent confounding looks exactly like signal on a stability check;** cross-sectional dispersion, not month-to-month wobble, is what buries the effect.

**How to apply:**
- Before treating a gap as evidence, compute the **spread of that same metric across the comparison units**. If `|gap| < ~2×SE` of the cross-unit distribution, you have no evidence — say that, rather than reporting it as "weak" or "suggestive."
- **Report the detection floor beside the finding**, so a downstream consumer can see whether the number clears it. A gap quoted without its dispersion invites everyone to over-read it.
- Swap the control/denominator once as a routine robustness step. It is cheap, and a sign flip is decisive.
- **Escalation rule — the part worth remembering longest: when the Nth pre-registered test of the same instrument CLASS fails, stop specifying test N+1 and ask whether the class can observe the phenomenon at all.** MARCO's three failures ran on payroll/price series while the population under study (undocumented workers who exited the labor force) is disproportionately **off-payroll and unresolvable within an establishment survey** — the subjects whose behavior *is* the mechanism were the ones the instrument could least see. That reframes three nulls from a run of bad luck into a finding about the measurement problem, and it is a stronger, more defensible claim than a fourth specification would have produced. Name what *would* reopen the question (a source that observes the population directly) so the conclusion stays falsifiable in both directions.
- Pair with a **pre-committed consequence written before the test runs** ([[finding_run_the_falsifier_before_promoting]]): decide in advance what a null obligates you to do, or the null gets re-litigated the moment it is inconvenient.

Related: [[finding_base_rate_the_instrument_before_its_event_table]] (base-rate a detector before reading its events — same instinct, applied to rates rather than dispersion), [[finding_spread_metric_blind_to_common_mode]], [[finding_normalization_choice_picks_opposite_winners]] (control/normalization choice flipping the answer), [[finding_verification_zero_is_ambiguous]].
