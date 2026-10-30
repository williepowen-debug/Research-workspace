# R1 — ARCHITECTURE / SPINE — FALCON whole-profile refresh 2026-10-30

**Reader:** R1 of 3 (DAEDALUS-spawned, read-only). **Started:** 2026-10-30 17:38:31 EDT (`date`). **Report written:** 17:42:53 EDT onward.
**HEAD at start:** `b2188833f`; **HEAD at write:** `2da72dad7` (other desks' commits; none touch `AGENTS/FALCON/`).
**FALCON tree state:** `git status --porcelain -- AGENTS/FALCON/` = **empty** at 17:38:31, 17:38:50 (before scripts), after scripts, 17:41:23 and 17:42:53. Last FALCON commit throughout: `475f2dea6 2026-10-30 16:49:55` ("NEXUS brief re-pinned to STATUS 87a5097a9"). **No FALCON commit landed mid-read.**
**Writes:** this file only. Mutation tests ran on copies in `/tmp/claude-1000/falcon-r1/FALCON/` only.
**Scripts run (none write the tree):** root `scripts/read_cap_check.py --agent FALCON`; `PROME/tools/reads_check.py --agent FALCON`; `scripts/brief_pin_check.py FALCON`; an import of `read_cap_check.boot_reads()` (in-memory). FALCON's five watch scripts were **read, not run**, because four of them write their `*_state.json` files into the tracked tree.

---

## A. File anatomy

Budget = 32,550 B (root Data Hygiene); cap = 54,250 B. "Boot" means the charter tells a session to read the file whole.

| File | Bytes | % of budget | Role | In-content stamp | State |
|---|---:|---:|---|---|---|
| `CLAUDE.md` | 50,986 | **157%** (94% of the cap) | Charter. Spawned card step 1 says to read it explicitly | No header date. Last commit `35bd7d149` 10/26 | LIVE. Grew 42,198 B (8/06) → 44,533 (8/20) → 48,131 (9/14) → 49,978 (10/01) → 50,986 (10/26) |
| `STATUS.md` | 13,634 | 42% | Boot 1 / closeout 9. Dashboard | `Updated: 2026-10-30 ~16:49 EDT` | CURRENT. Matches the desk's last commits |
| `SCRATCH.md` | 3,354 | 10% | Boot 2 / closeout 13 | `October 30, 2026, ~16:49 EDT` | CURRENT |
| `LESSONS.md` | 24,319 | **74.7%** (93 B below the 75% rotate line) | Boot 3 | Newest entry FAL-14, 2026-09-28; rotated 9/11 | LIVE. Unchanged since 9/28 |
| `MEMORY.md` | 23,209 | **71%** | Boot 3b (adds the 🔴 CARRIED OPEN section) | Newest entry 2026-10-29 | LIVE. Grew 17,527 B (10/01) → 23,209 (10/29), about 200 B/day. **The root read-cap tool does not count it (§E)** |
| `thesis/PREDICTIONS.tsv` | 23,664 | **73%** (748 B below 75%) | Boot 5 | `# As of 2026-10-30` | LIVE. Rotated 10/26 (27,625 → 22,225 B). Since then +1,439 B in 4 days. The comment header is **12,840 B = 54% of the file** |
| `workbook/SCHEMA.tsv` | 1,829 | 6% | Boot 4 (before KB writes) | — | FROZEN, verbatim from HAWK |
| `AGENTS/VOCABULARIES.tsv` | 7,074 | 22% | Boot 4 (before KB writes). Shared file | — | Not in FALCON's perimeter. No FALCON READS row |
| `NEXUS_BRIEF.md` | 6,547 | 20% | Closeout 14. NEXUS reads it whole at boot; HAWK reads it too | `As of 2026-10-30 16:50 EDT`, pin `87a5097a9` | CURRENT. `brief_pin_check` rc 0, OK-PINNED |
| `LAST_COMPLETION.md` | 1,752 | 5% | Completion receipt | `2026-10-29` | **One session behind.** The 10/30 relaunch did not refresh it; its delivery went to PROME/inbox |
| `SOURCES.md` | 12,136 | 37% | Reference index. Its own banner says it is not read at boot | Last additions 2026-09-08 | STALE vs MEMORY: none of NAVAREA IX, `imo.org` or the TankerMap API appear in it (grep = 0) |
| `thesis/THESIS.md` | 8,181 | 25% | Structure. STATUS holds the marks | v3.0 10/01; maintenance review 10/26; **dated rewrite trigger 2026-11-05** | CURRENT |
| `thesis/CHANGELOG.md` | 22,912 | 70% | Audit trail | Last entry 10/29 | LIVE. Title still `# HAWK CHANGELOG`; L5 says "Reverse chronological" but the entries are ascending |
| `thesis/TIMELINE.md` | 41,650 | 128% | Chronology | `Last Updated: 2026-10-29` (War Day 244) | CURRENT. Not read at boot |
| `thesis/PREDICTIONS_ARCHIVE.md` | 69,796 | 214% | Post-mortems and rotated rows | Header scoreboard "as of 2026-07-30" | Header STALE. Body has rotated rows up to FAL-05. No full post-mortem sections for FAL-04/05 |
| `thesis/FAL-01_REREGISTRATION_SCAFFOLD.md` | 15,775 | 48% | Case study, bannered DEAD | Last commit 2026-07-30 (92 days) | **Eligible for retirement** (over 60 days, not read at boot, referenced only by historical header and CHANGELOG lines) |
| `proposals/2026-08-10_self-audit-improvement-slate.md` | 15,155 | 47% | Historical proposal, bannered | Last commit 9/08 | Eligible for retirement around 11/07 |
| `templates/SCRATCH.template.md` | 2,042 | 6% | SCRATCH template | Last commit 7/12 | Title still `# HAWK SCRATCH` (L1) |
| `workbook/EXIT_PROTOCOL.md` | 13,116 | 40% | Falsification rail (v3) | §5 last review 10/29, next 11/04. **§1 kill table and §3 status stamped 2026-10-01** | LIVE. Detail is R2's |
| `board_log.tsv` | 134,298 | 413% | Mail log, grep-only cold surface | — | Read in scope only (READ_CAP rule 8). One repeated id (`SIG-W-20261004-011`) is a dated CORRECTION row, not a re-process |
| `scripts/` (5 `.py` + 4 state JSONs) | — | — | Boot 5a-3, 5b, 5b-2, 5b-3, 5b-4 | Transit state `last_run 2026-10-30T20:41Z`; bypass and baghdad 10/26; kharg 9/16 | All 9 files tracked. See §B |

## B. Boot path

| Step | What it reads or runs | What it checks | Note |
|---|---|---|---|
| Spawned card 1 (L29) | **This charter**, STATUS, SCRATCH. Scan `inbox/WALTER/` and `inbox/` | — | **Yes, boot scans both inbox lanes.** Step 6 (L82–88) processes them only when something is pending. At 17:38 both lanes were empty at top level (WALTER/processed 230, processed 96) |
| Card 2 (L30) | Transit + bypass + "2 staleness checks (5a/5c)" | — | Leaves out 5a-2 and 5a-3 (WARRISK), 5b (Baghdad) and **7b (R1 corrections check)**. Spawned sessions follow the card, so those four steps are not on the fast path (Inferred) |
| 0 (L36) | `git pull` | — | Root canon says a bare charter `git pull` means `--rebase` |
| 1–3b (L37–40) | STATUS, SCRATCH, LESSONS, MEMORY | — | Whole reads |
| 4 (L41) | VOCABULARIES, SCHEMA | Enum validation before a KB write | Conditional |
| 5 (L42) | PREDICTIONS.tsv + calibration preamble | Due or stale rows | — |
| 5a (L45) | `ledger_staleness.py FALCON --quiet` | Workbook content clocks | No `workbook/LEDGER_GLOB` file exists (root step 1c-bis expects one). Referred to R2 |
| 5a-2 (L50) | `ledger_staleness.py --glob WARRISK.tsv --days 7` | WARRISK file clock | The 7-day override is present (do-not-touch #3 ✓) |
| 5a-3 (L68) | `warrisk_row_staleness.py` | Each row's `As_Of` against its own `Stale_By`, registered falsifier first | — |
| 5b (L56) | `baghdad_watch.py` | Embassy RSS diff. Positive-alert backstop only; primary source is CTP/ISW + Shafaq | rc 0/1/2 |
| 5b-2 (L62) | `hormuz_transit_watch.py` | PortWatch chokepoint6, fires on a **band transition**. Retries ×6 since 10/29 | **The docstring (L12, L25) still says rc 1 = "at/below the 18/day bar"**, the superseded rule. The code (L72–92) is correct |
| 5b-3 (L73) | `bypass_watch.py` | Fujairah + Sohar export_tanker against a 30%-of-60-day floor computed at run time. Alarm is INVERTED | **rc 2 = DEGRADED since 10/29 (Sohar series empty upstream)** — no combined verdict |
| 5b-4 (L78) | `kharg_loadings_watch.py` | Positive detection only, optional | Inverted rc kept (L125/129) |
| 5c (L81) | STRIKES.tsv `# swept-complete through:` | More than 7 days behind ⇒ flag | Header reads **2026-10-29**. **STATUS L69 still says "October 28"** |
| 6 (L82–88) | inbox, BOARD (`rg`), WALTER lane (grep membership) | — | — |
| 7, 7b (L89–90) | web_search; `corrections_boot_check.py FALCON` | — | — |
| **Missing** | Root `CLAUDE.md` / `AGENTS.md` / `USER.md` explicit reads; runtime/model identification; `PROME/COMPLETION_SPEC.md` | — | grep finds no "COMPLETION_SPEC", "runtime" or "USER.md" in the charter. Practice covers it: STATUS L3 records the runtime and model |

## C. Current judgment

| Item | Finding | Receipt |
|---|---|---|
| Where it lives | `STATUS.md` (marks), `NEXUS_BRIEF.md` (consumer brief), `SCRATCH.md` (handoff) | — |
| Date | STATUS `Updated: 2026-10-30 ~16:49 EDT`. Its last commit is `87a5097a9 16:49:55`. The brief pin equals the STATUS HEAD (`brief_pin_check` rc 0) | Verified |
| Agreement with the desk's last commits | Consistent. The marks B 1 / C 14 / D 85, convergence 43/50, census 6, and FAL-06/07 OPEN match across STATUS L9–14, SCRATCH L4, NEXUS L3 and PREDICTIONS L4 | Verified |
| BOTTOM LINE currency | CURRENT (10/30 grade). It is **9 sentences**; charter L304 asks for 2–4. The heading has no date of its own; the header line dates it | Verified |
| Internal staleness | (1) STATUS L69 says the facility high-water is "October 28"; the STRIKES header says 2026-10-29. (2) NEXUS_BRIEF L63 says "Not covered 10/29: CTP/ISW Iraq/PMF, cyber/cable", but NEXUS L20 and STATUS L71 report both as covered in the 10/29 afternoon pass. (3) LAST_COMPLETION is still 10/29 | Verified |
| Review cadence | Weekly review was owed 10/28 and done 10/29, one day late and disclosed (STATUS L9; LAST_COMPLETION L2). The only commits in `AGENTS/FALCON/` on 10/27–28 are WALTER drops | Verified |
| Open Will decision | FAL-07 failure-search date (12/31 vs a 1/2 exception), routed to PROME on 10/30. Not urgent before 12/31 | SCRATCH L32 |

## D. Thesis and the scenario ladder

| Item | Finding | Receipt |
|---|---|---|
| **Ladder shape** | **The live ladder has three tiers, B/C/D, with no Scenario A.** The brief for this refresh called it "A/B/C/D". That label comes from the charter's own stale text: L37 ("scenario framework (A/B/C/D)"), L223 ("C→B, B→A") and the L288 heading ("A/B/C/D ladder inherited wholesale"). Charter L298, THESIS L46 and EXIT §2 L40 ("no Scenario A") all say three tiers. L298 itself warns that an A/B/C/D attribution to FALCON means "you are reading a pre-7/27 document", and the charter does this to itself | Verified |
| Version and stamps | THESIS **v3.0** (2026-10-01). Maintenance review 10/26. The structural snapshot in its evidence tables is dated 10/01. Marks match STATUS | THESIS L1–7 |
| Refresh trigger | **DATED**, at THESIS L80: FAL-06 resolving · a fifth belligerent axis · a dated Iran-Oman permanent-corridor framework · a third class-(iii) hull loss · or **2026-11-05**. EXIT §5 L103 repeats it ("Checked 2026-10-29"). RITI as a total loss would be the third class-(iii) loss, and SCRATCH L17 has it queued | Verified |
| Kill/exit rail dating | EXIT §5 is dated (last review 10/29, next 11/04). The **§1 kill table carries "status 2026-10-01"** — 29 days old (e.g. row 2 cites PortWatch 9/27, row 4 cites Brent 10/01). The 0/7 headline is restated as current in STATUS L18. §3 D-indicators are "status 2026-10-01, #5 re-read 10/07". Detail is R2's | Verified (stamps); Inferred (impact low: no row is near firing) |
| Charter kill summary | Charter L217–220 still lists the March-vintage bullets (pre-war oil, Brent <$80, BTFP 2.0), though L233 says to use EXIT v3. They are compatible with v3 rows #1/#2/#4/#6 but drop #3, #5 and #7 | Verified |
| Predictions | FAL-06 70%, resolves **2026-11-05** (6 days). FAL-07 65%, window to 12/31. The archive pointers for FAL-01..05 resolve **with content**: each `archive/PREDICTIONS_snapshot_2026-10-26.tsv` row carries its grade (FAILED/CONFIRMED/FAILED/PARTIALLY/FAILED). L30 of the header says the ARCHIVE "will be created at its first closed row", but it has existed since 7/17 | Verified |

## E. Read-cap and size

| Check | Result | Receipt |
|---|---|---|
| Root `read_cap_check.py --agent FALCON` | **rc 0**, 5 files found, none over budget. "PERIMETER IS THE CHARTER HEURISTIC — no declaration in READS.tsv… NOT a clean bill." It puts LESSONS at 75% (93 B headroom) and PREDICTIONS at 73% (748 B), both in the 70–75% band. Charter 50,986 B is "OUT OF PERIMETER by rule 20 unless declared" | Command output 17:38:50 |
| `reads_check.py --agent FALCON` | **rc 2: "NO DECLARED ROWS — perimeter is UNKNOWN, not clean."** `grep FALCON PROME/registry/READS.tsv` returns 0 rows | Verified |
| 🟠 **MEMORY.md is missing from the perimeter** | `boot_reads('FALCON')` returns STATUS, SCRATCH, LESSONS, SCHEMA and PREDICTIONS, but **not MEMORY.md** (23,209 B, 71%), even though boot 3b (L40) says to read it whole. **Cause:** the heuristic's SCOPE marker `"section"` matches within 80 characters after the token ("…**and the `🔴 CARRIED OPEN` section**"), so the file is classed as a scoped read and not counted. **Mutation test on a copy:** changing only `section` to `list` on L40 makes `MEMORY.md boot-step line 40` appear. A first edit removing "never read again" changed nothing, which falsified my first hypothesis. At about 200 B/day, MEMORY reaches 75% (24,412 B) in about 6 days, around 11/05 (Inferred), and **nothing will flag it** | Verified (mechanism); Inferred (date) |
| Rotate tier (≥75%) | No file is past 75% today. **Three boot surfaces sit in the 70–75% band at once**: LESSONS (no growth since 9/28, but any new lesson crosses), PREDICTIONS (its header grows one "As of" line per session, 400–730 B each), MEMORY (not counted) | Verified sizes; Inferred timing |
| PREDICTIONS projection | 22,225 B (10/26) → 22,407 → 22,983 → 23,664 (10/30). It needs one or two more interim header lines to cross 24,412 B. The 11/04 review and the 11/05 FAL-06 resolution will each write one | Verified history; Inferred date |
| Charter | **50,986 B = 157% of budget, 94% of the 54,250 B harness cap**, and growing about 1 KB a month. Spawned card step 1 makes it an explicit whole read, so in spawned mode it is a boot-mandated read over budget. The root tool keeps it out of perimeter unless declared (rule 20) | Verified bytes; Inferred classification |
| Attestation | None. No READS rows, so no ATTESTATION row | Verified |
| `board_log.tsv` | 134,298 B. The charter's grep-only wording is intact (L85–87), and the tool scores it as an honest scoped read | Verified |

## F. Do-not-touch items from the prior profile, re-checked

| # | Item | Now | Receipt |
|---|---|---|---|
| 1 | The 4 committed `*_state.json` files | HOLDS. All tracked (`git ls-files scripts/`). bypass state `primary_floor_daily 32115` (last_run 10/26) | Verified |
| 2 | Inverted rc on bypass and kharg | HOLDS, with an addition: bypass now has **rc 2 = DEGRADED** (missing primary, L124–157), so an empty series no longer reads as a false collapse. rc 1 = collapse (L197), rc 0 = HOLDING (L200). kharg rc 1 = flow (L125), rc 0 = uninformative (L129) | Verified |
| 3 | WARRISK three-clock header and `--days 7` | HOLDS (CLAUDE L50–53; WARRISK header L1–2 carries Cadence + "Last re-pull ATTEMPTED 2026-10-26"). All 5 rows EXPIRED (STATUS L17) | Verified |
| 4 | HAW-10 wording identity | HOLDS (THESIS L58: "Registered text in thesis/PREDICTIONS.tsv is canonical (HAW-10)") | Verified |
| 5 | False-fire register | MOVED: split from STATUS on 9/07 into `domain/FALSE_FIRE_REGISTER.md` (24,224 B, header says canonical home). The old STATUS:178-198 locator is dead | Verified |
| 6 | KB-HAWK duplicate IDs; GI-2026MAR-ISFAHAN | ISFAHAN present (2 hits in STRIKES). The KB-HAWK duplicates were not re-checked (R2) | Partial |
| 7 | 88/day baseline provenance block | HOLDS; moved to `hormuz_transit_watch.py` L45–59 (was 43–57) | Verified |
| 8 | SCHEMA.tsv verbatim | Present, 1,829 B | Verified (presence) |
| 9 | Frozen-with-successor chain | SCAFFOLD dead-banner ✓; ANALYSIS chain now ends at 9/11 (newest); DO-NOT-PORT ✓ (CLAUDE L339) | Verified |
| 10 | Correction about HAWK boot.py | Stands | Not re-checked |

## G. Reconciliation: prior profile and the 10/21 production review (my cluster)

| Item | Now | Receipt |
|---|---|---|
| Prior 🔴 write-back tail (8/6 rulings) | CLOSED (Δ 8/15). `VX-FALCON-SUNK-01` present; VX now has 10 rows incl. CASUALTY-01 | `grep -o '^VX-…' VX.tsv` |
| Prior 🔴 THESIS header/body ladder contradiction | CLOSED. v3.0 carries one ladder (L6, L50–52) | THESIS L6/L46–52 |
| Prior 🟠 EXIT §5 past its own clock | CLOSED for §5 (10/29 → 11/04). CHANGED: the §1/§3 status stamps are now 29 days old | EXIT L24, L73, L102 |
| Prior 🟠 TIMELINE stops 7/27 | CLOSED (10/29, War Day 244) | TIMELINE L3 |
| Prior 🟠 FRESH_LEG / BYPASS_INTEGRITY silent rot | Not re-checked (R2) | — |
| Prior 🟡 CLAUDE FILES table, 3 stale cells | CHANGED. KB, STRIKES and ANALYSIS now say to resolve from the file (closed). New stale cells: LESSONS "through FAL-09 at 9/8" (L316; now FAL-14), TIMELINE "through War Day 193" (L325; now 244), CHANGELOG (L326). **And the table has no row for** `WARRISK.tsv`, `domain/vessel-incidents/VESSELS.tsv` (the census ledger behind "6 confirmed"), `FRESH_LEG_BASELINE.md` (which STATUS L66 says governs the gate letter), `FALSE_FIRE_REGISTER.md`, `CASUALTY_RATCHET.md`, 4 of the 5 scripts, `LAST_COMPLETION.md`, `registry/` | grep of the FILES block L308–340 = 0 hits for each |
| Prior 🟡 MEMORY:30 dead ANALYSIS pointer | CLOSED (MEMORY L50: resolve the newest) | Verified |
| Prior 🟡 LAST_COMPLETION 7/30 | CHANGED. Now 10/29; one session behind again | Verified |
| Prior 🟡 SCRATCH template titled `# HAWK SCRATCH` | **OPEN** | template L1 |
| Prior 🟡 CHANGELOG header says reverse-chronological; practice is ascending | **OPEN** (L5; title `# HAWK CHANGELOG`) | Verified |
| Prior: no dated staleness trigger in the profile | **OPEN. DAEDALUS-owned. This refresh must add one** | prior profile L5 |
| Prior: no `workbook/PUBLISHED.tsv` | OPEN (`ls workbook` shows none) | Verified |
| Prior: P/K/R convergence split credited as a local invention | CHANGED: **gone from STATUS** (0 hits). The matrix is a plain 10-vector 43/50 | Verified |
| Prior: charter 330 lines | CHANGED: 340 lines / 50,986 B (157% of budget) | §E |
| 10/21 PR: A3 PASS (oil as a trade is LIQUID's by charter) | HOLDS. CLAUDE L257 is unchanged. The charter has had 2 commits since 10/21: G3 harness line 10/23 and the FLOW row 10/26. Neither grants a book | `git log` on the charter |
| 10/21 PR: L5 wants a "current clean owner cycle honoring Oct21 review and registered date grading" | PARTIAL. Dated grading is in practice (FAL-06 search ON 11/05, the FAL-07 conflict routed rather than self-edited). But the 10/28 weekly review was one day late, and READS is UNDECLARED (rc 2) | STATUS L9; reads_check |

## H. Ranked route list

| Rank | Sev | Finding (numbers) | Owner | Ask |
|---|---|---|---|---|
| 1 | 🟠 | **Boot perimeter UNDECLARED, and the heuristic undercounts it.** `reads_check` rc 2, 0 READS rows. The root tool leaves MEMORY.md (23,209 B, 71%) out because of the `"section"` scope marker at L40. Mutation-verified | FALCON (declare); DAEDALUS (tool) | FALCON: send a READS manifest packet to `PROME/inbox/` (STATUS, SCRATCH, LESSONS, MEMORY, PREDICTIONS whole; VOCABULARIES and SCHEMA conditional; board_log grep; CLAUDE.md charter_mode) plus an ATTESTATION row. DAEDALUS: record the SCOPE-marker false-scoped class on `read_cap_check.py` ("…and the X section" after a whole-read token) as a PATTERNS candidate. This is a repeat of the marker-word class |
| 2 | 🟠 | **Three boot surfaces in the 70–75% band**: LESSONS 74.7% (93 B headroom), PREDICTIONS 73% (748 B; header 12,840 B = 54% of the file, +1 line per session), MEMORY 71% (+~200 B/day, not counted) | FALCON | Rotate before 11/04: move PREDICTIONS "As of" history lines (all but the newest 2–3) to the archive snapshot, using the FAL-13 grep-F guard. Move MEMORY's struck WQ-230 item and older Findings to a dated archive. Write the next LESSONS entry only after a rotation |
| 3 | 🟠 | **Charter 50,986 B = 157% of budget, 94% of the harness cap**, growing about 1 KB a month (42,198 → 50,986 since 8/06). Spawned card step 1 makes it an explicit whole read | FALCON (with DAEDALUS for the split) | Hot/cold split: move the FILES-table history prose and the long "why" blocks (L52, L65, L80, L87, L320, L339) to a reference file. Declare the charter mode in READS |
| 4 | 🟡 | **Charter calls the ladder A/B/C/D** (L37, L223 "B→A", L288 heading) against its own L298, THESIS L46 and EXIT L40 ("no Scenario A"). It already leaked into this refresh's brief | FALCON | Re-label L37/L223/L288 to "3-tier B/C/D" |
| 5 | 🟡 | FILES table is missing 9+ live surfaces (VESSELS census, WARRISK, FRESH_LEG gate letter, FALSE_FIRE_REGISTER, CASUALTY_RATCHET, 4 scripts, LAST_COMPLETION). Stale cells at L316 (FAL-09), L325 (Day 193), L326 | FALCON | Add rows that point to the files, or to resolve-from-file rules |
| 6 | 🟡 | Two live instructions conflict: L143 "STATUS.md stays under 250 lines" vs L96 (instrument size check, replaced 10/09). L143 and L231 say `domain/sources/` "doesn't exist yet", but STATUS L3 cites a file in it | FALCON | Delete L143's line cap; drop the "dir doesn't exist" clauses |
| 7 | 🟡 | The spawned boot card leaves out 5a-2, 5a-3, 5b and **7b (corrections check)**. The charter has no explicit root-rules read, runtime identification or COMPLETION_SPEC reference (grep 0) | FALCON | Make card step 2 name every boot check, or "run steps 5a–5c + 7b"; add the root-canon read line |
| 8 | 🟡 | `hormuz_transit_watch.py` docstring L12/L25 still says rc 1 = the 18/day level bar; the code fires on band transition (L72–92). An instruction and its correction sit side by side | FALCON | Rewrite the docstring rc block |
| 9 | 🟡 | Internal currency slips: STATUS L69 "October 28" vs STRIKES header 10/29. NEXUS L63 "Not covered 10/29: Iraq, cyber" vs L20/STATUS L71 covered. LAST_COMPLETION one session behind. BOTTOM LINE 9 sentences vs the 2–4 rule (L304) | FALCON | Fix at the next closeout. Either relax L304 to the operator-surface canon or trim |
| 10 | 🟡 | EXIT §1 kill table and §3 stamped 10/01 (29 days) while STATUS restates 0/7 as current | FALCON (R2 to confirm) | Re-stamp §1/§3 at the 11/04 review |
| 11 | 🟡 | SOURCES.md is missing the primaries MEMORY relies on (NAVAREA IX Pakistan NHO, IMO incidents table, TankerMap JSON API, FIRMS area API quirks) | FALCON | Add a 10/14–10/29 block |
| 12 | 🟡 | Retirement: `FAL-01_REREGISTRATION_SCAFFOLD.md` (92 days, eligible now); proposal 8/10 (eligible around 11/07). `PREDICTIONS_ARCHIVE` header scoreboard frozen at 7/30. PREDICTIONS L30 says the archive "will be created" | FALCON | `git mv` to `archive/`; fix the two headers |
| 13 | 🟡 | Inheritance residue: SCRATCH template `# HAWK SCRATCH`; CHANGELOG `# HAWK CHANGELOG` + "Reverse chronological" (open since 8/07) | FALCON | Re-title; fix the order line |
| 14 | 🟡 | Profile has no dated staleness trigger (open since PR#5 9/01) | DAEDALUS | Add a dated clock in this refresh, e.g. FAL-06 resolution 11/05 or the THESIS rewrite trigger |

## I. Coverage

| File | Coverage |
|---|---|
| `AGENTS/FALCON/CLAUDE.md` | WHOLE: L1–90, 90–179, 180–259, 260–340 (340 lines; final line 340 reached) |
| `STATUS.md` | WHOLE (L1–77) |
| `MEMORY.md` | WHOLE (L1–62) |
| `LESSONS.md` | WHOLE (L1–116) |
| `SCRATCH.md`, `LAST_COMPLETION.md`, `NEXUS_BRIEF.md` | WHOLE |
| `SOURCES.md` | IN PART: L1–12, section index, grep for newer primaries |
| `thesis/THESIS.md` | WHOLE (L1–83) |
| `thesis/PREDICTIONS.tsv` | Header L1–30 (each line cut at 400 chars), rows L31–38 by field; archive snapshot grades for FAL-01..05 |
| `thesis/CHANGELOG.md` | IN PART: L1–15, heading index, last 12 lines |
| `thesis/TIMELINE.md` | IN PART: L1–12, heading index, last 6 lines |
| `thesis/PREDICTIONS_ARCHIVE.md` | IN PART: first 600 B, heading index |
| `thesis/FAL-01_REREGISTRATION_SCAFFOLD.md` | IN PART: L1–8 |
| `proposals/2026-08-10_…` | IN PART: L1–25 + grep for references |
| `templates/SCRATCH.template.md` | Headings only |
| `scripts/*.py` | Docstrings (L3–22) plus grep for state/rc/band logic; not run. State JSONs WHOLE |
| `workbook/EXIT_PROTOCOL.md` | IN PART: L24–40 + heading/date grep (R2 owns the rest) |
| `workbook/VX.tsv`, `WARRISK.tsv`, `STRIKES.tsv` | ID / header grep only (R2) |
| `PROME/registry/READS.tsv` | grep FALCON (0 rows), VOCABULARIES rows, header L1–5 |
| `scripts/read_cap_check.py` (root) | L181–376 (boot_reads), the marker constants L96–122 |
| Baseline: prior profile | WHOLE (L1–56). FALCON reply packet WHOLE (found in `DAEDALUS/inbox/processed/`, not `inbox/` as briefed). WAR_TRIAD stub WHOLE. PR 10/21 + reader reports: FALCON-grep hits only |
| NOT READ | `domain/*` contents, `workbook/KB.tsv`/`FLOW.tsv`, `research/`, `reports/`, `outbox/`, `archive/*` bodies (except the PREDICTIONS snapshot grades), `board_log.tsv` whole (by rule) |

**Closing tree check:** see the final line below.

**Closing tree check 2026-10-30 17:44:43 EDT:** `git status --porcelain -- AGENTS/FALCON/` = `` (empty = clean); last FALCON commit `475f2dea6 2026-10-30 16:49:55 -0400`; HEAD `2da72dad7`. No FALCON commit landed during the read.
