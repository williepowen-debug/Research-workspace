# OFR Brief 26-02: mapping private credit's hidden counterparty web

**The Office of Financial Research's March 2026 brief provides the most granular government analysis to date of how private credit funds are financially intertwined with banks and institutional investors.** By uniquely combining two confidential regulatory datasets — SEC Form PF and Federal Reserve Y-14 — authors Ted Berg and Jung Hoon Lee estimate total bank and nonbank lending to private credit entities at **$410–$540 billion**, with an additional **$300 billion in uncalled capital commitments** from limited partners. Despite this scale, the brief's headline conclusion is cautiously reassuring: vulnerabilities appear "contained," bank loans to private credit carry favorable risk metrics, and most funds operate with little or no leverage. The brief was published on March 12, 2026 — just days before a cascade of redemption restrictions, SaaS-sector writedowns, and Morgan Stanley's 8% default-rate projection pushed private credit into the center of financial stability debates.

---

## The brief fills a critical data gap no one else could

OFR Brief 26-02 is authored by Ted Berg and Jung Hoon Lee of the OFR, published March 12, 2026. Its core innovation is integrating two confidential regulatory datasets that no prior study had combined:

**SEC Form PF** captures borrowings by private credit funds from all lender types — banks and nonbanks, domestic and foreign — but excludes business development companies (BDCs). **Federal Reserve FR Y-14** captures lending by the largest U.S. bank holding companies subject to stress testing (CCAR), including loans to both private funds and BDCs, but underrepresents foreign banks. By merging these sources, the OFR achieves what it calls "a more comprehensive view of the private credit ecosystem and its interconnections."

The data covers **year-end 2024** and focuses on the **U.S. market**, though Form PF captures borrowings from foreign lenders as well. The authors identified **over 2,000 private credit funds** in Form PF filings and **551 private credit funds plus 147 BDC borrowers** in Y-14. Identification was painstakingly manual: the team cross-referenced commercial databases (Preqin, PitchBook), keyword searches in regulatory filings, public pension fund annual comprehensive financial reports, and insurer statutory filings (Schedule B/A). As of year-end 2024, the U.S. private credit market including BDCs exceeds **$1.6 trillion** — Preqin data shows $1.217 trillion for private debt funds, PitchBook shows $420 billion for BDCs.

The brief explicitly acknowledges that "identifying private credit funds in regulatory data is challenging" because the process is "manual, resource intensive, and imperfect." Notably, "private credit" was not even a distinct strategy category on Form PF when it was adopted in 2011, and although the SEC approved amendments in February 2024 to add it, those changes had not yet taken effect at the time of publication.

---

## How the $410–540 billion exposure range is constructed

The $410–540 billion range is **not** a confidence interval or a stress scenario — it represents a **lower and upper bound** for actual borrowings based on different readings of the same Form PF data, combined additively with BDC borrowings.

**Form PF component ($215–$345 billion, private funds only):** Reported borrowings by identified private credit funds totaled approximately **$215 billion**. However, the authors discovered that for many funds, the difference between gross assets and net assets substantially exceeded reported borrowings — suggesting potential underreporting. Adjusting for these discrepancies pushes the figure to **$345 billion**. The brief cautions that the gap may include non-interest-bearing liabilities and that some advisers may report undrawn borrowings in gross assets. Form PF does not include full balance sheets, so there is no mechanism to reconcile these discrepancies.

**BDC component ($195 billion, all lender types):** Because BDCs are not subject to Form PF, their borrowings were estimated from SEC 10-Q and 10-K filings. This figure captures borrowing from both banks and nonbanks, including bonds and notes payable to institutional investors.

**Combined: $215B + $195B = $410B (lower bound); $345B + $195B = $540B (upper bound).**

The Y-14 data provides a separate, narrower lens. The largest U.S. banks report **$123 billion committed** to private credit obligors (including $30 billion to BDCs), of which **$74 billion was utilized** (including $16 billion to BDCs) — less than 5% of total C&I loans outstanding across these banks. The utilization ratio has historically fluctuated between **50% and 65%**. These exposures are a small share of the **$1.6 trillion in aggregate Tier 1 capital** held by the same banks.

