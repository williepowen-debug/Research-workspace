# BOARD Delivery + Consumption Spec

**Version:** v0.21
**Created:** 2026-04-20 (v0.1 consumption-only) · **Extended:** 2026-06-17 (v0.2 delivery layer) · **Clarified:** 2026-06-18 (v0.3–v0.5 Quick-WALTER tightening) · **Collapsed:** 2026-06-26 (v0.6 single-machine platform-collapse — OpenClaw cut)
**Owner:** WALTER
**Status:** **Single-machine (desktop CC) since 2026-06-26 — OpenClaw cut; `delivered` is uniform (committed + on-origin); Quick-WALTER retired.** Delivery layer SHIPPED; consumption = Phase 2 self-apply (see §8). Approved-in-principle by Will + PROME + ORC (2026-06-17); v0.6 collapse Will-ratified 2026-06-26 (`design/OPENCLAW_CUTOVER_PLAN.md`).

---

## 0. Why v0.2 exists — "in BOARD" ≠ "received"

v0.1 defined a *consumption* mechanism (`board_log.tsv` + a recipient boot-step that scans `/BOARD/INDEX.md`). It shipped, but propagation to agent boot docs stalled ~2 months → BOARD became **write-only**. The prototype failure: **SIG-W-20260610-001 (BRENT action) + -002 (HAWK action) were correctly published to BOARD but delivered to nobody's inbox** — both were BOARD-only per the Apr-14 delivery policy, and the recipients had no working pull. The miss was *structural*, not a one-off: it was true for every IMMEDIATE/PRIORITY signal.

v0.2 adds a real **delivery layer** (a per-recipient handoff file WALTER actively creates) and a **phased-but-time-boxed** consumption rollout, with **telemetry shipping immediately** so the Phase-2 gap can't rot silently the way v0.1's did.

---

## 1. State vocabulary — published / delivered / consumed

Three orthogonal delivery states. **These are distinct from the signal-validity lifecycle** (`status:` = SUPERSEDED / FALSIFIED / EVENT-PASSED, FORMAT_SPEC v0.10) — do **not** overload the `status:` field to carry delivery state. Track delivery via file location + the WALTER-side `delivery_log.tsv`.

