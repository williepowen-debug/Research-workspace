# CROSS_REFS — REGINALD

**Purpose:** dispatch-time identifier-cache for WALTER. When about to dispatch a signal, grep this file for relevant bank ticker / channel code / cohort pattern / exposure term → cross-ref REGINALD IDs (REG-NN / KB-WAL-NNN / KB-OZK-NNN [peer] / VX-REG-NN / FLOW-REG-N / REG-T-NN / REG-CAL-YYYYMMDD-EVENT) → cite in `dispatch_note` so REGINALD's bank-side decision-loop tightens.

**Read-by:** WALTER at signal-dispatch time (NOT at boot — too dense for boot read; lookup-on-demand only).

**Source-of-truth:** REGINALD's `AGENTS/REGINALD/workbook/*.tsv` + `AGENTS/REGINALD/STATUS.md` + `AGENTS/REGINALD/CALENDAR.md` + `AGENTS/REGINALD/registry/THRESHOLDS.tsv` + `AGENTS/REGINALD/board/BOARD_LOG.tsv` + `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md`. This file is a denormalized **cache** for grep-speed at dispatch — REGINALD's TSVs/STATUS are the canonical source. If REGINALD's TSV says X and this cache says Y, **trust REGINALD's TSV**. This cache exists to surface relevance, not to replace.

**Refresh trigger:** REGINALD STATUS bump OR new KB/VX/FLOW row OR new prediction registered OR threshold tuned OR watchlist add/remove OR CALENDAR event added/removed. WALTER self-task on detection at next dispatch session.

**Last refreshed:** 2026-05-11 scaffold v0.1 post REGINALD ↔ WALTER LIAISON Turn 4 parallel-ship. Source commits: REGINALD `f59f715b` (LIAISON Turn 1) + `6e216fd4` (LIAISON Turn 3 + 3 files instantiated) + WALTER LIAISON Turn 4 commit (this turn).

**Pattern lineage:** modeled on `design/CROSS_REFS/RED.md` (canonical CROSS_REFS pattern, post RED LIAISON 5/6). REGINALD identifier surface is richer (multi-channel scoring + per-bank KBs + 5-tier watchlist) so this file has a Bank Watchlist top section + per-identifier-class sections.

---

## §0 — Operational state pointers

For dispatch-time orientation:

| Anchor | Path | Refresh trigger |
|--------|------|-----------------|
| **Current state + signal dashboard** | `AGENTS/REGINALD/STATUS.md` "SIGNAL DASHBOARD" / "ALERT BAND THRESHOLDS" | REGINALD-session each |
| **Bank watchlist + multi-channel scoring** | `AGENTS/REGINALD/STATUS.md` + `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md` | Watchlist add/remove or score change |
| **Active predictions REG-NN** | `AGENTS/REGINALD/STATUS.md` "PREDICTIONS" + `workbook/PREDICTIONS.tsv` | Prediction add / status change |
| **Thresholds (machine-readable, 8 rows v0.1)** | `AGENTS/REGINALD/registry/THRESHOLDS.tsv` (8-col schema) | Threshold add or value tune |
| **BOARD disposition ledger** | `AGENTS/REGINALD/board/BOARD_LOG.tsv` (11-col schema; 32-row backfill stub) | Per-signal disposition at consume |
| **Forward calendar** | `AGENTS/REGINALD/CALENDAR.md` (md primary; CALENDAR_DATA.tsv ~7d post-CARL self-task) | Event add/remove |
| **8-channel framework** | `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md` + `AGENTS/REGINALD/workbook/CHANNELS.md` | Framework version bump |
| **Cross-bank convergence patterns** | `AGENTS/REGINALD/workbook/CONVERGENCE.md` | New pattern surfaced |
| **CRE architecture** | `AGENTS/REGINALD/workbook/CRE_ARCHITECTURE.md` | CRE-side research bump |
| **NDFI research** | `AGENTS/REGINALD/workbook/NDFI_RESEARCH.md` | NDFI breakout updates |

