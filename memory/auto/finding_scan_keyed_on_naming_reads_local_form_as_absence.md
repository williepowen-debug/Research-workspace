---
name: finding_scan_keyed_on_naming_reads_local_form_as_absence
description: a scanner keyed on how a surface is NAMED/shaped reads "surface I cannot recognize" as "surface does not exist" — absence-of-recognizable-form ≠ absence-of-thing; before reporting N agents lack X, re-read a sample for X expressed in LOCAL forms, and fix by extract-and-stamp, never rebuild-over-a-working-thing
symptoms: an absence inferred from a DIFFERENCE (a kink read as a zero) · a filtered query counted for PRESENCE and reported as a MAXIMUM · "nothing since <date>" from a query that filtered on that date · scan says X is missing but X exists · "no agent has X" / "surface carries no X" refuted on re-read · grep pattern had no capacity to match the target · empty awk/section extract treated as a short section · column/id named differently (trigger_id vs gate_id) · clean scan against the wrong referent · recommendation right but rationale false · grep matched fine but ran over too few FILES · "appears nowhere in <X> and <Y>" quoted downstream as "appears nowhere" · read the .json and never the .md of the same document · searched the RECORDS and skipped the PROPOSAL · question already answered before it was raised · peer registers work off your scan and inherits its scope gap · a purpose-built coverage checker already existed, was green, and nobody ran it · two desks independently "verified at the artifact" and got the SAME clean zero · counted what my instrument MATCHED, not what the lane DELIVERED · your own commit body from weeks ago contradicts the absence you just asserted
metadata:
  type: finding
---

**A detection instrument that matches on canonical naming or file shape silently converts "expressed in a form I don't recognize" into "does not exist" — and the resulting finding reads as a capability gap in the SCANNED agents when it is a vocabulary gap in the SCANNER.**

**Worked case (2026-08-03 → corrected 2026-08-07, DAEDALUS Falsification Sweep F5).** The sweep's headline finding: *5 agents carry a live thesis and NO falsification surface* — encoded same-week into a ladder requirement and a blueprint amendment. Production-Review re-reads four days later: **4 of the 5 HAD live, exercised falsification discipline**, expressed in local forms the scanner could not name — an `EXIT / INVALIDATION` triad (WATT — which had graded a real MISS *through* it, with the registered migration executing as pre-written), numbered thesis-kill routes (OSPREY — known-defective and the owner correctly refusing self-repair), per-channel bidirectional flip rows with one already marked `falsified-direction` (AEOLUS), an in-thesis "What KILLS v2" block with an exercised kill condition (MIDAS). Only 1 of 5 was genuinely missing the thing. The scanner had matched kill-tree-shaped FILE NAMING.

**Why it is dangerous beyond one bad sweep row:** the finding fed a *standard* the same day (an L3 requirement), so grading against the blind detector would have mis-set grades, not just sweep rows — and the natural "fix" (make each agent author the canonical-shaped surface) would have **rebuilt over four working rails**, destroying local forms the fleet's own floor-not-ceiling principle protects.

## How to apply

- **Before reporting "N agents lack X" off any scan, re-read a SAMPLE of the N for X expressed in local vocabulary** — the scan's negative is a claim about its own pattern set until a human read confirms it. Sibling of `[[finding_verification_zero_is_ambiguous]]` ("never in its scope" branch) and `[[finding_count_measures_intake_not_domain]]` (a CLAUDE.md-only grep measures homing, not knowledge).
- **Split the finding into its two real parts:** (a) does the DISCIPLINE exist (judgment read), (b) is it on a surface the instrument can SEE/DATE (mechanical). Only (b) was true here — and (b) is still worth fixing, because an unfindable rail can't be freshness-checked.
- **The retrofit form follows from the split: EXTRACT-AND-STAMP** — give the existing local-form thing a findable/datable handle (one stamp line, a pointer, a canonical filename alias) — **never author-from-scratch over a thing that works.** Authoring fresh is only correct for the genuinely-missing residue.
- **Spec the v2 predicate on function, not shape:** "no surface, OR a surface with no evidenced fire path" flags the decorative rail correctly and stops flagging working local forms. And keep a disposition class for *live-but-known-defective-and-owner-escalated* — an owner refusing to self-amend its own falsifier (because the amendment would make it harder to trigger) is exhibiting the discipline, not lacking it.

---

**n=2 same agent, opposite content class, and the fix-form sharpens (WATT, 2026-08-17 — DAEDALUS append).** Two weeks after the kill-rail naming mis-read (PAT-078), a second FORM-keyed scan mis-read the SAME agent the SAME direction: the two-state pilot's scoping predicted "nothing to rotate" off a scan for dated session HEADINGS, while WATT's accretion lived inside prose BLOCKQUOTES self-labelled "retained for continuity" — 10,902 bytes of it, rotated legitimately on first pass. **Density and accretion are independent properties: bytes-per-line is evidence about FORMATTING, never about supersession.** Both instruments failed toward "clean," and a clean verdict is precisely the one nobody re-checks. Sharpened fix-form: key rotation/staleness targets on **SUPERSESSION SEMANTICS** (is this content replaced by later content in the same file?), with two cheap proxies that would have caught both instances — a block carrying a date older than the file's own Last-Updated stamp, and a block whose text self-labels ("prior," "retained," "superseded," "for continuity"). Owner corollary (WATT L-31): *a clean scan result about your file is evidence about the scanner until you have re-read the file yourself.*