The brief notes that actual BDC borrowings from banks are likely larger than Y-14 captures, because many BDCs borrow through **special purpose vehicles** (SPVs) with names that do not match the parent BDC — a significant identification gap.

Regarding creditor composition, **U.S. financial institutions provide approximately 80% of all lending** to private credit funds, with a more granular subset of Form PF data revealing that **global systemically important banks (G-SIBs) and other banking institutions** constitute the predominant funding sources. The brief does not name specific banks, but its Figure 4b (based on 109 Qualifying Hedge Funds identified as private credit) shows G-SIBs as the largest creditor category. The remaining 20% comes from foreign financial institutions.

---

## The $300 billion in uncalled capital and who owes it

Limited partners represent the second counterparty exposure channel. The brief estimates uncalled capital commitments at approximately **$300 billion** as of year-end 2024, with pension funds accounting for roughly **$100 billion** of these commitments. According to Figure 5a (net assets by investor type) and Figure 5b (uncalled capital by investor type), the primary investors in private credit funds include **pension funds, other investment funds, and insurance companies**. An "other" category encompasses foreign fund of funds, corporations, family offices, investment advisers, general partners, and employees.

The brief identifies two distinct risk amplification channels through LP relationships:

**Investment losses flow directly to LPs**, some of which are themselves leveraged. During downturns, leveraged LPs facing losses might be forced to liquidate unrelated assets to meet their own obligations — potentially triggering broader financial contagion. While a secondary market exists for trading LP interests, transactions would likely occur at **substantial discounts** to fund NAVs during stress.

**Capital call obligations create contingent liquidity risk.** LPs commit capital at fund inception but it is drawn down incrementally. In normal conditions this is manageable, but during protracted downturns, LPs may be forced to sell liquid assets (publicly traded stocks and bonds) to fund calls. The brief cites the 2007–08 financial crisis, when private fund capital calls created "severe liquidity strains for some very large private university endowments." LP default penalties can be "extremely punitive, potentially including forfeiture of the defaulting LP's entire prior capital contributions."

One mitigating factor unique to private credit (versus private equity): funds pay **regular periodic cash distributions** to LPs, so capital calls may be partially self-funding. However, during prolonged stress, cash distributions would decline due to loan defaults and a higher share of non-cash **payment-in-kind (PIK) distributions**.

The brief does not provide detailed concentration metrics on whether a few large LPs dominate, nor does it model stress scenarios quantifying what fraction of the $300 billion actually gets funded under stress.

---

## Bank loan characteristics reveal surprisingly favorable risk metrics

The Y-14 analysis of individual loan characteristics provides unique visibility into how banks underwrite private credit exposure:

- **86% of loans are secured** by first or second liens, with collateral frequently comprised of pools of individual corporate loans across various industries
- **41% are structured as five-year term loans**; the remainder consists primarily of revolving credit facilities
- **52% of loans are syndicated**, distributing risk across multiple institutions
- Only **21% meet regulatory classification criteria for "leveraged loans"** — suggesting banks maintain conservative underwriting standards
- All loans are **floating-rate**, minimizing banks' interest rate risk
- Median interest rate spreads above benchmark rates have remained relatively stable at **1.8% to 2.3%** since 2013

On credit risk, banks' internal assessments show a **12-month forward default probability averaging 1.3%** (equal-weighted), significantly lower than non-private credit loan categories. The diversified collateral pools may explain this. **Loss given default has averaged 32%**, with gradual improvement over time. When value-weighted, metrics are even more favorable: in 2021, value-weighted DP was 1.2% and LGD was 21%, suggesting larger loans carry lower risk profiles. However, during the COVID-19 pandemic, default probabilities escalated significantly — a reminder that these metrics are cyclically sensitive.

The brief notes that while loan-to-value ratios cannot be directly observed in confidential data, lending exposures are understood to be "often significantly overcollateralized to account for the riskiness of the underlying portfolio loans."

