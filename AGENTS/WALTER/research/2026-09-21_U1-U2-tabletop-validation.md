# U1/U2 tabletop validation — CHECKLIST v0.48

**WALTER · 2026-09-21 · `walter-e3`** · commissioned by Will in-session; case set specified by CATO (`runs/2026-09-21_1338_walter-upstream-review.md`, "Smallest useful next step").

⛔ **WHAT THIS ESTABLISHES AND WHAT IT DOES NOT.** A tabletop replay can show the revised contract **handles these cases**. ⛔ **It CANNOT establish live reliability**, because every case here was selected and graded by the author of the change. **Two things are outstanding before any reliability claim:** ① **an unseen counterexample from a non-implementing reader**, ② **observation of a small fresh batch** using existing records. **Neither has happened.**

---

## The contract being tested

**U1 — verifier response** (`CHECKLIST:113–122`): four fields inside the existing word cap — **CLAIM CHECKED · EVIDENCE LOCATOR (or explicit absence/access limit) · SUPPORTING OBSERVATION · BOUNDED CONCLUSION.** A verdict missing fields 2 and 3 is **not a VERIFIED result** — it may not be cited as verification and no confidence may be claimed from it. ⛔ **It is NOT a bar on dispatch:** the signal may still travel **explicitly labelled unverified**, which is what `INDETERMINATE` already does. **Insufficient evidence blocks the CLAIM OF VERIFICATION, not the routing decision.** **Remedy for a missing field: ask the verifier, before relying on the verdict.**

**U2 — own-conclusion check** (finalization): split WALTER's own most consequential sentence into **OBSERVED · INFERRED · UNKNOWN**; a prediction is not an observation; keep the direction of a conditional; say the unknown or delete the part.

---

## Case 1 — INACCESSIBLE SOURCE

**Input:** claim rests on a named report behind a paywall; verifier cannot open it.

| | |
|---|---|
| **Old rules, stated accurately** | ⚠️ **AMBIGUOUS, not deterministically a kill.** The pre-v0.47 letter had **two** doors: `FALSE` (*"no primary source exists to support it"*) → KILL, **and** `INDETERMINATE` (*"verification inconclusive within time budget"*) → route at lowered confidence. **An inaccessible primary could land on either.** ⛔ **That OVERLAP is the defect CATO named — not that a kill was forced.** What was missing was any requirement to state the access limit, so the choice was invisible to a later reader. |
| **New contract** | Field 2 forces the **explicit access limit** (*"paywalled at publisher, not read"*). Field 3 has no observation, so the response **cannot be cited as verification** → verdict grades unverified. Verdict grades **INDETERMINATE (b) INACCESSIBLE** per v0.47. |
| **Verdict** | ✅ **PASS.** The claim ends **unresolved, not disproved.** Disposition stays a separate relevance/urgency call. |

## Case 2 — IRRELEVANT-BUT-REAL CITATION

**Input:** verifier returns *"CONFIRMED (0.85)"* citing a genuine, current, correctly-formatted source — **which addresses an adjacent claim, not this one.**

| | |
|---|---|
| **Old rules, stated accurately** | ⚠️ **NOT unguarded — the desk was not bare here.** Phase 1.5 carried source-language triggers, and the `CONFIRMED`-scope guard (v0.34) already said a CONFIRMED does not certify a **shape claim** built across figures. ⛔ **But none of those tests claim-to-evidence FIT for an ordinary non-shape claim**, and the `Validated — source cited` box is a **presence test** that the citation satisfies. ⇒ **this remained the case the old rules were least able to see.** |
| **New contract** | Field 1 pins **the exact claim checked**; field 3 demands the **passage that bears on it**. The returned passage is about the adjacent claim, so **field 1 and field 3 do not match** — visible on the face of the response. |
| **Verdict** | ✅ **PASS, and this is the case the change is really for.** ⚠️ **HONEST LIMIT: detection depends on a reader noticing fields 1 and 3 disagree. The contract MAKES THE MISMATCH VISIBLE; it does not force anyone to look.** The `Validated` box is now annotated to say it cannot see this, and the own-conclusion check is the second net. |