**Current state at scaffold time (2026-05-11):**
- Overall status: **🟠 ELEVATED** (cohort fade pattern 12/12 intact post Q1 earnings; V1 Hidden CRE thesis getting direct primary-source validation via EGBN 10-Q May 7)
- BOARD_LOG: 32-row backfill stub (3 INTEGRATED Apr 14 + 16 BACKFILL action-primary + 13 BACKFILL info-cc + 3 PROME-pinch-hitter 5/9 BACKFILL-PENDING)
- Active predictions: REG-01 through REG-25 (most recent additions Apr 24)
- Workbook: VX 59 rows / KB 116+ rows + per-bank KBs (WAL 105 / OZK 185 in peer agent) / FLOW 22 rows
- Sub-agents: BROCK (BDC/PC, now top-level peer) + CREED (CRE market-level) + CORAL (Florida)
- Calibration cycle 1 clock: starts 2026-05-11 Turn 5 close → ETA May 25 (14d primary) OR N=15 forward BOARD dispositions (early-fire), synced w/ BRENT

---

## §1 — Bank watchlist (Q4-A overlap surface — TIER hierarchy)

5-tier hierarchy from REGINALD LIAISON Turn 3 Q4-(A). When dispatching a signal that mentions any string from TIER-1 / TIER-2 / NEW-TRACKING / EXTERNAL-WATCH, **REGINALD-info is mandatory** regardless of sub-agent action. OZK exception: OZK signals route to `../OZK` action; REGINALD-info ONLY when OZK signal also touches another REGINALD-watchlist ticker.

