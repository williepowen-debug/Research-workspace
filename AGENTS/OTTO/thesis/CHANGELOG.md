# OTTO Thesis CHANGELOG

Audit trail of **thesis/POV pivots** — every material change in OTTO's view, logged
old → new with a date and trigger. This is the trajectory record that STATUS-narrative
pruning would otherwise destroy (per auto-memory `[[finding_pov_changelog_pattern]]`).

**Scope:** analytical/thesis changes only — conviction shifts, mechanism reframes,
prediction-confidence moves of note, new transmission rows, case-status escalations.
NOT routine dashboard refreshes (those live in STATUS) and NOT structural doc/folder
changes (no separate MAINTENANCE log yet — candidate if structural churn grows).

**Versioning:** OTTO's live thesis currently lives in `STATUS.md` (§ THESIS), not a
versioned `thesis/THESIS.md`. Until that graduates, this log is dated-entry only — no
version tags. When/if the thesis moves to its own folder, this file moves with it.

**Format:** reverse-chronological. Each entry: `### YYYY-MM-DD — headline`, then
**Was → Is**, then **Trigger** (what evidence forced it), then **Touches** (which
docs/predictions moved).

---

### 2026-07-04 (session 015) — 2022-vintage CNL is bifurcated by tier; OTTO-04's blended-index metric decoupled from the substance
- **Was:** OTTO-04 ("2022 vintage CNL >25% by Sep 30") tracked as a single blended Fitch subprime-index number (22.42%@31mo) "in striking distance" of 25% (68% after the spring seasonal nudge). The 2022-vintage *magnitude* question and the *index-metric* question were treated as one.
- **Is:** Primary-source 10-D pull `[CONF SEC 10-D]` shows the "2022 vintage" is bifurcated **~2.3x by credit tier** at identical ~44-48mo seasoning — DEEP subprime (Exeter EART 2022-3 **27.58%** / 2022-2 26.34%) is already well past 25% and grinding to ~28-29% terminal, while BROAD subprime (Santander SDART 2022-6 **12.08%**) is nowhere near. The Fitch blended index is a composition-weighted average between, anchored DOWN by Santander's dominant $2B+ low-CNL deals. **So the thesis-relevant SUBSTANCE (deep-subprime 2022 impairment) is CONFIRMED >25% by primary source, but the blended-index METRIC OTTO-04 resolves on may NOT cross 25%** — a metric-falsification would not be a substance-falsification (same shape as OTTO-29/-26 falsified-on-window / confirmed-on-substance). Both tiers are DECELERATING into summer with no post-tax-season re-acceleration in the May-collection prints; the Fitch "May print" carries only March data (2mo lag), so the index hasn't turned either. OTTO-04 nudged **68→62%** on the composition drag.
- **Trigger:** session-015 primary-source EDGAR 10-D pull (EART 2022-2/-3, SDART 2022-6, May-2026 collection filed Jun-2026) + Fitch print sourcing (AutoRemarketing May 21 2026 = March data). Closed the standing "EDGAR 10-D blocked" tooling gap (403 = missing User-Agent header).
- **Touches:** OTTO-04 68→62% (PREDICTIONS.tsv + STATUS dashboard & predictions rows); STATUS 2022-CNL row rebuilt by-tier + Fitch DQ/ANL/recovery rows re-stamped with data-month; ML-182/-183. Applies auto-memory `[[finding_blended_index_masks_bifurcation]]` + `[[finding_decouple_idiosyncratic_from_systemic_leg]]` + `[[finding_measure_actionable_not_gross_rate]]`. **Resolved (Will-ratified Jul 4):** OTTO-04's canonical measure STAYS the blended index; a Sep-30 miss resolves falsified-on-window / confirmed-on-substance (deep-subprime tranche already >25% — OTTO-29 convention). Convention recorded in PREDICTIONS.tsv OTTO-04 Notes.