---

**n=3, and this one is COLUMN-NAME rather than file-form — plus the memory-holder committed it (WALTER, 2026-08-20).** WALTER measured the fleet's trigger-registry coverage and reported *"only 3 desks keep machine-readable registries; ≥6 gate families are prose-only"* — routed to DAEDALUS, ruled by Will, and carried on WALTER's own STATUS and closeout surfaces. **`PROME/GATES.tsv` exists at repo ROOT, is fully machine-readable, and already registered ALL SIX families marked "prose only" — 26 rows across many desks.** The scan keyed on the column name **`trigger_id`**; that file's column is **`gate_id`**. **A central registry was invisible to a scan looking for a synonym.**

⚠️ **Two things make this the sharpest instance of the three.** **(1) The blind spot was ONE WORD, not a form or a vocabulary** — no prose, no local convention, no judgement call; a well-formed TSV with a differently-named key column read as absence. **A scan that enumerates by IDENTIFIER NAME will miss every synonym, and synonyms are the norm across desks that never coordinated their schemas** (`trigger_id` / `gate_id` / `setup_id` all name the same concept in this fleet). **(2) WALTER HELD THIS MEMORY AND COMMITTED THE FAILURE ANYWAY** — which is the real finding: *possessing the lesson is not possessing the check.* It fired for others and not for its owner, on the same day WALTER also broke its own freshly-written FRED-T+1 rule four hours after writing it.

**Fix-form, additive to the two above:** when scanning for a CONCEPT across desks, **enumerate candidate files by SHAPE and CONTENT first (does it have rows with thresholds, owners, states?), and only then read whatever the id column happens to be called** — never make the identifier name the search key. And **check the repo ROOT, not only agent directories**: a fleet-central registry lives outside every `AGENTS/<NAME>/` path a per-agent sweep walks. `[[finding_comprehensive_grep_over_sampling]]`

---

**n=4, and this one adds the WALKED-PAST-EMPTY-EXTRACT facet — self-caught and self-retracted by the committer within the hour (MIDAS, 2026-08-27; banked at owner as L-30; PROME append).** MIDAS flagged PROME's HEARTBEAT §8 as *"carries no gold level at all."* False — the level was present in §8's GCZ26 path line in the pre-flag commit (`git show 9438c397a | grep -c '4,598\.20'` → 1). The instrument: a grep for `87.93|DIVERGENCE RESOLVED|encodes owed|deliberate disagreement|currency-stripped` — **not one term with the CAPACITY to match a price** — plus an `awk` section-extract that returned EMPTY (heading format mismatch) and was **walked past as if empty meant short, straight into a narrower grep with undiminished confidence.** Two sharp facets, additive to n=1-3: **(1) an EMPTY section-extract is a FAILED READ, not a short section** — the zero-result must be disambiguated before any whole-section property is asserted (sibling of the F5 lesson at the extract level); **(2) the actionable RECOMMENDATION was still correct** (the marks line genuinely lacked gold, and adding it improved the surface), so **every outcome-keyed check passed while the stated rationale was false** — the L-26 shape (right number, wrong construction label) at the level of a peer flag. Encode the true, narrow, checkable rationale ("the marks line lacks X"), never the whole-surface absence claim the instrument could not have established. Meta-instance: MIDAS committed this while reading a line that quotes its own §1.1 wrong-referent defect verbatim — *reading the sentence describing the defect is not running the check* (the WALTER n=3 lesson, recommitted by a different desk that also held it).

---

**Instance 2026-08-27 (REGINALD, Gate C) — the SECOND axis: the pattern was right and the SURFACE SET was short.** Every prior instance here is about a scanner whose *pattern* could not match the target. This one is the mirror: **the pattern matched perfectly and the scan still returned a false absence, because it was run over 2 of at least 4 surfaces.**

Before submitting a Kernel prediction I flagged that `REG-01`'s `opens_at` (2026-02-23) predated its 2026-08-27 submission, and asked whether backdating was legal. Checking whether anyone had already ruled it, I grepped **the ruling record and the sitting transcript** for `opens_at`. It matched only as the field name inside another desk's unrelated validation failures. I wrote: *"the question appears **nowhere** in the ruling record or transcript, and is not among the standing preconditions."* A coordinator registered it as a new precondition off **that same two-surface scope**.

**It had already been dispositioned — twice — before I raised it.** The activation packet's own open-questions section named `REG-01` **by ID** and posed my question verbatim (*"Bless or require re-cut"*), and the reviewer's report had **BLESSED** it with a tighter rule than mine. I had opened that packet's activation **JSON** and never its **`.md`** — the same document, a different file extension.

**Why it evaded the usual defence.** My sentence was *technically true and correctly qualified* — I named the two surfaces I searched. The failure was that **the qualification did not travel**: "appears nowhere in X and Y" is read downstream as "appears nowhere", and the coordinator inherited the gap without re-deriving the scope. **A scoped negative degrades to an unscoped one at the first hop.**

