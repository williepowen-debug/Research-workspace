# Prose-Remedy Census #1 — step 2 classification, desks N–Z

**Classifier:** non-owner (DAEDALUS-spawned), read-only on the repo except this record. **Started:** 2026-10-08 16:16 EDT (`date`). **Input:** `runs/2026-10-08_PROSE_REMEDY_CENSUS_01_CANDIDATES.tsv` (HEAD 46fa6ef4a), rows for NEXUS · ORACLE · OSPREY · OTTO · OZK · PROME · RED · REGINALD · SAM · SENTRY · SHADE · TERRY · VIOLET · VULCAN · WALTER · WATT · ZHAO (59 rows, TSV lines 30–88). **Playbook:** `sweeps/PROSE_REMEDY_SWEEP.md` §2.

## §0 Summary (59 candidate rows, 17 desks)

| Desk | Candidates | PROSE-REMEDY rows (distinct) | BUILT | DIAGNOSIS-ONLY | DECLINED | FALSE | Under-bar watch | Step-1 FP rate | Desk verdict |
|---|---|---|---|---|---|---|---|---|---|
| NEXUS | 3 | 1 (1) | 1 | 0 | 0 | 1 | 0 | 1/3 | 1 PROSE-REMEDY |
| ORACLE | 5 | 0 | 1 | 0 | 1 | 3 | 0 | 3/5 | **CLEAN (5)** |
| OSPREY | 2 | 1 (1, LOW) | 0 | 1 | 0 | 0 | 0 | 0/2 | 1 PROSE-REMEDY (low) |
| OTTO | 4 | 1 (1) | 0 | 0 | 0 | 3 | 0 | 3/4 | 1 PROSE-REMEDY |
| OZK | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0/1 | **CLEAN (1)** |
| PROME | 5 | 1 (1) | 0 | 0 | 0 | 4 | 0 | 4/5 | 1 PROSE-REMEDY (already on DOCKET L639) |
| RED | 8 | 2 (2; 1 LOW) | 2 | 0 | 0 | 4 | 0 | 4/8 | 2 PROSE-REMEDY |
| REGINALD | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0/1 | **CLEAN (1)** — 1 stale "owed" to strike |
| SAM | 6 | 1 (1) | 3 | 0 | 0 | 1 | 1 | 1/6 | 1 PROSE-REMEDY (+1 watch) |
| SENTRY | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1/1 | **NOT READ (DORMANT — out of perimeter)**; the 1 row read = FALSE |
| SHADE | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1/1 | **CLEAN (1)** |
| TERRY | 1 | 0 | 0 | 1 | 0 | 0 | (1 leg) | 0/1 | 0 PROSE-REMEDY (1 DIAGNOSIS-ONLY + a 0-session watch leg) |
| VIOLET | 10 | 0 | 3 | 0 | 0 | 7 | 0 | 7/10 | **CLEAN (10)** — positive control 5/5 BUILT |
| VULCAN | 4 | 4 (2) | 0 | 0 | 0 | 0 | 0 | 0/4 | 2 PROSE-REMEDY |
| WALTER | 3 | 1 (1) | 0 | 0 | 0 | 2 | 0 | 2/3 | 1 PROSE-REMEDY |
| WATT | 2 | 0 | 1 | 0 | 0 | 1 | 0 | 1/2 | **CLEAN (2)** — 1 stale charter figure to correct |
| ZHAO | 2 | 2 (2) | 0 | 0 | 0 | 0 | 0 | 0/2 | 2 PROSE-REMEDY |
| **Total** | **59** | **14 rows = 12 distinct remedies** (2 LOW) | **13** | **2** | **1** | **28** | **1** | **28/59 = 47%** | 10 desks with ≥1 PROSE-REMEDY · 6 CLEAN · 1 NOT READ |

