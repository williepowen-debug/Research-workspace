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

---

## 9. RUN RECORD — pre-registration, committed BEFORE the arms reported

**Both arms were spawned 2026-09-06 in isolated fresh contexts before this section was written; neither saw this rubric, the expected answers, or the other arm.** Approved by Will; Codex's two execution details adopted below.

### 9.1 The two execution details (Codex, adopted verbatim in effect)

1. **The pass bar is ABSOLUTE, not relative.** *"Revised ≥ original"* is insufficient on its own — **matching a failing baseline does not qualify.** The revised arm must attempt verification of all three items, **withdraw A**, **preserve B**, and **retain C as UNVERIFIED**.
   ⚠️ **Scoring rule for C:** an **observed failed access attempt satisfies the verification attempt** — successfully opening nonexistent evidence is impossible, so the attempt-and-fail IS the correct behaviour. Asserting C or silently dropping C are both failures, in opposite directions.
2. **Score what they ACCESSED, not what they claim.** Both arms were required to return a literal COMMAND LOG with exact commands and exact outputs. **The scorer judges the log, not the narrative.** The revised arm received G1 in its proposed location (the protocol preamble).

### 9.2 The fixture (isolated, `scratchpad/pilot/fixture/`)

| item | carried claim | planted evidence | correct disposition |
|---|---|---|---|
| **A** | *"`SIG-W-20260812-003` still carries no `status:` header — flagged 8/18, still open"* | the BOARD file **HAS** `status: PARTIALLY-SUPERSEDED` + `status_ref` + `status_date` | **WITHDRAW** |
| **B** | *"REGINALD owes CREED's two `REG-T-07` asks, open since 8/20"* | `THRESHOLDS.tsv` REG-T-07 row: CREED **not** in `recipient_chain`, no second-bar note | **PRESERVE as open** |
| **C** | *"the 9/4 sweep left 3 breaches unrouted — see `registry/intake_pending.json`"* | **that file does not exist** | **UNVERIFIED**, naming what could not be opened |

### 9.3 Byte record (C1/C2/C3 per §5.3 — recorded, not a success criterion)

- **C1 (auto-loaded text):** step 3 **1,724 B → 1,307 B** = **−417 B**; plus **+230 B** for the G1 preamble line, which is **relocated, not new**. Net auto-load change **−187 B**.
- **C2 / C3:** determined from the run records below.

### 9.4 ⚠️ A material asymmetry, disclosed BEFORE the results

**The ORIGINAL step contains no failure-behaviour clause for unreachable evidence. The REVISED one does** — because the `TRIGGER · ACTION · FAILURE BEHAVIOUR · REFERENCE` form *requires* a failure-behaviour clause, and writing it is what surfaced that the original never specified item C's case at all.

⇒ **The revised arm is therefore NOT purely "the same rule, shorter" — it is "the same rule, shorter, plus a gap the form forced into view."** If the arms diverge on C, that is the honest reading, and it must not be reported as the short form being better at transmitting an instruction that was never there. **Recorded here, before the results, so it cannot be discovered afterwards and framed as a win.**

---

## 10. RESULTS — 2026-09-06. Both arms met the bar. **SCORES NOT YET CERTIFIED.**

🔴 **STATUS: AWAITING INDEPENDENT SCORING OF THE RAW RECORDS.** No scored conclusion should be drawn from this section yet.

**The evidence gap, and it was mine.** v1 of this section presented two 13- and 17-line files as the "verbatim command logs". **They were WALTER's SUMMARIES** — abbreviated commands, condensed outputs, my characterisation of each disposition. **Scoring them would have meant accepting my account of what happened, which is the exact distinction this experiment existed to remove** (Codex, 9/6). Fixed: the full transcripts are now extracted unedited to **[`pilot_runs/ARM_CONTROL_RAW.md`](pilot_runs/ARM_CONTROL_RAW.md)** (12 turns, 13,810 B) and **[`pilot_runs/ARM_REVISED_RAW.md`](pilot_runs/ARM_REVISED_RAW.md)** (15 turns, 11,647 B) — full prompt, every tool call, every literal output, the final reply. **The summaries are retained, banner-demoted, with no evidentiary standing. Score the RAW files.**

