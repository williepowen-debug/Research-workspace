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
