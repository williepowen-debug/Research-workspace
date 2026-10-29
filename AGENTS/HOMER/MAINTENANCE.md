# HOMER Maintenance Log

Reverse-chronological log of **structural** changes: docs created/retired/moved, scripts built or changed, charter/boot/closeout amendments, schema changes. Answers *"why is HOMER organized this way, and what decision am I about to re-litigate?"*

- Analytical changes (grades, readings, thesis counts) live in `STATUS.md`, the workbook and `thesis/THESIS.md` §9, not here.
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
