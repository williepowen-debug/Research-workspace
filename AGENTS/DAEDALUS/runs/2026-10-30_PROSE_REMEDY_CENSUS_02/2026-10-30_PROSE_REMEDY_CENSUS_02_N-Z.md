# Prose-Remedy Census #2 — step 2 classification, desks N–Z

**Classifier:** non-owner (DAEDALUS-spawned), read-only on the repo except this record. **Started:** 2026-10-30 11:31 EDT (`date`). **HEAD:** c1ad5137f. **Input:** `AGENTS/DAEDALUS/runs/2026-10-30_PROSE_REMEDY_CENSUS_02/2026-10-30_PROSE_REMEDY_CENSUS_02_CANDIDATES.tsv`, rows for NEXUS · ORACLE · OSPREY · OTTO · OZK · PROME · RED · REGINALD · SAM · SHADE · TERRY · VIOLET · VULCAN · WAL · WALTER · WATT · YURI · ZHAO (91 rows; header-artefact rows with desk = "desk" ignored). Row numbers (#) below are the ordinal of the row within this N–Z slice of the TSV. **Playbook:** `AGENTS/DAEDALUS/sweeps/PROSE_REMEDY_SWEEP.md` §2. **Prior run:** `runs/2026-10-08_PROSE_REMEDY_CENSUS_01_N-Z.md`.

**Status:** COMPLETE — all 91 rows opened and classified; §0 written last (2026-10-30 11:40 EDT, `date`).

## §0 Summary (91 candidate rows, 18 desks)

| Desk | Candidates | PROSE-REMEDY rows (distinct) | BUILT | DIAGNOSIS-ONLY | DECLINED | FALSE | Step-1 FP rate (FALSE/cand.) | Desk verdict |
|---|---|---|---|---|---|---|---|---|
| NEXUS | 6 | 3 (2; 1 LOW) | 1 | 0 | 0 | 2 | 2/6 | 2 PROSE-REMEDY (page cap; LOW line cap) |
| ORACLE | 10 | 2 (2) | 2 | 2 | 2 | 2 | 2/10 | 2 PROSE-REMEDY (`polymarket.py` NOT-FOUND vs resolved; 250-line cap) |
| OSPREY | 7 | 1 (1 LOW) | 0 | 0 | 0 | 6 | 6/7 | 1 PROSE-REMEDY (LOW) |
| OTTO | 5 | 0 | 3 | 0 | 0 | 2 | 2/5 | **CLEAN (5)** |
| OZK | 2 | 1 (1 LOW) | 1 | 0 | 0 | 0 | 0/2 | 1 PROSE-REMEDY (LOW) |
| PROME | 4 | 1 (1) | 0 | 0 | 0 | 3 | 3/4 | 1 PROSE-REMEDY (WQ-206; approved build DOCKET L730) |
| RED | 7 | 2 (2) | 3 | 0 | 0 | 2 | 2/7 | 2 PROSE-REMEDY (CALENDAR twin event set; hypothesis bounds) |
| REGINALD | 3 | 0 | 1 | 0 | 1 | 1 | 1/3 | **CLEAN (3)** |
| SAM | 9 | 2 (2; 1 LOW) | 5 | 0 | 0 | 2 | 2/9 | 2 PROSE-REMEDY (KOYOMI runway; LOW line cap) |
| SHADE | 7 | 0 | 1 | 0 | 0 | 6 | 6/7 | **CLEAN (7)** |
| TERRY | 2 | 0 | 0 | 0 | 0 | 2 | 2/2 | **CLEAN (2)** |
| VIOLET | 10 | 0 | 4 | 0 | 0 | 6 | 6/10 | **CLEAN (10)** — control present |
| VULCAN | 4 | 0 | 2 | 0 | 0 | 2 | 2/4 | **CLEAN (4)** |
| WAL | 4 | 2 (1 LOW) | 0 | 0 | 0 | 2 | 2/4 | 1 PROSE-REMEDY (LOW) |
| WALTER | 1 | 0 | 0 | 0 | 0 | 1 | 1/1 | **CLEAN (1)** |
| WATT | 3 | 0 | 1 | 0 | 1 | 1 | 1/3 | **CLEAN (3)** |
| YURI | 2 | 0 | 1 | 0 | 0 | 1 | 1/2 | **CLEAN (2)** |
| ZHAO | 5 | 0 | 1 | 0 | 3 | 1 | 1/5 | **CLEAN (5)** |
| **Total** | **91** | **14 rows = 12 distinct** (5 LOW line caps) | **26** | **2** | **7** | **42** | **42/91 = 46%** | 8 desks with ≥1 PROSE-REMEDY · 10 CLEAN · 0 NOT READ |

Row arithmetic: 14 + 26 + 2 + 7 + 42 = 91 ✓. **Substantive (non-LOW) distinct PROSE-REMEDY, 7:** PROME WQ-206 aged-ACTION (47 STATUS dates; Will-approved build L730 unbuilt since 10/15) · NEXUS Will-facing page cap ≤6 KB / ≤150 words (14) · ORACLE `polymarket.py` reports resolved markets as PINNED BUT NOT FOUND (10; carried as a STATUS caveat) · ORACLE STATUS ≤250 lines (27; lines bind before bytes) · RED CALENDAR↔CATALYSTS event-set twin (35) · RED hypothesis count and 2–60% bounds (43) · SAM KOYOMI runway tripwire (23 runs). **Run #1 carry-over:** 8 of run #1's 12 distinct N–Z remedies are BUILT; RED ML-226 (run #1 A5) is still unbuilt but was dropped by step 1 (§2, §3.5). **Step-3 sentence:** 0 rows typed by this run (classification only); premise-verified at the source for 0 of 0.

## §1 Per desk, per row

### NEXUS (6 candidates, all form 2 — `AGENTS/NEXUS/CLAUDE.md`, charter split to rules + provenance `86cb450f7` 10/24; NEXUS has no `scripts/` or `tools/` dir)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 1 | CLAUDE.md:55 | PROSE-REMEDY (41) — LOW | "9. **STATUS sanity check:** under 200 lines (overflow → `STATUS_COLD.md` §H) · Δ convention consistent per row…" | No code counts NEXUS STATUS lines: no desk scripts; root `scripts/read_cap_check.py --agent NEXUS` measures BYTES (run 10/30: `STATUS.md 24,048 B 74% of budget`); `AGENTS/DAEDALUS/scripts/maturity_scan.py` flags >260 lines, a different threshold. Dominated: 105 lines at 229 B/line, so the 32,550 B budget binds at ~142 lines < 200. The other legs of step 9 are judgment reads. | "200 lines" since `c1fc64535` 3/02; 41 NEXUS-subject STATUS commit dates since |
| 2 | CLAUDE.md:63 | BUILT | "Current block ≤ 6 KB; the WHOLE FILE is measured at every session-end commit (the 0a instrument) and rotated at ≥75%" | Root `scripts/read_cap_check.py --agent NEXUS` (BOOT 0a, `CLAUDE.md:26`) run 10/30: `✅ AGENTS/NEXUS/LAST_COMPLETION.md 11,066 B 34% of budget (whole · NEXUS:15a)`, rotate-tier flag at ≥75%. The 6 KB block cap is the owner's "mechanism", not a test. Run #1's stale-claim residue (hand `wc -c`) is gone: the line now names the 0a instrument. | — |
| 3 | CLAUDE.md:91 | FALSE | "A single Polymarket/Kalshi print is not a hold: ≥3-day re-check and cross-source verification, and priced odds are ORACLE's domain" | A market-observation discipline (re-check on 3 days, cite ORACLE), not a computation with a failure direction on a NEXUS surface. The thin-liquidity flag itself is computed at ORACLE (`AGENTS/ORACLE/scripts/polymarket.py` THIN guardrail; run #1 row 37). | — |
| 4 | CLAUDE.md:96 | FALSE | "J. No standing probability without a registered falsifier. Any probability carried across sessions — … held or re-marked ≥2 passes" | Construction rule for falsifiers; "probability carried" and "convergence-level call" are judgment units, not countable fields. No specified computation. | — |
| 5 | CLAUDE.md:155 | PROSE-REMEDY (14) | "Will-facing page cap: ≤ 6 KB; the whole story first in ≤150 words; the caveats that survive simplification inside the page" | Two mechanical legs (page bytes ≤ 6 KB; lead ≤150 words) with no code: grep for `150 words`/`page cap`/6 KB constants over `scripts/*.py`, `PROME/tools/*.py`, `AGENTS/DAEDALUS/scripts/*.py` finds none; `read_cap_check.py` does not measure NEXUS pages. Other legs are judgment. | "150 words" since `ccd55ffaa` 9/29; 14 NEXUS STATUS commit dates since |
| 6 | CLAUDE.md:156 | PROSE-REMEDY (41) — LOW, duplicate of #1 | "STATUS under 200 lines (overflow → `STATUS_COLD.md` §H); long-form reports → `research/`." | Same uncomputed line cap as #1. | as #1 |

**NEXUS step-1 FP rate: 2/6.** Desk verdict: 2 distinct PROSE-REMEDY (1 LOW line cap, 1 page cap). Run #1's pin-check remedy (A1) is BUILT: repo-root `scripts/brief_pin_check.py` (`d67d4b431` 10/08), named at `CLAUDE.md:33` step 6.

### ORACLE (10 candidates; `scripts/` = kalshi, polymarket, test_cred_modes, test_mid_flag_edge, test_search_coverage; `tools/` = daily_pull.sh, disruption_supply_spread, metrics, routine_check, t6_pin, trade_marks)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 7 | MAINTENANCE.md:79 | FALSE | "CLAUDE.md (closes PROME/DAEDALUS PAT-041, inbox 7/10): the tool's run-cadence + WTI-month-roll owed-action were homed only in SCRATCH" | Unchanged since run #1 (row 34): a 7/17 history entry recording a completed doc move. | — |
| 8 | MAINTENANCE.md:188 | DIAGNOSIS-ONLY (not ORACLE's code) | "`workbook/LEDGER_GLOB` — NEW… the pass still reports "8 ledger(s) scanned" and prints seven rows, with HISTORY.tsv silent" | The defect is in repo-root `scripts/ledger_staleness.py` (owner named on the line as PROME; root `scripts/` is now DAEDALUS-granted). No remedy specified (cause hypothesised: no `ts`-named column). **Still reproduces 10/30:** `python3 scripts/ledger_staleness.py ORACLE` prints "7 ledger(s) scanned" and six rows; `workbook/HISTORY.tsv` (declared in `workbook/LEDGER_GLOB`) has no row. Live on `SCRATCH.md:54` "counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched)". Route to the `scripts/` owner, not ORACLE. | defect open since 8/27 |
| 9 | MAINTENANCE.md:202 | DIAGNOSIS-ONLY | "NEW TOOL GAP #1 — `polymarket.py history` writes TWO rows stamped with today's date… never dedupes" | Owner rejects the obvious remedy ("Do not "fix" it without deciding which consumer you are serving"); the right fix ("a separate intraday accessor") is named but not specified. Code unchanged: `scripts/polymarket.py:220-243` `clob_history()` appends every point with a UTC date string, no dedupe. Run #1 listed this as a recall miss. | — |
| 10 | MAINTENANCE.md:204 | DECLINED-BY-DESIGN | "CONFIRMED, NOT FIXED — `t6_pin.py` prints no leg summary after `WIN_END`… T6 is spent, so fixing it would be maintenance on a dead instrument." | Unchanged since run #1 (row 36); owner's written reason stands. Accept, never re-flag. | — |
| 11 | MAINTENANCE.md:219 | DECLINED-BY-DESIGN (weak) | "2026-09-07 — `kalshi.py event <SERIES>` reads a date-stamped series as a delisting (tool gap, logged not patched)" | Entry body `:223-224`: the fix ("`event` to fall back to the series endpoint… or print `SERIES-NOT-EVENT`") is "a build, not a one-liner", and "**Boot-impact: discipline, not code** — never conclude a Kalshi market is gone from an `event` zero; confirm with `search`, which certifies its own coverage." Owner chose discipline and named the certified alternative. Code unchanged (`scripts/kalshi.py` has no series fallback in the event path). Weak: the reason is cost, not design; DAEDALUS may rule it PROSE-REMEDY (11). | 11 ORACLE STATUS dates since 9/07 if re-ruled |
| 12 | MAINTENANCE.md:230 | PROSE-REMEDY (10) | "`polymarket.py pull` reports a RESOLVED market as `PINNED BUT NOT FOUND`, which buries a finding inside a maintenance warning." | Remedy specified on the surface: "a fix means querying the closed-market endpoint before reporting absence". Not built: `scripts/polymarket.py:478-481` still prints "⛔ PINNED BUT NOT FOUND — re-pin or retire" with no closed-market query (the `closed` flag at `:114` is read only for markets the slug lookup returns). Carried live as a caveat in place of the fix: `STATUS.md:126` "PINNED BUT NOT FOUND cannot tell resolved from a bad slug. Query `closed=true` first (10/28: both not-founds were resolutions)"; `SCRATCH.md:49` "(KB-ORC-101; held again 10/28)". The cost has recurred (9/17 WTI-$100, 10/28 two resolutions). | entry `d023cce33` 9/17; 10 ORACLE STATUS dates since |
| 13 | MAINTENANCE.md:298 | FALSE | "`scripts/kalshi.py` `fmt_row`: spread and |yes − mid| rounded to 4 dp before the edge comparisons… New `scripts/test_mid_flag_edge.py` (7/7 PASS" | DONE entry (10/09). Its "counter is owed only if Will approves" is a gated proposal (PROPOSAL, NOT ENCODED), not a carried remedy. | — |
| 14 | CLAUDE.md:56 | BUILT | "thin (<$5K liq) = ≥3-day re-check, never mark on one print; `[STALE]`-mark > carry-forward-as-current" | Run #1 row 37 (was `:54`) re-checked at HEAD: `scripts/polymarket.py:30-31` `THIN_LIQUIDITY = 5000.0`, `THIN_VOLUME = 5000.0`, `thin=True` flag. Residual (the ≥3-distinct-day count before marking) is printed advice, uncounted — noted, not counted. | — |
| 15 | CLAUDE.md:65 | PROSE-REMEDY (27) | "- **Compress.** STATUS.md under 250 lines." | No ORACLE script counts STATUS lines (grep of `scripts/*.py`, `tools/*.py` for `250`/`wc -l`: only Gamma page sizes); root `read_cap_check.py` measures bytes. NOT dominated: at 118 B/line (134 lines, 15,815 B) the byte budget binds at ~276 lines, so the 250-line cap binds first. Never breached (134). | since `800e89dd3` 4/02; 27 ORACLE STATUS dates since |
| 16 | CLAUDE.md:220 | BUILT | "Thin-liquidity guardrail (baked into the fetcher): markets < $5K liquidity are flagged ⚠️ `thin`… require a ≥3-day re-check" | Same computation as #14 (`scripts/polymarket.py:13-15,30-31`); same uncounted ≥3-day residual. | — |

**ORACLE step-1 FP rate: 2/10.** Desk verdict: 2 PROSE-REMEDY (1 tool fix, 1 line cap).

### OSPREY (7 candidates, all form 2; code = `scripts/strike_feed.py` + `scripts/tests/`; no `tools/`)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 17 | CLAUDE.md:87 | PROSE-REMEDY (31) — LOW | "- STATUS.md stays under 250 lines. Archive overflow to `domain/energy-strikes/` dated analysis files or `research/`." | Narrowed since run #1: closeout step 9 (`CLAUDE.md:48`) now names `PROME/tools/measure.py` "(lines + bytes)" — but `measure.py` only MEASURES (10/30 run: "112 lines (wc -l)"), it compares nothing against 250 and has no failure direction. `strike_feed.py` has no size logic. Dominated: 202 B/line (112 lines, 22,633 B) ⇒ the 32,550 B budget binds at ~161 lines < 250. | rule `3fb46ebdf` 7/12; 31 OSPREY STATUS dates since |
| 18 | CLAUDE.md:156 | FALSE | "Channel 2 (crude-export terminals) kill: no `crude-terminal`/`pipeline`/`oil-port`-class row whose struck asset lies on the Black Sea… for 30+ days AND seaborne crude exports hold ≥3.5M bpd" | A domain kill rule graded on a geography judgment plus an external Kpler/Bloomberg aggregate; not a desk-process remedy. (C2 KILLED on its letter 10/09, `fd547eaf4`.) | — |
| 19 | CLAUDE.md:171 | FALSE | "Rule: a channel steps DOWN one mark when the evidence that fired its Upgrade Trigger reverses on the SAME instrument for two consecutive prints AND no new in-channel `STRIKES.tsv` row…" | Domain mark-downgrade rule on external prints (Bloomberg 4-wk, EA/Kpler monthly). Not a carried remedy. | — |
| 20 | CLAUDE.md:172 | FALSE | "Back-test at ruling: no 4-wk print ≥ 3.9 M bpd since the week to 8/2… BRENT and HAWK have 7 days (to 2026-09-15) to object" | History of the 9/08 ruling and an expired objection window. | — |
| 21 | CLAUDE.md:190 | FALSE | "Brent sustains a break >$85 for 3+ sessions with ≥2 institutional legs (BRENT-owned call) AND at least one of those legs names Russia/Ukraine-theater causation" | Thesis-break rule owned by BRENT's call plus an attribution judgment. | — |
| 22 | CLAUDE.md:196 | FALSE | "> "Brent sustains a break >$85 for 3+ sessions with ≥2 institutional legs (BRENT-owned call) → decoupling thesis broken" | Quoted superseded text of #21. | — |
| 23 | CLAUDE.md:205 | FALSE | "OSP-06 (no sustained recovery to ≥3.9 M bpd on Bloomberg's 4-wk series by Oct 15): CONFIRMED = no such print with an as-of date ≤ 10/15" | Prediction resolution text; OSP-06 graded CONFIRMED 10/15 (`STATUS.md:29,65`, KB-197). | — |

**OSPREY step-1 FP rate: 6/7.** Desk verdict: 1 PROSE-REMEDY (LOW). Observation, not counted: the channel-kill pause clocks (`CLAUDE.md:149` "Measure pauses from the ledger's newest in-channel `Date`, not from memory"; `:166` "breached on 9/18") are a mechanical days-since count over `workbook/STRIKES.tsv` that no OSPREY code computes (`strike_feed.py` has no clock); the lines carrying it carry no step-1 token.

### OTTO (5 candidates; `scripts/` = backfill_collection_period, boot, catalyst_countdown, panel_10d, predictions_due, severity_divergence, shelf_halt_monitor)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 24 | MAINTENANCE.md:103 | FALSE | "`CLAUDE.md` v2.7 → v2.8: the recovery <28% trigger row now says FIRED 2026-09-02… step 7a's Amendment-10 timestamp check replaced by `scripts/brief_pin_check.py`" | DONE history entry (10/14). It records run #1's A2 closing: `CLAUDE.md:192` step 7a now reads "Checkable form (NEXUS Amendment 11…): `python3 scripts/brief_pin_check.py OTTO` prints OK". | — |
| 25 | CLAUDE.md:259 | FALSE | "`[ALLEG]` — litigation / plaintiff allegation only → weight ≤40% pending corporate-side or independent corroboration" | An evidence-weighting judgment cap, not a computation on a surface. | — |
| 26 | CLAUDE.md:287 | BUILT | "OTTO-internal docket steward — spawned every OTTO session with ≥7 days since its last run, plus T-3 pre-hearing." | `scripts/boot.py:81` `WINTERKORN_DUE_DAYS = 7`, `:85` `winterkorn_last_run()`, `:193-195` prints "🟠 WINTERKORN last ran … DUE this session"; fails loud at `:189` "cannot certify the last WINTERKORN run". The T-3 pre-hearing leg is not computed (no `T-3`/`hearing` logic in `boot.py` or `catalyst_countdown.py`) — residual noted, not counted (the hearing dates live in CATALYSTS and the boot countdown prints them). | — |
| 27 | CLAUDE.md:339 | BUILT (duplicate of #26) | "Every OTTO session with ≥7 days since its last run, plus T-3 pre-hearing (was "weekly Tue": it lapsed 81 days while…" | As #26. | — |
| 28 | CLAUDE.md:545 | BUILT (duplicate of #26) | "WINTERKORN.md # Sub-agent spec — docket steward (each OTTO session ≥7d since last run + T-3 pre-hearing)" | File-tree restatement of #26. | — |

**OTTO step-1 FP rate: 2/5.** Desk verdict: **CLEAN (5)**. Run #1's OTTO PROSE-REMEDY (brief ordering, A2) is BUILT via the shared `scripts/brief_pin_check.py`.

### OZK (2 candidates; `scripts/` = boot.py, flng_watch.py)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 29 | MAINTENANCE.md:41 | BUILT | "Still-open parity gaps (queued — see MEMORY NEXT SESSION): no `scripts/boot.py` boot kit; no `thesis/PREDICTIONS.tsv` + calibration scoreboard" | Unchanged since run #1 (row 44, then `:34`): `scripts/boot.py` exists (`68d99587f` 7/04); remaining legs are design decisions. Stale claim in a dated 7/04 history entry, low stakes. | — |
| 30 | CLAUDE.md:144 | PROSE-REMEDY (21) — LOW | "- **STATUS.md stays under 250 lines.** If it grows, archive prior section to `archive/` or push detail to sub-doc." | No OZK code counts lines (`scripts/boot.py` and `flng_watch.py`: no line-cap logic); OZK's charter names neither `read_cap_check.py` nor `measure.py`. Dominated: 171 B/line (121 lines, 20,701 B) ⇒ byte budget binds at ~190 lines < 250. | rule `fab828fb9` 4/24; 21 OZK STATUS dates since |

**OZK step-1 FP rate: 0/2.** Desk verdict: 1 PROSE-REMEDY (LOW).

### PROME (4 candidates; home `PROME/`, code in `PROME/tools/` and repo-root `scripts/`)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 31 | CLAUDE.md:59 | FALSE | "Session Process Controls (WQ-140, forward-only) · FREEZE LAPSED 2026-10-25… the charter target under 20,000 B (`measure.py`) measures the pass and licenses nothing." | A freeze-retirement notice (WQ-549 A, 10/30). The 20,000 B figure is declared by the owner as a measured target that "licenses nothing", not a gate with a failure direction; the measurement is `PROME/tools/measure.py`. | — |
| 32 | SCRATCH.md:61 | FALSE | "[October11 Standard closeout](reports/…) · [accepted WQ414/409/419 owner work](…) (no prior Deck A/B/C presentation work owed)" | A link list; "owed" is negated. Names the built size instrument `scripts/read_cap_check.py --agent PROME`. | — |
| 33 | STATUS.md:13 | FALSE | "Day's desk touches CLOSED (Fri 10/30: six C6 wakes…) … closeout_v1 rows written through `scripts/orch_log.py append`… Fresh spawns owed this afternoon" | Coordination row; "owed" = spawns. The script it names exists (`scripts/orch_log.py`) and is the DONE fix for the hand-appended rows (DOCKET L872). | — |
| 34 | CLAUDE.md:51 | PROSE-REMEDY (47) — WQ-206 leg; WQ-221 leg BUILT; build approved and registered | "Aged ACTION (WQ-206): unconsumed `action:` older than seven days at a DARK owner… → outcome ①, PROME L0 drain-only… Aged waits (WQ-221)" | **WQ-221 BUILT:** `PROME/tools/prome_gate.py:1056` `aged_waits()`, `:1077` `check_aged_waits()`, boot-wired `:1993`. **WQ-206 still uncomputed:** `PROME/tools/spawn_slate.py:67` "The aged-ACTION (WQ-206) and aged-waits (WQ-221) lanes are not computed here"; no `aged_action`/WQ-206 logic in `PROME/tools/*.py` or `scripts/*.py`. Since run #1 the remedy moved from design to an approved build: DOCKET L639 RESOLVED 10/24 (design delivered 10/08); **DOCKET L730** "S1 OWNER-UNCONSUMED BOOT LINE — BUILD (WQ-401 RULED APPROVE 2026-10-15)… labelled 'WQ-206 class'", owner PROME, state "PENDING — registered 2026-10-15… the next process slot", due "next-PROME-process-pass". Unbuilt 15 PROME STATUS dates after Will's approval. | ruled 9/10; 47 PROME STATUS dates since (15 since the 10/15 approval) |

**PROME step-1 FP rate: 3/4.** Desk verdict: 1 PROSE-REMEDY (registered as DOCKET L730; no new packet track — cite L730).

### RED (7 candidates; `scripts/` = base_rate_review, basis_check, board_log_append, boot, closeout_check (+test), gen_trigger_scan, nonsession (+test), review_debt, schema_check, status_mirrors, test_base_rate_flag, test_board_gap, test_tie_atoms)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 35 | MAINTENANCE.md:136 | FALSE | "W1 names `wc -l` + `read_cap_check.py --agent RED` as the binding ≤200-line check (DAEDALUS prose-remedy #1, item 2)." | DONE entry closing run #1's A6. Since superseded by code: `scripts/closeout_check.py:485-487` GATE "STATUS <= 200 lines" FAIL if `n > 200` (`dbf10d5bb` 10/15). | — |
| 36 | MAINTENANCE.md:248 | BUILT | "§⑤ itself is the specified-not-built check flagged at S41 — it is not set-difference based and will read green while a backlog exists" | Run #1 row 52 (then `:108`) re-checked: rebuilt S44 9/12 (`126f78227`) as an ID-diff + `scripts/test_board_gap.py`. History only. | — |
| 37 | MAINTENANCE.md:269 | BUILT | "`scripts/boot.py` still evaluates FT-10 from the mirror… Fix owed in the 9/4–9/11 window: point boot.py's FT-10 evaluation at the CBOE CSV" | Run #1 row 53 (then `:129`) re-checked at HEAD: `scripts/boot.py:87-129` FT-10 reads the CBOE CSV and "The yfinance mirror is NOT substituted"; `MAINTENANCE.md:867` records the fix. History only. | — |
| 38 | MAINTENANCE.md:375 | FALSE | "③ Fleet proposal routed — OUTBOX -021. `review_debt.py` offered to PROME/DAEDALUS as a fleet candidate… Coverage… must ship beside the debt count" | Unchanged since run #1 (row 55): a precondition on an outbound fleet proposal, not a remedy on RED's own instrument. | — |
| 39 | CLAUDE.md:68 | PROSE-REMEDY (35) — twin event-set leg | "W4 Forward state: `docket/CATALYSTS.tsv` is canonical…; `CALENDAR.md` is its narrative twin with the SAME event set… Any catalyst ≤7 days out must already have a written decision tree" | The twin invariant is fully specified (same event set; canon wins). Not computed: `scripts/closeout_check.py` check f compares only the HOLD / net-bear HEADER of CALENDAR vs STATUS (`:24`, `:428`); no RED script or repo-root script diffs the CALENDAR event set against CATALYSTS (grep `CALENDAR` over `AGENTS/RED/scripts/*.py`, `scripts/*.py`: only `docket_view.py`, which serves PROME/DOCKET). The ≤7-day decision-tree leg needs a catalyst→tree match (judgment) — not counted. VIOLET's `scripts/twin_check.py` is a working model. | "narrative twin" since `79ac051d2` 6/10; 35 RED STATUS dates since |
| 40 | CLAUDE.md:118 | BUILT | "Steelman before attacking… STATUS ≤200 lines. Don't pull punches." | `scripts/closeout_check.py:485-487` (as #35). | — |
| 41 | CLAUDE.md:162 | PROSE-REMEDY (43) | "Competing hypotheses: ≥4 scenarios with probabilities in STATUS…; no INDIVIDUAL hypothesis below 2% or above 60% — … a breach needs a written override line" | Fully specified count and bounds on STATUS's hypothesis table with a failure direction. Not computed: grep of `scripts/closeout_check.py`, `schema_check.py`, `boot.py` for scenario/hypothesis/bounds logic finds none (closeout_check's MANUAL list does not name it either). | "above 60%" since `3e4b234ba` 4/02; 43 RED STATUS dates since |

**RED step-1 FP rate: 2/7.** Desk verdict: 2 PROSE-REMEDY. Not on this run's list but open: run #1's A5 (`MAINTENANCE.md:880`, was `:740`, "Nothing compares `boot.py`'s METRIC_MAP source against each row's `instrument_basis` (ML-226)") — still uncomputed (`instrument_basis` appears in `boot.py` only as a comment at `:87`); see §2.

### REGINALD (3 candidates, all form 2; 21 entries in `scripts/` incl. `boot.py`, `earnings_countdown.py`, `thresholds.py`, `vx_ladder_check.py`)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 42 | CLAUDE.md:15 | BUILT | "Print≤~5 trading days: fuller sweep, FROZEN frame, issuer-verified dates/weekdays and POSITIONS checked against latest broker export before fire read." | The comparison is computed: `scripts/earnings_countdown.py:4` "Counts trading days to each bank's earnings date", `:129` flags "⚠️ ≤5d" / "🔴 ≤2d"; selftest `:95` "(want 5)". The "fuller sweep" it triggers is a session mode, judgment. | — |
| 43 | CLAUDE.md:60 | DECLINED-BY-DESIGN (weak) | "STATUS remains thesis-canonical, ≤250 lines, with root byte budget controlling above line count." | The owner wrote on the line that the byte budget, not the line count, binds; the byte budget is computed by root `scripts/read_cap_check.py`. No REGINALD script counts STATUS lines (grep `250`/line count over `scripts/boot.py`, `thresholds.py`: none). At 169 B/line (139 lines, 23,487 B) bytes bind at ~193 lines < 250, which agrees with the owner's sentence. If DAEDALUS rules owner-subordinated caps as PROSE-REMEDY, this is PROSE-REMEDY (75) LOW. | rule since `3e6a0ed98` 3/02; 75 REGINALD STATUS dates since |
| 44 | CLAUDE.md:147 | FALSE | "FHLB Advances (`REG-T-06`) | >$700B ×3 official quarterly prints; exit <=$650B ×2 | REVIEW after >$700B on 3 consecutive official quarterly advances" | A domain threshold-table row on quarterly official data with an explicit "no automatic crisis inference" clause; not a carried process remedy. | — |

**REGINALD step-1 FP rate: 1/3.** Desk verdict: **CLEAN (3)**. Run #1's H1 (`vx_ladder_check.py` "exit-code defect still owed") is not on this run's list; see §2.

### SAM (9 candidates; `scripts/` incl. `boot.py`, `closeout_check.py`, `catalyst_countdown.py`, `lib/boot_context.py`, `rate_differential.py`, `fxy_options.py`, `mof_flows.py`)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 45 | CLAUDE.md:27 | BUILT | "6. `thesis/PREDICTIONS.tsv` — read the calibration PREAMBLE + grep the OPEN rows… ✅ INSTRUMENT EXISTS — use it: `boot.py --predictions`" | The line itself names the built instrument (`scripts/lib/boot_context.py` present; corrected 9/18, DAEDALUS PR#6). Not a stale claim. | — |
| 46 | CLAUDE.md:84 | BUILT | "Note where the docket duty is actually stated: BOOT step 3 says past rows "are pruned at closeout"… `closeout_check.py` exists because that split is structural" | `scripts/closeout_check.py:62` step 10 "prune past; CALENDAR<->CATALYSTS sync — CHECKED A/B/C"; `:237` "A [step 10] CATALYSTS.tsv holds %d row(s) dated before today"; `:268` C event-count parity; `:305` C2 per-event match. | — |
| 47 | MAINTENANCE.md:182 | FALSE | "NEW — `scripts/rate_differential.py` (boot-wired). Mechanizes the SAM-41 bar… Built because the check had been carried "still un-run, next session" for eight sessions" | Unchanged since run #1 (row 60): a DONE line, H-4 positive evidence. | — |
| 48 | MAINTENANCE.md:538 | BUILT | "Remaining deferred (not workbook-hygiene): vol IV/skew proxy build in fxy_options.py (queued — CME route gated)" | Unchanged since run #1 (row 61): built `0a48b9012` + `46dfddb72` 5/28. History. | — |
| 49 | MAINTENANCE.md:552 | BUILT | "Viable free path identified: extend existing `fxy_options.py` to compute a 30d ATM-IV proxy (CVOL-equivalent) + 25d skew proxy" | Same item and commits as #48. | — |
| 50 | MAINTENANCE.md:616 | PROSE-REMEDY (23) | "Deferred (graduation rungs): boot-time staleness tripwire in catalyst_countdown.py (runway < ~10d → auto-nudge SAM to spawn KOYOMI)" | Re-checked at HEAD: no `runway`/`furthest`/`tripwire` logic in `scripts/catalyst_countdown.py`, `boot.py` or `lib/*.py`; `catalyst_countdown.py` was edited 10/29 (`77edf5fdd`, other fixes) without it. Runway is still hand-derived by KOYOMI (`docket/KOYOMI_MEMORY.md:607` "Derive counts, runway and consecutive gaps from TSV every run"; `:432` "total runway alone conceals missing December coverage"). The 5/28 "evaluate-mode until Will decides" gate still has no date or owner (run #1 asked the owner to confirm; no answer found on the surface). | KOYOMI Runs 2→24 (Run 24 = 10/20) = 23 runs |
| 51 | CLAUDE.md:77 | BUILT — form stale vs canon | "13a. Refresh `NEXUS_BRIEF.md`… Checkable form: the brief's commit timestamp ≥ this session's last STATUS commit timestamp." | `scripts/closeout_check.py:516-527` `check_brief_ordering()` computes the amendment-10 timestamp form. Amendment 11 (hash pin) is computed fleet-wide by repo-root `scripts/brief_pin_check.py` (10/08) and OTTO's charter now names it; SAM's charter and check still teach the superseded timestamp form. | — |
| 52 | CLAUDE.md:137 | PROSE-REMEDY (83) — LOW | "- STATUS.md stays under 250 lines." | `scripts/closeout_check.py:61` delegates step 9 to `read_cap_check.py` "(size only…)" — bytes, not lines; no SAM script compares STATUS line count to 250. Dominated: 165 B/line (93 lines, 15,338 B) ⇒ bytes bind at ~197 lines < 250. | since `3e6a0ed98` 3/02; 83 SAM STATUS dates since |
| 53 | CLAUDE.md:212 | FALSE | "Annual: Shunto wages ≥6.0% shock threshold (Feb-Mar cycle) → PROME 🟠. Re-activate next cycle." | Annual domain threshold, dormant until the Feb–Mar cycle. | — |

**SAM step-1 FP rate: 2/9.** Desk verdict: 2 PROSE-REMEDY (1 substantive, 1 LOW). Run #1's watch (`mof_flows.py` latest-week-only alert) is BUILT: `77edf5fdd` 10/29 "MOF every-new-week bar".

### SHADE (7 candidates; SHADE has no `scripts/` or `tools/` dir)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 54 | STATUS.md:15 | FALSE | "Live verdict + rails (§0o/§0r)… owners (§7), owed list (§10) | Boot-read whole… Budget 32,550 B; `python3 scripts/read_cap_check.py --agent SHADE` every closeout." | Unchanged since run #1 (row 66): section name "owed list"; the named script is the built root tool. | — |
| 55 | CLAUDE.md:46 | FALSE | "- **NOT RED** only if **CEILING ≤ 30%**." | A domain grading rule on a statutory-filing ratio (FLOOR/CEILING over General Account, `:41-47`), not a desk-process remedy. | — |
| 56 | CLAUDE.md:50 | FALSE | "4. TSR — UNAVAILABLE… No band or threshold until a calibration set across ≥5 insurers exists." | A methodological deferral of a domain metric; no remedy carried. | — |
| 57 | CLAUDE.md:93 | FALSE | "Fires when | BOTH legs, conjunctive (AND): (1) LEVEL — HY OAS > 280 bp, SUSTAINED ≥5 consecutive published sessions; (2) SIGN…" | Domain trigger definition. The sustain count is explicitly LIQUID's (`:98`). | — |
| 58 | CLAUDE.md:98 | FALSE | "Sustain count | A run is broken by any published session ≤280. OWNERSHIP SPLIT… SHADE does not maintain a parallel HY series or a parallel sustain count" | Ownership rule; SHADE is forbidden by design from computing this count. | — |
| 59 | CLAUDE.md:99 | FALSE | "SIGN-LEG WINDOW — prospective amendment registered 2026-10-12… Primary window: from the close of the last published HY OAS session ≤280bp" | Domain window definition (DOCKET L673). | — |
| 60 | CLAUDE.md:161 | BUILT — form stale vs canon | "11a. `NEXUS_BRIEF.md` fold — THE SESSION'S LAST WRITE-BACK… Checkable form: the brief's commit timestamp ≥ this session's last STATUS commit timestamp." | Computed fleet-wide by repo-root `scripts/brief_pin_check.py` (amendment 11, `d67d4b431` 10/08); run 10/30: "✅ SHADE OK-SAME-COMMIT brief and STATUS last committed together in cf97c133c". The schema keeps the check with the reader, not as a desk closeout step (`brief_pin_check.py` docstring, schema `:165,:175`). SHADE's charter still teaches the superseded amendment-10 timestamp form. | — |

**SHADE step-1 FP rate: 6/7.** Desk verdict: **CLEAN (7)**.

### TERRY (2 candidates; `scripts/` incl. `boot.py`, `ledger_sweep.py`)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 61 | CLAUDE.md:174 | FALSE | "`scripts/ledger_sweep.py` | Anti-drift guard — the fix for the class that hit this desk 5× on 2026-07-30… Never silence a finding by widening `COMPATIBLE`" | FILES-table description of a built guard (boot advisory, closeout blocking); the token hit is a prohibition, not an owed item. | — |
| 62 | CLAUDE.md:181 | FALSE | "`grades/` · `research/` · `archive/` | Print-grade outputs · standing research… · retired ≥60d material (`git mv` target per root Data Hygiene)." | FILES-table row citing the root retirement rule (root CLAUDE.md § Data Hygiene owns it). | — |

**TERRY step-1 FP rate: 2/2.** Desk verdict: **CLEAN (2)**. Run #1's watch leg (`ledger_sweep.py` `COMPATIBLE {CLOSED, FIRED}` blind spot) is BUILT: `scripts/ledger_sweep.py:184-187` removes the pair with the comment "CLOSED and FIRED are successive lifecycle states, not compatible current claims".

### VIOLET (10 candidates — founding desk / positive control; `scripts/` incl. `canary_staleness.py`, `twin_check.py`, `skew_integrity.py`, `writeback_order_check.py`, `thresholds.py`, `surface_agreement.py`, `backfill.py`)

Positive control re-checked at HEAD: run #0's five remedies are still present (`scripts/canary_staleness.py`, `scripts/twin_check.py`, `scripts/skew_integrity.py`, `catalyst_countdown.py` holiday table, `move.py` leg removal) — files present 10/30; not re-run this pass.

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 63 | CANARY_MAP.md:82 | BUILT (control #1, labelled history) | "this is the fourth-plus RED on this file, and a guard that cries wolf on a fixed weekly schedule is training its reader to wave the red through" | Unchanged since run #1 (row 68): `:86` "✅ FIXED 2026-09-04 PM (Will-directed) — the paragraph below was true when written and is kept as the record"; code `scripts/canary_staleness.py`. | — |
| 64 | LAST_COMPLETION.md:18 | FALSE | "GAPS: `^SKEW` back-sweep still owed and now weaker on both modes" | File FROZEN (`LAST_COMPLETION.md:3` "⛔ FROZEN 2026-09-06 — NOT MAINTAINED"); a data task, not a code remedy. Unchanged since run #1 (row 72). | — |
| 65 | LAST_COMPLETION.md:20 | FALSE | "BUILT (PM): ① COT staleness rebuilt THREE TIMES and the final one makes no calendar claim at all." | FROZEN record of the run-#0 build. Unchanged (run #1 row 73). | — |
| 66 | MAINTENANCE.md:255 | FALSE | "2. `backfill.py` — can now CREATE missing sessions. Its CBOE pass iterated `rows.items()`, so the gapcheck's own printed remedy (`--spot-only`) did nothing" | DONE "What changed" item (9/11). Unchanged (run #1 row 69, then `:199`). | — |
| 67 | MAINTENANCE.md:256 | FALSE | "3. `surface_agreement.py` — memo glob bounded to ONE delivery date… its printed remedy required editing a delivered record." | Same DONE entry (run #1 row 70). | — |
| 68 | MAINTENANCE.md:276 | FALSE | "Trigger: Taking the 9/11 settle that the 14:5x session left owed. `thresholds.py --supersede` wrote NULL for `skew`" | Trigger line of the 9/11 evening entry (heading `:274` "…`run_tests.py` built and wired as the 9th blocking contract"). DONE (run #1 row 71). | — |
| 69 | CLAUDE.md:46 | BUILT | "7. `STATUS.md` — write the dashboard back… Keep under 250 lines (archive overflow to `research/` or `archive/`)." | `scripts/thresholds.py:394` `CAPPED_DOCS = (("MAINTENANCE.md", 300), ("STATUS.md", 250))`, compared at `:403`. Unchanged (run #1 row 75). | — |
| 70 | CLAUDE.md:53 | BUILT | "12. `NEXUS_BRIEF.md`… Checkable form: the brief's commit timestamp ≥ the session's last STATUS commit timestamp." | `scripts/writeback_order_check.py` (closeout BLOCKING), plus fleet `scripts/brief_pin_check.py` (10/30: "✅ VIOLET OK-SAME-COMMIT"). Charter still teaches the amendment-10 form — note only. | — |
| 71 | CLAUDE.md:79 | BUILT | "- **Compress.** STATUS.md should stay under 250 lines." | Same as #69 (`scripts/thresholds.py:394`). | — |
| 72 | CLAUDE.md:164 | FALSE (for VIOLET) | "PROME-facing completion contract — a DATED memo ending in the COMPLETION block (… ≤10 lines, RESULT carries a number)" | Unchanged since run #1 (row 77): the memo ordering is computed (`writeback_order_check.py`); the block SHAPE (≤10 lines, number in RESULT) is PROME's fleet spec and is still computed by no script (grep `COMPLETION` over `scripts/*.py`, `PROME/tools/*.py`: only unrelated hits in `prome_gate.py`, `index_cold_shard.py`). Spec owner's item, not VIOLET's. | — |

**VIOLET step-1 FP rate: 6/10.** Desk verdict: **CLEAN (10)**.

### VULCAN (4 candidates; `scripts/` = catalyst_countdown, crwv_library, kb_catalog(+test), validate_workbook(+test); `tools/` = closeout_check, edgar_watch(+tests), gpu_panel, mag7, semi_watch, tsmc_watch)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 73 | CLAUDE.md:38 | BUILT | "Run `…/AGENTS/VULCAN/tools/closeout_check.py` FIRST… and LAST… BLOCKS on boot alarms left unactioned (a stale ledger or due prediction needs a fix, a FROZEN banner, or `DEFERRED to YYYY-MM-DD`" | `tools/closeout_check.py:313-325` "boot alarms block (VIOLET pattern)": `rec("BLOCK predictions due resolved", …"FAIL")`, per-leg freshness BLOCK rows. Line describes built code accurately. | — |
| 74 | CLAUDE.md:192 | BUILT | "Read whole startup surfaces stay under 32,550 B; run root `scripts/read_cap_check.py --agent VULCAN` and inspect its discovered perimeter." | Root `scripts/read_cap_check.py` computes the 32,550 B budget per declared read; the line names it. | — |
| 75 | CLAUDE.md:90 | FALSE | "Useful-life gate: ≥2 of 4 names change useful-life OR Microsoft shortening alone supports an S6 proposal." | Domain gate on company disclosures (judgment-read). | — |
| 76 | CLAUDE.md:121 | FALSE | "breadth, the red band's second leg | — | — | ≤ −7.5pp (base-rated: 5 distinct episodes in 23.3yr…" | Domain threshold-table cell. | — |

**VULCAN step-1 FP rate: 2/4.** Desk verdict: **CLEAN (4)**. Both run #1 VULCAN remedies are BUILT: R-V1 `tools/semi_watch.py:215-219` stamps `trade_date` from `America/New_York` ("never the UTC run date"); R-V2 `tools/edgar_watch.py:311-324` handles 52/53-week fiscal years ("MU's FY2026 ended 2026-09-03, a 53-week year"), `db3a52327` 10/15.

### WAL (4 candidates, all form 2; `scripts/` incl. `boot.py`, `maintenance_state_check.py`, `predictions_due_check.py`, `kb_expiry_check.py`, `derived_drift_check.py`; no `tools/`)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 77 | CLAUDE.md:106 | PROSE-REMEDY (16) — LOW | "- **STATUS.md ≤250 lines.** Archive prior sections rather than growing." | No WAL script compares STATUS line count (grep of `scripts/boot.py`, `maintenance_state_check.py` for `250`/line counts: only KB/nav parsing); WAL's charter names neither `read_cap_check.py` nor `measure.py`. Dominated: 173 B/line (114 lines, 19,714 B) ⇒ bytes bind at ~188 lines < 250. | "250 l" since `37ee2748e` 7/25; 16 WAL STATUS dates since |
| 78 | CLAUDE.md:148 | FALSE | "~~WAL close <$78 (threshold)~~ TERMINAL: `GATE-REG-T02` fired 9/1 ($77.26) and is RESOLVED… The live guard is `GATE-TERRY-ROLL70-EXIT` (≥$81.90 ×3), graded and routed by REGINALD" | A resolved domain gate; the live guard is REGINALD/TERRY's, and WAL's `scripts/boot.py:97` already reads its exit level from REGINALD's registry row. | — |
| 79 | CLAUDE.md:152 | FALSE | "MI3 ≥25% at any quarterly FFIEC pull (from 21.20% at Q2; one qualifying up-step crosses) | REGINALD | 🔴" | Domain threshold owned by REGINALD (`AGENTS/REGINALD/scripts/mi3_cohort_screen.py`); WAL `boot.py:114,329` prints the last MI3 quarter. | — |
| 80 | CLAUDE.md:173 | PROSE-REMEDY (16) — LOW, duplicate of #77 | "`STATUS.md` | Live dashboard (≤250 ln). Primary snapshot." | FILES-table restatement of #77. | as #77 |

**WAL step-1 FP rate: 2/4.** Desk verdict: 1 distinct PROSE-REMEDY (LOW).

### WALTER (1 candidate; `tools/` incl. `walter_doctor.py`, `signal_read_check.py`, `closeout_run.py`)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 81 | CLAUDE.md:51 | FALSE | "7. Scan BOARD/INDEX.md… Run `python3 AGENTS/WALTER/tools/signal_read_check.py SIGNAL_ID --read`… Oversized whole sources read in chunks still need a cap remedy." | Boot step naming a built tool (`tools/signal_read_check.py` present); "cap remedy" points to the fleet READ_CAP canon, not a WALTER computation carried as prose. | — |

**WALTER step-1 FP rate: 1/1.** Desk verdict: **CLEAN (1)**. Run #1's A11 ("≥3 stacked `full deferred` breadcrumbs", 65 sessions) is BUILT: `tools/walter_doctor.py:39` `full_closeout_owed`, `:1666-1684` counts `full deferred` SESSION_LOG headers since the last full closeout ("DAEDALUS Prose-Remedy #1, 10/8").

### WATT (3 candidates, all form 2; code = `boot.py`, `power_watch.py` at the desk root)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 82 | CLAUDE.md:111 | BUILT | "PJM RT LMP (real-time, $/MWh) | ≥$150 | ≥$500 | ≥$1,000 / cap | P1 → HENRY / AEOLUS" | `power_watch.py:127` `LMP_RED = 1000.0`, `:387-391` `lmp_band()` returns "RED (>=$1,000)" … "YELLOW (>=$150)"; Orange ≥$500 trips REVIEW rc 1 (`:58`). | — |
| 83 | CLAUDE.md:112 | FALSE (observation attached) | "PJM demand vs 24h peak (EIA-930) | ≥90% | ≥97% | reserve-shortage posting | P1 → HENRY" | A domain band row, not a carried remedy. Observation for the owner: the instrument does not compute these bands — `power_watch.py:107` `NEAR_PEAK_PCT = 95.0` ("within 5% of 24h peak = stress hint") is a third cutoff, matching neither the 90% Yellow nor the 97% Orange band in the charter. | — |
| 84 | CLAUDE.md:114 | DECLINED-BY-DESIGN | "BRA capacity clear vs cap | ≥50% of cap | ≥90% | at cap AND short of reliability req | P2 → CARL" | Owner's written reason in code: `power_watch.py:69-71` "Structural capacity cost: 2026/27 BRA cleared at the $329.17/MW-day cap… Annual cadence, tracked via BRA PDFs — not here." | — |

**WATT step-1 FP rate: 1/3.** Desk verdict: **CLEAN (3)**. Run #1's H2 (charter teaching 64,000 / 48,000 / 44,800 B) is corrected: `CLAUDE.md:177` now reads "Byte budget = the fleet read-cap 32,550 B"; no `64,000` remains in the charter.

### YURI (2 candidates, both form 2; `scripts/` = boot.py)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 85 | CLAUDE.md:68 | FALSE (observation attached) | "By 2026-10-24 (30 days from wiring), YURI has produced ≥3 actor calls, each citing ≥2 channels held by DIFFERENT desks… 0 such calls ⇒ the desk's premise is falsified" | A desk self-falsifier whose unit ("actor call… marginal to the channel desks") is a judgment, "Graded by DAEDALUS at the row's date" (`:70`); not a carried remedy. Observation for DAEDALUS (the grader): `workbook/INTENT_LEDGER.tsv:7` YUR-F01 resolve_by 2026-10-24, status cell still "OPEN — 0 of 3 qualifying…"; ledger header (`:1`, refresh 10/21) "YUR-F01 DAEDALUS grade 2026-10-24, 0 of 3 at 10/21". The grade date has passed; whether DAEDALUS has graded it elsewhere was not checked. | — |
| 86 | CLAUDE.md:103 | BUILT (byte legs); line leg dominated | "STATUS under 250 lines AND under 32,550 B; at ≥75% (24,412 B) rotate oldest history verbatim… until <70% (22,785 B)." | Root `scripts/read_cap_check.py --agent YURI` run 10/30: "✅ AGENTS/YURI/STATUS.md 19,153 B 59% of budget", rotate-tier flagged at ≥75%. The 250-line leg is not computed (`scripts/boot.py` has no line count) but at 277 B/line (69 lines) bytes bind at ~117 lines — residual, not counted. | — |

**YURI step-1 FP rate: 1/2.** Desk verdict: **CLEAN (2)**.

### ZHAO (5 candidates, all form 2; `scripts/` = boot.py, catalyst_countdown.py)

| # | file:line | Token | Surface fragment (≤160) | Evidence | Carry |
|---|---|---|---|---|---|
| 87 | CLAUDE.md:49 | DECLINED-BY-DESIGN (weak) | "1. `STATUS.md` — refresh the Signal Dashboard… Rewrite the spine; never prepend a fresh block over a stale body… Archive overflow to `archive/` to hold ≤250 lines." | No ZHAO code counts STATUS lines (`scripts/boot.py` line-cap logic covers NEXUS_BRIEF only, `:417`). The owner wrote, at the next line (`CLAUDE.md:50`), why the line cap is not the check: "READ-CAP IS THE BINDING CONSTRAINT, NOT THE LINE COUNT… run `…/scripts/read_cap_check.py --agent ZHAO` before committing… The ≤250-line cap is a proxy that has been wrong twice (264 lines = 47,477 B)." Bytes are computed by the root tool. At 136 B/line (179 lines, 24,293 B) bytes bind at ~239 lines < 250. If DAEDALUS rules owner-subordinated caps as PROSE-REMEDY, this is PROSE-REMEDY (22) LOW. | since `3e6a0ed98` 3/02; 22 ZHAO STATUS dates since |
| 88 | CLAUDE.md:56 | FALSE (for ZHAO) | "5. Dated delivery memo — write `PROME/inbox/{YYYY-MM-DD}_from-ZHAO_{slug}.md` ending with the COMPLETION block (… ≤10 lines)" | Same as VIOLET #72: the block shape is PROME's fleet spec; no script computes it; spec owner's item. | — |
| 89 | CLAUDE.md:254 | DECLINED-BY-DESIGN (weak), duplicate of #87 | "`STATUS.md` | Live dashboard — ≤250 lines. Signal dashboard, convergence matrix…" | FILES-table restatement of #87. | as #87 |
| 90 | CLAUDE.md:256 | BUILT | "`NEXUS_BRIEF.md` | Standing brief NEXUS consumes… (VIEW/CALIBRATION/CROSS-DOMAIN/NEXT/FORWARD CATALYSTS, ≤100ln)." | `scripts/boot.py:417` `BRIEF_MAX_LINES = 100 # CLAUDE.md CLOSEOUT 4 / FILES row: "≤100 lines" (DAEDALUS PROSE-REMEDY, 2026-10-09)`; `:20` "[7] NEXUS_BRIEF CAPS — ≤100 lines and ≤32,550 B". Brief at 87 lines today. | — |
| 91 | CLAUDE.md:267 | DECLINED-BY-DESIGN (weak), duplicate of #87 | "`archive/` | Superseded STATUS sections/versions and retired research. STATUS overflow lands here to hold the ≤250-line cap." | Restatement of #87. | as #87 |

**ZHAO step-1 FP rate: 1/5.** Desk verdict: **CLEAN (5)**. Both run #1 ZHAO remedies are BUILT: A3 ordering → `CLAUDE.md:55` "Check: `python3 scripts/brief_pin_check.py ZHAO`" (10/30 run: OK-SAME-COMMIT); A4 ≤100-line brief cap → `scripts/boot.py:417`.

## §2 Changes since run #1 (2026-10-08 N–Z record), with why

| Run #1 item | Run #1 verdict | Now | Why |
|---|---|---|---|
| NEXUS pin check (A1, `CLAUDE.md:49` then) | PROSE-REMEDY (3) | BUILT, off this run's list | Repo-root `scripts/brief_pin_check.py` (`d67d4b431` 10/08); NEXUS step 6 (`CLAUDE.md:33`) now names it. |
| NEXUS whole-file measure (H3, `:105` then) | BUILT + stale "hand `wc -c`" | BUILT, residue gone (#2) | `CLAUDE.md:63` now says "(the 0a instrument)". |
| ORACLE `MAINTENANCE.md:202` history dedupe | recall miss, unclassified | DIAGNOSIS-ONLY (#9) | Now on the list (v2 step 1); owner rejects the one-line fix, right fix unspecified. |
| ORACLE `:230` resolved-as-NOT-FOUND | not on run #1 list | PROSE-REMEDY (10) (#12) | Newly surfaced by v2 step 1; carried live as a STATUS caveat (`STATUS.md:126`). |
| OSPREY 250-line cap (A7) | PROSE-REMEDY (22) LOW | PROSE-REMEDY (31) LOW (#17), narrowed | Closeout step 9 now names `PROME/tools/measure.py` (lines + bytes), which measures but compares nothing. |
| OSPREY OWED-45 | DIAGNOSIS-ONLY | not on this run's list | `STATUS.md:40` line no longer matched; not re-checked. |
| OTTO brief ordering (A2) | PROSE-REMEDY (7) | BUILT (#24 records it) | `CLAUDE.md:192` step 7a now: "`python3 scripts/brief_pin_check.py OTTO` prints OK" (10/14). |
| PROME WQ-206 aged-ACTION (A12) | PROSE-REMEDY (26), registered L639 | PROSE-REMEDY (47), approved build L730 (#34) | L639 design delivered 10/08 and RESOLVED 10/24; Will approved the build 10/15 (WQ-401); L730 PENDING "next-PROME-process-pass"; still no code. |
| RED 200-line cap (A6) | PROSE-REMEDY (41) LOW | BUILT (#35, #40) | `scripts/closeout_check.py:485-487` GATE "STATUS <= 200 lines" (`dbf10d5bb` 10/15). |
| RED ML-226 METRIC_MAP vs `instrument_basis` (A5) | PROSE-REMEDY (9) | **still unbuilt; dropped from this run's list** | Line moved `:740` → `:880` ("Nothing compares `boot.py`'s METRIC_MAP source against each row's `instrument_basis`"); v2 step 1 did not emit it (recall miss — see §3). No RED script compares the two (`instrument_basis` in `boot.py` only as a comment, `:87`). Not counted in §0; carry would be S42→S57 by RED's own numbering. |
| REGINALD `vx_ladder_check.py` "still owed" (H1) | BUILT, stale claim | stale text gone | grep for "exit-code defect" in `AGENTS/REGINALD/STATUS.md` and `MEMORY.md`: zero hits. |
| SAM `mof_flows.py` latest-week alert (watch) | under the bar | BUILT | `77edf5fdd` 10/29 "MOF every-new-week bar". |
| SAM KOYOMI runway tripwire (A8) | PROSE-REMEDY (22) | PROSE-REMEDY (23) (#50) | Unchanged code; one more KOYOMI run (Run 24, 10/20); the "until Will decides" gate still undated. |
| TERRY `ledger_sweep.py` `{CLOSED, FIRED}` (watch) | 0 sessions, watch | BUILT | `scripts/ledger_sweep.py:184-187` removes the pair. |
| TERRY L372 class-fix | DIAGNOSIS-ONLY | not on this run's list | Not re-checked. |
| VULCAN `semi_watch.py` UTC date (A9) | PROSE-REMEDY (3) | BUILT | `tools/semi_watch.py:215-219` stamps America/New_York. |
| VULCAN `edgar_watch.py` MU 53-week year (A10) | PROSE-REMEDY (7) | BUILT | `tools/edgar_watch.py:311-324` 52/53-week logic (`db3a52327` 10/15). |
| WALTER "≥3 stacked full-deferred" (A11) | PROSE-REMEDY (65) | BUILT | `tools/walter_doctor.py:1666-1684` `full_closeout_owed`. |
| WATT 64,000 B charter figure (H2) | BUILT, stale | corrected | `CLAUDE.md:177` now teaches 32,550 B. |
| ZHAO brief ordering (A3) | PROSE-REMEDY (5) | BUILT | `CLAUDE.md:55` "Check: `python3 scripts/brief_pin_check.py ZHAO`". |
| ZHAO ≤100-line brief cap (A4) | PROSE-REMEDY (5) | BUILT (#90) | `scripts/boot.py:417` `BRIEF_MAX_LINES = 100` ("DAEDALUS PROSE-REMEDY, 2026-10-09"). |
| SENTRY perimeter leak | NOT READ (DORMANT) | absent from this run's list | v2 step 1 perimeter no longer emits SENTRY. |

Unchanged verdicts on lines re-read (line numbers may have moved): ORACLE #7, #10, #14; OZK #29; RED #36, #37, #38; SAM #47, #48, #49, #51; SHADE #54; VIOLET #63–#72. Each was re-opened at the cited line and the code situation re-checked at HEAD before reuse.

**Run #1 → run #2, N–Z:** of run #1's 12 distinct N–Z PROSE-REMEDY items, **8 are now BUILT** (NEXUS A1, OTTO A2, ZHAO A3, ZHAO A4, RED A6, VULCAN A9, VULCAN A10, WALTER A11); **4 are still open** (OSPREY A7 LOW, PROME A12, SAM A8, RED A5 off-list). Both run #1 watch items are BUILT; both H-1 stale claims (H1, H2) and H3 are corrected.

## §3 Limits and the step-3 sentence

1. **Step-3 sentence: 0 rows typed by this run (classification only); premise-verified at the source for 0 of 0.** Of the 8 run #1 N–Z remedies now BUILT, this classifier confirmed each exists at HEAD by reading the code line; it did not re-run their selftests, so premise verification of those builds is not claimed here.
2. **Session counts are proxies:** distinct dates of commits to the desk's STATUS (or PROME/STATUS.md) since the rule's first commit (`git log -S` on the phrase), filtered to subjects starting with the desk name where stated; KOYOMI runs for SAM #50. A charter rewrite can re-date a phrase (`-S` finds the earliest commit introducing the exact string), so carry ages for rules re-worded in the 10/15–10/24 charter splits (RED, NEXUS) were taken from the older phrasing where found.
3. **Form-2 policy applied (same as run #1):** a standing line cap with no computing code is PROSE-REMEDY, marked LOW where the 32,550 B byte budget binds first at the desk's measured density. **New this run:** where the owner wrote on the surface that the byte budget, not the line count, is binding (REGINALD #43, ZHAO #87/#89/#91), I used DECLINED-BY-DESIGN (weak) and gave the PROSE-REMEDY carry in case DAEDALUS rules otherwise. ORACLE #15 is NOT LOW: at 118 B/line the line cap binds before bytes.
4. **Domain thresholds** (OSPREY #18–#23, SHADE #55–#59, WAL #78–#79, WATT #83, VULCAN #75–#76, REGINALD #44) are classified FALSE: they grade external data, not a carried process remedy. They account for most of this run's FALSE rows (42/91 = 46%, vs run #1 N–Z 28/59 = 47%).
5. **Step-1 recall misses seen while reading (not counted):** RED `MAINTENANCE.md:880` ML-226 (run #1 A5, still unbuilt) is not on the v2 list although it carries "Nothing compares" + `boot.py` — DAEDALUS should check why `prose_remedy_candidates.py` dropped it (a R1–R6 exclusion such as a heading-scoped DONE rule is the likely cause; not verified). OSPREY channel-kill pause clocks (`CLAUDE.md:149,166`) are a mechanical days-since count with no code and no token.
6. **Observations routed by this record, not counted:** repo-root `scripts/ledger_staleness.py` still prints no row for ORACLE `workbook/HISTORY.tsv` (10/30: "7 ledger(s) scanned", six rows) — a `scripts/` owner item (DAEDALUS-granted); WATT `power_watch.py:107` near-peak 95% matches neither charter band (90/97); YURI YUR-F01 grade date 10/24 passed with the ledger still OPEN — DAEDALUS's own grading duty; SAM, SHADE and VIOLET charters still teach the amendment-10 timestamp form though the amendment-11 pin check passes for all three.
7. Whole-file reads of each desk's surfaces were not done; each row was read at its cited line with surrounding context only.

