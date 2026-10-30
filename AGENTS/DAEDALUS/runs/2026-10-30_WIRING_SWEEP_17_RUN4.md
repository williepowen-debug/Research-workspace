# WIRING SWEEP — LEG ⑰ METRIC-SURFACE SWEEP, RUN #4

**Run date:** 2026-10-30 (Fri) · stamp at file creation: `Fri Oct 30 12:26:34 EDT 2026` (`date`, same command as the write) · **Owner:** DAEDALUS · **Reader:** read-only non-owner reader (no subagents)
**Register:** `AGENTS/DAEDALUS/sweeps/WIRING_SWEEP.md:41` (⑰), method amendment `:67` (leg c), method rulings `:68` (i–iv)
**Method template:** `runs/2026-10-08_WIRING_SWEEP_17_RUN3.md`. Deviations stated where they occur.
**Standing:** read-only on the repository; this file and `runs/2026-10-30_WIRING_SWEEP_17_RUN4_SAMPLE.tsv` are the only writes. Nothing committed, nothing sent.

## 0. Headline (written last, `Fri Oct 30 12:36:15 EDT 2026`)

| Leg | Verdict | n | Worst instance |
|---|---|---|---|
| **Treatment: 10/8 asks** | **6 of 7 desks acted in writing inside 8 days** | 5 DONE (AEOLUS · FALCON · ORACLE · RED · REGINALD) · 1 PARTIAL (BROCK) · 0 NOT DONE · 1 DECLINED-IN-WRITING (CRUISE retired CRU-06) | BROCK BRK-013: band cells unchanged, STATUS strikes it "DONE 10/28" on two values supplied instead (DISCHARGED-BY-ASSERTION). 4 of 5 DONE carry a stale cell beside the fix |
| **(b) basis stated** | **NO MEASURABLE MOVEMENT** at population level; treatment visible at row level | b-len **21/33 = 64%** · b-3 10/33 = 30% · rule 7 **5/33 = 15%** | Same-rows counterfactual at 10/8 = 20/33 = 61%; the one treated row in the draw (FALCON IRAN-02) moved PARTIAL → STATED |
| **(a) metric surface** | **TREATMENT VISIBLE (ORACLE); control regressed (MIDAS)** | COMMAND-NAMED 9/33 = 27% (run #3 8%) · NO-METRIC-SURFACE 14/33 = 42% · producer exists 58% (run #3 44%) | MIDAS, run #3's only COMMAND-NAMED desk, dropped `metals_watch.py` from all 4 threshold rows in its 10/12 maintenance |
| **(c) perimeter** | **INSTANCES-FOUND, fewer (draw)** | 6/33 = 18% superset/subset/ambiguous (run #3 41%); 2 undisclosed | BROCK BRK-017 named "PIK→Default Conversion Rate", carries the share of defaults driven by PIK |
| **GATES** (`PROME/GATES.tsv`, whole) | **Instances cured; (b) flat** | 27 rows (19 carried, 8 added, 1 archived); (b) 23/27 = 85%; rule 7 13/27 = 48%; pointers 27/27 | 2 of run #3's GATES flags (LIQ-076 boot wire, COT-35B 4.909% reproduction) were raised on cell text already stale; NEXUS-WQ459-HY names no series |
| **Population** | **Pool widened per ruling (i)** | 34 files / 932 rows; LIVE 26 / 541; FROZEN 8 / 391 (42%); 333 live rows on 14 non-panel desks, 29 of them registry (HANS 17, HOMER 12) | 6 of 40 drawn rows (15%) were RETIRED/RESOLVED rows inside LIVE files; the denominator rule decides whether b-len reads 64% or 54% |

**(b) series:** 48% (8/28) → 41% (9/17) → 54% (10/8) → **64% (10/30)**, b-len. Run #4's pool adds registries and excludes 7 no-threshold rows (run #3: 1). One row of the change is treatment; the rest is pool, denominator and draw, inside about ±17pp. **The 10/8 packets worked as a delivery form (6 of 7 acted, median 4 days; run #2's 9/17 per-row round fixed 1 of 7 in 21 days), but the population basis rate under the written standard is still 15% (rule 7).**

---

## 1. TREATMENT — did each owner do the 10/8 ACTION's DONE-WHEN? (appended `Fri Oct 30 12:28:17 EDT 2026`, `date` in the append command)

**Base revision:** `2957c040a` (2026-10-08 15:13:30, the last commit before 15:15; the packets were committed at `6ac33d81a` 15:12:54, which touched only inbox files). Every named file was diffed `2957c040a` → HEAD `c1b78020f` (2026-10-30 12:23). All seven packets sit in `processed/`. Verdict is graded against the packet's own DONE-WHEN line, read at the artifact (row cells), not the desk's own claim.

| Desk | Ask (short) | What landed, where | Commit | Verdict |
|---|---|---|---|---|
| **AEOLUS** | one header line mapping each channel to the file/column of its level, instrument, window | `workbook/VX.tsv:1` `# LEVEL/INSTRUMENT MAP (added 2026-10-09 …)`: per channel → `<domain>/workbook/SERIES.tsv` instruments, band → `CLAUDE.md §THRESHOLDS` (exists, `:150`), window → `STATUS §UPGRADE TRIGGERS` (exists, `:27`) | `94d4b648c` 10/9 21:35 | **DONE** — one residual: the C3 entry still says "no registered series (CDD/HDD band untrippable)", but C3 was re-pointed on 10/10 (`8b510ad7b`) to NOAA CPC population-weighted HDD with the URL at `CLAUDE.md:161`; the map line was not updated, and STATUS item 16 still lists the C3 observation home as OPEN. The map is now wrong for one channel. |
| **BROCK** | (1) name both metrics + units on BRK-013, one band set per metric; (2) tell REGINALD which Medallia row is canonical | (1) `VX.tsv:15` Current cell now names both values (core dividend coverage 0.96x; asset coverage 188%, 10/28). **The band cells are byte-identical to 10/8**: Yellow `Div coverage <1.1x` · Orange `<1.0x + unrealized losses` · Red `Coverage <165% + div cut` — Red still says bare "Coverage". BROCK's STATUS strikes the item "DONE 10/28" on the strength of the values. (2) packet `REGINALD/inbox/processed/2026-10-14_from-BROCK_matched-Medallia-correction.md`: BXSL and BCRED June-30 rows both ~49.5¢, older 78¢ was a date mix; REGINALD's row already names BROCK canonical. But BROCK `STATUS.md:27` still carries "Medallia canonical → REGINALD" open, "NOT worked 10/30, carried to 10/31" | (1) `a30b820b4` 10/28 · (2) packet 10/14 (`c95847c8a` window) | **PARTIAL** — ask 2 met in substance (REGINALD has the figure); ask 1 not met at the row: the bands still grade on an unnamed "coverage" for Red. The "DONE 10/28" strike is a value supplied in place of the band re-cut asked for (DISCHARGED-BY-ASSERTION class, ⑰ fourth leg) |
| **CRUISE** | name CRU-06's basket and window | `VX.tsv:7` State `RETIRED 2026-10-14`, closing reading in Current; commit message: "VX-CRU-06 RETIRED 2026-10-14 (jobs done; no post-hoc basket)". Band cells unchanged on the retired row | `befe1efbb` 10/14 | **DECLINED-IN-WRITING** (retired with a stated reason; the row no longer grades, so DONE-WHEN is moot rather than met) |
| **FALCON** | (1) name the one instrument the IRAN-02 bands grade; (2) put the "<10 DEEPENING" band in the band columns or drop the citation | `VX.tsv:4` Green..Red cells each lead with the PortWatch band (`RED = <10/day = DEEPENING (PortWatch)`), Green carries `[INSTRUMENT, named 2026-10-14 …: IMF PortWatch Daily_Chokepoints_Data, … total transits/day … read by scripts/hormuz_transit_watch.py; band boundaries canonical in domain/FRESH_LEG_BASELINE.md]`; UKMTO text kept as labelled legacy; Notes "[Oct14] … asks 1+2 DONE". Paths exist | `ede013415` 10/14 21:56 | **DONE** — residual: the `[Oct14]` segment inside Current still says "Band-vs-instrument repair … still OWED as a proposal" (a dated historical segment, but it now contradicts the Notes cell beside it) |
| **ORACLE** | (1) a row→command map; (2) one window for ORC-07; (3) one venue for ORC-08 | (1) new `Producer` column (header `VX.tsv:1`), filled on all 12 rows; ORC-07's cell honestly says "NO 48h PRODUCER". (2) WQ-439 A (Will 10/15) encoded in ORC-07 Next_Trigger: "the letter stays 48h; graded ONLY on a 48h pair … UNKNOWN when no pair exists". (3) WQ-440 (a): "Trigger venue = Polymarket, Kalshi KXFED corroboration only"; ORC-08 then RETIRED AS SPENT 10/16, successors ORC-11/12 carry "Polymarket = trigger; Kalshi = corroboration only" in Producer | (1) `91ab67173` 10/15 · (2)(3) `1435334d0` 10/16 | **DONE** — residual: the ORC-07 and ORC-08 Producer cells still end "Window/Venue choice -> Will via PROME", written before the rulings that answered them |
| **RED** | (1) name the wage series in RED-002 Flip_If; (2) write AND/OR into RED-001 Flip_If | `VX.tsv:3` "ANY ONE leg flips (OR): PAYEMS … OR ICSA … OR UNRATE >5.0"; `VX.tsv:4` "FRED AHETPI YoY minus CPIAUCSL YoY, NEGATIVE on 3+ consecutive published months", with the AHE/AHETPI history stated | `79adf41e3` 10/9 10:34 | **DONE** |
| **REGINALD** | (1) re-cut/retire/re-date rows 9, 23, 37, 39; (2) re-point `:39` or mark CANNOT-FIRE; (3) one Medallia figure + ladder, `:51` cites BROCK | 5.01, 8.01, 14.01 RETIRED with reasons; 14.03 RETIRED + CANNOT-FIRE (SAM row absent); 17.01 Current = "→ BROCK VX-BRK-003 (CANONICAL): 49.5¢", Notes "ONE FIGURE, ONE LADDER = BROCK VX-BRK-003 … This row is a POINTER, not a second mark" (now at `VX.tsv:14/28/42/44/56`) | `0572114b8` 10/10 12:03 ("Will go-ahead") | **DONE** — residual: 17.01's own band cells still read `<90¢ · <85¢ · <80¢` while BROCK's are `90-95¢ · 80-90¢ · <80¢`; the row says "one ladder" in prose and keeps a second ladder in its cells (correction-beside-instruction form). One figure: met. One ladder: met in words only |

**§1 verdict: 5 DONE (AEOLUS · FALCON · ORACLE · RED · REGINALD) · 1 PARTIAL (BROCK) · 0 NOT DONE · 1 DECLINED-IN-WRITING (CRUISE, by retirement).** Four of the five DONE carry a residual where a cell written before or beside the fix now contradicts it (AEOLUS C3 map entry, FALCON Oct14 segment, ORACLE Producer tails, REGINALD 17.01 ladder cells). Time to act: AEOLUS 1 day · RED 1 · REGINALD 2 · FALCON 6 · CRUISE 6 · ORACLE 7–8; median 4 days; BROCK's ask 1 is the only one still open at 22 days, and its owner has it marked done.

**Contrast with run #3:** after the 9/17 per-row packets, 1 of 7 named instances was fixed in 21 days. After the 10/8 packets (short, one DONE-WHEN line each, DAEDALUS owning its own miss), 6 of 7 desks closed or retired in writing inside 8 days. That is a delivery-form difference worth recording, but it is n=7 on one round and the 10/8 packets also arrived with Will's attention on the sweep (REGINALD's commit cites "Will go-ahead").

---

## 2. Population census at HEAD, new pool (appended `Fri Oct 30 12:32:19 EDT 2026`)

**Pool (ruling i):** `AGENTS/<D>/workbook/{VX,TRIGGERS,THRESHOLDS}.tsv` + `AGENTS/<D>/registry/*THRESHOLDS*.tsv` + `AGENTS/<D>/registry/*TRIGGERS*.tsv` (one level, git-tracked). Glob hits excluded as not threshold registries, each read before excluding: `HANS/registry/THRESHOLDS_HISTORY.tsv` (cold append-only history of moved cell text, own banner), `RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv` (banner "GENERATED VIEW — do not hand-edit" of the canon file), `WALTER/registry/REG_THRESHOLDS_FIRED_LOG.tsv` (banner "FIRE-ONLY LOG — NOT AUTHORITATIVE"). Not matched by the glob and not added: `RED/registry/TRIGGER_OUTCOMES.tsv`, the WALTER pilot fixture copy. LIVE/FROZEN by `is_frozen()` imported from `scripts/ledger_staleness.py` (scratch `census.py`). Rows = non-`#`, non-blank lines minus the header.

| | Files | Rows | LIVE files / rows | FROZEN files / rows |
|---|---:|---:|---:|---:|
| workbook/ | 29 | 872 | 22 / **492** | 7 / 380 |
| registry/ | 5 | 60 | 4 / **49** | 1 / 11 (CREED) |
| **Pool** | **34** | **932** | **26 / 541** | **8 / 391** |

FROZEN (unchanged set since run #3): BRENT, CARL, HENRY, LABOR, LIQUID, OTTO, SAM VX + CREED/registry. **42% of pool rows sit in FROZEN ledgers** (391/932).

**Change since run #3 (10/8, 27 workbook files / 844 rows; LIVE 20 / 464):** +2 workbook files (`CYPHER/workbook/VX.tsv` 9 rows, added 10/22 `191ec1408`; `ISHM/workbook/VX.tsv` 8 rows, added 10/23 `080fbc7d6` — both new Tier-2 desks), +1 registry (`HOMER/registry/THRESHOLDS.tsv` 12 rows, built 10/28 `ea320da0f`, a machine transcription of HOMER's `CLAUDE.md` band table). Workbook LIVE rows 464 → 492 (+28). No registry changed LIVE/FROZEN state.

**LIVE rows outside the 8 panel desks:** **333 rows on 14 desks** — BOND, CREED (VX), CYPHER, FERT (VX + TRIGGERS), FLG (TRIGGERS), HANS (VX + registry), HAWK, HOMER (registry), ISHM, MARCO, OSPREY, VULCAN, WATT, ZHAO. Of these, **29 are live registry rows** (HANS 17, HOMER 12). Not graded here.

**Panel desks' live pool:** AEOLUS 43 · BROCK 25 · CRUISE 6 · FALCON 10 · MIDAS 5 · ORACLE 12 · RED 37 (VX 25 + registry 12) · REGINALD 70 (VX 62 + registry 8) = 208.

---

## 3. Sample (ruling ii) (appended `Fri Oct 30 12:32:19 EDT 2026`)

`random.seed(20261030)`; panel desks alphabetical; per desk, the pool is the union of that desk's LIVE pool files, listed (file sorted, line ascending); `random.sample(pool, 5)` (all rows if fewer than 5; MIDAS has exactly 5). Scratch `draw.py` imports `census.py`. **The 40 drawn rows were written to `runs/2026-10-30_WIRING_SWEEP_17_RUN4_SAMPLE.tsv` (desk · file:line · row ID · seed · pool) at `Fri Oct 30 12:29:00 EDT 2026`, before any row was graded.** Two drawn rows came from registries (RED-FT-06, RED-FT-04). One drawn VX row is registry-backed and was scored on the registry row per ruling (i): `REGINALD VX.tsv:61` VX-REG-18.02 (HY OAS) Orange `>320bps` = `registry/THRESHOLDS.tsv:4` REG-T-03 (`HY-OAS > 320`, sustain 3); its Yellow `>300` and Red `>400` VX bands have no registry row and are noted, not scored.

**Exclusions (no live threshold), stated so the denominator is visible:** VX-MIDAS-M1-POS (no registered band by design, as in run #3) · VX-CRU-06 (RETIRED 10/14, the 10/8 ask) · VX-CRU-02 (bands RETIRED to an OBSERVATION line 10/29, WQ-532 A) · VX-ORC-08 (RETIRED AS SPENT 10/16, WQ-440 b) · VX-RED-024 (RESOLVED-CONFIRMED 6/22, "keep as audit") · VX-RED-009 (RETIRED-UNMEASURED 10/28) · VX-REG-14.02 (RESOLVED-PASS 2/19). **n = 40 − 7 = 33.** Run #3 excluded 1 of 40. The retired/resolved share in the live pool is a composition fact in its own right: 6 of 40 drawn rows (15%) sit in files classified LIVE but carry no live threshold.

---

## 4. Legs (b) BASIS, (a) METRIC SURFACE, (c) PERIMETER on the 40 drawn rows (appended `Fri Oct 30 12:33:18 EDT 2026`)

### 4.1 Scoring rule, in writing (ruling iii) — run #3's three readings, unchanged

| Reading | Passes when | Use |
|---|---|---|
| **b-len** | every band leg names a LEVEL and the grading INSTRUMENT is recoverable from the row (any cell, incl. Source; for a registry row, its `grading_instrument`/`instrument_basis` cell) | **the series figure** |
| **b-3** | b-len AND the observation WINDOW is recoverable (undefined "sustained", "major", "mobilization", "pace" fail) | stricter |
| **b-rule7** | b-3 AND a REVISION POLICY is stated, or the series is an unrevised market price/settlement (PASS-NA) — STRICT_TEXT rule 7 letter | the standard as written |

(a) classes as run #3: COMMAND-NAMED (a cell names the script/command) · PRODUCER-EXISTS-UNCITED (a working producer exists in the desk or `FORGE/tools/market-data/`, no cell names it) · PROSE-VALUE · NONE. (c) as run #3: MATCH · SUPERSET · SUBSET · AMBIGUOUS · CANNOT-EVALUATE. The AEOLUS header map (treatment) was allowed to count for b-len "instrument recoverable"; in this draw it changed no grade (the drawn AEOLUS rows either name their instrument in the row or sit on legs the map itself says have no series).

### 4.2 Row-level grades (all 40 opened at HEAD; "Δ10/8" = row text changed since `2957c040a`, band/basis cells named)

| Desk | file:line | ID | Δ10/8 | (a) | b-len | b-3 | b-rule7 | (c) | Note (≤25 words) |
|---|---|---|---|---|---|---|---|---|---|
| AEOLUS | VX:38 | VX-AEO-35 | no | PRODUCER-EXISTS-UNCITED | STATED | STATED | FAIL | MATCH | Kaub ≤25 AND Duisburg ≤153, 3 complete days, PEGELONLINE; pull command in `water/SOURCES.md`, not cited; no revision rule on provisional gauge data |
| AEOLUS | VX:17 | VX-AEO-15 | no | NONE | PARTIAL | PARTIAL | FAIL | MATCH | C4→4 needs ">$10B single cat OR carrier insolvency"; whose cat-loss estimate unnamed; header map says loss leg has no series |
| AEOLUS | VX:39 | VX-AEO-36 | no | PRODUCER-EXISTS-UNCITED | PARTIAL | PARTIAL | FAIL | MATCH | 3 OR legs; PL ≥4 instrumented (NIFC), "Q3 cat-loss tally ≥110% of 10-yr avg" names no tally publisher |
| AEOLUS | VX:24 | VX-AEO-22 | no | NONE | PARTIAL | PARTIAL | FAIL | MATCH | corn/soy G/E "<55% Yellow"; header map: crop G/E has NO instrument (KB-AEO-092) |
| AEOLUS | VX:30 | VX-AEO-27 | no | PRODUCER-EXISTS-UNCITED | STATED | STATED | FAIL | MATCH | record-low elevations on the USBR daily series, post-fill-minimum basis stated; no revision rule |
| BROCK | VX:4 | VX-BRK-002 | Notes only | NONE | PARTIAL | PARTIAL | FAIL | MATCH | "div cut threatened" / "NII broken" undefined; inputs March, Last_Updated 2026-03-26 |
| BROCK | VX:26 | VX-BRK-024 | no | NONE | STATED | PARTIAL | FAIL | MATCH | rating-action counts; agencies named in Notes; "2+ downgrades" over no window |
| BROCK | VX:19 | VX-BRK-017 | no | NONE | STATED | STATED | FAIL | **AMBIGUOUS** | named "PIK→Default Conversion Rate"; value is share of defaults driven by PIK (Fitch 12-mo) — a different ratio, undisclosed; value 5/1 |
| BROCK | VX:21 | VX-BRK-019 | Source | NONE | PARTIAL | PARTIAL | FAIL | MATCH | "sponsors diverging / diff strategies" is a judgment count; at ceiling, no rescore possible (desk says so) |
| BROCK | VX:11 | VX-BRK-009 | Notes | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | MATCH | FRED BAMLH0A0HYM2 named; band window unstated; Current still the 6/17 value under a 10/14 Last_Updated |
| CRUISE | VX:7 | VX-CRU-06 | State | — | NO-LIVE-THRESHOLD | — | — | — | RETIRED 2026-10-14 (10/8 ask) |
| CRUISE | VX:4 | VX-CRU-03 | Source | NONE | PARTIAL | PARTIAL | FAIL | MATCH | "mass softening / pullback confirmed / >-20% pace": pace of which booking series, no window |
| CRUISE | VX:2 | VX-CRU-01 | Source (re-based $33.99 raw, 10/23) | COMMAND-NAMED | STATED | STATED | PASS-NA | MATCH | yfinance raw close + `FORGE/tools/market-data/fetch.py`; desk discloses signed-band display ambiguity (SF13) unresolved |
| CRUISE | VX:3 | VX-CRU-02 | bands RETIRED | — | NO-LIVE-THRESHOLD | — | — | — | OBSERVATION line, WQ-532 A 10/29 |
| CRUISE | VX:6 | VX-CRU-05 | Source | PROSE-VALUE | STATED | PARTIAL | FAIL | MATCH | "leverage climbing" no level; desk: "band re-spec is a residual" |
| FALCON | VX:9 | VX-HAWK-BABMANDAB-01 | Source | NONE | PARTIAL | PARTIAL | FAIL | MATCH | "sustained quiet", "mobilization signals" undefined; Red confirmation source unnamed; Notes cell still a bare date |
| FALCON | VX:5 | VX-HAWK-USIRAN-KINETIC-01 | Source | NONE | PARTIAL | PARTIAL | FAIL | MATCH | event bands, no named confirming source or bar |
| FALCON | VX:11 | VX-FALCON-SUNK-01 | Source | NONE | STATED | STATED | PASS | MATCH | class-tiered total-loss counts, 30d window, "later official ID governs" (revision rule) |
| FALCON | VX:4 | VX-HAWK-IRAN-02 | **bands (10/8 ask)** | COMMAND-NAMED | STATED | STATED | FAIL | SUBSET (disclosed) | PortWatch total transits/day via `hormuz_transit_watch.py`; AIS-visible lower bound, desk says so; no revision rule on lagged prints |
| FALCON | VX:3 | VX-HAWK-IRAN-01 | Source | NONE | PARTIAL | PARTIAL | FAIL | CANNOT-EVALUATE | Green ">25/day sustained", Orange "<2/day": the UKMTO-era counts IRAN-02 just retired, unnamed here |
| MIDAS | VX:2 | VX-MIDAS-M1 | threshold + source (10/12) | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | MATCH | "w/o real-yield spike" still undefined; `metals_watch.py` dropped from source 10/12 |
| MIDAS | VX:3 | VX-MIDAS-M2 | threshold + source (10/12) | PRODUCER-EXISTS-UNCITED | STATED | STATED | PASS-NA | SUBSET (disclosed) | GSR >85 s=3; standalone silver bands unscored to 11/1; `metals_watch.py` dropped |
| MIDAS | VX:4 | VX-MIDAS-I1 | threshold + source (10/12) | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | SUPERSET (disclosed) | "-20%" reference still unstated; "price comparison UNMEASURED" |
| MIDAS | VX:5 | VX-MIDAS-I2 | source (10/12) | PROSE-VALUE | PARTIAL | UNSTATED | FAIL | SUBSET (disclosed) | "major SA/Russia outage = 4" |
| MIDAS | VX:6 | VX-MIDAS-M1-POS | source | COMMAND-NAMED | NO-THRESHOLD | — | — | — | by design; `cot_gold.py` |
| ORACLE | VX:2 | VX-ORC-01 | +Producer | COMMAND-NAMED | PARTIAL | PARTIAL | FAIL | AMBIGUOUS | one band over three markets (bailout / ANY-bank / named-EOY); which grades unstated; Updated 2026-09-07 |
| ORACLE | VX:6 | VX-ORC-05 | +Producer | COMMAND-NAMED | STATED | PARTIAL | FAIL | CANNOT-EVALUATE | desk still has not read the resolution text (Updated 9/18) |
| ORACLE | VX:4 | VX-ORC-03 | +Producer | COMMAND-NAMED | STATED | PARTIAL | FAIL | MATCH | level on one read; re-check rule not in the letter; Updated 9/18 |
| ORACLE | VX:7 | VX-ORC-06 | +Producer | COMMAND-NAMED | STATED | PARTIAL | FAIL | MATCH | slug "ai-industry-downturn" for "AI bubble burst"; resolution text not read by this reader |
| ORACLE | VX:9 | VX-ORC-08 | +Producer | — | NO-LIVE-THRESHOLD | — | — | — | RETIRED AS SPENT 10/16 |
| RED | VX:25 | VX-RED-024 | no | — | NO-LIVE-THRESHOLD | — | — | — | RESOLVED-CONFIRMED 6/22 |
| RED | VX:17 | VX-RED-015 | Counter_Evidence | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | MATCH | Flip_If ">300 sustained 5d" (met 10/2, found 10/14); HY series still unnamed in Flip_If — same text run #3 graded |
| RED | VX:11 | VX-RED-009 | Strength | — | NO-LIVE-THRESHOLD | — | — | — | RETIRED-UNMEASURED 10/28 |
| RED | registry:7 | RED-FT-06 | operative basis (session clause) | COMMAND-NAMED | STATED | STATED | PASS | MATCH | VIX <16 s=5, FRED VIXCLS, sessions not observations, FRED date governs; boot.py METRIC_MAP named |
| RED | registry:5 | RED-FT-04 | no band change | COMMAND-NAMED | STATED | STATED | PASS | MATCH | Brent <75 s=3, ICE front-month SETTLEMENT governs, bar cannot complete a count; boot.py BZ=F named |
| REGINALD | VX:61 → registry:4 | REG-T-03 (for VX-REG-18.02) | VX Source only | PRODUCER-EXISTS-UNCITED | STATED | STATED | FAIL | MATCH | HY-OAS >320, 3 consecutive closes, FRED BAMLH0A0HYM2; no first-print/revised rule; VX row cites `fetch.py`, registry row cites no command |
| REGINALD | VX:43 | VX-REG-14.02 | no | — | NO-LIVE-THRESHOLD | — | — | — | RESOLVED-PASS 2/19 |
| REGINALD | VX:50 | VX-OTTO-1.03 | no | NONE | PARTIAL | PARTIAL | FAIL | CANNOT-EVALUATE | "Auto Recovery Ratio" of what pool; Source = "OTTO" (a FROZEN ledger); OWNER-DEFERRED, STALE since 2/16 |
| REGINALD | VX:63 | VX-REG-15.04 | no | COMMAND-NAMED | STATED | PARTIAL | FAIL | MATCH | `market.py` BZ=F; bar vs settlement unstated; value 8/12; Status YELLOW while its own Notes say $88.63 is below the >$100 Yellow line |
| REGINALD | VX:23 | VX-REG-6.09 | no | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | MATCH | "-10/-15/-20%" from an unstated reference; value 8/12 |

### 4.3 Results

| Leg (b) | Run #1 (8/28) | Run #2 (9/17) | Run #3 (10/8) | **Run #4 (10/30)** |
|---|---|---|---|---|
| Pool | workbook/ | workbook/ | workbook/ | **workbook/ + registry/** |
| Rows graded | 29 | 39 | 39 | **33** (40 drawn, 7 no live threshold) |
| **STATED (b-len)** | 14/29 = 48% | 16/39 = 41% | 21/39 = 54% | **21/33 = 64%** |
| STATED (b-3) | — | — | 10/39 = 26% | **10/33 = 30%** |
| STATED (b-rule7) | — | — | 3/39 = 8% | **5/33 = 15%** (3 PASS: SUNK-01, FT-06, FT-04 · 2 PASS-NA: CRU-01, MIDAS-M2) |

Per desk (graded · b-len · b-3 · rule7): AEOLUS 5·2·2·0 · BROCK 5·3·1·0 · CRUISE 3·2·1·1 · FALCON 5·2·2·1 · MIDAS 4·3·1·1 · ORACLE 4·3·0·0 · RED 3·3·2·2 · REGINALD 4·3·1·0.

| Leg (a) | Run #1 | Run #2 | Run #3 | **Run #4** |
|---|---|---|---|---|
| **NO-METRIC-SURFACE** (NONE + PROSE-VALUE) | 59% | 54% | 22/39 = 56% | **14/33 = 42%** (NONE 12 · PROSE 2) |
| COMMAND-NAMED | — | 33% | 3/39 = 8% | **9/33 = 27%** |
| PRODUCER-EXISTS-UNCITED | — | 13% | 14/39 = 36% | **10/33 = 30%** |
| producer exists (sum) | — | 46% | 17/39 = 44% | **19/33 = 58%** |

| Leg (c) | Run #3 | **Run #4** |
|---|---|---|
| MATCH | 18/39 | **24/33** |
| SUPERSET / SUBSET / AMBIGUOUS | 5 / 4 / 7 = **16/39 = 41%** | 1 / 3 / 2 = **6/33 = 18%** |
| of which undisclosed | 9 | **2** (BRK-017, ORC-01) |
| CANNOT-EVALUATE | 5 | 3 |

### 4.4 Decomposition — a sampling difference is not a treatment effect

**(b) b-len 54% → 64% (+10pp):**

| Component | Effect on the run-#4 figure | How measured |
|---|---|---|
| **Treatment (10/8 asks)** | **+1 row (+3pp)** | Of the 33 graded rows, one was named in a 10/8 ask and is graded live: FALCON IRAN-02, PARTIAL → STATED (b-len and b-3). The other asked-about rows that were drawn were retired (CRU-06, ORC-08) and fall out of the denominator. Counterfactual: the same 33 rows on their 10/8 text grade **20/33 = 61%** (only IRAN-02 differs; MIDAS's 10/12 threshold rewrites and CRU-01's re-base change no grade). |
| **Pool composition (ruling i)** | about +2pp | 3 of 33 graded rows are registry rows (FT-06, FT-04, REG-T-03), all STATED; without them 18/30 = 60%. |
| **Retired-row exclusion** | denominator 39 → 33 | 6 drawn rows retired/resolved (run #3: 0). These are not failures removed; they are rows whose thresholds no longer exist. |
| **Row draw (different seed)** | the residual, ~+4–5pp | 12 threshold rows appear in both run #3's and run #4's draw (BRK-009, CRU-01, CRU-05, BABMANDAB-01, SUNK-01, IRAN-02, IRAN-01, MIDAS M1/M2/I1/I2, RED-015). On those 12, run #3 graded b-len 8/12 at 10/8; this run grades 9/12 at 10/30: the only change is IRAN-02. |
| **Rater** | 0 on 11 overlap rows | the 11 unchanged overlap rows got the same grade here as in run #3 (all three readings). This reader had run #3's grades open, so that is consistency, not an independent calibration. |

★ **VERDICT (b): NO MEASURABLE MOVEMENT at population level; the treatment is visible at row level only.** 41% → 54% → 64% sits inside about ±17pp (95%, n=33). The one sampled row the 10/8 asks touched moved the right way. **Under the standard as written (rule 7) the stock is 15% compliant; with the window demanded, 30%.** The five rule-7 passes come from RED registry rows (FT-06, FT-04), a Will-ruled letter (FALCON SUNK-01) or unrevised prices (CRU-01, MIDAS-M2): the schema, not the sweep, carries the window and revision policy.

**(a) COMMAND-NAMED 8% → 27% (+6 rows), NO-METRIC-SURFACE 56% → 42%:**

| Component | COMMAND-NAMED rows |
|---|---|
| Treatment: ORACLE `Producer` column (10/8 ask 1) | **+4** (all 4 graded ORACLE rows; run #3 graded the same desk 0/5 named) |
| Treatment: FALCON IRAN-02 (10/8 ask 1) | **+1** |
| Pool composition: registry rows naming `boot.py` | +2 (FT-06, FT-04) |
| Desk-initiated, not asked: CRUISE CRU-01 cites `fetch.py` (10/14 basis fix) | +1 |
| Row draw: REGINALD 15.04 (`market.py`) | +1 |
| **Control regression: MIDAS** — the 10/12 "approved maintenance" (`989d42ad0`) rewrote every `source` cell and **dropped `metals_watch.py` from all four threshold rows** | **−3** |

The NO-METRIC-SURFACE drop (56% → 42%) is mostly draw and pool: the treatment rows moved from UNCITED to NAMED, which does not change NO-SURFACE. **Comparable figure (producer exists): 44% → 58%, inside sampling noise.** The treatment effect that is real is ORACLE: a desk-wide row→command map now exists and every row uses it.

**(c) 41% → 18%:** mostly draw. Of run #3's 16 perimeter instances, the panel ones that were asked about were cured or retired (IRAN-02 AMBIGUOUS → disclosed SUBSET; REG-17.01 now a pointer; ORC-08 retired; CRU-06 retired). The run-#4 draw happened to land on fewer multi-instrument rows. Not a population measurement of improvement.

---

## 5. GATES leg — `PROME/GATES.tsv`, whole (appended `Fri Oct 30 12:35:18 EDT 2026`)

**Population:** 27 data rows (L3–L29; header L2; 1 comment line L1), NF=12 on every row; 95,940 B. vs run #3 (`2957c040a`): **19 carried · 8 added** (GATE-BRK-OTIC · NEXUS-WQ459-HY · REG-27 · ORC-11 · REG-28 · REG-29 · REG-30 · ORC-12) **· 1 removed** (GATE-FLG-T08, terminal pass 10/9). 3 rows terminal but still in the file (NEXUS-SEAT-01 · TERRY-VLO-SCALE · ORC-11). All 27 rows opened (condition, state, last_checked, source, scannable, definition_surface, review_by). NOT-SEEN: none.

**Pointers:** every repository path in `source` and `definition_surface` exists (27/27 rows, 0 missing; scratch regex path check, owner-dir fallback for relative paths). Row-ID pointers checked: REG-27..30 each resolve to one row in `REGINALD/workbook/PREDICTIONS.tsv`; `VX-ORC-12` resolves in ORACLE `VX.tsv`. § anchors and commit hashes not resolved (as run #3).

### 5.1 Run #3's named GATES instances

| Row | Run #3 instance | Status 10/30 | Evidence |
|---|---|---|---|
| GATE-LIQ-079 | state "FIRE legs UNGRADEABLE-until-banded" (non-canonical token) | **FIXED by supersession** | WQ-535 A (Will 10/29 00:26 ET) banded FIRE legs 3/4; state now "NOT ARMED … FIRE legs 3/4 now BANDED". Token text removed at `e0e162ae8` (10/11). **Residual:** the condition cell still carries the 9/2 VINTAGE CONVENTION sentence "until then FIRE is UNGRADEABLE, not false" ahead of the new "FIRE LEGS 3/4 BANDED" paragraph — two live instructions in one cell; and "Owner-side mirror owed (L261)" (LIQUID's letter `FUNDING_SEIZURE_GATE_SCOPED.md:35-36` does carry "banded letter below (WQ-535 A)", `d2da72cd8` 10/29, so the mirror looks done and the cell's "owed" is stale) |
| GATE-LIQ-079 | last_checked 35 days old | **FIXED** | last_checked = 10/29 consumer read |
| GATE-LIQ-076 | last_checked said "NO BOOT INSTRUMENT READS THIS GATE" | **FIXED (text removed 10/19, `c5286bf6d`) — and the run-#3 flag was stale when raised** | `AGENTS/LIQUID/scripts/boot.py:656` "GATE-LIQ-076 legs … wired 2026-09-29": the boot wire existed 9 days before run #3 read the disclaimer |
| GATE-BRENT-COT-35B | "4.909% NOT re-reproduced since 8/13" — MATERIAL-IF-WRONG | **FIXED 10/8 16:38 (`8fc5ff0f2`) — and the run-#3 flag rested on a clause overtaken 29 minutes after it was written** | PROME wrote "not re-reproduced" at `9ca99225d` 2026-09-18 13:21; BRENT reproduced the bar at the CFTC archive at `1af68399c` 13:50 the same day (`scripts/cot_grade.py` built). The cell lagged until DAEDALUS Gate-Basis #2 struck it 10/8, about 1.5 hours after run #3 was written |
| GATE-TERRY-ROLL70-EXIT · GATE-TERRY-VLO-HELD-01 | `scannable=INSTRUMENT` with no command in any cell | **NOT FIXED** (COSMETIC) | no `.py`/command token in either row; producers exist (REGINALD `REG_T02_EXIT_LOG`, TERRY repro) |

**3 FIXED · 0 PARTIAL · 1 NOT FIXED (cosmetic) of 4 instance groups; 2 of run #3's GATES flags (076, COT-35B) were raised on cell text that was already stale.**

### 5.2 Re-measure

| Measure | Run #1 (n=29) | Run #2 (n=20) | Run #3 (n=20) | **Run #4 (n=27)** |
|---|---|---|---|---|
| **(b) STATED (b-len)** | 24 = 83% | 18 = 90% | 16 = 80% | **23 = 85%** |
| (b) STATED (b-3) | — | — | 16 = 80% | **23 = 85%** |
| (b) rule 7 | — | — | 8 = 40% | **13 = 48%** — 8 with a stated vintage/revision rule (HY-REKILL · LIQ-076 · LIQ-079 · FALCON-001 · COT-35B · T12S-DFII10 · BRK-OTIC · REG-30) + 5 unrevised close/settlement/market-price N/A (ROLL70-EXIT · VLO-SCALE · VLO-HELD-01 · ORC-11 · ORC-12) |
| (a) NO-METRIC-SURFACE | 38% | 45% | 11 = 55% | **14 = 52%** |
| (a) COMMAND-NAMED | — | 10 | 4 | **5** (HY-REKILL `boot.py` · LIQ-072 `boot.py` · LIQ-079 `boot.py` · COT-35B `cot_grade.py` · VLO-SCALE `fetch.py`) |
| (a) PRODUCER-EXISTS-UNCITED | 4 | 2 | 5 | **8** (LIQ-069 `gate069_legs.py` · LIQ-076 `boot.py:656` · ROLL70-EXIT · T12S · VLO-HELD-01 · ORC-11 · ORC-12 · WQ459-HY) |
| `scannable=INSTRUMENT` with no command named | — | 1 | 2 | **4** (ROLL70-EXIT · VLO-HELD-01 · ORC-11 · ORC-12; the ORC pair reach `polymarket.py` in one hop via ORACLE's new `Producer` column) |
| Pointers dereference | 28/29 | 19/20 | 20/20 | **27/27** |

**(b) PARTIAL rows (4):** GATE-LIQ-069 (leg ③ "AI-infra HY new-issue concessions" — no level; the owner's own `gate069_legs.py:257` prints "NO_INSTRUMENT") · GATE-LIQ-072 (leg 1 "BB-like spreads", SpaceX "pricing-date pinning owed") · GATE-OSPREY-001 (leg (b) "Kpler-confirmed liftings drop" — no magnitude) · **GATE-NEXUS-WQ459-HY (new)**: the 231-byte summary says "HY>=L+10bp for3 … CCC<=C0" and names no series; vintage and carry-forward rules are "owner letter" only.

**Decomposition 80% → 85%:** carried 19 rows: 15/19 STATED at 10/8 → 16/19 at 10/30 (LIQ-079 PARTIAL → STATED by WQ-535 A, a Will ruling, not a ⑰ ask); the 3 carried PARTIALs (069, 072, OSPREY) are unchanged. Added 8 rows: 7/8 STATED. Removed 1 (FLG-T08, STATED). Rule 7 40% → 48%: the 8 added rows are mostly REGINALD/ORACLE prediction-style rows written with MECE and first-figure rules (REG-30's "restated comparative becomes the baseline, noted" is a revision policy written in). **Verdict: no measurable movement; GATES remains far above the desk registries (85% vs 64% b-len; 48% vs 15% rule 7).**

### 5.3 New GATES instances (flags, not fixes)

| Row | Instance | Severity |
|---|---|---|
| GATE-NEXUS-WQ459-HY | summary names no series for "HY" or "CCC"; every basis rule lives only in the owner letter | WATCH (pointer resolves) |
| GATE-LIQ-079 | condition cell keeps "until then FIRE is UNGRADEABLE" beside "FIRE LEGS 3/4 BANDED"; "owner-side mirror owed" stale | COSMETIC (correction-beside-instruction) |
| GATE-ORC-12 | condition says "Letter: … VX-ORC-12 once encoded (until then this cell is the letter)"; definition_surface says encoded `f9a497d95` | COSMETIC |
| GATE-LIQ-069 · GATE-LIQ-076 | producers exist (`gate069_legs.py`, `boot.py:656`) and no cell cites them | COSMETIC |
| GATE-TERRY-ROLL70-EXIT | state and last_checked cells glue words ("exit0/3 through10/9close$74.27") — root Output Canon "never glue words" | COSMETIC |

---

## 6. Owner flags — for DAEDALUS to packet (this reader sent nothing) (appended `Fri Oct 30 12:36:02 EDT 2026`)

| # | Owner | Flag (one line) | Leg |
|---|---|---|---|
| 1 | **BROCK** | `VX.tsv:15` (BRK-013) band cells are unchanged since 10/8: Red still reads "Coverage <165% + div cut" with no metric named. STATUS strikes the ask "DONE 10/28" on the strength of the two values in Current. The 10/8 ask was one band set per named metric. | ⑰(b), discharged-by-assertion |
| 2 | **BROCK** | `STATUS.md:27` still carries "Medallia canonical → REGINALD" open, but your 10/14 packet (`REGINALD/inbox/processed/2026-10-14_from-BROCK_matched-Medallia-correction.md`) delivered the figure and REGINALD's row already cites you as canonical. Close it or say what is still owed. | ⑰ |
| 3 | **BROCK** | `VX.tsv:19` (BRK-017) is named "PIK→Default Conversion Rate" but carries the share of defaults driven by PIK (Fitch 12-mo). Those are different ratios; rename or re-source. | ⑰(c) |
| 4 | **REGINALD** | `VX.tsv:56` (17.01) says "ONE FIGURE, ONE LADDER = BROCK VX-BRK-003" while its own band cells keep a second ladder (<90 / <85 / <80¢ vs BROCK 90-95 / 80-90 / <80¢). Blank or align the cells. | ⑰(c) |
| 5 | **REGINALD** | 5 live rows still defer to FROZEN ledgers — `VX-OTTO-1.01/1.02/1.03/3.01` (OTTO, FROZEN) and `VX-REG-11.01` (LABOR, FROZEN) — the same class you retired for SAM on 10/10. 17 OWNER-DEFERRED rows remain STALE in all. | ⑰ ㉓ |
| 6 | **REGINALD** | `VX.tsv:63` (15.04 Brent) Status YELLOW while its own Notes say $88.63 [8/12] sits below the >$100 Yellow line; value 79 days old. | ⑰(b) |
| 7 | **AEOLUS** | `VX.tsv:1` map line still says "C3 = no registered series (CDD/HDD band untrippable)"; C3 was re-pointed 10/10 to CPC population-weighted HDD (`CLAUDE.md:161`). Update the C3 entry. | ⑰(a) |
| 8 | **FALCON** | `VX.tsv:3` (IRAN-01) Green ">25/day sustained" and Orange "<2/day" are the UKMTO-era counts IRAN-02 retired as a grading basis on 10/14; they name no instrument. Also `VX.tsv:4` Current's [Oct14] segment still says the repair is "OWED". | ⑰(b) |
| 9 | **ORACLE** | `VX.tsv:8/9` Producer cells end "Window/Venue choice -> Will via PROME"; WQ-439 A and WQ-440 (a) answered both on 10/15–10/16. `VX.tsv:2` (ORC-01) one band over three markets: say which grades. `VX.tsv:6` (ORC-05) resolution text still unread since 9/17. | ⑰(a)(c) |
| 10 | **MIDAS** | The 10/12 maintenance (`989d42ad0`) removed `metals_watch.py` from the `source` cell of all four threshold rows; the desk was run #3's only COMMAND-NAMED reference. Restore the command reference. | ⑰(a) |
| 11 | **PROME** | `GATES.tsv:7` (LIQ-079) condition keeps "until then FIRE is UNGRADEABLE" beside the WQ-535 BANDED paragraph, and says the owner mirror is owed when LIQUID's letter already carries it (`d2da72cd8`). `GATES.tsv:29` (ORC-12) still says "once encoded". | ⑰ |
| 12 | **PROME** | `GATES.tsv:23` (NEXUS-WQ459-HY) names no HY or CCC series in the row; `GATES.tsv:16/20` (ROLL70-EXIT, VLO-HELD-01) are `scannable=INSTRUMENT` with no command, unchanged from run #3. | ⑰(a)(b) |
| 13 | **DAEDALUS** | Banner run #3's §4.3 GATES flags: GATE-LIQ-076's "no boot instrument" (wired `boot.py:656` 9/29) and GATE-BRENT-COT-35B's "4.909% not re-reproduced" (reproduced `1af68399c` 9/18) were read from cell text that was already stale. | ⑰ record |
| 14 | **DAEDALUS** | Rule the denominator: 6 of 40 drawn rows (15%) were RETIRED/RESOLVED rows inside LIVE files. Either exclude them at draw time (filter by status) or keep the draw-then-exclude rule; run #3 and #4 handle it identically only by accident. | ⑰ method |
| 15 | **DAEDALUS** | 29 live registry rows outside the panel (HANS 17, HOMER 12 built 10/28) are in the pool and ungraded; HOMER's is a new machine registry. Decide whether run #5 widens the panel. | ⑰ method |

**Next step (ruling iv):** this reader sends nothing. Every row above needs a packet file named in DAEDALUS's next record, or it did not happen.

---

## 7. Doubts and limits (appended `Fri Oct 30 12:36:02 EDT 2026`)

1. **One reader, run #3's grades open.** On the 11 unchanged overlap rows this reader gave run #3's grades; that is consistency with a known answer, not independent calibration. No second reader.
2. **The b-len rise (54% → 64%) is not a finding.** One row of it is treatment (FALCON IRAN-02); the rest is pool composition (+3 registry rows), a different denominator (7 exclusions vs 1) and a different draw, inside a ±17pp interval.
3. **Treatment verdicts are graded against each packet's DONE-WHEN line, at the row**, not against the desk's own claim. Two judgment calls: CRUISE retiring CRU-06 is filed DECLINED-IN-WRITING rather than DONE (the row no longer grades, so DONE-WHEN is moot); REGINALD is filed DONE although its 17.01 ladder cells disagree with the "one ladder" claim (DONE-WHEN names "one current figure", which is met).
4. **The treatment cannot be separated from Will's attention.** REGINALD's fix cites "Will go-ahead", ORACLE's window and venue were settled by Will rulings WQ-439/440. The 10/8 packets and those rulings arrived in the same week.
5. **Exclusion of retired/resolved rows** is this reader's rule, stated in §3; run #3 excluded only a no-band row. Including the 6 retired rows as non-STATED would give b-len 21/39 = 54%, identical to run #3, which shows how much the headline depends on the denominator rule.
6. **(c) is row-text only.** No primary was fetched; ORACLE contract resolution texts were not read (ORC-05, ORC-06).
7. **(a) "producer exists" was checked by name** (script present in the desk or in `FORGE/tools/market-data/`, or a `SOURCES.md` pull command); no producer was executed.
8. **Pointer check is path existence only**; § anchors, line numbers and hashes inside cells were not resolved, except the specific hashes cited in §1 and §5.1, which were opened with `git show`.
9. **Legs not run:** DISCHARGEABLE-BY-TOKEN-GESTURE and DISCHARGED-BY-ASSERTION as population legs. One instance of the second surfaced in passing (BROCK BRK-013, flag 1).
10. **Size:** this record is over the 32,550 B read cap that binds boot-read surfaces; it is a run record, not boot-read. §0 is first so a truncating reader keeps the headline.
11. **Stamps:** every section stamp is `date` output from the same command that appended the section. The SAMPLE file has no stamp column; its write time is the `date` printed by the draw command (12:29:00).

