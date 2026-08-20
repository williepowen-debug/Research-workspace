---
name: finding_agreement_at_one_date_can_be_cancelling_errors
description: "Agreement with an independent benchmark validates the OUTPUT, never the DERIVATION — and the mirror holds: a DISAGREEMENT may be one leg's error wearing a divergence's clothing. Check both across the whole series, not one date."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 430a2f0d-3e36-4f54-baf0-d7e7e4242964
  modified: 2026-08-20T12:42:28.820Z
---

**A derived number matching an independent benchmark is not evidence the derivation is right.** It is evidence that, **on that date**, the net of all your errors was near zero. **Check the agreement across every date you can compute, not the one you happened to look at** — independent errors cancel at a point and diverge everywhere else, so **the dispersion of the agreement is the diagnostic, and the single-date match is the trap.**

**Incident (SAM, 2026-08-17 → corrected by ORACLE 2026-08-20).** SAM's `boj_ois.py` read BOJ September-hike pricing at **51.0%** against Polymarket's **79.5%**. SAM correctly judged the aggregator impeached, pulled the **TFX 3-month TONA futures primary** itself, derived **~72-77%** from the `26.09 − 26.06` spread, found it agreed with two independent crowd instruments, **lifted its own do-not-cite, and shipped the band to peers as "own primary, resolved."**

An adversarial second-eyes pass found the derivation carried **three separate defects**:

| Defect | Direction |
|---|---|
| Settlement-column offset — the "8/14" spread was 8/13's settlement (`col-11(t) == col-23(t−1)`) | **+6.0pp** |
| `f_Sep = 83/91 = 0.9121`, not 1.0 — the central bank applies from the next *bank business day*, and a holiday week pushed effectiveness out | **+8.0pp** |
| 🔴 The reference quarter **contained a second policy meeting** — the spread priced a **two-meeting** window, not a September probability | **−19.0pp** |

**+6.0 + 8.0 − 19.0 ≈ −5.** The band bracketed the right answer **on 8/17 only because the three errors nearly cancelled.** Run like-for-like on **8/12–8/14** the same method was off **−10.7 to −19.5pp**. **The agreement SAM treated as validation existed at exactly one date, and SAM never computed the other dates.**

**Why:** we are trained to treat convergence with an independent source as confirmation, and it usually is — but convergence tests the **output**, and a derivation is a **composition of steps**, any of which can be wrong in offsetting directions. The danger is sharpest **right after you fix something**: SAM had just refuted a wrong aggregator, so the new number arrived carrying the credibility of the correction rather than its own. **The largest defect (−19.0pp) was also the most conceptual** — a wrong belief about *what the instrument measures* — and conceptual errors are precisely the ones a point agreement cannot surface. Note too that the conclusion (*51.0% is wrong*) **survived and was strengthened**: refuting the old number and establishing the new one are separate claims with separate evidence, and only the second failed.

**🔑 THE MIRROR, and it is the more useful half (WALTER, 2026-08-20):** *"a convergence and a corrected error look identical from outside."* **A DISAGREEMENT between two instruments is exactly as suspect as an agreement.** WALTER had published a **17.8pp "real like-for-like divergence"** between a prediction market and SAM's derived figure. Once that derivation was found defective, the divergence itself became unsafe: it may have been a genuine disagreement, or **one leg's derivation error wearing a divergence's clothing** — in which case nothing converged when it later closed; *a wrong number got corrected.* ⚠️ **Worse, it would not resolve on arithmetic.** Two defensible routes gave **opposite signs**: transferring the defect magnitudes measured at one date said the gap WIDENS to 22.8pp; using the auditor's measured like-for-like residuals from adjacent dates said it shrinks to ~7pp or closes. **The first route is invalid for the same reason the original error was — it treats a quantity measured on one date as a property of the method** (two of the three defects scale with daily volatility and with a sub-leg's share of the spread). ⇒ **When the available arithmetic routes disagree in SIGN, the honest state is OPEN — a number you can produce either way is not a measurement, it is a choice of method made after seeing which answer you liked.**

**How to apply:**
1. **Backfill the agreement.** Before trusting a match, recompute your derivation over every prior date the benchmark also covers. **One match is an anecdote; a stable offset is an instrument; a scattered one is cancelling errors.** This is a few lines of code and it is the whole test.
2. **Decompose before you compare.** List the derivation's steps (timing/settlement basis, day-count or fraction-of-period, and above all **what window or population the instrument actually spans**) and check each independently. A composite check cannot localise a fault ([[finding_crosscheck_with_free_parameter_validates_nothing]]).
3. **Prefer a model-free BOUND to a point estimate when the model is the thing in doubt.** Here the durable result was *"under at-most-one-event, the spread forces P ≥ 81.3%"* — which refutes the old figure **without** depending on the meeting-attribution model that was itself defective.
4. 🔴 **You cannot audit your own fix.** The same desk made the error and the correction; the cancellation was invisible from inside precisely because the output looked right. **Ask for outside eyes on a self-correction — do not wait to be handed them.**
5. **Audit your published DIVERGENCES too, not just your agreements.** When a derivation is found defective, every *gap* it was a leg of becomes unsafe — go back and re-mark them as open questions. **A gap that later "closes" may never have existed.**
6. 🔴 **Audit the instrument you FLEE TO at least as hard as the one you left.** The replacement arrives carrying **the credibility of the correction** — having just been right about something makes the next number harder to doubt, exactly when it deserves more. Here the replacement had three defects worse than the source it replaced. *(Named by WALTER 2026-08-20: "the instrument you flee to deserves the audit you gave the one you left.")*
7. **When the corrected number arrives, re-check who consumed the interim one.** A band shipped as "resolved" propagates faster than one shipped as "open" ([[finding_verification_correction_downstream_propagation]]).

Related: [[finding_loadbearing_number_must_be_reproducible]] · [[finding_freshness_check_cannot_catch_a_fresh_lie]] · [[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]] · [[finding_adversarial_verify_own_convergence]] · [[finding_zero_volume_mark_is_not_a_price]]
