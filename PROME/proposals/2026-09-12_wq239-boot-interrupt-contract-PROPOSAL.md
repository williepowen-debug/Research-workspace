# WQ-239 — Boot interrupt contract · capability-scoped blocking · closeout duplication
**PROPOSED 2026-09-12 20:3x ET Sat · REVISED 20:4x on Will's direction (v3)** (LAPTOP `WilliePOwen`, session `prome-cg`) · **Origin:** an external CODEX review Will relayed in-session, three bounded changes · **Status: PROPOSED — no canon file edited.** ✅ **Will has RULED one leg already (20:41): both boot-runner copies are one unit of work, no separate approval cycle (R7 closed).** The four outcomes he set — report-then-continue · ask only when his answer is necessary for the next action · capabilities visibly unavailable until restored with deadlines driving escalation urgency only · no-task ⇒ start the highest-priority authorized work — are the spine of §1 and §2 in this revision.
⚠️ **`finding_relayed_recommendation_is_not_an_approval`** — a reviewer's recommendation relayed through the operator is still a recommendation. Change ① alters PROME's interrupt contract *with Will*, which is his to rule. Nothing in this record is installed without his word.

**Verdict up front: ① RIGHT but under-specified (the ask must become a REPORT, not disappear) · ② RIGHT in diagnosis, WRONG in the obvious remedy (demoting the check inverts the failure direction) · ③ RIGHT, and it is a re-discovery of a defect already registered at DOCKET L338 leg (d).**

★ **The revision history is the argument.** Draft 1 made the interrupt test *“a `WILL_QUEUE` row exists”* ⇒ it fired on every boot. Draft 2 made it *“a row past its needed-by”* ⇒ it fired on **`WQ-187` today**, and escalated an overdue capability to `BLOCKING` ⇒ a stale NASA key would stop a process edit. **Both drafts tried to decide the question from DATES.** Will's test decides it from **dependency** — *is my answer necessary for your next action?* — which is answerable without enumerating anything, and which fails in neither direction.

---

## §0 Acceptance conditions — written BEFORE any edit (WQ-229)

Stated as properties in the defect's own terms, not as a restatement of the symptom. **Each condition below is marked with how it is exercised: `[S#]` = a scenario in §4 · `[ART]` = verified at the named artifact · `[ARG]` = argued in prose and NOT tested.** ⛔ **An earlier draft of this line claimed “these are the test list” and that was false — 8 of 15 conditions had no test at all. The marks are the honest form; `[ARG]` is a disclosure, not a pass.**

