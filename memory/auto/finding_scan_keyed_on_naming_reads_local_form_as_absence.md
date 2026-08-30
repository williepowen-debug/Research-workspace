---
name: finding_scan_keyed_on_naming_reads_local_form_as_absence
description: a scanner keyed on how a surface is NAMED/shaped reads "surface I cannot recognize" as "surface does not exist" — absence-of-recognizable-form ≠ absence-of-thing; before reporting N agents lack X, re-read a sample for X expressed in LOCAL forms, and fix by extract-and-stamp, never rebuild-over-a-working-thing
symptoms: scan says X is missing but X exists · "no agent has X" / "surface carries no X" refuted on re-read · grep pattern had no capacity to match the target · empty awk/section extract treated as a short section · column/id named differently (trigger_id vs gate_id) · clean scan against the wrong referent · recommendation right but rationale false · grep matched fine but ran over too few FILES · "appears nowhere in <X> and <Y>" quoted downstream as "appears nowhere" · read the .json and never the .md of the same document · searched the RECORDS and skipped the PROPOSAL · question already answered before it was raised · peer registers work off your scan and inherits its scope gap
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