| State | Definition |
|-------|-----------|
| **published** | Signal file in `/BOARD/` + a row in `/BOARD/INDEX.md`. (Unchanged from today.) |
| **delivered** | Handoff file is **committed AND on origin** (reachable on the recipient's next pull). Written-but-unpushed is NOT delivered. See §3. |
| **consumed** | Recipient processed it: logged a disposition in its `board_log.tsv` **and** moved the handoff file to `inbox/WALTER/processed/`. |

**Reporting discipline:** never report "routed to AGENT" on *published* alone; never claim *consumed* until recipient-side processing exists. WALTER can assert *published* and *delivered* (the latter via §3's git-derived check); only the recipient can assert *consumed*.

---

## 2. The BOARD stays as-is

BOARD remains the permanent archive + discovery index, **unchanged**. Every route writes a full-but-minimal BOARD entry (signal file + one INDEX row + `route_log.tsv` append). **No stubs** — stubs create reconciliation debt and break `walter_doctor`'s `board_reconcile`. Heavy curation/reconciliation stays with Full WALTER (see §9). The delivery layer is *additive* to BOARD, not a replacement.

---

## 3. Delivery layer — the operational fix

### 3.1 Where
- **WALTER-only folder per recipient:** `AGENTS/{RECIPIENT}/inbox/WALTER/` (create if missing).
- **One file per signal per recipient.** No rolling file.
- **WALTER only ever CREATES files here — never edits an existing one.** The recipient reads, then moves it to `inbox/WALTER/processed/`. WALTER and the recipient never touch the same file → **collision-safe even if the recipient is active** (sidesteps both the shared-`.git/index` race and the rolling-file race; consistent with auto-memory `[[finding_pathspec_commit_race_safety]]` + `[[finding_concurrent_commit_index_race]]`).

### 3.2 Handoff file template (one per signal per recipient)

Filename: `AGENTS/{RECIPIENT}/inbox/WALTER/SIG-W-YYYYMMDD-NNN.md`

```markdown
# SIG-W-YYYYMMDD-NNN — short title
BOARD: /BOARD/SIG-W-YYYYMMDD-NNN-short-slug.md
Priority: IMMEDIATE | PRIORITY | ROUTINE | FLASH
Role: ACTION | INFO
From: WALTER
Date: YYYY-MM-DD
## Kernel
One-paragraph factual summary.
## Why you got this
Specific reason THIS recipient is receiving it.
## Requested action
- ACTION recipient: what to check/update/decide.
- INFO recipient: what to note, if anything.
## Confidence / caveats
Confidence score + verify-research / corrected-framing caveats.
## Cross-refs
Related signals, paired dispatches, thresholds, anchor files.
```

The kernel is a self-contained summary so the recipient can act without round-tripping to BOARD; the `BOARD:` line is the pointer to full detail.

### 3.3 `delivered` — single-machine definition

All agents run as Claude Code sessions on the one shared desktop repo (the OpenClaw/VPS platform was cut 2026-06-26 — see `design/OPENCLAW_CUTOVER_PLAN.md`). `delivered` has **one meaning for every recipient**:

> A handoff file is **delivered** when it is **written, committed, AND pushed/synced to origin** (reachable on the recipient's next pull). **Written-but-unpushed is NOT delivered.**

**Urgent fallback:** FLASH (and IMMEDIATE) while a sync is pending falls back to the existing **FLASH → Telegram/Will alert** path so the signal is never invisible. See §3.4 for the precedence→push handling.

### 3.4 Push handling by precedence

Push is **not** automatic blanket WALTER authority (see §7). The one standing auto-push authorization:

- **FLASH / IMMEDIATE:** WALTER may perform a **clean-tree scoped commit + push via `scripts/safe-push.sh`** (the ff-gated helper) — *only if* there is no unrelated/uncommitted work in the shared tree and no unsafe rebase condition (0g, Will-ratified 2026-06-26). Git pushes **commits, not files**, so this is: *commit only the exact WALTER / BOARD / recipient-handoff paths, verify the tree is clean/safe, `pull --rebase` if behind, push via the ff-gate, never force* — NOT "push specific files." This is the **only** standing auto-push authorization; all other pushes stay Will-coordinated.
- **PRIORITY / ROUTINE:** write + commit locally, mark `written_not_delivered_pending_push`, and surface in `walter_doctor` + closeout until a Will sync window (or the next push-train) pushes it.

---

### 3.5 Pull-complete recipient exemption — skip inbox delivery (added v0.7, 2026-07-04)

> **🔴 §3.5.6 — THE EXEMPTION'S FAILURE MODE HAS NOW MATERIALISED, DISCLOSED BY THE EXEMPT RECIPIENT ITSELF (recorded 2026-08-12; NO BEHAVIOUR CHANGE PROPOSED — this is a RECORD, and the disposition is Will's).**
>
> **What happened.** RED disclosed (`inbox/2026-08-12_from-RED_ft06-exit-defined…`, logged as its own `ML-RED-150`) that on 8/12 it **did not run its boot step 1.5 — the whole-INDEX BOARD scan — which has been RED's SOLE WALTER CHANNEL since the 7/09 pull-complete exemption.** Two signals addressed `action: [RED]` (`SIG-W-20260811-001` IMMEDIATE, `SIG-W-20260810-004` PRIORITY) sat unread while RED closed out, committed and pushed. **RED caught it only because Will asked whether it had processed its inbox, and RED checked its own boot sequence instead of answering from the inbox directory.**
>
> **🔑 THE STRUCTURAL POINT, IN RED'S OWN WORDS, AND IT IS ABOUT THE EXEMPTION AND NOT ABOUT RED:** *"there is no push to remind you, so skipping it is **silent by construction**… **an empty `inbox/` is not evidence the BOARD channel was consumed — different surfaces, and only one of them announces itself.**"*
>
> ⚠️ **This is the exemption's warrant inverted.** §3.5 rests on *"their own complete whole-INDEX BOARD-diff IS the pull."* That is a claim about a **step the recipient runs**, and **the exemption simultaneously removes the only artifact that would show the step was skipped.** For a non-exempt recipient an unconsumed handoff sits visibly in `inbox/WALTER/` and surfaces in `walter_doctor`'s `delivered_but_unconsumed`; **for an exempt recipient there is nothing to be unconsumed, so a skipped scan and a clean scan are INDISTINGUISHABLE on every surface either side keeps.** ⇒ **`delivered_but_unconsumed` reading zero for CARL/RED/PROME is not evidence of consumption; it is a definitional consequence of the exemption.**
>
> **What does NOT change, and why I am not proposing a change:** the exemption was Will-approved on measured evidence (complete-scan tooling + zero action-line appearances), **WALTER's side executed correctly here** — BOARD and `route_log` were written and the mechanism worked as specified — and **the outcome was benign**: RED graded FT-06 independently off the FRED primary and reached the identical answer. **But RED itself named why that is not a defence: *"that is convergence, and it is luck about the CONTENT of the channel I skipped, not evidence the step was unnecessary,"*** and the signal it did not read **also carried an owed action that luck did not cover.**
>
> **⚠️ AND THE PRECEDING SENTENCE IS THE ONE TO CARRY, because the tempting reading of this episode is the wrong one:** a benign outcome on a skipped step is the strongest available argument for skipping it again.
>
> **Options, for Will — recorded, none adopted:** **(a)** leave as-is and treat this as recipient-side discipline (status quo); **(b)** a lightweight self-check on the recipient side — the exempt agent asserts *"BOARD scan run, N new since cursor"* in its own closeout, giving the step an artifact without reintroducing a handoff; **(c)** narrow the exemption to non-ACTION dispatches only, which is already true for PROME (v0.12, info-only) but not for CARL or RED. **⚠️ (b) is the only one that closes the telemetry gap without adding delivery volume — and it is a change to ANOTHER agent's boot protocol, so it is not WALTER's to make.**
>
> *(Filed under §3.5 rather than §3.5.1 because that sub-section scopes what the exemption COVERS; this records what the exemption CANNOT SEE. Sits with `[[finding_verification_zero_is_ambiguous]]` — a zero certifies the check's SCOPE, not the world — and with `[[finding_deferral_rule_hides_its_own_cost]]`.)*


A recipient that runs a **complete BOARD consumption pass** at boot — one that dispositions **every unrecorded `SIG-W` ID** (not a tiered/selective subset), however implemented — already has a **complete pull**. ⚠️ **WARRANT RE-POINT (v0.19, PROME-ruled 2026-08-07 late, executed 2026-08-20): do NOT describe or specify this step as a "whole-INDEX BOARD diff."** `BOARD/INDEX.md` is ~19× any reader's context cap, so a step specified as *reading the whole INDEX* is a step nobody can run as written — **the warrant must cite what the qualifying tooling ACTUALLY does**: `board_scan.py`'s complete parse of every `BOARD/SIG-W-*.md` FILE past a stored cursor (PROME), or a complete grep-diff of INDEX signal-IDs against the recipient's own ledger (CARL/RED). The exemption itself stands unchanged; what changes is that its justification names a runnable mechanism rather than an unrunnable phrase. For such an agent the per-recipient `inbox/WALTER/` handoff is redundant with its own scan (both are fed the same BOARD entry), so **WALTER SKIPS the `inbox/WALTER/` handoff + the `delivery_log` delivery row for it.** The BOARD entry + `route_log` row are still written (the signal is published + audit-logged as normal); only the redundant push-delivery to that agent is skipped.

**Exemption criterion (verify empirically before adding an agent; wording re-pointed v0.19):** the agent's boot doc must run a **complete, ID-level BOARD disposition pass** — a file-parse past a cursor, or an ID-diff of INDEX rows against its ledger, dispositioning every unrecorded ID; the mechanism must be one the agent can actually execute (see the warrant re-point above). **Tiered/selective scans do NOT qualify** — they can skip the cluster an ACTION item lands in. Confirm by the 2026-07-04 CARL reconciliation method: the agent's ACTION handoffs already appear dispositioned in its ledger with **zero un-dispositioned ACTION**.

**Current exemption list:**
- **CARL** — runs a complete whole-INDEX BOARD-diff (`AGENTS/CARL/CLAUDE.md` boot step 5, diffs *all* of INDEX vs `board/BOARD_LOG.tsv`). Verified 2026-07-04: 22/22 ACTION handoffs already dispositioned, 0 misses → WALTER stops writing to `AGENTS/CARL/inbox/WALTER/`.
- **RED** (added 2026-07-09, Will-approved design-walkthrough) — runs a complete whole-INDEX BOARD scan at boot (`AGENTS/RED/CLAUDE.md` step 1.5, RED-scoped consumption pass: reads the cluster ToC + drills into every section). **Stronger case than CARL: RED is auto-cc'd INFO-only (never the ACTION owner)**, so dropping its handoffs carries *zero* ACTION-miss risk by construction. RED was 24% of all delivery-lane volume + the single largest `delivered_but_unconsumed` INFO pile — the per-signal handoff is pure redundancy with its own step-1.5 scan. → WALTER stops writing to `AGENTS/RED/inbox/WALTER/`; RED drains its current backlog normally, then its step-5.5 consume becomes a WALTER no-op (RED may retire it). *(Fixes the 2026-06-23 over-cc finding at the routing source, per `[[feedback...]]` delivery-telemetry calibration.)*
- **PROME** (added 2026-07-27, Will-approved twice — in-session to PROME, then re-confirmed directly to WALTER rather than accepted on relay) — runs a complete whole-INDEX scan via **`PROME/tools/board_scan.py`**, wired into `PROME/BOOT.md` step 6 as an every-boot `--advance` run. It parses the frontmatter of **every** `BOARD/SIG-W-*.md` past a stored cursor (`PROME/state/board_cursor.txt`), splits action-line from info-line, and prints one line per signal with the action owner in brackets. Verified over 7/24→7/27: **45 signals in ~1s on one screen**; idempotent. **Strongest case granted to date — PROME has been on the BOARD `action:` line 0 times out of 605, all-time** (`board_scan.py --audit`), and **the scanner `exit 1`s if that ever changes**, so the zero is *enforced* going forward rather than assumed. **The trade, stated with its cost:** PROME's inbox reached **32 items**, of which **20 were info-copies of signals whose ACTION owner already held its own copy** and 8 were already consumed the same day — its inbox had become a mirror of BOARD, clearable only by reading it (§3.5.2), i.e. ~20 reads/day of duplicates. **The pile is itself a hazard: PROME swept two signals into `processed/` UNREAD and caught it only on a file-count mismatch.** ⚠️ **Cost accepted on the record: reading an info-cc is what caught a measurement error in `SIG-W-20260727-006` on 7/27.** It is accepted because WALTER found the same error independently ~40 minutes later and self-retracted (`-016`) — the catch did not depend on PROME's copy — **but the loss is real and this bullet is the place it is written down.** → WALTER stops writing to `PROME/inbox/` **for dispatches where PROME is info-only.**
- **TERRY** (added 2026-08-26, v0.21 — **BY FALSIFIER, not by pull-complete warrant**): §3.5.5's non-renewable revert falsifier fired (an `action:` correction unconsumed ~78h; TERRY boots ~15 days in 38) and its ratified remedy is the RED-class exemption. **No handoffs, no delivery rows; BOARD + route_log still written.** Known, priced cost: the T-2 retraction class has no TERRY-side re-pull — TERRY reads BOARD/`route_log` at its own cadence, and WALTER flags any TERRY-instrument-touching correction to PROME for orchestration routing if time-critical.
- **NOT exempt — REGINALD** (BOARD-diff is *tiered/selective*, step 9b three-tier scope; the 7/4 reconciliation found an un-dispositioned ACTION — the OZK deed-in-lieu SIG-W-20260704-004 → keeps the lane + a drain-step) and **SAM** (no `/BOARD/` scan at all → the lane is its only intake).

**🔴 §3.5.4 — THE ACTION-LINE RULE (added v0.12, 2026-07-27, Will-approved). The exemption is only safe if `action:` actually means what it says.**

> **If a dispatch carries an ask directed at a named recipient, that recipient goes on the `action:` line — not `info:` with the ask buried in the body.**

**Why this is now load-bearing rather than tidy:** every pull-complete exemption rests on the claim *"this agent is never the ACTION owner, so dropping its push carries zero ACTION-miss risk."* That claim is only true if the `action:`/`info:` split is **accurate metadata**. **The defect that bought this rule was raised by PROME against its own proposal:** `SIG-W-20260727-016` was `action: [RED, LIQUID]`, `info: [..., PROME]` — **yet its §8 carried a direct operational ask to PROME as RESEARCH-INTAKE lane owner** (the OAS unit-label defect). Under the exemption, that ask would have arrived only as one line in a diff-scan and could plausibly have been skimmed past.

**This is §3.5.3's actionability test applied one level in:** §3.5.3 says *anything actionable is DISPATCHED, not noted*; §3.5.4 says *anything actionable **for a named recipient** marks that recipient as **actioned**.* Same asymmetry, same reasoning — an over-marked action line costs one extra handoff; an under-marked one hides an ask inside a document the recipient has been told they may skim.

**Mechanically enforced on the recipient side, not by WALTER's discipline alone:** `board_scan.py` **exits 1** on any action-line item, converting a hopeful skim into a hard stop. **⚠️ Scope note: this rule binds WALTER for EVERY recipient, not just exempt ones** — but it is *only* a hard stop for agents whose scanner enforces it. For non-exempt agents the handoff still lands regardless, so the rule is correctness-of-metadata there and a **safety precondition** here.

**Doctor:** `walter_doctor` carries a `PULL_COMPLETE` set that excludes exempt agents from `delivered_but_unconsumed` and instead flags any residual handoffs in their inbox as **to-ARCHIVE** (a one-time cleanup, not a consume-gap). **Transition:** existing pre-exemption handoffs are bulk-archived to `processed/` by PROME (cross-dir write, Will-authorized) once the exemption lands; going forward WALTER simply never creates them. Adding/removing an agent from the exemption edits both this list and the doctor's `PULL_COMPLETE` set.

#### 3.5.2 Who counts as "the recipient" — a SPAWNED INSTANCE does not consume (added v0.10, 2026-07-16)

**Rule: only the recipient's LIVE session consumes. A read-only spawned instance reading a handoff/note does NOT count as consumption, and MUST NOT move it to `processed/`.**

**Consumption ≠ reading. Consumption = INTEGRATION** — the recipient has folded the content into its own state (STATUS / KB / marks / gates). A spawned instance can *read* and even *act* (produce findings), but it **cannot integrate**: it holds no authority to re-mark its own agent's canonical state, so nothing has actually landed.

> **The tell, in one line (VULCAN's formulation, adopted verbatim — crisper than the original):** **the inbox is a prompt to ACT, so it should only clear when someone who CAN act has acted. A reader who cannot integrate cannot discharge it.** Use this as the test when the case is ambiguous — ask *"could this reader have discharged the obligation?"*, not *"did this reader read it?"*

**Why it matters (the failure this prevents):** if a spawned instance marks a note consumed, the **live** session's next boot inbox-scan shows **clean** — and the work exists only in a report nobody is prompted to open. **A cleared inbox is read as "handled." That silently converts a pending integration into a lost one.**

**Provenance (2026-07-16, and the direction is worth recording):** surfaced by **VULCAN — by DECLINING to act.** A read-only VULCAN instance, spawned by WALTER for the AI_INFRA_CAPEX axis check, was given a note whose own text invited `processed/`. It read it, acted on it (8 recommendations, R-01..R-08), **and deliberately left it unprocessed**, reasoning that *"consumption isn't integration — I read and acted; the live VULCAN hasn't folded R-01..R-08 into STATUS/KB yet,"* and flagged the ambiguity to WALTER rather than resolving it either way. **That judgment was correct and this spec did not cover it.** WALTER ratified + codified same-session. **The general lesson: an agent declining an in-scope action and flagging why is a spec-gap detector — treat it as a finding, not as friction.**

**Applies to:** dispatches (`inbox/WALTER/SIG-*.md`) and notes (`*-NOTE.md`) alike — the question is *who consumed*, orthogonal to §3.5/§3.5.1's *what's exempt*.

**Not mechanizable, and not claimed to be:** `delivered_but_unconsumed` measures whether a file moved to `processed/` — it cannot see *which* session moved it, and nothing in the repo distinguishes a spawned instance's `git mv` from the live session's. **This is an authorship discipline on the spawning coordinator** (WALTER: say it in the spawn prompt), not a check. Mechanizing it would need instance-provenance in the commit trailer — real cost, not obviously worth it, **not proposed.**

#### 3.5.1 Scope limit — the exemption covers DISPATCHES, not NOTES (added v0.9, 2026-07-16)

**The §3.5 exemption rests on a premise that is easy to lose: the content is ON BOARD.** The exemption is sound *only because* the recipient's whole-INDEX BOARD-diff **is** the pull — i.e. the handoff and the scan are fed the same BOARD entry, so the handoff is pure redundancy. **Remove the BOARD entry and the redundancy argument collapses: a BOARD-diff cannot surface something that was never on BOARD.**

**Rule:** a **non-BOARD note** to a pull-complete recipient (CARL, RED) **IS delivered to `AGENTS/{RECIPIENT}/inbox/WALTER/` — the §3.5 skip does NOT apply.** The inbox is that note's **only** delivery channel.

**What counts as a non-BOARD note** (the existing, unchanged fold/breadcrumb practice — this sub-section names its delivery consequence, it does not create a new artifact class): a create-only `*-NOTE.md` written to a recipient's `inbox/WALTER/` that carries a mechanism, correction, or cross-reference which **fails the Novelty gate as a signal** (owner already holds the event) but whose *value-add* the owner does not hold — so it is deliberately **not** dispatched: no BOARD entry, no `route_log` row, no `delivery_log` row. Worked examples: the **2026-07-11 CREED 1740-Broadway ratings-lag precedent** (event already in CREED's KB; the 17-month downgrade-lag *mechanism* was not) and the **2026-07-16 CARL retail-sales/savings breadcrumb** (CARL held the May print more precisely; the internal inconsistency between its own retail row and its own savings row was the delta) — the second is what surfaced this gap.

**⚠️ Known telemetry gap — accepted, named, NOT silently tolerated.** Because a note writes **no `delivery_log` row**, it is invisible to `walter_doctor`'s `delivered_but_unconsumed` **and** `written_but_undelivered` checks. **A note to a pull-complete recipient therefore has exactly one delivery path and zero telemetry behind it** — the weakest-instrumented thing WALTER produces, and a direct exception to the CONTRACT's "PROOF — instrumented (best-in-fleet)" claim. This is **tolerable at current volume** (2 notes total, ~1/wk at peak; both to non-exempt-or-adjacent agents) and is **not** worth a parallel ledger yet. **Escalation trigger: if note volume reaches ~1/wk sustained, OR a note is ever found unconsumed/missed, add a `note_log.tsv` (or a `delivery_log` row with `role: NOTE` + a `written_state` that the doctor can age) rather than continuing to rely on the recipient noticing an un-tracked file.** Until then the mitigation is that notes are rare, create-only, and boot-visible in the recipient's inbox.

**Author discipline:** a note to a pull-complete recipient **must state, in the note itself, why it is arriving in an inbox the recipient's §3.5 exemption would normally make redundant** — otherwise the recipient may reasonably read a stray inbox file as an exemption violation or a stale artifact and archive it unread. (Both worked examples above carry that line.)

**This is a clarification of §3.5's scope, not a change to it.** No agent moves in or out of `PULL_COMPLETE`; the doctor's set is untouched; every dispatch-path rule above is unchanged.

---

#### 3.5.3 🔴 THE ACTIONABILITY TEST — notes are NON-ACTIONABLE CONTEXT ONLY; anything actionable is DISPATCHED (added v0.11, 2026-07-25, **Will-directed**)

**Rule, and it is a hard one:**

> **If the content could change what the recipient DOES — a position, a watch, a threshold, a grade, a state, a calendar item — it is a SIGNAL and gets DISPATCHED, with the full BOARD + `route_log` + delivery-handoff + `delivery_log` treatment. NOTES are for NON-ACTIONABLE CONTEXT ONLY.**

**Apply the test by asking one question, and answer it pessimistically:** *"if the recipient never opens this, could they later take a decision they would have taken differently?"* **If yes — or if you are unsure — DISPATCH.** The asymmetry is the whole point: an over-dispatched context item costs one BOARD row and a little noise; an under-dispatched actionable item is invisible, untracked, and discovered only when the decision has already gone the other way.

**What remains a legitimate NOTE (non-actionable context):**
- A mechanism, precedent or cross-reference that **enriches** an owner's existing read without changing any call (the 7/11 CREED 1740-Broadway ratings-lag precedent).
- A **pointer to an unverified lead** — a headline-only item with no body reached, explicitly labelled as a pointer (the 7/24 LIQUID Goldman AI-junk-bond and VULCAN depreciation pointers).
- A **courtesy cross-reference** to work an owner already holds, sent so they know WALTER saw it.
- An **internal-inconsistency breadcrumb** where the owner holds both facts and the delta is only that they disagree (the 7/16 CARL retail/savings breadcrumb).

**What is now a DISPATCH even if it fails the Novelty gate as news:**
- **Any CORRECTION to a previously dispatched signal** whose consequence changes an action. *(Worked example: the 7/24 "the FHA/VA KILL rests on sector averages" caveat went out as a note. It was decision-changing — REGINALD was re-pointing a live watch on four banks — and it was re-issued as `SIG-W-20260724-007` at Will's direction. Under this rule it would have been dispatched at the outset.)*
- **Anything touching a registered threshold, falsification trigger, gate, or pre-registered prediction** — including proximity, exit-proximity, and suppression state.
- **Anything that switches a watch ON or OFF**, or re-points one.
- **A dated catalyst** the recipient does not already carry.
- **A refutation of a figure the recipient is using**, whether or not the underlying event is novel.

**Provenance (the evidence bar this cleared):** three instances inside ten days, two of them from recipients rather than from WALTER's own review. **VULCAN twice stated it would prefer notes arrive as dispatched signals** (7/19, after its axis-check note sat unread ~19h; reiterated in the 7/24 depreciation-pointer exchange). **Will directed the third** — first ordering the BKU re-point dispatched-not-noted (7/25), then ratifying the general narrowing. The recurring failure mode is identical each time: **actionable content routed down the one lane with zero delivery telemetry.**

**Effect on the §3.5.1 telemetry gap:** this **shrinks the exposure rather than instrumenting it.** Notes remain un-instrumented — but by construction they now carry nothing whose loss changes a decision, so the un-instrumented lane stops being a risk surface and becomes what it was always described as: courtesy context. **The `note_log.tsv` escalation trigger in §3.5.1 stays armed and unchanged**, but its expected trigger rate should fall, because the actionable traffic that was driving note volume now leaves through the dispatch path. **If note volume does NOT fall after this change, that is evidence the test is being applied too loosely — re-read §3.5.3 before adding a ledger.**

**This DOES change behaviour** (unlike §3.5.1, which was a clarification). It does not move any agent in or out of `PULL_COMPLETE`, and it does not alter the dispatch mechanics themselves — it changes **which lane content enters**, and it strictly increases the share of decision-relevant traffic that carries delivery telemetry.

---

#### 3.5.5 🔴 TERRY — ownership-keyed action routing, and NO info-cc (added v0.15, 2026-08-07; **Will-CONFIRMED in-session**, ruled by the owning desk in `FORUM/2026-08-07_system-review/06_proposals/07_TERRY_routing-disposition.md`)

> 🔴 **THE NON-RENEWABLE FALSIFIER FIRED — REVERT EXECUTED 2026-08-26 (v0.21, WALTER, mechanical execution of the ratified remedy).** **Condition met on the fact and on the instrument's own line:** `SIG-W-20260822-002-CORRECTION` (`action: TERRY`, delivered 2026-08-23T20:1xZ) sat unconsumed **~78h** at the 2026-08-26 boot, and the S1 owner-unconsumed line named TERRY (1A). Per the falsifier's letter below — *"REVERT TO THE RED-CLASS EXEMPTION. Do not tune the tests."* — **TERRY is now EXEMPT: no `inbox/WALTER/` handoffs, no `delivery_log` rows; BOARD + `route_log` still written.** T-1/T-2/T-3 are RETIRED as delivery gates (untouched as text, per the letter). ⚠️ **Stated plainly: this exemption rests on the FALSIFIER'S MANDATE, not on a pull-complete warrant — TERRY has no BOARD differ, and the accepted cost is the T-2 class ("TERRY can re-pull every price and cannot re-pull a retraction"), exactly as v0.15 priced it.** The unconsumed correction handoff STAYS in TERRY's inbox (create-only; TERRY consumes at next boot). ⚠️⚠️ **THE INSTRUMENT WAS BLIND WHEN IT FIRED:** `terry_override_ratio`'s falsifier leg parsed `timestamp_routed` with `fromisoformat` and SILENTLY SKIPPED every row carrying the desk's own `~HH:1xZ` anti-false-precision stamps — the doctor printed "falsifier unfired" while the condition stood met on disk. Fixed same session (parse fallback + exact-minute stamps mandatory in TSV fields); recorded because a guard that cannot see its own trigger class is the `[[finding_test_the_guard_not_just_the_guarded]]` shape, n+1. The section below is retained unedited as the record of the rule that ran 8/07–8/26.**

**Both halves or neither. The volume cut is what pays for the action obligation.**

> **A dispatch goes on `action: TERRY` if and only if it meets one of three tests. There is NO `info:` delivery to TERRY.**
>
> **T-1 — NAMED INSTRUMENT.** It names, or bears directly on the level of, a registered TERRY instrument: a live or staged `setup_id`, its underlying ticker, a card gate / kill line / invalidation / harvest level, a numbered `RISK_RULES` rule, or a load-bearing `SIGNALS.tsv` row.
> **T-2 — CORRECTION OR RETRACTION.** It corrects, retracts or retires **a number or level that any TERRY surface cites**, whether or not it names TERRY.
> **T-3 — CLOSED-MARKET EVENT.** A non-price event landing while the market is closed, on an underlying TERRY holds or has staged.

**Why this desk and not the RED exemption** (the question was live and the answer is specific, so it is written here rather than inferred): RED's exemption works because RED has a **complete self-generated interrupt** — its whole-`INDEX` BOARD diff regenerates the notification that ending delivery removes. **TERRY has no BOARD differ.** Every TERRY boot instrument (`boot.py`, `snapshot.py`, `chain_fetch.py`, `risk_calc.py`, `paper_book_mark.py`) reads a price, a chain or a ledger; none reads the BOARD or any other agent's state. So *"TERRY re-pulls at fire time"* is true of **prices** and false of **facts about the world** — and the asymmetry decides it: an unread info-cc costs a skimmed minute, an undelivered retraction costs a live card graded against a number that was retired last week. **T-2 is the test TERRY structurally cannot self-source** — `consumer_check.py` scans publisher→consumer *inside* the fleet, and WALTER relays third-party numbers no fleet agent ever published, so that check is blind to the class by construction.

**Deliberately excluded, and this is the guard against over-actioning:** general positioning colour · theater/war signals with no TERRY instrument attached (`IRAN_HORMUZ` was 53% of the old lane) · anything whose only connection is *"relevant to sizing."* §3.5.3's wording governs: **fires / falsifies / re-points — never "is relevant to."**

**Accepted, priced miss (n=1 of 32, ~3%):** an *anti-action* signal — one whose purpose is to stop a trade, e.g. `SIG-W-20260731-009` (*"no card action is implied and none is recommended"*, plus a date-trap warning) — fails all three tests. **It is not rescued by widening T-2**, because widening a definition to make one case pass is the move the desk's own guards forbid. If the class recurs at **n≥3 in 30 days** it earns its own numbered test on its own evidence.

**Discretionary override — logged, counted, and billed.** WALTER may send outside T-1/T-2/T-3 when judgement says to. Because there is no `info:` lane to TERRY, **any non-qualifying send IS an override.** Record it by prefixing the `delivery_log` `notes` cell with the token **`TERRY-OVERRIDE`** plus a one-line reason — countable by grep, no new file, no new register (same additive-marker idiom as §3.7).

**⚖️ THE OVERRIDE CLAUSE — ratified by TERRY 2026-08-07 via PROME, in TERRY's exact terms, to be graded as written:**

> **Ratio ≤10%. Denominator: trailing 90 days (one quarter). Activation: n≥10 dispatches in the window. n=1 report to TERRY is MANDATORY (the `TERRY-OVERRIDE` prefix stands). Breach ⇒ a MANDATORY READ OF THE OVERRIDE LOG — never an automatic widening of T-1/T-2/T-3.**

**Why 90 days and not 30** *(TERRY's reasoning, carried into the clause because a window without its rationale gets "tidied" back to the fleet default)*: at ~3 dispatches per 30 days, **n≥10 is unreachable by construction** — the activation condition can never be satisfied, so the test would sit permanently in a no-verdict band that never ends. That is the same defect class as the S2 `NONE` branch: *a test whose branch is determined by construction rather than by the world.* **90 days is the smallest window in which the rule is satisfiable at the projected volume.**

**Why a ratio and not an absolute count:** the thing being measured is a **rate of rule-misfit**, not a quantity of overrides. An absolute cap tightens silently as lane volume grows — the same 3 overrides mean something different against 10 dispatches than against 40 — and a threshold that changes meaning without anyone editing it is exactly what a registered threshold is supposed to prevent.

**⚠️ TERRY's own guard on its own clause, and the reason the breach action is *read the log* rather than *widen the tests*: the denominator is WALTER's volume, so the rule can be tripped by its own success.** A quarter in which WALTER routes few TERRY dispatches — because the tests are working and little qualifies — shrinks the denominator and inflates the ratio on the same override count. **A breach is therefore evidence that something needs LOOKING AT, never evidence of what.** Read the override log; if the tests really are cut too narrow, widen **only by adding a numbered test with its own falsifier — never by loosening an existing one.**

**🔴 TWO CLOCKS, DELIBERATELY UNHARMONISED — do not "fix" this.** The override clause runs on **90d / ratio / n≥10 activation**. The revert falsifier below runs on **30d / n=1 / no denominator at all**. They are different instruments: the override clause measures a *rate* and needs a satisfiable sample; **the falsifier is an EVENT test — one unconsumed `action:` item past 72h is a fact about a single delivery and has no denominator problem.** Harmonising the two windows would either make the falsifier need a sample it does not need, or drag the ratio back into the unsatisfiable band. *(TERRY ruled this explicitly. Recorded here because an inconsistency that is deliberate and an inconsistency that is an oversight look identical to a later reader — [[finding_deliberate_and_unnoticed_asymmetry_look_identical]].)*

> *Superseded provisional wording, retained per §3.6's additive-marker discipline — the paragraph this replaced, written 2026-08-07 before TERRY ruled: "Operative form until the lane produces ≥10 dispatches in a 30-day window: every override is logged and reported to TERRY inside that window, and the ratio test activates at n≥10." **WALTER flagged the 30-day boundary as unevaluable ([[finding_prereg_verdict_boundary_must_be_a_number]]) and declined to invent a replacement denominator; TERRY supplied 90d and the reason the interim wording was still wrong — it kept the unreachable activation condition rather than removing it.***

**Falsifier — symmetric, numeric, and NOT renewable (this is the half that protects Will, so it travels with the rule):**

> **If the S1 owner-unconsumed line ever names TERRY even once — an `action:` item unconsumed >72h — this desk cannot carry an action obligation at its launch cadence, and the correct disposition was the exemption after all. REVERT TO THE RED-CLASS EXEMPTION. Do not tune the tests.**

TERRY boots ~15 days in 38; an action line it cannot clear at that cadence is not attention, it is a second backlog wearing a priority label — the BOND shape this review convened to fix.

**Anti-ratchet payment, measured:** 32 deliveries/quarter → ~9–11. **Net −21 to −23 deliveries and −32 `delivery_log` rows per quarter**, adding no file, no script, no invocation site and no register. It kills outright more than it converts.

**Scope:** TERRY only. This is a **desk-scoped instantiation**, not the general ownership rule — the general form (extend §3.5.4 from *ask* to *ownership* fleet-wide) remains an unratified proposal (`06_proposals/01_WALTER_routing-lane-proposals.md` P2) and must not be inferred from this section.

---

**🆕 S1 IS BUILT (v0.19, 2026-08-20 — the 8/08 forum-carry item 2, PROME-accepted inverted-token design; S1 is the instrument that can revert this rule).** **Declaration convention at dispatch: every `action: TERRY` `delivery_log` row BEGINS its `notes` cell with its qualifying test token — `T-1`, `T-2` or `T-3` (closed vocabulary), optionally followed by a reason.** **Absence of a valid leading token IS an override by definition** — typos OVER-report, so the clause fires early; over-firing costs a read, under-firing costs the guard. `TERRY-OVERRIDE` survives as the human-readable reason prefix and is no longer load-bearing. **Rows written before 2026-08-20 are graded by the legacy discriminator (`TERRY-OVERRIDE` prefix = override)** — the new grammar does not manufacture violations out of rows that predate it. Enforced by `walter_doctor` **`terry_override_ratio`**: the ratified 90d / ≤10% / n≥10 clause (breach ⇒ READ THE OVERRIDE LOG, named signals, never a bare count, never auto-widen), **plus the revert falsifier as a separate event test — one `action:` item unconsumed >72h fires HIGH with the revert instruction.** Two clocks, deliberately unharmonised, now both machine-watched. *(The S1 hook entry remains coordinated with DAEDALUS's Rung A and is NOT built here — the doctor check is the instrument; a hook is a delivery vehicle for it.)*

### 3.5.7 🔴 THE DARK-OWNER DOORBELL — WALTER's half (added v0.20, 2026-08-23)

**Provenance:** WALTER-proposed 8/22 → **RULED ADOPTED** by Will via PROME 8/23 (*"ok go forward approved"*), three amendments + four riders; record `PROME/proposals/2026-08-22_dark-owner-doorbell-RULED.md`. **Rule 6b (`MESSAGING/CROSS_SESSION_MESSAGING.md`) is the SINGLE HOME of the gate's letter — this section is WALTER's operational half and POINTS to it, never restating its text.** Where the two disagree, 6b wins and the fix lands there, by Will's word.

**🔑 WHAT THE ORCHESTRATION RULING CHANGED, AND WHY THE GATE MOVED (Will-directed retune, in-session 2026-08-23).** The gate was calibrated when the only remedy behind a doorbell was **waking a whole desk in its own window** — expensive, disruptive, Will-in-the-loop. As of the two-tier ruling (`ORCHESTRATION_PLAYBOOK` §Two-tier, same day) the remedy is a **bounded named-subagent touch**: day-scoped, spawnable inside PROME's existing autonomy tier, and it **drains the desk's whole inbox**. ⚠️ **The gate did not become wrong; the PRICE BEHIND IT FELL by roughly an order of magnitude, and a gate calibrated against the old price is now systematically tight.** ⇒ **The error costs are now asymmetric in the OPPOSITE direction from v1: an over-doorbell wastes a cheap touch and is LOUD; an under-doorbell leaves a desk sitting on obligations and is SILENT.** `[[finding_standing_guard_is_a_false_negative_risk]]`

**🔴 THE UNIT OF DECISION MOVED FROM THE ITEM TO THE DESK.** v1 asked *"does THIS ITEM justify waking a desk?"* — correct when the touch cleared one item. Under the whole-inbox drain clause the touch clears **everything**, so v2 asks *"does THIS DESK's accumulated state justify a bounded touch?"* **The `action:` item is the TRIGGER; the backlog is the YIELD.** This is the direct fix for the blind spot the ruling itself named (§4 of the ruling packet): *"the doorbell selects on the CLOCK; the backlog concentrates on desks with no clock."* v1 could not reach HENRY or BROCK **by construction**; v2's leg 3b is built precisely to.

**P0 — PRECONDITION (NEW, and it is not optional): THE DESK MUST NOT ALREADY BE IN-FLIGHT.** Desks now have **three** states, not two: live-in-own-window · dark · **running as a PROME subagent**. Check `PROME/state/ORCH_LOG.tsv` for an open touch **and** `ListAgents`. **P0 fails ⇒ NO doorbell; note it and wait.**
   > 🔴 **P0 CORRECTED 2026-08-23 ~11:2x, BEFORE FIRST USE, on PROME's answer to the ASK this amendment shipped with — and the correction INVERTS which side of P0 is authoritative.** **`IN-FLIGHT` cells update at PROME's CONSUMPTION of a delivery: they lag a desk's real delivery by minutes and lag a DEATH INDEFINITELY** (a dead touch's row stays IN-FLIGHT until PROME notices). ⇒ **`IN-FLIGHT` IS NOT A LIVENESS INSTRUMENT AND MUST NEVER SUPPRESS A DOORBELL ON ITS OWN.** **Operative form: P0 fails only when IN-FLIGHT is CORROBORATED by liveness evidence — the desk present in `ListAgents`, OR writes in its dir within the last few minutes. An UNCORROBORATED `IN-FLIGHT` row means DARK: doorbell normally, and tell PROME the row is stale.** ⚠️ **Read the cell as *"PROME believes a touch is open,"* never as *"the desk is alive."* Had the uncorrected form shipped, a desk that DIED mid-touch — the case most needing a doorbell — would have been suppressed permanently, which is the precise silent false-negative this mechanism exists to remove.** `[[finding_test_the_guard_not_just_the_guarded]]` — this guard's own v1 failed on first examination, exactly as that memory predicts. **Semantics now encoded in the ledger's own header (`f1c33ff1f`), so P0's dependency is written rather than tribal.** *(Convergent: PROME's failure-path STEP 0 landed ~11:0x and this packet ~10:5x, neither having seen the other; PROME adopted the desk-dir-write-recency limb with credit.)*
 🔴 **Bought on pilot day one, 2026-08-23: SAM was declared dead on a credit-wall failure notice and respawned — while ALIVE** (PID 45988, 18 minutes elapsed, writing `STATUS.md` at 10:44:02 / 10:45:09 / 10:45:54, and listed live in `ListAgents`). Two sessions briefly pointed at one desk; **SAM-2 caught it, wrote nothing, and went idle citing root Critical Rule #2** — which is the only reason it cost nothing. **A failure NOTICE is not a death certificate** (`[[finding_record_of_an_action_is_not_the_action]]`, DEATH-CERTIFICATE limb). A doorbell against an IN-FLIGHT desk invites the same class from the other end.

**LEG 1 — OWNER UNAVAILABLE.** Not live in its own window; not IN-FLIGHT per P0. *(Unchanged in form. **Its valence inverted:** under v1 darkness was the OBSTACLE — there was little to be done about it without Will; under v2 it is the QUALIFYING CONDITION, because a transport now exists that serves it.)*

**LEG 2 — A TRIGGERING OBLIGATION.** At least one unconsumed `action:` item for that desk. **INFO alone NEVER fires this leg** — the yield field below is what INFO backlog feeds, and yield is not a gate. ⚠️ **CASE-NORMALISE THE MATCH.** `delivery_log.tsv` holds **478 lowercase `action` + 191 uppercase `ACTION` = 669**; a case-sensitive test reads **191 of 669 — a 71% undercount biased toward the NEWER rows**, because lowercase is the newer convention. A check written the obvious way reports a healthy queue off a quarter of its data (rider R1; RAV caught it pre-build).

**LEG 3 — DECAY. Either limb satisfies.**
- **3a — NAMED REFERENT** *(v1's limb, retained verbatim in effect)*: a named, checkable referent — a DOCKET row, a GATES row, a dated position expiry, **or a live position facing the next market open** — whose value decays before the desk's likely next boot. **NAMED, not asserted, and LOGGED** (the logging is what makes the miss counter computable at all — RAV's addition).
- **3b — CADENCE IS THE DEADLINE** *(NEW at v0.20)*: the desk's **median inter-session gap ≥7d** AND its **oldest unconsumed `action:` item already exceeds that gap**. **For a low-cadence desk the GAP ITSELF is the dated event**; demanding an external clock on top of it is the unfireable-conjunction error in a new costume — the same error Will corrected in leg 3's own first draft twelve hours earlier.
  > 🔴 **COMPUTE THE GAP FROM AUTHORED COMMITS ONLY.** `git log --author=…` over the desk's own commits — **NEVER `git log -- AGENTS/<DESK>/`**, which counts what OTHER agents (largely WALTER's own routing lane) write into that tree. That instrument reported HENRY at *"94 commits this month"* when **12 were HENRY-authored across 3 days**; it overturned a correct thesis on 8/22 and was struck from rule 6b on 8/23. **Building it into this gate would reproduce the identical error one level down, inside the mechanism the error was about.** `[[finding_path_scoped_git_log_measures_inbound_traffic]]`

**YIELD — a payload field, NOT a leg.** Total unfiled items the touch would clear, ACTION and INFO, at doorbell time. Because the drain clause clears the whole inbox, **yield is what separates a touch worth PROME's scarce slot from one that is not**: 1 ACTION + 40 INFO outranks 1 ACTION + 0 INFO. It never fires the gate on its own.

**EMISSION — every count names its age basis** (rider R2). PROME's 26 (signal-date) and the doctor's 22 (stricter, pull-complete residues excluded) are ONE population under TWO bases, not a disagreement.

**THE LOG — `AGENTS/WALTER/registry/DOORBELL_LOG.tsv`.** ⚠️ **The ruling said "the five-field log" without enumerating the five; these are they, and the enumeration is WALTER's** — `desk` · `referent` · `doorbelled` · `disposition` · `drained`. Four bookkeeping columns make the miss counter computable: `date` · `sig_id` · `yield_at_doorbell` · `consumed_at`. 🔴 **A ROW IS WRITTEN FOR EVERY DARK-RECIPIENT `action:` DISPATCH — NOT ONLY THE ONES DOORBELLED.** Without the non-doorbelled rows the miss counter has **no denominator** and can only measure the decisions that were already made, which is the shape of the §5 trap this gate was designed against.

**THE TWO COUNTERS** (`walter_doctor` checks, per amendment ③ — **NOT doorbells-per-dispatch**):
- **MISS** — for every dark-recipient `action:` dispatch, compare the logged referent's date against the actual consumption date. **Referent first = a miss, doorbelled or not.** This is the falsifiable half: over-spawns are loud, misses are silent, and **tuning on the visible number alone walks back to a 100+ unread backlog with every step looking like discipline.**
- **DECLINED** — doorbells PROME declined. **This one points at PROME, not WALTER:** if the gate fires correctly and PROME declines everything, drain rate stays high and misses stay low **while the mechanism is dead.**
- ⛔ **The ~⅓ tightener stays UNWIRED until a base rate exists** (`CHECK_STANDARD` §12, base-rate-before-wiring, Will-ratified 8/21). **v1 and v2 doorbells are TWO POPULATIONS under two price regimes — the 8/28 soak must not pool them**, or a price change will read as drift.

**Scored against the 8/22 worked night, same seven dispatches:** v1 = **1-of-7** (only `-002`/TERRY, on a live position facing Monday's open). **v2 ≈ 3-of-7** — TERRY still passes on 3a; **HENRY and BROCK now pass on 3b** (53 unfiled / 7 ACTION, ran 3 days that month, oldest unintegrated 15d; and 16 / 6, last run 8/13). MARCO still fails (boots daily against a 9/8 date); `-007` still fails for want of any referent. **The two v2 adds are exactly the two desks the ruling identified as the real backlog and that v1 structurally could not reach.** The gate is still marginal by design, and the marginality should stay visible.

**⛔ WHAT THIS SECTION DOES NOT DO.** It does not let WALTER spawn — **WALTER recommends, PROME triages, PROME spawns only where the tier permits, a new-direction domain spawn is a proposal to Will** (ratified; tier detail single-homed at `PROME/AUTONOMY.md`). It does not touch rule 6b's letter. It does not widen `action:`/`info:` semantics (§3.5.4 unchanged). It does not make yield a gate.

---

### 3.6 🔴 CORRECTION LIFECYCLE — who owns which half (added v0.13, 2026-08-07; encodes Will-accepted RAV roster-plan Ruling #4 via PROME 2026-08-05)

**The split, stated so it is written rather than remembered:**

| Half | Owner | What it means |
|---|---|---|
| **Downstream PROPAGATION of a corrected figure** | **THE PUBLISHER** of the figure | The agent that published a number owes the packets to whoever is citing it. Mechanism = root `CLAUDE.md` step 1c (`consumer_check.py` + a packet per 🔴 STALE owner). **WALTER is the publisher for figures WALTER publishes, and no one else's.** |
| **BOARD/signal correction LINKAGE** | **WALTER** | When a dispatched signal is corrected, WALTER links the corrected signal to the original **at every BOARD surface**, so that no consumer can arrive at the stale signal and read it clean. |

**⇒ These are NOT the same job and neither substitutes for the other.** A publisher can packet every downstream holder and still leave a stale BOARD signal that a future reader discovers cold; WALTER can link every BOARD surface and still leave a live agent citing the dead number in its own files.

**WALTER's linkage obligation is THREE surfaces, not one** *(this is the operative requirement — a `corrects:` header alone is not linkage, because it only points FORWARD and the reader arriving at the stale signal never sees it — the one-way-pointer defect found in the 8/3 staleness sweep, where two signal TITLES asserted a corporate default that never happened and sat untagged 6 and 11 days **while the correction already existed**)*:

1. **The correcting signal's `corrects:` header** — SIG-ID (or a list), `SELF`, or `EXTERNAL:` per `SIGNAL_FORMAT_SPEC` v0.15. Mandatory on `signal_type: correction`; enforced by `walter_doctor` `correction_target_declared`.
2. **The corrected signal's INDEX row** — append a visible back-marker naming the correcting SIG-ID and stating **in one line what is now wrong**. The INDEX is the discovery surface; a reader scanning the cluster must see it without opening the file.
3. **The corrected signal's FILE** — a banner immediately after the YAML front matter, same content. A reader who arrives by direct link, grep or an old citation never touches the INDEX.

**⚠️🆕 STATE THE DIRECTION, NOT ONLY THE NUMBER — added 2026-08-18 (BOND's rule, adopted; §3.6.2).** **When a corrected figure had CONCLUSIONS built on it, the marker must say explicitly whether those conclusions HOLD, WEAKEN, or FLIP.** 🔑 **A consumer CANNOT infer conclusion-inversion from a corrected number alone** — they get the new value and are silently left to re-derive a direction they may not know was load-bearing. ⚠️ **Bought the same day, twice, in one thread: WALTER published *"materially LESS alarming"* off a run-length of `79`; when BOND corrected it to `92` with a true post-2007 max of `11`, the honest read INVERTED to *understated*. BOND supplied corrected numbers and left the direction to be re-derived; WALTER happened to catch it.** 🔑 **WHY THIS RULE BINDS WALTER HARDER THAN THE DESK THAT PROPOSED IT — named explicitly at BOND's request, because the asymmetry is not obvious and determines who must actually keep it: the rule's VALUE SCALES WITH A DESK'S CORRECTION VOLUME, NOT WITH HOW OFTEN IT ERRS.** WALTER writes correction markers into a SHARED ARCHIVE at far higher volume than any desk sends packets, so **the population of readers who receive a corrected number WITHOUT a direction is overwhelmingly reading WALTER's surfaces.** ⇒ **A rule BOND proposed about its own conduct lands mostly here, because this is where the exposure is.** Do not read §3.6.2 as advice to senders; read it as a standing obligation on every marker this desk writes.

**And a corollary BOND drew from the same episode, adopted here: SHIP A RETRACTION AS ITS OWN PACKET, never folded into the next one.** The cost of a standalone packet is minutes; the cost of waiting is a wrong figure live on N surfaces for an unbounded interval — measured at **four surfaces for five minutes** in this instance, and only luck made that short.

**⚠️ State what SURVIVES, not only what broke.** Both markers must say which half of the original still stands. A marker reading only "CORRECTED" invites the reader to discard a sound argument along with a bad figure — the 7/24 calibration-vs-verdict lesson, applied to the linkage layer. *(Worked example: `SIG-W-20260807-001` corrects a DATE across four signals whose arguments are entirely unaffected, and every marker says so explicitly.)*

**Never edit the original's substance.** Markers are additive. The historical record is what lets a reader see that the correction *happened*.

#### 3.6.1 Backfill sweep — cadence, so it is not a remembered ritual

**The correction-link backfill (finding pre-existing dispatched signals whose corrections were never linked) runs as a NAMED STEP OF THE EXISTING STALENESS SWEEP, on that sweep's ~14-day cadence** — not as a separate calendar item.

**Why folded rather than free-standing:** the staleness sweep already walks every BOARD signal, already has a doctor check enforcing its cadence (`staleness_sweep_overdue`), and already produces an adjudication record in `registry/STALENESS_SWEEP_*.tsv`. **A second sweep with its own cadence would be a second thing to forget** — `finding_mechanize_the_cap_not_the_ritual`: a deferrable obligation wants an existing enforced hook, not a new one.

**Trigger (either fires it):** (a) the next staleness sweep, whichever comes first on the 14d cadence; (b) **immediately, out of cadence, whenever a correction is dispatched whose target is more than one signal** — because that is the case where the linkage load is largest and the chance of a missed surface is highest.

**The sweep step:** for every signal carrying `signal_type: correction`, confirm its target(s) carry back-markers at BOTH surfaces (INDEX row + file banner). Record non-linkages and the reason, the same way the staleness sweep records deliberate non-tags — **an unrecorded skip is indistinguishable from an oversight.**

⚠️ **Known limit, stated: this sweep can only find corrections that DECLARED themselves.** A correction dispatched without `signal_type: correction` is invisible to it. That is an **adoption** gap, not a detection gap, and it is exactly the trap of the 8/3 proposal — *never key a completeness check on the field whose absence is the defect*. The enum + mandatory `corrects:` shipped 8/3 (FORMAT_SPEC v0.15) with all 9 then-existing corrections retro-filled, so adoption is currently 100%; **if that ever slips, the sweep under-reports silently.**

---

### 3.7 🔴 EXPIRED — a delivery disposition, distinct from consumed and from backlog (added v0.14, 2026-08-07; **Will-ruled live in the FORUM system review**)

**The gap this closes.** Until now a delivered handoff had exactly two observable states: consumed (moved to `processed/`) or not. "Not consumed" covered two situations that are nothing alike — *the owner has not got to it yet* and *the decision it existed to inform has already been taken without it.* The second is unrecoverable at any price, and on every surface we keep it looks identical to the first: an old item with nothing due.

**Definition.** A delivery is **EXPIRED** when **both** legs hold:

1. the recipient has not consumed it, **and**
2. the **dated decision that would have consumed the answer has already passed.**

Leg 2 is NEXUS's wait-cost discriminator (`FORUM/2026-08-07_system-review/01_signal-latency/02_NEXUS_…`) run past its own deadline. The three-way split it produces is the point:

| Disposition | Test | What to do |
|---|---|---|
| **COSTLY** | unconsumed, consuming decision **inside** the window | escalate — launch the owner |
| **BACKLOG** | unconsumed, consuming decision **outside** the window, headroom remains | leave it; it will be consumed at the owner's next boot |
| **EXPIRED** | unconsumed, consuming decision **already passed** | **RETIRE the delivery. Do not escalate.** Launching the owner for it buys nothing |

**How it is recorded — one mechanism, additive, in place.** Prepend `EXPIRED <date> — <one-line reason naming the consuming event and its date>` to the `notes` cell of that row in `delivery_log.tsv`, separated from any existing note by ` | `. The original note text is **never** replaced (same rule as §3.6: markers are additive, never edit the original's substance). `delivery_log` is append-only in the sense that rows are never removed or rewritten; a retro-applied disposition marker in `notes` is the delivery-layer analogue of FORMAT_SPEC v0.10's retro-applied `status:` tagging on an append-only BOARD.

**Four things EXPIRED is NOT, and each has bitten something:**

- **Not `written_state`.** That column is a write-time creation stamp consumed by the doctor's git-derived delivery check (§4). It stays `delivered`, because the handoff *was* delivered. Expiry is about the decision, not the transport.
- **Not a move to `processed/`.** WALTER never moves another agent's inbox file (RULE 10, create-only), and doing so here would record a consumption that did not happen — the §3.5.2 false-clear, where a cleared inbox reads as "handled" at the owner's next boot.
- **Not a BOARD `status: EVENT-PASSED` tag on the signal.** Those two are different objects. The *signal* may be a perfectly accurate dispatch-time snapshot that a co-recipient consumed and graded on time; what expired is one recipient's copy. Tag the signal only if the signal itself is now actively misleading, per FORMAT_SPEC v0.10's own discipline — and note that tagging the BOARD copy would not reach the unread reader anyway, which is the one-way-pointer defect §3.6 exists to prevent.
- **Not a judgement about the recipient.** ZHAO's expiry below is a cadence fact, not a discipline finding.

**Mark every expired row of a signal, not just the one that prompted the review.** An identically-expired row left unmarked is precisely the state the category exists to end.

⚠️ **Known limit, stated on day one: this disposition is visible on the SENDER'S side only.** The recipient meets the handoff file, and the handoff is create-only and immutable to WALTER — so the owner still opens an expired item at its next boot with nothing on it saying so, and learns it is expired by reading a date. **There is no clean fix inside the current delivery layer**; the candidate fixes (a sibling `-EXPIRED.md` marker, or making handoffs WALTER-mutable) each cost more than the defect. Recording the gap here rather than papering it: `finding_dated_carry_item_has_no_expiry_check`. The structural answer is a declared `consuming_date` field carried by the signal at dispatch, proposed in `06_proposals/01_WALTER_routing-lane-proposals.md` P4.

**First application (2026-08-07):** `SIG-W-20260730-009` (yen −2%/day + won strongest since Feb, dispatched hours before the BOJ) → **ZHAO (action) and LIQUID (info) both EXPIRED**, unconsumed at 8 days, consuming event the 2026-07-31 BOJ policy meeting. Co-action SAM consumed it in 0.5 days and graded it at the print, so the signal did its job. Retired, not escalated.

---

## 4. `delivery_log.tsv` — WALTER-side delivery record

File: `AGENTS/WALTER/routed/delivery_log.tsv` — **WALTER-owned**, append-only, **one row per signal × recipient** (a single signal fanning to N recipients writes N rows). Separate from `route_log.tsv` (which stays one row per *signal* = the routing decision); the two have different cardinality, so they are not merged.

| Column | Type | Description |
|--------|------|-------------|
| `timestamp_routed` | ISO 8601 UTC | When WALTER wrote the handoff file. |
| `signal_id` | string | `SIG-W-YYYYMMDD-NNN`. |
| `recipient` | string | Agent name. |
| `role` | enum | `ACTION` / `INFO`. |
| `recipient_platform` | enum | `CLAUDE_CODE` (constant since the single-machine collapse, 2026-06-26). Historical `OPENCLAW` rows preserved as-is — append-only, never rewritten. |
| `precedence` | enum | `FLASH` / `IMMEDIATE` / `PRIORITY` / `ROUTINE`. |
| `handoff_path` | string | `AGENTS/{RECIPIENT}/inbox/WALTER/SIG-W-YYYYMMDD-NNN.md`. |
| `written_state` | enum (write-time stamp; **NOT** maintained post-write) | `written_not_delivered_pending_push` — the write-time default (handoff created; rides the next closeout `safe-push.sh`). Legacy values `COMMITTED` / `DELIVERED` / `DELIVERED_SHARED_CLONE` predate the 2026-06-26 single-machine collapse. **This is a creation stamp, not a lifecycle field** — WALTER does not flip it to delivered post-push (the ~560 rows stuck at `pending_push` are expected, not a backlog). **Authoritative delivered-state is git-derived** via the doctor's `written_but_undelivered` check (handoff committed AND on origin = delivered). Do not backfill. *(Formalized v0.8, 2026-07-09.)* |
| `notes` | free text | Optional. |

**Critical (requirement B):** WALTER records *written/committed* state only. Whether a committed handoff is **on origin / delivered** is **derived read-only from git by `walter_doctor`** (see §6) — PROME does **not** edit this log after pushing. WALTER owns the log; PROME owns the sync/push *action*; the doctor derives sync state. This keeps the log a WALTER-only write surface and avoids a cross-agent edit race.

**UTC discipline:** `Z` means UTC. Convert ET/local clock before writing; never append `Z` to local wall-clock time.

Header row (exact):
```
timestamp_routed	signal_id	recipient	role	recipient_platform	precedence	handoff_path	written_state	notes
```

---

## 5. `board_log.tsv` — consumption record (recipient-owned)

Each agent maintains `AGENTS/<NAME>/board_log.tsv` — local, append-only, one row per consumed signal. **v0.2 adds a `source` column** so a consumed entry records *how* the agent encountered the signal.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `timestamp_read` | ISO 8601 UTC | yes | When the agent read it. |
| `signal_id` | string | yes | `SIG-W-YYYYMMDD-NNN`. |
| `disposition` | enum | yes | `acted` / `noted` / `deferred` / `info-only` / `skipped`. |
| `source` | enum | yes (v0.2+) | `INBOX_WALTER` (delivered handoff file) / `BOARD_SCAN` (found via INDEX scan) / `MANUAL` (operator-supplied). |
| `notes` | free text | no | Optional. |

Header row (v0.2):
```
timestamp_read	signal_id	disposition	source	notes
```

**Migration:** existing logs (CARL/REGINALD 9-col; HAWK 4-col) are **owned by their agents** — WALTER does **not** edit them. Each agent adds `source` on its next touch; readers tolerate missing `source` (treat as `BOARD_SCAN`, the v0.1 behavior). Disposition enum unchanged from v0.1 (see table below).

| Disposition | Meaning |
|-------------|---------|
| `acted` | Incorporated into this session's analysis / decision / downstream dispatch. |
| `noted` | Read and filed; no action, no follow-up. |
| `deferred` | Will revisit — use `notes` for when/why. |
| `info-only` | Named in `info`; read for awareness, no action expected. |
| `skipped` | Judged irrelevant despite routing — rare; paper trail for routing-disagreement audit. |

### 5.1 FILED ≠ CONSUMED — an undeclared `git mv` is not a consumption record (added v0.15, 2026-08-07; TERRY's §8 defect against the S7 proposal, PROME-directed to record now)

**The pending P3/S7 proposal** (`06_proposals/01_WALTER_routing-lane-proposals.md`) would redefine the consumption record as **the `git mv` itself**, on the grounds that it carries an author, a timestamp and a message. **The author half does not hold in this repo, and TERRY produced the counterexample from its own lane.**

Commit `9be6a5ee6` (2026-07-10, *"WALTER 7/11: BOARD-consumption cleanup — archive stale/aware handoffs"*) moved **six items out of TERRY's inbox into TERRY's `processed/`**: `SIG-W-20260627-002`, `-20260628-004`, `-008`, `-009`, `-010`, `-20260702-001`. **A WALTER session filed TERRY's mail.** None of the six appears on any TERRY surface. Under the redefinition all six would read as TERRY consumption — and this is worse than the §3.5.2 spawned-instance case, because there at least *somebody read the item*.

**It cannot be filtered by authorship, structurally:** every agent in this fleet commits as the same git identity (`williepowen-debug <williepowen@gmail.com>`, verified on that commit). `git log --author` cannot separate a WALTER sweep from a TERRY consumption **anywhere in this repo**. The only remaining discriminator is prose in the commit subject — a recogniser over free text, which is the class that recurs.

**Therefore, binding on any future build of the git-derived record:**

> **A `git mv` into `processed/` is a CONSUMPTION record only when the moving commit DECLARES the consuming agent** — a `consume:<AGENT>` token in the subject, or a one-line append to `processed/.consumed.tsv` written by the mover. **A move with no declaration is `FILED`, not `CONSUMED`.**

Two states, machine-distinguishable, and **no new ledger for the 14 recipients P3 correctly refuses to burden.** Without it, S7 would hand S1 a measurement that reports six items as read by a desk that never opened them — and S1's entire value is that its output is a **fact**, not a status.

**Status: BUILT 2026-08-20 (v0.19, Will-directed execution of the 8/08 forum-carry packet).** The declaration grammar, precisely: **a moving commit is a CONSUMPTION record iff (a) its message (subject or body) contains the literal token `consume:<AGENT>`** (case-insensitive on the token, `<AGENT>` = the owner of the processed/ dir the file moved into), **or (b) the same commit appends to that dir's `processed/.consumed.tsv`.** Anything else is FILED. Enforced by `walter_doctor` **`filed_vs_consumed`**: undeclared moves dated on/after 2026-08-20 flag LOW by name; **moves before that date predate the grammar and are counted as an upper bound only, never flagged** — a ruling governs the next write, not the existing state. First live run: 9 declared-consumed, 114 pre-grammar, 0 undeclared. **The consumption numbers in the 2026-08-07 forum posts predate this distinction and do not separate FILED from CONSUMED** — they should be read as an upper bound on consumption until the declaration ships.

---

## 6. Telemetry — ships immediately (the anti-rot safeguard)

Two read-only checks in `walter_doctor.py` (also runnable by PROME via the portable-python fallback, §10). This is the single safeguard that stops a repeat of v0.1's silent stall.

### 6.1 `delivered_but_unconsumed`
For each `AGENTS/*/inbox/WALTER/*.md` not in `processed/`: a **delivered** handoff (on origin) older than **N days** (default **N=2**, configurable) → flag. Until the recipient's Phase-2 consume boot-step is installed, nothing moves to `processed/`, so this surfaces the consumption gap per recipient — exactly the intended visibility.

### 6.2 `written_but_undelivered` (git-derived)
For each non-`processed/` handoff file: derive push/origin state **read-only from git** (a handoff in commits ahead of `origin/master`, or not reachable from origin, = not delivered):
- **Committed-but-not-on-origin** → **MED** (genuinely undelivered; needs the §3.4 push). MED escalates for FLASH/IMMEDIATE precedence.
- **Uncommitted (`WRITTEN`)** → LOW (mid-session transient).
- If `origin/master` ref is unavailable (fresh/shallow clone) → INFO "origin ref unavailable, sync state underivable" (per `[[finding_shallow_clone_false_fork]]` — don't assert divergence on a missing ref).

---

## 7. Sync & push authority

WALTER commits locally; **pushing is Will-coordinated** (a Will-opened window or the push-train; root CLAUDE.md + auto-memory `[[feedback_defer_push_coordinate]]`). The single standing exception is the §3.4 FLASH/IMMEDIATE clean-tree scoped-push via the `safe-push.sh` ff-gate — **WALTER-self-authorized on a verified-clean tree** (0g, Will-ratified 2026-06-26; PROME is no longer an always-on push agent).

---

## 8. Consumption rollout — phased, but NOT open-ended

**Delivery ships first (Phase 1, this session).** Consumption is **Phase 2 — tracked and time-boxed**, because "define template, agents apply later" already failed once (v0.1 → the BRENT miss).

- **WALTER defines** the recipient consumption boot-step template (§8.1) and does **not** edit other agents' boot docs.
- **All recipients self-apply** the consume boot-step (§8.1) on next spawn — single-machine, every agent is a CC session. (The OpenClaw "PROME installs it" path is retired with the VPS.)
- **Time-box:** the `delivered_but_unconsumed` telemetry (§6.1) makes the gap visible per recipient every boot; it is the mechanism that prevents an open-ended stall.

### 8.1 Recipient consumption boot-step (template WALTER provides; others apply)

```markdown
### WALTER signal intake  (inbox/WALTER delivery lane)

At boot, after STATUS / MEMORY / LAST_COMPLETION:

1. List AGENTS/<YOU>/inbox/WALTER/*.md not yet in your board_log.tsv.
   (If board_log.tsv does not exist, create it with the v0.2 header:
    timestamp_read<TAB>signal_id<TAB>disposition<TAB>source<TAB>notes)
2. For each: read it, decide disposition (acted/noted/deferred/info-only/skipped),
   append a row to board_log.tsv with source=INBOX_WALTER,
   then `git mv` the file to inbox/WALTER/processed/.
3. Let `acted` items inform this session.
```

(`git mv`, not bash `mv`, per auto-memory `[[feedback_git_mv_for_inbox_processing]]` — bash `mv` leaves the deletion unstaged.)

**Note vs the v0.1 BOARD-scan boot-step:** v0.1 had recipients scan `/BOARD/INDEX.md` for rows naming them. v0.2's delivery lane replaces the scan with a directory list of files WALTER actively delivered — cheaper and gap-visible. An agent may run both (scan as a backstop), logging `source` accordingly.

---

## 9. Run mode — Full WALTER only

**Quick WALTER was RETIRED 2026-06-26** (0d, Will-ratified). It was a PROME-spawned, VPS-resident route-only mode — made moot by the OpenClaw cut. Its historical guardrails (registry-only RED-FT/REG-T/safety-net routing, canonical-lane discipline, the Iran-anchor guard, UTC-stamp discipline) live in git history; they no longer gate a live mode. UTC-`Z` timestamp discipline still applies to all BOARD/delivery artifacts.

- **Full WALTER** (Will spawns) is the **only** mode: everything — BOARD curation, registry refresh, anchor re-verify, audits, liaisons, full boot + closeout. Owns reconciliation.

---

## 10. Portability

Tools invoke with the portable-python fallback (also in CLAUDE.md boot step 0.5) so they run whether or not `.venv` is present:

```sh
PYTHON="${PYTHON:-python3}"
[ -x .venv/bin/python3 ] && PYTHON=.venv/bin/python3
$PYTHON AGENTS/WALTER/tools/walter_doctor.py
```

`walter_doctor.py` is **stdlib-only** (runs anywhere `python3` exists). The market-data threshold scan (CLAUDE.md step 6c, `dashboard.py`) needs the venv libs — confirm the venv exists wherever that scan runs.

---

## 11. Git scope + guardrails

WALTER may write only to: **`/BOARD/`**, **`AGENTS/WALTER/`**, and **`AGENTS/{RECIPIENT}/inbox/WALTER/`** (a second WALTER shared-write zone, same class as `handoff_WALTER/`). WALTER **never** edits a recipient's `STATUS` / `CLAUDE` / `MEMORY` / `board_log.tsv` / `processed/` contents — agents own consumption; WALTER owns delivery. Commit by **explicit pathspec** (per file), never `git add` a whole folder (per auto-memory `[[finding_pathspec_commit_race_safety]]`).

---

## 12. Messaging-overhaul superseding note

Auto-memory `[[project_messaging_overhaul]]` ("don't patch inbox/outbox/HERMES hygiene — file-based messaging being replaced") and `[[project_walter_cop_direction]]` ("don't build full inbox infra yet") are **superseded ONLY for this narrow WALTER signal-delivery lane** (create-only, per-signal, telemetry-audited). Confirmed intentional by Will 2026-06-17. This does **not** revive general inbox/outbox/HERMES infra; those memories stand for everything else. The earlier caution was about building *unguarded* inbox infra — the §6 telemetry is exactly the guard it wanted, which is why the reversal is scoped and safe.

---

## 13. Phase-1 acceptance checks ("done")

- [x] WALTER routes a signal → BOARD file + INDEX row + `route_log` row + delivery file(s) in each recipient's `inbox/WALTER/` + `delivery_log` row(s). *(Phase-1 shipped; Quick-WALTER retired 2026-06-26.)*
- [x] BOARD still reconciles (ToC = sections = files). *(verified 2026-07-03 — doctor `board_reconcile` ✓ at 434.)*
- [x] `walter_doctor` runs via portable python and includes both new checks (`delivered_but_unconsumed` + git-derived `written_but_undelivered`). *(both live + running every boot.)*
- [x] BRENT -001 / HAWK -002 audited; backfill handoff files created (narrow — those two only). *(delivery_log confirms both created 2026-06-17, COMMITTED — closed the structural BRENT miss.)*
- [x] Nothing claims `consumed` (Phase 2 not shipped). *(satisfied at Phase-1 ship; Phase-2 consume has since rolled to 9 agents, correctly logged.)*
- [x] Concise diff-stat shown; no push until Will/PROME approve. *(standing process criterion.)*

*(All boxes ticked/verified 2026-07-03 arch/infra audit — Phase-1 acceptance complete.)*

---

## 14. Future extensions (deferred)

- Cross-agent "0 consumers after 7 days" routing-gap telemetry (now partially covered by §6.1).
- Disposition analytics (skipped-rate → persistent mis-routing detection).
- ~~COP integration: per-agent "unread WALTER-delivery count" when COP resumes.~~ *(DROPPED 2026-07-03 — COP decommissioned 2026-06-28; dead conditional.)*

---

## Version History

- **v0.21** — 2026-08-26 — **§3.5.5's NON-RENEWABLE FALSIFIER FIRED; REVERT TO THE RED-CLASS EXEMPTION EXECUTED (mechanical execution of the TERRY-ratified, Will-confirmed remedy).** Trigger: `SIG-W-20260822-002-CORRECTION` (`action: TERRY`) unconsumed ~78h at the 8/26 boot + the S1 owner-unconsumed line naming TERRY. TERRY joins the exemption set (no handoffs / no delivery rows; BOARD + route_log written); T-1/T-2/T-3 retired as delivery gates, text retained. **Exemption-by-falsifier, NOT pull-complete-warrant — stated in the member bullet so the warrant re-point cannot be read as covering TERRY.** Same session: the enforcing doctor check was found BLIND to the very rows it graded (`fromisoformat` silently skipped `~HH:1xZ` stamps → "falsifier unfired" over a met condition); parser fallback shipped + exact-minute TSV stamps mandated. Doctor `PULL_COMPLETE` +TERRY. Pairs CHECKLIST v0.38 + ROUTING_TABLE v0.31; root CLAUDE.md's "CARL + RED + PROME" mirror is Will-gated and FLAGGED, not edited. **[CORRECTED same-day, PROME-verified repo-wide grep: NO such root line exists — the mirror is WALTER's own `CLAUDE.md` line 17 (IDENTITY delivery-layer bullet), WALTER-owned and fixed with this version. Nothing is queued to Will. The false flag was a mis-attributed referent — [[finding_instrument_reports_clean_against_the_wrong_reference]] class, mine.]**
- **v0.20** — 2026-08-23 — **§3.5.7 THE DARK-OWNER DOORBELL, WALTER's half + the Will-directed orchestration-era retune.** Encodes the 8/23 ruling (adopt + 3 amendments + 4 riders) and then re-calibrates it the same day on Will's word, because the two-tier orchestration ruling changed the PRICE behind the gate: the remedy went from waking a whole desk to a bounded, whole-inbox-draining subagent touch. **Unit of decision moves ITEM → DESK** (the action item is the trigger, the backlog is the yield); **new P0 precondition — desk must not be IN-FLIGHT** (bought pilot day one: SAM respawned while alive, two sessions on one desk, caught by SAM-2 under Critical Rule #2); **new leg 3b — cadence-is-the-deadline**, which is the first limb that can reach the no-clock backlog desks the ruling itself named as the real problem (v1 scored 1-of-7 on the 8/22 night and could not reach HENRY/BROCK by construction; v2 ≈ 3-of-7). Rule 6b keeps the letter; this section points and does not restate. Miss + declined counters defined; the ⅓ tightener stays UNWIRED pending a base rate, and v1/v2 doorbells are two populations the 8/28 soak must not pool.
- **v0.19** — 2026-08-20 — **The 8/08 forum-carry builds land (Will-directed): §3.5 WARRANT RE-POINT + §3.5.5 S1 BUILT + §5.1 S7 BUILT.** ① §3.5's justification no longer says "whole-INDEX BOARD diff" (INDEX is ~19× any reader's cap — an unrunnable phrase); it cites what the qualifying tooling actually does (file-parse past a cursor / ID-diff vs ledger). Exemption membership unchanged. ② §3.5.5 gains the inverted-token declaration convention (notes cell begins `T-1`/`T-2`/`T-3`; absence = override; legacy rows graded by the `TERRY-OVERRIDE` prefix) enforced by new doctor check `terry_override_ratio` incl. the 72h revert falsifier as a separate event test. ③ §5.1's `consume:<AGENT>` grammar ships with doctor check `filed_vs_consumed` (undeclared post-8/20 moves flag; pre-grammar moves are an upper bound, never flagged). Pairs FORMAT_SPEC v0.18 (`entities:` mandatory at dispatch) + CHECKLIST v0.35 + doctor 27→30 checks.
- **v0.18** — 2026-08-18 — **§3.6.2 STATE THE DIRECTION, NOT ONLY THE NUMBER** (BOND's rule, adopted): a correction marker whose figure had conclusions built on it must say whether they HOLD / WEAKEN / FLIP — a consumer cannot infer conclusion-inversion from a corrected number alone. Corollary: ship a retraction as its OWN packet. Binds WALTER hardest because marker volume concentrates the reader exposure here. *(History entry backfilled 2026-08-20 — the bump landed in the header and §3.6.2 but was never written here; same rot class as the v0.13 note below records.)*
- **v0.17** — 2026-08-12 — **§3.5.6 the pull-complete exemption's failure mode MATERIALISED, disclosed by the exempt recipient**: RED skipped its boot BOARD scan — its sole WALTER channel — and two `action:[RED]` signals sat unread; the exemption removes the very artifact that would show the skip, so a skipped scan and a clean scan are indistinguishable. Recorded, no behaviour change; three options tabled for Will. *(History entry backfilled 2026-08-20, as above.)*
- **v0.16** — 2026-08-07 — **⚖️ TERRY's override clause RATIFIED, replacing WALTER's provisional wording** (TERRY 2026-08-07 via PROME, its exact terms, graded as written): **ratio ≤10%, denominator trailing 90 days (one quarter), activation n≥10 dispatches in the window, n=1 report to TERRY MANDATORY (`TERRY-OVERRIDE` prefix stands), breach ⇒ a MANDATORY READ OF THE OVERRIDE LOG — never an automatic widening of T-1/T-2/T-3.** **90d not 30d because at ~3 dispatches per 30 days the n≥10 activation is UNREACHABLE BY CONSTRUCTION** — a no-verdict band that never ends, the same defect class as the S2 `NONE` branch; 90d is the smallest satisfiable window. **Ratio not absolute count** because the quantity being measured is a RATE of rule-misfit, and an absolute cap tightens silently as volume grows. **TERRY's guard on its own clause:** the denominator is WALTER's volume, so the rule can be tripped by its own success — a quiet quarter shrinks the denominator and inflates the ratio on the same override count; hence read-the-log, never auto-widen. **🔴 TWO CLOCKS, DELIBERATELY UNHARMONISED — do not "fix" this:** the override clause is 90d/ratio/n≥10; the revert falsifier stays **30d / n=1 / no denominator**, because it is an EVENT test (one unconsumed `action:` item past 72h is a fact about a single delivery) and has no denominator problem. Recorded because a deliberate asymmetry and an overlooked one look identical to a later reader. WALTER's superseded provisional paragraph retained in-section per the additive-marker discipline. Pairs ROUTING_TABLE v0.25 + CHECKLIST v0.33; §3.5.5's main override sentence, the ROUTING_TABLE row, the CHECKLIST Phase-3.5 gate and CLAUDE.md RULE 10 all carry the 90d denominator — **four surfaces edited for one number, which is the standing cost of having put the rule on four surfaces, and is cheaper than one of them silently disagreeing.**
- **v0.15** — 2026-08-07 — **NEW §3.5.5 TERRY (ownership-keyed ACTION routing + total kill of the `info:` lane) and NEW §5.1 FILED ≠ CONSUMED.** Will CONFIRMED in-session on TERRY's own forum disposition (option (c)). `action: TERRY` iff T-1 named registered instrument / T-2 correction-or-retraction of a number any TERRY surface cites / T-3 closed-market event on a held-or-staged underlying; **no `info:` to TERRY, ever**; both halves or neither, because the volume cut is what pays for the action obligation. Not the RED exemption: RED's whole-`INDEX` BOARD diff regenerates the interrupt, TERRY has no BOARD differ — *TERRY can re-pull every price and cannot re-pull a retraction*, and T-2 is the class `consumer_check.py` is blind to by construction. Evidence: four decision-changing consumptions of `info`-labelled pushes in 14 days on TERRY's ledgers, including a no-fire on a MET trigger and a grading guard that executed 8/7, against a routing table recording the desk as consuming nothing — **WALTER's own "0 action / 32 info" count was right and the inference from it was wrong.** Accepted priced miss: an anti-action signal fails all three tests, n=1 of 32 (~3%), NOT rescued by widening T-2. Anti-ratchet: 32 deliveries/quarter → ~9–11, net −21 to −23, no new file/script/register. Desk-scoped — the fleet-wide ownership extension of §3.5.4 stays unratified and is fenced off on every surface. **§5.1 (recorded, not built):** a `git mv` into `processed/` is a CONSUMPTION record only when the moving commit DECLARES the consuming agent; undeclared = **FILED**. Every agent in this repo commits as one git identity, so `git log --author` cannot separate a WALTER housekeeping sweep from a real consumption — commit `9be6a5ee6` filed six items into TERRY's `processed/` that no TERRY surface cites, and under the pending S7 redefinition all six would read as TERRY consumption. Binding on any future build; tonight's forum consumption numbers predate the distinction and are an upper bound.
- **v0.14** — 2026-08-07 — **NEW §3.7 EXPIRED — a delivery disposition distinct from consumed and from backlog.** Will-ruled live in the FORUM system review (`FORUM/2026-08-07_system-review/`), executed same session as the first live application. **The gap:** "not consumed" covered two situations that are nothing alike — *the owner has not got to it yet* (recoverable by one launch) and *the decision it existed to inform has already been taken without it* (unrecoverable at any price) — and they are **indistinguishable on every surface we keep.** EXPIRED requires both legs: unconsumed **and** the dated consuming decision already passed. Disposition is **RETIRE, never escalate** — launching the owner buys nothing. Recorded as an additive `EXPIRED <date> — <reason>` prefix in the row's `delivery_log` `notes` cell, the delivery-layer analogue of FORMAT_SPEC v0.10's retro-applied `status:` tagging on an append-only BOARD; **`written_state` is NOT touched** (a write-time transport stamp; the handoff *was* delivered), **the handoff is NOT moved to `processed/`** (RULE 10 create-only, and it would be a §3.5.2 false-clear), and the **BOARD signal is NOT tagged `EVENT-PASSED`** unless the signal itself is now misleading (different object; a co-recipient may have consumed and graded it on time). **Every expired row of a signal gets marked, not just the one that prompted the review.** ⚠️ **Known limit declared on day one: visible on the SENDER'S side only** — handoffs are immutable to WALTER, so the owner still opens an expired item with nothing on it saying so; no clean fix inside the current delivery layer, structural answer is a declared `consuming_date` at dispatch (`06_proposals/01_WALTER_routing-lane-proposals.md` P4). **Provenance:** the category was surfaced independently and within minutes by WALTER from the delivery log (`03_silent-fires/03_WALTER_wait-cost-triage.md`) and by NEXUS from the board (*"the signal did not age, it expired"*), both applying NEXUS's wait-cost discriminator. **First application:** `SIG-W-20260730-009` → ZHAO (action) + LIQUID (info), unconsumed 8d, consuming event the 2026-07-31 BOJ; SAM consumed it in 0.5d and graded it at the print.
- **v0.13** — 2026-08-07 — **§3.6 CORRECTION LIFECYCLE + §3.6.1 BACKFILL CADENCE** (encodes Will-accepted RAV roster-plan Ruling #4 via PROME 2026-08-05). The publisher of a figure owns downstream PROPAGATION (root step 1c / `consumer_check` + packets); WALTER owns BOARD/signal correction LINKAGE; neither substitutes for the other. Linkage is **three surfaces** — the `corrects:` header **plus** a back-marker on the corrected signal's INDEX row **plus** a banner in its file — because a `corrects:` header alone points only FORWARD and the reader who arrives at the stale signal never sees it. Backfill folded into the existing ~14d staleness sweep rather than given its own cadence. *(History entry added 2026-08-07 with v0.14 — the v0.13 bump landed in the header and in §3.6 but was never written here. Recorded rather than silently backfilled: this is the doc-mirror rot class the version-drift guard exists for, in the guard-owner's own spec.)*
- **v0.12** — 2026-07-27 — **§3.5 adds PROME to the pull-complete exemption (DISPATCHES only, info-only lines) + new §3.5.4 THE ACTION-LINE RULE.** Will-approved twice: in-session to PROME, then **re-confirmed directly to WALTER rather than accepted on relay** (a spec change to WALTER's own canonical doc). **PROME qualifies on both §3.5 preconditions, the second one measured:** `PROME/tools/board_scan.py` (every-boot `--advance`, cursor-based, parses every `BOARD/SIG-W-*.md`, complete-not-tiered — 45 signals in ~1s over 7/24→7/27, idempotent), and **0 action-line appearances out of 605 signals all-time, with the scanner `exit 1`ing if that ever changes** — the strongest case granted to date, enforced rather than assumed. **Motivation:** a 32-item PROME inbox of which 20 were info-copies whose ACTION owner already held its own copy ⇒ the inbox had become a BOARD mirror clearable only by reading it (§3.5.2); the pile was itself a bulk-sweep hazard (two signals moved to `processed/` unread, caught on a file-count mismatch). ⚠️ **Cost accepted on the record, not waved away:** reading an info-cc caught a `SIG-W-20260727-006` measurement error the same day; accepted only because WALTER found it independently ~40min later (`-016`), so the catch did not depend on PROME's copy. **§3.5.1 UNCHANGED — notes are still delivered to PROME** (both items that genuinely needed it this week were notes). **§3.5.4 is the safety precondition for every exemption, not a tidiness rule:** each exemption rests on *"never the ACTION owner ⇒ zero ACTION-miss risk,"* which is only true if the `action:`/`info:` split is accurate metadata — so **an ask directed at a named recipient puts that recipient on the `action:` line.** Defect that bought it, **raised by PROME against its own proposal**: `SIG-W-20260727-016` was `action: [RED, LIQUID]` / `info: [..., PROME]` while its §8 carried a direct operational ask to PROME as lane owner. This is §3.5.3's actionability test applied one level in (*actionable ⇒ dispatched* → *actionable **for a named recipient** ⇒ that recipient is **actioned***). `walter_doctor` `PULL_COMPLETE = {"CARL", "RED", "PROME"}`.
- **v0.11** — 2026-07-25 — **§3.5.3 THE ACTIONABILITY TEST** (Will-directed): notes are NON-ACTIONABLE CONTEXT ONLY; anything that could change what a recipient DOES is a SIGNAL and gets DISPATCHED with full BOARD + `route_log` + handoff + `delivery_log`. Test: *"if they never open this, could they later decide differently?"* — **yes or unsure → DISPATCH.** Shrinks the §3.5.1 telemetry gap rather than instrumenting it; the `note_log.tsv` trigger stays armed, and **if note volume does not fall, the test is being applied too loosely.** Evidence: 3 instances in 10 days, 2 raised by recipients (VULCAN ×2). CHECKLIST v0.28. *(Backfilled to this history 2026-07-27 — the v0.10 and v0.11 entries were missing while the header carried the bumped version.)*
- **v0.10** — 2026-07-16 — **§3.5.2: a SPAWNED INSTANCE does not consume; only the recipient's LIVE session does.** Consumption is INTEGRATION, not reading — a spawned instance can read and act but cannot fold content into its agent's canonical state, so if it marks a note `processed/` the live session's boot scan shows CLEAN and the work exists only in a report nobody opens. Authorship discipline on the spawning coordinator; **not mechanizable** (nothing distinguishes a spawned `git mv` from the live session's) ⇒ **say it in the spawn prompt.** Surfaced by VULCAN **by declining to act.** *(Backfilled 2026-07-27.)*
- **v0.9** — 2026-07-16 — **§3.5.1 scope limit: the pull-complete exemption covers DISPATCHES, not NOTES** (Will-directed, same-session). The §3.5 skip is sound only because the recipient's whole-INDEX BOARD-diff **is** the pull — handoff and scan are fed the same BOARD entry. A **non-BOARD note** (create-only `*-NOTE.md`: a mechanism/correction/cross-reference that fails Novelty as a signal but whose value-add the owner lacks — deliberately no BOARD entry / no route_log / no delivery_log) has **no BOARD entry for a BOARD-diff to find**, so the redundancy argument collapses and **the inbox is its ONLY channel**. Rule: notes to CARL/RED ARE delivered; the skip does not apply. **Names an accepted telemetry gap:** a note writes no `delivery_log` row → invisible to `delivered_but_unconsumed` AND `written_but_undelivered` = one delivery path, zero telemetry, a direct exception to the CONTRACT's instrumented-PROOF claim; tolerable at 2-notes-total volume, **escalation trigger = ~1/wk sustained OR any note found missed → add `note_log.tsv` or a `role: NOTE` delivery_log row**. Author discipline: a note to an exempt recipient must state why it's arriving in an inbox its exemption would normally make redundant (else it reads as a violation/stale artifact and gets archived unread). **Clarification only — no agent moves in/out of `PULL_COMPLETE`, doctor's set untouched, no dispatch-path rule changed.** Surfaced by the 2026-07-16 CARL retail-sales/savings breadcrumb; worked precedent 2026-07-11 CREED 1740-Broadway. No CHECKLIST bump (Phase 3.5 governs dispatch delivery; notes are not dispatches — a pointer was added).
- **v0.8** — 2026-07-09 — **§3.5 adds RED to the pull-complete exemption** (Will-approved design-walkthrough): RED runs a complete whole-INDEX BOARD scan (boot step 1.5) AND is auto-cc'd INFO-only (never ACTION) → zero ACTION-miss risk; it was 24% of delivery volume + the largest unconsumed-INFO pile. `walter_doctor` `PULL_COMPLETE = {"CARL", "RED"}`. WALTER stops writing `AGENTS/RED/inbox/WALTER/` handoffs. Also **formalized the `delivery_log.written_state` enum** (§ below): a write-time stamp, NOT a maintained lifecycle field — authoritative delivered-state is git-derived via the doctor's `written_but_undelivered` check (the 564 rows stuck at `written_not_delivered_pending_push` are expected, not a backlog; do not backfill).
- **v0.7** — 2026-07-04 — **§3.5 pull-complete recipient exemption** added (Will-approved, relayed via PROME). A recipient that runs a *complete whole-INDEX* `/BOARD/` diff-scan has a complete pull → WALTER skips its `inbox/WALTER/` handoff + `delivery_log` row (BOARD + route_log still written). First exemption: **CARL** (verified 7/4 — 22/22 ACTION already dispositioned, 0 misses). Explicitly NOT exempt: REGINALD (tiered scan; 1 un-dispositioned ACTION found) + SAM (no scan). `walter_doctor` `PULL_COMPLETE` set excludes exempt agents from `delivered_but_unconsumed` + flags residual handoffs as to-ARCHIVE. Provenance: WALTER↔PROME consume-step reconciliation 2026-07-04 (the "asymmetric-records" class; CARL/REGINALD asymmetry surfaced by the tiered-vs-complete distinction).
- **v0.6** — 2026-06-26 — **single-machine platform-collapse** (OpenClaw/VPS cut). `delivered` collapses to one definition (committed + on-origin); §3.3 platform table retired; §3.4/§7 push authority → WALTER-self-on-clean-tree via `safe-push.sh` ff-gate (0g); §4 `recipient_platform` constant `CLAUDE_CODE` going forward (historical `OPENCLAW` rows preserved, append-only); §8 all recipients self-apply consume; §9 **Quick WALTER RETIRED** (0d); §10 VPS framing dropped. Will-ratified 2026-06-26 (Phase-0 0a/0d/0e/0f/0g). Canonical: `design/OPENCLAW_CUTOVER_PLAN.md` + `BOARD_CONSUMPTION_SPEC_v0.6_CHANGESET.md`. (v0.3–v0.5 were Quick-WALTER tightening — moot with Quick retired.)
- **v0.2** — 2026-06-17 — Delivery layer added (`inbox/WALTER/` create-only handoff files + platform-nuanced `delivered` + `delivery_log.tsv` + git-derived sync telemetry + scoped-push policy + phased-time-boxed rollout + `board_log` `source` column + Quick/Full mode reference). Per "WALTER Routing v2 — Final Design Packet", Will + PROME + ORC approved-in-principle 2026-06-17.
- **v0.1** — 2026-04-20 — initial consumption spec (`board_log.tsv` + BOARD-scan boot-step). Defaults approved by Will via Telegram msg 938. Propagation stalled → motivated v0.2.
