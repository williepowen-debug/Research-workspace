# ACCEPTANCE — `board_scan.py`: consume only PUBLISHED signals, remember what was consumed, surface late arrivals (prome-2a)

**Written:** 2026-09-30 21:59 ET (`date`), BEFORE any edit to `PROME/tools/board_scan.py`.
**reads: 3 — THE EPISODE IS CLOSED (Review budget ceiling). No further correction to `board_scan.py` without Will's named authorization for a further read.**
- read 1 — 2026-09-30 22:03 → 22:18 ET, independent reader (general-purpose, Opus), 27 experiments in throwaway repos, report `…/scratchpad/reader1/REPORT.md` (session scratchpad; findings transcribed below): ❌ 6 (F1–F6) · ⚠️ 12 (F7–F18) · the live migration verified exact (1,112 rows, no action signal ever laundered by the old cursor). All six ❌ fixed 2026-09-30 22:25 ET; the fix pass is UNREVIEWED until read 2.

- read 2 — 2026-09-30 22:26 → 22:53 ET, a second independent reader (general-purpose, Opus), 13 experiment scripts and 10 mutation runs, report `…/scratchpad/reader2/REPORT.md`: F1 · F2 · F5 CLOSED; F3 · F4 · F6 PARTLY; NEW ❌ 5 — four ACTION-class (R2-1 a re-routed ask hidden by a sticky class · R2-2 amendment shapes passing quietly · R2-3 a hidden second action key in a new signal · R2-4 a filename that bricks the ledger) and one BASIS-class (R2-5 "routing unchanged" printed when it changed); ⚠️ W1–W6; live state verified exact (1,112 rows, 0 mismatches). All five ❌ and the three PARTLY findings fixed 2026-09-30 23:03 ET; this second fix pass is UNREVIEWED until read 3, which is the LAST read the budget allows.

- read 3 (FINAL) — 2026-09-30 23:03 → 23:25 ET, a third independent reader (general-purpose, Opus), 13 experiment scripts, 30 mutations, 4 differential runs against PyYAML; it could not write its report file (the harness refused), so its findings are transcribed in § Disposition after read 3 below and its scripts sit in the session scratchpad (`reader3/`). R2-4 CLOSED; R2-1 · R2-2 · R2-3 · R2-5 · F3 · F4 · F6 PARTLY; NEW ❌ 5 action-class (N-1..N-5) + 2 basis-class (N-6, N-7); ⚠️ N-8..N-14; live state exact (1,112 rows = 1,112 published blobs, 0 mismatches). Its verdict: KEEP as the blocking boot check — no weaker than v2 on any path tested; reverting would reopen R2-3, R2-4 and the seed defect. NOTHING was changed after this read.

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

## Amendments after read 2 (2026-09-30 23:03 ET) — the conditions stand except where restated here
- **One strict reader for every routing decision (R2-3 · F6).** `inspect_signal` counts every line whose key normalises to `signal_id` / `action` / `info` — indented, quoted or capitalised included — unions the names found, and makes any shape other than one plain `key: [a, b]` line per routing key a problem. PROME named on ANY action line counts as an action; PROME named unreadably is a problem. Measured before adoption: 0 of the 261 signals since 9/01 flagged; 0 non-standard routing-key lines on the whole board.
- **AC5 restated (R2-1 · R2-2 · R2-5).** A consumed signal whose committed blob changed is compared with THE BLOB IT WAS CONSUMED AT: PROME on action now and not then ⇒ late action, rc 1; any problem the old blob did not have ⇒ UNREADABLE, rc 1; otherwise quiet, and a change in PROME's routing is LISTED (class before → after), never called unchanged. Replayed over all 434 signal amendments since 2026-06-01: 434 quiet, 0 hard stops — the rule does not flood on old-format signals.
- **AC6 completed (F3 · W1).** `--seed-from-cursor` never records an action-routed file (it surfaces for acknowledgement instead) and is refused while the ledger exists on disk OR in HEAD.
- **Ledger integrity (R2-4 · F10).** Keys are percent-encoded stems, rows split on newline only, a repeated key is malformed, and the writer parses its own output back before replacing the file — a ledger the reader would reject or read differently is never written (rc 2). A published file whose name is not an ID is UNREADABLE and can be acknowledged without bricking later runs.
- **Tests (W6).** The F2 test now commits a subfolder copy with different routing; the cursor-not-UTF-8 leg runs with a ledger present and a control; R2-1..R2-5 each have a test. Fourteen mutations run against the suite: thirteen killed; one (ledger rows split with `splitlines`) is equivalent now that keys are encoded.
- **Observation, not a defect of this repair:** the strict reader treats the legacy `to:` key as action-equivalent, and two July signals (`SIG-W-20260716-001`, `-004`) name PROME on `to:`. Both predate the 7/27 exemption (delivered by inbox then) and sit consumed in the ledger as "not routed"; this is the known legacy-schema blind spot of `--audit` (DAEDALUS audit S3), unchanged.

