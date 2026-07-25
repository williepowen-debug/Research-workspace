# OTTO Thesis CHANGELOG

Audit trail of **thesis/POV pivots** — every material change in OTTO's view, logged
old → new with a date and trigger. This is the trajectory record that STATUS-narrative
pruning would otherwise destroy (per auto-memory `[[finding_pov_changelog_pattern]]`).

**Scope:** analytical/thesis changes only — conviction shifts, mechanism reframes,
prediction-confidence moves of note, new transmission rows, case-status escalations.
NOT routine dashboard refreshes (those live in STATUS) and NOT structural doc/folder
changes (those live in `MAINTENANCE.md`).

**Versioning:** OTTO's canonical thesis is `thesis/THESIS.md` (v1.1 as of 2026-07-04);
`STATUS.md` § THESIS is a live-state mirror. Entries here are dated and may cite the
thesis version they moved. *(Preamble corrected 2026-07-25 — it had described the
pre-Jun-9 layout, in which neither `thesis/THESIS.md` nor `MAINTENANCE.md` existed.)*

**Format:** reverse-chronological. Each entry: `### YYYY-MM-DD — headline`, then
**Was → Is**, then **Trigger** (what evidence forced it), then **Touches** (which
docs/predictions moved).

---

### 2026-07-25 (session 016, Will-directed) — Summer re-deterioration CONFIRMED on an instrument OTTO built itself; the "deep bleeds, broad is fine" framing weakens

**Was → Is:** the summer re-deterioration in subprime auto credit was OTTO's **expectation, untested**. Fitch's obtainable data stopped at **March 2026** (a seasonal tax-refund low), so every read since has been "unobserved, not disconfirmed" — a phrase this session used repeatedly and correctly. **Is: observed and confirmed.**

**Trigger:** Will asked whether the Fitch gap could be fixed. S&P and KBRA were tested and found closed (403 / paid). So OTTO built a **fixed panel of 7 named deals** parsed from SEC 10-D Exhibit 99.1 — the same primary documents the rating agencies aggregate.

**The result, from the first real run:**

| | trough → latest 60+ DQ | off trough |
|---|---|---|
| EART 2022-2 (DEEP) | 13.23 → **14.79%** | +1.56pp |
| EART 2022-3 (DEEP) | 12.27 → **13.59%** | +1.32pp |
| EART 2023-1 (DEEP) | 10.71 → **11.97%** | +1.26pp |
| EART 2024-1 (DEEP) | 9.37 → **10.26%** | +0.89pp |
| SDART 2022-6 (BROAD) | 8.88 → **10.45%** | +1.57pp |
| SDART 2023-1 (BROAD) | 8.62 → **9.96%** | +1.34pp |
| SDART 2024-1 (BROAD) | 7.78 → **9.19%** | +1.41pp |

**7 of 7 deals, both tiers, four vintages — troughed in spring, risen every month since, all now above their first observation.**

**The thesis-level wrinkle, and it cuts against OTTO.** Since s015 OTTO has framed the subprime picture as *deep-subprime bleeds while broad subprime holds up* — supported by Ally's five straight improving quarters and the 2.3× CNL tier split. The panel confirms the **level** gap (ANL 18.85% DEEP vs 6.41% BROAD, ~2.9×) but shows the **broad tier deteriorating as fast as or faster than deep off the trough** (+1.34 to +1.57pp vs +0.89 to +1.56pp). Level bifurcation is intact; **rate-of-change bifurcation is not.** That is a genuine qualification of OTTO's own framing and should temper any "it's contained to deep subprime" read.

**Second-order:** the DQ gap between tiers (1.3×) is far narrower than the loss gap (2.9×) — deep subprime converts delinquency into loss much faster, consistent with recoveries of 21.8-30.9% and falling on the 2022 vintages (EART 2022-3: 28.89 → 21.83% across Mar-Jun filings).

**Method note worth keeping:** the missing instrument turned out to be one parser away, inside documents OTTO was already reading for OTTO-04. The lesson generalises past this metric — **before accepting a data wall, check whether the primary documents already in hand contain the field.**

