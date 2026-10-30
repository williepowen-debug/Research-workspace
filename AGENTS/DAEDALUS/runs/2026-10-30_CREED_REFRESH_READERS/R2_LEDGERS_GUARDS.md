# CREED Mode-A refresh — Reader 2: LEDGERS · FALSIFICATION · GUARDS

**Reader:** R2 of 3 (DAEDALUS fan-out) · **Started:** Fri 2026-10-30 16:10:54 EDT (`date`) · **HEAD:** `461cbcc82`
**Mode:** read-only on all tracked files; only write = this file. Mutation tests ran on scratch copies under `/tmp/claude-1000/creed-r2/`.
**Pre-run tree state:** `git status --porcelain -- AGENTS/CREED/` → empty (0 paths) at 16:10:27 EDT.
**Baseline:** `profiles/CREED.md` (10/21 STALE banner, body vintage 8/11–8/20) · `upgrades/CREED_REVIEW_2026-08-20.md` · FLEET_MAP `CREED Market L4 H last-scored 2026-10-21`.

(sections A–I follow; written incrementally)

## A. Ledger table

`LEDGER_GLOB` = `workbook/*.tsv registry/*.tsv cases/*.tsv` (workbook/LEDGER_GLOB:1). Rows = non-`#` lines minus header. CRLF = 0 on every TSV. "Newest content" = newest date in the row date column (KB col 2, VX `Last_Updated` col 10, VX_HISTORY `Date`, etc.).

| File | Rows | Header state | Newest content cell | Silent-rot verdict |
|---|---:|---|---|---|
| workbook/VX.tsv | 34 | LIVE two-clock **2026-10-28 (late)** (VX.tsv:2) | Last_Updated 2026-10-28 | ✅ clean; header = content |
| workbook/KB.tsv | 90 | LIVE two-clock **2026-10-22 (evening)** (KB.tsv:2) | **16 rows KB-075..090 dated 2026-10-28** | 🟠 header LAGS content 6d (rows added 10/28, `eb4ae6d00`; header not advanced). Fails toward STALE (conservative), but the content clock is false |
| workbook/VX_HISTORY.tsv | 120 | LIVE two-clock **2026-10-22** (VX_HISTORY.tsv:2) | rows :121 (7.01 2026-10-28), :122 (9.03 Q3), :124 (5.03 2026-10-28), :125 (9.02 Sep) added 10/28 | 🟠 same lag (6d). Also **name-exempt** ("history") from the default scan — only `--strict` grades it |
| workbook/PREDICTIONS.tsv | 11 | LIVE two-clock **2026-10-22** (PREDICTIONS.tsv:2) | PRED-008 note rewritten 2026-10-28 (`eb4ae6d00`) | 🟡 header lags a note-only edit (data unchanged — arguably correct) |
| workbook/FLOW.tsv | 9 | LIVE two-clock **2026-10-28** (FLOW.tsv:2) | rows 01/02/03/06 10/28 | ✅ |
| workbook/SCHEMA.tsv | 15 | LIVE two-clock 2026-09-29 (SCHEMA.tsv:2) | — | ✅ (schema; name-exempt; `--strict` reads it STALE +30d — expected for a schema) |
| registry/THRESHOLDS.tsv | 11 rows (CREED-T-*) | **no two-clock line**; scanner classifies it **FROZEN** | band_status "STATE 2026-10-28" (THRESHOLDS.tsv:45,46,49) | 🔴 **LIVE registry silently exempted as FROZEN** — see E-1 |
| registry/CREED_T_FIRED_LOG.tsv | 3 fires (T-02, T-06b, T-08a) | `Cadence: EVENT-DRIVEN` + `Last re-pull ATTEMPTED: 2026-09-26` (FIRED_LOG.tsv:14-15) | T-08a fired 2026-09-26 | 🟠 re-pull clock **not advanced** although CREED demonstrably looked on 10/21 (T-01a/T-01b graded) and 10/28 (T-06/T-06b re-census) — the file's own text says that clock "records that CREED LOOKED" (FIRED_LOG.tsv:25-26) |
| registry/corrections_receipts.tsv | 9 | none (3-col receipt log) | 2026-10-29 | ✅ (git fallback; rc 0) |
| cases/CASES.tsv | 166 | LIVE two-clock 2026-10-28 (late) (CASES.tsv:2) | 10/28 | ✅ (matches STATUS:122 "cases 166") |
| cases/CASE_EVENTS.tsv | 412 | LIVE two-clock 2026-10-28 (late) (CASE_EVENTS.tsv:2) | 10/28 | ✅ |
| evals/results.tsv | 2 + comments | **FROZEN 2026-09-29** banner (results.tsv:1) | 2026-08-13 | ✅ correctly frozen (v1 record) |
| evals/results_v2.tsv | 8 | LIVE two-clock 2026-10-28 (results_v2.tsv:2) | 2026-10-28 | 🟡 outside LEDGER_GLOB (perimeter line names it) |
| board_log.tsv | 249 | none (log) | 2026-10-29 | ✅ log, not a ledger |

