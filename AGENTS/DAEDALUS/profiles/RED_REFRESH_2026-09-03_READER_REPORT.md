# RED profile refresh — Mode-A READER REPORT (2026-09-03)

**Reader:** DAEDALUS Mode-A profile reader (spawned by DAEDALUS lead) · **Measured:** 2026-09-03 ~21:1x EDT (`date`) at HEAD `658e6cd3b` (RED tip `9e55d4356`, 9/3 07:20 ET) · **Read-only** except this file. **Subject:** `AGENTS/RED/` (Utility class; FLEET_MAP row re-cut 2026-09-01 L5 conf M). **Prior profile:** `profiles/RED.md` body 2026-08-12 (STALE banner 9/1). Every claim below carries a file:line or a commit hash; numbers are measured today unless labelled otherwise.

**Headline corrections to the brief I was handed:** (1) **RED is NOT dark since 8/28** — six RED-authored commits 9/1–9/3 incl. two full closeouts (`b8e61d907` S39 9/2, `9e55d4356` S40 9/3). (2) **The registry is 18 columns, not 17** (col 18 `instrument_basis_operative` added S39 9/2, `MAINTENANCE.md:611`). (3) **SCHEMA.tsv is NOT "4 cols behind"** — it declares 18/18 for the registry and `schema_check.py` returns `✅ ALL CONFORM` rc=0 on 13/13 files today. (4) **FT-12 is 5 bps away and widening, not 3 bps** (SCRATCH.md CHANGES SINCE, HY 265 [9/2]); the 3-bps figure survives only on `STATUS.md:86` (mirror lag, defect D-3). (5) Tree is **3,368,429 B by `du -sb`** (353 files ✓); "4.2 MB" was block usage.

---

## 1. FILE ANATOMY — measured 2026-09-03

### 1a. Top level (`du -sb` for dirs, `wc -c` for files)

| Path | Bytes | Files | Note |
|---|---:|---:|---|
| `CALENDAR.md` | 28,062 | — | boot read (CLAUDE.md:50); rotated 9/2 (40,267→28,062, `b8e61d907`) |
| `CHALLENGE_IMPACT_LEDGER.md` | 20,298 | — | population stops at CHG-043, stats "as of 2026-07-31" (:5, :95) |
| `CLAUDE.md` | 41,489 | — | 352 ln; out of READ_CAP scope by canon (`BLUEPRINTS/READ_CAP.md:37`) |
| `LAST_COMPLETION.md` | 3,556 | — | last written 8/17 (`43330d28b`); see D-5 |
| `MAINTENANCE.md` | 97,484 | — | 614 ln; last entry `:609` S39 9/2 |
| `MEMORY.md` | 20,045 | — | boot read; rotated 9/2 (50,168→20,045) |
| `MEMORY_ARCHIVE.md` | 23,528 | — | pointer-only |
| `NEXUS_BRIEF.md` | 31,811 | — | 105 ln; rebuilt+rotated S40 (43,094→31,811); reader = NEXUS |
| `OUTBOX.md` | 144,115 | — | 973 ln; PROME dispatch ledger |
| `SCRATCH.md` | 12,683 | — | boot read; S40 handoff |
| `STATUS.md` | 30,004 | — | 157 ln; boot read; header rotated 9/3 to `reports/2026-09-03_S40_status_header_narrative.md` |
| `board_log.tsv` | 11,984 | — | 36 rows; pre-8/28 rows rotated to `archive/board_log_pre-2026-08-28.tsv` |
| `.claude/` | 557 | 1 | |
| `archive/` | 462,664 | 22 | LIVE retirement destination (recreated 8/12); 3 rotation files 9/2 + 3 `git mv` from workbook/ |
| `challenges/` | 273,246 | 20 | +5 since 8/12 (incl. `SELF_APPARATUS_REGISTRY_2026-08-27.md`) |
| `counter-evidence/` | 18,287 | 1 | `KRE_BULL_CASE.md` (MEMORY-referenced; keep) |
| `design/` | 19,196 | 1 | |
| `docket/` | 49,152 | 2 | CATALYSTS.tsv 46,142 (67 rows, 9-col) · WATCHLINES.tsv 3,010 (12 rows, 11-col, **sole CRLF file**) |
| `handoff_WALTER/` | 80,219 | 3 | HISTORICAL, README still presents live (D-8) |
| `inbox/` | 607,370 | 226 | 1 unprocessed top-level (SAM 9/3 07:46, post-close) · `processed/` 105 · `WALTER/` 0 top / `WALTER/processed/` 118 |
| `outbox/` | 72,477 | 11 | incl. NEW `outbox/kernel/submissions/CMD-01a06273….json` (IMMUTABLE, carve-out ④) |
| `registry/` | 70,344 | 5 | see §1c |
| `reports/` | 169,638 | 10 | +8 since 8/12 (STATUS narrative archives ×3, Kernel reviews ×4, S40 header) |
| `research/` | 248,548 | 21 | +7 since 8/12 |
| `scripts/` | 43,018 | 5 | boot.py · schema_check.py · review_debt.py (S33) · base_rate_review.py (S36d) · gen_trigger_scan.py (S39) |
| `thesis/` | 151,546 | 4 | CHANGELOG 138,133 · TIMELINE 8,990 · FRAMEWORK 3,630 · PREDICTIONS_README 793 |
| `workbook/` | 637,108 | 9 | 8 TSV + `KRE_EXECUTIVE_SUMMARY.md` (in LEDGER_GLOB) + `LEDGER_GLOB` |
| **TOTAL** | **3,368,429** | **353** | |

