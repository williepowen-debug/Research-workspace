# R4 — REGINALD per-bank tree + reports/ + research/ (DAEDALUS whole-profile refresh reader 4 of 4)

**Reader:** R4 (Opus 5.5, DAEDALUS-spawned, read-only) · **Started:** 2026-10-30 16:42:01 EDT (`date`) · **Written:** 2026-10-30 16:49–17:0x EDT · **HEAD at start:** `9f0975860`; HEAD at write `fd64b229d` (7 intervening commits, **0 touch `AGENTS/REGINALD/`**: `git log 9f0975860..HEAD -- AGENTS/REGINALD | wc -l` = 0).
**REGINALD tree state:** `git status --porcelain -- AGENTS/REGINALD/` = **empty at start (16:42) and at 16:49**; re-checked at end (§H). No write, launch or message to REGINALD. Only write = this file. Temporary census scripts live in my scratchpad only.
**Baseline:** `profiles/_prior/REGINALD_2026-10-30_before_refresh.md` (body = 8/07 rewrite) and `runs/2026-10-22_BANK_DESK_REVIEW/REGINALD.md`.

## Headline

**The F1 layer is gone. It was retired, not refreshed.** On 8/13 (`f69ff2963`, Will-ruled slate item R2) the whole per-bank subtree moved by `git mv` to `archive/per-bank/`. All 7 THESIS files had FROZEN banners from 8/10 (both CONTRADICTED banners were written as specified). MTB followed on 10/22 (`f984ce53c`). The live per-bank work now lives in three places: a Will-requested **EGBN research hub** (`research/EGBN/`, 10/20–10/22, Q3 included), **dated per-bank reports** (CFG Q3 grade 10/16; MTB 10/20; EGBN Q4 wall 10/22), and **cross-bank catch-ups**. The pre-registration-then-grade discipline continues through Q3.

**Residual risk sits with the killed OZK `37.6%` figure.** It still appears without a flag in **one live-cited report**, `reports/2026-07-30_bank-side-HY-attribution.md:122`. That report is the "Full test" that STATUS:60 and CLAUDE:152 send readers to. The figure also appears in **4 live KB rows** and **3 unbannered legacy xlsx files**.

---

## A. Per-bank census (all 7 now under `archive/per-bank/`; 101 files on disk, 55 tracked; 99 MB)

Method: a Python walk (`scratchpad/census.py`). "Banner" means a FROZEN, DEAD-FIGURE, SUPERSEDED or NOT-maintained token in the first 5 lines. "Body vintage" is the date in the body's own Updated/Date stamp. The newest date anywhere in the text is usually the 8/10–8/13 banner itself.

| Bank | Files (disk) | Analytical md/tsv, bannered/total | Body vintage | Banner date | THESIS stamp | State |
|---|---|---|---|---|---|---|
| EGBN | 9 | 6/9 (no banner: EARNINGS_PREP, EXTERNAL_PROMPTS, KB_INDEX) | 2026-04-06/07 | 8/10 | "⚠️⚠️ FROZEN 2026-08-10 — and CONTRADICTED", carries the 7/25 discriminator verbatim | ARCHIVED 8/13 · **also byte-identical copy in `research/EGBN/historical/per-bank/` (9/9 cmp IDENTICAL)** |
| CFG | 21 | 4/8 (STATUS has only the 8/13 DEAD-FIGURE banner, no FROZEN banner; header still reads "🟠→🔴 THESIS VALIDATED + FHLB FLIPPED") | 2026-03-30 / 04-16 | 8/10, 8/13 | "⚠️⚠️ FROZEN 2026-08-10 — VALIDATED … CONTRADICTED IN MEANING" | ARCHIVED 8/13 |
| ZION | 11 | 4/8 (TODO, INDEX, STATUS, FRAMEWORK unbannered) | 2026-03-27 / 05-09 | 8/10, 8/13 | FROZEN 8/10 | ARCHIVED 8/13 |
| MTB | 12 | 2/6 | 2026-04-15 | 8/10, 10/22 ("🧊 FROZEN 2026-10-22" on STATUS) | FROZEN 8/10 | ARCHIVED 10/22 (`f984ce53c`, record `archive/RETIREMENT_2026-10-22.md`) |
| FITB | 21 | 2/6 | 2026-04-16/17 | 8/10 | FROZEN 8/10 · "NOT a position name" kept at THESIS:5 | ARCHIVED 8/13 |
| PNC | 9 | 2/4 | 2026-04-16 | 8/10 | FROZEN 8/10 · "NOT a position name" kept at THESIS:5 | ARCHIVED 8/13 |
| RF | 18 | 2/6 | 2026-04-16 | 8/10 | FROZEN 8/10 · "NOT a position name" kept at THESIS:5 | ARCHIVED 8/13 |

