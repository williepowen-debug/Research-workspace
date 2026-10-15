# RED desk audit — findings ledger

**Auditor:** cold read-only auditor (spawned by team-lead) · **Run:** 2026-10-15, 10:33–10:50 ET (from `date`) · **Repo HEAD at start:** `75e1b12b3`
**Scope:** `AGENTS/RED/` only. Read-only, with one exception, disclosed here: `gen_trigger_scan.py --help` does not parse `--help`. It **regenerated** `registry/FALSIFICATION_TRIGGERS_SCAN.tsv`. The output was byte-identical: `git diff --stat` was empty, and `--check` afterwards printed "SCAN VIEW current". So nothing changed on disk, but the script's behaviour is itself finding 2.1.

⚠️ **The tree was being edited while I audited.** During the run the desk owner's session git-mv'd `challenges/KRE_*` into `archive/` and modified `KB.tsv`, `PREDICTIONS.tsv`, `scripts/base_rate_review.py`, `archive/README.md` and `workbook/KRE_EXECUTIVE_SUMMARY.md`. Findings on those files are as of about 10:36 ET. Where a finding changed during the run, the row says so: `review_debt` showed KB 28 → 0 rows past Stale_By, and the RED-25 timeframe was reformatted.

### Commands run (all from repo root unless noted)
```
ls -laR AGENTS/RED ; find AGENTS/RED -type d ; find … -type f
for p in <every charter-named path>; do [ -e "$p" ] …; done          # existence sweep
.venv/bin/python3 AGENTS/RED/scripts/<each>.py --help                # scripts sweep (boot.py / review_debt / schema_check ran fully; all read-only)
.venv/bin/python3 AGENTS/RED/scripts/test_*.py                       # 4 test files
.venv/bin/python3 AGENTS/RED/scripts/schema_check.py ; gen_trigger_scan.py --check
scratchpad tsvcheck.py  (tab-split only, no csv module): per-file CRLF/LF, header col count, per-row col count, blank lines, dup first-column keys
scratchpad req.py       : SCHEMA.tsv required=Yes cells empty?  (result: none empty)
awk -F'\t' … | sort | uniq -c   : value-domain census of Status/Strength/state columns vs SCHEMA allowed_values
scratchpad links.py     : md links + backtick paths in STATUS/CALENDAR/MEMORY/SCRATCH/NEXUS_BRIEF/CLAUDE/MAINTENANCE/archive/README, resolved vs AGENTS/RED/, repo root, memory/auto; then `find -name` for bare names
scratchpad retire.sh    : git log -1 per tracked file (excl archive/, processed/) < 2026-08-16, + grep -rlF basename in *.md/*.tsv outside archive/processed
scripts/read_cap_check.py --agent RED ; scripts/ledger_staleness.py RED --quiet ; scripts/corrections_boot_check.py RED ; AGENTS/RED/scripts/review_debt.py --quiet
git log -1 --format=%ad -- <file> ; git show --stat 75e1b12b3 ; git status --porcelain -- AGENTS/RED
```

---

