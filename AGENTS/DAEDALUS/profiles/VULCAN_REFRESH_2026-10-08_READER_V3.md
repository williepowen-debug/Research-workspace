# VULCAN profile refresh 2026-10-08 — READER V3 slice (DELTA since 2026-09-05)

**Reader:** V3 (read-only, DAEDALUS fan-out) · **Started:** Thu Oct  8 16:40:12 EDT 2026 · **Cluster:** everything that changed in `AGENTS/VULCAN/` since 2026-09-05 (git log, archive/, reports/, outbox/, inbox/processed/).
**Baseline under test:** `AGENTS/DAEDALUS/profiles/VULCAN.md` (body 2026-08-07, refreshed 2026-09-05; 52 lines) + FLEET_MAP row (last-scored 2026-10-01).

*(Sections appended as the read proceeds.)*

---

## 0. Size of the delta (measured)

| Measure | Value | Source |
|---|---|---|
| Commits touching `AGENTS/VULCAN/` since 2026-09-05 | **108** (50 VULCAN-prefixed subjects; 41 WALTER; 7 PROME; 4 DAEDALUS; 2 DEWEY; 2 ZHAO; 1 TERRY; 1 WATT) | `git log --since=2026-09-05 -- AGENTS/VULCAN/` |
| Lines | 362 file-changes, +5,945 / −1,283 | same, `--shortstat` |
| VULCAN sessions | **8**: 9/06 (×4 passes incl. 3 CODEX review rounds) · 9/11 · 9/13 · 9/25 · 9/29 · 10/01 · 10/02 · 10/08 | commit subjects |
| Dark windows | **9/14→9/24 (12 days)** · **10/03→10/07 (5 days)** | `f905c37ed` msg "boot after 12 dark days"; `GPU_INSTRUMENT_SPEC.md` §7b header "desk was dark 10/03–10/07" |
| Launch mix | PROME-spawned 5 (9/11, 9/13, 10/01, 10/02, 10/08) · Will-launched 3 (9/06, 9/25, 9/29) | commit bodies |
| Runtime/model trailers | Opus 5 (1M) 9/06, 9/13 · Fable 5.1 9/11 · Opus 5.5 9/25→10/08 · Opus 4.7 10/02 | `Co-Authored-By` lines |
| File growth 9/05 → now | STATUS 22,911→22,781 B (122→106 ln) · SCRATCH 21,429→16,263 · **CLAUDE.md 62,438→82,125 B (+31%)** · NEXUS_BRIEF 106,097→22,531 (rotated) · THESIS 54,695→62,585 · **CHANNEL_DETAIL 76,927→119,939 B** · LESSONS 43,273→61,436 (L-29..L-42) · EXIT_PROTOCOL 35,380→26,968 (peaked 56,347 then rotated 10/01) · **KB.tsv 218,906→320,244 B** (KB-150..203) · TRADE.md **byte-identical (8,090 B)** | `git show 211d555ce:<f> \| wc -c` vs `wc -c` |
| New files | `workbook/GPU_INSTRUMENT_SPEC.md` (41.5 KB) · `workbook/GPU_SERIES.tsv` (10 rows) · `workbook/GPU_PANEL_INPUT_TEMPLATE.json` · `workbook/MU_FQ4_RESOLVER.md` (FROZEN) · `tools/gpu_panel.py` (380 ln) · `scripts/test_validate_workbook.py` · 10 archive files | `git log --diff-filter=A` |

## 1. WHAT CHANGED since 2026-09-05

