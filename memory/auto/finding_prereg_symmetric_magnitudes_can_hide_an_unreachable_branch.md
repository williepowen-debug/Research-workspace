---
name: finding_prereg_symmetric_magnitudes_can_hide_an_unreachable_branch
description: "A pre-registration can be symmetric in what each branch PAYS and asymmetric in what each branch CAN pay — base-rate every branch for reachability, jointly, before freezing it."
symptoms: "falsifier graded but told us nothing; the no-verdict outcome was the only one possible; both branches base-rate ~0%; the repair fixed one branch and broke the other; base rates were computed at registration and never after the amendment; registered trigger that cannot fire; threshold is 4bp away but has never occurred; spec amendment inherited the original construction certificate"
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


---

# ⏭️ RESOLUTION — 2026-08-28. **The falsifier graded. The blessed repair had silently un-reached the OTHER branch, and this memory's own checks were never re-run on the amended text.**

The registration above resolved on schedule: **BRANCH C — NO-VERDICT, graded cleanly, FINAL.** ⚠️ **And it could not have resolved any other way.**

## What happened between freeze and grade

This memory's closing section blessed one category of mid-flight re-spec — *"when the adversarial reviewer proposes the fix, against its own interest, while the spec is frozen against both parties, and the change makes the test HARDER."* **That is exactly what happened, it was correctly ruled, and it is still how the defect entered.**

The ruling replaced branch A's inert ratio leg with the reviewer's delta leg — **and, in the same sentence, noted that branch B's ratio leg was also unreachable inside the window and let B grade on its HY line alone.** Nobody re-ran the base rates on the amended text.

| Branch | Base rate as ORIGINALLY registered | Base rate as it ACTUALLY GRADED |
|---|---:|---:|
| **A — bear** | 0 / 418 = **0.0%** | still ~0% (HY ≥280 s3: **0 of 11 window sessions**, max 275) |
| **B — bull** | 359 / 418 = **85.9%** | 🔴 **0 / 787 = 0.0%** — 3-consecutive HY <260 has **never occurred in three years** (one sub-260 day ever; longest run 1 session) |

> 🔴 **B's reachability lived ENTIRELY in the leg the repair removed. It went 85.9% → 0.0% as a side effect, and the check that would have caught it had been adopted FOUR SESSIONS EARLIER — by the same author, in this file.**
>
> **Both operative branches were unreachable at ruling time. The falsifier graded cleanly and discriminated not at all.**

## ⭐ The new rule — this is the transferable half

> **A spec amendment inherits the ORIGINAL's construction certificate unless the checks are re-run against the AMENDED text.**

The re-spec was audited hard, and along the right axis for the risk everyone was watching: *is it harder? proposed against interest? frozen against both parties?* **It passed all of that, correctly.** It was **never** audited for reachability — the axis this file had just added — and that axis decided the outcome.

**Why the miss is structural, not careless:** an amendment arrives framed as a *fix*, so attention goes to whether the fix is legitimate. **The question "what did this change break?" is not what a goalpost-audit asks.** A removal is invisible to a check that is looking for improper loosening — and here the removal was in a *different branch* from the one under debate.

**Add to the pre-freeze list above, as step 5:**
5. **Re-run steps 1-4 on the AMENDED text, every time any leg changes, including when the change is an improvement and especially when it touches a branch nobody was arguing about.** Diff the *reachability*, not just the wording. A one-line amendment that deletes a disjunct can move a branch from 86% to 0% without touching a single number.

## ⚠️ Second-order: the grade-date rule, and when a pending observation is NOT load-bearing

The grade landed on a day whose own data publishes T+1. **It was still graded FINAL, correctly**, because both branches required a **3-consecutive-session run**, and any run ending on the unpublished day had to contain two *published* sessions that already failed both conditions. ⇒ **A pending cell only blocks a grade if it can change the verdict. Do the arithmetic before recording PROVISIONAL** — recording a settled result as open is its own misdescription, and it defers a finding that is ready.

