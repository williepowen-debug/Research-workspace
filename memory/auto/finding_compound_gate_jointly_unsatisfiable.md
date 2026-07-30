---
name: finding_compound_gate_jointly_unsatisfiable
description: A multi-leg gate can be individually satisfiable on every leg yet JOINTLY unsatisfiable in the only state that matters — base-rate gates jointly AND conditional on the trigger state, never marginally.
metadata:
  type: feedback
---

**A compound gate's legs can each look healthy in isolation while the gate is unsatisfiable in the exact state it governs.** Marginal base rates hide this completely — which is why such a gate survives review indefinitely.

**Case (BRENT, 2026-07-30).** A convex trade's deploy gate was `{OVX/VIX ratio < 2.89 AND OVX < 44.2}`. I had escalated to the operator that it *"may be unfireable by construction — a dead switch."*

**Both halves of my own framing were wrong, in opposite directions:**
- **The gate was not rare.** It was met on **50.4% of the prior year's sessions** and had last opened **18 sessions earlier**. Had the operator ruled on my framing, the fix would have been *"lower the threshold"* — **the wrong repair to the wrong defect, loosening a capital gate for no reason.**
- **The real defect: the gate and the trade's own ARM TRIGGER were anti-correlated by construction.** The arm armed on **escalation**; the gate opened on **calm**. Over 753 sessions: gate open on **0 of 38 escalation days (0.0%)** vs **78.5% of all other days**. Requiring both *simultaneously* required an escalation event during a volatility lull — which had never once occurred.

## The tests to run

1. **Base-rate the gate JOINTLY, not leg-by-leg.** `P(all legs | trigger state)`, not `P(leg_i)`. A gate at 50% marginal and 0% conditional is a dead gate wearing a healthy number.
2. **Ask what the legs are correlated WITH — especially with the trigger itself.** If the event that arms the trade moves a gate leg *against* opening, the gate and the trigger are mutually exclusive and **no choice of threshold fixes it.** The repair must **break the simultaneity** (sequence: arm on the event → deploy on the first qualifying condition inside a **bounded, expiring** window), not re-tune it.
3. **Base-rate a proposed REPLACEMENT under the trigger state before proposing it.** My preferred fix — a "don't chase" price test — fired on **0.0% of escalation days too**, identically. **Any metric measuring "the move hasn't happened yet" is 0% on days the move is happening.** I would have shipped an identical defect wearing a new name. → `[[finding_base_rate_the_instrument_before_its_event_table]]`
4. **Check the proxy is still valid for the INSTRUMENT actually traded.** The same gate priced *vega* — while the plan mandated a **vertical spread specifically because a spread neutralises vega.** At constant moneyness the debit rose **+13.5%** across a +44% vol move and **asymptoted** above ~90% IV; the *forbidden* naked call rose **+140%**. **The gate was correctly specified for the instrument the plan bans.** A control inherited from an earlier structure outlives the structure it was written for.

## Discipline when repairing

**Breaking a simultaneity LOOSENS the gate — pair it with tightenings, or you have quietly increased willingness to trade under cover of a bug-fix.** (BRENT's pairing: a hard **expiry** on the armed state, a **new** structural-economics floor measured on a live chain, and a decompression benchmark that **re-ratchets on fresh escalation** so the gate self-tightens in a worsening crisis.) Same rule as `[[finding_threshold_spec_fails_before_world]]`'s latency-repair case: **a spec repair is not direction-neutral.**

**Proof-of-good-faith test worth stating explicitly in any re-spec: does the proposed rule fire TODAY?** If it does, you may have written it to fit the tape. BRENT's did not, and said so.

**Why it matters:** an unfireable gate reads as *discipline* — it produces a clean record of "correctly passed on the chase, N sessions running" — while actually being an unexamined defect that will govern capital at the next decision point. Related: `[[finding_threshold_level_is_a_measurement_not_a_constant]]`, `[[finding_guard_scope_expires_at_the_fill]]`, `[[finding_test_the_guard_not_just_the_guarded]]`, `[[finding_standing_guard_is_a_false_negative_risk]]`.
