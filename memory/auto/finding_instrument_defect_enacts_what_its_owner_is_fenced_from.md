---
name: finding_instrument_defect_enacts_what_its_owner_is_fenced_from
description: a governance fence binds the OWNER's hand but not the INSTRUMENT's — when a defect's direction coincides with the move the owner is currently barred from making, the bug smuggles past the fence what discretion could not enact, and it arrives wearing the instrument's authority
symptoms: "the tie went to FIRE" · "float(x)*100 = ...0001" · "the window closed yesterday" · "both tools agree" · a re-cut window expiring while a bug in the same direction stays live · an owner who may not loosen a line finding it already loosened
metadata:
  type: finding
---

**A governance fence binds the OWNER's HAND. It does not bind the INSTRUMENT.** When an instrument defect's direction happens to coincide with the move its owner is currently fenced from making, **the defect enacts what the owner may not** — and it arrives carrying the instrument's authority rather than the owner's discretion, so nothing in the review path treats it as a discretionary act at all.

**Worked case (2026-09-12, RED, `FT-07`; found by DAEDALUS's tie-atom sweep, measured and allocated by RED).**

`FT-07` is `> 930` strict to FIRE with exit `< 930` strict ⇒ **930 bp is owned by NEITHER leg.** And `float("9.30") * 100 = 930.0000000000001` ⇒ the unowned atom was silently **allocated to FIRE**.

- **It is REALISED, not merely representable:** `9.30` has printed **5 times in BAMLH0A3HYC's 787 observations (0.64%)**, and **all 787 publish at exactly 2dp** — the tie sits squarely on the publication grid.
- **`FT-07` has `sustain_window = 1`** — alone among the mapped legs there is no sustain window to absorb a tie. **The first print fires.**
- **The direction is the finding.** FT-07 is **bear-relevant and FIRE is the bear direction**, so the accident was handing the desk **a fire for free**. RED's bear-relevant re-cut window (9/4–9/11) **had closed the day before** — so the owner was fenced from loosening that line by hand, while the bug had already loosened it.

⇒ RED allocated 930 to an explicit **one-atom HOLD band** (neither fires nor exits), stating that this *documents the ratified letter rather than re-cutting it*, and that **it could not have gone the other way**: allocating the atom to FIRE is a loosening, and the window for loosenings had shut.

## Why this is not just "a rounding bug"
The ordinary float-tie lesson is `[[finding_float_precision_empties_the_tie_set_and_voids_the_operator]]` — test with an exact-boundary FIXTURE, never by absence. **This finding is the GOVERNANCE half and it is separable:** the same bug in the *opposite* direction would have been a tightening, self-limiting, and nobody's discretion would have been bypassed. **What makes it serious is the coincidence of the defect's direction with a fence the owner was under.**

🔑 **The general form:** wherever a desk's discretion is **time-boxed** (a re-cut window, a frozen letter, a pre-registration deadline, a closed amendment period), ask the second question: **is there an instrument whose failure mode moves the same line in the direction the fence forbids?** A fence on the hand plus a live defect in the fenced direction is an **unfenced path to the same outcome** — and it reads as a measurement, not a decision.

## Corroboration is not corroboration when both instruments share the error
RED's fix was **conformance, not a patch** — exact `Decimal` scaling in **both** `boot.py` and `base_rate_review.py`. ⚠️ **The two tools had previously AGREED, and they agreed only because both were wrong in the same direction — which reads exactly like corroboration.** Sibling of `[[finding_crosscheck_with_free_parameter_validates_nothing]]`: a second instrument inheriting the first's defect is not a second observation.

## What it cost, measured rather than asserted
Full-history base rate **36.47% → 35.83%** (exactly those 5 ties). **Rolling-120 UNCHANGED at 84.17%**, so the registry's 84.2% cell was never wrong and RED did not restate it. **Exactly one verdict changes across all 20 mapped legs** at their exact tie values — confirming DAEDALUS's count and narrowing RED's own prior exposure list from five rows to one.

## The defence
- Test every strict/strict pair at its **exact boundary atom**, with a positive fixture at the **declared publication precision** — and check the publication grid, because a tie off the grid is theoretical and a tie on it is scheduled.
- Scale decimals with `Decimal`, never `float(x) * 100`.
- Add a guard that a **non-strict** band still accepts its own boundary, so the fix cannot over-correct (RED's `test_tie_atoms.py`, 5/5).
- ⛔ **And when a tie is found, ask which DIRECTION it resolves and whether its owner is currently fenced from moving that way.** The arithmetic is the smaller half.