- **There are no dangling live links into the old paths.** I grepped root `*.md` for `<BANK>/<file>` path forms outside `archive/per-bank`. The only hits were bare ticker mentions (CLAUDE:128, STATUS:38, POSITIONS:87, ROADMAP:39), none of them a path. (Verified)
- **`archive/per-bank/` has no README or index banner, and neither does `archive/` (116 entries).** Location is the only marker for the unbannered half (EARNINGS_PREP ×6, FITB/PNC/RF STATUS scorecards, MTB analyses). The provenance lives in the commit body of `f69ff2963` and in `archive/RETIREMENT_2026-10-22.md`. 🟡
- **Stray file:** a CFG `…Citizens Financial Group Inc (CFG) Q1 2026_.md:Zone.Identifier` sits in `archive/per-bank/FITB/sources/`. Cosmetic. (Verified)
- `domain/` **no longer holds per-bank dirs.** Its 481 files are: 4 top-level md, `research/capital-rewrite-2026/` (4), and `sources/` (473). Of the sources, 18 are dated receipt dirs from 10/12–10/28 (~451 files) and 10 are Feb–Mar legacy files plus 12 receipts dated 10/12–10/13.

## B. reports/ since 8/07: frames vs grades, Q3 coverage

145 files: Jul 10 · Aug 10 · Sep 20 · Oct 105. The Oct count includes receipt bundles: `2026-10-20_organisation-cleanup/` (13), `2026-10-21_boot/` (15), `2026-10-21_owed-items/` (6) and similar.

| Pre-registered frame (FROZEN) | Graded by | Status at 10/30 |
|---|---|---|
| `2026-08-13_upcap_discriminator_PREREGISTERED` | `2026-08-13_upcap_decomposition` | GRADED same day: NOT SUPPORTED 0/14 |
| `2026-09-02_MTB_baltimore_FROZEN_frame` | in-file RESULT column, 9/02 2nd session | GRADED: "L2 = MUNICIPAL ⇒ TRUE AND IRRELEVANT; L5 = NO ROW" (file:4) |
| `2026-09-24_FL_bank_rail_Q3_FROZEN_frame` (BKU/SSB/AMTB/SBCF) | cells in `2026-10-22_catchup/REPORT.md:31` and following; STATUS:5 (10/28) | **PARTIAL.** Every 8-K read cell holds at 4/4; aggregate PROVISIONAL until the 10-Qs (~11/14) |
| `2026-10-07_WQ318_funding-vs-nonbank-baseline` + `2026-10-11_CFG_Q3_earnings_read-note` (checklist) | `2026-10-16_due-rows_CFG-Q3-grade_Nano_REG-T-03.md` §1 | GRADED: CFG **INCONCLUSIVE (leans DOWN)**, primary 8-K acc 0000759944-26-000206; call transcript not read (disclosed) |
| `2026-10-09_Q3_earnings_read_plan` (FROZEN before any print) | `2026-10-20_reported-bank-earnings-catchup` + `2026-10-22_catchup/REPORT.md` | PARTIAL. 10/20: "L180 breadth test remains UNKNOWN / not yet gradeable … FL aggregate is also ungraded" |
| `2026-10-23_ranking-test_FROZEN_protocol` (sha in commit and CALENDAR) | 11/07 run | PENDING. Honestly labelled "Retrospective validation, not a blind test" because 13/14 Q3 releases were read first |
| `2026-10-28_borrowing-screen_FROZEN_rule` | 11/07 Call-Report run | PENDING. Frozen before FDIC posted Q3 |

