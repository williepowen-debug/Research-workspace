---
name: finding_threshold_spec_fails_before_world
description: A pre-registered threshold usually fails because of how it was SPECIFIED, not because the world moved — audit the spec (published? seasonal? conjunction still reachable?) before concluding anything about the thesis.
metadata:
  type: feedback
---

Three distinct spec failures on live predictions inside seven days (CARL, 2026-07-18 → 07-24) — none of them told you anything about the world:

1. **Seasonal-boundary artifact.** A trigger comparing H2 insurer MCR to Q1 + 150bps fired *by the company's own guidance* in any normal year, because MCR always ramps H1→H2. It was firing while the FY guide *improved* — mechanism moving the opposite way.
2. **Metric that does not exist.** The re-spec replaced it with "ELV raises its FY26 benefit-expense-ratio guide" — and ELV publishes no FY BCR guide, in the release or on the call. The leg could never fire, in any state of the world.
3. **Conjunction that died mid-window.** "NCO ≥+30bps QoQ for two consecutive quarters *by Q3*" needed Q2 **and** Q3. Q2 printed −40bps, so after one observation the leg was arithmetically unreachable — yet the prediction sat OPEN, looking alive, with nothing marked resolved.

**Checks, cheapest first, before registering a threshold:**
- Does the issuer/agency **actually publish** this metric, on the cadence assumed? (Read one real filing, not a summary.)
- Would it fire in a **no-stress baseline year**? If yes, it measures seasonality, not stress. Prefer guide-revision *direction* or same-period YoY.
- For any **multi-period conjunction**, write down what must be true at each observation, and re-check after EVERY print whether the remaining window can still satisfy it.

**And after every print, ask which of three things happened:** the mechanism moved, the threshold moved, or the spec was never able to measure either. Only the first two are information. See [[finding_threshold_vs_mechanism]] for the mechanism-vs-threshold split; this is the layer beneath it. Multi-period conjunctions that die silently are the same family as [[feedback_dont_bank_unpassed_forecast]] and the boot-time "don't let a prediction sit OPEN-but-stale" rule in [[finding_boot_predictions_scan]].
