# OFR Brief 26-02: Mapping Private Credit's Hidden Counterparty Web

**Source:** Office of Financial Research (OFR), March 12, 2026  
**Authors:** Ted Berg and Jung Hoon Lee  
**Classification:** Regulatory research — private credit counterparty exposure  
**Coverage:** Year-end 2024 data, U.S. market focus

---

## Executive Summary

OFR Brief 26-02 provides the most granular government analysis to date of how private credit funds are financially intertwined with banks and institutional investors. By uniquely combining **SEC Form PF** and **Federal Reserve Y-14** data, the authors estimate:

- **$410–540 billion** in bank and nonbank lending to private credit entities
- **$300 billion** in uncalled capital commitments from limited partners
- **$123 billion** committed by largest U.S. banks (Y-14), of which **$74 billion utilized**

**Headline conclusion:** Vulnerabilities appear "contained" — but the brief landed just days before redemption restrictions, SaaS writedowns, and Morgan Stanley's 8% default projection pushed private credit into financial stability debates.

---

## Data Innovation: Merging Two Confidential Datasets

**SEC Form PF:** Captures borrowings by private credit funds from all lender types (banks/nonbanks, domestic/foreign), excludes BDCs.  
**Federal Reserve FR Y-14:** Captures lending by largest U.S. bank holding companies (CCAR), includes private funds and BDCs, underrepresents foreign banks.

**Coverage:**
- **2,000+ private credit funds** identified in Form PF
- **551 private credit funds + 147 BDC borrowers** in Y-14
- **Manual identification** via Preqin, PitchBook, pension fund reports, insurer statutory filings

**Note:** "Private credit" was not a distinct strategy category on Form PF when adopted in 2011. SEC approved amendments in February 2024, but changes had not yet taken effect at publication.

---

## The $410–540 Billion Exposure Range

| Component | Lower Bound | Upper Bound | Notes |
|-----------|:-----------:|:-----------:|:------|
| **Form PF (private funds)** | $215B | $345B | Upper bound adjusts for gross/net asset discrepancies suggesting underreporting |
| **BDC borrowings** | $195B | $195B | From SEC 10-Q/10-K (BDCs not in Form PF) |
| **TOTAL** | **$410B** | **$540B** | Not a confidence interval — represents data reconciliation bounds |

**Y-14 narrower lens:** $123 billion committed ($74B utilized) — less than 5% of total C&I loans. Utilization ratio historically 50-65%.

**Creditor composition:** U.S. financial institutions provide ~80% of all lending; G-SIBs are predominant funding sources per Figure 4b.

---

## The $300 Billion Uncalled Capital Channel

**LP commitments:** ~$300 billion (pension funds = ~$100B)

**Primary investors:** Pension funds, other investment funds, insurance companies

**Risk amplification mechanisms:**
1. **Investment losses flow directly to LPs** — leveraged LPs may be forced to liquidate unrelated assets during downturns
2. **Capital call obligations create contingent liquidity risk** — LPs may need to sell liquid assets (public stocks/bonds) to fund calls during stress

**Historical parallel:** 2007-08 crisis — private fund capital calls created "severe liquidity strains for some very large private university endowments"

**Mitigating factor:** Private credit funds pay regular periodic cash distributions (unlike private equity), so capital calls may be partially self-funding. But during stress, distributions decline due to defaults and higher PIK shares.

---

## Bank Loan Characteristics: Favorable Risk Metrics

| Metric | Value | Notes |
|--------|:-----:|:------|
| Secured loans | **86%** | First or second liens, collateral = pools of corporate loans |
| 5-year term loans | **41%** | Remainder primarily revolving credit facilities |
| Syndicated | **52%** | Risk distributed across multiple institutions |
| "Leveraged loan" classification | **21%** | Suggests conservative underwriting |
| Interest rate structure | **Floating-rate** | Minimizes bank interest rate risk |
| Median spread above benchmark | **1.8–2.3%** | Stable since 2013 |
| 12-month forward default probability | **1.3%** | Equal-weighted; significantly lower than non-PC loan categories |
| Loss given default | **32%** | Gradual improvement over time; value-weighted = 21% |

**Caveat:** Metrics are cyclically sensitive. COVID-19 pandemic saw significant default probability escalation.

---

## Systemic Risk Assessment

**Official conclusion:** Vulnerabilities "appear contained" but "warrant continued monitoring given the sector's rapid growth and evolving interconnections."

**What the brief identifies:**
- Direct credit loss on loans to PC entities
- Liquidity risk/fire-sale dynamics if leveraged LPs must sell assets
- Counterparty contagion from highly leveraged tail funds (95th percentile)
- Procyclical nature of capital call obligations

