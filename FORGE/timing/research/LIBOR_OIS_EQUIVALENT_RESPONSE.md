# After LIBOR: mapping counterparty risk in broken plumbing

**No single indicator replaces LIBOR-OIS as the counterparty risk signal — and that gap itself is the most dangerous feature of the post-LIBOR landscape.** The transition to SOFR deliberately stripped credit risk from the reference rate, scattering the information LIBOR-OIS once contained across a half-dozen imperfect proxies. The best practical composite today is a dashboard combining the AA financial commercial paper–T-bill spread (unsecured bank credit risk), bank CDS indices (direct default pricing), and the SOFR-IORB spread (reserve scarcity/plumbing stress). Meanwhile, the private credit fund gating crisis — with 12+ funds restricting withdrawals on a $222 billion retail base, JPMorgan marking down collateral, and Treasury convening emergency insurance regulator meetings on March 30, 2026 — is structurally the closest parallel to BNP Paribas's August 9, 2007 fund freeze in nearly two decades. The system enters March 31 quarter-end with reserves at a 4-year low, zero RRP buffer, escalating Standing Repo Facility usage, and reserve ampleness indicators that the NY Fed's Roberto Perli acknowledged on March 26 have "approached levels seen in Q1 2019" — the quarter before the September 2019 repo crisis.

---

## The ranked replacements for LIBOR-OIS

LIBOR-OIS worked because it captured both credit risk (LIBOR = unsecured interbank rate) and liquidity risk (the spread over the risk-free OIS rate) in a single number. SOFR is a secured overnight Treasury repo rate — it contains essentially zero credit risk. This means the old signal has fractured into components that must be monitored together.

**Rank 1: AA Financial CP – T-Bill spread.** This is the most practical single-indicator replacement. Commercial paper rates represent actual unsecured borrowing costs for financial institutions, directly analogous to what LIBOR measured. The OFR has incorporated 3-month AA Financial CP rates into its Financial Stress Index as the LIBOR replacement. Current levels sit around **10–25 bps**. The watch level is **50–100 bps**; alarm is **150+ bps**. During the GFC, the equivalent TED spread (LIBOR minus T-bills) hit **300+ bps** and the CP market froze entirely, requiring the Fed's CP Funding Facility. Limitation: in severe stress, the CP market can seize completely, making the spread less meaningful at exactly the moment it matters most.

**Rank 2: Bank CDS index spreads (iTraxx Senior Financials, CDX.NA.IG).** These directly price bank default risk and are the purest counterparty risk signal available. San Francisco Fed research found CDS spreads explained **~44% of the variation in LIBOR-OIS** during 2007-08 (the other 56% was liquidity premium). Normal G-SIB 5-year CDS sits at **40–60 bps**; watch level is **100 bps**; alarm is **200+ bps**. Lehman traded at **~700 bps** days before failure; Credit Suisse hit **1,000+ bps** before its absorption by UBS. Limitation: CDS markets are illiquid — only about 13 counterparties are active daily in single-name EU G-SIB CDS versus 160 for index CDS — and can reflect microstructure rather than fundamentals.

**Rank 3: SOFR + AXI (Across-the-Curve Credit Spread Index).** Designed by Stanford's Darrell Duffie, AXI measures the weighted-average credit spread of unsecured wholesale bank funding across all maturities. It is the theoretically correct answer — purpose-built to restore the credit component SOFR lacks, transaction-based, and volume-weighted across **~$463 billion/day** in underlying transactions. During COVID onset, SOFR+AXI tracked actual unsecured funding costs while pure SOFR fell. **Major caveat: near-zero market adoption.** Bloomberg's alternative (BSBY) was discontinued in late 2024 after IOSCO concerns. Until AXI is embedded in contracts and trading, it remains a monitoring tool.

**Rank 4: FRA-OIS spread.** Pre-June 2023, this was widely cited as the gold-standard LIBOR-OIS successor. The Fed's own FEDS 2015-091 paper modeled it in three regimes: normal (**<25 bps**), moderate stress (**25–50 bps**), and high stress (**>50 bps**). During SVB (March 2023), FRA-OIS spiked to **~60 bps**. Post-LIBOR cessation, however, the "FRA" leg now references SOFR — a risk-free rate — so credit content has been **significantly degraded**. It retains value as a term liquidity premium indicator but is no longer a counterparty credit signal.

