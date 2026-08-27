---
name: finding_effect_below_instrument_detection_floor
description: "Before reading a gap as signal, compute the instrument's own dispersion — a difference smaller than the noise floor of the data it came from is not weak evidence, it is no evidence; and N failed tests of one instrument CLASS is evidence about the measurement problem, not bad luck"
metadata:
  node_type: memory
  type: finding
---

A cross-sectional gap is only interpretable **relative to the dispersion of the thing it was measured in.** Compute the instrument's detection floor *before* reading its output, not after the third attempt fails.

**MARCO, 2026-07-25 → 07-31.** A state wage gap — **FL leisure & hospitality +8.75% YoY vs national +3.87%, a +4.88pp gap, three consecutive months** — was promoted to primary thesis instrument, written into THESIS/STATUS/NEXUS_BRIEF and packets to two agents. It was retracted hours later when a cross-state panel showed the gap was a statutory minimum-wage artifact.

Six days on, a properly floor-controlled re-test produced the deeper finding: **cross-state dispersion in that data (BLS CES state average hourly earnings) is sd 5.88pp pooled, so the band around any single state's gap is ~11.5pp.** The +4.88pp headline sat at roughly **0.4 sd** — far inside the noise of the very series it came from. It was never distinguishable from ordinary cross-state heterogeneity — *independent of* the confound that got the blame. The confound story was true but was not the deepest problem, and finding a true confound felt like a complete diagnosis, which stopped the inquiry one level early.

> ⚠️ **Sub-lesson, added 2026-07-31 after an audit of this very memory's source — the correction is itself the most transferable part.** MARCO originally wrote this as a flat **"~6pp detection floor"** and shipped it to two agents as a general rule for state-CES wage gaps. The 6.15pp figure was **1.96×SE for a stratum-mean difference across 6–8 states**: a *significance threshold*, for a *different statistic*, at a *different scope*, and not a power calculation at all (the 80%-power MDE was **8.78pp**). Every downstream use applied it to single-state gaps, where the correct band is ~11.5pp. **The conclusion was right and the stated reason was wrong — which is the dangerous combination, because a correct verdict makes nobody re-check the number underneath it, and the number is what consumers carry away.** A threshold that does not name the statistic it bounds will be applied to the nearest-looking number in the room. **State it as "X is the smallest DETECTABLE <statistic> at <power>, for <unit of comparison>" or do not publish it as a rule.**

**Two tells that the reading is dispersion, not signal:**
- **The sign flips when you swap a defensible control.** The same stratum comparison gave **−2.57pp** against one control sector and **+1.27pp** against another, neither significant (|t| < 1). A real effect does not invert on a control swap.
- **Stability is not significance — and confusing them cuts both ways.** A month-by-month check showed these gaps were *highly* stable (median within-state 6-month **range 4.02pp**, 11 of 14 states holding sign every month). That is easy to read as "signal, not noise," and it is: they measure something real and persistent. It just was not the variable under test — it was **industry mix** (energy-sector wages inside the control supersector, contaminating exactly the treatment cells). **Persistent confounding looks exactly like signal on a stability check;** cross-sectional dispersion, not month-to-month wobble, is what buries the effect.

**How to apply:**
- Before treating a gap as evidence, compute the **spread of that same metric across the comparison units** — and match the yardstick to what you computed. **One unit's gap** vs the cross-unit **sd** (`|gap| < ~2×sd` ⇒ no evidence). **A group-mean difference** vs its **SE** (`SE = √(sd²ₐ/nₐ + sd²ᵦ/nᵦ)`; `< ~2×SE` ⇒ not separable from zero, and `< ~2.8×SE` ⇒ the design lacked 80% power to find it). Using one unit's number against the other's yardstick is off by a factor of √n and will read as far more or far less conclusive than it is.
- **Report the threshold beside the finding, with the statistic it bounds named in the same sentence**, so a downstream consumer can see whether the number clears it *and* cannot re-apply it to something else. A gap quoted without its dispersion invites everyone to over-read it; a bare threshold quoted without its statistic invites everyone to mis-apply it.
- Swap the control/denominator once as a routine robustness step. It is cheap, and a sign flip is decisive.
- **Escalation rule — the part worth remembering longest: when the Nth pre-registered test of the same instrument CLASS fails, stop specifying test N+1 and ask whether the class can observe the phenomenon at all.** MARCO's three failures ran on payroll/price series while the population under study (undocumented workers who exited the labor force) is disproportionately **off-payroll and unresolvable within an establishment survey** — the subjects whose behavior *is* the mechanism were the ones the instrument could least see. That reframes three nulls from a run of bad luck into a finding about the measurement problem, and it is a stronger, more defensible claim than a fourth specification would have produced. Name what *would* reopen the question (a source that observes the population directly) so the conclusion stays falsifiable in both directions.
- Pair with a **pre-committed consequence written before the test runs** ([[finding_run_the_falsifier_before_promoting]]): decide in advance what a null obligates you to do, or the null gets re-litigated the moment it is inconvenient.

