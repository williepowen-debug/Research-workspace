---
name: finding_resolvability_defect_is_status_not_confidence
description: "A prediction that can't resolve because its window or instrument is broken is a Status change (STUCK), never a Confidence cut — pricing resolvability into Confidence corrupts the Brier record in both directions"
metadata: 
  node_type: memory
  type: finding
  originSessionId: ff1c1c39-faa7-4783-a62e-60f9509330da
  modified: 2026-07-26T03:01:53.712Z
---

`Confidence` can honestly express exactly one quantity: **P(the claim about the world is true)**. The moment a defect in the *row* — an impossible window, an instrument that publishes nothing, a gated data source — gets priced into that column, it stops meaning what the calibration score assumes it means.

**Diagnostic question:** *what, precisely, goes from X% to Y%?* If the old number answered "will this happen" and the new one answers "will this be **observable and scored** in the window," you have changed the question, not updated the answer. That is not a re-mark.

**Worked case (STUE → CARL, CRL-14, 2026-07-25).** Proposed cutting "MOHELA-caused defaults >500K" from **65% → 10%**. Will's one-line challenge — *"what goes from 65% to 10%?"* — exposed the error. Decomposed:
- **~10 pts** were a real world-update (first wave-1 data showed no complaint spike; a newly-visible ~1.3M/quarter cure channel meant the default pool churns rather than purely accumulating).
- **~45 pts** were two row defects: federal default is a **270-day** event (the DRG transfer the instrument counts is 360d), so a transition-caused default **could not exist** until ~3 quarters *after* the row's own window closed; and the Instrument column named "servicer-attributed defaults," a series **nobody publishes** — the litigation that would have produced attribution evidence was stayed by court order.

Neither defect is evidence about MOHELA. Booking them as Confidence would have been wrong twice over: it would tell a future reader we abandoned a thesis we still held (the same packet argued the mechanism was intact and proposed a successor at ~50%), and if the row later resolved MISSED it would **score as a good call** — crediting calibration we hadn't earned, for reasons unrelated to whether we read the domain correctly. **A low mark that is right for the wrong reason is worse than a high mark that is wrong**, because it silently inflates the record.

Correct move: **Confidence 65 → 55** (the genuine update only) and **Status OPEN → STUCK** (the window/instrument defects), then retire-and-replace with an in-window, instrument-named successor.

**Apply:**
1. Before re-marking, split the delta into *world-update* vs *row-defect* points. Only the first goes in `Confidence`.
2. Row defects go to `Status` (STUCK) plus a fix to the window/instrument — the row is broken, not the belief.
3. **Coherence check:** a properly-specified successor and the re-marked parent should land close, since they are the same claim. In the failed version they sat **40 points apart** — that gap is the tell. If your replacement and your re-mark disagree wildly, one of them is answering a different question.
4. Distinguish this from an honest MISS: a claim the world falsified is a MISS and *should* cost confidence. This rule is only for claims the world never got the chance to answer.

Extends [[finding_threshold_vs_mechanism]] (mechanism intact vs threshold stuck) from the *threshold* to the *scoring column*. See also [[finding_threshold_spec_fails_before_world]], [[finding_pre_register_against_the_carrying_filing]], [[finding_rebased_metric_check_made_date]], [[finding_discovery_instrument_defines_the_claim]].

## Extension (BRENT, 2026-07-30) — **UNFIREABLE ROWS SILENTLY INFLATE THE CALIBRATION SCOREBOARD**

A ledger-wide sweep applying *"can this even fire / can it resolve?"* to 7 OPEN predictions found **only 2 were clean.** The pattern is worth stating as a rule:

> **A row that cannot fire can never be WRONG. So it sits at high confidence forever, counts as an open question nobody has lost, and makes the scoreboard look better than the forecasting behind it.** The distortion is invisible precisely because nothing ever happens to the row.

⇒ **STUCK rows must be EXCLUDED from any accuracy tally, not carried as OPEN.** Two failure shapes found:

