# R2 — BROCK refresh reader 2 of 3: LEDGERS · FALSIFICATION · GUARDS

**Started:** 2026-10-30 13:17 EDT (stamped by `date`) · **Reader:** R2 (DAEDALUS Mode-A whole-profile refresh of BROCK) · **Mode:** read-only on every tracked file; this report is the only write.
**Baseline:** `AGENTS/DAEDALUS/profiles/BROCK.md` (vintage 2026-09-17, 10/21 STALE banner) — read whole (133 ln / 30,842 B).
**Tree check (start):** `git status --porcelain -- AGENTS/BROCK/` → empty (clean) at 2026-10-30 13:17 EDT.

_Sections are written incrementally; a section missing below means the reader was cut off before it._

## A. Ledger table — `workbook/` (16 files) + `docket/CATALYSTS.tsv`

Method: `grep -c '^#'` for header lines; data rows = non-`#` lines minus the column-header line; "newest cell" = max ISO date in the date column (or any cell where no date column), computed by awk/grep (commands in session, 13:18–13:25 ET). Tool verdicts from `python3 scripts/ledger_staleness.py BROCK` (default) and `--strict` (no by-name exemptions), both run 13:18 ET.

| File | Data rows | Header state (line 1 unless noted) | Content vintage vs newest cell | Tool default / `--strict` | Silent-rot verdict |
|---|---|---|---|---|---|
| `workbook/FLOW.tsv` | 27 (FLOW-BRK-001→027; status ACTIVE 10 · FIRED 6 · ARMED 7 · BUILDING 4) | LIVE two-clock `Last real data refresh: 2026-10-29` (FLOW-027 added) | newest `Last_Updated` cell 2026-10-29 = header ✅ | ok +1d / ok | ✅ LIVE, agrees |
| `workbook/VX.tsv` | 25 (VX-BRK-001→025, all 13 fields) | LIVE two-clock `2026-10-29` (VX-019; "VX-010 dated note only, value not refreshed") | newest `Last_Updated` 2026-10-29 = header ✅. But 8 rows carry `Last_Updated` 2026-05-01 or older (001/005/007/011/016/017/018 = 5/01; 002 = 3/26) — the header honestly says other rows keep their own vintages | ok +1d / ok | ✅ header true; 🟡 row-level vintages 182d (VX-002) — charter `CLAUDE.md:113` "skip rows >5 trading days old" is the only control |
| `workbook/PC_REDEMPTION_REGISTER.tsv` | 11 (+30 `#` header lines carrying GATE-BRK-R2 spec) | explicit `# Status: LIVE` override (line 1) + two-clock `2026-10-28` | max date cell 2026-11-13 (a forward date); header 10/28 = OCIC final ✅ | ok +1d / ok | ✅ |
| `workbook/PUBLISHED.tsv` | 22 | LIVE two-clock `2026-10-20 observations` (published 10/25) | newest `asof` 2026-10-20 = header ✅ | ok +10d / ok; `--nudge`: 4 STATUS-writes behind | ✅ honest; 🟡 behind 4 STATUS writes — e.g. it publishes `convergence_score`, which has not changed (58) so not wrong |
| `workbook/KB.tsv` | 397 (ids to KB-BRK-409; 12 id gaps 004/005/010/012/016/027/081–086), 13 fields every row ✅ | **no header line at all** — column header at line 1 | newest `Date` 2026-10-30 (KB-409) | ok +0d (git-commit fallback) | ✅ in practice (written every session); 🟡 no two-clock line, graded by git time. **391,710 B = 12× the 32,550 B budget** — never whole-readable |
| `workbook/PREDICTIONS.tsv` | 22, all 10 fields ✅ | no header line | newest grade 2026-10-29 (BRK-10) | ok +1d (git fallback); `--nudge` 1 behind | ✅ ledger itself current (see §B); 56,215 B = 173% of budget, declared `scoped` |
| `workbook/PREDICTIONS_ARCHIVE.tsv` | 10 | none | last row BRK-29 (7/9 move) | **exempt by name** / ⚠️ STALE +113d | 🟠 **abandoned convention, not frozen** — `PREDICTIONS_SCOREBOARD.md:3` says "Resolved rows live in `PREDICTIONS_ARCHIVE.tsv`", yet 5 rows resolved since 7/9 (BRK-27/30/02/22/10) stayed in PREDICTIONS.tsv. Neither FROZEN-bannered nor maintained |
| `workbook/PREDICTIONS_SCOREBOARD.md` | n/a (md) | `**Updated:** 2026-07-09` (`:3`) | 5 resolutions since (see §B) | not a TSV — outside every guard | 🔴 silent rot — see §B |
| `workbook/VX_HISTORY.tsv` | 14 | two-clock `# Last real data refresh: 2026-08-07` + line 2 `# LIVE append-log of VX field changes ... staleness grades from the line above, never mtime` | last row 2026-08-07. **14 commits to VX.tsv since 8/8, 0 to VX_HISTORY** (`git log --since=2026-08-08 -- …`); VX-BRK-020 `Status` changed RED→ORANGE 9/21 and ORANGE→RED 9/25 (git -p diff) — neither logged | **exempt by name ("history") in default mode** → never shown; `--strict` ⚠️ STALE +84d | 🔴 **declares LIVE append-log, not executed for 84 days; the default guard exempts it by filename, so the boot check BROCK runs (`--quiet`, default mode, `CLAUDE.md:48`) cannot fire on it** |
| `workbook/KB_ARCHIVE_MAR26.tsv` | 100 | none | last date 2026-12-31 (a forward cell) | exempt / ⚠️ STALE +218d | 🟡 **not an archive but a partial COPY**: 89 of its 100 ids are also in KB.tsv, **12 of those 89 differ** between the two files; 11 ids (004/005/010/016/027/081–086) exist only here. Two non-identical copies of one id |
| `workbook/SCHEMA.tsv` | 13 | none | n/a (data dictionary) | exempt / ⚠️ STALE +232d | ✅ dictionary; KB still 13-field so schema still matches |
| `workbook/BANK_BDC_MATRIX.tsv` | 33 | `# FROZEN 2026-07-04 — not maintained; STATUS is canonical…` + unfreeze condition ("Unfreeze only if reactivated as a live tracked surface") | n/a | FROZEN +117d | ✅ correctly dead |
| `workbook/BDC_CASH_COVERAGE.tsv` | 9 | `# FROZEN 2026-06-26 — last data 2026-02-23…` | max cell 2026-03-06 | FROZEN +126d | ✅ correctly dead |
| `workbook/LEDGER_GLOB` | 1 line: `workbook/*.tsv docket/*.tsv` | — | — | honoured: perimeter line "13 ledger(s) scanned" now includes `docket/CATALYSTS.tsv` | ✅ **NEW since 9/17** (prior profile §4 "LEDGER_GLOB does not exist" → CLOSED) |
| `workbook/RESEARCH_INDEX.md` | 19 ln | `# BROCK research index — October 25, 2026 closeout` | — | not a ledger | ✅ nav surface |
| `workbook/STATUS_ARCHIVE_MAR26.md` | 176 ln | `**Updated:** Mar 25, 2026` | — | not a ledger | 🟡 an archive living in `workbook/` not `archive/` |
| `docket/CATALYSTS.tsv` | 67 | none (8-col header) | newest dated row 2027-06-30; see §F | ok +0d (git fallback) | ✅ now IN the guard perimeter via LEDGER_GLOB; see §F for content |