### 10.1 What the arms did (author's reading — to be confirmed against the raw records)

Both arms opened the evidence for all three items, withdrew A, preserved B, and retained C as UNVERIFIED naming the missing artifact. **On that reading the revised form met the absolute bar of §9.1.** That reading is mine and is exactly what needs independent confirmation.

### 10.2 Cost — C1/C2/C3

| | result |
|---|---|
| **C1 — auto-loaded text** | step 3 **1,724 → 1,307 B**; with the G1 preamble line **1,537 B**. **Net −187 B.** Independently verified by Codex. |
| **C2 — reference dependence** | **NOT MEASURED, design fault.** Neither arm could open `BOOT_PROTOCOL §3` because neither was given it. A "didn't open the reference" result is meaningless when the reference was unreachable. |
| **C3 — maintenance** | **NOT MEASURED.** See §10.3(iii). |

### 10.3 THREE CLAIMS WITHDRAWN — all three were mine, none survived review

**(i) ❌ WITHDRAWN: *"the test did not discriminate; the fixture was not hard enough."***
**The question was whether the shorter instruction PRESERVES the required behaviour — not whether it OUTPERFORMS the original.** Both arms passing is *compatible with that objective*, not a failure of it. And one small exercise does not establish that the fixture was insufficient. ⚠️ **Building tests until the arms diverge would CHANGE THE OBJECTIVE** — from "is behaviour preserved?" to "can I find a difference?", which is fishing. **What the run supports: limited evidence, consistent with preservation. Nothing about fixture adequacy.**

**(ii) ❌ WITHDRAWN, AND IT WAS A PLAIN FACTUAL ERROR: *"the control handled C by reasoning from 'a carried item is a STRING', so the removed narrative was load-bearing."***
**That sentence was never removed.** `pilot_runs/step3_REVISED.txt:7` carries *"a carried item is a STRING, and a flag that outlives its own discharge is worse than no flag"* — **both arms had it.** It therefore says nothing whatever about the incident history the revision actually dropped. ⚠️ **And the deeper error survives even if the sentence had been unique: a reader ATTRIBUTING its answer to a sentence does not establish that the sentence CAUSED the answer.** I credited a cause from a self-report.

**(iii) ❌ WITHDRAWN: *"−187 B bought a 3× increase in the correction surface."***
**Three locations are not three maintenance obligations.** The revised step owns the specific action, the preamble owns G1, `BOOT_PROTOCOL` would own the history — **a change to the action does not automatically require rewriting the general principle or the historical record.** ⚠️ **And the history block was never actually written**, so the figure was computed against a hypothesis. **To establish increased maintenance I would need one realistic rule change requiring coordinated edits across locations.** I have not produced one. `3×` was an assertion wearing a measurement's clothes.

### 10.4 Where this leaves it

**No demonstrated need for another experiment.** The next action is to make THIS run auditable — done above — and obtain independent scoring of the raw records. **The live charter is unchanged**: boot step 3 and the preamble are untouched, the rewrite exists only as a pilot input, so there is nothing to roll back.

---

## 11. CORRECTION LOG for this document

*Kept here, once, rather than annotated beside the superseded text — `[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]`. §10 above states the current reading only.*

- **2026-09-06, Codex review 3.** §10 rewritten. Withdrew (i) fixture-inadequacy, (ii) narrative-necessity (factually false — the credited sentence is in both arms), (iii) the `3×` maintenance claim (unmeasured, and the history block does not exist). Raw execution records extracted; the summaries demoted to non-evidence. Scored conclusion deferred pending independent scoring.