## 1. Charter vs reality (`AGENTS/RED/CLAUDE.md`)

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 1.1 | ❌ | CLAUDE.md:40 (boot 1.5) | The charter says WALTER no longer pushes to this lane: "WALTER no longer pushes per-signal handoffs to `inbox/WALTER/`". Step 5.5 (L53) says the same lane is "LIVE". These are two live, contradictory statements, and a WALTER push landed today. | `inbox/WALTER/SIG-W-20261015-001-handoff.md` (delivery 2026-10-15T14:34Z, `to: RED`, PRIORITY) | Delete the 1.5 parenthetical. Keep 5.5 as the single statement of lane status. |
| 1.2 | ❌ | CLAUDE.md:87, :279, :289 (W6 + workbook table + Rules) | The charter still says "break-pathway moves → `FLOW.tsv`" and "Break pathway identified → add row to FLOW.tsv". The file itself is banner-frozen. | `workbook/FLOW.tsv:1` "# FROZEN 2026-07-05 -- NOT maintained" | Replace the three FLOW instructions with "FROZEN 7/05; break logic lives in VX/CHALLENGES". |
| 1.3 | ❌ | CLAUDE.md:86 (W5) | W5 says "`archive/handoffs/` is FROZEN", but the charter's own Archive table (L265) says that path was DELETED 2026-06-30. | `[ -e archive/handoffs ]` → MISSING | Drop the `archive/handoffs/` clause from W5. |
| 1.4 | ❌ | CLAUDE.md:256 (Working Directories) | The charter lists `competing-hypotheses/` ("Alternative scenario files"), but the directory does not exist. | existence sweep → MISSING | Remove the row, or say the hypotheses live in STATUS. |
| 1.5 | ⚠️ | CLAUDE.md:257 | `counter-evidence/` is described as "By-agent counter-evidence logs (CARL/, SAM/, etc.)". It holds one file, `KRE_BULL_CASE.md`, and no per-agent subdirectories. | `find counter-evidence` → 1 file | Re-describe the directory as it is, or retire it. |
| 1.6 | ⚠️ | CLAUDE.md:293 | The charter says "Old 7-col files archived as `*_old_7col.tsv` for reference", but no such files exist anywhere. | `ls workbook/*_old_7col*` → none; `find . -name '*old_7col*'` → none | Delete the rule. |
| 1.7 | ⚠️ | CLAUDE.md:53 (5.5) | The cited path `inbox/2026-07-09_from-WALTER_pull-complete-exemption.md` does not exist. The file is at `inbox/processed/…`. | existence sweep | Re-point to `inbox/processed/`. |
| 1.8 | ⚠️ | CLAUDE.md:54 (5.5) | The `inbox/WALTER/processed/` count is wrong: the charter says "117 files", the directory holds 138. | `find inbox/WALTER/processed -type f \| wc -l` → 138 | Drop the count; a count in a charter goes stale. |
| 1.9 | ⚠️ | CLAUDE.md:41 (1.5 b1) | The charter says "all 12 cluster sections", but `/BOARD/INDEX.md` has 13 cluster sections, including `LABOR_DOWN`. | `grep '^## ' BOARD/INDEX.md` → 13 after "Cluster overview" | Say "every cluster section" with no number. |
| 1.10 | ⚠️ | CLAUDE.md:250 | The charter says "sole canonical, RED-01…19", but PREDICTIONS.tsv runs RED-01…RED-25. | `awk -F'\t' 'NR>1{print $1}' workbook/PREDICTIONS.tsv` | Say "RED-NN" with no upper bound. |
| 1.11 | ⚠️ | CLAUDE.md:281 (SCHEMA row) | The registry is called "`registry/FALSIFICATION_TRIGGERS.tsv` (15-col)", but it has 19 columns. STATUS.md:57 calls it "18-col since S39". | `schema_check.py` → `FALSIFICATION_TRIGGERS.tsv 19 19 ok` | Remove column counts from prose; SCHEMA.tsv is canonical. |
| 1.12 | ⚠️ | CLAUDE.md:281 | The charter quotes "`ML.Thesis_Impact` = 104 distinct values on 167 rows". The live figures are 225 distinct values on 296 rows. | `cut -f11 ML.tsv \| sort -u \| wc -l` → 225 | Mark it as an S30 measurement, or drop it. |
| 1.13 | ⚠️ | CLAUDE.md:226-235 (WHAT YOU OWN → Core Files "read at boot") | `OUTBOX.md` (201,312 B) and `docket/CATALYSTS.tsv` are listed as "read at boot". No boot step reads OUTBOX, and reading it whole would be 6× the 32,550 B budget. | `wc -c OUTBOX.md`; boot steps 0–9e | Move OUTBOX to a "written, not boot-read" row. |
| 1.14 | ⚠️ | CLAUDE.md:220-293 (ownership tables) | The ownership tables omit live owned paths: `registry/` (5 files), `scripts/`, `outbox/` incl. `outbox/kernel/`, `design/`, `handoff_WALTER/`, `board_log.tsv`, `NEXUS_BRIEF.md`, `CHALLENGE_IMPACT_LEDGER.md`, `.claude/`. | `find . -type d`; tables at L220–293 | Add one table row per live directory or file. |
| 1.15 | ⚠️ | CLAUDE.md (whole) | The charter never names `scripts/nonsession.py` or the four `scripts/test_*.py`, and gives no step that runs the tests. | `grep -c nonsession CLAUDE.md` → 0; same for `test_` | Add a 9b-adjacent line: "after editing boot.py/base_rate_review.py run `scripts/test_*.py`". |
| 1.16 | ⚠️ | CLAUDE.md:265-266 (Archive table) | Two struck-through rows for deleted paths remain. They are clearly labelled, but `RED_SKELETON.md` appears on both rows, and CLAUDE.md:347 (anti-patterns) still names `RED_SKELETON.md`. | rows at L265–266, L347 | Collapse to one row and point history to MAINTENANCE.md. |
| 1.17 | ⚠️ | inbox/WALTER/ (boot 5.5) | One action-addressed signal sits in the lane with no `board_log.tsv` row. It is untracked in git and arrived about 1 minute after the S53 boot reported "Inbox 5 → 0". | `boot.py` §⑤: "ALERT 1 action-addressed signal(s) UNLOGGED … SIG-W-20261015-001"; `git status` `??` | Disposition it, log `source=INBOX_WALTER`, then `git mv` it to `processed/`. |
| 1.18 | ℹ️ | inbox/ (recursive) | Every directory that holds files is covered by a numbered step: `inbox/WALTER` → 5.5, `inbox/WALTER/processed` → 5.5 archive, `inbox/processed` → 5.6 archive. No uncovered delivery directory exists. | `find inbox -maxdepth 3 -type d` | None. |
| 1.19 | ℹ️ | workbook/LEDGER_GLOB | Root CLAUDE.md step 1c-bis reads `AGENTS/<NAME>/workbook/LEDGER_GLOB`, and RED has none, while 10 other desks do. `ledger_staleness` therefore uses its default perimeter and says "8 TSV(s) NOT scanned", including CATALYSTS, WATCHLINES and the registry. | `ls AGENTS/*/workbook/LEDGER_GLOB` (AEOLUS, BRENT, …); `ledger_staleness.py RED` perimeter line | Add a LEDGER_GLOB that declares RED's live ledgers. |

## 2. Scripts (`AGENTS/RED/scripts/`)

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 2.1 | ❌ | scripts/gen_trigger_scan.py | Any invocation other than `--check`, including `--help` and typos, rewrites `registry/FALSIFICATION_TRIGGERS_SCAN.tsv`. There is no argparse, only `if "--check" in sys.argv`. | `gen_trigger_scan.py --help` → "generated registry/FALSIFICATION_TRIGGERS_SCAN.tsv: 12 rows"; code L62 | Add argparse; reject unknown args; make writing an explicit `--write`. |
| 2.2 | ❌ | scripts/schema_check.py | It compares the header only and never counts columns per row. It printed "ML.tsv 14 14 ok … ✅ ALL CONFORM" while 9 ML rows have 13 cells (finding 3.1). The charter calls it the structural verifier ("Verify with `scripts/schema_check.py`, don't eyeball it"). | `schema_check.py` output vs tsvcheck (ML rows 249–257) | Add a per-row `len(cells)==len(header)` check that exits 1. |
| 2.3 | ⚠️ | scripts/schema_check.py | It does not check value domains, by design per its docstring. That is why the out-of-domain tokens in 3.5–3.9 are invisible to every instrument. | docstring; finding 3.5–3.9 | Add an advisory `--domains` mode for the token-enum columns. |
| 2.4 | ⚠️ | scripts/boot.py:399-417 (§③) | ① The catalyst countdown is unsorted and prints in TSV row order: T-6, T-1, T-6, T-1, T-5, T-4, T-0, so today's item prints last. ② The `startswith("pending")` filter makes any row whose status is not a canon token invisible, including the overdue one (finding 3.6, CATALYSTS row 69, status `🔴`, dated 9/14). | boot.py output §③; code L401–402 | Sort by date; print non-terminal unknown-status rows as ⚠️ instead of skipping them. |
| 2.5 | ℹ️ | scripts/nonsession.py | It is an importable module with no CLI: `--help` prints nothing and returns rc 0. `boot.py:137`, `base_rate_review.py:67` and the tests import it. It is mentioned once in MAINTENANCE and never in the charter. | `--help` run; grep imports | Name it in the charter (see 1.15). |
| 2.6 | ℹ️ | scripts/test_*.py | All pass. test_base_rate_flag: PASS 9/9 · test_board_gap: 8/8 · test_nonsession: 13 PASS lines out of 15 output lines · test_tie_atoms: 8/8. | runs above | None. |
| 2.7 | ℹ️ | scripts/ inventory vs charter | Every charter-named script exists: boot, schema_check, gen_trigger_scan, review_debt, base_rate_review, board_log_append. So do the root scripts it names: ledger_staleness, corrections_boot_check, read_cap_check, safe-push. Scripts the charter does not mention: nonsession.py, test_base_rate_flag.py, test_board_gap.py, test_nonsession.py, test_tie_atoms.py. | existence sweep; `grep -c <name> CLAUDE.md` | See 1.15. |
| 2.8 | ℹ️ | research/__pycache__/violet_skew_recheck.cpython-312.pyc | An orphan bytecode file (14 KB, dated Apr 19) whose source no longer exists anywhere. It is gitignored. | `ls research/__pycache__`; `git check-ignore` | `trash` the directory. |