**① Boot interrupt contract**
- A1. `[S1]` A boot where Will named a lane, with owed items and a credential gap unrelated to that lane, **starts the lane without stopping.**
- A2. `[S1,S4]` Owed work is still **visible to Will at the boot report** — reporting is not the same as asking, and dropping the report is not the goal. (⛔ CODEX's specimen report drops the owed slate entirely; I do not adopt that half.)
- A3. `[S5]` The **third-boot disposition survives.** A dated owed item reaching its third boot unrun still leaves SCRATCH for a DOCKET `COVERED:` annotation or a WQ row. **This clause, not the question, is the anti-rot carrier.**
- A4. `[S6]` The **`Last spine audit:` stamp check survives.** It rides in the same BOOT step 8 and `prome_gate.py boot` carries no check for it, so the runner is its only carrier — spine audit #13 (2026-09-12) caught the runner having dropped exactly this half once already.
- A5. `[T1,T2,S2]` **The interrupt test is ONE question, and it is about DEPENDENCY, not about urgency or dates:** *is Will's answer necessary for PROME's next action?* ⛔ **Not “is it dated”, not “is it overdue”, not “is it urgent”** — those set where an item appears in the report and how loudly, never whether work proceeds.
- A6. `[S9]` **Both runner copies are ONE unit of work** (`.claude/skills/boot/SKILL.md` at the repo root, `PROME/.claude/skills/boot/SKILL.md`) — they change in the same edit and their synchronisation is **not a separate approval cycle**. ✅ **RULED by Will 2026-09-12 20:41 ET**, settling residue R7. All three sites in each copy move together: the `description:` frontmatter, step 4, and step 7.
- A7. `[T1,T2]` ⛔ **An overdue obligation is NOT, by itself, an interrupt.** A boot carrying a past-due `WILL_QUEUE` row, a past-due capability follow-up, or both, **still continues independent authorized work.** Overdue raises escalation urgency inside the report; it never converts a report into a question.

**② Capability-scoped blocking**
- B1. `[S1]` A missing credential **does not gate work that does not use it** (editing a process document).
- B2. `[S3 PARTIAL]` A missing credential **does gate the dependent claim**, and the block is enforced **where the claim is made**, not only at boot.
- B3. `[ART]` The gate's classification and `BOOT.md`'s prose **agree** — the manual must not call it blocking while the gate treats it as scoped, or vice versa.
- B4. `[T2,ARG]` ⛔ **The check does not get quieter — and visibility, not gating, is what delivers that.** A missing capability stays **visibly unavailable at every boot until it is restored**; there is no state in which it stops being reported. `FFIEC_CDR_TOKEN` has been missing since 2026-08-07 **while classified BLOCKING** and blocking repaired nothing, so severity was never the binding constraint — **permanence of the report is.**
- B5. `[T2]` **A follow-up deadline drives ESCALATION URGENCY ONLY, never gating.** Past its needed-by, the capability rises to the top of the report as an urgent obligation and earns a stated escalation to Will; ⛔ **it never becomes a stop on unrelated work.** *(Will-directed 2026-09-12 20:41. An earlier draft escalated the overdue state to `BLOCKING` — that reinstates the original defect under a new name, since BLOCKING's contract is “disposition before proceeding” for ALL work.)*

**③ Closeout duplication**
- C1. `[S8]` The WQ-232 "does the boot path already reach it?" test governs **all tiers**, not Light alone.
- C2. `[ART]` All **three** surfaces that mandate a SCRATCH full rewrite change together (`CLOSEOUT.md:29` already correct · `:46` · `:118`). The 9/11 amendment changed 1 of 3 — that is the registered defect.
- C3. `[ARG — see residue R1]` **Unresolved obligations and evidence links survive the de-duplication** — measured, not asserted, by the blind-reader procedure already mandated for rotations.
- C4. `[ARG — see residue R5]` ⛔ **Rotation is not the remedy and must not be reported as one.** CODEX's closing caution is correct and is confirmed by today's own evidence: `ACTIVE_DECISIONS` went 76.4% → 73.6% **by rotating an 11-deep stamp chain**, with the behaviour that fills the file untouched.

**Neighbour categories (WQ-229 — CONSIDER all five, justified N/A where they do not apply):**
- **ORDINARY** — the three ordinary-path scenarios below: S1 · S2 · S4. (S3 is MISSING INFORMATION, below; S5/S6 test the removal.)
- **OVERLAP** — S6: change ① edits the same BOOT step that carries the spine-audit stamp; change ③ edits `CLOSEOUT.md`, which is at **30,863 B = 94.8%** of its 32,550 B read cap and whose rotate-vs-split decision (L338) is *itself* owed. **An amendment that grows that file before the sizing decision is the overlap failure.**
- **WRONG OWNER** — B2's point-of-use half is **not PROME's**: the FIRMS failure surfaces inside FALCON's workflow. PROME can register and route it; PROME must not edit FALCON's tooling. Split explicitly below.
- **MISSING INFORMATION** — S3: what PROME does when a task genuinely needs the absent credential.
- **CONCURRENT ACTIVITY** — N/A with reason: all four artifacts are PROME-owned (`BOOT.md`, both runner copies, `prome_gate.py`, `CLOSEOUT.md`); no other desk writes them, and `ListAgents` at implementation time is the standing preflight regardless.

---

## §1 Change ① — boot reports owed work instead of asking about it

**The defect, in the artifact's own words.** `BOOT.md` step 8 requires PROME to *"put OWED prior-session work to Will as a choice, not a mention."* The runner's frontmatter says it *"**FORCES** the owed-items question to Will before any directed work starts"*, and runner step 7 says *"the owed items are yours to have ASKED about."* **The obligation is unconditional — it is not conditioned on whether Will's answer would change what PROME does next.**

**Why it is now wrong, and it was not always wrong.** Step 8 exists because dated owed work used to rot unseen. Since then the carriers arrived: the generated `DOCKET-VIEW` block, `willq_view`, `firetime_check`, `spawn_list.py`'s due-row driver (WQ-184), the byte-budget meter, and step 8's own third-boot disposition. **The instruments took over the anti-rot job and the question was never re-scoped** — `finding_a_ruling_governs_the_next_write_not_the_existing_state`, in the slow direction.

**Today is the specimen.** Will opened with *"continue working on optimizing our system and catching up on anything owed"* — the lane was named in the first sentence. Boot still stopped and asked which owed item to take first.

**Draft replacement for BOOT.md step 8's owed clause** (exact text, to be transplanted in ONE edit):

> — **and REPORT, then CONTINUE.** The boot report carries **(i) urgent obligations, surfaced promptly**, and **(ii) a brief ranked owed-work digest**. PROME then continues the task Will directed. **If Will directed no task, PROME selects the highest-priority authorized work and starts it** — announced as a statement, never offered as a menu.
>
> **The interrupt test is ONE question: _is Will's answer necessary for PROME's next action?_**
> - **YES ⇒ ask, and stop on that item only.** It is necessary when the next action is a decision only Will can make (a trade or spend consequent; a Will-gated surface the lane must edit; a ruling the lane's next step consumes), or when a dependency PROME **can name** blocks the directed lane.
> - **NO ⇒ surface it and keep working.** A dated item, an **overdue** item, an urgent risk and a missing capability are all **SURFACED, never asked**, unless the YES branch independently applies. Urgency decides **where in the report an item appears and how loudly** — never whether work proceeds.
>
> ⛔ **An overdue obligation is not, by itself, an interrupt.** `WQ-187` sat at its needed-by on 2026-09-12 and needs Will's **hands**, not his **answer**; no PROME action depended on it. Stopping there would halt independent authorized work to re-ask something the digest already carried.
>
> Absent a YES, **routine authorized maintenance is PROME's to run, not to ask about** — the tier is `AUTONOMY.md`'s, and Tier 1 already covers follow-up work inside an approved workstream. **The third-boot disposition is UNCHANGED:** a dated owed item reaching its third boot unrun leaves SCRATCH for a DOCKET `COVERED:` annotation or a WQ row. **The `Last spine audit:` stamp check in this same step is UNCHANGED** — it has no other carrier.

⚠️ **This replaces the six-member closed list an earlier draft carried, and the replacement is Will's (2026-09-12 20:41), not a tidy of mine.** The list tried to make the trigger decidable by enumerating dated things, and it failed in both directions at once: it **fired on every boot** (any open `WILL_QUEUE` row past needed-by — `WQ-187` today) while **missing** cases no list anticipates. Keying on *dependency* instead of *urgency* is decidable without enumeration, because PROME can always answer whether its own next action needs an answer.

**What I do NOT adopt from CODEX.** Its specimen report ends *"Routine maintenance remains tracked"* and names no owed item. That is one step past the fix: it removes the interruption **and** the visibility. A1 and A2 are separate properties and the amendment must hold both.

---

## §2 Change ② — capability-scoped, and why the obvious remedy is wrong

**The diagnosis is right.** `prome_gate.py:759` wires `env_doctor` as `BLOCK`, and `BLOCK`'s contract (`prome_gate.py:30`) is *"disposition before proceeding"* — for **all** work. A missing NASA key has no bearing on editing a process document. Today that produced a 🔴 BLOCKED boot over three keys none of the session's work touches.

**⛔ The obvious remedy — demote `env_doctor` to `ADVISE` — is wrong, and the evidence is in the defect itself.** `FFIEC_CDR_TOKEN` has been absent **since 2026-08-07, the whole time classified BLOCKING**, and rode five machine switches. **Severity was never the binding constraint.** Demoting it would be `finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction` — trading a loud-and-safe failure for a silent-and-certifying one — on a check whose loud form already failed to produce a repair.

**Proposed instead: a third class, `CAPABILITY`, with a contract the other two do not have.**

| | `BLOCKING` | **`CAPABILITY` (new)** | `advisory` |
|---|---|---|---|
| rc contribution | rc=1, stops **everything** | **always 0 — no state of this class ever gates unrelated work** | 0 |
| names | the failing check | **the failing check AND its exact dependent workflows** | the failing check |
| reported | while failing | **at EVERY boot until RESTORED — there is no green, only `AVAILABLE` / `UNAVAILABLE`** | while failing |
| can be silenced | no | **no — not by a filed row, not by an allowlist, not by age** | yes, in practice |
| refused at point of use | — | **yes — the dependent claim is refused where it is made** | — |
| follow-up row past needed-by | — | **rises to the top of the report as an urgent obligation + a stated escalation — NEVER a gate** | — |

⛔ **Two drafts of this class failed before this one, and neither failure was mine to catch.** A blind read found that draft **failing its own B4**: green-on-registration would have turned today's rc=1 into rc=0 with all three keys still missing, and held it there for as long as the row stayed open — strictly quieter than BLOCKING, on the very instrument B4 cites. **Registration is a one-time act; absence is a standing state.** **Draft 2 then escalated the overdue state to `BLOCKING` — which reinstates the ORIGINAL defect under a new name**, because BLOCKING's contract is *“disposition before proceeding”* for ALL work: a stale NASA key would once again stop a process edit. **Will's correction (2026-09-12 20:41) removes gating from the class entirely**: the capability is *visibly unavailable until restored* — permanence of the REPORT is what keeps it loud — and the deadline moves only escalation urgency. This satisfies B1/B2/B4/B5 without a gate: unrelated work proceeds **in every state**, the gap is named at every boot, and it cannot be parked. It is also what today's session produced by hand — WQ-238 — so the class encodes a behaviour already judged correct rather than inventing one.

**⚠️ The half that is NOT PROME's (B2, wrong-owner).** `env_doctor.py:42-47` states the real failure mode itself: without the key, *"the laptop's first FIRMS pull fails as 'Invalid MAP_KEY' inside FALCON's own workflow, where it reads as a broken SERVICE rather than a missing key on this box."* **That point-of-use fix belongs to the desk that owns the workflow.** PROME's obligation is to route it; PROME does not edit FALCON's tooling. ⛔ **Change ② is therefore incomplete by construction on this box alone — and saying so is part of the proposal, not a caveat on it.**

---

## §3 Change ③ — closeout duplication (already half-registered)

**CODEX re-discovered a defect that is already on the docket.** `DOCKET L338` leg (d), registered 2026-09-11: *"`CLOSEOUT.md`:46 and :118 STILL mandate the SCRATCH 'full rewrite' WQ-232 removed at :29 — the amendment changed 1 of 3 surfaces (ARGUS ❌6)."* Verified at the artifact today: `:29` carries the corrected Light-tier rule, **`:46` and `:118` both still say "full rewrite."** An independent reviewer arriving at the same finding from the other direction is corroboration, and it makes the extension cheap — the edit was already owed.

**Proposal:** promote the WQ-232 "does the boot path already reach it?" table from Light-tier to **all tiers** (C1), and fix `:46` and `:118` in the same edit (C2). The five-row test is unchanged; only its scope widens.

**⛔ Sequencing constraint, and it is the reason this change goes LAST.** `CLOSEOUT.md` is at **30,863 B = 94.8%** of its 32,550 B read cap. Amending it *adds* bytes to a capped manual whose rotate-vs-hot/cold-split decision (L338) is **itself the owed item due today**. **The decision must land before the amendment**, or change ③ pushes the file nearer the ceiling to fix a rule about duplication — the overlap failure named at §0.

**CODEX's closing caution is correct and today supplies the proof.** *"Rotating files first would temporarily reduce their size while preserving the behavior that fills them again."* `ACTIVE_DECISIONS` went 76.4% → 73.6% today **by rotating an 11-deep `Updated:` stamp chain** — the generating behaviour untouched. C4 states this so the rotation is never reported as the repair.

---

## §4 Scenario tests — the draft run against concrete cases

CODEX asked for four (S1–S4). **S5/S6 are mine — they test the REMOVAL, which is where an amendment like this actually breaks. T1/T2 are Will's, set 2026-09-12 20:41, and they are the binding pair: _both must allow unrelated process work._** ⛔ **Draft 2 of this proposal failed BOTH of Will's tests, in opposite directions.** That is the strongest evidence in this record that the enumerate-the-dated-things approach was wrong in kind, not in detail.

| # | Scenario | Required behaviour | Draft holds? |
|---|---|---|---|
| **S1** | Today's boot: lane named, owed items present, credential gap unrelated to the lane | Report owed as one line, state the first action, **start** | ✅ no trigger fires — (a) no authority needed, (b) FFIEC/FIRMS do not block process work, (c) nothing dated worsens |
| **S2** | A `FIRED-UNEXECUTED` gate row, or a LIVE INSTRUMENT row past `review_by` | **Interrupt** | ✅ trigger (c), and both are already BLOCKING checks in `prome_gate.py` — decidable, not judged |
| **S3** | Will asks what FIRMS shows on the Petroline route | **Refuse at the point of use**, name the missing key on this box, do not substitute a weaker source silently | ⚠️ **PARTIAL** — PROME's side holds (trigger (b) fires, WQ-238 is the named blocker). **The FALCON-side message is not PROME's to fix** and stays wrong until that desk lands it. Stated, not smoothed. |
| **S4** | Boot with **no** directed task | ⛔ The case CODEX's phrasing does not cover — *"boot resumes your chosen work"* presumes chosen work exists | ✅ **as drafted:** report the ranked owed digest and **start the top item as a statement, not a question** (*"starting A"*), leaving Will a one-word override. Never an idle wait, never a menu. |
| **S5** | A dated owed item reaches its **third** boot unrun | Third-boot disposition still fires → DOCKET `COVERED:` or a WQ row | ✅ A3 — the clause is preserved verbatim and is the anti-rot carrier |
| **S6** | The edit lands on BOOT step 8 | The `Last spine audit:` stamp check **survives** | ✅ A4 — it has no other carrier; spine audit #13 caught the runner dropping this exact half once already |

**Added after the blind read and Will's direction — T1/T2 are the binding acceptance pair; S8/S9 exercise conditions that had no test at all (❌5).**

| # | Scenario | Required behaviour | Draft holds? |
|---|---|---|---|
| **T1** ★ | **Will's test 1 — today's actual boot.** Lane named (*"optimizing our system and catching up"*); **`WQ-187` is AT its needed-by 2026-09-12** and still unactioned; three credentials missing; owed items present | **Surface WQ-187 as an urgent obligation + the owed digest, then CONTINUE the process work** | ✅ **under the revised rule.** `WQ-187` needs Will's **hands** (a PAT + a bot token), not his **answer** — no PROME action depends on it ⇒ NO branch ⇒ surfaced, not asked. ⛔ **Draft 2 FAILED this test:** its trigger (a) fired on *"a `WILL_QUEUE` row at or past its needed-by"*, so WQ-187 would have stopped the session today. Found by Will, not by the blind read and not by me. |
| **T2** ★ | **Will's test 2 — the same boot replayed after 2026-09-19**, `WQ-238` past its needed-by, all three credentials **still missing** | **Escalate the capability loudly — and still allow unrelated process work** | ✅ **under the revised rule.** `CAPABILITY` contributes rc=0 in every state; past needed-by it rises to the top of the report as an urgent obligation with a stated escalation. ⛔ **Draft 2 FAILED this test too:** it escalated the overdue capability to `BLOCKING`, whose contract is *"disposition before proceeding"* for ALL work — a stale NASA key would have stopped a process edit. **The two drafts failed in opposite directions; the dependency test fails in neither.** |
| **T2b** | Same as T2, but the directed task **is** a FIRMS-dependent claim | **Refuse at the point of use, naming the missing key on this box** | ⚠️ **PARTIAL, same limit as S3** — PROME's side holds (YES branch: a named dependency blocks the lane). The FALCON-side message is not PROME's to fix. |
| **S8** | Standard closeout whose only change is a dated obligation **already registered in DOCKET** | SCRATCH writes **no narrative** and says so — a stated no-op, never silence | ✅ C1: the WQ-232 five-row test, applied past Light tier, returns "do NOT restate" |
| **S9** | The step-8 edit lands | **All three** runner sites stating the old contract change together, parity gate green | ✅ A6 — frontmatter `description:`, step 4 (*"Ask before any directed work."*) **and step 7** (*"yours to have ASKED about"*). ⛔ A6 originally named only the frontmatter; the blind read found the other two. |

**Not scenario-tested, and named rather than implied:** **B3** (verified at the artifact instead — and the disagreement it forbids *already exists today*: `BOOT.md` step 5 reads capability-scoped, *"fix or flag to Will before citing FRED-dependent levels"*, against a gate that is BLOCK-for-everything) · **B4** (argued, n=1) · **C2** (verified at the artifact) · **C3**/**C4** (argued; see residue).

**S3 and T2b are the same honest weak leg, reported as PARTIAL, not passed** — one point-of-use message, owned by FALCON.

---

## §5 What I recommend, and in what order

| | Change | Owner | Gate |
|---|---|---|---|
| **1st** | ① boot interrupt contract — `BOOT.md` step 8 + **both runner copies as ONE unit** (frontmatter, step 4, step 7) | PROME | **Will's word** (it is his interrupt contract). Runner-copy scope ✅ already ruled 20:41. |
| **2nd** | ② `CAPABILITY` class in `prome_gate.py` + the matching `BOOT.md` step-5 prose (B3) | PROME | Will's word — it changes what a 🔴 boot means |
| **2nd-b** | ② point-of-use failure message | **FALCON (not PROME)** | route a packet; do not edit |
| **3rd** | ③ WQ-232 test to all tiers + `:46`/`:118` | PROME | **after** the L338 rotate-vs-split decision, not before |

**Rec: approve ① and ② together; hold ③ behind the L338 decision.** ① and ② are the pair that changes what a restart costs you; ③ is hygiene that should not push a 94.8%-full manual higher until its own sizing question is settled.

**Implementation discipline if approved:** each canon file is drafted **here**, cold-read here (the WQ-178 plan read), and transplanted in ONE edit; the result read may force at most one further edit per file, then residue is declared in this record. `ListAgents` preflight before any spawn. Both `.claude/` copies move together or the parity gate fails.

## §6 Residue — declared, not dissolved (blind plan-read, 2026-09-12 20:3x)

**The read scored 13/26 ✅ · 8 ⚠️ · 5 ❌. All five ❌ are fixed above; the eight ⚠️ are declared here and NOT fixed, per the WQ-178 read budget. Two of the ❌ were failures of a condition against its own draft text — the draft violated B4 and A5 — and neither was found by me.**

- **R1 (⚠️1)** — C3's verification pointer resolves but **will not fire on the change it governs**: `CLOSEOUT.md` mandates a blind reader for *byte-flow rotations* and HEARTBEAT re-bases, and change ③ is an amendment, not a rotation. C3 is self-executing only if the L338 rotation happens first. Not restructured; the §5 sequencing already puts ③ last, which makes it true in practice but not by construction.
- **R2 (⚠️5, with the fact corrected here)** — the body's *"76.4% → 73.6%"* for `ACTIVE_DECISIONS` **does not reproduce**: `measure.py` reads **24,068 B against the 32,550 B budget** as of this record. The figure was true when STATUS wrote it and is stale now. ⚠️ **C4's direction survives the correction — the file shrank by rotating a stamp chain, with the generating behaviour untouched — but a ⛔ condition should not lean on a number a reader cannot re-derive.**
- **R3 (⚠️5, second half — self-inflicted)** — this record carries **three recomputable file sizes in prose**, which PROME's own § Session Process Controls forbid (*"a document never carries a figure a reader can recompute from an instrument… it names the instrument instead"*). Left in place this pass because the read budget allows ❌ fixes only; **the transplanted canon text must name `measure.py` and carry no figure.**
- **R4 (⚠️2)** — a stranger reading §3's *"goes LAST"* alone could take it as *after the split is executed*, which DOCKET L338 leg (g) explicitly flags as a prior overstatement: the precondition is the **decision**, not the split. §5 says so; §3 does not quote the clarification.
- **R5 (⚠️3)** — trigger **(b)** has no instrument. Under change ②, boot-time blocking is exactly what `CAPABILITY` stops doing, so a reader cannot tell whether (b) is evaluated from the dependent-workflow list, from PROME's judgement, or from an rc that is now green. **The "name what is missing" test added above narrows it; it does not instrument it.**
- **R6 (⚠️4)** — *"five machine switches"* is **unsourced**. `MACHINE_LOCAL` says the clause lapsed across every switch since 2026-08-07 without a count. The count should be dropped or derived before transplant.
- **R7 (⚠️7) — ✅ RULED, CLOSED.** Will 2026-09-12 20:41: **both boot-runner copies are in implementation scope and their synchronisation is not a separate approval cycle.** The repo-root copy (`.claude/skills/boot/SKILL.md`) is edited in the same unit of work as the `PROME/` copy; the parity gate is a check on that unit, not a second gate to clear.
- **R8 (⚠️6, partially fixed)** — A6 named only the runner frontmatter; the blind read found **two further sites** (steps 4 and 7). Now covered by S9. Residue: no check enumerates the sites, so the next contract change can miss one the same way.
- **R9 (⚠️8)** — bare filenames (`prome_gate.py`, `env_doctor.py`, `board_scan.py`) resolve only by search. All 11 pointers resolved; none dead.

**Four-state completion note (WQ-229):** this record is **PLAN-ONLY**. Not IMPLEMENTED · not TESTED · **the plan is INDEPENDENTLY READ** (one blind cold read, five ❌ fixed, eight ⚠️ declared) · **STILL UNRESOLVED:** S3's point-of-use half (FALCON's, not PROME's) and R7's repo-root grant question. The §4 table is reasoning against draft text, not execution against code — a scenario marked ✅ means *the drafted rule would produce this*, never *this was observed*.
