# ACCEPTANCE — `board_scan.py`: consume only PUBLISHED signals, remember what was consumed, surface late arrivals (prome-2a)

**Written:** 2026-09-30 21:59 ET (`date`), BEFORE any edit to `PROME/tools/board_scan.py`.
**reads: 0**

**Trigger:** Will, PROME window, 2026-09-30 21:52 ET, verbatim *"I have some feedback from CATO I would like to investigate and fix if true"*. CATO's finding RC1: `AGENTS/CATO/runs/2026-09-30_2132_system-recent-commits-review.md` (433084d2b). Reproduced by PROME the same hour with CATO's probe (`…_system-commit-probe.py`): an unfinished file advanced the cursor 004 → 005 at rc 0; the same file completed with `action: [PROME]` then read "nothing new"; a lower ID published after a higher one stayed hidden. Live incident: 2026-09-30 ~20:3x ET, three crash drafts (no missed action demonstrated).

**Defect in its own terms:** the scanner treats *a file exists on disk* as *the signal is published*, and *an ID at or below the high-water mark* as *this signal was consumed*. Both are false at exactly the moments that matter: an interrupted publication, and publication out of ID order.

**Design chosen (and why):** *published* = the file is committed at HEAD and unmodified in the working tree, with complete stamped metadata — WALTER stamps in the same command as the commit, so the commit is the publication act, and `BOARD/INDEX.md` is not read (WALTER's index design documents that this scanner never reads it). *Consumed* = remembered per FILE in `PROME/state/board_consumed.tsv`, so the pass becomes the ID-level diff WALTER's spec §3.5 asks for. `board_cursor.txt` stays as a display high-water mark.

## Acceptance conditions

1. **Ordinary behaviour preserved.** A published info/other signal is listed; `--advance` consumes it; the next run says nothing new. A published signal with PROME on `action:` returns rc 1 and is NOT consumed by `--advance` alone; `--advance --ack-actions` consumes it. A bare run writes no state.
2. **An unpublished file is never consumed.** Untracked, staged-uncommitted, or modified against HEAD ⇒ reported as held back, consumed under NO flag (including `--ack-actions`); once committed it surfaces as new — at rc 1 if PROME is on its action line.
3. **A committed file with incomplete metadata is a hard stop, never a silent consume.** No closed frontmatter · no `signal_id` · `signal_id` ≠ the filename's ID · `action` or `info` missing or not a bracketed list · empty `time_dispatched` ⇒ listed UNREADABLE, rc 1 (routing unknown), not consumed by `--advance`; only `--advance --ack-actions` (a human read it) consumes it.
4. **A late lower ID surfaces.** After a higher ID is consumed, a newly published lower ID is listed, at rc 1 if PROME is on its action line.
5. **A late action on a consumed signal surfaces.** A consumed signal whose committed content later puts PROME on `action:` re-surfaces at rc 1.
6. **Migration loses nothing and re-announces nothing.** With the legacy cursor and no ledger, every PUBLISHED file at or below the cursor is seeded as consumed (no flood of 1,100 old signals); published files above it are new; a file at or below the cursor that is unpublished at seeding stays unconsumed and surfaces when published. The seed is persisted only by `--advance`.
7. **Fail closed.** Git unavailable or failing, no `BOARD/`, or an unreadable or malformed ledger ⇒ rc 2 and NO state write.
8. **Interruption safety.** State is written atomically (temp file + replace). Nothing is consumed that the same run did not display.
9. **Interfaces preserved.** `parse_front`, `sig_key`, `clean` import and behave as before (`exempt_gap.py` imports them) · flags unchanged · `board_cursor.txt` still written on advance · exit codes 0 / 1 / 2 keep their meaning · `--audit` unchanged.
10. **Two published files sharing one ID both surface** (the ledger is keyed by file, so a reused ID cannot hide a second signal).

## Neighbours (WQ-229 — all five considered)
- **Ordinary:** AC1.
- **Overlap:** AC2 (tracked at HEAD *and* modified in the working tree; staged *and* uncommitted) · AC5 (consumed *and* changed) · AC6 (at or below the cursor *and* unpublished) · AC10 (one ID, two files).
- **Wrong owner:** WALTER owns `BOARD/` and publication; this tool writes only under `PROME/state/` and never under `BOARD/`. Signals routed to other desks are listed, never consumed on their behalf — other desks' ledgers are untouched. No further case: single-consumer state.
- **Missing information:** AC3 (metadata absent) · AC7 (no git, no ledger integrity) · no cursor and no ledger = a first run, everything published is new (pre-existing behaviour, kept).
- **Concurrent activity:** WALTER publishing mid-scan ⇒ the file is held this run and surfaces next run (AC2). Two PROME scans writing at once: N/A as a tested case — one PROME session at a time by design; the write is atomic and a lost update can only RE-surface a signal, never skip one (the safe direction, stated rather than simulated).

## Tests
`PROME/tools/tests/test_board_scan_publication.py` — throwaway git repositories only; one test falsifies the guard itself (publication check disabled ⇒ the draft IS consumed).

## State
*(filled after the work — IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED, never merged)*