Row arithmetic: 14 + 13 + 2 + 1 + 28 + 1 = 59 ✓ (TERRY's watch leg sits inside its DIAGNOSIS-ONLY row). **Step-3 sentence: 0 rows typed by this run (classification only); premise-verified at the source for 0 of 0. Founding control (VIOLET run #0): 5 rows typed; premise-verified at the source for 4 of 5 at first ship, 5 of 5 after `c685cc318` (9/6).**


## §1 Per desk, per row

### NEXUS (3 candidates, all form 2 — `AGENTS/NEXUS/CLAUDE.md`; NEXUS has no `scripts/`/`tools/` dir, zero `.py` outside archive)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 30 | `CLAUDE.md:49` "plus a 10-line cross-brief section (same instrument cited by ≥2 desks; explicit disagreements). Readers also run the pin check (`git log` brief vs STATUS HEAD)." | **PROSE-REMEDY (3)** — on the pin-check leg only | The matched `≥2 desks` leg is a judgment read (not counted). The **pin check** is a fully specified mechanical comparison (brief's STATUS pin vs `git log` STATUS HEAD; failure = pin ≠ HEAD ⇒ STALE; schema amendment 11, `templates/NEXUS_BRIEF_SCHEMA.md:164`, "an invariant checked at commit") and is run by LLM digest readers, not code: no `.py` in the repo computes it fleet-wide (amendment-11 code exists only per-desk for the desk's own brief: `VIOLET/scripts/writeback_order_check.py`, `WALTER/tools/walter_doctor.py`, `TERRY/scripts/boot.py`). Carried across 3 NEXUS digest passes by its own log: 9/29 (`83e6fe366`, adoption), 10/1 (`f61df31de`), 10/8 (`eac4e605a`; `brief_fallback_log.tsv` 2026-10-08 row "Pins: 10 FRESH, 4 STALE" — a reader-computed count). |
| 31 | `CLAUDE.md:105` "the current-session block is ≤ 6 KB (mechanism), and the WHOLE FILE is measured at every session-end commit (`wc -c`; the test) — ≥75% of budget (the BOOT 0a trigger) ⇒ rotate" | **BUILT** | The test half is computed by root `scripts/read_cap_check.py --agent NEXUS` (BOOT 0a, `CLAUDE.md:33`): run 16:2x 10/8 prints `✅ AGENTS/NEXUS/LAST_COMPLETION.md 6,116 B 19% of budget (whole · NEXUS:15a)` and flags rotate-tier at ≥75% (rule-5 band built `cc9357f89` 8/28, rotate-tier text `c7d0b6739` 9/14). The 6 KB block cap is declared "mechanism", not a test — the owner's own split, not a carried remedy. Stale-claim residue: the line says the closeout test is a hand `wc -c`; the boot tool already computes it. |
| 32 | `CLAUDE.md:270` "amendment 9 [Will-approved 2026-07-31] blesses the COMPACT variant for utility/single-seam agents; revert at ≥3 persistent edges or a thesis version" | **FALSE** | FILES-table description of the schema; the matched `≥3` is the amendment-9 revert condition ("persistent edges" is a judgment term), not a boot/closeout comparison and not a carried remedy. |

**NEXUS step-1 false-positive rate: 1/3.** Desk verdict: 1 PROSE-REMEDY.

### ORACLE (5 candidates; code in `scripts/` {kalshi, polymarket, test_search_coverage} + `tools/` {disruption_supply_spread, metrics, t6_pin, trade_marks})

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 33 | `SCRATCH.md:21` "0. ✅ **DONE 9/28: DOCKET L299** (see WHAT I DID 3). **Owed next:** re-read the Oct $110 leg on 3 separate days before any mark (thin)…Superseded text follows" | **FALSE** | DONE line; the pin+REGIME-bump remedy it carries as "superseded text" was executed 9/28 (`279b7aec1`: `REGIME = "v5-oct26-icewti110"`, `tools/disruption_supply_spread.py:125`, MONTH-ROLL RULE at :127). "Owed next" is a market-observation discipline, not a code remedy. |
| 34 | `MAINTENANCE.md:79` "**CLAUDE.md (closes PROME/DAEDALUS PAT-041, inbox 7/10):** the tool's run-cadence + WTI-month-roll owed-action were homed only in SCRATCH…" | **FALSE** | Dated 2026-07-17 history entry recording a completed doc move (the "Derived series" subsection). Mention of `owed`, not a carried remedy. |
| 35 | `MAINTENANCE.md:80` "**Owed manual action:** …re-pin the new month's WTI $100 market in `watchlist.tsv` or the supply leg silently ages out — the script hard-exits on >3d leg drift, so the failure is loud, but the re-pin is manual." | **FALSE** | Accurate history: the detection remedy is code (`disruption_supply_spread.py:240` hard-exit "Re-pin the current-month… or pass --allow-stale", built `3c01cbcb9` 7/17); the residual (choosing the next contract) is a selection, not a computation. Not a stale claim. |
| 36 | `MAINTENANCE.md:204` "🔧 CONFIRMED, NOT FIXED — `t6_pin.py` prints no leg summary after `WIN_END`… T6 is spent, so fixing it would be maintenance on a dead instrument." | **DECLINED-BY-DESIGN** | Owner wrote the reason (dead instrument) in the 9/4 entry; design note handed to "any successor tool"/DAEDALUS registration family. `t6_pin.py` last touched `82c3af234` 8/27. Accept, never re-flag. |
| 37 | `CLAUDE.md:54` "thin (<$5K liq) = ≥3-day re-check, never mark on one print; `[STALE]`-mark **>** carry-forward-as-current." | **BUILT** (form-2 comparison computed) | `<$5K` is computed: `scripts/polymarket.py:13-15` THIN-LIQUIDITY GUARDRAIL `thin=True` (`2a5fb620d` 6/19), `scripts/kalshi.py:42,129` `THIN_VOLUME`/`thin`, `tools/disruption_supply_spread.py:123,246-247` prints "do not mark on one print (≥3-day re-check)" (`3c01cbcb9` 7/17). Residual, noted not counted: the **≥3 distinct days** count before a mark is printed advice, not counted by any tool. |

**ORACLE step-1 false-positive rate: 3/5.** Desk verdict: **CLEAN (5 read)** — 0 PROSE-REMEDY.
*Off-list observation (recall miss, not classified here):* `MAINTENANCE.md:203` (9/4) "NEW TOOL GAP #2 — no guard can see a LADDER RE-BANDING… The honest fix (record each event's band structure at pull and diff it) is a build and is **not** attempted mid-event" — specified remedy, no `band` logic in `polymarket.py`/`kalshi.py` at HEAD; and `:202` dedupe-by-date "Reported, not patched". Neither carries a step-1 token (`not attempted`, `not patched`); see §3.

### OSPREY (2 candidates; code = `scripts/strike_feed.py` only)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 38 | `STATUS.md:40` "**Feed / sweep (9/29):** `strike_feed.py` 23 rows, 21 NONE all dispositioned in the feed file (gitignored, OWED-45); militarnyi RSS EMPTY_FEED (3rd run)" | **DIAGNOSIS-ONLY** | Names the defect by pointer (dispositions live in the git-ignored `FEED_CANDIDATES_*.tsv`, `.gitignore:1`) with no remedy on the line. OWED-45's own surfaces state it open, not specified as code: `domain/energy-strikes/L309_STRIKE_FEED_EVALUATION_2026-10-08.md:49` "`FEED_CANDIDATES_*.tsv` stays ignored, so dispositions still do not travel (OWED-45 stays open)" (`46d6f6dea` 10/8). The fix is a `.gitignore`/retention decision, not a computation. The OWED-34 leg of the same line was CLOSED 10/8 (L309 row (c)). |
| 39 | `CLAUDE.md:48` "**`STATUS.md`** — write the three-channel dashboard back… Keep under 250 lines (archive overflow to `domain/energy-strikes/` dated analysis files or `research/`)." | **PROSE-REMEDY (22)** — LOW | No script computes the 250-line comparison: `strike_feed.py` is the only desk code; root `scripts/read_cap_check.py` measures BYTES and is not named anywhere in OSPREY's `CLAUDE.md`; DAEDALUS `maturity_scan.py:280` flags `>260` lines fleet-wide (a different threshold, DAEDALUS's instrument, biweekly). Rule written `3fb46ebdf` 7/12; 22 distinct OSPREY STATUS commit dates since (session proxy). **Never breached** (100 lines today) and **dominated**: at today's 234 B/line the 32,550 B budget binds at ~138 lines — so the real gap is that OSPREY's closeout names no size check at all. |

**OSPREY step-1 false-positive rate: 0/2.** Desk verdict: 1 PROSE-REMEDY (low).

### OTTO (4 candidates; `scripts/` = abs_issuance_tracker, backfill_collection_period, boot, catalyst_countdown, extension_proxy, panel_10d, predictions_due, severity_divergence, shelf_halt_monitor)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 40 | `STATUS.md:51` "Instrument: `workbook/SHELF_ACTIVITY.tsv` — the OTTO-07 shelf-halt probe. FROZEN 2026-09-02 (single run 7/25); re-run `scripts/shelf_halt_monitor.py` when OTTO-07 needs a fresh reading." | **FALSE** | Token hit on "needs a"; the line declares a FROZEN ledger and names the built re-run script. Not a remedy. |
| 41 | `MAINTENANCE.md:132` "**Trigger:** Boot on 2026-07-25 after a 21-day dark period reported **one** recently-fired catalyst. Running `catalyst_countdown.py` directly showed **four**." | **FALSE** | Trigger line of the 2026-07-25 (session 016) entry whose "What changed" (lines 134-135) records both fixes built: `boot.py` section-sticky RECENTLY FIRED + `catalyst_countdown.py` adaptive `past_retention_days()`. DONE history. |
| 42 | `MAINTENANCE.md:303` "**Silent-pass bugs hide in path-rename edits.** `predictions_due.py` returned "ran cleanly, no alerts" when the TSV file didn't exist" | **FALSE** | A lesson inside the 2026-06-09 entry. The guard it implies is present: `scripts/predictions_due.py:29,58` prints "ERROR: … not found." and returns 1 (`c82458f99`, 6/08). History, not a carried remedy. |
| 43 | `CLAUDE.md:188` "7a. … the brief fold is the session's LAST write-back… **Checkable form: the brief's commit timestamp ≥ this session's last STATUS commit timestamp.**" | **PROSE-REMEDY (7)** | Fully specified comparison (brief commit time vs last STATUS commit time; fail = brief older). No OTTO script reads `NEXUS_BRIEF` (grep of `scripts/*.py`: zero hits); no repo-root script computes it. Encoded `fd45fca77` 8/27 (s020); carried by hand through s020 8/27 · s021 9/02 · s022 9/12 · s023 9/24 · s024 9/28 · 9/30 · 10/4 = **7 sessions** (each closeout commit subject cites "folded LAST"). ⚠️ **Also stale against canon:** schema amendment 11 (`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md:164`, ratified 8/07) "supersedes amendment 10's *timestamp* check… with a *hash equality*" — the typed form should be the hash pin, which VIOLET already has (`scripts/writeback_order_check.py`). |