**Touches:** `scripts/panel_10d.py` + `workbook/PANEL_10D.tsv` (new), STATUS (3 new dashboard rows, boot-pointer, BOTTOM LINE), `workbook/ML.tsv` ML-201/-202/-203/-204, MAINTENANCE (instrument build + 4 parser defects).

---

### 2026-07-25 (session 016, Will-directed) — OTTO-04 metric re-based to the deep-subprime 10-D tranche; the prediction was RETIRED rather than re-scored

**Was → Is:** OTTO-04 ("2022 vintage CNL >25% by Sep 30") resolved on the **Fitch blended subprime index** — a convention Will ratified 2026-07-04 when the only known problem was composition bias. **Is:** the canonical 2022-vintage measure is now the **deep-subprime 10-D tranche** — `Cumulative net loss ratio` for **EART 2022-2 / 2022-3**, pulled directly from SEC EDGAR.

**Trigger:** new information since the July ratification — the blended index is not merely biased, it is **unobtainable**. OTTO has no Fitch-direct access; the Auto Remarketing/AFN free mirror has decayed to where its newest indexed piece still covers the *January* index. Latest usable data: **March 2026**. Two consecutive WINTERKORN runs failed to verify a release.

**The metric change is right, and it is not the interesting part.** The deep-subprime tranche is what the thesis actually cares about, it is primary-source, and it is retrievable on demand. Full series now on file `[CONF SEC 10-D]`: **EART 2022-3** 25.21 → 25.53 → 25.90 → 26.27 → 26.60 → 26.95 → 27.28 → **27.58%** across the Dec-2025 → Jun-2026 filings, monthly deltas **decelerating .37 → .30pp**; **EART 2022-2** 24.23 → **26.34%**, .33 → .26pp.

**The interesting part: the prediction could not follow the metric.** OTTO-04 was made **2026-02-23**. On the re-based measure, **EART 2022-3 was already at 25.90%** (10-D filed 2026-01-28) and 2022-2 crossed 25% within days (25.22%, filed 2026-03-03). **The re-based claim was true-at-creation — zero forecasting content.** Scoring it CONFIRMED would have converted a likely-miss into a hit; it is the OTTO-30 known-unknown trap running in reverse.

**Disposition:** OTTO-04 **RESOLVED EARLY (2026-07-25)** as **FALSIFIED-on-metric / CONFIRMED-on-substance** (the OTTO-29 convention Will ratified Jul 4), with **no calibration credit taken**. Resolving early is correct because both metrics now have determinate answers — nothing is learned by holding it to Sep 30. Forward replacement opened: **OTTO-34** — *EART 2022-3 CNL ≥29.0% on the 10-D filed December 2026*, 60%, deliberately near-coin-flip, instrument and parse-recipe named in-row.

**The rule this establishes, which generalises past OTTO:** *when you re-base an open prediction's metric, test whether the new metric was already satisfied at the original Made_Date. If it was, the prediction is not re-based — it is retired, and a fresh forward claim replaces it.* Recorded in `PREDICTIONS_ARCHIVE.md` § credit note.

**What is genuinely still open:** OTTO-04's substance was never in doubt after s015. What has never been tested is **where deep-subprime 2022 terminates** — a ~29-30% grind versus a ~28.5% plateau. That is what OTTO-34 measures, and the observed deceleration (.37 → .30pp/mo) is what makes it a real question.

**Touches:** `thesis/PREDICTIONS.tsv` (OTTO-04 resolved + OTTO-34 created), `thesis/PREDICTIONS_ARCHIVE.md` (scoreboard 5/7 → 6/8 + credit note + the transferable rule), STATUS (§ PREDICTIONS, dashboard CNL row re-based, timeline), `docket/CATALYSTS.tsv` (2026-09-01 decision row closed ~5 weeks early).

---

### 2026-07-25 (session 016, RP-OTT-1.6) — "The books looked clean" stops being an inference and becomes a documented mechanism