**Perimeter line (default run):** `13 ledger(s) scanned; 4 TSV(s) NOT scanned by this pass: registry/corrections_receipts.tsv, research/2026-10-14_wave/fsk_may8_commitments.tsv, research/2026-10-29_arcc-mfic-shared/PAIRS.tsv, research/NDFI_BANK_LEVEL_Q4_2025.tsv`. "13 scanned" but only 9 rows print in default mode — the 4 by-name-exempt files (KB_ARCHIVE, PREDICTIONS_ARCHIVE, SCHEMA, VX_HISTORY) are counted as scanned and silently suppressed. **That count reads as coverage it does not deliver** (🟡, DAEDALUS-side tool presentation; the 🔴 consequence is VX_HISTORY above).

**`--nudge` (13:18 ET):** rc=1 — `STATUS moving without ledgers — 5 ledger(s) behind: PUBLISHED.tsv (4 STATUS-writes behind), PC_REDEMPTION_REGISTER.tsv (3), FLOW.tsv (2), VX.tsv (2), PREDICTIONS.tsv (1)`. Expected for an EVENT-DRIVEN desk; no `Cadence:` declarations exist in any header to quiet it correctly (🟡).

## B. Predictions

**Counts by Status (ledger of record, 13:19 ET):**
```
$ awk -F'\t' 'NR>1{print $6}' AGENTS/BROCK/workbook/PREDICTIONS.tsv | sort | uniq -c
      9 OPEN
      1 PARTIAL
      5 REMOVED
      3 RESOLVED-FALSE
      1 RESOLVED-FALSE-LETTER
      1 RESOLVED-TRUE
      1 STUCK
      1 SUPERSEDED
```
22 rows, every row NF=10 ✅. Prior profile (9/17) read 13 OPEN · 1 PARTIAL · 5 REMOVED · 1 SUPERSEDED · 1 RESOLVED-TRUE · 1 RESOLVED-FALSE-LETTER. Movement since: BRK-02 → RESOLVED-FALSE (10/2), BRK-22 → RESOLVED-FALSE (10/28), BRK-10 → RESOLVED-FALSE (10/29), BRK-32 → STUCK. Status vocabulary has grown to 8 tokens with no declared enum (`STUCK` is new; `RESOLVED-FALSE` vs `RESOLVED-FALSE-LETTER` both live) 🟡.

**Rows past `Resolve_Date` still OPEN:** **none.** OPEN/STUCK/PARTIAL resolve dates: BRK-04/06/11/16/18/25/26 = 2026-12-31 · BRK-32 STUCK = 2026-11-30 · BRK-31 = 2027-01-31 · BRK-23 = 2027-04-30 · BRK-07 = 2027-06-30. Every row whose date has passed (BRK-02 9/30, BRK-27 6/30, BRK-30 10/15) is terminal. ✅ The boot step 3 / closeout 7a pairing (`AGENTS/BROCK/CLAUDE.md:47`, `:63`) is executing.

**BRK-02 basis question (prior profile §7 Q3) — RESOLVED, letter vs grade checked:**
- Letter (`PREDICTIONS.tsv` BRK-02 col 2): *"Industry non-accruals rise to >2.5%"* — no basis named, as the prior profile said.
- Grade (col 7): FALSE 2026-10-02 on the Octus BDC Nonaccrual Report, aggregate non-accrual debt / all BDC debt **AT COST**, Q2-26 **1.90%**, down from 2.02%; instrument chosen *"on the 8/13 spec's own text (C2 population=INDUSTRY; §6 ranks class (a) 'best definition-match in principle'), not on value."*
- Verdict ✅ **the basis question dissolved rather than being ruled:** the resolver picked the cost basis — the basis the prior profile said *favours firing* — and it still read below 2.5%. A fair-value reading would be lower still (OBDC/MFIC FV < cost, `STATUS.md:50`). So no basis choice could have flipped the grade. The disagreement that *does* survive is the **statistic**, not the basis (aggregate 1.90% vs KBRA median 2.75% / DBRS average 3.4%), and it is recorded verbatim in the Result cell with *"a 'typical BDC' reading would flip to TRUE on KBRA - not the registered reading. Conflicted desk; grade goes AGAINST my book."* Invalidation ("decline 2 consecutive quarters") correctly held NOT met (one decline) → no APO-put action. Exemplary grade record.
- Residual 🟡: the resolver choice rests on an 8/13 spec ranking, not a pre-registered tie-break (the Result cell says so itself: *"No pre-registered tie-break existed"*).

**Recent grades (git `7f16f99a6` 10/30, `f7c0d3f9e` 10/29, `a30b820b4` 10/28):**

| Row | Letter | Grade | Check |
|---|---|---|---|
| L827 HTGC Q3 (WQ-511 falsifier; DOCKET:827) | *"THESIS FAILS FOR Q3 if ALL THREE hold: software book still marked ≥97% of cost AND non-accruals ≤1.0% of cost AND NAV/share ≥$12.15"* | THESIS FAILS FOR Q3 (`STATUS.md:15`, `:58`; KB-405/406) | ✅ all three legs pass on **both** perimeters: FV/cost 0.981 (label) / 0.976 (constant perimeter) ≥ 0.97; NA 0.4% ≤ 1.0%; NAV $12.26 ≥ $12.15. The relabelling break is named, and the grade survives it |
| BRK-10 HTGC NAV decline >10% | invalidation *"HTGC NAV stable or rising 2 consecutive quarters"* | RESOLVED-FALSE 10/29, ahead of 12/31 | ✅ $11.90 → $12.15 → $12.26 with three accession numbers; early grade on the invalidation letter is stated as such |
| BRK-22 ARCC div cut within 3 Q | — | RESOLVED-FALSE 10/28 on the declared Q4 dividend (8-K acc 0001628280-26-067382) | ✅ residual (board rescission before 12/29) named; mechanism-vs-threshold separated |
| L795 CABO weekly read | grade set CLOSED / NOT CLOSED / BLOCKED-BY-ORDER (primary) / press-only | NOT CLOSED (primary: no 8-K since 10/2) + hearing date press-only (`STATUS.md:13`) | ✅ two legs graded on their own source class |
| L794 CRMT eighth bridge | read feed Fri 10/30 after ~16:30 ET AND Mon 11/02 AM | baseline only 09:09 ET, *"not a grade"* (`STATUS.md:12`) | ✅ not yet due; correctly not graded |

