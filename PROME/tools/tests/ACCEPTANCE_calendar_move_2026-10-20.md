# ACCEPTANCE — move the generated DOCKET calendar view out of SCRATCH (2026-10-20)

**Authority:** Will 2026-10-20, 12:23 ET verbatim *"I am not sure the calendar view belongs in scratch"*; 13:18 ET option (a) *"A approved"*. Supersedes WQ-449 (keep or shrink the view inside SCRATCH).
**Defect, in its own terms:** a generated 21-day DOCKET projection (~11 KB) lived inside PROME's hand-written handoff file, so the handoff carried a generated block it does not own, and each closeout rewrote it there.

Written BEFORE editing (WQ-229).

## Acceptance conditions
1. `PROME/state/CALENDAR.md` exists, carries the `DOCKET-VIEW BEGIN/END` markers, and `scripts/docket_view.py --write PROME/state/CALENDAR.md` writes it. `--check-generated PROME/state/CALENDAR.md` passes.
2. `PROME/SCRATCH.md` no longer contains a `DOCKET-VIEW` block. One pointer line names the new file and DOCKET as the source.
3. The boot gate's "generated calendar freshness" check reads `PROME/state/CALENDAR.md` and names that path in its regenerate hint. A boot reading the old place cannot pass silently.
4. Every live instruction that told a session to write the view into SCRATCH names the new path: CLOSEOUT generated-blocks line and step command, gate hint. No live instruction is left pointing at SCRATCH for the view.
5. The boot still reports catalysts within 24h. BOOT step 2 names the new file, and READS.tsv declares it, so the boot-read manifest stays truthful and `read_cap_check --require-manifest` stays rc 0.
6. DOCKET.tsv is untouched; it remains the only source.

## Neighbours (consider, not perform)
- **Ordinary:** regenerate, then check → covered by 1 and 3.
- **Overlap:** the "handwritten calendar coverage" check also reads SCRATCH. It must not error now that the section is gone. Verify its verdict after the edit.
- **Wrong owner:** `scripts/docket_view.py` is SHARED (AUDIT_PERIMETER). It is not edited; only its target path changes.
- **Missing information:** a session that reads SCRATCH whole and expects the calendar there. Covered by the pointer line (2) and BOOT step 2 (5).
- **Concurrent activity:** other desks are live. PROME-only paths, pathspec commits.

## Addendum — fleet-doc acknowledgement sweep (Will 13:21 ET: *"make for the calendar is aknowledged/supported by boot up/close out and direction documents inside PROME"*)
- Pointed at `PROME/state/CALENDAR.md`:
  - BOOT step 2 and step 8
  - BOOT_MODULES need→read row
  - CLOSEOUT generated-blocks line, step 1 command, symmetry table (new row; DOCKET row's views)
  - SYSTEM doc table (new row; SCRATCH row no longer claims catalysts) and the canonical-sources row
  - STATUS work-queue pointer
  - boot and closeout skills, both copies, parity kept
- **Instrument defect found and fixed:** `prome_gate.check_symmetry()` harvested boot reads with `` `(?:PROME/)?[A-Z]…` ``. It could not see any path with a lowercase directory, so it passed `PROME/state/CALENDAR.md` unexamined.
  - New pattern allows lowercase segments.
  - Counterexample: with the CALENDAR row removed, the check flags it.
  - Its first honest run also surfaced `PROME/state/SPAWN_SLATE.md` and the pre-existing `PROME/BOOT_MODULES.md` gap. Both are declared one-way in CLOSEOUT.
  - Result: "9 boot-read surfaces all registered".
- State: IMPLEMENTED · TESTED. NOT independently verified (Will asked for no spawns at boot; reader offered).

## Correction — CATO result review (44ff05b5f, `AGENTS/CATO/runs/2026-10-20_calendar-review.md`)
reads: 1 (CATO, independent, result read with fresh counterexamples; Will-directed in CATO's window)
- **Calendar move: ACCEPTED by CATO** within tested scope.
- **CM1 (MEDIUM) — PROME overclaimed.** The addendum above said "with the CALENDAR row removed, the check flags it". That is false on the final snapshot. PROME's own test replaced every CALENDAR mention, not only the row. The check matched the basename anywhere in the section, so the DOCKET row's mention kept it passing.
  - **Fixed:** `symmetry_registered()` accepts only a table row's first cell or the explicit one-way line. Matching is by path, never by basename.
  - **Regression:** `test_symmetry_registration_2026-10-20.py`, 8 cases. They include CATO's row-only removal, the wrong-owner same basename, a comment mention, and the one-way path both ways.
- **CM2 (LOW) — fixed.** The SPAWN_SLATE one-way note now says the gate writes it at boot and at closeout.
- **State:** CM1/CM2 IMPLEMENTED · TESTED. The **two-correction stop has tripped on `prome_gate.py` this session**, so any further correction needs an independent read. CATO's re-review of the changed repair is the next read, on Will's direction.

## CATO read 2 — result of the CM1/CM2 repair (f07dfbc71, `PROME/inbox/2026-10-20_from-CATO_symmetry-result-and-backlog-plan-review.md`)
reads: 2. CM1 and CM2 are ACCEPTED within the current document format. 8 tests pass under ResourceWarning-as-error. **INDEPENDENTLY VERIFIED** within that scope.
**Declared residue (not fixed, disclosed):**
- **CM3:** a table row inside a fenced code example or a multiline HTML comment still counts as a registration. No such hidden row exists in the live symmetry section. It is deferred as lower-impact, and a fix needs a third read inside this episode's budget.
- The regression tests read the live documents, which is a maintenance limitation.
- `scripts/docket_view.py` help text still shows historical `--write PROME/SCRATCH.md` examples. That tool is SHARED; fix it at an authorized shared-tool touch.
