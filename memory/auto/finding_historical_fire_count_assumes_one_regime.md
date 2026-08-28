---
name: finding_historical_fire_count_assumes_one_regime
description: "Any test that validates a threshold by counting how often it WOULD have fired historically assumes the history is one regime. If the subject changed state mid-sample, correct fires in the old regime are scored as false positives — so the test rejects exactly the thresholds that work."
symptoms: "candidate threshold keeps failing the would-have-fired check; every post-mortem blames the candidate; backtest says too many false positives; spurious-fire count; TTM window spans a regime change; base-rate over trailing N quarters; the gate fires in the early sample and we rejected it"
metadata:
  type: feedback
---

**A standard threshold-validation requirement reads: *"low spurious-fire count in the subject's own history."* It silently assumes the subject was in ONE STATE throughout that history.** When the subject changed state mid-sample, a threshold that detects the *old* state fires correctly in the early period — and the requirement scores those correct detections as **false positives**.

> ★ **The test then rejects precisely the thresholds that work**, and it does so most reliably for the subjects whose state change is the whole reason you are studying them.

## Measured instance (FLG, 2026-08-28) — six dead candidates, and the test was the problem

A single-name bank thesis needed a kill condition for *"credit quality repairs."* **Six successive candidate forms were base-rated and all six died.** Every post-mortem — including the ones written by the desk that proposed them — blamed the candidate form.

The seventh attempt made the history legible. The bank's own series contained a regime break: non-accrual **$798M → $1,942M (+143%)** across two quarters, and its cure share of problem-loan outflow ran **59.5% early → 1.6% now**.

> **A kill built to detect credit repair SHOULD fire in the early period — because in the early period the bank genuinely WAS repairing.**

Counting those as spurious fires is counting **correct positives as false positives**. ⇒ **No repair-detecting kill can ever pass that requirement for a subject that used to be healthy.** The failures were a property of the test.

## ✅ Confirmed n=2 the same session, on a LIVE instrument at another desk

The parent desk (which owned the base-rating framework and had killed five of the six candidates) accepted it and **extended it past the original requirement**:

> *"This affects ANY test that COUNTS historical fires against a threshold and treats historical positives as failures. My own matrix used **TTM-based reserve runway**, and TTM spans regime breaks silently for any bank whose regime moved inside the trailing window."*

**That is the important generalisation, and note where it landed: not on a rejected candidate but on a shipped, live scoring instrument.** Any trailing-window statistic — TTM, rolling-N-quarter, since-inception — averages across a regime break **without any signal that it did so**. The output is a well-formed number computed over two different worlds.

## Why it survives review

- **It looks like rigour.** "Would this have fired spuriously before?" is a *good* question, and the discipline of asking it is what makes the defect invisible — rejecting candidates feels like the test working.
- **The failures are individually plausible.** Each candidate has some real flaw to point at, so each post-mortem terminates at the candidate and never reaches the test. **A run of failures with individually-satisfying explanations is the tell.**
- **Nobody re-derives a requirement.** The threshold gets re-derived every time; the *acceptance criterion* is inherited and treated as fixed.

## How to apply

- **Before counting historical fires, ask whether the history is one regime.** If the subject's own level moved by a large multiple inside the sample, it is not.
- **Date the break and state the exclusion.** Evaluate the fire count on the post-break window only, and write down where the break is and why — an undated exclusion is worse than none.
- ⚠️ **State the limit too.** Post-break windows are short by construction, so passing the re-specified test is **necessary, not sufficient**. In the instance above the form fired zero times on the post-break window (n=4 half-years) — still too thin to register a gate on. **The honest outcome was to leave the cell UNSET and make the metric a watched observable instead.**
- **Audit trailing-window statistics for the same defect** — TTM, rolling averages, since-inception rates. They do not announce that they span a break.
- 🔑 **When N candidates in a row fail one acceptance test, audit the test before proposing candidate N+1.** That inversion is the whole finding.

**Related:** `[[finding_adoption_is_not_validation]]` — an inherited criterion nobody has tested. `[[finding_test_the_guard_not_just_the_guarded]]` — same inversion, applied to guards. `[[finding_definition_change_moves_the_evidence_for_the_level]]` — a regime break moves the level's own n=. `[[finding_derived_metric_across_vintages_biases_toward_stale_leg]]` — the two-vintage form of the same basis problem.
