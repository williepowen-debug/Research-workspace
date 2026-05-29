# CARL CHANGELOG

Tracks all changes to THESIS.md and PREDICTIONS.tsv. Reverse chronological. Each entry documents what changed, why, and the old view vs new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new mechanism, thesis break, conviction reversal). Minor (Y) = refinement (updated evidence, threshold adjustment, vector upgrade/downgrade).
- PREDICTIONS: changes logged by Pred_ID.

---

## 2026-05-29 — CRL-18 CONFIRMED (GDP Q1 2nd est) + CRL-08 re-armed OPEN (gas un-sustained)

### PREDICTIONS.tsv — 2 rows, no THESIS version bump
**Author:** CARL (Will-directed 5/28-print resolution session)
**Trigger:** BEA GDP Q1 2nd estimate (May 28) + AAA pump re-check (May 29).

**CRL-18 OPEN → ✅ CONFIRMED (Date_Resolved 2026-05-28):**
- Predicted (May 1, 60% conf): Q1 GDP 2nd est revises advance 2.0% down 0.2-0.4pp into 1.6-1.8%.
- Actual: **+1.6%, -0.4pp** — landed at the bottom edge of the predicted band. Clean hit at 60% conf.
- Drivers (CARL-domain): consumer SERVICES decline led by healthcare (Census QSS) + private inventory drawdown (mfg+retail); goods (recreation/vehicles) revised UP = forced/trade-down pattern.
- **Stagflation signature in one release:** real growth revised DOWN while Core PCE prices revised UP to 4.4% ann. (from 4.3% advance); headline PCE 4.5% held. Realized core PCE 4.4% >> UMich 5-10Y 3.5% red line → **V12 (Stagflation Trap) hardens further post-Waller.**

**CRL-08 — FIRST-CROSS-NOT-SUSTAINED, re-armed OPEN (confidence 92% → 70%):**
- AAA $4.391 (May 29) = -17.3¢ from $4.564 peak (May 21), ~11¢ below the $4.50 threshold.
- Breach window ~May 21-26 (5-6 days at/above $4.50) decisively failed the 2-wk sustained requirement; Memorial Day spike fully reverting.
- Mechanism INTACT, threshold UN-sustained → prediction stays OPEN (re-armed), re-test requires fresh Iran-kinetic re-spike. No V5 score upgrade. Brent -10% from 5/5 peak transmitted in reverse at ~17-18d lag (empirically consistent both directions this cycle).
- Threshold-vs-mechanism discipline applied (cf. [[finding_threshold_vs_mechanism]]): threshold retraced but mechanism held → re-arm, not MISS.

**Apr PCE (Personal Income & Outlays, rel May 28, also grabbed 5/29):** Core PCE **3.3% YoY** (+0.2% MoM) = cycle high, accel from Mar 3.2%; headline PCE 3.8% YoY (+0.4% MoM). Savings rate **2.6%** (-100bps from Mar 3.6%); Real DPI -0.5% MoM (5th neg, accelerating); personal income flat 0.0%; Real PCE +0.1%. = buffer-exhaustion deepening + savings-funded-forced-consumption mechanic intensifying. No prediction resolved (CRL-19 was Mar, already MIXED) — STATUS data integration only.

**No THESIS.md change.** V12-hardening evidence accumulating across THREE 5/28-29 datapoints (Waller pivot + GDP Q1 stagflation composition + Apr monthly Core PCE 3.3%); formal V12 score-upgrade review + possible v2.5.2 minor still pending Jun 16-17 SEP per OPEN THREAD.

## 2026-05-03 PM7 — Workbook hardening: VX P1 + KB ref integrity + SCHEMA Option A + VX dedup P4

### Structural workbook work — 4 files touched, 1 commit (3b47901f)
**Author:** CARL (Will-driven session, post-PM6 grocery squeeze refresh)
**Trigger:** Will request to audit VX.tsv current status. Audit surfaced 9 distinct issues; Will approved P1 (Status canonicalization + Delegated_To split + tombstone drops), then dangle cleanup, then Option A SCHEMA expansion, then P4 (dup consolidation).

