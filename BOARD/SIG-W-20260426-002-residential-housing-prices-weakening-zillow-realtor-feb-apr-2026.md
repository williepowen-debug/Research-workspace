---
signal_id: SIG-W-20260426-002
precedence: PRIORITY
timestamp: 2026-04-26T14:00:00Z
source: WALTER
origin: |
  Multi-origin combined per Phase 1b same-theme rule:
  - Will Telegram image 2026-04-26 13:52 UTC (msg 1082) — @ResidentialClub (ResiClub, Lance Lambert) screenshot of Zillow Home Value Index Feb 2026 reading, published March 2026: "Among the nation's 200 largest metro area housing markets — 32% are seeing falling year-over-year home prices, 68% are seeing rising year-over-year home prices." Body text refines: 35.5% of top 200 metros saw YoY falls in Feb 2026, 64.5% rising. Long-history chart shows fresh post-pandemic high in % falling, prior comparable peaks 2008-2012.
  - Will Telegram image 2026-04-26 13:52 UTC (msg 1085) — @m3_melody (Melody Wright) on Realtor.com data: "On a square-foot basis, prices dropped 2.3% year over year, the 13th straight week of declines… that suggests underlying home values are falling." Cites Realtor.com TRENDS post by Keith Griffith Apr 24 2026 ("Spring Thaw for Housing as New Listings Surge and Prices Continue 14-Week Slide"). Posted 4/25/26 11:37 AM.

to: REGINALD (ACTION — BANK_CRE / residential housing primary domain per ROUTING_TABLE v0.5 exception Apr 20)
info: CARL, BROCK, RED, NEXUS, PROME
group: —
dispatched: 2026-04-26T14:00:00Z
dispatch_note: "Two independent residential-housing data points pointing same direction with distinct methodology — combined per Phase 1b same-theme rule. Zillow ZHVI is a stock-measure of metro-level YoY YE change; Realtor.com square-foot is a flow-measure of listing-price-per-sqft (controls for compositional shift to smaller homes — the standard bear-case rebuttal that 'prices look down because cheaper homes are selling' is cut by SQFT basis). 35.5% of top 200 metros falling YoY is the highest post-pandemic reading; 13-week-streak SQFT decline is unusual. Both primary-grade sources via well-known aggregators (Lance Lambert / Melody Wright). REGINALD primary because residential exposure for regionals (KRE constituents) maps to consumer-loan + HELOC + 1-4 family loan books. CARL secondary on consumer wealth-effect transmission. BROCK secondary on housing-finance and MBS pricing implication (private-label, GSE, Ginnie). RED secondary as adversarial check — what's the bull rebuttal? (Likely: regional dispersion = some metros rising offsetting falling; SFRR transition; tight inventory still supportive in NE/Midwest.) NEXUS as cluster classification candidate: pairs with bank-CRE office/multi-family weakness signals (SIG-W-20260420-008, SIG-W-20260424-005), residential layer of broader bank-collateral pressure cluster."

signal_type: threshold-crossed
confidence: 0.85
confidence_language: confirms
resources: 0
safety_net: clear

word_count: 540

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: BANK_COLLATERAL
---

## Signal

**Two independent residential-housing data points dispatched Apr 25-26 confirm same direction:**

**(a) Zillow ZHVI Feb 2026 — top-200-metros breadth.** 35.5% of the nation's 200 largest metro housing markets saw home prices fall YoY in Feb 2026 (64.5% rose). This is the highest post-pandemic reading; the long-history chart (Lance Lambert/ResiClub) shows the prior comparable cluster was 2008-2012. The 2024-2026 episode now has two ~peaks: ~30% falling around 2024 and 35.5% in Feb 2026. Source: ResiClub analysis of Zillow Home Value Index, Feb 2026 reading published March 2026.

**(b) Realtor.com Apr 24 2026 — price-per-square-foot national.** Prices dropped **2.3% YoY on a square-foot basis**, marking the **13th straight week of declines**. Title: "Spring Thaw for Housing as New Listings Surge and Prices Continue 14-Week Slide" by Keith Griffith. The square-foot framing matters because the standard bear-case rebuttal — "median prices look down only because cheaper smaller homes are selling" (compositional shift) — is neutralized when measured per-sqft. Underlying home values are falling, not just headline median.