## 3. TSV contracts (workbook/, registry/, docket/, board_log.tsv)

Per-file summary: all files are LF except `docket/WATCHLINES.tsv`, which is CRLF on all 13 lines. Headers match SCHEMA.tsv for all 13 covered files. No `required=Yes` cell is empty. ID-keyed files (KB, VX, ML, CHALLENGES, PREDICTIONS, FLOW, registry ×3) have no duplicate primary keys.

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3.1 | ❌ | workbook/ML.tsv lines 249–257 (ML-RED-248 … ML-RED-256, S45 2026-09-14) | These 9 rows have 13 cells against a 14-column header. The `Status` cell is missing, so every later column is shifted left: Status reads `A1` (that is the Confidence value), Confidence holds Thesis_Impact prose, and so on. | tsvcheck "MISMATCH … total 9"; `sed -n 249p` field dump; commit `bac98a001` | Insert the missing Status cell (tab) in all 9 rows; add the 2.2 guard. |
| 3.2 | ❌ | docket/CATALYSTS.tsv row 69 (2026-09-14, "VX.tsv scheduled re-review") | The status cell is the emoji `🔴`. That is not a status token, so the row is neither pending nor resolved. It is 31 days past its date and invisible to boot §③. | `awk -F'\t' 'NR==69{print $8}'` | Resolve it with an outcome (the VX pass ran S52-late). |
| 3.3 | ⚠️ | registry/FALSIFICATION_TRIGGERS.tsv lines 14–15 | Two blank trailing lines follow the last row. | tsvcheck "BLANK lines: [14, 15]" | Strip them. |
| 3.4 | ⚠️ | docket/WATCHLINES.tsv | It is the only CRLF file in RED. MAINTENANCE.md:636 says the opposite: that "VX.tsv, KB.tsv, CATALYSTS.tsv, CHALLENGES.tsv are CRLF" while ML and VX_HISTORY are LF. All four named files are now LF. An editor following MAINTENANCE would preserve or reintroduce the wrong ending. | `CRLF=13 LF=13`; MAINTENANCE.md:636 | Normalise WATCHLINES to LF and mark the MAINTENANCE line as historical. |
| 3.5 | ⚠️ | workbook/ML.tsv col Status | Out-of-domain values: `A1`×9 (from 3.1), `CURRENT`×5, `EXECUTED`×3, `FIXED`×2, `REGISTERED-PRE-DATA`, `PACKETED-TO-OWNER`, `IMPLEMENTED+TESTED (not independently verified)`, `DELIVERED-FAIL`, `CORRECTED`. | `cut -f9 \| sort \| uniq -c` vs SCHEMA allowed | Map them to canon or widen SCHEMA. |
| 3.6 | ⚠️ | docket/CATALYSTS.tsv col status | Out-of-domain values, against SCHEMA `pending;resolved;expired;superseded`: `resolved-gone`, `resolved-overtaken`, `redated-2026-08-04`×2, `resolved-unverified`, `RESOLVED-PARTIAL`, `🔴`. | `awk` census | Normalise to canon; carry the qualifier in notes. |
| 3.7 | ⚠️ | workbook/KB.tsv col Status | Values not in SCHEMA: `DATED-HISTORICAL`×9, `CURRENT`×4, `RESOLVED-GRADED`×3, `LIVE`×3, `SUPERSEDED-BY-REGIME`, `RESOLVED-SUPERSEDED`, `RESOLVED-NOT-MET`, `ACTIVE-UNREFRESHED`. Charter 9c prescribes "re-class `DATED-HISTORICAL`", yet SCHEMA does not list it. | census vs SCHEMA KB.Status | Add DATED-HISTORICAL to SCHEMA; map the rest. |
| 3.8 | ⚠️ | workbook/VX.tsv col Strength | Values not in SCHEMA: `WEAK-BULL`, `RESOLVED-SUPERSEDED`, `RESOLVED-CONFIRM-DEAD`, `FLIPPED-BEAR-TERMINAL`, `FLIPPED-BEAR (10/02; own Flip_If met)` (prose inside a token cell). | census | Put the qualifier in Notes; add the terminal tokens to SCHEMA. |
| 3.9 | ⚠️ | registry/FALSIFICATION_TRIGGERS.tsv col state | FT-08 `FIRED 2026-10-14 (Sept CPI); exit armed <2.5 s=1` and FT-10 `FIRED 2026-10-14 bar …` use the token `FIRED`, which is not in SCHEMA (`ARMED;FIRING-BANKED;FIRED-BANKED;UN-FIRED;BLOCKED`). WALTER auto-fire reads this surface. | `cut -f1,8` | Use `FIRED-BANKED` or add `FIRED` to SCHEMA. |
| 3.10 | ⚠️ | registry/FALSIFICATION_TRIGGERS.tsv FT-10 `state_detail` | The cell opens "ARMED - NOT FIRED. SUSTAIN COUNT 0 OF 4; THE RUN THAT OPENED 09/11 BROKE…" (S46, 9/18), while `state` says FIRED 10/14. The FIRED text sits only at the tail of a 6,701 B cell. | `awk '$1=="RED-FT-10"{print substr($19,1,140)}'` | Put the current state first; fold history after it. |
| 3.11 | ⚠️ | registry FT-06 `state_detail` | The cell reads "EXIT CLOCK 0 OF 5 as of 2026-09-12 (S44)", a count stamped 33 days ago, while the row's `last_reviewed` is 2026-10-14. | same | Re-count the exit clock or say "not re-counted since 9/12". |
| 3.12 | ⚠️ | registry FT-11 (`last_reviewed` 2026-09-12; state "ARMED; 0-of-5; precondition live [2026-09-10]") | The registry has not been touched for 33 days, while STATUS.md:2 and NEXUS:73 report live readings ("−10.0 on 10/13 … likely fires on the 10/15 official close"). The near-fire is not in the canon row. | `cut -f1,16`; STATUS:2 | Write the 10/13 Δ5 reading into the canon row. |
| 3.13 | ⚠️ | registry FT-03/04/05/09 | `last_reviewed` is 2026-08-27, 49 days old. | `cut -f1,16` | Re-review them, or document the review cadence. |
| 3.14 | ⚠️ | board_log.tsv | Signal ID `2026-10-12_from-CARL_auto-outflow-preparation-and-grading-letter-gaps` is logged twice, against the charter's "do NOT double-log". | `cut -f2 \| sort \| uniq -d` | Remove one row, or annotate it as a re-disposition. |
| 3.15 | ⚠️ | workbook/CHALLENGES.tsv col Grade | Out-of-domain values: `FAIL` (CHG-052, 053) and the compound `STRONG (OZK) / MODERATE (WAL, KRE Dec-60) / WEAK (KRE Nov-67)` (CHG-054). | `cut -f4` | Add FAIL to SCHEMA; split the compound into Key_Finding. |
| 3.16 | ⚠️ | workbook/PREDICTIONS.tsv RED-23 | Timeframe `2026-11-XX` is parsed as 11/15 by `boot.py` (`XX→15`), so the due date is invented. | boot.py L380–383 | Use the BLS date once confirmed. |
| 3.17 | ℹ️ | docket/CATALYSTS.tsv | It has no primary-key column (the `date` key repeats 15 times by design), so rows cannot be cited by ID. | tsvcheck DUPKEYS on `date` | Optional: add a `cat_id`. |
| 3.18 | ℹ️ | registry/corrections_receipts.tsv, registry/basis-hashes.json, board_log.tsv | None of these is described in SCHEMA.tsv. | `cut -f1 SCHEMA.tsv \| sort -u` | Add SCHEMA rows. |
| 3.19 | ℹ️ | workbook/VX.tsv IDs | `VX-RED-022` is absent, with no mention in VX, VX_HISTORY or ML. | `grep -c VX-RED-022` → 0/0/0 | Record why in VX_HISTORY. |
| 3.20 | ℹ️ | workbook/VX.tsv header | "Last real data refresh: 2026-06-02" is deliberately pinned to the stalest live row, so `ledger_staleness` reports VX "+135d behind" on every boot until CARL re-measures VX-009. A permanently lit alarm teaches readers to ignore it. | `ledger_staleness.py RED` | Time-box the pin, or exempt VX-009 explicitly. |
| 3.21 | ℹ️ | registry/FALSIFICATION_TRIGGERS.tsv size | 113,371 B for 12 rows. FT-11's `state_detail` cell alone is 13,494 B, and FT-10's is 6,701 B. | `length($19)` | Fold history out of the cells into reports/. |

