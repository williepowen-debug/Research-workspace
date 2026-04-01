<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Dealer Capacity: Balance Sheet + Regulation + Dislocations

Primary Dealer Intermediation Capacity — Factual Reconstruction

Your Task

Quantify the actual balance sheet capacity of US primary dealers to absorb Treasury selling in 2026. I need hard numbers, not narratives.

Context You Need

The US Treasury market has grown ~139% since 2010 (to ~\$36T outstanding) while primary dealer net positions grew only ~29%. Harvard's Vissing-Jorgensen found Treasury demand is now 5x more inelastic than pre-2010 — a 1% supply increase moves yields 9bps vs 2bps historically. Meanwhile, the Fed is still running QT and multiple large holder classes may become forced sellers simultaneously in 2026.

Current plumbing stress (as of March 2026):

• Fed's Perli (Mar 26): reserve ampleness metrics at Q1 2019 levels — the quarter before the Sep 2019 repo crisis
• Reverse repo (RRP): effectively zero (\$0.99B) — no buffer
• Standing Repo Facility (SRF): \$74.6B record usage (Dec 31, 2025), 38bps above offered rate leaked
• Reserves: \$2.8T at Waller's \$2.7T "problematic" boundary, concentrated in G-SIBs
• MMF assets: record \$7.86T, now intermediate ~50% of repo transactions

Questions

1. What is primary dealer aggregate balance sheet capacity for Treasuries? Give me: total net positions (latest FR 2004 data), gross long/short, how this has evolved since 2010. What's the maximum they've ever held? What's the binding constraint on expansion — SLR, VaR limits, internal risk limits, or balance sheet size?
2. How did Basel III / SLR / Volcker Rule change dealer capacity? Before 2010, dealers could warehouse Treasuries more freely. Quantify the capacity reduction. The SLR treats Treasuries identically to corporate bonds for leverage ratio purposes — how much capacity does this specifically remove? There was a temporary SLR exemption in 2020 — what was its impact on dealer activity, and what happened when it expired?
3. Historical dislocation data. For each episode, give me: the selling volume that triggered it, the price impact, the duration, and how dealers responded:
• Oct 15, 2014 Treasury flash crash: 37bp move in 10Y in 12 minutes
• Sep 16-17, 2019 repo crisis: overnight repo to 10%
• Mar 2020 Treasury market seizure: \$1.6T in selling, bid-ask blew out 8-10x
• Oct 2023 term premium repricing: 10Y to 5%, auction tails

What I Want Back

• Primary dealer aggregate position data (\$ terms, time series if available)
• Binding constraint analysis: which regulation caps capacity and by how much
• Table of historical dislocations: trigger volume → price impact → duration → resolution
• Any OFR, BIS, Fed staff, or TBAC papers on Treasury market liquidity and dealer capacity constraints
• NY Fed Liberty Street blog posts on market functioning

This is a deep, multi-part institutional research question. Here is a hard-numbers reconstruction across all four dimensions you requested.

***

## Primary Dealer Aggregate Position Data

The most current data shows primary dealer net Treasury holdings at **\$482 billion** as of early February 2026 — a record high. This is up from **~\$407 billion** in mid-April 2025 (near the record \$455B reached in late February 2025), and represents a dramatic expansion from pre-2019 norms.[^1][^2]

**Structural evolution (FR 2004A data, net Treasury positions):**


| Period | Net Treasury Position | Context |
| :-- | :-- | :-- |
| ~2010 baseline | ~\$70–80B (est.) | Pre-SLR, pre-Basel III |
| 2015–2018 avg | ~\$100–180B | Post-regulation compression |
| Early 2019 | ~\$250B+ | All-time high at the time [^3] |
| Sep 2019 (repo crisis) | All-time high at that date | Funded via repo, triggering Sep crisis [^4] |
| Mar 2020 | Constrained/unable to expand | SLR binding; Fed had to buy \$1T+ [^5] |
| 2021–2023 avg | \$100–200B range | Post-SLR exemption expiry compression |
| Feb 2026 | **\$482B (record)** | Driven by QT + reduced foreign official buying [^2] |

