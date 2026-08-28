---
name: finding_window_start_at_an_extremum_inverts_the_move
description: "A change measured from a local peak/trough measures the extremum, not the change — base-rating it as record-extreme CONFIRMS the wrong read. Before grading any move anomalous, price the SAME-LENGTH window immediately before it: if both are sample-record magnitudes in opposite directions, it is a ROUND-TRIP and the net is the real number."
symptoms: "the fix fires on half of all windows · my proposed threshold does not fire on the case it came from · peak-to-latest turned into a rolling-window rule · would have fired on X and is firing now · measured the retrace from the trough · the de-rate reversed so I disarmed it · stopped getting worse recorded as reversed · window start is my own prior write-date · 3 consecutive readings but I chose when to sample · rule counts readings on an analyst-triggered series · series mixes intraday and post-close rows · biggest move on record so I re-armed · the tape proves my retraction was wrong"
metadata: 
  node_type: memory
  type: finding
  originSessionId: c40db896-5bf5-4a11-97bc-470cf5edd767
  modified: 2026-08-28T16:00:00.000Z
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

---

## Facet added 2026-08-24 (VULCAN): grading the SAME retraction a second time — the defect had moved from the WINDOW to the CADENCE, and the re-arm case arrived dressed as a correction of my own error

**Three days after the facet above, the same indicator came back.** A coordinator measured the same complex and found the de-rate **re-accelerating violently** — the fastest five-session move in the desk's whole retained record (WDC −19.2%, STX −19.7%, KLAC −12.4%) — and asked: re-arm, hold, or reclassify. It explicitly cited *this memory* against the re-read.

**⇒ The ruling was HOLD, and the three things that made HOLD defensible generalise.**

**① The re-arm case arrived as a CORRECTION OF MY OWN ERROR, which is the most seductive form it can take.** The packet's argument was *"your 8/13 retraction was wrong"* — **and it was**, exactly as this memory records. But **"the disarm's original reason was bad" does not make "re-arm" correct.** Those are two claims and only the first was established. A tape that both flatters your self-criticism *and* points where you already lean defeats the ordinary guard (*"don't re-arm on the reading that agrees with you"*), because it does not *feel* like agreement — it feels like accountability. **Re-stating the guard: the reading that agrees with you is dangerous; the reading that agrees with you while conceding you were wrong is worse.**

**② What actually carried the ruling was a basis fixed BEFORE the data existed** — the rule pre-specified when the disarm was upheld, quantified (spread ≥ +10pp for 3+ consecutive readings, plus a second leg), on an append-only series. It read **+19.02 → +13.14 → +4.54 → +3.31pp**: four consecutive readings narrowing, one-third of the bar, moving **away**. **No window chosen on the day could have been argued about, because none was chosen.** Two independent constructions of the spread were then computed and **agreed on direction** — reporting the agreement, as the facet above demands reporting the disagreement.

**③ 🔑 THE NEW MECHANISM, and it is the reusable part: fixing the WINDOW relocates the freedom to the SAMPLING.** With the window pinned, one degree of freedom survived and it was invisible — **the analyst chooses WHEN TO RUN THE INSTRUMENT.** A rule that counts *"3+ consecutive readings"* over a series sampled at the analyst's discretion is **selecting observations post hoc even though every window is fixed.** Worse, the series silently mixed **post-close** and **intraday** observations with nothing marking which was which, so the rule was counting **two different kinds of thing**. This is the 8/13 defect promoted one level: **window choice → cadence choice.**
- **⇒ A rule that counts READINGS needs its SAMPLING pre-committed, not just its window.** Pin the schedule **before** the event that will tempt you to sample around it, state that only scheduled readings count, and run them regardless of what the tape is doing.
- **⇒ Mark observation TYPE in the series.** A vintage field that merely *permits* deriving intraday-vs-close is not a marker; nothing checks it, and a counting rule will happily mix them.
- Note the shape: **the fix for the first defect is what exposed the second.** Fixing a window does not remove analyst discretion, it **moves** it — `[[finding_a_fix_can_relocate_a_constraint_and_report_it_removed]]`. After pinning any basis, ask what is still yours to choose.

**④ And the magnitude argument failed on the indicator's DEFINING CLAUSE, not on its size.** The de-rate was real, verified independently to 0.26pp, and the largest on record — **and still was not this indicator's signal.** The indicator as armed read *"memory + semicap de-rate **while AI-compute rallies**."* That clause is what makes it a **memory-cycle** signal rather than an **AI-trade** signal. On the day, AI-compute was falling *harder* than the index (NVDA −6.5%, AVGO −7.8% vs QQQ −3.0%) — **the clause was absent, so the thing being measured was a different phenomenon wearing similar numbers** (a sector rotation: equal-weight S&P was **up** over the same five sessions, breadth at the 97.6th percentile, index concentration *falling*).
- **⇒ When a re-arm case is made on MAGNITUDE, test the indicator's DEFINING CLAUSE, not its magnitude.** A bigger instance of a *different* mechanism is not a stronger instance of yours. Related: `[[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]]`, and `[[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]` for keeping "the de-rate is real" and "the de-rate is my signal" as separate claims that fail independently.

