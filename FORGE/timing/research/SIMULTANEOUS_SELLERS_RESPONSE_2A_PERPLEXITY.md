# Simultaneous Sellers Response — Prompt 2A (Flow of Funds + Price Impact + Buyers)
# Source: Perplexity (no deep research) | Filed: 2026-03-31

> Note: This was run without deep research availability. Quality is lower than 1A/1B Perplexity responses. Key finding: price impact is highly state-dependent — once dealer balance-sheet utilization gets tight, the same amount of net selling produces much larger yield moves.

## Seller Volumes

### Basis Unwind
- $50-200B quarterly range is **plausible and maybe conservative** for an acute stress quarter
- Fed researchers: hedge funds sold **$173B net in March 2020 alone**, with basis traders ~$148B of that
- NY Fed 2025 review links March 2020 dash-for-cash to massive customer selling overwhelming dealers
- Source: [FEDS Notes Oct 2021](https://www.federalreserve.gov/econres/notes/feds-notes/sizing-hedge-funds-treasury-market-activities-and-holdings-20211006.html)

### Private Credit / Broader Fund Redemptions
- $15-25B quarterly estimate for private credit alone is **plausible but not well pinned by public data**
- Important context: open-end mutual funds sold **$236B of Treasuries in Q1 2020** (~1/3 of total Treasury sales that quarter) — Ma, Xiao, and Zeng via NY Fed
- If PC stress spills into broader fund redemptions, system-level selling could be much higher than $15-25B
- Source: [NY Fed Staff Report 1146](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1146.pdf)

### Foreign Official / Sovereign
- China: holdings fell from **$1.27T (Jun 2015) to ~$1.06T (Dec 2016)** = $210B over 18 months = ~$35B/quarter average
- Japan 2022 intervention: material but generally not equivalent to March 2020-style one-month liquidation
- TIC data caveat: custody shifts mean TIC is imperfect owner map
- My $20-45B quarterly range: roughly validated by China 2015-16 precedent ($35B/qtr avg)
- Source: [TIC SLT Table 5](https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.html)

## Estimate Validation Table

| Seller Class | Our Range | Evidence-Based Take | Source |
|---|---|---|---|
| Private credit funds | $15-25B/qtr | Plausible but uncertain; public primary flow evidence weaker than for mutual funds or hedge funds. Treat as scenario assumption, not validated fact. | [NY Fed SR 1146](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1146.pdf) |
| PE-controlled insurers | $10-30B/qtr | **Unverified.** Needs statutory filing or NAIC/SAP evidence to validate. | — |
| Japan life insurers | $12-30B/qtr | Plausible as medium-burn withdrawal. Historical TIC-measured Japanese holdings changes often smaller and noisier on quarterly net basis. | [TIC SLT Table 5](https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.html) |
| China/Gulf sovereign | $20-45B/qtr | About right for upper-stress China analog (2015-16 avg ~$35B/qtr). Gulf capacity harder to validate. | [TIC SLT Table 5](https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.html) |
| Hedge fund basis unwind | $50-200B/qtr | **Validated.** March 2020 alone = $173B net HF selling. | [FEDS Notes Oct 2021](https://www.federalreserve.gov/econres/notes/feds-notes/sizing-hedge-funds-treasury-market-activities-and-holdings-20211006.html) |

Dealer-capacity framing matches literature: NY Fed argues Treasury market functionality deteriorates materially when dealer BS utilization is high. Treasury debt growth has outpaced dealer intermediation capacity — market has "outgrown" dealer balance sheets under stress. [NY Fed SR 1070](https://www.newyorkfed.org/research/staff_reports/sr1070)

## Price Impact

**Key finding: no stable linear coefficient exists. It's a regime split.**

- Duffie et al.: when dealer capacity utilization sufficiently high, Treasury illiquidity becomes **much worse than yield volatility alone would predict** — net selling pressure amplified precisely when it matters most. [NY Fed SR 1070](https://www.newyorkfed.org/research/staff_reports/sr1070)
- March 2020 as upper-tail case: $173B HF + $236B mutual fund + foreign selling hit simultaneously + Fed intervened massively. Attributing clean "yield impact per $100B" from that episode is unreliable — it demonstrates **nonlinearity**, not a stable coefficient.
- Bräuning & Stein (Boston Fed): tighter dealer constraints → reduced positions → reduced turnover → worse liquidity → amplified price movements → impaired auction outcomes. 2020 SLR exemption increased constrained dealers' Treasury activity (confirms mechanism). Any mechanical price-impact estimate must be **adjusted upward** if dealer BS usage already elevated or VaR/SLR binding. [Boston Fed CPP 2025](https://www.bostonfed.org/-/media/Documents/Workingpapers/PDF/2025/cpp20250304.pdf)

## Buyer Step-In

### Banks
- Threshold is a **spread condition, not a single yield level.** NY Fed and Boston Fed: when SLR and BS constraints ease, dealers expand Treasury positions and turnover. Bank step-in requires: yields high relative to deposit/funding costs AND regulatory BS cost low. **Without SLR relief, attractive nominal yields alone may not produce rapid absorption.** [SSRN 5165816](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5165816)

### Foreign CBs (ex-China/Japan)
- IMF COFER 2025Q2: total reserves rising, USD still 56.32% of allocated reserves. Small exchange-rate-adjusted decline in share. Reserve-manager bid **weakened gradually, not disappeared.** Some non-China/Japan reserve managers remain structural buyers, but diversification means less capacity to absorb a large shock at any one yield than in prior decades. [IMF COFER Oct 2025](https://data.imf.org/en/news/october%201%202025%20cofer)

### Retail
- TreasuryDirect confirms participation exists. **No robust time series tying retail demand to specific yield thresholds** from sources retrieved. [TreasuryDirect](https://www.treasurydirect.gov/instit/annceresult/press/preanre/2025/R_20251112_2.pdf)

### Pensions, Insurers, SWFs
- **Insufficient data from this pass** to give hard yield-trigger levels. Needs second pass through primary mandates, annual reports, sector flow reports.

## Working Framework — Stress Quarter Selling Estimates

- **$100-250B** plausible from one or two major channels alone
- **$250-400B+** plausible if basis unwind overlaps with foreign official selling AND broader fund redemptions
- Market impact governed less by static demand elasticity, more by **whether dealer-capacity utilization crosses the Duffie et al. threshold** → liquidity deteriorates sharply → yields gap beyond normal-times flow model

## Data Gaps Remaining
1. PE-controlled insurer Treasury sales (needs NAIC/SAP filings)
2. Japan life-insurer quarterly Treasury disposal volumes (needs MOF flow-of-funds / Japanese filings)
3. Hard buyer step-in thresholds for pensions, insurers, retail, SWFs (needs mandate/annual report review)