**How to apply (adds to the rules above):**
- **Before writing "X appears nowhere", enumerate the surfaces that COULD carry X — then say which you searched and which you did not.** A negative with no denominator is not a finding.
- **Ask who would have had to write it down.** A governing question about *your* object is most likely to live in the document that *proposes* the action (packet, plan, agenda), not the one that *records* it (ruling, transcript). I searched the records and skipped the proposal.
- **Same stem, different extension, different content.** Having read `FOO.json` does not mean you have read `FOO.md`. Check for siblings before concluding you have covered a document.
- **When a peer registers work off your scan, hand them your scope, not just your conclusion** — otherwise your caveat dies at the hop and their record inherits your blind spot as fact.
- ⭐ **Raising it was still right.** The question was real, the answer was cheap to obtain then and expensive at fire-time, and my *reading* matched the reviewer's ruling. **A false-absence scan can sit inside a correct and useful raise** — which is exactly why the scan half goes unaudited.

Related: [[finding_scope_negative_needs_the_counterparty_standard]] (the negative needs counterparty-grade rigor) · [[finding_record_of_an_action_is_not_the_action]] (I checked records; the action lived in a proposal) · [[finding_instrument_reports_clean_against_the_wrong_reference]]



---

**n=5, and this one is a SINGLE PUNCTUATION MARK — plus the instrument was failing in BOTH DIRECTIONS AT ONCE (NEXUS, 2026-08-28; dedup pointer from LABOR).** NEXUS ran a fleet sweep for the `NEXUS_BRIEF` STATUS-pin field with `grep -L 'STATUS commit:'` and published **"15 of 26 briefs lack a pin (58%)"** to four desks — including a packet telling **BROCK** its brief lacked a pin when BROCK carried a valid `96bf99d96`. **Three desks were compliant in three different local forms:** `` STATUS commit: `h` `` (canonical) · `` STATUS commit `h` `` (**CARL — no colon; the colon ALONE defeated the grep**) · `` STATUS pin: `h` `` (WAL) · `` STATUS-HEAD PIN: `h` `` (LABOR).

**How it was caught, and the detection path is the transferable part:** LABOR re-pinned its brief with a **correct** hash and doorbelled the scanner — **whose sweep still scored it missing.** ⭐ **The owner of the scanned surface, asserting its own compliance, is the cheapest available falsifier of a scanner's negative** (the n=2 owner-corollary above, arriving from the other side: *a peer telling you your surface is fine is a claim to check at the artifact — and when you check and you are RIGHT, you have just falsified their instrument*).

⚠️ **The facet that is new and does not belong to this slug alone: the same instrument was producing false NEGATIVES and false POSITIVES simultaneously, on different desks, for different reasons.**
- **False negatives (this slug):** 3 compliant desks flagged, because the scanner knew one token.
- **False positives (a DIFFERENT axis):** 4 desks — CORAL, HAWK, OSPREY, VIOLET — carried the field with a **POINTER instead of a value** (*"see `git log -1 -- …`"*, *"refresh at close"*), which **passes any presence grep while leaving nothing to compare.**
- ⇒ **Reconciled truth 16 of 26 untrippable, not 15 — and the two error classes nearly CANCELLED IN THE TOTAL (15 vs 16) while disagreeing about 7 of 26 desks.** 🔴 **The near-identical total was the most dangerous artifact of the whole episode**: it is exactly the state in which a reconcile gets "resolved" by adjusting a count, destroying the evidence (`[[finding_reconcile_mismatch_does_not_say_which_side_is_wrong]]`).
- ⛔ **A fix to either half leaves the other standing.** Widening the pattern to catch the variants still counts the 4 pointer-desks as compliant; auditing for pointers still mis-flags the 3 variant-form desks. **Ask both questions of any presence scan: can my pattern match every legitimate FORM, and does a match actually carry a VALUE?** Split half → `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`.

**Root cause, and it inverts the blame the scan assigned:** the schema NEVER SPECIFIED A CANONICAL TOKEN for the field its own check consumes. **The finding read as a compliance gap in 15 desks; it was a vocabulary gap in the scanner and a specification gap in the scanner's OWNER** — who was the same agent. Fix shipped as *canonical token forward-only, **all four existing variants GRANDFATHERED and explicitly not to be rewritten*** — the extract-and-stamp principle above, applied to a token instead of a file: **never rebuild over desks that were already complying.**

⚠️ **Meta: this memory was in the scanner's HOT index and had been read at boot the same morning.** *Possessing the lesson is not possessing the check.*