**Was → Is:** The Invisible Exit's central claim is that a fraud lender's book *looks clean until the moment it collapses*. Until now OTTO supported that with outcome evidence — 30K missing vehicles, ~3% recovery, a Vervent mod program — i.e. **inference from how it ended**. **Is:** the mechanism is now documented at the point of control. All **eleven** Tricolor securitizations (2018-2025) carry a third-party agreed-upon-procedures report, and those procedures compare the securitization data tape **to Tricolor's own servicing and origination systems** — the systems the superseding indictment alleges were falsified. *"We compared Characteristics 8. through 12. to … the Servicing System Screen Shots"* (Deloitte). **A tape derived from a doctored source agrees with it by construction.**

**Trigger:** `[CONF SEC EDGAR]` — all 11 Form ABS-15G filings + 12 Exhibit 99.x AUP reports, depositor CIK 0001757871. Commissioned by Will as Tier 1 of the 2018-2021 vintage thread.

**Why it's thesis-level:** it converts the Secondary thesis's weakest link — *why did nobody notice for seven years?* — from a plausibility argument into a structural one. An AUP is a **reconciliation, not an audit**; it is not designed to test whether the originator's records are true. Three major firms (Crowe → Deloitte → Grant Thornton) each produced accurate reports that were, against this fraud, uninformative. Double-pledging is likewise outside scope: lien documents are checked, but on **150 of ~10,000 loans (1.5%)**, and confirming Tricolor's own lien is not a search for competing pledges. **No procedure inspects a vehicle.**

**Also retires a lead — my own, from earlier the same session.** I had headlined "2018-2021 vintages implicated." Tricolor securitized **two** deals in that window (TAST 2018-2, 2021-1) with a **32-month gap**; **nine of eleven** are 2022-2025. The 2022-centric frame was right. Corrected in STATUS, CHANGELOG, and NEXUS_BRIEF — the last of which had already gone out with the wrong gloss.

**Reusable output:** a 144A subprime shelf's ABS-15G/Exhibit 99.1 is its one public trace. Four cheap diagnostics now defined — *what is the tape compared against; who chose the sample; how large relative to the pool; has the provider rotated* — applicable to CPS, Flagship, Lendbuzz, SAFCO, GCAR.

**Touches:** `research/outputs/RP-OTT-1.6_Tricolor_ABS15G_Diligence_Forensics.md` (new), `workbook/ML.tsv` ML-195/-196/-197/-198, STATUS (BOTTOM LINE + criminal-track vector + 2018-2021 correction), NEXUS_BRIEF (retraction + new mechanism line), RESEARCH_STATUS index. No prediction moved.

---

### 2026-07-25 (session 016) — 🔴 DOJ has criminally charged BOTH of OTTO's thesis mechanisms; Invisible Exit escalates from inference to indictment

**Was → Is:** The Primary (Cockroach/double-pledging) thesis rested on bankruptcy-estate evidence and the Dec-2025 indictment's *bank-fraud* framing. The Secondary (Invisible Exit) thesis — that the immigrant subprime cohort skip-defaults in a way that **bypasses the 30→60→90 DQ chain**, which is why fraud-lender books look clean until collapse — was OTTO's own **inference from data**, explicitly the weaker leg (MEDIUM-HIGH, "structurally validated" only by the Tricolor 30K-missing-vehicles / Vervent Fresh Start evidence).

**Is:** a **superseding 8-count indictment** unsealed **2026-06-24** against founder Daniel Chu charges, as criminal conduct, that Tricolor executives *"manipulated delinquent loan data to make non-performing loans appear current"* **and** *"pledged the same collateral to multiple lenders simultaneously"*, plus fictitious payment records and falsified borrowing-base reports. **Both legs of OTTO's thesis are now federal criminal allegations, not OTTO inferences.**

**Trigger:** `[CONF DOJ/SDNY via Reuters, Bloomberg, NatLawReview, Barnes & Thornburg]` — surfaced 2026-07-25 during the 21-day catch-up sweep. **It happened Jun 24, ten days before OTTO's Jul 4 session, and was missed then too.**