## Residue declared after read 2 — ⚠️ findings NOT fixed
- **W2** with an absolute `GIT_DIR` exported into the tool's environment, a published action signal is listed as a held draft at rc 0. No current caller exports it (reader 2 checked the pre-commit hook and `rebase -x`). **The one known rc-0 hide path left; the fix is to scrub `GIT_DIR` / `GIT_WORK_TREE` from the environment passed to git.**
- **W5** a non-UTF-8 filename, or a directory named like a signal, is listed as held back indefinitely (nothing lost).
- Still open from read 1: F11 (placeholder stamp) · F12 (an EMPTY ledger floods; a repeated key is now rejected) · F13 (`--since` label) · F14 (held drafts absent from the gate verdict) · F16 (duplicate-ID display) · F17 (gate-isolation suite guards the cursor, not the ledger) · F18 (`PROME/BOOT.md` step 6 wording).
- Closed since read 1's residue list: **F10** (fixed with R2-4) · **F9 / W3** (blob comparison).

## Residue declared after read 1 — SUPERSEDED by the block above where they differ — ⚠️ findings NOT fixed (the read budget fixes ❌ only)
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

## Disposition after read 3 — FINAL (2026-09-30 23:27 ET; nothing below was fixed, by rule: two correction passes already made on this file, and the three-read ceiling is reached)

**STILL UNRESOLVED — action class (each reproduced by reader 3; none triggered by anything on the live board today):**
- **N-1** an ACKNOWLEDGED action signal whose ask is re-added or rewritten stays at rc 0: 'late' fires only when the consumed blob lacked PROME. Five committed amendments since July kept PROME on a signal's action line and would have passed with a count line only (`SIG-W-20260716-004` ×2 · `SIG-W-20260728-007` ×2 · `SIG-W-20260813-002`).
- **N-2** nine exotic YAML spellings that a real YAML parser reads as PROME on `action` (escapes, anchors and aliases, complex / tagged / anchored keys, a `---x:` line) are classed "not routed" with no problem code. 0 on the board.
- **N-3** a problem code the consumed blob already carried hides a NEW ask in the same field (codes are compared as strings). Exactly one consumed file is exposed, `SIG-W-20260411-002`.
- **N-4** `--seed-from-cursor` records files that name PROME on action in an unparseable form as "not routed"; its ledger-in-HEAD refusal is bypassed after `git rm` or through a symlinked state directory.
- **N-5** two committed non-UTF-8 filenames differing only in their bad bytes collapse into one entry (so W5's "nothing lost" was wrong). 0 non-ASCII names in BOARD's history.
**STILL UNRESOLVED — wrong text only:** N-6 the "(N consumed; ledger M files)" count omits rows the quiet refresh recorded · N-7 a legacy `info:` change still prints "routing unchanged" · the routing-change listing never reaches the gate verdict at rc 0 (F14).
**Weaknesses (lose nothing alone):** W2 confirmed, `GIT_WORK_TREE=<BOARD>` is a second trigger (one boot's delay; a relative `GIT_DIR`, the form git hooks export, gives rc 2) · N-8 `--ack-actions` acknowledges everything held when it runs, including a signal published after the operator looked · N-9 ledger AND cursor both lost ⇒ treated as a first run, everything floods · N-10..N-14 · tests: three behaviours have no failing test (name-union across action lines, `to:` routing, the continuation-line scan).

**WITHHELD from operational use (Review budget — withholding follows consequence):**
1. **`--seed-from-cursor` — DO NOT RUN.** A lost ledger is restored from git (`git checkout -- PROME/state/board_consumed.tsv`), never re-seeded. In this repository the flag is refused anyway while the ledger exists on disk or in HEAD.
2. **The line "N consumed signal(s) amended since consumption — PROME's routing unchanged" is NOT a finding.** When a scan prints it, list the amended signals from git and open every one that names PROME, before treating the boot as clear.
3. **An `--advance --ack-actions` run is trusted only after its own output has been read** — it acknowledges whatever is held at that moment.
**What a reader may rely on:** a signal is consumed only once committed; drafts are never consumed; a lower ID published late surfaces; a new signal in WALTER's plain schema that names PROME on `action` stops the boot; the ledger matches HEAD exactly as of the third read. WALTER's own rule still delivers every `action:` ask to `PROME/inbox/` as well (BOARD_CONSUMPTION_SPEC §3.5.8), so the scanner is not the only path for an ask — an in-place amendment of an existing signal is the case that second path does not cover.
**Next pass, in reader 3's order, as a NEW named read on Will's word:** N-1 hold · N-2 character whitelist · the W2 prefix check · N-4 seed skip · tests for the three unpinned behaviours.

## State
- **IMPLEMENTED** — `1ad0de004` (first form), reworked after read 1 (this commit).
- **TESTED (author)** — `test_board_scan_publication.py`, count by `grep -c 'def test_'`; four mutation runs each fail the suite; the reader's own experiment scripts re-run against the reworked tool reproduce none of F1–F6; the live ledger re-seeded through `--seed-from-cursor` equals the first seeding row for row (stem and class).
- **INDEPENDENTLY VERIFIED** — PARTLY, and no more than this: the migration and the live ledger (three reads, 0 mismatches each time) · the unchanged interfaces · the `read_blobs` parser · F1 · F2 · F5 · R2-4 · the changed-blob mechanics (withheld under a hold, re-fired after, missing consumed blob) · the write-back check · no state that leaves the gate stuck. Read 3 examined v3 itself, so v3 is not 'unreviewed' — it is reviewed and found incomplete.
- **STILL UNRESOLVED** — § Disposition after read 3 (N-1..N-7 and the weaknesses) plus the read-1/read-2 residue; publication semantics are WALTER's to confirm (packet). The tool stays the blocking boot check WITH those limits and the three withholdings; it is not withdrawn because every earlier version is weaker on every tested path.
