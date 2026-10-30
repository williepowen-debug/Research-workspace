# WAL profile refresh — Reader 1 of 3 (ARCHITECTURE cluster)

**Started:** 2026-10-30 12:27 EDT (`date`) · **Reader:** DAEDALUS helper (Mode-A fan-out, R1), read-only on all tracked files; only write is this file.
**Paths are relative to `AGENTS/WAL/` unless prefixed.** Byte figures from `wc -c` on 2026-10-30; budget 32,550 B, rotation trigger 24,412 B (75%).

(Sections written incrementally; coverage ledger in §I.)

**Repo HEAD at read:** `c1b78020f`. **WAL live?** No evidence of a live session: last WAL-authored commit `4a7d83e28` 2026-10-28 23:34 ET ("WAL MEMORY: owner questions sent to REGINALD and TERRY"); every later commit under `AGENTS/WAL/` is a peer delivery (WALTER `78e3eefe5`, REGINALD `9011ebff5`, TERRY `edf055f1a`, 10/29). 262 commits touch `AGENTS/WAL/` since 2026-08-07 (182 with a `WAL` subject prefix).

---

## A. What WAL is and does now

| Field | Value | Evidence |
|---|---|---|
| One line (WAL's words) | "You own one bank, deeply. Every office-classified migration, every FRAUD/ litigation development, every MI3 data point, every pre-registered grading frame on a WAL print — these are yours." | `CLAUDE.md:11` |
| Class / lineage | Market, single-name bank specialist (Western Alliance Bancorporation, NYSE: WAL). Promoted out of `AGENTS/REGINALD/WAL/` 2026-07-25; review at `AGENTS/DAEDALUS/builds/wal_promotion/PROMOTION_REVIEW.md` (exists) | `CLAUDE.md:3-5` |
| Edges | Sends to REGINALD (cohort), TERRY (WAL-GRIND adjudication; NOT-FIRED trade-idea packets), OTTO/BROCK (Jefferies / First Brands), OZK; receives from REGINALD, OTTO, BROCK, WALTER, TERRY | `CLAUDE.md:4,142-158` |
| Owns / does not own | Owns thesis + calibration record, print grading, Q3 10-Q read + $99M appraisal watch, MI3 trajectory, FRAUD litigation arc, WAL option book, KB + predictions. REGINALD keeps cohort/KRE/FHLB/BANK_EXPOSURE_MATRIX, funding, peers, severity and the price guards | `CLAUDE.md:136-138`; `STATUS.md:114` |
| Current judgment (10/28) | Thesis **v2.4** (dated 2026-08-20), weights Bear-fast 2 / Bear-medium 16 / Base 45 / Bull 30 / Tail 7, **EV $75.96, PT $52–76**, composite **13/25**; "nothing graded since 10/22". Q3 print + call graded on frozen frames (WAL-02 INVALIDATED at 30bps; WAL-01 INVALIDATED-PROVISIONAL at $272.75M; migrations DP2 DISCONFIRM final; coverage 118%). What is left of the bear: the **$99M life-science appraisal** (PENDING-10-Q, never benign) and the OREO (+$39M) / special-mention (+$81M) build. The Q3 10-Q (statutory Mon 11/9) is "the one carrier that decides it", and the weight move per outcome is **pre-registered and Will-approved** in `Q3_10Q_RESCORE_RULE_2026-10-22.md` (cure 16→8; unmentioned 16→12; partial write-down holds 16; majority loss 16→20) | `STATUS.md:3,9,32-34,40-52`; `CLAUDE.md:13` |
| Margin of safety | "~nil — spot oscillates around EV": 10/28 close $75.96 = EV exactly (0.00%) | `STATUS.md:30`; `WEAKNESSES.md:14` |
| Live book | **Yes, a book exists, pointer-held.** `POSITIONS.md` (vintage 2026-10-19 accepted broker mirror) lists 3 WAL put legs in 2 accounts: Fidelity Dec-18 $70P ×2 (new, owner/card UNKNOWN), Fidelity Dec-18 $65P ×4 (TERRY management card), Robinhood Dec-18 $70P ×1 (carries `GATE-TERRY-ROLL70-EXIT` ≥$81.90 ×3, time stop 12/4). WAL "never sizes, structures or recommends execution"; TERRY constructs, Will orders; this desk books dispositions from Will's captures and sends no expiry reminders | `POSITIONS.md:9-17`; `CLAUDE.md:156,177`; `STATUS.md:73,99` |
| Runtime as operated | Last session: "Claude Opus 5.5 on the laptop `WilliePOwen`, interactive" (10/28). A Codex shim `AGENTS.md` points back to the charter | `MEMORY.md:5`; `AGENTS.md:1-7` |

## B. File anatomy

Bytes from `wc -c` 2026-10-30. Boot-read classification = WAL's own declaration in `PROME/registry/READS.tsv` (29 manifest rows; `read_cap_check --agent WAL` rc 0, `rotation_due=2`). % = share of the 32,550 B budget.

| File / dir | Role (WAL's words where quoted) | Bytes (% budget) | Boot read? | Richness / note |
|---|---|---|---|---|
| `CLAUDE.md` | charter: identity, runtime/delivery, boot 0–8, closeout checklist, DOC OWNERSHIP, scope, signal table, FILES | 28,784 (**88%**) | whole (declared, READS row `WAL:RUNTIME-AND-DELIVERY`) | **rotate tier**: `read_cap_check` says remove 6,000 B to reach the 70% stop. Highest-value single file for orientation; carries the `#1 RULE` and every check's rationale |
| `AGENTS.md` | Codex shim; "adds no authority and does not duplicate the charter" | 1,045 (3%) | whole | — |
| `STATUS.md` | dashboard: BOTTOM LINE, LATEST, JUDGMENT, Q3 frozen-frame grades, five things, operator dependencies, convergence matrix, EXIT RULES (stamped), next carriers | 19,714 (61%), 114 lines | whole (boot 1) | under the ≤250-line rule (`CLAUDE.md:106`); also read whole by NEXUS and REGINALD |
| `MEMORY.md` | one current handoff: open question, LAST SESSION, NEXT SESSION 1–7, carried proposals | 7,567 (23%) | whole (boot 3) | older notes rotated verbatim with sha256 to `archive/MEMORY_before-*` |
| `INDEX.md` | "Cold-spawn entry point — mirrors canonical tokens" | 6,080 | summary (boot 4c reads it mechanically) | owner map of 26 files; glued-word tokens (see H) |
| `NEXUS_BRIEF.md` | synthesis brief for NEXUS, pinned to STATUS commit `4e713d7c1` | 6,165 (19%) | not WAL boot; read whole by NEXUS | current as of 10/28 23:28 |
| `THESIS.md` + `CHANGELOG.md` | thesis v2.4 + every superseded version inline; version-pinned history | 61,921 (481 ln) + 69,779 (655 ln) | scoped (header + calibration tables; CHANGELOG top entry) | THESIS header line 3 is the machine-read owner of version/EV/PT for `boot.py` and `derived_drift_check.py` |
| `WEAKNESSES.md` | "living counter-argument"; must re-fold at every thesis bump | 10,933 | not boot | Last Updated 10/22 (see H) |
| `SCENARIOS.md` | v2.4 EV table copied byte-for-byte; history at `archive/SCENARIOS_before-housekeeping_2026-10-14.md` | 11,101 | on demand | carries the anti-ratchet check and the strained PT-floor convention |
| `LEADERSHIP.md` | V4 record, refreshed 10/28 from 2026 proxy + 71 Form 4s | 9,256 | not boot | dated, sourced, open questions listed |
| `POSITIONS.md` | "canonical for WAL strikes/expiries/quantities"; desk's only trade surface | 8,970 | summary (4c regex checks) | vintage 10/19 accepted broker mirror |
| Frames | `Q2_GRADING_FRAME_2026-07-21.md` 17,899 · `PREPRINT_RECON_2026-07-17.md` 10,011 · `EARNINGS_PREP.md` 33,875 (+ rider 5,621) 🧊; `Q3_PRINT_GRADING_FRAME_2026-09-24.md` 28,635 (graded); `Q3_10Q_GRADING_FRAME_2026-09-24.md` 27,183 (frozen 10/22, awaiting filing); `Q3_10Q_RESCORE_RULE_2026-10-22.md` 6,656 | — | task-scoped | the desk's signature discipline |
| Reads / records | `Q2_10Q_READ_2026-08-07.md` 33,943 · `MI3_FIRST_RUN_2026-08-07.md` 16,628 · `Q1_2026_ANALYSIS.md` 16,608 | — | no | held from retirement because THESIS travels them |
| `REGINALD_CHANNEL.md` | pair log (204 lines; top entry 2026-10-19 FROM WAL) | 29,071 | scoped (boot 7 top-scan) | under the ~300-line archive rule |
| `STATUS_ARCHIVE.md` 72,450 · `MEMORY_ARCHIVE.md` 66,484 | verbatim crc-stamped rotations | — | no | — |
| `board_log.tsv` | WALTER consumption receipts (boot 7b) | 7,531 | summary | — |
| `registry/corrections_receipts.tsv` | R1 corrections receipts (boot 7a) | 166 | no | header-only so far |
| `workbook/` | `KB.tsv` 293,696 (270 rows / 20 groups; 184 ACTIVE) · `KB_INDEX.md` 2,375 (now **generated** navigation) · `PREDICTIONS.tsv` 23,504 (3 rows: WAL-01, WAL-02, REG-15) · `RETIRED_CLAIMS.tsv` 14,027 · `MI3_SERIES.tsv` 2,892 (12 quarters, two-clock + "Last attention check" line) · `DRIFT_HISTORY_2026-10-14.json` 56,026 (reviewed identity baseline) | — | summary (via scripts) | the record |
| `scripts/` | 11 files, 126,975 B on disk incl. `__pycache__` (see C) | — | executed, not read | 5 boot guards + 2 test files + 4 dated one-shot research scripts |
| `FRAUD/` (7 files, 134,044 B) | live homes `FIRST_BRANDS.md` 16,325 and `STUPIN_CRE.md` 15,183 (§FOLDs, 10/22); `AUDITOR_NEXUS.md` 13,535 (corrected inline 10/28); `STATUS.md`, `SYNTHESIS_V2.md`, `AUDIT_COMMITTEE.md` 📼 records with 9/24 riders; one 58,645 B `.docx` (Point Bonita, held: live references) | — | no | dated banners on every record |
| `MARKET/` (1 file) | `TRADE_LOG.md` 831 B, 🧊 FROZEN 2026-07-25 with phantom-strike banner | — | no | — |
| `reports/` (1 file) | `2026-10-22_READS.proposed.tsv` 4,877 — the READS proposal, since adopted into `PROME/registry/READS.tsv` | — | no | residue candidate |
| `research/` (61 files, 1.79 MB) | dated threads 9/27–10/28 + Q3 grades (`2026-10-19_Q3_STAGE1_GRADE.md`, `2026-10-21_Q3_STAGE2_CALL_GRADE.md`, `2026-10-19_Q3_FULL_READ.md`) + ~25 JSON receipts; `audit_2026-09-28/` (4 files); largest `2026-10-14_FFIEC-selected-fields.tsv` 1,020,335 B | — | no | Q3 grading lives here, not at desk root |
| `sources/` (124 files on disk, 35.7 MB; 114 tracked) | primary extracts; `q1_2026` 16.6 MB, `q2_2026` 6.7 MB, `2026-10-19_Q3` 6.2 MB; `ffiec_2026-10-14` (8 SDF quarters + receipts); `ffiec_2026-10-28` 308 B; `edgar_sweep_2026-10-28` 1.68 MB; `10k_fy2024/`, `10k_fy2025/` empty on this box (gitignored binaries) | — | no | `SOURCE_INVENTORY_2026-10-14.tsv` + `SOURCE_RECOVERY.md` record tracked vs local-only |
| `archive/` (47 files, 919 KB) | verbatim pre-edit copies (STATUS/MEMORY/INDEX/NEXUS/POSITIONS/SCENARIOS/LEADERSHIP `_before-*`), four RETIREMENT_SWEEP records (8/23, 9/24, 9/28, 10/28), `archive/FRAUD/` (7), `archive/MARKET/` (3/25 charts), `archive/sources/` (4) | — | no | each rotation names a sha256 or crc |
| `outbox/` | 1 loose packet (`2026-08-23_to-PROME_wave-3-delivery…md`, held as "delivery unverified") + `delivered/` 27 | — | no | PROME's 10/28 inbox packet "8-23-wave3-packet-consumed" answers the held item (unprocessed) |
| `inbox/` | **3 loose packets** (PROME 10/28, REGINALD 10/29, TERRY 10/29) + `processed/` 58; `inbox/WALTER/` **1 unrowed** (`SIG-W-20261029-020`) + `processed/` 14 | — | lane listing (boot 4c/6/7b) | all four arrived after the 10/28 close |
| Absent by design | `LESSONS.md` (findings live in MEMORY / charter rationale), `CALENDAR.md` (carriers live in STATUS §NEXT CARRIERS), `TRADE.md` ("no TRADE.md", `CLAUDE.md:177`), `SCRATCH.md` (MEMORY is the handoff) | — | — | — |

**Where the richness lives (top 5 for a section-task):** (1) `CLAUDE.md` boot 4b–4d + closeout checklist — every check with its born-from incident; (2) `STATUS.md` §Q3 FROZEN-FRAME GRADES + §EXIT RULES + §NEXT CARRIERS; (3) the frame set + `Q3_10Q_RESCORE_RULE_2026-10-22.md`; (4) `research/2026-10-19_Q3_STAGE1_GRADE.md` / `2026-10-21_Q3_STAGE2_CALL_GRADE.md`; (5) `workbook/KB.tsv` + `PREDICTIONS.tsv` Notes lineage.

## C. Boot and closeout: as written vs what the scripts deliver

All runs on 2026-10-30 12:28–12:29 EDT, host `DESKTOP-BC6EF81`, `PYTHONDONTWRITEBYTECODE=1`. Nothing written to the repo.

### C1. Boot steps (`CLAUDE.md:38-70`)

| Step | As written | Mechanism | Observed today |
|---|---|---|---|
| 0 | repo root, git state, explicit reads incl. root `USER.md` every boot | manual | — |
| 1–3 | STATUS whole; THESIS header + calibration + CHANGELOG top; MEMORY whole | manual reads | sizes in B |
| 4 | `ledger_staleness.py WAL --quiet` (+ `--trade`) | fleet tool | not run (fleet tool; R2 cluster) |
| 4b | `kb_expiry_check.py --quiet` | WAL script | **ALERT**: "8/184 ACTIVE rows past their own Stale_By (oldest 2d)" — KB-092/093/095/102/194/196/251 (Stale_By 10/28) + KB-227 (10/29). rc 0 (advisory by design) |
| 4c | `derived_drift_check.py --quiet` → also runs `maintenance_state_check.current_fields` (KB/INDEX/KB_INDEX counts, position mirrors, inbox lanes) | WAL scripts | **ALERT**: "CHECK: 2 named-field issues / 0 new claim identities; totals 14/63" — `inbox-WALTER 1 unrowed: SIG-W-20261029-020`; `inbox-unprocessed 3 packet(s)` (PROME 10/28, REGINALD 10/29, TERRY 10/29). rc 0 always |
| 4d | `predictions_due_check.py --quiet` | WAL script | **silent, rc 0** (clean: WAL-01 OPEN due 11/15, 16 d; WAL-02 and REG-15 closed) |
| 5 | `boot.py` (price vs EV and exit level; SEC; FFIEC filer list + JWT; FINRA). "rc 2 = UNCHECKED, never clean." Fallback `scripts/market.py` (root `scripts/market.py` exists) | WAL script | see C2 |
| 6 | inbox awareness from 4c's `inbox-*` lines | via 4c | 3 + 1 listed |
| 7 | REGINALD_CHANNEL top scan | manual | top entry is WAL's own 10/19; no REGINALD entry since |
| 7a | `corrections_boot_check.py WAL` | fleet tool | not run (R2 cluster) |
| 7b | WALTER intake: row each unrowed `inbox/WALTER/*.md` in `board_log.tsv`, `git mv` to processed | manual, listing from 4c | 1 owed |
| 8 | execute; grade off frozen frame; pre-register next frame against the filing that carries the metric | manual | — |

### C2. Guards run, both directions

| Guard | Alert direction (capable case) | Clean direction | Verdict |
|---|---|---|---|
| `test_boot.py` + `test_maintenance_state_check.py` (`python3 -m unittest`, from `scripts/`) | — | **Ran 19 tests, OK** (9 boot + 10 maintenance) | matches charter claims (`CLAUDE.md:194` "10/10"; `STATUS.md:27` "9 offline tests"). The maintenance fixture copies only 5 files, so `test_repaired_current_state` never sees the live inbox lanes; the lane cases are covered by their own synthetic tests |
| `kb_expiry_check.py` | live tree: quiet line printed (above); full mode lists 8 rows | scratchpad copy of KB with every ACTIVE `Stale_By` set to 2099: full mode prints "past their own expiry: 0 ✓"; **`--quiet` prints nothing at all** | works both ways; **quiet (the boot form) has no clean line**, and quiet mode also never prints the `blank` or `bad` (unparseable/short) counts |
| `predictions_due_check.py` | `--asof 2026-11-20 --quiet` → "1 OVERDUE (worst WAL-01 by 5d) — LOOK, do not force a grade", rc 0; `--strict` rc 1 | today, full mode: "✓ every open prediction carries a Resolve_By and none is past it"; **`--quiet` prints nothing** | works both ways; `RESOLVED-INVALIDATED` now in the CLOSED set (`predictions_due_check.py:41`, the 10/22 FLEET_MAP gap is fixed). Same silent-clean quiet form |
| `derived_drift_check.py` / `maintenance_state_check.py` | live: 2 named-field issues (inbox lanes); synthetic alert cases in the 10 unit tests (charter leg count, acquisition UNKNOWN, unannounced KB row, KB_INDEX group count, auto-load wording, WALTER lane, loose packet) | `test_repaired_current_state` returns `[]`; quiet clean path prints "Selected checks pass …" (has a clean line) | works; `maintenance_state_check.py` standalone: rc 0, `--strict` rc 1 on the same 2 issues. `DRIFT_HISTORY` `review_by` is 11/9 (MEMORY:13) so the history-review leg is not firing |
| `boot.py --offline` (whole script; zero network, zero writes) | — | — | rc **1**: one ATTENTION ("FFIEC JWT expires in 6d while the 2026-09-30 pull is still owed") + 4 UNCHECKED. Exit log pointer read: "last row 2026-10-29 (close 77.80): run 0 of 3, FIRED — REGINALD grades". Prints "STATUS.md price tokens date from 2026-10-28: re-sync…" |
| `boot.py` live network sections (`filings_section`, `ffiec_section`, `finra_section` called by import, skipping only the `fetch.py` price subprocess because `fetch.py` appends to a gitignored audit log and cache) | `since=2026-10-15`: 10 Form 4s read and classified routine (D,M / A), 10/19 8-K items 2.02, 9.01 → ATTENTION; FINRA with the KB reader stubbed to 9/30 → "FINRA settlement 2026-10-15 is newer than the KB's — log a KB row" | `since=2026-10-28`: "10-Q for 2026-09-30: NOT FILED (statutory Mon 2026-11-09, 10d)"; "No issuer filings since 2026-10-28"; Call Report "NOT FILED yet (3482 banks filed so far)"; FINRA latest 10/15 = KB's, no attention | every live source read; **UNCHECKED [] on this box**. Only remaining ATTENTION is the JWT. Note: the filer count moved 2,643 (10/28) → 3,482 (10/30) with RSSD 3138146 still absent on the Call Report due date |

**boot.py writes nothing** (confirmed from source: no file writes; FFIEC headers go to curl on stdin; `boot.py:19`). Its price step shells to `FORGE/tools/market-data/fetch.py`, which writes `.cache/` and appends `logs/market_data.log` (both gitignored) — so "read-only" holds for the repo, not the box.

**rc masking:** `Report.rc()` returns 1 whenever any ATTENTION exists, even with UNCHECKED items present (`boot.py:74-75`); the offline run above returned rc 1 with four sources unread. The SUMMARY block lists both classes, so a reader of the text is safe; a consumer of the exit code alone cannot tell "attention, all read" from "attention, four sources dark".

### C3. The four dated one-shot scripts (read whole, not run: each writes files)

| Script | Writes | State today |
|---|---|---|
| `ffiec_wal_retrieve_20261014.py` | `sources/ffiec_2026-10-14/WAL_<period>.sdf` + a `retrieval_*.json` receipt | **the live Q3 pull path** (`STATUS.md:106`, `MEMORY.md:22`). `OUT` is hard-coded to the 10/14 folder; MEMORY carries a `python3 -I -c` monkeypatch recipe to redirect it. Exit code is 0 on `HTTP_ERROR` and `INVALID_OR_UNAVAILABLE` (only network failure returns 3), so an HTTP 500 pull exits clean; the per-period status line and JSON receipt carry the truth. `OUT.mkdir(exist_ok=True)` has no `parents=True` |
| `ffiec_wal_analyze_20261014.py` | 3 files in `research/` | asserts `len(metrics) == 8` and last quarter 2026-06-30 — reproduces the 10/14 extraction only; not a forward tool |
| `earnings_bridge_20261014.py` | 2 files in `sources/followup_2026-10-13/` | its hash guard over 5 frozen/canonical files would now fail on 2 (`Q3_10Q_GRADING_FRAME` and `PREDICTIONS.tsv` changed legitimately 10/19–10/22; checked by hashing, not by running) |
| `earnings_bridge_20261019.py` | `research/2026-10-19_earnings-bridge.json` | its `protected_unchanged` guard would now fail on 3 of 6 (`Q3_10Q_GRADING_FRAME`, `THESIS.md`, `PREDICTIONS.tsv`) |

These are dated reproduction receipts; the reproduction claim is bounded to their run date. No charter row names them except the FFIEC retrieve recipe.

### C4. Closeout (`CLAUDE.md:76-89`)

Checklist: STATUS (sync both price tokens), THESIS+CHANGELOG (bump), PREDICTIONS (PAT-053 leg named), KB two-clock, POSITIONS (broker data only), INDEX mirror-sync, REGINALD_CHANNEL ACK, **NEXUS_BRIEF mandatory fold as the LAST WRITE, committed after the final STATUS commit**, MEMORY rewrite, root 1b–1e by reference, git pathspec commits + `safe-push.sh`, and "before asserting any inbox is empty, re-run 4c". No WAL-local closeout script; mechanics are root's. Observed 10/28: brief committed `a2fce0c55` 23:28 (pinned to STATUS `4e713d7c1`), then a MEMORY commit `4a7d83e28` 23:34 — the commit-after-STATUS rule held; the brief's own sentence "This brief is the session's last write" (`NEXUS_BRIEF.md:45`) did not.

## D. Per-dimension local form

| Dimension | Where it lives | Form | Rich? |
|---|---|---|---|
| STATUS / current judgment | `STATUS.md:7-9` BOTTOM LINE (2026-10-28) + `:32-34` JUDGMENT + `:11-28` LATEST table; mirrored (pointer-style) in `INDEX.md:5`, `NEXUS_BRIEF.md:3-22`, `MEMORY.md:3` | dated dashboard, source column on every LATEST row, price line with source/clock/basis (`:30`) | yes; the 10/22 FLEET_MAP gap "STATUS has no BOTTOM LINE" is closed |
| Thesis / scoring | `THESIS.md` header (`:3` version/EV/PT, machine-read) + calibration tables; weights canonical there. Convergence matrix `STATUS.md:75-86`: V1a 1 · V1b-broadening 2 · V1b-magnitude 4 · V2 5/5 historical EXCLUDED · V3 3 · V4 3 = 13/25 | scored vectors, each with "current evidence / next carrier" | yes |
| Exit / kill rules | `STATUS.md:88-99`, stamped "*Kill rail re-derived: 2026-10-22 … Re-checked 10/28*" (`:90`); 6 rules: Bear-medium KILL (NOT FIRED, leg b PENDING-10-Q) · Bear-fast KILL (FIRED 8/7) · Bear CONFIRM (NOT FIRED) · Thesis RETIRE (counter 2 of 3; coverage leg met) · GATE-REG-T02 (TERMINAL since 9/1) · Robinhood exit guard (REGINALD grades). Meaning column mirrored in `WEAKNESSES.md:34-42` | dated, each rule names its carrier filing | yes; the 10/22 "EXIT RULES lack a dated re-derivation stamp" gap is closed |
| Pre-registered outcome mapping | `Q3_10Q_RESCORE_RULE_2026-10-22.md` (Will-approved 12:37 ET); "amendable only by dated note before the 10-Q hits EDGAR" (`CLAUDE.md:125`) | frozen outcome→weight table | yes — new since 8/07; closes the 10/22 "no pre-registered 10-Q mapping" gap |
| Predictions | `workbook/PREDICTIONS.tsv` (23,504 B; 3 rows). WAL-01 OPEN, Outcome provisional INVALIDATED, Resolve_By 2026-11-15; WAL-02 RESOLVED-INVALIDATED 10/19 (10-Q confirm pending); REG-15 closed (transferred from REGINALD 8/12, scored 8/20). Read by `predictions_due_check.py` (boot 4d). **No forward prediction registered since WAL-01/02 (2026-04-24)**; MEMORY NEXT 2 plans "register forward Q4 predictions with dated Resolve_By" after the re-score | 10-col REGINALD schema + `Resolve_By`; dual-provenance Notes | thin (one OPEN row) |
| Logging / evidence | `workbook/KB.tsv` (270 rows, two-clock header lines 1–2; `Stale_By` per row read by 4b); `RETIRED_CLAIMS.tsv` (read by 4c CHECK 2); `CHANGELOG.md`; `board_log.tsv` (WALTER receipts); `registry/corrections_receipts.tsv`; `archive/RETIREMENT_SWEEP_*.md` | append ledgers with mechanical readers | yes |
| Convergence with peers | pointer-only seam with REGINALD ("pointer + last-verified date, NO restated figures", `CLAUDE.md:107`); pair log `REGINALD_CHANNEL.md`; packets direct to recipient inboxes (carve-out ①). 10/28 owner questions to REGINALD (debt/preferred, uninsured mix) and TERRY (IV/skew) — both answered 10/29 into `inbox/`, unprocessed | packets + channel | partial (answers sitting unread) |
| Trade surface | `POSITIONS.md` only ("no TRADE.md", `CLAUDE.md:177`); structural fields from accepted broker mirror; no marks/P&L; TERRY constructs, Will orders | per-leg table + history | yes, with stated vintage (10/19) |
| Primary-data falsifier series | `workbook/MI3_SERIES.tsv` (12 quarters to 2026-06-30; data clock 2026-08-07; attention line 10/28) | two-clock LIVE ledger, frozen grade bands in header line 4 | yes; Q3 row owed |

## E. Deviations from blueprint (and why)

| Deviation | Why (WAL's stated reason) | Verdict |
|---|---|---|
| No `LESSONS.md`; lessons live as rationale inside the charter checks and in MEMORY Findings | each check carries its born-from incident inline (`CLAUDE.md:55,60,65,85,89`) | equivalent for a single-name desk; the rationale is boot-read, which a LESSONS index would not improve |
| No `CALENDAR.md` / CATALYSTS ledger; carriers live in `STATUS.md` §NEXT CARRIERS (`:101-110`) | dashboard owns catalysts (`CLAUDE.md:115`) | equivalent while the carrier list is ~6 rows; `boot.py` now computes statutory 10-Q / Call Report dates itself |
| No `TRADE.md`; `POSITIONS.md` is the trade surface | "This desk's only trade surface — there is no TRADE.md" (`CLAUDE.md:177`) | deliberate; book exists, construction is TERRY's |
| No `SCRATCH.md`; `MEMORY.md` is the handoff | MEMORY holds one current handoff, history archived verbatim | equivalent |
| Kill rail lives in STATUS §EXIT RULES; the pre-registered outcome mapping is a separate dated file | frames are frozen and versioned per filing | better: frozen per-carrier files cannot be edited post-filing |
| Grading reports in `research/`, not `reports/` | historical | neutral; `reports/` holds only the adopted READS proposal |
| Drift detection by tree scan + reviewed identity baseline (`derived_drift_check.py`) rather than an enumerated fold list | "an enumerated fold-list is a hidden claim the list is complete" (`CLAUDE.md:60`) | better; a fleet-harvestable pattern |
| Codex shim `AGENTS.md` at desk root | runtime parity | standard since WQ-385 |
| Glued-word tokens in derived surfaces (`INDEX.md:5,38,44`; `SCENARIOS.md:3,7`; `POSITIONS.md:36`) | appear to be residue of a byte-trim pass | **debt**: root Output Canon forbids gluing words ("never glue words together to save bytes") |

## F. Do-not-touch quirks

1. **Frozen frames:** `Q2_GRADING_FRAME_2026-07-21.md`, `PREPRINT_RECON_2026-07-17.md`, `EARNINGS_PREP.md` — "Path fixes only, content NEVER" (`CLAUDE.md:123`). Superseded-looking numbers are correct history.
2. **`Q3_10Q_GRADING_FRAME_2026-09-24.md`** frozen 10/22 — graded verbatim when the 10-Q lands, never edited after (`CLAUDE.md:124`). **`Q3_10Q_RESCORE_RULE_2026-10-22.md`** — amendable only by dated note **before** the filing, then applied verbatim (`CLAUDE.md:125`). After 11/9 neither may change.
3. **`Q3_PRINT_GRADING_FRAME_2026-09-24.md`** graded 10/19–10/21: never edited.
4. **PREDICTIONS.tsv** Status/Confidence/Invalidation on WAL-01: Outcome is provisional and the row stays OPEN until the 10-Q cross-check; do not close it to quiet `predictions_due_check`. Notes lineage (dual provenance) verbatim.
5. **KB `Stale_By`:** never bulk re-date (`CLAUDE.md:55`; `kb_expiry_check.py:12-14`); `AWAITS:<carrier>@<date>` is the only sanctioned deferral and only with a scheduled-filing date.
6. **`workbook/RETIRED_CLAIMS.tsv`:** add a row in the same edit that kills a claim; do not delete rows (they are the drift check's CHECK 2 patterns).
7. **`workbook/DRIFT_HISTORY_2026-10-14.json`:** reviewed identity baseline; new identities need review, never bulk acceptance; `review_by` 11/9.
8. **THESIS superseded version blocks inline**, and the THESIS line-3 header format: two scripts regex it (`boot.py:89-93` first 6 lines; `derived_drift_check.py:59-70` first 1,200 chars, `**Version:** **v…**`, `EV $`, `PT $NN-NN`). Reformatting the header silently blinds `boot.py` (EV → UNCHECKED) and makes the drift check print "FIX ME" and exit 0.
9. **`STATUS.md` "Last Updated: YYYY-MM-DD"** on line 3 is read by `boot.py:84-86` as the default filing window start.
10. **KB row text "FINRA settlement YYYY-MM-DD"** in the Fact column is the key `boot.py` uses for the last short-interest reading (`boot.py:120-131`).
11. 📼 FRAUD records (`STATUS.md`, `SYNTHESIS_V2.md`, `AUDIT_COMMITTEE.md`): new state = new rider, never in place. 🧊 `MARKET/TRADE_LOG.md` banner. `FRAUD/WAL-JEF-PointBonita-Analysis-20260326.docx` held (live references).
12. **`INDEX.md` mirror discipline:** fix the source, re-sync; `maintenance_state_check` compares INDEX's "KB N rows / M groups" to KB.tsv.
13. **POSITIONS.md wording** "acquisition October 7 from earlier Activity" is a regression-test fixture anchor (`test_maintenance_state_check.py:22`); rewording it breaks the test, not the desk.
14. GATE-REG-T02 is TERMINAL — "never re-signal it" (`CLAUDE.md:148`).

## G. The 2026-08-07 profile (`AGENTS/DAEDALUS/profiles/WAL.md`) — what still holds

Line numbers are the profile's.

| Profile claim (line) | Now | Evidence |
|---|---|---|
| Stale banner: "STATUS11797 B, rotation_due=0"; "Stage2 call integration remains pending" (:3) | **FALSE** on both: STATUS 19,714 B; `rotation_due=2` (charter 88% + root CLAUDE 76%); Stage 2 graded 10/21 | `wc`; `read_cap_check`; `STATUS.md:38,45` |
| Grade L3 Conf-H, L4 re-examination flagged (:5) | superseded: FLEET_MAP row reads **L4 / M**, last scored 2026-10-22 | `FLEET_MAP.tsv` WAL row |
| Reference implementation of frozen pre-registered print-grading (:8) | **HOLDS**, extended: Q3 print frame graded verbatim 10/19–10/21; 10-Q frame frozen; outcome→weight mapping pre-registered before the filing | `CLAUDE.md:20,124-125` |
| REGINALD seam pointer-only (:11) | **HOLDS** | `CLAUDE.md:107`; `STATUS.md:30,99` |
| "WAL's own inbox is at ZERO" (:11) | **FALSE**: 3 loose packets + 1 unrowed WALTER signal | 4c output |
| `CLAUDE.md` 165 lines, SPAWNED-MODE card :30-38 (:16) | **FALSE**: 198 lines; the spawned-mode card is replaced by § RUNTIME AND DELIVERY (`:28-36`) | `CLAUDE.md` |
| Brief fold MANDATORY any session that writes STATUS (:16) | **HOLDS** | `CLAUDE.md:85` |
| INDEX "mirrors, never originates" (:16) | **HOLDS**, now mechanically compared for the KB count | `CLAUDE.md:120`; `maintenance_state_check.py:39-41` |
| STATUS 225/250 lines (:16) | **FALSE**: 114 lines | `wc -l` |
| THESIS v2.3 current; THESIS 398 / CHANGELOG 498 lines; SCENARIOS "EV $73.92, PT $52-74" (:17) | **FALSE**: v2.4 (8/20), EV $75.96, PT $52–76; 481 / 655 lines | `THESIS.md:3`; `SCENARIOS.md:9-20` |
| Every superseded THESIS version preserved inline (:17) | holds by header (`THESIS.md:3` lists v1.0–v2.3) — body not re-read in this cluster | — |
| 🧊 Q2 frame / PREPRINT_RECON / EARNINGS_PREP frozen; content never (:19) | **HOLDS**; two of them still hash-identical to the 10/13 receipt | hash check, C3 |
| KB 170 rows / 16 groups (:20) | **FALSE**: 270 rows / 20 groups (184 ACTIVE) | `INDEX.md:5`; `kb_expiry_check` |
| 🔴 `KB_INDEX.md` 25 rows stale, the only silent-middle surface (:20) | **RESOLVED**: now "generated group navigation", count/IDs checked per group by `maintenance_state_check` (`KB-group` test passes) | `KB_INDEX.md:1`; `maintenance_state_check.py:42-50` |
| PREDICTIONS 2 rows (:20) | **FALSE**: 3 rows (REG-15 transferred in 8/12) | `PREDICTIONS.tsv` |
| Fossils every one dated-bannered (:21) | holds for the files touched in this cluster (FRAUD records with 9/24 riders, MARKET/TRADE_LOG) — not re-measured tree-wide | — |
| Absent: scripts/, boot.py, CALENDAR, LESSONS, board_log (:22) | **PARTLY FALSE**: `scripts/` (11 files) and `boot.py` (10/28) and `board_log.tsv` exist; CALENDAR and LESSONS still absent (deliberate) | B, C |
| Exit-rule states: Bear-medium ⬜ ~mid-late Oct; Bear-fast FIRED 8/7; time-box DISSOLVED; RETIRE 1-of-3; price discipline stale token (:25) | Bear-fast and time-box **HOLD** as history; Bear-medium now NOT FIRED with leg (b) PENDING-10-Q; RETIRE counter **2 of 3**; price is one dated line (`STATUS.md:30`) | `STATUS.md:88-99` |
| WAL-01 25% OPEN, resolvability DEGRADED (:32) | **SUPERSEDED**: INVALIDATED-PROVISIONAL at $272.75M, row OPEN for the 10-Q cross-check, Resolve_By 11/15 | `STATUS.md:43`; `predictions_due_check` |
| WAL-02 50% OPEN, invalidation clause unsatisfiable (:33) | **SUPERSEDED**: RESOLVED-INVALIDATED 10/19 at 30bps | `STATUS.md:42` |
| Q2-10-Q pre-registration frame VOID (:35) | holds as history | — |
| DO-NOT-TOUCH 1–8 (:42) | all eight **HOLD**; F above adds 6 (10-Q frame, rescore rule, Q3 print frame, KB `Stale_By`, RETIRED_CLAIMS, THESIS header format) | F |
| Flag: STATUS:192 price cell / "two price tokens vs three" (:45) | **RESOLVED** (single price line) | `STATUS.md:30` |
| Flag: `DROPZONE.md` old-path ×2 (:45) | **MOOT**: no `DROPZONE.md` exists in `AGENTS/WAL/` | `ls` |
| Flag: scripts/ first increment (mandate #13) (:45) | **DONE**: 4b (8/20), 4c (8/20, extended 10/14 and 10/22), 4d (8/28), 5 `boot.py` (10/28) | `CLAUDE.md:51-66` |
| L4 re-cut gate (a) Q3 frames before the print; (c) boot.py built and wired same session (:48) | (a) **MET** (frames 9/24, print 10/19); (c) **MET** 10/28 (`STATUS.md:27`). (b) REGINALD-side consumption not assessed in this cluster | — |
| Open question DEV-9 inbox/WALTER lane (:54) | **RESOLVED**: boot 7b + `inbox-WALTER` lane in 4c | `CLAUDE.md:70`; `maintenance_state_check.py:65-68` |

**FLEET_MAP WAL row (DAEDALUS's own surface, dated 2026-10-22) is now stale on 6 of its 7 listed gaps:** "no pre-registered 10-Q mapping" (closed by `Q3_10Q_RESCORE_RULE_2026-10-22.md`), "EXIT RULES lack a dated re-derivation stamp" (closed, `STATUS.md:90`), "predictions_due_check CLOSED set lacks RESOLVED-INVALIDATED" (closed, `predictions_due_check.py:41`), "STATUS has no BOTTOM LINE" (closed, `STATUS.md:7`), "boot lane misses inbox/WALTER/" (closed), "0 READS rows" (29 manifest rows now). Still true: "no forward predictions after WAL-01".

## H. Ranked findings for the owner

No 🔴. The desk is in unusually good structural shape: every 10/22 FLEET_MAP gap but one has been closed by the owner, every boot guard ran and behaved in both directions, and the two frozen Q3 instruments plus the outcome mapping are in place before the filing.

| # | Sev | Finding | Evidence | Suggested owner act |
|---|---|---|---|---|
| 1 | 🟠 | **The Q3 Call Report / MI3 pull has a 6-day window and no wake.** Due today 10/30; at 12:28 ET RSSD 3138146 is still absent from FFIEC's 9/30 filer list (3,482 filers, up from 2,643 on 10/28). JWT expires Thu 11/5 (`boot.py` ATTENTION, live). WAL's plan is "retry from Sat 10/31 and before the JWT expires" (`MEMORY.md:22`), but the WAL rows on `PROME/DOCKET.tsv` I found are L171 (10-Q, 10/24–11/10), L180 (REGINALD's 11/7 cohort screen + JWT) and L219 (Will's 11/1 credential sitting) — none wakes WAL for the pull. Mitigant: the 11/1 renewal, if it happens, removes the deadline | `boot.py` live run; `STATUS.md:17,69,106`; DOCKET :171,:180,:219 | PROME/R3 to confirm whether a WAL wake exists 10/31–11/5; otherwise the Bear-fast re-test slips a quarter or waits on the renewal |
| 2 | 🟠 | **Four unprocessed arrivals since the 10/28 close**, including the two owner answers WAL asked for (REGINALD: WAL owns its own debt/preferred; TERRY: IV/skew is TERRY's, no standing series) — `MEMORY.md:25` says "defaults at the 10-Q grade are written in each packet", so these feed the 10-Q grade; plus PROME's packet that closes the held 8/23 outbox item; plus WALTER `SIG-W-20261029-020` (Carvana SEC investigation closed; `action: ["WAL"]`, PRIORITY, counter-evidence) unrowed in `board_log.tsv` | 4c output; `inbox/*.md` heads | process at next session (7b row + `git mv`); move the 8/23 outbox packet to `delivered/` |
| 3 | 🟠 | **Charter says the FFIEC credentials are desktop-only; they are not.** `CLAUDE.md:17` "credentials live on the DESKTOP only" and `:136` "desktop-only creds" contradict `STATUS.md:17,69` ("the credential works on the laptop", 10/28) and `PROME/MACHINE_LOCAL.md:13` (laptop PRESENT since 9/22). The last WAL session ran on the laptop. A boot-read false premise on the exact instrument the next pull needs | as cited | fix both charter lines; this is the class `derived_drift_check` cannot see (not a version/EV/PT/KB-count token) |
| 4 | 🟠 | **Charter in rotate tier: 28,784 B = 88% of budget**, rule-5 stop needs −6,000 B (`read_cap_check`). The 10/28 boot-kit wiring trimmed it (28,824 → 28,765, `MEMORY.md:14`) but it sits 4,372 B over the 75% trigger. Rationale paragraphs in 4b–4d and the closeout checklist are the natural rotation candidates (rationale already lives in each script's docstring) | `read_cap_check --agent WAL` | rotate rationale to an archive block or the script docstrings |
| 5 | 🟠 | **The live Q3 pull tool exits 0 on an HTTP error and needs a monkeypatch to target a new folder.** `ffiec_wal_retrieve_20261014.py` returns 3 only on network failure; `HTTP_ERROR` and `INVALID_OR_UNAVAILABLE` return 0 (`:92-103`); `OUT` is hard-coded to `sources/ffiec_2026-10-14` (`:16`), so `MEMORY.md:22` carries a `python3 -I -c` override recipe whose own caveat is that an `OUT` outside the repo labels a good pull INVALID (the `.sdf` is written before `relative_to(ROOT)` raises, `:89-91`) | as cited | add `--out` and a non-zero rc on any non-VERIFIED period before the pull; `boot.py` already checks the filer list first |
| 6 | 🟡 | **8 KB rows expired within two days of the 10/28 "0 expired" pass** — 7 carried `Stale_By 2026-10-28` (in date at the pass, expired next morning), 1 `2026-10-29`. KB-194/196 are the Barclays pre-guide rows that WEAKNESSES row 1 cites | `kb_expiry_check` full mode | judge at next session; a pass should also look at rows expiring within the next few days |
| 7 | 🟡 | **`WEAKNESSES.md` not folded after 10/28.** Short-interest row cites KB-229 (Sep 30) as "latest measured" (`:18`); KB-229 was superseded by KB-258 on 10/28 (`STATUS.md:28`). The 10/28 auditor-nexus weakening (KB-268), Nevada correction (KB-270) and ratings baseline (KB-265–267) are counter-argument material not reflected; header still 10/22 (`:3`). Charter requires re-fold at thesis bumps only (`CLAUDE.md:176`), so this is within the letter | as cited | add KB-229 → KB-258 to `RETIRED_CLAIMS.tsv` so 4c catches it; fold at the post-10-Q re-score |
| 8 | 🟡 | **Boot-form guards have no clean line.** `kb_expiry_check --quiet` and `predictions_due_check --quiet` print nothing when clean (verified with a clean KB fixture and today's ledger); quiet `kb_expiry_check` also drops the `blank` and `bad` (short/unparseable) counts. CHECK_STANDARD §3 asks for a watched clean line | C2 | print one clean line in quiet mode, including blank/bad counts |
| 9 | 🟡 | **`boot.py` exit code masks UNCHECKED under ATTENTION** (`:74-75`): `--offline` returned rc 1 with four sources unread. Text SUMMARY is correct; rc-only consumers are not | C2 | e.g. rc 3 for attention-plus-unchecked, or document that rc 1 does not mean all sources read |
| 10 | 🟡 | **Glued-word tokens in derived surfaces** (root Output Canon): `INDEX.md:38` "STATUScommit", `:44` "Stage2call", "recurringearnings/hedgebridge", "unresolvedNano", "laterorders", "Q3frame", "originalURL"; `:28` "integration31c02fd74"; `INDEX.md:5,24` "WAL02/WAL01", "Stage1/Stage2"; `SCENARIOS.md:3,7` "October14", "August20", "KB230"; `POSITIONS.md:36` "December4" | as cited | re-space at next INDEX sync |
| 11 | 🟡 | **No forward prediction since 2026-04-24.** One OPEN row (WAL-01) whose outcome is provisional; the plan to register Q4 predictions is sequenced after the re-score (`MEMORY.md:21`) | `PREDICTIONS.tsv` | the only 10/22 FLEET_MAP gap still open |
| 12 | 🟡 | `NEXUS_BRIEF.md:45` "This brief is the session's last write" — MEMORY was committed 6 minutes later (`4a7d83e28` after `a2fce0c55`). Within the charter rule (brief after final STATUS), outside the brief's own claim | git log | drop the sentence or keep MEMORY ahead of the brief |
| 13 | 🟡 | `reports/2026-10-22_READS.proposed.tsv` is residue of an adopted proposal (29 rows now live in `PROME/registry/READS.tsv`); `reports/` holds nothing else | `ls reports` | retire to `archive/` at the next sweep |
| 14 | 🟡 | Dated one-shot scripts' self-checks no longer pass (`earnings_bridge_20261014.py` 2 of 5 hashes; `earnings_bridge_20261019.py` 3 of 6 protected files changed legitimately); `ffiec_wal_analyze_20261014.py` asserts exactly 8 quarters. Correct as receipts, misleading if anyone re-runs them as tools | C3 | a one-line "dated receipt, not re-runnable after <date>" banner in each docstring |

**For DAEDALUS (own surface, not the owner's):** the FLEET_MAP WAL row (2026-10-22) is stale on 6 of 7 listed gaps (G, last paragraph), and the profile's own stale banner (`profiles/WAL.md:3`) is wrong on STATUS bytes, `rotation_due` and Stage 2.

## I. Coverage

**Read whole, every line** (chunks under 25 KB each; line ranges as read):

| File | Lines | Chunks |
|---|---|---|
| `AGENTS/DAEDALUS/profiles/WAL.md` (old profile) | 1–54 | 1 |
| `AGENTS/DAEDALUS/profiles/HOMER.md` (shape) | whole | 1 |
| `AGENTS/WAL/CLAUDE.md` | 1–198 | 1–80, 81–198 |
| `AGENTS/WAL/AGENTS.md` | 1–7 | 1 |
| `AGENTS/WAL/INDEX.md` | 1–46 | 1 |
| `AGENTS/WAL/STATUS.md` | 1–114 | 1–60, 61–114 |
| `AGENTS/WAL/MEMORY.md` | 1–35 | 1 |
| `AGENTS/WAL/NEXUS_BRIEF.md` | 1–45 | 1 |
| `AGENTS/WAL/WEAKNESSES.md` | 1–42 | 1 |
| `AGENTS/WAL/SCENARIOS.md` | 1–66 | 1 |
| `AGENTS/WAL/LEADERSHIP.md` | 1–88 | 1 |
| `AGENTS/WAL/POSITIONS.md` | 1–36 | 1 |
| `scripts/boot.py` | 1–437 | 1–200, 200–437 |
| `scripts/test_boot.py` · `scripts/test_maintenance_state_check.py` | 1–64 · 1–56 | 1 |
| `scripts/maintenance_state_check.py` · `scripts/predictions_due_check.py` | 1–90 · 1–118 | 1 |
| `scripts/derived_drift_check.py` · `scripts/kb_expiry_check.py` | 1–245 · 1–113 | 1 |
| `scripts/ffiec_wal_retrieve_20261014.py` · `scripts/ffiec_wal_analyze_20261014.py` | 1–107 · 1–136 | 1 |
| `scripts/earnings_bridge_20261014.py` · `scripts/earnings_bridge_20261019.py` | 1–83 · 1–169 | 1 |

Display caveat: lines were printed with `cut -c1-2000`–`3000` (scripts `cut -c1-260`–`400`). Prose lines in CLAUDE/STATUS/MEMORY/WEAKNESSES exceeding that width were truncated in display; the longest (e.g. `CLAUDE.md:13,60,85`, `STATUS.md:24-28`) were read to their natural ends as far as shown, and no finding depends on text beyond the cut.

**Anatomy only (names/sizes, no content):** `archive/` (47 files, listed with sizes), `research/` (61 files; names + 5 largest), `sources/` (per-subdir size and file count; 114 tracked), `FRAUD/` (7; first 3 lines of `STATUS.md` and `SYNTHESIS_V2.md` for banner state), `MARKET/` (1; first 4 lines), `reports/` (1), `outbox/` (1 loose + 27 delivered), `inbox/` (3 loose + WALTER 1 + processed 58/14; first ~700 B of the 4 unprocessed packets to classify them), `workbook/` (sizes; header lines of `KB.tsv`, `KB_INDEX.md`, `MI3_SERIES.tsv`; ID column of `PREDICTIONS.tsv`), `registry/`.

**Spot checks outside the cluster:** `THESIS.md` lines 1–8; `REGINALD_CHANNEL.md` header + entry headings; `FLEET_MAP.tsv` WAL row; `PROME/registry/READS.tsv` header; `PROME/DOCKET.tsv` rows 170, 171, 180, 219, 793 (+ a WAL/date grep); `PROME/MACHINE_LOCAL.md` FFIEC row; `FORGE/tools/market-data/fetch.py` write paths; `REGINALD/registry/THRESHOLDS.tsv` REG-T-02 row; sha256 of the 5 + 6 files named by the two earnings-bridge guards.

**Commands run (all read-only on the repo):** both unittest suites; `kb_expiry_check` (quiet + full + clean fixture in scratchpad); `predictions_due_check` (quiet, full, `--asof 2026-11-20` quiet and strict); `derived_drift_check --quiet`; `maintenance_state_check` (plain + `--strict`); `boot.py --offline`; boot.py's filings/FFIEC/FINRA sections live by import (clean case `since=2026-10-28`; alert case `since=2026-10-15` and a stubbed KB FINRA date); `read_cap_check.py --agent WAL`.

**Not read:** `THESIS.md` body (lines 9–481), `CHANGELOG.md`, `REGINALD_CHANNEL.md` entry bodies, the frame files, `Q2_10Q_READ`, `MI3_FIRST_RUN`, `Q1_2026_ANALYSIS`, `STATUS_ARCHIVE`, `MEMORY_ARCHIVE`, `EARNINGS_PREP*`, `PREPRINT_RECON`, `Q3_10Q_RESCORE_RULE` body, `board_log.tsv` rows, `KB.tsv` / `PREDICTIONS.tsv` / `RETIRED_CLAIMS.tsv` / `DRIFT_HISTORY` bodies, all `research/`, `sources/`, `archive/`, `FRAUD/` bodies, outbox/inbox processed packets. **Not run:** `boot.py`'s price section (its `fetch.py` subprocess appends to a gitignored log and cache), the fleet tools `ledger_staleness.py` and `corrections_boot_check.py` (R2 cluster), and the four one-shot scripts (each writes files).

*Completed: 2026-10-30 12:33 EDT.*
