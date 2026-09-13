# WQ-239 — Boot interrupt contract · capability-scoped blocking · closeout duplication
**PROPOSED 2026-09-12 20:3x ET Sat** (LAPTOP `WilliePOwen`, session `prome-cg`) · **Origin:** an external CODEX review Will relayed in-session, three bounded changes · **Status: PROPOSED, nothing edited.**
⚠️ **`finding_relayed_recommendation_is_not_an_approval`** — a reviewer's recommendation relayed through the operator is still a recommendation. Change ① alters PROME's interrupt contract *with Will*, which is his to rule. Nothing in this record is installed without his word.

**Verdict up front: ① RIGHT but under-specified (the ask must become a REPORT, not disappear) · ② RIGHT in diagnosis, WRONG in the obvious remedy (demoting the check inverts the failure direction) · ③ RIGHT, and it is a re-discovery of a defect already registered at DOCKET L338 leg (d).**

---

## §0 Acceptance conditions — written BEFORE any edit (WQ-229)

Stated as properties in the defect's own terms, not as a restatement of the symptom. **Each condition below is marked with how it is exercised: `[S#]` = a scenario in §4 · `[ART]` = verified at the named artifact · `[ARG]` = argued in prose and NOT tested.** ⛔ **An earlier draft of this line claimed “these are the test list” and that was false — 8 of 15 conditions had no test at all. The marks are the honest form; `[ARG]` is a disclosure, not a pass.**