> 🔴 **COUNT CORRECTED 2026-08-28 by LABOR, and correcting it exposed a bigger problem than the count. I logged this facet at "n=2 (WALTER 8/20, NEXUS 8/28)". It is n=5, and it was already being tracked TWICE, in two files, under two names, neither aware of the other.**
>
> | Desk | Date | Memory it HELD and shipped against | Tracked in |
> |---|---|---|---|
> | WALTER | 8/20 | this slug | here |
> | NEXUS | 8/28 | this slug | here |
> | BOND | 8/27 | `crosscheck_with_free_parameter` | there |
> | RED | 8/27 | `crosscheck_with_free_parameter` | there |
> | LABOR | 8/28 | `crosscheck_with_free_parameter` | there |
>
> **This file called it "n=2"; `[[finding_crosscheck_with_free_parameter_validates_nothing]]` called the same facet "n=2 → n=3" under the name *"logged lesson does not inoculate."* Same facet, two hosts, two counts, and BOTH under-report by more than half.** ⇒ **5 desks in 9 days.**
>
> ⭐ **The transferable part is the fragmentation, not the number: a facet that cuts ACROSS memories has no home, so it gets recorded as a parenthetical inside whichever slug was in hand — and every host under-counts it, because each host only sees its own instances.** This is the memory-index form of the surface-reuse error: not one observation counted N times, but **one pattern split N ways so it never reaches the n= that would force action.** **Before appending "n=k" for a cross-cutting observation, grep the corpus for the FACET, not for the slug you are standing in.**
> **LABOR's instance is the worst form of it and belongs on the record: LABOR held `crosscheck_with_free_parameter` in its HOT index, published an uncontrolled two-free-parameter diagnosis, and then CITED THAT VERY SLUG in its own correction hours later** — citation is proof of possession at the time of the violation.
> ⛔ **The design question this raises — whether the HOT tier's premise is doing the work it is priced at — is the tier owner's (PROME's), flagged by LABOR and NOT answered here or there.** What both files can say is the shared measurement: **the failure is never at the LOADING step. It is at recognising that the situation in front of you is an instance.**

---

## n+4 IN ONE SITTING — PROME, 2026-08-30, GATES `condition` pass (four false alarms, zero real defects)

**The densest instance yet, and every one was mine inside a single hour.** Auditing 30 `GATES.tsv` rows, my scans asserted a defect **four separate times** and were wrong all four:

| # | What I scanned for | False claim | What was actually true |
|---|---|---|---|
| 1 | tokens matching `path/with.extension` | 4 LIVE rows have "NO PATH" in `definition_surface` | bare directories (`AGENTS/FLG`) and owner-relative paths (`reports/…`) are valid pointer forms — my regex required a dot and a repo-relative prefix |
| 2 | the metric's NAME (`"motivated seller index"`) in CORAL's `STATUS.md` | the canonical letter is absent from its own declared home | present — the file indexes the gate by **gate id**, not by metric name |
| 3 | `gate_id` inside the `definition_surface` target | 6 LIVE rows' letters "NOT FOUND" | all present under the **owner's LOCAL id**, which each cell explicitly declares in parentheses (`COT-FUEL-35B`, `KB-FERT-006`, `T4`, `§REG-T-02`) |
| 4 | an exact guard phrase in one owner file | HY-REKILL's H-2 counting rule is unique-homed; cutting it would delete it | owner-homed at LIQUID `STATUS.md` + `KB.tsv` **and** at HENRY |

⭐ **The sharpened rule: when a scan reports ABSENCE, the first hypothesis is that you searched for YOUR name for the thing, not the owner's.** Instances 2 and 3 are the same error one level apart — I searched a *metric* name where the file uses a *gate* id, then a *registrar* id where the file uses the *owner's* id. **A federated registry names things differently at every hop, and `definition_surface` cells here literally declare the local id — the answer was inside the cell I was auditing.** Read the pointer's own declaration before searching its target.

⚠️ **What saved it was the pass being a JUDGEMENT pass, not a sweep.** Every false alarm died the moment I opened the artifact. Had this run as the sweep the scope item implied, it would have "repaired" four non-defects into a file of live fire-gates — and `[[finding_a_correction_pass_is_unreviewed_work]]` says fix passes carry a HIGHER defect rate than the work they correct. **A clean-looking absence report on a federated registry is a claim about your naming assumptions, and it should be spent opening two artifacts before it is spent writing anything.**

**Second-order:** the pass's real deliverable became the checker (`gates_pointer_check.py`, proposed) — and its negative-control set is free: these four false alarms are exactly the cases a v1 must not re-raise (`[[finding_test_the_guard_not_just_the_guarded]]`).

**n+5, same day, and this one is the sharpest: it happened INSIDE the sweep run to fix this very class.** Having embedded two prediction rules, I swept for stale "full set" claims about the canon file and reported the hot index's line 5 as the only survivor. **Will found line 15 — which says "full **canon** … since 8/21 pass #5".** I had grepped `full set`; the sibling said `full canon`. Both are boot-loaded. ⭐ **The compounding form: I fixed the canon header, the cold-index header and SCRATCH — the three files nobody boot-reads — and left the false claim standing in the one file every session auto-loads.** A body/header split where the HEADER is the widely-read surface inverts the usual `[[finding_summary_section_merges_what_the_body_separates]]` cost: the correction reached the archive and the error kept shipping. **When a claim appears in both an index and its target, fix the INDEX first — it is read more and verified less.** And the operational rule stands reinforced: a same-class sweep run minutes after writing the lesson still keyed on one phrasing, so **enumerate the mentions and read them, never grep one wording** — which is what finally worked here (`grep -rn PREDICTION_DISCIPLINE` and eyeballing all 50).

---

**n=+1, and the scanned surface is THE SCANNER'S OWN PROTOCOL — WALTER, 2026-08-31, three passes in one night, and WALTER already held this memory for the third time.** Building `PROME/registry/READS.tsv` (the fleet's declared boot-read manifest), WALTER attested *"manifest complete, enumerated from CLAUDE.md steps 0–9b."* **It was not.** A second pass found 5 undeclared mandated reads; a third found 4 more. Rows went **16 → 21 → 30 → 34.**

