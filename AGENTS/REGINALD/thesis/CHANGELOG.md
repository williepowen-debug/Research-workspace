# REGINALD CHANGELOG

Tracks all changes to THESIS.md and TIMELINE.md. Reverse chronological. Each entry documents what changed, why, and the old view vs new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new channel, thesis break, conviction reversal). Minor (Y) = refinement (updated probability, new evidence for existing view, threshold adjustment).
- TIMELINE: not versioned numerically — entries are dated. Events are marked RESOLVED with outcomes when they pass.

---

## 2026-04-16 — v1.4: C&I AS CONVERGENCE HIDING PLACE

### THESIS Updated → v1.4
**Author:** REGINALD + Will
**Action:** Added "C&I as Convergence Hiding Place" subsection to Section 2 (Architecture). Updated CFG row in Bank × Cluster table and Channel B bridge paragraph. Version bumped v1.3 → v1.4.

**What changed:**

**New framework — Three masking mechanisms within C&I (Section 2):**
The Q1 2026 earnings wave (MTB Apr 15, CFG Apr 16) revealed that C&I is not just where CRE hides — it's where ALL concentration risk hides. Three distinct mechanisms operate simultaneously:
1. **Memo Item 3** — CRE wearing C&I label (Cluster A risk, found at OZK/WAL/EGBN)
2. **NDFI opacity** — counterparty concentration invisible in aggregate C&I (Cluster B risk, found at CFG $12.5B / MTB $13.4B, zero counterparty disclosure at both)
3. **Reclassification** — growth velocity distorted by sub-category relabeling (CFG mgmt claims 5%/yr, 10-K shows 39.7% — 8x gap; MTB $1.3B C&I→NDFI recategorization)

Core insight: **the convergence isn't just eight channels hitting the same banks — it's eight channels hiding in the same bucket.** CRE ratio screens miss all three mechanisms. When Clusters A and B detonate together, losses emerge from the same C&I line item simultaneously with no prior warning from reported CRE metrics.

**CFG Bank × Cluster update:**
- Cluster A: 🟡 → 🟠 (CRE nonaccruals +10% QoQ, FHLB 60x YoY)
- Cluster D: 🟠 → 🟡 (consumer actually improving, NCO 38bps from 70bps YoY)
- Score: 9 → 12
- Van Saun first acknowledged screening counterparties for "liquidity gates"
- PE line utilization DOWN — partial disconfirmation of draw-spike thesis

**Old view:** Section 2 described three layers of hidden *CRE* (classification, NDFI wrapper, collateral fraud). The C&I bucket was understood as where CRE hides.
**New view:** Section 2 now shows C&I is where *all* concentration risk hides — CRE, fund finance, and counterparty exposure alike. The hiding place is shared, which means the detonation will be simultaneous.

**Evidence base:** CFG Q1 2026 earnings release + financial supplement + earnings call transcript (Apr 16). MTB Q1 2026 (Apr 15). FFIEC Call Report screens (Q4 2025).

**Why v1.4 not v2.0:** No new channels. No new targets. Same thesis structure. This is an analytical refinement — showing that the hiding mechanism (C&I) is shared across clusters, not just within Cluster A. The convergence thesis is strengthened, not changed.

---

## 2026-04-02 — TIMELINE: Branch Point Summary Table Added

### TIMELINE Updated
**Author:** REGINALD + Will
**Action:** Added Branch Point Summary table to TIMELINE.md. 13 events mapped with bull fork / bear fork / status tracking. Key sequence annotation added.

**What changed:**
- New section before POSITION CALENDAR: fork-tracking table for all major catalysts (Apr 10 CPI through Q2-Q3 2022 vintage maturities)
- 2 events marked RESOLVED (JEF Q1 = BULL, eSLR = divergence confirmed), 1 marked UNKNOWN (First Brands), 10 PENDING
- Key sequence formalized: OZK primes → second miss triggers sector repricing → Call Reports confirm → AOCI compounds
- Adopted SAM's branch point pattern for consistency across agents