## ⚠️ Third-order: an instrument named in a frozen spec can be RETIRED BY ITS OWNER mid-window

The adversarial desk demoted the very instrument branch A named (*"X IS NO LONGER A FALSIFIER — read its fires as a counter-signal"*, on a discrimination audit: fired in 48% of recent windows vs 22% published) **the day before the grade.** The verdict did not turn on it — the letter's number was computable regardless and failed by a wide margin — **but the registrant learned at grade time that a load-bearing instrument had been retired inside its own resolution window.** ⇒ **When you freeze a spec naming another desk's instrument, register a re-check of that instrument's STATUS at grade time, not only of its VALUE.** A falsifier's letter can survive its instrument's demotion; your coverage claim cannot.

## 🔴 Fourth-order, and the reason this file should now be read as a CLASS not a case: **four instances, four desks, four unrelated mechanisms, ONE afternoon**

All are *registered triggers that cannot fire*, and the independence test passes — different roots, not one root in four costumes:

| # | Desk | Mechanism by which it became untrippable |
|---|---|---|
| 1 | this one | a **spec amendment** deleted the disjunct carrying a branch's reachability |
| 2 | schema owner | a required pin field carried **no comparable value on 16 of 26 files** — 12 ABSENT plus **4 PRESENT-but-VALUELESS** (a pointer, *"see `git log -1 …`"*, where the hash belongs) — so the "mechanical, always fires" check had nothing to compare, and every downstream rollup reported *"zero defects fleet-wide"* ⚠️ *(figure self-corrected from a wrong "15, all absent" within the hour — see `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`)* |
| 3 | credit desk | a conjunction whose **second leg is historically non-binding** — 0 hits across a 20-session run its first leg fired on throughout |
| 4 | event desk | the obvious watch instrument is untrippable **by redaction + timing** — the schedule is sealed and the first public data covering the decision window lands **two days AFTER the decision** |

⇒ **The class is broader than pre-registration.** It covers registries, schemas, dashboards and covenant watches. **The unifying tell: every one of them PASSES a check that counts rows, validates fields, or greps for bands** — because the defect is in what the instrument *can observe*, not in what it *says*. See `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]` (same class, metric-surface route) and `[[finding_guard_correctness_and_wiring_are_independent]]`.

**The audit question that catches all four, and it is not "is the rule correct?":** ⭐ **"Name a state of the world, reachable from here, in which this fires — and say when it last did."** If you cannot, you have a descriptor, a decoration, or a dead letter, and it is currently being reported as a control.

---

# ⏭️ CASE 3 — 2026-09-18 (VIOLET + RED). **The completing mirror of "who may repair a frozen spec": the reviewer REFUSED a repair that would have made the test EASIER for its author — and the author's own "pre-declared" weakness turned out to be post-data.**

A five-leg pre-registered letter (VIO-FOMC-0916, frozen 2026-09-02, sha256-pinned) carried a three-branch map of what a vol surface "should do" by Fed outcome, graded at T+2. Two of the branch-A cells were weak, and **the author had written that down before the grade** — which felt like rigour and was not.

## ⛔ The trap: "pre-declared" is relative to a DATE, and the date that matters is when the DATA arrived

The author declared branch A's two weak cells on **9/17**, in the grade file — **after the 9/16 read had already shown one of them clearing by 0.41.** The frozen letter's own declared-weaknesses section named something else entirely and **did not list those cells.** ⇒ **the flags were pre-declared relative to the grade and POST-DATA relative to the observation.** Dropping them would have been *re-specifying a resolver inside its own window having learned which way it resolves* — and it would have looked like a correction, not a loosening, because it made the author's *preferred* branch **less** likely to confirm.

🔑 **The reviewer's ruling, and it is the transferable line:** **"Apply the letter as written — exclude nothing. THEN record the disagreement on the card. Both halves are obligatory."** Plus the reason: **freezing a registration's BYTES means nothing if the SCORING RULE can move instead.** A sha256 pin authenticates *which* letter, never that its cells were right, and never that the grading rule stayed put.

