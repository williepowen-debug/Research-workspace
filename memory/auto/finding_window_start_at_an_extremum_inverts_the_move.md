---
name: finding_window_start_at_an_extremum_inverts_the_move
description: "A change measured from a local peak/trough measures the extremum, not the change — base-rating it as record-extreme CONFIRMS the wrong read. Before grading any move anomalous, price the SAME-LENGTH window immediately before it: if both are sample-record magnitudes in opposite directions, it is a ROUND-TRIP and the net is the real number."
metadata: 
  node_type: memory
  type: finding
  originSessionId: c40db896-5bf5-4a11-97bc-470cf5edd767
  modified: 2026-08-16T02:33:23.246Z
---

**Correctly measured, correctly base-rated, and still inverted — because the window started at a peak.**

**The instance (2026-08-15, SAM → BOND, foreign-official UST custody).** SAM handed BOND a lead: H.4.1 marketable-UST custody fell **−$59.8B** from its 7/29 level to 8/13, *"the same order as the op estimates"* for a Japanese FX intervention on 7/30-31. Four Wednesday levels, pulled from the Fed primary, every number correct. BOND pulled **57 releases** to base-rate it — and the decline **is** the largest 2-week decline in a 14-month sample (z = −1.68, 2nd percentile). **The base rate confirmed the alarming read.**

Then the fortnight *before* the window:

| Window | Δ | z | percentile |
|---|---:|---:|---|
| **BUILD** 7/16 → 7/30 | **+58,716mn** | **+2.45** | **100th — largest 2wk build in sample** |
| UNWIND 7/30 → 8/13 | −59,791mn | −1.68 | 2nd |
| **NET** 7/16 → 8/13 | **−1,075mn** | — | **≈ zero** |

The level rose ~$59B *into* the event and came straight back: the 8/13 print sits within **$1.1B** of 7/16 and **$0.4B** of 7/09. **Read from the peak it says foreign officials sold $60B around an intervention. Read whole it says nothing happened.**

**Why base-rating does not save you.** Base-rating asks *"is this move unusual?"* — and a move off a local extremum genuinely **is** unusual, because reaching the extremum was unusual. The statistic is right and the inference is wrong. **The base rate confirms rather than corrects, which is worse than having no base rate at all**, because it launders a selection artifact into a quantified finding.

**⇒ The check, and it is one extra query.** Before grading any Δ as anomalous, price the **same-length window immediately preceding it** on the same base rate. Then:
- **Both extreme, opposite signs ⇒ ROUND-TRIP.** Report the **net**; the halves are an artifact of where you cut.
- **Prior window unremarkable ⇒ the move is real.** Now the base rate means what you wanted it to mean.

**The round-trip signature is the reusable tell:** *two* sample-record magnitudes back-to-back in opposite directions is not two rare events, it is one cut in the wrong place. **And the BUILD was the more anomalous half (z +2.45 vs −1.68)** — the half nobody looked at was the half carrying the information.

**Mechanism discrimination, which is where this pays.** A funding operation that sells reserves leaves a **level change**. A round-trip is what **custodian shifts, redemptions, and settlement timing** produce — which is exactly where SAM's own three stated caveats pointed (*all foreign officials not Japan · redemptions cut custody with no sale · custodian shifts move balances with no transaction*). **Ask what shape the proposed mechanism should leave, then check whether the data has that shape.** A round-trip refutes "they sold to fund it" without needing any counter-evidence.

**⚠️ Do not let the correction overshoot.** The **secular** decline in that series is real and large — **YoY −$258B** on the same line. The finding is the narrow one: *the op window contributed approximately nothing to it.* "Round-trip" must not travel as "the trend is fine."

**Generalises to every stock/flow series where a level is cut into windows** — reserves, fund flows, dealer inventories, open interest, custody, positioning. Related but distinct trigger: `[[finding_new_pin_needs_trajectory_before_level_read]]` fires when you have **no** history (a fresh pin) and covers this as a buried secondary case (*"Δ7d −5 was measured off the local 7/24 spike, not the base"*). **This one fires when you DO have the history and still cut it wrong** — SAM had four points and was still inverted. See also `[[finding_base_rate_the_instrument_before_its_event_table]]` and `[[finding_divergence_requires_fresh_likeforlike_baseline]]`.