**P1 — VX Status enum canonicalization + Delegated_To split (replicates KB Item #2a precedent):**
- Added `Delegated_To` column to VX.tsv (11→12 cols, matches KB schema enum: STUE/HOMER/GIG/PHAN/POLLY/POP/DOC or empty)
- Migrated 9 `DELEGATED TO HOMER` rows: split Status overload — assigned proper threshold-color (per band-match + WORKBOOK DISCIPLINE rule for ambiguous cases) + Delegated_To=HOMER. Threshold-color assignments: 2.01 GREEN (approaching Yellow), 2.02 GREEN [FLAG range value], 6.04 ORANGE, 6.05 ORANGE, 6.07 ORANGE, 6.08 ORANGE [FLAG categorical], MF-02 ORANGE, NAR-01 RED, HSG-02 RED.
- Normalized 3 RED-BREACHED → RED (1.04 Subprime Auto, SENT-01 UMich, MACRO-08 ISM Prices Paid) — preserved "BREACHED" in Notes.
- Normalized 1 YELLOW-borderline → YELLOW (MACRO-01 GDP 2.0%) with [FLAG] for May 28 second-est revision risk.
- Dropped 3 CONSOLIDATED tombstones (1.06 Student Loan Conditional, 6.01 CC 90+ NY Fed, ABS-15 Subprime Auto) — but FIRST updated 3 KB rows that referenced them (KB-055/060: 6.01→1.01; KB-059: dropped redundant ABS-15) per discipline.
- Result: 120→117 rows, Status enum clean (RED/ORANGE/YELLOW/GREEN/PENDING only).

**Dangle cleanup — KB→VX integrity pass:**
- Post-P1 verification surfaced 5 pre-existing dangling KB→VX refs (PM4/PM5 sessions wrote refs that didn't match canonical IDs). Verified-by-reading-target before each rewrite.
- KB-271 `VX-CARL-RETAIL` → `VX-CARL-6.10` (Retail Control Group, verified match)
- KB-272 `VX-CARL-MORTG-RATE` → `VX-CARL-HSG-01` (30-Yr Mortgage, verified match)
- KB-272 `VX-CARL-MBA-PURCH` → blanked (no MBA VX vector exists; backlog item)
- KB-273 `VX-CARL-CB-EXPECT` → `VX-CARL-SENT-02` (CB Expectations, verified match)
- KB-274 `VX-CARL-FOMC-RATE-PROXY` → blanked (FOMC vector deferred per ROADMAP)
- Result: 0 dangling KB→VX refs.

**Option A — SCHEMA Vectors-col formal expansion:**
- Audit surfaced 52 KB rows with 118 "off-spec" Vectors-col entries — 95 of which (Vector_N + CRL-NN) were semantically valid but unrecognized by SCHEMA enum. Pure mechanical replacement (Option B: Vector_N → VX-CARL-XXX anchors) would have lost thesis-vector + prediction-ref granularity.
- SCHEMA.tsv Vectors col `allowed_values` formally expanded to: `VX-{AGT}-NN, Vector_N, CRL-NN, FLOW-{AGT}-N.NN, {SUBAGT}-PNN, BRT-NN, →AGENT, or empty`. Description expanded to explain each ref type's purpose + KB-NNN restriction (DerivedFrom only).
- Then fixed only the 9 truly-broken refs: KB-031 (`STATE_DIFFUSION.tsv` filename dropped), KB-232/233/234 (5× `VX→AGENT` typos → `→AGENT`), KB-264/268 (KB-CARL-253 moved Vectors→DerivedFrom), KB-271 (`K-SHAPE` redundant tag dropped).
- Result: 521 refs all SCHEMA-recognized, 0 off-spec.

**P4 — VX dup consolidation:**
- Pair 1 (BNPL Late Rate): VX-CARL-1.03 (Mar 27, LendingTree, 0 KB refs, stale orphan) confirmed true dup of VX-CARL-BNPL-01 (Apr 17, Richmond Fed, 8 KB refs hooked in). Dropped 1.03.
- Pair 2 (Medical): Verification revealed VX-CARL-1.08 ($88-140B range incl. phantom debt) and VX-CARL-MED-01 ($88B narrow CFPB-reported point) measure subtly DIFFERENT things — disagreed on Status (YELLOW vs GREEN) because of band-cross from upper of range. Per WORKBOOK DISCIPLINE rule "if you can't write one threshold that meaningfully measures all bundled rows, they don't belong in one vector" — chose Will-approved Option A: rename to expose distinction. MED-01 → "Medical Collections (CFPB narrow)"; 1.08 → "Medical Debt Total (incl. phantom estimate)". Cross-reference Notes added to both.
- Result: 117→116 rows.

**Final integrity (cumulative):**
- VX: 116 rows × 12 cols, 0 col-count anomalies, Status enum {RED 42 / ORANGE 36 / GREEN 15 / YELLOW 14 / PENDING 10}, Delegated_To {empty 107 / HOMER 9}.
- KB: 273 rows unchanged, 0 dangling KB→VX, all 521 Vectors-col refs SCHEMA-recognized.
- SCHEMA: Vectors-col allowed_values formalized to multi-level ref system.

**Files touched:**
- `workbook/VX.tsv` (P1 schema expand + 9 migrations + 3 normalizations + 3 tombstones + 1 P4 drop + 2 P4 renames)
- `workbook/KB.tsv` (3 P1 ref-rewrites + 4 dangle rewrites + 7 Option A truly-broken fixes)
- `workbook/SCHEMA.tsv` (Vectors col allowed_values + description expanded)
- `ROADMAP.md` (+2 backlog adds: MBA Apps VX vector decision; CARL Status enum hardening sibling to Item #5)

**Backlog adds (ROADMAP investigations backlog):**
- MBA Apps VX vector decision — KB-272 covers MBA Composite/Purchase/Refi but no VX vector tracks them. Decision needed: create VX-CARL-MBA-APPS or accept informational-only.
- CARL Status enum hardening — VX schema not formal in SCHEMA.tsv (only KB schema is). Item #5 was demoted because col-bleed was artifactual, but Status enum + threshold-direction would benefit from formal definition. Pairs with Item #3 validator promotion.

**Open finding:**
- STUE/CLAUDE.md still has stale `VX-CARL-1.06: CONSOLIDATED — use SL vectors below` line. Sub-agent doc — flagged for Will rather than edited per Critical Rule #2 (subagents own their files).

---

## 2026-05-03 PM3 — CRL-19 RESOLVED (direction-correct/magnitude-light)

### PREDICTIONS: CRL-19 OPEN → MIXED
**Author:** CARL (STATUS staleness audit Cluster 1 refresh, May 3 PM3)
**Trigger:** BEA Mar PCE released Apr 30 with Q1 GDP advance (earlier than ~May 30 anticipated) — CRL-19 data now available.

**Outcome:** Mar Core PCE YoY 3.2% (KB-CARL-270). Predicted 3.3-3.5%. Direction CORRECT (acceleration from Feb 3.0% confirmed at +20bps), magnitude LIGHT (10bps below floor; predicted +30-50bps acceleration, actual +20bps). Strict-def: MISSED floor. Direction-only Brier good; magnitude Brier poor.

**Pattern:** Same disposition as CRL-01 (gas pump peak Mar 14-21 — direction right, magnitude wrong). Two of CARL's predictions now in MIXED/MISSED with direction-right/magnitude-low. Calibration question: are CARL predictions systematically over-magnitude or are these isolated cases?

**Vector #12 implication:** Bridge HOLDS — 3.2% monthly is consistent with 4.3% Q1 annualized via base-effect math (Jan/Feb low base lifts Mar print modestly). Stagflation Trap thesis itself unchanged. Calibration warning, not thesis warning.

**Files touched:**
- `thesis/PREDICTIONS.tsv` — CRL-19 Status OPEN → MIXED, Date_Resolved 2026-05-03, Outcome populated
- `STATUS.md` — CRL-19 row removed from Open table, added to Resolved table; Core PCE Monthly row updated to Mar 3.2% (was Feb 3.0%)
- `workbook/KB.tsv` — KB-CARL-270 logged BEA Mar release with full mechanism breakdown
- `workbook/VX.tsv` — VX-CARL-MACRO-07 Notes updated with bridge resolution

---

## 2026-05-03 — v2.5.1: MASKING FRAMEWORK NARROWED 6→4 + K-SHAPE/TARIFF SECTION + CRL-22, CRL-23

### THESIS v2.5 → v2.5.1
**Author:** CARL (response to external helper LLM stress test, Will-mediated review session May 3)
**Action:** Refinement. Masking framework breadth claim narrowed from 6 issuers to 4; reclassified UNH/ELV and DHI/PHM mechanisms into a sibling section (K-shape Selection + Tariff Transmission Confirmations); added two new predictions classified honestly as Vector #12 and Vector #10 transmission tests, NOT masking falsifications.

### TRIGGER

External helper LLM stress test of v2.5 cross-industry data masking framework (loaded into CARL `User Input/CARL KB_VECT convo.md`). Helper's pass 1: 3 mechanisms tight (ALLY/COF/RITM), 1 mixed (SYF), 2 loose (UNH/ELV, DHI/PHM); recommend downgrading breadth claim. Helper's pass 2 (after Will pushback "any worth here?"): found concrete content underneath UNH/V28 + DHI/tariff; recommended re-articulation + 2 new CRLs preserving 6-issuer breadth. CARL review of pass 1 vs pass 2 verdict: pass 1 was the more honest read; pass 2 over-corrected on weak pushback and stretched mechanism labels to preserve breadth. Substance check:

- **UNH/ELV "10% cost-trend pricing + V28 RAF unresolved"** — real H2 2026 risk, but NOT masking in the ALLY sense. MA carriers price entire 2026 plan year via CMS bid; defensive 10% pricing isn't a structural mechanism deferring visibility on the current book. V28 RAF is industry-wide regulatory determination, not company-specific masking. RITM uses an accounting rule to defer DQ recognition on its own borrowers — UNH is making a forward revenue assumption.
- **DHI/PHM "$10,900/home tariff hits FY27"** — real, sized, dated. But it's inventory cost-flow timing — materials bought pre-tariff work through COGS first. Mechanical, not management choice. ACL build (COF) IS deferred recognition; tariff cost lag is supply-chain physics.
- **Active-adult vs first-time mix shift** — genuine ALLY-analog (top of K transacting, bottom frozen) but it's K-shape selection, not masking — the helper's own proposed clarifying note correctly distinguishes this.

The helper's CRL-22 and CRL-23 are well-formed predictions (specific thresholds, invalidation criteria, position-action commitments) and worth adding regardless. But classifying them as masking falsifications would conflate three different mechanisms.

### CHANGES

**Change 1 — Cross-Industry Data Masking table narrowed 6→4 issuers.**
- Retained: ALLY, COF, RITM (tight masking — accounting/composition/securitization choices in the issuer's own book defer P&L recognition).
- Retained with caveat: SYF — ACL hedge leg is masking (forward-risk tell despite improving NCO); survivor-pool (Home & Auto -3.7%) explicitly flagged as K-shape selection, not masking. Only the ACL leg has the deferred-visibility property.
- Relocated: UNH/ELV → K-shape Selection + Tariff Transmission section (new, see below). DHI/PHM → same section.
- Meta-pattern definition tightened: "industry-specific *accounting/securitization choice within the issuer's own book*" (was "industry-specific accounting/structural mechanism" — too permissive, allowed pricing assumptions and supply-chain timing in).
- Added explicit note distinguishing masking vs K-shape selection.
- Crying-wolf X-thresholds simplified to 1 tier (credit issuers, 20bps); insurer/builder threshold removed since those mechanisms relocated.
- Boundary case rewritten to align with credit-issuer-only scope.

**Change 2 — New section: K-shape Selection + Tariff Transmission Confirmations.**
- UNH/ELV sub-section: K-shape selection (Vector #8 transmission via membership culling) + insurer pricing/regulatory contingency (Vector #12 transmission via cost-trend pricing + V28 RAF). Explicit "why not masking" reasoning. CRL-22 test.
- DHI/PHM sub-section: tariff transmission timing (Vector #10 + tariff regime durability) + active-adult selection (Vector #8 via demand-side cohort divergence). Explicit "why not masking" reasoning. CRL-23 test.
- "Why this section exists separately" rationale articulating the three-way distinction (masking / K-shape selection / tariff transmission timing) and why conflation breaks falsifiability.

**Change 3 — "What's Confirmed" rows for builder K-shape and insurer transmission re-tagged with "(selection, not masking)" and pointer to CRL-22/CRL-23.**

**Change 4 — Falsification structure unchanged for masking framework.** CRL-20 and CRL-21 still test the 4-issuer scope (ALLY, COF, SYF, RITM). Their thresholds remain valid since the 4-issuer scope was what they were originally designed against — the v2.5 rhetorical breadth ("5+ industries") was already implicitly testing the 4-issuer credit/servicer cluster.

### NEW PREDICTIONS

**CRL-22 — H2 2026 insurer MLR re-acceleration, 60% confidence:** UNH MCR H2 weighted ≥85.4% (+150bps) OR ELV BCR ≥88.3% (+150bps) AND V28 RAF final adverse. Tests Vector #12 + V28 regulatory contingency. NOT a masking framework falsification. Failure → insurer-side conviction -20pp; K-shape transmission story to credit issuers needs re-rating.

**CRL-23 — FY27 builder GM compression, 70% confidence:** DHI Q1 FY27 GM ≤17.5% OR PHM Q1 FY27 GM ≤22.0% AND tariff regime ≥10% effective sustained through Q4 2026. Tests Vector #10 + tariff regime durability. NOT a masking framework falsification. Failure → builder-side conviction -25pp; revisit demand-side weakness framing.

### HONEST CONVICTION COMMENTARY

The v2.5 masking framework promotion (May 1) was probably overconfident in its breadth claim. External review surfaced that "5+ industries, same meta-pattern" was rhetorical breadth not load-bearing evidence — only 4 issuers had genuine deferred-visibility mechanisms. Same calibration discipline applied to v2.5 score recalibration (58/60 → 53/70 = ~60% calibration + ~40% legitimate conviction reduction) now applied to the masking framework breadth: 6 issuers → 4. The narrowing does not weaken the bear thesis — UNH/ELV cohort culling and DHI/PHM tariff timing are still thesis-supportive observations with their own falsification structure (CRL-22/CRL-23). What the narrowing does is preserve falsifiability: CRL-20/CRL-21 now test what they were designed to test (credit/servicer issuer accounting choices), not a heterogeneous mechanism bundle that a CONTAINMENT critic could pick apart.

### FILES AFFECTED

| File | Change |
|------|--------|
| `thesis/THESIS.md` | Masking table narrowed 6→4 with SYF caveat; meta-pattern + boundary case rewritten; K-shape selection vs masking note added; new section "K-shape Selection + Tariff Transmission Confirmations" inserted between masking framework and Path C; "What's Confirmed" insurer/builder rows re-tagged; "What's Forecast" table adds CRL-22, CRL-23. |
| `thesis/PREDICTIONS.tsv` | +CRL-22, +CRL-23 (24 rows total). |
| `thesis/CHANGELOG.md` | This entry. |
| `workbook/KB.tsv` | KB-CARL-265 logging the v2.5.1 refinement. |
| `ROADMAP.md` | v2.5.1 hardening list updated; this item moved to RECENTLY RESOLVED. |

### ACKNOWLEDGMENT OF EXTERNAL REVIEW

Helper LLM's stress test (pass 1) was directionally correct. Helper's pass 2 over-corrected and the resulting draft would have preserved a 6-issuer table whose footnote contradicted its rows. CARL took the substance of helper's CRL-22 and CRL-23 drafts (good predictions) but classified them honestly as Vector #12 and Vector #10 transmission tests rather than masking falsifications. Architecturally aligned with how v2.5 already separates "thesis-internal mechanism puzzles" (CARL) from "counter-narrative observations" (RED) — same discipline applied here at the framework level.

### KB ROW LOGGED

- **KB-CARL-265** — v2.5.1 thesis refinement (masking framework narrowed 6→4 + K-shape/tariff section + CRL-22, CRL-23)

---

## 2026-05-01 — v2.5: PATH C ACTIVE + CROSS-INDUSTRY DATA MASKING + ARCHITECTURAL REALIGNMENT + 58/60 → 53/70 RECALIBRATION

### THESIS v2.4.1 → v2.5
**Author:** CARL (multi-stage drafting May 1 — r1/r2/r3 with two rounds of external review feedback integrated)
**Action:** Major refinement. Three structural changes plus architectural realignment with RED. Convergence rescaled from 58/60 (97%) → 53/70 (76%) — ~60% calibration discipline + ~40% legitimate conviction reduction.

### TRIGGER

Q1 2026 consumer earnings cycle (Apr 17 – May 1) materially complete. Mandatory thesis review per exit rules (Q1 consumer earnings = April 2026). Pattern across SYF/COF/UNH/DHI/PHM/ALLY/Rithm/Case-Shiller integrations: each issuer reports headline-clean while underlying cohort/composition deterioration is structurally embedded but not yet visible in P&L because of an industry-specific accounting/structural mechanism. ALLY composition-masking framework (KB-CARL-225) generalizes.

Plus: Q1 ATTOM REO conversion (+45% YoY) + bank Q1 provision builds (COF $230M, SYF +36bps to 10.42%) + Rithm advance receivable -$224M / -7.3% QoQ + builder K-shape explicit on call (DHI/PHM) = pre-specified Path C activation triggers from CHANGELOG v2.4 satisfied.

### THREE STRUCTURAL CHANGES

**Change 1 — Cross-industry data masking promoted from KB-225 to thesis-level methodology.**
- Generalizes across 5+ industries via different mechanisms but same META-pattern (12-24mo P&L visibility lag)
- Industries + mechanisms: ALLY (composition shift + CLN routing), SYF (survivor-pool), COF (ACL hedge + auto subprime mix), Rithm (FHA mod reclassification), UNH/ELV (membership culling + bronze-plan shift), DHI/PHM (one-time benefits + active-adult mix)
- Methodological commitments: decompose first, headline second; aggregate-only counter-data downgraded; standing cross-agent methodology; trade duration extends to Q1 2027+
- Falsification windows specified: **CRL-21 (Q3 2026 intermediate)** + **CRL-20 (Q1 2027 outer)**
- Crying-wolf X-threshold placeholders: 20bps for credit issuers, 50bps for non-credit (refinement deferred to standalone working doc)

**Change 2 — Path C ACTIVATING-RED → ACTIVE-RED (PROVISIONAL).**
- Pre-specified v2.4 trigger (Q1 bank earnings cluster confirming Path C provision build) satisfied
- Four channels confirmed: REO conversion + bank provision build + servicer stress + builder K-shape
- PROVISIONAL caveat: COF/SYF Q1'24/Q1'25 counterfactual baselines PENDING_VERIFY before promotion to FIRM
- Operational consequence specified: provisional = 50-75% bank-side put allocation; firm = full allocation; downgrade to ACTIVATING-RED if baseline shows normal seasonal

**Change 3 — Convergence matrix rescaled and architecturally aligned (12 → 14 vectors).**
- 5-definition tightened to "fully fired, no further upside in mechanism"
- V8 + V9 merged into single K-Shape Converging vector (eliminated double-count)
- V13 Federal Fiscal Capacity Stress added (score 3, supporting context)
- V14 Upper-Decile Wealth Stress added (score 3, supporting context)
- V15 Refi-Window dropped — counter-signal territory belongs to RED
- V16 Employment Structural Rot added (was load-bearing claim but missing from scored matrix)
- V2 Subprime Auto downgraded 5 → 4 (strict-definition: EART terminal but AMCAR/SDART have cushion)
- Multiple other 5s rescaled to 4s under tightened definition

### ARCHITECTURAL REALIGNMENT (the second-order finding)

External review surfaced that CARL was running its own internal red team in parallel with system-level RED agent. Counter-Evidence section in THESIS, plus `red_team/` folder (COUNTER_LOG, SOFT_LANDING, CONTAINMENT) duplicated work that belongs in RED's domain.

Action:
- `red_team/` folder moved to `handoff_RED/` (May 1, commit 3d0bdf75)
- THESIS Counter-Evidence section stripped, content staged at `handoff_RED/COUNTER_EVIDENCE_FROM_THESIS.md`
- Puzzles section trimmed: counter-narrative observations (prime mortgage stable, auto insurance cooling, savings rate, prime card stable) routed to RED. Thesis-internal mechanism puzzles (claims-duration paradox, HAROT prime, Path C provisional) retained in CARL.
- HY OAS reframed: was counter-evidence, now masking-thesis CONFIRMATION (public spreads lagging tranche-level stress is exactly what masking framework predicts)
- CARL CLAUDE.md FILES table updated: red_team/ row replaced with handoff_RED/ pointer ("Do NOT maintain; awaiting RED pickup")

### CONVERGENCE MATRIX

| # | Vector | v2.4 | v2.5 | Note |
|---|--------|------|------|------|
| 1 | CC 90+ DQ → GFC | 4 | 4 | Holds |
| 2 | Subprime Auto 60+ | 5 | **4** ⬇️ | Strict-def fix |
| 3 | Fannie MF DQ → GFC | 4 | 4 | Holds |
| 4 | Student Loan 90+ | 5 | **4** ⬇️ | Rescaled |
| 5 | Gas Price Squeeze | 5 | **4** ⬇️ | Rescaled |
| 6 | UI Exhaustion Wave | 5 | **4** ⬇️ | Mechanism unverified |
| 7 | FL Triple Squeeze | 4 | 4 | Holds |
| 8 | K-Shape Converging *(merged 8+9)* | 5+5 | **4** ⬇️ | Merge + magnitude caveat |
| 10 | Foreclosure Acceleration | 5 | **4** ⬇️ | Rescaled |
| 11 | SB Bankruptcy + Owner Income | 4 | **3** ⬇️ | Rescaled |
| 12 | Stagflation Trap / Fed Locked | 5 | **4** ⬇️ | Rescaled (TTM not crossed) |
| 13 | Federal Fiscal Capacity Stress | — | **3** | NEW supporting |
| 14 | Upper-Decile Wealth Stress | — | **3** | NEW supporting |
| 16 | Employment Structural Rot | — | **4** | NEW (was missing) |

V9 merged into V8. V15 (Refi-Window) dropped (RED domain). Total: **53/70** (76%).

### NEW PREDICTIONS

**CRL-20 — Q1 2027 outer falsification, 75% confidence:** at least 3 of {ALLY, COF, SYF, RITM} show NCO/DQ acceleration breaking the "headline clean" pattern. Specific: ALLY consumer auto NCO ≥+30bps QoQ for 2 consecutive quarters; COF Card NCO ≥+25bps QoQ for 2 consecutive quarters; SYF NCO breaks above FY26 ceiling 5.5%. Failure → masking thesis invalidated, CONTAINMENT validated.

**CRL-21 — Q3 2026 intermediate falsification, 60% confidence:** by Q3 2026, NCOs at ALLY/COF/SYF have begun visible inflection AND vintage-loss projections for FY2025/FY2026 vintages ≥+50bps above FY2023 vintage at comparable seasoning. Position-action commitment on failure: confidence -25-30pp + trim short positions 25% + extend duration to Q2 2027+.

### NEW SECTIONS

- **Cross-Industry Data Masking Framework** (with industry-mechanism inventory + falsification windows + crying-wolf operational thresholds + boundary case)
- **Path C — Activation Status** (with provisional/firm/downgrade-target operational distinction table)
- **Trade Duration Implications** (KRE/WAL Dec 2026 vs thesis Q1 2027+ gap; Path A roll structure recommendation; flag to FORGE/REGINALD)
- **Puzzles / Anomalies** (3 thesis-internal mechanism puzzles)
- **Fast Early-Warning Kill Mechanism** (1-month conviction-update triggers; HY OAS asymmetry tiered)

### HONEST CONVICTION COMMENTARY

Score 58/60 (97%) → 53/70 (76%) decomposes:
- ~60% calibration: matrix expansion, 5-definition tightened, V8/V9 merge, V2 strict-def
- ~40% legitimate conviction reduction: V6/V8/V12 honestly downgraded based on evidence gaps + multiple PENDING_VERIFY items

Not "calibration honest, not thesis weakening" — that was rhetorical sleight of hand in r1/r2 drafts. Honest framing: prior 58/60 was probably overconfident. V6, V8, V12 were never really at 5 on the evidence base. 53/70 is closer to true conviction we should have had all along. Both better calibration AND recognition of prior overconfidence.

The thesis is still CRITICAL. Every load-bearing vector (1-12 + 16) is at 4. No vector at 3 or below in the bear-thesis core.

### COUNTER-EVIDENCE / RED-AGENT NOTE

Under v2.5, aggregate-only counter-data is explicitly downgraded unless paired with cohort decomposition. Counter-narrative tracking is RED's domain — see `handoff_RED/`. Interface contract pending; ad-hoc until RED-CARL handshake protocol document written.

### REVIEW PROCESS NOTE (multi-stage drafting)

v2.5 was drafted in 3 revisions over ~6 hours with 2 rounds of external LLM review:
- r1 (commit c0e06744): initial draft, 12-vector matrix, 58/60 → 54/60
- r2 (commit 36c1e5f3): 13 reviewer critiques addressed; matrix expanded 14 vectors; rescaled
- r3 (commit 036c7247): architectural realignment after Will surfaced RED agent existence; 12 additional structural fixes; honest conviction reframe

Worth carrying forward as practice — thesis-level changes benefit from external review before promotion to canonical.

### STATUS DASHBOARD CHANGES (pending)

STATUS.md mirror updates: convergence matrix table (12 vectors → 14, scores rescaled, total 58/60 → 53/70), header banner (overall capsule), predictions table (+CRL-20, +CRL-21), counter-evidence section removal pointer.

### KB ROW LOGGED

- **KB-CARL-263** — v2.5 thesis statement (Path C ACTIVE + cross-industry data masking + 53/70 recalibration)

### NEXT REFRESH

- v2.5.1 hardening: PENDING_VERIFY items 1-9 (UMich triangulation, foreclosure 2019 baseline, Path C counterfactual, X-threshold operationalization, Brier audit, CONTAINMENT prior audit, COF/SYF candor puzzle, trade duration roll plan, RED-CARL interface)
- Q3 2026 — CRL-21 intermediate falsification window
- Q1 2027 — CRL-20 outer falsification window

---

## 2026-05-01 — LIVE OIL/PUMP REFRESH + CRL-08 REPRICE 78→92%

### NO THESIS VERSION BUMP
**Author:** CARL (live tactical refresh — Brent/WTI/AAA pump 2 trading days stale per >24hr rule)
**Action:** Brent path Apr 30 intraday $126 NEW HIGH (above Apr 29 $115); May 1 pullback to $107-110 on Iran updated peace proposal + Trump WPR 60-day deadline today. **AAA pump $4.392 May 1 — pump pass-through ACCELERATED beyond model**, gap to CRL-08 $4.50 threshold collapsed to $0.108. **CRL-08 reprice 78→92%**. KB-CARL-258 (Brent path), KB-CARL-259 (pump acceleration). VX-CARL-GAS-01 added.

### KEY DATA POINTS
- **Brent**: Apr 30 close $114.66, intraday peak $126 (NEW HIGH). May 1 8:45am ET $116.10 → intraday $107-108 range. 18d move from $98.18 (Apr 13) = +$10-12 / +10-12%.
- **WTI**: ~$106 May 1 (above $105, second weekly gain). Brent-WTI spread $2-4 = compressed (typical $5-10) reflecting physical-spot tightness.
- **AAA Pump**: $4.392 May 1 (+9.2¢ overnight vs Apr 30 $4.300, +33.3¢ WoW vs Apr 24 $4.059, +37.7% YoY vs $3.187). 5 states >$5.
- **Iran cluster**: WPR 60-day deadline TODAY (admin claims "terminated", Republicans defer, Democrats push back, no statutory pause-on-ceasefire); Iran updated peace proposal in Pakistani mediation; Hormuz blockade BOTH WAYS persists; rial -15% Apr 27-29 record low.
- **Hormuz**: per fxleaders 9.1 mbd shut-ins (~9% global supply), single-source un-verified — IEA OMR / EIA STEO needed.

### MECHANISM FINDING
Pump pass-through ACCELERATED — Brent breakout Apr 28-30 transmitted to retail in 3-4 days vs typical 2-4 week lag. Three explanatory channels:
1. Wholesale pre-positioning ahead of summer driving season (Memorial Day inventory pull-forward)
2. Refinery margin compression on diesel divergence (KB-CARL-253) — refiners running yields toward gasoline because they cannot pass distillate cost upstream
3. Hormuz blockade physical-spot tightness creating immediate spot-to-rack pricing

### PREDICTION CHANGE
**CRL-08** (Gas $4.50+ national avg, May-Jun 2026): **78% → 92%**
- Gap to threshold collapsed from $0.27 (Apr 29) to $0.108 (May 1)
- At overnight pace breaches May 2-3, at weekly pace by May 4-5
- 92% not 95%+ because: Iran peace proposal acceptance scenario (Brent collapse to $80-90, 10-15% probability) + behavioral demand destruction at $4.50+ + Trump WPR resolution pressure
- 92% not 85% because: gap collapsed, Brent $107+ + Hormuz blockade structural, Memorial Day premium incoming, Apr 19 conditional firmly in "breaks" branch

### THESIS / VECTOR IMPACT
**Vector #5 (Gas Price Squeeze):** intensity reinforced (already 5/5)
- Behavioral demand destruction at $4.50+ becomes next testable threshold; CARL prior assumption "$4.30+ behavioral breakpoint" may need revision upward if visible consumption maintains through $4.50 cross

**Vector #12 (Stagflation Trap):** energy-side CPI loading reinforced
- May/Jun gasoline +33% YoY adds ~30bps to headline CPI directly + secondary food/transit pass-through
- Fed pure-locked compounded

### STATUS DASHBOARD CHANGES
- Header timestamp + Overall capsule: refreshed with multi-thread May 1 PM integration
- Gas Pump row: $4.229 → $4.392 with full pace data
- Brent row: $110.38 → $107-110 May 1 range, with Apr 30 $126 intraday note
- WTI row: $106.51 → ~$106 May 1
- Iran Cluster Resolution row: WPR deadline + peace proposal + blockade-stalemate
- Predictions table CRL-08 row: 78 → 92% with full rationale

### KB / VX ROWS LOGGED
- **KB-CARL-258** — Brent path May 1 + Iran cluster + WPR deadline
- **KB-CARL-259** — Pump pass-through acceleration mechanism (3-4d vs 2-4wk)
- **VX-CARL-GAS-01** — AAA National Pump (newly tracked row, RED status, $4.392)

### NEXT REFRESH
- Daily AAA pump (track threshold breach if/when it happens)
- Weekly EIA inventory print (Wed) — distillate/gasoline stocks
- Weekly Brent close — sustainability test
- Mid-month IEA OMR — verify Hormuz shut-in numbers

---

## 2026-05-01 — RITHM/NEWREZ Q1 2026 INTEGRATION (NON-BANK SERVICER FRAMEWORK REINFORCED)

### NO THESIS VERSION BUMP
**Author:** CARL (3-day catch-up of Apr 28 print, was Danger Window PENDING)
**Action:** Rithm Q1 2026 integrated. Prior mgmt forecast "DQ will reverse in Q1" QUIETLY DROPPED — replaced by Newrez President Silverstein with "stable QoQ + FHA flatten via FHA modification guidelines normalization." Bear case INTACT but with explicit 12-24mo modification-accounting-cushion caveat added to thesis. Non-bank servicer stress framework REINFORCED. KB-CARL-257.

### KEY READS

**Headline financials (strong):**
- Revenue $1.38B (beat $1.25B cons)
- EAD $289.6M / $0.51 EPS
- Origination $15.5B (-18% QoQ, +31% YoY)
- BV/share $12.51
- NewRez total servicing UPB $850B (incl $257B 3rd-party)

**Credit (the watch metric — soft retraction):**
- Silverstein: "delinquencies remain stable quarter-over-quarter and the FHA delinquencies flattened as we normalize the impact of the new FHA modification guidelines"
- "Stable" ≠ "Reverse" — original forecast quietly dropped, no specific FHA DQ rate disclosed (opacity tell on the metric mgmt walked back), no Q2 DQ guidance

**Balance-sheet signals:**
- Servicer advances receivable: $2,866M Q1 vs $3,091M Q4 = **-$224M / -7.3% QoQ**
- MSR fair value mark loss: -$204M Q1 vs -$422M Q4 = **losses HALVED QoQ**

### THE ACCOUNTING TELL

"Normalize the impact of the new FHA modification guidelines" = HUD/Ginnie 2025 streamline-modification guidance allows trial-modified borrowers to be reclassified to current within 90-180 days, removing them from DQ rolls without underlying borrower performance improvement. Effects:
- Optical DQ smoothing for 12-24 months as new modification cohorts work through
- Advance receivable reduction without credit improvement (modification reclassifies need away)
- Headline DQ optics LAG underlying stress

### THESIS / VECTOR IMPACT

**Vector #10 (Foreclosure Acceleration):** UNCHANGED at 5/5
- Pipeline conversion thesis intact via Q1 ATTOM REO +45% YoY / FL +108%, NOT Rithm optic
- Bank-side will see underlying stress before optical DQ catches up

**Non-bank servicer stress framework:** REINFORCED
- Rithm "stable via mod-accounting" = directionally WEAKER input than "improving"
- PennyMac FHA DQ 7.5% (+160bps QoQ, KB-CARL-prior) remains cleaner stress proxy
- Bridge test: PennyMac Q1 (late Apr/early May) — does PennyMac FHA DQ continue rising despite same accounting tailwind, or also "stabilize"? Differential = signal on whether mod-accounting is universal cushion or NewRez-specific

**Path C (Housing → Banks):** transmission live; bank-side is the cleaner read

### COUNTER-EVIDENCE (RED-style flag)
- Headline beat was strong (revenue +10% vs cons, EAD beat)
- Market may take RITM print bullishly, pricing headline optics NOT modification-accounting nuance
- Stock-price action could diverge from underlying credit thesis for several quarters before pipeline visibly turns
- This is a counter-evidence input for any "RITM short" trade idea — the optical-cushion timeline is real and front-loads the thesis-vs-tape divergence

### STATUS DASHBOARD CHANGES
- Non-Bank Servicer Stress row: appended Rithm Q1 detail
- Danger Window Apr 28 row: marked Rithm RESOLVED, Case-Shiller still PENDING
- Apr 28 Rithm earnings row: struck-through with RESOLVED note

### KB ROW LOGGED
- **KB-CARL-257** — Rithm Q1 2026 integration with full modification-accounting cushion framework

### NEXT REFRESH
- Late Apr / early May — PennyMac Q1 (bridge test for mod-accounting universality)
- Q3 2026 — Rithm/Newrez Q2 (does "stable" hold?)

---

## 2026-05-01 — APR 30 GDP Q1 ADVANCE INTEGRATION (VECTOR #12 HARDENED)

### NO THESIS VERSION BUMP
**Author:** CARL (Will-directed catch-up of Apr 30 BEA print, was Apr 29 PM2 SCRATCH PRIORITY-1)
**Action:** Apr 30 BEA Q1 2026 GDP advance integrated. Headline 2.0% real (vs 2.3% cons / vs 1.3% GDPNow Apr 7) softens "stall speed" framing 0.7pp. **But realized Q1 NIPA inflation PCE +4.5% / core PCE +4.3% / GDP-domestic-purchases price index +3.6% data-confirms UMich un-anchoring (1Y exp 4.7%, 5-10Y 3.5%) — Vector #12 (Stagflation Trap / Fed Locked) HARDENED via realized inflation, not just expectational.** Q4 2025 revised down 0.7→0.5% on annual revision. STATUS dashboard updated, 3 KB rows added, ROADMAP thread closed.

### KEY READS

**Headline:**
- Real GDP Q1 2026: **+2.0% annualized** (advance estimate)
- vs consensus 2.3% (miss by 0.3pp)
- vs Atlanta Fed GDPNow Q1 final 1.3% (Apr 7 anchor — beat by 0.7pp)
- GDPNow stale anchor; Q2 GDPNow next replacement read

**Inflation (the real signal):**
- PCE price index Q1 NIPA: **+4.5% annualized**
- Core PCE Q1 NIPA: **+4.3% annualized**
- GDP price index gross domestic purchases: **+3.6%**
- Reference: Feb 2026 monthly Core PCE was 3.0% YoY — Q1 NIPA 4.3% reflects Jan/Feb/Mar re-acceleration that monthly YoY had not yet fully priced
- Bridge: March monthly core PCE (release ~May 30) should accelerate from Feb 3.0% YoY toward 3.3-3.5% to be consistent with Q1 NIPA 4.3% annualized

**Q4 2025 revision:**
- 1.4% (1st est) → 0.7% (3rd est) → **0.5% (annual revision Apr 30)**
- Cumulative downward revision -0.9pp from initial print
- Pattern: aggregate data systematically over-states near-term resilience, revises down as more granular source data incorporates

**Composition (K-shape signal):**
- Drivers: equipment (information-processing-heavy = AI capex), intellectual property products, inventory build
- Drags: residential AND non-residential structures (housing transmission live both sides)
- Services PCE driver: **healthcare-led** (forced consumption, non-discretionary cost-push)
- AI capex concentration via equipment + IPP pairs DIRECTLY with META + MSFT capex prints AMC Apr 30 (BOARD SIG-029-004) — feedback loop: if hyperscalers guide capex DOWN, Q1 2.0% headline driver hollows out for Q2

### THESIS / VECTOR IMPACT

**Vector #12 (Stagflation Trap / Fed Locked):** REINFORCED
- Score unchanged (already 5/5 max)
- Qualitative intensity HIGHER — UMich expectations un-anchoring is now data-backed not panic-spike
- Fed reaction function: cut blocked (4.3% core PCE ratifies un-anchoring), hike blocked (2.0% growth + ATL sentiment)
- 1970s analog confirmed: Fed loses inflation credibility → term premia widen → mortgage rates sticky high regardless of Fed front-end direction → housing transmission compounds (Vector #10 reinforcement via term-premium channel)

**Vector #10 (Foreclosure Acceleration):** secondary reinforcement
- Q1 GDP residential structures DRAG = housing transmission empirically live in NIPA, not just micro data
- Term-premium channel from Vector #12 = sustained mortgage-rate stickiness even if Fed cuts

**Two new predictions booked from this print:**
- **CRL-18** (60%, May 28 resolves) — Q1 2026 GDP second estimate revises advance 2.0% down by 0.2-0.4pp into 1.6-1.8% range. Pattern basis: Q4 2025 cumulative -0.9pp revision (1.4 → 0.7 → 0.5).
- **CRL-19** (70%, ~May 30 resolves) — March 2026 monthly Core PCE YoY accelerates from Feb 3.0% to 3.3-3.5% range. Bridge test for Q1 NIPA 4.3% annualized consistency.

CRL-09 (JOLTS Mar) and CRL-12 (SYF FY26 NCO) unrelated to this print.

### STATUS DASHBOARD CHANGES
- Header timestamp: Apr 29 PM2 → May 1 ~14:00 UTC
- "Overall" capsule: prepended May 1 GDP capsule
- GDP Q4 2025 row: 0.7% → 0.5%
- GDPNow Q1 row REPLACED with **Real GDP Q1 2026 (advance) 2.0%** + new **PCE Q1 NIPA 4.5%** + **Core PCE Q1 NIPA 4.3%** + **GDP Price Index Q1 3.6%** rows (+3 net rows)
- Vector #12 row: "REINFORCED May 1" tag added with realized PCE evidence
- Convergence summary line: May 1 reinforcement note added

### KB ROWS LOGGED
- **KB-CARL-254** — GDP Q1 2026 advance 2.0% headline + composition (Vector #10 + #12)
- **KB-CARL-255** — Q1 NIPA inflation PCE 4.5% / core 4.3% (Vector #12 hardening)
- **KB-CARL-256** — Q4 2025 GDP revision 0.7 → 0.5% (revision pattern flag)

### NEXT REFRESH
- May 28 — BEA second estimate for Q1 2026 (revision risk -0.2 to -0.4pp per pattern)
- May 30 — March monthly core PCE (bridge test for Q1 NIPA 4.3% consistency)
- Jun 26 — BEA third estimate Q1 2026

---

## 2026-04-29 (PM2) — AAA LIVE PUMP REFRESH + DIESEL DEMAND DIVERGENCE

### NO THESIS VERSION BUMP
**Author:** CARL (PRIORITY-1 from Apr 29 PM SCRATCH — close stale pump data window)
**Action:** Stale Apr 17 pump data refreshed live. CRL-08 78% reprice confirmed on track inside model. New K-shape finding logged: diesel-vs-gasoline divergence as freight demand destruction signal. STATUS dashboard updated. KB-CARL-252, KB-CARL-253 logged.

### LIVE DATA CONFIRMATION

**Gas Pump (CRL-08 confirmation):**
- AAA national regular: **$4.229 / gal** (Apr 29 live)
- vs prior STATUS print $4.076 (Apr 17): **+$0.153 / 12 days**
- Pace: yesterday $4.176 → +5.3¢ overnight; week-ago $4.020 (+$0.21 / 7d); month-ago $3.980 (+$0.21 / 30d); YoY $3.161 (+$1.07 / +33.8%)
- Brent pass-through completion: ~40% of crude move (+$12 / +12.5%) absorbed in pump (+$0.21 / +5.0%) — textbook 2-4wk lag still in pipeline
- **CRL-08 78% holds** — gap to $4.50 threshold = $0.27, 30d pace = $0.21, on track inside Apr 29 AM reprice model. Live print is confirmatory, not deflective.

**Diesel (NEW K-SHAPE FINDING):**
- AAA national diesel: **$5.464 / gal** (Apr 29 live)
- vs prior STATUS print $5.608 (Apr 13 EIA): **DOWN -$0.144 / -2.6%** despite Brent breaking $98 → $110+ same window
- Week-ago $5.489 (-$0.025 falling); month-ago $5.406 (+$0.058 mildly higher but rolling)
- **The signal: diesel falling while gasoline rises = freight/business-side demand destruction.** Distillate-weighted to trucking, freight rail, ag diesel, marine bunker — leading-edge business-cycle indicators. When refiners cannot pass distillate cost upstream and shift yields toward gasoline, soft distillate demand is the residual explanation.
- **Direct K-shape signal:** consumer-side pump rises (cost squeeze on bottom 60%) + business-side diesel falls (demand pullback on freight/ag) firing simultaneously and in opposite directions. Vector #9 (K-Shape Converging Downward) reinforced via business-side extension.

### CONVERGENCE MATRIX

- **Vector #5 (Gas Price Squeeze): 5/5 unchanged.**
- **Vector #9 (K-Shape Converging Downward): 5/5 unchanged** — but qualitatively reinforced via diesel divergence as new business-side demand-destruction confirmation.
- **Score: 58/60 held.**

### NEXT TRIGGERS

- **Diesel sustained 4+ weeks soft while Brent stays $100+:** would significantly strengthen freight-demand-destruction interpretation. Track ATA truck tonnage, Cass Freight Index, EIA distillate stocks (Wed weekly), refinery utilization.
- **Pump weekly refresh:** continue live AAA tracking; Memorial Day (May 25) seasonal premium expected to add $0.10-0.15.
- **CRL-10 (Food CPI):** ag-diesel softening could partially offset urea/wheat input cost — minor counter-signal, watch for compounding effects.

---

## 2026-04-29 (PM) — CRL-08 REPRICE ON BRENT BREAKOUT + CEASEFIRE-BRANCH RESOLUTION

### NO THESIS VERSION BUMP
**Author:** CARL (Step 4 of Apr 29 catch-up — Brent → CRL-08 reprice)
**Action:** CRL-08 confidence 65% → 78%. Mirror updated in STATUS.md predictions table. KB-CARL-248 logged.

### PREDICTION UPDATE

**CRL-08 — Gas pump prices hit $4.50+ national avg by May-Jun 2026**
- **Confidence: 65% → 78%**
- **Timeframe unchanged: May-Jun 2026**
- **Rationale (binary-branch resolved + Brent breakout):**
  - Apr 19 prior structure was conditional: 80% if Apr 21 ceasefire breaks, 30% if it holds, blended to 65% pre-resolution.
  - Apr 21 ceasefire did NOT resolve cleanly. Apr 24 contradictory diplomacy (Araghchi Islamabad, Trump talks-relaunch frame vs IRGC-Raja denial); WTI dropped to $94.40 on talks-hope then breakout.
  - **Apr 28-29: Brent $110.38 close / $115 intraday — 8-session streak, highest since June 2022, IEA on-record "largest supply shock on record" framing.** Cluster intensified, did not de-escalate.
  - Pass-through math: Brent +$12 from $98 → +$0.25-0.30/gal pump in 2-4wks → from $4.076 baseline → ~$4.30-4.40 in steady state before further oil moves. Closing $0.42 gap requires Brent sustained $110+ AND (refiner margin expansion via distillate tightness OR Memorial Day seasonal +$0.10-0.15 OR another $5-8 leg from kinetic event).
- **Why 78% not 85%+:**
  - $0.42 gap still meaningful — needs more than just current Brent staying flat
  - MS/Piper Sandler counter-frame (KB-CARL-236) valid: US net-exporter + 1.8% aggregate gas share caps structural multiplier
  - Demand destruction at $4.30+ retail moderates further moves
  - Brent $115 was intraday spike; close $110.38; 8-week sustainability not yet proven
  - Trump talks-relaunch optics could re-emerge (Witkoff/Kushner reportedly to Pakistan)
- **Why 78% not 65%:**
  - Binary conditional has effectively fired toward "breaks" branch
  - Cluster intensifying not resolving (Iranian rial -15% in 2 days, USS Pinckney shadow-fleet intercept Apr 26, Merz "no exit strategy" Apr 28)
  - IEA "largest supply shock on record" framing is uncharacteristic escalation language for that body
- **Invalidation unchanged.**

### CONVERGENCE MATRIX

- **Vector #5 (Gas Price Squeeze): 5/5 unchanged.** Already maxed; reprice reflects probability not vector score.
- **Score: 58/60 held.** No vector flips.

### NEXT TRIGGERS

- **Pump pass-through validation:** AAA daily refresh needed — pump $4.076 (Apr 17 stale) likely already $4.20-4.30 area on Brent $110.
- **Brent sustainability test:** does $110+ hold through next week, or pull back on talks-hope re-emerging?
- **May UMich + CPI:** validates inflation expectations un-anchoring vs noise; pairs with CRL-08 transmission read.
- **Memorial Day weekend (May 25):** organic seasonal premium kicks in — natural test of pump trajectory.

---

## 2026-04-29 — APR 21 EARNINGS CATCH-UP SYNTHESIS (10-day-late processing)

### NO THESIS VERSION BUMP
**Author:** CARL (catch-up after 10-day session gap; sub-agents POLLY + HOMER + SYF/COF research fork)
**Action:** Three earnings clusters processed retroactively. CRL-12 confidence revised DOWN 77→55%. STATUS dashboard +6 new rows (SYF/COF Q1, DHI Q2, PHM Q1, UNH Q1, ELV Q1). Convergence unchanged at 58/60.

### PREDICTION UPDATES

**CRL-12 — SYF FY2026 NCO exceeds 6.0% guidance ceiling**
- **Confidence: 77% → 55%**
- **Rationale:** SYF Q1 NCO 5.42% (-96bps YoY); SYF revised FY2026 guidance DOWN to <5.5% (well below 6.0% threshold CRL-12 requires). Headline path requires fresh credit loosening or material macro deterioration to overshoot. Survivor-pool caveat retained (Home & Auto receivables -3.7% YoY, active accounts -0.7%, ACL ratio BUILT +36bps to 10.42% despite clean headline = mgmt hedging forward risk). CFPB late-fee reinstatement remains tail risk that could push NCO back up. K-shape composition-masking (KB-CARL-243/244) confirmed on the ALLY framework.
- **Why not lower than 55%:** macro deterioration acceleration (gas $4.50+, food CPI Q3) could still pressure NCO into Q3-Q4 even on the cleaner book; ACL build signal preserves ~one-quarter pull-forward risk. 50% would imply CRL-12 has lost most of its load-bearing weight; 55% reflects still-meaningful but reduced probability.
- **Invalidation unchanged.**

### EVIDENCE UPDATES (no prediction-level changes)

**SYF/COF Q1 2026 (Apr 21):**
- SYF as above. COF Domestic Card NCO 5.1% (-109bps YoY) clean headline; **Auto book is the ALLY analog** — originations +21% YoY w/ "slightly higher subprime mix" admitted by management; $155M Consumer Banking ACL build + $230M total ACL build citing "potential downside scenarios." Discover acquisition: legacy book contracting -1.2% via prior tightening; replacement originations 8% on COF platform now → ~100% by Q3 2026 (forward NCO will reflect COF near-prime standards).
- KB-CARL-243 (SYF actuals), 244 (SYF ALLY scorecard), 245 (COF actuals), 246 (COF ALLY scorecard).

**DHI Q2 FY2026 (Apr 21) + PHM Q1 2026 (Apr 23):**
- DHI GM 20.1% reported / 19.7% normalized — beat 19.0-19.5% guide on litigation/warranty benefit + cost control, NOT price recovery. ASP -3% YoY $361,600. Cancellations 16% — "vast majority mortgage qualification failure." First-time 65% of closings. FY26 closings TRIMMED -500.
- PHM GM 24.4% MISS (-310bps from 27.5% Q1'25). Incentives +290bps to 10.9%. Q2 GM guided 24.1-24.4% = sequential compression. **PHM management names "K-shape" explicitly on call** — active adult orders +14% YoY, first-time flat.
- **CRITICAL:** $10,900/home tariff cost NOT in 2026 margins; FY27 hit. Current builder margins are the **pre-tariff floor**.
- Vector #10 (Foreclosure Acceleration) reinforced via new-home channel — cancellations are mortgage-qualification failures (consumer stress, not preference shift).

**UNH Q1 (Apr 21) + ELV Q1 (Apr 22):**
- UNH MCR 83.9% (vs 84.8% Q1'25; est ~85.5%) — NO MLR breach. MA membership -965K Q1 (FY guide ~-1.3M loss). FY adj EPS guide raised to >$18.25. DOJ investigation ongoing.
- ELV BCR 86.8% (+40bps YoY) — NO breach. Adj EPS $12.58 BEAT (vs $11.03 est). FY guide raised to >$26.75. $935M one-time CMS accrual (RA dispute, compliance Jul 31).
- **MA cost trend ~10% embedded in 2026 pricing** at both carriers (vs historical 3-5%) — re-acceleration thesis PARTIALLY CONFIRMED. V28 RAF recalibration unresolved → H2 2026 MLR re-acceleration risk.
- Mechanism note: insurer beats driven by membership culling + repricing → bronze-plan ACA shift = high-deductible trap activating = consumer-side stagflation transmission, **Vector #12 intact** (insurance is transmission channel, not clearing mechanism).

### CROSS-DOMAIN SYNTHESIS (KB-CARL-247)

K-shape WIDENING confirmed simultaneously across three independent earnings prints:
- **SYF**: bottom-of-K borrowers EXITING the book (survivor-pool); not recovery
- **PHM**: management explicitly labels "K-shaped economy" on call; active adult +14% YoY while first-time flat = top-of-K still buying, bottom frozen
- **POLLY (UNH/ELV)**: bronze-plan ACA shift = high-deductible trap activating in real time; MA cost trend re-acceleration ~10% (vs 3-5%)

Convergence Vector #9 (K-Shape Converging) remains 5/5. The earnings cluster did NOT contradict this; it provided three independent confirmations from credit-card, builder, and insurer angles. Aggregate "improvement" data continues to mask cohort-level deterioration.

### CONVERGENCE MATRIX

- **Vector #10 (Foreclosure Accel)**: 5/5 unchanged. New-home cancellations (DHI 16%, PHM 13%) "mortgage qualification failure" framing reinforces pipeline conversion thesis.
- **Vector #12 (Stagflation Trap)**: 5/5 unchanged. POLLY high-deductible trap + UMich Final 5-10Y inflation expectations 3.5% (un-anchoring deepened) = consumer-side stagflation confirmation.
- **Score: 58/60. Held.**

### NEXT TRIGGERS

- **CRL-08 reprice (gas $4.50+):** pending Brent breakout integration (Step 4 of this session).
- **CRL-05 (CC 90+ DQ >13.74% GFC):** SYF survivor-pool dynamic raises a structural question — if the worst SYF borrowers are exiting (book/charged off), where does the 12.7%→13.74% delta come from? Possible answer: prime/near-prime migration. CRL-05 mechanism shifts from subprime-deeper to prime-down. Confidence not changed pending Q1 NY Fed HHDC data (mid-May).
- **CRL-15/16/17:** SB and POP-driven predictions unchanged; no new earnings input.

---

## 2026-04-19 (PM) — BOARD SIGNAL INTEGRATION (Apr 17–19 WALTER dispatches)

### NO THESIS VERSION BUMP
**Author:** CARL (BOARD/INDEX.md integration pass — 15 CARL-relevant signals out of 30)
**Action:** Evidence update only. Convergence unchanged at 58/60. No vector score change. Two new rows in STATUS Macro/Energy (Qatar LNG, Iran Day-Cluster). One counter-frame logged to RED team. One prediction confidence adjusted.

### TRIGGER

Will directed CARL to use `BOARD/INDEX.md` as a pull-source while the file-based messaging overhaul is pending. 30 dispatches since Apr 17 PM#3 closeout. Highest-load signals: SIG-021 (MS oil-shock 1990-vs-2026 counter-framework), SIG-030 (Qatar LNG verified ~20% global offline since Mar 2), SIG-024/028/029 (Iran 8-channel escalation day-cluster Apr 18–19 + Netherlands LCP-O Apr 20).

### PREDICTION UPDATES

**CRL-08 — Gas pump prices hit $4.50+ national avg**
- **Confidence: 60% → 65%**
- **Timeframe: "extended from Apr 5" → "May-Jun 2026 (extended from Apr 5)"**
- **Rationale:** Apr 8 ceasefire had dropped confidence 80→60% (oil crashed 15% to $98). Three new loadings reverse some of that cut: (a) Qatar LNG verified ~20% global supply offline since Mar 2 via Iranian drone strikes on Ras Laffan + Mesaieed + QatarEnergy force majeure (KB-CARL-234); (b) Apr 18–19 8-channel Iran escalation day-cluster (KB-CARL-235); (c) Netherlands LCP-O activates Mon Apr 20. Apr 21 ceasefire expiry is a BINARY event — conditional probabilities: 80% on May-Jun $4.50 if ceasefire breaks, 30% if it holds. Bump held at 65% (not 70%) to honor the MS/Piper Sandler counter-frame's legitimate US net-exporter asymmetry (see RED team entry below).
- **Invalidation unchanged.**

### RED TEAM — MS/PIPER SANDLER OIL-SHOCK COUNTER-FRAME LOGGED

SIG-021 (MS 6-row 1990-vs-2026 comparison + Piper Sandler "gas matters less" note, 1.8% aggregate consumer spending share, US net-exporter since 2020, "real economy strong," "financial conditions liquid"). Logged to `red_team/COUNTER_LOG.md` with three-point rebuttal:

1. **Aggregate-masking (core CARL K-shape rebuttal):** 1.8% is population-weighted; bottom 60% gas share is ~4-5% of disposable income at $4.08. The K-shape IS the thesis — aggregate comfort is NOT the transmission channel.
2. **"Real economy strong":** Headline, not cohort. JOLTS 0.91 (inverted), LFPR 61.9%, UMich 47.6, FICO Spring 2026 -62pt avg, 9.2M student loan default cohort — all fire independently of any gas move.
3. **"Financial conditions liquid":** Masks structured-credit cracking — EART Class E CE breached (Apr 16), CMBS MF DQ 7.15% ATH (Trepp Mar), AFRMT BNPL composition degrading.

**Outcome:** Counter-frame does NOT change convergence score or CRL-05/CRL-08 confidence (beyond the explicit cap on the CRL-08 bump). Logged as legitimate dampener on magnitude, not invalidator of mechanism. Cached for recall next time MS/Piper material appears.

### KB ENTRIES ADDED (6)

- KB-CARL-234: Qatar LNG ~20% global offline since Mar 2 (A2 EMPIRICAL, 0.97 confidence via WALTER verify-research)
- KB-CARL-235: Iran 8-channel escalation day-cluster Apr 18–19 (A2 EMPIRICAL)
- KB-CARL-236: MS/Piper Sandler oil-shock counter-frame (B2 ASSUMPTION)
- KB-CARL-237: Institutional positioning extreme — not retail (B2 EMPIRICAL)
- KB-CARL-238: China Shock 2.0 info-only, attenuated US channel (A2 EMPIRICAL, stays ZHAO-owned)
- KB-CARL-239: KRE vs XLF counter-framing info-only (C3 EMPIRICAL, stays REGINALD-owned)

KB row count: 233 → 239.

### STATUS.md CHANGES

- Header block: Apr 19 BOARD integration note + ceasefire binary framing
- Macro/Energy section: +Qatar LNG row (🔴, verified since Mar 2), +Iran Day-Cluster row (🔴, 8 channels Apr 18–19)
- Cross-agent WAR row: updated with Netherlands LCP-O Apr 20 and ceasefire Apr 21 binary

### AWARENESS GAP CLOSED

Qatar LNG disruption in force since Mar 2 2026 was not previously in CARL STATUS or KB despite being a material multi-vector cost-squeeze loader (gas/LNG/industrial input). Gap identified via SIG-030 verify-research; filed KB-CARL-234 + STATUS row.

---

## 2026-04-17 (PM) — v2.4.1: PAYMENT HIERARCHY TIMELINE PUSHED (ALLY Q1 COUNTER-EVIDENCE + AUDIT)

### THESIS v2.4 → v2.4.1
**Author:** CARL (post-ALLY Q1 earnings + CARL-performed FY2024/FY2025 10-K reclassification audit)
**Action:** Minor refinement. Convergence unchanged at 58/60. No vector score change. Mechanism-level revision to payment hierarchy pathway timing.

### TRIGGER

Ally Financial Q1 2026 earnings (Apr 17): retail auto NCO 1.97% (-17bps QoQ), 30+ DQ 4.6%, 5th/4th consecutive quarter of YoY improvement respectively. Guidance maintained. Mgmt: "consumer behavior is resilient." Stock up. First real-time test of payment hierarchy cascade claim (prime/near-prime auto = next domino after subprime 60+ DQ breached 6.9% ATR) — headline test result: **CLEAN**, four consecutive quarters improving.

### AUDIT PERFORMED

Pulled ALLY FY2024 10-K (EDGAR acc 0000040729-25-000006, filed 2025-02-19) and FY2025 10-K (acc 0000040729-26-000005, filed 2026-02-25). Ran forensic comparison against REGINALD's regional bank reclassification framework (Layers 1-3: Memo Item 3, NDFI-in-C&I, sub-category reclassification) adapted to auto-lender toolkit (A-G: HFI→HFS, whole-loan sales, FDM/TDR, runoff segmentation, mix shift, reserve release, CLN/securitization routing). File: `domain/sources/ally/RECLASSIFICATION_AUDIT_FY2025.md`.

**Findings — NOT present:** HFI→HFS dumping, TDR re-aging, runoff/legacy segmentation, new line-item taxonomy, NDFI-analog hiding place, dealer/floorplan stress (floorplan shrinking).

**Findings — PRESENT (composition masking, not accounting fraud):**
- Used retail S-tier origination mix: **40% → 37%** (-3pp FY2024 → FY2025)
- Nonprime exposure (FICO<620): **9.7% → 10.1%** (+40bps, +$0.4B to $8.6B)
- ACL: **$3.7B → $3.5B** (-$224M / -6%) = reserve release into mix downgrade (Layer F)
- CLN issuance: **$0.77B → $1.1B** (+43% YoY), reference pools $7B → $10B (Layer G)
- Originations +11% YoY into worsening mix

### MECHANISM REVISION

**Old view (pre-Apr 17 2026):** Payment hierarchy — subprime → near-prime → prime auto — transmission in 1-2 quarters. ALLY Q1 was the first real test; expected to show early signs of near-prime migration (NCO ticking up, DQ stopping improvement).

**New view (v2.4.1):** Headline Ally Q1 is composition-driven, not genuine improvement:
- **Seasoning:** FY2024 higher-FICO originations rolling into 2026 NCO window (lower losses)
- **Mix routing:** Shift from used retail toward new retail (slower loss curve at same FICO)
- **Tail-risk routing:** CLN/securitization expanded +43% YoY, exporting first-loss tail to ABS investors

The FY2025 origination cohort is **like-for-like worse** than FY2024 — deterioration is embedded in the book, not yet in the P&L. The 18-24 month vintage seasoning lag means FY2025 loss window opens **2H 2026 and Q1 2027**.

**Payment hierarchy thesis NOT invalidated — TIMELINE PUSHED.** Near-prime P&L stress window moves from Q1-Q2 2026 to 2H 2026 / Q1 2027.

### CROSS-THESIS IMPLICATIONS

**K-shape within auto credit (new refinement):** Subprime ABS cracking (EART Class E CE breached Apr 16, AMCAR ~2mo, SDART ~7mo) co-exists with near-prime headline-clean = intra-credit K-shape. ABS monoline stress is localized; doesn't migrate up-quality automatically — it migrates via seasoning of the near-prime vintage being originated *now* under looser standards, which plays out with a ~18 month lag.

**Counter-signal containment:** The "Ally Stable 🟢" row in STATUS (Feb 10-D data) is CONFIRMED and EXTENDED, not overturned. But "stable" at headline ≠ "clean" at cohort. STATUS must distinguish the two.

**REGINALD handoff:** Auto-lender reclassification framework (KB-CARL-225) translates their 3-layer bank framework. CLN routing = structural analog of their C&I hiding place. Sent as outbox signal.

### PREDICTION UPDATES

**CRL-05 — CC 90+ DQ breaches 13.74% (GFC peak)**
- **Confidence: 85% → 82%** (mild reduction on headline/cohort distinction)
- **Rationale:** Student loan cascade still adding +0.5-1.0pp pathway, multi-vector cost squeeze intact — these don't require near-prime auto migration to work. But ALLY counter-evidence weakens the "consumer credit generally migrating up-quality" framing at the headline level. Cohort-level deterioration (nonprime share growing) preserves the thesis, just shifts the visibility window later.
- **No change to invalidation criteria.**

**CRL-02 — Subprime Auto 60+ DQ crosses 7.0%** (already CONFIRMED*)
- **Confidence: no change.** Subprime stress is independently confirmed; Ally near-prime data irrelevant to this cohort.

### NEW FRAMEWORK ENTRY

**Auto-lender reclassification methodology** (KB-CARL-225): 7-lever translation of REGINALD regional bank framework. Apply to SYF (Apr 21), COF (Apr 21), AXP (Apr 23). For SYF: no used-car tail, but CLN/mix shift via CareCredit vs Private Label segmentation potentially applicable.

### DANGER WINDOW UPDATE

Added: **Q1 2027** — FY2025 origination cohort full seasoning window. Near-prime auto P&L stress realization if thesis holds. If NCO/DQ deteriorate on unchanged macro at this point, thesis REACTIVATES HARD at the headline level.

---

## 2026-04-17 — v2.4: FORECLOSURE PIPELINE CONVERTING + CREDIT CASCADE EXECUTING

### THESIS v2.3 → v2.4
**Author:** CARL (via Apr 15 data processing — STUE + HOMER sub-agents)
**Action:** Minor refinement. Vector #10 (Foreclosure) upgraded 4→5. Convergence 57/60 → **58/60 CRITICAL**. Two mechanism confirmations added.

### CONVERGENCE MATRIX — Vector #10 Upgrade
| Vector | Change | Reason |
|--------|--------|--------|
| #10 Foreclosure Acceleration | 🔴 4 → 🔴🔴 **5/5** | ATTOM Q1 2026 (rel Apr 16): **Q1 REO completions 14,020 (+45% YoY)**. Previously the 878K 90+/FC pipeline was ACCUMULATING (inflow > outflow). Q1 2026 is first quarter at-scale CONVERSION — cure collapse (-40%) now translating to actual completions. Regime change, not incremental. FL Q1 REO +108% YoY (greatest nationally). Q1 filings 118,727 (+26% YoY). March monthly 45,921 filings (+18% MoM). |

### PREDICTION UPDATES

**CRL-04 — Student Loan 90+ DQ breaches 10%**
- **Confidence: 97% → 98%** (OPEN-NEAR CONFIRMED)
- **Evidence:** FICO Spring 2026 (data Apr 17): SL DQ rate now ~9.8% (up 25% from 7.9% Apr 2025). 6.1M borrowers with SL DQ reported Feb-Apr, avg score drop -69pts (25% saw -100pt+).
- **Counter-signal (minor):** Sweet v. McMahon Apr 15 ruling triggers ~271K tradeline deletions — credit RECOVERY for bounded cohort (~3% of defaulted borrowers). Directionally opposite but magnitude insufficient to move aggregate.
- **Near-term test:** NY Fed Q1 2026 QHDC (~May-Jun).

**CRL-06 — Foreclosures exceed 70K/quarter**
- **Confidence: 70% → 78%**
- **Evidence:** Q1 2026 ATTOM: 82,631 FC starts (already >70K on starts basis), 118,727 filings (+26% YoY), 14,020 REO (+45% YoY). Depending on threshold interpretation, may be CONFIRMED at starts level. Q2 projection likely higher on FL judicial lag.

### NEW MECHANISM / FLOW ENTRY

**FLOW-CARL-12.04 — Foreclosure Pipeline → REO Conversion → Bank Loss Realization (Path C Activation)**
- **Status:** ACTIVATING-RED (new)
- **Pathway:** Borrower 90+ DQ → cure rate collapse → foreclosure filing → legal process 3-12mo → REO completion → actual loss realized → NCO line → earnings hit → bank tightens → consumer denied. Non-bank servicer variant: Ginnie advance drain → warehouse line stress → potential failure (MFS UK template).
- **Why it matters:** Path C (Housing → Banks) previously theoretical, now mechanically active. Q1 bank earnings cluster (Apr 17-28: CFG/PNC/RF/FITB/MTB) = first visibility window for provision build on mortgage/CRE.

### STUDENT LOAN VECTOR CONFIRMATIONS

- **Sweet v. McMahon Apr 15 deadline MISSED** — DOE did not comply. Auto Full Relief triggered for ~170K non-Exhibit C borrowers. Combined with Exhibit C (missed Jan 28 ~170K), total ~271K. Self-executing, no stay. NOT thesis invalidation (court-compelled, bounded cohort).
- **SAVE judicially dead** — 8th Cir Mar 10 reversed + entered final judgment. Dual-elimination (legislative WFTCA Jul 2025 + judicial Mar 2026). Jul 1 transition locked.
- **AFT v. MOHELA in discovery** — Next status conf May 28. Three concurrent class actions active.

### NEW VECTORS (VX)

- **VX-CARL-HSG-05** — Foreclosure Pipeline Quarterly REO Completions (14,020 Q1 2026, RED)
- **VX-CARL-BLDR-01** upgraded to RED (HMI 38 → 34, breaches <40 threshold; new tariff cost shock +$10,900/home)
- **VX-CARL-HSG-01** updated (PMMS 6.37% → 6.30%)
- **VX-CARL-SL-02** updated (SL 90+ DQ ~9.8% per FICO Spring 2026)
- **VX-CARL-6.06** updated (FL Q1 REO +108% YoY, judicial state completion wave)

### KB ENTRIES ADDED

KB-CARL-215 through KB-CARL-221 (7 entries): Sweet v. McMahon ×2, DOE motion context, SAVE judicial death, FICO Spring 2026 cascade, MOHELA discovery, NAHB HMI April, ATTOM Q1 Foreclosures.

### HONEST ASSESSMENT

**Strengthened:** Mechanism confirmations — pipeline conversion (HSG), credit cascade execution (SL), Vector 10 upgrade defensible (not self-inflicted).
**Unchanged:** Market-transmission leg (HY OAS 294bps tight, SPX not in crisis, JPM Q1 benign). Complacency gap persists or widens.
**Counter-signal:** Sweet ruling produces credit RECOVERY for ~271K — directionally opposite the cascade. Small but directionally notable.

### TRIGGER FOR NEXT VERSION BUMP

- Q1 bank earnings cluster (Apr 17-28) confirming Path C provision build → v2.5 with full Path C activation upgrade.
- OR SYF Q1 Apr 21 breaching >6% NCO → credit cascade confirmed at issuer level.
- Reversal criterion: bank earnings downplay stress AND SYF NCO <5.0% → thesis mechanism questioned.

---

## 2026-04-14 — v2.3: FED LOCK MECHANISM + SUBPRIME AUTO CURE COLLAPSE CONFIRMED

### THESIS v2.2 → v2.3
**Author:** CARL (via WALTER inbox processing + ABS drill-down)
**Action:** Major thesis refinement. Vector #12 Stagflation Trap added. Convergence 51/55 → **57/60 CRITICAL**.

### CONVERGENCE MATRIX — Vector #12 Added
| Vector | Change | Reason |
|--------|--------|--------|
| #12 Stagflation Trap / Fed Locked | **NEW** 🔴🔴 5/5 | WALTER CPI/UMich signal integrated (Apr 10 data): UMich Apr preliminary 47.6 — RECORD LOW (biggest MoM drop in series). 1Y inflation exp 4.8% (+100bps), 5-10Y exp UN-ANCHORING at 3.4% (Fed red line breached). CPI Mar +3.28% YoY headline, +2.61% core. Mechanism: Fed cuts now validate un-anchoring → inflation-negative, not stimulus. Cannot cut (expectations), cannot hike (sentiment ATL). 1970s Volcker analog. RED Stagflation Spiral upgraded. HENRY "Fed cuts pushed H2 2027" reinforced. |

### KEY EMPIRICAL CONFIRMATIONS (Apr 14)
- **Subprime auto cure collapse confirmed industry-wide.** SDART 2024-1 (30+ DQ -43bps, CNL +26bps), EART 2024-2 (-177bps/+52bps deep subprime), AMCAR 2024-1 (-175bps/+24bps). HAROT 2024-2 prime control stable. Pattern: DQ bucket draining to charge-offs, not cures. EART already at projected terminal CNL (13.06%). KB-CARL-207, KB-CARL-210.
- **Discover ABS structure dissolved.** DCMT filed Form 15-12G Dec 19 2025 post-CapOne merger. DCENT in defeasance. Removed from abs_monitor. CC data now rolls into COMET. KB-CARL-208, KB-CARL-209.

### PREDICTIONS
No new predictions added — existing CRL-01 through CRL-17 remain appropriate. Notes updated on CRL-05 (cascade confirmation), CRL-08 (FL crossed $4). Future drill-down (#2 CNL trigger proximity) may generate CRL-18.

### KB Added (Apr 14: 7 entries)
KB-CARL-204 (UMich record low), KB-CARL-205 (CPI Mar), KB-CARL-206 (inflation expectations un-anchoring), KB-CARL-207 (SDART Feb loss acceleration), KB-CARL-208 (Discover deregistration), KB-CARL-209 (COMET baseline), KB-CARL-210 (cross-trust cure collapse confirmation).

### Cross-Agent Signals
- Previously sent: CARL → REGINALD (non-bank servicer warehouse exposure, Apr 13 — delivered Apr 14)
- Convergence bump to 57/60 should be propagated to PROME next spawn

---

## 2026-04-13 — HY OAS COMPRESSION + NON-BANK SERVICER RESEARCH + KB ARCHITECTURE

### THESIS v2.2 (refinement, not version bump)
**Author:** CARL (script-driven data refresh + research drill-downs)
**Action:** Major data refresh + structural finding on non-bank mortgage servicer transmission pathway.

### KEY FINDINGS
- **HY OAS complacency gap widening.** Spreads collapsed 346→294bps in 10 days (ceasefire Apr 8 = -18bps single session, plus NFP headline beat). Now BELOW 300bps elevated threshold while student loan defaults hit 9.2M, CMBS MF DQ reached ATH 7.15%, existing home sales approached <4.0M RED. Market split: JPM AM/Marks bullish ("tight justified"), Goldman 45% recession/Cambridge/Wellington/UBS warning on complacency. CARL interpretation: structural demand (CLO/pension/ETF flows) + index survivorship bias masking fundamental deterioration. Late-2007 analog (HY 260bps June → 800+ Nov). KB-CARL-200.
- **Non-bank mortgage servicer stress accelerating.** PennyMac FHA DQ spiked 5.9→7.5% single quarter Q4 2025, advance expenses +14%. GAO-26-107436 (Feb 2026): 35% of 550+ non-banks have high debt, only 30% profitable in 2022-23 downturn. **Ginnie Mae has NO stagflation stress test** — our thesis environment is the untested scenario. loanDepot $107.5M net loss, pledging GNMA MSR income. Lakeview (18% DQ)/Freedom (15.5%) private black boxes. MFS UK collapse (Feb 2026, Barclays $669M loss) = warehouse contagion template. Ginnie advance obligation asymmetry (advance until FINAL resolution) converts FHA DQ pipeline to cumulative cash drain. KB-CARL-202, KB-CARL-203, KB-HMR-046 through 052.

### Infrastructure Built
- 7-script CARL monitoring suite operational (thresholds, gas_tracker, consumer_pulse, catalyst_countdown, housing_pulse, abs_monitor, boot)
- abs_monitor expanded 4→6 issuers (added Exeter, Ally, GMF/AmeriCredit). 17 trusts tracked. SoFi excluded (private/144A).
- KB Migration Chunk 1 DONE: 44 housing entries delegated CARL → HOMER. HOMER KB 35→52 entries. Cross-domain claims retained in CARL.

### Cross-Agent Signal
- **CARL → REGINALD outbox:** Non-bank servicer warehouse line exposure. Request: check WAL/FHN/TCBI warehouse exposures, JPM Q1 warehouse commentary. Delivered Apr 14.

### KB Added (Apr 13: 5 entries)
KB-CARL-200 (HY OAS compression), KB-CARL-201 (CPI Energy +12.5%), KB-CARL-202 (non-bank transmission), KB-CARL-203 (Ginnie Mae no stagflation test), plus 7 HOMER entries on non-bank servicer research.

---

## 2026-04-09 — POP DEEP DIVE: INVISIBLE INCOME + BANK PIPELINE + NEW CONVERGENCE VECTOR

### CONVERGENCE MATRIX Updated
**Author:** CARL (via POP deep dive synthesis)
**Action:** New vector #11 added. Matrix expanded from 10 vectors (50pt) to 11 vectors (55pt). Score 47/50 → 51/55.

| Vector | Change | Reason |
|--------|--------|--------|
| #11 SB Bankruptcy + Owner Income | **NEW** 🔴 4/5 | POP deep dive confirmed: (1) Subchapter V +67% YoY BREACHED, Ch.11 +37%. (2) Owner income destruction refined to $73-145B annually ($83-165B tariff-adjusted) across two channels: active salary cuts (BofA 32%) + chronic income suppression. (3) SBA 7(a) defaults 3.7% (12-yr high). (4) 59% personal guarantees → business failure converts to consumer credit event. This is an explicit vector that was previously implicit in employment rot. Now measurable with leading indicators. |

### PREDICTIONS Added
| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-15 | **NEW** 65% | SBA 7(a) defaults exceed 6.5% by EOY 2026. Currently 3.7%, consensus 6.5-7.5%. Tariff acceleration + EIDL burden + elevated rates. |
| CRL-16 | **NEW** 60% | Regional bank Q2 2026 earnings show SB provision increases >25% YoY. Default lag model: tariff stress → charge-off = 9-12mo. Q2 = first window. |
| CRL-17 | **NEW** 55% | SB owner income destruction exceeds $100B annualized by Q3 2026 (tariff-adjusted). Wide confidence range — no survey measures cut magnitude. |

### KB Added (8 entries: KB-CARL-166 through KB-CARL-173)
Key entries: Owner income destruction refined estimate (166), CFPB primary earner data (167), S-corp distribution gap (168), SBA defaults (169), tariff importer burden (170), SubV +67% (171), regionals $600B SB loans (172), OZK NCO 1.18% (173).

### VX Added (2 vectors at CARL level)
- VX-CARL-POP-01: SB Owner Income Destruction — RED ($73-145B annually, invisible to BLS/payroll)
- VX-CARL-POP-02: SB Bankruptcy Pipeline — RED (SubV +67% BREACHED, SBA defaults 12-yr high)

### FLOW Added (2 cascades at CARL level)
- FLOW-CARL-11.01: Tariff → SB margin → owner comp → consumer spending (ACTIVE-RED)
- FLOW-CARL-11.02: SB stress → regional bank SB loan losses (WARMING-ORANGE, Q2-Q3 visibility)

### Source Documents
- POP/domain/sources/INVISIBLE_INCOME_DEEP_DIVE.md (610 lines, 32 sources)
- POP/domain/sources/SB_BANK_PIPELINE_DEEP_DIVE.md (338 lines, 46 sources)

---

## 2026-04-06 — STUE FIRST SPAWN: CASCADE AMPLIFIER FINDING + CRL-05 UPGRADE

### PREDICTIONS Updated
**Author:** CARL (via STUE analysis)
**Action:** CRL-05 confidence upgraded 72% → 82%. Two new predictions added (CRL-13, CRL-14).

| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-05 | 72% → **82%** | CC 90+ DQ GFC breach. STUE cascade analysis: student loan credit score destruction (-87 to -171 pts, NY Fed data) cascades into CC DQ. 10-12M borrowers face score damage → 3-5M cascade into CC 30+ DQ → est. +0.5-1.0pp to CC 90+ rate. This is an ADDITIONAL pathway to GFC breach beyond cost squeeze. Two independent mechanisms now identified: (1) multi-vector cost squeeze, (2) student loan credit score cascade. |
| CRL-13 | **NEW** 70% | SAVE non-selection rate >35%. Based on Oct 2023 precedent + MOHELA failures. 2.6M+ face $0→$407/mo payment cliff. |
| CRL-14 | **NEW** 65% | MOHELA-caused additional defaults >500K from July 1 transition. Servicer operational capacity near-zero for clean transition. |

**Key analytical finding:** Student loan vector is a **cascade amplifier**, not just a standalone 5/5 convergence score. It raises the effective impact of CC (Vector 1), subprime auto (Vector 2), K-shape convergence (Vector 9), and foreclosure acceleration (Vector 10) through the credit score destruction channel.

### STUE STATUS.md Updated
**Action:** Comprehensive refresh with Spawn 1 data pulls.
- SAVE: "ending" → **"REPEALED BY LAW"** (Working Families Tax Cuts Act)
- Added: ED final guidance Mar 31, Tiered Standard Plan option, 8.8M forbearance (6.5M SAVE), Exhibit C deadline MISSED (auto full relief), 25% of all borrowers DQ (3x pre-pandemic), 1,800+ colleges flagged, payment shock quantified ($0→$407/mo), spending destruction ($1.5-2B/mo), non-selection rate estimate (30-45%), Senate opposition to Treasury transfer
- Upgraded status: 🔴 → 🔴🔴 CRITICAL

### New KB Entries
KB-CARL-155 through KB-CARL-157 (HH spending-income scissors, BofA spending-by-income tier, Minneapolis Fed K-shape publication).

### Data Pruning
- KB-CARL-029: ACTIVE → SUPERSEDED (by KB-145)
- ML-CARL-SL-01: ACTIVE → SUPERSEDED (by KB-145, STUE owns detail)
- ML-CARL-SL-02: ACTIVE → SUPERSEDED (Ninth Circuit resolved, KB-149)
- VX-CARL-1.06: RED → CONSOLIDATED (into SL-01 through SL-07)
- VX-CARL-SL-03: "ENDING" → "REPEALED BY LAW"

**Old view:** Student loan at 5/5 max, standalone vector. SAVE "ending" Jul 1.
**New view:** Student loan at 5/5 AND cascade amplifier for Vectors 1/2/9/10. SAVE REPEALED BY LAW. CC GFC breach pathway now dual-mechanism (cost squeeze + credit score cascade). CRL-05 is the upgraded conviction call.

---

## 2026-04-04 — STUDENT LOAN VECTOR REFRESH: 4→5, STUE ACTIVATED

### THESIS Updated (minor, no version bump — convergence upgrade)
**Author:** CARL
**Action:** Student loan convergence vector #4 upgraded 4→5 (max). Convergence score 46→47/50. STUE sub-agent created.

**What changed:**
1. **FSA Data Center (Dec 2025, Mar 13 release):** 7.7M borrowers in default on $180B. +2.5M since Sep 2025. Active repayment 31+ DQ rate: 18.6% by dollar (vs 12.7% Dec 2019 — 46% worse). <40% of borrowers in repayment.
2. **~25% DQ rate:** Protect Borrowers/TCF analysis — 25% of borrowers with payment due are behind. 7.9M entered delinquency in first 3Q 2025. Projection: 13M in default by EOY 2026.
3. **SAVE ending Jul 1:** Settlement with Missouri. 7.5M borrowers get 90 days to select new plan. Non-selectors → 10-year standard plan (payment shock). RAP launches Jul 1.
4. **MOHELA failures:** 2.5M missed bills → 800K manufactured delinquencies. Wait times 7-50x peers. ~2M credit report errors. $7.2M DOE penalty.
5. **Treasury transfer (Mar 19):** Phase 1 — 9M defaulted borrowers to Treasury. Legal authority disputed.
6. **Sweet v. McMahon:** 205K automatic discharges (Ninth Circuit rejected DOE delay Mar 25). Minor positive, drop in bucket.

**Old view:** Student loan 90+ DQ at 9.6%, trending toward 10%. Vector score 4/5. SAVE enjoined, forbearance holding. Passive monitoring.
**New view:** Mass default event actively executing. 7.7M in default, 25% DQ, servicer failures amplifying, SAVE ending forces 7.5M into repayment Jul 1, Treasury transfer creating chaos. Vector score 5/5 (max). STUE sub-agent activated for dedicated tracking.

### PREDICTIONS Updated
| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-04 | 88% → **95%** | Student 90+ DQ >10%. FSA confirms 7.7M default, ~25% DQ, 18-29 cohort at 21%. SAVE ending Jul 1. Near-certain on next NY Fed release. |

### New KB Entries
KB-CARL-145 through KB-CARL-151 (7 entries covering FSA update, DQ rate, SAVE settlement, Treasury transfer, Sweet v. McMahon, MOHELA failures, demographic concentration).

### New VX Entries
VX-CARL-SL-05 (Borrowers in Default), VX-CARL-SL-06 (Treasury Transfer), VX-CARL-SL-07 (Servicer Failure). Existing SL-01 through SL-04 upgraded ORANGE→RED.

---

## 2026-04-03 — NFP MARCH: HEADLINE MASKS STRUCTURAL ROT

### PREDICTIONS Updated
**Author:** CARL
**Action:** Confidence adjustments on 3 predictions after NFP Mar +178K headline beat.

| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-05 | 75% → **72%** | CC 90+ DQ GFC breach. Headline beat removes single-month employment catalyst, but Feb revised to -133K, LFPR 61.9%, real wages near zero. Multi-vector cost squeeze now primary driver, not employment break. |
| CRL-09 | 75% → **73%** | JOLTS Mar <0.88. NFP +178K could imply some hiring channels reopened (healthcare, construction), but Kaiser return is one-time and LFPR collapse means denominator may shrink. |
| CRL-11 | 85% → **83%** | Hires rate ≤3.2%. NFP establishment survey shows hiring in healthcare/construction/transport, but Kaiser is one-time. LFPR collapse suggests discouraged workers exiting, not broad hiring. |

**Old view:** NFP -92K (Feb) was the employment catalyst accelerating consumer stress conversion.
**New view:** NFP Mar +178K headline removes acute employment break narrative but internals (LFPR 61.9%, Feb revised -133K, wages 3.5% YoY) confirm structural rot. Mechanism unchanged — cost squeeze is primary, not employment detonator. Timeline: no change to Q2-Q3 stress window.

**No THESIS version bump.** Thesis structure unchanged. Evidence base shifts slightly (employment less acute, but structural rot deepens). All load-bearing vectors intact.

---

## 2026-04-03 — FILE STRUCTURE REORGANIZATION

### THESIS.md Restructured
**Author:** CARL + Will
**Action:** Moved THESIS.md to thesis/ directory. Extracted Composition Shift narrative to this CHANGELOG. Convergence matrix marked as canonical (STATUS.md mirrors). PREDICTIONS.tsv moved from workbook/ to thesis/.

---

## 2026-03-31 — v2.1: JOLTS INVERSION + GAS $4 + TRIPLE NITROGEN SEIZURE

### THESIS Updated: v2.0 → v2.1
**Author:** CARL
**Action:** Minor version bump. Three vectors converging simultaneously confirmed.

**What changed:**
1. **JOLTS Feb: 0.91 (deepening).** Ratio dropped from 0.94 (Jan) to 0.91 in one month. Hires rate 3.1% = COVID-low. Quits rate 1.9% (8-month streak — workers trapped). Feb data PREDATES Iran — March will be worse.
2. **Gas $4.02 behavioral breakpoint FIRED.** Up $1.04 in 33 days (+35%). SPR 172M barrel release failing — gas rose through the entire release. CNN behavioral confirmation of fuel-vs-food tradeoffs.
3. **USDA wheat acreage: LOWEST SINCE 1919.** Corn -3.45M acres. Farmers fleeing N-intensive crops. Triple nitrogen seizure confirmed (Gulf + China + Russia). Food CPI loading for Q3-Q4.
4. **Convergence score upgraded:** UI exhaustion 4→5 (duration +2.0wk single month), gas confirmed at max. Total: 44→46/50.

**Old view (v2.0):** Multi-vector cost squeeze replacing employment detonator. Gas approaching $4, JOLTS newly inverted, food CPI possible but unconfirmed.
**New view (v2.1):** Three independent vectors SIMULTANEOUSLY confirmed/firing. Gas $4 breached. JOLTS deepening. USDA locks in food CPI. No longer prospective — executing. Q3 = consumption stress quarter.

### PREDICTIONS Added
- CRL-09: JOLTS Mar ratio <0.88 (75% conf)
- CRL-10: Food CPI YoY >4.0% (70% conf, Q4 2026)
- CRL-11: Hires rate ≤3.2% through Q2 (85% conf)

---

## 2026-03-27 — INSURANCE RELIEF COUNTER-SIGNAL

### THESIS Updated (minor, no version bump)
**Author:** CARL
**Action:** Added insurance relief as counter-evidence.

**What changed:**
- Auto insurance CPI collapsed from 20-30% to 5.9% YoY (BLS Feb 2026)
- Homeowners insurance decelerating: national +8.5%, FL +18%, down from 50% (Insurify 2025)
- Two cost-squeeze vectors easing

**Assessment:** Partially offsets thesis but outweighed by energy, food, and UI exhaustion vectors intensifying. No score change. Logged in counter-evidence section.

---

## 2026-03-10 — v2.0: MECHANISM SHIFT (MAJOR)

### THESIS Updated: v1.0 → v2.0
**Author:** CARL
**Action:** Major version bump. Thesis mechanism fundamentally changed.

**Old view (v1.0, Feb 2026):** Employment cracks → subprime auto/CC DQ spikes → bank NCOs → systemic repricing. Linear, fast, employment-first. Single-point-of-failure model.

**New view (v2.0, Mar 2026):** Multiple cost vectors (energy + food + insurance + HOA) simultaneously compress the bottom 60% while housing prices decline nationally. Employment is a slow grind, not a detonator. K-shape converging downward (top 40% now pulling back). Conversion through COST SQUEEZE + UI EXHAUSTION rather than mass layoffs.

**Why the mechanism changed:** v1.0 assumed employment breaks → credit collapses → banks eat losses. Reality is a multi-point-of-pressure system. We expected an earthquake; we got subsidence — the ground is sinking everywhere, slowly, from multiple causes. The destination (consumer credit crisis → bank losses) is the same; the path is different.

**Implications:**
- **Timing:** Slower than v1.0. Q2-Q3 stress, grinding not step-function.
- **Trades:** Longer duration needed. Roll timelines, don't trim positions.
- **Convergence score:** Established 10-vector matrix to track multi-source pressure.

### PREDICTIONS Established
- CRL-01 through CRL-08 created (initial prediction set)

---

## 2026-02-23 — v1.0: THESIS ESTABLISHED

### THESIS Created: v1.0
**Author:** CARL
**Action:** Initial thesis — "Beneath the Ice"

**Core claim:** 60% of American households are structurally fragile. Employment crack is the detonator. Subprime auto and CC delinquencies are the first visible signals. Bank NCOs follow.

**Initial predictions:** CRL-01 (gas peak stress), CRL-02 (subprime auto 60+ DQ >7.0%)

---

*This document is the audit trail for thesis evolution. Log every change with what/why/old→new. Read when assessing conviction or reviewing prediction calibration.*
