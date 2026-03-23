# OZK Folder Audit Report
**Date:** 2026-03-23 | **Auditor:** OZK Research Analyst (subagent)
**Purpose:** Pre-earnings integrity check before April 16, 2026

---

## 1. INCONSISTENCIES

### 1a. CRE Concentration — Three Different Numbers

| File | CRE/Tier 1 | CRE/Tangible Equity |
|------|-----------|---------------------|
| THESIS.md | — | **455% of tangible equity** |
| EVIDENCE.md (Capital Ratios) | **415%** | — |
| Temple 8 | — | **455% of tangible equity** |
| OZK_THESIS_FEB25.md | **415%** (Tier 1) | — |
| KBRA (cited in THESIS.md) | **358%** | — |

**Problem:** 455% and 415% are used interchangeably across files but refer to different denominators (tangible equity vs Tier 1 capital). KBRA's 358% is a third number. None of the files explicitly reconcile these three figures or state the denominator clearly. A skeptical reader would see "455%... 415%... 358%" and wonder which is real.

**Fix needed:** Add a reconciliation note. 415% = CRE/Tier 1 (10-K Dec 2024). 455% = CRE/tangible equity (Temple 8, likely using a different CRE definition or more recent data). 358% = KBRA's calculation (likely different scope). State the date and methodology for each.

### 1b. Unfunded Commitments — $19.08B vs $10.6B vs $18B

| File | Unfunded Figure |
|------|----------------|
| 10K_ANALYSIS_2024.md | **$19.08B** (from 10-K directly) |
| OZK_THESIS_FEB25.md | **$10.6B** ("Total Unused Commitments") |
| Temple 8 (behind paywall) | **$18B** |
| EVIDENCE.md | **$19.08B** |
| THESIS.md | **$19.08B** |
| 10-K geographic table | Unfunded = **$14.3B** (RESG geographic only) |

**Problem:** The Feb thesis uses $10.6B; every other file uses $19.08B. These are likely different measures (unused commitments vs total unfunded loan balances), but the discrepancy is never explained. The geographic table shows $14.3B unfunded for just real estate. The "~900% of Tier 1" figure in THESIS.md presumably uses $19.08B, but OZK_THESIS_FEB25.md calculates "~680%" using $10.6B. Both can't be the authoritative number.

**Fix needed:** Clarify which figure is which. $19.08B = total unfunded on closed loans (10-K Schedule RC-L equivalent). $14.3B = RESG geographic unfunded. $10.6B = likely a different call report line (unused commitments to lend). Reconcile or retire the $10.6B figure.

### 1c. Life Sciences Exposure — $3.2B vs $1.85B

| File | Life Sciences Total |
|------|-------------------|
| THESIS.md, Temple 8 | **$3.2B** (~10% of RESG) |
| 10K_ANALYSIS_2024.md | Stabilized $997M + Construction $851M = **$1.85B** |

**Problem:** $3.2B is cited repeatedly as the life sciences exposure, but the 10-K data extraction only shows $1.85B. The gap is $1.35B. Possible explanations: (a) $3.2B includes unfunded commitments, (b) $3.2B includes loans classified outside "Life Science" (e.g., office-medical hybrids), (c) Temple 8's number is wrong. This is never reconciled.

**Fix needed:** Source the $3.2B figure explicitly or revise to $1.85B (funded only from 10-K).

### 1d. ACL Ending Balance — $619M vs $632M

| File | ACL End of 2024/2025 |
|------|---------------------|
| 10K_ANALYSIS_2024.md | ACL ending 2024: **$619,360K** |
| THESIS.md, Temple 8 | ACL Q4 2025: **$632M** (declined from $680M peak Q3 2025) |

**Not technically a conflict** — these are different periods (FY2024 vs Q4 2025). But the narrative flow is confusing. The 10-K analysis covers Dec 2024; the Temple 8 / THESIS data covers Dec 2025. A reader could easily conflate them. The folder never presents a clean ACL bridge from $619M (Dec 2024) → peaked $680M (Sep 2025) → $632M (Dec 2025).

**Fix needed:** Add an explicit ACL timeline somewhere (EVIDENCE.md or THESIS.md).