**🔴 Scoreboard currency vs ledger.** `workbook/PREDICTIONS_SCOREBOARD.md:3` `**Updated:** 2026-07-09`; `:7` *"SCORE (fully-resolved, n=10)"*; `:11` *"7 / 10 = 70% correct · Brier 0.216"*; `:33` lists BRK-27 as *"Partial / mixed (kept active)"* (ledger: RESOLVED-FALSE-LETTER); `:56` *"12 OPEN + 2 PARTIAL as of 7/9. **Update this scoreboard whenever a prediction resolves.**"* Last commit `836548ba4` 2026-07-09. **Five resolutions since are absent** (BRK-27 60% F, BRK-30 65% T, BRK-02 75% F, BRK-22 60% F, BRK-10 50% F). Recomputed from ledger confidences (python, 13:20 ET; the n=10 figure reproduces exactly at 0.2160, which validates the method):

| Perimeter | Hits | Brier |
|---|---|---|
| Scoreboard as published (n=10) | 7/10 = 70% | 0.216 |
| All 15 resolved | **8/15 = 53.3%** | **0.2543** |
| Excluding BRK-27 (FALSE-ON-LETTER) | 8/14 | 0.2468 |

**The published calibration claim has flipped sign:** `:43` says Brier *"edges the 0.25 coin-flip baseline"* and the calibration read (`:39`) says the desk is *"Under-confident on the structural thesis … lean into directional structural calls"*. On the full resolved set the Brier is **0.254 — worse than a coin flip**, and the four post-July misses are all ≥50%-confidence bearish calls (BRK-02 75%, BRK-22 60%, BRK-27 60%, BRK-10 50%) — the *opposite* of the "under-confident" read. The surface still advising "lean into directional calls" is the one most likely to be consulted when the next prediction is written. This is a stated rule not executed (`:56`) on a calibration surface, and no guard covers `.md` files. **Route: owner (BROCK).**

**R-K2 reconcile (three counts disagree):** **CHANGED.** STATUS no longer prints a prediction count (grep of STATUS/NEXUS_BRIEF/SCRATCH/LAST_COMPLETION for `N OPEN`/`n=`/`Brier`: no hit outside LESSONS prose), so the disagreement is now two-way — ledger (9 OPEN + 1 STUCK + 1 PARTIAL, 6 resolved since 6/20) vs scoreboard (`:56` 12 OPEN + 2 PARTIAL; n=10) — and it **widened** from 2 missing resolutions to 5.

**PREDICTIONS_ARCHIVE convention abandoned (🟠):** scoreboard `:3` says resolved rows move to `PREDICTIONS_ARCHIVE.tsv`; since 7/9 none have (5 terminal rows remain in the live ledger; archive last row BRK-29). Either rule is fine — but the declared one is not the executed one, and the archive is neither FROZEN nor live.

## C. Falsification surface (DATED? current? where?)

**Dating (in-content, not mtime):** STATUS stamp `AGENTS/BROCK/STATUS.md:3` `**Updated:** 2026-10-30T09:1x-04:00` — 🟡 **the minutes are a typed placeholder (`1x`)**, i.e. a hand-written clock, not a `date` output (fleet memory `finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock`). Each EXIT section line carries its own fire/grade date in content (`:92` "RETIRED AS A KILL 9/2", `:97` "FIRED 8/12; Will RULED HOLD 8/13", `:106` "BRK-02 ❌ RESOLVED-FALSE 10/2", `:109` "BRK-10 ❌ RESOLVED-FALSE 10/29"). Matrix has a per-vector `Rescored` column (`:64-79`); composite rescored 2026-09-25 (`:83`). **DATED: YES. Current: YES for §1–§4 and the matrix (newest entries 10/28–10/30).**

**Rebuilt §3b inventory (as it stands 2026-10-30):**

| Surface (file:line) | Kills / flips what | Stamp (in-content) | Fired-state form | Δ vs 9/17 |
|---|---|---|---|---|
| `STATUS.md:90-93` §1 Thesis Kill | 100% PC overlay | `:3` + per-leg dates | `NOT FIRED` ×2; HY<260 `~~struck~~ RETIRED AS A KILL 9/2 (WQ-106)` with live HY 314 [10/28] | moved `:75-81` → `:90-93`; HY level refreshed |
| `STATUS.md:96-99` §2 Position-Specific | APO Dec18 $95P ×1 | "FORGE 10/14", "as of October8" | `FIRED 8/12; Will RULED HOLD 8/13` · `NOT FIRED` · `CURRENT CONDITION UNVERIFIED` (NAV-discount leg) | 🟠 the NAV-discount exit leg (`:99`) is **unverifiable at the moment** — latest RJ sector 32% as of 10/8, "same-day reading unavailable"; the refresh is a DAEDALUS 10/8 ask still owed (`:27`, "NOT worked 10/30") |
| `STATUS.md:101-103` §3 Convergence Downgrades | timeline | per-line 9/3 | `NOT FIRING — 2 of 3` | unchanged since 9/3 |
| `STATUS.md:105-110` §4 Time-Based / prediction-linked | BRK-* rows | per-row grade dates | RESOLVED-FALSE/TRUE · `STUCK` · `COUNT STAYS AT 2` · `OPEN` | BRK-02/10/22 graded; BRK-32 now STUCK |
| `STATUS.md:112` §5 TRIGGER LADDER + THESIS-KILL STEP-2 | 11 triggers; override of a compression-driven kill | heading only | **POINTER ONLY**: "rotated verbatim → `catchups/2026-10-22.md` § Rotated … Live status of every row is in §1–§4" | 🟠 **changed: off the boot read** (see below) |
| `catchups/2026-10-22.md:36` → `archive/STATUS_ROTATED_2026-09-02.md:125-140` (11-row table) + `archive/STATUS_ROTATED_2026-09-18.md:19-21` (state para "State, 9/2") | the ladder itself | **9/2** state | `2 of 11 FIRED…` | ladder last stated 9/2; three hops from STATUS |
| `catchups/2026-10-22.md:37-38` THESIS-KILL STEP 2 | override | `RUN 2026-08-28, 0 of 3 REVERSED` | ❌/❌/❌ | unchanged; off boot read, correct since STEP 2 applies only after the literal kill fires (`:38`) |
| `STATUS.md:64-79` convergence matrix (14 vectors) | per-vector score + next-level threshold | `Rescored` col (8/28 ×9, 9/3 ×3, 9/9, 9/25) | 58/70 (`:83`), arithmetic printed (`:84`) | composite 57→58 (9/25 Duration 3→4) |
| `workbook/PREDICTIONS.tsv` cols 6/8/9 | each claim | Made/Resolve dates + dated Result cells | 8 tokens (§B) | 3 more terminal |
| `workbook/PC_REDEMPTION_REGISTER.tsv:1-30` header | `GATE-BRK-R2` (a)/(b) | `# Status: LIVE` + two-clock 10/28 | (a) FIRED ×2 (North Haven 9/25, OCIC 10/2); (b) OCIC 29.8% NOT FIRED 10/28; review 2026-10-31 | (a) has FIRED since 9/17 |
| `workbook/VX.tsv` Yellow/Orange/Red/Status | per-vector level | two-clock 10/29 | 25 rows; VX-020 RED with recorded "no sustain count" disagreement | VX-020 changed twice, unlogged in VX_HISTORY (§A 🔴) |
| `workbook/FLOW.tsv` Status | pathway existence | two-clock 10/29 | ACTIVE 10 · ARMED 7 · FIRED 6 · BUILDING 4 | 25 → 27 pathways |
| `workbook/{BANK_BDC_MATRIX,BDC_CASH_COVERAGE}.tsv`, `trade/TRADE.md:1` | nothing — correctly dead | FROZEN banners | banner present | unchanged |

