# HOMER Maintenance Log

Reverse-chronological log of **structural** changes: docs created/retired/moved, scripts built or changed, charter/boot/closeout amendments, schema changes. Answers *"why is HOMER organized this way, and what decision am I about to re-litigate?"*

- Analytical changes (grades, readings, thesis counts) live in `STATUS.md`, the workbook and `thesis/THESIS.md` §9, not here.
- Entries from 2026-11-05 on run oldest to newest below the October block.
- **Consult before restructuring; this is not a per-session ritual.** Add an entry only when the structure changes.
- History before 2026-10-28: `archive/CLAUDE_charter_history_2026-09-29.md` (charter incidents) and `git log -p -- AGENTS/HOMER/CLAUDE.md`.

---

### 2026-10-28 — NV and CA lanes built (Will: "build them out")
- Two Opus helpers built source baselines (`reports/2026-10-28_evidence/lane_NV.md`, `lane_CA.md`); HOMER re-read the load-bearing figures (Redfin LV 18.58%, NY Fed NV CC 16.28%, C.A.R. median $899,720).
- `STATE_HSG.tsv`: 7 NV rows (incl. a correction of the stale 2025 row's two wrong labels) + 6 CA rows. Docket: 4 NV + 3 CA recurring rows. Charter Key Signals + Key Data Sources updated; COVERAGE lanes 14a/14b.
- No bands (Will-gated). CA insurance/FAIR Plan = AEOLUS (pointer row only).

### 2026-10-28 — file-hygiene sweep (Will-asked)
- **Retired to `archive/`** (>60 days, not boot-read, no live-doc reference — root Data Hygiene): `2026-07-12_FL-condo-reconciliation-package.md`, `2026-07-12_domain-sweep.md`, `2026-08-14_issuer-primary-sourcing-convention-PROPOSAL.md`, `2026-08-23_refresh-plan-AND-EXECUTION-RECORD.md`. Seven other pre-8/29 reports stay: live refs from `workbook/`, `docket/` or `thesis/`.
- **`workbook/LEDGER_GLOB` created** (declares `workbook/*.tsv`; registry excluded by design — the scanner grades its freshness).
- Glued word-number tokens fixed on live surfaces (STATUS, NEXUS_BRIEF, docket; root Output Canon). Ledger record rows from the 10/19 session still carry some glue — left as written.
- `OBLIGATIONS_OTHERS.md`: B8(a) found ANSWERED by WALTER 10/01; stale rent figure in §C replaced with a pointer.
- `MEMORY.md`: infra reachability updated (Fannie PDFs 403; S&P press, MBA Newslink, EDGAR work); new ownership seams recorded.
- **Not done, flagged:** `LESSONS.md` 24,035 B — **377 B under the 75% rotation trigger**; the next lesson append must rotate first. HOMER has no row in `PROME/registry/READS.tsv` (PROME-owned) so read-cap checks are heuristic.

### 2026-10-28 — desk-comparison build-out (Will-approved: "do all 5, route cases to CREED")
- **Trigger:** comparison with mature peers (REGINALD, CARL, CREED, CORAL, BOND, HENRY) found HOMER graded bands by hand, pre-registered prints rarely, and had no coverage map, case routing or structural log.
- **Built:**
  - `registry/THRESHOLDS.tsv` — machine-readable band registry (12 bands; retired FL YoY absent); one reading cell per band.
  - `tools/threshold_scan.py` — exact-decimal grader; highest-uncrossed-rung reporting; STALE/UNGRADED/NEAR flags; malformed rows fail closed (exit 2; tested with bad comparator, bad number, short row).
  - `registry/PREREG_2026-10_TREPP_MF_PRINT.md` — first Trepp MF pre-registration (frozen on commit).
  - `COVERAGE.md` — lane map (15 lanes; NV/CA flagged as uncovered).
  - This log.
- **Routing:** named MF cases → CREED `cases/CASES.tsv` by packet (charter §Scope); HOMER keeps no case ledger.
- **Charter:** BOOT 6b (scan), CLOSEOUT 2 (update reading cells; append PREREG grading), FILES table completed.

### 2026-10-28 — same session, earlier
- Ledger line-1 headers split (old headers to line 2) so `ledger_staleness.py` reads one clock; append-log rule added to six LIVE ledgers.
- BOOT step 8 PREDICTIONS read scoped (file over the read cap).
- Charter: "no book" line; HENRY edge formalized with a trigger rule; rent-breadth rule ⑥ (one dated row per refresh).
- `BUILDER.tsv`: DHI BUYDOWN TRACKER rows (one per fiscal quarter).

## 2026-11-05

- Charter: BOOT step 9a (combination watch, WQ-622 A); CLOSEOUT step 3 gains the WQ-619 miss line and the WQ-596 packet route.
- `KB_LIVE.tsv`: five `combo:` theme rows, KB-HOMER-043 to 047, review 2026-12-01 (docket row).
- `PREDICTIONS.tsv`: HOM-03 to HOM-06.

## 2026-11-12
- **READS manifest filed** (28 rows, transcribed by PROME into `PROME/registry/READS.tsv`): closes the 10/28 "no row in READS" note; `read_cap_check.py --agent HOMER` is now attested, not heuristic.
- Charter (WQ-678, DAEDALUS): F19 (BOOT 1 points to `docs/GIT_WORKTREE_PROCEDURES.md`) and F57 (CARL cross-references moved to `archive/CLAUDE_carl-cross-references_2026-11-12.md`) applied; F58 declined.

## 2026-11-20
- Charter CLOSEOUT 5 and two lines aligned to WQ-719 A / WQ-721 A (NEXUS brief written only when its content changes). Charter size question closed by root canon (50,000 B ceiling).
- THESIS §10 added (first formal grade under frozen criteria). STATUS rotated; STATUS rotation files for 11/11, 11/20, 11/23, 11/24, 11/25 in `archive/`.

## 2026-11-24 and 2026-11-25
- **THESIS §11:** A1 first conjunct restated (WQ-725, Will). **§12:** §1 paragraph adopted (Will). **§7 V6** added (PROME answer). First history move → `archive/THESIS_history_2026-11-25.md`.
- **Frozen-record incident:** the 11/20 grade row was overwritten (`62ef628cb7`) and restored (`0839878fe6`); LESSONS §57.
- Charter: HUD FHA performance source added to Key Signals and Key Data Sources; docket row added.

## 2026-11-25 cleanup pass (Will 14:29 ET, "yes lets do the clean up pass")
- **THESIS** 31,817 → under 22,785 B: §2, closed §6 rows, §8b table, §10 full text, §12 record and expired V5 moved verbatim to `archive/THESIS_history_2026-11-25b.md` (blocks F–K). §1, §3, §4, §5, §8a, §9, §11 byte-identical except as later dated. D18 added.
- **LESSONS** 25,029 → about 22,100 B: 12 hot rows shortened because a read surface already carries the rule; old rows in `archive/LESSONS_hot_rows_2026-11-25.md`; 57 rows and both cold registers unchanged in count.
- **NEXUS_BRIEF:** superseded SENDING rows moved verbatim to `archive/NEXUS_BRIEF_rows_2026-11-25.md`.
- **COVERAGE** refreshed (lane 1b opened) · **MEMORY** infra notes rewritten as one dated table · **OBLIGATIONS_OTHERS** B3–B6 closed, B11–B13 and the Oct-2025 FHA rule break added.
- Docket: thesis-grade row's early-date clause corrected (A1 is 0 of 2); read-cap row updated.

### 2026-11-25 (17:04 ET) — DAEDALUS structure block, steps 1 and 2 (Will 17:02 ET "ok go")
- Step 1: CATALYSTS rows PHM, MTH, NVR re-keyed from RESOLVED to `~late Jan 2027 — PATTERN`; prior keys kept in notes. Event label Q3 to Q4-2026.
- Step 2: servicer-watch trigger moved verbatim to `registry/SERVICER_WATCH.md` (rebuilds the original cell byte for byte, checked); row 3 keeps state and pointer, 40,229 to 28,108 B. Charter FILES row added. No class, level or route changed.
- NOT done: step 3 (BOOT first, CLOSEOUT file, READS re-sign), 4, 5, 7 (next fresh session); step 6 HELD for Will. Source block: `AGENTS/DAEDALUS/runs/2026-11-25_HOMER_ARCHITECTURE_REVIEW_READ.md` incl. addendum.