**Three escalations, in order of importance:**
1. **The Invisible Exit mechanism is charged.** "Making non-performing loans appear current" is precisely the DQ-chain bypass OTTO modelled. This is the strongest available validation short of conviction, and it should move the Secondary thesis's conviction up — it is no longer OTTO's private read of anomalous data.
2. **"Continuing financial crimes enterprise from at least 2018."** The alleged fraud ran **seven years** before collapse, so **originations** were tainted from 2018. ~~The indictment implicates 2018-2021 vintages, widening the impaired-collateral window materially.~~ **⚠ CORRECTED same day by RP-OTT-1.6:** that was overstated. Tricolor securitized only **two** deals in 2018-2021 (TAST 2018-2, 2021-1, with a 32-month gap); **nine of eleven** deals are 2022-2025. The securitized-collateral window did **not** widen materially, and the phrasing could have been read as *industry-wide* 2018-2021 vintage impairment, which does not follow from the indictment at all. **Lead retired; the wording was the error, not the indictment.**
3. **The statute is the tell on DOJ's own conviction.** DOJ invoked **18 U.S.C. § 225 (CFCE, the "financial kingpin" statute)** — mandatory minimum **10 years to life**, used a handful of times since the S&L crisis and not at all in over a decade. Prosecutors do not revive a dormant mandatory-minimum statute for a marginal case. Charges roughly doubled vs. the December original. Chu pleaded **not guilty 2026-06-30**.

**Fourth, separately dated:** former COO **David Goodgame pleaded GUILTY 2026-06-24** to six counts (bank/wire/securities fraud, conspiracy, false statements) and is **cooperating** against Chu — a flip from his Jan-2026 not-guilty plea. **This fires OTTO's standing outbound trigger** ("cooperating witness reveals new fraud/participants" → CARL, REGINALD, 🟠 ELEVATED). A cooperating COO is the highest-value fraud-surface-expansion vector available; expect new counterparties to surface through his proffer.

**Calibration note — this is a coverage failure, not a lucky find.** Four Tricolor criminal-track developments (Jun 24 superseding indictment, Jun 24 Goodgame plea, Jun 30 arraignment, Jul 7 trial re-date) all landed in a window OTTO was nominally awake for on Jul 4, and none were caught. The Jul 4 session swept *bankruptcy* dockets and *ABS* data but did not sweep the **criminal** track — which WINTERKORN's spec explicitly scopes as "selective: trial date + cooperator motions only." That scoping was too narrow: it treated the criminal case as a date-keeping problem when it is a *fraud-surface-discovery* channel.

**Touches:** STATUS (THESIS mirror, dashboard, ACTIVE VECTORS, CRITICAL TIMELINE), `workbook/ML.tsv` ML-191/-192/-193/-194, `thesis/THESIS.md` (conviction on Secondary — **owed, see LAST_COMPLETION gaps**), WINTERKORN spec scope (**owed**), cross-agent trigger to CARL/REGINALD.

---

### 2026-07-25 (session 016) — Double-pledge mechanic confirmed in a THIRD collateral class (floorplan/inventory)

**Was → Is:** OTTO tracked Tricolor's double-pledging across two collateral layers — the ABS warehouse (29,000 double-pledged loans) and the receivables layer ($113M disputed-ownership escrow). **Is:** a third layer is now primary-sourced — **floorplan/vehicle inventory**. TBK Bank (Triumph Financial) is agent on a $60.5M Tricolor floorplan facility holding ~$22.5M on a claimed *first-priority* interest in vehicle inventory, while its own 10-Q concedes "other creditors have asserted that they have interests in some of the collateral."

**Trigger:** `[CONF SEC 10-Q, TFIN CIK 0001539638, filed 2026-07-21]`, found via complete EDGAR full-text scan.

**Why it's thesis-level, not a dashboard row:** the Cockroach thesis claims fraud, once found, is broader than first disclosed. Each additional *collateral class* touched by the same mechanic is independent confirmation that Tricolor's double-pledging was systemic to the business model rather than confined to the securitization channel. It also opens a new discovery surface: **~$38M of the syndicate is held by unnamed participants.**

