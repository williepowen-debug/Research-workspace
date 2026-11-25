# Prose-Remedy Census #3: step 2 classification, desks A–M

**Started:** 2026-11-25 14:53 EST (`date`, first command) · **Written:** 2026-11-25 14:58 EST (`date` in the writing command) · **HEAD at write:** 55de4ed42e (moving; other sessions live) · **Classifier:** non-owner subagent for DAEDALUS, read-only; this file is its one write.
**Input:** `2026-11-25_PROSE_REMEDY_CENSUS_03_CANDIDATES.tsv` rows with desk A–M (73 rows, 20 desks) · **Playbook:** `sweeps/PROSE_REMEDY_SWEEP.md` §2 · **Prior:** `runs/2026-10-30_PROSE_REMEDY_CENSUS_02/2026-10-30_PROSE_REMEDY_CENSUS_02_A-M.md`.

## §0 Summary (73 rows · 20 desks · 73 opened at the live line · 0 NOT READ)

| Desk | Cand. | PROSE-REMEDY rows (distinct) | BUILT | DIAGNOSIS-ONLY | DECLINED | FALSE | FP rate | Verdict |
|---|---|---|---|---|---|---|---|---|
| AEOLUS | 14 | 0 | 1 | 0 | 0 | 13 | 93% | `CLEAN (14)` |
| BOND | 2 | 1 | 1 | 0 | 0 | 0 | 0% | 1: line cap, not LOW by arithmetic, no consequence seen |
| BROCK | 4 | 0 | 1 | 0 | 0 | 3 | 75% | `CLEAN (4)` |
| CARL | 3 | 2 (1) | 0 | 0 | 0 | 1 | 33% | 1: line cap, LOW |
| CORAL | 3 | 3 (1) | 0 | 0 | 0 | 0 | 0% | 1: line cap, LOW |
| CREED | 2 | 0 | 1 | 0 | 0 | 1 | 50% | `CLEAN (2)` |
| CRUISE | 2 | 1 | 1 | 0 | 0 | 0 | 0% | 1: line cap, LOW |
| CYPHER | 1 | 0 | 0 | 0 | 0 | 1 | 100% | `CLEAN (1)` |
| DEWEY | 2 | 0 | 1 | 0 | 0 | 1 | 50% | `CLEAN (2)` |
| FALCON | 2 | 0 | 2 | 0 | 0 | 0 | 0% | `CLEAN (2)`, one stale twin |
| FERT | 3 | 1 | 0 | 0 | 0 | 2 | 67% | 1: line cap, LOW |
| FLG | 4 | 1 | 0 | 0 | 0 | 3 | 75% | 1: line cap, LOW |
| GIBBS | 3 | 0 | 1 | 0 | 0 | 2 | 67% | `CLEAN (3)`, one stale clause |
| HANS | 7 | 0 | 3 | 0 | 0 | 4 | 57% | `CLEAN (7)` |
| HENRY | 6 | 3 (2) | 1 | 0 | 0 | 2 | 33% | 2: STATUS line cap LOW; MEMORY line cap not LOW by arithmetic, no consequence seen |
| HOMER | 2 | 0 | 1 | 0 | 0 | 1 | 50% | `CLEAN (2)` |
| ISHM | 2 | 1 | 1 | 0 | 0 | 0 | 0% | 1: line cap, LOW |
| LABOR | 7 | 0 | 1 | 0 | 4 (3) | 2 | 29% | `CLEAN (7)`; all 3 run #2 remedies DECLINED-BY-DESIGN |
| LIQUID | 1 | 1 | 0 | 0 | 0 | 0 | 0% | 1: line cap, LOW |
| MARCO | 3 | 0 | 2 | 0 | 0 | 1 | 33% | `CLEAN (3)`, one stale twin |
| **Total** | **73** | **14 (10)** | **18** | **0** | **4 (3)** | **37** | **51%** | 9 desks with PROSE-REMEDY · 11 `CLEAN` |

