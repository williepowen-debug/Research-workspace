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