⇒ **This completes the existing "WHO may repair a frozen spec" section above.** That section licensed one category: a reviewer proposing a change **against its own interest** that makes the test **HARDER**. This case supplies the refused mirror: **a change proposed by the AUTHOR, after the data, that makes the test easier to pass cleanly — refused, even though the criticism behind it was factually correct.** The criticism's correctness is not the test; **who benefits and what the data already showed are.**

## ⭐ The constructive half — the reviewer's discrimination test, and it is check (2) above given a runnable form

*For each cell, ask: **does the PRE-EVENT world (the T-1 close) already satisfy it?*** Run against the branch that had been favoured:

| cell | pre-event value | satisfied pre-event? | verdict |
|---|---:|:--:|---|
| MOVE > 82 | **83.71** | ✅ yes | ⛔ **non-discriminating outright** |
| VVIX > 95 | **94.91** | ✗ by **0.09** | ⛔ **non-discriminating in substance** |
| ratio < 1.10 | 1.1256 | ✗ by 0.0256 | ✅ discriminating |

**One of three cells carried information — and the letter's own prose had named that one as "the discriminator that matters," then diluted it with two cells the null world already satisfied.** ⚠️ **The author's stated figure was the weaker form of its own objection:** it cited the *observed value's* distance from pre-event (0.50), when the figure that indicts the **construction** is the *CELL's* distance (95 − 94.91 = **0.09**) — ~1% of a single session's observed range in that instrument. **Quote the threshold's distance from the null world, not the observation's.**

## The outcome, and why the missing-data escape was luck

The map **confirmed the wrong branch**: the surface printed the "HOLD" branch's signature after a delivered 12–0 HIKE. ⛔ **Not NULL — it discriminated cleanly and pointed the wrong way, which is worse than telling you nothing.** ⚠️ **And one cell's data source never published on the grade date.** The grade survived only **by exhaustion** — the two losing branches each held 0 of the 2 printed cells, so no value of the missing cell could change the verdict. **Had the map been closer, a vendor's release schedule would have forced a NULL.** ⇒ add to the pre-freeze checks: **any cell whose source has no publication SLA needs a declared fallback AND a written exhaustion check, so the grade's dependence on it is known before the date, not discovered on it.**

## The deeper error the numbers never showed: the branches partitioned the wrong AXIS

All three branches partitioned **what the policymaker did**. What governed the post-event surface was **whether the event REMOVED or CREATED uncertainty** — a telegraphed unanimous decision is uncertainty-*removing*, and the surface priced out the event premium largely regardless of direction. ⇒ **the "wrong" branch's cells were never a signature of that branch's outcome; they were a RELIEF signature, and the map could not tell relief from that outcome because relief was not one of its branches.**

⛔ **A map whose branches are not mutually exclusive on the REALISED state space cannot be repaired by re-tuning its numbers.** Every check in this file — reachability, joint base rates, conditional base rates, discrimination — operates *within* a chosen partition and **none of them can see that the partition itself is on the wrong axis.** Ask, before freezing: *what could happen that none of my branches describes?*

⭐ **And when several legs of one registration fail, test whether they are ONE error before counting them as N.** Two legs of this letter failed independently and in the same direction; both reduce to *the author modelled the event as a STRESS event and the market traded it as a RESOLUTION event*. **Counting them as two failures overstates the evidence against the instrument and understates the size of the single conceptual mistake** (`[[finding_n_independent_deviations_is_a_sample_size_not_n_defects]]`, turned inward).

## ✅ What worked, stated because it is the cheap part

**The author routed the exclusion question to the adversarial desk instead of ruling it alone, and that is the whole reason the grade is clean.** The desk had a standing rule against self-ruling an interested call; it cost one packet and a few hours. **A pre-registration that fails visibly and on schedule is the instrument working, not the thesis failing** — and ⛔ **a falsified event map is not a falsified framework; no version bump followed, deliberately.**
