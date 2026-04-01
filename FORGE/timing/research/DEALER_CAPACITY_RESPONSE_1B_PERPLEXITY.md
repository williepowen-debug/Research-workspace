# Dealer Capacity Response — Prompt 1B (Basis Trade / MMF / Issuance)
# Source: Perplexity Pro | Filed: 2026-03-31

# Treasury market stress mechanics: basis trades, MMF flows, and issuance dynamics in 2026

**The Treasury basis trade has grown to roughly $1.06 trillion in cash-futures exposure alone — 60% larger than its pre-pandemic peak — while the shock-absorbing ON RRP buffer has drained from $2.6 trillion to near zero, leaving the system structurally more fragile than at any point since March 2020.**

This matters because the three dynamics explored below are tightly coupled: a basis-trade unwind forces Treasury selling into a market where dealer balance sheets are constrained, while MMF cash — now deployed in $2.7 trillion of private dealer repo rather than parked safely at the Fed — could amplify or dampen the shock depending on whether funds face redemptions themselves. Treasury's deliberate front-loading into bills has bought time on the long end, but coupon issuance increases are coming in FY2027, and heavy settlement dates in Q2 2026 could stress dealer intermediation capacity at the worst possible moment.

---

## 1. The basis trade now exceeds $1 trillion — far above pre-pandemic levels

The hedge fund Treasury basis trade — long cash Treasuries financed in repo, short equivalent Treasury futures — has grown into one of the largest concentrated leveraged positions in global markets.

**Size estimates by source.** The BIS Quarterly Review (December 2025, Sushko & Todorov) provides the most granular decomposition: as of Q2 2025, hedge fund short Treasury futures associated with the cash-futures basis trade totaled **$1,060 billion**, with an additional **$631 billion** in interest rate swap spread trades (long Treasuries / pay fixed on swaps). Total hedge fund long Treasury exposures reached **$2,379 billion** — roughly 10% of all privately held Treasuries — against $1,748 billion in short exposures. The NY Fed's Roberto Perli confirmed in May 2025 that CFTC leveraged fund net shorts in Treasury futures with maturities ≤10 years exceeded **$1 trillion** by March 2025, well above the **$660 billion** pre-pandemic peak in February 2020.

The OFR's 2025 Annual Report (November 2025) placed total hedge fund industry Treasury positions at **$4.1 trillion**, up $1 trillion in 2025 alone. A critical data gap compounds the picture: Fed researchers discovered in October 2025 that TIC data **undercount Cayman-domiciled hedge fund Treasury holdings by approximately $1.4 trillion** as of end-2024. The actual footprint of leveraged Treasury strategies is substantially larger than headline figures suggest.

**Leverage mechanics are extreme but heterogeneous.** The basis trade's leverage derives from two sources simultaneously. On the cash leg, Treasury repo haircuts range from **0% to 2%** — a 1% haircut implies 100x leverage, a 2% haircut implies 50x. OFR data on non-centrally cleared bilateral repo shows a **large share of outstanding repo carries zero haircuts** for established hedge fund counterparties. On the futures leg, pre-pandemic leverage on Treasury futures was approximately **175x for 5-year and 120x for 10-year** contracts (BIS, September 2023). Post-2021, higher volatility and increased initial margins reduced these to roughly **70x and 50x** respectively. The combined trade leverage is typically characterized as **50x to 100x** (Better Markets, April 2025), though the CFTC's Market Risk Advisory Committee used a more conservative 20x for full-trade regulatory analysis.

The critical structural vulnerability is that margin requirements on both legs can tighten simultaneously. CME does **not** recognize the hedging offset provided by the long cash position when calculating futures margin — hedge funds must post full initial and variation margin on the short futures position despite holding a theoretically offsetting long position. When volatility spikes, both repo haircuts and futures margins rise in lockstep, creating a classic **margin spiral** (Brunnermeier & Pedersen, 2009).

**There is no single basis-point threshold for forced unwinds.** The unwind trigger depends on the speed and magnitude of the yield move, starting leverage and cash buffers, dealer willingness to continue financing, and whether clearing houses raise margins. Resonanz Capital (February 2026) identified four failure modes: (A) repo tightening forcing deleveraging, (B) futures margin jumps draining cash, (C) the basis widening before convergence generating mark-to-market losses, and (D) crowded exits where correlated selling overwhelms absorption capacity. In practice, these modes compound each other.

### March 2020 provides the calibration event

The sequence was rapid. By late February 2020, hedge funds held roughly **$991 billion** in cash Treasuries (Vissing-Jørgensen, BIS WP 966), with CFTC leveraged fund shorts at ~$660 billion. Between March 9 and 18, 10-year Treasury yields spiked an anomalous **64 basis points** (from ~0.54% to ~1.18%) even as equities collapsed — the "dash for cash" in which Treasuries temporarily lost their safe-haven status.

