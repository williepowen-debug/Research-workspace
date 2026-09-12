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

---

**n=2 — 2026-09-12 (BROCK, `DGS10` → convergence matrix). SAME DAY, DIFFERENT DESK, DIFFERENT INSTRUMENT TYPE — and it generalises the finding: the FENCE is optional, the DIRECTION is the invariant.**

BROCK's convergence matrix had a **"next level" cell that restated the CURRENT level's condition** as the route to the next one. `>4.75 sustained 5+` **is** the Orange band — the level the vector was already sitting at — so the cell named an already-satisfied condition as the trigger for an upgrade. **Orange was met and the matrix read as though Red were in reach.** Red is `>5.00%`; the window high was **4.95**, not through it. Convergence correctly **HELD at 57/70** once the cell was fixed (KB-BRK-288, LESSONS #36).

🔑 **BROCK's own statement of it, which is the general form:** *"a 'next level' cell restating the current level's condition manufactures an upgrade candidate out of nothing — **and it can only fire in the direction of whoever wrote the row.**"*

⚠️ **What n=2 changes about n=1.** n=1 (RED FT-07) had a governance fence — a closed re-cut window — and the defect walked past it. **n=2 has NO fence at all**, and is just as dangerous, because the defect *manufactures* the candidate rather than smuggling one past a barrier. ⇒ **The invariant is not "a fence was bypassed." It is that A DEFECT'S DIRECTION IS NOT RANDOM — it correlates with its author's interest**, because the author wrote the cell, chose the operator, picked the scaling, and set the band. **Ask of any instrument defect: which way does it fire, and who benefits?** A defect that fires against its author is self-limiting and gets found fast; one that fires *for* its author is quiet and gets banked.

✅ **Both instances were caught by the author and reported against interest** — RED allocated the tie to a HOLD band it could not have allocated to FIRE, and BROCK **declined the upgrade its own defect offered**. That is the control working, and it is a control made of judgement, not of code. **Neither desk's own tests would have caught it.**

🔑 **A THIRD leg in the same sitting, from the same desk, worth carrying with these:** LIQUID returned BROCK's routed `DGS10` count and **deliberately REFUSED to pick strict-vs-inclusive**, because 2026-08-31 printed **4.75 exactly** — the boundary atom again. BROCK's registered bar is strict ⇒ **7 consecutive closes, not 8**. BROCK's note: *"**8 is the reading that favours my book, and LIQUID was right not to hand it to me pre-made.**"* ⇒ **When a counterparty's answer has a free parameter that happens to favour the asker, the counterparty should return the parameter UNRESOLVED, not choose.** Choosing for the asker launders a discretionary call into a delivered measurement.


---

**n=3 — 2026-09-12 (RED, `FT-06`, same sitting). THE DETECTION HEURISTIC, which n=1 and n=2 lacked.**

`FT-06`'s fire leg is **anti-bear** and its exit leg **pro-bear**, and the measured asymmetry made the exit **~4× easier than the fire** — i.e. the looseness ran in **this desk's own direction**. RED **kept it, disclosed it, and declined to re-cut post-fire.**

🔑 **RED's tell, and it is the operational form of this whole finding:**
> **"The tell that you're about to re-tune a leg is that the fix happens to help you."**

⚠️ **Why it is hard rather than obvious: re-cutting would have SOUNDED like rigour.** *"27% is too loose for an exit"* is a genuinely good argument — and acting on it would have removed a **pro-bear trigger that a bear desk has every incentive to keep loose.** A tightening argument and a self-serving one are the same sentence here; only the direction distinguishes them.

⇒ **The three instances together:** n=1 a defect walked past a fence · n=2 a defect manufactured a candidate with no fence present · n=3 a *correct-sounding fix* would have done the same thing as either. **All three fire toward their author. The invariant holds across defect, absence-of-defect, and proposed-repair.** ⛔ **So the check applies to REPAIRS too, not just to bugs: before re-cutting any leg, ask which way the re-cut moves your own book.**

⚠️ **EVIDENTIAL LIMIT ON n=3, stated by RED and recorded because it weakens the case FOR RED.** RED declined to have *"argued against its own book twice"* counted as virtue: **both findings were CHEAP.** FT-10's exit **has never fired**; the FT-06 inversion **moved no weight**; **neither touched a live grade.** In its words — *"PAT-160's real test is a direction-check that **costs** the desk something, and nothing today asked that of me."*

⛔ **So the heuristic is validated only on cheap instances, and RED's own warning is the one to carry: a rule validated only on cheap instances WILL GET CITED ON EXPENSIVE ONES.** The three cases establish that the direction-check **finds** author-aligned defects; **none of them establishes that a desk will apply it when applying it costs a live position.** Treat n=1–3 as evidence about the *detector*, not yet about the *discipline*. **The first expensive instance is the real n=1.**