---

## What the brief says — and does not say — about systemic risk

The brief's conclusion is deliberately measured: vulnerabilities "appear contained" but "warrant continued monitoring given the sector's rapid growth and evolving interconnections." It does **not** provide explicit regulatory recommendations, stress testing proposals, or legislative requests. This restraint is consistent with the standard OFR disclaimer that "the views and opinions expressed are those of the authors and do not necessarily represent official positions or policy of the OFR."

The risk channels the brief identifies, whether explicitly or implicitly, include: direct credit loss on loans to private credit entities; liquidity risk and fire-sale dynamics if leveraged LPs must sell assets to meet capital calls; counterparty contagion if defaults at highly leveraged tail funds (the 95th percentile and above, representing **$81 billion or ~23% of estimated private fund borrowing**, with leverage ratios exceeding 3.5x) transmit stress to bank creditors; and the procyclical nature of capital call obligations.

The brief notably does **not** address: valuation opacity and mark-to-model risk in detail; rating inflation or NRSRO conflicts; the PE-insurer channel (fund manager → captive insurer → FHLB borrowing); offshore vehicle structures in Bermuda or Cayman; insurer-to-reinsurer risk transfers; inter-fund lending within the same PE platform; or circular bank exposures where a bank lends to a fund that invests in a company that also has facilities from the same bank. These omissions are largely data-driven — the authors work with what Form PF and Y-14 can see, and explicitly flag the remaining opacity.

---

## How OFR's estimates compare with the broader landscape

The gap between OFR's **$123 billion Y-14 bank commitment figure** and the wider market is striking but explicable. A structured comparison table in Figure 1 of the brief itself shows how prior estimates range from under $100 billion to over $500 billion:

| Source | Committed | Drawn | Period | Notes |
|--------|-----------|-------|--------|-------|
| **Moody's** (32-bank global survey) | $525B | N/A | 2023 | Highest; includes global banks |
| **Call reports** | $400B | $264B | 2024 | Broader "business credit intermediaries" |
| **Temple/Penn State** (Jang & Rosen) | $372B | N/A | 2023 | Includes BDCs |
| **Fed FSR** (May 2023) | $200B | N/A | 2021 | Excludes BDCs |
| **Fed FEDS Notes** (Berrospide et al.) | $95B | $56B | 2024 | Includes BDCs |

The OFR attributes divergence to inconsistent definitions of private credit, treatment of foreign lenders, committed-versus-utilized distinctions, BDC inclusion, and SPV identification challenges. The BIS (March 2025) estimates global private credit AUM at over **$2.5 trillion**; the FSB cites approximately **$2 trillion** globally. These total-market figures dwarf the OFR's bank exposure figures because they represent total assets under management — equity capital, unrealized gains, and dry powder — not just the lending/leverage channel.

Morgan Stanley's Joyce Jiang, publishing just four days after OFR Brief 26-02 on March 16, 2026, projected private credit default rates reaching **8%** — driven by AI disruption in software (estimated at 26% of BDC portfolios). This sharply contrasts with the **1.3% average 12-month forward default probability** banks report in Y-14. The gap likely reflects banks' assessment of their own senior, secured, overcollateralized exposure versus the default rate on underlying portfolio company loans. Fitch reported the U.S. private credit default rate had already reached **5.8%** as of January 2026. Goldman Sachs's Alex Blostein projected retail private credit fund **net outflows through 2026 and likely 2027**, with gross sales running approximately 50% below 2025 levels.

---

## Immediate policy ripple effects and institutional citations

OFR Brief 26-02 landed during an acute stress period for private credit. Within weeks of publication, multiple major funds imposed redemption restrictions — Blackstone ($82B fund, 7.9% redemptions vs. 5% cap), BlackRock/HPS ($26B, 9.3% vs. 5%), Apollo ($15.1B, 11.2% vs. 5%), Ares ($10.7B, 11.6% vs. 5%), Morgan Stanley ($7.6B, 10.9% vs. 5%), and Cliffwater ($33B, 14% vs. 7%). This wave prompted direct congressional attention.

