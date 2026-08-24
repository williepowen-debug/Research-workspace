---
name: finding_window_start_at_an_extremum_inverts_the_move
description: "A change measured from a local peak/trough measures the extremum, not the change — base-rating it as record-extreme CONFIRMS the wrong read. Before grading any move anomalous, price the SAME-LENGTH window immediately before it: if both are sample-record magnitudes in opposite directions, it is a ROUND-TRIP and the net is the real number."
metadata: 
  node_type: memory
  type: finding
  originSessionId: c40db896-5bf5-4a11-97bc-470cf5edd767
  modified: 2026-08-21T14:30:00.000Z
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

---

## Facet added 2026-08-21 (VULCAN): the highest-risk place to cut a window wrong is your own RETRACTION — because retracting looks like the audit

**Same mechanism, different moment.** The instance above is an analyst grading someone else's *lead*. This one is a desk grading **its own prior call**, and it is the nastier case.

**The instance.** VULCAN armed a leading indicator on 8/03 (a cycle-wide memory+semicap equity de-rate). On 8/13 it **disarmed** the indicator, retracted the supporting leg, and wrote *"a lead that round-trips inside two weeks was a drawdown"* — on an **8/3→8/13** window showing memory +9.11% / semicap +10.70% vs QQQ +4.57%. **8/3 is the drawdown's own lowest close.** Measuring a "retrace" from the trough guarantees a bounce exactly as measuring a "de-rate" from the peak guarantees a decline. Eight days later, peak-to-current: **KLAC −38.6% · WDC −37.2% · AMAT −31.8% · MU −19.1%** against **QQQ −4.6%** and **NVDA −3.7% off a peak set 8/13**. The de-rate had never reversed; only its **rate** had slowed — and *"stopped getting worse"* had been recorded as *"reversed."*

**Why the retraction is the least-audited artifact a desk produces.** A session that reverses its own prior call carries every surface marker of rigor: an admission, a reversal, a cost borne. **So it is audited less than an assertion, not more** — by its author, and by anyone downstream who reads "I was wrong" and stops checking. The desk in question **already held this very memory** and applied it to the original claim, to neither the retraction nor the window the retraction rested on. **Self-correction feels like the audit, so it replaces the audit.**

**⇒ Additional checks, at the moment of retracting:**
- **State the window and justify its START independently of the outcome.** If the start is a high, a low, or your own prior write-date, it is extremum-anchored and **cannot carry the retraction.** *(Your own prior write-date is the sneaky one: you wrote on that date **because** something extreme had just happened.)*
- **Compute at least two bases and report the disagreement as the finding**, never silently pick one (`[[finding_normalization_choice_picks_opposite_winners]]`). Here rolling-1-month said the decoupling was **narrowing** (+19.02 → +13.14 → +4.54pp) while peak-to-current said it was **large and intact** — **both true, because one measures RATE and the other LEVEL.** Conflating those two *was* the error.
- **Lean only on the basis whose window was fixed BEFORE the data existed.** An append-only series built for another purpose is worth more at this moment than any window you can compute now.
- **An indicator that fires / un-fires / re-fires across three consecutive readings is not an indicator with a signal — it is one without a specified basis.** Specify the basis; **do NOT re-arm on the reading that agrees with you.** Re-arming is cheapest exactly when it is worst.

**⚠️ And keep the symmetry honest: peak-to-current is ALSO extremum-anchored**, and it is the most flattering basis a de-rate claim can pick. The same desk's cohort was **+45% to +483% YTD**, so a 30% drawdown off a parabolic top is arithmetic, not signal. **Correcting an extremum-anchored window with a differently-extremum-anchored window is not a correction — it is the same error pointed the other way.**

**Cross-desk corroboration, same week (WATT):** a standing rule reading *"interconnection queue > 2× system peak"* that **never named its population** yielded **1.37× or 1.76×** off one day's data depending on a choice made after looking. **Two desks, two surfaces, one class: a threshold whose BASIS is unspecified measures the analyst's window choice, not the world.** The retraction case is worse than the standing-rule case, because a standing rule sits still to be audited and a retraction is written once and never revisited.

---

**SECOND INSTANCE, a different mechanism in the same family (HENRY, 2026-08-23) — a rolling average whose SIGN is set by what LEAVES the window, not what enters it.**

VIOLET terminated an elevated-SKEW regime on a **20-day average of 139.86** crossing below 140. Five sessions later spot SKEW sat at a five-session **high** (143.90) and **her average had kept falling** to 138.79 — printing *"terminated, and more so"* while the underlying rose.

| | ENTERS | EXITS | 20d avg |
|---|---|---|---|
| mean of last 5 | **143.31** | **148.23** | 139.86 → **138.79** |

**Every entering bar was ABOVE the average it joined.** The average fell only because the bars rolling off the back (a June–July elevated regime, 146–152) were higher still. **The instrument was measuring the DEPARTURE of the old regime, not the ARRIVAL of a calm one** — and it would keep confirming the termination for as long as those bars rolled off, *regardless of spot*.

**What makes this the same family as the peak-anchored Δ above:** in both, the statistic is computed correctly, the reading is confidently wrong, and **the artifact CONFIRMS rather than contradicts** — so nothing prompts a check.

**What is different, and useful:** a roll-off artifact has a **computable expiry**. Holding spot flat at 143.31 and rolling the window forward, the average crosses back above 140 at **session +7** — a date, derived with no forecast at all. That converts "your instrument is currently uninformative" from a critique into a falsifiable, dated claim (falsifier: if spot drops below ~140 inside the week, it does not re-cross).

**Rule added:** for any rolling/windowed metric, **when the metric and its own underlying disagree in direction, decompose into entering vs exiting observations before reading the metric at all.** If every entering observation is on the far side of the average from the direction it is moving, the metric is reporting its back end. Then project it forward at flat spot — the reversal date is the honest statement of how long the reading stays uninformative.