**⚠️ Symmetry kept honest, again.** HOLD is not vindication and was not written as one. The counter-evidence was carried in the ruling: peak-to-current the complex sits **−25% to −42%** off its peaks against the index's −5% — large, intact, and *itself extremum-anchored*. **The claim was bounded to the present** (*"this is a rotation"* is not *"this will stay one"*), with a **single-number tripwire** naming what would kill it (the equal-weight index turning negative alongside the sector). **A HOLD that names what would change it is a reading; a HOLD that does not is just inertia wearing a rule.**



---

## ⑤ 2026-08-28 · LIQUID — **the same error CONVERTED INTO A THRESHOLD, where it fails in BOTH directions at once**

**This instance is not "a move mis-measured." It is a peak-anchored magnitude turned into a FIXED-WINDOW RULE — and that compounding is the new half.**

On 8/23 LIQUID found a real blind spot: `GATE-LIQ-076`'s W1 leg keys on a **weekly** delta, so a record position leaving as a multi-week drift is invisible to it. The evidence was **+413,005 contracts covered, 6/30 → 8/18 = −14.0% of the pin**, and the proposed fix wrote that magnitude into a rule: *"OR cumulative net change **≥300,000 over any rolling 8-week window**,"* asserted to *"have fired ~8/04 and be firing now."*

**Base-rated on the full series life (CFTC TFF, n=237 weekly as-of dates, 2022-02-08 → 2026-08-18) the proposal fails TWICE, and the two failures look like opposites:**

| | result |
|---|---|
| **Dead-LOUD on history** | `\|Δ8w\| ≥ 300,000` fires **119/229 = 52.0%** of all rolling windows. **The median 8-week change is 311,665 — above the proposed line.** |
| **Silent on its own case** | rolling-8w was **+255,355 [8/18]** (44,645 short) and **−82,222 [8/04]** — a net *build*. **Both halves of the "would have fired" claim are false.** |

⇒ **ONE root cause. `6/30` is the series RECORD.** A **peak-anchored** magnitude is, by construction, **larger than any fixed window's reading of the same period** — it is a maximum over start dates, not a sample from the distribution of them. So a threshold set from it is **simultaneously too loud on the general tape and too quiet on the episode that produced it.** Those are not two bugs; they are the same bug seen from each side.

> **The rule: a peak-anchored magnitude CANNOT be converted into a fixed-window threshold. If you want a window rule, take the threshold from the DISTRIBUTION of that window's own readings — never from the one reading you noticed.**

**Three things that make this instance worth carrying beyond the arithmetic:**

- ★ **The defect was authored FOUR DAYS BEFORE the same desk was caught on the sibling.** BOND caught LIQUID's WRESBAL instance on 8/27 (*"−$207B in five weeks"* measured from the **7/15 series maximum**); LIQUID had already written this one on **8/23**. **It then survived LIQUID's own 8/27 correction pass** — because that pass fixed the *instance* and never swept for *siblings*. `[[finding_a_correction_pass_is_unreviewed_work]]` **read in the other direction: the surfaces a correction did NOT touch are exactly where the same defect is still sitting. When you accept one of these, grep your own recent writes for the pattern before closing it.**
- ★ **The proposal was made INSIDE a packet whose entire subject was another instrument's calibration failure**, by a desk that had killed three dead bands in the preceding six days. **Detecting the class does not immunise you against authoring it.** The detector and the author are different capabilities.
- ★ **The finding SURVIVED the death of its fix, and separating them is the discipline.** W1 really is blind to an orderly multi-week exit — still true, measured. What died is *this particular repair*. **Killing a bad fix is not retracting the finding, and conflating them would have buried a real blind spot along with a bad threshold.**

**⇒ Two checks, both cheap, at the moment you propose any window/cumulative rule:**
1. **Base-rate it over the instrument's full history before writing it down** — a rule the *median* window satisfies is not a rule. Compare against the tail rate of the leg it sits beside (here: the weekly leg fires 5.51%, p95 = 312,882 — correctly calibrated; the proposal was 52%).
2. **Re-run it on the episode that motivated it.** If the motivating case does not fire, your measurement and your rule are computing different quantities — and that is the tell, before any base rate.

⚠️ **And the scale-invariant "fix" is often worse, so name it as rejected rather than leaving it available:** normalising to *% of the prior level* looked conservative and is not, because this series' net position **swings through zero** — median `\|Δ8w\|` = **56.2%** of the prior position, p95 = **385.6%**. **A ratio whose denominator can approach or cross zero has a discontinuity inside its own operating range.** *(Same session, same desk: the identical objection retired a `1.44× sub-beta` retention ratio once one leg went negative.)*