## Case 3 — MIXED TRUE/FALSE CLAIM

**Input:** *"Multifamily CMBS delinquency hit 7.69% in August, the biggest jump of any property type."* Level supported; superlative not checked.

| | |
|---|---|
| **Old rules, stated accurately** | ⛔ **CORRECTION TO AN EARLIER VERSION OF THIS ROW: it claimed the old letter forced FALSE-or-CONFIRMED. That was WRONG — `CORRECTED-framing` existed precisely for a summary that "overstated or misframed", and the `CONFIRMED`-scope guard already warned that verified figures do not certify a derived shape claim.** ⇒ **the old rules had a home for this case.** What they lacked is the requirement to state **the claim AS CHECKED**, so the level and the superlative were never separated into two claims. ⚠️ **`SIG-W-20260921-005` shipped the merged version anyway and needed `-015` — evidence that the available guard was not EXECUTED, not that it was absent.** |
| **New contract** | Field 1 forces the claim to be stated **as checked** — so the level and the superlative are **two claims**. Field 4 bounds the conclusion to what was checked. U2 then splits the headline: **OBSERVED** = the August level; **UNKNOWN** = the cross-property ranking. |
| **Verdict** | ✅ **PASS.** The supported part survives with its support; the unverified ranking cannot travel in the title or justify a downstream finding. ⚠️ **Note this is a retrospective replay of a defect already corrected — it demonstrates the contract's behaviour, not that it would have fired in the live session.** |

## Case 4 — CONDITIONAL PREDICTION WITH NO OBSERVED OUTCOME

**Input:** the record says *"a real export ban would move Brent ~−$5/bbl in minutes."* The writer wants to conclude the ban is false.

| | |
|---|---|
| **Old rules, stated accurately** | ⛔ **CORRECTION TO AN EARLIER VERSION OF THIS ROW: it said "nothing checks the writer's own inference." That was WRONG.** `OPERATOR_BRIEF_SPEC` already required caveats to survive a summary **including the direction of a conditional**, and the `CONFIRMED`-scope guard already addressed over-reading evidence. ⇒ **the gap was COVERAGE AND EXECUTION at the final inference, not the absence of a rule.** ⚠️ **WALTER wrote "and hadn't" — asserting an observation the record does not contain — with those rules already in force.** Withdrawn only after CATO caught it. |
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

⚠️ **AND THE OLD-RULE COLUMNS WERE CORRECTED 2026-09-21 AFTER CATO OBJECTED.** The first version of this document **overstated how unguarded the old rules were** in cases 2, 3 and 4 — claiming `FALSE`-or-`CONFIRMED` was forced when `CORRECTED-framing` existed, and that *"nothing checks the writer's own inference"* when `OPERATOR_BRIEF_SPEC` already required conditional direction to survive. ⛔ **Overstating the old defect inflates the apparent value of the change, and it ran in the same direction as the day's other errors.** **The corrected reading is narrower and less flattering: in several of these cases a guard EXISTED and was not EXECUTED, which is a different problem from an absent rule — and one that new wording is less likely to fix.**

**What is NOT established:**
- **Live reliability.** Every case was chosen and graded by the change's author. `[[finding_adoption_is_not_validation]]`
- **That the checks will be RUN.** Case 4 is the live proof that the author of a rule can violate it minutes later. **A contract is not a control until something makes it fire.**
- **That no new overlap was introduced.** The v0.47 `UNSUPPORTED`/`INCONCLUSIVE` boundary is under separate independent read and is untouched here.
- **Any cost claim.** ⚠️ **Byte counts are NOT runtime measurements** and none is asserted.

