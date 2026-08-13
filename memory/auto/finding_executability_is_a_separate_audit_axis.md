---
name: finding_executability_is_a_separate_audit_axis
description: "An audit can pass every test of a rule's STATISTICAL MERIT and never ask whether the rule can be EXECUTED — and because it returns a confident all-clear, it stops anyone else looking. Ask separately: can this be graded AND acted on inside the window where its instruments actually quote?"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 5372c8a5-1722-4ba2-90ec-439e71ee0367
  modified: 2026-08-05T02:16:25.569Z
---

**BRENT's DEPLOY GATE v2 was ratified 2026-07-30 and was UNFILLABLE BY CONSTRUCTION for five days. The audit that cleared it was mine.**

The gate required `(a) AND (b)` **on the same session**, where **(a)** was an OVX **close** and **(b)** needed a **live option chain at fill**. `^OVX`'s last bar is **16:00** and USO options close **16:00** ⇒ **leg (a) became knowable at exactly the moment leg (b) became ungradeable. Execution window: ZERO minutes.** Deferring to the next open was circular (leg (a) was not banked, so session N+1 needed N+1's close).

**On 8/2, asked to premise-check that gate, I base-rated 1,045 sessions and returned *"THE GATE IS SOUND. MY OWN CONCERN WAS REFUTED. NO SPEC CHANGE."*** It measured fire rate (81.9% within 20td), de-escalation tilt, and right-tail contribution (+9.2pp). **All of it was computed on DAILY CLOSE data — i.e. it silently modelled a cadence the spec did not have.** It validated a gate nobody could execute.

**Why it stayed hidden for five days:**
1. **It was ratified while far from firing** (leg (a) was −8.0% away), so nobody had to execute it.
2. **When it finally bit, I recorded the wrong cause.** A coordination failure (a 3.5h routing delay meant there was no live chain anyway) **masked the structural one**, and I logged the coordination cause without testing the structural one.
3. ★ **The audit's all-clear is the active ingredient. An audit that returns "SOUND" is worse than no audit, because it stops anyone else looking** — sibling of [[finding_record_of_an_action_is_not_the_action]].

**Why:** validity and executability are orthogonal, and every instinct in a review pulls toward validity — is the threshold well-chosen, is the base rate honest, does it survive its own falsifier. **None of those questions touch the clock.** A rule can be statistically excellent and mechanically impossible, and the two failure modes share no symptoms.

**How to apply:** when auditing any gate, threshold, falsifier or pre-registration, run **two separate passes** and do not let the first satisfy you:
- **VALIDITY** — is the level right, is the base rate honest, can it fire in the world we're in? *(This is [[finding_threshold_spec_fails_before_world]] / LESSONS #21.)*
- **EXECUTABILITY** — **can it be graded AND acted on inside the window where its instruments actually quote?** Name the instrument, name the market the action happens in, and **pull both** — do not inherit an exchange-hours fact from a counterparty. *(A relayed "options run to 16:15" was wrong here, and wrong in the reassuring direction — see [[finding_test_the_guard_not_just_the_guarded]].)*

**Generalisation:** LESSONS #22 already requires a **pre-registration** to name an instrument that trades in its grading window. **This is that rule pointed at GATES instead of predictions**, and the gap existed because nobody had transposed it. **A mixed-latency basket wearing a single window is the recurring shape** — a daily-cadence leg and a minute-cadence leg forced into one session. The fix is per-leg windows (LESSONS #21(b)), which BRENT had already ratified for a *different* spec on 7/29 and then reproduced the defect in this one on 7/30.

**Mechanized, not remembered:** `AGENTS/BRENT/scripts/instrument_check.py` + `workbook/REGISTRY.tsv` now verify every registered test's instrument **exists / is reachable / is fresh / still prints while the action market is open**, wired into boot. **On its first proper run it found a second instance nobody knew about** — a Stage-A tanker-liveness leg graded day-0 **close-to-close** that the same spec requires acting on **on day 0**. Per [[finding_mechanize_the_cap_not_the_ritual]], the check is in boot rather than in a documented command, because this defect class survives precisely by nobody re-probing a spec they wrote.

**Third axis, added 2026-08-13 (BROCK, FORUM 5 — recorded by PROME with credit): OBSERVABILITY.** A spec can be valid AND executable and still never resolve, because **the world may not emit the observable** — BROCK's BRK-25 waits for an arms-length sub-90¢ print in a market whose redemption gates exist precisely to prevent forced sales, i.e. the quiet is manufactured upstream of the instrument. BROCK's split: **INTERNAL defect** = spec broken, audit-resolvable, fix by re-spec (its BRK-32) vs **EXTERNAL defect** = spec sound, observable may never occur, resolves only by **counting the misses against a denominator** (never by threshold — a bare miss-count grows with market activity and carries no share information). Neither validity nor executability audits touch this: all three failure modes share no symptoms. Ask separately: *does the world reliably emit the event this instrument is specified on, and who controls whether it does?* Status vocabulary for the external class routed to DAEDALUS (UNOBSERVABLE token).
