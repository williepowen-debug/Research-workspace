# Agent Profile — WAL (Western Alliance Bancorp single-name bank desk)

**Profile vintage:** 2026-10-30 (whole-profile refresh; replaces the 2026-08-07 body, preserved verbatim at `profiles/_prior/WAL_2026-10-30_before_refresh.md`, crc32 3865287047).

**Built by:** DAEDALUS · **Date:** 2026-10-30 · **Comprehension method:** 3-reader Mode-A fan-out (R1 architecture · R2 ledgers/falsification/guards · R3 flows/consumers/review reconciliation), raw reports at `runs/2026-10-30_WAL_REFRESH_READERS/`, synthesis `runs/2026-10-30_WAL_REFRESH.md`. Paths below are repo-relative.
**Subject state at build:** WAL not live; last WAL-authored commit `4a7d83e28` 2026-10-28 23:34 ET (laptop, Opus 5.5, interactive). Four arrivals since are unprocessed (PROME, REGINALD and TERRY packets; WALTER signal SIG-W-20261029-020).

> A Profile is DAEDALUS's durable understanding of a heavy agent. Section-tasks read the relevant slice of this, not the raw agent; re-read the file before applying any change (PAT-009).

---

## 1. Identity

- **What it is:** a market-class single-name desk that owns Western Alliance Bancorporation (NYSE: WAL) completely: "every office-classified migration, every FRAUD/ litigation development, every MI3 data point, every pre-registered grading frame on a WAL print" (`AGENTS/WAL/CLAUDE.md:11`). Promoted out of `AGENTS/REGINALD/WAL/` 2026-07-25 (`builds/wal_promotion/PROMOTION_REVIEW.md`).
- **Signature discipline:** frozen, pre-registered print and filing grading frames, graded verbatim, plus a pre-registered outcome → weight map (`AGENTS/WAL/Q3_10Q_RESCORE_RULE_2026-10-22.md`, Will-approved 10/22 12:37 ET). The fleet's reference implementation of that pattern.
- **Current judgment (owner, 10/28):** thesis **v2.4** (8/20); weights Bear-fast 2 / Bear-medium 16 / Base 45 / Bull 30 / Tail 7; EV $75.96, PT $52–76; composite 13/25. Q3 print + call graded 10/19–10/21: WAL-02 INVALIDATED (30 bps), WAL-01 INVALIDATED-PROVISIONAL ($272.75M office classified), migrations DISCONFIRM, coverage 118%. What remains of the bear is the **$99M life-science appraisal**, PENDING the Q3 10-Q (`AGENTS/WAL/STATUS.md:7-34`).
- **Seams:** REGINALD is the obliged consumer (cohort, KRE, funding, peers, price guards stay REGINALD's; pointer-only seam, `CLAUDE.md:107,136-138`). TERRY constructs trades; WAL books dispositions in `POSITIONS.md` and never sizes. Edges also to OTTO/BROCK (First Brands / Jefferies), OZK, WALTER.

## 2. File anatomy (where the richness lives)

| File | Role | Bytes (% of 32,550 B budget) | Boot read |
|---|---|---|---|
| `AGENTS/WAL/CLAUDE.md` | charter: boot 0–8, closeout checklist, doc ownership, signal table; every check carries its born-from incident inline | 28,784 (**88%**, rotate tier; L810 hot/cold split owed) | whole |
| `AGENTS/WAL/STATUS.md` | BOTTOM LINE, LATEST (sourced rows), JUDGMENT, Q3 frozen-frame grades, convergence matrix `:75-86`, **EXIT RULES `:88-99`** (stamped 10/22, re-checked 10/28), NEXT CARRIERS `:101-110` | 19,714 (61%), 114 lines | whole |
| `AGENTS/WAL/MEMORY.md` | one current handoff (open question, last/next session) | 7,567 | whole |
| `AGENTS/WAL/THESIS.md` + `CHANGELOG.md` | v2.4 + superseded versions inline; header line 3 is machine-read | 61,921 + 69,779 | scoped |
| Frames | Q3 print frame (graded) · **Q3 10-Q frame (frozen 10/22)** · re-score rule (amendable until the 10-Q is on EDGAR) · Q2 frames and `EARNINGS_PREP.md` 🧊 | 6–34 KB each | task-scoped |
| `AGENTS/WAL/workbook/` | `KB.tsv` 293,696 B (270 rows, 184 ACTIVE, two-clock header) · `PREDICTIONS.tsv` (3 rows) · `RETIRED_CLAIMS.tsv` (40 rows, drift-check patterns) · `MI3_SERIES.tsv` (12 quarters, LIVE, Q3 row owed) · `DRIFT_HISTORY_2026-10-14.json` (identity baseline, review_by 11/9) | — | via scripts |
| `AGENTS/WAL/scripts/` | `boot.py` (built 10/28, boot step 5) · `predictions_due_check.py` · `kb_expiry_check.py` · `derived_drift_check.py` · `maintenance_state_check.py` · 2 test files (19/19 pass) · 4 dated one-shot research scripts | — | executed |
| `AGENTS/WAL/REGINALD_CHANNEL.md` | pair log, 204 lines, top entry 10/19 | 29,071 | scoped (top-scan) |
| `AGENTS/WAL/POSITIONS.md` | only trade surface (no TRADE.md); accepted broker mirror vintage 10/19 | 8,970 | summary |
| `research/` (61 files) · `sources/` (114 tracked, 35.7 MB on disk) · `FRAUD/` (7) · `archive/` (47) | Q3 grade reports live in `research/`; FRAUD records carry dated riders; archive rotations carry sha256/crc | — | no |

Absent by design: `LESSONS.md`, `CALENDAR.md`, `TRADE.md`, `SCRATCH.md` (equivalents named in §4).

## 3. Per-dimension local representation

| Dimension | Local form |
|---|---|
| Current judgment | `STATUS.md:7` BOTTOM LINE + `:32-34` JUDGMENT; mirrored pointer-style in INDEX, NEXUS_BRIEF (pinned, `brief_pin_check` rc 0) and MEMORY |
| Convergence | six scored vectors in STATUS (V1a 1 · V1b-broadening 2 · V1b-magnitude 4 · V2 historical excluded · V3 3 · V4 3 = 13/25) |
| Exit / kill rules | STATUS §EXIT RULES, six rows with a dated re-derivation stamp |
| Predictions | `workbook/PREDICTIONS.tsv`: WAL-01 OPEN (provisional INVALIDATED, Resolve_By 11/15), WAL-02 RESOLVED-INVALIDATED 10/19, REG-15 RESOLVED-FAILED 8/20. **No new prediction since 2026-04-24**; Q4 rows promised for the 10-Q session (L793 item 4, ≤11/15) |
| Logging | KB.tsv with per-row `Stale_By`; RETIRED_CLAIMS; CHANGELOG; board_log; corrections receipts (0 unreceipted) |
| Trade surface | `POSITIONS.md` (book exists; TERRY constructs, Will orders) |
| Primary-data falsifier | `MI3_SERIES.tsv` (Bear-fast; Q3 Call Report pull owed, FFIEC token expires 11/5) |

## §3b. Invalidation-surface inventory (what `falsification_scan` and the sweep read)

| Surface | Stamp | State 2026-10-30 | Mechanical reader |
|---|---|---|---|
| STATUS §EXIT RULES `:88-99` (Bear-medium KILL · Bear-fast KILL · Bear CONFIRM · Thesis RETIRE · GATE-REG-T02 · Robinhood exit guard) | `Kill rail re-derived: 2026-10-22`, re-checked 10/28 (`:90`) | Bear-medium NOT FIRED (leg b PENDING-10-Q); Bear-fast FIRED 8/7; CONFIRM NOT FIRED; RETIRE counter 2 of 3, coverage leg MET; T02 TERMINAL; Robinhood guard run 0 of 3 (REGINALD grades) | **none — hand only.** `falsification_scan.py --agent WAL` sees `CHANGELOG.md` only, so it reads CURRENT whatever the STATUS stamp does (DAEDALUS tool gap) |
| `PREDICTIONS.tsv` Invalidation column | re-spec 8/20 | WAL-01 open-provisional | `predictions_due_check.py` (both directions verified) |
| `Q3_10Q_GRADING_FRAME_2026-09-24.md` | registered 9/24, frozen 10/22 | ARMED, awaiting the 10-Q (statutory Mon 11/9) | WAL by hand, verbatim |
| `Q3_10Q_RESCORE_RULE_2026-10-22.md` | Will-approved 10/22 | ARMED; amendment window closes when the 10-Q is on EDGAR | WAL by hand |
| `MI3_SERIES.tsv` | data clock 8/07, attention 10/28 | Q3 row owed | `ledger_staleness.py` (rc 1 at every boot until the pull) |
| `RETIRED_CLAIMS.tsv` | newest row 10/28 | 40 rows | `derived_drift_check.py` CHECK 2 |

⚠️ **Open frame gap (R2 O1, verified by DAEDALUS at the artifact 10/30):** the print frame defines B′₀ / B′ᵤ (appraisal disclosed below carrying, reserve zero or undisclosed) as **adverse** evidence (`AGENTS/WAL/Q3_PRINT_GRADING_FRAME_2026-09-24.md:126-133,187-194`). The 10-Q frame's letter table (`Q3_10Q_GRADING_FRAME_2026-09-24.md:53-58`) has no such letter, so that case reads literally as **B**, and the re-score rule maps B to **Bear-medium 16 → 12** (`Q3_10Q_RESCORE_RULE_2026-10-22.md:24`), a trim on evidence the print frame calls adverse. Only Will can amend the re-score rule, and only before the 10-Q appears on EDGAR.

## 4. Deviations from standard (+ why)

| Deviation | Verdict |
|---|---|
| No LESSONS / CALENDAR / TRADE / SCRATCH; equivalents are charter rationale, STATUS §NEXT CARRIERS, `POSITIONS.md`, MEMORY | equivalent for a single-name desk |
| Kill rail in STATUS; outcome mapping in a separate dated, frozen file | better: frozen per-carrier files cannot be edited after the event |
| Drift detection by tree scan + reviewed identity baseline, not an enumerated fold list | better; fleet-harvestable |
| NEXUS brief not in schema form (NEXUS census `n/a`); content current and pinned | deviation, not a consumption break |
| Glued-word tokens in INDEX, SCENARIOS, POSITIONS, RETIRED_CLAIMS, channel entries 10/14 and 10/19 | **debt** (root Output Canon) |
| `predictions_due_check --quiet` and `kb_expiry_check --quiet` print nothing when clean; `derived_drift_check` exits 0 always | **debt** (CHECK_STANDARD §3(b) clean line; drift advisory at boot) |

## 5. Load-bearing context / DO NOT TOUCH

1. Frozen frames: Q2 frame, PREPRINT_RECON, EARNINGS_PREP: path fixes only. Q3 10-Q frame: graded verbatim. Re-score rule: dated note before the filing only. Q3 print frame: graded, never edited.
2. WAL-01 stays OPEN until the 10-Q cross-check; never closed to quiet a guard.
3. KB `Stale_By`: never bulk re-dated; `AWAITS:<carrier>@<date>` is the only sanctioned deferral.
4. RETIRED_CLAIMS rows are drift-check patterns: append, never delete.
5. THESIS line-3 header format is regex-read by `boot.py:89-93` and `derived_drift_check.py:59-70`; reformatting blinds both silently. STATUS line 3 "Last Updated" is read by `boot.py:84-86`. KB Fact text "FINRA settlement YYYY-MM-DD" is `boot.py`'s short-interest key.
6. `POSITIONS.md` wording "acquisition October 7 from earlier Activity" is a test fixture anchor (`test_maintenance_state_check.py:22`).
7. 📼 FRAUD records take dated riders, never in-place edits. GATE-REG-T02 is TERMINAL: never re-signal.
8. `DRIFT_HISTORY_2026-10-14.json`: new identities need review, never bulk acceptance; `review_by` 11/9 lands on the 10-Q session.

## 6. Maturity snapshot (references `FLEET_MAP.tsv`; does not restate class)

Re-cut 2026-10-30 from this refresh: 7 of the 8 gaps recorded 10/22 are closed at the artifact (re-score rule, kill-rail stamp, CLOSED-set fix, BOTTOM LINE, inbox/WALTER boot step, 25 READS rows, REGINALD ACKs); `scripts/boot.py` now exists. **L3 dated-falsification leg adjudicated PASS** (dated rail + pre-registered mapping). Open: forward predictions (dated deferral ≤11/15), the 10-Q frame gap above, kill rail with no mechanical reader, charter at 88%, 8 ACTIVE KB rows past `Stale_By` (the 10/28 review missed them by the strict `<` boundary). Consumer leg evidenced: REGINALD (obliged, quotes grades accurately), TERRY (SHA-matched use of the Q3 report), NEXUS and RED (direction).

## 7. Open questions / comprehension gaps

- Has the Q3 10-Q filed? Not on EDGAR at 10/28 22:40 ET; no check since (no reader fetched EDGAR).
- Bear CONFIRM loses its last carrier at the 10-Q: re-derive or retire it at that session.
- Not read whole by any reader: THESIS body, CHANGELOG, frame bodies, KB.tsv (header, sample and scripted counts only), research/sources/archive bodies, 71 processed inbox packets.
- `boot.py` price step not run (network + cache writes).
