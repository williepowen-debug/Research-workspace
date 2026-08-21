---
name: finding_retired_threshold_has_no_publisher
description: "A threshold scoped to a position DIES when the position exits — but retirement is a side effect of an exit, not a republished number, so nothing announces it; our staleness tooling instruments REVISED values and is structurally blind to WITHDRAWN ones"
metadata:
  node_type: memory
  type: finding
---

**A registered level that is retired rather than revised propagates indefinitely, and it propagates looking healthy.**

## The instance (WALTER, 2026-08-03)

VIOLET's gamma band — **⚠️ 7,455 warn / 🔴 7,491 falsified** — was the thesis-kill on the live position `TRY-VIOLET-VIXCS`. WALTER's registry carried it, correctly, as a live registered level.

**On 7/30 the position exited TERMINAL** (realized −$111.60). **The band retired with it.** VIOLET said so in its own STATUS (*"the flip-band machinery retired with it"*, posture FLAT); PROME's `ACTIVE_DECISIONS` row read `EXITED — TERMINAL (COMPLETED)`; HENRY's MEMORY said *"Do NOT re-raise the VIOLET gate — dead… Any sighting of 7,496/7,455/7,491 is history."*

**WALTER carried it as live anyway** — into a dispatched signal on 8/2 (`SIG-W-20260802-004`, which called 7,455 *"HENRY's LIVE WARN LEVEL"*) and into a Will-facing boot report on 8/3, before catching it at owner-file verification.

## Why it survived — and the reason is structural, not sloppiness

**VIOLET DID publish when it RE-BASED the band.** On 7/28 it sent WALTER a publisher-side sweep packet (7,496 → 7,455/7,491, *"7,496 is retired"*) — exactly the `consumer_check` discipline, and WALTER updated off it correctly.

**Nobody published when the band was RETIRED, because retirement was a SIDE EFFECT OF A POSITION EXIT rather than a republication of a number.** There was no new value to sweep for.

⇒ **`consumer_check.py` takes `--old` and `--new`. There is no `--retired`.** The entire staleness apparatus is built around *a number that changed*. A number that **stopped existing** emits nothing.

## Why the failure direction is the dangerous one

A retired threshold sitting in a downstream registry:
- **does not error** — it is well-formed
- **does not go stale-flagged** — its vintage stamp is whenever it was last correctly copied
- **does not disagree with anything** — every surface citing it agrees with every other surface citing it, because they all inherited it from the same live-at-the-time source

**Consensus among consumers is not evidence, because they are not independent — they share an upstream.** The surface reads healthy in exactly the way [[finding_test_the_guard_not_just_the_guarded]] warns about, and it waits to be cited. **The citation then looks like diligence.**

## The corollary that makes it recur: links run in the author's direction

The same session produced a second instance of the identical shape. A BOARD correction carried a machine-readable `corrects:` field naming its targets — **but nothing pointed back**, so a reader arriving at the *corrected* signal could not learn a correction existed. Two signals whose titles asserted a corporate default that never happened sat untagged for 6 and 11 days.

⇒ **A pointer written at authoring time runs in the direction the AUTHOR travels. Readers travel the other way.** Both gaps are the same defect: *the link exists, and it is absent exactly where it is used.*

## Third form, from the same day: a lesson recorded in the CATCHER's file protects nobody

**HENRY made this exact error on 7/30**, PROME caught it, and HENRY wrote a hard trigger against it into HENRY's MEMORY. **WALTER repeated it four days later** — because the correction lived in the catcher's file and never reached the consuming registry. **A correction filed where the error was CAUGHT does not reach the next agent positioned to repeat it.**

**How to apply:**
- **When a position exits TERMINAL, sweep its registered kill/warn/gate levels the way its ledger row is swept.** Retirement is a publish event; it just does not feel like one, because nothing new was computed.
- **As a consumer:** a level whose owner has no live position is suspect on its face. Before citing another agent's registered threshold, **check the position's record, not just the number's file** — the number can be current and the *object it guards* gone.
- **As a publisher:** say *"X is retired"* explicitly and route it, rather than letting the exit imply it. An uncontested silence is not a notification.
- **Design:** any correction/retirement mechanism needs a **backward** pointer, or a check that walks the forward ones. Sibling of [[finding_guard_scope_expires_at_the_fill]] — that one says a threshold needs LEVEL + INSTRUMENT + **WINDOW**; this is the window's terminal case, where the window does not merely close but **ceases to exist**, and no one is on the hook to say so.

Related: [[finding_dated_stamp_is_a_trigger_not_a_shield]] · [[finding_reconcile_match_on_key_not_substring]] · [[feedback_reconciliation_is_last_line_move_catch_upstream]]

