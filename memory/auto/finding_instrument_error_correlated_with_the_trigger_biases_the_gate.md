---
name: finding_instrument_error_correlated_with_the_trigger_biases_the_gate
description: "When an instrument's own error GROWS with the event it measures, the gate reading it is biased in one direction and NO threshold choice fixes it — a floor smaller than the instrument's inter-vendor spread is not a threshold, and the window is UNGRADEABLE rather than merely noisy"
symptoms: "the threshold is smaller than the vendor disagreement; two trackers disagree by more than the trigger; the gate got MORE likely to fire during the outage; the measurement error and the event have the same cause; we can grade it if we just pick the better tracker; the window closed NOT MET so the premium is ours"
metadata:
  node_type: memory
  type: finding
---

A gate has **two** specifications, and only the numeric one usually gets reviewed: the **level**, and the **instrument that reads it**. This is a defect in the second that no amount of care with the first can repair.

**BRENT, 2026-09-12 → 09-14, n=3 on one desk in three days.** `BG-02`'s Petroline throughput resolver was written as *"a floor of ≥0.7 mb/d Yanbu/export loss on a 7-day MA."* The desk then measured what its own instruments do: **the inter-vendor spread on that quantity is 0.8 mb/d — LARGER than the 0.7 floor itself.** ⇒ which vendor you pick decides the verdict. **A floor smaller than the disagreement between the instruments that read it is not a threshold; it is a coin flip with a number written on it.**

## The sharper half, and it is the half that does not appear anywhere else

⛔ **The error is not symmetric noise. It is CORRELATED WITH THE TRIGGER.**

The instrument is AIS/satellite tanker tracking. **A real extended outage RAISES the dark-fleet share** — vessels go unreported precisely when the disruption is worst. So the measurement error and the event being measured have the **same cause**, and the error grows in the direction that makes the gate look satisfied.

> **During a real event, the instrument's error and the event are confounded BY CONSTRUCTION.**

This is categorically worse than being inside a noise floor, and the two must not be treated as one problem:

| | Detection floor (symmetric) | Correlated error (endogenous) |
|---|---|---|
| What you get | **No evidence either way** | **Biased evidence, in a known direction** |
| Fix by moving the threshold? | Yes — widen it past the floor | ⛔ **No. Every threshold inherits the bias.** |
| Failure mode | You conclude nothing | **You conclude something false, confidently** |
| Sibling canon | `[[finding_effect_below_instrument_detection_floor]]` | *this* |

⚠️ **So the remedy is never "pick the better tracker" or "tighten the floor."** The remedy is to say the window is **UNGRADEABLE on that leg** and require either (a) a leg whose error is *independent* of the event — a **statement-based** resolver, an official declaration, a contract date — or (b) all legs jointly, with the dark-share disclosed as a stated quantity rather than absorbed silently.

## Three rules that fall out, in the order they are usually violated

1. **Compare the floor to the instrument's own spread BEFORE registering the level.** If floor < spread, the letter is defective at registration and no observation can repair it.
2. **Ask which way the error moves during the event.** If it moves toward firing, the gate is a *one-way* instrument — it can manufacture a fire, and it can never manufacture a refusal. ★ Ask it as: *does my measurement get worse precisely when the thing I am measuring happens?*
3. **Pre-register the ungradeability BEFORE the window opens, never after it closes.** BRENT did this on 2026-09-14 for a window opening 9/17 — and that ordering is the whole value. Declaring a window ungradeable *after* an inconvenient reading is indistinguishable from `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]`.

⛔ **A LAPSE IS NOT A PASS.** When such a window closes unmeasured, `NOT MET` is a statement about the *instrument*, not about the world — it must never be banked as evidence the event did not happen, and never as a premium earned. *(Here a 3–5 week repair estimate put the entire 9/17–9/25 measurement window inside the outage, making LAPSE the modal outcome from the day it was registered.)*

## Why it recurs, and why the discoverer is the one least able to act

⚠️ **The desk that owns the gate is the desk whose convenience the defect serves**, so the correction is structurally under-supplied. Here the desk **impeached its own resolver, in the direction that made its own gate harder to fire**, and separately refused to set a missing session-count on a neighbouring gate *because the level had already gone through* — *"any number chosen now is chosen knowing the answer."* Both are the same discipline: `[[finding_instrument_defect_enacts_what_its_owner_is_fenced_from]]` — **the tell that you are about to re-tune a leg is that the fix helps you.**

⚠️ **It also survives review because every check on the NUMBER passes.** 0.7 is a real, reproducible, defensible figure; 0.8 is a real, reproducible, defensible figure. Nothing is miscalculated. The defect lives in the *relation between them*, which no per-figure audit inspects — the same reason `[[finding_crosscheck_with_free_parameter_validates_nothing]]` and the relabel class survive.

**Registered instances:** `WQ-234` (the narrow, desk-specific claim, to Will, needed-by 2026-09-18). The general form is this memory. Related: `[[finding_resolver_anchored_to_expected_event_inherits_slip_risk]]` governs the *date* a resolver hangs from; this governs the *instrument* it reads. They compose — a row can be correctly anchored and still ungradeable.
