# Falsification Freshness Sweep #4 — NEGATIVE-RESOLUTION leg (non-owner reader)

**Reader:** non-owner reader for DAEDALUS · **Opened:** 2026-10-08 16:15 ET (Thu, `date`) · **Closed:** 2026-10-08 16:26 ET (`date`) · **Status:** COMPLETE for this leg; dispositions are DAEDALUS's (packet-only per playbook).
**Canon:** `FORGE/PREDICTION_DISCIPLINE.md` § Grading & re-marking, bullet "Negative resolutions require a dated search attempt" (ratified Will 2026-08-17, row 52③; binds at registration: "name the search instrument in the spec alongside the resolve date") + WQ-172 amendment (Will 2026-09-03, forward-only: the attempt must fall INSIDE the window, floor and ceiling = resolve date; no author-activity limb). **Playbook:** `sweeps/FALSIFICATION_SWEEP.md` § "NEW LEG for run #2". **Prior run:** `runs/2026-09-17_FALSIFICATION_SWEEP_03.md` §4 + readers `upgrades/PRODUCTION_REVIEW_2026-09-17_READER_R{1..6}*.md` §6.
**Rules held:** read-only on the repository except this file; no commits, no messages, no subagents; no ledger edited. Scratch scripts and dumps live in the session scratchpad only.

---

## §0 Headline

| Measure | Run #3 (2026-09-17) | Run #4 (2026-10-08) | Population / command |
|---|---|---|---|
| OPEN rows | ~254 **rows opened by readers** (not the OPEN population — see §5 L1) | **155** OPEN-class rows in 38 of 41 ledgers | §1 parse: status token ∈ {OPEN…, ACTIVE, TRACKING…, STRENGTHENING, WEAKENING, ⚠ DUE-UNRESOLVED} |
| Negative-class | ~70 | **44** (30 NEG-E open-perimeter absence · 14 NEG-S register/level persistence) | judgment read of all 155 rows, definition §1.3 |
| Lacking a named search instrument | ~22 (+1 lacking only a dated window) | **17** = 10 with NONE + 7 PARTIAL/IMPLIED | §2 column "Instrument" |
| Lacking a dated search (window open) | (merged into the 22) | **8** with no dated search/read of the source in-row since 2026-08-09 (≥60 d) + **3** in-window reads OVERDUE or imminent + **1** post-canon row (FAL-06) with no dated-attempt clause | §2 column "Dated search" |
| Past-due, still OPEN, negative, ungraded | not measured | **1** — MARCO/BORDER `BDR-01` (resolve 2026-04-30, **161 days** past, no instrument, no search) | ISO resolve-date ≤ 2026-10-08 + prose-timeframe read |
| Run #3 desks still carrying the lack | 8 desks (+FALCON window; OZK also lacking in R6) | **6 of 10** (BROCK 5, REGINALD 3, AEOLUS 1 partial, HANS 1, OTTO 1 partial + 2 dated-stale, FALCON 1 on the successor row); **4 clear** (CORAL and OZK by repair; ZHAO and CREED by resolution, not repair) | §3 |

**Three findings that matter more than the counts:**
1. **The ask was never sent to 3 of the 9 owners run #3 names.** Run #3 §6 lists "negative-resolution rows: BROCK · CREED · ZHAO · HANS · …", but the ZHAO and HANS PR#6 packets carry **no** negative-resolution ask (`AGENTS/ZHAO/inbox/processed/2026-09-17_from-DAEDALUS_PR6-…md` ASK 1–2 and `AGENTS/HANS/inbox/processed/2026-09-17_from-DAEDALUS_PR6-…md` ASK 1–2 are both about VX/CATALYSTS/STATUS), and **CREED received no PR#6 packet at all** (no 2026-09-17 DAEDALUS file in `AGENTS/CREED/inbox/` or `processed/`). HNS-09 is therefore still un-instrumented with no owner ever asked. This is a DAEDALUS-side delivery defect (PAT-050 self-inclusion).
2. **"Processed" is not "done" — 2 of 7 asked desks filed the packet and did not execute the ask, with no deferral on record.** BROCK moved its packet to `processed/` in `8a6cbcc93` (2026-09-18, "inbox drained"); ask 3 ("add an `Instrument` column … fill the 5 negative-branch rows, by 2026-09-30") is unexecuted — header `AGENTS/BROCK/workbook/PREDICTIONS.tsv:1` unchanged and the only ledger commit since 9/17 is `0f2ef30b3` (BRK-02 resolve). REGINALD's ask 2 (instrument the 3 negative rows by 9/30) is likewise unexecuted; `STATUS.md:91` defers REG-03/REG-07 to the Q3 print and is silent on REG-06.
3. **The FALCON gap propagated to the successor.** Run #3 asked FALCON to add a dated search window to FAL-05. FAL-05 FAILED instead — graded 2026-09-28 but "failed IN FACT by 2026-09-17, i.e. graded 11 days late" (`AGENTS/FALCON/thesis/PREDICTIONS.tsv:30`). Its successor **FAL-06** (registered 2026-10-01, after both the 8/17 convention and WQ-172) names its instruments but again carries **no dated search floor/ceiling** (`:31` Invalidation: "CONFIRMED if no route fires by 2026-11-05 23:59 ET"). An in-window search schedule is exactly what would have caught FAL-05's fire on time.