### 1b. BOOT READS (from `CLAUDE.md` BOOT :36-73 + WHAT YOU READ :209-219) vs the 32,550 B budget

| Boot step | File | Bytes | % budget | Read form | Flag |
|---|---|---:|---:|---|---|
| 1 (:39) | `MEMORY.md` | 20,045 | 61.6% | whole | ✅ |
| 1.5 (:40) | `BOARD/INDEX.md` | 1,627,433 | 4,999.8% | scoped b1-b4 scan | ℹ️ scoped by design |
| 1.5 (:46) | `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` | 1,924 | 5.9% | cross-ref | ✅ |
| 2 (:49) | `STATUS.md` | 30,004 | **92.2%** | whole | 🟡 rotate-tier (≥75%) — rotated 8/28 AND 9/3, re-breached both times |
| 3 (:50) | `CALENDAR.md` | 28,062 | **86.2%** | whole | 🟡 rotate-tier |
| 3 (:50) | `docket/CATALYSTS.tsv` | 46,142 | 141.8% | scoped (`status=pending` ~14d; boot.py parses) | ℹ️ scoped |
| 3 (:50) | `workbook/PREDICTIONS.tsv` / `CHALLENGES.tsv` | 22,994 / 97,974 | 70.6% / 301.0% | DUE-scan (boot.py) | ℹ️ scoped |
| 4 (:51) | `thesis/CHANGELOG.md` | 138,133 | 424.4% | last 2-3 entries | ℹ️ scoped (READ_CAP rule 8 partial) |
| 5 (:52) | `SCRATCH.md` | 12,683 | 39.0% | whole | ✅ (NB: `read_cap_check --agent RED` did not list it — heuristic miss, harmless today) |
| 5.5/5.6 (:53/:57) | `inbox/WALTER/*.md`, `inbox/*.md` | 0 / 1 file | — | ls + triage | ✅ |
| 8 (:63) | `PROME/STATUS.md` | 24,171 | 74.3% | positions+convictions | ✅ |
| 9 (:64) | `scripts/boot.py` reads registry/WATCHLINES/CATALYSTS/PREDICTIONS/CHALLENGES/board_log | — | — | by column, in-script | ℹ️ |
| 9b (:69, closeout) | `workbook/SCHEMA.tsv` | 22,217 | 68.3% | script | ✅ |
| — | `registry/FALSIFICATION_TRIGGERS.tsv` | **57,729** | **177.4%** | **NOT a RED whole-read** (CLAUDE.md:69 "on-demand edit surface, never a RED boot whole-read; boot.py scans it by column") | ⚠️ see §1c |
| — | `CLAUDE.md` | 41,489 | 127.5% | harness auto-load | ℹ️ out of READ_CAP scope by canon (`READ_CAP.md:37`) |

`python3 scripts/read_cap_check.py --agent RED` (fleet tool, read-only) today: **rc=0, "0 over budget"**, 5 whole-read files found, STATUS.md + CALENDAR.md flagged 🟡 rotate-tier.

### 1c. Registry re-measure (the cross-agent mandated read)

| File | Bytes | % budget | Rows | Cols | Who reads it |
|---|---:|---:|---:|---:|---|
| `registry/FALSIFICATION_TRIGGERS.tsv` (canon) | **57,729** | **177.4%** (was 139% on 8/31 = ~45 KB; +12.6 KB in 3 days, FT-10/11 letters) | 12 | 18 | RED boot.py by column; WALTER **on demand** for load-bearing rows (`AGENTS/WALTER/CLAUDE.md:65`) |
| `registry/FALSIFICATION_TRIGGERS_SCAN.tsv` (GENERATED) | 6,840 | 21.0% | 12 | 13 (line 0 = banner) | **WALTER boot 6b whole-read** (`WALTER/CLAUDE.md:64-65`, "RESOLVED 2026-09-03") |
| `registry/OUTCOME_SPEC.tsv` | 3,940 | 12.1% | 12 | 7 | RED (boot 9d) |
| `registry/TRIGGER_OUTCOMES.tsv` | 1,753 | 5.4% | 11 | 8 | RED (W2) |
| `registry/corrections_receipts.tsv` | 82 | 0.3% | 1 | 4 | `scripts/corrections_boot_check.py` |

**Perimeter verdict:** the 139%-of-budget cross-agent read is **RESOLVED** — WALTER's mandated read moved to the 6,840 B view; the view's banner `sha256=3dd54163…c07c` **equals `sha256sum` of canon today** (verified). Canon itself is now 177% and growing ~4 KB/day; it is read on demand only, so no budget breach exists *today*, but WALTER's own rule (:64) says "open canon when a row is load-bearing" — FT-10/11/12 rows are 5.7 / 12.2 / 10.1 KB each.

---

## 2. WHAT CHANGED since 2026-08-12