### 1e. NCO Rate — 0.20% vs 1.18%

| File | NCO Rate | Period |
|------|----------|--------|
| 10K_ANALYSIS_2024.md | **0.20%** | FY 2024 |
| THESIS.md, Temple 8 | **1.18%** | Q4 2025 annualized |

**Same issue as 1d** — different periods, not a true conflict, but the juxtaposition is jarring and never bridged. The Feb thesis (OZK_THESIS_FEB25.md) references an NCO rate of 0.17% which appears to be a pre-earnings estimate that was then superseded.

### 1f. Construction Reserve Rate — Two Figures

| File | Construction ACL | Reserve Rate |
|------|-----------------|-------------|
| 10K_ANALYSIS_2024.md | $85,183K → $139,483K? | **0.89%** |
| 10K_ANALYSIS_2024.md (ACL Movement) | $235,845 (2023) → **$139,483** (2024) | -41% |
| EVIDENCE.md | — | **0.89%** |

**Problem:** The 10-K analysis says construction ACL was $235,845K in 2023 and $139,483K in 2024 (a 41% cut). But the reserve rate table shows construction reserve rate of 0.89% based on $85,183K ACL. These two numbers ($139,483K and $85,183K) both appear in the same file for construction ACL in 2024. Likely one is the specific reserve and the other is total (specific + general), but this is unclear and potentially a data extraction error.

**Fix needed:** Verify which number is the correct construction-specific ACL at Dec 2024 and reconcile.

### 1g. Total Office Exposure

| File | Office Total |
|------|-------------|
| 10K_ANALYSIS_2024.md | Stabilized $3,395M + Construction $481M = **$3,876M** |
| EVIDENCE.md | **$3.88B** |

This is consistent ✓ — just noting alignment.

---

## 2. GAPS

### 2a. No Q4 2025 10-Q / Earnings Data Extracted

The folder has the **FY 2024 10-K** and **Temple 8's Q4 2025 summary**, but there's no primary-source extraction of OZK's Q4 2025 earnings release or 10-Q. All Q4 2025 data (the $98.3M charge-offs, $632M ACL, 1.18% NCO rate, 54.4% RESG share, record EPS $6.18) comes secondhand via Temple 8. For a folder that aims to be "airtight," the actual Q4 2025 earnings release / 10-Q should be sourced directly.

**Priority: HIGH.** This is the most recent quarterly data and forms the baseline for the April 16 comparison.

### 2b. IQHQ RaDD — Critical Loan, Thin Sourcing

The $915M IQHQ RaDD loan is described as "the whale" and the August catalyst, but:
- No primary source for the $555M funded figure
- No source for Cole's $500M valuation estimate (who is Cole? Cole Credit Property Trust? An analyst?)
- No leasing data (the file just says "zero major tenants")
- No source for the maturity date (Aug 2026) — is this from the 10-K, an analyst, or Temple 8?
- No CoStar/CBRE vacancy data for the specific submarket

**Priority: CRITICAL.** If IQHQ is the thesis climax, it needs ironclad sourcing.

### 2c. "Extend-and-Pretend" — Asserted But Not Proven at Institution Level

The FDIC geographic data shows district-level PDNA-NCO gaps, but these are aggregate numbers for all banks in each district. The thesis asserts OZK specifically is engaging in extend-and-pretend, but the only OZK-specific evidence is:
- Pacific Center sold (one data point)
- Management language ("working with sponsors")
- ACL cuts while losses rose

There's no OZK-level TDR (troubled debt restructuring) data, no specific loan modification counts, no maturity extension disclosures. The 10-K may contain TDR data that wasn't extracted.

**Priority: MEDIUM.** The inference is reasonable but could be strengthened with 10-K TDR disclosures.

### 2d. Short Interest Data — No Source, No Date

THESIS.md states short interest is 14-15% with 12-18 days to cover. No source, no date. Short interest changes biweekly. This could be months old.

**Priority: LOW** (not thesis-critical, but relevant for position sizing).

### 2e. KBRA Negative Outlook — No Report Accessed

KBRA's Negative outlook is cited multiple times but the actual report isn't in `sources/`. The specific CRE figures KBRA uses (358%, 197%) differ from the 10-K figures, suggesting different methodology. Without the report, we can't verify or explain the discrepancy.

