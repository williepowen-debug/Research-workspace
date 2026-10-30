# Falsification Freshness Sweep #5 — NEGATIVE-RESOLUTION leg (non-owner reader R2)

**Reader:** read-only non-owner reader for DAEDALUS · **Opened:** 2026-10-30 12:52 EDT (Fri, `date`) · **Closed:** 2026-10-30 12:59 EDT (`date`) · **HEAD:** `ddb8148bc` · **Run #4 baseline commit:** `0c05cb8ab` (last commit before 2026-10-08 16:30 ET, the close of run #4's reader).
**Method template:** `runs/2026-10-08_FALSIFICATION_SWEEP_04_NEGRES.md` (definitions reproduced: OPEN-class token set §1.3, NEG-E / NEG-S classifier §1.3, Instrument NAMED / PARTIAL / IMPLIED / NONE §2). **Canon:** `FORGE/PREDICTION_DISCIPLINE.md` § Grading, "Negative resolutions require a dated search attempt" (Will 2026-08-17, row 52③) + WQ-172 (Will 2026-09-03).
**Rules held:** the only write is this file. No ledger edited, no commits, no messages. Scripts in the session scratchpad: `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-DAEDALUS/0c20d72d-8077-4bfe-bef2-ef05a9591275/scratchpad/census.py` (census at any git revision via `git show`) and `.../scratchpad/diff.py` (row-level diff between two census outputs).

---

## §0 Headline

| Measure | Run #4 (2026-10-08) | Run #5, run #4's 41 ledgers | Run #5, all 44 ledgers | Change explained by |
|---|---|---|---|---|
| OPEN-class rows | 155 (38 of 41 ledgers) | **161** | **165** (39 of 44) | −22 graded or no-verdict · −4 moved to `STUCK` · +32 new (+4 CYPHER) |
| Negative-class | 44 | **45** | **48** | −6 resolved · +7 new (+3 CYPHER) |
| Lacking a named instrument | 17 | **9** | **9** | −6 treatment · −2 resolved · +0 from new rows |
| Stale dated search (none since 8/31, window open) | 8 | **4** | **4** | −7 reads added · +3 aged past 60 days |
| Past-due, OPEN, negative-class, ungraded | 1 (BDR-01, 161 d) | **0** | **0** | BDR-01 graded 10/10 |
| Run #4 desks still carrying the gap | 6 of 10 | **1 of 6** (BROCK) | — | §3 |
| Asked desks (11) | — | **7 DONE · 1 PARTIAL (CARL) · 3 NOT DONE (BROCK, VULCAN, CORAL)** | — | §3 |

New ledgers since 10/08: GIBBS (10/14, 0 OPEN), CYPHER (10/22, 4 OPEN, 3 negative, all instrumented), ISHM (10/23, 0 OPEN).

**What matters more than the counts:**
1. **The treatment worked where it was delivered, and this time it was delivered.** All 11 run #4 owners got the ask by name (the run #3 delivery defect did not recur). The lacking-instrument fall from 17 to 9 is mostly owner repair (6 rows), not rows aging out. REGINALD, which filed its 9/17 ask without acting, executed all three rows on 10/10.
2. **BROCK is the residue: three asks, zero instrument cells.** BRK-11, BRK-18, BRK-25 and BRK-26 still have no named search instrument; three of them have had no dated search since 8/28 or earlier (BRK-18 since 6/8). They resolve 12/31. The difference from run #4 is that the deferral is now written down: `AGENTS/BROCK/STATUS.md:27` carries it to a 10/31 session.
3. **New rows are registering correctly.** All 10 new negative rows name their instrument at registration, and 7 carry an explicit in-window search date. One form question: FAL-07 schedules its FAILED-branch search on 2027-01-02, after its 12/31 event window (§5).
4. **Past-due today, outside the negative class:** YUR-F01 was graded MISS by DAEDALUS on 10/28, but YURI's ledger row still reads OPEN, 6 days past its resolve date (`AGENTS/YURI/workbook/INTENT_LEDGER.tsv:7`).

---

## §1 Census

### §1.1 Instrument check first: the script reproduces run #4 exactly
`python3 census.py 0c05cb8ab` returns **155 OPEN-class rows in 38 of 41 ledgers**, with every per-ledger count equal to run #4 §1.3 (AEOLUS 8 · BRENT 3 · BROCK 12 · CARL 13 + DOC 9 + GIG 5 + PHAN 5 + POLLY 8 + POP 5 · … · ZHAO 6). The same parser on HEAD is therefore comparable to run #4 on the OPEN count. Token set unchanged from run #4: `OPEN*`, `ACTIVE`, `TRACKING*`, `STRENGTHENING`, `WEAKENING`, `DUE-UNRESOLVED`; `NEEDS_VERIFY` and `HELD*` excluded.

