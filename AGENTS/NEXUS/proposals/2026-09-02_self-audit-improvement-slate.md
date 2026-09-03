# NEXUS — self-audit improvement slate

**Author:** NEXUS · **Date:** 2026-09-02 (~20:3x–22:xx ET) · **Task:** DOCKET **L206**, PROME commission 2026-08-17, Will-approved *"go ahead with your rec"* 8/17 eve · **Gate:** first session on/after **8/29, deliberately AFTER the 8/28 falsifier grade** (BRANCH C — NO-VERDICT, EARNED, FINAL). **Opened 9/2 — four days late; that lateness is itself item 2.**

**Method:** read the whole tree — **74 tracked files outside `processed/`** (`find AGENTS/NEXUS -type f -name '*.md' -o -name '*.tsv'`), every ledger, every boot surface, the schema NEXUS owns for 26 desks, the brief-health rollup, both inbox lanes. **Every byte figure comes from `PROME/tools/measure.py`** (WQ-140 measurement rule); staleness from **content-derived dates or in-file marks**, never mtime. **Every item below was found by reading, not recalled.**

**Status: PROPOSALS ONLY. Nothing here is executed, no marks moved, no thresholds re-specced — including the SELF items, which are offered for the batch, not self-approved.** Two exceptions are *not* slate items and are executed this session under separate standing authority: the **read-cap split** (item 2's cure — DAEDALUS PR#5's named re-promote condition, root-canon breach) and **WQ-105's four ACTIONs** (PROME-ruled 9/1, Will *"approve all of those with your recs"*). Both are listed in §HEALTHY/EXECUTED so they are not re-audited as open.

**Classification:** **SELF** = inside `AGENTS/NEXUS/`, reversible, no capital, weakens no falsifier, not a data-property question · **WILL** = fails at least one of those · **CROSS** = needs another desk's hand.

**Blind-parallel discipline:** DAEDALUS ran the parallel profile-audit of the same surfaces. Its two `P1-read-cap` packets sat **UNOPENED** in `inbox/` under the 8/28 held-note through the drafting of items 1–11 below; opened only at §DIFF, after this slate's findings were fixed. **Declared contamination, unchanged from the 8/28 briefing:** the packet FILENAMES carry the figures *"3 over budget, 1 over cap"* and a recut to *"2 over budget, 0 over cap"* — an `ls` made that unavoidable. Declaring it rather than claiming a cleanliness this slate does not have.

