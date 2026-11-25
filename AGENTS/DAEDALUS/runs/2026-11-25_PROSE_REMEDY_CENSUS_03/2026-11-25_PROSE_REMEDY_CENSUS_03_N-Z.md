# Prose-Remedy Census #3, step 2 classification, desks N–Z

**Classifier:** non-owner (DAEDALUS-spawned), read-only except this file. **Read window:** 2026-11-25 14:53:58 EST to this write. **Written:** 2026-11-25 14:58:31 EST (`date`). **HEAD at read:** 2310d4f3d4 (at write: 55de4ed42e). **Input:** the 98 N–Z rows of `2026-11-25_PROSE_REMEDY_CENSUS_03_CANDIDATES.tsv`; # = ordinal in that slice. All 98 live lines match the TSV text. **Playbook:** `AGENTS/DAEDALUS/sweeps/PROSE_REMEDY_SWEEP.md` §2.

## §0 Summary

| Desk | Cand. | PROSE-REMEDY non-LOW | PROSE-REMEDY LOW | Under-bar watch | BUILT | DIAGNOSIS | DECLINED | FALSE | FP rate |
|---|---|---|---|---|---|---|---|---|---|
| NEXUS | 5 | 0 | 1 | 0 | 1 | 0 | 1 | 2 | 2/5 |
| ORACLE | 11 | 0 | 0 | 0 | 3 | 2 | 2 | 4 | 4/11 |
| OSPREY | 6 | 0 | 1 | 0 | 0 | 0 | 0 | 5 | 5/6 |
| OTTO | 6 | 0 | 0 | 0 | 4 | 0 | 0 | 2 | 2/6 |
| OZK | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0/2 |
| PROME | 4 | 1 | 0 | 0 | 1 | 0 | 0 | 2 | 2/4 |
| RED | 9 | 0 | 0 | 1 | 3 | 0 | 3 | 2 | 2/9 |
| REGINALD | 3 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1/3 |
| SAM | 10 | 1 | 1 | 0 | 6 | 0 | 0 | 2 | 2/10 |
| SHADE | 7 | 0 | 0 | 0 | 1 | 0 | 0 | 6 | 6/7 |
| TERRY | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2/2 |
| VIOLET | 11 | 0 | 0 | 0 | 3 | 0 | 0 | 8 | 8/11 |
| VULCAN | 6 | 0 | 0 | 0 | 2 | 0 | 0 | 4 | 4/6 |
| WAL | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 2/3 |
| WALTER | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1/1 |
| WATT | 4 | 0 | 0 | 0 | 2 | 0 | 1 | 1 | 1/4 |
| YURI | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1/2 |
| ZHAO | 6 | 0 | 0 | 0 | 2 | 0 | 3 | 1 | 1/6 |
| **Total (18 desks)** | **98** | **2** | **5** | **1** | **31** | **2** | **11** | **46** | **46/98 = 47%** |

Row arithmetic: 2 + 5 + 1 + 31 + 2 + 11 + 46 = 98. All PROSE-REMEDY rows are distinct. Rows not read: 0. A desk with no PROSE-REMEDY and no watch row is CLEAN: ORACLE (11), OTTO (6), REGINALD (3), SHADE (7), TERRY (2), VIOLET (11), VULCAN (6), WALTER (1), WATT (4), YURI (2), ZHAO (6).

**Step-3 sentence:** 0 rows typed by this run; premise-verified at the source for 0 of 0. BUILT means the code line was read, not that its selftest was re-run.

**Carry:** sessions are distinct dates of desk STATUS commits (PROME: STATUS or SCRATCH) since the rule began; SAM row 52 uses KOYOMI runs. LOW means a STATUS line cap that the 32,550 B byte budget hits first at the measured bytes per line.

## §2 The non-LOW rows