**What the brief does NOT address (data gaps):**
- Valuation opacity and mark-to-model risk
- Rating inflation/NRSRO conflicts
- **PE-insurer channel** (fund manager → captive insurer → FHLB borrowing)
- **Offshore vehicle structures** (Bermuda, Cayman)
- Insurer-to-reinsurer risk transfers
- Inter-fund lending within same PE platform
- Circular bank exposures (bank lends to fund → fund invests in company → company has facilities from same bank)

---

## The 95th Percentile Leverage Tail

**Critical finding:** Funds with leverage above 3.5x represent:
- **$81 billion in borrowing** (~23% of estimated private fund borrowing)
- Concentrated pocket of risk at the margin

**Median leverage:** Much lower (conservative underwriting standards)

---

## Comparison with Other Estimates

| Source | Committed | Period | Notes |
|--------|:---------:|:------:|:------|
| **Moody's** (32-bank global) | $525B | 2023 | Highest; includes global banks |
| **Call reports** | $400B | 2024 | Broader "business credit intermediaries" |
| **Temple/Penn State** | $372B | 2023 | Includes BDCs |
| **Fed FSR** | $200B | 2021 | Excludes BDCs |
| **Fed FEDS Notes** | $95B | 2024 | Includes BDCs |
| **OFR Brief 26-02** | $123B (Y-14) / $410-540B (full) | 2024 | Most comprehensive U.S. view |

**Global context:** BIS estimates $2.5T global PC AUM; FSB cites ~$2T. These dwarf OFR bank exposure figures because they represent total AUM (equity, unrealized gains, dry powder), not just lending/leverage.

---

## Immediate Policy Ripple Effects

**Publication date:** March 12, 2026

**Within weeks:**
- Blackstone ($82B, 7.9% vs 5% cap), BlackRock/HPS ($26B, 9.3%), Apollo ($15.1B, 11.2%), Ares ($10.7B, 11.6%), Morgan Stanley ($7.6B, 10.9%), Cliffwater ($33B, 14%) — all imposed redemption restrictions

**Congressional response:**
- **CRS Insight IN12674** (March 27, 2026): Cited OFR brief directly, reproduced Figure 4b (G-SIB lending dominance)
- Senator Elizabeth Warren statement on PC turmoil

**FSOC:** Met March 25, 2026 — discussed "recent developments in private credit sector"; published proposed guidance on nonbank financial company designations

**Fed Chair Powell** (March 31, 2026): Fed watching PC market "super carefully"

**Contrasting data points:**
- Morgan Stanley Joyce Jiang (March 16, 2026): Projected **8% default rates** (vs banks' 1.3% forward probability)
- Fitch (January 2026): U.S. PC default rate already at **5.8%**
- Goldman Sachs Alex Blostein: Projected retail PC fund **net outflows through 2026-2027**, gross sales ~50% below 2025 levels

**Gap explanation:** Banks assess senior secured overcollateralized exposure; Morgan Stanley/Fitch assess underlying portfolio company loans.

---

## Key Data Gaps Acknowledged by OFR

1. **Form PF lacks full balance sheets** — discrepancies between gross/net assets and reported borrowings cannot be reconciled
2. **Counterparty subtypes not reported** — manual categorization required from limited Question 47 data
3. **Amended Form PF** (adding "private credit" category) not yet effective
4. **BDC SPVs systematically missed** — borrowings via vehicles with different names from parent BDC
5. **Conflicting classifications** between regulatory sources and commercial databases

**International coordination:** FSB, IMF, ECB have identified same gaps as priorities. FSB established Nonbank Data Task Force in 2026 work plan.

---

## Significance for Thesis

**Validates:**
- PC scale ($1.6T U.S. market) is systemically relevant
- Bank exposure ($123B committed) is manageable relative to $1.6T Tier 1 capital
- **But** tail risk (95th percentile leverage, $81B) is concentrated
- LP capital call channel ($300B) creates procyclical liquidity risk
- Data gaps (PE-insurer, offshore, inter-fund) mean true exposure > measured exposure

**Contradicts/Complicates:**
- OFR says "contained" — but published days before crisis accelerated
- Banks report 1.3% default probability vs Fitch 5.8% actual / Morgan Stanley 8% projected
- "Flying blind" admission (Senator Reed letter Mar 24) despite OFR report

**Implication:** The brief establishes empirical baseline but immediately tested by events. The "contained" conclusion was overtaken by redemption waves within weeks. This supports Stage 3→Stage 4 transition thesis (gates → financing tighten → honest marks → spillover).

---

## Files / Cross-References

- Related: `AGENTS/BROCK/inbox/processed/SIG-BROCK-20260331-treasury-fsoc-pc-investigation.md` (Senator Reed OFR letter)
- Related: `AGENTS/BROCK/STATUS.md` (Stage 5 regulatory cascade)
- Related: `AGENTS/SHADE/` (PE-insurer channel — gap in OFR data)
- Related: `MEMORY.md` (PC Contagion Mechanics)

---

*Captured: April 5, 2026*  
*Source: User research document — OFR Brief 26-02 analysis*
