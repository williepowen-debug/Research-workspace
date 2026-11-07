# L816: second wording amendment to the WQ-298 ③ CANNOT-FIRE bullet, canon record

**Written:** 2026-11-07, PROME, session prome-bf, laptop. **Status:** RULED by existing word: this is wording inside the rule Will ratified 2026-09-25 14:16 ET (WQ-298 ③, verbatim *"298 - approved"*). DAEDALUS's packet states "No Will decision. Both fixes are wording inside an already-ruled rule", and DOCKET L816 records that no Will decision is owed unless the plan read finds a meaning change. If the plan read finds one, this goes to Will and is not inserted.

**Source:** `PROME/inbox/processed/2026-10-23_from-DAEDALUS_L499-class2-pointer-and-two-residue-answers.md` § ACTION 2.

**Target:** `FORGE/PREDICTION_DISCIPLINE.md` line 39, the bullet beginning "An UNREACHABLE instrument marks the leg". Line 38 in the DOCKET row is the same bullet before a later line shift.

## Edit 1: a finite definition of "listed alternates"

OLD: `after the Class 6 reachability check (the publisher's API and listed alternates tried, and each attempt named) — is marked`

NEW: `after the Class 6 reachability check (the publisher's documented API or data endpoint, plus every alternate source named on the leg's own registration row or its paid-data-list row, tried, each attempt recorded as host · result code · date; an alternate named nowhere is not owed) — is marked`

## Edit 2: two window-close clauses

Inserted after the sentence `A leg left `CANNOT-FIRE` is not a resolved row, so WQ-112's scoring vintage is untouched.`:

` At window close: (a) a disjunctive kill still fires on its other legs, so one `CANNOT-FIRE` leg does not shelter the row; (b) a substitute registered after the data cannot rescue the row: observations dated before its registration never count.`

## Invariants for the plan read

1. Both edits land in one commit, on that one line, and no other byte of the file changes.
2. Neither edit changes a level, operator, instrument or consequence on any desk gate.
3. Edit 2 only states what the bullet and its neighbours already imply: disjunctive kills, the conjunctive weakest-leg rule in STATE_VOCABULARY Class 2, and the WQ-288 prospective-naming rule. A reader who finds a new obligation or a changed outcome must flag it ❌.
4. Edit 1's term "paid-data-list row" means a row of `PROME/registry/UNREACHABLE_MEASUREMENTS.tsv`, the list the bullet already names.
5. Existing grades do not change: a leg already marked `CANNOT-FIRE` under the old wording stays marked. Edit 1 sets the test from insertion forward.

## Review record

Plan read, Sonnet coldreader, 2026-11-07 10:04 ET: Edit 1 passes and Edit 2(a) passes. ❌ on Edit 2(b) as first drafted, "counts only for windows that open after its registration date": lines 38 and 39 let a prospectively registered substitute fire on later data inside the same window, so that text would change an outcome (reader's example: registered Dec 1, crosses its level Dec 15, fires today and would not under the draft). PROME confirmed this at both lines.

Disposition: per this record's own condition, the stricter window rule is NOT inserted. Edit 2(b) above is narrowed to the half that is already canon, the prospective-naming rule. DAEDALUS's stricter form stays available only on Will's word. Edit 1's host · result code · date format is a recording detail, disclosed here.

Result read, Sonnet coldreader, 2026-11-07 10:05 ET: 0 ❌. The diff is exactly the two edits on one line, and clause (b) changes no outcome against HEAD. Declared residue, not fixed, both already true at HEAD: (1) the bullet does not state the row's fate at window close when no other leg fires; DAEDALUS's packet answers it (the row resolves on its own letter, NO-VERDICT where the letter needs that leg, WQ-162); (2) "registration" is not defined as a specific date.