### 2f. Peer Comparison — Incomplete

The peer table (Huntington, Truist, "regional peer avg") has only two named peers. For a robust comparison:
- Missing: ZION, WAL, COLB, FNB, or other CRE-heavy regionals
- No source for peer ACL ratios (which quarter? which filing?)
- "Regional peer avg 1.75-2.05%" is a range with no named constituents

### 2g. Bull Case — No Quantified Probability

The bull rebuttals are qualitative. A PM would want to see: "What's the probability the thesis is wrong? What does OZK look like if IQHQ gets a tenant? What if construction stabilization rates are 60%+? What's the stock worth in the bull case?" There's no scenario analysis or target price framework.

### 2h. RC-C Data — Still Empty

EARNINGS_PREP.md has a placeholder table for RC-C state-level noncurrent rates. This is flagged in the research agenda but unfilled. It's the single most important data gap for the institutional-level thesis.

### 2i. Dividend History / Payout Ratio

Temple 8 mentions a "dividend kill switch" behind the paywall. The folder has no dividend data, payout ratio, or analysis of whether the 62-quarter streak is at risk. This would matter to a PM.

### 2j. Management Track Record / Gleason Bio

The bull case centers on "Gleason has never lost." The rebuttal is "never faced this environment." But there's no actual data on Gleason's track record through prior cycles (GFC, 2015-16 energy, COVID). A PM who knows Gleason would push back hard here.

---

## 3. STALE DATA

| Item | Date | Staleness | Refresh Priority |
|------|------|-----------|-----------------|
| **10-K data** | Dec 31, 2024 | **15 months old** | HIGH — Q4 2025 10-Q needed |
| **Insider scan** | Through Feb 24, 2026 | 1 month old | MEDIUM — check for Mar activity |
| **FDIC QBP** | Q4 2025 | Current | ✅ |
| **Temple 8 thesis** | March 2026 | Current | ✅ |
| **OZK_THESIS_FEB25.md** | Feb 25, 2026 | Superseded by newer files | LOW — archival only |
| **Stock price** | ~$49 (STATUS.md) | Needs daily refresh pre-earnings | LOW |
| **Short interest** | Undated | Unknown | MEDIUM |
| **IQHQ leasing status** | Unknown | Could be months old | **CRITICAL** |
| **Life sciences vacancy** | "35%" (no date) | Could be Q3 2025 or older | HIGH |
| **Peer ACL/NCO ratios** | Undated | Unknown quarter | MEDIUM |

### Most Critical Pre-Earnings Refreshes (from Research Agenda)
1. **RC-C Call Report** — institution-level noncurrent data (fills Gap 2h)
2. **IQHQ leasing updates** — any tenant activity (fills Gap 2b)
3. **8-K EDGAR watch** — already scheduled for Mar 25
4. **Life sciences vacancy Q1** — San Diego, Boston, Chicago
5. **Insider filings since Feb 24** — especially CRO Majumdar

---

## 4. STRENGTHS

### 4a. ACL-NCO Inversion — Airtight
The core mechanic (ACL 1.16% < NCO 1.18% = coverage <1.0x) is clearly sourced from Temple 8, internally consistent, and the peer comparison is devastating. This is the strongest single data point in the folder. A PM can verify it in 5 minutes from public filings.

### 4b. CRE Concentration — Undeniable
455% of tangible equity (or 415% of Tier 1 — both above 300% regulatory guidance) is a fact. The construction/Tier 1 at 142% vs 100% threshold is a fact. The unfunded commitment overhang is a fact from the 10-K. The denominator confusion (§1a) needs fixing, but the directional conclusion is bulletproof.

### 4c. Insider Activity — Compelling
CRO selling discretionarily (not under 10b5-1) while the bank cuts reserves is a genuinely strong signal. Zero insider buying during a 15%+ drawdown reinforces. This section is well-sourced with dates, amounts, and percentages.

### 4d. Geographic FDIC Analysis — Novel
Mapping OZK's loan book to district-level stress data (NY pipeline, Atlanta noncurrent, Dallas E&P gap) is original analytical work that adds value beyond what Temple 8 or sell-side provides. The "OZK is counted in Dallas but lends in NY/Atlanta" insight is non-obvious and important.