**Row 33, PROME `SCRATCH.md:17`, DOCKET 1179: PROSE-REMEDY (9; dates 11/17 to 11/25).** Already registered to PROME, due "next-PROME-process-pass". None of the four tools has a commit since 11/17 (`git log`: spawn_list 11/10, fetch.py 11/08, commit_check 9/10, orch_closeout 10/21).

| Leg | Unbuilt | Read at the code | What it costs |
|---|---|---|---|
| spawn_list | read only the leading annotation, not `prior:` history | `PROME/tools/spawn_list.py:132` searches the whole state cell plus notes | Reproduced 11/25 by calling `coverage()`: five PENDING rows read COVERED only from prior-state text (554 NEXUS 12/01, 784 CORAL 12/04, 811 12/22, 1214 VULCAN 11/27, 1256 AEOLUS 11/27). Three fall within seven days. Mitigated: `:469` prints the suppressed rows, and `SCRATCH.md:15` lists the VULCAN and AEOLUS 11/27 wakes by hand. No missed wake found |
| fetch.py roll day | name the contract or suppress the change on a roll day | `FORGE/tools/market-data/fetch.py:1051-1065` withholds a change by session state only; no test for a contract switch | One instance, 11/18: printed -5.16% against about -2.2% true. No later one found |
| orch_closeout | bind a receipt to a launch row that has no identity block | `PROME/tools/orch_closeout.py:158` requires owner and session match | Old rows print UNKNOWN permanently; a workaround (block at append) is in force |
| commit_check | none specified | `PROME/tools/commit_check.py:167,206` refuses and prints each bad path | Diagnosis only: it does what it says |