**Rank 5: SOFR-IORB spread.** This is a reserve scarcity and monetary plumbing indicator, not a credit signal. But it is the best early-warning metric for repo market dysfunction. Normal is **0 to -5 bps** (SOFR at or below IORB). In September 2019, this spread spiked to **~280 bps**. A persistent positive spread above **5 bps** is a watch signal; above **25 bps** sustained is alarm-level. The Dallas Fed's Lorie Logan has proposed using TGCR (Tri-Party General Collateral Rate) relative to IORB as an even more precise operating measure.

**Rank 6: Cross-currency basis swaps (USD/JPY, USD/EUR).** These capture dollar funding stress for non-US banks. The current USD/JPY 1-year basis is estimated at **-20 to -40 bps** (structural negative). Watch level is **-70 bps**; alarm is **-100 bps**; GFC peak was **-150 to -200 bps** at short tenors. Valuable as a global dollar shortage signal but does not specifically measure US bank counterparty risk.

**Rank 7: SOFR percentile dispersion (99th vs 1st).** Currently **~13 bps**. Captures repo market segmentation — some borrowers paying far more than others. Watch at **25–50 bps**; alarm above **75 bps**. Useful supplement but inherently noisy at quarter-ends and reflects collateral dynamics, not credit risk.

---

## Stress threshold table for the post-LIBOR dashboard