**Q3 coverage.** Mentions in October reports, by name: EGBN 37 · OZK 43 · WAL 42 · FLG 32 · CFG 30 · VLY 25 · CUBI 23 · AMTB 19 · HBAN 19 · ZION 18 · SSB 18 · BKU 17 · SBCF 16 · MTB 15 · PNC 4 · FITB 3 · RF 1. All 14 cohort names are covered. The out-of-cohort read-throughs (FITB/PNC/RF) are thin by design ("GIBBS review consumed, not repeated").

**Do Q3 grades feed STATUS's convergence matrix? Not yet, by explicit design (Verified).** STATUS:38 freezes the cohort scores ("FLG 6 · EGBN 5 · AMTB 5 · VLY 3 · … · CFG/HBAN 0"), and both STATUS:18 and `2026-10-22_catchup/REPORT.md:79` say "Scores move only at the 11/07 re-score". Q3 evidence reaches STATUS through the dated prose "Current judgment (10/30)" at STATUS:7 (problem loans rose at 7/10 names, coverage fell at 6/8, L801 drops the coverage leg) and through the "Evidence limits" line at STATUS:9.

**One consequence to flag (🟡, Inferred).** EGBN's own Q3 print gives CRE concentration **245.8%** and NPA/assets **1.75%**, up from 1.17% (`research/EGBN/data/EGBN_asset_quality_quarterly.tsv:27`, release p2/p11). STATUS_MATRIX:31 still describes EGBN only through the 7/25 Q2 grade (267.6%, "DE-RISKING"). The row is dated and the deferral is declared, so this does **not** violate the one-figure rule. But `245.8` appears nowhere in STATUS, STATUS_MATRIX or BANK_EXPOSURE_MATRIX: grep finds it only in the hub TSV, the two extract copies and a processed WALTER signal.

**Discipline verdict:** pre-register → freeze → grade-on-letter is **continuing and widening**. Q3 has 4 frozen frames plus 1 checklist, and 2 more frozen protocols are dated for 11/07. Defects are disclosed rather than re-tuned: the 10/23 protocol labels itself retrospective. No frame since 8/07 was edited after its print. (Spot-checked: git log on all 6 frame files shows the creation commit only, except where an in-file RESULT was appended.)

## C. research/: vintage census and retirement-eligible count

**Census (267 tracked files):** last-commit month: Oct 265 · Jul 1 (`prompts/README.md`) · Jun 1 (`CCC_HY_TRIPWIRE`). The git clock is misleading here because most files were copied or moved on 10/10–10/22. By the earliest date in the path: Oct 187 · Sep 7 · Aug 5 · Jul 2 · Jun 3 · May 1 · undated 62.

Structure: `EGBN/` hub (~190 files; copies plus Q3 8-K source set; INVENTORY.json and verifier) · `FHLB/` hub (36, of which 25 are COPIES with a 2-line source/commit/crc banner and `copies/MANIFEST.tsv`) · `market-technicals/` (25) · 3 top-level files (CCC_HY definitional source, plus 2 pointer stubs to `archive/research/`) · `outputs/` empty.

**Method for eligibility (Inferred; mechanical approximation of the root Data Hygiene rule):** a file counts as >60 days old when its content date is before 2026-08-31. Content date is the earliest path date, else the first-add date from `git log --follow --diff-filter=A`. A file counts as "referenced by a live doc" when its basename appears in REGINALD root `*.md`, `workbook/`, `scripts/`, `registry/`, `thesis/`, `trade/`, or any dated report/research file with a date on or after 8/31. README, INDEX and INVENTORY files are excluded as referrers, per clause ②. Boot-read status was not separately checked; none of these files is in a boot read list as far as I saw. Clause ① (pending dated events) was not applied mechanically. Output is at `scratchpad/elig.txt`.

