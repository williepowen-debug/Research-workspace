# WIRING SWEEP — LEG ⑰ METRIC-SURFACE SWEEP, RUN #3

**Run date:** 2026-10-08 (Thu) · stamp at file creation: `Thu Oct  8 14:57:43 EDT 2026` (`date`, same command as the write) · **Owner:** DAEDALUS · **Reader:** read-only reader (no subagents)
**Register:** `AGENTS/DAEDALUS/sweeps/WIRING_SWEEP.md:41` (⑰) · resolve_by 2026-10-08 (`runs/2026-09-17_WIRING_SWEEP_02_JUDGMENT.md:33`)
**Method source:** `runs/2026-09-17_WIRING_SWEEP_02_JUDGMENT_W2.md` §3 (run #2). Deviations stated where they occur.
**Standing:** read-only on the repository; this file is the only write. Nothing committed, nothing sent. NOT-SEEN used for any population not opened.

## 0. Headline (written last, `Thu Oct  8 15:10:46 EDT 2026`)

| Leg | Verdict | n | Worst instance |
|---|---|---|---|
| **Convention fix, run-#2 desks** | **NOT FIXED — never sent** | **0 of 5 fixed** (AEOLUS · FALCON · ORACLE · RED · REGINALD); MIDAS control unchanged and clean | No DAEDALUS packet since 9/17 asked any desk for the header line or boot wire. All 6 `VX.tsv` headers are byte-identical 9/17 → 10/8 |
| **(b) basis stated** | **NO MEASURABLE MOVEMENT** (no treatment occurred) | **21/39 = 54%** comparable reading · 10/39 = 26% with window · 3/39 = 8% under rule 7 as written | `REGINALD VX.tsv:39` (REG-14.03) still defers to `VX-SAM-9.02`, a row that does not exist in a FROZEN ledger, 8 days past REGINALD's own 9/30 re-cut date |
| **(a) metric surface** | **INSTANCES-FOUND, flat** | 22/39 = 56% no command (run #1 59%, run #2 54%) | ORACLE: 5/5 sampled rows have a working producer and none cites it, unchanged since run #2 |
| **(c) perimeter** | **INSTANCES-FOUND** (first measurement) | 16/39 = 41% superset/subset/ambiguous; 9 undisclosed | Medallia 1L registered twice on different ladders: BROCK `VX.tsv:5` 49.5¢ (BCRED Q2-26) vs REGINALD `VX.tsv:51` 78¢ (BXSL Q4-25) |
| Run #2 named desk instances (panel) | **1 FIXED · 1 SUPERSEDED · 5 NOT FIXED** | 7 | REGINALD's four rows; BROCK BRK-013 (packet drained 9/18, no disposition) |
| **GATES** (`PROME/GATES.tsv`, whole) | **Instances cured; (b) flat (rater)** | 20 rows (16 carried, 4 new, 4 archived); run-#2 instances 4 FIXED · 1 PARTIAL; (b) 16/20 = 80%; pointers 20/20 resolve | GATE-BRENT-COT-35B: gating base 4.909% not re-reproduced in 56 days. GATE-LIQ-079 still carries the non-canonical `UNGRADEABLE` token |
| **Population** | **Run #2 screen error + pool blind spot** | Run #2 filed 3 LIVE registries (CREED, HAWK, MARCO; 101 rows) as FROZEN, so 58% FROZEN is really 46%. 37 live registry rows sit outside `workbook/` | RED's and REGINALD's machine registries already carry the instrument/window columns the "convention fix" asks for, and have since May |

**(b) series:** run #1 14/29 = 48% (8/28) → run #2 16/39 = 41% (9/17) → **run #3 21/39 = 54% (10/8)**. Same comparable reading, n = 39 live rows on run #2's 8 desks. One row of the change is a real fix (CRUISE CRU-04, re-cut 9/19). The rest is a different row draw (the same 39 rows read 51% at 9/17), inside a ±16pp sampling interval. **The convention fix that run #3 was meant to measure was never sent, so there was nothing to measure.**


---

## 1. The convention-fix desks — did the fix land? (appended `Thu Oct  8 14:59:58 EDT 2026`, `date` in the append command)

**Which six.** Run #2 says "6 of 8 desks are CONVENTION defects" (`_JUDGMENT.md:24`; W2 `:146`). Its own triage table (W2 `:135-144`) names **five** CONVENTION-defect desks — AEOLUS · FALCON · ORACLE · RED · REGINALD (CONVENTION + PER-ROW) — plus **MIDAS = "CONVENTION-CLEAN — reference desk"**. BROCK and CRUISE are PER-ROW. So "six" counts MIDAS, whose verdict is *clean*: the defect count in run #2's own table is **5**, not 6. Graded below: the 5, plus MIDAS as a control (did the reference desk stay clean).

**Was the fix ever asked for?** Read every DAEDALUS→desk packet to these six desks since 9/17 (`ls AGENTS/<D>/inbox/processed/2026-09-17_from-DAEDALUS_PR6*`, `…/2026-10-0[12]_from-DAEDALUS*`; `grep -i "convention|header line|basis column|source column|instrument column|boot wire|schema|Anchor_Type"`):

| Desk | Packets since 9/17 | Convention ask in them? |
|---|---|---|
| AEOLUS | PR6 9/17 (profile, 1,461 B) · PR7 10/01 (reinsurance basis vs CORAL) | **NO** — 0 grep hits on PR6; PR7 asks a one-figure reconcile, not a schema line |
| FALCON | PR6 9/17 (853 B) · gate-basis 9/17 · GATE-FALCON-001 leg-2 10/01 | **NO** — gate-basis packets concern `PROME/GATES.tsv` row text, not `VX.tsv` schema |
| ORACLE | PR6 9/17 (1,005 B) | **NO** — per-row only: ORC-04 contract month (⑰) + downgrade trigger |
| RED | PR6 9/17 (SAM CH adjudicators) · PR7 10/01 (state-token artifact) | **NO** — 0 grep hits; no `Flip_If` instrument / `Anchor_Type` ask |
| REGINALD | PR6 9/17 (1,998 B) · 10/02 PREDICTIONS header clocks | **NO** — per-row only (`VX.tsv:37/:23/:9/:39`, address-a-desk rows); no OWNER-DEFERRED clock/pointer convention |
| MIDAS | PR6 9/17 (L4 notice) | n/a (reference desk) |

★ **The convention fix that run #2 named as "the next pass" was never sent to any desk.** The 9/17 PR6 round carried the per-row ⑰ defects only — exactly the delivery mode run #2 said was "measurably not working". `DAEDALUS/STATUS.md:31` carries "Wiring ⑰ #3 (resolve_by 10/8 PASSED)" as past-due-not-started; no DOCKET row carries the convention fix (`grep -n "⑰|metric-surface" PROME/DOCKET.tsv` → no ⑰ row).

**Did it land anyway (desk-initiated)?** Header line of each `workbook/VX.tsv` at `f1e620d7b` (last commit 2026-09-17 22:24) vs HEAD, and the `#` comment block, and `git log --since=2026-09-17 -- AGENTS/<D>/workbook/VX.tsv`:

| Desk | Run-#2 convention defect | Header 9/17 → HEAD | Comment block | VX commits since 9/17 | Verdict |
|---|---|---|---|---|---|
| AEOLUS | state-change LOG, no Source/Basis column; bands in free-text `Trigger` | `ID Date Vector Channel Old_State New_State Score Trigger Notes` — **identical** | none (0 → 0 lines) | 2 (`250f83ad1` 9/28, `e28573290` 10/8) — row content only | **NOT FIXED** |
| FALCON | migrated HAWK schema, no basis/as-of on row; B/C/D mark scale unbased | `ID Name Current_Value Status Green Yellow Orange Red Last_Updated Source Notes` — **identical** | 1 line, identical (migration note) | 2 (`0cab6ab47` 9/28, `b1556ceee` 10/7) — row content | **NOT FIXED** (see §6 doubt: header does carry `Source` + `Last_Updated`; run #2's "no Source/as-of" description is imprecise — the missing element is BASIS) |
| ORACLE | 4/5 rows have a producer (`scripts/kalshi.py`, `tools/*.py`) and cite none — "one header line or boot wire" | `ID Market Current State Watch Alert Critical Next_Trigger Updated` — **identical**; no producer column | none (0 → 0) | 4 (`d023cce33` 9/17 … `279b7aec1` 9/28) — rolls/rows | **NOT FIXED** — `CLAUDE.md:47` still says only "log threshold state-changes to `VX.tsv`"; no row→producer map in CLAUDE.md, header or boot (`grep -n "VX.tsv\|producer" AGENTS/ORACLE/CLAUDE.md`) |
| RED | `Flip_If` has no Instrument column; adopt FLG `Anchor_Type` | `ID Name Target Counter_Evidence Strength Bull_Wt Bear_Wt Flip_If Last_Reviewed Source KB_Links Notes` — **identical** | 1 line, re-worded 9/18 (staleness narrative, not schema) | 2 (`e6a26e1a7`, `037aabc6b` 9/18) | **NOT FIXED** |
| REGINALD | `OWNER-DEFERRED` with no clock / no pointer (+ per-row) | `ID Name Category Current_Value Yellow Orange Red Status Confidence Last_Updated Source Cross_Links Notes` — **identical** | 1 line, data-clock refresh 9/14 → 10/07 | 5 (`cdc52d872` 9/24 … `5453ee5ad` 10/7) | **NOT FIXED** at convention level (per-row status in §2/§5) |
| MIDAS (control) | — CONVENTION-CLEAN | `id channel indicator state score threshold source as_of notes` — **identical** | none | 2 (`8c3df0281` 9/25, `bc70f8a4a` 10/1) | **STILL CONVENTION-CLEAN** (schema unchanged; row-level re-check in §2) |

**§1 verdict: 0 of 5 FIXED · 0 PARTIAL · 5 NOT FIXED · 0 CANNOT-EVALUATE; control MIDAS unchanged.** The precondition of run #3 ("re-measure after the convention fix") did not occur; run #3 is therefore a **no-treatment re-measure**, and any movement in (b) below is drift or composition, not the fix.

---

## 2. Leg (b) — BASIS + WINDOW STATED: series run #1 → #2 → #3, with decomposition (appended `Thu Oct  8 15:05:39 EDT 2026`)

### 2.1 Population — reproduced exactly, and a screen defect found in run #2

**Pool definition reconstructed:** `AGENTS/*/workbook/{VX,TRIGGERS,THRESHOLDS}.tsv` → **27 registries** at both revisions (25 `VX.tsv` + FERT and FLG `TRIGGERS.tsv`; no THRESHOLDS file exists). Data rows = non-`#`, non-blank lines minus the header. Command: scratch `census.py <rev>` (`git ls-tree` + `git show`, `is_frozen()` imported from `scripts/ledger_staleness.py`).

| | Run #2 as printed (9/17) | Reproduced at `f1e620d7b` (last commit 9/17) | HEAD (10/8) |
|---|---|---|---|
| Registries / all rows | 27 / 829 | **27 / 829 — exact** | 27 / **844** (+15) |
| FROZEN, run #2's named list (BRENT CARL CREED HAWK HENRY LABOR LIQUID MARCO OTTO SAM) | 10 / 481 | **10 / 481 — exact** | 10 / **482** (HAWK +1) |
| LIVE, run #2's screen | 17 / 348 | **17 / 348 — exact** | 17 / **362** (+14) |
| FROZEN by the canonical recognizer `is_frozen()` | — | **7 / 380** | 7 / 380 |
| LIVE by the canonical recognizer | — | **20 / 449** | 20 / **464** |

⚠️ **Run #2's FROZEN screen mis-classified three LIVE registries as FROZEN: CREED (34 rows), HAWK (10→11), MARCO (57) = 101 rows.** All three declare LIVE in their own banner region: MARCO line 1 *"57 live indicator vectors. STATE: LIVE"*; CREED line 1 *"LIVE-with-staleness-alert"*; HAWK's line 1 contains *"scripts/boot.py is FROZEN"* mid-line — a prose mention, exactly the shape `ledger_staleness.py` rule 10 (9/03) exists to not read as a banner. **Consequence for run #2's headline: "58% of registry rows sit in FROZEN ledgers" (481/829) is 46% (380/829) by the fleet's own recognizer; the live threshold population was 449, not 348, rows.** Run #2's "overstates the LIVE threshold population by more than 2×" still holds but at a different ratio: ~1,130 / 348 = 3.2× as run #2 computed it, ~1,130 / 449 = 2.5× on the recognizer (run #1's ~1,130 not re-verified here). Neither sample is affected (no CREED/HAWK/MARCO row was drawn in run #2 or run #3), so the (b) series below is unaffected; the base-rate sentences are.

**Composition change 9/17 → 10/8 (run #2 screen):** +14 live rows = AEOLUS +5 (`VX-AEO-35..39`, same no-basis log form) · HANS +3 · ZHAO +3 · FLG/TRIGGERS +2 · FERT/TRIGGERS +1; 0 rows removed; 0 registries changed FROZEN/LIVE state (both classifiers).

### 2.2 Sample — deviation stated

Run #2's draw is **not reproducible from the record**: no sample file was saved (`grep -rl 20260917 AGENTS/DAEDALUS/` → no sample artifact), and `random.seed(20260917)` with `sample`/`shuffle`/`choices` over the 17 live registries or 16 desks does not return its 8 desks (6 variants tried, 0 match). **Run #3 therefore holds the DESK set fixed** (the 8 run-#2 desks — the treatment is per-desk) and redraws rows: `random.seed(20261008)`, per desk alphabetical, `random.sample(data_lines, 5)` (scratch `draw.py`). Drawn lines: AEOLUS 4,11,17,20,31 · BROCK 5,9,11,12,25 · CRUISE 2,3,5,6,7 · FALCON 3,4,8,9,11 · MIDAS 2–6 (all 5) · ORACLE 5,6,8,9,10 · RED 3,4,5,14,17 · REGINALD 7,24,34,51,54. **40 rows opened at the artifact; 1 NO-THRESHOLD (`VX-MIDAS-M1-POS`, "NO REGISTERED BAND — reporting vector only" by Will-gated design) ⇒ n = 39**, the same denominator run #2 used. **NOT-SEEN: none of the 40.**

### 2.3 Rubric — three readings, because run #2's was not written down

| Reading | Passes when | Use |
|---|---|---|
| **b-len** (run-#2-comparable) | every band leg names a level AND the grading instrument is recoverable from the row (any cell, incl. `Source`) | **the series figure** |
| **b-3** | b-len AND the observation window is recoverable (undefined "sustained", "major", "periodic", "spike" fail) | stricter cross-check |
| **b-rule7** | b-3 AND a revision policy is stated (or the series is an unrevised market price) — STRICT_TEXT rule 7 letter | the standard as written |

**Rater calibration (the only like-for-like rows available):** MIDAS has 5 rows and its `id|threshold|source` columns are byte-identical 9/17 vs HEAD (`diff` of `awk -F'\t' '{print $1" | "$6" | "$7}'` → identical). Run #2 graded MIDAS "4/5 STATED"; this reader's b-len gives **3/4 threshold rows** (I2 "major SA/Russia outage" fails). So b-len is, if anything, **slightly stricter** than run #2 on identical text — it does not inflate run #3.

### 2.4 Results

| Leg (b) | Run #1 (8/28) | Run #2 (9/17) | **Run #3 (10/8)** |
|---|---|---|---|
| Desks | BOND FERT FLG HAWK LABOR* LIQUID* MIDAS OSPREY (*FROZEN) | AEOLUS BROCK CRUISE FALCON MIDAS ORACLE RED REGINALD | same 8 as run #2 |
| Live rows graded | 29 | 39 | **39** |
| **STATED (b-len)** | **14 / 29 = 48%** | **16 / 39 = 41%** | **21 / 39 = 54%** |
| PARTIAL / UNSTATED (b-len) | 11 / 3 | 14 / 9 | 17 / 1 |
| STATED (b-3, window required) | — | — | **10 / 39 = 26%** |
| STATED (b-rule7, revision policy) | — | — | **3 / 39 = 8%** (1 PASS + 2 unrevised-price N/A) |
| Population (live rows) | ~1,130 unscreened | 348 (as screened) / 449 (recognizer) | 362 / 464 |

Per desk (threshold rows · b-len STATED · b-3 STATED): AEOLUS 5·1·1 · BROCK 5·3·0 · CRUISE 5·4·3 · FALCON 5·1·1 · MIDAS 4·3·1 · ORACLE 5·3·1 · RED 5·3·1 · REGINALD 5·3·2. Row-level grades: §2.6.

### 2.5 Decomposition of 41% → 54% (+13pp, +5 rows)

| Component | Rows | How measured |
|---|---|---|
| **Treatment (rows whose band letter changed since 9/17)** | **+1** | Band/Source cells of each sampled ID diffed `f1e620d7b` vs HEAD: only **VX-CRU-04** (re-cut 9/19, GREEN/ORANGE/RED + Source; PARTIAL→STATED) and **VX-ORC-04** (v4→v5 roll, Alert/Critical now UNSET; PARTIAL either way) changed bands. CRU-01/CRU-06 changed `Source` only (grade unchanged). Counterfactual on the same 39 rows at 9/17: **20 / 39 = 51%**. |
| **Convention fix** | **0** | §1: 0 of 5 desks changed a header, schema or boot wire. |
| **Population composition** | 0 in sample | +14 rows added fleet-wide, none drawn (AEOLUS +5 are in-pool but not drawn). |
| **Row draw (different rows, same desks)** | **+4** (≈ residual) | Run #2 rows unrecoverable; 51% (run-#3 rows at 9/17) vs 41% (run-#2 rows at 9/17) = same desks, same date, different 39 rows. |
| **Rater** | ≤0 | MIDAS calibration: this reader 1 row *stricter* on identical text. |

★ **VERDICT (b): NO MEASURABLE MOVEMENT, and none expected — the treatment did not occur.** At n=39 a proportion near 50% carries a 95% interval of about ±16pp, so 48% → 41% → 54% is one flat series with sampling scatter. The single attributable improvement is one row (CRU-04), a per-row fix CRUISE made answering the 9/17 packet. **Under the standard as written (rule 7) the stock is 8% compliant; with the window demanded, 26%.** The b-len figure that run #1 and #2 reported is the lenient reading, and it is the only one that looks like half.


### 2.6 Row-level grades (all 40 opened; a = metric surface, c = perimeter — §3)

| Desk | Line | ID | (a) | b-len | b-3 | b-rule7 | (c) | Note (≤25 words) |
|---|---:|---|---|---|---|---|---|---|
| AEOLUS | 4 | `VX-AEO-03` | NONE | UNSTATED | UNSTATED | FAIL | CANNOT-EVALUATE | no level at all; observation in Trigger |
| AEOLUS | 11 | `VX-AEO-10` | PROSE-VALUE | PARTIAL | PARTIAL | FAIL | MATCH | upgrade-to-4 'sustained multi-region EEA2+' - sustained undefined |
| AEOLUS | 17 | `VX-AEO-16` | NONE | STATED | STATED | FAIL | MATCH | >=1.5 OISST Nino-3.4 monthly; ONI 3-mo strength convention applied to 1-mo OISST |
| AEOLUS | 20 | `VX-AEO-19` | NONE | PARTIAL | PARTIAL | FAIL | MATCH | 'approaching very strong' level unstated (ONI MJJ named) |
| AEOLUS | 31 | `VX-AEO-29` | NONE | PARTIAL | PARTIAL | FAIL | MATCH | channel-kill resolves 11/30, kill level not on row |
| BROCK | 5 | `VX-BRK-003` | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | AMBIGUOUS | band holder unpinned (BCRED 49.5c vs BXSL/Apollo 77-78c); tools/soi_nonaccrual.py |
| BROCK | 9 | `VX-BRK-007` | NONE | PARTIAL | PARTIAL | FAIL | SUPERSET | gate/tender discount, vehicle unnamed (3 vehicles); Last_Updated 2026-05-01 |
| BROCK | 11 | `VX-BRK-009` | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | MATCH | FRED BAMLH0A0HYM2 named, band window unstated (kill leg 10 sessions stated); value 6/17 |
| BROCK | 12 | `VX-BRK-010` | NONE | STATED | PARTIAL | FAIL | AMBIGUOUS | median of which BDC universe (RJ/Cliffwater/Stanger) unpinned; value 3/23 STALE-marked |
| BROCK | 25 | `VX-BRK-023` | NONE | PARTIAL | PARTIAL | FAIL | MATCH | legal-event bands; Yellow 'unrebutted' ungradeable; Status STUCK |
| CRUISE | 2 | `VX-CRU-01` | PRODUCER-EXISTS-UNCITED | STATED | STATED | PASS-NA | MATCH | CCL close vs named ref $33.45 2026-02-06; price series no revision; reading 9/18 |
| CRUISE | 3 | `VX-CRU-02` | NONE | STATED | STATED | FAIL | MATCH | CCL reported fuel $/mt ex allowances; guide vs print disclosed |
| CRUISE | 5 | `VX-CRU-04` | NONE | STATED | STATED | FAIL | MATCH | RE-CUT 9/19 answering W2: unit+population+window named; run-2 instance FIXED per-row |
| CRUISE | 6 | `VX-CRU-05` | PROSE-VALUE | STATED | PARTIAL | FAIL | MATCH | 'leverage climbing' no level |
| CRUISE | 7 | `VX-CRU-06` | PRODUCER-EXISTS-UNCITED | PARTIAL | PARTIAL | FAIL | AMBIGUOUS | band 'sector move' basket/window unnamed; separate CCL-RCL falsifier fully based (WQ-222 TR) |
| FALCON | 3 | `VX-HAWK-IRAN-01` | NONE | PARTIAL | PARTIAL | FAIL | CANNOT-EVALUATE | composite event+level bands; 'sustained' undefined; Yellow MOU leg historical |
| FALCON | 4 | `VX-HAWK-IRAN-02` | PRODUCER-EXISTS-UNCITED | PARTIAL | PARTIAL | FAIL | AMBIGUOUS | bands UKMTO-tanker vs reading PortWatch/Kpler; Current cites a '<10 DEEPENING band' absent from band columns; hormuz_transit_watch.py boot-wired |
| FALCON | 8 | `VX-HAWK-ISR-01` | NONE | PARTIAL | PARTIAL | FAIL | MATCH | 'periodic'/'multiple' undefined; Yellow keyed to Apr 12-20 window |
| FALCON | 9 | `VX-HAWK-BABMANDAB-01` | NONE | PARTIAL | PARTIAL | FAIL | MATCH | Red event has no named confirming source; Notes cell = bare date |
| FALCON | 11 | `VX-FALCON-SUNK-01` | NONE | STATED | STATED | PASS | MATCH | class-tiered total-loss counts, 30d green window, Will 9/7 stands (post-fire treatment stated) |
| MIDAS | 2 | `VX-MIDAS-M1` | COMMAND-NAMED | STATED | PARTIAL | FAIL | MATCH | 'w/o a real-yield spike' undefined; GC=F continuous; WGC leg UNMEASURED |
| MIDAS | 3 | `VX-MIDAS-M2` | COMMAND-NAMED | STATED | STATED | PASS-NA | SUBSET | band on GSR only; silver -48% invisible (BAND-BLIND, disclosed by desk) |
| MIDAS | 4 | `VX-MIDAS-I1` | COMMAND-NAMED | STATED | PARTIAL | FAIL | SUPERSET | '-20%' reference/window unstated; rolling 2yr median; >=4 roots disclosed |
| MIDAS | 5 | `VX-MIDAS-I2` | PROSE-VALUE | PARTIAL | UNSTATED | FAIL | SUBSET | 'major outage' undefined; price-blind (disclosed) |
| MIDAS | 6 | `VX-MIDAS-M1-POS` | COMMAND-NAMED | NO-THRESHOLD | NO-THRESHOLD | NO-THRESHOLD | MATCH | no registered band by design (Will-gated); cot_gold.py |
| ORACLE | 5 | `VX-ORC-04` | PRODUCER-EXISTS-UNCITED | PARTIAL | PARTIAL | FAIL | MATCH | run-2 Aug-contract defect superseded by v5 Oct $110 roll (id 4936102, ICE venue disclosed); Alert/Critical UNSET pending Will (CANNOT-FIRE, disclosed) |
| ORACLE | 6 | `VX-ORC-05` | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | CANNOT-EVALUATE | desk itself has not read the contract's resolution bar |
| ORACLE | 8 | `VX-ORC-07` | PRODUCER-EXISTS-UNCITED | STATED | STATED | FAIL | SUPERSET | band is 48h move; Current/State held on D7d/D30d moves - reading window != letter window |
| ORACLE | 9 | `VX-ORC-08` | PRODUCER-EXISTS-UNCITED | PARTIAL | PARTIAL | FAIL | AMBIGUOUS | venue unpinned: Alert '>66%' met on PM 66.5, ~1pt short on Kalshi |
| ORACLE | 10 | `VX-ORC-09` | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | SUBSET | rotation subject graded on S&P leg only |
| RED | 3 | `VX-RED-001` | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | MATCH | Flip_If legs joined by commas (AND/OR unstated); claims series/window unnamed; NFP vintage discussed in-row, no policy |
| RED | 4 | `VX-RED-002` | PRODUCER-EXISTS-UNCITED | PARTIAL | PARTIAL | FAIL | AMBIGUOUS | wage series unpinned: fired on AHE 3.6 vs CPI 3.8, re-checked on AHETPI-CPIAUCSL; Jul -0.023pp near-tie |
| RED | 5 | `VX-RED-003` | PRODUCER-EXISTS-UNCITED | STATED | STATED | FAIL | SUBSET | nominal retail sales (goods) for 'consumer spending'; no revision policy on a heavily revised series |
| RED | 14 | `VX-RED-012` | NONE | PARTIAL | PARTIAL | FAIL | MATCH | 'canaries reverse negative' - metric (revenue? sequential?) unnamed; 'next quarter' relative |
| RED | 17 | `VX-RED-015` | PRODUCER-EXISTS-UNCITED | STATED | PARTIAL | FAIL | MATCH | 'HY OAS >300 sustained 5d' - concept not series; Last_Reviewed 2026-08-07 |
| REGINALD | 7 | `VX-REG-3.01` | NONE | STATED | STATED | FAIL | SUPERSET | named '90+ DQ', instrument PDNA (90+ AND nonaccrual); value Q4-2025, REFRESH-OWED since 2026-03-27 |
| REGINALD | 24 | `VX-REG-9.01` | NONE | STATED | PARTIAL | FAIL | CANNOT-EVALUATE | FDIC QBP line unnamed; value 2026-03-04 |
| REGINALD | 34 | `VX-REG-12.01` | NONE | PARTIAL | PARTIAL | FAIL | CANNOT-EVALUATE | '>$10B agg' over what window/population; Red 'Gates' undefined; news tally |
| REGINALD | 51 | `VX-REG-17.01` | NONE | STATED | STATED | FAIL | AMBIGUOUS | OWNER-DEFERRED (BROCK) no clock/pointer; 78c BXSL Q4-25 vs BROCK VX-BRK-003 49.5c BCRED Q2-26 on a DIFFERENT ladder |
| REGINALD | 54 | `VX-REG-17.04` | NONE | PARTIAL | PARTIAL | FAIL | SUPERSET | collateral quality graded on BDC equity NAV discount; BDC set unpinned; Source = a desk; OWNER-DEFERRED |

---

## 3. Legs (a) METRIC SURFACE and (c) PERIMETER (appended `Thu Oct  8 15:07:57 EDT 2026`)

### 3.1 (a) — does a command return the number? (same 39 rows)

| (a) class | Run #1 (n=29) | Run #2 (n=39) | **Run #3 (n=39)** |
|---|---|---|---|
| **NO-METRIC-SURFACE** (NONE + PROSE-VALUE) | 17 = 59% | 21 = 54% | **22 = 56%** (NONE 19 · PROSE-VALUE 3) |
| COMMAND-NAMED (row cites the script/command) | — | 13 = 33% | **3 = 8%** (all MIDAS: `metals_watch.py`) |
| PRODUCER-EXISTS-UNCITED | 3 | 5 = 13% | **14 = 36%** |
| producer exists, cited or not (sum) | — | 18 = 46% | **17 = 44%** |

**Comparable figure = NO-METRIC-SURFACE: 59% → 54% → 56%, flat.** The COMMAND-NAMED / UNCITED split is **not** comparable: this reader counts a row as COMMAND-NAMED only when a cell names the script; a named FRED series or ticker with `FORGE/tools/market-data/fetch.py` able to return it is UNCITED. MIDAS calibration agrees with run #2 on identical text (run #2 "4/5 command-named"; here 3 threshold rows + `M1-POS` = 4/5), so the split difference sits in rows run #2 drew and this run did not; the producer-exists sum (46% → 44%) is the stable number. **ORACLE is still 5/5 PRODUCER-EXISTS-UNCITED** — `scripts/polymarket.py` / `scripts/kalshi.py` / `tools/disruption_supply_spread.py` return every value, and no row, header or `CLAUDE.md` line maps row → command (§1). That is run #2's ORACLE finding, unchanged.

### 3.2 (c) — PERIMETER: does the instrument measure the thesis's subject? (first measurement; runs #1 and #2 did not report (c))

| (c) verdict | n / 39 | Rows |
|---|---:|---|
| MATCH | 18 | — |
| **SUPERSET** (instrument contains the subject) | 5 | BRK-007 (3 vehicles, none named) · MIDAS-I1 (≥4 roots, disclosed) · ORC-07 (any market, by design) · REG-3.01 (named "90+ DQ", graded on PDNA = 90+ **and** nonaccrual) · REG-17.04 (collateral quality graded on BDC equity NAV discount) |
| **SUBSET** (instrument sees part of the subject) | 4 | MIDAS-M2 (GSR only; silver −48% invisible — disclosed "BAND-BLIND") · MIDAS-I2 (outage-only, price-blind, disclosed) · RED-003 (nominal goods retail sales for "consumer spending") · ORC-09 (rotation graded on the S&P leg only) |
| **AMBIGUOUS** (instrument not pinned; two readings disagree) | 7 | BRK-003 / REG-17.01 (Medallia: which holder) · BRK-010 (which BDC median) · CRU-06 ("sector") · FAL IRAN-02 (UKMTO-tanker band vs PortWatch/Kpler reading) · ORC-08 (Polymarket meets Alert, Kalshi does not) · RED-002 (AHE vs AHETPI vs WGT) |
| CANNOT-EVALUATE | 5 | no instrument named to test (AEO-03, FAL IRAN-01, ORC-05 — desk has not read the contract's resolution bar, REG-9.01, REG-12.01) |

**Perimeter defect rate (SUPERSET + SUBSET + AMBIGUOUS): 16 / 39 = 41%**; disclosed on the row by the owner in 7 (MIDAS ×3, BRK-003, ORC-08, FAL IRAN-02, REG-3.01 partially), undisclosed in 9. Direction matters (WIRING_SWEEP.md:67, FLG's case fired toward FIRING): of the 9 undisclosed, REG-3.01 and REG-17.04 are superset-toward-firing (PDNA ≥ 90+DQ; equity discount moves before collateral does).

★ **The worst (c) instance is a cross-desk fork on one subject:** Medallia 1L is registered twice — `AGENTS/BROCK/workbook/VX.tsv:5` (`VX-BRK-003`, ladder 90–95 / 80–90 / <80¢, value **49.5¢ BCRED Q2-26**, non-accrual) and `AGENTS/REGINALD/workbook/VX.tsv:51` (`VX-REG-17.01`, ladder <90 / <85 / <80¢, value **78¢ BXSL Q4-25**, "OWNER-DEFERRED (BROCK)", unchanged since 2026-02-27). Two ladders, two holders, two vintages; root CLAUDE.md's "reconcile shared metrics to one figure" is not met, and REGINALD's deferral has no clock or pointer to BROCK's row.

### 3.3 Run #2's named MATERIAL desk instances — panel re-check (row md5 at `f1e620d7b` vs HEAD)

| Desk:row | Run #2 defect | Row 9/17 → HEAD | Status 10/8 |
|---|---|---|---|
| ORACLE `VX-ORC-04` | bands keyed to August WTI-00, readings September | CHANGED (Alert/Critical) | **SUPERSEDED** — v4 retired; v5 Oct 10 pinned (id 4936102, ICE venue disclosed); Alert/Critical **UNSET pending Will** ⇒ CANNOT-FIRE, disclosed |
| CRUISE `VX-CRU-04` | RED letter met since 7/2, score ORANGE | CHANGED (bands + Source) | **FIXED 2026-09-19** — re-cut to Big-3 count from 7/2, row cites the W2 packet |
| REGINALD `VX-REG-14.01` | % bands vs ¥ value; bands overlap | UNCHANGED | **NOT FIXED** — REGINALD deferred "VX row re-cuts to 9/30 deadline" (`1c0c870ac` msg); deadline passed 8d |
| REGINALD `VX-REG-8.01` | $/door ladder vs "Active FL/NV" | UNCHANGED | **NOT FIXED** (same deferral) |
| REGINALD `VX-REG-5.01` | defers to SAM's FROZEN ledger | UNCHANGED | **NOT FIXED** — SAM `VX.tsv` line 1 still `# FROZEN 2026-08-17` |
| REGINALD `VX-REG-14.03` | defers to `VX-SAM-9.02`, which does not exist | UNCHANGED | **NOT FIXED** — `grep -c '^VX-SAM-9.02' AGENTS/SAM/workbook/VX.tsv` → 0 |
| BROCK `VX-BRK-013` | "ladder inverted" | UNCHANGED | **NOT FIXED — and run #2's description looks wrong** (§6): Yellow/Orange are *dividend* coverage (x), Red is *asset* coverage (%); the defect is two unnamed metrics under one word, not an inversion. BROCK drained the packet 9/18 (`8a6cbcc93`) with no recorded disposition |

Panel: **1 FIXED · 1 SUPERSEDED (now CANNOT-FIRE, disclosed) · 5 NOT FIXED** of 7.

### 3.4 Schema census — the convention at population level (all 17 run-#2-live registries, header line only)

| Column the convention needs | Registries carrying it (of 17) |
|---|---|
| Instrument / Source column | 13 (none: AEOLUS · BOND · FERT/VX · ORACLE) |
| Instrument as its own column | 2 (FERT/TRIGGERS, FLG/TRIGGERS) |
| `Anchor_Type` | 1 (FLG) |
| Basis / window / sustain column | **0** |
| Revision-policy column | **0** |

Command: header line of each `workbook/{VX,TRIGGERS}.tsv` (`grep -v '^#' f | head -1`).

### 3.5 ⚠️ POOL BLIND SPOT — the convention already exists, outside the pool, at two of the "convention-defect" desks

Run #2's pool (and this run's, to stay comparable) reads only `workbook/`. Threshold registries outside it (`git ls-files 'AGENTS/*' | grep '\.tsv$' | grep -v /workbook/ | grep -iE 'thresh|trigger'`, minus views/logs/fixtures):

| Registry | State (`is_frozen`) | Rows | Basis-bearing columns | Cells filled (presence only) | Created |
|---|---|---:|---|---|---|
| `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` | LIVE | 12 | `threshold_value · sustain_window · instrument_basis · instrument_basis_operative` | 12/12 each; revision/vintage token 2/12 | 2026-05-06 |
| `AGENTS/REGINALD/registry/THRESHOLDS.tsv` | LIVE | 8 | `threshold_value · sustain_window · grading_instrument · value_basis` | 8/8 each; revision token 0/8 | 2026-05-10 |
| `AGENTS/HANS/registry/THRESHOLDS.tsv` | LIVE | 17 | `band · sustain · value_basis · scannable` | 17/17 each; revision token 0/17 | 2026-08-28 |
| `AGENTS/CREED/registry/THRESHOLDS.tsv` | FROZEN | 11 | — | — | — |

**37 live rows NOT-SEEN by the ⑰ pool, all with level + window + instrument cells present** (presence, not content — a pointer in a cell passes a presence test; not graded at content here). RED's boot evaluates its registry live (`AGENTS/RED/CLAUDE.md:125`). So for **RED and REGINALD the prescribed convention fix ("add an Instrument column / adopt Anchor_Type"; "a clock and pointer") already exists in the registry their machinery reads — since May**; their `VX.tsv` is a dashboard/counter-evidence surface whose bands are not the graded thresholds. Run #2's 5-desk convention diagnosis is therefore **3 clean convention defects (AEOLUS · FALCON · ORACLE) + 2 pool-definition questions (RED · REGINALD)**: either the pool includes `registry/`, or VX bands at desks with a machine registry are declared DASHBOARD-not-gate. REGINALD's OWNER-DEFERRED rows remain a real defect either way.

---

## 4. GATES leg — `PROME/GATES.tsv`, whole (appended `Thu Oct  8 15:09:18 EDT 2026`)

**Population:** 20 data rows (L3–L22; header L2; 1 comment line), 12 fields on every row (NF=12 ×20). vs run #2 (`f1e620d7b`): **16 carry forward · 4 added** (GATE-HOMER-THESIS-KILL · GATE-NEXUS-T12S-DFII10 · GATE-TERRY-VLO-HELD-01 · GATE-TERRY-VLO-SCALE) **· 4 removed** (GATE-REG-T02 · GATE-TERRY-007 · GATE-TERRY-ROLL70 · GATE-TERRY-USO135C; 4 terminal rows archived 10/03, `817acf59e`). Of the 16 carried, 9 had the `condition` cell rewritten since 9/17 (all grew). **Not like-for-like with run #2 (16/20 overlap), and run #2 was not like-for-like with run #1.** All 20 rows opened. NOT-SEEN: none.

### 4.1 Run #2's named GATES instances

| Row | Run #2 defect | Status 10/8 | Evidence |
|---|---|---|---|
| GATE-OSPREY-001 | `source` pointer dead | **FIXED 2026-09-17 13:12** | `dbf5155d5` (`git log -S "outbox/delivered/2026-07-23_to-PROME_cpc-day4"`); path exists |
| GATE-BRK-R2 | `scannable=INSTRUMENT`, no producer | **FIXED 2026-09-17 10:3x** | re-tagged JUDGEMENT, L408, provenance in the cell |
| GATE-LIQ-072 / -076 | `last_checked` 9/02 certified a check nobody ran | **FIXED** | 072 → 2026-10-01 14:25 consumer read of LIQUID memo; 076 → 2026-10-08 08:39 mirror of LIQUID owner grade (memo `eaff67bba`) |
| GATE-HY-REKILL | "LIQUID owes the fold" open 14d after discharge | **FIXED** | text absent at HEAD; `git log -S "owes the fold"` → `dbf5155d5` |
| 069 / 076 / 079 | Class-2 `CANNOT-FIRE` re-cut into non-canonical tokens | **PARTIAL** | 072 now renders leg 3 as canonical `CANNOT-FIRE`; 069 fired 2-of-2 9/26 (moot); **079 state still reads "FIRE legs UNGRADEABLE-until-banded"** (non-canonical; `STATE_VOCABULARY.md:50` defines this exact case as `CANNOT-FIRE`) |

**4 FIXED · 1 PARTIAL · 0 NOT FIXED.** The GATES side, owned by one desk with a review loop, cured its instances within hours of run #2; the desk side (§3.3) cured 1 of 7 in 21 days.

### 4.2 Re-measure

| Measure | Run #1 (n=29) | Run #2 (n=20) | **Run #3 (n=20)** |
|---|---|---|---|
| **(b) STATED (b-len)** | 24 = 83% | 18 = 90% | **16 = 80%** |
| (b) STATED (b-3) | — | — | 16 = 80% |
| (b) rule 7 (b-3 STATED + revision policy) | — | — | **8 = 40%** = 5 tokened (HY-REKILL · LIQ-076 · COT-35B · FLG-T08 · NEXUS-T12S) + 3 unrevised settlement/close prices N/A (ROLL70-EXIT · VLO-SCALE · VLO-HELD-01). Revision token present on 8 rows (case-insensitive regex over `condition` for: AS FIRST PUBLISHED · VINTAGE CONVENTION · GRADE-AT-PUBLICATION · FIRST PRINT · first-published), 3 of them on PARTIAL rows (069/072/079) |
| (a) NO-METRIC-SURFACE | 11 = 38% | 9 = 45% | **11 = 55%** |
| (a) COMMAND-NAMED | — | 10 | 4 (HY-REKILL `boot.py` · 079 ARM leg `boot.py` · COT-35B `cot_grade.py` · VLO-SCALE `fetch.py`) |
| (a) PRODUCER-EXISTS-UNCITED | 4 | 2 | 5 (072 · 076 · ROLL70-EXIT · NEXUS-T12S · VLO-HELD-01) |
| Pointer present / dereferences | 28 / 29 | 20 / **19** | **20 / 20** (every path in `source` + `definition_surface` exists; regex path check — §6) |
| `scannable=INSTRUMENT` with no producer | — | 1 (BRK-R2) | **0**; but 2 of 5 INSTRUMENT rows cite no command (ROLL70-EXIT, VLO-HELD-01 — producers exist: REGINALD `registry/REG_T02_EXIT_LOG.tsv`, TERRY own repro) |

**(b) PARTIAL rows (4):** GATE-LIQ-069 (leg 3 "AI-infra HY new-issue concessions widening" — no level) · GATE-LIQ-072 (leg 1 "3rd/4th similar IG issuer at BB-like spreads"; SpaceX leg "pricing-date pinning owed") · GATE-LIQ-079 (FIRE legs unbanded, owner proposal due 10/31) · GATE-OSPREY-001 (leg (b) "Kpler-confirmed liftings drop" — no magnitude).

**Decomposition 90% → 80%:** the 4 added rows are 4/4 STATED; the 4 removed rows are not re-graded here. All four PARTIAL rows **carried from run #2 and were PARTIAL on the 9/17 text too** (069/072/079's unlevelled legs and OSPREY's "drop" are in the `f1e620d7b` cells; OSPREY's condition is byte-identical). So the −10pp is **rater, not decay**: this reader fails a disjunctive gate when any leg is unlevelled; run #2 evidently passed them. On the run-#2 reading the GATES figure would be ~18–20/20. **Verdict: no measurable movement; GATES basis discipline remains far above the desk registries (80–90% vs 26–54%).** The (a) rise 45% → 55% is likewise a classification difference (no carried row lost a producer), not a regression.

### 4.3 New GATES instances (flags, not fixes)

| Row | Instance | Severity |
|---|---|---|
| GATE-LIQ-079 | `last_checked` = 2026-09-03 20:3x (35 days); FIRE legs CANNOT-FIRE until banded, proposal due 10/31 | WATCH (disclosed) |
| GATE-LIQ-076 | `last_checked` cell itself says "NO BOOT INSTRUMENT READS THIS GATE (wiring still owed)" | WATCH (disclosed) |
| GATE-BRENT-COT-35B | "4.909% … NOT re-reproduced since 8/13; BRENT owes the reproduction (REGISTRY:131)" — a GATING leg's frozen base, 56 days unreproduced | **MATERIAL-IF-WRONG** (a gating constant no one has re-derived) |
| GATE-TERRY-ROLL70-EXIT · GATE-TERRY-VLO-HELD-01 | `scannable=INSTRUMENT` with no command named in any cell | COSMETIC (producer exists) |

---

## 5. Owner asks — flags for DAEDALUS to packet (this reader sent nothing) (appended `Thu Oct  8 15:10:31 EDT 2026`)

| # | Owner | Ask (one line) | Leg |
|---|---|---|---|
| 1 | **DAEDALUS** | The convention fix run #2 named as "the next pass" was never packeted — send AEOLUS, FALCON and ORACLE the one-line convention ask, or record why not. | ⑰ |
| 2 | **DAEDALUS** | Rule the pool: include `AGENTS/*/registry/*THRESHOLDS*/*TRIGGERS*.tsv` (37 live rows), or declare VX bands DASHBOARD-not-gate at desks with a machine registry (RED, REGINALD, HANS). | ⑰ |
| 3 | **DAEDALUS** | Add correction banners to the run #2 W2 record: FROZEN 481/829 = 58% is 380/829 = 46% by `is_frozen()`; "6 of 8" is 5; BRK-013 is mixed-metric, not inverted. | ⑰ |
| 4 | **DAEDALUS** | Save the drawn sample (desk, line, ID) with every seeded run; run #2's 40 rows cannot be reconstructed. | ⑰ |
| 5 | AEOLUS | `workbook/VX.tsv` is a state log with no level/instrument columns; 5 rows added since 9/17 in the same form. Name in one header line where each channel's level and instrument live. | ⑰(a)(b) |
| 6 | FALCON | `VX.tsv:4` (IRAN-02) bands are on UKMTO tanker counts while readings are PortWatch/Kpler, and Current cites a "<10 DEEPENING band" absent from the band columns. | ⑰(b)(c) |
| 7 | ORACLE | 5 of 5 sampled rows have a working producer (`polymarket.py`, `kalshi.py`, `tools/*.py`) and none cites it. Add one row→command map. | ⑰(a) |
| 8 | ORACLE | `VX.tsv:8` (ORC-07) holds 🔴 on Δ7d/Δ30d moves against a 48h letter; `:9` (ORC-08) Alert is met on Polymarket and not on Kalshi — pin the venue. | ⑰(b)(c) |
| 9 | RED | `VX.tsv:4` (RED-002) Flip_If names no wage series; it fired on AHE and was re-checked on AHETPI. `:3` (RED-001) Flip_If does not say AND or OR. | ⑰(b)(c) |
| 10 | REGINALD | `VX.tsv:37/:23/:9/:39` are unchanged 8 days past your own 9/30 re-cut deadline (`1c0c870ac`); `:39` still defers to `VX-SAM-9.02`, which does not exist. | ⑰ ㉓ |
| 11 | REGINALD + BROCK | Medallia 1L is registered twice: `REGINALD VX.tsv:51` 78¢ BXSL Q4-25 vs `BROCK VX.tsv:5` 49.5¢ BCRED Q2-26, on different ladders. Reconcile to one figure and one ladder. | ⑰(c) |
| 12 | BROCK | `VX.tsv:15` (BRK-013) uses "coverage" for dividend coverage (x) and asset coverage (%). Name both metrics on the row. | ⑰(b) |
| 13 | CRUISE | `VX.tsv:7` (CRU-06) band "sector move" names no basket or window; the separate CCL−RCL falsifier is fully based. | ⑰(b) |
| 14 | PROME | `GATES.tsv:7` (LIQ-079) state reads "UNGRADEABLE-until-banded"; `STATE_VOCABULARY.md:50` names this case `CANNOT-FIRE`. | ⑰ vocab |
| 15 | BRENT (via PROME) | `GATES.tsv:12` (COT-35B) Leg B's gating base 4.909% has not been re-reproduced since 8/13 (REGISTRY:131). | ⑰ GATES |

---

## 6. Doubts and limits (stated so nothing reads cleaner than it is)

1. **Run #2's (b) rubric was never written down.** b-len is calibrated on one desk only (MIDAS, 5 identical rows, this reader one row stricter). On GATES the same reading gives 16/20 where run #2 gave 18/20 on mostly identical text. Read the (b) series as ±1–2 rows of rater noise plus about ±16pp of sampling noise.
2. **Run #2's rows cannot be recovered**, so run #3 holds the desks fixed and redraws the rows. Run #2 → run #3 compares the same desks on different rows, not the same rows over time. The 7-row named-instance panel (§3.3) is the only true panel.
3. **The (a) COMMAND-NAMED / UNCITED split is not comparable** across runs (§3.1). Only NO-METRIC-SURFACE and the producer-exists total are comparable.
4. **(c) is a first measurement by one reader from row text only.** No external primary was fetched for any (c) or (b) verdict; every value is read as the desk states it.
5. **Errors found in run #2's record** (W2, carried into `_JUDGMENT.md:9,24`): (i) FROZEN screen counted CREED, HAWK and MARCO as FROZEN; all three are LIVE by banner and by `is_frozen()`. (ii) "6 of 8 desks are CONVENTION defects": its own table lists 5 plus MIDAS "CONVENTION-CLEAN". (iii) BRK-013 "inverted ladder" is more plausibly two unnamed metrics. (iv) FALCON "no Source/as-of columns": the header carries `Source` and `Last_Updated`; what is missing is a basis. None of these changes the (b) series. (i) changes the base-rate sentences.
6. **The pool excludes `registry/`**: 37 live rows (RED 12, REGINALD 8, HANS 17) are NOT-SEEN at content. Only cell presence was counted, and a pointer in a cell passes a presence test.
7. **The pointer check is path-existence only** (regex over `source` and `definition_surface`). § anchors, line numbers and commit hashes inside cells were not resolved.
8. **Legs not run:** DISCHARGEABLE-BY-TOKEN-GESTURE and DISCHARGED-BY-ASSERTION were not re-measured (brief scoped to a/b/c). One observation in passing: REGINALD (`1c0c870ac`) and BROCK (`8a6cbcc93`) filed their 9/17 ⑰ packets to `processed/` with the rows unchanged. REGINALD wrote a dated deferral, now past; BROCK recorded no disposition. A packet counted as processed is not a row counted as fixed.
9. **Size:** this record is about 40 KB, over the 32,550 B read cap that binds boot-read surfaces. It is a run record, not boot-read. A reader truncating at the cap loses §5–§6, so §0 is placed first.
10. **Stamps:** every section stamp is `date` output from the same append command. The §1 stamp was corrected once in-file from a typed placeholder to the command's own output (14:59:58).