### §1.2 Population at HEAD
- Run #4's 41 ledgers, all still present.
- **New since 10/08 (named separately, not in run #4's population):** `AGENTS/GIBBS/workbook/PREDICTIONS.tsv` (added `08d273fca` 2026-10-14; 0 OPEN), `AGENTS/CYPHER/workbook/PREDICTIONS.tsv` (added `18770981e` 2026-10-22; 4 OPEN), `AGENTS/ISHM/workbook/PREDICTIONS.tsv` (added `080fbc7d6` 2026-10-23; 0 OPEN) → **44 ledgers**.
- **Adjacent, not a ledger:** `AGENTS/REGINALD/registry/PREDICTION_RESOLVE_BY.tsv` (added 2026-10-22) — a resolve-by sidecar for REGINALD's OPEN rows, read by REGINALD's `boot.py`; used here only for §2 dates.
- **New state since 10/08:** four MARCO sub-ledgers (BORDER, HOUSING, MIGRATION, WORKFORCE) now carry `FROZEN 2026-10-10 — not maintained` banners; TOURISM does not. Their rows still hold `ACTIVE` tokens.
- Exclusions unchanged from run #4 §1.2 (snapshots, archives, mirrors, NEXUS monitor, ORACLE odds logs, SHADE none, CORAL criterion table, KB/FLOW/VX ledgers, REGISTRY).

### §1.3 OPEN counts at HEAD
| Population | OPEN-class rows | Ledgers with ≥1 |
|---|---|---|
| Run #4's exact 41 ledgers, run #4 token rule | **161** | 37 of 41 |
| + 3 new ledgers (CYPHER 4) | **165** | 39 of 44 |
| 44 ledgers, excluding the 4 FROZEN-bannered MARCO sub-ledgers (14 `ACTIVE` tokens) | 151 | 35 of 40 |

Row-level (`diff.py`): of run #4's 155, **129 still OPEN**, **26 left** the OPEN class; **36 new** OPEN rows (32 in run #4's ledgers + 4 CYPHER). 129 + 32 = 161; + 4 = 165.

The 26 that left, by HEAD status:
| Bucket | n | Rows |
|---|---|---|
| Graded or terminal | 17 | BRT-30 CONFIRMED · BRK-10, BRK-22 RESOLVED-FALSE · DOC-P02, POP-P03 MISSED · CRL-25 RETIRED · FERT-12 MISS · HEN-46 RESOLVED-NO-VERDICT-AS-WRITTEN · LAB-11 RESOLVED · LIQ-07 RESOLVED-S2 · BDR-01 RESOLVED · OSP-06 CONFIRMED · REG-07 VOID · WAL-02 RESOLVED-INVALIDATED · WATT-10 MISS and WATT-12 HIT (both moved to `WATT/workbook/PREDICTIONS_ARCHIVE.tsv`) · ZHA-18 RESOLVED NO |
| No verdict by instrument | 5 | CARL subs DOC-P07, GIG-P02, GIG-P03, GIG-P04, GIG-P06 → `NO-VERDICT-BY-INSTRUMENT` |
| STUCK (unresolved, out of the token set) | 4 | BRK-32, CRL-21, OTTO-11, ZHA-05 — `STUCK` is canonical (`DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md:86`, "cannot resolve because window/instrument broke"); no ledger held a STUCK row at `0c05cb8ab`. None of the four was in run #4's negative class. |

### §1.4 Negative class and instrument lack at HEAD
Classifier unchanged from run #4 §1.3 (NEG-E open-perimeter absence · NEG-S single-register persistence · positive threshold or event reads whose FALSE branch is "didn't cross" on one named series or one scheduled publication are NOT counted). Applied by reading: (a) all 44 of run #4's negative rows re-located at HEAD; (b) all 36 new OPEN rows read (Prediction + criteria / invalidation / instrument + notes); (c) the 129 carried rows that run #4 did not class negative were NOT re-read (their letters were assumed unchanged; §6 L2).

| Measure | Run #4 (10/08) | HEAD, run #4's 41 ledgers | HEAD, all 44 ledgers |
|---|---|---|---|
| OPEN-class | 155 | **161** | **165** |
| Negative-class | 44 (30 NEG-E · 14 NEG-S) | **45** (35 NEG-E · 10 NEG-S) | **48** (38 NEG-E · 10 NEG-S) |
| Lacking a named instrument | 17 (10 NONE · 7 PARTIAL/IMPLIED) | **9** (4 NONE · 5 PARTIAL) | **9** (CYPHER adds 0) |
| Stale dated search (none since 2026-08-31, window open; owner STATUS checked where named) | 8 | **4** (BRK-11, BRK-18, BRK-25, VULCAN-13 — all four also lack an instrument) | 4 |
| Past-due, OPEN, negative-class, ungraded | 1 (BDR-01) | **0** | 0 |

**New negative-class rows (10; 7 in run #4's ledgers + 3 CYPHER) — every one carries a named instrument:**
| Row · file:line | Class | Resolve | Instrument | Dated search |
|---|---|---|---|---|
| HNS-11 · `AGENTS/HANS/workbook/PREDICTIONS.tsv:12` | NEG-S (France-Germany 10Y does NOT print >200bp) | 2026-12-31 | NAMED (ideal-investisseur daily rows) | continuous register |
| OSP-07 · `AGENTS/OSPREY/thesis/PREDICTIONS.tsv:18` | NEG-E (FAILED = no refinery-class strike row after a pre-registered sweep) | 2026-11-15 | NAMED (`strike_feed.py` + STRIKES.tsv + named confirmers) | pre-registered sweep in letter — exemplary |
| YUR-005 · `AGENTS/YURI/workbook/INTENT_LEDGER.tsv:9` | NEG-E (DECIDED-LAPSE = no act on the complete perimeter) | 2026-11-02 | NAMED (publication.pravo.gov.ru government block, government.ru; NOT secondary) | at resolve |
| YUR-006 · `:10` | NEG-E (DECIDED-NO = no Decree-302 list amendment published by 11/15) | 2026-11-15 | NAMED (pravo presidential block, kremlin.ru acts) | at resolve |
| ZHA-19 · `AGENTS/ZHAO/workbook/PREDICTIONS.tsv:20` | NEG-E (NO = no Federal Register document in window) | 2026-11-10 | NAMED (federalregister.gov + public-inspection desk; STUCK if unreachable 11/10 and 11/11) | dated by the STUCK clause |
| ZHA-20 · `:21` | NEG-E (NO = no MOFCOM 公告 in window) | 2026-11-11 | NAMED (mofcom.gov.cn 公告 list; STUCK if unreachable) | dated by the STUCK clause |
| FAL-07 · `AGENTS/FALCON/thesis/PREDICTIONS.tsv:37` | NEG-E (FAILED = no confirmed US strike on Iran 10/22–12/31) | 2026-12-31 | NAMED (CENTCOM / DoD / White House or two independent wires) | ⚑ "graded by the 2027-01-02 dated search" — two days AFTER the event window; see §5 |
| CYP-02 · `AGENTS/CYPHER/workbook/PREDICTIONS.tsv:6` | NEG-E (MISS = no confirmed US bank compromise tied to the wave vectors) | 2027-01-31 | NAMED (EDGAR Item 1.05, five state-AG breach portals, named vendor newsrooms) | search window 2027-01-24..01-31 inside the window — exemplary |
| CYP-03 · `:7` | NEG-E (MISS = no primary document naming an MSP / RMM entry route) | 2026-12-31 | NAMED (Maine / CA / WA AG portals, EDGAR, named news query) | 2026-12-24..12-31 — exemplary |
| CYP-04 · `:8` | NEG-E (MISS = 0 KEV adds for four named product families) | 2027-04-30 | NAMED (CISA KEV JSON, dateAdded + vendorProject filter) | 2027-04-24..04-30 — exemplary |

**Boundary calls on new rows (NOT counted, stated so a second reader can move them):** ZHA-21 (FALSE = item absent from one scheduled Xinhua closing-day list) · REG-27 (FALSE = no quarterly SSB print ≥0.70% across four releases on one series) · CYP-01 (count ≥6 vs ≤5 on EDGAR Item 1.05, a count threshold not an absence) · CRL-32 (saving-rate level on two scheduled BEA prints) · MIDAS-14 / MIDAS-15 ("band holds at floor" = a single-date level read). None of them lacks an instrument, so moving them changes the negative count only.

**Carried negative rows still lacking an instrument (9):**
| # (run #4 §2) | Row · file:line | Lack at HEAD | Run #4 |
|---|---|---|---|
| 7 | BRK-11 · `AGENTS/BROCK/workbook/PREDICTIONS.tsv:7` | NONE; last dated read 2026-08-28 | NONE |
| 8 | BRK-18 · `:13` | NONE; last search 2026-06-08 (row now self-qualifies 10/14: "absence not freshly verified", `c95847c8a`) | NONE + stale |
| 9 | BRK-25 · `:18` | NONE; last dated read 2026-08-28 | NONE |
| 10 | BRK-26 · `:19` | NONE (10/15 pre-data statement on what counts; no feed named) | NONE |
| 13 | PHAN-P04 · `AGENTS/CARL/sub_agents/PHAN/workbook/PREDICTIONS.tsv:44` | PARTIAL — Instrument cell byte-identical to 10/08 ("company/regulatory filings"); dated 10/28 read now present | PARTIAL |
| 15 | PHAN-P07 · `:47` | PARTIAL — cell unchanged ("state AG actions"); dated 10/28 read + CARL ruling on county DAs | PARTIAL |
| 17 | POLLY-P07 · `AGENTS/CARL/sub_agents/POLLY/workbook/PREDICTIONS.tsv:9` | PARTIAL — the <50K leg still has no source; row says 10/28 "no CA private-carrier re-entry volume primary pulled" | PARTIAL + stale |
| 31 | OTTO-31 · `AGENTS/OTTO/thesis/PREDICTIONS.tsv:17` | PARTIAL — dated read 10/19 added; row's own scope caveat says aggregate corporate-trust data is not a dated non-mortgage measure | PARTIAL + stale |
| 41 | VULCAN-13 · `AGENTS/VULCAN/workbook/PREDICTIONS.tsv:4` | PARTIAL — row unchanged since 8/27; "venue sweep" scheduled 11/08 in `AGENTS/VULCAN/STATUS.md:89,94` | PARTIAL |

---

## §2 Past-due and ungraded today (Resolve_By before 2026-10-30, status still OPEN-class)

Command: ISO resolve date from each ledger's resolve column (REGINALD from `registry/PREDICTION_RESOLVE_BY.tsv`), else the last ISO date in Timeframe (86 rows from a resolve column or sidecar, 23 from Timeframe); the 56 prose-only timeframes judged by reading. MIDAS-16 resolves today (10/30) and is not counted.

**Negative-class: 0.** BDR-01 was graded RESOLVED-CORRECT on 2026-10-10 (`AGENTS/MARCO/sub_agents/BORDER/workbook/PREDICTIONS.tsv:3`, `693f39170`).

**All classes (for completeness — none negative):**
| Desk | Row · file:line | Due | Days past | State |
|---|---|---|---|---|
| YURI (grader DAEDALUS) | YUR-F01 · `AGENTS/YURI/workbook/INTENT_LEDGER.tsv:7` | 2026-10-24 | **6** | Graded MISS by DAEDALUS 10/28 (`runs/2026-10-28_YURF01_GRADE.md`; Will ruling recorded `AGENTS/DAEDALUS/STATUS.md:11`), but the ledger row still reads `OPEN`, "COUNT 0/3 AS OF 2026-10-21"; ledger last committed `30407dd09` 10/21. A grade that exists only off-ledger. |
| CARL/DOC | DOC-P10 · `AGENTS/CARL/sub_agents/DOC/workbook/PREDICTIONS.tsv:11` | 2026-10-29 (BEA Q3 advance) | 1 | TRACKING; pre-release expectation written 10/28. Ordinary grading lag. |
| CARL/DOC | DOC-P05 · `:6` | Q3 2026 | ~30 | `⚠ DUE-UNRESOLVED [DATA-NEEDED: Gallup-West Health 2026]` — honest token; grade on Gallup publication (~12/15 per `DOC/STATUS.md:177`). |
| MARCO (4 FROZEN sub-ledgers) | BDR-02 (5/31) · HSG-01 (9/30) · HSG-02 (6/30) · MIG-01 (6/30) · MIG-02 (9/30) · MIG-03 (9/30) · WF-01 (5/31) · WF-02 (6/30) · WF-03 (6/30) | 5/31–9/30 | 30–152 | Still `ACTIVE` tokens, but each ledger now carries `FROZEN 2026-10-10 — not maintained … do not cite rows as current` and names the rows UNGRADED with main-ledger twins where they exist. Run #4's ask ("freeze-banner or grade") was met by banner. |

Not counted, checked: CRL-29 (`AGENTS/CARL/thesis/PREDICTIONS.tsv:32`) — first checkpoint ~10/20 passed and recorded "CRL-29 10/21: NO VERDICT" at `AGENTS/CARL/STATUS.md:20`; the row's letter re-checks at the ~Nov Q3 HHDC, so OPEN is consistent. OZK-09's Timeframe date 2026-07-23 is a freeze date, resolve ~late Jan 2027. HAW-20 resolves 10/31 with dated primary pulls scheduled on 10/31 (`AGENTS/HAWK/STATUS.md:13`), which is the WQ-172 floor = ceiling form.

---

## §3 Treatment — the 11 desks run #4 asked (packets `AGENTS/<D>/inbox/processed/2026-10-08_from-DAEDALUS_sweeps-gatebasis2-falsif4-prose1.md`)

Packet check: `grep -n 'Falsification #4 (negative resolution)'` on every 2026-10-08 DAEDALUS packet. **All 11 owners in run #4 §4 received the ask by name** (AEOLUS ask 2 · BROCK ask 3 · CARL ask 1 · CORAL ask 1 · FALCON ask 2 · HANS ask 2 · MARCO ask 1 · OTTO ask 1 · REGINALD ask 2 · VULCAN ask 1 · WATT ask 1). The run #3 delivery defect (asks named in the record but absent from packets) did **not** recur. All 11 packets sit in `processed/`. Ledger evidence: `git log --since=2026-10-08T16:30 -- <ledger>` and `git log -S` on the added text.

| Desk | Rows asked | Verdict | Evidence (commit · file:line) |
|---|---|---|---|
| AEOLUS | AEO-03 resolving instrument; AEO-09 overdue NIFC 10/01 read | **DONE** | AEO-03: Guy Carpenter US Property-Cat ROL Index named prospectively, NO-VERDICT branch if unpublished by 1/15 — `94d4b648c` 10/09, `AGENTS/AEOLUS/workbook/PREDICTIONS.tsv:4`. AEO-09: "10/10 CHECKPOINT (NIFC 10/01 outlook): NOT met", next 11/01 — `6cecff5bc` 10/10, `:10`. |
| BROCK | BRK-11 / -18 / -25 / -26 instrument + dated attempt before 12/31 | **NOT DONE** (third consecutive run) | No instrument on any of the four; header `AGENTS/BROCK/workbook/PREDICTIONS.tsv:1` still has no Instrument column (the 9/17 ask). Difference from run #4: the deferral is now on record — `AGENTS/BROCK/STATUS.md:27` "by Fri 10/30 … NOT worked 10/30 … carried to the 10/31 R2 session … search instrument + dated attempt for BRK-11/18/25/26" (first written `813f0fe1a` 10/09). BRK-18 gained a self-qualification only ("absence not freshly verified", `c95847c8a` 10/14, `:13`). Eight ledger commits since 10/08, none touching these four rows' instruments. |
| CARL | PHAN-P04/P07 primaries; POLLY-P07 source for the <50K leg + dated read; DOC-P08 dated KFF read | **PARTIAL** | Dated halves done 10/28: PHAN-P04/P07 reachability reads (`db25db7d4`, `AGENTS/CARL/sub_agents/PHAN/workbook/PREDICTIONS.tsv:44,47`), POLLY-P07 Q3 check (`db25db7d4`, `POLLY/workbook/PREDICTIONS.tsv:9`), DOC-P08 KFF Sep 16–21 read (`b63faa241`, `DOC/workbook/PREDICTIONS.tsv:9`). Instrument halves not done: all four Instrument cells byte-identical to `0c05cb8ab` (md5 compare); PHAN-P04 still records its null in COCKROACH.tsv, POLLY-P07 says "no … re-entry volume primary pulled". |
| CORAL | Housekeeping: `THESIS.md:115-116` grade cells; `FL_Forward_Log.md` Ocala row | **NOT DONE** (housekeeping only; no negative row affected) | `AGENTS/CORAL/thesis/THESIS.md:115` still "Instrument note owed", `:116` "Amendment-3 ruling still unlocated" beside the installed rule at `AGENTS/CORAL/STATUS.md:113`; Ocala row now `AGENTS/CORAL/workbook/FL_Forward_Log.md:18` "⏳ Pending" since 7/29. 9 CORAL STATUS commits since 10/08; none touches either file's cells. |
| FALCON | FAL-06 dated search floor/ceiling before 11/05 | **DONE** | DATED-SEARCH PRECONDITION adopted under Will WQ-433, floor = ceiling = 11/05, after-window attempt = NO-VERDICT — `6e4c9d21c` 10/14, `AGENTS/FALCON/thesis/PREDICTIONS.tsv:36`. Successor-row caveat for FAL-07 in §5. |
| HANS | HNS-09 aggregate, cost-of-risk series, "material" threshold before Q3 results | **DONE** | Ex-ante definitions frozen 10/21 before any result in the set: fixed 9-bank set, CoR and NII tests, sector rule (≥3 graded; MISS if ≥ one-third fail), mechanised in `scripts/hns09_grade.py` + `workbook/HNS09_Q3_RESULTS.tsv` + 11 tests — `1c67cc742` 10/21, `AGENTS/HANS/workbook/PREDICTIONS.tsv:10`. First grades 10/29 (Deutsche graded, BNP incomplete). |
| MARCO | Grade or VOID BDR-01; freeze-banner or grade 4 sub-ledgers; TOUR-01/03 instruments + dated reads | **DONE** | BDR-01 RESOLVED-CORRECT and four sub-ledgers FROZEN-bannered — `693f39170` 10/10, `AGENTS/MARCO/sub_agents/BORDER/workbook/PREDICTIONS.tsv:1,3`. TOUR-01 StatCan WDS PIDs 24-10-0056/0057 named — `693f39170` 10/10, `TOURISM/workbook/PREDICTIONS.tsv:2`. TOUR-03 BTS T-100 FJE seats, letter Will-ruled 10/14 — `bb3c924e3` / `6c4fa1ff0` 10/14, `:4`. |
| OTTO | Record the OTTO-12 10/01 attempt; dated reads on OTTO-07 and OTTO-31 | **DONE** | OTTO-12: "October1 scheduled attempt MISSED, explicitly recorded now, not backdated" + actual attempt 10/19 — `17d088e9b`, `AGENTS/OTTO/thesis/PREDICTIONS.tsv:11`. OTTO-07: EDGAR FTS check 10/14 and controlled re-run 10/25 — `6d94bd2b1`, `1b2d83bd5`, `:6`. OTTO-31: dated read 10/19 — `80aab5846`, `:17` (instrument stays PARTIAL; not in the ask). |
| REGINALD | REG-03, REG-06 instruments; name the SSB Q3 line for REG-07 | **DONE** | All three on 10/10 under Will "go ahead" — `5344a98c8`. REG-03 in-row: FDIC QBP CRE NCO rate ≥1.5× Q2, dated attempt on the Q2 QBP, next ~11/25 (`AGENTS/REGINALD/workbook/PREDICTIONS.tsv:6`). REG-06 out-of-row because the row is Kernel-pinned: EDGAR submissions forms list + `8k_monitor.py` + scans 10/31, 11/30, 2027-01-05 (`AGENTS/REGINALD/registry/NOTES.md:314`). REG-07 named, then VOIDed as mis-lettered 10/15 (WQ-412; `:10`). Run #4's NOT DONE → DONE. |
| VULCAN | VULCAN-13 venue + borrower universe + dated sweep before 11/15 | **NOT DONE** (deferral on record inside the ask's date) | Row unchanged since 8/27 (`c6669e4f3` 10/20 touched other rows only), `AGENTS/VULCAN/workbook/PREDICTIONS.tsv:4`. Sweep scheduled 11/08 — `AGENTS/VULCAN/STATUS.md:89,94` (first written `076cc1753` 10/23). |
| WATT | WATT-12 coverage pull by 10/09 | **DONE** | Pulled and graded HIT 10/09, coverage proven 9/26–10/8 (n 286–288/day, 0 days lost) — `24870a2ce`, row moved to `AGENTS/WATT/workbook/PREDICTIONS_ARCHIVE.tsv:14`. |

**Roll-up:** 7 DONE (AEOLUS, FALCON, HANS, MARCO, OTTO, REGINALD, WATT) · 1 PARTIAL (CARL) · 3 NOT DONE (BROCK, VULCAN, CORAL — VULCAN with a dated deferral before its own deadline, CORAL housekeeping only). **Of run #4's 6 desks still carrying the gap, 1 still carries it: BROCK.** REGINALD, which filed its 9/17 ask without acting, executed within two days of the 10/08 re-ask. BROCK has now received the ask three times (9/17, 10/08 and a carried STATUS item) with zero instrument cells filled; the four rows resolve 12/31.

---

## §4 Decomposition of the count changes

| Measure | Run #4 | Treatment (owner named instrument) | Resolved / left class | New registrations | Definition / token | HEAD (run #4 ledgers) | + new ledgers | HEAD (all) |
|---|---|---|---|---|---|---|---|---|
| OPEN-class | 155 | 0 | −22 (17 graded/terminal + 5 NO-VERDICT-BY-INSTRUMENT) | +32 | −4 (OPEN → `STUCK`, a canonical status outside run #4's token set: BRK-32, CRL-21, OTTO-11, ZHA-05) | **161** | +4 (CYPHER) | **165** |
| Negative-class | 44 | 0 | −6 (BRT-30 CONFIRMED · FERT-12 MISS · BDR-01 RESOLVED · OSP-06 CONFIRMED · REG-07 VOID · WATT-12 HIT) | +7 (HNS-11, OSP-07, YUR-005, YUR-006, ZHA-19, ZHA-20, FAL-07) | 0 | **45** | +3 (CYP-02/03/04) | **48** |
| Lacking an instrument | 17 | −6 (AEO-03, HNS-09, TOUR-01, TOUR-03, REG-03, REG-06) | −2 (BDR-01 graded; REG-07 instrumented then VOIDed — counted as resolved, not treatment) | 0 (all 10 new negative rows NAMED) | 0 (REG-06 counted NAMED from an out-of-row sidecar; under a strict in-row reading it stays lacking → 10) | **9** | 0 | **9** |
| Stale dated search | 8 | −7 (POLLY-P07, DOC-P08, TOUR-01, TOUR-03, OTTO-07, OTTO-31, REG-03 all gained dated reads) | 0 | 0 | +3 (BRK-11, BRK-25 crossed the 60-day line on 8/28 reads; VULCAN-13 on its 8/27 read) | **4** | 0 | **4** |

Arithmetic checks: OPEN 155 − 22 − 4 + 32 = 161 ✓ · negative 44 − 6 + 7 = 45 ✓ · lacking 17 − 6 − 2 = 9 ✓ · stale 8 − 7 + 3 = 4 (BRK-18 the one carried) ✓.

**Reading:** the lacking-instrument fall (17 → 9) is mostly treatment (6 of 8), not resolution — the reverse of run #3 → #4, where 5 of the clearances were resolutions. New registrations brought no new lack: all 10 new negative rows name their instrument at registration and 7 carry an explicit dated-search window (OSP-07, FAL-07, CYP-02/03/04, and ZHA-19/20 via their STUCK-on-unreachable clause). The residue is concentrated: 4 of 9 are BROCK's, 3 are CARL sub-ledger Instrument cells, 1 OTTO, 1 VULCAN.

---

## §5 Owner flags for DAEDALUS to packet (proposals only — nothing sent by this reader)

| Owner | Flag (one line) | file:line |
|---|---|---|
| BROCK | Third ask, still zero instrument cells: name a search instrument (e.g. EDGAR 10-Q/N-CSR coverage set; SEC litigation-release + administrative-proceedings feeds; a named secondary-loan venue for BRK-25) and a dated in-window attempt for BRK-11/18/25/26 before 12/31 — the 10/31 R2 session is the owner's own recorded date; consider escalating to PROME if it slips again. | `AGENTS/BROCK/workbook/PREDICTIONS.tsv:7,13,18,19`; deferral `AGENTS/BROCK/STATUS.md:27` |
| CARL | Fill the Instrument cells, not just the reads: PHAN-P04 a primary failure source (not COCKROACH.tsv), PHAN-P07 a state-AG press/court-docket source, POLLY-P07 a source for the <50K re-entry leg. Dated reads done 10/28. | `AGENTS/CARL/sub_agents/PHAN/workbook/PREDICTIONS.tsv:44,47`; `AGENTS/CARL/sub_agents/POLLY/workbook/PREDICTIONS.tsv:9` |
| VULCAN | Hold the 11/08 VULCAN-13 venue sweep and write the venue + borrower/facility universe into the row before it runs (the sweep is scheduled in STATUS, the row is unchanged since 8/27); REFUTED is an open-perimeter absence. | `AGENTS/VULCAN/workbook/PREDICTIONS.tsv:4`; `AGENTS/VULCAN/STATUS.md:89,94` |
| YURI | YUR-F01 was graded MISS by DAEDALUS on 10/28 and ruled by Will, but the ledger row still says OPEN "0/3 AS OF 2026-10-21" — record the grade in the row (6 days past its 10/24 resolve date). | `AGENTS/YURI/workbook/INTENT_LEDGER.tsv:7` |
| FALCON | FAL-07's FAILED branch is "graded by the 2027-01-02 dated search", two days after the 12/31 event window — confirm this is inside the row's resolution window under WQ-172 (floor and ceiling = the resolve date; an after-window attempt is NO-VERDICT), or move the search to 12/31 as FAL-06 does. A question, not a finding: the row has no Resolve_By column to settle it. | `AGENTS/FALCON/thesis/PREDICTIONS.tsv:37` |
| CORAL | Housekeeping, second ask: the criterion 5 / 6 grade cells still say "Instrument note owed" and "ruling still unlocated" beside the installed rule; Ocala ⏳ since 7/29. Before the 11/15 falsify grade. | `AGENTS/CORAL/thesis/THESIS.md:115-116`; `AGENTS/CORAL/workbook/FL_Forward_Log.md:18` |
| OTTO | Informational: OTTO-31's instrument is still PARTIAL by the row's own scope caveat (aggregate corporate-trust data is not a dated non-mortgage measure); the ~11/05 Q3 10-Q read is the next chance to name the line it grades on. | `AGENTS/OTTO/thesis/PREDICTIONS.tsv:17` |
| DAEDALUS (self) | (a) Write-back check PASSED this time: all 11 run #4 §4 owners got the ask by name. (b) Canon question worth one line in the run doc: REGINALD's REG-06 instrument lives in a sidecar because the row is Kernel-pinned — decide whether out-of-row instruments count as NAMED for this leg (this reader counted it; strict in-row gives 10 lacking, not 9). (c) `STUCK` now holds 4 formerly-OPEN rows and the leg's token set excludes it; decide whether future runs census STUCK rows separately (none is negative-class today). | `AGENTS/REGINALD/registry/NOTES.md:314`; `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md:86` |
| Exemplars for canon | CYPHER registered three negative rows with named instruments and explicit in-window search windows on its first ledger (CYP-02/03/04); OSP-07's pre-registered sweep; HANS's mechanised HNS-09 grader with tests. | `AGENTS/CYPHER/workbook/PREDICTIONS.tsv:6-8`; `AGENTS/OSPREY/thesis/PREDICTIONS.tsv:18`; `AGENTS/HANS/workbook/PREDICTIONS.tsv:10` |

---

## §6 Limits

- **L1 — Census like-for-like on OPEN only.** The script reproduces run #4's 155 / 38-of-41 exactly at `0c05cb8ab` (§1.1), so the OPEN series compares. The negative and lacking counts depend on a judgment classifier; this reader applied run #4's written definition but is a different reader (run #4 L2 named ~10 boundary rows; §1.4 names 6 more).
- **L2 — Carried non-negative rows not re-read.** The 129 carried OPEN rows that run #4 classed out of the negative class were assumed to keep their letters. A row re-lettered since 10/08 into a negative form would be missed. Only the 44 run-#4 negative rows and the 36 new rows were read.
- **L3 — Dated-search staleness uses in-row dates plus the owner STATUS lines named.** The "latest in-row date" pass is a regex over each row (ISO, M/D and "October14" forms); a date in a row is not always a search (BRK-18's "October30" is a request, read and discounted by hand). Owner STATUS checked for BROCK, VULCAN, REGINALD (REG-01 Trepp read at `STATUS.md:109`), HAWK, CARL/DOC, CORAL.
- **L4 — Status tokens.** `STUCK`, `NO-VERDICT-BY-INSTRUMENT`, `MISSED`, `RETIRED`, `VOID` read as outside OPEN, per run #4's token rule. The 14 `ACTIVE` rows in FROZEN-bannered MARCO sub-ledgers are counted OPEN under that rule (the 151 figure in §1.3 excludes them).
- **L5 — Prose timeframes.** 56 OPEN rows carry no ISO date; past-due for them was judged by reading the timeframe text. "Q3 2026" rows awaiting an annual publication (DOC-P05) are listed, not called defects.
- **L6 — Scope.** This is the negative-resolution leg only; scanner flags and rail buckets belong to other run #5 readers. No ledger edited, nothing sent, no commits.