- **Resolution gated on a precondition that has not occurred** — e.g. *"X remains impaired ≥60-90 days EVEN AFTER the chokepoint reopens."* The substance was already **true by 1.4×** (128 days, repair measured in years) and the row **still could not close**, because the reopening never happened. **Carrying it as OPEN simultaneously overstated the open-question count AND understated what was actually known** — a reader of the ledger thought it was unsettled. It wasn't.
- **The compound-gate defect, inside a prediction** — three AND-joined legs required *simultaneously*; the one cleanly measurable leg was a **9.6%** event and another required a **regime flip**. → `[[finding_compound_gate_jointly_unsatisfiable]]`
  **Compounding it:** the row's 82% was confidence in the **consequence GIVEN the trigger**, but no `P(trigger)` was recorded anywhere — so the ledger displayed *"82% prediction"* for something that had never been able to fire. **Record P(trigger) separately from P(consequence | trigger), or the conditional gets read as unconditional.**

**Two more shapes from the same sweep, both worth checking for:**
- **Ambiguous premise** — *"sustains $90+ THROUGH Q2"* had two defensible readings with **opposite verdicts** (80.6% of sessions ≥$90 vs a close of $72.92). **Found because a grading script printed a verdict contradicting its own prose** — the ambiguity surfaced *in the grader*. A prediction that can be graded either way cannot be graded honestly.
- **Threshold contradicting the agent's own thesis** — a registered *"−$20-40"* move landed **below the price floor the same agent's thesis asserted holds.** Registered when the premium was larger; the premium shrank and the threshold didn't. → `[[finding_threshold_level_is_a_measurement_not_a_constant]]`

**⚠️ THE DISCIPLINE WHEN FIXING: change STATUS and NOTES only. Never retro-edit the registered claim or the confidence** — that converts a calibration record into a flattering narrative. **Register disambiguated successors FORWARD**, and say in the note which reading the successor adopts and why.

## Extension (RED, 2026-08-07) — **A GATE RE-DATED TWICE FOR WANT OF AN INPUT IS DRIFTING TOWARD UN-FALSIFIABLE. GIVE IT A BACKSTOP AND A DECLARED FAILURE MODE.**

The rows above are broken by their own *spec*. There is a second, quieter way a falsifier stops being one: **the spec is fine, the world produced the event, and nobody graded it.** Each individual re-date is defensible — you genuinely lack the input, and running the test on absent data would be worse. Repeat it and the gate has silently become permanent.

**Case.** RED's CHG-027 capitulation-review gate needed a BDC recognition cluster. The cluster **printed in the world** on schedule; the owning agent was dark across the window, and a proxy session graded only one name that **pre-dated** the cluster. Second consecutive re-date (7/25-28 → 8/4-8/6 → …), **both caused by input-availability rather than evidence.** Nothing in the row looked wrong at any point: status ACTIVE, a real forward date, an honest reason attached to each slip.

**The tell is the reason-for-slip, not the slip.** One re-date on evidence is normal. **Two re-dates whose stated reason is "the input wasn't produced" is a different object** — and it is invisible in exactly the way the parent rule describes, because a gate that never evaluates can never be lost.

**Apply, when you catch the second slip:**
1. **Change the status to something that reads as broken** (`ACTIVE-BLOCKED`, not `ACTIVE`) so a downstream reader cannot mistake "not evaluated" for "evaluated benign." **Never let an ungraded gate score benign-by-default** — absence of an adverse grade is not an adverse-free grade. See [[finding_count_what_published_before_reading_the_verdict]].
2. **Set a HARD BACKSTOP date and write the failure mode into the row now**: at the backstop you resolve on whatever partial evidence exists and record the gate as **having failed on data availability, not on the world.** A named bad outcome is what makes the deadline real; a date alone slips again.
3. **Route the ASK to whoever can produce the input, with the fix specified** — usually the work is already scoped in the owner's own notes and does not need you. **Flag it at the point you notice, not at the deadline**, so the three weeks are usable.
4. **Say it about yourself in the same words you'd use about someone else.** This is the drift you would flag instantly in another agent's book; the only reason it survives in your own is that each step was locally reasonable.

Pairs with [[finding_audit_resolution_path_before_reattempt]] (resolution is usually blocked by the PATH, not by missing data) and [[finding_never_received_is_not_doesnt_hold]]. The parent rule keeps a broken row from corrupting `Confidence`; this extension keeps a *never-evaluated* row from quietly becoming an assumption.