**🟠 The trigger ladder's "Live status of every row is in §1–§4" (`STATUS.md:112`, repeated `catchups/2026-10-22.md:36`) is false for 4 of 11 rows.** Walking the 11-row table (`archive/STATUS_ROTATED_2026-09-02.md:129-140`) against STATUS today:

| Ladder row (9/2) | Where it lives now | Verdict |
|---|---|---|
| APO >$130 ×3 → next band >$145 | §2 `:97` + watch `:44` | ✅ |
| HY <260 ×10 (observable) | §1 `:92` | ✅ |
| HY <270 ×2 (FIRED 8/27, discharged) | nowhere | ✅ historical, fine |
| Arms-length sub-90¢ print → BRK-25 | §4 `:108` | ✅ |
| First SEC enforcement filing → BRK-26 | §4 `:110` | ✅ |
| Major BDC Q2 NAV markdown >5% | nowhere (Q2-specific, graded) | ✅ spent |
| KKR adds to FSK support within 90d | carried-debt watch `:44`, **not §1–§4** — and the 90d window from the 5/11 package closed ~8/9 | 🟠 stale watch item |
| BCRED redemption / sponsor backstop refused | matrix `:66` (GATE-BRK-R2), **not §1–§4** | 🟡 lives, but not where the pointer says |
| Bank PC loss disclosure → BRK-31 | obligations `:14` + matrix `:73`, **not §1–§4** | 🟡 lives, not where the pointer says |
| **VIX spike +3 without HY widening** | **nowhere** (`grep -c VIX STATUS.md` = 0) | 🟠 **dropped silently in rotation** (or retired without a record — no retirement line found) |
| 3+ vectors 🔴→🟠 | §3 `:102` | ✅ |

**Citation chain decay (🟠):** `BRK-25`/`BRK-26` `Action_If_Falsified` still read *"(TRADE.md §9)"*; `trade/TRADE.md:5` says §9's *"only live home"* is STATUS §5; STATUS `:112` is now a pointer to `catchups/2026-10-22.md:36`, itself a pointer to `archive/STATUS_ROTATED_2026-09-02.md`. **Four hops to a 9/2-vintage table**, and the ladder's *firing* actions name an expired instrument — "BRK-25 → BIZD **Sep** $12P" (`archive/STATUS_ROTATED_2026-09-02.md:134`). The *falsified* action ("do NOT open") is harmless; the *fired* action is dead. TRADE.md:5's "only live home" sentence is now false.

**Kill-tree state:** STEP-2 substance check last RUN 2026-08-28, 0 of 3 reversed (`catchups/2026-10-22.md:37-38`); correctly dormant — STEP 2 applies only after LIQUID's 2-close `GATE-HY-REKILL` fires (`STATUS.md:112`); HY 314 [10/28] vs 260 (`:92`). ✅ 2-of-3 override rule intact (`catchups/2026-10-22.md:38`).
**Trigger-ladder state:** last whole-ladder state sentence is **9/2** ("2 of 11 FIRED…", `archive/STATUS_ROTATED_2026-09-18.md:21`). No re-statement since. 🟠 Not wrong for the rows that moved into §1–§4, but no surface states the ladder whole any more.

**Exit-rule template drift (🟡):** charter `AGENTS/BROCK/CLAUDE.md:186-189` §4 Time-Based still reads *"Q2 2026 earnings = next major resolution event (~late April/May)"* and *"If no new stress signal by Jun 2026, reassess thesis freshness"* — both dates passed; STATUS §4 has replaced them with prediction-linked reads, but the charter template that generates STATUS still carries expired dates. `CLAUDE.md:177-180` §2 still names "BCRED redemptions <2%" and "NAV discount <10%" — consistent with STATUS `:98-99` ✅.

## D. Trade leg (L4 reading A)

**Exact banner, `AGENTS/BROCK/trade/TRADE.md:1`:** `> # 🧊 FROZEN 2026-07-27 — not maintained; STATUS.md is canonical, do not cite rows as current` — followed by `:3` *"**Condition, not lifecycle:** …"*, `:5` (§9 migrated to STATUS §5, "now its only live home"), `:7` position truth → STATUS + `FORGE/STATUS.md`, TERRY constructs, `:9` disposition 7/27 in response to DAEDALUS 7/22. Last edit `c95847c8a` 10/14 (`:7` PORTFOLIO→FORGE/STATUS wording only).

**Explicit unfreeze/re-arm condition: NONE.** `grep -n -iE 'unfreeze|re-arm|rearm|thaw|lift' trade/TRADE.md` → one hit, `:16` (historical body "Stage 2 persists…"), not a condition. Compare `workbook/BANK_BDC_MATRIX.tsv:1` which does carry one (*"Unfreeze only if reactivated as a live tracked surface"*). 🟠 **Under the ladder's reading A, "declared flat/frozen" qualifies only WITH an explicit unfreeze/re-arm condition — TRADE.md has a freeze rationale, not an unfreeze condition.** `trade/NAMES.md:1` and `trade/CROSS_ANALYSIS.md:1` now carry `HISTORICAL` banners (10/14) — also without re-arm conditions.