## 4. Mirror drift (Doc-Mirror table)

**Prediction tally computed from PREDICTIONS.tsv (10:41 ET): 25 rows = 13 CORRECT · 10 WRONG · 2 ACTIVE (RED-23, RED-25).**
**Open challenges per CHALLENGES.tsv:** CHG-027 ACTIVE-GRADED · 028 LIVE-RE-ANCHORED · 044 ACTIVE-CONCEDED · 045 ACTIVE · 049 ACTIVE · 054 ACTIVE (6 rows).

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 4.1 | ❌ | STATUS.md:82-96 "Currently ACTIVE" | The table lists 5 challenges that the TSV shows as closed: CHG-042 (RESOLVED 8/27), CHG-046 (RESOLVED-CONVERGED 8/28), **CHG-047 shown as "STRONG — ACTIVE" vs TSV RESOLVED-CONVERGED 2026-09-06**, CHG-048 (RESOLVED-CONVERGED 8/27) and CHG-051 (RESOLVED 10/14). | CHALLENGES.tsv col 6 | Rebuild the table from the TSV's non-RESOLVED rows only. |
| 4.2 | ❌ | STATUS.md:98 | "RESOLVED … CHG-006 through CHG-041" includes CHG-027 and CHG-028, which are both open. The line also omits 001–005, 042, 047, 051, 052 and 053. | TSV | Make it "all rows not listed above", or generate it. |
| 4.3 | ❌ | STATUS.md:113 | STATUS reads "TALLY … 10 WRONG / 13 CORRECT / 1 ACTIVE (RED-23)", but the TSV has 2 ACTIVE (RED-25 is missing). CALENDAR.md:43 says "2A" and NEXUS_BRIEF.md:31 says "1 ACTIVE", so the three mirrors disagree. | tally above | Set all three to 13C/10W/2A with a date. |
| 4.4 | ❌ | STATUS.md:66 | STATUS shows FT-06 "🔴 FIRING-BANKED"; the registry `state` is `FIRED-BANKED; exit 0-of-5 [2026-09-12]`. | registry cut -f1,8 | Copy the canon token. |
| 4.5 | ❌ | STATUS.md:11 | The banner says "⚠️ S46 (2026-09-18) supersedes the FT-10 lines everywhere below: the run BROKE … count is 0-of-4", but FT-10 FIRED 10/14 (STATUS:68, registry). This is a live instruction that now contradicts the file. | STATUS:11 vs :68 | Delete the banner. |
| 4.6 | ❌ | STATUS.md:72 | STATUS says "WL-11 Brent <95 (firing)", but boot shows WL-11 🟢 clear (105.17 vs <95). It also says "WL-07 USDJPY >160 (0.07 away)", while boot shows 2.14 away. | `boot.py` §② | Re-pull or delete the sentence. |
| 4.7 | ❌ | CALENDAR.md:25 | The row says "10/31 … CHG-051 re-review", but CHG-051 was RESOLVED 2026-10-14. | TSV CHG-RED-051 | Drop it from the row. |
| 4.8 | ⚠️ | CALENDAR.md:17 vs CATALYSTS.tsv | The L657 BRK-26 row, "10/14 (due)", has no canon row, and its due date has passed. STATUS:3 says the reading was done. The calendar has an event the canon lacks. | CATALYSTS has no L657 row | Add it to canon as resolved, or drop it from CALENDAR. |
| 4.9 | ⚠️ | CALENDAR.md:24 vs CATALYSTS.tsv row 25 | CALENDAR has IQHQ/OZK Q3 "Tue 10/20 after close / call Wed 10/21" (SCRATCH:72 agrees on 10/20); the canon row is `2026-10-21` "[DATE EST]". Canon is supposed to win, and here canon is the stale one. | row 25 | Re-date canon to 10/20 and mark it confirmed. |
| 4.10 | ⚠️ | CALENDAR.md:5 header | The header says "Last Updated 2026-10-09 (S51)" and "Event set … at 10/01 (14 rows)". The body carries S52 (10/14) content, and canon now has 15 pending rows. | `awk '$8~/^pending/'` → 15 | Restamp the header. |
| 4.11 | ⚠️ | CALENDAR.md:31; WATCHLINES WL-08 label; CATALYSTS row 30 | Canon still says "KRE Dec $60P x7". CALENDAR itself warns that FORGE shows it rolled to a Dec-31 65P, but neither the canon row nor the WL-08 label was fixed. | row 30; WATCHLINES WL-08 Label | Fix canon and label after verifying against FORGE (PROME-owned). |
| 4.12 | ⚠️ | STATUS.md:61-70 (falsification table) vs registry/boot | STATUS still shows FT-07 at "CCC 1,146 [9/28], 216bp over" (live: 1,282 [10/14]); FT-11 at "NO NEW GRADEABLE WINDOW 9/14 — FRED frontier still 09/10"; and FT-12 at "52bp away … HY 312 [FRED 9/30]" (live: 65bp, 325). | `boot.py` §②; STATUS:2 | Re-pull the rows or reduce them to tokens with a date. |
| 4.13 | ⚠️ | STATUS.md:57 | STATUS calls the registry "18-col since S39"; it has 19 columns. | schema_check | Drop the column count. |
| 4.14 | ⚠️ | NEXUS_BRIEF.md:69 vs CATALYSTS row 62 / CALENDAR:23 | NEXUS has EGBN Q3 as "~10/21 AMC (est., unconfirmed)"; canon and CALENDAR have it CONFIRMED (EagleBank IR 10/7). | row 62 | Restamp NEXUS. |
| 4.15 | ⚠️ | STATUS.md:86-96 (grade column) | The Grade column mixes status tokens: CHG-027 "ACTIVE-GRADED" (TSV grade MODERATE); CHG-028 "LIVE" (TSV status LIVE-RE-ANCHORED); CHG-049 "ACCEPTED-IN-FULL" (not a TSV token). | TSV cols 4 and 6 | Show grade and status as separate columns, copied from canon. |
| 4.16 | ℹ️ | STATUS.md:114 | STATUS has "🆕 FT-10 Wednesday conditional resolved AGAINST RED this session". That is the S46 (9/18) event, presented as new. | ML/PREDICTIONS RED-24 | Drop the 🆕 and date it 9/18. |