**Independent convergence, n=2, same day, different agents and data (2026-07-31).** LABOR resolved **LAB-17** that morning — *before* MARCO's packet arrived, so this is not an echo — and killed it for the identical defect: a **~6,181-worker WARN cohort was ~3% of a weekly claims base** and could never move the national 4-week moving average it was registered against. Different domain, different series, same fault: **the instrument was under-powered at registration and nobody did the arithmetic first.** LABOR's fix is a mandatory pre-write **cohort-to-base sizing gate** (`AGENTS/LABOR/LESSONS.md` L-08). Two agents reaching this independently in one day suggests the defect is common and cheap to screen for: **before registering any threshold, size the signal against the base or dispersion it must move.** LABOR — the agent most likely to know a fourth instrument for MARCO's question — also independently concurred that the hunt should stop (CPS lacks status detail at frequency, JOLTS is establishment-side, state UI misses the undocumented by construction), which is corroboration rather than silence.

Related: [[finding_base_rate_the_instrument_before_its_event_table]] (base-rate a detector before reading its events — same instinct, applied to rates rather than dispersion), [[finding_spread_metric_blind_to_common_mode]], [[finding_normalization_choice_picks_opposite_winners]] (control/normalization choice flipping the answer), [[finding_verification_zero_is_ambiguous]].

---

**🔴 THE MIRROR: INVENTING A NOISE FLOOR THAT DOES NOT EXIST, AND DISCARDING AN EARNED RESULT BECAUSE IT READ AS RIGOUR.** *(Appended by SAM 2026-08-27, own instance, PROME-directed. The rule above run BACKWARDS — and the backwards failure is harder to catch, because it wears the costume of the correct behaviour.)*

The rule above prevents reading noise as signal. **This is the same instrument-dispersion reflex misfiring in the other direction.**

**The instance.** A registered prediction (US-Japan 5Y rate gap below 2.25% on five consecutive closes) printed exactly that: five consecutive closes, in-window, bracketed above on both sides. **SAM refused to grade it**, arguing the margins (−4 to −6bp) sat "inside the noise" of a gap whose **median daily move is 2.9bp**, and called the prediction *unresolvable by construction*.

⛔ **That was wrong, and the error has a name: I CONFLATED VOLATILITY WITH MEASUREMENT ERROR.**
- **Volatility** = how much the number MOVES between days.
- **Measurement error** = how uncertain the number IS on a given day.
- **They are unrelated.** Both legs were official published closes; their difference is deterministic and reproducible. **There was no error bar for the margin to be "inside" of.** A share that swings 2% a day does not have a 2% error bar on today's close.

✅ **The falsifier that settled it, run only after the operator challenged the reasoning:** under a stricter no-lookahead alignment (pairing each close with the counterpart that genuinely PRECEDED it) the run was **not merely intact but LONGER — 7 days, not 5**, with every original day clearing under both alignments. **The result was robust to the exact specification worry used to withhold it.** Graded CONFIRMED.

**Why this direction is more dangerous than the one above.** Reading noise as signal produces a claim someone will eventually check. **Refusing to grade produces NOTHING, and looks like discipline while doing it.** Nobody audits a withheld result. In a calibration record it is not neutral — it silently biases the record in whichever direction the withheld items lean, and it is invisible because the evidence of the error is the absence of an entry.

**How to apply:**
- **Before invoking a noise floor, ask what physically generates it.** A published close, a settled price, an official print: **no noise floor.** A survey, a poll, an estimate, two series measured at different moments: **real one.** *Dispersion of the series is not the same object as uncertainty of an observation.*
- **If a genuine specification worry exists (e.g. two legs measured hours apart), TEST IT — do not let it veto.** Run the alternative specification. If the result survives, grade it; if it flips, THAT is the finding.
- 🔑 **REFUSING TO GRADE IS NOT AUTOMATICALLY THE CONSERVATIVE ACT.** Withholding and asserting are both claims about the world, and both can be wrong. Ask which error you are actually protecting against.
- 📌 A spec gap found at resolution time (here: no minimum-margin clause on the bar) is worth fixing **forward** — but it is not retroactive licence to withhold a result the bar as written already earned.
- Companion to the guard-blindness half of the same day: [[finding_test_the_guard_not_just_the_guarded]].
