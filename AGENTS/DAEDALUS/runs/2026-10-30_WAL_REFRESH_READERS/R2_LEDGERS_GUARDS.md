# WAL refresh — Reader 2 of 3: LEDGERS · FALSIFICATION · GUARDS

**Run start:** 2026-10-30 12:27 EDT (`date`) · DAEDALUS Mode-A helper (not owner) · read-only against the repo; only write is this file (plus scratch fixtures under the session scratchpad, outside the repo).
**Baseline:** `AGENTS/DAEDALUS/profiles/WAL.md` (12,010 B, built 2026-08-07, STALE annotation 2026-10-21) — read whole.
**Status:** COMPLETE — sections 1–8 below. Top finding: O1 (re-score rule has no row for a below-book appraisal without a disclosed reserve; window closes when the 10-Q hits EDGAR).

**WAL live-session check:** last WAL-authored commits `03125d44c` 2026-10-28 22:58 and `4e713d7c1` 2026-10-28 23:28 ("WAL housekeeping"); every AGENTS/WAL commit since is an inbound packet (REGINALD `9011ebff5`, WALTER `78e3eefe5`, TERRY `edf055f1a`, 10/29). `git status --porcelain -- AGENTS/WAL` = 0 lines before and after every guard run below.
**Cluster file list (bytes):** THESIS.md 61,921 · workbook/PREDICTIONS.tsv 23,504 · workbook/RETIRED_CLAIMS.tsv 14,027 · workbook/MI3_SERIES.tsv 2,892 · workbook/KB_INDEX.md 2,375 · workbook/KB.tsv 293,696 · registry/corrections_receipts.tsv 166 · Q3_10Q_GRADING_FRAME_2026-09-24.md 27,183 · Q3_PRINT_GRADING_FRAME_2026-09-24.md 28,635 · Q3_10Q_RESCORE_RULE_2026-10-22.md 6,656 · EARNINGS_PREP.md 33,875 · EARNINGS_PREP_BANNER_RIDER_2026-08-23.md 5,621 · scripts/predictions_due_check.py 5,414 · kb_expiry_check.py 5,643 · derived_drift_check.py 12,708 · maintenance_state_check.py 5,965.

---

## 1. Predictions ledger (`workbook/PREDICTIONS.tsv`, 3 data rows, 11 columns, `tsv_append --check` rc 0)

| ID (line) | Claim (verbatim Prediction cell) | Conf (as made) | Resolve_By · anchor | Status | Date_Resolved | Outcome / what resolves it |
|---|---|---:|---|---|---|---|
| WAL-01 (:7) | "WAL Office classified loans exceed $500M by end of Q3 2026" | 25% | 2026-11-15 · release/call 10/19–10/20 + SCHEDULED-FILING 10-Q due 11/9 (Notes, 10/19 entry) | **OPEN** | blank | Outcome cell: "2026-10-19 Stage1 INVALIDATED (PROVISIONAL): EX99.2 slide 13 Office 25% x classified 1091M=272.75M <=500M ... CROSS-CHECK-UNRUN, Q3 10-Q pending." **Resolves on the Q3 10-Q** (10-Q frame §1 cross-check: deck Office $ ≤ 10-Q classified loans + OREO). Only outcomes left: FINAL INVALIDATED (pass), NO-VERDICT/INSTRUMENT-CONFLICT (fail), or provisional stands tagged CROSS-CHECK-UNRUN. It cannot become CONFIRMED. |
| WAL-02 (:8) | "WAL ex-fraud NCO rate exceeds 40bps in at least one of Q2 or Q3 2026" (row is Q3-only since the 8/20 re-spec; Prediction text not updated, flagged in its own 9/28 Notes) | 50% | 2026-11-15 · same | **RESOLVED-INVALIDATED** | 2026-10-19 | "INVALIDATED: Q3 company-reported NCO 0.30%=30bps <=40bps; 45.8M net=48.0M gross-2.2M recoveries, EX99.1 acc 0001628280-26-066286 ... (10-Q-confirm pending: 10-Q frame §2 precedence)". **The Q3 10-Q can still flip it** (only if its ratio or fraud attribution differs at printed precision; logged as a dated CORRECTION). |
| REG-15 (:9) | "WAL hidden CRE ratio (Memo3/C&I) exceeds 30%" | 60% | 2026-08-31 (filled retrospectively 8/28) · SCHEDULED-FILING | RESOLVED-FAILED | 2026-08-20 | MI3 21.20% at 6/30/2026 on the legacy ÷item-4 basis. Closed; nothing pending. |

**Past due:** none as of 2026-10-30 (WAL-01 due 11/15, 16 days out; guard output in §4).
**Rows that resolve on the Q3 10-Q:** WAL-01 (final grade) and WAL-02 (confirm or correct).
**Has the Q3 10-Q been filed?** **Not as of 2026-10-28 ~22:40 ET** per the desk's own surfaces: `STATUS.md:15` ("Not on EDGAR at ~22:40 ET 10/28: issuer filings since 9/24 are only the 10/19 8-K and ten 10/19 Form 4s. Statutory Mon 11/9; ledger Resolve_By 11/15"; receipt `sources/edgar_sweep_2026-10-28/SWEEP_RECEIPT.md`; KB-WAL-259 Stale_By 2026-11-09). **After 10/28 22:40 ET: UNKNOWN** — no desk surface is newer, the 10/29 inbound packets (REGINALD, TERRY, WALTER SIG-W-20261029-020 on Carvana) do not mention a WAL 10-Q, and this reader did no web check (none was asked for). The desk's `scripts/boot.py` performs the EDGAR check at its next boot.
**Forward predictions:** none. No row has been made since 2026-04-24 (REG-15 was a transfer). When WAL-01 closes, the ledger has **zero OPEN rows**; `Q3_10Q_RESCORE_RULE_2026-10-22.md:54` says forward Q4 predictions are registered in the 10-Q session. This was already a FLEET_MAP gap on 10/22 ("no forward predictions after WAL-01") and is still open.
**Ledger hygiene inside the rows:** WAL-02 Outcome "9M LAM 126.4/Cantor 26.1" — checked, not heredoc residue: the 10/19 grade report (`research/2026-10-19_Q3_STAGE1_GRADE.md:24`) reads "The nine-month LAM126.4/Cantor26.1 adjustments", so "9M" = nine-month. Ambiguous to a cold reader on a ledger that has had two `$`-expansion repairs (REG-15 9/28, KB-173..177 9/24), but not a defect.

