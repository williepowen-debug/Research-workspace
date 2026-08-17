# DELEGATION TIER — which specification questions an agent rules itself

**Owner:** DAEDALUS · **Created:** 2026-08-07 · **Status:** ADOPTED (Will, in-session, forum slate item S8, as amended).
**Provenance:** `FORUM/2026-08-07_system-review/06_proposals/02_DAEDALUS_proposal-set.md` §P4 (tests 1-4, the riders, the falsifier) · `06_proposals/04_DAEDALUS_amendments.md` §2 (test 5, the row-33 correction, the sub-item split) · `04_will-time-automation/04_NEXUS_delegation-tier-reply.md` (test 5 and the sub-item discipline are NEXUS's, adopted verbatim).
**Text mode:** STRICT (`BLUEPRINTS/STRICT_TEXT.md`) — this file is a gate spec.
**Root-canon pointer: NOT SHIPPED. Will-gated.** Agents receive this file cited in a PROME self-rule packet, not from root `CLAUDE.md`.

## Why this exists

Measured 2026-08-07: **8 of 13 unstruck `PROME/WILL_QUEUE.md` rows (62%) were type `RULE`** — specification questions escalated to Will because no agent held authority to settle a question. One row (12, HENRY) waited 10 days for permission for HENRY to read HENRY's own inbox. This tier removes that class. It grants no authority over capital, over another agent's files, or over the calibration record.

## THE FIVE TESTS

An agent may self-rule a specification question when **ALL FIVE** pass. **Any single failure sends the question to Will.** A third party grades a past ruling by answering the five questions against the diff.

| # | Test | The question a grader asks | Fails when |
|---|---|---|---|
| 1 | **SCOPE** | Does the ruling change any file outside `AGENTS/<ASKER>/`? | Any file outside the asker's own directory changes |
| 2 | **REVERSIBILITY** | Does undoing the ruling require editing more than one file? | Two or more files must change to undo it |
| 3 | **NO-CAPITAL** | Does the ruled text gate, size, select strikes for, price, or set an **exit** for a position? | Any of those five. **Exit rules count** — this clause is the correction to the OSPREY row 33 verdict, where DAEDALUS misapplied its own test on 2026-08-07 |
| 4 | **ANTI-SELF-SERVING** | After the ruling, is the agent's own falsifier easier to trigger or unchanged, and is no threshold easier to satisfy? | A falsifier becomes harder to trigger, or a threshold becomes easier to satisfy |
| 5 | **DATA-VS-INSTRUMENT** | Is the subject a property of **data** — revision handling, vintage, publication cadence, unit base, weekday convention — rather than a property of the asker's own instrument? | The subject belongs to the world. Such a question is fleet-wide by default, however local the file |

**Test 5 exists because tests 1-4 are all properties of the ASKER and none can see the subject.** MIDAS's L-15 (do thresholds grade once at publication, or re-grade on revision?) passes tests 1-4 and is fleet-wide: BLS revised May-June payrolls by −103K in the same window, and QCEW 2026-08-28 is a scheduled benchmark revision LABOR has already pre-priced. MIDAS ruling one way and LABOR the other produces two incompatible calibration conventions with no tie-breaker (PAT-076).

### Refinement — CHECK versus DO

A mechanism that only **checks** an already-ratified rule passes test 1 even when the checked rule is fleet-wide. A change to **what agents must do** fails test 1. Worked case: NEXUS brief-schema amendment 11 (`pin-follows-STATUS-HEAD`) converts a ratified requirement from remembered to checked, changes no agent's obligations, and is therefore self-rulable. Amendments 9 and 10 changed what a brief IS and correctly required Will.

### Sub-item discipline (NEXUS, adopted)

**Grade sub-items, never rows.** An agent filing a `RULE` ask with more than one sub-item files each as a separate row with its own `consumes_by` date. Measured 2026-08-07: **4 of 7 live `RULE` rows contained a self-rulable half queued behind a Will half.** A mixed row inherits the verdict of its strictest sub-item until it is split.

## RIDERS — mandatory on any self-ruling that touches a prediction, threshold, or kill condition

- **R1 — Date the re-spec.** The ruling carries the ISO date it was made.
- **R2 — Preserve the superseded text verbatim, in place**, marked `SUPERSEDED <YYYY-MM-DD>`. R2 is the PAT-076 tie-breaker, not bookkeeping.
- **R3 — Do not move a confidence, probability, or weight in the same edit as a re-spec.** Split the work into two dated edits. R3 is what keeps a broken-instrument repair from becoming a grade.

## RECORD FORMAT

The agent writes the ruling into the file the ruling changes, as one dated block:

```
**SELF-RULED <YYYY-MM-DD> (DELEGATION_TIER):** <the question, one sentence>
→ <the ruling, one sentence>. Tests 1-5 PASS. Riders: <R1,R2,R3 | n/a>.
SUPERSEDED <YYYY-MM-DD>: "<prior text, verbatim>"
```

## DIGEST — `AGENTS/SELF_RULINGS.tsv`

**The ruling agent appends its own row at ruling time and commits that row itself**, path-scoped, under root `CLAUDE.md` Git Protocol carve-out ② (self-authored rows in a shared cross-agent log; `AGENTS/SIGNALS.md` is the class precedent, which is why the file sits at `AGENTS/` and not inside `PROME/`).

Columns: `date · agent · question · ruling · tests_passed · record_path · riders_applied`

**Why the author writes it, and not PROME from a packet:** a digest assembled from packets fails whenever the packet is not sent, which is the orphan class this fleet has fixed three times and not extinguished (measured 2026-08-07: 0 orphans in 932 ledgered handoff deliveries against a still-live orphan rate in the unledgered packet lane). Binding the record to the act of ruling removes the failure mode instead of detecting it. **PROME reads the file at boot and rolls new rows into Will's digest. PROME never authors a row.**

## FALSIFIER

> **If within 60 days ANY self-ruling is reversed by Will, the tier narrows or dies. One reversal, not a rate.**

Grade on **2026-10-06**. The reversal count is read from `AGENTS/SELF_RULINGS.tsv` against Will's rulings.

## WHAT THIS IS NOT

- Not authority over another agent's files. Cross-agent edits keep both AUTHORITY guards (permission AND idle target).
- Not authority over capital, in any form, at any size.
- Not authority to grade, resolve, or re-mark a prediction. Repairing a broken instrument under R1-R3 is not grading it.
- Not a licence to skip the record. **An unrecorded self-ruling is a violation of the tier, not an exercise of it.**
- **Not exercisable inside a forum session** (Will-ratified 2026-08-10). Two independent grounds, either sufficient: the record requirement cannot be met (forum charters bar participant commits, and an unrecorded self-ruling is a violation, not an exercise — see the line above), and the venue is contaminated (peers are auditing the frozen spec the agent would be re-specifying). In-forum the agent states the question, rules nothing, and defers to its next dedicated session. Mirror: `FORUM/CHARTER_TEMPLATE.md` rule 13. *(Provenance: MIDAS [recordability ground] and BRENT [contamination ground] derived the exclusion independently, blind, in the same phase — forum 4, 2026-08-10; zero self-rulings attempted. The contamination ground is the more general — it survives a hypothetical charter that allowed participant commits.)*