**OTTO step-1 false-positive rate: 3/4.** Desk verdict: 1 PROSE-REMEDY.

### OZK (1 candidate; `scripts/` = boot.py, flng_watch.py)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 44 | `MAINTENANCE.md:34` "**Still-open parity gaps (queued — see MEMORY NEXT SESSION):** no `scripts/boot.py` boot kit; no `thesis/PREDICTIONS.tsv` + calibration scoreboard…" | **BUILT** | The only code leg is built: `scripts/boot.py` added `68d99587f` 2026-07-04 ("add scripts/boot.py v0.1 boot kit… wire into boot step 5") — same day as this 7/04 entry. A predictions ledger exists at `workbook/PREDICTIONS.tsv` (`07d6e6d8c` 4/24; the line's `thesis/` path was wrong when written). Remaining legs (matrix conformance, NEXUS_BRIEF vs REGINALD_CHANNEL) are design decisions, not computations. Stale claim in a dated history entry — H-1 stamp-over-body instance, low stakes (the entry is history). |

**OZK step-1 false-positive rate: 0/1.** Desk verdict: **CLEAN (1 read)**.

### PROME (5 candidates; home `PROME/`, code in `PROME/tools/`)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 45 | `STATUS.md:17` "installed under the rule-5 stop (`measure.py`)… Owed: NEXUS contest (L36) · RED FT-02 manual grade · Deck REFERENCE republish (WQ-382) · RECENTLY DONE roll-off." | **FALSE** | Token `Owed` lists coordination items (a contest, a manual grade, a republish, a roll-off), each on its own DOCKET/WQ row; `measure.py` is named as the built tool that ran. No code remedy. |
| 46 | `STATUS.md:22` "`~/Research-Intake/scripts/newsweep_config.py`… R3 sets 8–9 LANDED 2026-09-28 14:5x ET… sets 1–7 owed 10/02" | **FALSE** | `owed` = watch-lists owed by desks for a WALTER test (data deliveries), tracked at DOCKET L452. Not a computation. |
| 47 | `STATUS.md:23` "Publication — LATEST at this stamp: the `prome-e4` closeout's publication (Deck · Helm · Fleet-Ops) is recorded in its PUBLISH row… (Deck Owed v74 · Helm v52…)" | **FALSE** | Every token hit is the artifact name "Deck **Owed**" (5×); scripts named are the built publishers (`decision_deck.py`, `will_handbook.py`, `fleet_dashboard.py`). Grep noise. |
| 48 | `SCRATCH.md:23` "**THU 10/8:** Fifth Plenum… · ARGUS AUDIT-PERIMETER ROW FOR `USER.md` — OWED since 2026-09-30… (L591)" | **FALSE** | A rendered DOCKET roll-up; each OWED item is a registered dated row with owner (e.g. `PROME/DOCKET.tsv` L591, due 2026-10-09, "Adding the row is a PROCESS change… one per session under WQ-299 R1"). A queue, and the L591 item is a manifest row (data), not code. |
| 49 | `CLAUDE.md:51` "**Aged ACTION (WQ-206):** unconsumed `action:` older than seven days at a DARK owner… **Aged waits (WQ-221):** …blocking desk is dark ≥7 days → the same L0 drain-only authority" | **PROSE-REMEDY (26)** — on the WQ-206 leg; WQ-221 leg **BUILT** | **WQ-221 BUILT:** `PROME/tools/prome_gate.py:948-986` `aged_waits()`/`check_aged_waits()` "⛔-waits rows whose blocker is dark ≥7d", boot-wired `:1611` (`dd9a5d5d3` 9/11). **WQ-206 not computed as a predicate:** all three inputs exist — handoff age + ACTION/INFO role in `AGENTS/WALTER/tools/walter_doctor.py:1047-1066` (threshold `N_UNCONSUMED_DAYS = 2`, not 7), inbox age ≥7d in `PROME/tools/spawn_slate.py:240-241`, `days_dark` in `prome_gate.py` — but the join (ACTION ∧ ≥7d ∧ owner dark) is done by hand, and the tool says so: `spawn_slate.py:67` "The aged-ACTION (WQ-206) and aged-waits (WQ-221) lanes are not computed here", `:241` "WQ-206 lane if any is an `action:` handoff — not classified here". Rule ruled 9/10 (`PROME/proposals/2026-09-10_wq206-aged-action-rule-RULED.md`, which names no instrument); 26 distinct `PROME/STATUS.md` commit dates 9/10→10/8 (session proxy). |

**PROME step-1 false-positive rate: 4/5.** Desk verdict: 1 PROSE-REMEDY.
**Corroborated by PROME's own record (found later in this pass, WALTER row 82):** `PROME/DOCKET.tsv` L304 graded YES 2026-10-08 14:54 ET — two demonstrated misses the WQ-206 line would have caught — and L639 (due 10/13, NEXUS designs; build is Will's word) already registers "the missing WQ-206 boot instrument". The remedy is queued; the packet should cite L639, not open a second track.

### RED (8 candidates; `scripts/` = base_rate_review, board_log_append, boot, gen_trigger_scan, review_debt, schema_check, test_board_gap, test_tie_atoms)