### 2026-07-04 — Systemic subprime-ABS funding-freeze sub-thread DISCONFIRMED (OTTO-05 falsified)
- **Was:** OTTO carried a systemic funding-stress leg alongside the fraud-pattern leg — the expectation that subprime auto ABS spreads keep widening (OTTO-05: BBB >250bps by Jun 30), with dealer reluctance to print below-IG framed as a market-freezing signal. Composite severity ran 🔴🔴.
- **Is:** The funding-freeze sub-thread is **disconfirmed.** Subprime BBB ABS spreads **TIGHTENED to +140bps** (EART 2026-3, settled ~Jun 24) from +190 in Mar; the deal **upsized to $1.2bn** and Exeter earned its **first-ever AAA** — a market that is open, deep, and repricing tighter, not freezing. Ally (near-prime) credit is *improving* (NCO/DQ down YoY, 4 straight quarters). **The fraud-pattern leg (Tricolor recovery ~3%, First Brands → majority Ch.7) is intact and idiosyncratic; it is NOT transmitting into a broad subprime-ABS repricing.** Composite downgraded 🔴🔴 → 🔴 fraud-leg / 🟠 systemic-funding-leg. The two legs must be kept distinct: cockroach fraud-discovery ≠ systemic funding stress.
- **Trigger:** Jul 4 catch-up sweep of the Jun 30 prediction resolve — EART 2026-3 direct primary print (+140bps BBB) `[CONF SEC FWP/IFR]`; Ally Q1 credit metrics + Jul 21 earnings timing.
- **Touches:** OTTO-05 FALSIFIED; OTTO-28 FALSIFIED-on-window; OTTO-04 nudged 75→68% (seasonal); STATUS signal-status 🔴🔴→🔴/🟠 + dashboard ABS rows; ML-177/-179. **Follow-up ✅ DONE (Jul 4, THESIS v1.1):** updated `thesis/THESIS.md` — conviction-decomposition (Magnitude leg split into idiosyncratic-fraud-recovery HIGH vs systemic-funding LOW) + transmission chain (stage 3/7 + critical observation) + why-now driver 2 (reversed) + risk matrix + break condition + calibration scoreboard. Fraud-pattern predictions (OTTO-01/-29/-32) unchanged in substance.