> **Deliberately NOT re-listed** (already on PROME's ledger or ruled): WQ-105's amendment-12 / schema-CAP ruling · the VULCAN §4.5 line-ceiling referral · the HOMER ordering defect · GATE-NEXUS-SEAT-01 (grades 10/07) · the T-12 re-spec candidate list (pre-named; frozen at the ~9/11 second-C window, item 6 governs how).

---

## THE SLATE — ranked by value

### 1. 🔴 The largest boot surface in this directory has never been measured, because a read-cap perimeter is defined by a VERB and two NEXUS-owned files use different verbs for the same read — SELF (reconcile) + WILL (the consequence) · ~1 session

**Evidence, measured:**

| Surface | Bytes | vs 32,550 B budget | vs 54,250 B cap | Seen by `read_cap_check.py`? |
|---|---:|---:|---:|---|
| `PREDICTIONS_MONITOR.md` | **57,566 B** | **177%** | **106%** | ❌ **NO** |
| `STATUS.md` | 46,471 B | 143% | 86% | ✅ yes — flagged 🟠, graded, demoted on |
| `templates/NEXUS_BRIEF_SCHEMA.md` | 22,909 B | 70% | 42% | ✅ yes |
| `CONFIRMED.md` | 7,216 B | 22% | 13% | ✅ yes |
| `SIGNALS.md` | 6,859 B | 21% | 13% | ✅ yes |

`scripts/read_cap_check.py --agent NEXUS` reports its own perimeter verbatim: *"28 'read' line(s) scanned (0 on-demand/grep + **4 SCOPED-read token(s) excluded by marker**), 4 whole-read file(s) found."* `PREDICTIONS_MONITOR.md` is one of the four exclusions.

**Why it is excluded, and why that is a defect and not a judgment:** two NEXUS-owned sentences describe the same read.
- `CLAUDE.md:33` (BOOT step 3): *"**open** `PREDICTIONS_MONITOR.md`, **scan** for items whose trigger date has passed"* → reads as SCOPED, so the instrument excludes it.
- `CLAUDE.md:235` (WHAT YOU READ table): *"`PREDICTIONS_MONITOR.md` (NEXUS) | Prediction confidence + past-trigger items | **Full at boot (per BOOT step 3)**"* → reads as WHOLE, **and cites the very step that exempts it.**

**What it catches:** the desk spent 8/28 rotating STATUS from 61,022 B to 46,033 B, published the residual as a root-canon breach, escalated it to this slate, and was **demoted L5→L4 over it (item 2)** — while a **larger** file sat beside it, unmeasured, at 106% of the CAP itself. The instrument was not wrong; it read the sentence that exempts. ⭐ **Transferable: a perimeter defined by a verb inherits every ambiguity in how the owner wrote the verb — and the owner is the one party who cannot see the ambiguity, because both sentences read correctly to them.** Class: `[[finding_instrument_reports_clean_against_the_wrong_reference]]`, in its perimeter form.

**Sub-finding, measured, and it is the reason the file grew:** `PREDICTIONS_MONITOR.md` **line 3 is 9,119 B — 15.8% of the file in a single line.** That line carries the current (8/28) pass block **with the prior (8/17) pass block nested inside its own parenthetical**, unclosed. The file's standing accretion rule is *"keep the CURRENT pass + ONE prior inline; archive the rest at each prune."* The rule is being satisfied by **nesting** rather than by two sibling blocks — so at the next prune there is no second block to rotate, and the header only ever grows. (STATUS has the same shape, milder: `STATUS.md` line 3 = 3,895 B, line 8 = 1,889 B.)

**Proposal — SELF leg:** rule which verb is correct (I believe WHOLE is: BOOT step 3 requires resolving *past-trigger* items, which needs the ACTIVE/FORWARD section read in full, not grepped), reconcile the two sentences to one, and re-run the instrument. **WILL leg:** if WHOLE is correct, this desk has **two** over-budget boot surfaces, not one, and the second is bigger — that changes what "cured" means for the L4→L5 re-promote and should be Will's call, not mine, because I am the interested party.

---

### 2. 🔴 The read-cap breach outlived its own escalation date, and the honest disclosure that bought time is what bought the silence — SELF · **CURED THIS SESSION**

**Evidence, quoted:** `STATUS.md:3` (written 8/28): *"a BREACH, carried openly … **Escalated to the 8/29 slate** with a named candidate split; NOT improvised at closeout."* The slate opened **9/2**. DAEDALUS PR#5 (9/1, `inbox/2026-09-01_from-DAEDALUS_PR5-…`) graded it, and its sentence is the finding: *"A breach carried openly with an escalation date is honest, but **the date passed and 'carried openly' became 'carried'**."* Cost, measured: **NEXUS demoted L5 → L4** in `AGENTS/DAEDALUS/upgrades/PRODUCTION_REVIEW_2026-09-01.md` §2. Second cost: DAEDALUS's own packet records *"The DAEDALUS commission #2 blind legs (8/29–31) **slipped on the NEXUS side**"* — my lateness held a second desk's audit.

**What it catches — the general shape, not the instance:** the breach lived in **one header sentence of one file**. NEXUS's boot sweeps a **CATALYST DOCKET** for dated obligations; the cure date was never a docket row, so nothing in this desk's own sequence re-raised it. ⭐ **A declared breach with a named cure date is a dated obligation wearing prose clothing — it is exempt from the one instrument that would have caught it, by format alone.** Sibling: `[[finding_dated_carry_item_has_no_expiry_check]]`, here with the twist that the disclosure *is* what made it feel handled.

**Proposal (SELF, offered not taken):** any NEXUS-declared defect carrying a named cure date gets a **CATALYST DOCKET row on the cure date** at the moment it is declared — same table, same sweep, no new mechanism. The prose sentence stays; the docket row is what makes it expire loudly.

**Executed this session (not a proposal — DAEDALUS's named re-promote condition + root canon):** `STATUS.md` hot/cold split, verbatim moves with crc32, pointers both ways. Before/after in §EXECUTED.

---

### 3. 🔴 The commission's own headline question, answered: the falsifier design worked at grading and failed at discriminating — and the failure is a class — SELF (the rule) + WILL (the fleet leg) · ~30 min to encode

**The graded answer** (`research/2026-08-28_successor_falsifier_RESOLUTION.md` §8):

| Question | Verdict |
|---|---|
| Graded cleanly, no discretion? | ✅ **Yes** — 11 published sessions, zero judgement calls, robust to both readings of "sustained 3" and to the unpublished 8/28 cell |
| Did it **discriminate**? | ❌ **No.** Both operative branches base-rated ~0% *at ruling time*. **C was the only producible outcome.** |
| Did the guard-set catch it? | ❌ **No — and the guard EXISTED and was four sessions old.** It did not travel with the re-spec. |
| Did the adversarial repair help? | ✅ On its own terms (A became honest and harder) ⚠️ **and it silently un-reached B.** |

**The mechanism, measured at primary:** ruling ⑤ repaired branch A's unreachability by **relocating it onto branch B**. Pass B (8/12) base-rated the ORIGINAL branches (**A 0/418 = 0.0% · B 359/418 = 85.9%**) and adopted *reachability base-rating* permanently into the construction set. ADDENDUM 2 then **stripped B of its ratio leg** — and B's reachability lived entirely in that leg. Re-measured 8/28 (n=787 daily, 2023-08-29→2026-08-27): **3-consecutive HY <260 runs = 0 in three years** (one sub-260 day ever, 2025-01-22 at 259; longest run 1 session). **B: 85.9% → 0.0%, as a side effect, four sessions after the check was adopted, and nobody re-ran it.**

⭐ **The transferable rule, and it is the slate's best item: a spec amendment inherits the ORIGINAL's construction certificate unless the checks are re-run against the AMENDED words.** The re-spec was audited for goalpost-moving (it passed, correctly) and never for reachability (which decided the outcome). **Three parties touched ruling ⑤ — RED proposed it against its own interest, PROME routed it, Will adopted it — and re-running the construction set was nobody's named job.**

**Proposal — SELF leg:** add a **re-run-on-amendment** step to NEXUS's falsifier construction set: any amendment to a frozen falsifier's *letter* re-runs the **full** set against the amended text — reachability base-rate · symmetric magnitudes · numeric NO-VERDICT edges · non-renewable clause · the repeated-no-move note — and **the amendment is not encoded until the re-run is written into the record.** Owner = the encoder (me), because the encoder is the last hand on the text and the only one who sees the final words.
**WILL leg (this is the part I should not rule):** should the same bind fleet-wide when a Will ruling amends **any** desk's frozen spec? It would put a checkable obligation on the ruling pipeline itself, which is PROME's rail, not mine.

---

### 4. 🔴 Three desks have converged on one number, Disc-H correctly counted it once, and counting once is the only thing Disc-H can do — SELF (the instrument) + WILL (the consequence) · ~1 session

**Evidence, measured:** **`HY <260 sustained-3` is simultaneously** my branch B · RED's replacement thesis-kill `RED-FT-12` (registered 8/27, `IMMEDIATE-FALSIFY`) · **and** HENRY's kill leg. One FRED series, one threshold, one persistence rule, **three desks**. Base rate **0 of 787 sessions in three years.** At 8/27 it sat **3bp from the line**; LIQUID's 9/1 watcher has it **moving away** (see §BOARD DELTAS). Disc-H fired correctly and the board says so: *"Three desks, one number — that is concentration risk in the measurement apparatus, not convergence in the evidence."*

**What it catches — and it is the honest limit of my own discipline:** **Disc-H changes the COUNT and has no ACTION.** Having correctly refused to count one instrument three times, the board had nothing further to do, and the fact that the fleet's three most load-bearing credit kill-lines are the *same* line went into a sentence rather than into an instrument. A fourth desk adopting it tomorrow would produce the identical sentence. And the same board carries a **4-desk convergence of registered triggers that cannot fire** (`STATUS.md:13`): my branch B (0/787) · the brief-pin gap (16 of 26 untrippable) · REGINALD's re-arm (0 hits in a 20-session run) · WALTER's CRMT covenant watch (redaction + publication lag). **That convergence passes the independence test — four genuinely different roots — which makes it a property of the fleet, not of one desk.**

**Proposal — SELF leg:** the THRESHOLD PROXIMITY table gains an **instrument-concentration** count: for each registered trigger, how many distinct desks key a trigger to the same series+threshold+persistence. Cheap; it is a read of surfaces I already read.
**WILL leg:** when that count reaches 3, should it **force** one of the three to re-spec, and who chooses which? I am one of the three and must not be the chooser. **This is the fleet-effective-N question in its sharpest form: C3 puts break-relevant roots at ~4, and if three of the fleet's credit kill-lines are one line, the credit root is instrumented by a single number.**

---

### 5. 🔴 My own Discipline I caught this class in July, I wrote the rule, and I shipped the failure anyway — on five surfaces — SELF · ~20 min to repair, and the repair is not the point

**Evidence:** `STATUS.md` carries **"Kharg 1.5M bpd offline is a real blockade fact"** (and cognates) in **9 places across 5 sections** — the split rationale (line 8), M-06, root R2, T-01, T-20, the threshold table, and the narrative gap both sides. WALTER's `SIG-W-20260831-001` (conf 0.95, `CORRECTED-FRAMING`) establishes: Kharg exports ran **1.98m bpd (Feb) → ~135k bpd (Aug)** off the **mid-July** blockade — **and loading RESUMED 2026-08-12.**

**What it catches:** the underlying claim is not false; **its STATE is.** Discipline I, in my own words, says: *"An EVENT has a date; a STATE (an FM, a ban, a closure) has a DURATION and needs a **lifted-check**, not a memory of the start date."* I wrote that rule on 7/31 after the "zero confirmed barrels offline" propagation, and then carried a **blockade** — the archetypal STATE — for 21 days with no lifted-check, on the board with the highest fan-out in the fleet. ⚠️ **And the resumption pre-dates my last pass:** loading resumed 8/12; my 8/28 pass re-wrote the M-06 row and did not re-check it.

**The second half, and it is worse than the first:** the same window produced the **Kharg strike that never happened** — three desks reached off **one AI-generated video** posted by the President (Reuters AI-detection; WALTER's new `AI-GENERATED STATE-ACTOR ARTEFACT` guard). Provenance-tracing **inverts** here: the originator is primary and the artefact is synthetic. My board never carried the strike — that is WALTER's catch, not mine — but it carried the **stale state** the strike story was grafted onto, which is what made the graft look plausible.

**Proposal (SELF):** every STATUS cell asserting a **STATE** (a closure, a blockade, a force majeure, a freeze, a suspension, a moratorium) carries a **`lifted-check: <date>`** stamp beside its start date, and an un-refreshed lifted-check ages the cell the way the Δ-column ages a row. **Not a new discipline — Disc-I already says this. What is missing is a place on the surface for the answer to live**, which is why the rule executed as a memory instead of as a check. ⭐ **A discipline with no field on the surface it governs is a discipline that runs only when remembered.**

---

### 6. 🟠 Disc-J is half-satisfied on the number this desk publishes most, and I can now name which half — SELF (measure) + WILL (the demotion) · ~30 min

**Evidence:** the split has a **registered** falsifier (Disc-J's letter is met) that **grades** cleanly and **discriminates not at all** (item 3). Measured history of the number: **Unresolved has sat 38 / 38 / 38 / 35 / 35 / 35 across six consecutive marks**; Break 21 / Grind 44 held at the 8/28 grade; **this is the 2nd consecutive NO-VERDICT** and the non-renewable clause is **ARMED, C #1 of 2**. Holding was what the letter instructed — but Disc-J's own construction requirements name *"an explicit note of what a **repeated no-move** would mean, since holding the same number twice under a branch that should have moved it is a self-protection tell."*

**What it catches:** Disc-J was written to stop a probability being carried on rationale alone. It succeeded — and then a falsifier that *cannot fire* satisfied it, because Disc-J's construction list requires symmetric magnitudes, numeric NO-VERDICT edges and a non-renewable clause, **and does not require reachability.** The instrument that would have caught it (base-rating) existed in the construction set and was never wired into the discipline text.

**Proposal — SELF leg:** Disc-J's construction requirements gain a fifth: **reachability base-rate, at registration AND at every amendment** (item 3's rule, promoted from the falsifier record into the discipline that governs the number).
**WILL leg, and I want this ruled against me rather than by me:** when a standing probability's current falsifier has **both** operative branches base-rating below some floor (5%? 10%?), should the STATUS split line be required to say **"this number is currently un-falsifiable"** in the file — Disc-J's own *"the number is a mood, not an estimate"* clause, applied to NEXUS's headline output? It would be a self-declared demotion of the desk's most-consumed figure, which is exactly why it should not be a SELF call.

---

### 7. 🟠 The instrument NEXUS owns for 26 desks was blind to 62% of its population for three rollups; the retraction shipped, the FIX has not been designed — CROSS + WILL · ~1 session

**Evidence** (`brief_health.md` rollup #4, 8/28, self-published): §4.4 **trigger (a)** — which `CLAUDE.md` BOOT step 6 calls *"mechanical / always fires"* — compares the brief header's STATUS commit hash to that desk's STATUS HEAD.

| Class | n | Desks |
|---|---:|---|
| **A** — pin present, resolvable hash | **10** | BROCK · CARL · FALCON · LABOR · MARCO · ORACLE · OTTO · SAM · VULCAN · WAL |
| **B** — no pin field at all | **12** | AEOLUS · BOND · BRENT · HENRY · HOMER · LIQUID · MIDAS · RED · REGINALD · SHADE · WATT · ZHAO |
| 🔴 **C** — field present, value a pointer/promise | **4** | CORAL · HAWK · OSPREY · VIOLET |

⇒ **executable on 10 of 26 = 38%; untrippable on 16 of 26 = 62%.** Rollups #1–#3 each concluded *"zero brief-gap defects fleet-wide — the standard is working."* **Retracted 8/28.** ⚠️ *What is NOT retracted:* detection was never zero — `BRIEFS_MAP` flagged desks CONTENT-STALE repeatedly (VULCAN 7/17, 7/31, 8/3) via **commit-date drift**, a second, undocumented mechanism. **But a redundancy nobody registered is not a control**, and the documented mechanism was not the one running.

**What it catches:** amendment 11 (`pin-follows-STATUS-HEAD`, NEXUS self-ruled 8/07) already *imposes* the invariant. What 16 desks lack is **the field** — so the invariant is unenforceable on 62% of the fleet while reading as ratified. The retraction is published; **nothing has been proposed that would move a single desk from class B to class A.**

**Why CROSS + WILL, and the constraint is on the record in my own file:** the fix touches **16 files outside `AGENTS/NEXUS/`**. Amendment 11's own self-ruling recorded the boundary verbatim: *"if amendment 11 were ever propagated as 'every agent adds a step to its closeout doc', it would change ~26 files outside this directory and **test 1 would FAIL**."* **Proposal:** one packet to all 16 desks specifying the exact header field and its value, sent as a **schema requirement** (which NEXUS owns of record) rather than as a closeout-step edit (which it does not) — **routed through PROME, batched, not 16 conversations.**

---

### 8. 🟠 At n=26 this desk built three detectors, got three answers, and a definition plus a two-minute read settled it — SELF · ~10 min to encode

**Evidence:** the pin question above. Three successive detectors were built against 26 files; **the third repeated the first's error one level up** (matching a *mention* of pinning as a *field*). NEXUS published **15/26, all "absent"** off a single string grep; **LABOR's correct pin scored as missing exposed it within the hour**; reconciled to **16/26 in three classes** and the claim was withdrawn inside thirty minutes. The settled figures came from a **definition** (A/B/C, above) and reading 26 headers.

**What it catches:** the automation was not slow — it was *unfalsifiable at the scale it ran*. A detector over 26 items produces a number nobody can eyeball, so a wrong number survives until an outsider's counter-example lands. **Where else is this desk automating a population small enough to read?** Checked, three places: the **26-brief census** (`BRIEFS_MAP`) — its own rule already says re-verify on disk each pass, correct, and it verified correct tonight (26/26); the **fleet-freshness scan** (a `git log` per file — a read, not a detector); the **26-brief line/byte measurements** — a read. **One of three is the risk, and its own rule already governs it. The class is closed here, not open.**

**Proposal (SELF):** encode the standing rule in `CLAUDE.md` beside the disciplines: **at n ≤ ~30 with a contested definition, settle the DEFINITION and READ — do not write a detector.** ⭐ *A detector is a claim about the definition, and at small n it is the more expensive way to be wrong, because the number it produces cannot be eyeballed.*

---

### 9. 🟠 A correction to a signal this board already consumed has no route back onto the board — SELF · ~20 min

**Evidence, two live instances from one window, both found by other desks and neither by any NEXUS mechanism:**
1. **DEWEY 9/2** (`REQ-DEWEY-20260829-001`): `SIG-W-20260828-045` attributes to NVDA's 10-Q the phrase *"primarily related to the procurement of memory."* DEWEY checked 10-Q (acc `0001045810-26-000075`), 8-K CFO commentary and press release (acc `0001045810-26-000073`) — **VERIFIED absence**; the filing says *"primarily memory **and manufacturing facilities**."* The paraphrase entered via secondary coverage **carrying a `[PRIMARY]` tag.** ⇒ the memory-only read of the **$119B → $279B** jump does not survive. And `SIG-W-20260828-034`'s Bernstein turbine survey (**75%**) is **SEARCH-NOT-FOUND** across 11 formulations — *"one verified arrival and one unreached claim; the convergence is materially weaker than it appeared."*
2. **WALTER 8/31**: the Kharg state, item 5.

**What it catches:** `board_log.tsv` records a disposition (`acted`/`noted`/`deferred`/`info-only`/`skipped`) at the moment of consumption and **has no state for "the signal I consumed was later corrected."** Disc-G (relayed-premise decomposition) binds **at intake** — by design, *"the cheapest place to kill a weld is before it enters the file"* — which is right, and leaves the post-intake correction with no owner. ⭐ **`[[finding_claim_outlives_its_discredited_instrument]]`, in its board form: the disposition is a permanent record of a judgment made against evidence that has since moved.**

**Proposal (SELF):** `board_log.tsv` gains a **`corrected`** disposition and a re-check obligation — when a correction lands on a signal already logged `acted`/`noted`, the original row is annotated with the correcting signal's id and the board cells it fed are named. Costs one column and one closeout question: *"did anything I consumed get corrected since?"*

---

### 10. 🟡 `CLAUDE.md` at 50,948 B is the biggest thing this desk loads every boot, and it is outside the read-cap perimeter by construction — WILL / CROSS (DAEDALUS owns READ_CAP) · flagging, not proposing a cut

**Evidence, measured fleet-wide:** `AGENTS/NEXUS/CLAUDE.md` = **50,948 B / 342 lines** — 4th-largest agent `CLAUDE.md` in the fleet (VULCAN 56,323 · LABOR 54,544 · WALTER 53,960 · **NEXUS 50,948** · HOMER 49,282). **It is larger than the `STATUS.md` this desk was demoted over.** It is auto-injected by the harness, not read by a boot *step*, so `read_cap_check.py` cannot see it, and root canon's wording — *"any surface a **boot protocol tells a session to READ WHOLE**"* — arguably does not reach an auto-load.

**Why I am flagging and not proposing:** this file is the **sole carrier** of ten synthesis disciplines under NEXUS's own spec-text rule (*inline-first, tag-as-provenance* — a rule living only in a `[[memory]]` tag goes dead on any machine where that memory is not loaded). **Cutting it trades one canon for another, and the trade is not mine to price.** Note also that this is a **fleet-shaped** number, not a NEXUS one: five desks are within 6 KB of each other at the top, which suggests a common cause rather than five independent hygiene failures.

**Question for Will / DAEDALUS:** are auto-injected agent `CLAUDE.md` files inside the read-cap perimeter? If yes, what is the sanctioned split for a file whose entire design premise is that the rules must be inline?

---

### 11. 🟡 Retirement backlog and one dead-shape surface — SELF · ~20 min total

**Evidence, measured** (age from git commit date; "refs" = live-doc references outside `archive/`, excluding the file itself):

| File | Age | Live refs | Retirement-eligible? |
|---|---:|---:|---|
| `recon/2026-06-06_self_audit.md` | 88 d | **0** | ✅ yes |
| `research/2026-06-06_e_phase_outputs.md` | 86 d | **0** | ✅ yes |
| `research/2026-06-17_fomc_pre_registration.md` | 78 d | **0** | ✅ yes |
| `recon/2026-06-06_e_phase_pre_registration.md` | 88 d | 1 | ⚠️ check the referrer's liveness |
| `recon/2026-06-06_c_id_index.md` | 88 d | 1 | ⚠️ same |
| `research/2026-06-08_cpi_pre_registration.md` | 86 d | 1 | ⚠️ same |
| `research/2026-07-10_correlation-collapse-map_packetA.md` | 48 d | 0 | ❌ not yet 60 d |
| `research/2026-08-03_split_and_coverage_prereg.md` | 30 d | 2 | ❌ live (Disc-J worked example) |

**Scope note, applying root canon's own two clauses honestly:** clause ② says an index/nav reference does **not** count as "referenced by a live doc." The three ⚠️ rows each have exactly one referrer and I did **not** verify whether that referrer is analytical or navigational — **so they are listed as unresolved, not as eligible.** Only the three `refs=0` rows are clean. **Nothing moved this session** (proposals-only, and a retirement sweep at the tail of a long session is the pattern the 8/28 briefing correctly refused).

**Also in this bundle:** `outbox/` — top level is empty, `delivered/` holds 9 files, newest **2026-07-22**. That is **empty-by-design and healthy** (carve-out ① practice since ~7/23), confirmed rather than assumed. No action.

---

## Cross-cutting observation — the reason six of these rhyme

**Six of the eleven items are the same shape: a check that exists, is correct, is loaded, and does not RUN — because nothing in the executing sequence calls it.**

| # | The check that existed | Why it did not run |
|---|---|---|
| 1 | `read_cap_check.py` | its perimeter is a verb, and the owner wrote two verbs |
| 2 | the CATALYST DOCKET sweep | the cure date was prose, not a row |
| 3 | reachability base-rating (adopted, 4 sessions old) | nothing re-ran it against the amended text |
| 5 | **Discipline I's lifted-check** (my own rule, written 7/31) | no field on the surface for the answer to live in |
| 6 | Disc-J's construction list | complete, and missing the one requirement that mattered |
| 7 | §4.4 trigger (a), *"mechanical / always fires"* | 16 of 26 desks have no field for it to read |

**This is not a knowledge gap and never was.** In every case the desk held the correct rule, in writing, at the time. ⭐ **The generalisable ask for Will: NEXUS's failures are overwhelmingly INVOCATION failures, not judgment failures — should this desk's improvement work stop producing new disciplines (there are ten; A–J) and start producing FIELDS and ROWS, i.e. places on the executing surfaces where an existing rule's answer is forced to appear?** Items 2, 4, 5 and 9 are all one field or one column each. That is the same fix the July memory-index repair used and the same conclusion closeout step 9b reached in August — *"put the existing knowledge into the sequence that actually executes"* — which suggests the pattern is now at n≥3 on this desk and should be ruled once rather than patched four times.

⚠️ **Stated against myself:** an owner whose every finding turns out to be "my rules are right, they just don't run" has produced a flattering diagnosis. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`. **The falsifier for it is item 3 and item 6, which are judgment failures in the construction set, not invocation failures — I did not have the right rule, I had an incomplete one.** So the pattern is real but not total: **2 of 11 are judgment, 6 of 11 are invocation, 3 are structural/scope.** I would not have found the split by looking for it; it fell out of the count.

---

## ✅ CHECKED AND FOUND HEALTHY — recorded so nobody re-audits it

1. **Fleet brief coverage: 26/26 on disk** (`ls AGENTS/*/NEXUS_BRIEF.md | wc -l` = 26), matching `BRIEFS_MAP`'s census. **Freshness is healthy and improving: 11 of 26 refreshed within the last 2 days** (BRENT · CARL · HAWK · LABOR · MIDAS · REGINALD · SAM · ZHAO on 9/2; BOND · FALCON 9/1; HOMER 8/31); oldest is WATT at 8/17. The 8/28 "BROCK is the fleet's stalest at 8/03" finding is **closed** — BROCK refreshed 8/28 in direct response.
2. **`templates/NEXUS_BRIEF_SCHEMA.md` cured its own read-cap breach and the cure HELD**: 42,103 B (78% of cap) → **22,909 B (42%)** on 8/28 via §§6–7 hot/cold split, `crc32 3f13bf74`. Re-measured tonight: **22,909 B, unchanged — zero re-accretion in 5 days.** The split is the working exemplar for item 2's cure.
3. **The Δ-column convention is being honoured, verified row by row:** matrix `Last updated` values are **2026-08-07 (M-09) / 08-12 ×5 / 08-17 ×3 / 08-28 (M-08)** — genuinely old dates on un-moved rows, not bumped by the 8/28 no-op review. The column is doing exactly the job it exists for, which is why the board's own staleness is visible at a glance.
4. **`SIGNALS.md` is not a copy of the STATUS matrix** — 2 active rows (S-26082801 phantom-AI-demand; S-26060701 El-Niño), both genuinely unabsorbed, both with a named destination and a stated reason for non-absorption. 6,859 B. The anti-pattern it guards against is not occurring.
5. **`CONFIRMED.md` (7,216 B)** is inside budget and the C-05 fired-legs-only rule adopted 8/03 is holding — no forward leg found parked in a confirmed row this pass.
6. **`outbox/` empty-by-design**, per the 7/28 key-files audit: top level empty, `delivered/` frozen at 7/22, consistent with carve-out ① direct-to-inbox practice. Not rot.
7. **`PROME/inbox/` path discipline:** packets addressed to PROME this session went to `PROME/inbox/` at the **repo root**. No `AGENTS/PROME/` regrowth from this desk. (`[[finding_prome_inbox_is_repo_root_not_under_agents]]` — the tree has re-grown twice fleet-wide since 7/24, so this is checked, not assumed.)
8. **Closeout step 16's cwd-proof wrapper** — independently confirmed resolved by DAEDALUS PR#5 (*"Resolved: closeout step-16 cwd verify (`CLAUDE.md:99`)"*).
9. **The 8/28 STATUS prose rotation was clean:** 7 of 7 identified prose blocks moved verbatim with crc32 to `archive/2026-08-28_STATUS_prose_rotation.md`, zero live-state surfaces touched. Re-verified: the matrix, thresholds, docket, chain, tensions, split and gap in today's file are byte-consistent with that claim. **The 8/28 pass did not fail at rotation; it stopped at the live-state boundary, correctly, and said so.**

## ⚙️ EXECUTED THIS SESSION under separate standing authority — NOT slate items, do not re-adjudicate

| What | Authority | Result |
|---|---|---|
| `STATUS.md` hot/cold split under the 32,550 B budget | root canon §Data Hygiene (Will-approved 8/28) + DAEDALUS PR#5 re-promote condition #1 | **46,471 B → see §EXECUTED figures in `LAST_COMPLETION.md`** |
| Full matrix review dated after 8/28 | DAEDALUS PR#5 re-promote condition #2 | run this session |
| WQ-105 (a) grade the amendment-12 watch **MISSED** · (b) encode amendment 12 · (c) write the schema-amendment **CAP** · (d) release VULCAN's held revert · (e) packet HOMER | PROME 9/1, Will *"approve all of those with your recs"* | all five |

---

## 📊 SUMMARY TABLE

| # | Item | Class | Cost | Catches |
|---|---|---|---|---|
| 1 | 57,566 B boot surface invisible to the read-cap instrument (perimeter defined by a verb) | SELF + **WILL** | ~1 sess | the desk's largest unmeasured surface; a second uncured breach |
| 2 | Breach outlived its own escalation date (cost: L5→L4, + held DAEDALUS's leg) | SELF (**cured**) | done | every future declared-defect-with-a-cure-date |
| 3 | Falsifier graded ✅ / discriminated ❌ — **amendment inherits the original's certificate** | SELF + **WILL** | ~30 min | every re-spec of a frozen instrument, fleet-wide |
| 4 | Three desks, one number — Disc-H counts once and cannot act | SELF + **WILL** | ~1 sess | the credit root instrumented by a single line |
| 5 | Disc-I's lifted-check never ran on a 21-day-old STATE, on 9 board cells | SELF | ~20 min | stale STATES on the fleet's highest fan-out surface |
| 6 | Disc-J satisfied by an unfalsifiable falsifier | SELF + **WILL** | ~30 min | the desk's most-consumed number |
| 7 | Brief-pin instrument blind to 62% of its population; fix undesigned | **CROSS + WILL** | ~1 sess | the standard NEXUS owns for 26 desks |
| 8 | Detector-at-small-n (3 detectors, 3 answers, n=26) | SELF | ~10 min | a wrong number nobody can eyeball |
| 9 | A correction to a consumed signal has no route back onto the board | SELF | ~20 min | 2 live instances this window, both found by other desks |
| 10 | `CLAUDE.md` 50,948 B outside the read-cap perimeter by construction | **WILL/CROSS** | — | a fleet-shaped question, flagged not proposed |
| 11 | Retirement backlog (3 clean, 3 unresolved) + `outbox/` confirmed healthy | SELF | ~20 min | doc rot; nothing moved this session |

**Ranked by value, not by cost.** 🔴 items 1–5 · 🟠 6–9 · 🟡 10–11. **SELF-only: 5, 8, 9, 11 (+2 cured). Needs Will: 1, 3, 4, 6, 10. Needs another desk: 7.**

---

## 🔴 §DIFF — DAEDALUS's blind leg vs NEXUS's own measurement — **THE REPRODUCIBILITY TEST FAILED, AND IT FAILED ON ITEM 1**

*Opened only after items 1–11 were written to disk (`git log` proves the ordering). Per PROME's 8/28 ruling, verbatim in intent: **"if the recut ('3 over → 2 over') says something about the TOOL, that is an 8/29 finding, not contamination."** It does.*

**DAEDALUS's ORIGINAL packet (8/28 13:xx), first row of its table:**

| | file | bytes | % of cap | verdict | found at |
|---|---|---|---|---|---|
| 🔴 | `PREDICTIONS_MONITOR.md` | **57,566** | **106%** | **OVER THE CAP — cannot be read whole** | boot-step line 84 |

**DAEDALUS's CORRECTION (same day, same hour): that row is GONE.** Ground given: *"the instrument scored SCOPED reads as whole reads."* Counts re-cut **3→2 over budget, 1→0 over the cap.** Kill-string ④: *"`3 over budget, 1 over the cap`."*

⇒ **The two blind readers agree on the byte count to the byte (57,566 B) and disagree on whether it counts. And the disagreement is the finding: the correction that "fixed" the instrument is the thing that made this desk's largest surface disappear.** I reached item 1 from the NEXUS side, blind, by reading my own two contradictory sentences; DAEDALUS reached the same file from the instrument side and then removed it. **Neither reader was wrong about the bytes. The tool has no way to represent "the owner's surfaces disagree about the verb."**

**Three things this says about the TOOL, offered to DAEDALUS as P1/R7 input, not as a grade of its work:**

1. ⭐ **The stated bias direction is wrong in this case, and the exception is not rare.** The correction's cause note says: *"the bias is one-directional (**a scoped read can only OVER-count**), so the first tranche's fleet figure was inflated."* That holds **only if the boot verb is ground truth.** The boot verb is not ground truth — it is *a claim by the owner*, and here the same owner's WHAT-YOU-READ table (`CLAUDE.md:235`) makes the opposite claim (*"Full at boot"*) **while citing the very boot step that exempts it.** Where an owner's surfaces disagree, the recut is one-directional in the **opposite** direction: it **under-counts, silently, and the file drops off the report entirely** — which is strictly worse than the over-count it fixed, because an over-count is loud and an omission is not. **The correction traded a loud false-positive for a silent false-negative.** (`[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]` — measured here, not cited by analogy.)
2. ✅ **DAEDALUS's own original packet already named the correct disposition, and the correction discarded it.** Verbatim, from the packet the correction supersedes: *"If a listed file is **not** read whole at boot, the fix is to make the boot step **say what IS read** (a section, a grep, a head) — that is a correct protocol statement, not a workaround; **a whole-read claim on a file this size is the defect either way.**"* NEXUS's table makes exactly that whole-read claim, on exactly that file. **By DAEDALUS's own standard, written by DAEDALUS, before the correction, this is a defect either way — and the correction is what stopped anyone from being asked about it.**
3. **The two readers found it on different lines, which locates the perimeter's real edge.** DAEDALUS found it at *"boot-step line 84"* — which is inside the **CLOSEOUT** block (step 9c/10's *"scan `PREDICTIONS_MONITOR.md`"*), and the correction's fix note says nested non-boot sub-protocol blocks are now skipped. **I found it at `CLAUDE.md:33` (BOOT step 3) and `CLAUDE.md:235` (WHAT YOU READ).** So the original flagged it for a reason that was genuinely wrong (a closeout line is not a boot read) and the correction removed it for a reason that is also wrong (BOOT step 3 is a real boot line, and the table calls it whole). **Two errors, opposite directions, same file, net result zero flags.** ⭐ *A correction pass is unreviewed work* — `[[finding_a_correction_pass_is_unreviewed_work]]`, at n+1, and this instance is the sharper form: the correction was **right about the original's reason** and **wrong about the file**.

**What survives unchanged and is not disputed:** the rule itself (32,550 B per boot-mandated whole read, per surface, owner chooses how, never raise the number) · every surviving row of the corrected table · `STATUS.md` as a genuine breach, which is cured this session. **DAEDALUS's measurement of `STATUS.md` (46,033 B, 85%) and `NEXUS_BRIEF_SCHEMA.md` (42,103 B, 78%) reproduce NEXUS's own 8/28 figures exactly.** The instrument is sound on unambiguous surfaces; the defect is confined to the ambiguous ones, which is where it matters.

**Owed to DAEDALUS (packet sent this session):** this DIFF, so R7-stage-2's `READS.tsv` — which replaces the heuristic with **the owner's declaration** — is designed knowing that **the owner's declaration is exactly what was self-contradictory here.** A declaration file inherits this defect unless it is validated against the desk's *other* read-describing surfaces, not just accepted. That is a design input available only because two readers stayed blind.

---

*Companion artifacts: `BRIEFING_2026-08-29_SYSTEMS_REVIEW.md` (the input pack this slate consumed) · `research/2026-08-28_successor_falsifier_RESOLUTION.md` §8 (item 3's graded answer) · `brief_health.md` rollup #4 (item 7) · `STATUS.md` + `STATUS_COLD.md` (item 2's cure).*
