# U1/U2 tabletop validation — CHECKLIST v0.48

**WALTER · 2026-09-21 · `walter-e3`** · commissioned by Will in-session; case set specified by CATO (`runs/2026-09-21_1338_walter-upstream-review.md`, "Smallest useful next step").

⛔ **WHAT THIS ESTABLISHES AND WHAT IT DOES NOT.** A tabletop replay can show the revised contract **handles these cases**. ⛔ **It CANNOT establish live reliability**, because every case here was selected and graded by the author of the change. **Two things are outstanding before any reliability claim:** ① **an unseen counterexample from a non-implementing reader**, ② **observation of a small fresh batch** using existing records. **Neither has happened.**

---

## The contract being tested

**U1 — verifier response** (`CHECKLIST:113–122`): four fields inside the existing word cap — **CLAIM CHECKED · EVIDENCE LOCATOR (or explicit absence/access limit) · SUPPORTING OBSERVATION · BOUNDED CONCLUSION.** A verdict missing fields 2 and 3 is not a verification result and is not routable. **Remedy for a missing field: ask the verifier, before relying on the verdict.**

**U2 — own-conclusion check** (finalization): split WALTER's own most consequential sentence into **OBSERVED · INFERRED · UNKNOWN**; a prediction is not an observation; keep the direction of a conditional; say the unknown or delete the part.

---

## Case 1 — INACCESSIBLE SOURCE

**Input:** claim rests on a named report behind a paywall; verifier cannot open it.

| | |
|---|---|
| **Old contract** | Verdict line only. *"FALSE — no primary source obtainable."* Routes to **KILL** as `framing-false` under the pre-v0.47 letter. |
| **New contract** | Field 2 forces the **explicit access limit** (*"paywalled at publisher, not read"*). Field 3 has no observation, so **fields 2+3 fail the routable test** → verdict is not accepted as a verification result. Verdict grades **INDETERMINATE (b) INACCESSIBLE** per v0.47. |
| **Verdict** | ✅ **PASS.** The claim ends **unresolved, not disproved.** Disposition stays a separate relevance/urgency call. |

## Case 2 — IRRELEVANT-BUT-REAL CITATION

**Input:** verifier returns *"CONFIRMED (0.85)"* citing a genuine, current, correctly-formatted source — **which addresses an adjacent claim, not this one.**

| | |
|---|---|
| **Old contract** | Passes. The `Validated — source cited` box is a **presence test** and the citation is present. ⚠️ **This is the case the old contract was least able to see.** |
| **New contract** | Field 1 pins **the exact claim checked**; field 3 demands the **passage that bears on it**. The returned passage is about the adjacent claim, so **field 1 and field 3 do not match** — visible on the face of the response. |
| **Verdict** | ✅ **PASS, and this is the case the change is really for.** ⚠️ **HONEST LIMIT: detection depends on a reader noticing fields 1 and 3 disagree. The contract MAKES THE MISMATCH VISIBLE; it does not force anyone to look.** The `Validated` box is now annotated to say it cannot see this, and the own-conclusion check is the second net. |

## Case 3 — MIXED TRUE/FALSE CLAIM

**Input:** *"Multifamily CMBS delinquency hit 7.69% in August, the biggest jump of any property type."* Level supported; superlative not checked.

| | |
|---|---|
| **Old contract** | One verdict for the whole sentence. Either FALSE (killing a true figure) or CONFIRMED (certifying an unverified ranking). ⚠️ **This is `SIG-W-20260921-005`, which shipped and needed correction by `-015`.** |
| **New contract** | Field 1 forces the claim to be stated **as checked** — so the level and the superlative are **two claims**. Field 4 bounds the conclusion to what was checked. U2 then splits the headline: **OBSERVED** = the August level; **UNKNOWN** = the cross-property ranking. |
| **Verdict** | ✅ **PASS.** The supported part survives with its support; the unverified ranking cannot travel in the title or justify a downstream finding. ⚠️ **Note this is a retrospective replay of a defect already corrected — it demonstrates the contract's behaviour, not that it would have fired in the live session.** |

## Case 4 — CONDITIONAL PREDICTION WITH NO OBSERVED OUTCOME

**Input:** the record says *"a real export ban would move Brent ~−$5/bbl in minutes."* The writer wants to conclude the ban is false.

| | |
|---|---|
| **Old contract** | Nothing checks the writer's own inference. ⚠️ **THIS IS WALTER'S ACTUAL ERROR OF 2026-09-21 — it wrote "and hadn't," asserting an observation the record does not contain.** Withdrawn only after CATO caught it. |
| **New contract** | U2 splits it: **OBSERVED** = the record predicts a move · **UNKNOWN** = whether the move occurred, because **no dated price observation exists in the record**. The rule *"a prediction is not an observation"* names this case literally. |
| **Verdict** | ✅ **PASS on the tabletop.** ⛔ **BUT THE STRONGEST CAVEAT IN THIS DOCUMENT ATTACHES HERE: the check would have had to be RUN. WALTER wrote that sentence while actively reasoning about evidentiary standards, and no contract self-executes.** **This case is the reason an unseen counterexample from a non-implementing reader is required and is NOT optional.** |

## Case 5 — PROPERLY SUPPORTED CLAIM (the must-not-break case)

**Input:** *"Trepp August multifamily CMBS DQ is 7.69%, flat MoM"*, secondary carrying the figure with a date.

| | |
|---|---|
| **New contract** | Field 1 = the level claim. Field 2 = Multifamily Dive, 2026-09-16, URL. Field 3 = the passage carrying 7.69% flat MoM. Field 4 = *reported at 7.69% on a dated secondary, not a Trepp primary.* U2: **OBSERVED** = the reported figure · **INFERRED** = nothing · **UNKNOWN** = comparability with other series. |
| **Verdict** | ✅ **PASS — and it must pass without gaining certainty.** ⚠️ **The success condition is that the supported claim survives WITHOUT being strengthened.** The bounded conclusion still says *reported on a secondary*, not *Trepp says*. ⛔ **No added friction, no extra approval, no longer output.** |

---

## Result

**5 of 5 handled on the tabletop.** ⛔ **This is a design-behaviour result, not an operational one.**

**What is NOT established:**
- **Live reliability.** Every case was chosen and graded by the change's author. `[[finding_adoption_is_not_validation]]`
- **That the checks will be RUN.** Case 4 is the live proof that the author of a rule can violate it minutes later. **A contract is not a control until something makes it fire.**
- **That no new overlap was introduced.** The v0.47 `UNSUPPORTED`/`INCONCLUSIVE` boundary is under separate independent read and is untouched here.
- **Any cost claim.** ⚠️ **Byte counts are NOT runtime measurements** and none is asserted.

**Owed before any reliability claim:**
1. 🔴 **One unseen counterexample from a non-implementing reader.** CATO or HAWK qualify. **Not optional — case 4 is why.**
2. 🔴 **Observation of a small fresh batch** through existing records.
3. ⚠️ **HAWK's v0.47 acceptance must cover the RESULTING version if the verdict-table wording moves.** The exact reviewed revision is pinned at `8d2c9b8ef` in `design/history/CHECKLIST_VERSION_HISTORY.md`. **v0.48 did NOT alter the verdict-table rows** — it changed `:116` and the finalization block — **but HAWK is being told so it can confirm rather than assume.**