**The other reading-A route — signals/proposals reach a consumer: MET.** BROCK→TERRY packets since 9/17 (git log `-- AGENTS/TERRY/inbox`, grep BROCK): 8 BROCK-authored packets — `2026-10-02_from-BROCK_expression-comparison-evidence.md` (commit `0a04cad71`), `10-23 WQ511-bdc-leg-pointer` (`00ca3152a`), `10-25 FSK-funded-software-correction`, `10-25 HTGC-preliminary-source-leads` (`4a047930c`), `10-25 three-followups-valuation-and-draw-results`, `10-28 ARCC-Q3-read-and-MFIC-takeout` (`81d09a51f`), `10-29 ARCC-MFIC-economics-addendum` (`90858ad28`), `10-29 HTGC-Q3-falsifier-fired` (`5e15a19cd`). Seven are in `TERRY/inbox/processed/` (consumed); the 10/29 HTGC packet is **pending** in `TERRY/inbox/`. The 10/29 packet names TERRY's card by path (`setups/CREDIT_hyg-jan15-77-74P_or_htgc-16P_REG-T-04_2026-10-23.md`, leg (b)) and states the grade's consequence for it. ✅ **BROCK's analysis is feeding TERRY's card construction in the current period (falsifier → card leg), which satisfies the consumer half without needing TRADE.md.** The live trade surface is effectively TERRY's card + STATUS §2, not `trade/`.
- 🟡 One packet admits lateness: ARCC read *"one day late (10/28 ~23:45 ET, not 10/27 pre-open), so it did not inform your 10/27 card close"* (`TERRY/inbox/processed/2026-10-28_from-BROCK_ARCC-Q3-read-and-MFIC-takeout.md:10`) — self-disclosed.
- 🟡 `trade/` working tree holds empty, untracked dirs `ARCC/ ARES/ KKR/ OWL/ WFC/ NATIONAL_DENTEX/` (`git ls-files trade` = 3 files + `trade/APO/` 4); not shown by `git status` (empty dirs). Cosmetic.

## E. Guard runs (both directions)

Tree check: `git status --porcelain -- AGENTS/BROCK/` empty before every run (13:18:19, 13:22:29, 13:23:35) and after every run (13:18:25, 13:18:31, 13:22:29, 13:22:47, 13:23:35, 13:23:48) — **no run wrote to the tree.** Every mutation was on a copy under `/tmp/claude-1000/…/scratchpad/{selfcheck,fscan,corr}/`. rc read bare (`out=$(…); rc=$?`) after a hook flagged one piped `$?` read (the falsification_scan `--agent` run; re-run bare: RC=0).

| # | Command (repo root) | rc | Key output | What PASS proves | Capable case (fires?) | Clean case (quiet?) | Verdict |
|---|---|---|---|---|---|---|---|
| E1 | `python3 scripts/ledger_staleness.py BROCK` (BROCK boot step 3 runs it `--quiet`, `CLAUDE.md:48`) | 0 | 9 rows printed: FROZEN ×2, ok ×7; "13 ledger(s) scanned; 4 TSV(s) NOT scanned" | no non-exempt workbook/docket TSV is >30d behind STATUS on its two-clock/git vintage | ✅ `--strict` same tree → rc 1, "4 stale" (KB_ARCHIVE +218d, PREDICTIONS_ARCHIVE +113d, SCHEMA +232d, **VX_HISTORY +84d**) | ✅ default mode quiet on the 7 LIVE ledgers whose headers are true | **🔴 for BROCK's use:** the default/`--quiet` form BROCK runs at boot exempts `VX_HISTORY.tsv` by filename although its own header declares it a LIVE append-log (§A). The guard *can* fire (`--strict`) but the invocation the charter wires *cannot* fire on the one silently rotting declared-LIVE ledger. 🟡 DAEDALUS-side: "13 scanned" counts suppressed exempt files as scanned |
| E2 | `… ledger_staleness.py BROCK --nudge` (root closeout 1c-bis) | 1 | "5 ledger(s) behind: PUBLISHED (4 STATUS-writes) · PC_REDEMPTION_REGISTER (3) · FLOW (2) · VX (2) · PREDICTIONS (1)" | — | fires | n/a | ✅ working; 🟡 BROCK declares no `Cadence: EVENT-DRIVEN` header, so it fires every STATUS-only session |
| E3 | `python3 scripts/corrections_boot_check.py BROCK` (boot 5b, `CLAUDE.md:54`) | 0 | "0 unreceipted NAMED rows for BROCK (register 110 row(s) … receipts on file: 21)" | every NAMED BROCK correction in `AGENTS/WALTER/registry/CORRECTIONS.tsv` has a receipt | ✅ `--receipts <copy minus COR-20261029-07> --today 2026-10-30` → **rc 1** "1 NAMED correction(s) unreceipted … COR-20261029-07 [LIVE]" | ✅ `--receipts <full copy>` → rc 0 | ✅ **both directions verified.** Newest receipts are NO-OP with a scope note (`registry/corrections_receipts.tsv` tail, e.g. COR-20261029-07 "grep of AGENTS/BROCK 2026-10-28 empty"). Coverage mode: 41/41 desks wired |
| E4 | `python3 AGENTS/BROCK/scripts/brock_selfcheck.py` (closeout 6c, `CLAUDE.md:62`) | 0 | "gates with FIRE RECORD: GATE-BRK-R2 · resolved predictions: 5 · matrix rows: 14 · CLEAN" | (1a) every future/live line naming a FIRE-RECORDed gate carries FIRED; (1b) STATUS doesn't call a RESOLVED-* row open in 5 phrasings; (2) matrix sum = composite (58), Y = 5×rows (70); (3) KB/VX 13 fields | ✅ **fires on 5 mutations:** t1 "GATE-BRK-R2 state: 0 fired" → 1a; t2 "BRK-10 still OPEN" → 1b; t4 Duration 🔴(4)→🟠(3) w/o composite change → [2] "sum 57 ≠ 58"; t5 12-field KB row → [3]; t8 future CATALYSTS row naming GATE-BRK-R2 w/o FIRED → 1a | ✅ clean copy → rc 0 | ✅ real guard, falsified-before-adoption claim holds. **Blind spots measured:** 🟠 **t7 `"GATE-BRK-R2 (a): NOT FIRED — BCRED at 2"` → CLEAN rc 0** — `"FIRED" not in live.upper()` (`brock_selfcheck.py:77`) is satisfied by the substring inside "NOT FIRED", i.e. the guard passes the exact pre-fire wording it was built to catch (the VX-BRK-004 "three at 2" class). 🟡 t3 "BRK-10 OPEN, resolves 12/31" → CLEAN (1b phrasings are enumerated, documented `:29`). 🟡 t9 CATALYSTS row "BRK-22 still OPEN" → CLEAN (1b reads STATUS only, `:88`) — yet charter trap 5 (`CLAUDE.md:28`) lists CATALYSTS among surfaces and says "`scripts/brock_selfcheck.py` checks this." Live instance of the gap: `docket/CATALYSTS.tsv:15` still reads "BRK-24/01 open to 6/30 — disposition at next session" though both resolved 7/9 (past-dated, so no check reaches it) |
| E5 | `python3 AGENTS/DAEDALUS/scripts/falsification_scan.py --agent BROCK` | **0** | "Searched: 0 falsification surfaces across 0 agents" + "🔴 MARKET AGENT, NO THESIS-CLASS FILE AND NO SURFACE THIS SCAN CAN SEE (1) … BROCK" | — | ✅ scratch copy with `Kill rail re-derived: 2026-09-01` inserted under `## EXIT RULES` → **rc 1**, "BROCK `STATUS.md:89` kill rail (in-STATUS) STALE-FLAGGED 59d" | ✅ same line with `2026-10-30` → rc 0, CURRENT | ✅ scan works both ways **once the labelled stamp exists** (`IN_THESIS_RAIL`, `falsification_scan.py:172`, added today for WAL). **🟠 BROCK carries no such stamp, so its real rail (§C) is invisible to the fleet's only falsification detector**, and the 🔴 bucket line **does not drive rc** (rc 0 in `--agent` mode). Note: `--help` is not parsed — `falsification_scan.py --help` runs the full fleet scan (read-only, rc 1 on 8 STALE rows) 🟡. 🟡 fail-open found while testing: with no `FLEET_MAP.tsv` present, `agent_classes()` (`:247-249`) returns `{}` silently and BROCK lands in "non-Market — falsification not applicable", rc 0 — the exact swallow the 8/23 fix (`:548-550`) was written against, reachable by a missing/renamed class source |
| E6 | `python3 scripts/claim_check.py --check weekday AGENTS/BROCK/docket/CATALYSTS.tsv AGENTS/BROCK/STATUS.md` | 1 | `CATALYSTS.tsv:26 "Tue 8/11" — 2025-08-11 is a Monday, not Tue` | — | fires | — | 🟡 **false positive, DAEDALUS-side tool:** the row's own date cell is `2026-08-12` and 2026-08-11 **is** a Tuesday (`python3 -c "…date(2026,8,11).strftime('%a')"` → Tue). The tool inferred year 2025 for a bare `8/11` inside a 2026-dated row. BROCK's claim is correct; STATUS weekday claims (Fri 10/30, Mon 11/02, Sun 11/01, Thu 11/05) all clean |
| E7 | `python3 scripts/read_cap_check.py --agent BROCK` | 0 | STATUS 22,729 B = **70%** · LESSONS 23,596 B = **72%** (70–75% band, "owes 812 B more" if just rotated) · SCRATCH 1,432 B = 4% (declared `BROCK:0b`) · catchups 13 members, largest 15,392 B · board_log 154,003 B declared `grep` · PREDICTIONS 56,215 B `scoped` · `rotation_due=0` | every declared whole read under budget | not mutated (DAEDALUS-owned constants; verified elsewhere) | — | ✅ STATUS 98% → 70%, LESSONS 97% → 72%, SCRATCH 142% → 4% since 9/17. 🟡 LESSONS sits in the band the tool itself cannot adjudicate |