`git log --since=2026-08-12 --format='%h %ad %s' --date=short -- AGENTS/RED` → **149 commits** (RED-authored ≈ 94 per PR#5 :12; the rest are inbound packets). Ten structurally important changes:

| # | Hash | Date | Change |
|---|---|---|---|
| 1 | `fc7255bcc` | 8/20 | **Boot step 5.6 added** (general-inbox scan) after 18 packets accumulated 8/12–8/20 unenumerated; A1/A2 addendum blocks (CLAUDE.md:57) |
| 2 | `3c65de028` / `e715b9ace` | 8/20 | S33: `inbox/WALTER/` found LIVE while spec said NO-OP — step 5.5 rewritten (CLAUDE.md:53-56, "audit boot specs by DELIVERY DIRECTORY") |
| 3 | `6c36db72d` | 8/20 | **`scripts/review_debt.py` shipped + boot 9c** — row-level Stale_By/Last_Reviewed enforcement (KB past-Stale_By 33→9) |
| 4 | `56f687743` | 8/27 | **RED-FT-11 registered** (Treasury buyback attribution classifier, conditional, live 9/9) |
| 5 | `9d47a0dad` → `dbd0b8034` | 8/27 | **CHG-RED-051 — first APPARATUS self-challenge on RED's own registry**; deliverables: registry **15→17 cols** (`last_reviewed`, `rolling_base_rate`), NEW `OUTCOME_SPEC.tsv` + `TRIGGER_OUTCOMES.tsv`, NEW `base_rate_review.py` + boot 9d, **FT-12 registered** (HY<260 s=3, 0.0% base rate), FT-01 adjudicated to counter-signal |
| 6 | `6dd695ecb` | 8/28 | S38g read-cap housekeeping: STATUS 86,955→29,689 B; board_log 100,890→3,907 B (rotation to `archive/board_log_pre-2026-08-28.tsv`) |
| 7 | `f09b90a84` / `a8c2bf928` | 8/28 | Boot 9e corrections check wired (DAEDALUS packet) + first R1 receipt APPLIED (`registry/corrections_receipts.tsv`) |
| 8 | `2d701bdc8` / `0e9b21118` | 8/28 | Amendment-inherits-certificate audit of FT-01/06/07/08/11 (`challenges/2026-08-28_amendment_inherits_cert_audit.md`); VX-RED-004 closed FLIPPED-BEAR-TERMINAL |
| 9 | `b8e61d907` (+`20caea9aa`) | 9/2 | **S39 closeout:** registry **col 18 `instrument_basis_operative`** (17→18, append-only); NEW `scripts/gen_trigger_scan.py` → `FALSIFICATION_TRIGGERS_SCAN.tsv` (WALTER 6b consumer); MEMORY/CALENDAR verbatim rotations to `archive/`; first Kernel immutable submission `outbox/kernel/submissions/CMD-01a06273….json`; SCHEMA.tsv +14 rows |
| 10 | `9e55d4356` | 9/3 | **S40 closeout:** FT-10 grading basis DECLARED under WQ-162 (CBOE publisher of record; 0.77→0.23 margin withdrawn); FT-11 v1.1 encoded with BOND; **tie-set defect in RED's own base rate** → `research/2026-09-02_FT11_v1.1_second_path_partition_AND_tie_set.md` (now fleet canon `BLUEPRINTS/SPEC_LETTER_STANDARD.md:28` SL-5); STATUS header rotated to `reports/`; NEXUS_BRIEF rebuilt |

**New files since 8/12 (non-inbox, `git log --diff-filter=A`):** 35 — `archive/` ×4 (3 rotations + board_log) · `challenges/` ×5 · `outbox/` ×3 (incl. `kernel/`) · `registry/` ×4 (SCAN, OUTCOME_SPEC, TRIGGER_OUTCOMES, corrections_receipts) · `reports/` ×9 · `research/` ×7 · `scripts/` ×3. **Moved:** 3 misfiled `workbook/*.md` → `archive/` (R100). Inbox adds: 63.

---

## 3. THE FALSIFICATION LAYER — graded at the artifact

Header (18 cols): `trigger_id · metric · threshold_op · threshold_value · sustain_window · action · instrument_basis(7) · state(8) · action_magnitude · recipient_chain · falsification_thesis_ref · exit_op(12) · exit_threshold · exit_sustain · exit_source · last_reviewed(16) · rolling_base_rate(17) · instrument_basis_operative(18)`.

| Row | Letter | `state` (c8, verbatim) | `instrument_basis` c7 / c18 (chars) | `last_reviewed` | Exit (c12-14) | **SL-5: strictness declared?** | **SL-5: published precision declared?** |
|---|---|---|---|---|---|---|---|
| FT-01 | HY-OAS < 280 s=3 | `FIRING-BANKED` | 244 / 194 | 8/27 | ≥280 s=3 | ❌ | ❌ |
| FT-02 | HY-OAS > 320 s=3 | `ARMED` | 244 / 194 | 8/27 | <300 s=3 | ❌ | ❌ |
| FT-03 | BRENT-PAPER > 130 s=5 | `ARMED` | 1,781 / 322 | 8/27 | <115 s=5 | ❌ | ❌ |
| FT-04 | BRENT-PAPER < 75 s=3 | `ARMED` | 1,781 / 322 | 8/27 | ≥85 s=3 | ❌ | ❌ |
| FT-05 | INITIAL-CLAIMS > 250 s=1 | `ARMED` | 160 / 153 | 8/27 | ≤225 s=2 | ❌ | ❌ |
| FT-06 | VIX < 16 s=5 | `FIRED-BANKED` | 1,759 / 237 | 8/27 | ≥18 s=5 | ❌ (the word "strictly" at c9 is about magnitude, not the operator) | ❌ |
| FT-07 | CCC-OAS > 930 s=1 | `FIRING-BANKED` | 177 / 160 | 8/27 | <930 s=3 | ❌ | ❌ |
| FT-08 | CORE-CPI-3MO-ANN ≥ 3.0 s=1 | `ARMED` | 355 / 255 | 8/27 | <2.5 s=1 | ❌ | ❌ |
| FT-09 | BREAKEVEN-5Y5Y > 2.55 s=5 | `ARMED` | 336 / 165 | 8/27 | <2.40 s=5 | ❌ | ❌ |
| FT-10 | SKEW-CBOE ≥ 150 s=4 | `ARMED` | 2,994 / 670 | 9/2 | <140 s=4 | ✅ "≥150 NON-STRICT so 150.00 FIRES; exit <140 STRICT so 140.00 does NOT exit" (c7 §3, c18) | ✅ "publishes at exactly 2 dp (VERIFIED 9219/9219 rows)"; tie sets {150.00} 0 occ / {140.00} 2 realised |
| FT-11 | UST-30Y-RALLY-ATTRIBUTION ≤ −10.2 s=5 | `ARMED-UNFIRED (precondition live from 2026-09-09, …)` | 7,415 / 690 | 9/2 | ≥0 s=0 = "does NOT exit on a classification" (c15) | ✅ v1.1 leg (iv) "≤ −4bp NON-STRICT (tie −4 counts)" (c18); c17 "tie atom at exactly −4bp = 23/661 = 3.5%" | ✅ "integer-valued" / "integer bp" (c17; research file :133 `rint(x*100)` before differencing) — but the **precondition leg −10.2 on DGS30 (published 2dp %) has no tie clause** |
| FT-12 | HY-OAS < 260 s=3 | `ARMED-UNFIRED (never satisfied at s=3 anywhere in the 3y sample)` | 8,213 / 304 | 9/2 | ≥260 s=3 | ✅ c18 "STRICT < 260: an observation of exactly 260.0 does NOT count" | ⚠️ partial — "percent ×100 = bps" states the conversion, not the series' published precision |

**FT-11 operator, quoted:** c3 `<=`, c4 `-10.2`; v1.1 leg (iv) at c18: *"leg (iv) Delta5(2*DGS20-DGS10-DGS30) <= -4bp NON-STRICT (tie -4 counts) as a FLOW-ALTERNATIVE route, plus a SECOND PRECONDITION PATH on fly<=-4 with no 30Y rally that yields a BUTTERFLY-ONLY FLOW FLAG (no usable FUND branch, 17.6% resolution)."* **Tie-set clause (c17):** *"v1.1 leg(iv) CORRECTED 2026-09-02 S40: <=-4bp AS WRITTEN (non-strict) = 8.5% uncond / 6.2% given-precondition (5/80), LR~21; the S39b-registered 5.0%/3.8%/LR~34 is the STRICT cut (<-4) — tie atom at exactly -4bp = 23/661 = 3.5% of sample."* Research artifact: `research/2026-09-02_FT11_v1.1_second_path_partition_AND_tie_set.md` (13,150 B; §2 :50 "the base rate BOND selected on is a STRICT cut; the letter BOND adopted is NON-STRICT"; :134 all operators written out non-strict).

**FT-12 current state cell:** `ARMED-UNFIRED (never satisfied at s=3 anywhere in the 3y sample)` · c17 `0.0% @120obs [2026-09-02]` · live HY **265 [9/2]**, 5 bps away and widening (SCRATCH.md CHANGES SINCE; `STATUS.md:86` still says "NEAR (3bps) … 263 [8/27]" — D-3).

**SL-5 tally:** 3 of 12 rows carry a strictness declaration (FT-10/11/12); 1 of 12 names the series' published precision in full (FT-10); **9 rows (FT-01…09) are silent on both**, two of them FIRING on integer-bp series (FT-01 at 280, FT-07 at 930). RED already queues a "registry-wide tie-set audit … both ends of every two-way trigger" for the 9/4–9/11 window (SCRATCH.md NEXT SESSION item 3).

**Other layer facts:** exits are now defined 12/12 (were 2/9 on 8/12); the literal `UNDEFINED` token appears 6× in prose only. `OUTCOME_SPEC.tsv` has all 12 trigger ids; `TRIGGER_OUTCOMES.tsv` 11 grades (FT-01 ×9, FT-06, FT-07; 4 UNRESOLVED with `resolve_after` ~9/9 · ~9/9 · ~9/26 · ~10/29 — SCRATCH item 4 carries the 9/9 pair). WALTER `FALSIFICATION_FIRED_LOG.tsv` holds 5 RED-FT rows (FT-01 ×3, FT-06, FT-07).

---

## 4. `workbook/SCHEMA.tsv` — the "4 cols behind" claim, resolved with numbers

| Fact | Value |
|---|---|
| Exists / parses | Yes; 22,217 B, 143 lines, **6-col header** `file · variable_name · data_type · allowed_values · required · description`, tab-delimited (every line splits to 6 fields; 0 CRLF) |
| Last touched | `b8e61d907` 9/2 (+14 rows for col 18 + SCAN view); prior `dbd0b8034` 8/27, `19565dd39` 8/12 (84→111 rows) |
| Files declared / cols declared vs live header | KB 13/13 · VX 12/12 · ML 14/14 · CHALLENGES 11/11 · PREDICTIONS 10/10 · FLOW 9/9 · VX_HISTORY 7/7 · **FALSIFICATION_TRIGGERS 18/18** · FALSIFICATION_TRIGGERS_SCAN 13/13 · OUTCOME_SPEC 7/7 · TRIGGER_OUTCOMES 8/8 · CATALYSTS 9/9 · WATCHLINES 11/11 |
| `python3 AGENTS/RED/scripts/schema_check.py` (read-only) today | `✅ ALL CONFORM`, **rc=0**, 13/13 `ok`, same order |

**Verdict: the "4 cols behind" claim is REFUTED at today's tree.** It was true on 8/12 (8 declared vs 12 live — `schema_check.py` docstring :10-12) and was fixed the same day (`19565dd39`); both later column additions (8/27 +2, 9/2 +1) landed with SCHEMA rows in the same commit. Value domains remain deliberately out of scope (docstring :19-25) — a structural PASS, not a vocabulary one.

---

## 5. `workbook/VX.tsv`

| Fact | Value |
|---|---|
| Layout | line 0 = banner, **header = line 1**, 25 vector rows (27 lines); 12-col; LF |
| Data clock (banner :1) | `Last real data refresh: 2026-06-02` — *"the OLDEST LIVE vector's Last_Reviewed … set deliberately to the stalest live row so ledger_staleness keeps the alert LIT while 9 of 17 live vectors remain CARRIED-not-measured (S33 2026-08-20)"* |
| `CARRIED` marker count (rows 2+) | **9** (VX-003/005/006/007/008/009/010/012/026) — unchanged from the S33 banner figure |
| `REVIEWED-MEASURED` count | 4 (VX-001/006/014/017; VX-006 carries BOTH markers) |
| Closed-state rows | 11 (FLIPPED/RESOLVED/TERMINAL family incl. VX-004 closed 8/28 `0e9b21118`) |
| Last commit touching VX | `0e9b21118` 8/28 (VX-004 closure only; no CARRIED row re-instrumented since 8/12) |
| Dated re-trigger for the carry | **Exists in prose, not in the docket:** "9/12 VX re-review" at `workbook/ML.tsv:205` (ML-RED-205), `OUTBOX.md:352`, `SCRATCH.md` NEXT SESSION item 3 ("Carried: … VX 9/12 re-review"), and the 8/27 ledger-nudge rider `25e406d52` ("VX 9/12-dated"). **`docket/CATALYSTS.tsv` has NO row for it** (grep `VX|2026-09-12` → only 6/09–7/03 resolved rows). |

So the FLEET_MAP leg-(c) condition ("VX carried-count falls or is re-based") is **NOT met** today: 9 CARRIED, clock 6/02, and the instrument that would move it (the 9/12 pass) is invisible to boot 3's DUE-scan by construction.

---

## 6. DO-NOT-TOUCH quirks — re-verified

| # | Prior quirk (profile §5) | Status today | Evidence |
|---|---|---|---|
| 1 | KB/VX/FLOW/CHALLENGES/PREDICTIONS = RED's adversarial schema, never generic-ize | **PRESENT** | `CLAUDE.md:268-296` workbook table; VX 12-col, FLOW frozen, CHALLENGES 11-col live |
| 2 | Registry = WALTER auto-fire; WATCHLINES = soft display; `UNDEFINED` exits honest | **PRESENT, half-retired** | `CLAUDE.md:68`; exits now defined 12/12 (§3) — `UNDEFINED` survives only in prose; **FT-11's `≥0 s=0` exit is a deliberate "does not exit on classification" (c15), not a blank** |
| 3 | Steelman-before-attack ordering | **PRESENT** | `CLAUDE.md:26 / :199 / :352`; `STATUS.md:40` BULL CASE STEELMAN precedes `:52` COUNTER-SIGNALS |
| 4 | Discipline overlay: dated stamp = TRIGGER not shield | **PRESENT (moved)** | `CLAUDE.md:116` (was :84) |
| 5 | Amendment-10 fold-LAST rule | **PRESENT, RECONCILED** | `NEXUS_BRIEF.md:105` "under revision"; `CLAUDE.md:110` "per-ENDING, not per-day" — keep the reconciled form |
| 6 | LAST_COMPLETION dual-role (spawn-contract surface, never boot-read) | **PRESENT but the fleet contract moved** | `CLAUDE.md:241` still says PROME-spawned sessions MUST overwrite it; `PROME/COMPLETION_SPEC.md:3` RE-KEYED 8/13 to a dated outbox memo; S40 (a PROME spawn) wrote `outbox/2026-09-02_to-PROME_…` and left LAST_COMPLETION at 8/17 — **re-cut the quirk to "expected permanently stale unless the spec reverts"**; residue "retired LAST_COMPLETION" at `:86` and `:234` |
| 7 | Dated historical records stay uncorrected (STATUS:40 principle) | **PRINCIPLE TEXT GONE from STATUS** (`:40` is now the steelman header; grep for the principle in STATUS/CLAUDE/MEMORY → null); **practice persists** — `CALENDAR.md:7` still carries the $100.19 figure in a resolved header line, rotated copy at `archive/CALENDAR_resolved_rotation_2026-09-02.md` | re-home or drop the quirk |
| 8 | FLOW.tsv FROZEN | **PRESENT** | `workbook/FLOW.tsv:0` banner "FROZEN 2026-07-05" |
| 9 | Canonical predictions = `workbook/PREDICTIONS.tsv` only | **PRESENT** | `CLAUDE.md:249`; `thesis/PREDICTIONS_README.md:5` dead archive path persists (D-7) |
| 10 | CRLF guard on whatever is CRLF at read time | **PRESENT** | `docket/WATCHLINES.tsv` is the sole CRLF file (13 CR lines; every other TSV 0) — unchanged since 8/12 |
| — | KB Status case-split (`ACTIVE`/`Active`, old D2) | **GONE** | KB col 9 today: 39 `ACTIVE`, 0 `Active` |

**NEW load-bearing quirks (add):**

| # | Quirk | Evidence |
|---|---|---|
| N1 | **Banner-line-0 files: header is LINE 1** — `VX.tsv`, `FLOW.tsv`, `FALSIFICATION_TRIGGERS_SCAN.tsv`. A `head -1 | awk NF` reads 1 field; a naive `NR>1` counts the header as a row (this is how RED itself published "9 of 18") | `VX.tsv:1` banner text; `schema_check.py` FILES map carries per-file header index |
| N2 | **Never parse RED TSVs with Python `csv`** — literal `"` in prose cells; split on tab | `CLAUDE.md:69`; `schema_check.py` docstring :27-30 (ML-RED-168) |
| N3 | **`FALSIFICATION_TRIGGERS_SCAN.tsv` is GENERATED** — never hand-edit; regenerate after every canon edit; banner sha256 must equal canon's or WALTER treats it as STALE | `CLAUDE.md:69`; `WALTER/CLAUDE.md:64`; `gen_trigger_scan.py:62-68` `--check` |
| N4 | **Registry column additions are APPEND-ONLY** (positional consumers of cols 0–16) | `MAINTENANCE.md:611` |
| N5 | **VX banner clock 2026-06-02 is DELIBERATE** — do not bump on an edit; only a re-instrumentation of the stalest live row may move it | `VX.tsv:1` |
| N6 | **`outbox/kernel/submissions/*.json` are IMMUTABLE** (carve-out ④) — never edit/move/delete; never a boot read | `MAINTENANCE.md:611-613` |
| N7 | **SCRATCH.md template comment lists headings WITHOUT `##` on purpose** — anchored edits must use body-unique strings and verify by heading OFFSET (ML-RED-155) | `SCRATCH.md:3-22` |
| N8 | `boot.py` `CORE-CPI-3MO-ANN` deliberately unmapped (still) | `scripts/boot.py:63` |
| N9 | **FT-10 grade basis = CBOE `SKEW_History.csv`; Yahoo `^SKEW` is a provisional mirror that cannot complete a grade** — never quote a FT-10 margin off boot.py's line | registry FT-10 c7 §(1)/(4), c18 |
| N10 | **A FLOW classification on FT-11 moves NO weight** (an instrument finding, not a world finding) | FT-11 c9, c18 |

---

## 7. DEFECTS (flag, never fix)

| ID | Sev | Where | Defect | Suggested fix |
|---|---|---|---|---|
| D-1 | 🟠 | `registry/FALSIFICATION_TRIGGERS.tsv` col 8 rows FT-01/06/07/11/12 → propagates to `FALSIFICATION_TRIGGERS_SCAN.tsv` col 7 (WALTER 6b parses it) | `state` — a **new** (8/27) cross-agent-parsed column — carries non-canonical tokens: `FIRING-BANKED`, `FIRED-BANKED`, `ARMED-UNFIRED (…prose…)`. Canon `BLUEPRINTS/STATE_VOCABULARY.md:46-54`: `ARMED / FIRED / NOT-FIRED …`, "`UNFIRED` → `NOT-FIRED` on new surfaces", banked/held rides the `Response` axis (:57). Grandfathering does not apply — the column postdates the vocabulary | Canonical token in c8; move the parenthetical qualifier to notes/`Response`; regenerate the view |
| D-2 | 🟠 | `scripts/boot.py:69` `"SKEW-CBOE": ("yf","^SKEW",…)` | boot.py evaluates FT-10 from the mirror the FT-10 letter disqualifies (c18). Correct today only because both print 144.12; on a mirror defect (0.79%/session, two modes) the boot line would grade off a NO-VERDICT source. **RED self-declared** (`9e55d4356` §10; SCRATCH item 3) | Label the boot line PROVISIONAL or read the CBOE CSV; until then never cite a FT-10 margin from boot.py |
| D-3 | 🟡 | `STATUS.md:86` and `:125` | Doc-mirror lag: FT-12 row "🟡 NEAR (3bps) … HY 263 [8/27]" vs registry c17/c18 + SCRATCH (265 [9/2], 5 bps, widening); `:125` "WL-11 Brent <95 (firing)" vs SCRATCH "WL-11 un-fired, 0.43 above". CLAUDE.md:118-125 says canonical wins | Refresh the two narrative rows at next W1 |
| D-4 | 🟠 | registry rows FT-01…09 (and FT-12 precision, FT-11 precondition leg) | **SL-5 not met on 9/12 rows** — no operator-strictness or published-precision clause; FT-01 (<280) and FT-07 (>930) are FIRING on integer-bp series where a boundary print changes a sustain count | Run the queued registry-wide tie-set audit (SCRATCH item 3) with all five SL-5 clauses incl. exit legs and same-operator base rates |
| D-5 | 🟡 | `CLAUDE.md:241` (+ residue `:86`, `:234`) | Charter says PROME-spawned sessions MUST overwrite `LAST_COMPLETION.md` per `PROME/COMPLETION_SPEC.md`; that spec re-keyed delivery 8/13 to a dated outbox memo (`COMPLETION_SPEC.md:3`). RED's S40 followed the new spec; the charter line now instructs the old one | Amend :241 to the outbox-memo contract; reconcile :86/:234 "retired" wording |
| D-6 | 🟡 | `CLAUDE.md:256` | `competing-hypotheses/` listed under Working Directories; directory does not exist (8/12 D6 residue, 22 d) | Strike the row or create the dir |
| D-7 | 🟡 | `thesis/PREDICTIONS_README.md:5` | "Archived verbatim at `archive/superseded_workbook/…`" — path absent (deleted `1cb18fbc3`, recoverable at `1cb18fbc3^`); 8/12 D6 residue | Documented-loss form (CORAL CLAUDE.md:5 template) |
| D-8 | 🟡 | `handoff_WALTER/README.md:6` | "RED does NOT yet maintain a `board/BOARD_LOG.tsv`" — `board_log.tsv` live since 7/5 (36 rows + rotated archive); 8/12 D7 persists, no closed-banner | HISTORICAL banner at :1 |
| D-9 | 🟡 | `CHALLENGE_IMPACT_LEDGER.md:5`, `:95` | Population CHG-001…043, stats "as of 2026-07-31"; CHG-044…051 (8 rows, 34 d) unscored; NEXUS-cited | Re-populate or banner the vintage |
| D-10 | 🟠 | `docket/CATALYSTS.tsv` (absence) | The 9/12 VX re-review — the item that gates FLEET_MAP conf M→H — exists only in prose (ML-RED-205, OUTBOX:352, SCRATCH item 3 "Carried"); boot 3 / boot.py DUE-scan cannot see it | One CATALYSTS row, `status=pending`, 2026-09-12 |
| D-11 | 🟡 | `STATUS.md` 30,004 B (92.2%), `CALENDAR.md` 28,062 B (86.2%), `NEXUS_BRIEF.md` 31,811 B (97.7%, reader's cap) | All three sit at rotate-tier; STATUS re-breached within 6 days of two rotations (8/28, 9/3) — rotation cadence < growth rate | Structural: move the falsification narrative table out (STATUS:73 already pointer-only) or rotate at ≥75% every closeout |
| D-12 | 🟡 | `workbook/KRE_EXECUTIVE_SUMMARY.md` + `challenges/KRE_EXECUTIVE_SUMMARY.md` | Duplicate basename persists (8/12 D8; opposite verdicts); the workbook copy is also declared in `workbook/LEDGER_GLOB` (an .md in a TSV-ledger glob) | RENAME, never merge; drop from LEDGER_GLOB |
| D-13 | 🟡 | `STATUS.md:151-157` BOTTOM LINE | Body vintage S29 (8/12) with an S32 (8/20) rider and a closing "*RED Session 29:*" paragraph; 11 sessions later. Defensible as "unchanged — 15× NO WEIGHT MOVED", but it narrates FT-06's fire as "the session's real finding" | Restamp or rewrite at next W1 |
| D-14 | 🟡 (DAEDALUS-side) | `scripts/read_cap_check.py --agent RED` | Perimeter heuristic lists 5 whole-reads and misses `SCRATCH.md` (CLAUDE.md:52 "Read `SCRATCH.md`"); harmless at 39% today | Note for the READS.tsv replacement |

No 🔴 silent-failure defect found: every guard RED depends on (`schema_check`, `gen_trigger_scan --check`, `review_debt`, boot.py ⑤) was watched producing its clean line in the 9/2 and 9/3 commit bodies and (schema_check, sha256) re-run here.

---

## 8. MATURITY READ — Utility class, per leg

| Leg | Verdict | Evidence |
|---|---|---|
| **L0** dir + CLAUDE.md | **MET** | `AGENTS/RED/CLAUDE.md` 352 ln, CONTRACT :22-28 |
| **L1** STATUS + BOTTOM LINE | **MET** (caveat D-13) | `STATUS.md:2` Last Updated 2026-09-03 ~07:2x ET; BOTTOM LINE `:151` present |
| **L2** structured record accruing, valid schema | **MET** | ML-RED-213 (213 rows, zero ID gaps); CHALLENGES 51 rows, 6 ACTIVE-class rows all dated (027→10/31, 044→9/15, 045→11/15, 047→9/3, 049→9/15, 051→10/31); PREDICTIONS 22 rows (1 ACTIVE RED-04→9/30, 21 RESOLVED); `schema_check.py` rc=0 13/13; registry 12 rows × 18 cols with `last_reviewed` 8/27 (9 rows) / 9/2 (3 rows) |
| **L3** role rubric applied consistently | **MET** | CONTRACT :22-28 → `thesis/FRAMEWORK.md`; steelman `STATUS.md:40` before counter-signals `:52`; base-rate-FIRST on every 2026 registration (FT-10 c7, FT-11 c17, FT-12 c7); CHG-051 apparatus self-challenge (`challenges/SELF_APPARATUS_REGISTRY_2026-08-27.md`); tie-set defect found in its own number pre-go-live (`9e55d4356` §4) |
| **L4** output consumed by others | **MET** | `AGENTS/WALTER/CLAUDE.md:65` boot 6b whole-reads `FALSIFICATION_TRIGGERS_SCAN.tsv` (RESOLVED 9/3 note :64); `AGENTS/BOND/STATUS.md:138` standing obligation keyed to `RED-FT-11` ("route the F2 read to RED as the ops publish"); `AGENTS/NEXUS/STATUS.md:116` cites `RED-FT-12`; `PROME/DOCKET.tsv:235` `RED-FT-11`; `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` 5 RED-FT rows; NEXUS reads `NEXUS_BRIEF.md` via `AGENTS/NEXUS/CLAUDE.md:36` BRIEFS_MAP; fleet canon `BLUEPRINTS/SPEC_LETTER_STANDARD.md:28` SL-5 born from RED+CREED 9/3 |
| **L5** clean closeouts + CURRENT | **MET** (two mirror-lag caveats) | **Closeouts after 8/28: TWO.** S39 `b8e61d907` 9/2 10:21 ET — body records schema_check ALL CONFORM · gen_trigger_scan --check current · claim_check clean · read_cap 0 over · memory_index_check rc=0 · ledger nudge answered per file; touched STATUS/SCRATCH/OUTBOX/MAINTENANCE/CHANGELOG/KB/ML/board_log (+17). S40 `9e55d4356` 9/3 07:20 ET — same battery + corrections_boot_check rc=0 + consumer_check --self on the withdrawn 149.23; W-A addendum executed (STATUS/SCRATCH/OUTBOX/NEXUS_BRIEF/MAINTENANCE all in the file list); read-cap breach it created (33,375 B) fixed in-session. **Independently re-verified today:** schema_check rc=0; SCAN sha256 == canon; read_cap_check rc=0; inbox 1 top-level (arrived 07:46, after close); `board_log.tsv` last rows 2026-09-02T23:03 incl. explicit BOARD "0 signals" and WALTER-lane "EMPTY — VERIFIED at the path" tokens. **Not clean:** `STATUS.md:86/:125` mirror lag (D-3); registry state tokens (D-1). "Dark since 8/28" is refuted. |

**Confidence recommendation: HOLD at M (do not lift to H yet).** The FLEET_MAP `Next_upgrade` cell names two conditions: *"VX carried-count falls or is re-based AND one closeout after 8/28 is clean."* The second is met twice over. **The single deciding fact against H: `grep -c CARRIED workbook/VX.tsv` = 9, identical to the S33 (8/20) banner figure, with the banner clock still 2026-06-02 and the 9/12 re-review that would move it absent from `docket/CATALYSTS.tsv` (D-10).** Re-cut to H on the first commit after 9/12 in which that count falls or the banner is re-based with the row-level evidence — a one-line check.

---

## 9. OPEN QUESTIONS for RED (could not be resolved from the files)

1. **VX 9/12 pass:** is the 9/12 re-review scheduled to land on 9/12, will it re-instrument the 9 CARRIED rows or freeze them, and why is it not a `CATALYSTS.tsv` row when the DUE-scan is the only thing that reads dates at boot?
2. **State tokens (D-1):** are `FIRING-BANKED` / `FIRED-BANKED` / `ARMED-UNFIRED (…)` a registered local vocabulary agreed with WALTER, or unreconciled with `STATE_VOCABULARY.md`? Does WALTER's 6b recognizer key on them?
3. **FT-11 v1.0 partition:** the 4/68/8 vs 5/71/4 vs 4/60/16 non-reconciliation is "cause UNKNOWN" with a 9/9 deadline (SCRATCH item 3) — what is the plan if it does not reconcile by 9/9: go live with the disclosure, or hold the precondition?
4. **FT-10 wiring (D-2):** which remedy — CBOE CSV fetch in boot.py, or a PROVISIONAL label — and by when?
5. **SL-5 backfill (D-4):** will the 9/4–9/11 tie-set audit cover FT-01…09 fire AND exit legs and recompute `rolling_base_rate` on the operator as written (SL-5 clause 4)?
6. **LAST_COMPLETION (D-5):** given `COMPLETION_SPEC.md` re-keyed 8/13, does RED intend to retire the file for real or keep it as a legacy surface — and which does `CLAUDE.md:241` mean to say?
7. **FT-12 mirror (D-3):** was `STATUS.md:86` (3 bps / 263 [8/27]) deliberately left at S40 because the header rotation moved the narrative, or missed at W1?
8. **CHALLENGE_IMPACT_LEDGER (D-9):** what cadence re-populates it (CHG-044…051 unscored, 34 d)? NEXUS cites it.
9. **NEXUS_BRIEF at 97.7%:** whose cap governs (reader's = NEXUS) and is there a rotation plan before the next fold breaches it?
10. **8/12 residue (D-6/7/8/12):** are `competing-hypotheses/` row, PREDICTIONS_README path, handoff_WALTER README, and the KRE_EXECUTIVE_SUMMARY basename collision in RED's own hygiene queue, or should DAEDALUS packet them?
11. **Canon growth:** `FALSIFICATION_TRIGGERS.tsv` grew 45→57.7 KB in 3 days (FT-10/11 letters). Is the "registry prose split" carried in SCRATCH item 3 meant to move letters to `research/` with the row keeping the operative clause (col 18)?