**Out-of-perimeter TSVs (scanner's own perimeter line):** evals/results.tsv, evals/results_v2.tsv, research/data/2026-10-22_fdic_restructured_nfnr_series.tsv, research/data/2026-10-28_case_residual_flags_patch.tsv — research data files, not ledgers; evals is the only one with a live clock.

**Counts cross-check (selfcheck "actual" line vs disk):** VX 34 · KB 90 · PRED 11 (open 3) · workbook files 9 — all match disk and STATUS:122. ✅

## B. Predictions

**Command:** `awk -F'\t' '!/^#/ && NR>1 && $1 ~ /^PRED/{print $7}' workbook/PREDICTIONS.tsv | sort | uniq -c` →
`3 OPEN · 2 RESOLVED-FALSE · 1 RESOLVED-PARTIAL · 5 RESOLVED-TRUE` (11 rows).

| ID | Conf | Resolves | Status | Note |
|---|---:|---|---|---|
| 001 | 40% | Trepp DQ Aug–Dec 2026 | OPEN | office DQ >12.00 **and holds 2 prints**; Sep 12.16 = leg 1; Oct print (~early Nov) decides (PREREG_2026-11) |
| 002 | 45% | Trepp SS Jul–Dec 2026 | OPEN | Sep 16.85, moving away |
| 008 | 45% | KREF Q4 (~Feb 2027) | OPEN | note refreshed 10/28 |
| 002a | **none** | June SS | RESOLVED-TRUE | retrospective; excluded from calibration with reason (SCOREBOARD:79) ✅ |
| 003/006 | 35/30 | QBP / MBA | RESOLVED-FALSE | |
| 004/005/007/009 | 60/70/15/30 | | RESOLVED-TRUE | |
| 010 | 70% | Athene 10-Q | RESOLVED-PARTIAL | not scored, Will 9/29 (SCOREBOARD:80) |

- **Past resolve date and still open:** **none.** 001/002 run to 2026-12-31; 008 to ~Feb 2027. ✅
- **Grade-vs-letter checks:** 009 letter ">50% sustained" → TRUE on May 70/Jun 65 (FIRED_LOG.tsv:30) ✓; 007 letter "≥10pp over any trailing 3-mo window" → TR −10.12 on 9/24 and price-only −13.59 on 9/25 (THRESHOLDS.tsv:48) — passes on both bases, so the basis ruling of 9/10 cannot have manufactured the hit ✓; 006 letter "≥+$10.0B as printed" → +$7,830M FALSE ✓; 001 "holds 2 consecutive" correctly NOT graded on leg 1 ✓. No letter drift found.
- **Brier arithmetic re-derived:** 0.49 + 0.1225 + 0.7225 + 0.16 + 0.09 + 0.09 = 1.675; ÷6 = **0.279** — matches SCOREBOARD:14. Hit-rate 4/6 matches (003/004/005/006 right side). ✅
- **Calibration surface:** `PREDICTIONS_SCOREBOARD.md` updated 2026-10-22 (SCOREBOARD:3); no resolution since, so current. Brier 0.279 is **worse than the 0.25 coin-flip baseline** and the scoreboard says so (SCOREBOARD:14, :37-67 — the "false premise" analysis). ✅ honest.
- 🟡 Kernel-pinned: 001/004/007 were submitted to Gate C (outbox/kernel/submissions/ 12 JSONs); 004/007 are CREED-graded but "Kernel records stay OPEN until a Gate C sitting" (CALENDAR.md:29). Two ledgers, two states — disclosed.
- 🟡 Book is thin: only 3 OPEN, zero new predictions registered since 7/27 (all Date_Made 2026-07-27 or earlier per PRED rows). With 8 of 11 resolved, the L3 "predictions resolving" leg will starve after the Oct print unless new ones are registered.

## C. Falsification surface (rebuilt inventory, as of HEAD 461cbcc82)

| # | Surface | Where | Dated / current? | Verdict |
|---|---|---|---|---|
| 1 | Frozen trigger registry (11 CREED-T rows, 10 cols) | registry/THRESHOLDS.tsv:38-49 | Per-row `STATE <date>` in band_status: T-01a/01b/04 2026-10-22 (:39,:40,:43); T-06/06b/08b 2026-10-28 (:45,:46,:49); T-08a FIRED 9/26 (:48); T-02 spent (:41); T-03 re-based 8/27 + scope limit encoded (:42); T-05/T-07 static (:44,:47) | ✅ dated per row; ⚠️ but see E-1 (no file-level clock; scanner treats it FROZEN) |
| 2 | Open band-authority obligation (D) n=12 base-rating | THRESHOLDS.tsv:26-30; counter = threshold_scan | n = 9/8/6/4/2 per vector today (scan output) | ✅ live, counted, nothing DUE |
| 3 | Fire ledger | registry/CREED_T_FIRED_LOG.tsv:30-32 | 3 fires with effective/fired/detection-lag columns | ✅ (🟠 re-pull clock stale, A) |
| 4 | **Pre-registered grading letter for the next print** | registry/PREREG_2026-11_TREPP_PRINT.md:1-30 | Written 2026-10-22 13:44 ET, FROZEN on commit; T-01a decision rule, tie convention (12.00 ≠ >12), refuse-list, noise yardstick (mean 13.5bp, n=6) fixed in advance | ✅ **strength — the best-formed falsification artifact on the desk** |
| 5 | Prior PREREGs (graded record below the line) | PREREG_2026-09 / PREREG_2026-10 | graded 9/02, 10/21 | ✅ history, correctly superseded by -11 |
| 6 | Thesis Counter-Signals (6 thresholds) | thesis/THESIS.md:115-123 | **list itself unstamped** ("Would weaken the bear read:"), wording is *weaken*, not *kill*; no sustain/session-count handle | 🟡 OPEN since 8/20 (review 🟡 "threshold list unstamped") |
| 7 | Live counter-signals block | THESIS.md:125-132 | "as of 2026-10-28", 🆕 markers on 10/28 adds; equity-tape counter-signal explicitly retired (:132) | ✅ |
| 8 | Convergence matrix as-of line | THESIS.md:93 | says **"rows 3–7 2026-09-30 … row 7's CBRE Q3 not yet checked"** | 🟠 **contradicted by its own body:** row 7 (THESIS.md:103) carries "Q3 [CBRE, 10/23]: 18.2%"; rows 3 and 6 (:99, :102) carry 🆕 10/28 reads. Partial-refresh class (CREED's own trap #8, CLAUDE.md:74) — the as-of header certifies a vintage the cells no longer have |
| 9 | Kill rails / exit | — | No thesis-level KILL rule with a session count exists; the desk's falsification is carried by (1)+(4)+(6). Charter scope says "Not a trade recommendation" (THESIS.md:5) | 🟡 acceptable for no-book Tier-2; same "handle thin" note as profile §3 |

**Kill-rail state today:** T-02 FIRED-spent · T-06b FIRED (S6 held at 3, Will) · T-08a FIRED (S8a = 4, Will 9/28) · **T-01a LEG 1 OF 2** (Oct print ~early Nov decides, ≥12.01 fires) · T-01b clear (115bp) · T-03 not fired (Q3 QBP ~late Nov, CALENDAR.md:9) · T-04/T-07/T-08b qualitative, T-08b re-grade after STWD/ACRE 11/6 (THRESHOLDS.tsv:49).

`falsification_scan.py --agent CREED` graded **thesis/CHANGELOG.md** (newest entry 2026-10-28) → CURRENT. Its PASS proves only that the append-only changelog has a recent entry; it never reads the Counter-Signals list (#6) or the matrix as-of line (#8). The defect at #8 is invisible to it by construction.

## D. Trade leg (L4 reading A)

- **No trade surface exists** (`ls AGENTS/CREED | grep -i trade` → none). Charter: "trade execution or position decisions — Will approves" (CLAUDE.md:33), "Do not execute trades" (CLAUDE.md:234); THESIS scope "Not a trade recommendation" (THESIS.md:5). ⇒ **"no book by charter"** branch of reading A. No explicit declared-flat banner is needed under that branch, but none of the three surfaces says the words "no book" — the branch is inferred from scope lines, not declared. 🟡
- **Signals reaching a consumer (the other half of reading A):** T-08a fire packets landed at REGINALD (`inbox/processed/2026-09-26_from-CREED_T-08a-FIRED…`), LIQUID, PROME (commit `afbf56264`, 9 files). ✅ consumer leg met via REGINALD (processed) + PROME.
- 🟠 **TERRY leg claimed but never delivered.** THRESHOLDS.tsv:48 recipient_chain and FIRED_LOG.tsv:32 `routed_to` both say **"TERRY (info)"**. `afbf56264` (CREED's 9/26 fan-out) sent nothing to TERRY; `grep -rn 'T-08a' AGENTS/TERRY` → **0 hits**; TERRY inbox/processed holds no CREED packet since 9/1 (only a 10/23 PROME card that quotes CREED in passing). The ledger records a route that has no artifact (record-of-action ≠ action).
- TERRY setups/SETUPS.tsv/SIGNALS.tsv: no CREED-sourced setup since 9/1 (grep 'CREED' → 0 rows). Expected for a no-book transmitter; it means L4 rests on the "signals reach a consumer" leg alone.

## E. Guard runs (all from repo root; tree `git status --porcelain -- AGENTS/CREED/` = 0 paths before AND after every run)

| # | Command | rc | Key output | Capable case (scratch) | Clean case | Verdict |
|---|---|---:|---|---|---|---|
| E-1 | `ledger_staleness.py CREED` / `--writes --abs-floor` | 0 / 0 | 9 rows; **THRESHOLDS.tsv = FROZEN**; FIRED_LOG quiet (EVENT-DRIVEN) | Copy of THRESHOLDS with line 5's "FROZEN TERMS" → "Will-gated terms": `is_frozen` **True → False** | — | 🔴 **The registry is exempted by a prose MENTION.** THRESHOLDS.tsv:5 "# Threshold bands are FROZEN TERMS" sits in the 6-line banner region and is read as a dead-banner. The LEDGER_GLOB was extended to `registry/*.tsv` on 8/20 *because* the registry had been "outside ALL staleness enforcement — the exact surface class whose staleness produced K5" (CLAUDE.md:111). That enforcement is void for the one file it was for. (`finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it`.) |
| E-1b | `--strict --writes --abs-floor` | 1 | adds VX_HISTORY (+7d ok) and SCHEMA (STALE +30d) | — | — | VX_HISTORY only graded under `--strict`; boot recipe (CLAUDE.md:117) runs non-strict → live append ledger name-exempt. 🟡 (8/20 🟡 OPEN) |
| E-1c | `--nudge` | 0 | "STATUS not moving this session" | — | — | thresholdless; correct for an idle desk |
| E-2 | `corrections_boot_check.py CREED` | 0 | 0 unreceipted of 110 register rows; 9 receipts | not mutated (writer path) | ✅ | PASS covers presence of receipts only (its own disclaimer). ✅ |
| E-3 | `falsification_scan.py --agent CREED` | 0 | 1 surface CURRENT = thesis/CHANGELOG.md (stamp 10/28) | — | ✅ | 🟠 PASS = changelog recency; blind to C#6/C#8 (DAEDALUS-side scope note) |
| E-4 | `claim_check.py --check weekday CALENDAR.md STATUS.md` | 0 | "✓ 2 file(s) clean" | Scratch CALENDAR with `**2026-11-12** (Thu)`→`(Wed)`: **still clean, rc 0**. Plain-form fixture `2026-11-12 (Wed)`: fires rc 1 | my own `date` check: all 5 labels correct (9/27 Sun, 9/29 Tue, 10/28 Wed, 11/12 Thu) | 🔴 **cannot fail on CREED's dominant form.** `RE_WEEKDAY_AFTER` (scripts/claim_check.py:103-105) allows no `**` between date and day; 4 of CREED CALENDAR's weekday pairs are `**date** (Day)` (CALENDAR.md:15,16,20,23). No wrong label today — the guard is blind, not the calendar wrong. Fleet tool → DAEDALUS |
| E-5 | `AGENTS/CREED/scripts/threshold_scan.py` (boot 4c) | **1** | 5 comparable/6 unscannable; **T-01a "🔴🔴 TRIPPED … NOT IN THE FIRE LEDGER … GO GRADE IT AT PRIMARY NOW. This is the K5 state"** | VX-2.01 → 18.40: T-01b TRIPPED rc 1 ✓; T-08a row deleted from FIRED_LOG: T-08a TRIPPED ✓ | T-01a → 9.50: **rc 0** ✓ | ✅ both directions. 🟠 **but no sustain model** (`grep -i sustain threshold_scan.py` → 0 hits): a graded leg-1-of-2 row prints the K5 alarm text every boot until the Oct print; CREED overrides it by hand (STATUS:38 "T-01a shows TRIPPED = leg 1, graded"). A standing false-K5 line is the always-red shape that trains skipping. Also NEAR (11.90) → rc 1 |
| E-6 | `AGENTS/CREED/scripts/creed_selfcheck.py` (closeout 8b) | 0 | VX 34 · KB 90 · PRED 11 (open 3) · files 9; ✓ CLEAN; 3 disclosed colour exceptions | ③ KB-074 Conf → "80%": **flags, rc 1** ✓. ① fake T-01b fire row: flags STATUS + THESIS "never names it" ✓ | real tree rc 0 ✓ | 🔴 **check ① "no fire marker" branch cannot fail.** Scratch THRESHOLDS with every `FIRED` removed from T-08a's own row (0 in-row, 8 elsewhere) → **✓ CLEAN rc 0.** The marker test is `FIRE_MARK.search(body)` over the WHOLE FILE (creed_selfcheck.py:64-67), and `\bFIRED\b` also matches "NOT FIRED". Any surface naming two triggers, one fired, satisfies it for all. CLAUDE.md:157 states the rule as "a trigger … must show a fire marker on every surface that names it" — not what is enforced |
| E-7 | `scripts/boot.py` | not run | RETIRED 2026-09-02 (boot.py:1-25; README.md:45) | — | — | ✅ retired-with-note (8/20 #6 CLOSED). 🟡 its retirement docstring still cites "boot step 7's `find -mtime`" (boot.py:18), replaced 9/29 by ledger_staleness (CLAUDE.md:122) |
| E-8 | `scripts/workbook_patterns.py --help` | 1 | ModuleNotFoundError openpyxl (system python; docstring says `.venv/bin/python3`) | — | — | ran before reading — failed at import, no writes (tree 0 paths after). Not a boot/closeout guard |

## F. registry/ · evals/ · cases/ — purpose and liveness

**registry/ (8 top-level files + 2 dirs = 21 files)**

| File | Registers | State | Verdict |
|---|---|---|---|
| THRESHOLDS.tsv | 11 frozen CREED-T bands + live band_status + open obligation (D) | LIVE, edited 10/28 (`eb4ae6d00`); 15,559 B = 48% of read budget | ✅ content; 🔴 scanner-exempt (E-1) |
| THRESHOLDS_NOTES.md | verbatim cold history of THRESHOLDS cells (sha-pinned source, THRESHOLDS_NOTES.md:4) | on-demand history | ✅ |
| CREED_T_FIRED_LOG.tsv | 3 fires, effective vs fired vs lag | LIVE, EVENT-DRIVEN | ✅ (🟠 re-pull clock 9/26) |
| PREREG_2026-11_TREPP_PRINT.md | grading letter for the Oct prints | LIVE, frozen-above-line, written 10/22 | ✅ strength |
| PREREG_2026-10 / PREREG_2026-09 | Sep / Aug print letters + graded records below §6 (:46 / :61) | graded history | ✅ (self-describing as graded; no "superseded" banner needed — the class name carries it) |
| BAND_REVISIT_2026-08-27.md | month-1 band revisit, executed 6d late, lateness recorded (:3) | closed episode; cited by THRESHOLDS:37 | ✅ history, live-referenced |
| corrections_receipts.tsv | R1 corrections receipts (9) | LIVE, 10/29 | ✅ |
| kernel_staged/ (README + 6 JSON) | Gate C Increment-2 commands 101-106, staged 8/27 | README.md:4 says **"⛔ STAGED ONLY. NOTHING HERE HAS BEEN SUBMITTED"** — but all 12 commands (101-106, 111-116) are in `outbox/kernel/submissions/` | 🟡 **stale claim on a registry surface, no banner**; not referenced by README/CLAUDE/STATUS (grep → 0); 64 days old → retirement-eligible under root Data Hygiene |
| kernel_staged_v2/ (6 JSON, no README) | commands 111-116 | same; last commit `652169902` 2026-08-27 | 🟡 dead without a banner |

**evals/ (11 files):** README (v1 + v2 sections), 4 cases × INPUT/RUBRIC, results.tsv (v1, FROZEN 9/29 banner, results.tsv:1), results_v2.tsv (LIVE). v2 rebuilt 10/22 with contamination rule v2 (evals/README.md:57); baseline 4/4 PASS on surface `35c1f0dfcbae`, re-run 4/4 PASS on `302c26c49cd4` 10/28 — **that sha = current `sha256(CLAUDE.md)`[:12]** (computed), so the suite is current to the live charter ✅. Limits CREED itself states: all 4 cases test traps whose text is in the prompt → "retrieval-and-application, not independent judgment" (README.md:72). 🟡 case_02 moved TARGET → GUARDRAIL after one pass (results_v2 rows 2 vs 6; README.md:66 "TARGET → now GUARDRAIL once it passes") → **zero TARGET cases**: the suite can now only detect regressions, never improvement. Disclosed; next-build intent stated.

**cases/ (15 files):** a named-distress case ledger (cases/README.md:6-8) — CASES.tsv 166 rows (29 cols), CASE_EVENTS.tsv 412 events, CASE_NOTES.md (390,964 B, read by section only), README (vocab + registered pattern questions :55-70 + selection-bias limit :10 + readiness limits :82), sources/ (Will's v3/v4 xlsx + 9 verbatim TSV exports). Live, in LEDGER_GLOB, two-clock 10/28. Cases have no open/closed flag; `latest_status` is the lifecycle: SOLD 68 · UNKNOWN 25 · SPECIAL_SERVICING 19 · REO 17 · FORECLOSURE 12 · DEFAULT 9 · MODIFIED 4 · BANKRUPTCY 4 · NOTE_SALE 3 · RECEIVERSHIP 2 · FORECLOSED 2 · EXTENDED 1. **Refuted hypothesis:** FORECLOSED vs FORECLOSURE looked like a token fork — both are defined vocab (README.md:45). 🟡 25 UNKNOWN status / 24 UNKNOWN status_as_of (~15%) — disclosed by the selection-bias/readiness limits, not a defect. `scripts/import_cre_workbook.py` APPENDS to CASES/CASE_EVENTS/CASE_NOTES (import_cre_workbook.py:341-350) — a one-shot importer with an append path — **hypothesis 'a re-run would duplicate' REFUTED:** it refuses if any CRE- seed id or workbook event is already present (import_cre_workbook.py:24, :172-174). ✅

**scripts/ (10):** threshold_scan (boot 4c, live), creed_selfcheck (closeout 8b, live), s8a_relative (S8a recompute, boot 6.6), trepptalk_sweep (+test), test_history_validation (copies CREED to a temp home, runs scan+selfcheck), test_s8a_float_tie, workbook_patterns (reproduces the cases pattern note; needs `.venv` openpyxl), import_cre_workbook (one-shot importer, appends), boot.py (RETIRED).

## G. Reconcile prior-profile / 8/20-review items in this cluster

| Item (source) | Now | Receipt |
|---|---|---|
| Profile §2: "PREDICTIONS.tsv = 10 open … SCOREBOARD honest n=0" (CREED.md:36) | **CHANGED** — 11 rows, 3 open, 6 scored (Brier 0.279), 2 excluded | §B |
| Profile §2: evals "SHIPPED UNRUN" (CREED.md:40) | **CHANGED → CLOSED** — v1 ran 8/13 (VOID, frozen); v2 4/4 ×2 | results.tsv:1; results_v2.tsv |
| Profile §2: boot.py mechanics-only (CREED.md:41) / review #6 orphan + mtime | **CLOSED** retired-with-note | boot.py:1-25; README.md:45 |
| Profile §3: invalidation "no session-count/FIRED handle" (CREED.md:49) | **CHANGED** — FIRED handle + sustain windows + PREREG letters exist; the THESIS Counter-Signals list itself still has no N and no stamp | THRESHOLDS.tsv:38-49; FIRED_LOG; THESIS.md:117-123 |
| Profile §3: predictions "missing substance" (CREED.md:51) | **CLOSED** | §B |
| Profile §2 registry: "audit the row→vector→reader CHAIN" (CREED.md:37) | **CHANGED** — reader exists (threshold_scan, both-direction verified); new hole is the *staleness* reader for the registry file (E-1) | E-1, E-5 |
| Review #1 boot-time threshold scan | **CLOSED** | CLAUDE.md:86; E-5 |
| Review #2 source_of_truth pointers T-01b/T-02/T-08a | **CLOSED** — 2.01 / 3.04 / 7.01 | THRESHOLDS.tsv:40,41,48 |
| Review #3 T-08a basis | **CLOSED** — TR, WQ-215 | THRESHOLDS.tsv:35-36 |
| Review #4 month-1 revisit untracked | **CLOSED** — executed 8/27 | BAND_REVISIT_2026-08-27.md:3 |
| Review #5 evals self-defeating | **CLOSED** (rule v2) with disclosed limit | evals/README.md:57 |
| Review #7 PRED-009 swapped cells / token fork | **CLOSED** | PREDICTIONS row 009: Date_Resolved "2026-06 … / 2026-08-20", Status RESOLVED-TRUE |
| Review #8 VX-1.02 compound refuted cell | **CLOSED** — single headline 8.02% [Trepp Sep, PRIMARY-READ] | VX.tsv VX-CREED-1.02 |
| Review #9 LEDGER_GLOB absent | **CHANGED** — exists and covers registry + cases; but THRESHOLDS exempted by prose (E-1), evals outside glob, VX_HISTORY name-exempt | workbook/LEDGER_GLOB:1; E-1 |
| Review #10 T-03 scope limit only in SCRATCH | **CLOSED** — in the row | THRESHOLDS.tsv:42 "⚠️ SCOPE LIMIT (pre-registered 2026-08-20) … ONE-SIDED" |
| Review 🟡 Counter-Signals list unstamped | **OPEN** | THESIS.md:115-117 |
| Review 🟡 VX_HISTORY name-exempt | **OPEN** | E-1b |
| Review 🟡 FLOW off-vocab / no per-row date | not re-checked (FLOW 9 rows, header 10/28) | — |
| 10/21 banner "STATUS 24,217 B, below rotation trigger" (CREED.md:3) | **CHANGED** — STATUS **26,261 B = 81%** (rotate-tier); also THESIS 80%, COVERAGE 79%, VX.tsv 78%: `read_cap_check --agent CREED` rc 0, **rotation_due=4** | read_cap_check output 16:1x EDT |

## H. Ranked route list

| Rank | Sev | Finding | Owner | Ask |
|---:|---|---|---|---|
| 1 | 🔴 | creed_selfcheck check ① "no fire marker" branch cannot fail (file-level `\bFIRED\b`, matches "NOT FIRED"); proven by scratch mutation | **CREED** | scope the marker to the trigger's own row/line (THRESHOLDS: the row's col 10; prose: same line or ±N chars), exclude `NOT FIRED`; re-falsify with the T-08a mutation |
| 2 | 🔴 | THRESHOLDS.tsv exempted as FROZEN by "FROZEN TERMS" prose (THRESHOLDS.tsv:5) | **CREED** (header wording + add `# LIVE ledger.` + two-clock line) · **DAEDALUS** (ledger_staleness banner-region rule: a line-initial `# Threshold bands are FROZEN …` should not read as a dead banner; or require the marker as first token after `#`) | one-line header fix desk-side; tool fix fleet-side |
| 3 | 🔴 | claim_check weekday blind to `**date** (Day)` (claim_check.py:103-105); 4 of CREED's calendar labels unguarded | **DAEDALUS** (scripts/ owner) | allow optional `**` between date and day in RE_WEEKDAY_AFTER; fixture both forms; base-rate other desks |
| 4 | 🟠 | FIRED_LOG/THRESHOLDS route "TERRY (info)" for T-08a never delivered | **CREED** | send the info packet or strike TERRY from the routed_to cell with a dated note (record ≠ action) |
| 5 | 🟠 | THESIS matrix as-of line (THESIS.md:93) contradicts row 7/3/6 cells | **CREED** | re-stamp the as-of line (trap #8) |
| 6 | 🟠 | threshold_scan has no sustain model → standing false "K5 state" alarm on T-01a leg 1 | **CREED** | read col 6 sustain + a graded-leg marker → print `LEG k OF n (graded <date>)`, not TRIPPED |
| 7 | 🟠 | KB / VX_HISTORY two-clock headers 6d behind content; FIRED_LOG re-pull clock 34d behind actual looks | **CREED** | advance headers at the 10/28 vintage; closeout step 1 to name the header |
| 8 | 🟠 | read-cap: 4 boot reads in rotate-tier (STATUS 81%, THESIS 80%, COVERAGE 79%, VX 78%) | **CREED** (R1 likely owns) | rotate to <70% at next launch |
| 9 | 🟡 | kernel_staged/README "NOTHING SUBMITTED" false; v2 dir bannerless; 64d old | **CREED** | banner or `git mv` to archive/ |
| 10 | 🟡 | evals: zero TARGET cases; results_v2 outside LEDGER_GLOB | **CREED** | add a not-in-prompt TARGET case (already its stated next build) |
| 11 | 🟡 | Counter-Signals list unstamped, "weaken" not "kill", no N | **CREED** | stamp + per-line sustain (Will-gated if it moves a band) |
| 12 | 🟡 | prediction book thin: 3 open, none registered since 7/27 | **CREED** / PROME (L3 leg health) | register 2-3 new dated predictions before the Oct print resolves 001 |
| 13 | 🟡 | falsification_scan for CREED grades only CHANGELOG recency | **DAEDALUS** | note in scan output that a CHANGELOG PASS ≠ counter-signal currency |
| 14 | ℹ️ | CREED CLAUDE.md = 39,557 B (> 32,550 budget), always-loaded, out of read-cap perimeter | R1 / **DAEDALUS** | cross-reader item, not graded here |

## I. Coverage

| Surface | Read | Notes |
|---|---|---|
| profiles/CREED.md | whole (79 lines) | baseline |
| upgrades/CREED_REVIEW_2026-08-20.md | whole (61 lines) | baseline |
| FLEET_MAP CREED row | whole | grep |
| CREED CLAUDE.md (39.5 KB) | in part: :78-164 (boot order, workbook, closeout) + greps | >32 KB rule |
| registry/THRESHOLDS.tsv | whole (cut -c1-700 per line; band_status cells truncated) | |
| registry/CREED_T_FIRED_LOG.tsv | :1-32 (rows cut to verdict cols) | |
| registry PREREG_2026-11 | :1-30; PREREG-09/10, BAND_REVISIT, THRESHOLDS_NOTES: heads only | |
| registry/kernel_staged README | :1-15; JSON 111 head only | |
| workbook/*.tsv | headers + row/column extracts via awk/grep; KB.tsv (173 KB) never whole | |
| PREDICTIONS.tsv | all 11 rows, cols 1-9 (Notes truncated) | |
| PREDICTIONS_SCOREBOARD.md | :1-14 + all table/heading lines | |
| THESIS.md | :1-12, :68-135 | :136-end skipped (handoffs/open Qs — R1/R3 cluster) |
| STATUS.md | :1-8 + grep of headings | rest = other readers |
| CALENDAR.md | whole (29 lines, cut 330 chars) | |
| evals/README.md | headings + :53-66; results*.tsv whole (cols 1-6) | case INPUT/RUBRIC files not read |
| cases/README.md | :6-9, :32-46, :55-70; CASES.tsv status/status_as_of columns | CASE_NOTES.md (391 KB) not read |
| scripts | creed_selfcheck :1-75; threshold_scan :50-62 + greps; boot.py :1-52; workbook_patterns :1-15; write-path grep of all 10 | trepptalk/s8a/tests not read |
| Not read | SCRATCH (only 3 grep hits), COVERAGE, MAINTENANCE, LAST_COMPLETION (grep only), notes/VX_NOTES, catchups/, research/, inbox/ | other readers' clusters |

**Post-run tree state:** `git status --porcelain -- AGENTS/CREED/` → 0 paths after every script run (last check after read_cap_check). Scratch copies: `/tmp/claude-1000/creed-r2/` (root/ = full CREED copy; mutated files restored there after each test).