Row arithmetic: 14 + 18 + 0 + 4 + 37 = 73. Desk column: 14+2+4+3+3+2+2+1+2+2+3+4+3+7+6+2+2+7+1+3 = 73.
By form: form 1 = 14 rows (BUILT 9, DECLINED 1, FALSE 4; FP 29%). Form 2 = 59 rows (PROSE-REMEDY 14, BUILT 9, DECLINED 3, FALSE 33; FP 56%). 27 of the 33 form-2 FALSE rows are signal, band, kill or routing rows; the other 6 are base-rate history, governance, judgment rules, a gate registry and a dated census.

**Bottom line:** every remaining A–M PROSE-REMEDY is a file line cap. Eight of the ten distinct items are LOW (bytes bind first). Two (BOND, HENRY MEMORY) are not dominated by arithmetic, and neither has come near its cap since 10/30. No non-line-cap remedy is left unbuilt in A–M.

## §1 Rules applied

- **Signal/kill/routing/band row = FALSE** (task rule).
- **Session count = distinct commit dates on the desk's own `STATUS.md` from the clause's introducing commit (exclusive) to HEAD.** Run #2 counted the whole directory, which also counts other desks' inbox commits (WALTER, PROME). Directory counts are in brackets for comparison, so the lower numbers here are a basis change and not fewer sessions.
- **LOW test:** (STATUS bytes ÷ lines) gives the line at which 32,550 B binds. Below 250 = the byte budget dominates = LOW. Root `read_cap_check.py` run read-only per desk.
- **Line-cap code search:** all git-tracked `.py`/`.sh` of each desk (archives excluded) for `250`, `wc -l`, line-cap names. Only HANS counts lines (`AGENTS/HANS/scripts/doc_audit.py:103`, `:517-518`). Root `read_cap_check.py` counts bytes.

## §2 PROSE-REMEDY rows (14 rows, 10 distinct)

Cost column: max STATUS lines in any committed version since 10/30 · bytes now / % of 32,550 B.

