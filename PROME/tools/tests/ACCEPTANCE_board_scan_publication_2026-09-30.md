# ACCEPTANCE — `board_scan.py`: consume only PUBLISHED signals, remember what was consumed, surface late arrivals (prome-2a)

**Written:** 2026-09-30 21:59 ET (`date`), BEFORE any edit to `PROME/tools/board_scan.py`.
**reads: 1**
- read 1 — 2026-09-30 22:03 → 22:18 ET, independent reader (general-purpose, Opus), 27 experiments in throwaway repos, report `…/scratchpad/reader1/REPORT.md` (session scratchpad; findings transcribed below): ❌ 6 (F1–F6) · ⚠️ 12 (F7–F18) · the live migration verified exact (1,112 rows, no action signal ever laundered by the old cursor). All six ❌ fixed 2026-09-30 22:25 ET; the fix pass is UNREVIEWED until read 2.

**Trigger:** Will, PROME window, 2026-09-30 21:52 ET, verbatim *"I have some feedback from CATO I would like to investigate and fix if true"*. CATO's finding RC1: `AGENTS/CATO/runs/2026-09-30_2132_system-recent-commits-review.md` (433084d2b). Reproduced by PROME the same hour with CATO's probe (`…_system-commit-probe.py`): an unfinished file advanced the cursor 004 → 005 at rc 0; the same file completed with `action: [PROME]` then read "nothing new"; a lower ID published after a higher one stayed hidden. Live incident: 2026-09-30 ~20:3x ET, three crash drafts (no missed action demonstrated).

**Defect in its own terms:** the scanner treats *a file exists on disk* as *the signal is published*, and *an ID at or below the high-water mark* as *this signal was consumed*. Both are false at exactly the moments that matter: an interrupted publication, and publication out of ID order.

**Design chosen (and why) — AMENDED after read 1, see § Amendments:** *published* = the file is in HEAD's tree, its name AND content read from HEAD, with complete stamped metadata — WALTER stamps in the same command as the commit, so the commit is the publication act, and `BOARD/INDEX.md` is not read (WALTER's index design documents that this scanner never reads it). *Consumed* = remembered per FILE in `PROME/state/board_consumed.tsv`, so the pass becomes the ID-level diff WALTER's spec §3.5 asks for. `board_cursor.txt` stays as a display high-water mark.

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

## Amendments after read 1 (2026-09-30 22:25 ET) — the conditions above stand except where restated here
- **AC2 restated (read-1 F1 · F2 · F7 · F8).** *Published* = present in HEAD's tree; names come from `git ls-tree` (BOARD's own entries, no recursion) and content from `git cat-file`, never from the working tree. So a committed signal that is deleted locally, edited without a commit, or shadowed by a same-named file in a subfolder is still classified at its COMMITTED content; a file on disk that is not in HEAD (untracked, or staged and uncommitted) is a draft, reported as held back and consumed under no flag. The original wording — *"modified against HEAD ⇒ held back"* — is WITHDRAWN: it let an uncommitted edit hide a published action line at rc 0, against the design's own rule that the commit is the publication act.
- **AC3 extended (F6).** `signal_id`, `action` or `info` given more than once ⇒ UNREADABLE.
- **AC5 extended (F4).** A consumed signal whose committed content changed is re-examined: PROME newly on a readable action line ⇒ late action, rc 1; frontmatter no longer closed, a routing key repeated, or an action entry naming PROME in any unreadable form ⇒ UNREADABLE, rc 1. The ledger records the blob each file was consumed at; an unchanged file is never re-examined (F9).
- **AC6 restated (F3).** Migration is one explicit act, `--seed-from-cursor`, refused once a ledger exists; it lists every action-routed file it records as dispositioned. A ledger that is MISSING while a cursor exists ⇒ rc 2, nothing written — the ledger is never rebuilt implicitly. No cursor and no ledger = a first run, everything published is new.
- **AC7 extended (F5).** Git not installed, a non-UTF-8 ledger or cursor, an unwritable state directory, and any unexpected exception ⇒ rc 2, never rc 1. The module imports without git (the repository root comes from the file's own location).

## Residue declared after read 1 — ⚠️ findings NOT fixed (the read budget fixes ❌ only)
- **F10** a committed file matching the glob but not the ID pattern, once acknowledged, writes a ledger row the reader rejects ⇒ every later run rc 2 until a hand repair. Zero such names live. **The one residue item that can brick the check — first candidate for any further pass.**
- **F11** a placeholder stamp (`time_dispatched: TBD`) passes; what WALTER's unstamped drafts carry is UNKNOWN — asked of WALTER in the packet.
- **F12** an empty ledger floods every signal as new (safe direction); a duplicate stem resolves last-wins.
- **F13** the `--since` label reads "since <cursor>" and lists consumed files as new (manual mode, not used by the gate).
- **F14** held drafts do not appear in the gate verdict (the gate shows detail only on rc ≠ 0).
- **F16** two files sharing an ID print the same `signal_id` twice without the filename.
- **F17** `test_gate_isolation_L294_F7` guards the live cursor against test writes, not the ledger.
- **F18** `PROME/BOOT.md` step 6 still cites the old line numbers and "since cursor" wording — a manual edit, for the spine pass.
- Closed as a side effect of the ❌ fixes, not by separate work: **F7** and **F8** (content from HEAD) · **F9** (blob-keyed re-examination) · **F15** (no `git status`, so no index refresh or lock).

## Neighbours (WQ-229 — all five considered)
- **Ordinary:** AC1.
- **Overlap:** AC2 (tracked at HEAD *and* modified in the working tree; staged *and* uncommitted) · AC5 (consumed *and* changed) · AC6 (at or below the cursor *and* unpublished) · AC10 (one ID, two files).
- **Wrong owner:** WALTER owns `BOARD/` and publication; this tool writes only under `PROME/state/` and never under `BOARD/`. Signals routed to other desks are listed, never consumed on their behalf — other desks' ledgers are untouched. No further case: single-consumer state.
- **Missing information:** AC3 (metadata absent) · AC7 (no git, no ledger integrity) · no cursor and no ledger = a first run, everything published is new (pre-existing behaviour, kept).
- **Concurrent activity:** WALTER publishing mid-scan ⇒ the file is held this run and surfaces next run (AC2). Two PROME scans writing at once: N/A as a tested case — one PROME session at a time by design; the write is atomic and a lost update can only RE-surface a signal, never skip one (the safe direction, stated rather than simulated).

## Tests
`PROME/tools/tests/test_board_scan_publication.py` — throwaway git repositories only; one test falsifies the guard itself (publication check disabled ⇒ the draft IS consumed).

## State
- **IMPLEMENTED** — `1ad0de004` (first form), reworked after read 1 (this commit).
- **TESTED (author)** — `test_board_scan_publication.py`, count by `grep -c 'def test_'`; four mutation runs each fail the suite; the reader's own experiment scripts re-run against the reworked tool reproduce none of F1–F6; the live ledger re-seeded through `--seed-from-cursor` equals the first seeding row for row (stem and class).
- **INDEPENDENTLY VERIFIED** — NOT YET. Read 1 verified the migration and the unchanged interfaces; its six ❌ are fixed but the fix pass is unreviewed. Read 2 is next.
- **STILL UNRESOLVED** — the residue above; publication semantics are WALTER's to confirm (packet).