### 2026-06-09 — Carvana carved out as separate-conviction sub-thesis (v1.0 THESIS introduction)
- **Was:** Carvana bundled in the Primary Cockroach case table at equal weight to the 4 confirmed cases (Tricolor / First Brands / MFS / PrimaLend). STATUS § THESIS showed all 5 rows in one table; conviction implied uniform on the pattern.
- **Is:** Carvana is a **separate sub-thesis with explicit LOWER conviction.** Reasons: (a) allegation-only — no DOJ indictment, no SEC action, no auditor resignation; (b) GT ratified May 5 (disconfirms the "GT resigns" red-line trigger); (c) governance vote 96% against separation = thesis-confirming on related-party concern but not the Cockroach archetype; (d) insider signal mixed (CFO selling vs RSU withholding); (e) William Blair June conviction list = bull offset; (f) no short-seller activity Mar 15–Jun 8 (Gotham/Hindenburg/MW silent — mild evidence the thesis isn't ripening). **Cockroach case count is now 4 confirmed, not 5.** Carvana re-enters the Primary table only if Jun 12+ discovery surfaces specific manipulation evidence.
- **Trigger:** thesis/THESIS.md v1.0 introduction (Jun 9) forced the bundling question. Carving out is the substantive change; the folder consolidation is the structural one.
- **Touches:** thesis/THESIS.md v1.0 dedicated CARVANA SUB-THESIS section + decomposed-conviction footer ("Carvana sub-thesis: LOWER"); STATUS § THESIS reframed (4 confirmed + 1 alleged carve-out). No prediction-confidence move on the existing OTTO-NN rows.

### 2026-06-09 — Tricolor §341 resolution-slip past Sep 30: modeled-likely → concrete
- **Was:** OTTO-29 Tricolor distribution-plan resolution-slip past Sep 30 was *modeled likely-slip* (no plan filed May–Jun per STATUS).
- **Is:** **Concrete.** WINTERKORN inaugural pre-fire verification (Jun 9) caught a Verita-noticed §341 continuance to **Nov 11 2026**. The Jun 17 §341 meeting itself happens but is already noticed-continued; distribution-plan filing slips past the Sep 30 OTTO-29 resolve by docket-confirmed action, not projection. Substance call unchanged (Tricolor recovery near-zero); only the resolution-window assertion firmed.
- **Trigger:** WINTERKORN sub-agent inaugural run (Jun 9, T-3 pre-hearing verification) caught it. The catch is exactly the value-prop the sub-agent was built to deliver (the canonical Jun 17→Jun 12 failure mode, made cadence-driven).
- **Touches:** STATUS CRITICAL TIMELINE (Jun 17 row reframed; new Nov 11 row added); CATALYSTS.tsv (Jun 17 Tricolor row date_class modeled→confirmed + Nov 11 row added); OTTO-29 substance sharpened (Notes-column refresh pending — date stays Sep 30).

### 2026-06-08 — ABS structural claim falsified + OTTO-05 recalibrated (data refresh)
- **Was:** Subprime ABS market "IG-only — BB/single-B tranches not clearing" (structural 🟠); BBB spread extrapolated ~200-235bps; OTTO-05 (BBB >250 by Jun 30) at 62%.
- **Is:** **Below-IG IS clearing** — Exeter EART 2026-2 placed BB- (+380) and single-B (+320) tranches publicly (Mar 20, SEC FWP). Direct BBB print **+190bps** (EART Class D) sits *below* the extrapolation. OTTO-05 dropped 62 → 48% (needs +60bps in 3wk absent a fresh catalyst). "IG-only" claim retired.
- **Trigger:** Jun 8 dashboard data-refresh sweep — primary-source SEC FWP for EART 2026-2 superseded OTTO's hand-extrapolated spread levels.
- **Touches:** OTTO-05 (62→48%); STATUS SIGNAL DASHBOARD (3 spread rows); issuance row 🟠→🟢-reframed. Calibration note: OTTO had been over-extrapolating BBB off A-rated + a too-wide BBB-over-A premium.

### 2026-06-08 — First Brands OTTO-32 resolver: Jun 17 → Jun 12
- **Was:** OTTO-32 (First Brands majority Ch.7) resolver = Jun 17 plan-confirmation hearing.
- **Is:** Operative resolver is the **Jun 12 UST convert-or-dismiss hearing** (10am CT, §1112(b)). May 20 DS denied (entanglement + <14d creditor review + admin-insolvency); Jun 17 confirmation is now *contingent on surviving Jun 12*. Conviction unchanged (85%) — only the resolver date/mechanism moved earlier.
- **Trigger:** Jun 8 catalyst-prep sweep (Law360 #2482099 / Octus) — surfaced the §1112(b) hearing OTTO's timeline had folded into "Jun 17."
- **Touches:** OTTO-32 Notes; STATUS CRITICAL TIMELINE + signal-trigger; CATALYSTS.tsv (new Jun 12 row, Jun 17 re-characterized).

### 2026-06-02 — First Brands Ch.7: IN MOTION → ADVANCING
- **Was:** Ch.7 conversion "in motion" (US-Trustee dismiss-or-convert motion filed May 13).
- **Is:** Mechanism **advancing** — 4 Evolution SPV debtors already converted (Apr 9 Lopez order); PMG plan routes all other 111 debtors to Ch.7; May 20 conditional-DS approval DENIED on admin-insolvency grounds (the denial basis = UST's outright-conversion argument, so it cuts *toward* thesis). Confirmation re-targeted Jun 17.
- **Trigger:** First Brands docket sweep (Jun 2) — Law360 / CreditSights cleared the auth-gated Kroll docket.
- **Touches:** OTTO-32 held 85%; STATUS CRITICAL TIMELINE; ML-OTTO-171.

### 2026-05-22 — Wilmington Trust: franchise-exit thesis collapses to narrow Tricolor resignation
- **Was:** 🔴🔴 "Wilmington exiting its entire non-mortgage ABS custodial business" (billions in ABS); OTTO-31 opened 60%.
- **Is:** 🟠 narrow — only the **Tricolor-specific** indenture-trustee resignation (Sep 20 2025) is corporate-confirmed. Full-exit allegation **denied corporate-side** (American Banker, M&T anon source: unit "is accepting new clients") + active-business evidence (#2 US ABS/MBS trustee 1H 2025). OTTO-31 dropped 60 → 30%.
- **Trigger:** May 22 PM corporate-side sweep. Plaintiff allegation = litigation rhetoric, not franchise exit.
- **Touches:** OTTO-31 (60→30%); STATUS active vectors (split into Wilmington-narrow + successor-vacuum rows); auto-memory `[[finding_refresh_not_retire_perentity_profiles]]`-adjacent calibration lesson (weight `[ALLEG]` ≤40%).

### 2026-05-21 — Tricolor recovery: deadline + magnitude corrected
- **Was:** Vehicle-sale deadline Apr 30 (per Apr 15 recalibration); recovery outcome open.
- **Is:** Operative deadline was **Mar 31** (no extension); auctions ran; ~3% recovery projected (5,857 vehicles / $39.5M net); **~30K vehicles missing, up to $1.1B** (Invisible Exit at industrial scale); $113M distribution gridlock = new transmission mechanic.
- **Trigger:** May 21 sourced docket + AFN auction-proceeds reporting superseded the Apr 15 recalibration.
- **Touches:** OTTO-29 raised to 80% (substance) but flagged resolution-at-risk; STATUS dashboard + thesis blocks; ML-OTTO-145 supersedes ML-OTTO-140.

### 2026-04-15 — Recovery-signal metric reframed: vehicle proceeds → ABS note price
- **Was:** "Recovery outcome" framed around vehicle auction proceeds ($125M cost-basis ceiling).
- **Is:** The signal-rich metric is **ABS note market price** (already <10¢ on the dollar = >90% implied noteholder loss), not vehicle proceeds. The question was mis-framed.
- **Trigger:** Apr 15 Tricolor recovery deep-dive; Will wanted the reframe said plainly before the data.
- **Touches:** Cockroach magnitude strengthened; Invisible Exit structurally validated.

---

*Seeded 2026-06-08 from STATUS/MEMORY trajectory at CHANGELOG introduction. Pre-2026-04 pivots not backfilled — reference STATUS archive + ML.tsv if needed.*
