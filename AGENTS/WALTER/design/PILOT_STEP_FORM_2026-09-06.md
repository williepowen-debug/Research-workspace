# PILOT — does a shorter boot step preserve behaviour? (scope, 2026-09-06)

**Status:** SCOPED, NOT STARTED. Awaiting Will's go.
**Origin:** Codex review 2026-09-06, after the false-cap-alarm repair. Will: *"go ahead and scope the pilot."*
**Question under test (Codex's wording, adopted):** *does the shorter instruction preserve reliable behaviour while reducing reading and maintenance?* **File size alone cannot answer it** — which is why the outcome measures below are behavioural and the byte count is demoted to a secondary observation.

---

## 1. Why a pilot at all, stated honestly

The claim that motivated this — *"WALTER's charter is over cap and rotation only buys a week"* — **was withdrawn.** `READ_CAP.md:37` exempts an auto-loaded charter, and the growth-rate argument was computed off the cliff it had already conceded. **Nothing here is urgent, and the pilot must not be justified by the retracted framing.**

What survives is narrow and was Codex's phrasing: **the intended separation between instruction and incident history is inconsistently applied.** The pilot tests whether closing that gap on ONE step is net-positive. **It is allowed to come out negative** — see §6.

⚠️ **The measurement below is an ESTIMATE, not an audit.** It depends on which sentences I classified as history, and I am the wrong person to make that call unreviewed.

---

## 2. Target selection — measured, not chosen by feel

Per-step measurement of the 20 boot steps (25,192 B total):

| step | bytes | incident prose | % | what it is |
|---|---:|---:|---:|---|
| 7e | 4,996 | 1,317 | 26% | RESEARCH-INTAKE lane, 6 sub-steps |
| 6b | 4,775 | 336 | **7%** | threshold registries |
| **3** | **1,721** | **1,257** | **73%** | **read + evaluate `LAST_COMPLETION`** |
| 1 | 2,493 | 1,585 | 64% | STATUS + Iran anchor |
| 9 | 736 | 587 | 80% | LIAISON discovery |

**TARGET: step 3.** Four reasons, in order of weight:

1. **A live, dated failure exists.** Step 3 failed on **2026-09-06** — I read the carried `SIG-W-20260716-004` flag and reported it to Will without testing it; it had been discharged 9/4. So the behaviour the rewrite must preserve is not hypothetical: *evaluate each carried item before surfacing it.* **A pilot on a step with no known failure mode cannot be graded.**
2. **Highest narrative density at meaningful size** (73%).
3. **Low blast radius.** One action, few obligations (§3), no Will-ruled cross-references.
4. **6b is the counter-example that proves the metric isn't just "big steps."** It is nearly as large and only **7%** incident — its bulk is genuine condition specification (which rows are scannable, which cannot fire). **Shortening 6b would delete rules, not history.** It is explicitly NOT a target.

**Step 1 is the follow-on if this works** — deferred because it carries a Will-ruled read-cap perimeter ruling and the Iran re-verify trigger.

---

## 3. BEFORE-census (READ_CAP rule 18 — audit by obligation, not by byte)

Step 3 obliges exactly six things:

| # | Obligation |
|---|---|
| O1 | Read `LAST_COMPLETION.md` |
| O2 | Treat `FOLLOW-UP` + `OPEN DESIGN DECISIONS` as the canonical running list of open items |
| O3 | Carry them forward every closeout |
| O4 | **EVALUATE** them — reading is not evaluating |
| O5 | For every carried item naming a FILE / COMMIT / FIGURE / CONDITION, check whether it is still true **before surfacing it in the boot reply** |
| O6 | Prioritise: start with the items whose evidence you already hold |

Everything else in the step is provenance: the 8/20 potash instance, *"PROME caught it; I did not"*, the 12(c) cross-reference, and two `[[finding_]]` links.

### 🔴 The census already found something a byte check never would

The step's final sentence —

> *"When a step's verb is 'read' or 'refresh', ask what would happen if the thing were already gone or already false — if the answer is 'nothing', the step is decorative."*

— **is not a step-3 obligation at all. It is a general test that applies to every step in the protocol**, and it is the sentence that diagnosed the `## BOTTOM LINE` absorption on 9/6 (12(e)'s verb was "re-cut"; the answer was "nothing"). **Filed inside step 3, it is invisible to anyone reading any other step.**

⇒ **A naive "move the narrative to `BOOT_PROTOCOL`" would bury the most portable rule in the step.** This is exactly the loss rule 18 exists to catch, and it is why the census runs first. **Disposition is a decision the pilot must make explicitly, not a side effect** — options: promote to a general principle in the protocol preamble, or to fleet auto-memory. **Not to be resolved by whoever happens to be editing.**

---

## 4. The rewrite

**Target form** (Codex): `TRIGGER · REQUIRED ACTION · FAILURE BEHAVIOUR · REFERENCE`, **preserving any example necessary to interpret the rule.**

⚠️ **"Preserving the example" is the load-bearing clause and the hardest judgement.** O5 is abstract; the potash instance is what makes "still true" concrete. **The pilot keeps ONE instance, in one line, chosen for interpretive value — not for being the most dramatic.** Candidate: the 9/6 `SIG-W-20260716-004` case, because it is fresher and shows the mirror form (the action happened, the record didn't).

**Constraints, binding:**
- **No obligation may be dropped.** The after-census must return all six, or the rewrite is rejected.
- History goes to `BOOT_PROTOCOL.md` §3, which is **off the boot reading path** — per READ_CAP rule 17 that is the branch that CAN reduce reading cost, and the branch that owes an obligation re-homing.
- **The active instruction states current behaviour once.** No correction-beside-the-old-text (`[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]` — the defect found on this desk four times today).

---

## 5. Outcome measures — PRE-REGISTERED, because a test scored after the fact is not a test

**Primary — does the short form transmit the obligations?**
Spawn a `coldreader` on the NEW step text ALONE (no history, no charter context) and ask: *what does this step require you to do, and how would you know you had failed?* **Grade: does it recover all six obligations of §3?**
- **PASS** = 6/6 recovered.
- **PARTIAL** = O1–O3 recovered, O4/O5 lost ⇒ the rewrite kept the *reading* and dropped the *evaluating*, which is the whole point of the step. **Treated as FAIL.**
- **FAIL** = any of O4/O5/O6 not recovered.

**Secondary — maintenance cost.** At the next real boot: was step 3 executed correctly **without opening `BOOT_PROTOCOL` §3**? Evidence = the boot transcript, not recollection.

**Tertiary — bytes.** Recorded, not a success criterion. **A rewrite that shrinks the step and loses O5 is a failure with a good byte number**, which is the failure mode this whole week was about.

---

## 6. The confound, and what would falsify the pilot

🔴 **I would be author, executor and grader of a single observation.** `[[finding_crosscheck_with_free_parameter_validates_nothing]]` — a test with a free parameter validates nothing, and "I wrote it and it reads clearly to me" is entirely free.

**Mitigations, all three required:**
1. **Criteria pre-registered above, before the rewrite exists.** No goalpost movement.
2. **The primary grader is blind** — a `coldreader` that has never seen the old step. Its answer is the result, not my read of its answer.
3. **Codex reviews the diff**, as it did the repair.

**Abort / negative results, declared in advance:**
- Cold reader recovers <6 obligations after **two** rewrite attempts ⇒ **the pilot returns NEGATIVE: this step's behaviour requires its narrative.** That is a publishable result and the honest end of the fleet-wide idea, not a reason for attempt three.
- The rewrite grows any other surface by more than it cuts from the charter ⇒ rule 17: report the total, stop claiming a saving.
- The general-principle sentence (§3) cannot be re-homed without a ruling ⇒ **stop and ask**, do not decide it inside an editing pass.

**Explicitly out of scope:** any other boot step, any closeout step, any other desk, and any fleet-wide recommendation. **n=1 is a floor that reads like a count** — one step succeeding says nothing about nineteen others.

---

## 7. Cost

One session, ~45 minutes: census (done, §3) → rewrite → coldreader spawn (~$0.05) → grade → commit or revert. **Revert is one `git checkout` of one line.**

**Decision needed from Will:** go / no-go, and whether the §3 general-principle sentence is re-homed by WALTER or ruled by PROME.
