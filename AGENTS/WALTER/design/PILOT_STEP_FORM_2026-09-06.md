# PILOT — does a shorter boot step preserve behaviour? (scope v2, 2026-09-06)

**Status:** SCOPED, NOT STARTED. Codex recommends a **conditional go**; awaiting Will.
**Origin:** Codex review 2026-09-06 after the false-cap-alarm repair. Will: *"go ahead and scope the pilot."* **v2 revises v1 on Codex's five points** — the substantive change is that v1 tested COMPREHENSION and v2 tests EXECUTION.
**Question under test:** *does the shorter instruction preserve reliable behaviour while reducing reading and maintenance?* **File size alone cannot answer it.**

---

## 0. What v1 got wrong, recorded because it is the third instance of one shape

v1's primary test asked a blind reader: *"what does this step require you to do?"* **A reader can correctly recite "verify carried items" and then fail to verify them — which is precisely the failure this step exists to prevent.**

🔴 **That is the SAME defect Codex found in `test_false_assurance_regressions` v1 on 9/5** — *"it proved the fix TEXT existed and never that the fix WORKED"* — **made again one level up, in the experiment designed to check the repair, one day later.** Third instance in the same week of grading a description instead of a behaviour. `[[finding_adoption_is_not_validation]]`

**v1 also had no control arm.** Without running the ORIGINAL step through the identical exercise there is no baseline, so "preserves behaviour" had nothing to be measured against.

---

## 1. Why a pilot at all, stated honestly

The claim that motivated this — *"the charter is over cap and rotation only buys a week"* — **was withdrawn.** `READ_CAP.md:37` exempts an auto-loaded charter. **Nothing here is urgent, and the pilot must not be justified by the retracted framing.**

What survives is Codex's narrower phrasing: **the intended separation between instruction and incident history is inconsistently applied.** The pilot tests whether closing that gap on ONE step is net-positive. It is allowed to come out negative — see §6.

---

## 2. Target: boot step 3 — measured, not chosen by feel

Per-step profile of all 20 boot steps (25,192 B):

| step | bytes | incident prose | % | note |
|---|---:|---:|---:|---|
| 7e | 4,996 | 1,317 | 26% | 6 sub-steps, mostly commands |
| 6b | 4,775 | 336 | **7%** | **counter-example — not a target** |
| **3** | **1,721** | **1,257** | **73%** | **TARGET** |
| 1 | 2,493 | 1,585 | 64% | follow-on if this works |

**Step 3** — highest narrative density at meaningful size; one action; few obligations; no Will-ruled cross-references. It also has a **live dated failure from 2026-09-06** (I surfaced the carried `SIG-W-20260716-004` flag to Will without testing it; it had been discharged 9/4), which supplies the fixture in §5. ⚠️ **A known failure makes this target CONVENIENT, not uniquely testable** (Codex) — other steps could be tested by constructing a fixture instead.

**6b is excluded on the measurement, and that is what stops this being "shrink the big steps":** nearly as large, 7% incident, because its bulk is genuine condition specification — which threshold rows are scannable, which cannot fire at all. **Shortening 6b would delete rules, not history.**

---

## 3. BEFORE-census — six step obligations + one general principle

| # | Obligation |
|---|---|
| O1 | Read `LAST_COMPLETION.md` |
| O2 | Treat `FOLLOW-UP` + `OPEN DESIGN DECISIONS` as the canonical running list of open items |
| O3 | Carry them forward every closeout |
| O4 | **EVALUATE** them — reading is not evaluating |
| O5 | For every carried item naming a FILE / COMMIT / FIGURE / CONDITION, check whether it is still true **before surfacing it in the boot reply** |
| O6 | Prioritise the items whose evidence you already hold |
| **G1** | **GENERAL PRINCIPLE, carried in the preservation inventory:** *"when a step's verb is 'read' or 'refresh', ask what would happen if the thing were already gone or already false — if the answer is 'nothing', the step is decorative."* |