**Other BROCK-local tooling:** `tools/soi_nonaccrual.py` (156 ln) — extractor, not a guard; not exercised (needs a live SOI fetch; out of read-only scope). Recorded as **not tested**.

## F. `docket/CATALYSTS.tsv`

67 data rows, 8 columns on every row (`awk NF` → 67×8) plus **one blank line at `:41`** in mid-file 🟡. Rows are **not date-sorted** (`sort -c` → first disorder at data line 38, 2026-11-13 before older dates) 🟡 — appended, not maintained in order.

**`date_class` values now (13:24 ET):** confirmed 23 · hard 22 · modeled 13 · soft 3 · window 2 · standing 1 · fired 1 · estimated 1 · attempted-unresolved 1 · **blank 0**. 9 distinct tokens (was 8 incl. a blank on 9/17). **No declared enum anywhere** — `grep -rn date_class AGENTS/BROCK` (excluding archive/inbox) hits only `MAINTENANCE.md:40` (column list); no script under `scripts/` or `AGENTS/DAEDALUS/scripts/` lints it. New tokens since 9/17: `soft`, `window` (rows 59, 66, 67, 69); `hard` grew from 6 to 22.

**Rows dated ≥ today (forward docket):** 2026-10-31 OCIC (`:40`, already ✅ CLOSED 10/28) · 2026-11-01 CRMT STD Sunday (`:61`) · 2026-11-05 FSK (`:60`), CABO Q3 (`:68`) · 2026-11-06 MFIC (`:65`, modeled) · 2026-11-13 BCRED Q3 10-Q (`:39`), CABO hearing (`:69`, soft/press-only) · 2026-12-03 BCRED Q4 letter (`:44`) · 2026-12-31 ARCC N-14 (`:66`, "placeholder, not a deadline") · 2027-04-30 Athene NAIC (`:38`) · 2027-06-30 ARCC–MFIC close (`:67`). STATUS obligations (`STATUS.md:12-23`) agree on every near date. ✅ The prior profile's Q4 (9/18 CRMT date missing from BROCK's docket) is moot — the whole CRMT bridge ladder is now carried (`:43`, `:54-56`, `:61`).

**Past-dated rows without a recorded outcome (🟠):** of 55 rows dated < 2026-10-30, **19** carry no outcome token (CLOSED/FIRED/✅/RESOLVED/GRADED/SUPERSEDED/RETIRED/DONE/MET) in the event cell or the first 250 chars of notes. Spot-check of 7: outcome present in prose in 3 (`:12` Form PF "largely DEREGULATORY", `:35` X1 "Settled 18 days early", `:58` CABO "READ EARLY … Next weekly read Fri 10/30", superseded by `:62`); **none recorded in 4** — `:15` still says *"BRK-24/01 open to 6/30 — disposition at next session"* (both resolved 7/9 per `PREDICTIONS_ARCHIVE.tsv`), `:20` ARCC Q2 7/29 (only the pre-registration text), `:24` CCLFX 8/7 (only the watch note), `:50` bank Q3 10/13 (provisional, "calls/final10Qs pending"). The file has **no outcome/state column**; newer rows encode it by prefixing the event cell with `✅ CLOSED <date> — …` (`:40`, `:54-56`, `:62-64`), older rows never got the treatment. Consequence: `brock_selfcheck` 1a only reads future-dated rows (`brock_selfcheck.py:69`), so nothing reads the past-dated ones at all.