---

## 2. Invalidation-surface inventory now (baseline = profile §3, vintage 2026-08-07)

"Mech?" names the mechanical reader if any. Kinds per PAT-077 as in the old profile.

| Surface | Kills / flips what | Dated stamp (in-content) | State 2026-10-30 | Graded by / mechanical reader | Changed since 8/07? |
|---|---|---|---|---|---|
| `STATUS.md` §EXIT RULES (`:88-99`), 6 rows | the thesis and its legs | **`Kill rail re-derived: 2026-10-22`** (`STATUS.md:90`, "Re-checked 10/28: no carrier has landed since, no state changed") | see the six rows below | WAL by hand; **no mechanical reader** — `falsification_scan.py --agent WAL --tsv` (run 12:3x today, rc 0) sees only `CHANGELOG.md` (CURRENT, stamp 10/22, v2.4 = live); STATUS-embedded rails are outside its SURFACE_PATTERNS | **YES** — stamp added (FLEET_MAP 10/22 had "EXIT RULES lack a dated re-derivation stamp (L3 leg AT RISK)"); Time-box row gone (dissolved 8/7); Price-discipline row replaced by two gate rows |
| ↳ Bear-medium KILL (`:94`) | Bear-medium 16% | 10/22 | **NOT FIRED**: leg (a) 0 new office migrations MET at Q3 (DP2 final 10/21); leg (b) benign $99M appraisal PENDING-10-Q | 10-Q frame §4 letter C; weight consequence pre-registered in RESCORE §2 | leg (a) newly MET (Q3) |
| ↳ Bear-fast KILL (`:95`) | Bear-fast | 10/22 | **FIRED 8/7**, in v2.4 (10%→2%); "Q3 untested" | FFIEC MI3 (`MI3_SERIES.tsv`); next carrier Q3 Call Report (due 10/30, not filed at 10/28) | no state change; v2.4 executed 8/20 |
| ↳ Bear CONFIRM (`:96`) | bear upgrade | 10/22 | **NOT FIRED**: WAL-01 provisionally invalid, WAL-02 invalid (10-Q confirm pending) | PREDICTIONS WAL-01/02 | **NEW form**: carriers are now the two ledger rows. After the 10-Q its only live path (a WAL-02 10-Q flip >40bps) closes, so the rule will have **no future carrier** — see finding O3 |
| ↳ Thesis RETIRE (`:97`) | the thesis | 10/22 | **NOT FIRED**: broadening counter 2 of 3; coverage leg MET 118.43% (574.4/485); appraisal PENDING-10-Q | print frame §7 basis pin (funded+unfunded ACL ÷ nonaccrual); 10-Q frame §5 confirms | counter 1→2 (Q3); coverage leg MET (was 96%) |
| ↳ GATE-REG-T02 (`:98`) | PROME gate, close < 78 | — | **TERMINAL** since 9/1 | PROME | new row since 8/07 |
| ↳ Robinhood exit guard (`:99`) | GATE-TERRY-ROLL70-EXIT (≥81.90 × 3 official closes) | 10/27 owner log | FIRED, run 0 of 3 (REGINALD grades; WAL claims no count) | REGINALD / `PROME/GATES.tsv:16` | new row since 8/07 |
| `workbook/PREDICTIONS.tsv` Invalidation column | WAL-01, WAL-02 | re-spec 2026-08-20 (P2/P3, Will-ruled 8/12) | WAL-01 OPEN-provisional; WAL-02 RESOLVED-INVALIDATED; REG-15 RESOLVED-FAILED | `predictions_due_check.py` (Resolve_By, verified both directions §4) | **YES** — 8/07 "resolvability DEGRADED" and "invalidation FORMALLY UNSATISFIABLE" both repaired 8/20; WAL-02 resolved 10/19 |
| `Q3_PRINT_GRADING_FRAME_2026-09-24.md` | WAL-01/02 Stage-1; migration N=2; guide; $99M letter; mgmt 9/16 benchmark; non-credit falsifier | registered 2026-09-24 (`52304eeae`); §10 rules 9/28 (WQ-325, Will); print date pinned 10/9 | **DISCHARGED** (Stage 1 graded 10/19, Stage 2 10/21) | WAL; reports `research/2026-10-19_Q3_STAGE1_GRADE.md`, `research/2026-10-21_Q3_STAGE2_CALL_GRADE.md` | **NEW** since 8/07 |
| `Q3_10Q_GRADING_FRAME_2026-09-24.md` | WAL-01 final; WAL-02 confirm/correct; $99M disposition; Cantor tie-out; RETIRE coverage leg; NDFI 25.9% test; OREO; hotel O1–O8 | registered 2026-09-24 (`6c488c239`); **FROZEN 2026-10-22** (`d00afcc78`, §8 freeze note `:112-113`) | **ARMED, awaiting filing** (EDGAR ≥ Mon 10/26; statutory Mon 11/9) | WAL at filing; DOCKET L171 | **NEW** since 8/07 (replaces the VOID Q2-10-Q frame class) |
| `Q3_10Q_RESCORE_RULE_2026-10-22.md` | maps 10-Q outcomes to weight changes (Bear-medium, Tail) | registered 2026-10-22 (`1d4d4210a`); **Will-approved 12:37 ET** (`a5c98e8d3`, §6 `:59`); amendment window open until the 10-Q appears on EDGAR | ARMED | applied by WAL in the 10-Q session as a versioned THESIS/SCENARIOS/CHANGELOG edit | **NEW** (closes the 10/22 FLEET_MAP gap "post-Q3 thesis weights undated with no pre-registered 10-Q mapping"). Gap: no row for a below-book appraisal with no or undisclosed reserve (finding O1) |
| `THESIS.md` v2.1 MI3 calibration table (`:290-297`, "IMPLICATION COLUMN RETIRED 2026-08-20 (P9)") | V1a band | frozen; P9 retirement 8/20 | Status column live (graded `<24%` "V1 plateaued"); Implication column retired, preserved struck | `MI3_SERIES.tsv` Band_v21_calibration column | **YES** — 8/07 "proposed for retirement (P9)" → RETIRED 8/20 |
| `workbook/MI3_SERIES.tsv` | Bear-fast (MI3 <25%) | `Last real data refresh: 2026-08-07`; `Last attention check: 2026-10-28` | 12 quarters, last 2026-06-30 = 21.20%; Q3 row owed (Call Report due 10/30, FFIEC JWT expires 11/5) | `ledger_staleness.py` (held, +83d) | attention line added 10/28; no data since 8/07 |
| `Q2_GRADING_FRAME_2026-07-21.md` | Q2 legs | 🧊 frozen | DISCHARGED | — | unchanged (last commit 7/25 path-only) |
| Q2 10-Q pre-registration frame | — | — | ⛔ VOID / never written (record unchanged) | — | unchanged |
| PROPOSED v2.3.1 condition | — | — | **REJECTED + RETIRED 2026-08-20 (P4, Will-ruled 8/12)** (`STATUS_ARCHIVE.md:298`) | — | **YES** (was "DOES-NOT-FIRE, UNRATIFIED" 8/07) |
| Bear-fast time-box (~Sep 1) | — | — | dissolved 8/7; no longer listed in EXIT RULES | — | removed from live table |
| `EARNINGS_PREP.md` | Q1 pre-print record | 🧊 FROZEN CALIBRATION RECORD rider applied 2026-09-02 (`41d04d943`, `:2-3`) | frozen, cite as history | — | rider added (resolves the 8/23 two-classification defect) |
| `workbook/RETIRED_CLAIMS.tsv` (40 rows) | dead claims that must not revive on live surfaces | newest row 2026-10-28 | live | `derived_drift_check.py` CHECK 2 | grew from ~0 at 8/07 (born 8/20) to 40 rows |

