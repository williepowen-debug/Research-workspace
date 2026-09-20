---
name: finding_a_spread_needs_a_basis_neutral_to_what_its_legs_do_not_share
description: "Putting both legs of a spread on the SAME basis is not enough and is the thing that hides the bias: if the legs differ in a property the basis ignores — one pays a dividend, one does not — identical treatment debits one leg one-sidedly, and every internal-consistency and arithmetic check reproduces it cleanly."
metadata:
  type: feedback
  symptoms: both legs use the same series so the comparison is fair · I used closes for both names · the spread went negative and I explained why · a reviewer reproduced my arithmetic exactly · relative drawdown vs a peer · excess return over a benchmark · A outperformed B on N of M days · the ruling named the threshold and the base and the window · price return vs total return · one name pays a dividend and the other does not
---

**A spread is not made sound by putting both legs on the SAME basis. It is made sound by a basis that is NEUTRAL with respect to the properties the legs do not share.** Identical treatment of unlike things is the bias, and it is invisible precisely because "I used closes for both" sounds like rigour.

**Bought 2026-09-19, by CRUISE, against its own headline finding of the same day.**

`VX-CRU-06`'s falsifier (WQ-222, Will-ruled) measures **CCL's excess drawdown over RCL** from a fixed base, on each close, through the Q3 print. Both legs were computed on unadjusted daily closes — the same series, the same source, the same convention. **RCL went ex-dividend $1.50 inside the window. CCL's last dividend predated the base and the third operator pays none.** So the comparison silently debited the payer by 0.565pp from the ex-date onward.

The two affected readings **flipped sign**: −0.3745 → +0.1904 and −0.4490 → +0.1159. The desk's published finding — *"CCL, the only UNHEDGED operator, drew down LESS than 58%-hedged RCL on three of five closes with Brent above $103"* — became **one** of five, and the inference built on it (that a retired fuel thesis had gained fresh tape support) had to be withdrawn.

## Why nothing caught it

- **Same-basis feels like controlled-for.** The error is not a mismatch between the legs; it is a *match* applied to legs that differ in a dimension the basis does not represent. There is no inconsistency for a consistency check to find.
- **An arithmetic verification re-derived from the same inputs reproduces it perfectly.** An independent reviewer (CATO) re-computed all five values that day and they agreed to four decimals — correctly, and it scoped itself as *"verified arithmetic from owner inputs, not independent certification of price history."* **Agreement was guaranteed by construction.** Cf. [[finding_inherited_defect_propagates_though_both_ends_act_correctly]] and [[finding_crosscheck_with_free_parameter_validates_nothing]].
- **The ruling was specific and still silent on it.** WQ-222 fixed the threshold, the base and the window — three of four degrees of freedom — and never said *price or total return*. **A letter can be precise and incomplete, and the precision is what stops you looking for the gap.** Cf. [[finding_unnamed_instrument_makes_a_threshold_a_family]].
- **The bias was flattering.** It made the desk's own preferred reading (the retirement looks good) stronger, so nobody re-checked an agreeable number. Cf. [[finding_a_charitable_reading_of_your_work_is_the_one_to_check]].

## How to apply

1. **Before publishing any A-minus-B metric, name what the legs do NOT share** — dividend policy, buybacks, currency, index membership, listing venue, fiscal calendar, share-count changes, split history — **and ask whether the chosen basis is blind to it.** Blindness plus asymmetry equals one-sided bias. Same-basis is the precondition, not the answer.
2. **Dividend payer vs non-payer is the common case and it has a one-line check:** pull the dividend history for every leg over the window before you publish, not after someone asks. A single ex-date inside the window is enough to flip small spreads.
3. **When the letter is silent on the basis, grade on the letter, compute BOTH and check invariance.** If the verdict is the same under every reading, grade it and record the ambiguity; if the basis would decide it, that is NO-VERDICT. Do not quietly pick the one you prefer, and **do not re-specify a ruled instrument yourself** — route the gap to whoever owns the ruling.
4. **Separate what survives from what dies, explicitly.** Here the *verdict* was invariant (not tripped under either basis) while the *interpretation* reversed. Say both. **Withdraw the dead claim rather than annotating beside it** — cf. [[finding_correction_beside_an_instruction_leaves_two_live_instructions]].

Related: [[finding_distance_to_a_threshold_is_a_claim_about_its_basis]] · [[finding_spread_metric_blind_to_common_mode]] · [[finding_level_and_rate_look_like_agreement_until_you_name_which]] · [[finding_exact_level_authenticates_a_wrong_direction]] · [[finding_loadbearing_number_must_be_reproducible]]
