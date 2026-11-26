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
- **Plan adopted (Will 17:19 ET "ok go, record it as the plan", recorded 17:19 ET):** steps 3, 4, 5, 7 and the red-mark cleanup next fresh session; then one data script, scope approved by Will first; filing reader possibly later; step 6 HELD. Text: SCRATCH § PLAN OF RECORD.

### 2026-11-25 (17:31 ET) — plan item 1 done: DAEDALUS steps 3, 4, 5, 7 and STATUS red marks (Will 17:19 ET)
- **Step 3:** charter BOOT moved to the top; CLOSEOUT steps moved to `CLOSEOUT.md`, numbers unchanged. Every charter line conserved except 4b, which gained one sentence on keeping column 1 short. READS re-sign proposed: `reports/2026-11-25_READS.proposed.tsv`, to PROME.
- **Step 4:** CATALYSTS column 1 = next date plus basis on 42 rows; each old cell kept verbatim at the front of notes; 3 event labels rolled (MBA NDS, LGIH, DFH). 11 RESOLVED rows archived verbatim to `archive/CATALYSTS_resolved_2026-11-25.tsv`. Kept: the A1 restatement row, because it holds 2027-02-20 (also written on the formal-grade row).
- **Step 5:** 42 cut LESSONS rows (DAEDALUS counted 40) are each one complete sentence; 22,409 to 18,599 B. Earlier row text: commit `4d59fcd5c4`; cold registers untouched.
- **Step 7:** THESIS §10 moved verbatim to `thesis/FORMAL_GRADES.md`; §10 is a pointer; §9 headed LIVE. §1, §3, §4, §6 to §8, §11 byte-identical.
- **STATUS:** 44 red marks to 5 (four bands past Red, servicer Class A). Rows with no band say "observation" or nothing. Stars left.
- **Start-up read** (charter + STATUS + SCRATCH + LESSONS + docket print; excludes root files, inbox, MEMORY): see SCRATCH. Row numbers in CATALYSTS changed; row-number citations before this date refer to the old file.
- NOT done: step 6 (held for Will); script 1 (scope draft with Will).