> 🔴🔴 **SCORE COLUMN RE-CUT 2026-08-22 AGAINST `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md` **v2.0** (rebuilt 2026-08-20). THE ENTIRE PRIOR SCORE SET WAS DEAD, NOT JUST ONE ROW — and this file is read AT DISPATCH TIME, so a dead score silently mis-prioritises a live signal.**
>
> **What happened (DAEDALUS packet 8/20, verified by WALTER at REGINALD's matrix rather than accepted on relay):** REGINALD rebuilt the matrix on 8/20 (`75f0dd18b`) and **the ranking INVERTED. FLG went from `8`, LAST of 7, to `6`, FIRST of 14 scored banks.** REGINALD's own commit states the v1 scores *"could not be derived from v1's own method"* and that **no rescale commit, scale note or method document exists anywhere in the repo.** ⇒ **v1 and v2 are not the same scale and v1 numbers are not convertible — they are retired, not adjusted.** **AMTB was never in the v1 table at all.**
>
> 🔑 **THE COST THIS WAS ACTUALLY INCURRING: a signal on the cohort's now-HIGHEST-scored name resolved here to `TIER-2` with an EMPTY primary-thesis cell — deprioritised off a number nobody could reproduce.**
>
> ⚠️ **REGINALD'S OWN CAVEAT, CARRIED VERBATIM BECAUSE A RE-CUT IS EXACTLY WHERE IT WOULD BE LOST: A `0` IS NOT A CLEAN BILL OF HEALTH. CFG scores 0 while holding the cohort's SECOND-LARGEST private-credit NDFI book (~$4.5B committed) — reported and DELIBERATELY UNSCORED. Do not let this table turn "unscored" into "safe."** `[[finding_verification_zero_is_ambiguous]]`
>
> 📌 **This file's header already said REGINALD's own surfaces WIN over this cache. That rule was correct and did not save anyone — nothing re-read the cache when the matrix moved.** ⇒ **a precedence rule is not a refresh mechanism.** `[[finding_retired_threshold_has_no_publisher]]`

| Tier | Ticker | v2.0 score (rank of 14) | Status | Primary thesis | Recent activity |
|------|--------|---------------------|--------|----------------|-----------------|
| **TIER-1** | **FLG** | **6 — 🔴 1st** | **PEER-ROUTED as of 2026-08-22 → `AGENTS/FLG/` action** (ROUTING_TABLE v0.30); REGINALD-info on cohort overlap | CRE conc. 327.5% · NPL 4.88% · reserve/NPL 29% (cohort-worst coverage) · NYC rent-regulated multifamily | Registered as a single-name desk 8/20; **zero gates, zero thresholds** |
| **TIER-1** | EGBN | **5 — 🟠 2nd=** | Watchlist active | CRE conc. 258.2% · NPL 2.05% · reserve/NPL 88%; V1 Hidden-CRE primary-source validation | Cohort-max office CRE 10.77% |
| **TIER-1** | **AMTB** | **5 — 🟠 2nd=** | **NEW — absent from the v1 table entirely** | CRE conc. 218.4% · NPL 2.46% · reserve/NPL 51% | Added at the v2.0 rebuild |
| **TIER-2** | VLY | **3 — 🟡 4th** | Watchlist active | CRE conc. 319.5% · reserve/NPL 128%; provisions-mask −66% YoY tell | — |
| **TIER-2** | OZK | **2 — 5th=** | **PEER-ROUTED → `../OZK` action**; REGINALD-info only when an OZK signal also touches another watchlist ticker | CRE conc. 259.5% · reserve/NPL 154%; IQHQ maturity; SUB-NOTE Oct 1 reprice | — |
| **TIER-2** | WAL | **2 — 5th=** | **PEER-ROUTED → `AGENTS/WAL/` action** (ROUTING_TABLE v0.20); REGINALD-info | CRE conc. 161.1% · reserve/NPL 86%; office single-point conc.; **$122.5M** the cohort's largest NDFI-linked figure in the matrix | **`REG-T-02` (<78, sustain-1) RULED UN-FIRED 8/20 — exited 6/30; a close <78 from 8/21 is a FIRST FIRE OF A NEW CYCLE.** 8/21 close **$79.67** |
| **TIER-2** | SSB | **2 — 5th=** | Watchlist active | CRE conc. 281.0% · reserve/NPL 217%; FL/TX exposure — **CORAL primary cross-feed** | — |
| **TIER-2** | BKU | **2 — 5th=** | Watchlist active | CRE conc. 193.9% · reserve/NPL 95% | — |
| **TIER-2** | SBCF | **2 — 5th=** | Watchlist active | CRE conc. 229.6% · reserve/NPL 210% | — |
| **TIER-2** | ZION | **1 — 10th=** | Watchlist active | CRE conc. 151.7% · reserve/NPL 226%; cohort-fade pattern; FHLB-decline side | — |
| **TIER-2** | MTB | **1 — 10th=** | Watchlist active *(was EXTERNAL-WATCH)* | CRE conc. 103.9% · reserve/NPL 180%; Baltimore CRE thesis; FHLB-surge side | — |
| **TIER-2** | CUBI | **1 — 10th=** | Watchlist active | CRE conc. 179.2% · reserve/NPL 293%; **cohort-max NDFI 19.96%** | — |
| **TIER-2** | CFG | **0 — 13th=** ⚠️ | Watchlist active | ⚠️ **A 0 IS NOT SAFETY — CFG holds the cohort's second-largest private-credit NDFI book (~$4.5B committed), REPORTED AND DELIBERATELY UNSCORED.** Cohort-fade 12/12; FHLB-surge side | — |
| **TIER-2** | HBAN | **0 — 13th=** ⚠️ | Watchlist active *(was NEW-TRACKING)* | Same unscored caveat applies. SBA + small-business + CRE | — |
| **NEW-TRACKING** | FITB | not in v2.0 | Added May 8 | POSITIONS broker refresh | — |
| **HISTORICAL-ON-WATCH** | FBC, WBS, BHRB, FHN | not in v2.0 | tracked historically | — | — |

**Dispatch-time grep procedure:** when an incoming signal body / dispatch_note mentions any ticker from the table above, surface REGINALD-relevant context: `REGINALD watchlist tier X / score Y / current thesis Z / recent activity W`. For EXTERNAL-WATCH tier, REGINALD-info is mandatory but with the note "watchlist-context tier" so REGINALD knows the priority is observational not active.

---

## §2 — Predictions (REG-NN) — active + recent-resolved

Source: `AGENTS/REGINALD/workbook/PREDICTIONS.tsv` + STATUS.md "PREDICTIONS" section. Refresh trigger: prediction status change.

| ID | Topic | Prediction | Horizon | Confidence | Status |
|----|-------|-----------|---------|------------|--------|
| **REG-01** | Office CMBS DQ | Stays >10% | Through 2026 | 90% | ACTIVE |
| **REG-02** | FHLB advances | Spike >$600B | Q2-Q3 2026 | 60% | ACTIVE |
| **REG-03** | Tier 1 capital raise | At least one Tier 1 bank | H2 2026 | 50% | ACTIVE |
| **REG-04** | Chicago→Phoenix pattern | Replication | H1 2026 | 65% | ACTIVE |
| **REG-20** | WAL major stress event | Earnings miss / dividend cut / capital action | Apr-Jun 2026 | 82% | **RESOLVED-CONFIRMED-PARTIAL 2026-05-08** (Apr 21 1 of 3 OR-conditions; modest tape reaction; PARTIAL credit) |
| **REG-24** | WAL Office classified | >$500M by Q3 2026 | Q2-Q3 2026 | 60% | ACTIVE (Apr 24 add — $946M Office maturity wall driver) |
| **REG-25** | WAL ex-fraud NCO | >40bps in Q2 OR Q3 2026 | Q2-Q3 2026 | 55% | ACTIVE (Apr 24 add — Q1 39bps above mgmt 25-35bps guide) |

*Other REG-NN predictions (REG-05 through REG-19, REG-21-23) tracked in `PREDICTIONS.tsv`. Cache holds only active+recent-resolved for grep-speed; full history → workbook.*

---

## §3 — KB anchors (KB-WAL-NNN + KB-OZK-NNN peer-cross-ref)

KB row identifiers for dispatch-time citation:

| Identifier class | Source | Row count (2026-05-11) | Cross-ref pattern |
|------------------|--------|------------------------|-------------------|
| **KB-WAL-NNN** | `AGENTS/REGINALD/workbook/KB.tsv` (WAL-specific subset) | ~105 rows | WAL-specific deep dive (Office maturity wall, NCO trajectory, V1+V2+V3 thesis, ex-fraud Q1 39bps) |
| **KB-REG-NNN** | `AGENTS/REGINALD/workbook/KB.tsv` (general bank-thesis KB) | ~116 rows | General bank-thesis claims (HC methodology, 8-channel framework, cohort-fade pattern, FHLB-bifurcation, etc.) |
| **KB-OZK-NNN** | `AGENTS/OZK/workbook/KB.tsv` (PEER AGENT — not REGINALD-owned) | ~185 rows | OZK-specific deep dive (CRE concentration, FDIC filings, IQHQ maturity, SUB-NOTE reprice). **PEER-ROUTED:** OZK signals → `../OZK` action; REGINALD-info on cohort overlap only. |
| **VX-REG-NN** | `AGENTS/REGINALD/workbook/VX.tsv` | 59 rows | Counter-evidence vectors against REGINALD bank-stress thesis (bull-case steelman material) |
| **FLOW-REG-N** | `AGENTS/REGINALD/workbook/FLOW.tsv` | 22 rows | Upstream/downstream agent transmission paths (LABOR → REGINALD; REGINALD → RED, etc.) |

*Dispatch-time grep: if a signal touches a named bank or thesis element on REGINALD's framework, surface KB-row hits for the recipient agents.*

---

## §4 — Channel codes (Q4-B overlap surface — 8-channel framework + v0.9 enum candidate)

REGINALD's 8-channel BANK_EXPOSURE_MATRIX framework. **v0.9 candidate:** `bank_transmission` FORMAT_SPEC field with these 8 codes as enum values (parallel to CARL's `consumer_transmission` + BRENT's `energy_transmission`). When a signal touches any channel code (via dispatch_note, cluster_secondary, or body-text grep), REGINALD-info is mandatory.

| Code | Channel | Full name | Mandatory REGINALD-info trigger |
|------|---------|-----------|----------------------------------|
| `cre` | CRE | Commercial real estate (offices, hotels, MF) | Office concentration / CRE / multi-family / hotel-distress / forced-sale price discovery |
| `hidden_cre` | HC | Hidden CRE (RCON2746 / Memo Item 3 reclassification) | MI3 / RCON2746 / hidden CRE explicit framework callout |
| `ndfi` | NDFI | Non-depository financial institution exposure | NDFI breakout / capital-call / secured-PC-finance / other-finance-insurance |
| `private_credit` | PC | Private credit / BDC (overlap with BROCK-primary) | BDC gates / PIK rates / fund redemptions / PC default cascade |
| `mfs_fraud` | MFS | Mortgage fraud / fund-finance fraud chain (LAM/Cantor template) | Fraud reclassification / fund-finance disclosure / Schedule O / LAM-Cantor pattern |
| `cmbs_maturity` | CMBS | CMBS maturity wall (2026 $875B per MBA) | CMBS DQ / special-servicing / B-piece holder / loan-trust impairment |
| `fed_layoffs` | FED-LAYOFFS | DOGE federal layoffs cascade (DC corridor) | DC bank exposure / federal layoff cascade / Trump EO / DOGE specific mention |
| `stagflation_trap` | STAGFLATION | Stagflation trap (oil → consumer → bank borrower stress) | Oil pump-pass-through + consumer DQ + bank borrower stress chain (Brent ≥$110 cluster) |

**v0.9 enum candidate (pre-cosigned in REG LIAISON Turn 4, V0_9_STACK.md tracker):**
```yaml
bank_transmission: cre | hidden_cre | ndfi | private_credit | mfs_fraud | cmbs_maturity | fed_layoffs | stagflation_trap
```

### §4a — NDFI 5-category schema breakdown (FFIEC RC-C 10.a-10.e)

The `ndfi` channel code above is the aggregate. **Per FFIEC RC-C call report schedule, NDFI decomposes into 5 named sub-categories** — at dispatch, when a signal touches NDFI substance, grep for the sub-category to surface the right framing in dispatch_note. Added 2026-05-14 (WALTER self-task per 5/11 NDFI deep-dive return).

| Sub-code | RC-C line | Sub-category | Greppable terms | YE 2025 scale (FDIC primary) |
|----------|-----------|--------------|-----------------|------------------------------|
| `ndfi_securities` | 10.a | Loans to securities firms (broker-dealers, dealers' financing) | "broker-dealer financing" / "securities firm credit line" / "dealer loans" | — |
| `ndfi_insurers` | 10.b | Loans to insurance carriers + insurance underwriters | "insurer credit facility" / "reinsurance financing" / "captive insurer lending" — **SHADE cross-feed primary** | — |
| `ndfi_other_finvehicles` | 10.c | Loans to other financial vehicles (REITs, REIT-affiliates, finance companies, mortgage finance) | "finance company line" / "REIT credit facility" / "consumer finance lender" | — |
| `ndfi_pe_pc` | 10.d | Loans to private equity / private credit funds (capital-call lines, NAV lending, subscription lines, fund finance) | "capital-call facility" / "subscription line" / "NAV facility" / "fund-finance" / "private credit fund line" — **BROCK overlap primary** | — |
| `ndfi_other` | 10.e | Loans to other NDFIs (residual; mostly unconventional non-bank lenders) | "other NDFI" / residual 10.e classification | — |
| **NDFI aggregate (10.a + 10.b + 10.c + 10.d + 10.e)** | **10.x** | **Full NDFI exposure** | "NDFI" / "non-depository financial institution" / "Memo Item 10" | **$1.4T industry** / **+35.2% YoY** / single-name top WFC $212B (21% of total loans) / MS BCI $X (19.73%) / CUBI 33% |

**Single-bank concentration tier (sourced from 5/11 NDFI deep-dive primary):**

| Bank | NDFI %-of-loans | $-exposure | Tier flag | Notes |
|------|-----------------|------------|-----------|-------|
| WFC | 21% | ~$212B | TIER-1 NDFI scale | Q1 2026 first fraud-related NDFI loss disclosed |
| MS | 19.73% | (BCI) | TIER-1 NDFI growth | +316bps QoQ (one of the steepest quarterly accelerations) |
| CUBI | 33% | mid-tier bank | OUTLIER | %-of-loans concentration outpaces majors; mid-bank fragility tell |
| WAL | TBD pending Q1 NDFI breakout disclosure | TBD | Watch | Investor-Day 5/12 did not disclose NDFI sub-cat |

**Forward-test:** **2026-05-16 FFIEC call-report-bulk public-data-distribution (REG-CAL-20260516-FFIEC-PDD)** — first bank-level NDFI 5-cat splits publicly available for YE 2025 / Q1 2026 deltas. Plan a coordinated WALTER+REGINALD+BROCK pull on release.

**Cross-agent overlap map:**

| Sub-code | Primary agent | Secondary agent | WALTER cross-feed |
|----------|---------------|-----------------|-------------------|
| `ndfi_securities` | REGINALD | BOND, HENRY | broker-dealer-funding |
| `ndfi_insurers` | **SHADE** (PE-insurer-nexus primary) | REGINALD | insurer-shadow-banking |
| `ndfi_other_finvehicles` | REGINALD | LIQUID | finance-company-credit-cycle |
| `ndfi_pe_pc` | **BROCK** (PC-fund-finance primary) | REGINALD | BDC-fund-line-strain |
| `ndfi_other` | REGINALD | BROCK | residual / new mechanism flag |

**Sponsor-bifurcation overlay (5/11 image-batch finding, sharpened 5/14 BROCK REQ):**

When `ndfi_pe_pc` substance + sponsor named, run sponsor-action-comparison cross-cluster:

| Sponsor strategy | Indicators | Read |
|------------------|------------|------|
| **Double-down** (KKR template) | Sponsor-backstop (preferred equity injection + tender) / multi-vehicle stress concurrent / capital-flexibility constraint not yet binding | Bear thesis on portfolio quality is firm; sponsor reads stress as transient |
| **Cash-out** (Apollo template) | Shopping captive listed BDC / lending halted / NAV-discount sale / redemption acceleration | Bear thesis on portfolio quality is firm; sponsor reads stress as durable + reaches exit |

Same data, opposite strategies = leverage-and-flexibility tell, not thesis-direction tell. Surface both in dispatch_note when applicable.

**Source:** FFIEC Call Report Schedule RC-C 10.a-10.e + FDIC 2026 Risk Review + WALTER 5/11 NDFI deep-dive sub-agent return + 5/11 image-batch SIG-W-20260511-038/-039/-040 sponsor-bifurcation context. WALTER outbox REQ-BROCK-20260514 filed in parallel to this append.

---

## §5 — Cross-bank pattern keys (Q4-C overlap surface — cohort/structural indicators)

When a signal references any cohort-level pattern (string match in dispatch_note or signal-body), REGINALD-info is mandatory **even when no specific bank ticker is named** — REGINALD synthesizes across names.

| Pattern key | Description | Current state |
|-------------|-------------|---------------|
| `cohort_fade_pattern` | 12/12 active; reset on any miss-into-rally print | 12/12 intact post Q1 earnings; WAL/OZK 4/21 both missed |
| `fhlb_bifurcation` | 4/3 split: DECLINE (FITB,RF,ZION,VLY) / SURGE (MTB,CFG,PNC) | Active May 2026 |
| `provisions_mask_deterioration` | Provisions-vs-NCO timing tell — leading indicator | VLY -66% YoY tell logged; CFG candidate |
| `office_single_point_concentration` | Single-bank office exposure concentration | WAL Slide 12 38% / EGBN 10-Q text |
| `hidden_cre_relabeling_trajectory` | MI3 / RCON2746 quarterly delta | Q1 bulk update expected mid-May FFIEC PDD |
| `mi3_rcon2746_screen` | Hidden CRE methodology applied to any bank | EGBN screen confirmed; framework spreadable |
| `ndfi_breakout_decomposition` | Capital-call vs secured-PC vs other-finance trajectory | Active research thread |

---

## §6 — Specific exposure terms (Q4-D overlap surface — high-precision greppable strings)

Dispatch-time grep checks on signal body-text. High-precision tags that flag REGINALD-mandatory routing even on signals from non-bank-domain sources.

```
"Memo Item 3" / "RCON2746"                              — Hidden CRE methodology
"FHLB advance" / "FHLB borrowing"                       — funding-stress indicator
"Schedule O" / "Table 16"                               — large-credit disclosure (10-Q drill)
"criticized assets" / "classified assets"               — leading credit migration
"30-89 day past due" / "Special Mention"                — leading-bucket buildup
"Capital call" + "Secured PC finance" + "Other finance and insurance"  — NDFI breakout
"office concentration" / "CRE office"                   — single-point office stress
"hidden CRE" / "MI3"                                    — explicit framework callout
```

**Note on (B)+(C)+(D) combinations:** signals frequently hit multiple overlap surfaces simultaneously (e.g., a WAL 10-Q signal might hit ticker-WAL + channel-cre/hidden_cre + pattern-office_single_point_concentration + exposure-term-criticized-assets). REGINALD-info routing is set on first-hit; additional surfaces enrich the dispatch_note but don't multi-route. De-dupe: REGINALD-info appears once on the info: line regardless of how many overlap surfaces fired.

---

## §7 — Thresholds (REG-T-NN) — pointer to registry

Source-of-truth: `AGENTS/REGINALD/registry/THRESHOLDS.tsv` (8-col, 8-row v0.1 shipped REG LIAISON Turn 3 2026-05-11). Read at WALTER spawn-protocol step 6b alongside RED-FT-NN. Auto-dispatch via CHECKLIST v0.10 Phase 2 step 7 eval pass. Stale-fire suppression via `AGENTS/WALTER/registry/REG_THRESHOLDS_FIRED_LOG.tsv` (5-col, header-only at v0.1 ship).

| ID | Metric | Threshold | Sustain | Action | Recipient chain |
|----|--------|-----------|---------|--------|-----------------|
| REG-T-01 | KRE-PRICE | <$60 | 1 sess | ALL-ALL-ACUTE | REGINALD action / ALL-AGENTS info / Will |
| REG-T-02 | WAL-PRICE | <$78 | 1 sess | V1V3-ACCELERATE | REGINALD action / Will |
| REG-T-03 | HY-OAS | >320 bps | 3 sess | CREDIT-CANARY-FIRED | REGINALD action / CARL info |
| REG-T-04 | HY-OAS | >350 bps | 3 sess | ISSUANCE-FREEZE | REGINALD action / LIQUID action / Will |
| REG-T-05 | INITIAL-CLAIMS | >300K | 1 sess | ORANGE-TO-RED | REGINALD action / CARL LABOR info |
| REG-T-06 | FHLB-ADVANCES | >$700B | 3 sess | EARLY-CRISIS | REGINALD action / LIQUID info |
| REG-T-07 | OFFICE-CMBS-DQ | >15% | 3 sess | CRE-ACCELERATE | REGINALD action / BROCK SHADE info |
| REG-T-08 | SOFR-IORB | >+15 bps | 3 sess | LIQUID-FHLB-SPIKE | REGINALD action / LIQUID action / Will |

---

## §8 — Calendar pointer (REG-CAL-YYYYMMDD-EVENT)

Source-of-truth: `AGENTS/REGINALD/CALENDAR.md` (markdown, REGINALD-owned, primary forward-dates). Future `AGENTS/REGINALD/CALENDAR_DATA.tsv` (machine-parseable, follows §2b CARL/BRENT pattern when those calendars land) — REGINALD self-task ~7d post-CARL DATA_RELEASE_CALENDAR.md ship.

Pre-cosigned May/June scope (REG LIAISON Turn 3 Q6):

| Event ID | Date | Bank | Type | Window | Notes |
|----------|------|------|------|--------|-------|
| REG-CAL-20260511-WAL-10Q | 2026-05-11 | WAL | 10Q-FILING | ±72h-IMMEDIATE | Range May 11-13; highest-impact for V2.0 thesis |
| REG-CAL-20260511-OZK-10Q | 2026-05-11 | OZK | 10Q-FILING | ±72h-IMMEDIATE | OZK peer-agent owns; REGINALD-info on cohort-fade |
| REG-CAL-20260512-WAL-INVDAY | 2026-05-12 | WAL | INVESTOR-DAY | ±24h-IMMEDIATE | Leucadia inventory pressure; Office de-risk story |
| REG-CAL-20260515-EXPIRY | 2026-05-15 | WAL,SSB | OPTIONS-EXPIRY | T-3-IMMEDIATE | WAL $75P + SSB $95P cluster — pin-risk SSB |
| REG-CAL-20260516-FFIEC-PDD | 2026-05-16 | ALL | CALL-REPORT-BULK | ±48h-IMMEDIATE | MI3 / RCON2746 Q1 bulk update; mid-May target |
| REG-CAL-20260601-REINSURE | 2026-06-01 | SSB,OZK | REINSURANCE | ±5d-PRIORITY | FL property reinsurance renewals; CORAL primary |
| REG-CAL-20260618-AOCI-CLOSE | 2026-06-18 | ALL | REG-COMMENT-CLOSE | ±14d-PRIORITY | AOCI capital rewrite comment period closes; Cat III/IV $49.5B |
| REG-CAL-20260618-EXPIRY | 2026-06-18 | ALL | OPTIONS-EXPIRY | T-7-IMMEDIATE | WAL $85P/$65P + SSB $90P + KRE multi + IWM $250P + HYG $75P |
| REG-CAL-20260730-WAL-Q2 | 2026-07-30 | WAL | EARNINGS-AMC | ±48h-IMMEDIATE | REG-25 ex-fraud NCO test + REG-24 Office classified test |
| REG-CAL-20260801-IQHQ-MAT | 2026-08-01 | OZK | LOAN-MATURITY | ±7d-IMMEDIATE | OZK peer-agent primary; REGINALD-info |
| REG-CAL-20261001-OZK-SUBNOTE | 2026-10-01 | OZK | SUB-NOTE-REPRICE | ±5d-PRIORITY | $350M sub notes 2.75%→SOFR+209; OZK peer primary; REGINALD-info |

**Dispatch-time pre-position logic:** WALTER reads CALENDAR_DATA.tsv at boot, builds in-memory pre-position queue for next 7 sessions. At dispatch, if signal touches a named bank in the pre-position queue + within precedence_override_window, auto-flag `event_window: open` + `event_ref: <REG-CAL-id>` + override precedence per the row's window-precedence column.

---

## Refresh discipline

| Trigger | Sections to refresh | Cost |
|---------|--------------------|------|
| REGINALD STATUS bump | §0 + §1 multi-channel scores + §2 predictions status + recent-activity column | ~5min |
| New KB-WAL-NNN or KB-REG-NNN row | §3 row counts | ~1min |
| Watchlist add/remove | §1 table + §0 (operational state) | ~5min |
| New REG-NN prediction | §2 table | ~2min |
| Threshold tune (REG-T-NN value change) | §7 table | ~2min |
| CALENDAR event add/remove | §8 table | ~3min |
| BANK_EXPOSURE_MATRIX scoring change | §1 multi-channel score column | ~3min |
| New cohort pattern surfaced | §5 table | ~5min |

WALTER self-task on detection — read REGINALD STATUS at next dispatch session, diff against this cache, update as needed.

---

*v0.1 scaffold — shipped 2026-05-11 in REGINALD LIAISON Turn 4 close-cosign. Pattern lineage: design/CROSS_REFS/RED.md. v0.2 candidates: expand to include REGINALD VX-REG-NN counter-evidence vector summary (per RED CROSS_REFS §3 pattern) + recent-resolved-conf delta tracking when calibration cycle 1 fires.*