**Weekday claim_check:** 1 flag (`:26` "Tue 8/11"), a tool false positive (E6). 0 true weekday errors.

## G. Reconcile prior-profile items in this cluster

| Prior item (profile line) | Now | Receipt |
|---|---|---|
| **R-K2** three live prediction counts disagree (`profiles/BROCK.md:98`) | **CHANGED — narrower but deeper.** STATUS no longer prints a count, so it is now ledger vs scoreboard; the scoreboard gap grew from 2 to **5** missing resolutions, and the published Brier (0.216, "edges coin-flip") recomputes to **0.254 (worse than coin-flip)** on the full resolved set | §B; `PREDICTIONS_SCOREBOARD.md:3,7,11,43,56`; last commit `836548ba4` 2026-07-09 |
| **R-K3** `date_class` no declared enum, no lint, one blank (`:42`, `:96`) | **OPEN (blank fixed).** 9 tokens, 0 blanks; still no enum/lint; 2 new tokens (`soft`, `window`) since 9/17 | §F; `grep -rn date_class AGENTS/BROCK` → `MAINTENANCE.md:40` only |
| `CATALYSTS.tsv` outside the staleness perimeter, charter in future tense (`:96`) | **CLOSED.** In `LEDGER_GLOB`; `ledger_staleness` scans it (+0d); charter now present-tense (`AGENTS/BROCK/CLAUDE.md:65`, `:255`). Still no READS row — by design (STATUS carries near items, `CLAUDE.md:65`) | E1 output; `CLAUDE.md:65` |
| `domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md` silent-rot middle (`:97`) | **CLOSED.** Line 1: `> **HISTORICAL — banner added October14,2026.** April2 cascade narrative is historical, not current transmission or a maintained score.` (`**Last updated:** 2026-04-02` kept at `:5`) | file `:1`, `:5` |
| `workbook/LEDGER_GLOB` does not exist (`:102`) | **CLOSED.** Created `d6371e157` 2026-10-02 ("LEDGER_GLOB (CREED adoption 1-2)"); content `workbook/*.tsv docket/*.tsv`; the tool honours it (perimeter 13) | `git log --diff-filter=A` |
| `BANK_BDC_MATRIX` / `BDC_CASH_COVERAGE` FROZEN (`:40`, `:79`) | **UNCHANGED ✅** — FROZEN +117d / +126d, banners at `:1` | E1 output |
| `PREDICTIONS_SCOREBOARD` cadence undeclared (`:133` Q6) | **OPEN.** The file does declare one (`:56` "Update this scoreboard whenever a prediction resolves") — it is the execution that is missing, ×5 | §B |
| `trade/TRADE.md` exemplar freeze banner (`:48`, `:85`) | **CHANGED.** Banner intact, but `:5` "STATUS §5 … now its only live home" is now false (STATUS §5 is a pointer to a catch-up pointer to a 9/2 archive table); still **no unfreeze/re-arm condition** | §C, §D |
| `trade/NAMES.md` Last Updated 5/01 neither frozen nor refreshed (`:100`) | **CLOSED** — `HISTORICAL` banner 10/14 (`trade/NAMES.md:1`); `CROSS_ANALYSIS.md:1` likewise | `c95847c8a` |
| §3b ladder state "2 of 11 FIRED" (`:73`) | **CHANGED** — ladder rotated off STATUS 10/22; no surface restates it whole; 4 of 11 rows are not where the pointer says, 1 (VIX +3 w/o HY) appears nowhere | §C |
| `STATUS.md` 98% / `LESSONS.md` 97% of budget (`:94`) | **CLOSED** — 70% / 72% (E7) | E7 |
| *(new)* `VX_HISTORY.tsv` | **NEW 🔴** — declared LIVE append-log, 84d silent, exempt by filename in the wired guard | §A, E1 |
| *(new)* `KB_ARCHIVE_MAR26.tsv` | **NEW 🟡** — 89 ids duplicated in KB.tsv, 12 diverge | §A |

## H. Ranked route list

