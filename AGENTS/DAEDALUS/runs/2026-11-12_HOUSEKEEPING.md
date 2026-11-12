# DAEDALUS housekeeping pass — 2026-11-12

**Authority:** Will, DAEDALUS window, 2026-11-12 08:53 ET, verbatim "ok go" on the boot report's suggested pass (small owed items, own map row, then the overdue Staleness Sweep and the four overdue Production Review queues). Runtime: Claude Code, Opus 5.5 (`claude-opus-5-5`), desktop `DESKTOP-BC6EF81`. Boot gate 20261112T134831Z rc 0 (CLEAN 3, DUE 1). Raw sweep output: `runs/2026-11-12_STALENESS_EVIDENCE/`.

## 1. Small owed items

| Item | Source | Result |
|---|---|---|
| READS re-attestation | `inbox/2026-11-09_from-PROME_WQ654-READS-applied-receipt.md` | Re-enumerated (§2). One missing dependency found: `docs/GIT_WORKTREE_PROCEDURES.md`, which root `CLAUDE.md` now requires reading whole before every commit and pull. Packet to PROME carries the delta; PROME transcribes. |
| SHADE ledger registration | `inbox/2026-11-07_from-PROME_counterpart-and-reconciliation.md` item 5 | DONE. `scorecards/LEDGERS.tsv` row 31 (between SAM and VULCAN), same columns as CORAL. Dry render `scorecard.py --week-ending 2026-11-12 --no-write`: SHADE 3 rows read, 32 ledgers read, 0 CANNOT-EVALUATE; selftest 27/27. PROME may clear `forecast_report.py:18`'s SHADE note. |
| SURFACES AGENTS.md row | `inbox/2026-11-07_from-PROME_L852-L556-answers.md` ACTION 3 | DONE. Row re-cut: chain table retired by WQ-651 A (b46830e89f); State UNMECHANIZED to OWNED; residue named (roles paragraph and potash line summarize owners). Old cells to `SURFACES_HISTORY.tsv`. |
| L816 narrowing | `inbox/2026-11-07_from-PROME_L816-window-clause-not-inserted.md` | NO OBJECTION. My 10/23 draft (b) "counts only for windows that open after its registration date" was called wording-only but would change an outcome (reader's Dec 1 / Dec 15 case); PROME's narrower "observations dated before its registration never count" is the correct wording-only form. Verified at `FORGE/PREDICTION_DISCIPLINE.md:39`. Self-finding: an unreviewed correction claimed "wording only" and was not (PAT class: a correction pass is unreviewed work). |
| NEXUS B6 tie clause | same L852/L556 packet, ACTION 2 | NO-OP. `BLUEPRINTS/STRICT_TEXT.md` rule 7 (line 24) already ends "Fixed-precision series: declare the TIE convention (strictness + published precision) at registration — SPEC_LETTER_STANDARD.md SL-5". The packet's premise that rule 7 has no tie clause is wrong; no new clause (Will 2026-10-31: fewer rules). |
| L852 ACTION 1 launchers | same packet | Honoured: no CHECKS row for `agents.py`, `agents_gui.py`, `install_agents.py`, `kimi_launcher.py`. |
| ZHAO B24 write-back | `inbox/2026-11-11_from-ZHAO_B24-applied.md` | CLOSED. 711dcd8f28 on origin/master; charter step 7 states the NONE pin form (Will WQ-660 A); `scripts/brief_pin_check.py ZHAO` rc 0, OK-SAME-COMMIT edeea8381 (proves the pin, not content). Chain: harness-skips row 16 (`runs/2026-11-04_HARNESS_SKIPS_RECONCILIATION.md:46`) and disposition plan line 27 are history; closure recorded here and in STATUS. |
| WALTER SIG-W-20261110-009 | `inbox/WALTER/` | INFO, logged. Item for DAEDALUS: a relayed, unverified claim (@LimestoneHQ, 2026-11-09) that coding agents followed an outdated CLAUDE.md/AGENTS.md over the code in 90% of choices. Not verified; no action. It is the risk the READS attestation exists to reduce. |

## 2. READS re-enumeration (attestation delta)

Method: path-token diff of each boot-defining instruction surface between the 10/09 attestation base (96622a3492) and HEAD 72c4e7b4f, then a read of the new tokens in context; for moved scripts, a diff of literal file-path tokens (inputs). This session also read root CLAUDE.md, AGENTS.md, USER.md, the charter, OPERATIONS.md, STATUS, FLEET_DIRECTORY, PATTERNS_HOT, HANDOFF, all 9 inbox packets, `PROME/COMPLETION_SPEC.md` and `docs/GIT_WORKTREE_PROCEDURES.md` whole, and the playbook's Runtime mechanics and Cross-session sections.

| Surface (moved since 10/09) | New path tokens | Dependency verdict |
|---|---|---|
| root `CLAUDE.md` | `docs/GIT_WORKTREE_PROCEDURES.md`; `KERNEL/GATE_C_C7_RUNBOOK.md`; `FORUM/README.md`; a ruling record | **NEW: GIT_WORKTREE_PROCEDURES read whole before commit/pull** (4,007 B, 12% of budget). KERNEL runbook = PROME custody only (N/A). FORUM README = design pointer (N/A). |
| `AGENTS.md` | `PROME/SCRATCH.md` | pointer (N/A) |
| `USER.md` | 6 record/pointer paths | records cited for provenance (N/A) |
| `PROME/COMPLETION_SPEC.md` | `FORGE/PREDICTION_DISCIPLINE.md` | registration rule for PROME (N/A at boot) |
| `PROME/ORCHESTRATION_PLAYBOOK.md` | `MACHINE_LOCAL.md`, `ORCH_INFLIGHT.md`, `orch_log.py` | PROME orchestration (N/A) |
| `OPERATIONS.md` | archive/receipt pointers; Navigation names `HANDOFF.md` | **Declare HANDOFF.md** as read in practice (13,526 B, 42%); OPERATIONS says it adds no mandatory boot file, so declared `whole` at the navigation step, not a SPAWN step. |
| `scripts/read_cap_check.py` | test fixtures + WALTER signal_read_check | no new DAEDALUS input |
| `corrections_boot_check.py`, `complete_check.py`, `docket_owed.py`, `docket_view.py`, `ROSTER.md` | none / pointers | no new input |

Other READS findings for PROME: row 292 (`profile_clock_check.py`, mode `RETIRED-2026-11-09`) fails `reads_check.py` SCHEMA ("BASIS row must carry mode 'boot-defining'"); the tool accepts RETIRED only on READ rows. Row 286 source-step key should move to `DAEDALUS:sweeps/PRODUCTION_REVIEW-1`. Basis hashes refreshed in `registry/basis-hashes.json` (attested 2026-11-12); hashes identify versions, not correctness.

## 3. Fleet Staleness Sweep #7 (cadence 21d, last 10/21, +1d)

| Mode | Flags | Note |
|---|---|---|
| default | 6 ledgers at 6 desks (10/21: 31 at 7) | classified below |
| trade | 2 (CORAL, MARCO TRADE.md) | 27 agents graded; 16 matched no trade surface and are NOT certified |
| abs-floor | identical to default | — |
| strict | 30 at 19 desks, 24 strict-only, mostly `SCHEMA.tsv` (+41 to +245d) and named archives | candidates; a schema file is static by design |
| writes | 62 at 17 desks, 56 writes-only | candidates for owner cadence confirmation, not defects |

| Flag | Class | Disposition |
|---|---|---|
| MARCO `workbook/VX.tsv` +32d | **REAL, one row** (corrected after review, § 6) | The header is right by its own rule (`VX.tsv:5`: the date is the OLDEST live-and-tracked vector's Last Updated, not the last edit). That row is `VX-MARCO-SFE-03` (Florida Citizens policies in force, 8/31 data, reconciled 10/10), not tagged STALE BY DESIGN. Other rows were refreshed through 11/11. Packet to MARCO: refresh SFE-03 or tag it STALE BY DESIGN with its next print. |
| SAM `workbook/BIS_GLI.tsv` +58d | CANDIDATE | Quarterly BIS series, 2026-Q1 rows pulled 9/15; no Cadence declaration. Owner checks whether Q2 2026 is published, then refreshes or declares `SCHEDULED`. Via PROME rollup. |
| CORAL `workbook/FL_ENROLLMENT.tsv` +44d | UNDECLARED-QUIET | Stored annual school-year report (9/28); quiet by nature, no Cadence line (`grep -ci cadence` = 0). Owner may add one. Via rollup. |
| BRENT `workbook/LESSONS_INDEX.tsv` +33d | UNDECLARED-QUIET | A lessons index; header says last_verified is reconciliation, not data freshness; event-driven, no Cadence line. Via rollup. |
| LIQUID `workbook/GATE079_CALENDAR_EXCLUDED.tsv` +43d | SCAFFOLD-CORRECT | Static rule-derived calendar, complete through 2027-06-30. Skip. |
| CARL `COCKROACH.tsv` +61d | HELD | Tool prints held, attention 15d. Skip. |
| CORAL, MARCO `TRADE.md` | DECLARED-WRONG-FORM (tool vocabulary) | Both open "DECLARED FLAT … Not stale: this is the maintained state"; the recognizer does not know "DECLARED FLAT". Reading A passes these surfaces. Mechanism note only; a recognizer patch needs approval and is not proposed (Will 2026-10-31, fewer checkers). |

**Strict and writes legs:** the 24 strict-only flags are 20 `SCHEMA.tsv` files and 4 named archives/histories (BROCK PREDICTIONS_ARCHIVE, SAM FLOW_ARCHIVE and KB_ARCHIVE, VIOLET VX_M1_HISTORY): static by class, no routing. The 56 writes-only candidates are not routed per owner: since WQ-578 (10/31) root closeout step 1c-bis nudges each desk about its own ledgers at its own closeout, so a sweep packet would duplicate that nudge.

**Dormant freezes:** 0. All six flagged owners committed their STATUS on 2026-11-11, so pre-approval leg (b) fails for each; nothing frozen.

**Class-10 (bounded):** same 88-file perimeter as 10/21 minus own registry drafts, own regex (`OWED|PENDING|NEVER-DELIVERED|AWAITING|BACKFILL-PENDING`, terminal tokens excluded): 35 candidates, 11 with both an artifact and a later date, 14 with one, 10 with neither; WALTER DOORBELL_LOG holds 11. Not comparable to 10/21's 14 (different regex); stays a conform-on-touch leg, no routing.

**Month containers:** 60 month-named `.md` files; 10 carry a heading dated after their month. All 9 earlier hits were known at 10/21 (MIDAS September, VULCAN August and September, OTTO, others are rotation-date headings). The one new hit, `MIDAS/analysis/STATUS_ARCHIVE_2026-10.md:162`, is a rotation heading dated 11/06 over October 23–30 content: correct month, not a straggler. The heuristic over-flags rotation-date headings.

**Self-scope:** writes-candidates `PATTERNS.tsv` (+10d, event-driven by design) and `SURFACES.tsv` (re-cut today). Outbox flat files: 1 (`outbox/2026-11-07_startup-completion.md`, sender's record of a delivered packet). Doc-retirement is its own queue (30d, last 10/22, not due).

## 4. Production Review queues (each 21d, last 10/21, +1d)

| Queue | Result |
|---|---|
| check-registry | 6 root `scripts/` files added since 10/21 have no row; none is a check: 4 launchers (excluded by PROME L852 ACTION 1), `research_reader.py` (read-only research worker), `sec_contact.py` (WQ-600 setting reader). Own new `fleet_view.py` is a view generator. 0 rows owed. Scope limit: agent-local checks at other desks were not re-enumerated. |
| invocation-mapping | Mechanical cite-check of every row's named invoker, then a manual re-check of each miss. **4 stale rows corrected** (old cells to `CHECKS_HISTORY.tsv`): `firetime_check.py` boot scan retired 10/31 (WQ-578 G3, prome_gate.py:1583) → MANUAL-BY-DESIGN; `docket_row_cap.py` closeout run and pre-commit cap retired 10/31 (pre-commit:4) → MANUAL-BY-DESIGN; `pipeline_rc_guard.py` PreToolUse hook dropped from settings.json 10/31 → MANUAL-BY-DESIGN; `claim_check.py` invoker re-pointed from `PROME/CLOSEOUT.md:178` to `prome_gate.py:1557`. `docket_line_stability.py` wording fixed (row-cap step gone). All other named invokers still cite their check. These changed after the 10/21 run; the queue caught real drift. |
| unwired-checks | 2 rows: `wiring_census.py` UNWIRED (since 9/07) and `validate_all.py` BUILT-UNWIRED (since 9/10). PROME ruled 09:0x ET (prome-e8 message; commit ea2771bfff): both on demand, no invoker. Both rows set to MANUAL-BY-DESIGN; 0 UNWIRED rows remain. PROME also transcribed the READS delta (verified: reads_check reads DAEDALUS ATTESTED 2026-11-12, no SCHEMA error) and cleared the SHADE note. |
| roster-health | `render_directory.py` rc 0: 46 agents (34 ACTIVE, 7 TIER-2, 2 DORMANT, 3 SPECIAL), HERMES/YEYOU dropped by design; both co-registration guards passed. Directory regenerated (date line only). |

## 5. Not done in this pass

- Provider-switch Harness re-test (`sweeps/HARNESS_AUDIT_SWEEP.md:7`): owed since this session runs on Claude after Codex on 11/09; separate session.
- Weekly scorecard (due 11/13), D:L490 set (11/15): not started.
- Production Review #10 whole pass (14d cadence, last 11/02, due 11/16): not started; the four queues above are its sub-queues only.

## 6. Review

REVIEW: required for candidate interpretation and register corrections. One independent Sonnet cold reader (coldreader agent, 2026-11-12 ~09:01 ET) checked 28 claims at the artifacts: 23 ✅, 5 ⚠️, 0 ❌. Ledger kept at the session scratchpad; findings and dispositions:

| Reader finding | Disposition |
|---|---|
| MARCO VX "header lag (false alarm)" contradicts the file's own header rule (`VX.tsv:5`); oldest live row SFE-03 is 10/10 | **ACCEPTED, my error.** Re-classified REAL, one row; MARCO packet rewritten before commit to ask about SFE-03, not the header. Verified at `VX.tsv:3-9,120`. |
| CORAL / BRENT labelled DECLARED-WRONG-FORM but carry no declaration | ACCEPTED; re-labelled UNDECLARED-QUIET. |
| CHECKS `docket_row_cap.py` cell credits 91e310264e for the pre-commit removal; that commit says pre-commit was NOT done | ACCEPTED; verified the cap was removed by CATO cd0f1a2544 (2026-10-31); cell corrected. |
| Row 286 key "PRODUCTION_REVIEW-1" undefined | ACCEPTED; delta key now `DAEDALUS:sweeps/PRODUCTION_REVIEW.md-step1-Detect` (the profile-clock instruction sits under step 1). |
| "REVIEW: see § 6" pointed at a missing section | Fixed by this section. |

The reader confirmed the § 3 counts, the four other invoker corrections, STRICT_TEXT rule 7, the L816 text, the SHADE row, the GIT_WORKTREE requirement and the reads_check SCHEMA error. Self-lesson: I read the header's date and the rows' dates but not the header's definition. This is the existing pattern (a stamp is read against its own stated basis), so no new PATTERNS row.