The ~29% growth in net positions you cited in your context is actually an undercount relative to the gross balance sheet usage. In 2024, primary dealers averaged **\$545–944 billion in daily turnover**, and gross Treasury long + financing positions for SLR-subject dealers alone were **\$450.6B long + \$1,863B in financing = ~\$2.31 trillion** as of June 2024. Average daily Treasury transaction volume for all primary dealers was **\$614.3 billion**.[^6][^7][^8]

***

## Binding Constraint Analysis: SLR

The **Supplementary Leverage Ratio is the primary binding constraint** — not VaR, not internal limits, though those matter secondarily. The key mechanics:

- SLR treats **gross** positions (long + short) as leverage exposure, penalizing the classic dealer model of running matched books[^7]
- For the 6 largest dealers as of June 2024, total leverage exposure headroom was **\$7,307B** (39.4% expansion capacity)[^6]
- If that headroom were fully directed to Treasury intermediation, the 6 largest dealers could theoretically expand Treasury long positions + financing by **316%** from current levels[^6]
- However, that theoretical ceiling is unreachable: capital is fungible and must cover all risk-weighted assets simultaneously

**The SLR's quantified bite on capacity:**

- Each additional \$1 of Treasury holding lowers a G-SIB's SLR by ~4.87 basis points[^9]
- Exempting UST held for trading (~\$81B average at one G-SIB) would increase SLR by **3.94 percentage points**[^9]
- Exempting *all* US Treasury securities (~\$222.7B average) would increase SLR by **5.48 percentage points**[^9]

**VaR and internal risk limits** are the *second* binding constraint. Boston Fed research (Bräuning \& Stein 2024) using confidential microdata found that a one-standard-deviation tighter internal risk-limit shock causes a **2.1% fall in net Treasury position** per dealer, a **7.4 pp lower turnover**, and a **9.8 pp stronger increase in margin requirements**. These are the limits that bite *faster* than regulatory floors in acute stress.[^10]

***

## SLR Exemption: The 2020 Natural Experiment

The April 2020 SLR exemption is the cleanest evidence of regulatory capacity suppression:

- The Fed announced a temporary exemption on **April 1, 2020**, excluding Treasuries and Fed reserves from the SLR denominator, originally set to expire **March 31, 2021**[^11]
- Motivation: the March 2020 seizure demonstrated dealers could not expand balance sheets to absorb selling because the SLR was binding — the Fed had to purchase **>\$1 trillion** in Q1 2020 to resolve the dysfunction[^5]
- On **March 19, 2021**, the Fed announced the exemption would *not* be renewed; dealer stocks fell on the news, with the abnormal returns sensitive to how binding their individual SLR was[^11]
- The exemption's expiry immediately re-tightened effective capacity and is widely cited as the reason the Fed has been studying a permanent Treasury exclusion from the SLR ever since[^5]

***

## Historical Dislocation Table

| Episode | Trigger Volume | Price Impact | Duration | Dealer/Resolution Response |
| :-- | :-- | :-- | :-- | :-- |
| **Oct 15, 2014 Flash Crash** | ~\$500B intraday; equity mini-crashes cascaded into Treasuries [^12] | 37bp roundtrip in 10Y in 12 minutes | ~15 minutes (intraday) | Liquidity returned organically; no Fed intervention; attributed to HFT/thin book, not balance sheet constraint |
| **Sep 16–17, 2019 Repo Crisis** | \$54B in Treasury settlements on Sep 16 + \$120B reserve drain from tax payments [^4] | Overnight repo to 10% intraday; GCF repo to 8%+ | ~4 days until Fed repo ops; fully resolved over ~3 weeks | Fed restarted repo operations (~\$75B/day initially); dealer net positions were at all-time high, balance sheets full [^3] |
| **Mar 9–18, 2020 Treasury Seizure** | Mutual funds, foreign officials, hedge funds all simultaneously selling; ~\$1.6T in estimated outflows | 10Y yield +64bps in 9 days; bid-ask spreads 8–10x normal; off-the-run spreads blew to multiples of on-the-run [^13] | ~10 days until Fed emergency purchases began (March 15–19) | Fed purchased **>\$1T in Q1 2020** [^14]; SLR exemption followed April 1; US banks were net *sellers* [^15] |
| **Aug–Oct 2023 Term Premium Repricing** | QT + rising Treasury issuance + macro uncertainty; no acute forced selling event | 10Y rose from ~4.0% to 5.02% by Oct 19; 30Y auction tailed **3.7bp** on Oct 12 — largest 30Y tail since 2021 [^16] | ~3.5 months (Aug–Oct 2023) | No Fed intervention; resolved via TBAC/Treasury issuance composition shift toward bills; term premium compression into 2024 [^17] |