### 2026-11-25 (18:31 ET) — script 1 built: `tools/fetch_series.py` (Will 18:28 ET, "yes go ahead and build"; scope `reports/2026-11-25_script1-scope-DRAFT.md` option A)
- Four feeds (PMMS, FMHPI, Treasury curve, Apartment List roster extract) into `data/series/<feed>/`, logged in `data/series/FETCH_LOG.tsv`. Grades nothing; no boot step, rule or band added.
- `--selftest`: 12 malformed inputs (truncated, empty, renamed column, non-numeric, stale copy, fewer rows, bad date, missing geography, missing roster cities, no month columns) all refused.
- Live run 18:30 ET checked against hand readings: PMMS 7.21% [11/25] ✓ · FMHPI national Sept +1.94% YoY SA ✓ · Treasury 11/24 2Y 4.63 / 10Y 4.91 ✓ · Apartment List full-file SHA-256 = the 10/28 hand record ✓, extract cells identical to the hand extract (quoting differs: the script keeps the publisher's lines), `rent_breadth.py` on it gives 39/100 ✓. First live Apartment List run failed loudly on a protocol-relative link; pattern fixed.
- Second run: all four UNCHANGED, nothing re-saved. FL statewide FMHPI deliberately not kept (CORAL owns statewide FL).
- 353 lines against the ~150 scoped. Keep-or-delete test: end of the December refreshes.
- **18:53 ET follow-up (Will "ok go"):** `treasury_prior_year` feed added; it runs only on January 1–7 so December's last trading days are saved. Selftest gains three date cases (pass); a live run into a scratch folder saved the 2025 file (newest 2025-12-31, 249 rows) and a second run read UNCHANGED. Treasury 11/25 close (10Y 4.85, 2Y 4.61) added as a context row in `RATES.tsv` and on STATUS; the 11/25 spread stays on the 11/24 close (LESSONS §44).

### 2026-11-25 (22:31 ET) — script 2 built: `tools/filing_reader.py` (Will 22:02 ET "build script 2 now", full scope; DAEDALUS notes `AGENTS/DAEDALUS/runs/2026-11-25_HOMER_SCRIPT2_READ.md`)
- Six servicers (PFSI, RKT, UWMC, LDI, ONIT, RITM) × six lines (advances cash, hedge cash, Fannie/Freddie liquidity cushion, 60+ delinquency, debt/equity/unsecured notes, MSR fair value). Rithm included as data only (on the 8/23 panel and the 9/29 sweep; owns Newrez); it is NOT added to SERVICER_WATCH.
- All SEC access through DEWEY's `edgar_doc.py` as a command (facts, exhibits, doc); DEWEY's file not edited; packet `AGENTS/DEWEY/inbox/2026-11-25_from-HOMER_depends-on-edgar_doc.md`.
- **Tag survey (Q3-2026 10-Qs, 22:19 ET): 11 of 36 company-line pairs carry a standard tag.** Advances 0 of 6 · hedge cash 1 (PFSI) · liquidity cushion 0 · 60+ delinquency 0 · debt/equity 6 of 6 (equity tag at all six; debt tags differ by issuer) · MSR 4 (RKT, LDI, ONIT, RITM; not PFSI, UWMC). Everything else is text: the tool prints the statement rows with location and link.
- **Text route, Q3 run:** rows found for 27 of 36 pairs; **9 not found** (RKT advances and hedge cash; UWMC advances, cushion and delinquency; LDI advances; ONIT hedge cash; RITM cushion and delinquency). A found row can still be the wrong row (LDI's cushion hit is a paragraph on MSR sales; LDI's hedge hit is a valuation line, not cash). Reading stays required.
- Tests: `--selftest` 5 malformed inputs refused + 6 behaviour checks. `check` matches 5 hand readings: PFSI advances −$240.5M, PFSI cushion $793.8M vs $699.5M, PFSI hedge $1,349.8M (tagged), LDI 60+ 2.05%/1.45% and $2.37B (vs the 8-K's 2.0%/1.5%, a different document), LDI equity $310.9M (tagged).
- Fix after the first run: liquidity hits now print the 3 blocks above them; Onity's row is unreadable without its "Required | Reported" header (required $83.1M, reported $146.6M: no shortfall). A delinquency pattern that matched Rithm valuation paragraphs was dropped. First draft trashed; the kept draft is `reports/filing_drafts/2026-09-30_servicers_DRAFT_2026-11-25_2226.md`.

### 2026-11-25 (23:13 ET) — filing reader: statement pages, confirmed labels, balance sheet change (Will 22:52 ET "build 1 and 2 and 3")
- **1 Statement pages:** reads FilingSummary.xml, then the cash flow and balance sheet pages (R<n>.htm) through DEWEY's `doc`. Rows parsed as label + one number per column, scale from the page header, parentheses negative; definitions after "X" ignored. Tested first on Rocket's cash flow page (advances row "Advance receivables, net" 365 vs 131, $M, which the text search missed).
- **2 Confirmed labels:** `registry/FILING_LABELS.tsv`, written only by `filing_reader.py confirm`, which refuses a label not on that filing's page. Labels compared with numbers masked (PennyMac's servicing-rights label carries changing dollar figures). A stored label missing later prints "Confirmed label NOT FOUND", never a guess. Stored 4: PFSI advances, PFSI hedge settlements, RKT advances, LDI total equity (each read by hand or against a hand reading).
- **3 Change since last draft:** balance sheet lines only (debt/equity, servicing rights), from the previous draft's `_values.tsv`; cash lines say year-to-date, no change computed.
- **Bugs found by tests and fixed before use:** date header lines read as rows (number pattern allowed "30,"); "Balance Sheets Sheet" titles cut at the first "Sheet" (Rocket); a crash instead of a reported error on that case.
- Tests: `--selftest` 12 malformed inputs refused, 14 behaviour checks. `check` 8 of 8 hand readings match (adds PFSI advances and hedge rows and LDI equity from the statement pages).
- **Runs:** June and September 2026 drafts, 6 of 6 companies each. September vs the 22:26 draft: exact figures (statement or tag) 11 → 21 of 36 company-line pairs; nothing found 9 → 7 (RKT hedge; UWMC advances, cushion, delinquency; LDI advances; RITM cushion, delinquency). **A pattern match is not a confirmed row:** UWMC, LDI and ONIT "hedge" matches are changes in derivative balances, not settlement cash. The 22:26 draft is removed (superseded).
- **23:30 ET follow-up (DAEDALUS upgrade read, relayed by Will 23:22 ET):** (1) a bare year (19xx/20xx) at the end of a label is now label text, never a figure; a row with fewer figures than columns is no longer assigned to columns and prints "blank cell: read the page" (DEWEY's text drops blanks, so the blank column is unknown). Two selftest cases added (16 checks). (2) Cash flow lines in the draft now say "a positive figure added cash, a negative used it"; MEMORY gains the reporting rule (direction in words). Re-run: check 8 of 8; Q3 draft figures identical to 23:07 (values file diff empty); no blank-cell rows on the Q3 pages. 23:07 Q3 draft replaced by 23:25.

### 2026-11-25 (23:47 ET) — DAEDALUS step 6 closed, not done (Will 23:46 ET "ok agreed go ahead")
- Band derivation history (~4.5 KB) stays in `CLAUDE.md` § Key Thresholds. Reasons: ~5% of the start-up read; several derivation lines act as caveats at every boot (FL Orange is a bracket, FC-starts Red is a judgment, the 0.63–0.72% FL zone is weak evidence, rank ≠ level); the first outside split mis-classed ~5 KB of rules as history.
- Reopen only if `CLAUDE.md` passes 45,000 B (docket row, standing). DAEDALUS's split (`AGENTS/DAEDALUS/runs/2026-11-25_HOMER_ARCHITECTURE_REVIEW_READ.md`) is the starting point then.