| Indicator | Current (est.) | Normal | Watch | Alarm | 2007-08 Peak |
|:---|:---:|:---:|:---:|:---:|:---:|
| AA Fin. CP – T-Bill spread | 10–25 bps | <30 bps | 50–100 bps | 150+ bps | 300+ bps (TED) |
| G-SIB 5Y CDS (avg) | 50–80 bps | <60 bps | 100–150 bps | 200+ bps | 200–600 bps |
| SOFR + AXI credit spread | ~15–25 bps | <25 bps | 40–75 bps | 100+ bps | N/A (didn't exist) |
| FRA-OIS (3M) | 10–20 bps | <25 bps | 25–50 bps | 50+ bps | 350+ bps |
| SOFR – IORB spread | -2 bps | -5 to 0 bps | >+5 bps persist. | >+25 bps sust. | ~280 bps (Sep 2019) |
| USD/JPY xccy basis (1Y) | -20 to -40 bps | 0 to -15 bps | -40 to -70 bps | -100+ bps | -150 bps |
| USD/EUR xccy basis (3M) | -16 to -22 bps | 0 to -15 bps | -30 to -60 bps | -80+ bps | -120 bps |
| SOFR 99th-1st pctile | ~13 bps | <15 bps | 25–50 bps | 75+ bps | N/A |
| SRF usage (quarter-end) | $30–80B exp. | <$80B, 1-day | $80–120B | $120B+ or multi-day | N/A |
| HY OAS | 342 bps | <300 bps | 400–500 bps | 600+ bps | 2,000+ bps |
| CCC OAS | 1,013 bps | <700 bps | 1,000–1,200 bps | 1,500+ bps | 3,500+ bps |

**How to read the table**: Any single indicator at "watch" warrants attention. Two or more at "watch" simultaneously, or one at "alarm," signals probable stress. Three or more at "alarm" is crisis-level and likely means counterparty risk is being actively priced across markets.

---

## Private credit is the BNP Paribas moment — it's already happening

The structural parallel between BNP Paribas freezing three subprime funds on August 9, 2007 and the current private credit gating crisis is the most important finding in this research. The sequence mirrors 2007 almost exactly.

On August 9, 2007, BNP Paribas suspended redemptions in three funds worth **~€2 billion**, citing an inability to value subprime assets. LIBOR-OIS spiked 60 bps that day and never normalized. In Q1 2026, **12+ private credit funds** have restricted withdrawals on a **$222 billion** retail asset base. Bloomberg reported on March 26 that **$13 billion** in redemption requests hit private credit funds in Q1 alone, with **$4.6 billion** in investor capital trapped behind 5% quarterly NAV caps. Apollo Debt Solutions received requests for 11% of NAV but honored only ~$730 million. Blue Owl's OBDC II eliminated tender offers entirely. Ares Strategic Income saw requests hit **11.6%** of NAV.

The catalyst is AI disruption of software companies — private credit's largest sector exposure at **~25% of all loans (~$500B+ outstanding)**. SaaS stocks collapsed approximately 30% between October 2025 and February 2026. Private credit default rates have reached **5.8%**, potentially rising to **8% (Morgan Stanley estimate)** or **13% in a severe AI scenario (UBS estimate)**. PIK (payment-in-kind) usage is rising, masking true defaults.

**The JPMorgan collateral markdown on March 11, 2026 is the critical escalation.** JPMorgan marked down software loans used as collateral and restricted lending to private credit funds — creating a potential doom loop: markdowns → less leverage → forced sales → more markdowns. Alt-manager stocks (Blackstone, Apollo, KKR, Ares, Blue Owl) have collectively lost over **$100 billion** in market capitalization. Goldman Sachs projects the retail private credit sector could shed **$45–70 billion** in AUM over the next two years.

The most dangerous transmission channel runs through PE-owned insurance companies. Apollo's Athene holds Level 3 (hardest-to-value) assets comprising roughly **one-third** of total assets. Related-party investments total **$60.1 billion (13.7%** of total assets). AM Best found ~20% of investments by Athene and Global Atlantic are loans to affiliated PE funds — circular risk. Across the US life insurance industry, illiquid investments have reached **18% ($685 billion)** of $3.8 trillion in fixed income holdings, with **10 life insurers** accounting for 43% of all illiquid assets. Treasury Secretary Bessent's announcement on March 30 of emergency meetings with insurance regulators confirms policymakers see this exact transmission mechanism.

What would confirm this as a full crisis: a second major bank following JPMorgan in marking down private credit collateral; a rating downgrade of a PE-owned insurer (Athene, Global Atlantic); a BDC unable to refinance its 2026 maturing debt (23 of 32 rated BDCs have **$12.7 billion** in unsecured debt maturing in 2026 — a **73% increase** over 2025); or contagion from private credit to the CLO market. Mohamed El-Erian has publicly compared the situation to the early stages of 2008. Jeffrey Gundlach called private credit the "top candidate to start the next financial crisis."

---

## The Standing Repo Facility reveals escalating structural fragility

The SRF's usage trajectory tells a story of progressive system tightness that most market participants are underappreciating. Established in July 2021 as a ceiling on repo rates (set at the top of the Fed Funds target range), the SRF was designed as a backstop — not for regular use. Reality has diverged sharply from design intent.

Usage has escalated relentlessly: from effectively **zero** through 2023, to modest draws in mid-2024, to **$10B+** at June 2025 quarter-end, **$18.5B** in September 2025, **$29.4B** at October month-end, **$50.35B** at October 31, and a record **$74.6B** at December 31, 2025. Each successive quarter-end and month-end has been larger than the last. The SRF's ceiling also "leaks" — repo rates traded **38 bps above the SRF rate** on December 31, 2024, indicating stigma and operational friction prevent the facility from functioning as a hard cap.

In December 2025, the Fed acknowledged the severity by removing the $500 billion aggregate daily limit, moving to full allotment, adding morning operations, and effectively renaming the facility. Simultaneously, the Fed ended QT on December 1, 2025 and began **$40 billion/month** in Reserve Management Purchases — the same playbook as October 2019, when the Fed began T-bill purchases after the September repo crisis.

For March 31, 2026 quarter-end: **$30–80B in SRF usage would be normal plumbing** (consistent with the escalation trend). **$80–120B** would be a watch signal — exceeding any prior Q1 draw and suggesting the liquidity cushion is thinner than expected. **$120B+ or multi-day elevated usage** would be alarm-level, indicating either genuine reserve scarcity or distribution failures. The critical distinction: window-dressing resolves within 1–2 business days. If SRF usage remains elevated through April 2–3, that is a stress signal, not plumbing.

The interaction with **$2.8 trillion in reserves** is concerning. Governor Waller suggested reserves below **8% of GDP (~$2.7T)** "could be problematic." Barclays estimates the lowest comfortable level at **$2.7T**. At $2.8T, the system is at the boundary. Crucially, reserves are **concentrated in G-SIBs** — and the 2019 lesson demonstrated that aggregate reserves can appear sufficient while distributional problems cause severe dysfunction. Jamie Dimon stated in October 2019 that JPMorgan "could not lend more" into the repo market despite having surplus reserves, because regulatory constraints prevented rapid deployment.

**Zero RRP ($0.99B) is the single most important structural change** relative to 12 months ago. When ON RRP was at $2+ trillion, it served as an elastic buffer — any repo rate pressure was self-correcting as MMFs shifted from ON RRP to private repo. That buffer is entirely gone. Every marginal liquidity shock now falls directly on reserves. As Apollo Academy's Torsten Slok noted: "once RRP reaches zero, there may no longer be abundant reserves in the banking sector, which increases the probability of an accident somewhere in the plumbing."

---

## Where normal tightening ends and counterparty risk begins

The line between routine quarter-end friction and genuine counterparty risk being priced is defined by **duration, breadth, and spillover** — not magnitude alone.

In 2007, the sequencing was: subprime delinquencies → ABCP market freeze → LIBOR-OIS explosion → bank CDS widening → CP market disruption → interbank lending seizure. Each stage took weeks to months. In September 2019, the sequencing was compressed: reserve concentration → SOFR spike on tax date → intraday rates to 10% → emergency Fed repo operations — but stress was contained to secured markets and resolved in days. The 2019 event was a plumbing failure, not a credit event.

**Normal quarter-end tightening** looks like: SOFR spikes 10–25 bps above IORB for 1–2 days; EFFR stays within the target range; SRF usage concentrated on the statement date and returns to near-zero within 48 hours; pressures are confined to secured/repo markets; bank CDS barely moves.

**Counterparty risk being priced** looks like: SOFR spikes persist 3+ business days; EFFR breaches the top of the target range and stays there; SRF usage remains elevated on non-quarter-end days (rising baseline); pressures spill from secured into unsecured markets (FX swaps, commercial paper); bank CDS widens **50+ bps** within days; cross-currency basis swaps for multiple currencies widen simultaneously; Fed Funds volumes collapse as banks refuse to lend to each other; MMF prime fund outflows begin with concurrent government fund inflows; and the discount window is accessed (stigma-breaking event).

NY Fed SOMA Manager Roberto Perli's March 26, 2026 speech contained a critical data point: reserve ampleness indicators — specifically the share of repo transactions at rates above IORB and the share of bank payments occurring late in the day — have **"approached levels seen in Q1 2019."** The EFFR has risen from 7 bps below IORB to just 1 bp below, compressing "much faster than observed in early 2018." Domestic bank borrowing in the federal funds market has "increased notably." These are the exact same early indicators that preceded the September 2019 repo crisis, now appearing six months after the Fed ended QT.

---

## Japanese bank dollar funding adds a coincident risk window

Japan's fiscal year-end on March 31 creates a coincident stress window that could amplify any domestic US funding disruption. Japanese banks hold gross dollar liabilities exceeding **$2 trillion**, funded through a mix of foreign currency deposits, medium-term FX swaps, corporate bonds, and crucially, short-term FX swaps where roughly **70% of turnover is less than one week** in maturity.

The USD/JPY cross-currency basis — currently estimated at **-20 to -40 bps** for 1-year maturities — is not at alarming levels by historical standards. The narrowing of the US-Japan rate differential (Fed cuts in 2025, BOJ hikes to 0.75%) has structurally compressed the basis from its **-80 to -90 bps** levels of 2016 and 2022. However, quarter-end effects are quantitatively significant: academic research by Du, Tepper, and Verdelhan documents an average **148 bps** one-day jump in 1-week CIP deviations at quarter-ends, with Japan's fiscal year-end adding an additional **10-20 bps** of pressure.

The key distinction for whether a Japan FY-end basis spike signals broader stress: seasonal spikes are contained to the final 1–2 trading days and normalize within the first week of April. Genuine stress manifests as widening that starts in mid-March, extends to 3-month and 1-year tenors (not just overnight), coincides with rising Japanese bank CDS spreads, and does not normalize promptly in April.

Norinchukin — which took a record **¥1.9 trillion ($12.7 billion)** net loss in FY ending March 2025 after selling ¥10+ trillion in foreign bonds — appears to have stabilized. The bank forecasts a modest profit for FY ending March 2026 and has raised ¥1.2 trillion in capital. However, it has pivoted heavily into CLOs, with holdings rising 25% to **¥8.2 trillion ($54 billion)** — representing 18% of its portfolio. A CLO market disruption triggered by US private credit stress could reopen Norinchukin's wounds.

---

## Seven hidden stress indicators most participants aren't watching

**1. Reserve ampleness approaching Q1 2019 levels.** Perli's March 26 speech is the single most important official signal. The share of repo transactions above IORB and late-day payment processing patterns — the Fed's own internal gauges — are flashing the same readings as the quarter before the September 2019 repo crisis. The FHLB-to-IORB arbitrage spread has compressed from a stable **7 bps** during 2022-2024 to **~1 bp** in H2 2025. If it hits zero, marginal reserves are fully bid away.

**2. MMF portfolio composition without RRP backstop.** Money market fund assets have reached a record **$7.86 trillion** (March 18, 2026) while their primary parking lot — the ON RRP facility — has been drained to zero. These funds now intermediate roughly **50% of repo market transactions**. Without ON RRP as an elastic buffer, any shock causing MMFs to pull back from private repo creates an immediate funding crisis for dealers and leveraged investors. This structural vulnerability did not exist 12 months ago.

**3. Dealer balance sheet structural mismatch.** Treasury debt held by the public has grown **139%** since 2014 (to ~$24 trillion), while primary dealer balance sheets grew only **29%** ($3.3T to $4.2T). Brookings/Fed research estimates central clearing could create **$1.3 trillion** in additional capacity — implying current capacity is severely constrained. This structural mismatch is the fundamental cause of auction tails, quarter-end rate spikes, and periodic market dislocations, and it worsens with every Treasury auction.

**4. SOFR volatility regime change.** SOFR daily standard deviation jumped from **1.91 bps** (pre-September 2024 cut) to **2.62–5.72 bps** — a structural threefold increase in day-to-day rate movement. This isn't noise; it reflects a fundamentally different liquidity environment.

**5. BTFP expired with no successor.** The Bank Term Funding Program ceased new loans in March 2024 and fully wound down by March 2025. No replacement exists. Banks with significant unrealized losses on held-to-maturity portfolios have **no facility** that lends at par value of collateral — they must take haircuts at the discount window or FHLB. This creates a latent vulnerability if deposit outflows recur at any institution.

**6. Smaller banks increasing FHLB dependence.** Risk.net reported in February 2026 that smaller US banks were increasing FHLB borrowings in Q4 2025 after the Fed told examiners not to discourage use. FHLBank Chicago advances rose **9.5%** to $61.1 billion. Insurance companies now account for **~$160 billion or 20%+** of total FHLB lending, creating a cross-contamination channel if PE-insurer stress materializes.

**7. Treasury auction demand inelasticity.** Harvard Business School research (2025) found demand elasticity for Treasuries has deteriorated dramatically — yields now rise **9 bps** per 1% increase in supply versus **2 bps** pre-2010, making the market **almost five times more inelastic**. The Treasury-SOFR swap spread at 10-year maturity has declined from **-20 bps** (end-2021) to **-53 bps** recently, meaning Treasuries are structurally cheapening versus swaps. This means any large-scale forced selling (by private credit funds, insurance companies, or foreign holders) will have outsized price impact.

---

## Conclusion: a system priced for perfection entering a stress window

The post-LIBOR financial system has no equivalent of the single, liquid, universally watched counterparty risk thermometer that LIBOR-OIS provided. That information deficit is itself a systemic risk — stress signals are now distributed across multiple less-liquid, less-watched metrics that require active monitoring and expert interpretation. The best practical replacement is a dashboard combining CP-T-bill spreads, bank CDS indices, the SOFR-IORB spread, and cross-currency basis swaps, supplemented by the hidden plumbing metrics catalogued above.

The private credit fund gating crisis is not a future risk — it is the present-tense equivalent of BNP Paribas's August 2007 fund freeze, already larger in scale ($222B base vs. €2B) and more interconnected through the PE-insurer channel. The critical transmission mechanism runs from private credit markdowns through PE-owned insurance companies (Athene, Global Atlantic) into dollar funding markets via rating downgrades, FABN market disruption, and FHLB system stress.

The system enters March 31 quarter-end with three structural vulnerabilities that did not exist 12 months ago: zero RRP buffer, reserves at the estimated comfort boundary with ampleness indicators matching Q1 2019, and a private credit sector experiencing its first serious stress test. The most novel and underappreciated insight from this research is Perli's March 26 admission that internal Fed metrics have reached pre-September 2019 levels — combined with the absence of the RRP buffer that existed in 2019 (when ON RRP wasn't yet a factor) and the added overlay of private credit contagion risk that has no 2019 parallel. The next 72 hours — spanning Japan's fiscal year-end, US quarter-end, and the Treasury's emergency insurance regulator meetings — will test whether these vulnerabilities remain latent or begin compounding.