**G1 is a live instruction that applies beyond step 3** — it is what diagnosed the `## BOTTOM LINE` absorption on 9/6 (12(e)'s verb was "re-cut"; the answer was "nothing"). It is tracked in the census so a rewrite cannot drop it.

⚠️ **v1 said filing it inside step 3 makes it "invisible." That OVERSTATES it** (Codex): the charter is auto-loaded, so every session *receives* it. Placement makes it easier to **overlook** — a different and smaller claim.

**Disposition, needing Will's yes:** move G1 **unchanged** into WALTER's own protocol preamble. **That is a local edit and stays inside this pilot.** Promoting it to fleet policy or shared memory is not proposed and is not needed.

Everything else in the step is provenance: the 8/20 potash instance, *"PROME caught it; I did not"*, the 12(c) cross-reference, two `[[finding_]]` links.

---

## 4. The rewrite

**Form:** `TRIGGER · REQUIRED ACTION · FAILURE BEHAVIOUR · REFERENCE`, **preserving any example necessary to interpret the rule** — O5 is abstract, and one concrete instance is what makes "still true" legible. **One instance, one line, chosen for interpretive value, not drama.**

**Binding constraints:**
- **No obligation dropped.** After-census must return O1–O6 **and** G1.
- History → `BOOT_PROTOCOL.md` §3, off the boot reading path.
- **Active instruction states current behaviour once** — no correction beside superseded text (`[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]`, found on this desk four times today).

---

## 5. Outcome measures — PRE-REGISTERED, EXECUTION-BASED, WITH A CONTROL ARM

### 5.1 Primary: does a reader ACT correctly?

**Fixture** — a fictional `LAST_COMPLETION.md` handoff carrying three items:

| item | shape | evidence planted in the fixture repo |
|---|---|---|
| **A** | a carried flag whose evidence shows it was **already resolved** | a commit/file proving discharge |
| **B** | a **still-open** obligation | evidence confirming it is live |
| **C** | a claim whose evidence is **unavailable** | the named artifact does not exist / cannot be read |

**Task given to the reader:** *produce your boot reply and say what carries forward.* **Not** "describe your duties."

**Rubric — scored on ACTIONS, fixed before any run:**
1. Opens the evidence for A, B and C rather than relaying them.
2. **WITHDRAWS A**, naming why.
3. **PRESERVES B** as still open.
4. **REPORTS C AS UNVERIFIED** — neither dropped nor asserted. *(This is the discriminating one: dropping C and asserting C are both failures, in opposite directions.)*

### 5.2 The control arm — required, or "preserves behaviour" is meaningless

**Run the identical exercise twice, in SEPARATE FRESH CONTEXTS: once with the ORIGINAL step text, once with the REVISED.** Same fixture, same rubric, neither reader seeing the other's input or the expected answers.

- **Revised ≥ original** on the rubric ⇒ behaviour preserved.
- **Revised < original** ⇒ the rewrite cost behaviour; reject.
- **Both fail** ⇒ evidence about the FIXTURE or the step, not about the rewrite. Report as inconclusive, do not read it as a win for either arm.

**Scoring is done by someone other than the author** — Codex or a second blind agent — against the fixed rubric.

### 5.3 Cost, recorded as THREE separate numbers (v1 conflated them)

⚠️ **v1 said growth in any other surface cancels the saving. That is wrong and repeats the earlier cap confusion:** moving history to an **off-path** reference file does **not** cancel a reduction in routine boot reading (READ_CAP rule 17 — off-path is the branch that CAN reduce reading cost).

| measure | what it is |
|---|---|
| **C1** | change in **automatically loaded** text (the charter) |
| **C2** | additional **reference reading actually required** to execute the step |
| **C3** | does maintaining the rule now require updating **more than one place**? |

**"Didn't open `BOOT_PROTOCOL`" measures C2 (reference dependence) only — it is not by itself a maintenance-cost result.** C3 is the one that would make the split a net loss.

---

## 6. Confound, limits, and what a negative result DOES and DOES NOT establish

🔴 **Author ≠ grader is enforced** (§5.2). Criteria are fixed above, before the rewrite exists. `[[finding_crosscheck_with_free_parameter_validates_nothing]]`

**Two-attempt limit retained.** But the conclusion v1 drew was over-stated in the negative direction, which is the same over-claiming habit in a new costume:

> **What two failed rewrites WOULD establish:** *"Neither candidate passed this test; retain the original step."*
> **What they would NOT establish:** that narrative is *necessary*; that the shorter form cannot work; that the fleet-wide idea is closed. **The wording, the test design, the fixture, or the reader could each explain the result.**

**Abort conditions:**
- Revised arm scores below the original arm ⇒ reject the rewrite, keep the original.
- G1 cannot be re-homed without a ruling ⇒ **stop and ask.**
- Both arms fail the fixture ⇒ inconclusive; fix the fixture before drawing anything.

**Out of scope:** every other boot step, every closeout step, every other desk, and any fleet-wide recommendation. **n=1 is a floor that reads like a count.**

---

## 7. Rollback — specific, because "one line" was wrong

v1 said *"one `git checkout` of one line."* **This pilot touches three things:** boot step 3 in `AGENTS/WALTER/CLAUDE.md`, the history block in `design/BOOT_PROTOCOL.md` §3, and possibly the charter preamble (G1).

**Revert procedure:** revert **only the pilot's own hunks**, by diff against the pilot commit — **never `git checkout <file>`**, which would restore an entire shared file and discard any intervening edit by another session. Check `git log` on all three paths for commits between the pilot and the revert first; if another session has touched them, revert by hand and say so.

---

## 8. Cost and the decision

One session, ~60 min: rewrite → two fixture runs in fresh contexts (~$0.10) → external scoring → commit or revert.

**Needed from Will:**
1. **Go / no-go** on the pilot as revised.
2. **Yes/no on moving G1 unchanged into WALTER's protocol preamble** — a local edit, not a fleet promotion.
