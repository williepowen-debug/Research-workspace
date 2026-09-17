# Registered-Gate Basis Sweep — run #1, VINTAGE-CHECK leg (procedure steps 1, 4, 5, plus step-3 owner-surface reconciliation and the pipeline-keying leg)

**Date:** 2026-09-17 (Thu) · **Reader:** DAEDALUS fan-out reader (read-only) · **Perimeter file:** `PROME/GATES.tsv` (22 lines; 1 comment header + 1 column header + **20 gate rows**, L3–L22)
**Playbook:** `AGENTS/DAEDALUS/sweeps/GATE_BASIS_SWEEP.md` · **Canon:** `FORGE/PREDICTION_DISCIPLINE.md` § Registration (incl. FROZEN-ON-REVISABLE, L6) · `AGENTS/DAEDALUS/BLUEPRINTS/SPEC_LETTER_STANDARD.md` SL-5 (L34–L36)
**Not in this record:** step 2 (blind grade-read, other readers) · step 3 negative control on the retrieval path (done by DAEDALUS this morning — ALFRED path `VINTAGE-PATH-VERIFIED`; **not redone here**). **Dispositions are not mine** — no packets written; each gate carries the one-line re-registration ask its owner would receive.

---

## 1. PERIMETER — every non-comment row classified (20 of 20, none skipped)

| # | gate_id | line | owner | state | IN-SCOPE? | reason |
|---|---|---|---|---|---|---|
| 1 | GATE-HY-REKILL | L3 | LIQUID | LIVE | **IN-SCOPE** | FRED `BAMLH0A0HYM2` |
| 2 | GATE-LIQ-069 | L4 | LIQUID | LIVE (ARMED 1-of-2) | **IN-SCOPE** | FRED `BAMLH0A1HYBB` / `BAMLH0A3HYC` / `BAMLH0A0HYM2` + official equity closes (L1/L4); L2/L3/L5 judgment limbs graded inside |
| 3 | GATE-LIQ-072 | L5 | LIQUID | LIVE | **IN-SCOPE** | FRED `BAMLC0A0CM` |
| 4 | GATE-LIQ-076 | L6 | LIQUID | LIVE | **IN-SCOPE** | CFTC TFF weekly · NY Fed PD weekly · MOVE/VIX closes |
| 5 | GATE-LIQ-079 | L7 | LIQUID | LIVE / NOT ARMED | **IN-SCOPE** | NY Fed SOFR 99th pct · IORB (ARM leg); FIRE legs owner-declared UNGRADEABLE |
| 6 | GATE-FALCON-001 | L8 | FALCON | LIVE (legs 1+3 FIRED, leg 2 OPEN) | **IN-SCOPE** | TankerMap Bab tanker-transit series (leg 2, the pending leg); Yanbu weekly loadings (leg 3, fired) |
| 7 | GATE-OSPREY-001 | L9 | OSPREY | LIVE (leg b FIRED; a/c OPEN) | **NOT GRADED** (event gate) | the two PENDING legs are an assessment RESULT (SPM structural damage) and a corporate DECLARATION (Tengiz force majeure) — no published series; the one series-keyed leg (b, Kpler liftings) already FIRED 7/24 |
| 8 | GATE-NEXUS-SEAT-01 | L10 | NEXUS/PROME | LIVE | **NOT GRADED** (judgment gate) | counts Will's decisions by proximate input; no published series |
| 9 | GATE-OP-SCALE-01 | L11 | TERRY/PROME | LIVE | **NOT GRADED** (judgment gate) | internal closed-position count; no published series |
| 10 | GATE-BRENT-COT-35B | L12 | BRENT | LIVE | **IN-SCOPE** | CFTC disaggregated COT `f_disagg.txt` |
| 11 | GATE-FERT-G5 | L13 | FERT | LIVE | **IN-SCOPE** | DTN Progressive Farmer weekly retail $/ton |
| 12 | GATE-FERT-G3 | L14 | FERT | LIVE | **NOT GRADED** (event gate) | MOFCOM/NDRC policy act; owner-declared un-base-rateable at registration (n≈2 regime changes/12mo) |
| 13 | GATE-TERRY-007 | L15 | TERRY/BOND | LIVE (0-of-5) | **IN-SCOPE** | FRED `DGS10` official closes |
| 14 | GATE-REG-T02 | L16 | REGINALD/WAL/Will | **RESOLVED (FIRED 9/1)** | **NOT GRADED** (RESOLVED) | terminal; successor guard is row 18 |
| 15 | GATE-CORAL-MSI-01 | L17 | CORAL/Will | LIVE (leg stood down 9/13) | **IN-SCOPE** | Parcl metro Motivated Seller Index |
| 16 | GATE-FLG-T08 | L18 | FLG/PROME | LIVE | **NOT GRADED** (date-keyed event gate) | fires on the NYC RGB order's effective date 2026-10-01 — an administrative effective date, not a series. ✅ note: it is the only NOT-GRADED row that already carries an explicit REVISION POLICY (`GRADE-AT-PUBLICATION`) |
| 17 | GATE-TERRY-ROLL70 | L19 | TERRY/REGINALD/Will | **RESOLVED (FILLED 9/2)** | **NOT GRADED** (RESOLVED) | terminal |
| 18 | GATE-TERRY-ROLL70-EXIT | L20 | REGINALD/TERRY/Will | LIVE (0-of-3) | **IN-SCOPE** | WAL official closes (Yahoo via `scripts/market.py`) |
| 19 | GATE-TERRY-USO135C | L21 | TERRY/Will | **RESOLVED 9/9** | **NOT GRADED** (RESOLVED) | terminal; position closed |
| 20 | GATE-BRK-R2 | L22 | BROCK | LIVE | **IN-SCOPE** | SEC tender filings (SC TO-I/A), filing-primary — "filings" named in the playbook perimeter |

**IN-SCOPE: 12 · NOT GRADED: 8** (3 RESOLVED · 4 judgment/event · 1 date-keyed event).

---

## 2. SUMMARY TABLE — the 12 in-scope gates