**Old view:** Branch points described in narrative within each week's section — no summary view
**New view:** All forks visible in one table at bottom of TIMELINE, with status tracking and sequence annotation

**Note on THESIS:** No version bump — TIMELINE structural improvement, no thesis change.

---

## 2026-03-31 — v1.3: WHAT'S PRICED IN + PRUNING

### THESIS Updated → v1.3
**Author:** REGINALD + Will
**Action:** Added Section 6 "What's Priced In." Pruned redundancy across document (channel detail data → VX.tsv, target thesis numbers → bank files, Layer 1 table → KB, Section 4 Dual Failure merged into cluster framework, cross-agent table → CLAUDE.md pointer).

**What changed:**
- New Section 6 maps the gap between consensus view and our view per bank
- 8 blind spots identified: MI3, NDFI, fraud, SSFA, fund finance, AOCI compound, multi-cluster, DOGE structural
- Price gap table: OZK ~40-50% gap, WAL ~10-30%, CFG ~5-15% but widest sentiment gap
- Edge ranking: CFG (widest consensus-vs-reality gap), OZK (4 edges beyond Temple 8), WAL (fraud wildcard is uncorrelatable)
- Pruning: 546 → 494 lines despite adding 3 new analytical sections (interaction map, loss quant, what's priced in)
- Data points extracted to workbook/VX.tsv references throughout

**Key gap flagged:** OZK has no consensus EPS estimates in our files (Gap #10 in EARNINGS_PREP). This must close before Apr 16.

**Old view:** No systematic mapping of consensus vs our view
**New view:** Per-bank price gap quantified, blind spots catalogued, edge ranked

---

## 2026-03-31 — v1.2: LOSS QUANTIFICATION

### THESIS Updated → v1.2
**Author:** REGINALD + Will
**Action:** Added Section 5b "Loss Quantification — The Math" between target theses and timeline.

**What changed:**
- Built loss scenario tables for OZK and WAL using Layer 1-adjusted true CRE exposure
- Five scenarios: Mild (5%/40%) through Crisis (20%/70%)
- OZK: ACL exhausted at Moderate, CET1 breaches buffer at Crisis (6.4%)
- WAL: ACL exhausted at Moderate, CET1 at 4.8% in Crisis — plus SSFA bomb ($17.2B at 20% RW, scrutiny drops CET1 by ~2%)
- Key finding: "Moderate" scenario (10% default, 50% severity) is BELOW current CMBS-implied levels — this is the base case, not the stress case
- Explicitly noted what's NOT included: Layer 2 (NDFI), AOCI, capitalized interest from reserves

**Data sources:** FFIEC Call Report Q4 2025, FDIC API, OZK 10-K Q4 2025, WAL FFIEC RC-R, KB entries. Subagent data pulls from OZK/sources/ and WAL/sources/.

**Old view:** Qualitative description of exposure ("OZK has 37.6% MI3" and "WAL has 474% CRE/Tier 1")
**New view:** Quantified capital impairment under five loss scenarios showing exactly when each bank breaks

---

## 2026-03-31 — v1.1: CHANNEL INTERACTION MAP + VALIDATION SCORING

### THESIS Updated → v1.1
**Author:** REGINALD + Will
**Action:** Added Channel Independence Analysis (cluster reclassification), Cross-Cluster Amplification map, Bank × Cluster Exposure table. Replaced flat validation lists with weighted Thesis Scorecard.

**What changed:**

**Channel Interaction Map (new Section 1.5):**
- Reclassified 8 channels into 4 independent clusters: A (CRE Recognition Complex: #1+#2+#6), B (Shadow Banking: #3+#4), C (Fraud/Episodic: #5), D (Macro Trap: #7+#8)
- Mapped 6 cross-cluster amplification pathways with speeds and status (from FLOW.tsv data)
- Identified FHLB Cascade as the convergence node (5+ distinct flows terminate there)
- Built Bank × Cluster table showing WAL and ZION at 3/4 cluster exposure — highest non-linear risk
- Key insight formalized: independence BETWEEN clusters (not between all 8 channels) is what makes convergence lethal

**Validation Scoring (rewritten Section 7):**
- 5 confirmation gates, weighted: G1 Systemic earnings (30%), G2 CRE recognition (25%), G3 Channel B bridge (20%), G4 Funding stress (15%), G5 Hidden exposure (10%)
- Current score: 38% from gates + ~20% from supporting validations = **58% effective confidence**
- 6 invalidation criteria scored: **8% invalidation risk**
- Net assessment: 50% MEDIUM-HIGH, waiting on G1 (Apr 16-29)
- Added scenario table: what moves confidence to 85%/70%/40%/20%

**Old view:** 8 channels listed as independent; validation was a flat checklist with no scoring
**New view:** 4 independent clusters with mapped interactions; validation is a weighted scorecard producing a trackable number (58% confirmed, 8% invalidation risk)

**Why this is v1.1 not v2.0:** No structural thesis change. Same channels, same targets, same conviction. This is analytical refinement — making the existing thesis more precise, not changing it.

---

## 2026-03-31 — THESIS FOLDER CREATION + v1.0 BASELINE

### Structural Change
**Author:** REGINALD + Will
**Action:** Created `thesis/` folder. Moved THESIS.md from REGINALD root. Created TIMELINE.md and CHANGELOG.md. Adopted SAM's thesis management pattern.

**What changed:**
- THESIS.md moved to `thesis/THESIS.md`, versioned as v1.0
- TIMELINE.md created — forward-looking catalyst calendar pulled from STATUS.md KEY CATALYSTS section and expanded with branch points, "our view" annotations, and position calendar
- CHANGELOG.md created (this file) — audit trail for thesis evolution
- STATUS.md KEY CATALYSTS section replaced with pointer to `thesis/TIMELINE.md`

**Why:** Thesis had grown to 326 lines with no version control or change tracking. Catalysts were a flat table in STATUS.md with no analytical commentary. The new structure separates the *what we believe* (THESIS), the *what's coming* (TIMELINE), and the *how our view evolved* (CHANGELOG).

**Thesis state at v1.0:**
- 8 channels, 6 at red+, all open simultaneously
- 3-layer hidden CRE architecture (classification, NDFI wrapper, collateral fraud)
- Dual failure channels: A (CRE, positioned) + B (PC/NDFI, uninitiated)
- 5 target banks: OZK (reservoir), WAL (fast transmission), EGBN (pure concentration), ZION (benchmark), CFG (fund finance bridge)
- Conviction: HIGH
- Primary near-term catalyst: Q1 earnings wave (Apr 16-29)

---

## PRE-CHANGELOG THESIS EVOLUTION (summary)

The thesis evolved through multiple sessions prior to formal change tracking. Key milestones reconstructed from STATUS.md archives and research outputs:

| Date | Change | Why / Trigger | Impact |
|------|--------|---------------|--------|
| ~Feb 2026 | Initial convergence thesis formulated | Observed multiple stress channels converging on same bank balance sheets simultaneously — no existing framework captured multi-channel risk | 5 channels identified; thesis differentiated from consensus "CRE is bad" narrative |
| ~Feb 11 | Sub-agents deployed (CREED, CORAL, RENO, TEX) | Needed granular geographic data to test whether stress was national or concentrated in specific MSAs | Geographic coverage expanded; FL and DC emerged as highest-stress corridors |
| ~Feb 23 | Hidden CRE methodology developed (Memo Item 3 screen) | Anomaly: OZK's C&I doubled (+153%) over 8 quarters while construction fell 36.9%. Investigated Call Report classification rules → found RCON2746 | Layer 1 architecture established; OZK true CRE 71.5% vs reported ~35%. Metropolitan Capital precedent (failed Jan 30 at 39.6% MI3) |
| ~Mar 4-5 | Workbook framework built (VX, KB, FLOW, PREDICTIONS) | Signal volume was exceeding working memory. Needed structured storage with cross-links to prevent losing connections between data points | Analytical infrastructure; enabled systematic tracking of 59 vectors, 116+ KB entries, 22 flow pathways |
| ~Mar 6 | NFP / federal layoffs channel added | Feb NFP + DOGE 307K+ confirmed cuts. DC corridor direct hit to EGBN (100% DC). Recognized this was a separate channel from CRE — employment-driven, not asset-driven | Channel 7 formalized; EGBN escalated to Tier 1 |
| ~Mar 10 | NDFI/Whalen research integrated | Whalen IRA Bank Book revealed $1.54T NDFI (later revised to $4.2T with undrawn). Realized NDFI was Layer 2 — CRE hidden inside fund finance structures, invisible to all regulatory screens | Layer 2 architecture; NDFI exposure 5.1x prior $300B model. Changed the scale of the thesis fundamentally |
| ~Mar 13 | CRE maturity wall research ($875B) | MBA data + Trepp maturity schedules quantified the forcing function. $400B pushed forward from prior years = no more extensions available | Channel 6 quantified; calendar-driven inevitability established. Maturity wall = the thesis has a deadline |
| ~Mar 17 | Insider scan + MFS/fraud chain mapped | Cantor $270M ring discovered (WAL $98M, ZION ~$100M). Insider behavior scan showed zero buying at OZK/WAL. MFS £2B double-pledging surfaced | Channel 5 formalized; fraud losses bypass delinquency pipeline = fast, unpredictable channel |
| ~Mar 21 | Jefferies Q1 preview — V2 chain hypothesized | Connected Jefferies FI exposure → WAL lending relationship → MFS losses. Predicted JEF Q1 would show credit losses from same fraud chain hitting WAL | WAL thesis sharpened; V2 became testable prediction (confirmed 4 days later) |
| ~Mar 25 | JEF Q1 CONFIRMED V2 chain | Jefferies reported: EPS $0.70 vs $0.91 (-23%), $17M MFS losses, First Brands fraud, SMFG backstop walked back. Exactly what we predicted | **Major validation.** First external confirmation of a thesis-derived prediction. Conviction moved from MEDIUM-HIGH → HIGH |
| ~Mar 26 | Analyst downgrades on WAL (Weiss, Barclays, WFC) | Weiss Buy→Hold, Barclays PT $105→$90, WFC PT $83→$79. Street catching up to what we identified weeks earlier | Market starting to reprice. Consensus PT ~$85-90 vs our $47-60. Still a gap but narrowing on the headline CRE story |
| ~Mar 26 | AOCI capital rewrite signal integrated | Fed/FDIC/OCC proposed mandatory AOCI phase-in for Cat III/IV banks. $49.5B aggregate hit. Recognized this as SEPARATE capital drain from credit losses — two simultaneous bleeds | Originally treated as part of Channel 8. Realized it's its own mechanism — regulatory capital drain independent of credit performance |
| ~Mar 27 | Stagflation trap formalized | Brent hit $112.57 (Hormuz closed since Mar 2). PPI +0.7% (hottest in 2+ years). 10Y hit 4.48%. Recognized the macro backdrop wasn't just "rates stay high" — it was actively hostile to bank earnings | 8th channel added. Changed thesis from "banks face losses" to "banks face losses AND cannot earn through them." Closed the escape route |
| ~Mar 30 | CFG 10-K confirmed $12.5B fund finance | Annual filing disclosed fund finance book (+40% YoY) with $4.0B in unspecified-collateral secured PC finance. Quantified the Channel A → Channel B bridge | Channel B bridge quantified. CFG became the tradeable expression of PC→bank transmission. Uninitiated but on deck |
| Mar 31 | Thesis folder created, v1.0 baseline | Thesis matured enough to need version control and change tracking | Formal tracking begins. SAM's thesis management pattern adopted |

---

*Thesis → `THESIS.md`*
*Timeline → `TIMELINE.md`*