Session clock: RED numbers its sessions; after S41 (9/06) the commit subjects carry S42 → S50f (S42 9/09 · S43 9/10 · S44 9/12 · S45 9/14 · S46 9/18 · S47 · S48 · S49 10/1 · S50 10/1).

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 50 | `STATUS.md:6` "**Addendum S50b 2026-10-01…** EGBN Q3 re-dated to ~10/21 AMC (est.). **boot.py DUE-scan widened** so none of this can hide again → ML-RED-273." | **FALSE** | DONE line: `953ef4dda` 10/1 "RED S50b: sweep A-block cleared + boot.py DUE-scan widened (ML-RED-273)". |
| 51 | `MAINTENANCE.md:72` "🔴 **SCAN view breached WALTER's read cap AT 101.1% — RED's own doing, same session.**… **Remedy = restore the documented split, not rotate and not trim**" | **FALSE** | S44 (9/12) table row recording the remedy EXECUTED in the same row: "View **32,918 → 30,345 B (93.2%)**; `read_cap_check.py --agent WALTER` ✅ READ-CAP 0". Residue "still rotate-tier" is a size state the root tool computes. |
| 52 | `MAINTENANCE.md:108` "§⑤ itself is the **specified-not-built** check flagged at S41 — it is not set-difference based and **will read green while a backlog exists**" | **BUILT** | S42 (9/09) history line; rebuilt S44 9/12 (`126f78227`): `MAINTENANCE.md:63` "`boot.py` section ⑤ REBUILT as an ID-DIFF… set difference, no date floor, over all three ledgers" + `scripts/test_board_gap.py` (14 tests, exit 1 on failure). Stale only as history; no live surface repeats it. |
| 53 | `MAINTENANCE.md:129` "**`scripts/boot.py` still evaluates FT-10 from the mirror.**… **Fix owed in the 9/4–9/11 window: point boot.py's FT-10 evaluation at the CBOE CSV, or label its output PROVISIONAL.**" | **BUILT** | S40 (9/02) line; fixed S41 9/06 (`e90076474` "RED S41b… boot.py was the false-fire source"): `MAINTENANCE.md:726` "`boot.py` METRIC_MAP `SKEW-CBOE` re-pointed `yf ^SKEW` → new `cboe` source type; added `cboe_skew()`… fails LOUD and never substitutes the mirror". Carried 1 session (S40→S41), inside its own window. |
| 54 | `MAINTENANCE.md:214` "**`workbook/PREDICTIONS.tsv` — RED-22 added, and its `Timeframe` cell had to be fixed TWICE.**…`parse_fuzzy_date` anchors `^…$`" | **FALSE** | S34 (8/27) DONE record ("`Timeframe` is now the bare date… DUE-scan returns 🟢 again"). The detector already exists: the DUE-scan prints MANUAL CHECK on an unparseable cell. |
| 55 | `MAINTENANCE.md:235` "**③ Fleet proposal routed — OUTBOX -021.** `review_debt.py` offered to PROME/DAEDALUS as a fleet candidate… **Coverage (rows dated / rows total) must ship beside the debt count before any fleet adoption**" | **FALSE** (for RED) | A precondition RED attached to an outbound fleet proposal (S33c 8/20), not a remedy on RED's own instrument (RED populates `Stale_By`; coverage is a fleet-ranking concern). No fleet adoption has happened (`scripts/` has no review_debt; not in DAEDALUS `CHECKS.tsv`). If the proposal is live, its owner is the recipient (PROME/DAEDALUS), not RED. |
| 56 | `MAINTENANCE.md:740` "2. **Nothing compares `boot.py`'s METRIC_MAP source against each row's `instrument_basis` (ML-226).**…**none asks "does the tool read what the card says?"**" | **PROSE-REMEDY (9)** | Under S41's heading (9/06) "**⚠️ SPECIFIED, DELIBERATELY NOT BUILT — both would have been unreviewed code at closeout**" (`:737`) — a timing reason, not a design decline. Spec: per registry row, compare `boot.py` `METRIC_MAP[metric]` source (`scripts/boot.py:69`) to the row's `instrument_basis`/`instrument_basis_operative`; fail = tool reads a source the card disqualifies (2 of 12 rows at the time; ML-RED-226 "A DISCLOSED DEFECT IS NOT A FIXED ONE - MEASURED AT 25 DAYS"). Sibling #1 was built at S44; #2 was not: no RED script reads `instrument_basis` against `METRIC_MAP` (`gen_trigger_scan.py` copies the cell; `base_rate_review.py:215` reads it only for an arm date). Carried S42→S50 = **9 sessions**, and it never reached the S50 TODO sweep (`reports/2026-10-01_S50_todo_sweep.md`: zero hits for ML-226/METRIC_MAP). |
| 57 | `CLAUDE.md:82` "W1. **`STATUS.md`** — challenges, hypothesis weights… falsification-trigger statuses. ≤200 lines; archive overflow to `reports/`." | **PROSE-REMEDY (41)** — LOW | No RED script counts STATUS lines (`boot.py` has none); `read_cap_check.py` is not named in RED's charter (RED runs it by practice: `MAINTENANCE.md:67` S44 "✅ `read_cap_check.py --agent RED` back to READ-CAP 0"). Rule present since `f0f13fb39` 3/14; 41 distinct STATUS commit dates since. **Never breached** (129 lines) and **dominated**: at 178 B/line the 32,550 B budget binds at ~181 lines < 200. |

**RED step-1 false-positive rate: 4/8.** Desk verdict: 2 PROSE-REMEDY (1 substantive, 1 low).

### REGINALD (1 candidate)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 58 | `STATUS.md:49` "the ladder is exhausted (no band beyond RED). Detector: `scripts/vx_ladder_check.py` (exit-code defect still owed). Matrix score unchanged" | **BUILT** — stale claim (H-1) | The defect (`MEMORY.md:43`: "import failure exits 1 = reads as a breach") was fixed `b6544d45d` 2026-09-24 00:15 ET "REGINALD: ladder detector exits 2, not 1, when yfinance is missing" (`try: import yfinance … except ImportError: … sys.exit(2)`). **Watched 10/8:** `/usr/bin/python3` (no yfinance) → `rc=2`. The "still owed" text was re-written AFTER the fix at the 9/29 (`a5bdcd09f`) and 10/7 (`5453ee5ad`) closeouts — 2 sessions of stamp-over-body. Same stale clause on `MEMORY.md:43`; that line's second leg ("census other frozen-baseline bands in VX.tsv into the script (M2)") is a real open item, not on the candidate line. |

**REGINALD step-1 false-positive rate: 0/1.** Desk verdict: **CLEAN (1 read)** — 1 BUILT-stale for the owner to strike.

### SAM (6 candidates; 27 entries in `scripts/` incl. `lib/`, `tests/`)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 59 | `STATUS.md:35` "The 9/13–19 week was late and posted together with 9/20–26. `mof_flows.py` alerts on the LATEST week only, so **the trip was invisible to the alert** (defect #3, fix owed)." | **PROSE-REMEDY (1) — under the ≥2-session bar; NOT counted in §0** | Remedy implied and specified by `MEMORY.md:46` ("evaluates its one-week bar on the LATEST week only. A late week landing with the next one is never alerted") — i.e. evaluate every week posted since the last read. Code unchanged: `scripts/mof_flows.py:295,351` keys the weekly alert on `latest = rows[-1]`; last commit to the script `3fed218d5` 8/27. Found at the 10/1 L0 wake (`95d11fed8`, first appearance of "defect #3"); SAM has had no session since (later SAM-path commits are WALTER/DAEDALUS/BOND packets). **Re-check at run #2: if a SAM session passes without the fix, it qualifies.** |
| 60 | `MAINTENANCE.md:182` "**NEW — `scripts/rate_differential.py`** (boot-wired). Mechanizes the SAM-41 bar… Built because the check had been carried *"still un-run, next session"* for **eight** sessions" | **FALSE** | DONE line — this IS a prose remedy that was typed (2026-09-08 entry). Positive evidence for H-4, not a candidate. |
| 61 | `MAINTENANCE.md:538` "**Remaining deferred (not workbook-hygiene):** vol IV/skew proxy build in fxy_options.py (queued — CME route gated); insurers/<name>.md retire-vs-refresh" | **BUILT** | 2026-05-28 session #3/#4 text; built two sessions later the same day: `0a48b9012` 5/28 "build FXY-derived vol proxy (ATM IV + 25d RR) into fxy_options.py" + `46dfddb72` calibration; recorded `MAINTENANCE.md:500` "(closes the CVOL/RR gap)". Stale only as history. |
| 62 | `MAINTENANCE.md:552` "**Viable free path identified:** extend existing `fxy_options.py` to compute a 30d ATM-IV proxy… **Build decision pending Will** — not yet built." | **BUILT** | Same item, same commits (`0a48b9012`, `46dfddb72`, 5/28). |
| 63 | `MAINTENANCE.md:616` "**Deferred (graduation rungs):** boot-time staleness *tripwire* in catalyst_countdown.py (runway < ~10d → auto-nudge SAM to spawn KOYOMI) → weekly scheduled run" | **PROSE-REMEDY (22)** | Specified 2026-05-28 (compute days to the furthest `docket/CATALYSTS.tsv` event; fail < ~10d ⇒ nudge). Not built: no `runway`/`tripwire` logic in `scripts/catalyst_countdown.py` or `boot.py`. The cost already landed: `docket/KOYOMI_MEMORY.md:52` (Run 22 self-audit, 9/11) "Run 21's headline "Runway: 501d" was WRONG — 136d… No instrument produced it: `catalyst_countdown.py`… prints no furthest-event figure… Hand-computed, uncheckable, and wrong by exactly 365 days." Carried across KOYOMI Runs 2→23 (Run 23 = 9/29, `c78f2d17e`) = 22 runs. The 5/28 gate ("evaluate-mode until Will decides he likes the pattern") has no date or owner and the pattern has since run 23 times — owner to confirm whether that gate still stands; if it does, re-classify DECLINED. |
| 64 | `CLAUDE.md:77` "13a. **Refresh `NEXUS_BRIEF.md`** … Checkable form: *the brief's commit timestamp ≥ this session's last STATUS commit timestamp.*" | **BUILT** | `scripts/closeout_check.py:516-525` `check_brief_ordering()` (git `%ct` brief vs STATUS; "F [step 13a] NEXUS_BRIEF.md was committed BEFORE the last STATUS.md commit"), built `c327b7859` 9/19 "the 6 prose-only closeout steps now have an instrument"; invoked at `CLAUDE.md:80` step 15 (PROVISIONAL per CATO 9/19). Note: computes the amendment-10 *timestamp* form that schema amendment 11 superseded with hash equality. |