| Desk | file:line | Token | Quoted line | What is unbuilt; what it costs |
|---|---|---|---|---|
| BOND | CLAUDE.md:49 | `PROSE-REMEDY (55)` [128] **not LOW** | "STATUS.md should stay under 250 lines. If it's growing, archive old research to `domain/sources/`." | A line count. 119 B/line, so bytes bind only near 271 lines (the ORACLE precedent from run #2; run #2 listed this row as LOW). **Does not matter now:** max 120 lines; 13,917 B / 43%. One real breach in the record: 276 lines in an 8/18 version, when the file was also 88 KB (end of day 241 lines / 88,138 B), so bytes would have caught it. |
| HENRY | CLAUDE.md:235 | `PROSE-REMEDY (63)` [150] **not LOW** | "`MEMORY.md` … ≤100 lines; check `wc -l AGENTS/HENRY/MEMORY.md` from the repository root." | The comparison (the count is a named command). 262 B/line puts 100 lines at about 26 KB, so lines bind first. **Does not matter now:** 67 lines, max 79 since 10/30. The only touch of the cap found since 7/01 is 100 lines on 7/28. |
| CARL | CLAUDE.md:158 | `PROSE-REMEDY (94)` [178] LOW | "STATUS.md stays under 250 lines. Archive to `domain/sources/`." | Line count. Bytes bind near 174 lines. Max 129 · 22,426 B / 69%. `:114` already names `read_cap_check` ("whole-read bytes, not line counts"). Owner deferred WQ-678 K13 (this duplicate) to its 12/01 charter review (`AGENTS/CARL/research/2026-11-14_L150/READ.md`): a date, not a reason to stay prose, so not DECLINED. |
| CARL | CLAUDE.md:257 | same remedy (89) [172] LOW | "Primary memory. ≤250 lines." | as :158 |
| CORAL | CLAUDE.md:60 | `PROSE-REMEDY (30)` [92] LOW | "Keep under 250 lines; archive overflow to `workbook/` or `archive/`." | Line count. Bytes bind near 152. Max 143 · 29,581 B / 91%. `:34` names `read_cap_check`. Owner "declined for now" WQ-678 F43 as a text trim deferred to a quieter session (`STATUS_DETAIL.md:2105`): deferral, not a design reason. |
| CORAL | CLAUDE.md:134 | same (30) LOW | "STATUS.md stays under 250 lines." | as :60 |
| CORAL | CLAUDE.md:221 | same (30) LOW | "Primary snapshot. ≤250 lines." | as :60 |
| CRUISE | CLAUDE.md:75 | `PROSE-REMEDY (24)` [50] LOW | "Compress. STATUS.md should stay under 250 lines." | Line count; no desk scripts exist. Bytes bind near 177. Max 153 · 28,117 B / 86%; charter does not name `read_cap_check`. |
| FERT | CLAUDE.md:159 | `PROSE-REMEDY (25)` [50] LOW | "STATUS.md ≤250 lines, REWRITTEN not prepended (blueprint R3)" | Line count only. Byte leg IS code: `AGENTS/FERT/closeout_check.py:80-82` runs `read_cap_check.py --agent FERT` (`f785f97244`, 10/28; run #2's "byte leg unwired" missed it). Max 124 · 27,919 B / 86%. |
| FLG | CLAUDE.md:164 | `PROSE-REMEDY (15)` [37] LOW | "STATUS.md ≤250 lines and inside root's read-cap budget (root § Data Hygiene)" | Line count only. Run #2's drifted local byte constant (32,000 B) is gone (`34d6a74649`, 11/16). Max 175 · 22,547 B / 69%. Bytes bind near 239. |
| HENRY | CLAUDE.md:113 | `PROSE-REMEDY (90)` [183] LOW | "STATUS.md stays under 250 lines." | Line count. Bytes bind near 123, the current length: 123 lines · **32,338 B / 99%**, so the line cap reads half-empty while the byte budget is 212 B from breach. STATUS was 22,441 B on 11/24. Charter names the byte check for LESSONS only (:232). WQ-678 K38–K52 (K52 = this duplicate) sit in HENRY MEMORY.md:67 as open. |
| HENRY | CLAUDE.md:231 | same (87) [180] LOW | "Primary memory. ≤250 lines." | as :113 |
| ISHM | CLAUDE.md:265 | `PROSE-REMEDY (10)` [22] LOW | "≤250 lines and under the 32,550 B read budget, REWRITTEN not prepended;" | Line count only; byte leg named at :267. Max 61 · 10,884 B / 33%. |
| LIQUID | CLAUDE.md:88 | `PROSE-REMEDY (98)` [180] LOW | "STATUS.md stays under 250 lines." | Line count. Bytes bind near 123. Max 112 · 24,034 B / 74% (run #2: 92%, rotated since). Charter names no byte check. |

## §3 LABOR, graded at the artifact (run #2's three remedies)

Owner answer `inbox/processed/2026-11-05_from-LABOR_prose-remedy-census-2-answer.md`: 3 of 3 DECLINE, with reasons. No code was added, so nothing is BUILT. All four rows are `DECLINED-BY-DESIGN`.

| Remedy | file:line | Owner's claim | Checked at the artifact |
|---|---|---|---|
| B5b | CLAUDE.md:24 "Any card dated ≤ today whose grade is not already written into `STATUS.md` is owed work" · :65 "For each card whose date is ≤ today, ask one question: has it been GRADED?" | `catalyst_countdown.py` prints unpruned dated rows as PAST DUE; the 11/3 JOLTS miss was an unlaunched session | **HOLDS.** `AGENTS/LABOR/scripts/catalyst_countdown.py:89-113` prints the block first and unconditionally. Card moves to `graded/`: 11/03 JOLTS on 11/05 (2 days late, the owner's own case); 11/05 claims and Challenger, 11/06, 11/12, 11/19 and 11/25 each on the card date. Top level holds only 12/01 and 12/03 cards (not due). **0 unconsumed-card misses since the decline.** Residual: a card whose catalyst row was pruned is in nobody's list; no instance found. |
| B5 | CLAUDE.md:52 "must not diverge in event set" | Graded rows collapse to pointers, so strict equality would flag every closeout; L-34's failure (no row at all) is invisible to it | **First leg HOLDS** (STATUS:100-103 are collapsed pointers). **Second leg holds for L-34's case** (no TSV row and no card for the next print). **But the sets do differ today among open events, in both directions:** TSV 12/02 BLS Metro (LOW, "No threshold: record-only") and 2027-01-29 ECI ("Card owed ~2027-01-22") are not in the STATUS calendar (:104); STATUS "Dec 8 … productivity revised (no line)" has no TSV row. Cost today: none, as the first two are in the machine feed the boot reads and the third carries no line. So the charter sentence is not literally true; the decline stands. |
| C2-0 | CLAUDE.md:87 "every OPEN row ≥60% confidence whose confidence has not moved in 60+ days" | Four OPEN rows, one ≥60%, LAB-19 moved 34 days ago | **HOLDS exactly** at `833528e756^`: LAB-08 4%, LAB-12 8%, LAB-18 10%, LAB-19 81% [10/02]. Now 7 OPEN, one ≥60% (LAB-21 68% [11/05], 20 days). Nothing selected, then or now. |

LABOR CLAUDE.md:52 is a form-1 row (it names the script), :24/:65/:87 are form 2. The decline is written in the packet, not on the surface, so the generator will re-list these rows; the packet is the owner's reason.

## §4 BUILT (18)

Read, not falsified under CHECK_STANDARD §3, except where "run" is stated. "Stale" means the surface line lags the code.

| Desk | file:line | Quoted line | Code |
|---|---|---|---|
| AEOLUS | CLAUDE.md:81 | "Checkable form: the brief's commit timestamp ≥ your last STATUS commit timestamp." | root `scripts/brief_pin_check.py:119` (A10 fallback); run 11/25: OK-SAME-COMMIT, rc 0. Wording is superseded A10. |
| BOND | CLAUDE.md:28 | "Run `python3 monitors/docket_check.py` … keys on CUSIP" | `AGENTS/BOND/monitors/docket_check.py:107`, `:131` |
| BROCK | CLAUDE.md:61 | "Budget is BYTES, not lines: `scripts/read_cap_check.py --agent BROCK`" | root `scripts/read_cap_check.py:72`, `:873` |
| CREED | CLAUDE.md:145 | "check with `scripts/read_cap_check.py --agent CREED`" | same |
| CRUISE | CLAUDE.md:47 | "Ledger staleness check … `scripts/ledger_staleness.py` CRUISE" | root `scripts/ledger_staleness.py:173` (content clock), named on the line |
| DEWEY | CLAUDE.md:180 | "Review dates ≥ today; no semicolons, tabs or line breaks" | root `scripts/corrections_boot_check.py:301-302` |
| FALCON | CLAUDE.md:98 | "Size check by instrument, never by a remembered number: … `read_cap_check.py` … replaced the \"under 250 lines\" prose 2026-10-09" | root `read_cap_check.py`; new candidate by the case-insensitive fix, not a remedy |
| FALCON | CLAUDE.md:145 | "STATUS.md stays under 250 lines." (stale twin of :98) | same. WQ-678 E-FA3 asked to strike it; FALCON deferred Changelist B 11/16 to its read-cap session (`reports/2026-11-16_bahrain-bab-card-grade.md:58`). STATUS 30,020 B / 92%. |
| GIBBS | STATUS.md:60 | "the tool itself was not run because it writes FORGE output files even in `--dry-run`" (stale) | Fixed 11/16: `FORGE/tools/filing-watch/poll_edgar.py:204`, `:207` gate writes on `not args.dry_run` (`4634486e3e`, D:L902). A dated 10/31 read whose reason no longer holds. |
| HANS | CLAUDE.md:21 | "MATCH STATUS CELLS BY PREFIX, NEVER BY EXACT MEMBERSHIP" | `AGENTS/HANS/scripts/boot.py:82`, `:94` |
| HANS | CLAUDE.md:25 | "RUN `scripts/finding_check.py`'s `gate()`" | `AGENTS/HANS/scripts/finding_check.py:135`; construct validity declared judgment |
| HANS | CLAUDE.md:95 | "STATUS.md stays under 250 lines." | `AGENTS/HANS/scripts/doc_audit.py:517-518` |
| HENRY | CLAUDE.md:66 | "a date inside the next 14 days … sat ≥10 days unread" | `AGENTS/HENRY/scripts/boot.py:453-454`, `:486`, `:501`, `:514` |
| HOMER | CLAUDE.md:233 | "Checkable form: the brief's commit timestamp ≥ the session's last STATUS commit timestamp." | `brief_pin_check.py:114-119`; run 11/25: STALE-PIN, advisory under WQ-719 A, rc 0. A10 wording. |
| ISHM | CLAUDE.md:266 | "at ≥75% (24,412 B), rotate the oldest history blocks" | root `read_cap_check.py:72`, `:873`; the rotation is manual |
| LABOR | CLAUDE.md:83 | "A card is owed when a print is multi-loaded … or is a quarterly …" | `AGENTS/LABOR/scripts/card_required_check.py:62-79` patterns, `:176-200` late/missed; boot leg `scripts/boot.py:51` |
| MARCO | MAINTENANCE.md:108 | "a `date+event` uniqueness check is one line — built into `catalyst_countdown.py` by `572cad695`" | `AGENTS/MARCO/scripts/catalyst_countdown.py:90`. Not stale: see §6. |
| MARCO | CLAUDE.md:159 | "STATUS.md stays under 250 lines." (stale twin of :52, which names `read_cap_check`) | same root tool. MARCO holds all charter edits that arrive by agent message (`STATUS.md:103`). |

## §5 FALSE (37)

| Desk | Lines | Why |
|---|---|---|
| AEOLUS (13) | CLAUDE.md:155, :158, :159, :160, :163, :164, :165, :171, :191, :192, :209 | Signal/band/exit rows. :155 "ACE vs normal … ≥110%" · :158 "South Africa corn … ≤−15%" · :159 "Australia wheat … ≤−15%" · :160 "WINTER heating demand … ≥+10%" · :163 "Reinsurer cat-loss tally … ≥110%" · :164 "Panama Canal daily transits … ≤32" · :165 "READ THE ROW ABOVE WITH THIS GUARD" · :171 "Colorado River implementation milestone" · :191 "Kaub … ≤ 40 cm" · :192 "Duisburg-Ruhrort … ≤ 180 cm" · :209 "Kaub daily mean ≥77 cm on 10 consecutive complete days" (exit rule, graded by hand in STATUS:85, 7 of 10; no desk script) |
| AEOLUS | CLAUDE.md:203 · :351 | "BASE-RATED 2026-10-31 (KB-AEO-230 …)" = recorded base rate · "Promotion to a core channel (C7) requires ≥3 trigger fires" = governance |
| BROCK (3) | CLAUDE.md:30 · :170 · :179 | "Before registering any threshold, run two tests" = judgment · "default rate declining 2 consecutive quarters" and "BCRED redemptions fall below 2% for 2 consecutive quarters" = kill/exit rows |
| CARL (1) | CLAUDE.md:207 | "~~CC 90+ DQ >13.74%~~ … ≥7.50% (CRL-30)" = routing row |
| CREED (1) | MAINTENANCE.md:28 | "SCRATCH \"owed out\" … CLOSED unsent" = closed item |
| CYPHER (1) | CLAUDE.md:72 | "Wake bar: an estimated loss ≥ $500M" = event wake row (new 11/02) |
| DEWEY (1) | CLAUDE.md:235 | "Slate-building method … adversarially verify each candidate" = method |
| FERT (2) | CLAUDE.md:114 · :145 | "GATE-FERT-G5 (DTN retail DAP or MAP > $1,000/ton)" = gate registry · "food-at-home ≥+0.4% m/m" = routing row |
| FLG (3) | STATUS.md:136 · CLAUDE.md:147 · :149 | "Owed to me: ① ~~WALTER harness verdict~~ ✅" = done receipts (the exit-code flag is another desk's and was handed over) · "ACL/nonaccrual coverage moves ≥10pp" and "loans QoQ turns positive ≥2 quarters" = routing rows |
| GIBBS (2) | CLAUDE.md:14 · :139 | "the perimeter is a NAMED LIST, not an asset line" = read instruction · "`INDUSTRY-WIDE` on ≥2 items" = routing row |
| HANS (4) | CLAUDE.md:161 · :162 · :163 · :167 | "EA core HICP ≥2.5 watch" · "UK core CPI ≥3.0 watch" · "ECB Deposit Rate hike to ≥2.75%" · "EU storage gap to 5-yr norm" = band rows |
| HENRY (2) | MAINTENANCE.md:140 · CLAUDE.md:171 | "Still owed to Will: post-change eval re-run" = discharged at MAINTENANCE.md:127 "POST-WIRING EVAL RE-RUN … 3/3 PASS" · "USD/JPY … \|Δ\| ≥2%/day" = signal row |
| HOMER (1) | CLAUDE.md:109 | "RUNG CENSUS (2026-08-23 …) Test every RUNG" = dated census; the all-observations test is not coded (grep `tools/*.py`: 0), unchanged from run #2 |
| LABOR (2) | CLAUDE.md:192 · :260 | "U-3 ≥5.0% (grade JOINTLY with LFPR — L-06)" = routing row · "Cohort-to-base ratio ≥~10%" = indicator reference |
| MARCO (1) | CLAUDE.md:191 | "MIA negative YoY, 2 consecutive months" = routing row |

## §6 Verdict changes since run #2, and corrections to run #2

| Item | Run #2 | Now |
|---|---|---|
| LABOR B5b / B5 / C2-0 | PROSE-REMEDY ×3, not LOW | DECLINED-BY-DESIGN ×3 (§3) |
| LIQUID line cap | LOW, STATUS 92% of bytes | LOW, STATUS 74%. The live risk is gone. |
| FLG | LOW + drifted byte constant | LOW; constant removed `34d6a74649` |
| HENRY :54 ordering | BUILT, A10 wording | resolved: names `STATUS commit: <hash>` A11 form; not a candidate |
| BOND line cap · HENRY MEMORY cap | LOW · LOW | re-graded not LOW by the byte arithmetic, no consequence seen |
| AEOLUS :189, BRENT SCRATCH:12, BROCK :70, HOMER :291, LIQUID :84 and :146 | FALSE/BUILT | no longer candidates |
| **Correction: MARCO MAINTENANCE** | "'worth adding' clause … delete ask not executed" | **Run #2 was wrong.** `git show c1ad5137f:AGENTS/MARCO/MAINTENANCE.md` line 108 already read "built into `catalyst_countdown.py` by `572cad695`" (owner edit `693f391708`, 10/10). |
| **Correction: FERT byte leg** | "byte leg unwired" | `closeout_check.py` wired it 10/28 (`f785f97244`), two days before run #2. |

A–M remedies built since run #2: **0** (3 declined by the owner; none needed typing). PROSE-REMEDY 18 rows / 13 distinct → 14 / 10; the fall is the three LABOR declines.

## §7 Step-3 sentence and limits

**0 rows typed; premise-verified at the source for 0 of 0.** Nothing here is fixed.
1. "No code computes it" was searched in git-tracked desk code and root `scripts/`; hooks, CI and `PROME/tools/` were not.
2. Two root tools were run read-only: `brief_pin_check.py` (AEOLUS, HOMER, HENRY; rc 0) and `read_cap_check.py --agent` (12 line-cap desks, all rc 0). No desk script was run.
3. Byte state seen on the way, not counted: rotate tier (≥75%) at HENRY 99%, AEOLUS 98%, FALCON 92%, CORAL 91%, CRUISE 86%, FERT 86%, MARCO 80%. The byte tool is advisory at that tier (rc 0). HENRY and AEOLUS were committed today and may be mid-session.
4. Same wording, not candidates: GIBBS CLAUDE.md:154 and CYPHER CLAUDE.md:189 ("≤250 lines and under the 32,550 B read budget"), CARL CLAUDE.md:256 ("Cap 100 lines").
5. No build, rule or packet is recommended. Non-LOW costs are stated in §2 and are nil on the evidence read.

**Closed:** 2026-11-25 14:58 EST (`date`)
