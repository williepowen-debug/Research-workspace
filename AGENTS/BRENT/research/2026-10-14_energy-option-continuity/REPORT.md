# Continuing energy option exposure — October 14, 2026

**Result:** the most promising construction to investigate is **USO December 18 $162/$175 call debit spread**, one spread, 65 calendar days. It preserves a meaningful payoff on another crude rally within the existing structural tenor and ~$500 loss limit. This is BRENT's research comparison, not a TERRY-approved card or a recommendation to submit an order today. The physical trigger, fresh owner assessment and Will's capital approval are not established by affordable premium.

**Authority:** Will's direct “Okay agree can you dig into that?” follows his concern about having no calls or similar energy options after today. Research approved; no automatic replacement, roll, new capital, gate change or monitoring cadence. Will handles today's calls. Those calls' eventual outcome remains unverified here.

## What we are buying exposure to

The strongest defensible case for new crude convexity is another disruption-driven rise over the coming weeks, while export access remains impaired. It is weaker as an assertion that every part of the energy complex will keep rising. October14 IEA estimates show crude exports recovering more than products; today's shipping study finds commercial-access risk without authenticating incremental oil loss after the latest strikes. December diesel arbitrage economics have improved, a counterargument to extrapolating prompt fuel scarcity indefinitely. Demand damage is also real in the IEA estimates.

USO's published objective references daily WTI futures changes; BNO references Brent. BNO is economically closer to seaborne/Gulf risk, but that does not prove relative upside from here. Neither fund is a fixed conversion of spot crude over a multi-month holding period. Live holdings/weights and NAV premium were not recovered: the issuer page bodies still expose blank dynamic holdings/key-fact fields. [USCF USO](https://www.uscfinvestments.com/uso), [USCF BNO](https://www.uscfinvestments.com/bno).

Refiner options express a different mechanism: realized product margins captured by functioning company assets, weighed against what earnings/valuation already anticipate. Existing L689/L694 work has not established that incremental earnings edge. A new option screen does not repair that missing premise.

## Current price comparison

Yahoo/yfinance snapshot began **2026-10-14 17:30:17 UTC / 13:30 EDT**; underlying regular-market observations were 17:29:51–17:30:12 UTC. USO reference **$154.19**. Vendor says zero-minute underlying delay for USO/BNO and twenty minutes for refiners; quote fields are asynchronous (USO underlying bid/ask154.39/154.42 differs from regularMarketPrice154.19). **Option bid/ask timestamps and quote delay are unavailable. LastTradeDate timestamps trades, not quotes. These are screening inputs, not executable or synchronized broker quotes.** All calls saved in [raw snapshot](vendor-snapshot.json); reproducible arithmetic in [analysis](analysis.json) and [script](analyze.py). Retrieval time is not market observation time.