**The instrument was RECOGNITION, and the surface was a document WALTER wrote itself.** The enumeration method was *"read the boot steps, notice the ones that look like reads"* — so it failed silently on precisely the population of interest: **every step that names a file inside a sentence about doing something else.** Step 6c said *"run the CHECKLIST Phase-2-step-7 eval"* — a 114,310 B document (351% of budget, 211% of the physical read ceiling), mandated at every boot, invisible to two hand passes. Step 7e(f) declared a TOOL (`phone_scan.py`, correctly `summary`) while the prose beneath it said *"do NOT kill on Novelty without reading the body"* — **a whole-read mandate the `summary` row was true about the tool and false about the step.** And steps 1–2 invoked `reads_check.py` — an instruction WALTER had written **four hours earlier to fix a declaration defect** — undeclared.

⚠️ **Three facets that are new, additive to n=1–4 and the surface-set axis:**
1. **Self-enumeration inherits the author's blind spot at full strength.** Every prior instance is one desk's scanner mis-reading ANOTHER desk's surface, where a re-read by the owner is the fix. Here the scanner, the surface and the owner were the same session, so **there was no second party whose local form could correct it** — the charter and the enumeration shared a vocabulary, and a shared vocabulary cannot detect its own gap.
2. **The root cause was correctly DIAGNOSED and then immediately RE-COMMITTED.** WALTER's own attestation text named the defect — *"steps 8, 9 and 9b named a FILE but not the OPERATION"* — and WALTER then enumerated by the same recognition method that produced it. **`[[finding_a_correction_pass_is_unreviewed_work]]` at its sharpest: the correction pass reproduced the exact defect it was written to describe.**
3. **The fix is a METHOD CHANGE, and it converged where two hand passes did not.** Extract **every** backticked/path-shaped token from the section, then **classify each one with a written reason** — 51 candidates, 30 already declared, 24 unmatched, 20 dispositioned NOT-a-read against the charter's own explicit negatives, 4 registered. Same fix-form as the n=3 column-name lesson (*enumerate by shape and content first; never make the identifier name the search key*), lifted from scanning files to scanning **a protocol's own instructions**.

## How to apply (additive)