Key asymmetry: the 2014 and 2023 episodes were **book-depth** problems (thin markets, thin auction demand). The 2019 and 2020 episodes were **balance sheet capacity** problems — dealers were full or couldn't expand. The 2026 risk profile more closely resembles 2019/2020 with the additional amplifier that RRP buffer is now zero [as per your context].

***

## Key Papers and Official Sources

**Federal Reserve / NY Fed:**

- **Fed FEDS Note (Oct 2024):** *"Assessment of Dealer Capacity to Intermediate in Treasury and Agency MBS"* — contains the June 2024 SLR capacity table with dealer-by-dealer breakdown[^6]
- **Fed FEDS Note (Sep 2024):** *"The Treasury Tantrum of 2023"* — term premium decomposition, QT + issuance drivers[^17]
- **NY Fed Liberty Street (Nov 2025):** *"How Has Treasury Market Liquidity Fared in 2025?"* — notes April 2025 depth declined to lowest since March 2023, then recovered[^18]
- **NY Fed Liberty Street (Jul 2022):** *"The Global Dash for Cash in March 2020"* — cross-country comparison, explains why US dealers couldn't absorb[^15]
- **Fed FEDS Note (Feb 2020):** *"What Happened in Money Markets in September 2019?"* — full mechanics of the repo crisis with dealer position data[^4]

**BIS:**

- **BIS Working Paper 966 (Oct 2021):** *"The Treasury Market in Spring 2020 and the Response of the Federal Reserve"*  — causal evidence on Fed purchases[^13]
- **BIS Working Paper 1138:** *"Dealer Capacity and US Treasury Market Functionality"* — shows significant functionality loss when dealer balance sheets are stressed[^19]

**Boston Fed / OFR:**

- **Boston Fed Working Paper 24-07 (Bräuning \& Stein):** *"The Effect of Primary Dealer Constraints on Intermediation in the Treasury Market"* — confidential microdata, VaR and SLR shock quantification[^10]
- **Boston Fed (Dec 2025):** *"Relaxing Dealers' Risk Constraints Can Make Treasury Market More Resilient"*[^7]
- **OFR Blog (Apr 2023):** *"OFR Identifies Factors That May Have Contributed to the 2019 Spike in Repo Rates"*[^3]
- **OFR Blog (Aug 2024):** *"Banks' Supplementary Leverage Ratio"*[^20]

**SIFMA / TBAC:**

- **SIFMA (Apr 2025):** *"Enhance Market Resilience by Exempting Treasuries from Leverage Ratios"* — quantifies SLR impact per \$1 of Treasury held[^9]
- **TBAC Report (Oct 2023):** Documents the 3.7bp 30Y tail and auction demand stress[^16]
- **Under Secretary Liang speech (Nov 2024):** Explicitly acknowledges "increase in Treasury securities outstanding relative to dealer capacity...partly reflecting regulations adopted in response to the GFC"[^21]

***

## Synthesis: The 2026 Capacity Envelope

The theoretical **SLR headroom allows 316% expansion** from current Treasury long + financing levels for the 6 largest dealers. But the operative constraint is that the \$482B record net position  already represents dealers absorbing QT float and reduced foreign official buying  — they are running elevated inventories *without a stress event*. The Perli/Waller reserve floor warning and zero RRP buffer mean that in a simultaneous forced-seller scenario (foreign official liquidation + hedge fund deleveraging), dealer expansion would require either:[^2][^1][^6]