Entry estimate buys at the displayed long ask and sells at the displayed short bid, multiplied by100. Costs below include **illustrative $0.65/contract opening fees**, not verified account charges. Expiration results exclude closing fees and assignment/exercise costs. No midpoint fills assumed. Standard bull-call-spread payoff mechanics: [Options Industry Council](https://www.optionseducation.org/strategies/all-strategies/bull-call-spread-debit-call-spread).

| Research alternative | Displayed legs | Opening cost / max expiration loss | Expiration breakeven | Maximum expiration profit | Assessment |
|---|---|---:|---:|---:|---|
| **USO Dec18 162/175 spread** | Buy162C ask9.00; sell175C bid5.05 | **$396.30** | **$165.963, +7.64%** | **$903.70** | Preferred research candidate; long+5.07%, short+13.50%; within existing structural geometry |
| USO Dec18 160/175 spread | Buy160C ask9.60; sell175C bid5.05 | $456.30 | $164.563, +6.73% | $1,043.70 | Pays $60 more for earlier participation; long only+3.77%, so do not self-certify compliance with the existing approximately5% long-strike letter |
| USO Dec18 180 outright call | Buy180C ask4.65 | $465.65 | $184.6565, +19.76% | Uncapped | Affordable only with a much more demanding strike; poor default for ordinary continuation |
| BNO Jan15 70 outright call | Buy70C ask4.80 | $480.65 | $74.8065, +14.47% | Uncapped | 93DTE; no listed60–90DTE expiry returned today; outside present structural tenor/registered vehicle |
| BNO Jan15 69/75 spread | Buy69C ask5.20; sell75C bid3.20 | $201.30 | $71.013, +8.67% | $398.70 | Cheaper dollar ticket, but93DTE, other vehicle, gross debit33.333% ofwidth; do not round to33.0% or call eligible |
| VLO Dec18 480/490 spread | Buy480C ask33.00; sell490C bid27.00 | $601.30 | $486.013, +6.45% | $398.70 | Above cap at displayed sides; own-company edge still missing |
| MPC Dec18 500/510 spread | Buy500C ask35.00; sell510C bid29.00 | $601.30 | $506.013, +5.76% | $398.70 | Above cap at displayed sides; own-company edge still missing |
| PSX Dec18 310/320 spread | Buy310C ask16.70; sell320C bid12.50 | $421.30 | $314.213, +6.75% | $578.70 | Fits dollar cap, but much poorer payoff per dollar and friction than preferred USO; same missing earnings premise |

These are bounded examples, not an exhaustive optimization of all strikes. Other refiner spreads can fit the cap by moving strikes; that alone is no reason to select them. The USO structural vehicle/strike/economics letter is not silently imposed as a newly binding refiner rule.

## What the preferred spread actually delivers

At $3.95 gross debit, the $13 width costs **30.3846% of width**, or30.4846% including assumed opening fees, versus the existing33.0% economics ceiling. It puts about$396 at risk for about$904 maximum profit, approximately2.28:1. These are present screening properties, **not an at-fire BG03 grade**. The long strike is5.07% above the quoted underlying reference and the short13.50% above, matching the published shape without changing the tenor or pushing an outright call farther out just to fit the cap.

| USO move by December18, measured from154.19 | USO at expiry | Spread profit/loss after assumed opening fees |
|---|---:|---:|
| Flat | $154.1900 | **−$396.30** |
| +5% | $161.8995 | **−$396.30** |
| +10% | $169.6090 | **+$364.60** |
| +15% | $177.3185 | **+$903.70** |

These are expiration scenarios, not price forecasts, probabilities or expected returns. A modest rally can still lose the entire premium. A rally before expiry can create a different marked result because time and implied volatility remain; no pre-expiry profit amount is forecast. At/above175 the expiration profit is capped. The outright180 call, by comparison, still loses its full premium at+15% and earns only$37.15 at+20% at expiry.

**The cost objection is material:** the displayed immediate liquidation value is only$3.15 (long bid8.75 minus short ask5.60). Crossing both ways plus assumed fees costs **$82.60**, about20.84% of opening outlay. The162C has169 open interest/3 reported volume, and its last trade was October13;175C has2,152 OI/26volume and an October14 trade. A previous trade date does not establish a stale quote, but neither does today's retrieval establish a live one. The175C quote is0.55 wide. Good theoretical geometry does not guarantee a reasonable combination fill; owner/broker confirmation could reject this candidate.

Long162 implied volatility is46.76%, short17548.62%, vendor estimates. Selling the higher-strike call offsets part of the premium and some volatility exposure, in return for capping the tail. No reliable delta/theta/vega, IV rank, historical sector event envelope, calibrated probability of a+7.6% move or volatility-adjusted expected edge was obtained. Do not infer “cheap” from a sub-$500 debit, or predictive skill from the earlier calls' favorable mark.

## Horizon and decision

December18 gives65 days, covering the October15 policy/inventory evidence and a multi-week disruption/winter-demand horizon. It does not require choosing the next few days correctly. More time also costs money: the150C asks14.20($1,420 premium),160C9.60($960),175C5.60($560), before fees; each exceeds the one-card cap. This explains why the spread, rather than an outright near-the-money call, is the useful continuation candidate under current terms. It does not establish December as an optimal holding period.

Today's USO vendor reference is **+0.72%** versus prior close. No direct cheaper-convexity measurement supporting a green-day call exception was made. The BG02 physical head clause has not been established by the new container casualty or the lagged single-vendor AIS diagnostic; WQ192 is not lifted. A successful earlier call is not an entry signal. New162/175 construction changes strike/structure from today's150C; it is a **new deployment**, not a roll exemption.

**BRENT judgment:** keep this USO December162/175 construction as the leading research alternative, decline a buy recommendation on current evidence. Its advantage is intelligible continued crude upside within tenor/cap; its problems are expensive execution friction and an unproved probability/price edge. BNO is a possible separate research alternative if scope/tenor is deliberately changed later, not a workaround today. Refiner options do not presently offer a better-supported substitute.

**Concrete owner-ready next step:** TERRY can evaluate this saved162/175 candidate against an actual broker combination quote, Greek/theta/volatility diagnostics, current book and the exact approval/entry letter; reject it if the spread cannot be traded economically. BRENT's economic question remains whether forthcoming physical evidence improves the case for a sufficiently large crude move, while the October15 worksheet is already prepared. No new mandatory check, threshold, re-arm, scheduled poll, owner dispatch or order created. A different fresh tactical thesis would need its own explicit construction/authority; the structural band is not shortened under a new label.

## Evidence and validation

Reused owned [shipping](../2026-10-14_shipping-check/REPORT.md), [OMR](../2026-10-14_boot-omr/REPORT.md), [expression comparison](../2026-10-12_USO-view/EXPRESSION_COMPARISON.md), TERRY's October12 BNO feasibility note and MPC/L689 card. Current full BG01–09, BH01–16 and TERRY risk/construction rules read before assessment. Source file SHA256 and contract/expiry/strike identity, bid/ask ordering, debit bounds and payoff floor/cap checks recorded in analysis.json. No position, prediction, holding grade, company forecast or THESIS5.13 change.