Margins on Treasury futures rose **over 30%** across note contracts and more than doubled on bond futures. Hedge funds sold between **$100 billion** (Barth & Kahn, Journal of Monetary Economics 2025, basis traders specifically) and **$173 billion** (Banegas, Monin & Petrasek, all hedge funds) in cash Treasuries, reducing total Treasury exposure by **$430 billion**.

The selling multiplier was significant: each dollar of basis-trade unwind generated direct selling pressure that further widened spreads and triggered additional margin calls in a self-reinforcing loop.

The Fed's response was massive. On March 15 it announced at least $500 billion in Treasury purchases; on March 23 it moved to purchases "in amounts needed" (effectively unlimited). Actual purchases, not just announcements, were necessary to stabilize markets — daily purchases exceeded **$100 billion** on some days. From mid-March to mid-April 2020, the Fed purchased approximately **$1.3 trillion** in Treasuries. Through July 31, 2020, cumulative SOMA purchases reached **$1.77 trillion** in Treasuries plus **$892 billion** in agency MBS.

### The trade has grown back — and evolved

After collapsing in 2020, the basis trade remained subdued until H2 2022 when quantitative tightening and rising Treasury issuance recreated favorable conditions. Between June 2022 and September 2023, hedge funds expanded Treasury positions by over **$1.1 trillion** (Barth & Kahn). The cash-futures basis trade reached $1.06 trillion by Q2 2025, but growth has since shifted to the **swap spread trade**, which surged from $281 billion (Q1 2024) to $707 billion (March 2025) before contracting 11% during the April 2025 tariff-related turbulence.

The April 2025 episode — while "unnerving" per the NY Fed — was **not nearly as disruptive as March 2020**, partly because the Standing Repo Facility provided backstop funding and dealers remained willing to intermediate.

---

## 2. MMFs hold $7.9 trillion with no RRP buffer remaining

Money market funds have become the dominant marginal lender in short-term Treasury-linked markets, and the exhaustion of the ON RRP facility has fundamentally altered the plumbing.