**What grades WAL-01/02 next:** the Q3 10-Q, read in the frozen 10-Q frame's order (§6: subsequent events first), then the re-score rule applied verbatim.

---

## 3. Frame integrity (git history of each frozen frame)

Method: `git log --follow` on each file; for the two Q3 frames, `git diff -U0 <registration commit> HEAD` and compare every hunk's start line with the line where the dated-annotation section begins in the registered version.

| Frame | Registered | Freeze rule | Commits after registration | Body (§0–§7/§8) edited after registration? | Edited after its event? |
|---|---|---|---|---|---|
| `Q3_PRINT_GRADING_FRAME_2026-09-24.md` | `52304eeae` 2026-09-24 00:30 | "Post-print edits are forbidden" (`:7`) | 7 (9/24 ×2, 9/28 ×4, 10/09 ×1); last `7cedffe74` 2026-10-09 10:05 | **No.** One hunk only: `@@ -108,0 +109,91` — pure insertion after line 108; §9 starts at line 106 in the registered version. §10 (9/28) is a Will-authorized dated addition (WQ-325), §10.4 amends §10.1/§10.2 before first use, struck-not-deleted | **No.** Print 2026-10-19 AMC; last edit 10/09 |
| `Q3_10Q_GRADING_FRAME_2026-09-24.md` | `6c488c239` 2026-09-24 00:47 | "no edits after the filing"; FROZEN for grading 10/22, after which §8 "takes only filing-clock pins and reader notes; no cell edits" (`:113`) | 10 (9/24 ×2, 9/27 ×2, 9/28 ×3, 10/09 ×2, 10/22 ×1); last `d00afcc78` 2026-10-22 11:12 | **No.** One hunk: `@@ -91,0 +92,31` — insertion after line 91; §8 starts at line 88 | **No** (no filing yet; no commit since the freeze) |
| `Q3_10Q_RESCORE_RULE_2026-10-22.md` | `1d4d4210a` 2026-10-22 12:30 | amendments only as dated §6 notes until the 10-Q is on EDGAR | 1: `a5c98e8d3` 12:38 adds one §6 line (Will's approval). Verified `git diff 1d4d4210a a5c98e8d3`: single `+` line at §6 | **No** | **No** |
| `EARNINGS_PREP.md` | 2026-03/04 (REGINALD era) | 🧊 path fixes only | 2026-08-20 `c975af77e` (banner de-versioned), 2026-09-02 `41d04d943` (+2 banner lines = the rider) | banner lines only (checked: the 8/20 diff touches line 1 only; the 9/02 diff is 2 insertions) | n/a |
| `Q2_GRADING_FRAME_2026-07-21.md` | `08d4dd131` 2026-07-10 | 🧊 | last `77f0c0e42` 2026-07-25 (WP-W3 path rewrite) | path-only per the commit subject | not re-read this pass |

**Caveat on "annotations only":** both Q3 frames' annotation sections carry rule content, not just notes. The 10-Q frame's 9/28 ~16:3x note restates the effective Cantor rule with a WAL-derived net-basis line ("NET-of-allowance figure confirms if < $66.5M — this numeric translation of '~$70M' to the net basis is WAL's reading, flagged to PROME in the receipt") and re-reads §5's V3 ACTION text against the 9/28 re-score. These are permitted pre-filing, dated and disclosed, but a grader who reads only §1–§7 will grade differently from one who reads §8. Frozen ≠ "read only the body".

---

## 4. Guards run in both directions (rc read bare: `out=$(cmd); rc=$?`, never through a pipe)

Fixtures: `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-DAEDALUS/0c20d72d-8077-4bfe-bef2-ef05a9591275/scratchpad/walfix/` (copies of two scripts + a doctored PREDICTIONS/KB) and `.../scratchpad/walroot/` (a tar copy of `AGENTS/WAL` without `sources/`, `inbox/`, `__pycache__`, run with `python3 -B`). Nothing under the repo was written; `__pycache__` mtimes unchanged (10/14, 10/22).

| Guard (boot step) | Case | Command | Printed (key line) | rc |
|---|---|---|---|---:|
| `predictions_due_check.py` (4d) | clean, real data | default | "open rows checked: 1 closed (skipped): 2 · 🟢 WAL-01 due 2026-11-15 in 16d (open 189d) · ✓ every open prediction carries a Resolve_By and none is past it" | 0 |
| | clean, boot form | `--quiet` | **(prints nothing)** | 0 |
| | clean, strict | `--strict` | — | 0 |
| | alert, real data | `--asof 2026-11-16` | "🔴 WAL-01 due 2026-11-15 OVERDUE 1d (open 206d)" + LOOK-not-grade advice | 0 |
| | alert, strict quiet | `--asof 2026-11-16 --strict --quiet` | "⚠️ predictions due: 1 OVERDUE (worst WAL-01 by 1d) — LOOK, do not force a grade" | **1** |
| | alert, blank fixture (WAL-01 Resolve_By emptied) | default; `--strict --quiet` | "🟠 WAL-01 NO Resolve_By — cannot be evaluated, and a blank is not a pass"; quiet: "1 with NO Resolve_By" | 0; **1** |
| | CLOSED set | (code read) | `RESOLVED-INVALIDATED` is in CLOSED (`:43`) — the 10/22 DAEDALUS finding 3 is fixed; WAL-02 correctly skipped | — |
| `kb_expiry_check.py` (4b) | alert, real data | default | "ACTIVE rows: 184 · past their own expiry: 8 ⚠️ (4%) · awaiting a filing: 0 · Stale_By blank: 0 · still in date: 176"; oldest: KB-WAL-092/093/095/102/194/196/251 (2026-10-28, 2d) and 227 (2026-10-29, 1d) | 0 (advisory by design) |
| | alert, boot form | `--quiet` | "⚠️ KB expiry: 8/184 ACTIVE rows past their own Stale_By (oldest 2d) — re-verify, mark SUPERSEDED, or extend WITH A REASON" | 0 |
| | clean fixture (the 8 rows removed) | `--kb <fixture>` | "past their own expiry: 0 ✓ (0%) · still in date: 176" | 0 |
| | clean fixture, boot form | `--kb <fixture> --quiet` | **(prints nothing)** | 0 |
| `maintenance_state_check.py` (inside 4c) | alert, real tree | default | "Named current-field issues: 2; new historical-pattern identities: 0; cleared reviewed identities: 10." CHECK inbox-WALTER "1 unrowed: SIG-W-20261029-020"; CHECK inbox-unprocessed "3 packet(s)" (PROME 10/28, REGINALD 10/29, TERRY 10/29) | 0 |
| | alert, strict | `--strict` | same | **1** |
| | clean (copy, empty inbox lanes) | `--root walroot --strict` | "Named current-field issues: 0; new historical-pattern identities: 0; cleared reviewed identities: 10." | 0 |
| | alert, seeded KB_INDEX drift (NDFI 6→7) | `--root walroot --strict` | "CHECK KB-group NDFI count/IDs disagree" | **1** |
| | alert, seeded revived claim ("The current thesis is v2.2 and PT $50-68 now." appended to the copy's NEXUS_BRIEF) | `--root walroot --strict` | "new historical-pattern identities: 2" + two bare `NEW <sha256>` lines | **1** (0 without `--strict`) |
| | unit tests | `python3 -B -m unittest test_maintenance_state_check` | "Ran 10 tests ... OK" | 0 |
| `derived_drift_check.py` (4c) | alert, real tree, boot form | `--quiet` | "CHECK: 2 named-field issues / 0 new claim identities; totals 14/63" + the two inbox issues | 0 (always) |
| | real tree, full | default | "canonical: v2.4 · EV $75.96 · PT $52-76 (… 74 files) · CHECK 1 — stale version/EV/PT tokens: 14 · CHECK 2 — retired claims found alive: 63" (all reviewed history in `DRIFT_HISTORY_2026-10-14.json`) | 0 |
| | clean copy | `--root walroot --quiet` | "Selected checks pass: no new identities or named-field disagreements; 14/63 reviewed-pattern hits, 10 cleared." | 0 |
| | seeded revived claim | `--root walroot --quiet` | "CHECK: 0 named-field issues / 2 new claim identities; totals 16/63" | 0 (always) |
| `scripts/corrections_boot_check.py WAL` (root) | real | default | "CORRECTIONS-CHECK 0 OK: 0 unreceipted NAMED rows for WAL (register 110 row(s) … receipts on file: 3)"; INFO COR-20260925-13 ALL-row dead-at-cap | 0 |
| `falsification_scan.py --agent WAL --tsv` (DAEDALUS) | real | — | one row: `CHANGELOG.md` CURRENT, stamp 2026-10-22, v2.4 = live. No other WAL surface matched | 0 |

**Guard observations:**
- All four desk guards fire on a capable case and print a clean line in their full form. **In the boot form (`--quiet`, CLAUDE.md:53, :63) two of the four print nothing when clean** (predictions_due, kb_expiry). A boot transcript cannot tell "ran clean" from "did not run". The CHECK_STANDARD §3 clean-line rule (`BLUEPRINTS/CHECK_STANDARD.md:29,33`) is met only by the non-quiet form.
- `derived_drift_check.py` exits 0 on every outcome, by design. Its boot form therefore never blocks; only `maintenance_state_check.py --strict` turns a new identity into rc 1, and `--strict` is not in the charter's boot lines (CLAUDE.md:58 runs `derived_drift_check.py --quiet`).
- `maintenance_state_check.py` reports new claim identities as bare SHA-256 hashes with no path or line; locating them needs a second run of `derived_drift_check.py` without `--quiet`.
- `DRIFT_HISTORY_2026-10-14.json` `review_by` = **2026-11-09**. From 11/10 both drift guards add a `history-review` issue. That is the statutory 10-Q date, so the 10-Q session and the baseline expiry coincide.
- **KB expiry boundary:** the 8 rows now expired carried Stale_By 2026-10-28/29 in the commit before the 10/28 "KB expiry review" (`4e713d7c1^`) and still do at HEAD. The check uses strict `d < today`, so on review day 10/28 these rows read in date and the session never judged them; they expired the next day. Rows expiring on the review day fall through.

---

## 5. Ledger hygiene (root CLAUDE.md § Data Hygiene: LIVE-with-two-clock or FROZEN-bannered, never the silent middle)

`ledger_staleness.py` was run from repo root with the charter's own forms (CLAUDE.md:48-49). The `--agent` flag does not exist; the form is a positional `WAL`. No `workbook/LEDGER_GLOB` file exists, so the default `workbook/*.tsv` perimeter applies.

| Ledger | Bytes | Header state | Data clock / other clocks | Rows | `tsv_append --check` | ledger_staleness verdict |
|---|---:|---|---|---:|---|---|
| workbook/KB.tsv | 293,696 | **LIVE two-clock** (lines 1–4; header row line 5) | `Last real data refresh: 2026-10-28` · `Staleness sweep (no data): 2026-10-28` · three `Historical data refresh` lines (10/22, 10/21, 10/14, 10/13…) kept as history | 270 (184 ACTIVE / 86 SUPERSEDED; 0 duplicate IDs, 001–270 contiguous; 0 ACTIVE rows with blank Stale_By; 8 SUPERSEDED rows with blank Stale_By, which the checker skips) | rc 0, 13 cols | ok +1d |
| workbook/PREDICTIONS.tsv | 23,504 | **LIVE two-clock** (lines 1–5) | `Last real data refresh: 2026-10-19` · `Historical data refresh: 2026-08-20` · `Staleness sweep (no data): 2026-09-28` | 3 | rc 0, 11 cols | ok +10d; `--abs-floor --abs-days 7`: "⚠️ UNATT +10d [attention 33d via 'Staleness sweep'] abs 12d" (rc 1) |
| workbook/MI3_SERIES.tsv | 2,892 | **LIVE two-clock + attention** (lines 1–4) | `Last real data refresh: 2026-08-07` · `Staleness sweep (no data): 2026-08-07` · `Next real data: Q3-2026 Call Report ~Oct-Nov 2026` · `Last attention check: 2026-10-28` (FFIEC filer list lacks RSSD 3138146; due 10/30; JWT expires 11/5) | 12 | rc 0, 11 cols | **held +83d [attention 3d]** — counted stale; drives rc 1 on every form |
| workbook/RETIRED_CLAIMS.tsv | 14,027 | **neither**: 5 `#` lines of purpose/usage, no clock | git-time fallback | 40 | rc 0, 5 cols | ok +0d (git time) |
| workbook/KB_INDEX.md | 2,375 | generated navigation, not a TSV | header "270 rows / 20 groups, Inventory updated October 28" | — | — | not scanned. Group counts and IDs verified against KB by `maintenance_state_check` (clean, and fires on seeded drift) |
| registry/corrections_receipts.tsv | 166 | neither (append-only receipts) | — | 3 (COR-20260915-02 NO-OP; COR-20260927-05/-06 APPLIED, all 9/24–9/27) | rc 0, 4 cols | not scanned (perimeter line names it) |
| *(outside cluster)* board_log.tsv | 7,531 | neither | — | 15 | rc 0, 5 cols | not scanned (top-level TSV) |

Line endings: all four workbook TSVs are LF (`file`: "UTF-8 text"); no CRLF risk.

**ledger_staleness results:**

| Invocation | rc | Result |
|---|---:|---|
| `ledger_staleness.py WAL` | **1** | KB ok +1d · MI3_SERIES held +83d · PREDICTIONS ok +10d · RETIRED_CLAIMS ok +0d · "→ 1 stale: freeze … or refresh at closeout." Perimeter: "4 ledger(s) scanned; 6 TSV(s) NOT scanned: registry/corrections_receipts.tsv, reports/2026-10-22_READS.proposed.tsv, research/2026-10-14_FFIEC-metrics.tsv, research/2026-10-14_FFIEC-selected-fields.tsv (+2 more)" (the +2 = research/2026-10-14 and 2026-10-19 `Q3-evidence-worksheet.tsv`) |
| `WAL --quiet` (charter boot form) | **1** | "⚠️ [WAL] 1 stale ledger(s) behind STATUS: MI3_SERIES.tsv (+83d behind, held (attention 3d))" + perimeter line |
| `WAL --trade --quiet` | 0 | "1 agent(s) with a matching trade surface graded; 0 … NOT certified"; full form: `POSITIONS.md` ok +6d |
| `WAL --writes` | 1 | same verdicts; writes-behind 0w / 4w / 6w / 0w |
| `WAL --abs-floor --abs-days 7` | 1 | 2 stale: MI3_SERIES (abs 85d) and PREDICTIONS (UNATT, abs 12d) |
| `--selftest` | 0 | "LEDGER-STALENESS SELFTEST ✓ 40/40 cases behaved" |

**Verdict:** the three data ledgers are LIVE with content-derived two-clock headers. None is in the silent middle. MI3_SERIES is LIVE-but-behind by design: its data source has not published, and the 10/28 attention line records the check. It will read rc 1 at every boot until the Q3 Call Report row lands. RETIRED_CLAIMS has no clock header; it is a registry, and git time is an acceptable proxy, but strictly it is neither state the rule names.
**Old-profile hygiene flag resolved:** 8/07's "🔴 KB_INDEX 25 rows stale … the tree's ONLY silent-middle surface" is fixed. KB_INDEX now reads 270/20, matching KB, and a guard (`maintenance_state_check`, KB-group leg) enforces it.

---

## 6. Ranked findings

### 🔴 O1 — The re-score rule and the 10-Q frame have no outcome row for a below-book $99M appraisal with zero or undisclosed reserve. The literal letter files it as **B**, which trims the bear. The only window to fix it closes when the 10-Q reaches EDGAR.
- Print frame §10.1/§10.4(b) (`Q3_PRINT_GRADING_FRAME_2026-09-24.md:126-133, 187-194`) defines **B′₀** (below carrying, reserve explicitly zero) and **B′ᵤ** (below carrying, reserve undisclosed → "PENDING the 10-Q (10-Q frame §4)"). Both are "adverse evidence: KILL leg (b) is not satisfied, and each counts as a C (credit) breach".
- The 10-Q frame §4 letter table (`Q3_10Q_GRADING_FRAME_2026-09-24.md:42-58`) has only A, A′ (below carrying **with** a specific reserve, `:55`), B ("still nonaccrual, no charge-off", `:56`), C (`:57`) and "Nothing anywhere" (`:58`). `grep "B′\|B'"` returns 0 hits in the 10-Q frame and in the re-score rule.
- `Q3_10Q_RESCORE_RULE_2026-10-22.md:21-27` maps only C / B / NO-VERDICT / A′ / A. A 10-Q that discloses a below-book appraisal with no reserve satisfies B's literal text, so it maps to **Bear-medium 16 → 12, EV $76.60**. That is a bear trim on evidence the print frame calls adverse. The error runs toward all-clear.
- The 10-Q frame is frozen (no cell edits after 10/22, `:113`). The re-score rule's amendment window is open "only until the 10-Q appears on EDGAR" (`:5`, `:59`): EDGAR ≥ Mon 10/26, statutory Mon 11/9. **Owner action, Will-gated:** a dated §6 amendment adding B′₀/B′ᵤ rows (or an explicit statement that B′ maps to the A′ row), before the filing. Route: WAL → Will via PROME.

### 🟠 O2 — WAL's live kill rail has no mechanical reader. The fleet scan certifies WAL off a proxy.
- The rail lives in `STATUS.md:88-99` with stamp `Kill rail re-derived: 2026-10-22` (`:90`). `falsification_scan.py --agent WAL --tsv` returns one row, `CHANGELOG.md` CURRENT (stamp 10/22, v2.4 = live). STATUS-embedded rails are outside its SURFACE_PATTERNS, and the in-thesis rail detection reads only THESIS.md's head.
- So the scan reads CURRENT for WAL whatever happens to the STATUS stamp. The 10/22 FLEET_MAP gap ("EXIT RULES lack a dated re-derivation stamp (L3 leg AT RISK)") is **fixed in content** (the stamp exists and is dated), but no instrument would notice it going stale. Profile §3b should record the mechanical reader as "none (hand only); falsification_scan sees CHANGELOG only".

### 🟠 O3 — After the 10-Q the ledger and one exit rule run out of carriers.
- PREDICTIONS has 1 OPEN row (WAL-01). No new prediction since 2026-04-24, six months (REG-15 was a transfer). When WAL-01 closes, the ledger has 0 OPEN rows. `Q3_10Q_RESCORE_RULE_2026-10-22.md:54` promises Q4 rows "in the 10-Q session after WAL-01 closes" — a promise, not a registered row. This was a FLEET_MAP gap on 10/22 and is still open.
- `STATUS.md:96` Bear CONFIRM = "WAL-01 Office > 500 or WAL-02 NCO > 40". WAL-01 can no longer confirm: the 10-Q only passes, voids or leaves unrun the cross-check, never flips to CONFIRMED. WAL-02's only remaining path is a 10-Q correction >40bps. After the filing the rule has **no future carrier** and needs a dated re-derivation or retirement, or it becomes an unfireable row that reads NOT FIRED forever.

### 🟠 O4 — 8 ACTIVE KB rows are past their own Stale_By, and the expiry review missed them by the boundary.
- `kb_expiry_check.py`: 8/184 (KB-WAL-092, 093, 095, 102, 194, 196, 251 on 2026-10-28; 227 on 2026-10-29). Two are load-bearing: KB-194 is management's 9/16 Q3 pre-guide (the print frame §6 benchmark) and KB-227 is the Ontario FDIC-R stay.
- These dates are identical at `4e713d7c1^` and at HEAD, so the 10/28 "KB expiry review" (STATUS:3) saw them as in date (strict `d < today`) and never judged them. A review should treat "expires today" as due.

### 🟠 O5 — Two of the four boot-line guards are silent when clean, and the drift guard can never block at boot.
- `predictions_due_check.py --quiet` and `kb_expiry_check.py --quiet` (CLAUDE.md:53, :63) print nothing on a clean case (watched above). That fails the CHECK_STANDARD §3(b) clean-line contract in the form the desk actually runs. A boot log cannot show they ran.
- `derived_drift_check.py` exits 0 always. The only rc-1 path for new drift identities is `maintenance_state_check.py --strict`, which is not a charter boot line. Detection works (verified on a seeded case); enforcement at boot is advisory only.

### 🟡 Minor
- **Y1 — `$`-expansion residue on a fresh RETIRED_CLAIMS row.** `workbook/RETIRED_CLAIMS.tsv:46` (died 2026-10-28) replacement reads "Nevada commercial HFI **.0B of 4.3B** (4.5%)". KB-WAL-270 gives Nevada $2.0B of $44.3B, so this is "$2.0B of $44.3B" with `$2`/`$4` expanded away. Introduced `4e713d7c1` 2026-10-28 23:28. Same class as the 9/24 and 9/28 repairs (`finding_unquoted_heredoc_expands_dollar_figures`).
- **Y2 — glued words in ledger cells**, contrary to the root Output Canon: `RETIRED_CLAIMS.tsv:40-41` ("Charter mirrored oneleg after Fidelity65P addition", "October7acquisitionverified, grossfillprice/cardunknown"), `:39` ("Ontario B1 docket-evidenced atOctober2; otherthreeU"). The KB header lines also carry "KB254-257", "September30", "Doc100".
- **Y3 — a "live" replacement value that has gone stale:** `RETIRED_CLAIMS.tsv:24` replacement "187 rows / 20 distinct Group values (live; STATUS.md owns it)". KB is 270 rows. The cell asserts "live".
- **Y4 — `maintenance_state_check.py` prints new identities as bare SHA-256 hashes** (no path or line). The reader must re-run `derived_drift_check.py` without `--quiet` to find them.
- **Y5 — the drift baseline expires on the 10-Q deadline:** `DRIFT_HISTORY_2026-10-14.json` `review_by` = 2026-11-09. From 11/10 both drift guards add a `history-review` issue, landing on the same session as the 10-Q grade.
- **Y6 — WAL-02 Prediction/Timeframe text still reads "Q2 or Q3"** (`PREDICTIONS.tsv:8`). Documented in its own 9/28 Notes; the Invalidation cell governs. Cosmetic.
- **Y7 — MI3_SERIES makes `ledger_staleness WAL --quiet` rc 1 at every boot** until the Q3 Call Report lands (due 10/30; FFIEC JWT expires 11/5, the same week). Expected, but it is the boot's standing alert. If the JWT lapses before the pull, it stays red.
- **Y8 — DAEDALUS-side, not WAL's:** `FLEET_DIRECTORY.md:46` describes WAL as "thesis-of-record v2.3". v2.4 has been current since 2026-08-20. The FLEET_MAP row (Last_scored 2026-10-22) lists gaps that are now closed: the re-score rule exists, the kill-rail stamp exists, the CLOSED set includes RESOLVED-INVALIDATED (`predictions_due_check.py:43`), STATUS has a BOTTOM LINE (`STATUS.md:7`), and the inbox/WALTER lane is checked by `maintenance_state_check`. Only "no forward predictions after WAL-01" remains from my cluster's share. The re-cut should drop the closed ones.
- **Y9 — frame annotations carry rule content** (§3 caveat): a 10-Q grader must read §8, not only §1–§7.

### Clean results worth recording (positive controls)
- Both Q3 frames' registered bodies are byte-unedited since registration; no frame was edited after its event (§3).
- PREDICTIONS: every row carries Resolve_By, the CLOSED set is correct, and the guard fires both ways including the blank class.
- KB: 270 rows, contiguous IDs, 0 duplicates, 0 ACTIVE blank Stale_By (8/07 had 41), all rows 13 columns.
- corrections: 0 unreceipted NAMED rows.

---

## 7. Old-profile reconciliation (profile `WAL.md`, vintage 2026-08-07; my cluster's claims only)

| Old-profile claim | Now | Source |
|---|---|---|
| "PREDICTIONS.tsv 2 rows, REGINALD 10-col schema" | 3 rows, **11 cols** (Resolve_By added 8/28); REG-15 transferred and graded 8/20 | PREDICTIONS.tsv:6-9 |
| WAL-01 "resolvability DEGRADED", "Schedule O VOID" | re-instrumented 8/20 to the deck slide + 10-Q cross-check; provisionally INVALIDATED 10/19 at $272.75M | PREDICTIONS.tsv:7 |
| WAL-02 "invalidation clause FORMALLY UNSATISFIABLE" | repaired 8/20 (exhaustive >40/≤40, Q3-only); RESOLVED-INVALIDATED 10/19 at 30bps | PREDICTIONS.tsv:8 |
| "KB.tsv 170 rows/16 groups" | 270 rows / 20 groups | KB.tsv; KB_INDEX.md |
| "🔴 KB_INDEX 25 rows stale … the tree's ONLY silent-middle surface" | **fixed** and guarded | KB_INDEX.md:3; maintenance_state_check |
| "Absent: scripts/, boot.py, CALENDAR …" | `scripts/` now holds 4 ledger guards + boot.py (10/28) + tests; CALENDAR still absent (the THESIS correction at `:299` records that the claimed CALENDAR row never existed) | scripts/; THESIS.md |
| v2.1 MI3 table "Implication column proposed for retirement (P9)" | RETIRED 8/20, preserved struck | THESIS.md:290-297 |
| "PROPOSED v2.3.1 condition … UNRATIFIED" | REJECTED + RETIRED 8/20 (P4) | STATUS_ARCHIVE.md:298 |
| Exit rules (6): Bear-medium ⬜, Bear-fast ✅ FIRED, Time-box ✅ DISSOLVED, Bear CONFIRM ⬜, RETIRE ⬜ 1-of-3, Price discipline 🟢 | 6 rows, different set: Bear-medium NOT FIRED (leg a MET), Bear-fast FIRED, Bear CONFIRM NOT FIRED, RETIRE NOT FIRED **2 of 3** + coverage MET, GATE-REG-T02 TERMINAL, Robinhood guard (REGINALD-graded). Time-box and Price discipline gone. **Dated stamp 10/22** | STATUS.md:88-99 |
| "Q2-10-Q pre-registration frame … VOID" | still VOID (record); the Q3 10-Q frame was registered 30 days early and frozen 10/22, so the class did not repeat | Q3_10Q frame :3, :113 |
| EARNINGS_PREP 🧊 frozen-by-design | rider applied 9/02; FROZEN wins over STALE-VINTAGE; content unedited | EARNINGS_PREP.md:1-3 |
| FLEET_MAP 8/07 re-cut gate (a) "Q3 frames written before 10/13 print + 10/24 10-Q" | **MET**: print frame 9/24 (25 days before the actual print), 10-Q frame 9/24 (30+ days early) | git log |
| gate (c) "boot.py first increment built + wired" | built + wired 10/28 (`03125d44c`; not in my cluster to verify) | git log |

---

## 8. Coverage (exact ranges read; `wc -c`/`wc -l` at 12:27 EDT)

| File | Size | Read | Not read |
|---|---|---|---|
| `AGENTS/DAEDALUS/profiles/WAL.md` | 12,010 B | **whole** (one `cat`) | — |
| `AGENTS/DAEDALUS/profiles/HOMER.md` | 13,501 B | headings + lines 42–64 (§3, §3b), cells cut at 900 chars | §1–2, §4–7 |
| `AGENTS/DAEDALUS/runs/2026-10-28_HOMER_REFRESH_READERS/R2_LEDGERS_GUARDS.md` | — | bytes 1–6,000 + heading list | rest (skim only, as instructed) |
| `AGENTS/WAL/THESIS.md` | 61,921 B / 481 lines | **whole**, 3 chunks: bytes 1–21,000 · 21,001–42,000 · 42,001–61,921 (final line = the v2.2 footer, observed) | — |
| `workbook/PREDICTIONS.tsv` | 23,504 B | **whole**: bytes 1–12,000 + 12,001–end; plus a parsed per-row field dump | — |
| `workbook/RETIRED_CLAIMS.tsv` | 14,027 B / 47 lines | all 47 lines with each line cut at 700 chars; the two longer lines (24: 797, 30: 716 chars) read to end separately for line 24; **line 30 chars 701–716 not read** | line 30 tail (16 chars) |
| `workbook/MI3_SERIES.tsv` | 2,892 B | **whole** | — |
| `workbook/KB_INDEX.md` | 2,375 B | **whole** | — |
| `workbook/KB.tsv` | 293,696 B / 275 lines | header lines 1–5 (each cut at 2,500 chars, so the long line-4 clock history is truncated); sample rows KB-WAL-001, 100, 150, 230, 259, 270 (selected fields, cut 160 chars); the 8 expired rows' Status/Stale_By/Notes tail; KB-WAL-270 Fact. **Scripted whole-file counts** (status, column counts, Stale_By, IDs) | **not read whole** — about 262 rows' prose not read |
| `registry/corrections_receipts.tsv` | 166 B | **whole** | — |
| `Q3_10Q_GRADING_FRAME_2026-09-24.md` | 27,183 B / 122 lines | **whole**: bytes 1–13,600 + 13,601–end | — |
| `Q3_PRINT_GRADING_FRAME_2026-09-24.md` | 28,635 B / 199 lines | **whole**: bytes 1–14,500 + 14,501–end | — |
| `Q3_10Q_RESCORE_RULE_2026-10-22.md` | 6,656 B / 59 lines | **whole** (`cat -n`), EV arithmetic re-computed (77.60 / 76.60 / 75.96 / 75.32 all reproduce) | — |
| `EARNINGS_PREP.md` | 33,875 B / 360 lines | **whole**: bytes 1–17,000 + 17,001–end | — |
| `EARNINGS_PREP_BANNER_RIDER_2026-08-23.md` | 5,621 B | **whole** | — |
| `scripts/predictions_due_check.py` | 5,414 B | **whole** | — |
| `scripts/kb_expiry_check.py` | 5,643 B | **whole** | — |
| `scripts/derived_drift_check.py` | 12,708 B | **whole** | — |
| `scripts/maintenance_state_check.py` | 5,965 B | **whole** | — |
| Context reads outside the cluster | — | `STATUS.md` lines 1–40 (cut 400 chars) + 70–115 (cut 330/500) + heading list; `CLAUDE.md:44-66` + grep hits :48-63, :190-194; inbox listing + `SIG-W-20261029-020` first 1,500 B; `research/2026-10-19_Q3_STAGE1_GRADE.md:24` (grep); FLEET_MAP WAL row; `falsification_scan.py:38-50, 300-345` + grep; `CHECK_STANDARD.md` lines 29, 33; `DRIFT_HISTORY_2026-10-14.json` keys/review_by only; DOCKET L170/L171 (cut 400 chars); GATES grep | everything else |

**Not read at all (in or near the cluster):** `scripts/boot.py`, `test_boot.py` (R1's; boot.py was not run because it makes network calls), `scripts/test_maintenance_state_check.py` source (run, not read), `CHANGELOG.md`, `SCENARIOS.md`, `WEAKNESSES.md`, the Stage-1/Stage-2 grade reports beyond one grep line, `research/*worksheet.tsv`, `Q2_GRADING_FRAME_2026-07-21.md` body.
**No web/EDGAR check** was made, so the Q3 10-Q filing state after 2026-10-28 22:40 ET is UNKNOWN.

**Run end:** see the timestamp line below.
**Run end:** 2026-10-30 12:35 EDT
