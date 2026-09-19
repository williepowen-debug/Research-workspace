---
name: finding_threshold_spec_fails_before_world
description: A pre-registered threshold usually fails because of how it was SPECIFIED, not because the world moved — audit the spec (published? seasonal? conjunction still reachable?) before concluding anything about the thesis.
symptoms: "the resolver column isn't in the file" · "threshold fires in a quiet year" · "noise floor from one month" · "blocked on a field nobody opened"
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

---

**Two more instances, MARCO 2026-09-19 (n=5), both on instruments that had looked
maintained for weeks:**

4. **The named resolver field did not exist — and nobody had opened the artifact.**
   Two live instruments (a vector band and an expected-signal) both named *"the NTTO
   primary workbook's vs-2019 column"* as their resolver and sat blocked on it for four
   weeks, logged as *"PRIMARY WORKBOOK NOT READ"*. The workbook was **one fetch away**,
   and when opened, **all 35 sheets contained no vs-2019 column at all.** This is
   defect #2 above (*a metric that does not exist*) in its worst form: the spec did not
   merely name an unpublished metric, it named a **field inside a specific file that
   nobody had ever opened**. ⇒ **When you register a resolver, open the artifact once
   and confirm the field is there.** The cost is one fetch; the alternative is gating
   real work on a fiction. *(The fix was primary-to-primary arithmetic from two files,
   which satisfied what the prohibition was actually about.)*

5. **A "measured noise floor" derived from n=1.** A registered identification condition
   required a divergence *">2.5pp"*, recorded as **"the measured noise floor"** — from
   **one** observation. Measured over 11 quiet pre-period months the quantity moves
   **mean 4.21pp, max 7.95pp**, and **82% of ordinary months clear 2.5pp** (45% clear it
   in the hypothesised direction). The condition would have fired on almost nothing.
   ⇒ **Check #2 above — *would it fire in a no-stress baseline year?* — has a
   prerequisite: the dispersion estimate must itself have a sample size.** One
   observation is a reading, not a floor. Say n beside any threshold justified as
   "noise", and if n is 1, it is an anecdote wearing a decimal.
   *(Related: the same audit found the wording admitted three readings whose
   false-positive rates were 45% / 30% / 10% — see
   [[finding_spec_that_is_both_falsifier_and_trigger_permits_only_disambiguation]].)*

**What both share with 1–3: the instrument looked fine.** Nothing was stale, no check
failed, and in each case the defect was visible for free in the artifact the spec
itself named.
