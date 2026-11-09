# WQ-655 — NOW consolidation: migration proposal (PROPOSAL — direction approved, migration NOT approved)

**Authority:** WQ-655, Will 2026-11-09 14:21 ET (`PROME/proposals/2026-11-09_wq655-fleet-view-phase1-RULED.md`): *"prepare a concrete NOW consolidation proposal. I approve the direction, but not the migration yet."* Author PROME prome-6f. Nothing below has been executed. Inventory taken 2026-11-09 14:3x ET with `git grep` at HEAD 5bd30b6b6e.

**Objective (Will's words):** NOW owns immediate priorities and dependencies, referencing existing ledgers rather than copying their state; eliminate competing current-state sections; less effort reconstructing state, more useful research.

## 0. Recommendation in one paragraph
Keep the file name `PROME/SCRATCH.md` and rebuild its contents as the NOW page. Renaming is optional; keeping the name avoids rewriting about 30 live references plus hundreds of historical links. Slim `PROME/STATUS.md` to its standing parts (restrictions, standing readings, spine-audit stamp, surfaces), which other desks also read. Retire `PROME/HANDOFF.md` as a boot read: its session entries already duplicate the daily notes (`memory/YYYY-MM-DD.md`), and its resume pointers become NOW's header. Every carried line in SCRATCH, HANDOFF and STATUS gets a named authoritative home before it leaves (section 2). History is preserved by one verbatim snapshot plus the daily notes and git. No new checker; existing generated blocks move, they are not rebuilt.

## 1. The NOW page (the new SCRATCH), target about 8 KB, no history paragraphs

| Section | Holds | Source / rule |
|---|---|---|
| Header | Updated (stamp from `date`), session id, machine, last daily-note link | hand, one line |
| **Next, in order** | ≤ 10 ranked actions, each naming its ledger key (DOCKET L#, GATES id, WQ-n, FORGE D-n) or "no row: <reason>" | hand; references, never copies state |
| **Waiting on / dependencies** | who owes what, and when PROME messages them (e.g. SAM after SoftBank 01:30 ET) | hand, written as it happens |
| **Open with Will** | the generated `willq_view.py` block (moved from today's "Pending Will") + the one HANDS-parked line | generated, unchanged tool |
| **Book** | the generated book line (`will_brief.py --book-line`) + a pointer to FORGE | generated; positions stay in FORGE |
| **This session** | session-bound counts and limits (launches, C9 count, read-episode counts, restart checkpoint) | hand; reset at closeout, carried only by the restart-checkpoint rule |
| **Standing words** | pointers only (USER.md sections, WQ rows) — no restated text | hand |
| **Links** | CALENDAR · FLEET (when built) · STATUS § Restrictions · HEARTBEAT | static |

## 2. What moves, and its authoritative destination

### 2a. From SCRATCH (current lines, HEAD 5bd30b6b6e)

| Current content | Authoritative destination | Note |
|---|---|---|
| L6 closeout narrative · L10 DAEDALUS packets consumed · L14 done at 11/8 closeout · L29/L31 rotation notes | daily note `memory/<date>.md` (already written each closeout) | history |
| L7 Will's job-application folder (laptop only) | `PROME/MACHINE_LOCAL.md` new row | machine-local fact |
| L8 position of the work (HYG ×5, oil reopen) | GATES `GATE-TERRY-HYG-FOLLOW-01`, DOCKET L1089; NOW references | already there |
| L9 next, in order | NOW § Next | the one live block |
| L11 live windows at closeout | `PROME/state/ORCH_LOG.tsv` (CLOSE rows) + the fleet view | already recorded |
| L12 standing words | NOW § Standing words as pointers → `USER.md` (quiet mode, no expiry nagging), WQ-653 row, the 11/5 "reconstruction stopped" word → a `USER.md` line | Will's preferences live in USER.md |
| L13 WQ-653 limits · OZK-09 45% question for Will | WQ-653 RECENTLY DONE row; OZK-09 question → a WILL_QUEUE row (Type DECISION or INFO) | currently a question with no row |
| L15 consumed this session | NOW § This session | session-bound |
| L16 owed from PROME (HANS and SHADE told · GIBBS L780 · FERT mirror by 12/03) | DOCKET rows (L780 exists; two new PROME rows) | today they have no row |
| L17 session timers | NOW § This session | |
| L18 laptop power settings and restore line | `PROME/MACHINE_LOCAL.md` (laptop column) | machine-local |
| L19 git guard state pointer | `PROME/STATUS.md` § Live surfaces row | standing |
| L20 memory ceiling (~20 sessions, stop at 1–2 GB free) | `PROME/MACHINE_LOCAL.md` (desktop and laptop capacity) + one line in `PROME/ORCHESTRATION_PLAYBOOK.md` § launch | it is a launch rule |
| L21 open with Will | WILL_QUEUE (rows exist: WQ-645, 615, 513) → NOW § Open with Will (generated) | |
| L22 decisions app state | `PROME/STATUS.md` § Live surfaces (it already has a Decisions-app work row) | standing |
| L23 carried from 11/5 (D-98, FORGE rotation, WALTER certify, CATO challenge, CREED terms, funding rates) | FORGE D-rows (D-98) · DOCKET rows for the rest · CATO challenge now delivered (`PROME/inbox/` 11/9) | each line gets a key or is closed |
| L24 residual desk gaps (WQ-622 set-up at WALTER, NEXUS, REGINALD; GIBBS charter; BKU) | inbox packets to each desk, or DOCKET rows | owner-held |
| L25 PROME process carry | DOCKET rows (L925 exists) · ideas list for the unruled ones | |
| L27 carried (L835, READS attestation, FALCON read cap, ORACLE collision) | DOCKET L835 · a DOCKET row for the READS attestation · FALCON's own STATUS (it carries the 158%) · ORACLE collision CLOSED today (45a7701876) | |
| § Pending Will (generated block) | NOW § Open with Will | markers move, tool unchanged |
| § Operator card (book, positions, closed trades, standing guards WQ-302/357/360/365) | book line → NOW; positions and trades → `FORGE/STATUS.md` (already the mirror); the standing guards → `PROME/ACTIVE_DECISIONS.md` GUARD rows | guards must not be lost |
| § Open carry (desk context, retired WQ-430 sequence, HEARTBEAT pointer, ARGUS follow-through, known defects, desktop recovery carry) | DOCKET rows where an obligation remains; retired items → the snapshot; HEARTBEAT pointer → NOW § Links | |
| § History and cleanup evidence | the migration snapshot | history |
| § Calendar pointer | NOW § Links | |
| § Theme homes (ELLISON, ASCL) | `PROME/STATUS.md` § Live surfaces | standing ownership |

### 2b. From HANDOFF

| Current content | Destination |
|---|---|
| Current-state line and Resume pointers | NOW header |
| The five session entries | daily notes `memory/2026-11-05.md` … `2026-11-09.md` (each entry already names its account file); retired as a section |
| Existing approvals, positions and repair order | FORGE (positions, D-rows) · WILL_QUEUE RECENTLY DONE and `proposals/*-RULED.md` (approvals) · ACTIVE_DECISIONS (TERRY acceptance guard) |
| Older unresolved continuity | DOCKET rows for what is still owed (broker unknowns are FORGE D-80/82/83/90); the rest to the snapshot |
| The file itself | kept as a short stub pointing to NOW and the daily notes (so old links resolve), no longer a boot read |

### 2c. From STATUS

| Current content | Destination |
|---|---|
| Helm-retired banner | snapshot (already ruled, WQ-461) |
| Updated / Last spine audit stamps | **stay** (the spine-audit stamp is read by BOOT step 8 and the spineaudit skill) |
| Current Work Queue (pointer table) | NOW § Next (its rows are pointers already) |
| Owner lanes table | each lane's standing instruction → the owner desk's STATUS by packet, or an ACTIVE_DECISIONS GUARD row where PROME must enforce it (DEWEY "⛔ do not spawn off the batch-2 recipe"; LIQUID re-scope; the HY re-kill pointer is already GATE-HY-REKILL) |
| **Restrictions** and **Standing readings** | **stay verbatim** — the one binding section; NOW links to it |
| Live surfaces / ownership | **stays**, gains the theme homes, decisions-app and git-guard rows |
| History and retained audit carry | snapshot |

WALTER (READS row 143) and NEXUS (row 341) read the head of `PROME/STATUS.md`; the header shape is preserved, so their reads do not change.

## 3. What needs updating (live consumers only; historical packets and plans keep their old links)

**Scripts and generated blocks**
- `PROME/tools/willq_view.py` — none if the file name stays SCRATCH; the marker block moves within the file.
- `scripts/docket_view.py` — docstring examples still name `--write PROME/SCRATCH.md`; the view now writes CALENDAR. Text fix only.
- `PROME/tools/prome_gate.py` — the WILL_QUEUE reconcile and the HANDOFF/SCRATCH comments (L49); any check keyed to HANDOFF (none found that reads it); `check_claims` path list unchanged.
- `scripts/read_cap_check.py` + `PROME/registry/READS.tsv` rows 108 (HANDOFF whole → retire), 109 (SCRATCH whole → NOW whole, new description), 114 (STATUS whole, smaller).
- `PROME/tools/argus_scope.py` perimeter / `PROME/state/argus_review.json` — names SCRATCH and HANDOFF in the recorded perimeter; update at the next recorded baseline.
- Tests that fixture these files: `test_repeat_boot.py`, `test_closeout_simplification_WQ240.py`, `test_git_guard_L294_F6.py`, `gate_fixture.py` — rerun; fix only where a path or section heading is asserted.
- `PROME/tools/fleet_dashboard.py` (retired library) parses SCRATCH's pending block — check whether `will_handbook.py` still calls that parser; if so, point it at NOW's block.

**Instructions (reference counts at HEAD)**
- `PROME/BOOT.md` (6): steps 1 (HANDOFF read → retired), 2 (SCRATCH → NOW), 4 (STATUS scope).
- `PROME/BOOT_MODULES.md`: the resume branch's checkpoint location (NOW § This session).
- `PROME/CLOSEOUT.md` (12) and `PROME/CLOSEOUT_PROCEDURES.md` (6): the HANDOFF write step retired; SCRATCH write becomes "NOW kept current; closeout trims it and writes the daily note".
- Skills, root and PROME copies kept identical: `boot` (2), `closeout` (1), `spineaudit` (2).
- `PROME/CLAUDE.md` (2): **§ Handoff Requirement** is rewritten (PROME's own charter — Will-gated).
- `PROME/SYSTEM.md` (14): Boot Trust Stack.
- `PROME/COMPLETION_SPEC.md` (5), `PROME/GIT_COORDINATION.md` (1), `PROME/ACTIVE_DECISIONS.md` (3), `AGENTS.md` (1, operating references line — root doc, Will-gated), `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` (2, DAEDALUS-owned: packet, not an edit), `MESSAGING/FIRST_ACTIVATION.md` (1, historical — leave).
- `PROME/MACHINE_LOCAL.md`, `USER.md` (Will has granted PROME edit rights), `PROME/ORCHESTRATION_PLAYBOOK.md`: receive moved lines.

## 4. How restrictions, approvals, obligations and history survive
- **Restrictions:** unchanged and in place in `PROME/STATUS.md` § Restrictions; nothing moves.
- **Approvals:** already authoritative in WILL_QUEUE RECENTLY DONE, its ledger (`PROME/registry/WQ_LEDGER.tsv`) and the `proposals/*-RULED.md` records; NOW references them.
- **Unresolved obligations:** the section-2 table is executed line by line in one pass. Every line ends in a DOCKET row, GATES row, WQ row, FORGE D-row, ACTIVE_DECISIONS guard, desk packet, NOW line or the snapshot. The pass is complete when no line of the old SCRATCH, HANDOFF and STATUS lacks a destination. This is a one-time hand mapping, not a new checker.
- **Standing guards** in the SCRATCH operator card and the STATUS owner lanes become ACTIVE_DECISIONS GUARD rows or owner-desk text, never dropped.
- **History:** one verbatim snapshot of all three files at the migration commit (`PROME/archive/NOW_MIGRATION_<date>/`, crc32 recorded) + the daily notes + git.

## 5. What can be retired, and what each supplied or caught

| Retired | What it supplied | What it caught | Why it is safe |
|---|---|---|---|
| HANDOFF as a boot read (step 1) | last 3–5 sessions in summary; resume pointers | nothing mechanically; it pointed to SCRATCH | daily notes hold the account; NOW holds the pointers |
| CLAUDE.md § Handoff Requirement (3–5 entries, archive older) | a rolling continuity log | — | replaced by "NOW current + daily note" |
| SCRATCH carry blocks (★NEXT L10–L27, § Open carry) | reminders of obligations without rows | **they hid the ORACLE collision as a note for days** | each obligation gets a ledger row, so the due-date machinery sees it |
| SCRATCH operator card | a positions glance | stale-mirror risk (it duplicated FORGE) | book line + FORGE pointer; guards to ACTIVE_DECISIONS |
| STATUS Current Work Queue + Owner lanes | a pointer index; owner standing instructions | — | pointers move to NOW; instructions to owners or guards |
| SCRATCH/STATUS rotation notes and archive indexes | provenance of rotations | — | git and the snapshot |
| *Candidate, decided after the fleet view is judged:* the spawn-slate top-block read (BOOT step 6) | due desks, receipt gaps, in-flight touches | due rows with no citing return | only if the fleet view's exception section shows the same items; otherwise kept |

## 6. Migration order, when approved
1. Snapshot the three files verbatim.
2. Execute the section-2 mapping (new DOCKET/WQ/guard rows first, then moves).
3. Rewrite SCRATCH to the section-1 structure; slim STATUS; HANDOFF becomes a stub.
4. Update the section-3 consumers (scripts and tests first, then instructions, skill copies in parity).
5. Review under PROME's charter for a canon edit: one blind read of this plan before step 1, one of the result after step 4 — no more.

## 7. Open choices for Will
1. Keep the name SCRATCH (recommended) or rename to NOW.md.
2. HANDOFF: a stub that points onward (recommended, keeps old links working) or delete.
3. The spawn-slate read: retire only if the fleet view proves it redundant (recommended) or keep regardless.