**SAM step-1 false-positive rate: 1/6.** Desk verdict: 1 PROSE-REMEDY counted (+1 watch, under the bar).

### SENTRY (1 candidate) — ⚠️ OUT OF PERIMETER (ROSTER DORMANT)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 65 | `STATUS.md:36` "- `scripts/fetch_feeds.py` has no committed test file — extract to `scripts/test_fetch_feeds.py` (polish item; logged in TODO)." | **FALSE** (out of perimeter) | `PROME/ROSTER.md:128-131` lists SENTRY under **DORMANT** — the playbook perimeter is ACTIVE + TIER-2 + SPECIAL. The desk's own banner (`STATUS.md:3`, PROME as registrar, 2026-09-24, WQ-256 (d)) says "the TODO/ROADMAP items in this directory are HISTORICAL and must NOT be executed — rebuilding the pipeline is a Will ruling, not a task." `AGENTS/SENTRY/scripts/` does not exist (the script survives only at `archive/SENTRY_pipeline/fetch_feeds.py`). Last real commit `58c9e02aa` 5/09. Step-1 perimeter leak — see §3. |

**SENTRY step-1 false-positive rate: 1/1.** Desk verdict: `NOT READ (DORMANT — out of perimeter)` for the census; the one row was read and is FALSE.

### SHADE (1 candidate)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 66 | `STATUS.md:15` "Live verdict + rails (§0m)… owners (§7), owed list (§10) \| **Boot-read whole. Canonical on live state.** Budget 32,550 B; `python3 scripts/read_cap_check.py --agent SHADE` every closeout." | **FALSE** | Token hit is the section name "owed list (§10)"; the script named is the built root tool, invoked. |

**SHADE step-1 false-positive rate: 1/1.** Desk verdict: **CLEAN (1 read)**.

### TERRY (1 candidate; `scripts/` = boot, chain_fetch, chain_parse, csv_pnl, decoupling_series, grade_print, greeks, ledger_sweep, paper_book_mark, positions_from_forge, risk_calc, snapshot, test_snapshot_coverage)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 67 | `STATUS.md:27` "**Owed:** 🔴 **DOCKET L372** class-fix PROPOSAL (since 9/14; both instance gates are dead ⇒ a construction rule + template check) · 🔴 **`ledger_sweep.py` check A blind spot:** `COMPATIBLE` pairs `{CLOSED, FIRED}`…" | **DIAGNOSIS-ONLY** (L372 leg) + watch (ledger_sweep leg, 0 sessions) | **L372 leg:** the defect is named (gates test a HEADLINE, blind to COMPOSITION; `PROME/DOCKET.tsv` L372) and the fix is only named as a category ("a construction rule + template check"), owed to Will as a PROPOSAL — no computation is specified yet. Carried since 9/14 across 13 distinct TERRY STATUS commit dates; the owner's ask is to write the spec, not the code. **ledger_sweep leg:** fully specified ("a ledger still claiming FIRED/ACTIVE beside a CLOSED card passes… Narrow it with selftests; never widen"; `scripts/ledger_sweep.py:183` `frozenset({"CLOSED", "FIRED"})`) but first written this session (`e1c53844a`/`326235a68`, 10/8 11:10–11:58 ET) — 0 sessions carried, under the bar; re-check at run #2. |

**TERRY step-1 false-positive rate: 0/1.** Desk verdict: 0 PROSE-REMEDY (1 DIAGNOSIS-ONLY, 1 watch).

### VIOLET (10 candidates — the founding desk / positive control; 43 entries in `scripts/` incl. `tests/`)

**Positive control — run #0's five remedies (`ec5d05b69` 2026-09-04 13:56 ET, KB-VIO-240): all five BUILT at HEAD.**

| # | Remedy | At HEAD | Wired | Watched 10/8 |
|---|---|---|---|---|
| 1 | COT staleness schedule-aware (KB-VIO-226) | `scripts/canary_staleness.py`, last `c685cc318` 9/6 (v4: cadence+grace from the ledger, no calendar synthesis — KB-VIO-243, after v2/v3 were premise-wrong) | boot (`boot.py:55` `--quiet`) + closeout BLOCKING (`closeout_guard.py:79` `--strict`) | `canary_staleness.py --selftest` → "all cadence-rule selftests pass", rc 0 |
| 2 | `catalyst_countdown.py` holiday table | `NYSE_HOLIDAYS` `:36`, `HOLIDAY_COVERAGE` 2026-01-01..2027-12-31 `:58` (`ec5d05b69`) | boot | not re-run (static table read) |
| 3 | `move.py` phantom GATE-VIO-116 leg (KB-VIO-219) | removed; `move.py:52,69` carry the removal note | boot | — |
| 4 | `skew_integrity.py` (KB-VIO-241) | present (`ec5d05b69`) | **deliberately not boot-wired** ("the defect HEALS, so a check run before the work does not bound the work") — DECLINED-BY-DESIGN for wiring, BUILT as code | — |
| 5 | `twin_check.py` (KB-VIO-235) | rewritten `717c8f9a0` 9/4 (the external-review fix: bidirectional) | closeout BLOCKING (`closeout_guard.py:83`) | `twin_check.py --quiet` → **rc 1**, "🔴 TWIN CHECK — 4 item(s) need an OPERATOR decision" — the guard is live and currently RED on VIOLET's CALENDAR/CATALYSTS pair (observation, not a census finding) |