---

## GENERALIZED 2026-08-20 (BOND) — retirement is ONE MEMBER of a four-member class, and the class is "a state change with no publisher"

Three independent reviews of one desk on one day (BOND's own boot, PROME's oversight pass, DAEDALUS's Will-directed structure review) each found a different defect. **All four turned out to be this same shape**, and the retirement case above is member 3:

| # | The state that changed | What was left saying otherwise | Undetected for |
|---|---|---|---|
| 1 | A registered **TRIGGER FIRED** (Treasury doubled a buyback cap; the vector's RED trigger read "cap LIFTED") | the vector still scored 1; the trade surface still read *"($2B cap held.)"* | 1 day |
| 2 | The **CALENDAR** crossed a position's mandated checkpoint (60-DTE on a Sep-30 option) | the checkpoint was mandated in **four** files and had **never run** | 19 days |
| 3 | A metric was **RETIRED** (an auction tail, unscoreable by construction) | the headline vector's RED threshold cell still keyed on it | 23 days |
| 4 | A **LEVEL WAS FIXED** and the distances DERIVED from it were not | "33bp to the line" / "88bp to the line", computed off superseded levels, survived every level correction on every surface | weeks |

**The unifying property: a LEVEL gate announces itself, because something recomputes it every boot. The other four kinds of input announce nothing.** Freshness tooling is built almost entirely around *a number that changed* — so a fired trigger, a crossed date, a withdrawn metric and a stale derived quantity all emit exactly zero signal while looking perfectly well-formed.

**Note the inversion that makes this worth carrying: cost and tractability are UNRELATED.** The cheapest to detect (a fired trigger, 1 day) is the hardest to automate — it needs event semantics. The most expensive (23 days) is a **grep against a declared list.**

**How to apply — the fix is a REGISTRY, not cleverness:**
- Keep a declared list of **dated checkpoints** (expiries, hard closes, deliver-by dates) and diff it against today at boot. Cheap, and it caught a 19-day-overdue mandatory review on its first run.
- Keep a declared list of **retired tokens** with the date and reason, and grep live surfaces for them. Guard the *announcements* of the retirement so the retraction itself does not fire.
- **Never store a distance — recompute it from the level.** A derived figure does not inherit a fix to the thing it derives from; fix the pair or neither.
- ⚠️ **A registry-driven check is honest only if it says so: it sees exactly what is DECLARED and nothing else.** A clean pass means *"nothing declared fired"*, never *"nothing fired"* — the same failure mode as a missing docket row, where the absent entry is invisible in a way a wrong entry never is. **Adding the row IS the work; the check is the cheap part.**
- **Supersession is a BLOCK property, not a line property.** A retained-verbatim row under a "SUPERSEDED" banner carries no guard words of its own — scope the guard to the heading, or the checker flags the archive it was told to keep.

*(BOND instance: `AGENTS/BOND/monitors/watchers.py` + `WATCH_DATES.tsv` / `RETIRED_TOKENS.tsv`, wired INTO the existing boot check so boot stays ONE invocation — a pass needing two commands gets half-run. 11 fixtures, every one a real shipped defect. It found 4 more live defects on its first run.)*

Related: [[finding_dated_carry_item_has_no_expiry_check]] · [[finding_banded_threshold_with_no_metric_surface_is_untrippable]] · [[finding_guard_correctness_and_wiring_are_independent]]

---

## Extension 2026-08-21 (ZHAO↔PROME routing seam) — member 5: a FILING MOVE is a state change with no publisher, and only the MOVER can see the collision

PROME routed cross-agent stubs citing a peer packet at its canonical `outbox/` path; **minutes later the owner, correctly following its own charter's filing convention, was about to `git mv` the packets to `outbox/delivered/`** — which would have silently killed two live cross-agent pointers before their consumers ever booted. Caught only because the mover grepped for inbound citations of the path *before* moving (and it had to think to do so — nothing prompts it).

**The general shape: a per-agent filing convention (`delivered/`, `processed/`, `archive/`) and a cross-agent citation compete, and the citation has to win — but the collision is visible ONLY to the agent doing the filing, at the moment of filing.** The citer cannot see the convention; the consumer arrives after the move; the mover is executing a rule that is locally correct. Same family as the corollary above — the pointer runs in the author's direction, and the filing convention travels the other way.

**How to apply:**
- **As the mover:** before filing a file another desk may cite, grep for inbound citations of its path. `firetime_check`'s tolerant-follow ("artifact filed to processed/ — checked there") is the model: a convention that moves files needs either a look-before-move or a checker that follows the move.
- **As the citer:** write move-tolerant citations — **owner + filename + the convention dir it may move to**, never a bare fixed path with a scheduled death.
- n=1, logged as a seam, not claimed as a fleet pattern (finder ZHAO, 2026-08-21).

**Same-hour second half (PROME error, owned — the mitigation itself demonstrated the class):** PROME wrote the move-tolerance fix, committed it LOCALLY, and messaged the mover *"your hold can release."* **The commit was not on origin — the stubs as published still hard-cited the fixed path.** Had the mover trusted the green light, the move would have produced exactly the breakage the fix was written to prevent, in the window between writing the fix and shipping it. The mover instead verified at origin, ran the push-train itself (the sanctioned mechanism), re-verified the tolerance live on both stubs, and only then moved. **The receiver-side blind spot: only the CONSUMER's view of the shared source of truth determines whether a fix is in force.** A peer's "you're clear" is a truthful report about their LOCAL state; both parties can be entirely correct while the fix is absent from where it has to be read. So the mitigation pair generalises: look-before-move (mover's side) **+ check-the-fix-is-where-the-consumer-reads (receiver's side)** — and as the FIX AUTHOR, when a message green-lights a peer action contingent on your commit, **push before sending, or say "in force after the next train" — never a bare all-clear.** [[finding_record_of_an_action_is_not_the_action]] — the commit is the record; origin is the action.

---

## Extension (VULCAN, 2026-08-21) — the publisher can be absent BY CORRECT DESIGN, and that form is worse

The WALTER instance above is **retirement-by-side-effect**: nobody published because there was no new value to publish. That is an accident of how exits work.

**There is a second form, and it is a standing condition rather than an accident: the owner DECLINES to fan out, and is RIGHT to.**

**Instance.** VULCAN's closeout doc stated the NEXUS brief-fold check as *"brief commit timestamp ≥ last STATUS commit timestamp"* — schema **Amendment 10**, delivered to VULCAN by a PROME packet on 8/4. **Amendment 11 superseded that check with a hash equality on 8/7** (a timestamp can tie, and runs non-monotonically across a rebase). VULCAN ran the retired check for **14 days**.

**Why nobody told it:** NEXUS, as schema owner-of-record, explicitly ruled that A11 must **NOT** be propagated as a per-agent closeout step — under its delegation tier, ~26 instruction edits across other agents' directories would **fail the scope test**. The amendment is *"a CHECK on an obligation §4.1 already imposes"*, enforced at the check, not by fleet-wide instruction edits.

**That ruling is correct.** And its entire cost lands on consumers, who cannot see it.

## Why this form is more dangerous than the side-effect form

- **It is not a one-off.** It recurs *every* time an owner rightly declines to fan out a refinement. Correct scoping discipline **systematically generates** unpublished supersessions.
- **Nothing anywhere errors.** The consumer's stated rule is well-formed, its local checks pass, and it is confidently wrong.
- **The consumer often has the pointer already.** VULCAN's own doc said *"schema questions → NEXUS"*. The pointer was there and was never travelled — and it was found only because an unrelated question sent VULCAN to the schema, **six hours after it had restructured the schema-governed file without opening the schema.**

## The rule that falls out — consumer-side, because it is the only side that can act

**If your own file cites another agent's rule BY NAME AND NUMBER, that citation is a POINTER YOU ARE OBLIGED TO TRAVEL AT LEAST ONCE — not a fact you inherited.** Version-numbered citations (`Amendment 10`, `decision row 19`, `§4.4`) are the highest-yield targets: a number in the citation means the owner *versions* that rule, which means it *changes*, which means your copy has a shelf life.

⚠️ **Do not wait to be told, and do not read silence as currency.** The owner's file is canonical; your copy is a cache with no invalidation.

## Sibling form, same day (VULCAN) — the surface that cannot signal its own staleness

A superseded figure survived in `workbook/FLOW.tsv` after the correction reached five narrative surfaces (STATUS, THESIS, TRADE, VX, EXIT_PROTOCOL). **A bare TSV has no date column, no `as_of`, no header and no banner — so nothing in it will ever LOOK old, and the guard must be written INTO the cell or it is not there at all.** DAEDALUS banked this as the "worst case, in-cell-guard mandatory" tier of `[[finding_record_of_an_action_is_not_the_action]]`.

⚠️ **And the automation caution that came with it:** if a checker is ever built for this, **frozen prediction baselines need an EXEMPTION, not a guard** — a graded prediction's baseline is *evidence*, so a tool that "fixes" it corrupts the calibration record while printing success. On one real sweep the raw hit count was **44 and exactly 1 was genuine**; the rest were valid guards a narrow regex missed, or frozen references that must never move.