The Congressional Research Service cited the brief directly in **CRS Insight IN12674** ("Private Credit Funds Redemption Restrictions: Market Context and Policy Issues," March 27, 2026), reproducing Figure 4b showing G-SIB lending dominance and characterizing the OFR study as evidence that "some rely on bank funding, creating potential spillover channels to the broader financial system." Senator Elizabeth Warren issued a statement on private credit turmoil cited in the CRS report.

The **FSOC met on March 25, 2026** — 13 days after the brief's publication — and its readout noted discussion of "recent developments in the private credit sector." The Council simultaneously published proposed interpretive guidance on nonbank financial company designations. While the readout does not name OFR Brief 26-02 explicitly, the OFR directly supports FSOC's analytical work, making it virtually certain the findings were briefed to Council members.

**Fed Chair Powell**, speaking at Harvard on March 31, 2026, stated the Fed is watching the private credit market "super carefully." Capital Advisors Group published a detailed analysis on April 1, 2026, calling the OFR report "one of the most comprehensive views of private credit counterparty exposure to date." Bloomberg published at least seven articles on private credit stress between March 17–April 1, 2026, though paywall restrictions prevent confirming direct citations. No dedicated OFR press release, staff testimony, or academic citations have appeared yet — consistent with the brief's recent publication date.

---

## Significant data gaps the OFR itself acknowledges

The brief is commendably transparent about what it cannot see. Key acknowledged gaps include:

Form PF does not include full balance sheets, so discrepancies between gross assets minus net assets and reported borrowings **cannot be reconciled**. Counterparty subtypes are not reported in Form PF — the OFR staff had to manually categorize creditors from the limited data available in Question 47 filings, which cover only the 109 Qualifying Hedge Funds identified as private credit (most private credit funds are not QHFs). The amended Form PF adding "private credit" as a reporting category had not yet taken effect. BDC borrowings via SPVs with names different from the parent entity are systematically missed in Y-14 data. Conflicting classifications between regulatory sources and commercial databases created "ambiguity regarding the appropriate categorization" of some funds, and some entities invest across multiple asset classes.

Critically, the brief does **not** address several risk channels the user asked about: offshore vehicle opacity (Bermuda, Cayman structures), insurer-to-reinsurer transfers (Athene, Global Atlantic, F&G, Everlake-type structures), inter-fund lending within the same PE platform, BDC exposure to affiliated credit funds, or the circular bank-fund-company exposure chain. These gaps reflect the fundamental limitation of Form PF and Y-14 — they see what regulated entities report through structured fields, not the full web of arrangements that characterize modern private credit. The FSB, IMF, and ECB have all separately identified these same data gaps as priorities for international regulatory coordination, with the FSB establishing a Nonbank Data Task Force in its 2026 work plan specifically to address them.

---

## Conclusion

OFR Brief 26-02 establishes an important empirical baseline: direct bank exposure to private credit, at $123 billion committed through Y-14 banks, represents less than 8% of the $1.6 trillion U.S. market and a fraction of banks' $1.6 trillion Tier 1 capital. The broader $410–540 billion lending estimate, while larger, still carries favorable credit characteristics — 86% secured, low default probabilities, conservative leverage at the median. These findings validate the "not yet systemic" thesis.

The brief's deeper value lies in what it reveals at the margins. The **95th-percentile leverage tail** — funds with leverage above 3.5x accounting for $81 billion in borrowing — represents a concentrated pocket of risk. The **$300 billion in uncalled capital** creates a procyclical liquidity channel that stress-tested poorly during 2007–08. And the systematic identification challenges — SPV obfuscation, missing BDC borrowings, conflicting classifications — suggest the true exposure is likely higher than any single dataset captures. The brief arrived at a moment when its carefully qualified reassurance was immediately tested by redemption waves, software-sector writedowns, and projections of 8% default rates. It is a foundational document for the regulatory debate over private credit's place in the financial system — not because it sounds an alarm, but because it establishes what the government can actually measure and, perhaps more importantly, what it still cannot.