---

## §1 Population

### §1.1 Included — 41 ledgers
Command: `ls AGENTS/*/workbook/PREDICTIONS.tsv AGENTS/*/thesis/PREDICTIONS.tsv AGENTS/*/sub_agents/*/workbook/PREDICTIONS.tsv` → **39** files, plus two declared non-standard prediction ledgers found via `AGENTS/*/workbook/LEDGER_GLOB` and a `find AGENTS -iname '*predict*'` sweep: `AGENTS/YURI/workbook/INTENT_LEDGER.tsv` (OPEN/HIT/MISS/VOID rows) and `AGENTS/TERRY/CALIBRATION.tsv` (pre-registered probability calls) → **41**.

Desks covered: AEOLUS · BOND · BRENT · BROCK · CARL (+ DOC, GIG, PHAN, POLLY, POP subs) · CREED · CRUISE · FALCON · FERT · FLG · HANS · HAWK · HENRY · HOMER · LABOR · LIQUID · MARCO (+ BORDER, HOUSING, MIGRATION, TOURISM, WORKFORCE subs) · MIDAS · OSPREY · OTTO · OZK · RED · REGINALD · SAM · TERRY · VIOLET · VULCAN · WAL · WATT · YURI · ZHAO.

### §1.2 Excluded, with reason
| Excluded | Reason |
|---|---|
| `AGENTS/BRENT/research/2026-09-15_*/before/thesis/PREDICTIONS.tsv` (2) | historical snapshots of BRENT's ledger |
| `*_ARCHIVE.tsv` / `*_ARCHIVE.md` (BROCK, WATT, BRENT, FALCON, HAWK, OSPREY, OTTO, SAM) | resolved/archived rows |
| `AGENTS/CARL/PREDICTIONS_MIRROR.md` | mirror of `CARL/thesis/PREDICTIONS.tsv` (double count) |
| `AGENTS/NEXUS/PREDICTIONS_MONITOR.md` / `PREDICTIONS_COLD.md` | monitor of other desks' rows, not a ledger of its own |
| `AGENTS/SAM/docket/PREDICTION_SCHEDULE.json`, `research/outputs/…/prediction-rows-frozen.json` | schedule / frozen copy |
| ORACLE (`ODDS_LOG`, `KALSHI_ODDS_LOG`, …) | market-odds logs, not desk forecasts (its `LEDGER_GLOB` declares no prediction ledger) |
| SHADE | no forecast ledger exists (run #3 R5 also NOT-SEEN) |
| CORAL `workbook/FL_Forward_Log.md` + `thesis/THESIS.md` falsify table | event calendar / criterion table, not a row ledger; read ONLY for run #3 follow-through (§3) |
| All `KB.tsv` / `FLOW.tsv` / `VX*.tsv` / `SCHEMA.tsv` that carry an OPEN token (`grep -rlP '\t(OPEN|ACTIVE|…)\t' AGENTS --include='*.tsv'`, ~60 files) | observation / vector / schema ledgers, not forecasts |
| DAEDALUS `sweeps/REGISTRY.tsv` | deadlines, not predictions (run #3 R1 same call) |

### §1.3 OPEN count and the classifier
- **OPEN-class = 155 rows** (parse of each ledger's `Status` column; tokens counted: `OPEN*`, `ACTIVE`, `TRACKING*`, `STRENGTHENING`, `WEAKENING`, `⚠ DUE-UNRESOLVED`). 38 ledgers hold ≥1; BOND (2 TRUE), VIOLET (6 terminal incl. `HELD`/`HELD_WITH_DEFECT`), TERRY (2 graded) hold 0. Not counted: OTTO-10 `NEEDS_VERIFY` (a held FALSIFIED grade under investigation); MARCO/TOURISM TOUR-02/TOUR-04 (6-field malformed rows whose cells read RESOLVED).
- Per-ledger OPEN counts: AEOLUS 8 · BRENT 3 · BROCK 12 · CARL 13 + DOC 9 + GIG 5 + PHAN 5 + POLLY 8 + POP 5 · CREED 3 · CRUISE 1 · FALCON 1 · FERT 1 · FLG 3 · HANS 3 · HAWK 2 · HENRY 1 · HOMER 1 · LABOR 5 · LIQUID 2 · MARCO 4 + BORDER 4 + HOUSING 3 + MIGRATION 4 + TOURISM 4 + WORKFORCE 4 · MIDAS 2 · OSPREY 1 · OTTO 7 · OZK 4 · RED 2 · REGINALD 4 · SAM 2 · VULCAN 5 · WAL 2 · WATT 4 · YURI 2 · ZHAO 6 = **155**.
- **Classifier (read, not keyword):** every one of the 155 rows read (Prediction + resolution/invalidation/criteria + notes); negative candidates re-read whole with targeted extraction of instrument/search/date clauses. A row is **negative-class** if a SCORED outcome depends on establishing that something did NOT happen / was NOT published / did NOT change inside a window:
  - **NEG-E (open-perimeter absence):** the absence must be established across actors, filings or announcements not reducible to one register ("no SEC enforcement filing", "no shelf halts", "no circular removes the area") — the convention's core target.
  - **NEG-S (single-register persistence):** the letter asserts a level/state persists or is not crossed on one register ("does NOT close ≥4.00%", "stays >10%") — instrument = the register; lower risk, still needs a dated read.
  - **NOT counted:** positive threshold or event claims whose FALSE branch is merely "didn't cross" on one named series or scheduled publication (e.g. CREED-001/002 on Trepp, BRK-22 ARCC dividend, SAM-42 BOJ rate, LIQ-04, CRL-28, ZHA-01/07). Counting them would make nearly every row negative. Boundary calls are listed in §5 L3.

---

## §2 Instances — all 44 negative-class OPEN rows

Instrument: **NAMED** = a specific source/feed/query in the row · **PARTIAL** = form named, venue/universe or threshold not · **IMPLIED** = only the obvious issuer · **NONE**. Dated search: latest dated search/read of the source recorded IN THE ROW (owner surfaces checked where noted). ⚑ = carries a lack.

| # | Desk | Row · file:line | Class | Resolve | Instrument | Dated search | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | AEOLUS | AEO-03 · `AEOLUS/workbook/PREDICTIONS.tsv:4` | NEG-S (stays soft, ROL ≤+5%) | 2027-01-15 | ⚑ **NONE in row** ("Jan'27 property-cat ROL ≤ +5% YoY" — whose ROL?). Proxy SEARCH instrument (Artemis cat-bond spread) + dated attempt 2026-09-28 20:02 EDT live only in `DAEDALUS/inbox/processed/2026-09-28_from-AEOLUS_AEO-03-search-instrument-PR6.md`; resolving instrument (Guy Carpenter Jan-1 ROL) PROPOSED, `AEOLUS/STATUS.md:135` | proxy 9/28 (out of row) | ⚑ lacking resolving instrument |
| 2 | AEOLUS | AEO-08 · `:9` | NEG-E (FALSE = no PJM Cold Weather Alert posting DJF) | 2027-03-01 | NAMED (PJM Inside Lines / emergency-procedure log) | window not open | OK |
| 3 | AEOLUS | AEO-09 · `:10` | NEG-E (FALSE = TX/OK never removed in any NIFC issuance 10/01–12/01) | 2026-12-01 | NAMED (NIFC monthly outlook, regional section governs) | ⚑ **10/01 issuance in-window read OVERDUE** — self-flagged `AEOLUS/STATUS.md:126` "🔴 OVERDUE — not read 10/8" | ⚑ in-window read owed |
| 4 | AEOLUS | AEO-10 · `:11` | NEG-S (Mead not ≤1,035 ft) | 2026-12-31 | NAMED (USBR 921/49 daily) | 2026-09-27 | OK |
| 5 | AEOLUS | AEO-12 · `:13` | NEG-E (FALSE = no ACP advisory ≤47.0 ft) | 2027-04-30 | NAMED (numbered ACP Advisory; search-then-fetch; index forbidden) | window opens 2027-01-01 | OK — exemplary |
| 6 | BRENT | BRT-30 · `BRENT/thesis/PREDICTIONS.tsv:43` | NEG-E (no circular ≥JWLA-035 removes either area) | 2026-10-26 | NAMED (JWC Listed Areas, circular number as detector) | read at 10/26 per letter | OK |
| 7 | BROCK | BRK-11 · `BROCK/workbook/PREDICTIONS.tsv:7` | NEG-E (FALSE = no BDC breaches 150%) | 2026-12-31 | ⚑ NONE (no filing set/feed; 8/28 BCRED 10-Q is evidence, not an instrument) | 2026-08-28 | ⚑ instrument |
| 8 | BROCK | BRK-18 · `:13` | NEG-E (Invalidation "No GPU failure rate data published") | 2026-12-31 | ⚑ NONE | ⚑ **2026-06-08** ("6/8 sweep") — 122 d | ⚑ instrument + stale |
| 9 | BROCK | BRK-25 · `:18` | NEG-E (FALSE = no arms-length <90¢ trade) | 2026-12-31 | ⚑ NONE ("NO-PRINT-EXIT COUNT" kept, no venue) | 2026-08-28 | ⚑ instrument |
| 10 | BROCK | BRK-26 · `:19` | NEG-E (FALSE = "no enforcement action by Dec 31") | 2026-12-31 | ⚑ NONE (no EDGAR litigation-release / SEC admin-proceedings feed named) | 2026-08-28 (prose) | ⚑ instrument |
| 11 | BROCK | BRK-31 · `:22` | NEG-E (FALSE = 11 named banks, no PC/NDFI attribution) | 2027-01-31 | NAMED (the 11 banks' Q3/Q4 prints) | 2026-09-03 | OK |
| 12 | CARL/PHAN | PHAN-P03 · `CARL/sub_agents/PHAN/workbook/PREDICTIONS.tsv:42` | NEG-E (no 1033 enforcement in 2026) | 2026-12-31 | NAMED (CFPB rule 1033 compliance date / docket) | 2026-09-10 | OK |
| 13 | CARL/PHAN | PHAN-P04 · `:43` | NEG-E (12% ⇒ modal = <2 new failures) | 2026-12-31 | ⚑ PARTIAL ("company/regulatory filings"; COCKROACH.tsv is the ledger the null is recorded in, not a source) | 2026-09-10 (explicit DID_NOT_APPEAR null) | ⚑ instrument |
| 14 | CARL/PHAN | PHAN-P05 · `:44` | NEG-E (15% ⇒ modal = not identifiable) | Q4 2026 | NAMED (FHA Mortgagee Letters / HUD final guidance) | 2026-09-10 SEARCH-NOT-FOUND | OK |
| 15 | CARL/PHAN | PHAN-P07 · `:46` | NEG-E (FALSE = <5 states' AG enforcement) | 2026-12-31 | ⚑ PARTIAL ("state AG actions"; count rests on Natl Law Review / Mondaq secondaries) | 2026-09-10 | ⚑ instrument |
| 16 | CARL/POLLY | POLLY-P03 · `CARL/sub_agents/POLLY/workbook/PREDICTIONS.tsv:5` | NEG-S (Citizens remains <400K) | Q4 2026 | NAMED (citizensfla.com PIF) | 2026-08-10 | OK |
| 17 | CARL/POLLY | POLLY-P07 · `:9` | NEG-S (no meaningful re-entry; <50K net new) | Q4 2026 | ⚑ PARTIAL (CA DOI rank named; the <50K leg has no source) | ⚑ none dated since registration 2026-04-09 | ⚑ instrument + stale |
| 18 | CARL/DOC | DOC-P08 · `CARL/sub_agents/DOC/workbook/PREDICTIONS.tsv:9` | NEG-S (healthcare remains #1 worry) | Nov 2026 | NAMED (KFF monthly tracking poll) | ⚑ none dated since 2026-04-09 | ⚑ stale |
| 19 | FALCON | FAL-06 · `FALCON/thesis/PREDICTIONS.tsv:31` | NEG-E (no NET Gulf-ally crude loss 10/01–11/05) | 2026-11-05 | NAMED (operator/state FM, stated capacity offline, Kpler/Vortexa weekly) | ⚑ **no dated search floor/ceiling clause** (registered 10/01, post-WQ-172) | ⚑ dated-attempt clause |
| 20 | FERT | FERT-12 · `FERT/workbook/PREDICTIONS.tsv:15` | NEG-S (DTN MAP not >$975) | 2026-12-02 | NAMED (DTN weekly, US national avg) | weekly articles | OK |
| 21 | HANS | HNS-08 · `HANS/workbook/PREDICTIONS.tsv:9` | NEG-S (Bund not ≥4.00%) | 2026-12-31 | NAMED (TradingEconomics / Bundesbank daily close; continuous anchor) | continuous | OK |
| 22 | HANS | HNS-09 · `:10` | NEG-S (sector shows NO material rise in cost-of-risk) | 2026-11-30 | ⚑ NONE (no aggregate, publisher or "material" threshold; resolver-drift corrected 9/19) | 2026-09-18 (HANS-T-14, a narrower perimeter) | ⚑ instrument |
| 23 | HAWK | HAW-20 · `HAWK/thesis/PREDICTIONS.tsv:42` | NEG-E (no codification instrument moves DOWN) | 2026-10-31 | NAMED (Federal Register, USTR, CIT/CAFC dockets, Majlis/IRNA, foreign ministries) | required dated pull; none yet in row (window open, 23 d left) | OK — exemplary |
| 24 | HAWK | HAW-22 · `:44` | NEG-E (no NEW disclosed terminal loss) | 2026-12-22 | NAMED + final search 12/15–12/21 | in letter | OK — exemplary |
| 25 | MARCO/BORDER | BDR-01 · `MARCO/sub_agents/BORDER/workbook/PREDICTIONS.tsv:2` | NEG-S (shutdown continues past Day 60) | **2026-04-30 PASSED** | ⚑ NONE | ⚑ none — ledger untouched since 2026-04-18 | ⚑ **PAST-DUE UNGRADED** |
| 26 | MARCO/TOURISM | TOUR-01 · `MARCO/sub_agents/TOURISM/workbook/PREDICTIONS.tsv:2` | NEG-S (2-yr stack stays below −25%) | 2026-12-31 | ⚑ PARTIAL (series named, publisher not) | ⚑ 2026-05-31 — 130 d | ⚑ instrument + stale |
| 27 | MARCO/TOURISM | TOUR-03 · `:4` | NEG-E (no seat restoration to 2025) | 2027-12-31 | ⚑ NONE | ⚑ 2026-05-31 | ⚑ instrument + stale |
| 28 | OSPREY | OSP-06 · `OSPREY/thesis/PREDICTIONS.tsv:17` | NEG-S (no Bloomberg 4-wk ≥3.9 M bpd) | 2026-10-15 | NAMED + SEARCH-ATTEMPT GUARD + VOID path | 2026-10-08 day 1 of 10/8–10/15 obligation (`OSPREY/STATUS.md:43`) | OK — exemplary |
| 29 | OTTO | OTTO-07 · `OTTO/thesis/PREDICTIONS.tsv:6` | NEG-E (15% ⇒ modal = no shelf halts) | 2026-12-31 | NAMED (`scripts/shelf_halt_monitor.py`; own note says EDGAR re-instrument owed) | ⚑ 2026-07-25 — 75 d; no final read scheduled | ⚑ stale |
| 30 | OTTO | OTTO-12 · `:11` | NEG-E (no major warehouse lender exits) | 2026-12-31 | NAMED (EDGAR 8-K 1.01/1.02 for CACC/CPSS/CRMT/VRM + press query; limit stated) | 2026-09-24; ⚑ "NEXT ATTEMPT 2026-10-01" not recorded (7 d) | ⚑ in-window read owed |
| 31 | OTTO | OTTO-31 · `:17` | NEG-E (12% ⇒ modal = no formal wind-down) | 2026-12-31 | ⚑ PARTIAL (WT statement / 10-K, in Invalidation only) | ⚑ 2026-07-25 — 75 d | ⚑ instrument + stale |
| 32 | OTTO | OTTO-33 · `:19` | NEG-E (no new counterparty named) | 2026-12-31 | NAMED (EDGAR FTS monthly, CourtListener, Ch.7 docket; "NOT press monitoring") | 2026-08-27 | OK — exemplary |
| 33 | OTTO | OTTO-35 · `:21` | NEG-E (every SDT run REFUTE/NV) | 2027-06-30 | NAMED (`scripts/severity_divergence.py`) | next run ~11/15 | OK |
| 34 | OZK | OZK-09 · `OZK/workbook/PREDICTIONS.tsv:26` | NEG-E (FALSE resolves by absence after sweep) | ~late Jan 2027 | NAMED (3-leg sweep: `flng_watch.py`, 8-K bundles, 10-Q notes; added 9/24) | precondition: legs executed and dated | OK (repaired 9/24) |
| 35 | REGINALD | REG-01 · `REGINALD/workbook/PREDICTIONS.tsv:3` | NEG-S (office DQ stays >10%) | 2026-12-31 | NAMED (Trepp, REG-T-07) | 2026-08-27 (July 11.91%) | OK |
| 36 | REGINALD | REG-03 · `:5` | NEG-E (FALSE = no recognition wave) | 2026-12-31 | ⚑ NONE ($936B unreconciled, "re-spec deferred") | ⚑ no search for the event ever recorded | ⚑ instrument + stale |
| 37 | REGINALD | REG-06 · `:8` | NEG-E (10% ⇒ modal = both avoid raise) | 2026-12-31 | ⚑ NONE (no 8-K/424B/press scan named) | 2026-08-27 | ⚑ instrument |
| 38 | REGINALD | REG-07 · `:9` | NEG-S (Invalidation: SSB NPLs stay <0.3%) | Q2–Q3 2026 window **closed 9/30**; grades at SSB Q3 print (~late Oct) | ⚑ IMPLIED (SSB quarterly disclosure) | 2026-08-27 | ⚑ instrument; grade owed at print |
| 39 | SAM | SAM-33 · `SAM/thesis/PREDICTIONS.tsv:49` | NEG-E (BOJ does NOT deploy capping ops) | 2026-12-31 | NAMED (BOJ ops files `ope2026MMDD.xlsx`, append-only op-audit) | 2026-09-16 | OK — exemplary |
| 40 | VULCAN | VULCAN-08 · `VULCAN/workbook/PREDICTIONS.tsv:3` | NEG-E (FALSE = 0 of 3 named filers disclose) | 2027-02-15 | NAMED (FY26 10-K / Q1 10-Q of GOOGL/AMZN/META) | window not open | OK |
| 41 | VULCAN | VULCAN-13 · `:7` | NEG-E (REFUTED = none of (a)/(b)/(c) lands) | 2026-11-15 | ⚑ PARTIAL (forms named, "filing-primary"; no venue or borrower universe) | none recorded (registered 8/21) | ⚑ instrument |
| 42 | VULCAN | VULCAN-15 · `:9` | NEG-E (no firm curtailability mechanism enters effect) | 2026-11-15 | NAMED (FERC docket; calendar anchor) | read at 11/15 per letter | OK |
| 43 | WATT | WATT-12 · `WATT/workbook/PREDICTIONS.tsv:5` | NEG-S (MISS = zero ≥$1,000 intervals, coverage proven) | 2026-10-31 | NAMED (DM2 5-min, pnode 1) + 14-day coverage duty | ⚑ last pull 2026-09-25 (`WATT/STATUS.md:33`); feed retains ~15 d (`:77`) ⇒ pull due **≤10/09** or 9/26+ days go ungradeable | ⚑ imminent |
| 44 | YURI | YUR-004 · `YURI/workbook/INTENT_LEDGER.tsv:8` | NEG-E (FALSE = no mobilisation decree) | 2026-10-31 | NAMED (publication.pravo.gov.ru, kremlin.ru; NOT secondary) | 2026-10-02 baseline; weekly 10/09… | OK — exemplary |

**Tallies (from this table):** NEG-E 30 · NEG-S 14 = 44. Instrument NONE 10 (#1, 7, 8, 9, 10, 22, 25, 27, 36, 37) · PARTIAL/IMPLIED 7 (#13, 15, 17, 26, 31, 38, 41) = **17**. Stale dated search (none in-row since 2026-08-09, window open) 8 (#8, 17, 18, 26, 27, 29, 31, 36). In-window read overdue/imminent 3 (#3, 30, 43). Post-canon row with no dated-attempt clause 1 (#19). **Past-due ungraded 1 (#25).** Exemplary forms worth citing as fleet references: AEO-12, HAW-20, HAW-22, OSP-06, OTTO-33, SAM-33, YUR-004.

### §2.1 Item 4 — resolution date TODAY or PASSED, still OPEN, negative
| Row | file:line | Resolve | Days past | Instrument / search | State |
|---|---|---|---|---|---|
| **BDR-01** "DHS shutdown continues past Day 60" | `AGENTS/MARCO/sub_agents/BORDER/workbook/PREDICTIONS.tsv:2` | 2026-04-30 | **161** | NONE / none | `ACTIVE`; ledger last commit 2026-04-18; **ungraded** |

Command: ISO resolve-date parse over the 155 rows (`resolve_date|resolve_by|resolution_date|resolves_on|timeframe` columns) returned 10 rows ≤ 2026-10-08, all MARCO sub-ledgers; BDR-01 is the only negative-class one. Prose-timeframe rows were judged by reading: none negative is past its letter's date. **Closest to the line (not yet past):** REG-07 — its Q2–Q3 data window closed 9/30 and it grades at the SSB Q3 print (~late Oct) on an IMPLIED instrument; OSP-06 resolves 10/15 (7 days; guard live, day-1 search done 10/8).
**Adjacent, outside the negative class (so not in item 4's count):** the other 9 past-date MARCO sub-ledger rows — BDR-02 (5/31), HSG-01 (9/30), HSG-02 (6/30), MIG-01 (6/30), MIG-02 (9/30), MIG-03 (9/30), WF-01 (5/31), WF-02 (6/30), WF-03 (6/30) — all `ACTIVE`, ungraded, in sub-ledgers untouched since 2026-04-18 (TOURISM 2026-06-01), with no FROZEN banner; and CARL/GIG GIG-P03/GIG-P06 `⚠ DUE-UNRESOLVED [DATA-NEEDED] 2026-08-10` (positive thresholds; the named instrument (Gridwise) publishes only annually).

---

## §3 Run #3 desks — follow-through (git log since 2026-09-17 on each ledger)

Command per desk: `git log --since=2026-09-17 --format='%h %ad %s' -- <ledger>`; packet check: `find AGENTS/<D>/inbox -iname '*2026-09-1[7-9]*DAEDALUS*'` + grep of the packet's ASK lines.

| Desk | Run #3 rows lacking | Ask in the 9/17 packet? | Ledger commits since 9/17 | Run #4 state | #3 → #4 |
|---|---|---|---|---|---|
| BROCK | 5 (BRK-26, -25, -18, -11, -04) | YES — ASK 3: `Instrument` column + fill 5 rows by 9/30 | `0f2ef30b3` 10/02 (BRK-02 resolve only) | **NOT DONE**; packet filed `processed/` in `8a6cbcc93` 9/18, no deferral found in `STATUS.md`. Schema unchanged (`:1`). BRK-04 now classed by this reader as a level read (out of class) but still has no source | **5 → 5** (4 in class + BRK-04) |
| CREED | 6 (002, 004, 005, 007, 008, 010; dated-search half) | **NO PACKET DELIVERED** | `72303435c` 9/26 … `c36124db1` 9/29 | 004 RESOLVED-TRUE 9/28 · 005 RESOLVED-TRUE 9/29 (8-K Item 5.07) · 007 RESOLVED-TRUE 9/28 · 010 RESOLVED-PARTIAL (not scored, Will 9/29) · 002, 008 OPEN — both positive threshold reads on named instruments (Trepp; KREF 10-K), out of class by this reader's definition | **6 → 0 by resolution, not repair** |
| ZHAO | 1 (ZHA-16, venue unnamed) | **NO** — packet ASKs 1–2 are CATALYSTS/VX | `dd6661e99` 9/30 | ZHA-16 RESOLVED NO 9/30 at window close on the MOFCOM 9/28 statement (named at grade) | **1 → 0 by resolution** |
| HANS | 1 (HNS-09) | **NO** — packet ASKs 1–2 are VX/STATUS | 9 commits 9/18–10/01 | HNS-09: dated sweep added 9/18, resolver-drift corrected 9/19; **aggregate / publisher / "material" threshold still unnamed** | **1 → 1** |
| CORAL | 2 (crit 5, crit 6) | YES — ASK 2 by 9/30 | `496403f3b`, `8ce8ecb83`, `4661cb048` (THESIS, 9/28) | crit 5: instrument BUILT (`tools/bkcy/`, AOUSC F-2, Will-ruled WQ-321 scoring at `thesis/THESIS.md:129-132`) · crit 6: instrument named + search dated 2026-11-04 (FL Division of Elections certified Ballot No. 3) at `STATUS.md:117` — **DONE**. Housekeeping: the grade-table cells `THESIS.md:115-116` still read "Instrument note owed" / "ruling still unlocated" beside the new rule; `workbook/FL_Forward_Log.md:16` Ocala row ⏳ Pending since 7/29, file untouched since 2026-07-23 | **2 → 0** |
| AEOLUS | 1 (AEO-03) | YES — ASK 1 by 9/30 | `a173cfb6b` 9/18, `250f83ad1` 9/28 (neither touches AEO-03) | Proxy search instrument + dated attempt 9/28 delivered to DAEDALUS (packet in DAEDALUS `inbox/processed/`); resolving instrument PROPOSED, not entered (`STATUS.md:110,135`; `inbox/processed/2026-10-08_from-AEOLUS_PR7-dispositions.md:5`) | **1 → 1 (PARTIAL; owner acted)** |
| REGINALD | 3 (REG-03, -06, -07) | YES — ASK 2 by 9/30 | `d3a60d512` 10/07 (inbox drain) | **NOT DONE** — no instrument on any of the three; `STATUS.md:91` defers REG-03 re-spec + REG-07 re-mark to the Q3 print; REG-06 unmentioned | **3 → 3** |
| OTTO | 1 instrument (OTTO-12) + 3 dated-search (OTTO-07 partial, -31, -12) | YES — ASK 2 (OTTO-12 only) by 9/24 | `9df77c858` 9/24 … `3f488b4e1` 9/30 | OTTO-12 **DONE** 9/24 (instrument + dated attempt), but its own "NEXT ATTEMPT 2026-10-01" is unrecorded · OTTO-07 / OTTO-31 unchanged since 7/25 (not in the packet) | **instrument 1 → 1 (OTTO-31 partial) · dated 3 → 2 (+1 owed read)** |
| OZK (R6, not in run #3's 8-desk list) | 1 (OZK-09) | YES — ASK 1 | `c46016675` 9/24 ("OZK-09 guard") | **DONE** — negative-branch 3-leg sweep instrument + dated precondition | **1 → 0** |
| FALCON (window only) | 1 (FAL-05 dated window) | YES — ASK 1 by 9/24 | `0cab6ab47` 9/28, `437af2327` 10/01 | FAL-05 FAILED 9/28 (graded 11 d after the fact); successor FAL-06 has **no dated-attempt clause** | **1 → 1 (on the successor)** |

**Roll-up (row-level, 22 of run #3's 22 + 1 accounted; R6's third lacking row is not named in R6 §6 and is not traced):** **11 still lacking** on the same or successor row (BROCK 5 incl. BRK-04 · REGINALD 3 · AEOLUS 1 partial · HANS 1 · FALCON 1 on FAL-06) · **4 repaired** (CORAL crit 5 + crit 6, OTTO-12, OZK-09) · **5 left by resolution** (CREED-004/-005/-007/-010, ZHA-16) · **2 still OPEN but re-classed out** by this reader (CREED-002, -008 — positive threshold reads on named instruments; run #3's lack on them was the dated-search half, and CREED-002's in-row notes still show only the June read). Of the 7 desks that actually received the ask: **3 executed** (CORAL, OTTO, OZK), **1 partial** (AEOLUS — acted, resolving instrument still PROPOSED), **2 did not** (BROCK, REGINALD — both past their 9/30 date with no recorded deferral), **1 overtaken** (FALCON — gap reappeared on the successor). The 3 desks never asked (CREED, ZHAO, HANS) cleared 2 of 3 only because the rows resolved.

---

## §4 Per-owner asks (one line each; DAEDALUS packets them — nothing sent by this reader)

| Owner | Ask |
|---|---|
| BROCK | Name a search instrument in-row for BRK-11 / BRK-18 / BRK-25 / BRK-26 (e.g. EDGAR 10-Q/N-CSR coverage set, SEC litigation-release + admin-proceedings feed) with a dated attempt before 12/31 — the 9/17 ask 3 (due 9/30) is unexecuted and was filed `processed/` on 9/18 with no deferral; BRK-18's last search is 6/8. |
| REGINALD | Name instruments for REG-03 (source for the "wave" + reconcile $936B) and REG-06 (8-K / 424B / press-release scan for EGBN + WAL), and name the SSB Q3 line REG-07 grades on before that print (~late Oct) — 9/17 ask 2 (due 9/30) unexecuted. |
| AEOLUS | Enter AEO-03's resolving instrument (Guy Carpenter Jan-1 US property-cat ROL, or a named alternative) in `Resolution_Criteria` prospectively before the Jan-1 renewal; read the overdue 10/01 NIFC issuance for AEO-09. |
| HANS | Name HNS-09's aggregate (bank set or publisher), cost-of-risk series and the "material" threshold before Q3 results open (~late Oct) — never asked in run #3 (DAEDALUS defect). |
| FALCON | Add a dated search floor/ceiling (WQ-172) to FAL-06 before 11/05 — the FAL-05 gap carried into the successor, and FAL-05's fire was graded 11 days late. |
| OTTO | Record the OTTO-12 attempt the row scheduled for 2026-10-01 (or say it did not run); put a dated in-window read on OTTO-07 (EDGAR re-instrument owed by its own note) and OTTO-31 (last read 7/25). |
| VULCAN | Name VULCAN-13's search venue and borrower/facility universe for legs (a)/(b)/(c) and log a dated sweep before 11/15 — REFUTED is an open-perimeter absence. |
| CARL (PHAN / POLLY / DOC subs) | PHAN-P04/P07: name primaries (failure filings; state-AG press/court dockets), not COCKROACH.tsv or secondaries · POLLY-P07: a source for the <50K leg + a dated read · DOC-P08: a dated KFF read (none since 4/09). |
| MARCO | Grade or VOID BDR-01 (161 days past, no instrument), and freeze-banner or grade the 4 sub-ledgers carrying 9 more past-date `ACTIVE` rows; name instruments + dated reads for TOUR-01 / TOUR-03. |
| WATT | Run the WATT-12 coverage pull by 2026-10-09 (last 9/25; ~15-day feed retention) or the 9/26+ days become ungradeable. |
| CORAL | Housekeeping only: the `THESIS.md:115-116` grade cells still say "instrument note owed / ruling unlocated" beside the installed rule; `FL_Forward_Log.md:16` Ocala ⏳ since 7/29. |
| DAEDALUS (self) | Run #3 §6 named CREED / ZHAO / HANS as negative-resolution owners, but no packet carried the ask (ZHAO, HANS) or no packet existed (CREED) — correct the run #3 record and send the HANS ask; add "packet carries every §6-named ask" to the sweep's write-back check. |

---

## §5 Limits

- **L1 — Run #3 → #4 is not like-for-like on the denominator.** Run #3's "~254 OPEN rows" summed the rows its six readers OPENED as candidates (R2: 3+1+2+15+13+8 = 42 = its cohort row), across a different ledger set, by six readers with different classifiers (R2 counted FALSE-branch absences on named series — CREED-001/002/008 — that R4 and this reader exclude as "benign level negatives"). The 70 → 44 and 22 → 17 moves are partly definitional. §3 is the like-for-like comparison (same rows, re-measured).
- **L2 — One reader, one classifier.** The NEG-E / NEG-S / excluded line is a judgment, stated in §1.3. A second reader could reasonably move BRK-04, BRK-22, SAM-42, ZHA-07, LIQ-04, CRL-28, CREED-001/002/008, VULCAN-10, POLLY-P05 into the class (all have a FALSE branch read off one register); none of them would add a past-due row.
- **L3 — Dated-search reads are in-row only, except where named.** Owner surfaces were checked for AEOLUS, OTTO, OSPREY, WATT, CORAL, REGINALD, BROCK (STATUS) only. A dated read logged in another desk's STATUS / research file would be missed — the 8 "stale" rows may overstate.
- **L4 — First-pass cells truncated at 600 characters;** all 44 negative-class rows were re-read through targeted full-cell extraction of instrument / search / date clauses, not page-by-page.
- **L5 — Status-token parse.** VIOLET `HELD` / `HELD_WITH_DEFECT` read as terminal; OTTO-10 `NEEDS_VERIFY` excluded; GIG `⚠ DUE-UNRESOLVED` included in OPEN. ISO resolve-date parse only covers ledgers with a date column; prose-timeframe rows were judged by reading.
- **L6 — Scope.** The other §-legs of sweep #4 (scanner STALE flags, F1/F5 buckets) are not covered here (see `runs/2026-10-08_FALSIFICATION_SWEEP_04_FLAGS.md`). No ledger edited, nothing sent; asks in §4 are proposals for DAEDALUS to packet.
- **L7 — Live events seen in passing, not assessed:** WALTER `d5f3fb70d` (10/8) "OZK cause found → SIG-W-20261008-017 (RaDD bridge to Fri 10/9)" may bear on OZK-09's FALSE branch; OSPREY notes a 9/28 Russian decree restricting export-data publication (`OSPREY/STATUS.md:17`) — an instrument risk for Russia-flow rows, not for OSP-06's Bloomberg tanker-tracking series as written.