| Area | Older than 60 days | No live reference (eligible candidates) | Notes |
|---|---|---|---|
| research/ | 34 | **21** | 18 are **FHLB/copies/** (hub copies; the source of each lives elsewhere, and retiring a copy is a design choice, not hygiene) + EGBN/historical/per-bank EARNINGS_PREP, EXTERNAL_PROMPTS, KB_INDEX (copies of archive files) |
| reports/ | 20 | **12** | Includes DO-NOT-TOUCH items: `2026-07-20_ZION_Q2_grade` **+ `_STAGING`**, `2026-07-22_WAL_Q2_stage2_grade`, the 7/18 HBAN and ZION scaffolds; also all four 8/13 slate reports, 8/23, and the two 8/28 reports |
| domain/ | 20 | **10** | `HIDDEN_CRE_{CONSOLIDATED,SCREEN_Q4_2025,TREND}.xlsx` (2/23), capital-rewrite KBRA, KB_ADDITIONS and SOURCE_MEMO (3/27), APOLLO_INTERCONNECTION, FDIC_QBP_Q4_GEOGRAPHIC, WAL_PRIOR_RESEARCH_EXTRACTS, FL_MIGRATION_REFERENCE |
| sources/ (root) | 4 | **3** | Trepp ×2 (2/10), SSB_Q4_2025_Earnings.docx |
| **Total** | **78** (+ board, earnings_briefs: both referenced) | **46** | |

Caveats on the 46:
1. **Basename matching produces false positives for generic names** (STATUS.md, THESIS.md, KB.tsv, INDEX.md). The EGBN/historical copies of those names showed as "ref", and the path-qualified grep finds only INVENTORY.json and research/EGBN/README:91 (an index). The true count is therefore **up to 6 higher** (≈52).
2. **Clause ① or DO-NOT-TOUCH removes at least 5 report candidates** (ZION grade, ZION STAGING, WAL stage-2, the 7/18 scaffolds). **Net actionable is about 41, of which about 21 are hub copies.** The genuinely retirable, non-copy, non-protected set is **about 20**: domain 10 + sources 3 + reports ~7 (8/13 ×4, 8/23, 8/28 ×2).
3. FL_MIGRATION_REFERENCE is cited by `CLAUDE.md`, but that hit was missed because CLAUDE.md lists it in a FILES table. Per clause ② a table row is an index, so the file stays eligible. This needs a judgment call.

**Sample-verified references (Verified):**
- `reports/2026-07-30_bank-side-HY-attribution.md` → STATUS:60, CLAUDE:152, TRADE.md. **Live, keep.**
- `research/CCC_HY_TRIPWIRE_2026-06-25.md` → STATUS, VX.tsv, README "⛔ DO NOT ARCHIVE". **Keep.**
- `domain/WAREHOUSE_EXPOSURE.md` (4/14, unbannered) → only `STATUS_DASHBOARD.md` (a cold satellite, which counted as live in the 10/22 retirement). **Keep, borderline.**
- `domain/sources/HIDDEN_CRE_*.xlsx` → no live reference. The only non-archive mention is DECK_EVIDENCE.md, and that is to `RP-REG-6`, not the xlsx. **Eligible.**

**Stale index row (🟡, Verified):** `research/README.md:20` lists `WAL_10Q_DRILL_2026-05-21.md` as a live file "(this directory)". It was archived 9/02 (`01562e8d5`) and now exists only at `archive/research/WAL_10Q_DRILL_2026-05-21.md`. The README footer also still reads "*Updated 2026-07-17*" above later appended notes.

**Duplication (🟡, Verified):** 84 of 129 files in `research/EGBN/sources/` are byte-identical twins of `domain/sources/<same rel path>` (28.4 MB). `domain/` is 150 MB, `research/EGBN` 36 MB and `archive/per-bank` 99 MB. This is by design: Will asked for "physical report/source copies … originals stay authoritative" (EGBN README:3). It is guarded by `verify_inventory.py`. **I ran that script read-only at 16:4x: rc=1, 193 files checked, 0 copy errors, and 3 originals changed since the 10/20 capture** (`workbook/KB.tsv`, `PREDICTIONS.tsv`, `VX.tsv`). The `research/EGBN/data/workbook/` extracts of those three ledgers are now behind their originals. They are labelled "Snapshot captured October20" (data/README:3), so this is honest, but the verifier's rc=1 is not wired to anything I found.

## D. Contradictions / one-figure violations (receipts)

| # | Sev | Finding | Receipt | V/I |
|---|---|---|---|---|
| D1 | 🟠 | **The KILL-ON-SIGHT OZK `37.6%` is unflagged in a live-cited report.** `reports/2026-07-30_bank-side-HY-attribution.md:122` reads "OZK … **hidden CRE 37.6% — worst in my screen**". It was written 7/30, before the 8/07 refutation, and has one commit ever (`7ab9579b1`). The file has no banner (head:1–5) and no correction (grep for struck/kill/dead/correction/9.35 returns only line 51, unrelated, and §D1 at :157, a TERRY correction). STATUS:60 and CLAUDE:152 ("Full test→") send every REG-T-03 reader there. Line :125 "ZION hidden CRE 1.8% — cleanest" is the same legacy screen basis | `grep -n '37\.6%' reports/2026-07-30_bank-side-HY-attribution.md` → :122; `grep -n bank-side-HY-attribution STATUS.md CLAUDE.md TRADE.md` → STATUS:60, CLAUDE:152 | Verified |
| D2 | 🟠 (out of my cluster, noticed) | **The live `workbook/KB.tsv` has 4 rows that assert `37.6%` as validating, with no flag:** ML-REG-098 ("validates WAL 24.2% and OZK 37.6% … as systemic"), -115, -129, -133. Only ML-REG-075 carries a flag. There is no MI3 note in the KB header lines and no superseding row cites these IDs. KB is append-only, so the fix is a correction row or header note, never an edit. These rows are also copied into `research/EGBN/data/workbook/KB.tsv:15-16` | `grep -n '37\.6' workbook/KB.tsv` → lines 86,109,129,139,143; per-row flag test = 1,0,0,0,0 | Verified |
| D3 | 🟡 | **3 legacy xlsx carry 0.3757 (=37.6%) with no banner or sidecar:** `domain/sources/HIDDEN_CRE_SCREEN_Q4_2025.xlsx` (Risk Rankings!A15 "OZK is the most extreme: 37.6% of C&I is hidden CRE"), `_CONSOLIDATED_ANALYSIS.xlsx` (Q4 2025 Screen!F5, OZK Detail!B22), `_TREND_ANALYSIS.xlsx` (OZK Trend!B22, Comparative Summary!B12). No live doc cites them. **Retire them, which fixes it** | openpyxl cell scan | Verified |
| D4 | 🟡 | `archive/per-bank/EGBN/EXTERNAL_PROMPTS.md` repeats **547%** 5 times (:32, :53, :88, :106, :150) with no banner. The same text is copied to `research/EGBN/historical/per-bank/`, which is fenced at directory level by EGBN README:91 ("historical and frozen"). Archive location plus hub fence makes this acceptable; noted because it is the one EGBN file that would re-seed 547 if pasted into an external LLM, which is its purpose | census banner = "-" | Verified |
| D5 | 🟡 | `archive/per-bank/CFG/STATUS.md` header :5 still reads "THESIS VALIDATED + FHLB FLIPPED" under only a DEAD-FIGURE banner (37.6). The FROZEN/CONTRADICTED banner was placed on CFG/THESIS and WEAKNESSES, **not on STATUS** (35 KB, the largest CFG file). The FHLB hub copy `research/FHLB/copies/REGINALD/archive-per-bank-CFG__STATUS.md` inherits this and adds a "COPY, not canonical" banner. Archive location mitigates | head -5 | Verified |
| D6 | 🟢 | **One-figure sample vs the specialist desks:** FLG `$1,571M` (loans with no allowance) in REGINALD STATUS:7 matches `AGENTS/FLG/STATUS.md:41`. STATUS keeps WAL and OZK pointer-only (STATUS "RESEARCH — POSITION NAMES": "Their version, EV and PT are never mirrored here"). No per-bank file asserts a *current* figure, because every per-bank file is archived and bannered. The EGBN hub states its figures as dated Q3 facts and defers judgment to STATUS (README:3) | grep | Verified (sample of 1 FLG figure + WAL/OZK seam rule; full cross-desk reconcile NOT done) |

## E. DO-NOT-TOUCH items re-verified

| Item | Now | Receipt |
|---|---|---|
| 7/18 pre-registered frames + graded fills + STAGING | **INTACT.** No commits since 8/07 on any `reports/2026-07-*` file except the 8/10 `53ae6a607` append to `smalltier_FL_CRE-DQ_Q2_watchcard.md` (+16 lines "RESULT-2 — COMPLETED … NO threshold above was edited"; append-only) | `git log --since=2026-08-07` per file |
| EGBN 7/25 frame and grade copies in the hub | byte-identical to `reports/` originals (`cmp` IDENT ×2). The copies are not the canon, so this is safe | cmp |
| 7/25 EGBN reserve-read discriminator | **INTACT** at `reports/2026-07-25_…:81`, and **carried verbatim into the EGBN THESIS banner** (archive/per-bank/EGBN/THESIS.md:1, "Carry the discriminator before any refresh") | grep |
| "547% FLAGGED not overwritten" | **HELD.** EGBN/THESIS body still says 547% at :13, :24, :64, :71, :108 under the CONTRADICTED banner; `archive/BANK_EXPOSURE_MATRIX_v1…:311` "🔴 547% ⚠️[CONTRADICTED — see banner]". Live matrix and STATUS_MATRIX cite 267.6% (Q2) with v1's 497/547 named as wrong | grep |
| "NOT a position name" for FITB/PNC/RF | **HELD** at THESIS:5 in all three | grep |
| ZION/TODO §0 | **INTACT** ("### 0. Stop treating thin folder as clean evidence", :9). Only commits: 5/09 create and 8/13 move | git log --follow |
| CCC_HY_TRIPWIRE "⛔ DO NOT ARCHIVE" (research README) | **HELD** in place | ls |

## F. Prior-profile items in my cluster: reconciliation

| Prior item (8/07 body) | Now | Receipt |
|---|---|---|
| Per-bank tree "ZERO banner convention" (F1 layer) 🔴 | **CLOSED by retirement.** Bannered 8/10 (15 files, both CONTRADICTED banners), archived 8/13 (6 dirs) and 10/22 (MTB) | `f69ff2963`, `f984ce53c`, §A |
| EGBN/THESIS CONTRADICTED (crisis vs de-risking; 547 vs 267.6) | **CLOSED** with a banner carrying both facts plus the discriminator; body unedited | THESIS:1 |
| CFG/THESIS CONTRADICTED-BY-SIGN-FLIP | **CLOSED** with a sign-flip banner ($12.85B, provision fell, coverage 152%). **Residual:** CFG/STATUS header still says "VALIDATED" (D5) | THESIS:1, STATUS:5 |
| EGBN 5-file contradiction cluster (INDEX "start here") | **CLOSED.** EGBN/INDEX:1 "⚠️⚠️ FROZEN 2026-08-10 — do NOT 'start here.'" STATUS, SCENARIOS and WEAKNESSES are bannered | census |
| 3 dead per-bank KB ledgers (EGBN/CFG/ZION) | **CLOSED.** All three KB.tsv carry banners and sit in archive. `ledger_staleness.py` skips `archive` (:612 `UNSCANNED_SKIP_DIRS`), so it is out of scope by design. EGBN KB_INDEX "12 rows" vs 19 non-empty lines: unchanged, archived, moot | grep |
| "Every Q2 grade landed in reports/, per-bank files untouched": the architecture question | **ANSWERED: YES, deliberate.** Grades and frames live in `reports/`, per-bank folders are archived, and EGBN gets a research hub. Q3 follows the same pattern (§B) | §B |
| ZION/THESIS broken link `../WAL/FRAUD/AUDITOR_NEXUS.md` | **CLOSED** ("re-pointed 8/10", now `../../WAL/FRAUD/…` at :25) | grep |
| 3 per-bank INDEX files point at `../WAL/`, `../OZK/` | **OPEN but moot.** FITB:32, RF:31 and PNC:32 still say `../WAL/`, `../OZK/`; under archive/per-bank these now resolve to nothing. Archived and bannered | grep |
| CORAL's 6/19 write into RF/ (two writers) | **MOOT.** RF archived | — |
| `reports/` "frozen-good, never tidy" | **HOLDS** (§E). 12 of 20 old reports are now retirement-eligible on the letter; **5+ are protected** | §C |
| MI3 repair "15+ surfaces" (core; partly mine via DECK_EVIDENCE and per-bank) | **MOSTLY CLOSED.** DECK_EVIDENCE:25 has a dated correction; FROZEN 7/09 banner at :1; INSIDER_BEHAVIOR_SCAN, RP-REG-7_OZK_THESIS, CFG/STATUS and ZION/Q1 have DEAD-FIGURE banners; NDFI_HIDDEN_CRE_HYPOTHESIS FROZEN 10/10; STATUS_MATRIX:35 KILL-ON-SIGHT; CLAUDE:127. **OPEN:** D1 (live-cited report), D2 (4 KB rows), D3 (3 xlsx), and per-bank MTB/THESIS:55 plus EGBN/THESIS:65 tables (archived and bannered, but the banner does not name 37.6) | §D |
| DECK_EVIDENCE propagation (question e) | **PROPAGATED** for OZK (STRUCK, "Do NOT use the OZK line in any deck") and WAL ("drop 'and growing'; live Q2-26 21.20%"). #2's body (:41, :44) still says "accelerating hidden CRE growth" / "jumped most aggressively". The file is FROZEN and the correction covers it in substance, so 🟡 at most | DECK:25, :41 |

## G. Ranked route list

| Rank | Sev | Finding (numbers) | Owner | Ask |
|---|---|---|---|---|
| 1 | 🟠 | D1: `reports/2026-07-30_bank-side-HY-attribution.md:122` asserts OZK "hidden CRE 37.6% — worst in my screen", unflagged, in the report STATUS:60 and CLAUDE:152 call the "Full test" for REG-T-03 | REGINALD | Append a dated DEAD-FIGURE note at the head: name 37.6% KILL-ON-SIGHT, live 9.35% legacy / 5.46% uniform basis (6/30/26), rank 5/14. Leave body :122 unedited (the "flagged not overwritten" convention) |
| 2 | 🟠 | D2: 4 live KB rows (ML-REG-098/115/129/133) assert 37.6% as validating; only -075 is flagged; header carries no MI3 note | REGINALD (route to the reader owning workbook/ for dedup) | One append-only correction row naming the 4 IDs, or a KB header line. Never edit the rows |
| 3 | 🟡 | Retirement backlog ≈20 genuine, non-copy, non-protected files older than 60 days with no live reference (domain 10, root sources 3, reports ~7); 46 on the mechanical letter (≈52 after basename false positives). The 10/22 pass covered only root files, MTB and the outbox | REGINALD | Next closeout retirement pass; exclude 7/18–7/22 frames, grades and STAGING by name (DO-NOT-TOUCH) and the hub copies (design) |
| 4 | 🟡 | D3: 3 HIDDEN_CRE xlsx carry 0.3757 unbannered (subsumed by rank 3) | REGINALD | Retire under rank 3; this removes the last unbannered numeric carrier of 37.6% outside archive |
| 5 | 🟡 | `research/README.md:20` lists `WAL_10Q_DRILL_2026-05-21.md` as live; it was archived 9/02 (`01562e8d5`); footer "Updated 2026-07-17" | REGINALD | Strike the row → `archive/research/` |
| 6 | 🟡 | EGBN Q3 facts (CRE conc 245.8%, NPA 1.75% vs 1.17%) live only in the hub; STATUS_MATRIX:31 EGBN row speaks only Q2 (dated, deferral declared until 11/07) | REGINALD | None before 11/07. At the re-score, make sure the EGBN row is replaced with Q3, not appended |
| 7 | 🟡 | `verify_inventory.py` rc=1: 3 originals (KB/PREDICTIONS/VX) changed since the 10/20 capture; hub extracts are stale snapshots (labelled) and the rc is wired to no check | REGINALD | Decide whether the extracts are refreshed or declared frozen-at-capture; either way, say which in data/README |
| 8 | 🟡 | `archive/per-bank/` and `archive/` have no README or index banner; about half the per-bank analytical files are unbannered (location-only marker); CFG/STATUS:5 "VALIDATED" header (D5); EXTERNAL_PROMPTS 547% ×5 (D4) | REGINALD | One `archive/per-bank/README.md` (frozen 8/10–10/22, live homes = STATUS, `reports/`, `research/EGBN/`; CFG STATUS "VALIDATED" and EGBN 547% are contradicted). Covers D4, D5 and the dead `../WAL/` INDEX links in one file |
| 9 | 🟢 | EGBN per-bank copied twice (archive + hub, 9/9 identical); 84/129 hub sources duplicate domain/sources (28.4 MB) | none (Will-requested design) | Record as design, not clutter: **add to DO-NOT-TOUCH** "EGBN hub copies + INVENTORY/verifier" |

**New DO-NOT-TOUCH candidates:** (a) the `research/EGBN/` copy hub with INVENTORY.json and verify/refresh scripts (Will-requested 10/20 and 10/22); (b) `research/FHLB/copies/` with MANIFEST.tsv (copy banners name source, commit and crc); (c) the 10/23 ranking-test and 10/28 borrowing-screen FROZEN files (sha-pinned, graded 11/07); (d) the FL Q3 frame until its ~11/14 final grade.

## H. Coverage (exact)

**Read whole:** nothing in my cluster was read whole.

**Read in part (line ranges):**
- `archive/per-bank/*/THESIS.md` (lines 1–6, all 7; EGBN line 1 full plus grep 547/267; CFG line 1 full) and `*/STATUS.md` (1–6, all 7).
- `research/README.md` (whole visible text, lines cut at 300 chars).
- `research/EGBN/README.md` (1–60 of ~95, cut at 400 chars).
- `research/EGBN/verify_inventory.py` (1–30, the whole script) and `data/README.md` (1–3).
- `research/FHLB/README.md` (grep "copies").
- `domain/*.md` heads (4 lines each) plus `capital-rewrite-2026/INDEX.md` 1–25.
- `domain/sources/*.md` first 2 lines; `RP-REG-7_OZK_THESIS.md` 1–6.
- reports: `2026-09-02_MTB…`, `2026-09-24_FL…`, `2026-10-09_Q3…`, `2026-10-11_CFG…`, `2026-10-23_ranking…`, `2026-10-28_borrowing…` (1–8 each); `2026-10-16_due-rows…` (1–12); `2026-10-20_reported-bank-earnings-catchup` (1–10); `2026-07-30_bank-side-HY-attribution` (1–6, 115–125); `2026-07-25_EGBN…` (grep discriminator).
- `DECK_EVIDENCE.md` (1–14, 25–27, 38–60, 214–230 of ~230).
- `STATUS.md` (5–40, grep reports/ and EGBN); `archive/RETIREMENT_2026-10-22.md` (1–15).
- prior profile (30–47 plus grep); 10/22 review (grep).

**Greps:** for `37.6%`, `547%`/`267.6`, `245.8`, `VALIDATED`, the HIDDEN_CRE and legacy-source basenames, `historical/per-bank`, and the `AUDITOR_NEXUS` and `../WAL/` links.

**Census only (mechanical, no content read):**
- all 101 `archive/per-bank` files (size, banner, newest date);
- all 267 tracked `research/` files (last-commit date, path date);
- 481 `domain/` files (count per dir); 145 `reports/` (name/date);
- the eligibility script over research, domain, reports, sources, board and earnings_briefs (`scratchpad/elig.py`, `elig.txt`);
- byte-identity cmp: EGBN historical vs archive (9), research/EGBN/sources vs domain/sources (129);
- openpyxl cell scan of the 3 HIDDEN_CRE xlsx;
- `earnings_briefs/VLY_Q1_2026.md` (banner "🧊 STALE — 2026-10-07", present), `sources/` (4 heads), `board/BOARD_LOG.tsv` (579 lines, last row 10/30, **live, not an archive**), `session_archive/SESSION_LOG_2026-03-03.md` (archive by header).

**Not read:**
- Bodies of the ~100 Oct reports and of `research/market-technicals/`, `research/FHLB/` reports, `research/EGBN/{context,reports,peer-research}`, `domain/sources/2026-10-*` receipt dirs (~451 files).
- `archive/` beyond per-bank (≈270 files), and `BANK_EXPOSURE_MATRIX.md` beyond 3 grep hits.
- Every binary (PDF/htm/xlsx except the 3 scanned).

`read_cap_check.py` was not run (not needed for this cluster). There was **no full cross-desk one-figure reconcile**: one FLG figure was sampled.

**End-of-run git state (2026-10-30 16:51:44 EDT, `date`):** `git status --porcelain -- AGENTS/REGINALD/` = **0 lines (clean)**. HEAD is `01ac975d7`; it moved from `9f0975860` because of other desks' commits, and none of them touch REGINALD. I wrote nothing under `AGENTS/REGINALD/`. The only script I executed inside the REGINALD tree was `verify_inventory.py`, which only reads, hashes and prints.