| # | Sev | Finding (path:line) | Route | Ask |
|---|---|---|---|---|
| 1 | 🔴 | `workbook/PREDICTIONS_SCOREBOARD.md:3,7,11,43,56` — 5 resolutions unscored since 7/9; published Brier 0.216 "edges coin-flip" / "lean into directional calls" is now **0.254, worse than coin-flip**, with all four new misses ≥50% bearish | **BROCK (owner)** | re-score (or FREEZE-banner and move calibration elsewhere); restate the calibration read; consider adding the scoreboard to closeout 7a's write-back |
| 2 | 🔴 | `workbook/VX_HISTORY.tsv:1-2` declares a LIVE append-log; 0 rows since 8/7 across 14 VX commits incl. VX-BRK-020 RED→ORANGE→RED (9/21, 9/25); `ledger_staleness` default/`--quiet` (the form `CLAUDE.md:48` wires) exempts it by filename | **BROCK** (freeze or backfill + resume) · **DAEDALUS** (tool: a file whose own header says `Status: LIVE`/`LIVE append-log` should override the by-name exemption, as `Status: LIVE` already overrides dead-banners) | owner picks FROZEN or LIVE; DAEDALUS fixes the exemption precedence |
| 3 | 🟠 | `STATUS.md:112` + `catchups/2026-10-22.md:36` "Live status of every row is in §1–§4" — false for 4/11 ladder rows; **VIX +3 w/o HY widening row appears nowhere**; ladder last stated 9/2 | **BROCK** | restate the ladder (or retire rows on the record) in STATUS; fix the pointer sentence |
| 4 | 🟠 | Citation chain `PREDICTIONS.tsv` BRK-25/26 col 9 "(TRADE.md §9)" → `trade/TRADE.md:5` "only live home" (false) → `STATUS.md:112` → `catchups/2026-10-22.md:36` → `archive/STATUS_ROTATED_2026-09-02.md:134` (fired action names expired "BIZD **Sep** $12P") | **BROCK** | repoint BRK-25/26 to the live surface; refresh or strike the expired instrument |
| 5 | 🟠 | `trade/TRADE.md:1-9` freeze has no explicit unfreeze/re-arm condition (L4 reading A wants one); consumer half IS met via 8 BROCK→TERRY packets since 10/2 | **DAEDALUS** (grading call) · **BROCK** (one-line condition is cheap) | DAEDALUS: decide whether the TERRY-consumer route alone satisfies reading A; BROCK: add the condition anyway |
| 6 | 🟠 | Falsification rail invisible to `falsification_scan.py` (no `Kill rail re-derived:` stamp); `--agent BROCK` exits 0 over a 🔴 bucket line | **BROCK** (add the labelled stamp at `## EXIT RULES`) · **DAEDALUS** (🔴 bucket should not exit 0 in `--agent` mode) | — |
| 7 | 🟠 | `brock_selfcheck.py:77` passes "GATE-BRK-R2 (a): NOT FIRED" (substring) — the pre-fire wording class it was built for; 1b reads STATUS only while charter trap 5 (`CLAUDE.md:28`) claims CATALYSTS coverage; live miss `CATALYSTS.tsv:15` "BRK-24/01 open" | **BROCK** | tighten 1a to reject `NOT FIRED` unless leg-qualified; extend 1b to CATALYSTS/VX or narrow the charter claim |
| 8 | 🟠 | `docket/CATALYSTS.tsv` — 19 of 55 past-dated rows carry no outcome; no state column; nothing reads past-dated rows | **BROCK** | add an `outcome`/`state` column or a one-time close-out pass |
| 9 | 🟠 | `PREDICTIONS_ARCHIVE.tsv` convention (scoreboard `:3`) abandoned since 7/9, file neither FROZEN nor live | **BROCK** | pick one rule and banner the other |
| 10 | 🟡 | `date_class` 9 tokens, no enum/lint (R-K3) | BROCK | declare enum in the TSV header or MAINTENANCE |
| 11 | 🟡 | `claim_check.py` weekday false positive (year inferred 2025 for `Tue 8/11` in a 2026-08-12 row) | **DAEDALUS** (`scripts/` owner) | infer year from the row's own ISO date |
| 12 | 🟡 | `falsification_scan.py:247-249` returns `{}` silently if `FLEET_MAP.tsv` is absent → Market agents fall into "not applicable"; `--help` runs the full scan | **DAEDALUS** | fail loud on empty class map; parse `--help` |
| 13 | 🟡 | `ledger_staleness` "13 ledger(s) scanned" counts by-name-suppressed files | DAEDALUS | print the exempt count separately |
| 14 | 🟡 | `KB_ARCHIVE_MAR26.tsv` duplicates 89 KB ids, 12 diverge; `STATUS_ARCHIVE_MAR26.md` lives in `workbook/` | BROCK | banner as superseded copy or move to `archive/` |
| 15 | 🟡 | `STATUS.md:3` stamp minutes typed as `09:1x`; charter `CLAUDE.md:186-189` exit-§4 template carries expired dates (Apr/May, Jun 2026); `STATUS.md:44` "2nd KKR support package at FSK within 90d" window closed ~8/9; `CATALYSTS.tsv:41` blank line, rows unsorted | BROCK | housekeeping |
| 16 | 🟡 | DOCKET L186 "next-BROCK-session" (PENDING since 8/13) carried at `STATUS.md:36` through many sessions — a session-keyed date never fires | PROME / BROCK | give it a calendar date (W3 grades 11/30) |

**Strengths to keep (✅):** BRK-02 grade record (resolver chosen on spec text, disagreement and conflict recorded, cost-basis chosen and still FALSE); L827 HTGC grade survives both perimeters; `corrections_boot_check` verified both ways; `brock_selfcheck` real and falsifiable on 5 mutations; two-clock headers on FLOW/VX/PUBLISHED/PC_REDEMPTION_REGISTER all **true** against their newest cells; no OPEN prediction past its Resolve_Date; read-cap rotation executed (98%→70%); BROCK→TERRY falsifier-to-card feed live.

## I. Coverage

| Read | How | Notes |
|---|---|---|
| `AGENTS/DAEDALUS/profiles/BROCK.md` | **whole** (133 ln) | baseline |
| `AGENTS/BROCK/CLAUDE.md` | **whole** in 2 chunks (1–130, 130–271; final line 271 reached) | |
| `AGENTS/BROCK/STATUS.md` | **whole** (116 ln) | |
| `workbook/` 16 files | heads (first 4 lines, ≤700 chars) of all 16; column-scoped awk/grep over every TSV | `KB.tsv` (391,710 B), `PREDICTIONS.tsv` (56,215 B) **never read whole** — awk/cut only. `PREDICTIONS_SCOREBOARD.md` whole (56 ln, lines cut at 400 chars). `RESEARCH_INDEX.md`, `STATUS_ARCHIVE_MAR26.md`, `SCHEMA.tsv`: head only |
| `docket/CATALYSTS.tsv` | column-scoped awk; full row text for `:12,15,20,24,26,35,50,58` and all rows ≥10/20 (cells truncated at 70–330 chars) | not read whole (49,425 B) |
| `trade/TRADE.md` | `:1-16` + grep; `NAMES.md`/`CROSS_ANALYSIS.md` `:1-6` | §1–§8 body **skipped** (frozen record, not in scope) |
| `scripts/brock_selfcheck.py` | **whole** (123 ln) | |
| `tools/soi_nonaccrual.py` | **skipped** (line count only) — extractor, not a guard; needs live SOI fetch |
| `catchups/2026-10-22.md` | `:30-38` | `archive/STATUS_ROTATED_2026-09-02.md:125-140`, `_2026-09-18.md:19-24` |
| `board_log.tsv` | **not read** (out of cluster; 154,003 B) | |
| DAEDALUS/root tools | `falsification_scan.py:25-34,172,238-262,410-450`; `ledger_staleness.py` `--help` + grep; `corrections_boot_check.py --help` + grep | write paths checked by grep before every run |
| `PROME/DOCKET.tsv` | lines 185, 186, 587, 794, 795, 827, 829, 833 (cut 420 chars) | |
| `PROME/registry/READS.tsv` | BROCK rows 229–247 (cut 200 chars) | |
| TERRY inbox | filenames + git log since 9/17; heads of 2 packets | |
| **Not covered** | `LESSONS.md`, `SCRATCH.md`, `MAINTENANCE.md`, `NEXUS_BRIEF.md`, `EXPECTED_SIGNALS.md`, inbox/, research/, domain/sources/ | other readers' clusters |

**Tree check (end):** see final line.
**Tree check (end):** `git status --porcelain -- AGENTS/BROCK/` → empty (clean) at 2026-10-30 13:26:09 EDT. Report complete.