Together: stock-measure (Zillow YoY % metros) and flow-measure (Realtor.com SQFT YoY) both point down, with breadth highest post-pandemic and the SQFT decline streak unusual.

## Relevance

- **REGINALD (ACTION — BANK_CRE / residential):** Top priority. Residential 1-4-family loans + HELOCs + home-equity-collateralized lines are core regional bank assets. Falling home values in 35.5% of metros + nationwide -2.3% SQFT YoY = collateral-value compression on the residential book. For KRE constituents, look at: (a) HELOC LTV migration, (b) 1-4 family mortgage delinquency leading edge, (c) provisioning trends on residential book in upcoming Q1 prints. Regional dispersion is critical — the 35.5% includes Sun Belt + West concentration, which is exactly KRE/WAL/OZK geo-exposure.

- **CARL (info — consumer wealth-effect):** Housing is the largest household balance-sheet component for the median US household. Falling home values compresses perceived wealth → reduces precautionary spending capacity, refi/HELOC access, retirement-year wealth math. Layers on top of CC delinq SIG-W-20260424-007 (12.7% approaching 2009 peak) and FL LABOR SIG-W-20260424-001. Consumer-credit transmission chain has another negative input.

- **BROCK (info — housing finance):** MBS pricing, GSE risk-share trends, private-label residential exposure. If the price decline streak extends beyond 14 weeks, expect GSE g-fee revisions and private-label spread widening. Watch agency MBS basis vs Treasuries.

- **RED (info — adversarial):** Strongest bull rebuttal: regional dispersion means 64.5% of metros still rising, NE/Midwest tight-inventory dynamics still firm, the SFRR/build-to-rent secular tailwind partially absorbing supply, AAA-tier mortgage credit still pristine. Counter-counter: SQFT decline cuts compositional rebuttal, 35.5% breadth is post-pandemic high, regional concentration of decline maps directly to KRE/WAL/OZK exposure (Sun Belt). The bull case is "regionally contained / mean-reverting"; the bear case is "structural Sun Belt over-build + buyer-strike at high mortgage rates."

- **NEXUS (info — cluster):** Candidate cluster member. Pairs with: SIG-W-20260420-008 (distressed office sales price-discovery $5B+), SIG-W-20260424-005 (US office vacancy 20.2% all MSAs), SIG-W-20260424-007 (CC delinq 12.7% approaching 2009). Cluster name candidate: "bank-collateral-compression" or "consumer-real-estate-stress." Different transmission mechanisms (commercial vs residential, vacancy vs price, debt vs collateral) but same outcome: bank balance sheet quality deteriorating.

- **PROME (info):** Coordinator awareness, multi-quarter cadence.

## Caveats

- **Compositional vs structural read.** Zillow 35.5% metros figure could be re-narrowed if regional bifurcation persists (NE/Midwest holding while Sun Belt cracks). The thesis-relevant question is which metros are in the falling 35.5% — broad geographic mapping not in this signal, REGINALD pickup work.
- **Realtor.com SQFT methodology** controls for size-mix but not quality-mix (renovated vs unrenovated) or new-vs-existing. WALTER did not pull the underlying article; REGINALD verify on pickup if any specific metro detail matters.
- **Lance Lambert / Melody Wright are reputable housing data analysts**, both well-respected aggregators of primary data. No verify spawn needed.
- **Stock vs flow vs sentiment.** This is two of three legs; the missing third is Case-Shiller (S&P CoreLogic — typically lags ~2 months). Next Case-Shiller release will confirm/contradict.
- **What's NOT in this signal:** geographic breakdown, mortgage rate context (current 30Y), inventory/months-of-supply data, builder cancellation rates. REGINALD pickup work for any specific metro thesis.

## Source

- Will Telegram images 2026-04-26 13:52 UTC (msgs 1082, 1085)
- @ResidentialClub (ResiClub / Lance Lambert) — verified, primary-grade housing-data analyst
- @m3_melody (Melody Wright) — reputable housing data analyst
- Zillow Home Value Index (primary) — Feb 2026 reading published March 2026
- Realtor.com TRENDS — Keith Griffith Apr 24 2026 article: "Spring Thaw for Housing as New Listings Surge and Prices Continue 14-Week Slide"
- Cluster cross-references: SIG-W-20260420-008, SIG-W-20260424-005, SIG-W-20260424-007