## 5. Stale-marked vs carried-as-current

Sampling: I read STATUS.md, CALENDAR.md, NEXUS_BRIEF.md and SCRATCH.md whole, about 45 dated or undated figures in all. Below are the inline figures that are presented as current, are older than 2026-10-09 or undated, and sit outside blocks labelled folded, historical or prior. Lines that carry an explicit STALE marker or a "kept as history" label are excluded.

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 5.1 | ❌ | NEXUS_BRIEF.md:7 | The brief says "HY OAS was **312 [FRED 9/30]** … `RED-FT-02` … ARMED, 0 of 3, 8bp away, NOT fired". The same file's L3 and L73 say 325 [10/14], 1 of 3. NEXUS is the fleet-consumed surface. | NEXUS:3,7,73 | Delete or replace the HY credit paragraph. |
| 5.2 | ❌ | NEXUS_BRIEF.md:44-46, :52 (SENDING / WAITING) | The tables are still 10/01 vintage: "FT-02 8bp away, unfired", "312 [9/30], 0 of 3", "HY OAS 10/1 obs onward". | same | Rebuild the tables. |
| 5.3 | ❌ | NEXUS_BRIEF.md:80-81 | NEXUS says the first FT-02 fire is "days to weeks away" and that "none mechanical left this week". It is now 2 cells away, and the 10/15 H.4.1 + LIQ-07 pre-stated Acute +1 sits this week. | STATUS:2 | Rewrite NEXT DECISION POINT. |
| 5.4 | ⚠️ | NEXUS_BRIEF.md:10 | NEXUS says "Thesis version: S51 weights (2026-10-09…)", but the weights are S52b (10/14). | NEXUS:30 | Restamp. |
| 5.5 | ⚠️ | NEXUS_BRIEF.md:18-22 (VIEW) | The VIEW cites HY 312, CCC 1,179, 5y5y "2.36% [9/30]", BB+B 81% and FT-12 "52bp away" as the present view, with no fold label. Only the S50 line says "RE-PULL (10/01)". | NEXUS:18–22 | Re-pull the figures, or label the section "10/01 view". |
| 5.6 | ⚠️ | NEXUS_BRIEF.md:31-32 | The brief says "RED-04 resolved CORRECT today" and "CH-009 for RED today". "Today" was 10/01. | NEXUS:31–32 | Date the events. |
| 5.7 | ⚠️ | STATUS.md:48 | The bull counter cites "CCC 1,267 (+192 since 9/22), FT-02 4bp away" (10/13 vintage). L2 of the same file has CCC 1,282 and FT-02 crossed. | STATUS:2 vs :48 | Re-pull. |
| 5.8 | ⚠️ | STATUS.md:52 | STATUS says "hypothesis weights NOT yet re-derived (after Fri NFP)", but they were re-derived S51 10/09 and moved S52. | STATUS:3, :19 | Delete the clause. |
| 5.9 | ⚠️ | STATUS.md:32 | STATUS says "⛔ The weights themselves are STILL S29 8/12 and were NOT re-derived today". This is false since S51. It also says the Key Driver cells were folded, yet L21–28 still hold S29 and S41 driver text. Row L24 (Stag) and row L27 (Soft) have 5 cells in a 4-column table. | STATUS:21–32 | Remove the ⛔ sentence; trim the rows to 4 cells. |
| 5.10 | ⚠️ | STATUS.md:107 | Priority 3 still reads "Daily FT-02 (HY >320 s=3, 315 [10/8], 0 of 3)" and "LIQ-07 asks 10/15–16". | STATUS:2 | Mark it done or restamp it. |
| 5.11 | ⚠️ | STATUS.md:116 | The heading "MISSING DATA WANTED (8/12)" survives over a pointer. | — | Fold the heading too. |
| 5.12 | ⚠️ | CALENDAR.md:33 (daily row) | The daily row has "FT-02 … (316 [10/13], 4bp, 0 of 3) · CCC 1,267" (now 325, 1 of 3, 1,282). | boot §② | Restamp the daily row at every addendum. |
| 5.13 | ⚠️ | CALENDAR.md:35 (standing guards) | "Dated Brent $114–120 vs paper ~$102" and "5y5y 2.36, flat" are 10/01 vintage and undated inline. STATUS:48 and SCRATCH:67 now say "~$29 over paper". Guard (6) in the same paragraph forbids exactly this. | CALENDAR:35 | Date or refresh the levels. |
| 5.14 | ❌ | SCRATCH.md (whole) | There is no S53 addendum section. Commit `75e1b12b3` (S53, 10:34 ET) changed the FT-02 state to 1-of-3 and corrected VX-026, touching STATUS, NEXUS, OUTBOX and the registry, but not SCRATCH. That breaches charter W-A **A2** ("always, no judgment call"). SCRATCH:9 and :53 still carry "316 [10/13], 4bp". | `git show --stat 75e1b12b3` | Write the S53 addendum. |
| 5.15 | ⚠️ | thesis/CHANGELOG.md | The S53 addendum changed a registered-trigger state (FT-02 0 → 1 of 3), but CHANGELOG was not touched. Charter W-A **A4** makes W3 mandatory when "a registered-trigger state change[s]". | `git show --stat 75e1b12b3` | Add a CHANGELOG line (or decide that a count change is not a "state" change and say so in the charter). |
| 5.16 | ⚠️ | thesis/TIMELINE.md | The file says "v3 … Last Updated: 2026-06-22", with Path A 44 / B 50 / War 6, a framework the current six-hypothesis weights have replaced. It has no FROZEN banner. The charter (CLAUDE.md:332, Key Frameworks, "Track position/expiry mismatches in `thesis/TIMELINE.md`") presents it as live. Root Data Hygiene says such files are frozen or live, never in between. | head of the file; `git log -1` 2026-06-22 | Banner it FROZEN and amend the charter line, or refresh it. |