**Owed before any reliability claim:**
1. 🔴 **One unseen counterexample from a non-implementing reader.** CATO or HAWK qualify. **Not optional — case 4 is why.**
2. 🔴 **Observation of a small fresh batch** through existing records.
3. ⚠️ **HAWK's v0.47 acceptance must cover the RESULTING version if the verdict-table wording moves.** The exact reviewed revision is pinned at `8d2c9b8ef` in `design/history/CHECKLIST_VERSION_HISTORY.md`. **v0.48 did NOT alter the verdict-table rows** — it changed `:116` and the finalization block — **but HAWK is being told so it can confirm rather than assume.**


---

# PART 2 — FRESH-BATCH OBSERVATION (2026-09-21, live, unselected)

⛔ **THIS IS THE HALF THE TABLETOP CANNOT PROVIDE: material WALTER did not choose.** Source: `RESEARCH-INTAKE data/2026-09-20/news.json`, the batch deferred from this morning's boot. **103 NEW-classified items.**

## What the batch actually contained

| Finding | Measure |
|---|---|
| **Syndication inflation, measured** | **The Moscow refinery strike of 19–20 Sep appears under TEN separate outlets** (Reuters · CNN · Kyiv Post · Al Jazeera · BBC ×2 · NBC · PBS · The Media Line · FT). **Ten items, ONE event.** |
| **That event is ALREADY OWNED** | OSPREY logged it as `RU-20260920-MOSCOW-REFINERY` before this morning's boot; WALTER killed it on **Novelty (already-ours)** at ~15:0xZ and `SIG-W-20260921-002` / `-019` already carry it. ⇒ **10 items → 1 pre-existing kill, no dispatch.** |
| **Riyadh claim** | Items *"Houthis say they targeted Saudi capital"* + *"Flames and smoke at Riyadh's King Khalid airport"* — **already dispatched this morning as `SIG-W-20260921-009`.** Already-ours. |

✅ **This independently reproduces MEMORY finding #4 — *the lane counts OUTLETS, not SOURCES; syndication inflation is structural, not occasional*. Measured ratio on today's top story: 10:1.**

## 🔴 A LANE FINDING THE CONTRACT DID NOT CAUSE AND DOES NOT FIX

**Every FT and BBC item in this batch carries `agents=[]` — the lane assigns them NO recipient at all.** Two of them are among the most routable things in the file:

- **`"Big Tech uses guarantees to keep $300bn AI exposure off balance sheets"` (FT, 2026-09-20)** — squarely VULCAN + BROCK: off-balance-sheet AI-infrastructure exposure is the financing leg of the AI-capex thesis, and WALTER already dispatched a related item on 2026-06-27 (`SIG-W-20260627-033`).
- **`"Wall Street expects US to issue about $1tn of short-term debt as borrowing costs climb"` (FT, 2026-09-20)** — squarely BOND.

⇒ **The highest-value items in the batch are UNROUTED BY CONSTRUCTION, because the tagging is keyed to labelled feeds and the FT/BBC pulls carry no agent tags.** ⛔ **This is a lane defect, NOT a v0.48 defect, and v0.48 does nothing about it.** **Recorded here because a fresh-batch observation that only confirmed the change under test would be the weaker result.** Raised separately; not folded into this validation.

## What this observation does and does not establish about v0.48

⛔ **HONEST SCOPE — and it is narrower than "we tested it live."**
- **The batch exercised GATE 1 (Novelty), not the new contract.** Ten of the top items resolved on already-ours, which the pre-existing filter handled before v0.48 existed. **v0.48 changed nothing about that path and is not credited for it.**
- **U1 is exercised only where a verify-research spawn actually fires.** One item in this batch triggered Phase 1.5 (`"Morgan Stanley caps private credit fund withdrawals again as 11% seek exits"`, Investing.com 2026-09-19 — a secondhand outlet citing a primary, carrying a specific figure). **That spawn was run under the new four-field contract; result recorded below.**
- **U2 is a drafting check on WALTER's own sentence and cannot be observed from the batch at all** — only from what WALTER then writes.

⇒ **A fresh batch tests the FILTER far more than it tests this change.** ⛔ **It does NOT establish that v0.48 improves live outcomes**; it establishes that v0.48 did not disrupt an ordinary batch, and it surfaced one lane defect that has nothing to do with it.