**Row 52, SAM `MAINTENANCE.md:616`: PROSE-REMEDY (23 KOYOMI runs, unchanged; 8 SAM STATUS dates since run #2).** Unbuilt: no `runway`, `furthest` or `tripwire` in `catalyst_countdown.py`, `boot.py` or `lib/`. Owner gate: "until Will decides he likes the pattern" (undated); SAM carries it at `MEMORY.md:62`.
- It matters as a gap: the last KOYOMI run was 10/20 (Run 24). `docket/CATALYSTS.tsv` holds 5 forward rows: 11/27, three on 11/30, then 2027-01-25. No December row, though `docket/RELEASES.md` has BOJ MPM Dec 17-18, and `STATUS.md:20` carries December BOJ pricing (71%). `KOYOMI_MEMORY.md:427` gives Nov+Dec coverage to the first November run (`MEMORY.md:57` repeats the debt); no November run is on record.
- It does not matter as a remedy: the test as written (runway under about 10 days) reads 61 days to 1/25 and would be silent today. `KOYOMI_MEMORY.md:432` says so. The overdue thing is a KOYOMI run, not the tripwire.

**Row 35, RED `MAINTENANCE.md:13`: under-bar WATCH (0 sessions; written 11/25 00:2x ET).** `scripts/base_rate_review.py:205` `FT11_LEGS` has four series, and `ft11_legs` (`:209`) has no butterfly leg. Cost: RED found five second-path windows never recorded at the time (9/14, 9/17, 9/18, 10/21, and 11/10 to 11/18), and states nothing was mis-scored because FLOW moves no weight (`thesis/CHANGELOG.md:10`). RED's `SCRATCH.md:20` owns it as "extend, do not add a new check".

## §3 RED METRIC_MAP against `instrument_basis` (row 41, recall miss restored)

**Does code compare them today? No.** `AGENTS/RED/scripts/boot.py:354-366` looks up `METRIC_MAP[r["metric"]]` and never reads `instrument_basis` or `instrument_basis_operative`. The only basis-aware code is a hard-coded PROVISIONAL tag for BRENT-PAPER (`:362-365`). `basis_check.py` hashes files. `base_rate_review.py:274` reads the cell for an arm date only. **Instance read 11/25, 12 rows:** nine metrics; seven mapped. HY-OAS, CCC-OAS, INITIAL-CLAIMS, VIX, BREAKEVEN-5Y5Y and SKEW-CBOE match the declared source; BRENT-PAPER is the disclosed PROVISIONAL one. CORE-CPI-3MO-ANN and UST-30Y-RALLY-ATTRIBUTION are unmapped and print "manual check" (`:358`). So: unbuilt, 0 undisclosed mismatches, owner-declined. Side fact, not counted: FT-10's `instrument_basis_operative` still reads "defect rate 0.79%/session", which `boot.py:88-92` says is withdrawn.

## §4 Run #2 items, graded at the artifact

| Run #2 non-LOW item | Now | Evidence |
|---|---|---|
| PROME WQ-206 aged ACTION (47) | **BUILT** 11/16 | row 34. WQ-577 kept it to one line, so a Will-RULING packet under 7 days old has no own leg, and the item ② liveness re-point and `due:` template were left out; this is recorded on DOCKET 730 |
| ORACLE `polymarket.py` resolved pin (10) | **BUILT** 11/04 | row 12; live test is the owner's, not replayed |
| ORACLE STATUS ≤250 lines (27) | **DECLINED** 11/04 | `MAINTENANCE.md:343`; old `CLAUDE.md:65` line is gone, `:48` keeps "<250 lines". Now 132 B/line: bytes bind at line 244, so it has become LOW too |
| NEXUS page cap (14) | **DECLINED** 10/31 | row 5, reason on the line |
| RED CALENDAR twin (35) | **DECLINED** 11/04 | row 42 |
| RED hypothesis bounds (43) | **DECLINED** 11/04 | row 43 |
| RED ML-226 (off-list) | **DECLINED** 11/04 | row 41, §3 |
| SAM KOYOMI tripwire (23) | still PROSE-REMEDY (23) | row 52 |

Run #2 N–Z: 7 substantive plus ML-226 = 8; 2 BUILT, 5 DECLINED, 1 open. The five LOW caps (NEXUS, OSPREY, OZK, SAM, WAL) are unchanged; PROME got one fleet note 10/30 (`PROME/inbox/processed/2026-10-30_from-DAEDALUS_prose-remedy-census-2.md`), and no charter moved on it. **What LOW costs:** nothing; each desk's STATUS is under the byte budget (highest OSPREY 90%, SAM 89%).

## §5 Limits

1. Will's 10/31 word (fewer checkers and rules) governs: this record recommends no build.
2. Evidence words on PROME rows are what I read or called read-only; tool selftests were not run. `coverage()` and `owner_unconsumed()` were imported and called, with no write.
3. Form-2 false positives are still mostly signal and kill tables (OSPREY, SHADE, VULCAN, WAL). The 11/25 case-insensitive change added nine N–Z rows by its own list (ORACLE 2, PROME 1, RED 2, VIOLET 1, VULCAN 1, WATT 1, ZHAO 1); of those only PROME `SCRATCH.md:17` is a new PROSE-REMEDY.
4. Whole-file reads were not done; each row was read at its line with nearby context.

## §6 Rows


### NEXUS

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 1 | CLAUDE.md:55 | PROSE-REMEDY (54) LOW | "9. **STATUS sanity check:** under 200 lines" | No code counts the lines; bytes are computed by root `scripts/read_cap_check.py`. 99 lines, 229 B/line: bytes bind at line 141. |
| 2 | CLAUDE.md:63 | BUILT | "the WHOLE FILE is measured at every session-end commit (the 0a instrument) and rotated at ≥75%" | `scripts/read_cap_check.py`, called at `CLAUDE.md:26`. |
| 3 | CLAUDE.md:91 | FALSE | "A single Polymarket/Kalshi print is not a hold: ≥3-day re-check" | Evidence discipline; odds are ORACLE's. |
| 4 | CLAUDE.md:96 | FALSE | "No standing probability without a registered falsifier … held or re-marked ≥2 passes" | Judgment rule, no countable field. |
| 5 | CLAUDE.md:154 | DECLINED-BY-DESIGN | "≤ 6 KB; … ≤150 words … Stays prose (census #2 DECLINE 10/31)" | Owner reason is on the line. Verified in place. |

### ORACLE

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 6 | MAINTENANCE.md:79 | FALSE | "the tool's run-cadence + WTI-month-roll owed-action were homed only in SCRATCH" | 7/17 history of a finished doc move. |
| 7 | MAINTENANCE.md:80 | FALSE | "**Owed manual action:** … re-pin the new month's WTI $100 market … the failure is loud, but the re-pin is manual" | Detection is code: `tools/disruption_supply_spread.py:238-242` hard exit. The re-pin is done (last ledger row 11/25 on `will-wti-reach-110-in-november-2026`). |
| 8 | MAINTENANCE.md:188 | DIAGNOSIS-ONLY | "the pass still reports "8 ledger(s) scanned" and prints seven rows, with HISTORY.tsv silent" | Not ORACLE's code; no remedy given. Still reproduces 11/25: `ledger_staleness.py ORACLE` says 7 scanned, prints 6 rows. HISTORY.tsv was last committed 11/06. |
| 9 | MAINTENANCE.md:202 | DIAGNOSIS-ONLY | "`polymarket.py history` writes TWO rows stamped with today's date … never dedupes" | Owner rejects the one-line fix. `scripts/polymarket.py` `clob_history()` still appends every point. |
| 10 | MAINTENANCE.md:204 | DECLINED-BY-DESIGN | "`t6_pin.py` prints no leg summary after `WIN_END` … maintenance on a dead instrument" | Owner reason on the line. |
| 11 | MAINTENANCE.md:219 | DECLINED-BY-DESIGN | "`kalshi.py event <SERIES>` reads a date-stamped series as a delisting (… logged not patched)" | Weak: `:224` "discipline, not code", `search` certifies coverage. Same as run #2. |
| 12 | MAINTENANCE.md:230 | BUILT | "`polymarket.py pull` reports a RESOLVED market as `PINNED BUT NOT FOUND` … **not patched**" | `scripts/polymarket.py:143` `closed_outcome()`, called `:500`, prints `:505`. The line is dated history; the close is at `:340`. |
| 13 | MAINTENANCE.md:298 | FALSE | "`fmt_row`: spread and /yes − mid/ rounded to 4 dp … 7/7 PASS" | DONE entry. |
| 14 | MAINTENANCE.md:340 | FALSE | "**`polymarket.py`:** BUILD on Prose-Remedy Census row 12" | DONE entry for row 12. |
| 15 | CLAUDE.md:56 | BUILT | "thin (<$5K liq) = ≥3-day re-check, never mark on one print" | `scripts/polymarket.py:30-31,97`. The 3-day count stays advice (noted at run #2). |
| 16 | CLAUDE.md:194 | BUILT | "**Thin-liquidity guardrail (baked into the fetcher)**" | Same code as 15. |

### OSPREY

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 17 | CLAUDE.md:89 | PROSE-REMEDY (39) LOW | "- STATUS.md stays under 250 lines" | No code counts the lines; bytes are computed by root `scripts/read_cap_check.py`. `CLAUDE.md:50` names `measure.py`, which prints lines and compares nothing. 242 B/line: bytes bind at line 134. STATUS is at 90% of budget. |
| 18 | CLAUDE.md:158 | FALSE | "**Channel 2 (crude-export terminals) kill:** … for **30+ days**" | Kill rule. |
| 19 | CLAUDE.md:179 | FALSE | "a channel steps DOWN one mark when …" | Domain mark rule. |
| 20 | CLAUDE.md:180 | FALSE | "no 4-wk print ≥ 3.9 M bpd since the week to 8/2" | History of the 9/08 ruling. |
| 21 | CLAUDE.md:198 | FALSE | "Brent sustains a break >$85 for 3+ sessions" | Kill rule. |
| 22 | CLAUDE.md:209 | FALSE | "OSP-06 (no sustained recovery to ≥3.9 M bpd …)" | Prediction resolution text. |

### OTTO

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 23 | CLAUDE.md:193 | BUILT | "If `… brief_pin_check.py" OTTO` reports **PIN-UNRESOLVED** …" | Root `scripts/brief_pin_check.py`; run 11/25: OTTO OK-PINNED. |
| 24 | MAINTENANCE.md:115 | FALSE | "`CLAUDE.md` v2.7 → v2.8 … replaced by `scripts/brief_pin_check.py`" | DONE entry. |
| 25 | CLAUDE.md:259 | FALSE | "`[ALLEG]` … weight ≤40%" | Evidence weighting. |
| 26 | CLAUDE.md:287 | BUILT | "spawned every OTTO session with ≥7 days since its last run" | `scripts/boot.py:81,85,193`. |
| 27 | CLAUDE.md:339 | BUILT | "Every OTTO session with ≥7 days since its last run" | As 26. |
| 28 | CLAUDE.md:535 | BUILT | "docket steward (each OTTO session ≥7d since last run" | As 26. |

### OZK

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 29 | MAINTENANCE.md:41 | BUILT | "no `scripts/boot.py` boot kit" | `AGENTS/OZK/scripts/boot.py` exists. Stale 7/04 history. |
| 30 | CLAUDE.md:140 | PROSE-REMEDY (25) LOW | "- **STATUS.md stays under 250 lines.**" | No code counts the lines; bytes are computed by root `scripts/read_cap_check.py`. 119 lines, 178 B/line: bytes bind at line 182. |

### PROME

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 31 | CLAUDE.md:61 | FALSE | "the charter target under 20,000 B (`measure.py`) measures the pass and licenses nothing" | Owner says it is no gate. |
| 32 | SCRATCH.md:15 | FALSE | "CHECKPOINT 2026-11-25 14:01 ET" | A hand-off list of wakes and dated rows. Nothing uncomputed is specified here; the orch_closeout residue is row 33. |
| 33 | SCRATCH.md:17 | PROSE-REMEDY (9) | "the tool misses on D:L1179 (four: spawn_list, commit_check, fetch.py on a Brent contract-roll day, orch_closeout)" | See §2. Registered as DOCKET 1179. |
| 34 | CLAUDE.md:51 | BUILT | "**Aged ACTION (WQ-206):** unconsumed `action:` older than seven days at a DARK owner" | `PROME/tools/inbox_census.py:190` `owner_unconsumed()`, `PROME/tools/prome_gate.py:1029`, wired `:1630` (d0a5365d8c 11/16; DOCKET 730 RESOLVED, one independent reader). Called read-only 11/25: WAL 5 items, 2 ACTION ≥7d; OZK 2 items. Waits leg: `prome_gate.py:1009`. |

### RED

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 35 | MAINTENANCE.md:13 | PROSE-REMEDY (0) WATCH | "FT-11's v1.1 second path has no scanner (ML-RED-336); the repair (extend … `ft11_legs` …) is owed next session" | See §2. Written 11/25: 0 sessions, under the ≥2 bar. |
| 36 | MAINTENANCE.md:198 | FALSE | "W1 names `wc -l` + `read_cap_check.py --agent RED`" | DONE entry. |
| 37 | MAINTENANCE.md:274 | BUILT | "SCAN view breached WALTER's read cap AT 101.1% … PROPOSED to WALTER (`state`/`state_detail` split)" | The split exists: `state_detail` is column 19 of `registry/FALSIFICATION_TRIGGERS.tsv`; the SCAN view is 21,364 B (65.6% of 32,550). History line. |
| 38 | MAINTENANCE.md:310 | BUILT | "§⑤ itself is the **specified-not-built** check flagged at S41" | `scripts/boot.py` ID set-difference plus `scripts/test_board_gap.py` (run #2 row 36). History line. |
| 39 | MAINTENANCE.md:331 | BUILT | "**`scripts/boot.py` still evaluates FT-10 from the mirror.**" | `scripts/boot.py:87-101` reads the Cboe CSV. History line. |
| 40 | MAINTENANCE.md:437 | FALSE | "`review_debt.py` offered to PROME/DAEDALUS as a fleet candidate" | Condition on an outbound proposal. |
| 41 | MAINTENANCE.md:942 | DECLINED-BY-DESIGN | "**Nothing compares `boot.py`'s METRIC_MAP source against each row's `instrument_basis` (ML-226).**" | Declined 11/04; reason at `CHARTER_PROVENANCE.md:407`. Code answer in §3. |
| 42 | CLAUDE.md:69 | DECLINED-BY-DESIGN | "`CALENDAR.md` is its narrative twin with the SAME event set" | Declined 11/04, same place. By hand 11/25: all 19 forward CATALYSTS rows have their date in CALENDAR except 12/18, whose status is `superseded`. No miss. |
| 43 | CLAUDE.md:163 | DECLINED-BY-DESIGN | "≥4 scenarios …; no INDIVIDUAL hypothesis below 2% or above 60%" | Declined 11/04, same place. Values not re-read by me. |

### REGINALD

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 44 | CLAUDE.md:15 | BUILT | "Print≤~5 trading days: fuller sweep" | `scripts/earnings_countdown.py:64` counts trading days; selftest `:95`. The sweep is a session mode. |
| 45 | CLAUDE.md:62 | DECLINED-BY-DESIGN | "≤250 lines, with root byte budget controlling above line count" | Weak, as run #2. 176 B/line: bytes bind at line 184; STATUS is at 91%. (91) if re-ruled. |
| 46 | CLAUDE.md:135 | FALSE | "FHLB Advances (`REG-T-06`) / >$700B ×3 official quarterly prints" | Signal table. |

### SAM

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 47 | CLAUDE.md:27 | BUILT | "INSTRUMENT EXISTS — use it: `boot.py --predictions`" | `scripts/boot.py:106,297`; `scripts/lib/boot_context.py`. |
| 48 | CLAUDE.md:85 | BUILT | "`closeout_check.py` exists because that split is structural" | `scripts/closeout_check.py:229-250` (A, A2, B, B2). |
| 49 | MAINTENANCE.md:182 | FALSE | "**NEW — `scripts/rate_differential.py`** (boot-wired)" | DONE entry. |
| 50 | MAINTENANCE.md:538 | BUILT | "vol IV/skew proxy build in fxy_options.py (queued — CME route gated)" | `scripts/fxy_options.py` (0a48b9012, 46dfddb72). History. |
| 51 | MAINTENANCE.md:552 | BUILT | "extend existing `fxy_options.py` to compute a 30d ATM-IV proxy" | As 50. |
| 52 | MAINTENANCE.md:616 | PROSE-REMEDY (23) | "boot-time staleness *tripwire* in catalyst_countdown.py (runway < ~10d → auto-nudge SAM to spawn KOYOMI)" | See §2. |
| 53 | STATUS.md:9 | BUILT | "`ltv_lookup.py` holds the 9/30 base at 157.35 and gives the wrong FX sign" | `research/outputs/2026-11-06_softbank/ltv_fx_sensitivity.py` (d346a52192) and a printed warning in `ltv_lookup.py` (56154ee62d), both 11/11. |
| 54 | CLAUDE.md:78 | BUILT | "Checkable form: *the brief's commit timestamp ≥ this session's last STATUS commit timestamp*" | `scripts/closeout_check.py:516` (advisory since WQ-719 A). `brief_pin_check.py`: SAM OK-PINNED. |
| 55 | CLAUDE.md:138 | PROSE-REMEDY (91) LOW | "- STATUS.md stays under 250 lines." | No code counts the lines; bytes are computed by root `scripts/read_cap_check.py`. 99 lines, 293 B/line: bytes bind at line 110. STATUS is at 89% of budget. |
| 56 | CLAUDE.md:213 | FALSE | "Annual: Shunto wages ≥6.0% shock threshold" | Dormant signal. |

### SHADE

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 57 | STATUS.md:15 | FALSE | "owed list (§10) … `read_cap_check.py --agent SHADE` every closeout" | Section name; tool is built. |
| 58 | CLAUDE.md:46 | FALSE | "**NOT RED** only if **CEILING ≤ 30%**" | Grading rule. |
| 59 | CLAUDE.md:50 | FALSE | "No band or threshold until a calibration set across ≥5 insurers exists" | Deferral of a metric. |
| 60 | CLAUDE.md:93 | FALSE | "HY OAS > 280 bp, SUSTAINED ≥5 consecutive published sessions" | Trigger row. |
| 61 | CLAUDE.md:98 | FALSE | "A run is broken by any published session ≤280" | Trigger row; LIQUID owns the count. |
| 62 | CLAUDE.md:99 | FALSE | "SIGN-LEG WINDOW … session ≤280bp" | Trigger row. |
| 63 | CLAUDE.md:161 | BUILT | "Checkable form: the brief's commit timestamp ≥ this session's last STATUS commit timestamp" | Root `scripts/brief_pin_check.py`: SHADE OK-PINNED 11/25. Line now carries WQ-719 A. |

### TERRY

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 64 | CLAUDE.md:175 | FALSE | "`scripts/ledger_sweep.py` / **Anti-drift guard.**" | Describes built code; the token is in a prohibition. |
| 65 | CLAUDE.md:182 | FALSE | "retired ≥60d material" | Root rule cited. |

### VIOLET

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 66 | CANARY_MAP.md:82 | BUILT | "a guard that cries wolf on a fixed weekly schedule" | `:86` "FIXED 2026-09-04"; `scripts/canary_staleness.py` present. |
| 67 | CLAUDE.md:186 | FALSE | "republish to the existing URL (… flag the republish as owed)" | Publishing step, not a computation. |
| 68 | LAST_COMPLETION.md:18 | FALSE | "`^SKEW` back-sweep still owed" | File FROZEN 2026-09-06. |
| 69 | LAST_COMPLETION.md:20 | FALSE | "**BUILT (PM):** ① COT staleness rebuilt THREE TIMES" | FROZEN file, DONE. |
| 70 | LAST_COMPLETION.md:21 | FALSE | "Remedy is a check, not a third sweep: **NEW `surface_agreement.py`**" | FROZEN file, DONE; script present. |
| 71 | MAINTENANCE.md:190 | FALSE | "`backfill.py` — can now CREATE missing sessions" | DONE entry. |
| 72 | MAINTENANCE.md:191 | FALSE | "`surface_agreement.py` — memo glob bounded to ONE delivery date" | DONE entry. |
| 73 | MAINTENANCE.md:211 | FALSE | "Taking the 9/11 settle that the 14:5x session left owed" | Trigger line of a DONE entry. |
| 74 | CLAUDE.md:46 | BUILT | "Keep under 250 lines" | `scripts/thresholds.py:407` `CAPPED_DOCS`, compared `:416`. |
| 75 | CLAUDE.md:75 | BUILT | "STATUS.md should stay under 250 lines" | As 74. |
| 76 | CLAUDE.md:160 | FALSE | "ending in the COMPLETION block (… ≤10 lines" | Shape is PROME's spec, not VIOLET's. |

### VULCAN

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 77 | CLAUDE.md:38 | BUILT | "**BLOCKS on boot alarms left unactioned**" | `tools/closeout_check.py:348`. |
| 78 | CLAUDE.md:190 | BUILT | "Read whole startup surfaces stay under 32,550 B" | Root `scripts/read_cap_check.py`. |
| 79 | SCRATCH.md:51 | FALSE | "**Owed at the 11/27 slot** … mag7.py slot 12" | Dated data reads with existing tools. |
| 80 | SCRATCH.md:60 | FALSE | "**Owed post-close:** mag7.py slot 11 plus semi_watch.py" | Prior 11/20 block; data reads. |
| 81 | CLAUDE.md:89 | FALSE | "Useful-life gate: ≥2 of 4 names change useful-life" | Domain gate. |
| 82 | CLAUDE.md:120 | FALSE | "**≤ −7.5pp** (base-rated …)" | Threshold cell. |

### WAL

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 83 | CLAUDE.md:106 | PROSE-REMEDY (22) LOW | "- **STATUS.md ≤250 lines.**" | No code counts the lines; bytes are computed by root `scripts/read_cap_check.py`. 127 lines, 158 B/line: bytes bind at line 205. |
| 84 | CLAUDE.md:131 | FALSE | "~~WAL close <$78 (threshold)~~ **TERMINAL**" | Resolved gate. |
| 85 | CLAUDE.md:135 | FALSE | "MI3 ≥25% at any quarterly FFIEC pull" | Signal table. |

### WALTER

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 86 | CLAUDE.md:49 | FALSE | "Oversized whole sources read in chunks still need a cap remedy" | Names a built tool; fleet canon owns the cap. |

### WATT

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 87 | CLAUDE.md:176 | BUILT | "Byte budget = the fleet read-cap **32,550 B** … enforced by `boot.py` leg 3" | `AGENTS/WATT/boot.py:183-191,271`. |
| 88 | CLAUDE.md:112 | BUILT | "PJM RT LMP … ≥$150 / ≥$500 / ≥$1,000" | `power_watch.py:126-127,384,472`. |
| 89 | CLAUDE.md:113 | FALSE | "PJM demand vs 24h peak … ≥90% / ≥97%" | Signal table. Side fact unchanged: `power_watch.py:107` hint is 95%, neither band. |
| 90 | CLAUDE.md:115 | DECLINED-BY-DESIGN | "BRA capacity clear vs cap / ≥50% / ≥90%" | `power_watch.py` docstring: "Annual cadence, tracked via BRA PDFs — not here." |

### YURI

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 91 | CLAUDE.md:69 | FALSE | "≥3 actor calls, each citing ≥2 channels" | Desk falsifier with a judgment unit; YUR-F02 runs to 11/28. |
| 92 | CLAUDE.md:104 | BUILT | "STATUS under 250 lines AND under **32,550 B**; at ≥75% … rotate" | Byte legs: root `read_cap_check.py` (65%). Line leg dominated: bytes bind at line 103. |

### ZHAO

| # | Line | Class | Quoted | Evidence |
|---|---|---|---|---|
| 93 | CLAUDE.md:49 | BUILT | "**READ-CAP IS THE BINDING CONSTRAINT, NOT THE LINE COUNT**" | Names root `read_cap_check.py`. This is the owner reason for 94, 96, 98. |
| 94 | CLAUDE.md:48 | DECLINED-BY-DESIGN | "Archive overflow to `archive/` to hold ≤250 lines" | Weak, reason at `:49`. Bytes bind at line 248. (32) if re-ruled. |
| 95 | CLAUDE.md:55 | FALSE | "ending with the COMPLETION block (… ≤10 lines)" | As 76. |
| 96 | CLAUDE.md:253 | DECLINED-BY-DESIGN | "Live dashboard — ≤250 lines" | As 94. |
| 97 | CLAUDE.md:255 | BUILT | "`NEXUS_BRIEF.md` … ≤100ln" | `scripts/boot.py:486` `BRIEF_MAX_LINES = 100`. |
| 98 | CLAUDE.md:266 | DECLINED-BY-DESIGN | "STATUS overflow lands here to hold the ≤250-line cap" | As 94. |