**Second-order:** TBK carries the $22.5M **unreserved** 9.5 months post-Ch.7 on an "adequately secures" assertion, against inventory where OTTO's own data shows ~30,000 vehicles missing and ~3% realized recovery. Loss-recognition lag is itself now a tracked mechanic (same shape as the $113M escrow: *banks cannot book losses cleanly even when substance is clear*).

**Touches:** STATUS (new ACTIVE VECTOR + 3 dashboard rows + timeline), `workbook/ML.tsv` ML-184, NEXUS_BRIEF (new REGINALD send-row), WALTER signal `SIG-OTTO-WALTER-20260725-tricolor-floorplan-tfin`. No prediction moved — this is new surface, not a resolution.

---

### 2026-07-25 (session 016) — Two predictions downgraded hard on primary evidence; the failure mode is measure-design, not luck

**Was → Is:** OTTO-30 **45% → 12%**; OTTO-31 **30% → 12%**.

**Trigger — OTTO-30:** a *complete* EDGAR full-text scan (all operating-company forms mentioning "Tricolor", 2026-04-15 → 07-25) returned **zero new US bank names**. Every in-window filer disclosed before the window opened. **Trigger — OTTO-31:** MTB Q2 (Jul 15) posted record EPS $5.32 vs $4.66 est with no wind-down language and active promotion of Wilmington's custody franchise — a second corporate-side disconfirmation.

**The pattern worth naming.** With OTTO-26 (right direction, wrong date), OTTO-29 (confirmed-on-substance, falsified-on-window), OTTO-04 (deep-subprime substance confirmed, blended-index metric may miss) and now OTTO-30, **four of OTTO's claims have failed or are failing on how the claim was *measured* rather than on whether the world moved as expected.** OTTO-30 is the cleanest case: it asked "does a 6th bank *disclose*" — but a bank that disclosed in Sept 2025 and was never *found* is indistinguishable, from OTTO's side, from one that never disclosed. The prediction measured OTTO's own discovery latency, not the world. **Both times OTTO's named-bank list was found incomplete (OBK, now TFIN), the cause was press-sampling rather than complete scan.**

**Corrective adopted:** discovery-type claims must specify the *instrument* (complete EDGAR FTS, not press monitoring) and a pre-registered re-check. OTTO-30 now carries one: re-run the identical query 2026-08-15; still zero → FALSIFIED.

**Touches:** `thesis/PREDICTIONS.tsv` (OTTO-30/-31 confidence + notes), STATUS § PREDICTIONS, MEMORY (finding), auto-memory candidate.

---

### 2026-07-25 (session 016) — OTTO-32 resolution mechanics reframed (confidence held at 85%)

**Was → Is:** Jul 28 was carried as a same-day resolver ("plan confirmed = OTTO-32 CONFIRMED early"). **Is:** Jul 28 is the **opening of a multiday contested confirmation trial** — creditors sought further production on the litigation claims at the plan's core, the court is weighing privilege issues pre-trial, and every plan revision has drawn "a wall of objections" including the UST `[PRESS Law360/Octus/TT]`.

**Trigger:** T-3 pre-hearing verification pass.

**Why it matters even though confidence didn't move:** the *substance* (111/112 debtors → Ch.7) is unchanged and the Sep 30 window stays comfortable — but anything scoring OTTO-32 off a Jul 28 headline would misread a process readout as a verdict. **Catalyst-date ≠ resolution-date** (auto-memory `[[finding_catalyst_vs_consequence_conflation]]`).

**Also newly surfaced:** debtor suits vs Patrick James + Onset Financial seek **>$2.7B** and are **stayed** pending the criminal case; Lopez ordered a criminal-proceedings status update by **Jul 13** — a dated node that was never on OTTO's docket.

**Touches:** `thesis/PREDICTIONS.tsv` OTTO-32 notes, STATUS (§ PREDICTIONS, CRITICAL TIMELINE, BOTTOM LINE), `docket/CATALYSTS.tsv`.

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