### 4e. Three-Wave Structure — Clear and Tradeable
The catalyst timeline (Atlanta now → NY Q2 → IQHQ Aug) maps cleanly to the position structure ($42.5P May → $45P Aug). This is what a PM wants: a falsifiable sequence with defined checkpoints.

### 4f. 10-K Data Extraction — Thorough
The 10K_ANALYSIS_2024.md is a genuinely comprehensive extraction: loan composition, geographic detail, property type breakdowns, NPAs, charge-offs, ACL activity, reserve rates, unfunded commitments, deposits, liquidity, rate sensitivity, capital ratios. It's the backbone of the evidence base.

---

## 5. OVERALL ASSESSMENT

### What Would Convince a Skeptical PM

1. **The math is real.** ACL < NCO is not an opinion. CRE concentration above regulatory thresholds is not an opinion. $19B unfunded > $14B liquidity is not an opinion. The numerical core of the thesis is verifiable from public filings.

2. **The catalyst structure is clear.** April 16 earnings → Q2 pipeline conversion → August IQHQ maturity. Each wave has a defined trigger and a binary outcome. This is tradeable.

3. **The insider signal is strong.** CRO selling discretionarily while cutting reserves is the kind of signal that makes people lean forward.

4. **The FDIC geographic work is differentiated.** Most short sellers are looking at OZK's reported numbers. The district-level mismatch (HQ vs. loan origination geography) is an edge.

### What Would Make a PM Push Back

1. **"Where's the Q4 2025 10-Q?"** The folder's primary data source is a Dec 2024 10-K. All Q4 2025 numbers come from a third-party short thesis (Temple 8). For a position this sized, you need to own the primary data. This is the single biggest credibility gap.

2. **"Your whale has no sourcing."** IQHQ is positioned as the thesis climax, but the $555M funded, $500M valuation, "zero tenants," and Aug 2026 maturity all lack primary sources. If challenged on any of these, the response is "Temple 8 said so." That's not good enough for a concentrated short.

3. **"What's your loss scenario?"** There's no explicit P&L framework. What's the stock worth if ACL is rebuilt? What's it worth if IQHQ gets a tenant? What's the downside to the short if Gleason pulls off another quarter of extend-and-pretend? No scenario analysis, no target price, no position sizing rationale beyond "size accordingly."

4. **"Crowded trade."** 14-15% short interest with 12-18 days to cover. The folder acknowledges this but hand-waves it ("squeezes are temporary"). A PM would want to know: what's the max drawdown tolerance? What's the cover trigger? What does a squeeze to $60+ do to the position?

5. **"The 10-K is 15 months old."** Construction reserve rates, unfunded commitments, geographic concentrations — all from Dec 2024. A lot can change in 15 months, especially for a bank actively managing down CRE exposure.

6. **"You're conflating denominators."** The 455% / 415% / 358% / 900% CRE concentration numbers come from different sources with different methodologies. This looks sloppy, even if each number is individually correct.

### Bottom Line

The thesis is **directionally strong** with a **well-defined catalyst structure**. The core mechanics (ACL inversion, CRE concentration, insider selling) are robust. But the folder has a **sourcing problem at the thesis climax** (IQHQ) and a **data freshness problem** (10-K is Dec 2024, no Q4 2025 primary extraction). It reads like a B+ research folder trying to support an A-conviction position.

**To make it airtight before April 16:**
1. Pull and extract OZK's Q4 2025 earnings release / 10-Q (primary source for all the Temple 8 numbers)
2. Source IQHQ independently (CoStar, CBRE San Diego, 10-K/Q disclosures, SEC filings)
3. Reconcile the CRE concentration denominators in one clean table
4. Fill the RC-C data (institution-level noncurrents)
5. Add a scenario analysis with explicit stock targets (bull/base/bear)
6. Resolve the $3.2B vs $1.85B life sciences gap
7. Resolve the construction ACL discrepancy ($85M vs $139M)

---

*Generated 2026-03-23 by OZK audit subagent. This report should be re-run after the pre-earnings research agenda items are completed.*