**① Boot interrupt contract**
- A1. `[S1]` A boot where Will named a lane, with owed items and a credential gap unrelated to that lane, **starts the lane without stopping.**
- A2. `[S1,S4]` Owed work is still **visible to Will at the boot report** — reporting is not the same as asking, and dropping the report is not the goal. (⛔ CODEX's specimen report drops the owed slate entirely; I do not adopt that half.)
- A3. `[S5]` The **third-boot disposition survives.** A dated owed item reaching its third boot unrun still leaves SCRATCH for a DOCKET `COVERED:` annotation or a WQ row. **This clause, not the question, is the anti-rot carrier.**
- A4. `[S6]` The **`Last spine audit:` stamp check survives.** It rides in the same BOOT step 8 and `prome_gate.py boot` carries no check for it, so the runner is its only carrier — spine audit #13 (2026-09-12) caught the runner having dropped exactly this half once already.
- A5. `[S2,S7b]` The three interrupt triggers are **decidable from surfaces boot already reads** — not from judgement about what Will "would want."
- A6. `[S9]` Both runner copies (`.claude/skills/boot/SKILL.md`, `PROME/.claude/skills/boot/SKILL.md`) change together and the parity gate stays green; the runner's `description:` frontmatter also states the old contract (*"FORCES the owed-items question"*) and must change with it.

**② Capability-scoped blocking**
- B1. `[S1]` A missing credential **does not gate work that does not use it** (editing a process document).
- B2. `[S3 PARTIAL]` A missing credential **does gate the dependent claim**, and the block is enforced **where the claim is made**, not only at boot.
- B3. `[ART]` The gate's classification and `BOOT.md`'s prose **agree** — the manual must not call it blocking while the gate treats it as scoped, or vice versa.
- B4. `[ARG n=1]` ⛔ **The check does not get quieter.** `FFIEC_CDR_TOKEN` has been missing since 2026-08-07 **while classified BLOCKING**, across five machine switches. Blocking severity was never the binding constraint, so removing severity cannot be the fix, and lowering it would trade loud-and-safe for silent-and-certifying.
- B5. `[S7]` The scoped state is satisfiable **only by a registration that is still in date**, never by ignoring it — green requires a `WILL_QUEUE` row naming the gap **AND within its needed-by**. ⛔ **Registration alone is NOT sufficient and an earlier draft of this condition said it was** — registration is a one-time act, absence is a standing state; without the date leg, filing the row buys permanent silence.

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

> — **and REPORT owed prior-session work as a ranked one-line digest with a stated first action** (*"owed: A · B · C — starting A"*), then start it. ⛔ **Do NOT stop for an answer.** PROME interrupts Will at boot **only** on a member of the closed list below. **The list is EXHAUSTIVE: an item not on it is REPORTED, never asked. Members are added by ruling, never by judgement in the moment** — an open head clause plus examples is not a decidable test, it is discretion wearing a list's clothes.
>
> **(a) AUTHORITY, and DUE** — a `WILL_QUEUE.md` § OPEN row **at or past its needed-by date**; a trade or spend consequent; or a Will-gated surface the named lane would have to edit. ⛔ **NOT the mere existence of a `WILL_QUEUE` row** — the queue is never empty, so that reading interrupts on every boot and the amendment changes nothing.
> **(b) DEPENDENCY** — the named lane's next action cannot be executed without a specific missing artifact, credential or ruling, **named in the report**. Test: PROME can state what is missing. If it cannot name it, it is not (b).
> **(c) DATED, and worse for waiting** — exactly these six: a `GATES.tsv` row `FIRED-UNEXECUTED` · a LIVE INSTRUMENT `GATES.tsv` row past `review_by` · a `WILL_QUEUE` row at or past needed-by · **a `DOCKET.tsv` row dated inside 24h** · **an expiry or roll inside 5 sessions on a live position surface** (root rule #8 puts rolls, trims and expiries before new research threads, and expiries live on position surfaces, not in `GATES`/`DOCKET`) · **an unconsumed ACTION-class packet in `PROME/inbox/`**.
>
> ⚠️ **The last three members were added after a blind read found the first draft closed them out** — it reported a catalyst inside 24h, a Monday expiry seen at a Saturday boot, and an overnight 🔴 escalation as *not* interrupt-worthy, while BOOT step 8's own surviving sentence still opens *"Flag top issues: catalysts within 24h…"*. **A trigger list that drops what the step it replaces already required is a narrowing disguised as a clarification.**
>
> Absent every member, **routine authorized maintenance is PROME's to run, not to ask about** — the tier is `AUTONOMY.md`'s, and Tier 1 already includes follow-up work inside an approved workstream. **The third-boot disposition is UNCHANGED:** a dated owed item reaching its third boot unrun leaves SCRATCH for a DOCKET `COVERED:` annotation or a WQ row.

**What I do NOT adopt from CODEX.** Its specimen report ends *"Routine maintenance remains tracked"* and names no owed item. That is one step past the fix: it removes the interruption **and** the visibility. A1 and A2 are separate properties and the amendment must hold both.

---

## §2 Change ② — capability-scoped, and why the obvious remedy is wrong

**The diagnosis is right.** `prome_gate.py:759` wires `env_doctor` as `BLOCK`, and `BLOCK`'s contract (`prome_gate.py:30`) is *"disposition before proceeding"* — for **all** work. A missing NASA key has no bearing on editing a process document. Today that produced a 🔴 BLOCKED boot over three keys none of the session's work touches.

**⛔ The obvious remedy — demote `env_doctor` to `ADVISE` — is wrong, and the evidence is in the defect itself.** `FFIEC_CDR_TOKEN` has been absent **since 2026-08-07, the whole time classified BLOCKING**, and rode five machine switches. **Severity was never the binding constraint.** Demoting it would be `finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction` — trading a loud-and-safe failure for a silent-and-certifying one — on a check whose loud form already failed to produce a repair.

**Proposed instead: a third class, `CAPABILITY`, with a contract the other two do not have.**

| | `BLOCKING` | **`CAPABILITY` (new)** | `advisory` |
|---|---|---|---|
| rc | rc=1, stops everything | **rc=0 for unrelated work** | rc=0 |
| names | the failing check | **the failing check AND the exact dependent workflows** | the failing check |
| goes green when | fixed | **fixed, OR a `WILL_QUEUE` row names the gap AND that row is within its needed-by date** | fixed |
| prints when failing | yes | **yes — at EVERY boot, dependent workflows named; green here means “tracked”, never “absent from the report”** | yes |
| escalates | — | **to `BLOCKING` the moment no row names it, or its row passes needed-by** | — |
| ignorable | no | **no — green requires registration** | yes, in practice |

⛔ **The escalation row is the whole design, and the first draft did not have it.** A blind read found that draft **failing its own B4**: green-on-registration would have turned today's rc=1 into rc=0 with all three keys still missing, and held it there for as long as the row stayed open — strictly quieter than BLOCKING, on the very instrument B4 cites. **Registration is a one-time act; absence is a standing state.** Keying green on the row's *date* rather than its *existence* is what makes the state falsifiable: the gap gets a clock, and the clock expiring restores the block. This satisfies B1/B2/B4/B5: unrelated work proceeds, the gap is named at every boot, and it cannot be parked. It is also what today's session produced by hand — WQ-238 — so the class encodes a behaviour already judged correct rather than inventing one.

**⚠️ The half that is NOT PROME's (B2, wrong-owner).** `env_doctor.py:42-47` states the real failure mode itself: without the key, *"the laptop's first FIRMS pull fails as 'Invalid MAP_KEY' inside FALCON's own workflow, where it reads as a broken SERVICE rather than a missing key on this box."* **That point-of-use fix belongs to the desk that owns the workflow.** PROME's obligation is to route it; PROME does not edit FALCON's tooling. ⛔ **Change ② is therefore incomplete by construction on this box alone — and saying so is part of the proposal, not a caveat on it.**

---

## §3 Change ③ — closeout duplication (already half-registered)

**CODEX re-discovered a defect that is already on the docket.** `DOCKET L338` leg (d), registered 2026-09-11: *"`CLOSEOUT.md`:46 and :118 STILL mandate the SCRATCH 'full rewrite' WQ-232 removed at :29 — the amendment changed 1 of 3 surfaces (ARGUS ❌6)."* Verified at the artifact today: `:29` carries the corrected Light-tier rule, **`:46` and `:118` both still say "full rewrite."** An independent reviewer arriving at the same finding from the other direction is corroboration, and it makes the extension cheap — the edit was already owed.

**Proposal:** promote the WQ-232 "does the boot path already reach it?" table from Light-tier to **all tiers** (C1), and fix `:46` and `:118` in the same edit (C2). The five-row test is unchanged; only its scope widens.

**⛔ Sequencing constraint, and it is the reason this change goes LAST.** `CLOSEOUT.md` is at **30,863 B = 94.8%** of its 32,550 B read cap. Amending it *adds* bytes to a capped manual whose rotate-vs-hot/cold-split decision (L338) is **itself the owed item due today**. **The decision must land before the amendment**, or change ③ pushes the file nearer the ceiling to fix a rule about duplication — the overlap failure named at §0.

**CODEX's closing caution is correct and today supplies the proof.** *"Rotating files first would temporarily reduce their size while preserving the behavior that fills them again."* `ACTIVE_DECISIONS` went 76.4% → 73.6% today **by rotating an 11-deep `Updated:` stamp chain** — the generating behaviour untouched. C4 states this so the rotation is never reported as the repair.

---

## §4 Scenario tests — the draft run against concrete cases

CODEX asked for four. S5/S6 are mine: they test the **removal**, which is where an amendment like this actually breaks.

| # | Scenario | Required behaviour | Draft holds? |
|---|---|---|---|
| **S1** | Today's boot: lane named, owed items present, credential gap unrelated to the lane | Report owed as one line, state the first action, **start** | ✅ no trigger fires — (a) no authority needed, (b) FFIEC/FIRMS do not block process work, (c) nothing dated worsens |
| **S2** | A `FIRED-UNEXECUTED` gate row, or a LIVE INSTRUMENT row past `review_by` | **Interrupt** | ✅ trigger (c), and both are already BLOCKING checks in `prome_gate.py` — decidable, not judged |
| **S3** | Will asks what FIRMS shows on the Petroline route | **Refuse at the point of use**, name the missing key on this box, do not substitute a weaker source silently | ⚠️ **PARTIAL** — PROME's side holds (trigger (b) fires, WQ-238 is the named blocker). **The FALCON-side message is not PROME's to fix** and stays wrong until that desk lands it. Stated, not smoothed. |
| **S4** | Boot with **no** directed task | ⛔ The case CODEX's phrasing does not cover — *"boot resumes your chosen work"* presumes chosen work exists | ✅ **as drafted:** report the ranked owed digest and **start the top item as a statement, not a question** (*"starting A"*), leaving Will a one-word override. Never an idle wait, never a menu. |
| **S5** | A dated owed item reaches its **third** boot unrun | Third-boot disposition still fires → DOCKET `COVERED:` or a WQ row | ✅ A3 — the clause is preserved verbatim and is the anti-rot carrier |
| **S6** | The edit lands on BOOT step 8 | The `Last spine audit:` stamp check **survives** | ✅ A4 — it has no other carrier; spine audit #13 caught the runner dropping this exact half once already |

**Added after the blind read — these three exercise the conditions that had no test at all (❌5).**

| # | Scenario | Required behaviour | Draft holds? |
|---|---|---|---|
| **S7** | The FFIEC/FIRMS gap with WQ-238 filed, and WQ-238 **passes its needed-by** with the keys still absent | **Escalate to `BLOCKING`** — a filed row must not buy permanent silence | ✅ **only under the repaired rule.** ⛔ The FIRST draft FAILED this: green-on-registration would have held rc=0 indefinitely, which is the silent-and-certifying outcome B4 forbids. Caught by the blind read, not by me. |
| **S7b** | Boot with WQ-238 and WQ-239 open, both **inside** their needed-by, and no other trigger | **Do not interrupt** | ✅ under the repaired trigger (a). ⛔ The FIRST draft FAILED this too — "a `WILL_QUEUE` row" fires on every boot, because the queue is never empty. |
| **S8** | Standard closeout whose only change is a dated obligation **already registered in DOCKET** | SCRATCH writes **no narrative** and says so — a stated no-op, never silence | ✅ C1: the WQ-232 five-row test, applied past Light tier, returns "do NOT restate" |
| **S9** | The step-8 edit lands | **All three** runner sites stating the old contract change together, parity gate green | ✅ A6 — frontmatter `description:`, step 4 (*"Ask before any directed work."*) **and step 7** (*"yours to have ASKED about"*). ⛔ A6 originally named only the frontmatter; the blind read found the other two. |

**Not scenario-tested, and named rather than implied:** **B3** (verified at the artifact instead — and the disagreement it forbids *already exists today*: `BOOT.md` step 5 reads capability-scoped, *"fix or flag to Will before citing FRED-dependent levels"*, against a gate that is BLOCK-for-everything) · **B4** (argued, n=1) · **C2** (verified at the artifact) · **C3**/**C4** (argued; see residue).

**S3 is the honest weak leg and is reported as PARTIAL, not passed.**

---

## §5 What I recommend, and in what order

| | Change | Owner | Gate |
|---|---|---|---|
| **1st** | ① boot interrupt contract — `BOOT.md` step 8 + both runner copies + the runner `description:` frontmatter | PROME | **Will's word** (it is his interrupt contract) |
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
- **R7 (⚠️7)** — §0 calls all four artifacts PROME-owned, but one runner copy lives at the **repo root** (`.claude/skills/boot/SKILL.md`), outside `PROME/`. **Whether editing it needs a separate Will grant is not settled here and should be settled before ① is implemented** — the parity gate requires both copies to move together, so this is on the critical path, not a footnote.
- **R8 (⚠️6, partially fixed)** — A6 named only the runner frontmatter; the blind read found **two further sites** (steps 4 and 7). Now covered by S9. Residue: no check enumerates the sites, so the next contract change can miss one the same way.
- **R9 (⚠️8)** — bare filenames (`prome_gate.py`, `env_doctor.py`, `board_scan.py`) resolve only by search. All 11 pointers resolved; none dead.

**Four-state completion note (WQ-229):** this record is **PLAN-ONLY**. Not IMPLEMENTED · not TESTED · **the plan is INDEPENDENTLY READ** (one blind cold read, five ❌ fixed, eight ⚠️ declared) · **STILL UNRESOLVED:** S3's point-of-use half (FALCON's, not PROME's) and R7's repo-root grant question. The §4 table is reasoning against draft text, not execution against code — a scenario marked ✅ means *the drafted rule would produce this*, never *this was observed*.