Step-1 recall on the control: the five surface in rows 68 and 73 (form 1). Run #0's premise caveat holds: 1 of 5 shipped premise-wrong (COT, typed three times) — *"5 rows typed; premise-verified at the source for 4 of 5 at first ship, 5 of 5 after `c685cc318`."*

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 68 | `CANARY_MAP.md:82` "this is the fourth-plus RED on this file, and a guard that cries wolf on a fixed weekly schedule is training its reader to wave the red through" | **BUILT** (control #1) | Inside the section headed "2026-09-04 (AM) — DIAGNOSIS AS WRITTEN AT THE TIME" (`:66`) and marked "✅ FIXED 2026-09-04 PM (Will-directed)" (`:86`); code `canary_staleness.py` v4 `c685cc318`. Labelled history — not a stale claim. |
| 69 | `MAINTENANCE.md:199` "2. **`backfill.py` — can now CREATE missing sessions.** Its CBOE pass iterated `rows.items()`, so the gapcheck's own printed remedy (`--spot-only`) did nothing over a gap." | **FALSE** | "What changed" item of the 2026-09-11 ~14:5x entry — DONE. |
| 70 | `MAINTENANCE.md:200` "3. **`surface_agreement.py` — memo glob bounded to ONE delivery date.**… **its printed remedy required editing a delivered record.**" | **FALSE** | Same entry, DONE. |
| 71 | `MAINTENANCE.md:220` "**Trigger:** Taking the 9/11 settle that the 14:5x session left owed. `thresholds.py --supersede` wrote NULL for `skew`" | **FALSE** | Trigger line of the 2026-09-11 (evening) entry; its "What changed" (`:223-227`) records the fix + `tests/test_stale_column_witness.py` (27 checks) + `run_tests.py` as the 9th blocking contract. |
| 72 | `LAST_COMPLETION.md:18` "**GAPS:** **`^SKEW` back-sweep still owed and now weaker on both modes**" | **FALSE** | File is two-state FROZEN: `LAST_COMPLETION.md:3` "⛔ FROZEN 2026-09-06 — NOT MAINTAINED… Do not read it as current". The back-sweep is a data task, not carried on any live VIOLET surface (zero hits in STATUS/SCRATCH/MAINTENANCE/CANARY_MAP). |
| 73 | `LAST_COMPLETION.md:20` "**BUILT (PM):** ① **COT staleness rebuilt THREE TIMES**… ⑤ **NEW `twin_check.py`**… every remedy had been written as prose for 2 days to 7 weeks" | **FALSE** | FROZEN record of the run-#0 build (the control itself). |
| 74 | `LAST_COMPLETION.md:21` "**REVIEW ROUND 3 (Codex, via Will)**… Remedy is a check, not a third sweep: **NEW `surface_agreement.py`, BLOCKING**" | **FALSE** | FROZEN record; the remedy it names is built (`scripts/surface_agreement.py`, closeout BLOCKING). |
| 75 | `CLAUDE.md:46` "7. **`STATUS.md`** — write the dashboard back… Keep under 250 lines (archive overflow to `research/` or `archive/`)." | **BUILT** | `scripts/thresholds.py:388` `CAPPED_DOCS = (("MAINTENANCE.md", 300), ("STATUS.md", 250))`, prints "CAP BREACH: … lines (cap ~250)" (`:406`); built `f73ebf092` 7/30 "third guard (doc-cap enforcement)"; its docstring (`:394-395`) names this exact prose rule as the one "that nothing enforced". |
| 76 | `CLAUDE.md:53` "12. **`NEXUS_BRIEF.md`** … Checkable form: **the brief's commit timestamp ≥ the session's last STATUS commit timestamp.**" | **BUILT** | `scripts/writeback_order_check.py` (`1dda98e31` 9/4 "Amendment 10 was a sentence, not a check; now it is code") — closeout BLOCKING (`closeout_guard.py:82`); tracks NEXUS_BRIEF, SCRATCH and the dated PROME memo (`:66-80`). This is H-4's founding instance. |
| 77 | `CLAUDE.md:164` "**PROME-facing** completion contract — a **DATED memo** ending in the COMPLETION block (`PROME/COMPLETION_SPEC.md`: …≤10 lines, RESULT carries a number)." | **FALSE** (for VIOLET) | FILES-table row citing PROME's spec. The memo's *ordering* is computed (`writeback_order_check.py:79`); the block *shape* (≤10 lines, a number in RESULT; `PROME/COMPLETION_SPEC.md:46,50`) is computed by no script in the repo — but that is the spec owner's (PROME's) fleet-wide rule, not a VIOLET remedy. Noted in §3. |

**VIOLET step-1 false-positive rate: 7/10.** Desk verdict: **CLEAN (10 read)** — 0 PROSE-REMEDY; positive control 5/5 BUILT.

### VULCAN (4 candidates; `scripts/` = catalyst_countdown, validate_workbook(+test); `tools/` = edgar_watch(+test), gpu_panel, mag7, semi_watch, tsmc_watch)

Session clock (VULCAN STATUS commit dates): 9/03 · 9/06 · 9/11 · 9/13 · 9/25 · 9/29 · 10/01 · 10/02 · 10/08. **The 4 rows dedupe to 2 distinct remedies:**
- **R-V1 `semi_watch.py` trade_date from the UTC run date [L-38].** Spec on the surface: "fix to the ET trade date or state the 16:00–20:00 ET window" (`STATUS.md:98`); `LESSONS.md:44` L-38 (9/29). Code unchanged: `tools/semi_watch.py:197-200` `now = _dt.datetime.now(_dt.timezone.utc)` … `row["trade_date"] = now.strftime("%Y-%m-%d")`; last commit to the tool `0e21628ea` 8/13. Found 9/29 (`461d388e9`), carried 10/01 · 10/02 · 10/08 = **3 sessions**.
- **R-V2 `edgar_watch.py` derives MU's window off the refuted 52-week period end.** Diagnosed 9/03 (`975937fc6`: "the 91-day-spacing derivation silently assumed a 52-week year… FY2026 is a 53-week year ending 2026-09-03"); spec on the surface: the true FY end is 9/03, "so the real window opens ~a week later" (`SCRATCH.md:77`). Code unchanged since `ce5a85983` 8/27. Carried 9/06 · 9/11 · 9/13 · 9/25 · 9/29 · 10/01 · 10/02 = **7 sessions** as an owed fix; on 10/08 it left the owed list and survives only as a caveat (`STATUS.md:87` "ignore `edgar_watch.py`'s printed window — wrong period end") — the caveat has replaced the fix (`[[finding_naming_a_caveat_can_substitute_for_fixing_it]]`).

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 78 | `STATUS.md:98` "**④ STILL OWED, named as owed:** … `semi_watch.py` stamps `trade_date` from the UTC run date — fix to the ET trade date or state the 16:00–20:00 ET window [L-38]" | **PROSE-REMEDY (3)** — R-V1 | As above. The same line's other legs are analysis/data tasks (MU 10-K GM re-check, a one-off `who_cares` count test, QQQ weight), not standing checks — not counted. |
| 79 | `SCRATCH.md:9` "4. **Housekeeping still owed (STATUS ④):** archive the four 10/01-graded PREDICTIONS rows by ROW · `semi_watch.py` ET stamp [L-38] · S2 spot series needs a NEW cadence" | **PROSE-REMEDY (3)** — R-V1 (duplicate of 78) | 10/08 SCRATCH block, same remedy. |
| 80 | `SCRATCH.md:27` "5. **Housekeeping owed (unchanged from 10/01):** … `semi_watch.py` UTC-stamp fix [L-38] · `edgar_watch.py` MU 52-week display defect" | **PROSE-REMEDY (7)** — R-V2 (+ R-V1) | 10/02 block; carries both. |
| 81 | `SCRATCH.md:48` "5. **Housekeeping owed:** … `semi_watch.py` UTC-stamp fix [L-38] · `edgar_watch.py` MU 52-week display defect · the S2 spot series needs a NEW cadence" | **PROSE-REMEDY (7)** — R-V2 (+ R-V1) | 10/01 block; carries both. |

**VULCAN step-1 false-positive rate: 0/4.** Desk verdict: 4 PROSE-REMEDY rows = **2 distinct remedies**.