## 6. Retirement candidates (>60 days, i.e. last commit before 2026-08-16; not in boot steps; scanned outside archive/ and processed/)

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 6.1 | ⚠️ | challenges/SSB_CHALLENGE.md (21,773 B, last commit 2026-08-07) | Zero references in any .md or .tsv outside archive/. | retire.sh | `git mv` to archive/. |
| 6.2 | ⚠️ | outbox/2026-07-24_to-PROME_chg043-premium-breadth-redteam.md (3,025 B, 07-24) | Zero references. | retire.sh | `git mv` to archive/. |
| 6.3 | ⚠️ | outbox/2026-07-24_to-PROME_s24-remark-and-grades.md (3,827 B, 07-24) | Zero references. | retire.sh | `git mv` to archive/. |
| 6.4 | ⚠️ | outbox/2026-07-29_to-PROME_fomc-graded-registry-closed-remark.md (3,864 B, 07-29) | Zero references. | retire.sh | `git mv` to archive/. |
| 6.5 | ⚠️ | research/STALENESS_AUDIT_2026-06-02.md (7,274 B, 06-02) | Referenced only by MAINTENANCE.md, which is a log and not a live analytical doc. | retire.sh | Retire. |
| 6.6 | ⚠️ | research/WAL_OZK_APR21_FRAMEWORK.md (11,703 B, 04-18) · challenges/VIOLET_SAM_RESPONSE_GRADING_2026-06-11.md (24,341 B) · challenges/VIOLET_SKEW_CHALLENGE.md (7,400 B, 04-19) · challenges/SAM_PREBOJ_STRESSTEST_2026-06-10.md (12,894 B) · outbox/2026-07-10_to-PROME_chg041-final-grade.md (2,377 B) | Referenced only from RED's append-only logs (ML.tsv, OUTBOX.md or CHANGELOG), which are records, not live docs a reader travels. Whether ML.tsv counts as "live" is the owner's call. | retire.sh | Retire if the owner rules that logs are records. |
| 6.7 | ⚠️ | MEMORY_ARCHIVE.md (23,528 B, last commit 2026-06-02) | It is charter-named as the W7 home for verbose bodies but has not been touched in 135 days, while MEMORY.md has grown to 22,096 B (some lines are over 590 chars). Either W7's "verbose body → MEMORY_ARCHIVE.md" is not being practised, or the file is dead. | `git log -1`; `awk '{print length}' MEMORY.md` | Resume W7 offload, or amend W7. |
| 6.8 | ⚠️ | CHALLENGE_IMPACT_LEDGER.md (20,298 B, last commit 07-31) | The ledger measures challenge impact over "all 43 rows … CHG-RED-001…043"; there are now 54. The charter does not name it, though the CONTRACT's "proof of consumption" is its subject. | head of file | Freeze-banner it, or refresh it and name it in the CONTRACT. |
| 6.9 | ℹ️ | LAST_COMPLETION.md (last commit 2026-08-17) | It becomes >60d eligible on 10/16. Its header "## COMPLETION — RED — 2026-08-17 STATUS: ✅ DONE" is a currency-implying name, and the charter keeps it on disk deliberately. | `git log -1` | Archive it on 10/16 (the charter already says it is never boot-read). |
| 6.10 | ℹ️ | Held (referenced live): DEBATE_OIL_TRANSMISSION (MEMORY.md), CATALYST_FRAMEWORK_APR2 (MEMORY.md), HY260 (TIMELINE/VX), handoff_WALTER/* (root CLAUDE.md, WALTER), design/JOINT_PROPOSAL (WALTER), thesis/FRAMEWORK.md, FLOW.tsv (charter-named) | Not eligible. | retire.sh | None. |
| 6.11 | ℹ️ | challenges/KRE_* (4 files) | These were being `git mv`'d to archive/ during this audit (SCRATCH #16). The staged rename is uncommitted. | `git status` RM ×4 | Commit with archive/README update. |

## 7. Dead links

Resolved against `AGENTS/RED/`, the repo root, the file's own directory and `memory/auto/`. Bare filenames were then searched with `find`. False positives, where the bare name resolves under `scripts/`, `research/` or elsewhere, are removed.

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 7.1 | ❌ | CLAUDE.md:53 | `inbox/2026-07-09_from-WALTER_pull-complete-exemption.md` is missing; the file is at `inbox/processed/…`. MAINTENANCE.md:602 has the same dead path. | existence sweep | Re-point both to `inbox/processed/`. |
| 7.2 | ❌ | CLAUDE.md:256 | `competing-hypotheses/` is missing. | existence sweep | See 1.4. |
| 7.3 | ❌ | CLAUDE.md:86 | `archive/handoffs/` is missing. | existence sweep | See 1.3. |
| 7.4 | ⚠️ | MAINTENANCE.md:231 | `PROME/proposals/2026-08-28_p1-read-cap-RULED.md` is not present anywhere, and `git log --all` on the path shows nothing. | `find`; `git log --all -- <path>` | Correct the reference. |
| 7.5 | ⚠️ | MAINTENANCE.md:156, :172 (×2), :786 | These are packet paths in recipients' `inbox/` that were since moved to `processed/`: BOND 2026-09-10, VIOLET 2026-09-09, PROME 2026-09-09, WALTER 2026-09-02. The class: links written at delivery die when the recipient drains its inbox. | `find -name` → all under `…/inbox/processed/` | Cite `processed/` paths, or cite commit hashes. |
| 7.6 | ⚠️ | MAINTENANCE.md:231 | `inbox/processed/2026-08-28_from-DAEDALUS_P1-read-cap-RULED-…` is a truncated filename with an ellipsis, so it cannot resolve. | links.py | Write the full name. |
| 7.7 | ⚠️ | MAINTENANCE.md:299, archive/README.md:40-44 | `workbook/CHG-RED-005_*.md`, `workbook/RUSSIAN_OIL_CHALLENGE.md` and `challenges/KRE_*` are pre-move paths. archive/README was being edited during the audit. | links.py | Confirm that README lists the post-move paths. |
| 7.8 | ℹ️ | CLAUDE.md:250, :265; MEMORY.md:9; MAINTENANCE.md:379, :561, :567, :581, :584, :660, :665, :680 | These dead paths are explicitly described as deleted or retired: `thesis/PREDICTIONS.tsv`, `archive/RED_SKELETON.md`, `archive/status_snapshots/…`, `AGENTS/PROME/…`, `archive/violet_skew_recheck_apr2026/`, `archive/superseded_workbook/`. They are intentional and labelled. | links.py | None (the labels are adequate). |
| 7.9 | ℹ️ | NEXUS_BRIEF.md:12 `measure.py`, MAINTENANCE.md:130 `exempt_gap.py` | Both are bare names that live in `PROME/tools/`, so they resolve only by search. | `find` | Write `PROME/tools/…`. |

All `reports/…` and `archive/CALENDAR_*` links in STATUS.md and CALENDAR.md resolve.

## 8. Size and read-cap (budget 32,550 B; root CLAUDE.md)

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 8.1 | ⚠️ | AGENTS/RED/CLAUDE.md | At **43,108 B** it is 132% of the 32,550 B budget. It is read whole at every boot as the desk's instructions. `read_cap_check` excludes it: "charter … OUT OF PERIMETER by rule 20 unless declared; injection UNCONFIRMED". | `read_cap_check.py --agent RED` ℹ️ line | Declare a charter mode in READS.tsv, or move historical prose (the 5.5 and 9c narratives) to MAINTENANCE. |
| 8.2 | ⚠️ | STATUS.md | It is 23,309 B, 72% of budget, with 1,103 B of headroom before the 75% rotation trigger. Today's S53 addendum alone added one long line. | `read_cap_check` "Headroom to the trigger: 1,103 B" | Rotate at the next closeout; 4.1/5.x deletions also free bytes. |
| 8.3 | ℹ️ | MEMORY.md 22,096 B (68%) · board_log.tsv 19,192 B (59%) · CALENDAR.md 8,218 B (25%) · SCRATCH.md 7,238 B (22%) · NEXUS_BRIEF.md 13,661 B (42%) | All are under budget. None is within 15% of the cap (≥27,668 B). | `read_cap_check`; `wc -c` | None. |
| 8.4 | ℹ️ | thesis/CHANGELOG.md 173,211 B | It is declared `scoped` (tail read) and is newest-first. One out-of-order entry sits at the bottom ("2026-07-31 S27b addendum" after "2026-02-14"), so a reader taking "the last 2–3 entries" from the end gets 2/14 and 7/31. | `grep -n '^## '` L1004, L1009 | Move the S27b entry into date order; write "top 2–3 entries" in charter boot 4. |
| 8.5 | ℹ️ | STATUS.md line cap | 129 lines, under 200. | `wc -l` | None. |

## 9. Duplicated or contradictory instruction homes

| # | Severity | Where | What is wrong | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 9.1 | ❌ | Registry column count | The column count has four homes with four answers: CLAUDE.md:281 "15-col"; MAINTENANCE.md:242 "15→17 cols"; STATUS.md:57 "18-col since S39"; actual 19. | schema_check | One home, SCHEMA.tsv; prose carries no count. |
| 9.2 | ❌ | Prediction tally | STATUS:113 "1 ACTIVE"; CALENDAR:43 "2A"; NEXUS:31 "1 ACTIVE"; canon 2 ACTIVE. Charter L250 "RED-01…19"; canon RED-01…25. | §4 | Keep one tally line, ideally generated by boot.py §④. |
| 9.3 | ❌ | FT-10 state | Registry `state` FIRED · registry `state_detail` opens "ARMED - NOT FIRED … 0 OF 4" · STATUS:11 banner "count is 0-of-4" · STATUS:68 FIRED. | §3.10, §4.5 | Current state first, in every home. |
| 9.4 | ❌ | FLOW.tsv | The charter (W6, L279, L289) says to add rows; the file banner says FROZEN 7/05. | §1.2 | Amend the charter. |
| 9.5 | ❌ | inbox/WALTER lane | Charter 1.5 says no pushes to the lane; charter 5.5 says LIVE. | §1.1 | Amend 1.5. |
| 9.6 | ⚠️ | Archive paths | Charter W5 says `archive/handoffs/` is FROZEN; the charter's Archive table says DELETED; MAINTENANCE.md:701-712 "STANDING HYGIENE CHECKLIST" still says to refresh "`CALENDAR.md` FALSIFICATION WATCH" and to "move to CALENDAR RESOLVED". Both sections were frozen or rotated out (CALENDAR:39–41, :54). | cited lines | Retire the MAINTENANCE checklist (boot 9a–9e supersede it), or bring it up to date. |
| 9.7 | ⚠️ | CRLF rule | MAINTENANCE.md:636 says four TSVs are CRLF; on disk only WATCHLINES is. Auto-memory `finding_crlf_textmode_tsv_flip` tells editors to check endings, so a stale per-file list misleads. | §3.4 | Mark the line as historical. |
| 9.8 | ⚠️ | Challenge set | STATUS "Currently ACTIVE" has 10 rows; CHALLENGES.tsv has 6 non-resolved; boot.py §④ lists 6. CHG-047 is ACTIVE in STATUS and RESOLVED-CONVERGED in canon. | §4.1 | Generate the STATUS table from the TSV. |
| 9.9 | ⚠️ | KB status vocabulary | Charter 9c prescribes the token `DATED-HISTORICAL`; SCHEMA.tsv KB.Status does not list it, and the TSV holds 9 rows with it. | §3.7 | Add it to SCHEMA. |
| 9.10 | ℹ️ | STATUS line cap | The cap is stated three times in the charter (W1, Output Rules, Anti-patterns), consistently as ≤200. | — | None (consistent). |

---

## Summary: the ten most consequential findings

1. **❌ ML.tsv rows 249–257 (ML-RED-248…256) are column-shifted.** Status is missing, so `A1` sits in Status and every later field is off by one. `schema_check.py` reported "ALL CONFORM" because it never counts cells per row (3.1, 2.2).
2. **❌ STATUS "Currently ACTIVE" has 10 rows; canon has 6 open.** CHG-042/046/047/048/051 are closed in CHALLENGES.tsv (CHG-047 is RESOLVED-CONVERGED 9/6 but shown ACTIVE). The "CHG-006 through CHG-041 resolved" line wrongly includes the open CHG-027 and CHG-028 (4.1, 4.2).
3. **❌ The FT-10 state has four contradictory homes.** The registry `state_detail` opens "ARMED - NOT FIRED … 0 OF 4" and STATUS:11 banners "count is 0-of-4", while the trigger FIRED 10/14 (3.10, 4.5, 9.3).
4. **❌ NEXUS_BRIEF, the fleet-consumed surface, contradicts itself.** L3/L73 say HY 325, FT-02 1 of 3; L7, L44–52 and L80–81 still say 312 [9/30], "0 of 3, 8bp away", "days to weeks away" (5.1–5.3).
5. **❌ The S53 addendum skipped W-A floor step A2 (no SCRATCH addendum) and A4's W3 (no CHANGELOG line)** after changing a registered-trigger count (5.14, 5.15).
6. **❌ The charter gives contradictory live instructions.** 1.5 says WALTER no longer pushes to `inbox/WALTER/` while 5.5 says LIVE, and a push landed today, unlogged (1.1, 1.17). W6 and the Rules still direct writes to the FROZEN FLOW.tsv (1.2). W5 cites the deleted `archive/handoffs/` (1.3).
7. **❌ `gen_trigger_scan.py` writes on any invocation, including `--help`.** It rewrote the registry scan view during this audit (byte-identical this time) (2.1).
8. **❌ The prediction tally disagrees across three mirrors (1A / 2A / 1A), and the charter's "RED-01…19" is stale.** Canon is 13C / 10W / 2A over RED-01…25 (4.3, 9.2).
9. **⚠️ Token-domain drift is invisible to every instrument.** There are out-of-SCHEMA tokens in ML, KB, VX, CHALLENGES and CATALYSTS statuses and in registry `state` (`FIRED`). One CATALYSTS row carries status `🔴` and is 31 days overdue, but boot §③ skips it (3.2, 3.5–3.9, 2.4).
10. **⚠️ The charter is 43,108 B (132% of the read budget), unmeasured by `read_cap_check` (out of perimeter), and names five paths that do not exist.** The missing paths are `competing-hypotheses/`, `archive/handoffs/`, `counter-evidence/CARL|SAM/`, `*_old_7col.tsv` and the inbox exemption path. Its ownership tables omit `registry/`, `scripts/`, `outbox/`, `board_log.tsv` and `NEXUS_BRIEF.md` (8.1, 1.4–1.7, 1.14).
