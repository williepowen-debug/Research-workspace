---
name: finding_update_size_must_track_instrument_distance_from_evidence
description: When you move a prediction on another desk's finding, the size of the move must track how far YOUR instrument sits from what the finding is about — and a counterfactual conditioned on an OUTCOME cannot be cashed on a DIRECTION
symptoms:
  - "I moved my number more than the desk whose evidence it was"
  - "pre-registered counterfactual, took the full value on directional evidence"
  - "my prediction grades a different object than the finding is about"
  - "band re-weighting more than doubled on a finding with no magnitude"
  - "the author fenced their own finding as non-calibratable and I calibrated off it"
metadata:
  type: feedback
---

Two ways to mis-size an update on a peer's evidence. Both fired on the same
move (LABOR `LAB-08`, 2026-08-27), and RED — whose evidence it was — caught
both within the hour.

**(1) A DOWNSTREAM-graded instrument must move LESS than an upstream-graded
one.** Berger's QCEW claim, verified at the BLS primary, is a finding about the
**preliminary** benchmark. RED grades `RED-22` on the preliminary and moved
**52 → 40 (12pp)**. LABOR grades `LAB-08` on the **final**, reached from the
preliminary through a **0.76** shrinkage ratio, and moved **35 → 15 (20pp)** —
*further, on the instrument further from the evidence.* The final is the
preliminary plus an independent step the evidence is silent on; an extra step
contributes variance and therefore **damps** the transmitted update. It showed
in the band re-weighting: `P(≥700K) 0.375 → 0.12`, and `P(<450K-or-up)`
**0.275 → 0.65** — more than doubling on a finding carrying no magnitude at all.

**(2) A counterfactual conditioned on an OUTCOME may not be cashed on a
DIRECTION.** The 15% was pre-registered as *"if Band E LANDS, my 35% should
have been ~15%."* **Band E did not land** — what arrived was evidence *pointing*
at Band E. Pre-registration bought protection against the *chase* (the timing),
and that was mistaken for a licence on the *size*. Worse, the evidence's author
had explicitly fenced it: RED's limit (b) states current `PAYNSA` already embeds
the prior benchmark, so the `+211K` residual **cannot be mapped to a job count.**
A calibrated number was taken off a finding marked non-calibratable.

**How to apply.** Before moving a prediction on someone else's finding, ask in
order: **(a) Does my instrument grade the SAME object the finding is about?** If
it grades a downstream object, name the intervening step, ask whether the
evidence speaks to it, and if it does not, my move should be *smaller* than the
originating desk's — and I should be able to say why out loud. **(b) Is the value
I am taking conditioned on an outcome that has not occurred?** Direction is not
outcome; short of the condition firing, the honest update is a fraction of the
counterfactual and the fraction needs its own argument. **(c) Did the author fence
it?** Their stated limit binds me at least as tightly as it binds them —
see [[finding_rederived_signal_loses_the_senders_caveats]], of which this is the
sharpest form: the fence was lost on evidence handed over *directly, in the same
conversation*, not across a hop.

**Corollary on deadlines.** *"I have already moved twice today"* is a reason not
to move **again right now**; it is not a reason to carry a number you believe is
mis-derived indefinitely. Check when each instrument actually resolves: `RED-22`
graded the next morning, so RED holding was correct; `LAB-08` resolves 6 months
out, so the right disposition was **annotate now, re-derive off the PRINTED
figure** — updating off a number rather than off an argument is the one further
move that cannot be a chase. Partners with
[[finding_registered_gate_captures_attention]].