**Current scale and composition.** As of March 18, 2026, ICI reports total MMF assets of **$7.86 trillion** (Crane Data's broader measure: ~$8.27 trillion). Government MMFs comprise roughly **$6.47 trillion (82%)**, prime MMFs **$1.25 trillion (16%)**, and tax-exempt funds $143 billion (2%). Institutional funds account for 60.5% of assets ($4.75 trillion), with government institutional funds alone at $4.50 trillion. Liquidity metrics remain healthy: government MMFs hold **75.2% daily liquid assets** and **86.8% weekly liquid assets** (February 2026).

**The $2.6 trillion RRP drain is the defining flow event.** The Fed's ON RRP facility peaked at roughly **$2.6 trillion in December 2022** and has declined to near zero in 2026. This ~$2.3 trillion reallocation represents one of the largest liquidity shifts in modern financial markets. According to FEDS Notes (Bostrom, March 2025), between April 2023 and November 2024, MMFs shifted approximately **$1.7 trillion into T-bill holdings** and roughly **$900 billion into private repo** (split between $600 billion overnight and $300 billion term). By Q2 2025, MMF private repo exposure hit a record **$2.7 trillion**, with total repo allocation exceeding **$3 trillion (41% of assets)**.

Over one-third of MMFs' repo exposure now runs through FICC, concentrated among a handful of large clearing member sponsors.

**The intermediation chain matters enormously for stress scenarios.** When MMF cash flowed from the RRP into dealer repo, it provided dealers with cheap funding — theoretically expanding their capacity to intermediate Treasury markets and finance hedge fund basis trades. However, this funding expansion occurs against regulatory constraints. The **Supplementary Leverage Ratio (SLR)** treats all assets equally regardless of risk, meaning every dollar of Treasury intermediation consumes scarce balance sheet capacity. Three of six largest U.S. bank holding companies were bound by the enhanced SLR prior to the December 2025 reform.

Outstanding Treasuries have grown roughly **4x relative to primary dealer balance sheets** since 2007. Dallas Fed President Logan stated in May 2025 that "the demand for intermediation could overwhelm the supply of intermediation and create market dysfunction."

The December 2025 eSLR reform — reducing the surcharge for G-SIBs — was specifically designed to ease this constraint, creating an estimated **$384 billion in excess Tier 1 capital** (up from $174 billion). Expanded central clearing through FICC provides approximately **$1.4 trillion** in netting benefits, with an additional $1.3 trillion available if all Treasury repo were cleared (Liang & Zhu, Brookings, February 2026 update).

### A $500 billion MMF outflow would transmit directly into dealer capacity

Based on current portfolio allocations and historical precedents, a $500 billion MMF redemption event would propagate through several channels. Proportional to the current ~36-41% repo allocation, roughly **$180-205 billion** would exit dealer repo, directly reducing dealer funding capacity for Treasury intermediation and hedge fund financing. Approximately **$150-200 billion** in T-bill sales would pressure short-end yields. With the ON RRP buffer exhausted, there is no shock absorber — every marginal liquidity shock now falls directly on bank reserves.

Historical precedents bracket the range. In 2008, institutional prime MMFs lost **$410 billion (30% of assets)** within four weeks of the Reserve Primary Fund breaking the buck, triggering the Treasury's $2.7 trillion guarantee program and the Fed's AMLF facility. In March 2020, prime institutional outflows exceeded **$25 billion per day** at the peak, and MMFs cut commercial paper holdings by **$35 billion** in two weeks, accounting for 74% of the decline in CP outstanding. Government MMFs simultaneously absorbed **$838 billion** in flight-to-quality inflows during March 2020 alone.

The second-order transmission is what matters most: dealer balance sheet contraction from lost repo funding would reduce capacity to intermediate Treasury markets, potentially widening bid-ask spreads and reducing market depth precisely when hedge fund basis trade unwinds are generating forced selling. This is the coupled-system risk: MMF stress → dealer funding withdrawal → basis trade margin calls → forced Treasury selling → wider spreads → further MMF stress.

---

## 3. Treasury is front-loading into bills while holding coupons flat

The Treasury Department has adopted an explicit strategy of absorbing incremental borrowing needs through T-bill issuance while maintaining coupon auction sizes unchanged — buying time on the long end but building duration risk into future issuance needs.

**Bill issuance dominance is confirmed.** In 2025, **84% of gross government debt issuance was in T-bills** (maturities ≤12 months), the highest ratio since the financial crisis (RSM US, January 2026). Four-week bill auctions averaged **$101 billion per auction** in 2026, more than double the $47 billion average in 2016 and now the largest single-security offering by the Treasury (Peterson Foundation). T-bills outstanding reached approximately **$6.6 trillion** as of January 31, 2026 (TBAC presentation).

While the specific $195 billion to $352 billion 12-week surge figure could not be precisely verified from primary sources, the broader pattern of aggressive bill issuance growth is unambiguous across multiple official sources.

**Treasury has been explicit about this strategy.** Secretary Bessent stated the Treasury will "initially issue most of the new supply in the bill market as opposed to coupons" to take advantage of lower short-term yields. The November 2025 Quarterly Refunding Statement announced expected bill auction size reductions in December followed by increases from mid-January 2026 "based on expected fiscal outflows." The TBAC unanimously recommended maintaining all nominal coupon, FRN, and TIPS auction sizes at current levels in their February 2026 meeting, with coupon increases not anticipated before FY2027.

**Bills currently represent roughly 22% of outstanding marketable Treasury debt**, above TBAC's historical ~20% guidance but below the November 2008 crisis peak of nearly 35%. T. Rowe Price projects the bill share will rise to **23-25%** as the government finances the One Big Beautiful Bill Act's fiscal package. Standard Chartered (February 2026) suggested Treasury could raise the bill share by 2.5 percentage points over three years, creating ~$0.9 trillion in additional bill supply.

### Upcoming auction schedule and settlement stress points

The TBAC recommended the following long-end auction sizes through mid-2026 (all sizes in billions, per February 4, 2026 financing table):

| Security | Apr 2026 | May 2026 | Jun 2026 | Type |
|----------|----------|----------|----------|------|
| 10-Year Note | $39B (Apr 8) | $42B (May 12) | $39B (Jun 10) | Reopen / New / Reopen |
| 20-Year Bond | $13B (Apr 22) | $16B (May 20) | $13B (Jun 16) | Reopen / New / Reopen |
| 30-Year Bond | $22B (Apr 9) | $25B (May 13) | $22B (Jun 11) | Reopen / New / Reopen |

**Two settlement dates pose concentration risk for dealer balance sheets.** April 30, 2026, concentrates roughly **$196 billion+** in coupon settlements (2-year $69B, 5-year $70B, 7-year $44B, 20-year $13B, plus TIPS and FRN). June 30, 2026 — quarter-end — carries a nearly identical **$196 billion+** load. Quarter-end settlement coinciding with regulatory reporting dates amplifies the balance sheet impact, as dealers typically reduce positions to window-dress leverage ratios.

**Net new issuance projections confirm the structural challenge.** The CBO's February 2026 outlook projects a **$1.9 trillion federal deficit** for FY2026 (5.8% of GDP), with cumulative deficits of **$23.1 trillion** over 2026-2035. Treasury's own estimates show $574 billion in net marketable borrowing for Q1 2026 (January-March) and $109 billion for Q2 2026 (April-June, artificially low due to April tax receipts). The median primary dealer estimate shows Treasury is "slightly overfunded" in FY2026 at current coupon sizes, but a **$1.1 trillion funding shortfall** emerges in FY2027-28 — meaning coupon auction increases become unavoidable.

---

## 4. The regulatory and structural backdrop is shifting rapidly

Several reforms are converging that could either mitigate or amplify stress dynamics in 2026.

**Central clearing mandates create a December 2026 deadline.** The SEC's Treasury clearing rule requires cash transaction clearing compliance by **December 31, 2026** and repo clearing by **June 30, 2027** (both dates extended 12 months in February 2025). CME Securities Clearing was approved as a second clearing agency in December 2025 alongside FICC. Cross-margining agreements between FICC and CME were amended in December 2025, and FICC's new "Collateral-in-Lieu" service (approved December 2025) addresses the double-margining problem by allowing liens on repo collateral.

The Chicago Fed Letter (2026) analyzed how the clearing mandate could affect basis trade mechanics — requiring margin at the CCA could reduce leverage but also raise the cost of the trade.

**The academic literature provides a clear warning.** Duffie et al. (FRBNY Staff Report 1070, August 2023) found that when **dealer balance sheet utilization reaches sufficiently high levels, Treasury market liquidity is much worse than predicted by yield volatility alone** — consistent with occasionally binding constraints. On March 12, 2020, Treasury illiquidity reached **5.4 standard deviations** above its mean while dealer capacity utilization hit its sample record high.

Bräuning & Stein (Boston Fed, July 2024) directly observed dealers' internal risk limits using confidential microdata, confirming that binding constraints directly impair intermediation. Primary dealer net cash Treasury positions remain around **$150-200 billion** — roughly 10x larger than their DV01-adjusted hedged positions — while daily Treasury repo and reverse repo financing at primary dealers has grown to **$6.1 trillion** (December 2025). The ratio of outstanding Treasuries to dealer intermediation capacity continues to widen, making each stress episode potentially more acute than the last.

---

## The coupled-system risk for 2026 stress scenarios

The three dynamics examined here form a feedback loop that did not exist in this configuration before. The basis trade at **$1+ trillion** (versus $660 billion pre-pandemic) creates a larger potential forced-selling event. The exhaustion of the **$2.6 trillion RRP buffer** means MMF cash is deployed in private markets rather than safely parked at the Fed — useful for dealer funding in normal times, but a vulnerability if MMFs face redemptions. Treasury's bill-heavy issuance strategy has successfully avoided stressing the long end, but the **$1.1 trillion coupon shortfall** projected for FY2027-28 means this runway is finite.

The key variables to monitor are: CFTC leveraged fund net short positioning (available weekly), MMF repo allocation versus T-bill holdings (OFR Money Market Fund Monitor, quarterly with some weekly data), primary dealer net positions (FRBNY, weekly), and repo rate volatility at quarter-ends and settlement dates.

The April 30 and June 30 settlement clusters, each exceeding $196 billion in coupon settlements, represent the nearest-term pressure points where these dynamics could interact.

The eSLR reform and expanding central clearing provide meaningful structural relief — the estimated **$2.7 trillion** in combined netting benefits and freed balance sheet capacity could substantially improve dealer absorption capacity. But these benefits are partially forward-looking: the cash clearing mandate doesn't take effect until December 2026, and the largest netting gains depend on repo clearing not required until June 2027. For the next several quarters, the system operates with pre-reform plumbing against post-crisis-scale positions.

### Key official sources for ongoing monitoring

- **OFR Hedge Fund Monitor** — CFTC TFF net notional Treasury futures, updated weekly
- **OFR Money Market Fund Monitor** — MMF portfolio composition from SEC N-MFP filings
- **FRBNY Primary Dealer Statistics** — Weekly dealer positions, published Thursdays
- **FRED RRPONTSYD** — Daily ON RRP balances
- **ICI Weekly MMF Data** — Total assets by fund type
- **TBAC Quarterly Refunding Archives** — Next release May 6, 2026
- **BIS Quarterly Review** — Next issue June 2026 (watch for Sushko/Todorov updates)
- **OFR 2026 Annual Report** — Expected November 2026
- **CBO Budget and Economic Outlook** — Updated projections expected mid-2026