| gate | owner | obs the grade reads | unnamed elements | **verdict** | base-rate operator (SL-5c) | revisable? (WQ-175) | pipeline keying |
|---|---|---|---|---|---|---|---|
| GATE-HY-REKILL | LIQUID | **2** (+ every published print as a reset-reader) | — | **BASIS-NAMED** | ✅ **MATCHED** — `0 of 177` 2026 obs strictly `<260`, computed on the letter's own strict `<` (`KILL_MEMO_HY_OAS_260.md:51,78`). Doubles as an SL-5(e) realisation declaration in the letter's own unit | ICE/FRED index; letter NAMES `AS FIRST PUBLISHED` ⇒ compliant; pre-9/4, annotated | ⛔ **ARRIVAL on vintage** — `fetch.py:330-357` sends no `realtime_start`; `boot.py` crun is IDENTITY on (series, date-order) only |
| GATE-LIQ-069 | LIQUID | **≥3** L1 · **2** L2 · n/a L3 · **2–10** L4 · **1/action** L5 | published precision + tie (L1, L4) · reset rule (L1 5-session window) · operator strictness (L4 `−15%/session`) | **BASIS-UNNAMED** (precision/tie · reset · L4 strictness) | **CANNOT-EVALUATE** — no base-rate computation on file | pre-9/4; vintage NAMED as-first-published | same FRED path — ARRIVAL on vintage |
| GATE-LIQ-072 | LIQUID | **1** (IG OAS) · **2** (SpaceX endpoints, **UNPINNED since 7/9**) · source-named-at-grade legs | pricing-date endpoints (SpaceX leg, owner-owed 70 days) · precision + tie (`>94` carries no decimal) | **BASIS-UNNAMED** (endpoint dates · precision/tie) | **CANNOT-EVALUATE** — none on file | pre-9/4; vintage NAMED | same FRED path — ARRIVAL on vintage |
| GATE-LIQ-076 | LIQUID | **up to ~8** (W1 ≤4 · W2 1–2 · W3 2, any 2-of-3 in a rolling 2wk window) | precision + tie (all three legs) · reset rule · MOVE vendor (two producers named across surfaces) | **BASIS-UNNAMED** (precision/tie · reset) **+ cell-vs-letter referent disagreement** (§3) | **CANNOT-EVALUATE** as a base rate (letter carries context only: "~4× the largest cover in the 30-wk history") | pre-9/4; vintage NAMED; **CFTC re-issues COT and NY Fed restates PD** | not scripted — hand-graded from primaries |
| GATE-LIQ-079 | LIQUID | **≥4** (SOFR99 + IORB on each of ≥2 consecutive non-calendar days). FIRE legs: **0 gradable** | precision + **rounding order on a DERIVED spread** (round the legs or the difference?) · tie at exactly +30.0 · reset rule · FIRE-leg thresholds (owner-declared, dated) | **BASIS-UNNAMED** (precision/tie · rounding order · reset) — ARM leg; FIRE legs owner-declared UNGRADEABLE with a dated 10/31 proposal ✅ | ✅ **MATCHED** — `2 of 8 non-calendar episodes (n=1 true positive)` computed WITH the ≥2-consecutive persistence leg the letter carries (`FUNDING_SEIZURE_GATE_SCOPED.md:27`). ⚠ owner's own R4 caveat: census built in an RRP-buffered regime (`:52`) | pre-9/4; vintage NAMED; **NY Fed revises SOFR** | `boot.py` daily ARM detection; no vintage parameter |
| GATE-FALCON-001 | FALCON | leg 2 (the pending one): **≥3** (≥2 print-days + the "prevailing 7dma" reference). legs 1/3 FIRED | ⛔ **operator/boundary — there is NO magnitude at all** ("a step-down"; the number 8 explicitly de-registered) · "prevailing" reference window · precision/tie · reset · "enforcement-attributable" has no instrument | **BASIS-UNNAMED (operator/boundary, reference window, precision, tie, reset)** | **CANNOT-EVALUATE** — none on file | pre-9/4; TankerMap restates nothing declared | `scripts/hormuz_transit_watch.py` is PortWatch-only (corroborator, cannot fire leg 2); leg 2's own reads are manual. PortWatch script keys on print date + alarms >10d lag ⇒ IDENTITY |
| GATE-BRENT-COT-35B | BRENT | **2 fields from 1 weekly print** (MM gross shorts, OI) + **8 FROZEN basis obs** in the base median | **vintage convention** (CFTC re-issues COT reports; the cell's "re-read every print, never a latch" is a re-read rule, not a vintage choice) | **BASIS-UNNAMED (vintage)** — the only gap; operator/boundary is the register's best-specified (MECE, exhaustive, ties resolved) | ✅ **MATCHED** — accepted NO-VERDICT rate **33.6%** computed on the registered band itself (`REGISTRY.tsv:131`; build `setups/2026-08-12_35b-COT-successor-band-N1-build.md`) | **YES — CFTC re-issues.** Registered 8/14, pre-9/4 ⇒ **annotated, grades as-first-published** | ✅ **IDENTITY** — `cot_grade.py:127,147-151` verifies `report_date` IN-ROW against `--expect`, **exit 3 = NOT FRESH, DO NOT GRADE**; market matched by NAME (`:95-100`). ⚠ a CFTC **re-issue of the same report_date** would be silently adopted |
| GATE-FERT-G5 | FERT | **2 per weekly print** (DAP, MAP; OR-joined) | vintage convention · published precision (DTN prints whole $) · tie at exactly $1,000 | **BASIS-UNNAMED (vintage, precision/tie)** | ⛔ **OPERATOR-MISMATCH — and worse: series + unit + frequency mismatch** (see §4) | pre-9/4 ⇒ annotated | no producer — `scannable` correctly re-tagged JUDGEMENT 8/28; owner grades at the T4 wake |
| GATE-TERRY-007 | TERRY/BOND | **5 consecutive closes** (+ each ≥4.50 close as a reset-reader) | vintage convention (H.15/DGS10 IS revised) · **reset rule for the EXIT counter** | **BASIS-UNNAMED (vintage, exit-count reset)** — precision + tie + consecutiveness are all NAMED and exemplary | **CANNOT-EVALUATE** — none on file | pre-9/4 (registered 8/19) ⇒ **annotated, grades as-first-published** | ⛔ **ARRIVAL on vintage** — `fetch.py fred DGS10` returns latest-revised |
| GATE-CORAL-MSI-01 | CORAL/Will | **10** (5 metros × 2 readings) + 2 vintage stamps for the spacing leg | **the five-metro SET is not enumerated in the frozen letter** · which clock governs spacing (observation date vs page `Updated:` stamp — they disagreed 11d vs 10d at the live grade) · precision · tie at exactly 6.00 · reset · **no re-fire condition registered** (owner-flagged, WQ-241) | **BASIS-UNNAMED (metro set, vintage clock, precision/tie, reset)** | **CANNOT-EVALUATE** — none on file | pre-9/4 (8/23) ⇒ annotated | no producer; owner pulls Parcl direct, triple-verified per value (`<title>`/`og:description`/JSON) |
| GATE-TERRY-ROLL70-EXIT | REGINALD/TERRY/Will | **3 consecutive closes** (+ each non-qualifying close as a reset-reader) | published precision · tie at exactly 81.90 · **settled-bar rule** (exists in owner practice since 9/14, not in the letter) | **BASIS-UNNAMED (precision/tie, settled-bar/vintage)** — series, unit, basis, operator, consecutiveness, reset all NAMED | **CANNOT-EVALUATE** — none on file. ⚠ the one adjacent figure (TERRY's ~1-in-5) is flagged on the row itself as an UPPER BOUND measured at a different level, distribution not re-run | pre-9/4; `unadjusted` in `THRESHOLDS.tsv:3` IS the equity-restatement declaration ✅ | ⛔ **ARRIVAL** — `scripts/market.py:28-29` reads `regularMarketPrice` with a silent `previousClose` FALLBACK and takes **no date argument at all**. ✅ **IDENTITY re-imposed at the ledger**: `REG_T02_EXIT_LOG.tsv:1` = one row per **SETTLED** regular-session close |
| GATE-BRK-R2 | BROCK | **(a) 3 consecutive quarterly prints**, each itself an aggregation of that quarter's offer(s) · **(b) 1 quarter** | vintage (preliminary vs **final** SC TO-I/A) · operator strictness ("sub-100%", "<25%") · precision of an issuer-stated proration · reset rule | **BASIS-UNNAMED (vintage, operator strictness, precision/tie, reset)** — unit and prospective window are exemplary | **CANNOT-EVALUATE** — out-of-sample 4-for-4 at BREIT+SREIT exists (`research/2026-09-03_WQ158_OUT_OF_SAMPLE_RESULTS.md`), but with strictness undeclared on BOTH the letter and the computation, "same operator" is not checkable | **YES — an SC TO-I/A is by construction an AMENDMENT.** Registered 9/3, pre-9/4 ⇒ annotated — **and the annotation collides with practice** (§5) | filing-primary, hand-graded; `instrument_check.py` probes reachability only, does not grade on the row's `direction`/`threshold` cells |

**Tally: BASIS-NAMED 1 · BASIS-UNNAMED 10 · OPERATOR-MISMATCH 1.**

---

## 3. STEP 3 — GATES cell vs the owner letter at `definition_surface` / `source`

Opened for all 12. Eight agree; **four disagree**, each with both locators.

### ❌ D1 — GATE-HY-REKILL: the GATES cell asserts an owed fold that was discharged 14 days ago
- `PROME/GATES.tsv:3` (condition cell, final clause): *"definition_surface does NOT yet hold this letter — **LIQUID owes the fold** (the ruled exception in header ENVELOPE COLUMNS)"*
- `AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md:45-49`: *"★ GATE-HY-REKILL — THE CANONICAL LETTER … **folded here 2026-09-03** — this file is the registry's `definition_surface`"*, carrying the letter **verbatim** at `:47`.
- Fold commit `28a5e3be0` (2026-09-03, *"WQ-162 letter FOLDED into its definition surface"*).
- **Verdict: REFUTED.** The obligation is discharged; the cell still advertises it as open. The cell is also, on its own words, the canonical home — so a reader is told the canonical letter is elsewhere *and* that elsewhere does not have it.

### ❌ D2 — GATE-BRENT-COT-35B: the owner registry cell carries the pre-9/06 Leg-A form and the truncated base
- `PROME/GATES.tsv:12`: *"crude MM gross shorts vs FROZEN base **122,904.5** … **carry the .5 or the levels do not reproduce**. Leg A: **≤109,164 SPENT | 109,165-118,325 NO-VERDICT (deadband decisive; 113,745 is its CENTRE, not a boundary)** | ≥118,326 NOT-SPENT."*
- `AGENTS/BRENT/workbook/REGISTRY.tsv:131` (notes): *"base **122,904** = trailing-8wk median … **Leg A bar: shorts <= 113,745 = SPENT.** NO-VERDICT deadband 109,165-118,325."*
- `AGENTS/BRENT/scripts/cot_grade.py:69-77`: *"CORRECTED 2026-09-06: the base is NOT an integer … **Displaying it truncated as 122,904 is what made the frozen letter fail its own arithmetic check for three independent blind readers**"*; `leg_a()` at `:103-108` implements the GATES form (deadband decisive), not the registry's.
- **Verdict: REFUTED — the owner surface is the stale one.** The registry cell states an operator (`≤113,745 ⇒ SPENT`) that is internally inconsistent with its own next sentence and would grade a 110,000 print SPENT where letter and script both say NO-VERDICT. GATES ✅ · script ✅ · owner registry ❌. Machine-readable columns on the same row compound it: `direction=below`, `threshold=113745` (cols 6/7) — **latent, because `instrument_check.py` does not grade on them**, but it is the exact pair a future consumer would read.

### ❌ D3 — GATE-LIQ-076: the GATES cell carries a MOVING referent where the letter froze a number
- `PROME/GATES.tsv:6`: leg (a) = *"SOFR-3M lev short **at/past record** or >300K single-week cover"*.
- `AGENTS/LIQUID/workbook/DEALER_POSITIONING_NEXUS_WATCH.md` §Fire conditions, W1: *"SOFR-3M lev net beyond **−2,950,000** contracts (new record past the −2,943,898 [6/30] peak) **OR** a one-week cover >300,000 contracts"*.
- **Verdict: DISAGREEMENT.** "At/past record" is a TRACKED referent that migrates every weekly print; the letter is FROZEN at a stated number. `finding_threshold_level_is_a_measurement_not_a_constant` — the three-valued menu in `FORGE/PREDICTION_DISCIPLINE.md:5`. The letter is right and the summary decayed.
- Second, smaller: the GATES cell names no producer for W3's MOVE leg ("vendor named at grade"); the letter names **two** — *"FORGE fetch.py ^MOVE"* and *"VIOLET's figure governs"*. Not contradictory on today's numbers; it is an unresolved producer choice sitting on a leg whose bar (MOVE>85) is ~10 points away.

### ❌ D4 — GATE-BRK-R2: the two surfaces carry different review dates
- `PROME/GATES.tsv:22` `review_by`: **2026-10-31**.
- `AGENTS/BROCK/workbook/PC_REDEMPTION_REGISTER.tsv:1` (escalation-line header): *"GATES row GATE-BRK-R2, owner BROCK, INSTRUMENT, **review 2026-11-15**, definition_surface = THIS FILE"*.
- **Verdict: DISAGREEMENT (16 days).** Not a basis element, but it is a clock on a gate whose earliest third read (OCIC Q3 final, ~late Oct) falls **between** the two dates — so the two surfaces disagree about whether the gate is reviewed before or after its own earliest fire.

### ✅ Agreements worth recording
- **GATE-CORAL-MSI-01** — GATES `:17` is explicitly summary+pointer and says so; `AGENTS/CORAL/STATUS.md:92-104` holds the verbatim frozen letter and declares itself canonical under PAT-006. Content agrees.
- **GATE-TERRY-ROLL70-EXIT** — GATES `:20`, `AGENTS/TERRY/setups/WAL_dec18-70P-duration-roll_2026-09-01.md:7,56`, `AGENTS/REGINALD/registry/THRESHOLDS.tsv:3` and `REG_T02_EXIT_LOG.tsv:1-4` all carry `≥81.90 × 3 consecutive` with the same reset. Four surfaces, one figure.
- **GATE-LIQ-069 / 072 / 079 / HY-REKILL** — the WQ-162 vintage convention is mirrored verbatim on each owner surface (`KB.tsv` KB-LIQ-069/072 notes; `FUNDING_SEIZURE_GATE_SCOPED.md:37`; `DEALER_POSITIONING_NEXUS_WATCH.md:10`). The mirroring is clean; the leg-label map flag at `DEALER_POSITIONING_NEXUS_WATCH.md:10` (*"the registry's `last_checked` cell says a TFF print graded leg (c)"*) was returned to PROME 9/3 and I did not re-verify whether it landed.
- **GATE-FALCON-001** — `AGENTS/FALCON/domain/FRESH_LEG_BASELINE.md:48-49,66` confirms PROME's condition summary as drafted, with one named non-blocking preference (the word "FRESH" omitted from the leg-2 clause). Owner-adjudicated, agreed.

### ⚠ D5 — a cross-surface note that is not a cell disagreement but is now false
`AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md:59` item 6: *"**Vintage verification path: NOT available from this box.** FRED's `fredgraph.csv?...&vintage_date=` returns HTTP 200 and SILENTLY IGNORES the parameter (OTTO `9cdd27494`; n=3 independent failures incl. **ALFRED 404s**)."* The WQ-162 vintage convention on **four** LIQUID surfaces is justified by that SEARCH-NOT-FOUND. Per today's step 3 the ALFRED path is **VINTAGE-PATH-VERIFIED**. The convention itself is unaffected (it is a rule on what the grader does, and it is the right rule), but its stated *reason* is refuted on four surfaces, and the door it closed — "any future vintage check must carry a negative control" — is now open.

---

## 4. STEP 4 — base-rate operator check (SL-5c)

| gate | base rate on file? | operator it was computed on | operator the letter carries | verdict |
|---|---|---|---|---|
| GATE-HY-REKILL | ✅ `0 of 177` (2026 obs strictly <260, own FRED pull 9/2) — `KILL_MEMO_HY_OAS_260.md:51,78` | **strict `<260`** | **strict `<260.0`** | ✅ **MATCHED.** Also satisfies SL-5(e): a realisation figure, in observations, the letter's own unit. `0 of N` is a complete declaration |
| GATE-LIQ-079 | ✅ `2 of 8 non-calendar episodes`, n=1 true positive — `FUNDING_SEIZURE_GATE_SCOPED.md:27` | `≥+30bp` **with** the ≥2-consecutive persistence leg | `≥+30bp` **AND** non-calendar **AND** ≥2 consecutive | ✅ **MATCHED.** ⚠ owner's R4 (`:52`): census built in an RRP-buffered regime — *"do not treat sign-off as calibration"* |
| GATE-BRENT-COT-35B | ✅ accepted NO-VERDICT rate **33.6%** — `REGISTRY.tsv:131` | the registered three-branch band itself | same band, MECE | ✅ **MATCHED** |
| **GATE-FERT-G5** | ✅ but on the **wrong instrument** — `PROME/inbox/processed/2026-08-17_from-FERT_gate-proposals-base-rated-plus-three-asks.md:40` | **Pink Sheet DAP $781.3/mt**, *"93rd pct of 2016–2026 (only 7.1% of **months ≥**$780/mt)"* — **non-strict `≥`, monthly, $/mt** | **DTN Progressive Farmer weekly retail, strict `>` $1,000/ton** — and the condition cell's own words are *"**NEVER conflate w/ Pink Sheet $/mt** or NOLA $/st"* | ⛔ **OPERATOR-MISMATCH**, compounded by series + unit + frequency. ★ **The same packet catches the identical defect one row down**: `:44` for G4 — *"The base rate is computed on Pink Sheet urea E. Europe FOB $/mt … **The gate names NOLA $/st — a different instrument**"* — and the correction was written for G4 and not applied to G5, in the same table, by the same author, in the same pass |
| GATE-BRK-R2 | out-of-sample 4-for-4 (BREIT, SREIT) — `AGENTS/BROCK/research/2026-09-03_WQ158_OUT_OF_SAMPLE_RESULTS.md` | "sub-100%" — strictness undeclared | "sub-100%" — strictness undeclared | **CANNOT-EVALUATE.** With the operator undeclared on both sides, sameness is unverifiable in either direction. ✅ the desk did the harder half well: `PC_REDEMPTION_REGISTER.tsv:1` refuses to fire (b) on OCIC 22.82% *because that observation helped PLACE the level* — a design statistic, self-excluded |
| LIQ-069 · LIQ-072 · LIQ-076 · FALCON-001 · TERRY-007 · CORAL-MSI-01 · ROLL70-EXIT | ✗ none on file | — | — | **CANNOT-EVALUATE** (7 of 12) |

**Run-#1 result on the one-time leg: 1 OPERATOR-MISMATCH (FERT-G5), 3 MATCHED, 1 uncheckable-by-construction, 7 with no computation on file.**

---

## 5. STEP 5 — revisable-series check (WQ-175 FROZEN-ON-REVISABLE)

Forward-only. **Every in-scope letter was registered before 2026-09-04** (latest: GATE-BRK-R2, 2026-09-03 — one day inside). So **all 12 are ANNOTATED, never re-graded**, and each *"grades as-first-published"* under WQ-162.

| gate | series restated by its issuer? | letter carries formula + dated illustration + recompute + named resolving vintage + revision watch? | annotation |
|---|---|---|---|
| GATE-HY-REKILL | ICE BofA via FRED — occasional restatement | **partially, and the best in the register**: no formula is needed (a bare level on a level series), vintage NAMED (`AS FIRST PUBLISHED`), a revision rule IS registered (*"a revision arriving before a count closes is noted, never substituted"*, and closed-count rules at `KILL_MEMO:54`) — no dated catalyst row, so the revision watch is a rule, not a clock | **pre-9/4, grades as-first-published** — compliant in substance |
| GATE-LIQ-069 / 072 / 076 / 079 | FRED OAS indices · **CFTC re-issues COT** · **NY Fed restates PD and SOFR** | vintage NAMED as-first-published on all four (WQ-162 mirror); no revision watch, no recompute instruction — none needed (all four are bare LEVELS, not computed thresholds) | **pre-9/4, grades as-first-published** |
| **GATE-BRENT-COT-35B** | ✅ **YES — CFTC re-issues COT reports** | ⛔ **NO vintage convention at all.** The threshold IS computed (base = an 8-obs trailing median of a revisable series; bar = base − 1.0 median_unit), which is exactly the FROZEN-ON-REVISABLE shape — and the cell freezes the NUMBER (`122,904.5`), not the formula. Mitigations already on the row: the formula is reproducible in `cot_grade.py:74-76`, re-basing is explicitly gated on a new N1 build + a Will ruling, and *"REVERT: re-read every print, never a latch"* forces a fresh read. What is missing is the **resolving-vintage name** — first print or re-issue? | **pre-9/4, grades as-first-published** ⇒ **the first print of each report_date governs**; a CFTC re-issue would be silently adopted by `cot_grade.py` today (it matches on `report_date`, not on vintage) |
| **GATE-BRK-R2** | ✅ **YES — an SC TO-I/A is an amendment by construction** | ⛔ **NO vintage convention.** And the annotation **collides with the register's own practice**: WQ-162 pre-9/4 default = as-first-published ⇒ the PRELIMINARY filing; the register grades the **FINAL** SC TO-I/A (`PC_REDEMPTION_REGISTER.tsv:2`: *"OCIC's Q3 **final** SC TO-I/A ~late Oct"*; *"the Q3 10-Q ~11/13 carrying the **FINAL DOLLAR VALUE** of the second print"*). Registered 9/3 — **one day** before the rule that would have caught it | **pre-9/4, grades as-first-published** — ⚠ and the owner is in fact grading a later vintage. This is the one place where the annotation and the practice point at **different numbers**, and nothing on either surface reconciles them |
| GATE-FERT-G5 | DTN — no published revision schedule located; membership call is the owner's | no vintage convention | **pre-9/4, grades as-first-published** |
| GATE-TERRY-007 | ✅ **H.15/DGS10 is revised** | no vintage convention; precision/tie/consecutiveness exemplary (`FLOW-TRIGGER_duration-TLT-put.md:18`) | **pre-9/4, grades as-first-published** — ⚠ and the grading pipeline cannot deliver that vintage (§6) |
| GATE-CORAL-MSI-01 | ✅ Parcl recomputes its index; pages re-stamp | no vintage convention; **two clocks in use at the live grade and neither declared governing** (11d observed / 10d by page vintage) | **pre-9/4 (8/23), grades as-first-published** — first-published = the page as first stamped, which is the reading the owner in fact used |
| GATE-TERRY-ROLL70-EXIT | ✅ Yahoo back-adjusts (splits/dividends) **and** publishes in-progress bars | ✅ **`unadjusted` declared** at `THRESHOLDS.tsv:3` — the correct equity-restatement declaration, and the only one in the register. ⛔ the **in-progress-bar** vintage is undeclared; the owner's working rule (a settled bar is one whose **volume has stopped moving**, TERRY+REGINALD 2026-09-14, `GATES.tsv:20`) lives only in a `last_checked` cell | **pre-9/4, grades as-first-published** |
| GATE-FALCON-001 | TankerMap — unknown; no schedule located | leg 2 has no threshold to freeze, so the question does not reach a number | **pre-9/4, grades as-first-published** |

**No in-scope letter is a bare number on a payrolls/GDP/JOLTS/CPI-class series, so no `BASIS-UNNAMED (vintage)` is raised under §5's bare-number clause alone.** The two that carry the FROZEN-ON-REVISABLE *shape* (BRENT-COT-35B, BRK-R2) are both pre-9/4 and both take the new kind at their **next owner touch**, per the canon's own transition clause.

---

## 6. STEP 6 — pipelines: IDENTITY vs ARRIVAL keying (the OTTO 10-D/A class)

| pipeline | gates it grades | keys the observation on | verdict |
|---|---|---|---|
| `FORGE/tools/market-data/fetch.py::fred_fetch` (`:330-357`) | **GATE-TERRY-007** (named in the task) · GATE-HY-REKILL · LIQ-069/072 via `boot.py` | params sent: `series_id`, `api_key`, `file_type`, `sort_order=desc`, `limit`. **No `realtime_start` / `realtime_end`.** Result rows keyed `{date, value}` | ⛔ **IDENTITY on (series, date) · ARRIVAL on VINTAGE.** FRED's default realtime window is *today*, so the value returned is the **latest revision as of fetch time**. Two gates (`HY-REKILL`, and `TERRY-007` by its pre-9/4 annotation) declare **AS FIRST PUBLISHED** and their own grading tool cannot produce it. A re-run of the same date on a later day can return a different number with no tell. ⚠ `:354` also drops `.` (missing) rows silently — *benign here*, because both letters say non-publication days do not break consecutiveness, but it means a caller cannot distinguish "no print" from "not fetched". Cache TTL 300s (`:102`) is too short to matter |
| `AGENTS/LIQUID/scripts/boot.py::crun` (`:98-103`) | GATE-HY-REKILL (machine primary) · GATE-LIQ-079 ARM | counts the current consecutive run over `fred_fetch`'s newest-first list; compares `x*100 < lim` | **IDENTITY on series + list ORDER; no date-gap check; vintage inherited from `fred_fetch` ⇒ ARRIVAL.** The `<260` branch was repaired 9/2 (it had printed a two-close label off one print, `:116-117`) — the surviving gap is vintage, not counting |
| `AGENTS/BRENT/scripts/cot_grade.py` | GATE-BRENT-COT-35B | `--expect <report_date>`; `report_date` read **IN-ROW** and compared; mismatch ⇒ **exit 3, DO NOT GRADE** (`:127,147-151`). Market matched by **NAME** across a 2022 code rename (`:95-100`) | ✅ **IDENTITY (series + as-of date), fail-closed.** The best-keyed pipeline in the register. Residual: it fetches the current `f_disagg.txt`, so a CFTC **re-issue carrying the same `report_date`** is adopted silently — identity on the date, not on the vintage |
| `scripts/market.py` (`:26-36`) | GATE-TERRY-ROLL70-EXIT · (historically) GATE-REG-T02's 9/1 fire | `info.get("regularMarketPrice") or info.get("previousClose", 0)` — **no date argument, no session field, no settled-bar check, and a silent fallback to the PRIOR close** | ⛔ **ARRIVAL, and the fallback is the sharp edge**: a stale/So-quote run returns *yesterday's* close labelled as today's, at `rc=0`. This is the same object that produced the 9/14 in-progress-bar episode (`GATES.tsv:20`: bar failing its own OHLC sanity check, Close moving 79.14→79.03→79.13→79.10 with volume still climbing). `THRESHOLDS.tsv:3` names it as the instrument for a basis (*"regular-session close, unadjusted"*) it cannot itself certify — an SL-4(a) producibility gap between letter and named tool. ✅ **Mitigated downstream, not upstream**: `REG_T02_EXIT_LOG.tsv:1` appends **one row per SETTLED regular-session close**, and the run count is *"COUNTED from this file, never carried in prose or from memory"* |
| `AGENTS/BRENT/scripts/instrument_check.py` | none (reachability prober) | `load_registry()` `:102-111`; probes sources, does **not** read the `direction`/`threshold` columns | ✅ no keying exposure — which is also why D2's mis-encoded `below/113745` pair is **latent, not live** |
| `scripts/hormuz_transit_watch.py` | GATE-FALCON-001 leg 2 — **corroborator only** | PortWatch `Daily_Chokepoints_Data` FeatureServer; reports print age, alarms >10d lag (`FRESH_LEG_BASELINE.md:31`) | **IDENTITY on print date** ✅, but the letter's anti-false-fire clause (`:51`) bars it from firing leg 2 at all (*"a PortWatch-only read cannot fire leg 2"*). Leg 2's actual instrument (TankerMap) has **no pipeline** — every read is manual |

---

## 7. PER-GATE ELEMENT MATRICES

Legend: **N** = named · **U** = unnamed · **—** = not applicable to this gate's form.

### GATE-HY-REKILL — 2 observations
| element | obs 1 | obs 2 | locator |
|---|---|---|---|
| series (ticker) | **N** `BAMLH0A0HYM2` | **N** | `GATES.tsv:3` = `KILL_MEMO_HY_OAS_260.md:47` |
| unit + conversion | **N** bp = published % × 100 | **N** | same |
| vintage convention | **N** AS FIRST PUBLISHED | **N** | same |
| operator + boundary | **N** strictly `< 260.0` | **N** | same |
| published precision + tie | **N** FRED publishes 0.01% = whole bp; *"260 is not <260"* | **N** | `KILL_MEMO:54,56,78` |
| consecutiveness | **N** two consecutive **published** obs; non-publication days do not break; an unpublished day is not an observation | **N** | `GATES.tsv:3`; `KILL_MEMO:55` |
| reset | **N** any published obs `≥260.0` resets to 0 | **N** | same |
**⇒ BASIS-NAMED.** The only letter in the register that names all seven on every observation.

### GATE-LIQ-069 — L1 ≥3 · L2 2 · L3 n/a · L4 2–10 · L5 1/action
| element | L1 (BB>220 & CCC-flat) | L2 (CRWV CDS) | L3 (new-issue) | L4 (cohort equity + HY) | L5 (ORCL ladder) |
|---|---|---|---|---|---|
| series | **N** `BAMLH0A1HYBB`, `BAMLH0A3HYC` | **U** → declared UNGRADED absent a named vendor ✅ | **U** → declared UNGRADED ✅ | **N** CRWV/IREN/APLD/NBIS official closes + `BAMLH0A0HYM2` | **N** agency published rating action |
| unit | **N** bp | — | — | **N** % / bp | **N** notch |
| vintage | **N** | **N** (convention applies) | **N** | **N** | **N** as first published |
| operator + boundary | **N** `>220`; flat = `|5-session CCC Δ| ≤15bp` | — | — | **U** `−15%/session` strictness undeclared; HY `≥5bp` **N** | **N** 2nd agency to IG floor OR any to HY |
| precision + tie | **U** | — | — | **U** | — |
| consecutiveness | — | — | — | — | — |
| reset | **U** (nothing resets a 5-session flat window) | — | — | **U** | — |
**⇒ BASIS-UNNAMED (precision/tie · reset · L4 strictness).** ✅ L2/L3's *"UNGRADED absent a named source"* is the compliant way to carry an un-instrumented leg.

### GATE-LIQ-072 — 1 + 2 + source-named-at-grade
| element | IG OAS | SpaceX gap (2 endpoints) | 3rd/4th issuer | 144A |
|---|---|---|---|---|
| series | **N** `BAMLC0A0CM` | **N** SpaceX vs cohort | **U** → UNGRADED ✅ | **U** → UNGRADED ✅ |
| unit | **N** bp = % × 100 | **N** pp | — | — |
| vintage | **N** | **N** | — | — |
| operator + boundary | **N** `>94` | ⛔ **U** *"fails to compress 4-6wk"* — no magnitude, and **the two pricing-date endpoints are UNPINNED, owner-owed since 2026-07-09** | — | — |
| precision + tie | **U** (`>94` carries no decimal on a series published to whole bp) | **U** | — | — |
| consecutiveness / reset | — | — | — | — |
**⇒ BASIS-UNNAMED (endpoint dates · precision/tie · leg-2 magnitude).** The pinning debt is **70 days old** and is carried identically on both surfaces (`GATES.tsv:5`; `KB.tsv` KB-LIQ-072 notes) — agreed, not disagreed, which is why nothing flags it.

### GATE-LIQ-076 — up to ~8 (2-of-3 in a rolling 2wk window)
| element | W1 (SOFR-3M lev) | W2 (PD warehouse) | W3 (MOVE/VIX) |
|---|---|---|---|
| series | **N** CFTC TFF SOFR-3M leveraged-fund net (no contract code) | **N** NY Fed PD API, G10>10y / G5L10 | **N** MOVE, VIX — ⚠ **two producers named** (`fetch.py ^MOVE` and *"VIOLET's figure governs"*) |
| unit | **N** contracts | **N** $mm | **N** index points |
| vintage | **N** AS FIRST PUBLISHED | **N** | **N** same-session closes |
| operator + boundary | ⛔ **GATES cell TRACKED** (*"at/past record"*) vs **letter FROZEN** (`beyond −2,950,000`) — see D3; cover `>300,000` **N** | **N** `<−$12.0B`; `<−$800mm` | **N** `>85` while `<20` |
| precision + tie | **U** | **U** | **U** |
| consecutiveness | **N** both weeks of a cover | **N** ×2 consecutive weeks (G5L10) | — |
| reset | **U** | **U** | **U** |
| conjunction window | **N** any 2 of 3 inside a rolling 2 weeks | | |
**⇒ BASIS-UNNAMED (precision/tie · reset) + D3 referent disagreement.**

### GATE-LIQ-079 — ARM ≥4 obs (SOFR99 + IORB × ≥2 days); FIRE 0 gradable
| element | SOFR99 (each day) | IORB (each day) | FIRE legs |
|---|---|---|---|
| series | **N** NY Fed SOFR 99th percentile | **N** IORB | **N** series named (EFFR−IORB · above-IORB borrowing · reserve-demand slope · dispersion) |
| unit | **N** bp | **N** bp | **N** |
| vintage | **N** AS FIRST PUBLISHED | **N** | **N** |
| operator + boundary | **N** spread `≥ +30bp` (non-strict) | — | ⛔ **U — NO THRESHOLDS** (*"widening"*, *"slope negative"*, *"SRF>0"*); owner declares FIRE **UNGRADEABLE, not false**, with a dated commitment: bands + base rates as a PROPOSAL by **2026-10-31** ✅ |
| precision + tie | **U** — and the sharper gap: **rounding ORDER on a derived spread is undeclared** (round the two legs to bp then subtract, or subtract then round? two published 2dp percent series ⇒ the two orders can straddle +30) | **U** | — |
| non-calendar | **N** in the letter (`±2 business days of quarter-end / month-end / Apr-15 excluded`), **U** in the GATES cell (summary omission, not a conflict) | | |
| consecutiveness | **N** ≥2 consecutive such days | **N** | — |
| reset | **U** | **U** | — |
**⇒ BASIS-UNNAMED (precision/tie · rounding order · reset) on ARM.** ✅ Best-handled un-instrumented legs in the register: named, declared UNGRADEABLE, and dated.

### GATE-FALCON-001 — leg 2 (pending) ≥3 obs; legs 1 & 3 FIRED
| element | leg 1 (FIRED 7/23) | **leg 2 (OPEN)** | leg 3 (FIRED 8/15) |
|---|---|---|---|
| series | **N** UKMTO/Ambrey/JMIC-confirmed hull attack | **N** TankerMap `analytics/straits/bab-el-mandeb`, tanker transits 7dma | **N** Yanbu weekly dark-fleet-capable loadings |
| unit | — | **N** tankers/day | **N** mb/d total / crude |
| vintage | **N** date-check first (anti-recirculation clause) ✅ | **U** (reads carry a data stamp; no convention) | **U** |
| operator + boundary | **N** post-7/20, in-zone, confirmed | ⛔ **U — NO MAGNITUDE AT ALL.** *"a FRESH step-down from the PREVAILING 7-day average"*; **the number 8 is explicitly de-registered** (`FRESH_LEG_BASELINE.md:48`). The reference window ("prevailing") is also undefined | ⛔ **U** — `≤~3.0` / `≤~2.55`: the **`~` voids the boundary** |
| precision + tie | — | **U** | **U** |
| consecutiveness | — | **N** sustained ≥2 print-days | **N** first qualifying weekly print |
| reset | — | **U** | — (fired, cannot re-fire) |
| attribution predicate | — | **U** *"attributable to enforcement"* — a judgment with no instrument; carried by the anti-false-fire clauses (`:51`) rather than a test | — |
**⇒ BASIS-UNNAMED (operator/boundary · reference window · precision · tie · reset).** ★ The 9/14 grade *worked* only because the sign was unambiguous (**+47% w/w, 7dma 3.1→4.0**): a −5% read is **ungradable on this letter**. The owner is explicit that the leg was *"UNGRADED-ON-BASIS"* at three prior touches (`:59,64`) — the letter's gap and the grading record agree.

### GATE-BRENT-COT-35B — 2 fields from 1 weekly print + 8 frozen basis obs
| element | Leg A (MM gross shorts) | Leg B (OI-share) | frozen base (8 obs) |
|---|---|---|---|
| series | **N** CFTC disagg `f_disagg.txt`, market by NAME, code 067651, MM-short col 14 | **N** same print's OI | **N** trailing-8wk 2026-06-16..08-04 |
| unit | **N** contracts | **N** % to 4dp | **N** contracts |
| vintage | ⛔ **U** — no convention; CFTC re-issues | ⛔ **U** | ⛔ **U** (a median OF a revisable series) |
| operator + boundary | ✅ **N, MECE and exhaustive**: `≤109,164` SPENT / `109,165–118,325` NO-VERDICT / `≥118,326` NOT-SPENT; *"113,745 is its CENTRE, not a boundary"* | **N** `≤4.909%` SPENT, GATING | **N** base − 1.0 median_unit; deadband ±0.5 |
| precision + tie | **N** integer contracts; non-strict boundaries stated exhaustively ⇒ ties resolve | **N** 3dp bar vs 4dp computed share | **N** `122,904.5` — *carry the .5* |
| consecutiveness | — | — | — |
| reset | **N** *"REVERT: re-read every print, never a latch"* | **N** | **N** re-basing = new N1 build + Will ruling |
| joint rule | **N** both legs must AGREE, Leg B GATING, disagreement ⇒ NO-VERDICT (a real answer) | | |
**⇒ BASIS-UNNAMED (vintage)** — one element, on an otherwise exemplary letter. See D2 for the owner-surface divergence.

### GATE-FERT-G5 — 2 observations per weekly print (DAP, MAP; OR-joined)
| element | DAP | MAP |
|---|---|---|
| series | **N** DTN Progressive Farmer weekly retail, publisher `dtnpf.com` ✅ with an explicit anti-conflation clause | **N** |
| unit | **N** $/ton — *"NEVER conflate w/ Pink Sheet $/mt or NOLA $/st"* ✅ | **N** |
| vintage | **U** (article publishes a prior data week; no convention) | **U** |
| operator + boundary | **N** strict `> $1,000/ton` | **N** |
| precision + tie | **U** — DTN prints whole $; a print at exactly `$1,000` does not fire under strict `>`, undeclared | **U** |
| consecutiveness | — (single print fires) | — |
| reset | — | — |
| base rate | ⛔ **OPERATOR-MISMATCH** (§4) | ⛔ same |
**⇒ OPERATOR-MISMATCH** (and BASIS-UNNAMED on vintage + precision/tie).

### GATE-TERRY-007 — 5 consecutive closes (+ reset-readers)
| element | each of the 5 |
|---|---|
| series | **N** official FRED `DGS10`; **`^TNX` explicitly excluded and count-neutral** ✅ |
| unit | **N** percent |
| vintage | **U** — no convention; H.15/DGS10 is revised. Pre-9/4 ⇒ annotated *"grades as-first-published"* |
| operator + boundary | **N** strict `<4.50` |
| precision + tie | ✅ **N** — *"Strict <4.50 on the **published two-decimal** DGS10: **4.50 itself does not qualify**"* (`FLOW-TRIGGER_duration-TLT-put.md:18`) |
| consecutiveness | ✅ **N** — FIVE CONSECUTIVE; **holidays count-neutral**; an unpublished session is *"UNKNOWN and still owed, not discharged"*; *"grade the observation date, not the release date"* |
| reset | ⛔ **U for THIS counter.** The cell states Ruling B's reset for the **arm-#2** counter (*"a SINGLE close <4.50 = arm-#2 counter RESET only"*). Nothing states what resets the **0-of-5 exit** run. "Consecutive" implies it — but the only reset rule written beside it belongs to a different counter running in the opposite direction, which is the read a stranger would take |
**⇒ BASIS-UNNAMED (vintage · exit-count reset).**

### GATE-CORAL-MSI-01 — 10 observations (5 metros × 2 readings) + 2 vintage stamps
| element | each metro reading | spacing leg |
|---|---|---|
| series | **U** — *"Parcl FL metro **Motivated Seller Index (MSI, 0–10 composite scale)**"* names the index ✅ and carries a load-bearing anti-mislabel clause ✅, but **the five metros are not enumerated in the frozen letter** (Tampa · Punta Gorda · North Port · Cape Coral · Lakeland appear only in the grades). `5-of-5` is a count over an unnamed set | — |
| unit | **N** 0–10 index | **N** days |
| vintage | ⛔ **U — and it bound at the live grade**: two clocks, **11 days observed vs 10 days by page `Updated:` stamp**, and the letter names neither as governing (`STATUS.md:107`) | ⛔ same |
| operator + boundary | **N** `>6.0` strict; breadth `<5-of-5` | **N** `≥10 DAYS APART` |
| precision + tie | **U** — Parcl publishes 2dp (`5.91`, `6.01`); a metro at exactly `6.00` is undeclared. Live margins were **0.09** and **0.01** |
| consecutiveness | ✅ **N** — *"TWO CONSECUTIVE readings"*, and the owner verified it at the artifact (no reading logged between; KB ends ML-CORAL-074) | |
| reset | **U** | |
| re-fire | ⛔ **ABSENT** — owner-flagged, WQ-241; *"the 8/23 gap with the sign flipped"* | |
**⇒ BASIS-UNNAMED (metro set · vintage clock · precision/tie · reset).** ★ The owner graded **on the frozen letter, not re-fitted**, and registered the rule defect prospectively — the correct handling of a defective letter at the grading table.

### GATE-TERRY-ROLL70-EXIT — 3 consecutive closes (+ reset-readers)
| element | each of the 3 |
|---|---|
| series | **N** WAL, Yahoo via `scripts/market.py` (`THRESHOLDS.tsv:3`) |
| unit | **N** USD per-share |
| vintage | **partial** — ✅ `unadjusted` declared (the equity-restatement leg); ⛔ **U** on the in-progress-bar question. The owner's working rule (**a settled bar is one whose VOLUME has stopped moving** — two tools, seven minutes, both `703,916`) lives only in a `last_checked` cell, not in the letter |
| operator + boundary | **N** `≥ $81.90` non-strict |
| precision + tie | **U** — Yahoo carries 2–4dp; a close of exactly `81.90` satisfies `≥` by default but is undeclared |
| consecutiveness | **N** THREE CONSECUTIVE sessions |
| reset | ✅ **N** — *"a close <81.90 resets the count"*, and `REG_T02_EXIT_LOG.tsv:4` restates it |
**⇒ BASIS-UNNAMED (precision/tie · settled-bar/vintage).** ★ Four surfaces carry `≥81.90 ×3` identically (§3) — the best-reconciled figure in the register.

### GATE-BRK-R2 — (a) 3 consecutive quarterly prints · (b) 1 quarter
| element | leg (a) | leg (b) |
|---|---|---|
| series | **N** per-vehicle SEC tender filings, **filing-primary**; issuer-stated proration qualifies, **computed cap/requests do NOT** ✅ | **N** same |
| unit | ✅ **N, load-bearing** — *"THE UNIT IS PART OF THE LEVEL: quarterly, Σ(accepted)/Σ(submitted); monthly readings are RECORDED but NEVER GRADED"* | ✅ **N** |
| vintage | ⛔ **U** — preliminary vs **final** SC TO-I/A; annotation and practice diverge (§5) | ⛔ **U** |
| operator + boundary | **U** *"sub-100%"* — is exactly 100.00% sub-100%? | **U** *"<25%"* — is exactly 25.00% a fire? OCIC's 22.82% sits 2.18pp inside |
| precision + tie | **U** — issuer prorations publish at varying precision | **U** |
| consecutiveness | ✅ **N** `≥3 CONSECUTIVE` | — |
| reset | **U** — does a 100% quarter reset the run to 0? | — |
| window | — | ✅ **N** prospective: repurchase pricing date **on/after 2026-09-03**; OCIC 22.82% excluded **because it helped place the level** |
**⇒ BASIS-UNNAMED (vintage · operator strictness · precision/tie · reset).**

---

## 8. THE ONE-LINE RE-REGISTRATION ASK PER GATE *(listing only — dispositions are not this reader's; no packets written)*

| gate | owner | the ask the owner would receive |
|---|---|---|
| GATE-HY-REKILL | LIQUID | Strike the *"LIQUID owes the fold"* clause from the GATES condition cell — the fold landed `28a5e3be0` 2026-09-03 — and re-point item 6 of the canonical letter, whose *"ALFRED 404s / no vintage path"* justification is refuted by the 2026-09-17 `VINTAGE-PATH-VERIFIED` result (the convention itself stands). *(cell is PROME's; letter is LIQUID's)* |
| GATE-LIQ-069 | LIQUID | Add published precision + tie convention to L1's `>220` / `≤15bp` and L4's `−15%/session`, and a reset rule for L1's 5-session flat window. |
| GATE-LIQ-072 | LIQUID | **Pin the SpaceX pricing-date endpoints** (owed since 2026-07-09, 70 days) or declare the leg UNGRADEABLE-until-pinned the way 079's FIRE legs are; add precision/tie to `>94`. |
| GATE-LIQ-076 | LIQUID | Replace the GATES cell's *"at/past record"* with the letter's frozen **`beyond −2,950,000 contracts`** (D3); name ONE producer for the MOVE leg; add reset rules. |
| GATE-LIQ-079 | LIQUID | Declare the **rounding order** for the SOFR99−IORB spread (legs-then-subtract vs subtract-then-round) and the ARM reset rule; the FIRE-leg bands are already dated to 2026-10-31 and need no new ask. |
| GATE-FALCON-001 | FALCON | **Give leg 2 a magnitude and a reference window** — *"step-down"* with the number 8 de-registered leaves the leg gradable only when the sign is unambiguous; and replace leg 3's `~` boundaries with exact ones if it is ever re-registered. |
| GATE-BRENT-COT-35B | BRENT | **Name the resolving vintage** (first print vs CFTC re-issue) and register a re-issue watch; **and fix `REGISTRY.tsv:131`** — the owner cell still carries `base 122,904` and `Leg A bar: shorts <= 113,745 = SPENT`, both superseded 2026-09-06 (D2), plus the latent `direction=below / threshold=113745` column pair. |
| GATE-FERT-G5 | FERT | **Re-compute the base rate on the letter's own instrument and operator** — DTN retail weekly $/ton, strict `>` — or mark the registered 93rd-pct figure explicitly as Pink-Sheet CONTEXT, never this gate's base rate (§4); add the $1,000 tie convention. |
| GATE-TERRY-007 | TERRY/BOND | Write the **exit-counter reset rule** explicitly beside Ruling B's arm-#2 reset (the two counters run opposite directions on one level), and name the DGS10 vintage. |
| GATE-CORAL-MSI-01 | CORAL/Will | **Enumerate the five metros in the letter** and name which clock governs the ≥10-day spacing (observation date vs page vintage — they disagreed at the live grade); add the `6.00` tie convention. The re-fire gap is already Will's (WQ-241). |
| GATE-TERRY-ROLL70-EXIT | REGINALD/TERRY | **Promote the settled-bar rule into the letter** (*volume static across two tools* — it exists only in a `last_checked` cell) and add the `81.90` tie convention; note that `scripts/market.py` cannot certify the basis `THRESHOLDS.tsv:3` names. |
| GATE-BRK-R2 | BROCK | **Name the resolving vintage** (preliminary vs final SC TO-I/A) — the pre-9/4 annotation says as-first-published while the register grades the final — declare strictness on *"sub-100%"* / *"<25%"*, add the (a) reset rule; and reconcile `review_by` 2026-10-31 (GATES) vs 2026-11-15 (register header) (D4). |

---

## 9. WHAT THIS READER COULD NOT DO
- **Step 2 (blind grade-read)** and **step 3's negative control** are other readers' / already done — not attempted, not re-verified.
- **CANNOT-EVALUATE on publisher revision behaviour** for DTN, TankerMap and Parcl: no published revision schedule was located for any of the three from this box, and I did not fetch. The membership call under WQ-175 is the letter owner's, stated on the letter — none of the three states it.
- **NOT-SEEN, never 0:** whether the `DEALER_POSITIONING_NEXUS_WATCH.md:10` leg-label relabel returned to PROME on 2026-09-03 has landed in the GATES `last_checked` cell — I read the current cell but did not diff its history.
- `PROME/GATES.tsv:13` GATE-FERT-G5 carries `review_by` / `consumed_by` **2026-09-16** and today is 2026-09-17 — the DTN Wednesday wake appears **lapsed by one day**. Flagged as an observation only; clock state is outside this sweep's basis perimeter.
