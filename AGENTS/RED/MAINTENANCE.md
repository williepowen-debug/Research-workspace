# RED Maintenance Log

Reverse-chronological log of **structural** changes to RED's docs, folders, schemas, and tooling. Each entry: what changed, why, files touched, boot-impact.

---


## S43 — 2026-09-10 ~16:1x ET

**Trigger:** PROME Tier-1 due-row spawn on DOCKET **L315** (WQ-184 L0 rule — a registered dated row naming the desk IS the approval; Will's word for the 9/10 slate 11:53 ET). FT-11 arm-date correction + F2 grade + the L247 F1 re-check leg + a 3-packet inbox drain.

| What changed | Files touched | Boot-impact |
|---|---|---|
| **`RED-FT-11` arm date CORRECTED 2026-09-09 → 2026-09-10** across **all five canon fields** carrying the claim (`instrument_basis` ×2 sites, `state`, `action_magnitude`, `rolling_base_rate`, `instrument_basis_operative` ×3 sites); `last_reviewed` 9/6 → 9/10. **Superseded text preserved VERBATIM** in the `state` cell with the reason. No threshold, leg, sustain window, partition figure or weight touched. | `registry/FALSIFICATION_TRIGGERS.tsv` | `boot.py` reads the card live; `gen_trigger_scan.py` re-run — **SCAN view regenerated, 12 rows, 25,730 B (33% of canon)**. `schema_check.py` ✅ ALL CONFORM. |
| **F2 RESOLVED OFF-THE-RUN recorded + v1.1 ACTIVATION encoded** on the same row (state cell + operative cell), with the full primary-verified operation record, the three contamination flags, and the DGS30-UNKNOWN clause. | `registry/FALSIFICATION_TRIGGERS.tsv` | As above. **The activation has no application window yet** — it applies at the next NON-FIRED window, unidentifiable until the 9/10 DGS30 close posts. |
| 🔴 **`scripts/base_rate_review.py` HARDCODED the arm date.** Line 196 emitted the literal `" (live from 2026-09-09)"` gated on a substring test (`'precondition live' in row['state']`) — so after the registry was corrected **the boot surface would have contradicted its own canon at every future boot**. Patched: new `_arm_date_note(row)` derives the date from `instrument_basis_operative` (**first** match wins, so a dated correction quoting SUPERSEDED text cannot win), falls back to `state`, then to **silence — never to a stale literal**. | `scripts/base_rate_review.py` | Boot step 9d now prints `(live from 2026-09-10)`, derived. Verified by re-running. |
| **Mirror re-dated and resolved:** `docket/CATALYSTS.tsv` row 68 `2026-09-09 → 2026-09-10`, event text corrected with the superseded wording quoted, `window` → `today`, status `pending` → **`RESOLVED-PARTIAL`** with the op-side record and the explicit re-grade date. | `docket/CATALYSTS.tsv` | `boot.py` § catalyst countdown no longer shows a `T--1` row for a passed date. `claim_check.py --check weekday` ✓ clean. |
| **`STATUS.md` rotated under the READ_CAP budget — TWICE, and the second pass was the honest one.** The S43 header pushed it over the **32,550 B** budget. First rotation folded the **S42 header (1,177 B, crc32 `1364258009`)** and the **S41 `[Prior]` header (508 B, crc32 `482982337`)** verbatim; still over. Then the **§ PRIOR SESSIONS ARCHIVED nav block (608 B, crc32 `678959618`)** and the **§ MISSING DATA WANTED (8/12) block (1,912 B, crc32 `816405192`)** — the latter carrying a **29-day-old stamp**. Result **31,022 B, READ-CAP 0 ✅**, 156 lines. ⚠️ **MISSING DATA WANTED is FOLDED, NOT RESOLVED — every item in it is still wanted.** | `STATUS.md`, **new** `reports/2026-09-10_S42-S41_status_headers_folded.md` | STATUS stays a boot whole-read, now under budget. Four pointer lines replace the folded blocks. |
| **`board_log.tsv` ROTATED — it had breached the read cap before this session even appended.** It stood at **31,564 B = 97% of the 32,550 B budget**, and the 9 S43 dispositions took it to **36,819 B, over**. The **36 rows dated before 2026-09-06** moved verbatim to `archive/board_log_pre-2026-09-06.tsv`; 33 kept + 9 new. Result **24,231 B ✅**. | `board_log.tsv`, **new** `archive/board_log_pre-2026-09-06.tsv` | Boot 1.5 / 5.5 read is back under budget. **The archive is the file to grep for "has RED already seen this?" before 9/6.** ⚠️ A first rotation attempt used a `2026-08-15` cutoff that moved **0 rows** (the log's oldest row is 8/28) and *grew* the file with its own banner — reverted, which also reverted the 9 new rows; they were re-appended. **Lesson: measure the date distribution BEFORE choosing a cutoff, and never revert a file you have already appended to without re-applying the append.** |
| **9 disposition rows appended** (3 `INBOX_GENERAL` acted + 1 BOARD `noted` + 5 BOARD `info-only`), clearing the boot-1.5 obligation `boot.py` § ⑤ flagged 🟡 (6 RED-addressed signals newer than the last disposition). Inbox drained: 3 packets `git mv`-ed to `inbox/processed/`. | `board_log.tsv`, `inbox/processed/` | § ⑤ should read clean at next boot. |
| **New adversarial report + workbook rows.** L247 F1 review (FAIL, 2 exhibits). ML-RED-234…237, KB-RED-097…099, CHG-RED-052. | **new** `challenges/2026-09-10_L247_F1_recheck_outcome_vector_spec.md`; `workbook/ML.tsv`, `KB.tsv`, `CHALLENGES.tsv` | `schema_check.py` ✅ ALL CONFORM. |
| **Packet written to BOND** (carve-out ①) on the falsified `total_par_amt_offered` cell, with one ask. **No BOND file touched.** | **new** `AGENTS/BOND/inbox/2026-09-10_from-RED_your-offer-to-cover-is-NOT-uncomputable-…md` | None on RED's boot. bond-14 doorbelled per messaging rule 6. |

**Structural lesson worth carrying (→ ML-RED-234/235).** **One fact — FT-11's arm date — lived in EIGHT places:** five registry fields, one hardcoded tool literal, one docket row and one CALENDAR/STATUS narrative pair. Five were corrected by editing the row, one by patching code, two by editing mirrors. **A scan keyed on the registry alone would have reported the correction complete while the boot surface still printed the dead date.** `[[finding_hand_fixing_named_rows_is_not_fixing_the_class]]` · `[[finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live]]`.

## S42 — 2026-09-09 ~21:1x ET

**Trigger:** PROME Tier-1 due-row spawn on DOCKET **L275** (WQ-184 L0 rule — a registered dated row naming the desk IS the approval). FT-10 published-bar owner follow-up + a 3-packet inbox drain.

| What changed | Files touched | Boot-impact |
|---|---|---|
| **`STATUS.md` rotated under the READ_CAP budget.** The S42 FT-10 grade pushed it to **34,679 B** — over the **32,550 B budget** (cap 54,250 B), `read_cap_check.py` 🟠. Two blocks rotated out **VERBATIM, crc-stamped, nothing edited**: the S41 `[Prior]` header line (1,487 B, crc32 `4219352712`) and the S29 closing reflection (2,139 B, crc32 `2119793974`). Both are content-duplicated on live surfaces (§ CURRENT ASSESSMENT + the hypothesis table; `reports/2026-08-12_S29-S30_status_narrative_archive.md`). Result **31,915 B, READ-CAP 0 ✅**. | `STATUS.md`, **new** `reports/2026-09-09_S41-header_S29-reflection_folded.md` | STATUS stays a boot whole-read and is now under budget. Two pointer lines replace the folded blocks — **the pointers are the only new boot bytes.** |
| **FT-10 card re-graded by the owner** (state col 8, `last_reviewed` col 16 → 2026-09-09, grade text appended to col 17). **No clause amended, no threshold or sustain moved.** | `registry/FALSIFICATION_TRIGGERS.tsv` | boot.py reads the card live; `gen_trigger_scan.py` re-run — **SCAN view regenerated, 12 rows, 15,210 B (22% of canon)**. `schema_check.py` ✅ ALL CONFORM. |
| **New owner-grade research doc** — the run that broke, which bar broke it, next countable bar, earliest fire, and the `boot.py`-reads-the-publisher confirmation at line numbers. | **new** `research/2026-09-09_FT10_RUN_BROKEN_OWNER_GRADE.md` | Not boot-read; cited from STATUS, the card, OUTBOX and NEXUS. |
| **`RED-23` amended pre-data** (append-only, both vintages left readable per the S25 rule the row invoked at registration). Confidence **HELD at 60%** — basis changed, number did not. | `workbook/PREDICTIONS.tsv` | DUE-scan unaffected (`Timeframe` cell untouched, still `2026-11-XX`). |
| **Workbook + log rows:** ML-RED-231/232/233, KB-RED-094/095/096, 3 `board_log` dispositions (`source=INBOX_GENERAL`). | `workbook/ML.tsv`, `workbook/KB.tsv`, `board_log.tsv` | ⚠️ **`board_log.tsv` is at 28,378 B pre-append = 52% of cap, rotate-tier (≥75% of budget).** Not rotated this session — **flagged, owed at the next full closeout.** |
| **3 inbox packets consumed and `git mv`'d** to `inbox/processed/` (2 LABOR, 1 ORACLE). Top-level inbox → 0; `inbox/WALTER/` was already 0. | `inbox/` → `inbox/processed/` | Boot 5.6 general-inbox scan reads clean next boot. |
| **Carve-out ① packets authored + committed:** VIOLET (FT-10 reset, ≤5 lines) and the PROME delivery memo. **No file outside `AGENTS/RED/` was edited.** | `AGENTS/VIOLET/inbox/2026-09-09_from-RED_ft10-run-broken-count-is-zero.md`, `PROME/inbox/2026-09-09_from-RED_ft10-run-broken-owner-grade.md` | None. |

**NOT done this session, and stated rather than left to look done:** the **boot 1.5 BOARD scan** — `boot.py` §⑤ reports **23 RED-addressed signals newer than the last disposition (2026-09-06), 2 of them action-addressed**. This was a **bounded FT-10 + inbox spawn**, not a full boot; the backlog is real, is dated, and is owed at the next full session. ⚠️ Compounding it: §⑤ itself is the **specified-not-built** check flagged at S41 — it is not set-difference based and **will read green while a backlog exists**, so its current 🔴 is informative but its future 🟢 is not.

**Also still open (carried, not re-derived):** nothing compares `METRIC_MAP` against each registry row's `instrument_basis` cell. FT-10 was mis-wired to the disqualified mirror for four days **with the correct basis written on its own card** — the card and the code disagreed and **no check reads both**. Specified-not-built since S41; survives S42.

---

## S40 — 2026-09-02 ~23:0x ET

**Trigger:** PROME wave-4 spawn (Will 22:43, *"Spawn the next six"*); WQ-162 RULED; five inbox packets (PROME · VIOLET · BOND · CORAL · NEXUS).

| What changed | Files touched | Boot-impact |
|---|---|---|
| **`RED-FT-10` grading basis DECLARED** (8 clauses; series moved to CBOE `SKEW_History.csv`, publisher of record; Yahoo demoted to provisional mirror) + row re-graded | `registry/FALSIFICATION_TRIGGERS.tsv` cols 7/16/17/18; new `research/2026-09-02_FT10_GRADING_BASIS_DECLARED.md` | ⚠️ **boot.py's FT-10 line now evaluates a PROVISIONAL MIRROR, not the declared basis** — see the wiring gap below |
| **`RED-FT-11` v1.1 encoded** on BOND's adopted design call; leg-(iv) base rate corrected for the tie convention | `registry/FALSIFICATION_TRIGGERS.tsv` cols 7/16/17/18; new `research/2026-09-02_FT11_v1.1_second_path_partition_AND_tie_set.md` | none (manual row) |
| Scan view regenerated after both canon edits (CLAUDE.md 9b) | `registry/FALSIFICATION_TRIGGERS_SCAN.tsv` — 12 rows, 6,840 B, 11% of canon | WALTER boot 6b consumes it |
| CORAL confirmation encoded; `Stale_By` → 2026-11-15 | `workbook/KB.tsv` (KB-RED-046, KB-RED-052) | review-debt: two rows off the past-due list |
| **`NEXUS_BRIEF.md` rebuilt + rotated for the READER's cap** (READ_CAP rule 15): Jackson Hole corrected to 8/27–29; FORWARD CATALYSTS table rebuilt (7 of 12 rows were resolved August events); NEXT DECISION POINT rewritten; six dated FOLD blocks (S38h·S38b·S38·S36d·S35·S34) moved **verbatim** | `NEXUS_BRIEF.md` **43,094 → 31,811 B** (132% → **98%** of 32,550 B); new `archive/NEXUS_BRIEF_folds_rotation_2026-09-02.md` (17,463 B, crc32 2842239224 + a second crc for the appended S38h block) | NEXUS boot surface now under budget |
| Armed read recorded pre-print on the SAM rail | `workbook/CHALLENGES.tsv` (CHG-RED-047) | disposition at next boot on SAM's write-back |
| 4 findings rows | `workbook/ML.tsv` ML-RED-209 … 212 | — |
| STATUS / CHANGELOG / OUTBOX / SCRATCH / board_log (7 rows) | — | — |

**⚠️ WIRING GAP OPENED BY THIS SESSION, stated rather than deferred (`[[finding_guard_correctness_and_wiring_are_independent]]`):** FT-10's letter now declares CBOE as the grading basis and says the Yahoo mirror **cannot complete a grade**. **`scripts/boot.py` still evaluates FT-10 from the mirror.** Tonight the two agree (144.12 both) so the printed line is correct — **but it is a PROVISIONAL DISPLAY, not a grade**, and on any session where the mirror drops or mis-values a bar (measured: 0.79% of sessions) boot.py would print a clean row off a series the letter has disqualified. **Fix owed in the 9/4–9/11 window: point boot.py's FT-10 evaluation at the CBOE CSV, or label its output PROVISIONAL.** Not done tonight — the two-correction discipline and the late-session rule both say a new tooling edit is the wrong last act of a session that has already made two canon edits.

**Read-cap note:** `STATUS.md` 29,570 → **32,087 B = 98.6% of the 32,550 B budget.** Under, but this is the next rotation and it should not be deferred twice.

---

## 2026-08-28 (S38g) — P1 read-cap housekeeping: STATUS fold + board_log rotation, 2 files went from 🔴 OVER-CAP to green

**Trigger:** DAEDALUS P1 read-cap ruling (Will-approved 2026-08-28) — any file the boot protocol tells a session to read whole stays under 32,550 B (60% of the harness single-read cap). Instrument: `scripts/read_cap_check.py --agent RED`. Canon: `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`. RED's measured state at the ruling: **STATUS.md 86,955 B (157% of cap) and board_log.tsv 100,890 B (186% of cap) — both 🔴 OVER-CAP.**

**What changed:**
- **STATUS.md folded** from 86,955 B → **29,689 B (55% of cap, 91% of budget; 🟡 rotate-tier but under cap and readable)**.
  - S38 section (lines 10-63, 6,912 B) and S35 section (lines 64-93, 4,863 B) archived verbatim → `reports/2026-08-28_S35-S38_status_narrative_archive.md`.
  - State-line (line 2, was 32,053 B — 98% of cap on ONE row) rewritten to today's day-summary only, dropping the "Prior:" chain going back to 8/27 evening (verbatim snapshot preserved in the archive under STATE LINE SNAPSHOT).
  - Three archive-pointer sections (SESSION 34, SESSIONS 31 & 33, SESSION 29/30) consolidated into a single PRIOR SESSIONS ARCHIVED nav block.
  - FALSIFICATION CRITERIA (was 6,073 B narrative-mirror of registry TSV) compressed to firing/near-firing rows + registry pointer; full verbose form archived under STATUS SECTION SNAPSHOTS.
  - OPEN CHALLENGES (was 8,250 B verbose table) compressed to headline row-per-CHG; canonical detail lives in `workbook/CHALLENGES.tsv` Resolution cells; verbose form archived.
  - TOP ADVERSARIAL PRIORITIES (was 6,528 B with historical Section 0 audit-plan) compressed to 7 standing items; live priorities live in SCRATCH's NEXT SESSION block; verbose form archived.
- **board_log.tsv rotated** from 100,890 B → **3,907 B (7% of cap, 12% of budget; ✅ ok)**.
  - 220 rows dated pre-2026-08-28 moved verbatim to `archive/board_log_pre-2026-08-28.tsv` (with header + provenance banner).
  - Live board_log retains header + 12 rows dated 2026-08-28. Future rotation cadence: monthly at closeout of the last session in the month, or on demand if read-cap check flags.

**Files touched:**
- `AGENTS/RED/STATUS.md` (rewrite, 86,955 → 29,689 B)
- `AGENTS/RED/board_log.tsv` (rewrite, 100,890 → 3,907 B)
- `AGENTS/RED/reports/2026-08-28_S35-S38_status_narrative_archive.md` (new)
- `AGENTS/RED/archive/board_log_pre-2026-08-28.tsv` (new)

**Boot-impact:** POSITIVE. Both boot-mandated whole-reads now under cap; no partial-read degradation risk. Every durable outcome remains on its live canonical surface (registry TSV, CHALLENGES.tsv, PREDICTIONS.tsv, ML.tsv, KB.tsv, CHANGELOG.md); the compression only touched narrative-mirror sections in STATUS.

**Residual over-budget (not over-cap, no fix owed today):**
- **MEMORY.md 50,168 B (92% of cap)** — Will-ruled 2026-07-28: RED must NOT compact its own MEMORY; flag to PROME. Recorded in this session's SCRATCH OPEN THREADS.
- **CALENDAR.md 40,267 B (74% of cap)** — under cap, readable, not urgent. Rotation candidate at next housekeeping pass (resolved catalysts to archive).

**Instrument note:** DAEDALUS's `read_cap_check.py` now recognizes existing scope markers ("last 2-3 entries" for CHANGELOG, scripted reads on KB/CHALLENGES) as `ℹ️ scoped-read-not-lean, not counted`. No wording fix needed for those three (heuristic false-positives in the original P1 packet, corrected in DAEDALUS's same-day recut).

**Provenance:** ruling `PROME/proposals/2026-08-28_p1-read-cap-RULED.md` (Will "P1 approved go ahead"); DAEDALUS packets `inbox/processed/2026-08-28_from-DAEDALUS_P1-read-cap-RULED-…` + `…CORRECTION-P1-read-cap-packet-recut-…`. Root CLAUDE.md Data Hygiene amended 2026-08-28 with the byte-budget rule.

**Distinct from `thesis/CHANGELOG.md`**, which logs **analytical** changes (confidence shifts, hypothesis re-weighting, challenge resolutions, prediction scoring). If a change moves a number or a probability → CHANGELOG. If it moves a *file, schema, or boot path* → here.

**Conventions (adopted from SAM, S16):**
- Archive-next-to-active-doc where practical; `archive/` root holds legacy/superseded.
- Verify-before-archive: confirm content is captured elsewhere before cutting (lossless by construction).
- Loop-closer: when a structural change adds/moves a file, update `CLAUDE.md`'s FILES tables + boot steps in the same pass, so a future RED knows it exists.

---

## 2026-08-27 (S36d) — CHG-051 deliverables: registry 15→17 cols, outcome-axis pair, base-rate review tool + boot step 9d

- **Trigger:** Will-directed execution of CHG-RED-051's three owed deliverables (registry had no correctness axis; base rates computed once, never recomputed; FT-01 label self-refuting at 48.3%@120obs).
- **What changed:** ① `registry/FALSIFICATION_TRIGGERS.tsv` **15→17 columns** — `last_reviewed` + `rolling_base_rate` APPENDED (cols 0–14 positions unchanged; WALTER notified pre-landing per the T5 precedent, packet in their inbox committed ahead of the change). All 12 rows populated from a fresh computation. FT-01 action relabeled (analytical half → CHANGELOG); **FT-12 registered** (new row). ② **Two new files:** `registry/OUTCOME_SPEC.tsv` (7-col, pre-committed proxy/horizon per trigger) + `registry/TRIGGER_OUTCOMES.tsv` (8-col, per-fire grade ledger, scored at horizon). ③ **New script `scripts/base_rate_review.py`** (read-only, recompute + ≥2× drift flag + `--candidate` pre-registration mode + FT-11 Δ5 surfacing). ④ `workbook/SCHEMA.tsv` +17 contract rows; `scripts/schema_check.py` file map +2 entries. ⑤ `CLAUDE.md` **boot step 9d added** (runs the review; W2 extended to disposition resolved TRIGGER_OUTCOMES rows).
- **Files touched:** registry/FALSIFICATION_TRIGGERS.tsv · registry/OUTCOME_SPEC.tsv (new) · registry/TRIGGER_OUTCOMES.tsv (new) · scripts/base_rate_review.py (new) · scripts/schema_check.py · workbook/SCHEMA.tsv · CLAUDE.md · AGENTS/WALTER/inbox/ (notification packet, carve-out ①).
- **Boot-impact:** one new advisory step (9d, ~10s, network); `schema_check` 12/12 conform verified post-change; `base_rate_review` round-trips 1.0× against the fresh cells. ⚠️ Migration method: tab-split + field-count validation pre/post + `os.replace` — never `csv` (ML-168).


## 2026-08-27 (S35) — CHG-RED-051 opened (first APPARATUS-class self-challenge); CHG-RED-049's missing ledger row written retroactively

**Trigger:** Will-directed — open the apparatus self-challenge owed under ML-RED-185 (RED stood 0 of 2).

**What changed:**
- **NEW** `challenges/SELF_APPARATUS_REGISTRY_2026-08-27.md` (121 lines) — CHG-RED-051, STRONG, target = RED's own `registry/FALSIFICATION_TRIGGERS.tsv`. Three charges (no outcome axis · base-rate staleness · the synthesis), four pre-registered falsifiers of which **three were run in-session** rather than deferred.
- `workbook/CHALLENGES.tsv` — **two** rows added: CHG-RED-051, and **CHG-RED-049 retroactively.**
- `workbook/ML.tsv` — ML-RED-190 (the apparatus finding), ML-RED-191 (the missing-row defect).
- `OUTBOX.md` — RED-TO-PROME-20260827-024, 🔴, one ACTION owed (fleet base-rate-staleness sweep proposal).
- `thesis/CHANGELOG.md`, `STATUS.md`, `board_log.tsv` — folded.

**⚠️ The structural finding of the pass (ML-RED-191): CHG-RED-049 was issued, delivered to CARL, and narrated on FOUR surfaces — SCRATCH, MAINTENANCE, board_log, ML.tsv — while the canonical `CHALLENGES.tsv` row was never written.** `boot.py`'s DUE-scan reads `CHALLENGES.tsv`, so the challenge was **invisible to automated loop-closure by construction** and would have aged silently. **It was caught by accident** — CHG-051 needed the next free ID and 049 was missing from the sequence. **No check found it.**

**Boot-impact:** none to the sequence. One extra ACTIVE row in the DUE-scan (051, dated 2026-10-31; 049 dated 2026-09-15). **Owed and NOT built this session:** a `Last_Reviewed` + rolling base-rate column on the registry, and an outcome axis with pre-committed proxy/horizon — both named in the challenge as deliverables rather than half-shipped under time pressure.

## 2026-08-27 (S34 addendum) — structural

1. **`registry/FALSIFICATION_TRIGGERS.tsv` — `RED-FT-11` ADDED** (10 → 11 rows), `ARMED-UNFIRED`, precondition live **2026-09-09**. ⚠️ **It is a CONDITIONAL CLASSIFIER, not a threshold row, and `boot.py` correctly reports it `⚪ unmapped metric, manual check`.** That is disclosed rather than papered over: **a three-leg classification over a window has no single-metric comparator form, so it cuts against my own `ML-RED-156`** (machine-consumed registrations should carry their conjunction in the machine columns). **Labelled a MANUAL row.** Mitigation available later — the precondition alone (Δ`DGS30` 5-session) is mappable and would surface *when to look*.
2. **`research/BUYBACK_ATTRIBUTION_2026-08-27.md`** — new: design, base rates, the struck first design, the 8/19 validation, four limits.
3. **`workbook/ML.tsv`** — ML-RED-189.
4. **`docket/CATALYSTS.tsv`** — 2026-09-09 row added (buyback step-up effective; FT-11 precondition goes live).
5. **Routed AT THE WRITE** to BOND, TERRY and PROME inboxes — the `FT-06` lesson from this morning applied the same day (filling a `recipient_chain` is not routing).

**Boot-impact:** registry is 11 rows; FT-11 prints ⚪ by design.


## 2026-08-27 (S34) — structural changes

**Trigger:** Will-directed boot after 7 dark days + a Will-assigned KERNEL Gate C adversarial review.

1. **`workbook/PREDICTIONS.tsv` — RED-22 added, and its `Timeframe` cell had to be fixed TWICE.** As registered the cell was prose (*"Resolves Fri 2026-08-28 ~10:00 ET on the BLS…"*) which `boot.py`'s DUE-scan printed as **MANUAL CHECK**. ⚠️ **`parse_fuzzy_date` anchors `^…$` and requires the WHOLE cell to be a bare ISO date (or a `Q`/month form) — prose ANYWHERE makes an ACTIVE row invisible to automated loop-closure.** My **first** fix (leading the cell with the ISO date) **did not work**, and only re-running the tool showed that. `Timeframe` is now the bare date; the resolver detail moved to `Invalidation`. **Boot-impact: DUE-scan returns 🟢 again.** *(Same class as ML-RED-125 — an undated ACTIVE row is DUE-scan-invisible by construction.)*
2. **`workbook/CHALLENGES.tsv`** — **CHG-RED-049** opened (CARL, STRONG) · **CHG-RED-050** opened and RESOLVED (KERNEL Gate C review) · **CHG-RED-048** → RESOLVED-CONVERGED · **CHG-RED-042** → **ACTIVE-BLOCKED** with a hard 9/30 backstop and its failure mode written in.
3. **`workbook/ML.tsv`** — ML-RED-183…188 appended (FT-08 leg structure ×2 · the argument-vs-apparatus mechanism · the same-primary replication error · the cross-perimeter comparison class · the shared-antecedent loop with LABOR).
4. **`workbook/KB.tsv` KB-RED-067** — the DFII10 label re-corrected on its **third** pass (BOND's canonical string encoded verbatim), and the row's **core claim SPLIT** into its two decompositions, with the policy-path half downgraded to CONTESTED and then **re-grounded** so it does not depend on BOND's instrument.
5. **`research/` — two new files:** `QCEW_FRAMEWORK_2026-08-28.md` (pre-catalyst decision tree, FROZEN, two pre-data addenda) and `QCEW_PRIMARY_CHECK_2026-08-27.md` (primary verification + LABOR's charge + the seasonality refutation).
6. **`challenges/` — `2026-08-27_KERNEL_GATE_C_LIVE_INTERFACE_ADVERSARIAL_REVIEW.md`** (review + 2 delta re-reviews). **`2026-08-20_SAM_V20_BLIND_PASS.md`** header count corrected three→four.
7. **`research/FOMC_FRAMEWORK_JUL28-29_2026.md`** — dead-framework banner added (it carried the false "DFII10 series high" label in prose and in branch R-C). **Content left intact** — a pre-catalyst framework's value is recording what was believed before the print.
8. **`AGENTS/SAM/red/CHALLENGES.md`** (RED's editing right, S31) — **CH-009 and CH-012 now carry STATED input perimeters** rather than inferable ones, verified by grep across the whole rail. Line count 280 → 291, **verified RISING** (a falling count would signal anchor-splice deletion, ML-RED-155).
9. **No tooling changed. Nothing written into `KERNEL/`** — verified with `git status -- KERNEL/` at every commit in the review sequence.

**Boot-impact:** DUE-scan green; `board_log` current; `schema_check` ALL CONFORM throughout.


## 2026-08-20 (S33c) — PHASE 2 CLOSED: IQHQ row re-anchored · retirement sweep (3 moved / 3 held) · fleet proposal routed

**Trigger:** Will — "finish out the remaining phase 2 items."

**① IQHQ docket row re-anchored — and it was never a missing-date problem.** The row read `2026-08-XX / 🔴 / pending`, which `boot.py` rendered as the nonsense countdown `T-~-5`. Verified **at the owner** rather than through a summary: OZK mgmt on the 7/22 call had a **multi-year extension + recap in negotiation** (sponsor + mezz lender engaged), interest paid from pre-established reserves, *"will remain a pass-rated credit,"* ~92 days to disclosure — and **OZK's own STATUS says "likely no Aug print."** A-extend 30% + B-migration 45% ⇒ **~75% of the scenario tree produces nothing observable in August.** Re-anchored to the **OZK Q3 call ~2026-10-21, explicitly stamped `[DATE EST]`** (derived from mgmt's "~92 days" + Q2 cadence, **not** a confirmed release notice — ML-RED-173, the tilde that cost six surfaces on WAL V4). **Standing guard written into the row: an August that passes quietly is the MODAL path and must NOT be scored as benign** — the WAL V4 class, already covered by OZK's frozen Option-2 ruling (recognition counts through the Q4'26 print absent an *executed* extension). ⚠️ **Stale figure corrected and it was RED's: the row carried `$140M` weighted EL against the owner's `~$129M`** (7/23 re-weight, Will-approved, OZK-09 52→45) — 28 days behind the publisher.

**② Retirement sweep — 3 archived, 3 held back, and the hold is the finding.** Moved `workbook/CHG-RED-005_EVENING_CHALLENGE.md`, `workbook/CHG-RED-005_REVISED.md`, `workbook/RUSSIAN_OIL_CHALLENGE.md` → `archive/` (now 18 files), each verified zero-reference on **four** axes: RED live docs · RED TSV ledgers · a **fleet-wide external-consumer grep** · and inbound links from other candidates. ⚑ **Held: `challenges/KRE_CHALLENGE.md`, `KRE_CHALLENGE_SUMMARY.md`, `KRE_DEBATE_PREP.md`.** They qualified on age *and* on RED's own live-doc scan — and the external grep found them **cross-linked to `workbook/KRE_EXECUTIVE_SUMMARY.md`**, the R13 collision half already held back on 8/12. **Retiring the leaves while the root waits on T11 leaves that root pointing into `archive/` — strictly worse than leaving them.** **THE CANDIDATE LIST IS A GRAPH, NOT A LIST OF FILES:** a file with zero *referrers* can still BE a *referrer*, and that direction is invisible to a check that only counts inbound links. Method note recorded in `archive/README.md` for the next pass.

**③ Fleet proposal routed — OUTBOX -021.** `review_debt.py` offered to PROME/DAEDALUS as a fleet candidate, **with two deliberate brakes on RED's own result.** ⚠️ **(a) DO NOT circulate the raw fleet total.** 16 desks carry `Stale_By`; 11 populate it; raw past-due is **767 rows** — but RED's own raw count was 33 against an honest 9 (**~73% noise**, terminal-status rows never owed a review). A contaminated number that reads unaffordable gets deferred instead of fixed, which is exactly how RED's debt survived. ⚠️ **(b) THE RANKING INVERTS WITHOUT A COVERAGE AXIS.** Five desks score a perfect **0** — FALCON, HAWK, HOMER, LABOR, WAL — and they are not clean: **0 of 792 rows carry a date at all.** On a naive check those five rank **best in fleet, ahead of every desk that fills the field honestly.** **An unpopulated field scores perfectly**, so the check as it stands would reward *deleting* a review field over honouring it (`finding_verification_zero_is_ambiguous`; the ML-182 corollary, no longer hypothetical). **Coverage (rows dated / rows total) must ship beside the debt count before any fleet adoption** — named as a required change, not a nice-to-have.

**Files touched:** `docket/CATALYSTS.tsv` · `archive/` (+3, `git mv`) · `archive/README.md` · `OUTBOX.md` (-021) · `SCRATCH.md` · `MAINTENANCE.md`. **Boot-impact:** none new; `boot.py`'s countdown stops printing the malformed `T-~-5` row. Verified: `schema_check` ✅ ALL CONFORM, `boot.py` countdown clean, `review_debt` runs.

---

## 2026-08-20 (S33b) — `scripts/review_debt.py` SHIPPED (Will-ruled: "fix the check, not just the rows") + boot step 9c + two published counts corrected

**Trigger:** Will approved both S33 questions — **(1) Phase 2.5 (the Treasury-buyback instrument) jumps ahead of Phase 3**, and **(2) Phase 2 fixes the CHECK, not just the rows.** This entry is ruling (2).

**Constraint that shaped the design:** `scripts/ledger_staleness.py` is a **shared root script outside RED's dir** — RED cannot commit to it (root Git Protocol). So the check is **RED-local first** (`AGENTS/RED/scripts/review_debt.py`, the `boot.py`/`schema_check.py` precedent), proved here, and **proposed onward to the fleet via PROME** — which is also the right order, because ML-182 says every agent carrying a KB/VX review-date column has the same gap and that is not RED's call to make unilaterally.

**What it checks — three axes, and the third is the one a naive version misses:** ① `KB.Stale_By` past-due on non-terminal rows · ② **TERMINAL rows still CITED by a live surface** (STATUS / NEXUS_BRIEF / CALENDAR / SCRATCH / VX / registry) — no review *scheduled*, contents must still be *current*, the `KB-RED-001` class · ③ live `VX.Last_Reviewed` older than 45d. Read-only, exit 0 by default (`--strict` gates, `--quiet` for boot). **Deliberately never keyed on mtime** — git sync restamps it and the check would fail FALSE-NEGATIVE (`finding_mtime_is_corrupted_by_git_sync`); every date is read from row content. **Wired as boot step 9c**, beside 9a with an explicit note that 9a reads FILE vintage and cannot answer a row-level question.

**⚑ THE TOOL'S FIRST RUN FOUND A DEFECT IN ITS OWN AUTHOR'S WORK, AND IT WAS A COUNT PUBLISHED HOURS EARLIER.** `VX.tsv` carries a two-clock banner on **line 0** with the **header on line 1** — the banner says so in prose. The S33 correction was measured with `awk NR>1`, which skips the banner and then **reads the HEADER ROW AS A LIVE VECTOR**. So *"9 of 18"* went out on four surfaces; the true denominator is **17**. The numerator was unaffected (the header's `Last_Reviewed` cell is the literal string, which loses a date comparison), **so the error appeared ONLY in the total — an off-by-one that flattered the ratio and was invisible by eye.** Corrected on `STATUS.md`, `SCRATCH.md`, `MAINTENANCE.md`, `OUTBOX.md` (-020) and in the `VX.tsv` banner itself, which had also been carrying the *older* wrong figure (*"7 of 14"*) since S30. **Both published figures were wrong and both understated the debt — i.e. both wrong in RED's favour.** The skip-`#`-banner rule is now in `rows()` with the incident written into its docstring: **a prose warning inside a file does not parse.**

**Also this pass:** `NEXUS_BRIEF.md` identity header repaired — body and `As of:` were current to S32 while **line 3 still read `Status: 🔴 vS29` and line 6 `Thesis version: S29`**. The brief was folded; its *identity* line was not, and that line is what NEXUS reads. Now `vS33`, with the weights explicitly marked **current-not-stale** (three closed sessions, no weight change, each saying so) so a reader cannot mistake stability for rot — the inverse of `finding_header_edit_is_the_edit_most_mistaken_for_maintenance`.

**Files touched:** `scripts/review_debt.py` (new) · `CLAUDE.md` (boot 9c + 9a caveat) · `NEXUS_BRIEF.md` · `workbook/VX.tsv` (banner) · `STATUS.md` · `SCRATCH.md` · `OUTBOX.md`. **Boot-impact:** one new ~1s read-only step (9c). Verified after: `review_debt` runs, `schema_check` ✅ ALL CONFORM, `boot.py` ⑤ 🟢.

---

## 2026-08-20 (S33) — KB.tsv Stale_By disposition rule adopted + 33→9 pass; ML status-rot closed

**Trigger:** Will-directed open-items sweep found **33 of 86 KB rows past their own `Stale_By` date** (22 still `ACTIVE`, worst 61d) against a CLAUDE.md rule that says they "must be reviewed/refreshed by that date." Nothing enforces it — `ledger_staleness.py` reads FILE vintage, so KB.tsv scored **clean** while 38% of its rows were overdue. Same blind-spot shape as the VX `Last_Reviewed` gap named at T7.

**What changed — a disposition rule, not just an edit pass.** The 33 decomposed into three populations (ML-RED-181): **(a) 12 terminal-status rows** (`RESOLVED`/`INVALIDATED`/`REVISED`/`CORRECTED`/`VERIFIED`/`DISPUTED-DEMOTED`) that were never owed a re-review — `Stale_By` is a review trigger for LIVE facts and a terminal row carrying one is pure noise; **(b) 9 dated event records**, true as history and dangerous only because nothing marked them as history; **(c) 9 genuine live-content rows.** **Adopted:** terminal rows carry `n/a-historical` / `n/a-resolved`, never a live date; dated event records get `STATUS=DATED-HISTORICAL` so they cannot be read as current state. ⚠️ **The rule's own limit, found during the pass and written into it: terminal status does NOT make a row safe if a live surface CITES it** — `KB-RED-001` is `REVISED` and still feeds VX-001/VX-006 (both STRONG, live) while its Fact cell asserts *"NFP +178K confirms employment channel stalled"* against a **−23K** print. **Disposition is two-dimensional: STATUS decides whether a review is SCHEDULED; CITATION decides whether the CONTENTS must be current.**

**Files touched:** `workbook/KB.tsv` (24 rows across two passes, 33→9 overdue) · `workbook/ML.tsv` (ML-112/113/114 status-rot closed; **ML-180/181/182 appended**) · `STATUS.md` (S33 section + header) · `SCRATCH.md` (S33 addendum + 5-phase plan). **Method:** tab-split only (**never `csv`** — ML-RED-168), whole-file field-count validated pre *and* post, `.tmp` + `os.replace`. `schema_check.py` ✅ ALL CONFORM after.

**Boot-impact:** none — no boot step added. **Deliberately so:** the fix this class actually needs is a CHECK (extend the staleness reader to row-level `Stale_By` and VX `Last_Reviewed`), queued to Phase 2. **Editing the rows without fixing the check buys ~30 days.**

**⚑ Two analytical finds surfaced by the hygiene pass, both logged and one routed:** KFRC Q2 unrecorded for 24 days because its conjunction had already broken on the other leg (ML-180 → 8/28 QCEW input, not scored); and **VX-RED-004's published omission** — the fleet-facing staleness figure read *"7 of 14"* against a measured **9 of 17**, understated in RED's favour, hiding a 79-day-stale SAM/Japan vector whose flip line (`30Y JGB >2.5%`) sits ~1.6pp behind its instrument. Both in STATUS §S33.

---

## 2026-08-20 (S33 boot) — boot step 5.5 CORRECTED: the "dead" WALTER lane is live, and this is the SAME defect as 5.6, found hours later

**Trigger:** S33's boot ran the new step 5.6 clean (top-level `inbox/` empty — S32's drain held) and then found **10 files dated 8/13–8/18 sitting in `inbox/WALTER/`**, the lane step 5.5 had described since 7/09 as NO-OP, empty-by-construction, and safe to retire. Delivered by WALTER's own commits (`2737db745`, `1f7c8c98f`, `88d292654`) and **fleet-wide, not RED-local: 23 agents holding ~216 files the same morning** (HENRY 38 · LIQUID 44 · MARCO 25 · BRENT/BROCK 14 each). **Nothing was lost** — all 10 had been caught independently by boot 1.5's whole-INDEX scan and logged `source=BOARD` during S32's pass. **That is the finding, not the reprieve: the redundancy covered for the spec, and a redundancy is not a control.**

**What changed:** `CLAUDE.md` step **5.5** rewritten from empty-check-or-retire → **LIVE lane with consume/log/move mechanics**, an explicit no-double-log rule for signals already dispositioned under `source=BOARD` this session, `source=INBOX_WALTER` for the rest, and the destination named unambiguously (`inbox/WALTER/processed/`, 117 files — *not* `inbox/processed/`, 5.6's general archive; **this session moved the 10 to the wrong one first and self-caught**). The §3.5 pull-complete exemption is kept as live history: **what lapsed was the empty-directory corollary RED inferred from it, never WALTER's grant.** 10 files `git mv`'d to the lane archive.

**Boot-impact:** step 5.5 goes from a no-op glance back to a real read step (cheap — triage by filename, bodies only on a RED hit). **Standing obligation added: at any boot that changes the channel list, run `ls -R inbox/` and reconcile every directory holding files against a numbered step.**

**⚑ Class, third instance in nine days — `[[finding_canonical_surfaces_stale_inbox_carries_live_state]]`.** S32 added 5.6 because the spec enumerated BOARD + a retired lane and never the general inbox (18 packets). S33 found the retired lane was never retired. **Both are one failure: the boot sequence was audited against its own channel list instead of against the delivery directories** — and the apply-rule that says exactly that was written by S32, *into this memory*, hours before S33 violated it one subdirectory away from where S32 was working. The memory's Instance 3 + a sharpened apply rule land at this session's W7. **The S30 architecture audit graded this boot "symmetric" while both lanes were mis-specced** — a second data point for OUTBOX -019 to DAEDALUS (the audit's coverage claim was about the enumerated set, `finding_scan_keyed_on_naming_reads_local_form_as_absence`).

---

## 2026-08-20 (S32 closeout) — boot step 5.6 added: GENERAL INBOX SCAN — the lane the boot spec never enumerated

**Trigger:** 18 unprocessed packets found accumulated 8/12–8/20 in `inbox/` top level — including the MI3 primary data the docket carried as "unfetched," two decision asks aging 5 days, and two same-day SAM asks. Root cause structural: the boot sequence enumerated BOARD (1.5) and the retired WALTER lane (5.5) but never the general packet directory; the disposition obligation followed the *enumerated lanes*, not the *delivery directory*. Root-cause-consistent with two independent fleet reads same morning (YEYOU YEY-011: 27 unprocessed elsewhere; WALTER's repaired ACTION telemetry) — per PROME, DAEDALUS's ~9/2 pass has the lane class.

**What changed:** `CLAUDE.md` boot step **5.6** added (read/triage every top-level `inbox/*.md`, disposition in `board_log.tsv` `source=INBOX_GENERAL`, `git mv` to `processed/`, answer superseded packets against CURRENT state). No renumbering — 5.6 slots between existing cited steps. **Boot-impact:** one new read step; the S30 architecture audit graded the boot symmetric without seeing this lane, so the audit's coverage claim was about the enumerated set (`finding_scan_keyed_on_naming_reads_local_form_as_absence` class) — flagged to DAEDALUS in OUTBOX -019.

---

## 2026-08-20 (S32) — FT-10 registered (registry 10 → 11 rows) + boot.py: `cmp_op` four-op dispatch, ^SKEW in TICKERS, SKEW-CBOE in METRIC_MAP

**Trigger:** the SKEW ruling (SIG-20260818-004, action:RED) — registering the tail-bid-reload line surfaced that `boot.py`'s comparator silently evaluated every non-`>` operator as `<` (a `>=` row with data would have printed a SIGN-INVERTED verdict — `>=150` read as `<150` = false FIRING at 142.93; FT-08 was shielded only by being unmapped). ML-RED-178.

**What changed.**
- **`registry/FALSIFICATION_TRIGGERS.tsv`** — RED-FT-10 appended (`SKEW-CBOE >= 150 s=4`, ACUTE +2 / MANAGED −2, exit = the standing <140 s=4 kill line; full basis + base-rate provenance in-row). Append verified: trailing newline pre-checked, whole-file field-count 11/11 rows × 15 cols, zero literal quotes kept (the registry's quote-free state is the only reason csv round-trips ever survived it — ML-RED-168).
- **`scripts/boot.py`** — (1) `cmp_op` rewritten to explicit `>` / `<` / `>=` / `<=` dispatch, unknown op now **raises** instead of silently picking a branch; (2) `^SKEW` added to TICKERS (tape section + FT-10's price source); (3) `SKEW-CBOE` added to METRIC_MAP with the lag note (Yahoo ^SKEW publishes lagged → the tool reads completed sessions — the *inverse* of the FT-06 ^VIX-runs-ahead defect, ML-RED-176).
- **Functional verify both directions:** FT-10 renders 🟢 `clear, live 142.93 vs >=150 (dist -7.07)`; `schema_check.py` exit 0 (10/10 files conform); WATCHLINES ops audited (`<`/`>` only — no watchline hits the new paths).

**Boot-impact:** trigger check now evaluates 9 of 11 registry rows live (FT-08 stays unmapped by design). WALTER notified same-pass — co-signed surface, row addition + the comparator fix both named.

---

## 2026-08-12 (S30) — `archive/` recreated (Will-ruled) + 14 files retired into it + the dead-path pointers repaired (T8 / audit R4+R14)

**Trigger:** Will's ruling — *"RED should have its own archive"* — which unblocked T8. Audit R4 (dead `archive/` paths) + R14 (archive backlog) + PROME's prune-scan delta.

**What changed.**
- **`archive/` recreated** with a `README.md` that records what it is, what was archived, what was **held back**, and why the directory had to be recreated at all.
- **14 files `git mv`'d in** from `challenges/`, `reports/`, `research/` — every one verified unreferenced under **both** a loose and a strict reading of *"referenced by a live doc"*.
- **Dead-path pointers repaired** in `CLAUDE.md` (FILES table) and `MEMORY.md` (a **live markdown link in a boot-read file**), repointed to `git show 1cb18fbc3^:…` rather than left claiming paths that do not exist.

**⚠️ The prune's premise was false, and the pointers outlived the content by six weeks.** `1cb18fbc3` (2026-06-30, *"prune dead 0-ref agent archives, public-prep track A"*) deleted **38 RED files**. Two were demonstrably referenced: **`archive/RED_SKELETON.md`** (cited in `CLAUDE.md`'s own table AND `MEMORY.md`) and **`archive/status_snapshots/STATUS_2026-04-02.md`** (a live markdown link in boot-read `MEMORY.md`). **All 38 remain recoverable at `1cb18fbc3^` — the content was never lost, only the pointers broke.** **The prune is NOT reversed**: it was a deliberate public-prep decision that is not RED's to undo, and restoring any file is a Will/PROME call.

**⚑ THE FINDING, and it inverts the audit's own estimate.** The audit reported *"5 of 5 oldest spot-checked UNREFERENCED."* **True of those five, and badly unrepresentative: a full check of all 33 candidates found 19 REFERENCED (58%).** The cause is structural — **age correlates with reference-status** (old files are old precisely because nothing kept pointing at them), so **ranking by age and sampling the head over-estimates the unreferenced share**. **Acting on the extrapolation would have retired 19 files that live surfaces cite.** Same family as ML-RED-163: *a rate computed on a ranked head is a claim about the head, not the population.* ML-RED-175.

**Held back deliberately:** `challenges/KRE_EXECUTIVE_SUMMARY.md` qualifies on the strict reading but is **one half of the R13 name collision** — two documents sharing a basename with **opposite verdicts** (45% *"WILL LOSE MONEY"* vs `workbook/`'s 75% *"A-"*). **Archiving one half while the other stays live makes the collision worse**: the survivor would carry no signal that a contradicting twin exists. Resolve the collision (T11), then retire.

**Boot-impact: NONE.** No boot step reads `archive/`. `schema_check.py` unaffected (it maps files explicitly). **Retirement backlog after this pass: 19 referenced files stay in place; the >60d rule is now satisfiable because a destination exists.**

---

## 2026-08-12 (S30) — disposition-ledger obligation moved off the retired lane + `boot.py` §⑤ makes it checkable (T10 / audit R6)

**Trigger:** Audit R6 — *"the disposition-ledger obligation stayed attached to the retired lane."*

**The defect.** RED's `board_log.tsv` rule lived in **boot step 5.5**, the `inbox/WALTER/` lane, which went **NO-OP on 2026-07-09** when WALTER granted RED the §3.5 pull-complete exemption. **Boot step 1.5 — the whole-BOARD scan that BECAME RED's sole WALTER channel on that same date — carried no ledger obligation at all.** For 34 days the rule governed a channel receiving nothing while the channel receiving everything was ungoverned. Result: `board_log.tsv` dormant **8/07 → 8/12** while RED consumed **two action-addressed signals** unlogged. ⚠️ **The S29 remedy fixed *running* step 1.5 and not *recording* it — which is why the gap survived its own fix.**

**What changed.**
- **`CLAUDE.md` boot 1.5** now carries the obligation as its canonical home: the row schema, the disposition vocabulary (`acted`/`noted`/`deferred`/`info-only`/`skipped`), `source=BOARD`, and the reason it moved.
- **`CLAUDE.md` boot 5.5** demoted to a forward-pointer rather than deleted — *a reader landing there from an old reference needs to be sent forward, not left with silence.*
- **`CLAUDE.md` boot 9** notes that `boot.py` now grades the obligation.
- **`scripts/boot.py` — NEW section ⑤ `BOARD DISPOSITION GAP`.** Compares the newest BOARD signal **addressed to RED** (`action:`/`info:` header scan, reading only files newer than the last logged disposition) against the newest `board_log` row.

**⚑ Why a CHECK and not just a relocated rule.** A moved rule is still a remembered ritual, and the original failed precisely because **nothing checked it** (`[[finding_mechanize_the_cap_not_the_ritual]]`). **And why NOT a staleness alert, for two independent reasons:** `board_log.tsv` is **excluded fleet-wide** from `ledger_staleness`'s outside-glob warning **by design** (~15 agents carry it at top level; counting it would false-fire across the fleet), **and** age cannot distinguish *"no signals arrived"* from *"signals arrived and went unlogged"* — it would fire every quiet week and stay **silent in the exact failure mode**.

**Verified both directions** (the T2 standard — functionally, not by inspection): clean state prints **🟢 nothing addressed to RED is undispositioned**; reproducing the 8/07 state prints **🔴 27 RED-addressed signal(s) … 3 are action:**. `board_log.tsv` restored byte-identical after the test.

**Boot-impact:** one new section at the end of `boot.py` (~+1s, reads only BOARD files newer than the last disposition). No existing section changed.

---

## 2026-08-12 (S30) — VX.tsv review-or-carry pass + PAT-044 two-clock header closes the staleness blind spot (T7 / audit R9)

**Trigger:** Audit R9 (VX = "the one genuinely stale ledger… silent-rot middle, no banner") + RED's own standing open thread that `ledger_staleness.py RED` ran CLEAN while VX was stale.

**What changed.**
- **`workbook/VX.tsv` — 13 of 25 rows touched: 6 MEASURED (instrument pulled, `Flip_If` graded leg by leg), 7 CARRIED.** Carried rows' `Last_Reviewed` **deliberately NOT bumped**; each carries an explicit `CARRIED` marker naming its owner and the instrument that would move it, plus a 2026-09-12 re-review.
- **VX-RED-013 RETIRED** (`WEAK` → `RESOLVED-SUPERSEDED`) at **129 days**, the oldest row in the ledger: its premise *"Sanctions expire Apr 11"* resolved on 2026-04-11 and the Russia ban now runs to 2027-01-31, so its central contingency expired four months before anyone looked. Retired rather than re-dated — re-dating preserves a live-looking row whose contingency no longer exists.
- **`workbook/VX_HISTORY.tsv` +2 rows** (VX-013 retirement; VX-017 evaluated-no-change, logged because the flip condition was *graded and found ungradeable*).
- **`workbook/CHALLENGES.tsv` — both dangling cross-links cleared** (CHG-RED-024 → `VX-RED-022` + `KB-RED-041`; CHG-RED-027 → `VX-RED-022`). These are the **only** gaps in otherwise contiguous sequences (VX 001-026, KB 001-086) — the signature of an ID **cited in a link whose row was never authored**, not a deleted row. Refs removed from the ref-only link columns; the fact recorded in `Resolution` so the claim is not silently erased.
- **`workbook/VX.tsv` gains a PAT-044 two-clock banner at line 0**; **`scripts/schema_check.py` FILES map updated to `skip=1`** for it (same shape as FLOW.tsv).

**⚑ The staleness blind spot, and the repair site was not where RED had it filed.** The standing thread said *"fix the check, not just the file."* **Right about the diagnosis, wrong about the repair site:** `ledger_staleness.py` has *preferred* an in-content two-clock date since 2026-07-22 and falls back to git-commit time only when none is present — and VX.tsv had none while being committed regularly, so it graded permanently fresh. **The fix needed no shared-code edit and no PROME dependency: write the header.** Set to **2026-06-02, the OLDEST LIVE row's `Last_Reviewed`, NOT the pass date**, so the alert stays lit while 7 live vectors remain carried. **Before: `rc=0`, no VX line. After: `⚠️ STALE +72d … → 1 stale`.**

**Boot-impact:** boot step 9a now surfaces VX as stale (intended). `schema_check.py` still reports **10 of 10 conform**. No boot step parses VX.tsv.

**⚠️ Deferred on purpose, and grouped so it is not lost:** every `Flip_If` threshold in VX needs the `instrument_basis` treatment the falsification registry got in T5 — **VX-017 proved an unlabeled threshold is ungradeable** (three instruments, three answers). That is a threshold change and belongs in its own dated pass, alongside FT-07's `sustain=1` and `VX.Strength`'s strength/lifecycle conflation.

---

## 2026-08-12 (S30) — SCHEMA.tsv refreshed against measured reality + `scripts/schema_check.py` shipped (T6 / audit R8 + DAEDALUS sweep item 3)

**Trigger:** Audit R8 ("a co-signed contract that silently drifted") + DAEDALUS's completeness-sweep rider on `CHALLENGES.Resolved_Date`. **T5 widened the gap** — the registry went to 15 columns against a schema documenting 8 — so T6 could not slip.

**What changed.**
- **`workbook/SCHEMA.tsv` 84 → 111 rows.** Registry block rewritten 8 → **15** columns (the `exit_*` quad, undocumented since 7/29, plus S30's `instrument_basis`/`state`/`action_magnitude`). **`docket/CATALYSTS.tsv` (65 rows) and `docket/WATCHLINES.tsv` (12 rows) gained coverage — they had NONE.**
- **Value domains re-declared against MEASURED usage** in 11 columns. **Disposition split by kind rather than flattened wholesale.**
- **`scripts/schema_check.py` NEW** — read-only structural conformance check, exit 1 on drift.

**DATA fixed (only where genuinely wrong):**
- **KB.tsv `Status` + `Epistemic` case-folded to upper — 50 cells.** `ACTIVE` 31 + `Active` 18 → **49**. The split was *temporally clean* (every row after 7/5 lowercase), so an exact-match consumer **silently dropped the 18 newest live rows while reporting success.** ⚠️ **`Epistemic` was worse than the audit found and was never flagged: 18 distinct values on 85 rows against 3 declared, same case split (`FACT` 4 / `Fact` 7).** Case-only — **proven**: 25 lines changed, **0 of them non-case**.
- **PREDICTIONS.tsv RED-21 `Status` `CORRECT` → `RESOLVED`.** A category error, not a vocabulary choice: correctness already lived in `Outcome` (`"RESOLVED CORRECT. BLS USDL-26-1378…"`). Status domain is now exactly `ACTIVE;RESOLVED`.

**CONTRACT widened (where the vocabulary is legitimately richer — data untouched):**
- **`ML.Thesis_Impact` redeclared Categorical → String.** 4 values declared; **104 distinct on 167 rows**, mostly full sentences. For several rows it is *the only prose record of why a weight moved* — flattening would destroy information. The contract was wrong, not the data.
- **`CHALLENGES.Grade`** — the contract said "letter grade A+ to F" while **40 of 46 rows use the WEAK…COMPELLING strength scale**. Two incompatible scales in one column; strength is canonical, 5 letter-graded rows frozen as pre-05/2026 legacy.
- `CHALLENGES.Status` (12 distinct — `RESOLVED-CONVERGED` encodes a real adversarial-cycle outcome), `ML.Status` (19), `ML.Category` (+`CHALLENGE-GRADE`, `CALIBRATION`), `KB.Status`/`KB.Epistemic`.
- **`CHALLENGES.Resolved_Date`** — DAEDALUS's 5 prose-in-a-date-field rows: **shape documented** (split on first space) rather than the rationale stripped; new prose forbidden.
- **`VX.Strength` conflation DOCUMENTED, deliberately NOT fixed** — 13 values across **two axes** (strength `WEAK…COMPELLING` vs lifecycle `RESOLVED-*`/`FIRED`) on 25 rows. Splitting it is a 25-row migration and belongs in its own dated pass; recorded so the next reader doesn't mistake the mess for meaning.
- **`FLOW.tsv`** — noted that line 0 is the FROZEN banner, so a header-keyed parser reads the banner as the header.

**Boot-impact: NONE** (no boot step reads SCHEMA.tsv). **Verified:** `schema_check.py` reports **10 of 10 files conform exactly and in order**, and was tested **both directions** — induced drift (removed one KB column) → exit **1** with the correct diagnosis; restored → exit **0**.

**⚠️ INCIDENT DURING THIS PASS — a fourth member of the S30 tooling class, and the most dangerous.** The first attempt used `csv.reader`/`csv.writer` on KB.tsv and PREDICTIONS.tsv. **Python's csv module treats a literal `"` inside a TSV cell as field quoting**, so a read-modify-write round-trip **silently rewrote PREDICTIONS RED-08's `Outcome` cell from `"` to `W`** — a row the pass was not editing. **The tell was a diff LARGER THAN THE EDIT: 6 rows changed for a 1-row edit.** Restored via `git checkout` (uncommitted) and redone with raw tab splitting. Quote counts: **ML 36 · CHALLENGES 10 · KB 6 · PREDICTIONS 6**; the registry has **0**, which is the only reason S30's two earlier csv round-trips on it were safe — **verified field-by-field against a pre-change backup, 0 unintended changes.** **Rule now in the checker's docstring: never use the csv module on these TSVs.** ML-RED-168.

---

## 2026-08-12 (S30) — FALSIFICATION_TRIGGERS.tsv re-spec: 12 → 15 columns, 7 UNDEFINED exits closed (T5 / audit R7a-R7b / PROME Amendment 3)

**Trigger:** DAEDALUS audit R7 (a: no instrument-basis column; b: no state column) + PROME Amendment 3 (action-magnitude column) + WALTER's `SIG-W-20260811-002` §5 N5 ask, which converges independently on the same file.

**What changed.** `registry/FALSIFICATION_TRIGGERS.tsv`: **12 → 15 columns.** Added `instrument_basis`, `state`, `action_magnitude`, **inserted after `action`** (positions 7-9); `exit_*` moves from 9-12 to 12-15. All existing columns keep their relative order; no column renamed, no row added or removed (9 rows).
- **`instrument_basis`** — exact series/venue/basis + publication cadence + which date governs the sustain count. **N5 scope stated per row rather than assumed**: cash/derived series (HY OAS, CCC OAS, ICSA, VIXCLS, T5YIFR) say explicitly that N5 (i)/(ii) do not bind them.
- **`state`** — closed set `ARMED` / `FIRING-BANKED` / `FIRED-BANKED` / `UN-FIRED` / `BLOCKED`. Aimed at the banner on WALTER's own `FALSIFICATION_FIRED_LOG.tsv` (*"cite this log ONLY for 'did X ever fire', never for 'is X fired now'"*) — `state` answers the second question in a machine-readable cell.
- **`action_magnitude`** — the pre-registered size, or explicit `NONE` with a reason. Closes ML-RED-144.
- **Exits:** 7 rows moved off `UNDEFINED` (FT-02/03/04/05/07/08/09), all set pre-data. **`UNDEFINED` no longer appears in the file.**

**Files touched.** `registry/FALSIFICATION_TRIGGERS.tsv` (the change) · `STATUS.md` §11 + falsification-table note + priority 0 · `thesis/CHANGELOG.md` (A4-mandated) · `OUTBOX.md` (RED-TO-PROME-...-013) · `NEXUS_BRIEF.md` (2 corrections, in-place, still 100/100 lines) · `workbook/ML.tsv` (ML-RED-159..162) · packets to `AGENTS/WALTER/inbox/` and `AGENTS/BRENT/inbox/` (carve-out ①).

**Boot-impact: NONE, and this was verified functionally rather than by inspection.** `boot.py` is header-keyed (`dict(zip(head,row))`), so column count and position are irrelevant to it; WALTER's step 6b/6c is a human read-loop. Re-ran `boot.py` after the change: **all 9 triggers still evaluate, 15/15 fields on every line, 10 lines total (no embedded newlines).**

**⚠️ LANDMINE FOUND BEFORE IT FIRED — record this, it generalizes.** `boot.py`'s `tsv()` keeps a row only if `len(row) >= len(head) - 2`. **Adding 3 header columns without widening all 9 data rows would have failed `12 >= 13` on every row and printed an EMPTY trigger section — no error, no warning, no exit code**, on the very scan that decides whether a pre-registered falsifier fired. **A parser tolerance written to survive dirty data becomes a silent-failure amplifier under schema change, because the two are indistinguishable to it.** ML-RED-159; promoted to auto-memory.

**Why the columns went mid-file and not appended:** the actual consumption path is WALTER's *human* read-loop, and `state`/`action_magnitude` are useless to a human sitting behind `exit_source`, which on FT-06 is ~1,900 characters. Checked for positional parsers before choosing (boot.py header-keyed; WALTER human; their FIRED_LOG banner states the exit quad is parsed by no code on either side), and **notified WALTER before the change landed** with an explicit offer to move the columns to the end if any positional reader exists on their side.

**Not done in this pass, deliberately:** FT-07's sustain=1 (32.5% base rate) and FT-04's regime-descriptor level (64.5%) are flagged in-row but **not re-cut** — threshold changes belong in their own dated pass, and re-cutting bear-side thresholds in the session the bear lost six points is indistinguishable from moving goalposts. Queued.

---

## 2026-08-12 (S29f) — ADDENDUM CLOSEOUT (W-A) spec added to CLAUDE.md; Amendment 10 reconciled

**Trigger:** DAEDALUS audit R2 (root cause of R2/R3) + PROME's sequencing guidance + RED's own per-ending self-audit of 2026-08-12.

**What changed:** `CLAUDE.md` gains a **§ADDENDUM CLOSEOUT (W-A)** block after W10, running at **every session ending after the first in the same day**. 3-step always-floor (A1 STATUS addendum · A2 SCRATCH addendum · A3 commit+push) + 6 conditionals each keyed to a checkable FACT, of which **A4 is load-bearing**: *any* weight / confidence / registered-trigger-state change makes **W3 and W8 MANDATORY**. Plus a one-question self-check with the explicit rider that **"they already know via another route" is not routing**.

**⚠️ Amendment 10 RECONCILED, not overridden:** *"the NEXUS_BRIEF fold goes LAST"* is now **per-ENDING, not per-day**. It was authored for single-ending sessions and is self-refuting in a multi-ending one — on 8/12 the brief declared itself folded-last while four further endings and several commits followed. NEXUS_BRIEF footer updated to flag the revision.

**Evidence base (measured, in the spec):** S29 ended five times; each addendum ran ~3 of 10 W-steps; **W8 skipped 4-of-4, W3 3-of-4**. The repair became its own session (T14).

**Boot-impact: NONE on boot** — this is a write-back-side addition only; boot steps 0-9a unchanged. Sessions that end once are unaffected. **Fleet:** DAEDALUS holds this as a PAT candidate (RED validates, fleet inherits after one clean multi-ending day = audit L5 gate (a)).

**Immediate catch by the new rule:** A4 run against 8/12's own record found the **S29d Policy Rescue 2→4 / Managed 34→32 move had never reached `thesis/CHANGELOG.md`.** Entry written same session with its lateness disclosed rather than backdated.

---

## 2026-08-12 (S29d/e) — DAEDALUS audit + PROME amendments: FT-08 machine form corrected, FT-09 wired into boot.py, WAL V4 docket row added

**Trigger:** `AGENTS/DAEDALUS/upgrades/RED_AUDIT_2026-08-12.md` (18 findings, Will-directed) + PROME's three amendments (durable record in DAEDALUS's inbox; relayed to RED as an addendum packet) + PROME's prune-scan R4 delta packet.

**What changed:**
1. **`registry/FALSIFICATION_TRIGGERS.tsv` — FT-08 machine form CORRECTED (audit R7c).** Was `CORE-CPI-MOM >= 0.4, sustain 1` with the AND-leg (3-mo ann ≥3.0%) stranded in the notes column *beside the sentence explaining why single-leg firing is noise*. boot.py and WALTER read machine columns only → **the row fired on exactly what its own registration forbade.** Now `CORE-CPI-3MO-ANN >= 3.0, sustain 1` — the 3-month annualized figure **is** the conjunction as one machine-readable quantity, so no consumer can fire a half-test. Instrument basis written into the row (R7a). Defect was self-created ~3h after ML-RED-144 diagnosed the class.
2. **`scripts/boot.py` — `T5YIFR` added to `FRED_SERIES` + `METRIC_MAP` (audit R17, promoted to hours-tier by PROME amendment 2).** FT-09 was 24bps from firing while rendering `unmapped metric, manual check`. **`CORE-CPI-3MO-ANN` deliberately left unmapped** — a release-derived 3-month compound has no FRED series and failing loud is correct for it; recorded as a decision, not an omission.
3. **`scripts/boot.py` — numeric precision fixed in two formatters, a defect introduced by change 2 and caught before commit.** Thresholds printed at `.0f` rendered FT-09's 2.55 as **`>3`** (a 24bp-away line displaying as 69bp-away), and the FRED tape printed `2%` for 2.31%. Evaluation was correct throughout; only display rounded. Thresholds now print at registered precision (2dp when sub-100 and non-integer, else integer); tape at 2dp for sub-100 series. **Regression-verified: HY 272bps / CCC 1,023bps / claims 199K unchanged.**
4. **`docket/CATALYSTS.tsv` — WAL V4 row added for 8/13 (audit R5).** Named the next binding test in four narrative surfaces with no docket row; boot.py §3 iterates `status=pending` only, so **the T-1 catalyst RED called binding would not have printed.** Verified now printing ⏰ T-1. Violation of RED's own W4 mirror rule.

**Boot-impact:** §① tape gains a `5y5y Breakeven` row; §② now evaluates FT-09 live (**8 of 9** hard triggers auto-evaluated, up from 7 — FT-08 stays manual by design). CLAUDE.md:59's full-coverage claim is closer but still not literally true; queued with the hygiene batch.

**DEFERRED, deliberately, per PROME's sequencing:** R3 dispute-marking **HELD for BRENT's basis ruling** (one relabeling pass after the ruling, not a marking pass before it — the four existing ⚠️ marks stay); **amendment 3's ACTION-MAGNITUDE column** and R2/R7b/R8/R9/R4/R10-R18 → **dedicated hygiene session.** Absorbing an 18-finding list into a live catalyst day is the R2 failure mode itself.

---

## 2026-08-12 (S29) — two NEW registry triggers (FT-08 core CPI, FT-09 5y5y breakeven); FT-06 fired and exposed a magnitude spec-gap; KB-RED-067 doubly corrected

**Trigger:** S29 write-back (W4/W6/W9) on a live catalyst day + PROME packet `2026-08-11_from-PROME_forum4-close-weights-inputs-and-corrected-references.md` (MIDAS DFII10 flag) + DAEDALUS packet `2026-08-11_..._weekday-range-guard-shipped`.

**What changed:**
1. **`registry/FALSIFICATION_TRIGGERS.tsv` — 2 rows APPENDED, 1 row updated.** **RED-FT-08** (`CORE-CPI-MOM >= 0.4`, sustain 1, action `STAGFLATION-RE-ARM`, +3 — compound: also requires 3-mo annualized ≥3.0%) and **RED-FT-09** (`BREAKEVEN-5Y5Y > 2.55`, sustain 5, action `EXPECTATIONS-UNANCHOR`, +4). Both registered **PRE-DATA** so the S29 −6 Stagflation move reverses on registered lines rather than by argument. **RED-FT-06 marked FIRED** (8/11 close).
2. **⚠️ Registry spec-gap DISCLOSED, not silently patched: FT-06's `action` column named a DIRECTION but no MAGNITUDE** (`MANAGED-DECLINE-CONFIRM`), unlike FT-01 (−2) and the SKEW kill (−2). The −2 was set **post-data** by analogy and is labelled as such in STATUS, the registry notes, CHANGELOG, OUTBOX and NEXUS_BRIEF. **Structural follow-up owed: audit the whole registry for other direction-only actions before the next one fires** — the hole is invisible until a trigger fires. Logged in SCRATCH NEXT SESSION #3. ML-RED-144.
3. **`workbook/KB.tsv` — KB-RED-067 CORRECTED on two axes** and `Stale_By` pushed 2026-08-15 → 2026-09-15. (a) the dead **"DFII10 series high" label** (post-2024 / ~2.75-yr high; all-time 3.15 [11/2008]; owner **BOND**) ⚠️ **[SUPERSEDED 2026-08-27 S34 — the corrected label recorded here was ITSELF wrong: it is post-**2023** / ~2.77-yr, verified at the FRED primary. This dated entry is left INTACT as an accurate record of what the 8/12 pass did; the live correction is in `workbook/KB.tsv` KB-RED-067 and STATUS priority #7. Do not cite this line for the label.]** — flagged by MIDAS via PROME; (b) a **stale LEVEL** nobody flagged (2.37-2.39 vs an actual **2.43 [FRED 8/10]**), found only as a side effect of chasing the label, three days before its own Stale_By. **The same string in `thesis/CHANGELOG.md`, `workbook/ML.tsv`, an outbox packet and `research/FOMC_FRAMEWORK_JUL28-29_2026.md` was DELIBERATELY LEFT INTACT** — those are dated historical records, and rewriting them would damage an accurate account of what was believed when (same principle as the S28 `claim_check` false-positive ruling). ML-RED-149.
4. **`docket/CATALYSTS.tsv`** — rows 48 (July CPI) and 58 (FT-06) resolved with outcomes; **3 forward rows appended**: ~8/17 CARL V2 on OTTO's 10-D panel · Fri 9/11 Aug CPI (RED-FT-08's first live test) · Nov 2026 HHDC (CHG-RED-045 resolution).
5. **`workbook/CHALLENGES.tsv`** — **CHG-RED-045** opened (CARL HHDC kill-rule, resolves Nov HHDC).
6. **Auto-memory:** 1 NEW (`finding_hypothesis_needs_an_instrument_for_its_defining_mechanism`) + **2 EXTENDED IN PLACE** rather than created — `finding_prereg_verdict_boundary_must_be_a_number` (the ACTION-magnitude half of the same defect) and `finding_standing_guard_is_a_false_negative_risk` (the scoped-exemption-read-wider form). **Dedup-before-create honoured: 3 findings, 1 new index row**, against a MEMORY.md sitting at 72% of its byte cap. Edits done in-place via python to preserve the harness hardlinks (verified: inode unchanged).

**Boot-impact:** `boot.py` §2 now evaluates **9** registry triggers instead of 7 — **verified by running it after the edit, not assumed.** FT-08 and FT-09 are not in `boot.py`'s metric map, and it degrades correctly: both render **`⚪ RED-FT-0x <METRIC> — unmapped metric, manual check`**, which is an explicit instruction rather than a silent `n/a`. **They must be graded MANUALLY** — FT-08 at the Fri 9/11 CPI release, FT-09 on the daily breakeven check (FRED `T5YIFR`) — **until someone wires `T5YIFR` into the `FRED_SERIES` map**; `CORE-CPI-MOM` is a release-derived MoM figure and is probably not worth wiring at all. Recorded as a known, correctly-signposted gap. ⚠️ **Also observed on the same run: FT-06 renders `FIRING … sustain '5' needs trail/judgment`** — its VIX source is the live price feed, which carries no close-trail, so boot.py **cannot auto-count a sustain window for it.** That is why this session's fire was graded by hand against FRED `VIXCLS` closes; **do not read boot.py's FT-06 line as a completed sustain count.** Boot steps and CLAUDE.md FILES tables otherwise unchanged; no files created, moved or retired.

---

## 2026-08-07 (S28) — CATALYSTS.tsv blank-row repair + 4 forward rows; NEXUS Amendment 10 brief-fold ordering adopted

**Trigger:** S28 write-back (W4/W9) + PROME fleet-propagation packet `2026-08-04_from-PROME_nexus-amendment-10-brief-fold-ordering.md`.

**What changed:**
1. **`docket/CATALYSTS.tsv` — pre-existing blank row removed** (was line 40 in the committed file, confirmed against `git show HEAD:`). It predates this session; found when a schema check threw on it. File is now 60 rows, all NF=9. *A blank row is invisible to eyeball review and throws any strict TSV reader — worth the 5-second check at every write-back.*
2. **4 forward rows added:** `2026-08-11` FT-06 earliest completion (with the DIET-guard disposition **pre-decided before the print**) · `2026-08-19` July FOMC minutes (makes LABOR's 7/29 grade final) · **`2026-08-21` CHG-027 HARD BACKSTOP** (self-imposed; carries its own declared failure mode) · `2026-08-28` QCEW preliminary benchmark (largest scheduled labor risk in the window).
3. **Two rows re-statused:** the `2026-08-04` BDC cluster row → **`BLOCKED`** (printed but never graded — see CHANGELOG S28 ⑥); the `2026-08-07` CHG-044 amendment window → `resolved` (closed with no response, explicitly not scored as vindication).
4. **`registry/FALSIFICATION_TRIGGERS.tsv`** — FT-01 `exit_source` rewritten for the re-fire + composition adjudication; **FT-06 `exit_source` now carries the broken-streak-resets ruling** so the semantics live with the trigger rather than only in STATUS prose. **`docket/WATCHLINES.tsv`** — WL-03 re-armed as FT-01's live exit.
5. **NEXUS Amendment 10 ADOPTED:** the `NEXUS_BRIEF.md` fold is now the session's **LAST** write-back — after the final STATUS write, immediately before git commit (checkable form: brief commit timestamp ≥ STATUS commit timestamp). Executed that way this session. *Rationale worth keeping: the 7/31 fleet audit found 5-of-5 content-stale briefs had refreshed and then kept working — refreshing is not the fix, ordering is.*

**Files touched:** `docket/CATALYSTS.tsv`, `docket/WATCHLINES.tsv`, `registry/FALSIFICATION_TRIGGERS.tsv`, `NEXUS_BRIEF.md`, `MAINTENANCE.md`.

**Boot-impact:** `boot.py` DUE-scan and catalyst countdown now surface the 8/11 / 8/19 / 8/21 / 8/28 rows; the BLOCKED status makes the ungraded BDC gate visible at boot instead of reading as a benign pending row. No schema or boot-path change — `CLAUDE.md` needs no edit.

## 2026-07-24 (S25, evening) — FOMC framework versioned to v1.1; docket re-anchored ±2 months; KB.tsv stray blank line removed

**Trigger:** CARL inbox packet falsifying a load-bearing premise in `research/FOMC_FRAMEWORK_JUL28-29_2026.md` (shipped ~6h earlier in S24) + LABOR packet correcting a docket date + adding a fleet-unowned FOMC leg.

**What changed (structural only — analytical content in `thesis/CHANGELOG.md` 2026-07-24 S25):**

| File | Change | Boot-impact |
|---|---|---|
| `research/FOMC_FRAMEWORK_JUL28-29_2026.md` | **Versioned v1.0 → v1.1.** Added §0 (correction + evidence table), §0b (CHG-028 three-rung re-spec), §L (oil-language sub-axis), §LAB (labor-language sub-axis), Guards 6-7. **Corrections are struck-and-marked in place, not silently rewritten** — v1.0's priors remain readable so the amendment can be graded separately. | None (research/, not boot-read). Execute on 7/28-29. |
| `docket/CATALYSTS.tsv` | KFRC row re-dated **8/04 → 7/27**; July-CPI row re-specced to a pre-registered non-event (priority 🔴→🟠); **5 rows added** — Aug CPI **9/11**, Sept CPI **10/14**, Oct CPI **11/10**, ECI **7/31**, Sept FOMC **9/15-16** (added as `[DATE EST]`, all verified later the same session — see below). | boot.py catalyst countdown now surfaces KFRC at T-3 instead of missing it; ≤14d window gains ECI. |
| `STATUS.md` | CHG-028 row rewritten; priorities 1/6 rewritten, 7-8 added; scorecard 2→3 ACTIVE; missing-data gains a date-verification block. | Still <200 lines. |
| `workbook/` | ML-RED-110…115 (6); KB-RED-070…076 (7); PREDICTIONS RED-21; CHALLENGES CHG-028 row updated in place (Status → `LIVE-RE-ANCHORED`). | — |
| `workbook/KB.tsv` | **Hygiene: removed a stray mid-file blank line (old line 55, between KB-054 and KB-055).** Pre-existing and committed — confirmed via `git show HEAD:` before touching, so it was not introduced this session. A 0-field row breaks naive TSV parsers. | Removes a silent-fail risk in any future KB reader. |
| `board_log.tsv` | 5 dispositions logged; 5 packets `git mv`'d to `inbox/processed/`. | Inbox empty again. |

**✅ Follow-up CLOSED same session (S25b, Will-directed) — and it mattered: 3 of the 4 CPI dates were wrong.** Verified vs the **OMB/White House PFEI CY2026 schedule** + usinflationcalculator (independent 2nd) + federalreserve.gov. **July CPI = Wed 8/12 (the fleet, including me, carried 8/13)** · Aug = **Fri 9/11** · Sept = **Wed 10/14** · Oct = **Tue 11/10 ✅** · Sept FOMC = **9/15-16 ✅, carries an SEP** · ECI = **Fri 7/31 ✅**. All `[DATE EST]` markers removed from the docket; framework → **v1.1a**; correction packet routed to HENRY/CARL/PROME + `outbox/2026-07-24_to-FLEET_cpi-calendar-correction-july-print-is-8-12.md`.

**🔧 Tooling finding (fleet-relevant, KB-RED-077):** **`bls.gov` returns HTTP 403 to WebFetch *and* to curl with a full browser UA** — the usual user-agent workaround does not work. Use the **OMB PFEI CY2026 PDF as the accessible primary**, and extract it with **`pdftotext -layout`**; plain `pdfminer.extract_text` scrambles the month-grid into unusable fragments.

**📋 Process rule adopted:** **verify a date in the same pass that creates the dated row.** I created five `[DATE EST — verify]` rows and deferred verification to "next boot" — the ML-RED-064 MI3 failure mode exactly, missed by one day only because Will redirected. A row marked "verify later" is a row that will be cited before it is verified.

**⚠️ Fleet hygiene flagged to PROME (not RED's to fix):** **PROME has two live inbox paths** — `PROME/inbox/` and `AGENTS/PROME/inbox/` — both receiving traffic from different agents on the same day, with root `CLAUDE.md` asserting the second doesn't exist. Delivered to both; needs a precedence ruling.

**Not changed:** no hypothesis weights, no confidence, no VX vectors (checked — none of this session's data touches a vector's `Flip_If`). `CLAUDE.md` unchanged (no new boot step; the framework was already a `research/` artifact).

---

## 2026-07-24 (S25, late) — ⚠️ CROSS-DIR: `AGENTS/PROME/` migrated and removed on Will's explicit instruction

**Logged here even though it is outside RED's tree**, because a future RED reading `git log` will find RED commits touching `PROME/`, `AGENTS/WALTER/` and `AGENTS/DEWEY/` and needs to know why that was authorized.

**Trigger:** RED's S25 hygiene flag (PROME had two live inbox paths receiving traffic from different agents the same day) → Will ruled in-session: *"PROME uses PROME/inbox — kill the AGENTS/PROME one"*, then *"tell PROME to fix BOOT.md step 6."*

**Authority:** Will, explicit, per-instance. **This is not a precedent** — root CLAUDE.md's "never write outside your own dir" stands; the carve-out here was a direct operator instruction, and the self-authored-packet carve-out covered the notices.

**What was actually there — the reason this wasn't a one-line delete:** **55 files**, including **5 live unprocessed packets** (2× DEWEY 7/24, 1× WALTER 7/24, 1× RED, + WALTER signal `SIG-W-20260724-006` written 2026-07-24T23:55Z, still `written_not_delivered_pending` in WALTER's own delivery log).

| Content | Destination | Commit |
|---|---|---|
| 5 live unprocessed | `PROME/inbox/` (flat, top level — unmissable at boot) | `46d79cd8` |
| 16 `inbox/processed` + 33 `WALTER/processed` | `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/reaccumulated_2026-06-25_to_07-24/` + README | `46d79cd8` |
| `.claude/settings.local.json` — **gitignored**, so git history would NOT have preserved it | copied to that archive as `PRESERVED_settings.local.json.txt`, then `gio trash` (no `trash`/`trash-put` binary on this box — root rule 11 honoured via the available tool) | `46d79cd8` |
| Notices to WALTER / DEWEY / PROME | their `inbox/` dirs, per the self-authored-packet carve-out | `46d79cd8`, `8a84190a` |

**★ The finding worth keeping, not the deletion:** `AGENTS/PROME/` **had already been archived on 2026-06-24 — and regrew to 55 files in one month**, because ~30 rows of WALTER's `routed/delivery_log.tsv`, DEWEY's routing, and **PROME's own `BOOT.md` step 6** all still pointed at it. *Deleting a dead shared path does nothing; the writers are the root cause.* RED flagged all three owners and edited none of their files. **Promoted to auto-memory** (`finding_dead_path_regrows_unless_senders_repointed`).

**Also flagged, not fixed (owners' calls):** `PROME/CLOSEOUT.md:24` carries the same stale claim as BOOT step 6; `PROME/GIT_COORDINATION.md` lines 34/131/142 read *more* correctly post-deletion and must **not** be swept by a find-and-replace; the preserved settings file granted a bare `Bash(git *)` that PROME's live settings lacks.

**Boot-impact on RED:** none. Watch item added to SCRATCH OPEN THREADS: **if `AGENTS/PROME/` reappears, that is the sender-routing regression, not a delivery surface.**

---

## 2026-07-24 — NEXUS_BRIEF refresh hardened into W8 (was un-listed in the write-back sequence; sat one session stale)

**Trigger:** Will asked at S24 close whether RED's `NEXUS_BRIEF.md` had been updated today — it hadn't (stamped 7/17/S23), despite its own footer promising per-closeout freshness. Root cause: the brief was stood up 7/6 (PROME/NEXUS ask, `inbox/processed/2026-07-06_from-PROME_via-NEXUS_write-nexus-brief.md`) but was never added to the SPAWN PROTOCOL's W1-W10 write-back list, so the S24 closeout — which ran every listed W-step — skipped it cleanly. A checklist can only protect what's on it.

**What changed:** `CLAUDE.md` W8 now includes "Refresh `NEXUS_BRIEF.md` whenever state moved this session"; also folded the root-canon self-authored-packet carve-out (ratified 7/23) into W8's "never write into another agent's directory" line, which had gone stale against root CLAUDE.md. Brief itself rewritten to vS24 in the same pass.

**Files touched:** `CLAUDE.md` (W8), `NEXUS_BRIEF.md` (vS23→vS24), this file.

**Boot-impact:** none at boot; write-back gains one conditional step. Skip-condition is explicit: a session that moved NO state (pure read/verify session) may leave the brief untouched — the footer stamp then honestly shows the last state-moving session.

**Trigger:** WALTER notice `inbox/2026-07-09_from-WALTER_pull-complete-exemption.md` (Will-approved design-walkthrough 7/9) — RED added to BOARD_CONSUMPTION_SPEC §3.5 v0.8 alongside CARL: boot step 1.5's whole-INDEX BOARD scan already IS RED's complete pull (auto-cc INFO-only, never ACTION owner on a WALTER dispatch → zero ACTION-miss risk from dropping the per-signal handoff lane, which was 24% of delivery-lane volume and the largest unconsumed-INFO pile).

**What changed:** `CLAUDE.md` step 5.5 rewritten — WALTER stops writing to `inbox/WALTER/`; the step is now a no-op / cheap empty-check rather than live intake. Step 1.5 corrected 10→12 cluster sections (CLIMATE_MACRO added 6/28, missed in the original count). Drained the pre-exemption backlog same session (8 files: `board_log.tsv` rows + `git mv` to `processed/`) before the lane went dormant.

**Boot-impact:** step 5.5 no longer needs a live glob-and-disposition pass each boot; step 1.5 is now the sole WALTER-signal channel. Friction → log here if `inbox/WALTER/` ever gets a stray post-exemption file (should route to `walter_doctor` as a to-ARCHIVE flag per WALTER's own doctor script).

---

## 2026-07-05 (Session 22) — 12-day catch-up: board_log.tsv created, 98-signal inbox drain via workflow, 6/26 partial-closeout swept, FLOW frozen

**Trigger:** Will-directed 12-day catch-up (last full closeout S21b 6/23). A **6/26 partial session** had filed CHG-RED-041 + its challenge report but never updated STATUS/SCRATCH/CALENDAR/CHANGELOG (left anchored 6/23) — swept this session.

**(1) `board_log.tsv` created (v0.2 schema).** First WALTER-lane delivery log for RED (`timestamp_read / signal_id / disposition / source / notes`). 98 backlogged `inbox/WALTER/` signals triaged via a background **Workflow** (10 agents, batches of 10, structured-schema classification: 0 ACTION / 26 moves-weight / 66 watch), then bulk board_log'd + `git mv`'d to `processed/`. Commit `4917ea0e`.

**(2) Workflow `args` gotcha (tooling lesson).** The Workflow tool delivered `args` to the script as a JSON-**encoded string**, not an array (`files.slice().map` threw on the string). Fix: defensive `Array.isArray(args) ? args : JSON.parse(args)` atop any workflow taking `args`. First run failed 0-agents; second succeeded.

**(3) Pre-commit sanity caught a concurrent NEXUS session.** During the drain, `git diff --cached` surfaced 3 foreign-staged NEXUS files + HEAD had moved to a PROME commit since boot = an active concurrent NEXUS+PROME session. Pathspec commits (`git commit AGENTS/RED/…`) correctly excluded all of it. **Push held (Will-coordinated)** — do not sweep-push while NEXUS is mid-flight.

**(4) FLOW.tsv FROZEN.** +87d stale behind STATUS (ledger_staleness flag). Prepended a `# FROZEN 2026-07-05` banner (audit-only, Apr-vintage rows); STATUS/VX/CHALLENGES are canonical for live break-pathway logic.

**(5) CATALYSTS date corrections.** WAL Q2 re-dated ~7/16 (was 7/30 — REGINALD, 2wk earlier); OZK 7/21 pinned; +3 rows (30Y auction 7/9, EGBN 7/22, DISH-rebalance 7/31 mechanical-CCC trap).

**Boot-impact:** `board_log.tsv` is new (boot step 5.5 now has a log to append to). `inbox/WALTER/` top-level empty again. FLOW frozen (staleness alert clears). No schema/boot-path changes. KB +7 / ML +3 / VX 3-reviewed / CATALYSTS +3.

---

## 2026-06-23 (Session 21 + 21b) — Crash recovery + 40-signal WALTER inbox sweep + CRLF tooling lesson

**Trigger:** S21 session (6/23 ~8:38 PM) crashed mid write-back; Will then directed a chunked sweep of the WALTER inbox backlog.

**(1) Crash recovery (no data loss).** The crash hit during the *atomic rename* of STATUS.md (write-to-temp → rename never landed). Recovered by completing the interrupted write from the `.tmp.<pid>` atomic-write temp (lost exactly one edit — the Brent/OVX 6/23 counter-signal row). HEAD object-integrity clean (no repeat of the SAM 6/22 git-corruption); fleet tree clean. Commit `74af4477`. Crash temp parked in session scratchpad (redundant once STATUS recovered).

**(2) WALTER inbox fully drained — 40 signals → `inbox/WALTER/processed/`.** Processed in 5 themed chunks (A banks/credit 5 · B oil/Hormuz 11 · C FL/housing 5 · D Japan/FX/rates 5 · E positioning/consumer 12), each git-mv'd and committed separately (`3bac8c26`/`2928a378`/`5a144add`/`4ec9ffb2`/`0477eae6`). Analytical content → `thesis/CHANGELOG.md` (NO weight change; 3 residuals). `inbox/WALTER/` top-level now empty; processed/ holds all 40.

**(3) CRLF tooling lesson (boot-relevant for any TSV editor).** RED's workbook/docket TSVs are MIXED line-endings: VX.tsv, KB.tsv, CATALYSTS.tsv, CHALLENGES.tsv are **CRLF**; ML.tsv, VX_HISTORY.tsv are **LF**. A Python *text-mode* read/write silently converts CRLF→LF across the WHOLE file → destructive whole-file diff + merge risk on the shared branch (hit once on VX.tsv mid-sweep, caught pre-commit via `grep -c $'\r'`, restored from HEAD, re-applied in **binary mode** preserving `\r`). **Rule: edit CRLF TSVs in binary mode (split on `b"\n"`, preserve trailing `b"\r"`); `printf`-appended rows (LF) into CRLF files are non-destructive (clean +N) and fine.** Promoted to auto-memory `finding_crlf_textmode_tsv_flip`.

**Boot-impact: neutral.** No file added/moved/renamed structurally; STATUS/SCRATCH/CHANGELOG/CALENDAR refreshed in place; 6 KB + 5 ML + 3 catalyst + 1 challenge rows appended, VX-025 refined. Next boot's BOARD-consumption pass finds inbox/WALTER/ empty (all 40 filed).

---

## 2026-06-02 (Session 16) — SAM-pattern adaptations: CATALYSTS.tsv backbone + this MAINTENANCE log + boot-slim

**Trigger:** Will — "other agents developed meaningful structure; adapt some for RED." Studied SAM; adopted three patterns.

**(1) New `docket/CATALYSTS.tsv`** (structured forward-catalyst backbone, adapted from SAM `docket/CATALYSTS.tsv`). 28 forward catalysts (imminent→Dec), 9 cols: date / window / event / bear_signal / bull_signal / red_threshold / priority / status / notes. **Now the queryable source of truth for catalyst dates/thresholds** (row-by-row prunable — the fix for *why* CALENDAR went stale: prose tables are hard to update incrementally).
- **`CALENDAR.md` slimmed:** removed the IMMINENT + IMMEDIATE + NEAR-TERM + MEDIUM-TERM date-tables (~85 lines, migrated to TSV) → replaced with a pointer + top-imminent summary. **Also dropped a genuinely stale "IMMEDIATE (May 22-29)" section** (already-past events: Tokyo CPI 5/22, calibration retro 5/25, AFT 5/28, OZK 5/29). CALENDAR keeps the narrative layer: RESOLVED history, FALSIFICATION WATCH, scoring windows, exit backstops.

**(2) New `MAINTENANCE.md`** (this file, adapted from SAM `MAINTENANCE.md`). Splits structural-change logging out of `thesis/CHANGELOG.md` (which was carrying both). Going forward, file/schema/boot changes log here.

**(3) Boot-slim `MEMORY.md`** (adapted from SAM boot-slimming discipline). MEMORY's methodology section had grown to multi-hundred-word bullets read in full every boot. Moved the verbose bodies to `MEMORY_ARCHIVE.md` (lossless), kept one-line lesson + `→ MEMORY_ARCHIVE.md#anchor` pointer inline. Load-bearing lessons stay scannable at boot; full depth one pointer away.

**(4) Loop-closer — `CLAUDE.md` updated** so future-RED finds the new structure: boot step 3 now scans `docket/CATALYSTS.tsv`; boot step 4 notes structural changes live here not CHANGELOG; Core-Files table updated (MEMORY = one-liners + archive; CALENDAR = narrative layer; CATALYSTS.tsv added); new "Reference/archive" table rows for `MAINTENANCE.md` + `MEMORY_ARCHIVE.md`. (Did NOT touch the 3 separately-flagged charter items — dual PREDICTIONS, RED_SKELETON refs, TIMELINE staleness — those await Will.)

**Boot-impact: positive** — CALENDAR ~150→88 lines (15.7→11.3KB); MEMORY 35.7→17.6KB (−50%, methodology bodies → MEMORY_ARCHIVE.md); combined RED-owned boot read ~73→~51KB. CATALYSTS.tsv read selectively (status=pending next ~14d), not in full.

**Also this session (logged in `research/STALENESS_AUDIT_2026-06-02.md`, summarized here for the structural record):**
- **Repaired missing `.venv`** (didn't exist; `python3 -m venv --without-pip` + get-pip bootstrap + `pip install yfinance requests`). Market tool live again. NOTE: `.venv` is gitignored; proper fix is `sudo apt install python3.12-venv` (needs Will's sudo).
- **Dedupe:** removed 5 md5-identical `archive/`↔`challenges/` copies (kept challenges/).
- **Relocated** completed VIOLET skew-recheck bundle (10 files incl 1.78MB CSV) → `archive/violet_skew_recheck_apr2026/`; 3 old-format TSVs → `archive/superseded_workbook/`; loose HAWK signal → `inbox/processed/`.
- **Schema fix:** normalized 2 ragged `workbook/KB.tsv` rows (12/14-col) → all 42 rows uniform 13-col.

---

## 2026-06-02 (Session 16, cont.) — retired the duplicate/contradictory `thesis/PREDICTIONS.tsv`

**Trigger:** Will — "take a look at Predictions." Investigation of the dual-file flag (audit §C item 1).

**Finding:** `thesis/PREDICTIONS.tsv` wasn't just stale — it was the **unreconciled pre-ML-RED-068 fork** with *contradictory IDs*. It numbered the May predictions RED-11–14 (conflicting with canonical, where RED-11–14 = the Apr-18 batch and the May predictions = RED-16–19), and was missing the Apr-18 batch + RED-15–19 entirely (14 rows, ragged 6/7-col, last touched May 17). The Session-14 ML-RED-068 cleanup reconciled STATUS/MEMORY/CALENDAR but **missed this file.**

**Fix (lossless):**
- `git mv thesis/PREDICTIONS.tsv → archive/superseded_workbook/PREDICTIONS_thesis_unreconciled_PRE-ML-RED-068.tsv` (verbatim preserved). Verify-before-archive: confirmed `workbook/PREDICTIONS.tsv` is a complete superset (RED-01–19, uniform 10-col) and the only genuinely-unique content (BRENT v2.0 challenge-rationale phrasing) lives in `CHG-RED-024` / `challenges/BRENT_V2_CHALLENGE.md`.
- New breadcrumb `thesis/PREDICTIONS_README.md` — points to the canonical file + warns against re-forking.
- **`CLAUDE.md` updated:** removed `thesis/PREDICTIONS.tsv` from the Thesis-Directory table; added a callout that `workbook/PREDICTIONS.tsv` is sole canonical.

**Resolves:** charter-flag item 1 (dual PREDICTIONS). Remaining flagged items: RED_SKELETON refs in CLAUDE.md; `thesis/TIMELINE.md` staleness.

---

## 2026-06-02 (Session 16, cont.) — cleaned up retired `RED_SKELETON.md` references in CLAUDE.md

**Trigger:** Will — "look at the RED_SKELETON references" (audit §C item 2).

**Finding:** `RED_SKELETON.md` was retired Apr 5 (superseded by `workbook/VX.tsv`), but `CLAUDE.md` still cited it as a **live** reference in 3 places — "Reference for deep work," "Rebuild when time permits," and an anti-pattern — risking a future RED consulting or rebuilding a **Feb-12-vintage** file (per-agent counter-evidence registry incl. a stale agent roster: CREED, old MARCO framing). Verified VX.tsv (per-target vectors) fully supersedes its counter-evidence content; nothing unique to salvage.

**Fix:**
- `CLAUDE.md`: removed the `RED_SKELETON.md` row from the WHAT YOU READ table; removed the "Reference (not boot-critical)" subsection and re-filed it under **Archive** as `archive/RED_SKELETON.md` **RETIRED** (do-not-rebuild); generalized the anti-pattern to "don't trust stale registry data — verify VX/KB `Last_Reviewed`/`Stale_By`."
- `MEMORY.md`: corrected the Apr-5 "DELETED" note (archived copy retained; CLAUDE.md mentions cleaned up).
- `archive/RED_SKELETON.md` itself kept as historical record (correctly placed).

**Resolves:** charter-flag item 2. **Remaining flagged item:** `thesis/TIMELINE.md` staleness (Apr 20, predates channel-migration).

---

## Pre-S16 (retroactive note)

Before S16, structural and analytical changes were both logged in `thesis/CHANGELOG.md`. Earlier structural history (folder reorganizations, the Apr 5 RED_SKELETON deletion, workbook 7-col→14-col migration, the May WALTER LIAISON file instantiations) lives in `thesis/CHANGELOG.md`, `MEMORY.md` "Cleanup Done" notes, and git history. This file starts the clean separation.

---

## STANDING HYGIENE CHECKLIST (run periodically — candidate for a future maintenance-steward sub-agent)

- [ ] `workbook/VX.tsv` — review each vector's Last_Reviewed; flip/resolve any whose Flip_If fired; log to VX_HISTORY.tsv. (S16: was 7 weeks stale — don't let it recur.)
- [ ] `workbook/KB.tsv` — review entries past Stale_By; supersede point-in-time facts overtaken by events; extend live themes.
- [ ] `docket/CATALYSTS.tsv` — prune resolved (status→resolved + move to CALENDAR RESOLVED), add upcoming, refresh thresholds vs live anchors.
- [ ] `CALENDAR.md` FALSIFICATION WATCH — refresh spot values vs live (market tool: `.venv/bin/python FORGE/tools/market-data/fetch.py price <tickers>`).
- [ ] `STATUS.md` ≤200 lines; archive detailed reports to `reports/`.
- [ ] Dedupe `archive/` vs `challenges/`; relocate completed research to `archive/`.
- [ ] Cross-file consistency: PREDICTIONS scoring matches across STATUS/CALENDAR/workbook (S16 caught a RED-19 contradiction).

---

## 2026-06-10 (S17) — Market-tool "breakage" diagnosed: interpreter selection, NOT a broken tool (S16 venv punchlist item CLOSED)

**Symptom:** `python3 FORGE/tools/market-data/fetch.py price ...` → `ModuleNotFoundError: No module named 'yfinance'`. Looked like the S16 "yfinance missing" regression.

**Diagnosis (verified, not assumed):** NOT broken, NOT API overload. The error is a deterministic import failure — it fires before any network call, so rate-limiting/overload is excluded. Root cause: bare `python3` = Ubuntu system interpreter, which is PEP-668 externally-managed (`/usr/lib/python3.12/EXTERNALLY-MANAGED`) — packages can never be pip-installed there by design. All repo packages live in `.venv/`.

**Verified healthy state:** `.venv/bin/python3` = Python 3.12.3 with yfinance 1.2.0 + pandas 3.0.2 + working pip; `fetch.py price` returns live quotes; `dashboard.py` renders Tier 1/2 clean (tested 6/10 ~3:15 PM ET).

**Rule:** always invoke market tools as `.venv/bin/python3 FORGE/tools/market-data/fetch.py ...` (venv activation does not persist across shell calls). The hygiene checklist below already says this — the S17 boot miss was using bare `python3` from muscle memory before re-reading it.

**Closes:** S16 punchlist item 4 ("proper venv fix: sudo apt install python3.12-venv; pin pandas; test dashboard.py") — overtaken by events. Venv exists with working pip (no apt package needed for current state); pandas 3.0.2 runs dashboard.py without error (no pin needed); dashboard tested ✅.

**Optional shared-tooling improvement (Prome-side, NOT RED's file to edit):** `fetch.py`/`dashboard.py` could self-re-exec under the repo venv when imported modules are missing, making them interpreter-agnostic for all agents. Flagged via OUTBOX rather than edited directly (FORGE is shared tooling).

---

## 2026-06-10 (S17) — SPAWN PROTOCOL codified: BOOT / EXECUTE / WRITE-BACK (closeout hardening, Will-approved)

**Trigger:** Will asked whether RED has a proper closeout vs SAM/BRENT/VIOLET. Audit verdict: RED had the network's best boot and its weakest closeout — write-list buried in boot step 10, one handoff line, no DUE-resolution rule, no live-event override, handoff fragmented across LAST_COMPLETION.md + numbered archive/handoffs/. Plan approved on all defaults (D1-D5) 6/10.

**What changed:**
- `CLAUDE.md`: "BOOT SEQUENCE" → "SPAWN PROTOCOL" with BOOT (read, steps 0-9 — preserved BOARD b1-b4 scan; added DUE-scan to step 3, live-anchors step 9 w/ venv path) / EXECUTE (step 10 + **live-event override**, VIOLET pattern) / **WRITE-BACK W1-W10** (read→write pairings; W2 loop-closure "never OPEN-but-stale" extended to CHALLENGES.tsv — RED-unique; W10 git block w/ local-commit default) / discipline overlay (+ RED-specific: counter-signal weights carry as-of dates) / **Doc-Mirror table** (CATALYSTS.tsv→CALENDAR; PREDICTIONS.tsv→STATUS scorecard; CHALLENGES.tsv→STATUS table; canonical wins).
- `SCRATCH.md` NEW — canonical handoff, template at top, rewritten in place at W5. `LAST_COMPLETION.md` RETIRED (breadcrumb left). `archive/handoffs/` FROZEN (README_FROZEN.md; git history versions SCRATCH).
- File tables in CLAUDE.md updated (WHAT YOU READ, Core Files, Archive).

**Dogfood result (Phase 3, same session):** first DUE-scan run found the predictions ledger materially wrong — RED-12/13/14/15/17 ACTIVE-but-stale since late Apr/May, RED-07 canonical lagging its mirrors, RED-08 STATUS-drifted. **TRUE tally 7W/7C/5A vs published "5W/2C/4A" — wrong on all three numbers.** Dispositioned same session; mirrors synced. Validates the recipe's core claim: mechanical scan > vigilance.

**Boot-impact:** next session boots on the new protocol — reads SCRATCH.md (not LAST_COMPLETION), runs DUE-scan at step 3, uses `.venv/bin/python3` per step 9. Friction → log here.

**Out of scope (deliberate):** NEXUS_BRIEF enrollment (Will/NEXUS-phase decision, D3), scripts/boot.py build, KOYOMI-analog steward (Will-deferred S16).

---

## 2026-06-10 (S17, evening) — `scripts/boot.py` built (boot kit; closes the last parity carve-out)

**Trigger:** Will: "FORGE may be a little dated… keep as-is or build?" Plan approved on all defaults (D1-D5).

**What changed:**
- `scripts/boot.py` NEW (~250 lines, READ-ONLY): ① TAPE (11 tickers via FORGE `fetch.py` imported as a library + FRED HY/CCC/claims) ② TRIGGER CHECK (registry hard triggers + WATCHLINES soft lines, live distance + FIRING/NEAR/clear, true sustain-trail evaluation on FRED metrics) ③ CATALYST COUNTDOWN (docket pending ≤14d, fuzzy-date tolerant) ④ DUE-SCAN (predictions past-timeframe → 🔴; unparseable timeframe → ⚠️ manual; ACTIVE challenges listed with age). Venv self re-exec shim — bare `python3` now works for this script.
- `docket/WATCHLINES.tsv` NEW (11 rows): soft/display thresholds (VIX>23 VIOLET line, VIX>20 window, HY 280 re-cross, CCC 955/1000 gates, USDJPY 160, KRE/WAL/SPY position legs, Brent<95 sub-trigger-d). Deliberately separate from `registry/FALSIFICATION_TRIGGERS.tsv` (WALTER auto-fire surface — display rows there could cause unwanted dispatches).
- `CLAUDE.md` boot step 9 → run boot.py; Doc-Mirror table gained the triggers row.

**Dogfood (live test vs known answers):** ①-③ matched the hand-built S17 picture exactly (FT-01 sustained-firing 278/275/276, FT-07 firing, VIX>20 firing, re-cross NEAR −2, CCC gate NEAR −4, T-1 backstop). **④ found catch #3 of the day: 14 stale ACTIVE challenges from April (CHG-RED-006..022, 53-69d old)** — never status-dispositioned (e.g. CHG-RED-008 "rescue revised to 20%" vs current 4%; CHG-RED-018 owed-closure from Apr). Queued as next-session cleanup pass (needs per-row resolution notes, not a rush job).

**Boot-impact:** boot steps 3+9 mechanical halves now one command. Friction → log here. Known limits: yf metrics can't evaluate multi-day sustain (flagged inline); fuzzy timeframes print ⚠️ manual rather than silently passing.

## 2026-07-31 — S27
- **Trigger:** boot found two write-back misses from the S26 night session (PROME-spawned, post-outage). **What changed:** (1) `thesis/CHANGELOG.md` — S26's owed W3 entry (weights 62→68) was never written; backfilled at S27, explicitly labeled BACKFILLED. (2) `NEXUS_BRIEF.md` — skipped its promised per-closeout refresh a SECOND time (first: 7/24); rewritten to vS27, stale 8/13-CPI catalyst row purged. Pattern note: both misses came from a spawned night session running a 4-item task packet — the write-back tail is exactly what a scoped spawn skips (cf. auto-memory `finding_spawned_agents_ship_artifact_skip_writeback`). **Files touched:** thesis/CHANGELOG.md, NEXUS_BRIEF.md. **Boot-impact:** none structural; W3/W8 unchanged as rules — the gap was invocation, not specification.
- **Registry:** FT-01 row rewritten to EXIT-EXECUTED/RE-ARMED state (first exit ever executed off `registry/FALSIFICATION_TRIGGERS.tsv`); WL-03 note updated to COMPLETED-but-live-as-exit-semantics. No schema change.
- **CLAUDE.md amendment (same day, follow-on):** `feedback_red_edge` one-liner embedded into the IDENTITY block per PROME's Phase-2 embed packet (memory three-tier restructure — the row no longer auto-loads from MEMORY.md; CLAUDE.md is now its auto-loading home). Confirmation routed via OUTBOX #4; packet → `inbox/processed/`.
- **New file (same day, S27b): `CHALLENGE_IMPACT_LEDGER.md`** — harmful-revision measurement over CHG-RED-001..043 (PROME 7/25 P6 task). Rubric pre-registered in its own commit before grading (task guard). Re-grade cadence: UNRESOLVABLE-YET rows at their named windows (see ledger footer). Boot-impact: none (not a boot-read file; DUE-scan picks up the CHG-010 stale-ACTIVE flag it surfaced).
- **S27b (same day): CLAUDE.md W2 amendment** — added the undated-ACTIVE rule ("every ACTIVE challenge row must carry a resolution date/event or named re-review date"; CHG-RED-010 root cause, ML-RED-125). New file `CHALLENGE_IMPACT_LEDGER.md` (logged above). `workbook/CHALLENGES.tsv`: 27 legacy rows with non-10-field counts found (pre-existing at HEAD, quoting/schema-evolution artifacts) — queued for a dedicated audit pass, NOT mass-edited (frozen record the impact ledger graded against). Boot-impact: W2 text only.

## 2026-07-31 — S27 Phase 3 (workbook data-integrity repair)
- **Diagnosis correction first:** the earlier S27b note above ("27 legacy rows with non-10-field counts, quoting/schema artifacts") was WRONG in both count and cause — the file's true canon is **11 columns** (`BOARD_Refs` added 2026-05-06, correctly documented in `SCHEMA.tsv` all along; RED's CLAUDE.md workbook table carried the stale 10-col line and my audit inherited it). Real defect set: **30 short rows** (missing trailing empty cells — incl. the two rows I appended earlier today), **1 stray blank line**, **1 content-placement defect** (CHG-028's Resolved_Date cell held a narrative blob), **1 misfiled ref** (CHG-016 VX-RED-015 in KB_Links).
- **Repair executed (content-preserving, verified programmatically):** all rows padded to 11 fields (empty cells only); blank line removed; CHG-028 blob relocated VERBATIM into Resolution with a relocation marker + window date `2026-11-10 (two-print 10/14+11/10)` installed; CHG-016 ref moved to VX_Links; W2 dates installed on CHG-042 (`2026-08-24 re-review`), 043 (`2026-08-15 re-review`), 044 (`2026-11-30 final window`). Post-repair: 44/44 rows at NF=11; every non-empty original cell verified present.
- **RED-21 Timeframe** made machine-parseable (`2026-08-12`, prose → Notes) — boot.py DUE-scan now 🟢 clean, the standing ⚠️ retired.
- **CLAUDE.md** workbook table corrected to 11-col (SCHEMA.tsv named canonical). **Files touched:** workbook/CHALLENGES.tsv, workbook/PREDICTIONS.tsv, CLAUDE.md, SCRATCH.md. **Boot-impact:** DUE-scan noise eliminated; no schema change (the schema was always 11 — the docs and my audit were behind it).

## 2026-07-31 — S27 Phase 4 (CALENDAR narrative layer + WATCHLINES labels)
- **Trigger:** closeout-sweep items 9-11 + 15-remainder. **What changed:** (1) CALENDAR "Top imminent" paragraph rewritten to 7/31 vintage (S22-vintage narrative retired to the resolved tables); (2) PREDICTION SCORING WINDOWS reconciled to canonical PREDICTIONS.tsv — RED-17/10 were carried stale-ACTIVE though CORRECT, RED-18 stale-ACTIVE 26 days though WRONG; section now = ACTIVE windows (RED-21 8/12, RED-04 9/30) + resolved history; (3) FALSIFICATION WATCH section **FROZEN whole** (root Data-Hygiene option (a)) — canonical homes are the registry/WATCHLINES TSVs boot.py evaluates; the section had presented S17/S20 anchors as "active triggers"; (4) EXIT-WINDOW BACKSTOPS **FROZEN — all realized/expired**; (5) WATCHLINES role labels re-pointed on WL-02/07/08/09/10 (Jun-stack/blackout vintage tokens retired; **thresholds untouched**).
- **⚠️ Self-introduced bug caught by the mirror check:** the morning docket re-date set the BDC rows' status to `redated-2026-08-04`, which boot.py's `status=pending` filter DROPS — the CHG-027 capitulation-review gate had silently vanished from the catalyst countdown for ~5 hours. Fresh 🔴 pending row (2026-08-04) added; countdown verified restored. Class: a status-token change on a LIVE row must preserve scanner visibility — resolve-and-REPLACE, never re-label in place (state-token lesson, cf. finding_state_token_sweep_all_surfaces).
- **Files touched:** CALENDAR.md, docket/CATALYSTS.tsv (+1 row), docket/WATCHLINES.tsv. **Boot-impact:** countdown restored; watchline evaluation unchanged (labels only).

## 2026-07-31 — S27 Phase 5 (LAST_COMPLETION reconciliation + the class fix; sweep CLOSED 20/20)
- **LAST_COMPLETION.md reconciled, kept:** investigation (PROME/COMPLETION_SPEC.md + file git history) showed the S26 spawned session wrote it CORRECTLY — the fleet spawn contract REQUIRES every spawned sub-agent to overwrite `AGENTS/<name>/LAST_COMPLETION.md`; RED's S17 local retirement was never reconciled with that spec. CLAUDE.md reference table now documents the dual role: spawn-contract surface only, per-spawn report to PROME, expected stale between spawns, never boot-read; SCRATCH stays sole canonical handoff. No deletion (would put the next spawn in breach), no PROME packet needed (no conflict remains).
- **Class fix for the sweep's signature:** Discipline-overlay line added to CLAUDE.md WRITE-BACK — a dated section stamp older than the previous session forces re-read-or-restamp-or-freeze; a date is a TRIGGER, not a shield. Promoted to auto-memory `finding_dated_stamp_is_a_trigger_not_a_shield` (generalizes: the SKEW clock masked 8d behind a dated anchor, the pre-FOMC priorities surviving two sessions, two predictions ACTIVE 26d post-resolution). Mechanization (a date-token grep script) deliberately DEFERRED — the manual rule gets one chance first; build the script only if it fails once.
- **Sweep ledger: all 20 flagged items CLOSED** — P1: 16/17/18/20 · P2: 1-8 · P3: 12/13/14/15-rows · P4: 9/10/11/15-labels · P5: 19 + class fix. Two self-caught bonuses along the way: the SKEW 2-of-4 clock (P2) and the boot.py pending-filter bug from my own morning re-date (P4).

## 2026-09-02 — S39 (Kernel Sitting 2 verifier seat + WALTER scan view + read-cap rotations)

- **Trigger:** (1) Kernel Gate C Sitting 2 — RED authored/committed its first immutable command; (2) WALTER 8/31 proposal for a generated scan view of the trigger registry (Will-ruled 9/1: RED owns the restructure); (3) DAEDALUS P1 read-cap packets + PROME referent correction (MEMORY.md 92% is RED's own file).
- **What changed:** `outbox/kernel/` created — `MIDAS-06_VERIFY_NATIVE_COMPANION.json` (typed companion) + `submissions/CMD-01a06273-bff9-7eb3-8390-fef3df579d9c.json` (**IMMUTABLE — never edit, move or delete; carve-out ④**). `registry/FALSIFICATION_TRIGGERS.tsv` gained col 18 `instrument_basis_operative` (17→18 cols; appended, positional consumers of 0–16 unaffected). NEW `scripts/gen_trigger_scan.py` → NEW generated `registry/FALSIFICATION_TRIGGERS_SCAN.tsv` (13 cols, `#` banner line 0 with canon sha256). `workbook/SCHEMA.tsv` +14 rows; `scripts/schema_check.py` registers the view (skip 1). `MEMORY.md` 50,168→20,045 B and `CALENDAR.md` 40,267→28,062 B by two-state rotation → `archive/MEMORY_rotation_2026-09-02.md` (crc32 3870475095) and `archive/CALENDAR_resolved_rotation_2026-09-02.md` (crc32 2382785441), verbatim, pointer lines left in place. `CLAUDE.md` 9b: regenerate view after any registry edit, `--check` at closeout.
- **Files touched:** the above + `board_log.tsv`, `workbook/KB.tsv` (047/054/057), `workbook/ML.tsv` (206/207), `reports/2026-09-02_KERNEL_GATE_C_SITTING2_MIDAS06_VERIFICATION.md`, `AGENTS/WALTER/inbox/2026-09-02_from-RED_scan-view-BUILT-…md` (carve-out ①).
- **Boot-impact:** MEMORY.md boot read is now 37% of cap (was 92%). `read_cap_check --agent RED` = 0 over budget. Closeout gains one command (`gen_trigger_scan.py --check`). Nothing under `outbox/kernel/submissions/` is ever a boot read or an editable surface.

## 2026-09-06 (S41) — structural changes

| Trigger | What changed | Files | Boot-impact |
|---|---|---|---|
| FT-10 basis declared 9/2 but wiring left on the mirror (ML-218) | `boot.py` METRIC_MAP `SKEW-CBOE` re-pointed `yf ^SKEW` → new `cboe` source type; added `cboe_skew()` + `cboe_run_length()`; `eval_line` gained a `cboe` branch that COMPUTES the sustain run and prints the bar date; fails LOUD and never substitutes the mirror | `scripts/boot.py` | §② now prints `COUNTING n-of-4` with the CBOE bar date instead of a flat `FIRING` |
| VIOLET caveat via PROME (ML-224) | `^SKEW` removed from the yfinance `TICKERS` list; §① TAPE now prints the CBOE bar with its date from the same cached pull the grade uses | `scripts/boot.py` | tape and grade agree by construction |
| WALTER `SIG-W-20260906-003` (ML-226) | `VIX` METRIC_MAP re-pointed `yf ^VIX` → `fred VIXCLS`, the basis the card has named since 8/12; `VIXCLS` added to `FRED_SERIES` tape | `scripts/boot.py` | FT-06 sustain now COMPUTED (trail shows 9/1's 16.34 breaking the run) |
| Trail formatter rendered VIXCLS 16.34 as `16` beside a `<16` line | trail values now print at the threshold's own precision | `scripts/boot.py` | a run-breaking value no longer displays as one sitting on the line |
| FT-11 partition reconciled | PRECISION clause added (integer bp, `round(Δ×100)` before comparison); partition `4/68/8`→`5/71/4` | `registry/FALSIFICATION_TRIGGERS.tsv` + SCAN regenerated | none |
| FT-10 Labor Day ruling + mirror census | non-session clause with its test; basis argument re-cut from rate to MODE | `registry/FALSIFICATION_TRIGGERS.tsv` + SCAN | none |
| DAEDALUS D-10 | VX 9/12 re-review added as a dated row | `docket/CATALYSTS.tsv` | DUE-scan can now see it |
| Read-cap (STATUS twice over budget) | two-state folds, verbatim + crc-stamped: S40/S39 header narrative; 8/12 bull steelman (**re-steelmanned fresh**); NEXUS_BRIEF S29 fold | `reports/` ×3, `STATUS.md`, `NEXUS_BRIEF.md` | STATUS 33,380 → **32.1KB**; brief 33,186 → 30,894 B |
| RED-22 width 9≠10 (DAEDALUS) | 744 B `Invalidation` recovered verbatim from `a0e7db189`; whole file audited 23/23 | `workbook/PREDICTIONS.tsv` | none |
| RED-23 Timeframe held prose | corrected to `2026-11-XX` in the session it was written | `workbook/PREDICTIONS.tsv` | DUE-scan parses it |

**⚠️ SPECIFIED, DELIBERATELY NOT BUILT — both would have been unreviewed code at closeout:**
1. **`boot.py` §⑤ BOARD disposition check is broken (ML-223).** It compares the newest signal against the newest log-row DATE, so **any** new row silences it — it went 🔴 20-undispositioned → 🟢 after three unrelated rows were logged, with 18 still unconsumed. Fix = set-difference the RED-addressed signal IDs against the `signal_id` column and report the MISSING SET.
2. **Nothing compares `boot.py`'s METRIC_MAP source against each row's `instrument_basis` (ML-226).** Two of twelve rows were graded off sources their own cards disqualified; both mismatches were *disclosed on the rows* and survived every check RED runs. `schema_check` validates structure, `read_cap` bytes, `review_debt` row age — **none asks "does the tool read what the card says?"**