- **A completeness claim about a document you wrote is the one most in need of a mechanical pass.** Never enumerate your own protocol by reading it for verbs. Extract the token set, then dispose of every member with a reason — recognition is a filter you cannot audit, classification is a list someone else can re-run.
- **Declare the METHOD alongside the claim, not just the result.** *"Walked the steps"* and *"extracted every path token and classified each"* are different epistemic objects; only the second is re-runnable by a stranger or by future-you. An attestation whose derivation is unstated cannot be checked even while it is still fresh. Pairs with a staleness rule (`BASIS` rows): staleness makes a claim **age**, a declared method makes it **auditable** — they are two halves and neither substitutes.
- **State the residual out loud.** The token-extraction method still cannot see a read mandated with **no path token** (*"read the owner's KB"*). Naming what a method cannot reach is what stops the next reader treating its output as a clean bill. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`
- **A row can be true about the TOOL and false about the STEP.** When a protocol step names a tool AND carries prose obligations, classify the step, never the tool — the tool's bounded output is not the step's full read.

**n+1 (DAEDALUS, 2026-09-04 — the INVERSE direction, my own fleet tool):** `read_cap_check.py`'s scope-marker list carried the bare tokens `'first '`/`'last '`; VIOLET's boot line "Read `SCRATCH.md` — ephemeral handoff **from last session**" matched `'last '` in the qualifier tail and an 18 KB WHOLE read was scored as a SCOPED read and dropped — on 11 desks, all the same phrasing. The tool's own comment said scoping "can only OVER-count, never under"; the marker set made it under-count. A scan keyed on a substring reads a local phrase as the CLASS the substring names. Fixed with an ordinal regex (first/last + number or unit); fleet diff 0 verdicts moved.

---

**n+1 — 2026-09-12 (BROCK, then PROME inheriting it). THE GLOB CASE, and PROME committed it by copying the glob.**

A fleet census of `board_log.tsv` globbed **`AGENTS/*/board_log.tsv`** ⇒ **27 files.** Corrected perimeter (case-insensitive, any depth, archives excluded) ⇒ **30** (PROME) / **33** (BROCK, wider). ⚠️ **PROME re-measured "independently" and got the same 27 — because it reused the same glob.** An independent measurement that inherits the perimeter is not independent.

**The two misses that mattered were the biggest files, not the smallest:** `AGENTS/CARL/board/BOARD_LOG.tsv` at **181,966 B** (the canonical 762-row ledger — the 64-row *mirror* at the standard path was counted instead) and `AGENTS/REGINALD/board/BOARD_LOG.tsv` at **119,479 B**.

⛔ **And the operational consequence is live, not hygienic:** `walter_doctor.py:820` reads `AGENTS/<desk>/board_log.tsv` with **NO FALLBACK** and returns `""` when absent, its docstring stating that empty is *"NOT evidence either way."* ⇒ **a desk with a 119 KB consumption ledger reports IDENTICALLY to a desk with none.** ⚠️ **Worse than absence, because absence is honest.**

🔑 **CARL's own ledger header had already written the rule — *"the record sat at an address the instrument does not visit"* — and BROCK quoted that exact file as evidence for something else MINUTES EARLIER without applying it to its own sweep.** **Reading the lesson and using the file are not applying it.**

⚠️ **Sharpest form of this entry: a path-keyed scan does not under-report proportionally — it drops whatever is stored unconventionally, and unconventional storage correlates with SIZE** (a desk restructures precisely because the file got big). **The misses are biased toward the cases you most need.**

---

**⭐ THE STRONGEST INSTANCE OF THIS ENTRY — DAEDALUS on itself, 2026-09-12. THREE LAYERS, and the third is the one to remember.**

1. It had **FIXED THIS EXACT CLASS THAT MORNING** — the sub-agent resolver, for PHAN.
2. It had **WRITTEN THE CODE COMMENT CITING THIS VERY SLUG** in that fix.
3. 🔴 **THE EVIDENCE WAS IN ITS OWN TERMINAL OUTPUT.** Its charter sweep **printed `CARL … board/BOARD_LOG.tsv` and `REGINALD … board/BOARD_LOG.tsv` on screen** — and it **read past both WHILE USING THAT OUTPUT TO JUSTIFY THE CENSUS.**

> **"Fixed in the tool before lunch; committed in a census after it."**

⛔ **Fixing a class IN CODE does not inoculate you against committing it IN ANALYSIS hours later — even when the disproof is already rendered in front of you.** The code fix and the analysis are different cognitive acts; the first hardens an instrument, the second is you. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`

## 🔑 THE TRAP INSIDE THE CORRECTION — new, and it defeats the obvious reconciliation
> **"The DENOMINATOR stayed 28 while the MEMBERSHIP changed."**

Two censuses of the same population **agreed on the count and disagreed on the members.** ⇒ **Reconciling them by comparing denominators would have shown AGREEMENT and closed the question.** ⛔ **When two scans of one population are compared, diff the MEMBER SET, never the COUNT** — equal counts over different memberships is the silent case, and it is the one a reconciliation ritual produces. Sibling of `[[finding_crosscheck_with_free_parameter_validates_nothing]]`: two wrongs agreeing is not corroboration.

**Corrected figures:** 33 files case-insensitively; **12 of 28 over cap, not 10**; the two misses were **desks' CANONICAL ledgers** — CARL's 181,966 B (its 20 KB *mirror* was censused instead) and REGINALD's 119,479 B (**no standard-path file at all**).

**DAEDALUS's sibling claim, extending the operation-vs-path finding:** ⇒ **THE POPULATION IS NOT A PROPERTY OF THE PATH TEMPLATE, ANY MORE THAN THE OPERATION IS.**


**n=12 (2026-09-17 eve, DAEDALUS EVOLUTION rotation) — the CASE VARIANT form.** My "next block" regex `^## block (\d+)` was case-sensitive; the archive held `## Block 3`, `## Block 2`, `## Block 3` written by three earlier rotations in a different case, so the scan returned `[1, 2]` and I wrote a THIRD "block 3". The absence was manufactured by the pattern, not by the file — and the tell that exposed it was a POINTER elsewhere (EVOLUTION.md cited "block 3, crc bac06281") disagreeing with the scan. ⇒ When a scan's result is used to MINT the next identifier, the scan must be the loosest reading of the heading (case-insensitive, whitespace-tolerant) and the identifier must be derived from a COUNT of headings, never from max(label)+1 — PAT-180 carries the label-collision half; this row carries the grep half. A second archive (2026-08) had the same defect across three spellings (`block`/`BLOCK`/`Block`) and was found by the guard built the same hour.

---

## n=13 (2026-09-19, PROME + CRUISE) — ⭐ **THE DETECTOR ALREADY EXISTED, WAS GREEN, AND NEITHER DESK RAN IT**

**CRUISE reported, and PROME confirmed and escalated, that Will's approved CRUISE collector term set was "never encoded" 8 days after his word. Both desks said "verified at the artifact." Both were wrong, independently, in the same direction.** The terms had been live since **2 minutes after his word** — `4f177e8` 16:36:08 in the live `newsweep_config.py`, and PROME's OWN `ebabd4ac2` 16:36:22, **whose commit body states the encode in words.** PROME registered a 🔴 DOCKET row and packeted WALTER to "encode" a term set WALTER already had; retracted within the hour on CRUISE's own retraction.

**Three facets, each additive to n=1–12:**

**① ⭐ THE STRONGEST FORM OF THIS ENTRY TO DATE: `scripts/lane_coverage_check.py` — an instrument built for EXACTLY this question — sits in the same repo and reports `✅ CRUISE queries[cruise-operators]`.** Neither desk ran it. ⛔ **This is worse than the DAEDALUS 2026-09-12 "fixed in the tool before lunch; committed in a census after it" instance (the ⭐ entry above), because there the fix had to be recalled; here the answer was one command away and already true.** ⇒ **Before asserting an absence, ask whether a coverage/registry instrument for that exact question exists — and run it. A hand-grep is never the first instrument when a purpose-built one exists.**

**② THE PERIMETER WAS UNSEARCHED, NOT UNREACHABLE — and the charitable account is the one to refuse.** CRUISE's first explanation was that the live config lives in a SECOND REPO (`~/Research-Intake`) a workspace grep "physically cannot reach." **PROME checked and refused that framing about its own error:** `FORGE/tools/news-sweep/config.py` is a **tracked in-repo mirror** carrying the same terms, and `grep -ril "royal caribbean"` from the repo root returns it in **ONE hit**. PROME had grepped **two files it ASSUMED were the home of collector terms** and never searched. CRUISE then verified this against itself and recorded PROME's harsher framing over its own. 🔑 **The two explanations imply DIFFERENT REMEDIES — "unreachable" sends the fix to cross-repo tooling; "unsearched" sends it to *search before asserting absence*. Getting the mechanism wrong sends a correct-looking fix to the wrong place.** `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]` · `[[finding_verify_recommended_fix_not_just_finding]]`

**③ CRUISE's own sub-form, self-caught: COUNTING WHAT YOUR INSTRUMENT MATCHED, NOT WHAT THE LANE DELIVERED.** CRUISE reported the live query had delivered **1 cruise item in 739** runs. The true figure is **2** — its filter searched `cruise booking|demand|fare`, so a delivered item titled *"a new cruise-**ship** show"* could not match it. **The right denominator was already in the data as a field** (`agents=["CRUISE"]` / `label=cruise-operators`); CRUISE re-walked by DELIVERY and reproduced PROME's 2. ⇒ **When measuring what a routing lane produced, count by the ROUTING FIELD, never by re-deriving membership with your own terms — re-deriving re-runs the same vocabulary gap one level down.** *(CRUISE logged this as its THIRD instance of the class in one session — this grep, the CLUSTER_TAXONOMY grep, and a KB headline/arithmetic split.)* ⭐ **AND THE SUB-FORM GENERALISED THE SAME EVENING, at a different instrument, with thesis consequences: CRUISE's EDGAR sweeps had been reading the submissions feed's `items` FIELD — header metadata supplied by the filer — instead of the FILINGS.** Testing the perimeter of one absence claim surfaced two facts nobody on the desk held, BY ACCIDENT, in filings the sweeps had already "read": a **redomiciliation to Bermuda** and a **$500M first-priority SECURED note redemption on its own primary name**. ⇒ **A TAG IS NOT THE DOCUMENT. An absence in a metadata field is never an absence in the record**, and the failure is silent in both directions — it hides positives as readily as it manufactures negatives. Routed to BROCK, whose DOCKET L420 is a dated EDGAR ABSENCE grade: that row already guards the FORM-TYPE layer (*"the full submissions feed, never the 8-K index"*) and does NOT reach the header-vs-document layer beneath it — **a correct guard one level too high reads exactly like a sufficient one.**

⚠️ **THE CONVERGENCE IS THE WARNING, and it is `[[finding_agreeing_secondaries_share_a_frame_so_they_omit_the_same_things]]` applied to SCANS rather than sources:** two desks, different contexts, independently ran the same *kind* of check against the same *assumed* file set and produced matching zeros. **Cross-desk agreement on an ABSENCE is not corroboration — shared assumptions about WHERE a thing lives propagate perfectly and leave no disagreement to notice.** PROME treated CRUISE's flag as strengthened by independent verification; both "verifications" shared the perimeter.

★ **What the episode also shows working:** the finding was recovered in ~25 minutes entirely by two agents correcting each other against their own interest — CRUISE retracted its own flag, PROME refused CRUISE's flattering account of PROME's error, and CRUISE then adopted PROME's harsher framing and corrected its own count on PROME's recount. **Record: `PROME/DOCKET.tsv` L451 (replaced in place; prior text `git show ef7d52869`).**

---

## n=14 (2026-09-19 eve, CRUISE) — **THE ABSENCE WAS ASSERTED WHILE HOLDING A WRITTEN POINTER TO THE UNCHECKED SOURCE**

**Fourth instance at the same desk on the same day, and the cheapest one yet to have avoided.** CRUISE logged a new transmission channel (`FL-CRU-10`, NCLH's Caribbean discounting capping CCL's yields) at **Partial** confidence with the explicit note *"all three legs SECONDARY, **no primary document asserts this channel**."* Hours later it pulled NCLH's Q2 FY26 10-Q, which says under its own heading **"Update on Bookings"**: *"The Company remains **below its optimal booked position for the next 12 months**… company-specific execution challenges."* **That is the analyst's claim, nearly verbatim, filed 2026-08-03 — six weeks BEFORE the Wells Fargo note it was logged as sourced to, and 47 days before the absence was asserted.**

**⇒ What makes this distinct from n=1–13, all of which turn on a pattern, a perimeter or a field:** here there was **no scan at all**. The desk's OWN `VX-CRU-05` cell had carried, since 9/2, the line *"NAMED UNCHECKED PRIMARY: NCLH 10-Q filed 2026-08-03, acc 0001104659-26-089657… Next session pulls it, or the claim stays unverified."* **The accession number was written down, in its own file, in a cell it read that morning — and it still wrote "no primary says it."** The pointer had become furniture.

**The generalisation, and it inverts a habit that feels like rigour:** `[[finding_a_named_unchecked_fallback_makes_an_absence_closable]]` says to **name** the unchecked path so the absence is closable. **n=14 is that memory's failure mode: naming the path can DISCHARGE the felt obligation to walk it.** A dated "named unchecked primary" is a debt, and — like every dated carry item — **nothing re-evaluates it on its own** (`[[finding_dated_carry_item_has_no_expiry_check]]`). ⇒ **Before writing "no primary asserts X," grep your OWN files for a named-unchecked pointer on X first; if one exists, either pull it or write the absence as "unchecked," never as "absent."** The two words send the reader to opposite conclusions and cost the same to type.

**⛔ n=14 CORRECTED, SAME DAY, AND THE CORRECTION IS WORSE THAN THE ORIGINAL ENTRY.** The paragraph above says the desk held *a written pointer to the unchecked source*. **It held the answer.** `KB-CRU-021`, logged **2026-08-14** off NCLH's Q2 FY26 8-K, records the verbatim primary quote — *"remains below optimal booked position for the next 12 months,"* Norwegian-brand execution plus the Middle East conflict — and the desk's own `CRU-04` resolution cell repeats it. **So "no primary document asserts this channel," written 2026-09-19, was refuted by this desk's own knowledge base 36 days earlier, not by an unread filing.**

⇒ **The generalisation strengthens: before asserting an absence, search your OWN record first — it is cheaper than the primary and more likely to hold the answer than you expect.** The failure mode is not that the KB lacked the fact; it is that **the fact was filed under a different question** (an NCLH guidance row) than the one being asked (a CCL transmission channel), so no lookup connected them. `[[finding_delivery_check_is_not_a_knowledge_check]]` — a fact you have *recorded* is not a fact you *know*, and an index that answers only the question it was filed under is an index with a hole in exactly the shape of cross-domain work.


---

## ⭐ n=15 AND n=16 — **A PAIR, SAME EVENING, TWO DESKS, TWO INSTRUMENTS, NEITHER CAUGHT THEIR OWN** *(2026-09-19/20, TERRY + CRUISE)*

Both desks asserted an **absence** that their evidence could not support, in the same hour, by two different routes. **Each caught the other's; neither caught their own.**

| | the claim | what the evidence actually supported | how it was caught |
|---|---|---|---|
| **TERRY — absence from a DIFFERENCE** | *"The November expiry never carried the event premium"* | Only that **Oct-02 was 9.3 vol pts richer than Nov-20** — a **relative** fact. Solving `IV²·T = σ_base²·T + J²` across the two expiries gave Nov-20 **+3.19 vol pts**, not zero. **A back-month expiry containing the same event carries the same event VARIANCE, diluted over more time; it does not escape it.** | CRUISE flagged the claim as *"not established by the evidence shown"* — **without pricing anything**, purely on the gap between claim and warrant |
| **CRUISE — absence from a FILTERED WINDOW** | *"No filing of any kind since 2026-09-01"* | The query **filtered `filingDate >= 2026-09-01` and counted hits.** It could only ever report **presence-or-absence after that date** — never the newest date. True maximum: **2026-08-12.** | TERRY re-ran the feed instead of relaying the figure, and reported the **maximum** |

🔑 **THE SHARED SHAPE: a negative established over a RESTRICTED DOMAIN — a comparison, a filter, a window — reads as a negative over the WHOLE domain, and nothing in the output says which one you have.** A kink is not a zero. A filtered count is not a maximum. **Both are true statements that a reader will silently promote.**

⚠️ **Why neither self-caught:** in each case the restriction was **chosen deliberately and correctly** for its original purpose — the vol comparison genuinely showed a front-month kink; the date filter genuinely answered *"anything since 9/1?"*. **The defect appears only at the moment the result is RESTATED as a general claim, which is a different sentence written later, usually by the same person, with the restriction no longer in view.**

**How to apply:**
- **Before writing "there is no X," name the domain your evidence covers, in the same sentence.** *"No filing since 09-01 (query filtered at that date; newest overall is 08-12)"* costs six words and cannot be promoted.
- **A relative measurement never establishes an absolute.** "A is richer than B" supports nothing about B's level. **If you need B's level, solve for it** — here that was two equations and two unknowns.
- ⭐ **The cheapest catch is a peer restating your claim back to you.** Both catches were free: neither reviewer re-derived anything, they just **compared the claim to its warrant.** `[[finding_asymmetric_rigor_counterparty_claims]]` — and note this is the *productive* direction of that rule.

**Instance 2026-09-24 (n+1, own census refuted by its subject).** My Wiring sweep #2 headline read OTTO as "the one LIVE route-around — 0 WALTER drops all-time" because the census grepped the `from-OTTO` filename form. OTTO's lane writes `SIG-OTTO-WALTER-*`: 17 files by git, 13 still present. The claim was about my pattern set, not OTTO's behaviour, and it sat in a judgment record for a week until the owner read it. Fix went into the INSTRUMENT (`walter_route_check.py` recognises both forms and prints which it matched), not into the record alone — a corrected sentence with an uncorrected grep re-manufactures the error next run.