1. A repeat of the 2020 SLR exemption (currently under active discussion in the Basel III endgame rulemaking), or
2. Fed SRF activation at scale (the \$74.6B record usage in Dec 2025 you cited indicates it's already being stress-tested), or
3. Emergency QE — the 2020 precedent suggests the threshold is a roughly 60–70bp yield spike over ~2 weeks before Fed intervention becomes inevitable
<span style="display:none">[^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34]</span>

<div align="center">⁂</div>

[^1]: https://www.facebook.com/KobeissiLetter/posts/treasury-holdings-at-financial-institutions-are-surgingprimary-dealer-holdings-o/1235797482028999/

[^2]: https://adamjosephson.substack.com/p/primary-dealers-volume-hits-record

[^3]: https://www.financialresearch.gov/the-ofr-blog/2023/04/25/ofr-identifies-factors-that-may-have-contributed-to-the-2019-spike-in-repo-rates/

[^4]: https://www.federalreserve.gov/econres/notes/feds-notes/what-Happened-in-Money-Markets-in-September-2019-20200227.htm

[^5]: https://bpi.com/treasury-market-resiliency-and-large-banks-balance-sheet-constraints/

[^6]: https://www.federalreserve.gov/econres/notes/feds-notes/assessment-of-dealer-capacity-to-intermediate-in-treasury-and-agency-mbs-markets-20241022.html

[^7]: https://www.bostonfed.org/publications/current-policy-perspectives/2025/relaxing-dealers-risk-constraints-can-make-treasury-market-liquid.aspx

[^8]: https://www.federalregister.gov/documents/2024/01/16/2023-27860/standards-for-covered-clearing-agencies-for-us-treasury-securities-and-application-of-the

[^9]: https://www.sifma.org/news/blog/enhance-market-resilience-by-exempting-treasuries-from-leverage-ratios

[^10]: https://www.bostonfed.org/-/media/Documents/Workingpapers/PDF/2024/WP2407.pdf

[^11]: https://www.federalreserve.gov/econres/notes/feds-notes/impact-of-leverage-ratio-relief-announcement-and-expiry-on-bank-stock-prices-20230629.html

[^12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5665520/

[^13]: https://www.bis.org/publ/work966.htm

[^14]: https://e-axes.com/the-u-s-treasury-market-the-march-2020-dislocations-and-reform/

[^15]: https://libertystreeteconomics.newyorkfed.org/2022/07/the-global-dash-for-cash-in-march-2020/

[^16]: https://home.treasury.gov/news/press-releases/jy1865

[^17]: https://www.federalreserve.gov/econres/notes/feds-notes/the-treasury-tantrum-of-2023-20240903.html

[^18]: https://libertystreeteconomics.newyorkfed.org/2025/11/how-has-treasury-market-liquidity-fared-in-2025/

[^19]: https://www.bis.org/publ/work1138.pdf

[^20]: https://www.financialresearch.gov/the-ofr-blog/2024/08/02/banks-supplementary-leverage-ratio/

[^21]: https://home.treasury.gov/news/press-releases/jy2721

[^22]: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_2004

[^23]: https://www.newyorkfed.org/markets/primarydealers

[^24]: https://catalog.data.gov/dataset/government-securities-dealers-reports

[^25]: https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding/primary-dealers

[^26]: https://www.newyorkfed.org/financial-institution-supervision/reporting-forms-and-instructions/reporting-forms/fr-2004wi-guide-sheet

[^27]: https://www.federalreserve.gov/reportforms/forms/FR_200420130331_i.pdf

[^28]: https://www.newyorkfed.org/financial-institution-supervision/reporting-forms-and-instructions/reporting-forms/fr-2004si-guide-sheet

[^29]: https://www.suerf.org/wp-content/uploads/2025/05/SUERF-Policy-Brief-1173_Brauning_Scheicher_Stein.pdf

[^30]: https://www.reginfo.gov/public/do/DownloadDocument?objectID=1706701

[^31]: https://www.federalreserve.gov/econres/notes/feds-notes/insights-from-revised-form-fr2004-into-primary-dealer-securities-financing-and-mbs-activity-20220805.html

[^32]: https://www.newyorkfed.org/markets/counterparties/primary-dealers-statistics

[^33]: https://adamtooze.com/2020/11/28/chartbook-newsletter-5/

[^34]: https://tipswatch.com/2024/10/20/what-about-thursdays-auction-of-a-new-5-year-tips/