### WALTER (3 candidates; 25 files in `tools/` incl. `walter_doctor.py`, `closeout_check.py`)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 82 | `LAST_COMPLETION.md:51` "5b. **🆕 10/13 (NEXUS wake, DOCKET L639) — S1 RE-OPENED AS A SPEC**… an ADVISORY `prome_gate.py boot` check on `inbox_census.py` = the missing WQ-206 aged-ACTION instrument" | **FALSE** (for WALTER) | A forward wake: WALTER owes an argument at an artifact ("Nothing owed before the artifact lands; the build is Will's word"). The remedy it names is PROME's — and it **corroborates PROME row 49**: `PROME/DOCKET.tsv` L304 graded YES 10/08 14:54 ET on two demonstrated misses (DEWEY 9/18→9/24, AEOLUS 9/6→9/10), L639 (10/13) registers the design. |
| 83 | `CLAUDE.md:76` "`AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv` (RED-FT — the **GENERATED scan view**, read this at boot; **count the rows; 12 as of 2026-09-03**" | **FALSE** | A read instruction ("read the file and count the rows"), not a comparison with a failure direction. The view's freshness is computed (RED `gen_trigger_scan.py --check`; WALTER boot 6b banner-sha, cited `tools/walter_doctor.py:2631`). Count at HEAD = 12 (RED-FT-01…12), so the as-of figure is still true. |
| 84 | `CLAUDE.md:132` "**Tier 2 — FULL (steps 12-16):** run when… OR a boot finds **≥3 stacked `full deferred` breadcrumbs** (surface "full closeout owed?" in the boot reply)" | **PROSE-REMEDY (65)** | Fully specified count (stacked `light-closeout — full deferred` breadcrumbs since the last FULL; ≥3 ⇒ surface "full closeout owed?"). No WALTER tool counts them: zero hits for `full deferred`/`breadcrumb`/`light-closeout` logic in `tools/*.py` (`walter_doctor.py:1618-1630` counts STATUS *leads*, a different cap). The data is sitting there: `SESSION_LOG.md` carries 47 literal `light-closeout — full deferred` tags. Rule since `63ce71109` 6/28; 65 distinct `LAST_COMPLETION.md` commit dates since (session proxy). |

**WALTER step-1 false-positive rate: 2/3.** Desk verdict: 1 PROSE-REMEDY.

### WATT (2 candidates, both form 2; code = `boot.py`, `power_watch.py` at the desk root)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 85 | `CLAUDE.md:43` "⚠️ **Revert to the full schema** at the next brief refresh if WATT reaches **≥3 persistent live cross-agent edges** OR starts carrying a **thesis version**" | **FALSE** | NEXUS amendment-9 revert trigger; "persistent live cross-agent edge" is undefined as a countable unit — a scope judgment, not a specified computation (same reading as NEXUS row 32). |
| 86 | `CLAUDE.md:182` "**<250 lines AND <64,000 bytes**… At **≥75% (48,000 B)** rotate… until **<70% (44,800 B)**… Checked at boot (leg 3)." | **BUILT** — stale claim (H-1) | `boot.py:175-214` `status_byte_budget()` checks STATUS + SCRATCH + PREDICTIONS against `READ_CAP_BUDGET = 32_550` (75% = 24,412 B), and its own comment `:155` says "⛔ WATT's self-set 64,000 B budget is RETIRED (2026-09-03)" (`42f924bb8`). The charter line still teaches 64,000 / 48,000 / 44,800 — unchanged since `3d2dd9707` 8/17, stale across 4 WATT STATUS dates since 9/03. A reader following the charter would rotate at 2× the enforced trigger. The 250-line leg is printed (lines + B/line), not compared; the code comment records why bytes, not lines, bind at this density (195 B/line ⇒ byte budget binds at ~166 lines). |

**WATT step-1 false-positive rate: 1/2.** Desk verdict: **CLEAN (2 read)** — 1 BUILT-stale for the owner to correct.

### ZHAO (2 candidates, both form 2; `scripts/` = boot.py, catalyst_countdown.py)

| TSV | Surface line (quoted ≤200) | Verdict | Evidence |
|---|---|---|---|
| 87 | `CLAUDE.md:55` "4. **`NEXUS_BRIEF.md`** — refresh every closeout… ≤100 lines. ⚠️ **ORDERING RULE**… **Checkable form: the brief's commit timestamp ≥ the session's last STATUS commit timestamp.**" | **PROSE-REMEDY (5)** | Two specified comparisons (brief commit time ≥ last STATUS commit; brief ≤100 lines), neither computed: `scripts/boot.py` never opens `NEXUS_BRIEF.md` (its only `100` is an oil-price zone at `:56`). Adopted `d757fb63b` 9/02; carried 9/17 · 9/18 · 9/19 · 9/25 · 9/30 = 5 sessions. **The defect it guards has already fired by hand:** `799e65c14` 9/18 "closeout re-run — the NEXUS ordering rule was broken by working past my own close"; 9/19 re-folded the brief four times (`068e753c7`, `0c86259a8`, `454f8aa5d`, `303dbc501`). Brief is at **exactly 100 lines** today. Typed form should be amendment-11 hash equality (see OTTO row 43). |
| 88 | `CLAUDE.md:256` "\| `NEXUS_BRIEF.md` \| Standing brief NEXUS consumes for cross-agent synthesis (VIEW/CALIBRATION/CROSS-DOMAIN/NEXT/FORWARD CATALYSTS, ≤100ln)." | **PROSE-REMEDY (5)** — duplicate of 87's ≤100-line leg | FILES-table restatement of the same uncomputed cap. |

**ZHAO step-1 false-positive rate: 0/2.** Desk verdict: 2 PROSE-REMEDY rows = **2 distinct remedies** (ordering; line cap).

## §2 Per-owner asks (STRICT one-liners; DAEDALUS packets them — none sent by this classifier)

