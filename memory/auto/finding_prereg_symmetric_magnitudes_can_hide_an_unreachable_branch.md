---
name: finding_prereg_symmetric_magnitudes_can_hide_an_unreachable_branch
description: "A pre-registration can be symmetric in what each branch PAYS and asymmetric in what each branch CAN pay — base-rate every branch for reachability, jointly, before freezing it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0127dd63-a2fb-47ed-8bbd-4d66dbce8d27
  modified: 2026-08-12T22:00:00.994Z
---

**Checking that a falsifier's branches move the number by equal amounts is not the same as checking that both branches can fire.** A registration can be perfectly symmetric in **magnitude** and completely asymmetric in **outcome** — and it passes every construction check that asks about form.

## Case (NEXUS, 2026-08-12)

The successor falsifier for the fleet's most-consumed number (a 2-6wk probability split) was frozen with four construction checks: symmetric ±6pp magnitudes both directions, numeric NO-VERDICT edges, a non-renewable clause, and a written statement of what a repeated no-move would mean. **All four passed. None of them asks whether a branch is reachable.**

Base-rated afterwards over 422 sessions:

| Branch | Condition | Rolling-window base rate |
|---|---|---:|
| **A — bear** | ratio ≥3.60 on 3-of-5 **AND** HY OAS ≥280 sustained 3 | **0 / 418 = 0.0%** |
| **B — bull** | ratio <3.40 s=5 **OR** HY <260 s=3 | **85.9%** |

**Branch A had never been satisfied once in nineteen months** — and **that unconditional number was itself misleading, which is the second half of this finding.**

## ⚠️ The correction, delivered by the adversarial desk within the hour — an unconditional joint base rate can hide the REAL defect

The author read "0 of 418 windows" as *"branch A cannot fire."* **The adversarial reviewer, pulling the same series independently, found something sharper and more damaging:**

- Branch A's ratio leg was **already satisfied on 8 consecutive sessions, at the sample maximum** ⇒ 🔴 **SATISFIED ON DAY ONE.**
- Branch B's ratio leg needed a move so large it was **unreachable inside the resolution window.**
- ⇒ **Branch A collapsed to its HY leg alone; branch B collapsed to its HY leg alone. The ratio — the instrument the falsifier existed to test — contributed NOTHING to either branch.**

**Both branches were live. The gate was not dead; it was measuring only one of its two instruments.** Conditional on the live regime, branch A needed just +8bp on HY — very reachable. **The unconditional joint 0.0% pointed at a defect that was real but mis-described, and it flattered the author** by making the self-catch look bigger than it was.

⇒ **Two distinct checks, and the second is the one that bites: (1) CAN each branch fire? (2) does each LEG still discriminate, conditional on the state at freeze-time?** A leg true on day one is a **descriptor, not a test** (`[[finding_escalation_line_needs_delta_not_level]]` — *would it fire on day one? then it is a descriptor*). **A registration can pass check (1) on every branch and still be worthless, because the leg carrying the thesis is inert.**

**The repair the reviewer proposed, and its shape is the transferable part: re-express the descriptor leg as a DELTA keyed to the claimed mechanism.** Here: replace a *level* line on the ratio with *"the tail retraces <40% of any index retracement over the window"* — which was 17% vs 94% on live data, tests the thing actually being claimed, can fail, and is not true on day one.

## The mechanism — and it generalises past ratios

**The gate's second leg was the first leg's DENOMINATOR.** The ratio was CCC/HY; branch A demanded the ratio be high *and* HY be wide, but HY widening mechanically pushes CCC/HY down. The tape shows it cleanly: on the days HY was widest the ratio was at its lowest, and vice versa. **The legs were anti-correlated by construction, so no choice of threshold repairs it** — only a different instrument does.

**The general form: whenever one leg of a compound condition is an input to another leg's calculation, the legs cannot be treated as independent evidence and may be mutually exclusive.** Ratios, spreads, shares, per-capita figures and index-relative measures all embed another published series. **Ask what is in the denominator before pairing it with a level test on that same series.**

## The tests to add before freezing any multi-leg registration

1. **Base-rate each branch for REACHABILITY, jointly, not leg-by-leg.** Marginal rates hide this entirely: here the legs were 3.3% and 64.3% individually, and 0.0% together.
2. **Name what each leg is arithmetically MADE OF.** If leg 2's series appears inside leg 1's formula, the pairing is suspect by construction.
3. **Base-rate CONDITIONAL on the current state, not only unconditionally.** An 85.9% branch is not 85.9% likely from a state 36bp away from it. Both numbers are needed; neither alone is the answer.
4. **Symmetry of magnitude ≠ symmetry of outcome.** Write both down. If one branch is reachable and the other is not, the registration has a lean regardless of the equal ±N it advertises.

## Discipline when the defect is found AFTER freezing

⛔ **Disclose, do not move.** Re-cutting a frozen branch after registration — especially the branch whose failure to fire favours the author's own standing call — is indistinguishable from moving goalposts, whatever the merits. **Let it grade as written, and put the base rates on the record BEFORE it resolves**, so the outcome is read against a published expectation rather than a fresh rationalisation. Pre-commit in the same breath to (a) the expected branch, (b) that the expected branch scores nothing, and (c) taking the full move if the unreachable branch somehow fires.

**Also check what survives:** the same registration's NO-VERDICT clause named the live state exactly and its non-renewable rider still forced a real downstream obligation. **A partially defective falsifier is not an inert one** — say which half failed, rather than discarding the whole thing.

## Why it matters

**An unreachable branch reads as rigour.** It produces a clean record of "registered, falsifiable, graded on schedule" while the number it governs can only ever be pushed one way. Related: `[[finding_compound_gate_jointly_unsatisfiable]]` (the same arithmetic in a capital gate — it already said "base-rate jointly AND conditionally," which is why **detection was never the gap here; invocation was**), `[[finding_ratio_gauge_denominator_branch]]`, `[[finding_base_rate_the_threshold_before_building_it]]`, `[[finding_prereg_verdict_boundary_must_be_a_number]]`, `[[finding_resolvability_defect_is_status_not_confidence]]` (this is a STATUS mark, never a confidence cut).

## ⚠️ And on WHO may repair a frozen spec

The author's first instinct — **disclose, do not move** — was right for a change that would **loosen** the branch favouring their own standing call. **It was wrong as a blanket rule.** When the **adversarial reviewer proposes the fix, against its own interest, while the spec is frozen against both parties, and the change makes the test HARDER**, the goalpost objection does not apply. **That is the one category of mid-flight re-spec that survives scrutiny** — and refusing it on a reflex preserves a gate everyone now knows is inert.

**Still do not SELF-rule it.** The interested party routes the proposed repair to the coordinator with both readings attached. *(Sibling move the same day: another desk deferred a self-rulable row overnight rather than self-ruling at the end of a long session.)*

⚠️ **Sibling defects found by three different desks on the same afternoon, all one class — a registration checked for form and never for what it can do:** one desk registered a trigger with a **direction and no magnitude**; one had base-rated its thresholds, instruments and anchors but **never its windows** (a prediction market found the cycle's most extreme observation sitting one row above the window it graded); this one checked magnitudes but **never reachability**. **Audit your own registry along the axis you have not audited it on yet.**