| Date | Change | Commit | Consequence for the profile |
|---|---|---|---|
| 09-06 | Boot found 4 packets acted-on-but-unfiled, 3 fired catalyst rows unmarked; fixed | `0ad6cf0b3` | Closeout record-keeping lags action (self-caught) |
| 09-06 | WALTER correction REFUTED at primary (NVDA "procurement of memory" IS in 8-K Ex-99.2); FL-VULCAN-12 LIVE→CANDIDATE; WATT 55 GW seam defect found 33 days old | `db3d4ae2b` | Seam row in profile §3 was citing wording that was wrong at 9/05 read (already corrected in profile 9/08) |
| 09-06 | **GPU-rental instrument encoded** (11th ledger, zero rows, cadence pre-committed); validator could not grade an empty ledger → fixed | `c6f1161e5` | New instrument + new ledger absent from 9/05 profile |
| 09-06 | **PREDICTIONS split** 57,244→37,332 B; 8 resolved rows → `archive/PREDICTIONS_RESOLVED_2026-09.tsv` (crc 0xc3603220); mag7 cadence pre-committed | `28f74d735` | New archive; VULCAN-07 gate now lives ONLY in STATUS triad (`STATUS.md:66`) — a do-not-touch candidate |
| 09-06 | 3 CODEX review rounds: validator `allowed_values` enforced (11 unchecked closed sets found); KB-148 HBM multiple downgraded to PROVISIONAL; regression suite `test_validate_workbook.py` (31 cases) whose own control check could not fail → fixed | `eafe981e4` `68e392d73` `8c33df2d2` | Outside reviewer (CODEX) found real defects incl. desk misrepresenting the reviewer; regression suite is new tooling |
| 09-06 | Desk found PROME's 9/3 GPU ruling never reached its cc list (WATT/DEWEY); delivered and verified | `892dda92a` `2ca2cd971` | Cross-desk routing finding originating at VULCAN |
| 09-11 | **VULCAN-17 registered** — NVDA guarantee-commitment level $108,529M max gross (DEWEY REQ-002 integrated); inbox 14→0; `SCRATCH_ARCHIVE_2026-09.md` created, `STATUS_ARCHIVE_2026-09.md` (created 9/06) appended | `e44593197` | New open prediction; S5 instrument |
| 09-13 | **GPU-PANEL-01 FROZEN**; contract tier is an EMPTY set (no public 12-mo H100 quote at 4 vendors) ⇒ the designed spread is UNGRADEABLE; OCPI index found; `gpu_panel.py` built (selftest 16/16, failed first run on own arithmetic); 3 cadence misses recorded | `d437a068d` | The instrument the 9/05 profile didn't know about lost its designed measurement before its first row |
| 09-13→09-24 | **DARK 12 days.** Missed: mag7 slots 9/18, 9/25 (9/11 already missed); semi_watch 9/18, 9/22; GPU readings 2-3 | `f905c37ed` msg; FLEET_MAP row | L5 currency leg broken; S2 re-arm rule became UNGRADEABLE (6 of 8 slots lost → later 0 of 8) |
| 09-24 | PROME caught NEXUS_BRIEF at **137,282 B** (2.2–4.2× read cap) | `f39972f32` | Outside-caught defect |
| 09-25 | Boot after dark; ORCL 10-Q read (off-BS leases $260B→$288B; $3.3B guarantee unmentioned); Jupiter force majeure; STATUS rotated **whole** (30,476 B) into live `CHANNEL_DETAIL.md` §E; NEXUS_BRIEF rotated 137,282→13,895 B; maturity line L3→L4 corrected per DAEDALUS PR#6; WQ-295 cadence declared **WEEKLY** + 11 WATCH_FOR phrases | `f905c37ed` `193ed19e7` `274dfcf12` `d8c537482` | CHANNEL_DETAIL becomes a live rotation sink (deviation); declared cadence is new contract |
| 09-29 | **MU_FQ4_RESOLVER.md written before the print** (14-week-quarter trap, no-substitute-figure rule); GPU §7a 10/05 decision pre-written (R-A..R-H); register pruned 18 rows → archive; **kill-rail leg 4 (financing structure) ADDED: 1 of 3 → 1 of 4 by addition**; new S1 safety/demand sub-read | `98d815913` `45f3fa7f2` `c4c586aac` | Kill rail restructured (profile cites old :28-30); pre-registration discipline exemplary |
| 09-29 | 9/25 and 9/29 semi_watch/mag7/GPU slots MISSED | `87b83ff89`, `c0fe1d3ba` | — |
| **10-01** | **MU FQ4 GRADED** from the frozen resolver: VULCAN-02 HIT · **-11 FALSIFIED** · -12 HIT (letter; composition disagrees) · -14 HIT ⇒ **S2 3→2 FORCED**, composite 15→14/25; EXIT_PROTOCOL Micron half rewritten, log rotated 56,347→25,925 B; packets to PROME/HENRY/CARL/LIQUID/WALTER/WATT/VIOLET | `bbd75b2e7` `57c2ea6ed` | The profile's own refresh trigger fired; first score move in 15+ sessions |
| 10-02 | Fri post-close slot 4 TAKEN: mag7 (breadth −5.07pp, 3.7th pctile, 2.4pp from red leg) + **GPU reading 4 = first GPU_SERIES row** (10 cells); TERRY ask ACK'd with a 4-point starter (contains wrong QQQ-membership fact) | `fbb97d895` | First on-cadence slot taken since 9/04 |
| 10-03→10-07 | **DARK 5 days**; 10/05 L250 re-decide and TERRY 10/05 08:30 reply both missed on date | `GPU_INSTRUMENT_SPEC.md` §7b header; TERRY packet | Second dark window after declaring WEEKLY |
| 10-08 | L250 applied 3 days late: §7a **R-A both tracks** (CFTC review to 11/09; ICE no date); TSMC Sep swept (+41.1%); Samsung Q3 OP +20.0% QoQ; inbox 17→0; **QQQ-membership correction to TERRY** (CRWV IS in NDX, ORCL is not — the 10/02 fact had been folded into TERRY's FINAL L590); STATUS cells → CHANNEL_DETAIL §F | `00a13c4c1` `23ef70e7c` | A VULCAN defect reached a FINAL trade card before self-correction |

## 2. EVERY claim in the 9/05 profile (§2–§6), graded at today's artifact

| # | 9/05 claim (profile line) | Verdict | Evidence today |
|---|---|---|---|
| C1 | "Last session 2026-09-03" (`VULCAN.md:14`) | **CHANGED** | Last session 2026-10-08 (`STATUS.md:3`); 8 sessions since (§0) |
| C2 | "STATUS 122 ln" (`:14`) | **CHANGED** | 106 ln / 22,781 B = 70% of budget (`read_cap_check.py --agent VULCAN`, rc 0) |
| C3 | "11.4k-line build-out: `tools/edgar_watch.py`, `mag7.py`, `scripts/catalyst_countdown.py`" (`:14`) | **CHANGED** | All three exist; build-out grew: `tools/gpu_panel.py`, `scripts/test_validate_workbook.py`, `workbook/GPU_INSTRUMENT_SPEC.md`, `MU_FQ4_RESOLVER.md` added. Tracked files under `AGENTS/VULCAN/`: 261 (163 at 9/05 base `211d555ce`). The 11.4k counting method is not recorded, so no like-for-like line count |
| C4 | "Kill rail LIVE at `EXIT_PROTOCOL.md:28-30`, re-read not restated" (`:14`) | **CHANGED** | The rail is at `EXIT_PROTOCOL.md:21-24` and has **4 legs**: leg 4, financing structure, was added 9/29 (`c4c586aac`; §8 `:149-153`). It is still re-read leg by leg (`:125`, `:132`, `:140`) |
| C5 | "Conf M→H gate MET, at four readers' artifacts" (`:16-17`) | **CHANGED** | Gate stays met (FLEET_MAP Conf H, scored 10/01), but **2 of the 4 cited reader artifacts no longer carry the citation** (C9, C10). The live consumers today are a different set (C18) |
| C6 | WATT `STATUS:38` "32 GW is the firm figure" (`:21`) | **STILL TRUE** (in substance) | `WATT/STATUS.md:38` reads "32 GW firm coincident vs 55 GW utility-reported (non-coincidence + duplication, NOT a haircut)". Wording changed, figure held. WATT last STATUS 2026-09-25 (`a521269db`) |
| C7 | WATT `STATUS:79` "🟡 Owed to VULCAN: the hedged-vs-floating share of neocloud load" (`:21`) | **CHANGED** | No "owed to VULCAN" line remains. The question now sits as WATT's **own premise**: `WATT/STATUS.md:91` (OPEN 6b "Resolve the hedged/floating split FIRST") and `:108`. The two-way obligation was re-homed, not discharged |
| C8 | VULCAN↔WATT seam: corrected wording, aggregate forecast vs firm coincident peak (`:22`) | **STILL TRUE** | `VULCAN/STATUS.md:26` "~55 GW aggregate utility-reported forecast / ~32 GW firm coincident-peak (two bases, never netted…)", `:44`, `:63`. WATT side: `WATT/STATUS.md:39` "✅ VULCAN seam CLOSED 9/25 at ITS artifact" |
| C9 | ZHAO `STATUS:18` "High-tech mfg 52.9 — held in expansion — VULCAN's leg" (`:23`) | **FALSE** | `ZHAO/STATUS.md:18` is now a BIS-perimeter row. Hi-tech 52.9 survives at `:63` ("PMI cluster (AUG) … hi-tech 52.9"), **with no VULCAN attribution**. The ownership acknowledgement is gone |
| C10 | VIOLET `STATUS:94` "Equity concentration (VULCAN-owned)" (`:24`) | **FALSE** | `VIOLET/STATUS.md:71` "Equity concentration · 🟡 2 · S5TH 45 [9/24] … **(WALTER SIG-006, HENRY owns)**". No "VULCAN" string anywhere in VIOLET STATUS. VIOLET was last current 2026-09-28 (`e7a3ac8ab`); VULCAN's 10/01 MU packet sits **unconsumed** in `VIOLET/inbox/` |
| C11 | Volume: 8 WATT, 7 VIOLET, 4 ZHAO, 4 HENRY, 3 NEXUS in `processed/` (`:26`) | **CHANGED** | Same method (filename contains "vulcan", processed paths): WATT **16**, VIOLET 7, ZHAO **7**, HENRY **6**, NEXUS 3. Unconsumed today: **WATT 2** (10/01 MU grade, 10/08 L250), **VIOLET 1** (10/01) |
| C12 | "WATT ran 9/3 and is the strongest consumer" (`:28`) | **CHANGED** | WATT has been dark since 9/25 (`WATT/STATUS.md:1` "Last Updated 2026-09-25"). Its last action on VULCAN content was closing the seam on 9/25. The strongest live consumer is now NEXUS (C18) |
| C13 | Grade **L4, Conf H** (`:30`) | **STILL TRUE** | FLEET_MAP `VULCAN Market L4 H … 2026-10-01`. ⚠️ `VULCAN/STATUS.md:5` still cites "Last_scored 2026-09-17": the PR#7 re-score was never packeted (no DAEDALUS packet to VULCAN between 10/01 and 10/08 16:35) |
| C14 | L1–L2 floor PASS (`:33`) | **STILL TRUE** | STATUS with BOTTOM LINE (`STATUS.md:104-106`). Ledgers accruing: `validate_workbook` "11 ledgers conform" (`fbb97d895`, `193ed19e7` bodies); KB +54 rows |
| C15 | L3 convergence / exit / predictions PASS, rail re-read (`:34`) | **STILL TRUE** | Matrix `STATUS.md:20-30`. Four predictions resolved 10/01 against a pre-print resolver (§4 below). Rail re-read on 9/25, 9/29, 10/01 and 10/08 (`EXIT_PROTOCOL.md` §7) |
| C16 | L3 dated falsification surface at `EXIT_PROTOCOL.md:28-30` (`:35`) | **CHANGED** | The surface is at `:21-24`. ⚠️ **Its freshness claim is stale again**: `EXIT_PROTOCOL.md:3` "Newest entry: 2026-10-01 … bump it whenever an entry lands", but a 2026-10-08 entry landed at `:140` (`00a13c4c1` diff touches only `@@ -137` and leaves the header alone). This is the exact defect DAEDALUS PR#6 flagged on 9/17, and VULCAN fixed it on 9/25 (`f905c37ed`) |
| C17 | L4 TRADE leg PASS: "`TRADE.md` present" (`:36`) | **CHANGED (at risk)** | Present but **byte-identical since 2026-08-27** (`65b365943`). `ledger_staleness.py VULCAN --trade` gives **STALE +42d**. Content now FALSE in places: `TRADE.md:5` "every channel is at 3 🟠" (S2 has been 2 since 10/01); `:16` Mag-7 32.9085% [8/26] (now 34.5445%); `:27` "Next state change to watch: MU FQ4 ~2026-09-29" (graded 10/01). Under reading A (ratified 10/01), the per-channel "Trigger to propose" column (`:14-20`) can serve as the re-arm condition, but the surface asserts a state the desk's own STATUS contradicts. SCRATCH carries it as "TRADE.md 36 days stale (not touched)" (`SCRATCH.md:9`); 36 is a carried figure, and the true age at 10/08 is 42 |
| C18 | L4 "signals flowing AND consumed — PASS, 4 readers" (`:37`) | **CHANGED** | Still PASS, on different readers. **NEXUS** carries VULCAN's figures as canonical (`NEXUS/STATUS.md:31` M-09 "VULCAN composite 14/25 … Mag-7 34.54% … −5.07pp [10/2]", `:45`, `:47`). **HENRY** `STATUS.md:65`. **TERRY** folded a VULCAN fact into its FINAL card L590 (the fact was wrong; see F-B). **PROME** DOCKET L114, L547, L564 and L250 all RESOLVED from VULCAN artifacts. The original WATT/ZHAO/VIOLET legs have decayed |
| C19 | L5 PARTIAL: current ✅ (2d); needs a second clean cycle (`:38`) | **CHANGED** | FLEET_MAP 10/01: "L5 current NOT MET: dark 9/13-9/24; mag7 slots 9/11, 9/18, 9/25 missed; 0 of 8 pre-committed S2 slots". Since then the 10/02 slot was TAKEN, but the 10/05 L250 decision ran 3 days late (dark 10/03-10/07) |
| C20 | Next-upgrade: "L5 on two consecutive clean cycles. The consumption gate is closed" (`:40`) | **CHANGED** | FLEET_MAP Next_upgrade now: "L5 on two consecutive WEEKLY cycles that take every registered slot (first: mag7 slot 4 + GPU reading 10/02; then the 10/05 compute-futures read) with no outside-caught defect". Cycle 1 met on 10/02; **cycle 2 failed**: the 10/05 read was taken 10/08 |
| C21 | F-1: tripwire candidate (n=1), review 2026-09-12, dedup vs PAT-115 (`:43`) | **CHANGED (lapsed twice)** | Not ruled at 9/12 (`DAEDALUS/runs/2026-09-25_INBOX_DISPOSITIONS.md:16`). Reached n=2 via HANS 9/18, then deferred to PR#7 10/01 (`2e1cdfdd2`), where it was not ruled either: there is no "tripwire" row in `PATTERNS.tsv` (only PAT-115 at `:118`). A **DAEDALUS-owned** carried assertion, not a VULCAN gap (VULCAN traced the provenance to DAEDALUS's own commit `cdde3ef30`: `DAEDALUS/inbox/processed/2026-09-25_from-VULCAN_PR6-asks-done…md:11-12`) |
| C22 | F-2: S4_SERIES latest month July; next edition ~9/10 (`:45`) | **CHANGED (resolved)** | `S4_SERIES.tsv` tail: Aug row written 2026-09-11 (filed 9/10), Sep row written 2026-10-08 (filed 10/08). The monthly cadence held both times |
| C23 | F-3: dated trigger = MU FQ4 (~9/30, grade 10/01) or 21d → checkpoint 2026-09-26 (`:4`, `:47`) | **CHANGED (FIRED, refresh late)** | The 9/26 checkpoint passed with no refresh. MU printed 9/30 and was graded 10/01 (`bbd75b2e7`). FLEET_MAP 10/01 says "Profile FIRED". This refresh starts **7 days after the trigger and 12 days after the checkpoint** |
| C24 | DO-NOT-TOUCH 1: the 55/32 GW seam, "adopt verbatim, never net or average" (`:50`) | **STILL TRUE** | `VULCAN/STATUS.md:26` "two bases, never netted"; `WATT/STATUS.md:38` |
| C25 | DO-NOT-TOUCH 2: the kill rail is re-read, not restated (`:51`) | **STILL TRUE** | `EXIT_PROTOCOL.md:140` "re-read leg by leg, nothing moved"; each leg is re-stated with a dated instrument read (`:141-145`) |
| C26 | DO-NOT-TOUCH 3: `catalyst_countdown.py` is the P3 consolidation donor; "the fleet-wide consolidation reads from here" (`:52`) | **CANNOT-VERIFY** | No consolidated tool or reader exists. There are **10 divergent copies**, every md5 distinct (`md5sum AGENTS/*/scripts/catalyst_countdown.py`). VULCAN's copy gained an NYSE holiday calendar on 9/06 (`c6f1161e5`); HAWK and VIOLET copies carry 0 "holiday" hits. P3 traces to `DAEDALUS/runs/2026-08-28_WIRING_SWEEP/RUN_RECORD.md:107` ("consolidation proposal P3"), and no record shows it ran. The protection is still prudent, but its stated reason has no live consumer |

**Tally (26 claims): STILL TRUE 7 · CHANGED 16 · FALSE 2 · CANNOT-VERIFY 1.**
Header claims outside §2–§6, also checked: the 9/08 correction banner ("Confidence stays H … not as independent verification of market figures") is **STILL TRUE**.

## 3. The thesis under test since 9/05: the events, and what VULCAN graded

### 3a. MU FQ4: the profile's own refresh trigger

| Step | Fact | Where it is recorded |
|---|---|---|
| Pre-registration | `workbook/MU_FQ4_RESOLVER.md` was written **2026-09-29 09:28 ET** (`98d815913`), before the 9/30 16:30 ET print. It pre-states the 14-week-quarter trap (FQ4 = 98 days, so a flat business guides FQ1 about −7.1%), forbids substituting a sell-side figure for TrendForce, and reads F3 at the 9/30 close, not after hours | resolver §2 `:48-77`, §5 `:109-120` |
| Timing proof | **Byte-checked by me:** `git diff 41b210490 bbd75b2e7 -- …MU_FQ4_RESOLVER.md` shows exactly two hunks, the FROZEN banner (`@@ -1,5 +1,8`) and the appended §6 (`@@ -112,3 +115,41`). §§1–5 are untouched after the print, so the sheet's own claim (`:3`) holds. Under PREDICTION_DISCIPLINE `:33` this is a valid timing claim (the spec commit precedes the result) | git |
| Grades (10/01, `bbd75b2e7`) | **VULCAN-02 HIT** (branch a: DRAM high-teens % up, NAND ~+30%) · **VULCAN-11 FALSIFIED** (all three legs: TrendForce 4Q26 conventional DRAM **+10–15% ≥ +10%**; FQ1 guide $61.5B > FQ4 $54,229M; MU 9/30 close $1,065.11 ≥ $940.70) · **VULCAN-12 HIT on the letter** via the guide branch (GAAP GM 86.76%; FQ1 guided 85.95% GAAP / 86.25% non-GAAP), with the **composition disagreement recorded** (Micron attributes the dip to incentive comp, a cost item, not a price ceiling, so no magnitude is claimed) · **VULCAN-14 HIT** (TSMC cum Jan-Aug +39.3% ≥ +37.0%) | resolver §6 `:121-155` |
| Score consequence | **S2 3 → 2, FORCED** by VULCAN-11's registered if-falsified action. Composite 15 → 14/25. The S2 leading indicator was RETIRED (the re-arm rule was UNGRADEABLE, 0 of 8 slots) | `STATUS.md:25`, `:30`, `:62` |
| Recorded where the rail says? | **YES, on every surface checked:** ① `PREDICTIONS.tsv` `status`/`resolution` cells set (HIT / FALSIFIED / HIT / HIT) with primaries and accession numbers; ② resolver §6 (FROZEN); ③ STATUS calibration line `:70` ("17 registered · 12 RESOLVED … 5 OPEN"); ④ EXIT_PROTOCOL §4 marked RESOLVED/SPENT (`:59`) and §4b made live (`:78`); ⑤ PROME `DOCKET.tsv` L114 and **L547 RESOLVED** citing `bbd75b2e7`; ⑥ packets to PROME, HENRY, CARL, LIQUID, WALTER, WATT, VIOLET (WATT and VIOLET **unconsumed**) | as cited |
| Open tail | ① The four graded rows are **still in the live ledger** ("archive by ROW" has been owed since 10/01: `STATUS.md:70`, `:98`). ② The **MU 10-K re-check of VULCAN-12's FQ4 GM** is owed (`:98`; 10-K expected ~10/09) | `STATUS.md:98` |
| ⚠️ Registration gap found at grade time, disclosed rather than smoothed | VULCAN-11's F1 letter ("≥ +10%") never said how to grade a **published RANGE**. TrendForce printed 10–15%, with the floor **exactly on** the inclusive line. The grade is clean only because every point clears; the sheet itself says "had TrendForce printed 9–14%, this leg would have needed a rule §2 never wrote" (`:139`). The 9/29 resolver re-wrote traps but did not add a range rule. PREDICTION_DISCIPLINE `:31` (name the grading basis at registration) post-dates the 8/03 registration, so this is grandfathered, but the class is live for VULCAN-13/-15/-17 | resolver `:139` |

### 3b. Other events since 9/05 that tested the thesis

| Date | Event | VULCAN's read | Score effect | Ref |
|---|---|---|---|---|
| 9/11 | ORCL Q1 FY27 8-K: capex $28.5B/qtr, FCF −$5B, $20B ATM | S5 strand | none | `e44593197`, KB-156 |
| 9/11 | NVDA guarantee book baseline $108,529M max gross (incl. $105B SB Energy) | **VULCAN-17 registered** (resolves at the ~11/19 10-Q) | none | KB-153..155 |
| 9/12–14 | "Slow-the-frontier" shock; SOX −5.9% on 9/14 | **price event, not capex** (0 capex/contract changes) | none | KB-166, `STATUS.md:67` |
| 9/24 | ORCL **force majeure on Project Jupiter** (2.45 GW) | S3 = DELAY, not removal of firm capacity; S5 = first risk-transfer exercise (n=1) | none | KB-167/174, `STATUS.md:26` |
| 9/11→9/25 | ORCL 10-Q: off-BS DC leases **$260B → $288B**; $3.3B guarantee **unmentioned** | S5 strand; kill-rail leg 4 from-state | none | KB-168 |
| 9/25 | OpenAI frontier pause (open-ended); SB Energy IPO postponed | new S1 safety/demand sub-read (3 pauses / 2 labs / 0 contract changes); SB Energy **AMBIGUOUS on the letter**, withdrawn S-1 pre-stated as PULLED | none | KB-173..178, `STATUS.md:65`, `:67` |
| 9/30 | **MU FQ4** | §3a | **S2 3→2** | above |
| 9/30 | TrendForce 4Q26 DRAM +10–15% public | VULCAN-11 F1; thesis-kill **leg 3 strengthened** (1 of 4 quarters in hand) | via VULCAN-11 | KB-187, `EXIT_PROTOCOL.md:23` |
| 10/02 | Breadth RSP−SPY 63d **−5.07pp** (3.7th pctile), up from +3.70pp on 9/01 | S1 band stays YELLOW on the AND; breadth leg 2.4pp from red | none | `MAG7_SERIES.tsv` 10/02 row |
| 10/02 | AMZN ~$8B GB SPV in talks; Toshiba HDD −10% | capex funded differently, not cut; storage crack outside S2's cell | none | KB-191/192 |
| 10/05 | CME/ICE compute futures **did not list** | §7a **R-A** applied 10/08 (3 days late) | none | KB-193/194, GPU spec §7b |
| 10/08 | Samsung Q3 OP +20.0% QoQ; TSMC cum Jan-Sep +41.1% | leg 3 "a 2nd major agrees"; S4 no-stress | none | KB-195/196 |

**Kill-rail reading, net:** thesis-kill moved **1 of 3 → 1 of 4 by ADDITION** (9/29), not by evidence. The desk flags the risk against itself: "an added AND-leg makes the thesis HARDER to kill, which is the direction to distrust" (`EXIT_PROTOCOL.md` §8 item 1), with guards stated (levels, instruments and a 2027-03-31 date). ⚠️ On 10/08 leg 3 was annotated "a 2nd major agrees" on **Samsung operating profit** (`:143`), but the leg's named instrument is the TrendForce contract series plus MU prints (`:23`). That is corroboration outside the instrument, harmless as worded ("agrees", not "met"), and worth watching as instrument drift.

## 4. Template §4: deviations from standard (+why), seen in the delta

| Deviation | Where | Better / equivalent / debt | Why |
|---|---|---|---|
| **Pre-print resolver sheets**, frozen after use, cited from the PREDICTIONS resolution cells | `workbook/MU_FQ4_RESOLVER.md`; GPU spec §7a (byte-unchanged since 9/29: I diffed `98d815913` against HEAD, and the only difference is the appended §7b) | **Better** | Makes the timing claim auditable by git; the fleet exemplar for grading against a pre-registration |
| STATUS rotated **whole** into a LIVE on-demand file, not `archive/` | `CHANNEL_DETAIL.md` §E (30,476 B, crc `0x02b4969e`, **crc verified by me** against `193ed19e7^`) and §F (10/08 cells) | **Debt (watch)** | It keeps the evidence live for per-channel reads, but CHANNEL_DETAIL grew from 77 KB to 120 KB in 33 days and is now a second, uncapped sink. Rule 17 ("a watch written there does not travel", `STATUS.md:16`) is the guard |
| Charter as a giant FILES table: per-tool cells of 1.6–4.9 KB carrying incident narrative | `CLAUDE.md:237-267`; total **82,125 B** (+31% since 9/05); out of read-cap perimeter "unless declared" (`read_cap_check` charter line) | **Debt** | A free-text register cell accretes the story of each finding (the FLEET_MAP `Gaps` lesson, repeated in a desk charter). It is also where staleness hides: see F-A |
| Outbound packets written straight to recipients' `inbox/`; `outbox/` unused since before 9/05 | 40 `from-VULCAN` packets since 9/05 across 11 inboxes; `ls outbox` returns nothing ≥ 2026-09-05 | **Equivalent** (root carve-out ①) | Delivery is verifiable at the recipient; the desk itself verified a cc-delivery gap that way (`2ca2cd971`) |
| Instrument cadences pre-committed **before** the first row (GPU, mag7) and misses recorded, never cured off-cadence (L-21) | `CLAUDE.md:237-238`, `:257-260`; `1d8e00620` | **Better** in design; **debt** in execution | 0 of 8 S2 slots; mag7 slots 1–3 (9/11, 9/18, 9/25) missed, slot 4 (10/02) taken. The rule is right, and attendance is the gap (FLEET_MAP L5) |
| A declared WEEKLY cadence (WQ-295, 9/25) followed by a 5-day dark window that missed a dated decision | `PROME/inbox/processed/2026-09-25_from-VULCAN_cadence-and-watch-terms.md`; GPU spec §7b header | **Debt** | PROME's re-spawn rail covers post-close slots (DOCKET L564 pattern), but the 10/05 L250 row was not re-spawned on date |
| A predicted-but-unpublished trade surface left unfrozen with stale body | `TRADE.md` (C17) | **Debt** | Blueprint §8 / PAT-023: FROZEN banner OR a live alert. The alert fires (`boot.py:386` runs `ledger_staleness --trade`), and the desk carries it, "not touched", for 3 sessions: `SCRATCH.md:9`, `:27` |

## 5. Template §7: open questions / comprehension gaps

1. **Is `TRADE.md` a live surface or a frozen one?** It reads live ("every channel at 3"), is 42 days stale and makes false state claims. Under reading A, does the per-channel "Trigger to propose" column count as an explicit re-arm condition? This decides the L4 trade leg at the 10/15 review.
2. **Who owns the WATT-side obligation now?** The hedged-vs-floating split moved from "owed to VULCAN" to WATT's own premise (`WATT/STATUS.md:91`). Did VULCAN's 9/06 answer (`WATT/inbox/processed/2026-09-06b_…`) discharge VULCAN's half, or is a VULCAN input still owed? Not traced.
3. **Why did ZHAO and VIOLET drop the VULCAN attribution?** It could be a deliberate re-attribution (VIOLET now says "HENRY owns" equity concentration) or rotation loss. Not traced in their git history. If deliberate, a **routing fact** changed (who owns equity concentration) that neither VULCAN's STATUS nor `_NETWORK.md` may reflect.
4. **`CLAUDE.md:259` and `GPU_INSTRUMENT_SPEC.md:4` describe a zero-row ledger that has had 10 rows since 10/02.** The 10/02 session wrote "CLAUDE.md unchanged (no … instrument … touched)" (`fbb97d895` body). Is the step-4b FILES self-check scoped to *structural* change only? If so, a state claim inside a FILES cell is outside every check.
5. **P3 / `catalyst_countdown.py`**: is the consolidation still planned? If not, DO-NOT-TOUCH #3 should be re-based (C26).
6. **CHANNEL_DETAIL.md (120 KB)** has no byte rule of its own. Is it ever read whole (by NEXUS, PROME or a boot)? Not checked beyond VULCAN's own boot perimeter.
7. **Model/runtime variance across sessions** (Fable 5.1 on 9/11, Opus 4.7 on 10/02) is recorded only in commit trailers. Not assessed for effect.

## 6. Findings (ranked)

- **F-A 🔴 Charter and instrument spec assert a zero-row GPU ledger that has had 10 rows since 10/02.** `CLAUDE.md:259` reads "HEADER ONLY, ZERO ROWS — STILL DELIBERATE … The first row lands at reading 2, 2026-09-18". `GPU_INSTRUMENT_SPEC.md:4` reads "ZERO ROWS WRITTEN … First row is reading 2, 2026-09-18". In fact `GPU_SERIES.tsv` has 10 data rows, first written at reading 4 on 2026-10-02. Two sessions passed (10/02, 10/08) without catching it, the first saying explicitly that CLAUDE.md was unchanged. CLAUDE.md is the boot-loaded file, so every boot reads a false instrument state. (VULCAN fixed the same class on 9/06 in `7a0a32ffc`: "surviving in the one file that auto-loads at every boot".)
- **F-B 🔴 A VULCAN fact reached a FINAL trade card wrong, and was self-corrected six days later.** The 10/02 starter to TERRY said ORCL and MU are the direct AI-debt names in QQQ, and the answer is backwards: CRWV is in the Nasdaq-100 and ORCL is not. TERRY folded it into L590 FINAL (`76c75516b`). The correction landed 10/08 (`TERRY/inbox/processed/2026-10-08_from-VULCAN_QQQ-membership-correction-and-ask-closed.md:5-9`, L-41, KB-202). It was self-caught, not outside-caught, so FLEET_MAP's "no outside-caught defect" leg survives. It is still the first VULCAN defect since 9/05 to reach a trade surface, and the source was a fact relayed from memory.
- **F-C 🟠 EXIT_PROTOCOL freshness header regressed** (C16): `:3` says "Newest entry: 2026-10-01" with a 10/08 entry at `:140`. This repeats a PR#6 finding VULCAN fixed on 9/25.
- **F-D 🟠 TRADE.md false-state, not just stale** (C17). It is carried as "not touched" across 3 sessions under a miscounted age (36 vs 42 days).
- **F-E 🟠 Consumption evidence rotated out from under the Conf-H citation** (C5, C9, C10, C12). The gate is still met through NEXUS, HENRY, TERRY and PROME, but the profile's four named citations are half gone and WATT and VIOLET are dark with VULCAN packets unconsumed. Confidence H should be re-based on today's readers, not carried.
- **F-F 🟡 DAEDALUS-side carried items:** F-1 tripwire candidate lapsed at 9/12 and again at PR#7 10/01 (C21). PR#7's 10/01 re-score was never packeted, so `VULCAN/STATUS.md:5` says "Last_scored 2026-09-17" (C13): the same propagation class DAEDALUS recorded against itself at PR#6.
- **F-G 🟡 Attendance is the binding L5 constraint**, not quality. Two dark windows (12 days and 5 days) after a WEEKLY declaration. The 10/05 L250 decision was taken 3 days late, though it was pre-written, so the late application could not move the answer (§7a byte-unchanged).
- **Strength, recorded so the review is not uniformly damning:** pre-registration discipline is fleet-grade (resolver sheet and §7a both byte-verified frozen). Rotations are verbatim and crc-true (two crcs verified by me: NEXUS_BRIEF `0xadc7bff2` = `274dfcf12^`; STATUS → CHANNEL_DETAIL §E `0x02b4969e` = `193ed19e7^`). The desk refuted a WALTER correction at the primary (`db3d4ae2b`) and caught a fleet cc-delivery gap (`892dda92a`).

### Hypotheses I held and that were REFUTED (recorded per UPGRADE_PROTOCOL)
- *Expected the MU grade to be recorded only in STATUS/PREDICTIONS:* REFUTED. It is on six surfaces, including PROME DOCKET L547 RESOLVED.
- *Expected the resolver to have been touched above §6 after the print:* REFUTED by the git diff (2 hunks, banner and §6 only).
- *Expected §7a to have been edited after 10/05:* REFUTED (byte-identical apart from the appended §7b).
- *Expected F-2 (S4 monthly freshness) still open:* REFUTED. The Aug and Sep rows landed on cadence.

## 7. NOT-READ (coverage limits)

- **Commit diffs read in full:** only `00a13c4c1` (EXIT_PROTOCOL hunk), `bbd75b2e7` (resolver hunks via diff), `98d815913` (§7a block). All other 105 commits were read as **messages and stat only**, and the 9/06 `eafe981e4` and `892dda92a` messages were truncated in my dump past ~40 lines.
- WALTER-authored commits (41): subjects only. The **56 WALTER signals** processed since 9/05 (`inbox/WALTER/processed/`) and `board_log.tsv` dispositions are **not read**; I did not verify per-signal disposition, only that each file moved.
- `reports/` since 9/05 (5 files: 9/25 ×4, 9/29 ×1): names only, **bodies not read**.
- `archive/` bodies: headers only for `STATUS_ARCHIVE_2026-09.md`. Not opened: `SCRATCH_ARCHIVE_2026-09.md`, `CATALYSTS_FIRED_2026-09/10.tsv` + READMEs, `EXIT_PROTOCOL_LOG_ARCHIVE_2026-10.md`, `NEXUS_BRIEF_ARCHIVE_2026-09.md` (crc checked only), `PREDICTIONS_RESOLVED_2026-09.tsv`. crcs not checked for the PREDICTIONS split (`0xc3603220`), SCRATCH rotations, the EXIT log archive or CATALYSTS_FIRED (`0xed0ccdc9`).
- Not read in full: `THESIS.md`, `CHANNEL_DETAIL.md`, `NEXUS_BRIEF.md`, `LESSONS.md` (headings L-29..L-42 only), `KB.tsv` (row count only; KB-150..203 bodies unread), `GPU_INSTRUMENT_SPEC.md` (§ headings, `:4`, `:278-281`, §7a diff only), `CLAUDE.md` (grep + `:237-267` cell heads; `:259` read).
- Not run: `boot.py`, `validate_workbook.py`, `test_validate_workbook.py`, `gpu_panel.py --selftest`, `corrections_boot_check.py VULCAN`, `claim_check`. Desk validation claims ("11 ledgers conform", "selftest PASS", "31/31") are **taken from commit messages and not executed** (the outward-guard rule is unapplied here).
- Peer artifacts: only the STATUS lines cited plus inbox listings. No peer git history was traced for the VIOLET/ZHAO attribution drop (§5 Q3). The answer content of the WATT 9/06b packet was not read (§5 Q2).
- Not checked against `AGENTS/_NETWORK.md`, `PROME/ROSTER.md` or VULCAN's `registry/corrections_receipts.tsv`.
- Slices V1 and V2 (`VULCAN_REFRESH_2026-10-08_READER_V1.md`, `_V2.md`) exist beside this file and were **not read**, deliberately; this slice is independent.

---
*Slice closed Thu Oct  8 16:48:18 EDT 2026 (read-only; this file is the only write).*