| # | Owner | ACTION (surface line · carry · token) |
|---|---|---|
| A1 | NEXUS | NEXUS types the digest-reader pin check (`AGENTS/NEXUS/CLAUDE.md:49` "Readers also run the pin check (`git log` brief vs STATUS HEAD)") as a script over every brief. Carry: 3 sessions (9/29, 10/1, 10/8). Token: `PROSE-REMEDY (3)`. |
| A2 | OTTO | OTTO types `AGENTS/OTTO/CLAUDE.md:188` "brief's commit timestamp ≥ this session's last STATUS commit timestamp" as a closeout check, in the amendment-11 hash form. Carry: 7 sessions (8/27→10/4). Token: `PROSE-REMEDY (7)`. |
| A3 | ZHAO | ZHAO types `AGENTS/ZHAO/CLAUDE.md:55` "brief's commit timestamp ≥ the session's last STATUS commit timestamp" as a closeout check, in the amendment-11 hash form. Carry: 5 sessions (9/17→9/30); the rule broke by hand on 9/18 (`799e65c14`). Token: `PROSE-REMEDY (5)`. |
| A4 | ZHAO | ZHAO types the `NEXUS_BRIEF.md` "≤100 lines" cap (`AGENTS/ZHAO/CLAUDE.md:55`, `:256`) into `scripts/boot.py` or the closeout check. Carry: 5 sessions; the brief is at 100 lines on 10/8. Token: `PROSE-REMEDY (5)`. |
| A5 | RED | RED types `AGENTS/RED/MAINTENANCE.md:740` "Nothing compares `boot.py`'s METRIC_MAP source against each row's `instrument_basis` (ML-226)" as a check. Carry: 9 sessions (S42→S50). Token: `PROSE-REMEDY (9)`. |
| A6 | RED | RED adds a line-count comparison for `AGENTS/RED/CLAUDE.md:82` "≤200 lines", or names `read_cap_check.py --agent RED` in W1 as the binding check. Carry: 41 STATUS dates. Token: `PROSE-REMEDY (41)`, LOW. |
| A7 | OSPREY | OSPREY names a size check in closeout step 9 for `AGENTS/OSPREY/CLAUDE.md:48` "Keep under 250 lines". Carry: 22 STATUS dates. Token: `PROSE-REMEDY (22)`, LOW. |
| A8 | SAM | SAM types `AGENTS/SAM/MAINTENANCE.md:616` "runway < ~10d → auto-nudge SAM to spawn KOYOMI" into `catalyst_countdown.py` (it prints no furthest-event figure today), or records that the 5/28 Will gate still stands. Carry: 22 KOYOMI runs. Token: `PROSE-REMEDY (22)`. |
| A9 | VULCAN | VULCAN changes `tools/semi_watch.py:200` to stamp the ET trade date, per `AGENTS/VULCAN/STATUS.md:98` "[L-38]". Carry: 3 sessions (10/01, 10/02, 10/08). Token: `PROSE-REMEDY (3)`. |
| A10 | VULCAN | VULCAN re-derives MU's period end in `tools/edgar_watch.py` from the 53-week year ending 2026-09-03, per `AGENTS/VULCAN/SCRATCH.md:77`. Carry: 7 sessions (9/06→10/02); since 10/08 carried only as an "ignore" caveat. Token: `PROSE-REMEDY (7)`. |
| A11 | WALTER | WALTER types `AGENTS/WALTER/CLAUDE.md:132` "≥3 stacked `full deferred` breadcrumbs" as a `walter_doctor.py` count over `SESSION_LOG.md`. Carry: 65 LAST_COMPLETION dates since 6/28. Token: `PROSE-REMEDY (65)`. |
| A12 | PROME | No new packet. DOCKET L639 (due 10/13) already carries the WQ-206 aged-ACTION instrument for `PROME/CLAUDE.md:51`. Token: `PROSE-REMEDY (26)`, registered. |
| H1 | REGINALD | REGINALD strikes "exit-code defect still owed" at `AGENTS/REGINALD/STATUS.md:49` and `MEMORY.md:43`; `b6544d45d` (9/24) fixed the defect, watched rc 2 on 10/8. Token: `BUILT` (H-1, stale 2 sessions). |
| H2 | WATT | WATT replaces "64,000 bytes / 48,000 B / 44,800 B" at `AGENTS/WATT/CLAUDE.md:182` with the 32,550 B budget `boot.py:175` enforces. Token: `BUILT` (H-1, stale since 9/03). |
| H3 | NEXUS | NEXUS names `read_cap_check.py` (BOOT 0a) as the whole-file test at `AGENTS/NEXUS/CLAUDE.md:105`, in place of the hand `wc -c`. Token: `BUILT`, LOW. |

**Watch list for run #2 (no packet now):** SAM `STATUS.md:35` `mof_flows.py` latest-week-only alert (1 session, under the bar) · TERRY `STATUS.md:27` `ledger_sweep.py` `COMPATIBLE {CLOSED, FIRED}` blind spot (written 10/8, 0 sessions) · TERRY L372 class-fix (DIAGNOSIS-ONLY; the ask is a spec, not code) · OSPREY OWED-45 (DIAGNOSIS-ONLY; a `.gitignore` retention decision).

## §3 Limits

1. **Session counts are proxies, named per row:** desk-numbered sessions where the desk numbers them (RED S-numbers, OTTO s0NN, KOYOMI runs), else distinct commit dates of the desk's STATUS/LAST_COMPLETION. A date with two sessions counts once (under-count); a date with only a peer's packet commit is excluded by subject filter where I filtered (SAM, VULCAN, OTTO, ZHAO) and NOT excluded where I did not (OSPREY 22, RED 41, PROME 26, WALTER 65) — those four can over-count.
2. **Form-2 policy I applied:** a standing cap/comparison rule with no computing code is `PROSE-REMEDY` with carry counted from the rule's commit; where the 32,550 B byte budget binds before the line cap at the desk's measured density (OSPREY ~138 lines vs 250; RED ~181 vs 200), I marked it LOW. A judgment term with no countable unit ("persistent live cross-agent edges", NEXUS row 32 / WATT row 85) is `FALSE`. DAEDALUS may rule a different policy; the per-row evidence supports either reading.
3. **Class finding across desks (not a per-desk ask):** the NEXUS_BRIEF amendment-10 *timestamp* check is typed at SAM (`closeout_check.py:516`) and VIOLET (`writeback_order_check.py`), prose at OTTO and ZHAO — and schema amendment 11 (`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md:164`, 8/07) superseded the timestamp form with hash equality, so even the typed copies compute the retired form. NEXUS's schema says the invariant "is enforced at the check, not by fleet-wide instruction edits" (`:175`) — one shared check would close A1, A2, A3 and the two typed copies at once. Owner of that call: NEXUS (schema) with DAEDALUS (`scripts/`).
4. **Step-1 perimeter leak:** SENTRY (ROSTER DORMANT, `PROME/ROSTER.md:128-131`) is in the candidate list; the playbook perimeter is ACTIVE + TIER-2 + SPECIAL. I did not check whether BARON (the other DORMANT desk) or any A–M desk leaked the same way.
5. **Step-1 recall misses seen while reading (not classified, not counted):** ORACLE `MAINTENANCE.md:203` ladder re-banding diff ("is a build and is **not** attempted") and `:202` history dedupe ("Reported, not patched") — no step-1 token matches either phrasing. SAM's runway defect is evidenced in `docket/KOYOMI_MEMORY.md:52`, a file outside the perimeter. Candidate tokens to test at the next refinement: `not patched`, `not attempted`, `still derives`, `ignore .* printed` — under the playbook rule, only with a fleet before/after diff.
6. **Fleet-level gap outside every desk's lane:** no script checks the COMPLETION block shape (`PROME/COMPLETION_SPEC.md:46,50`: ≤10 lines, RESULT carries a number). Owner = PROME (spec). Not counted.
7. **Live edits during the read:** a concurrent PROME session modified `PROME/STATUS.md` (+3/−4) and `PROME/SCRATCH.md` (+5/−5) by 16:30 EDT; my PROME rows 45–48 quote the HEAD `46fa6ef4a` text the TSV was built on (I read them before the change). `PROME/CLAUDE.md:51` is unchanged.
8. **What I executed (read-only):** `scripts/read_cap_check.py --agent NEXUS`; `AGENTS/REGINALD/scripts/vx_ladder_check.py` under `/usr/bin/python3` (no yfinance ⇒ exits at import, no network, rc 2 observed); `AGENTS/VIOLET/scripts/canary_staleness.py --selftest` (rc 0); `AGENTS/VIOLET/scripts/twin_check.py --quiet` (rc 1 — VIOLET's own blocking closeout contract is RED on 4 items at 16:2x EDT; reported to DAEDALUS as an observation, not a census finding). `git status` after the runs shows no file changed by them. Everything else is `git log`/`grep`/`sed` reads.
9. **Not done:** desks A–M (the sibling record `runs/2026-10-08_PROSE_REMEDY_CENSUS_01_A-M.md`); packets; registry `last_run`/Run Log write-back (DAEDALUS's, after both halves).

*Record closed 2026-10-08 16:31 EDT (`date`). Classifier: non-owner, read-only; this file is its only write.*
