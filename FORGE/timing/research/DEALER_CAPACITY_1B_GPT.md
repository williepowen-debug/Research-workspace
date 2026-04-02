# Prompt 1B Response — GPT-5.4
## Basis Trade, MMF Flows, and Issuance Mix

**Source:** GPT-5.4 (via Will)
**Filed:** 2026-03-31

---

The three pressure points are: a still-large but hard-to-measure Treasury basis trade, an MMF sector that has largely redeployed cash from ON RRP into bills and repo rather than leaving the system, and a Treasury issuance mix that is still leaning heavily on bills while long-duration supply keeps coming on a fixed monthly calendar. The net result is that absorption in 2026 depends less on outright "investor demand" than on balance-sheet transmission through hedge funds, MMFs, dealers, and FICC-sponsored repo.

## Basis Trade

A good working estimate for the current cash-futures basis trade is roughly **$1.06 trillion**, based on BIS using OFR/Form PF data for Q2 2025 short Treasury futures linked to basis activity; BIS also says this trade had "largely stagnated" since early 2024, so that figure is still a reasonable anchor for 2026 unless you want a more market-implied proxy. More expansive figures such as $1 trillion-plus of short futures or $1.8 trillion-plus of Treasury holdings capture broader hedge fund Treasury exposure and can overstate pure basis size because they include other relative-value trades and collateral holdings.

On leverage, the clean regulatory benchmark is around **50x** because OFR notes Treasury repo haircuts are typically about 2%, implying maximum leverage of roughly the inverse of the haircut. Market commentary often cites 20x-100x for basis-style books, but the academically grounded number from OFR is that 50x is entirely feasible and small changes in margin or financing can therefore require very large cash outlays.

There is no single universal unwind threshold in basis trades because the trigger is not just a yield move; it is the combination of futures variation margin, cash-bond mark-to-market, repo rollover terms, and whether the cash bond and future diverge. Mechanically, at 50x leverage, equity is about 2% of gross exposure, so a roughly **2% adverse unhedged move wipes out equity**; that corresponds very roughly to about a **25bp move on a 10-year** duration asset with duration near 8, or about a **40bp move on a 5-year** duration asset near 4.5-5, before allowing for hedge offsets. In practice, basis funds can face liquidity stress well before that because variation margin is paid in cash immediately while gains on the cash bond may be illiquid, delayed, or smaller if the basis widens.

For selling pressure, a full unwind of a $1.06 trillion basis book would imply on the order of **$1 trillion of cash Treasury sales**, partly offset by covering of about $1.06 trillion in futures shorts. The cash-market impact matters more for market functioning because those bonds are financed in repo and need balance-sheet space from dealers, sponsors, or end buyers, so even a partial unwind can create hundreds of billions in gross cash selling over a short window.

In March 2020, OFR says Treasury market illiquidity imposed large losses on relative-value hedge funds, many significantly unwound positions, and basis trades were stressed by both margin and rollover risk. OFR's nuanced conclusion is that the evidence "casts doubt" on the claim that basis-trade stress itself was the main amplifier of Treasury illiquidity, though it clearly was a major casualty and an obvious channel for further disruption absent Fed intervention in Treasury and repo markets. The Fed later noted the basis trade was partly unwound in March 2020 and has since risen back above prior peaks.

## MMF Flows

The most important fact on MMFs is that when ON RRP drained, the money mostly did not disappear; Fed staff found that from April 2023 to November 2024, MMFs reduced ON RRP by about **$2 trillion** while increasing allocations by about **$1.8 trillion to Treasury securities** and about **$900 billion to private Treasury-collateralized repo**, including roughly $1.7 trillion more in bills, $600 billion more in overnight Treasury repo, and $300 billion more in term Treasury repo. That is the cleanest empirical map for "RRP depletion → where cash goes."

So for a current MMF complex around **$7.5-$7.9 trillion**, the base case is: cash goes into bills, private repo against Treasury collateral, and cleared/sponsored repo rather than back into Fed RRP.

OFR reported MMF assets at $7.4 trillion at Q1 2025 and over $7.5 trillion in Q2 2025, with repo allocations above $2.8 trillion and then above $3 trillion, while private repo reached $2.5 trillion and then $2.7 trillion.

On the "MMFs handle ~50% of repo" point: the more defensible sourced phrasing is that **MMFs are now a dominant cash lender in repo**, with OFR stating their non-RRP repo reached nearly **a fourth of the estimated $12 trillion U.S. repo market** in Q2 2025. OFR also says more than a third of MMFs' repo exposure was to FICC by Q1 2025, and about a quarter of the growth in repo was via centrally cleared repo.

**Critical insight:** If MMFs shift from RRP to dealer repo and Treasury financing, that generally adds market financing capacity but **not clean dealer warehousing capacity**. MMFs provide the cash leg that funds hedge funds, dealers, and sponsored borrowers against Treasury collateral; this helps Treasury financing clear, but it still relies on dealers or sponsors to intermediate, and OFR stresses that Fed facilities do not pass directly into the markets where basis traders borrow without dealer intermediation.

So MMF migration from RRP to repo is supportive for funding liquidity, but it does **not** remove primary-dealer balance-sheet constraints. If MMFs face redemptions, they can shrink repo lending and bill purchases, which withdraws cash from the exact channels now replacing ON RRP.

### Flow Map
```
ON RRP declines → MMFs reallocate to bills and Treasury repo
More MMF repo cash → more financing for dealers, sponsored repo, and hedge-fund Treasury books
More financing helps market absorption at margin, but by funding levered holders NOT creating true dealer BS inventory capacity
MMF redemptions reverse that support → tighten repo → raise unwind risk for leveraged Treasury trades
```

## Issuance Mix / Auction Calendar

The surge in bill issuance is consistent with deliberate front-loading away from duration stress. The observable fact pattern is that MMFs absorbed a large share of post-RRP cash into bills, while Treasury has continued heavy bill financing and regular coupon issuance — the mix you would expect if officials wanted to exploit the strongest part of the demand curve.

### Long-End Auction Calendar (Apr–Jun 2026)

| Security | Announcement | Auction | Settlement |
|----------|-------------|---------|------------|
| 10Y Note (reopen) | Apr 2 | Apr 8 | Apr 15 |
| 30Y Bond (reopen) | Apr 2 | Apr 9 | Apr 15 |
| 20Y Bond (reopen) | Apr 16 | Apr 22 | Apr 30 |
| 10Y Note (new) | May 6 | May 12 | May 15 |
| 30Y Bond (new) | May 6 | May 13 | May 15 |
| 20Y Bond (new) | May 14 | May 20 | Jun 1 |
| 10Y Note (reopen) | Jun 4 | Jun 10 | Jun 15 |
| 30Y Bond (reopen) | Jun 4 | Jun 11 | Jun 15 |
| 20Y Bond (reopen) | Jun 11 | Jun 16 | Jun 30 |

**Key settlement clusters:** Apr 15, Apr 30, May 15, Jun 1, Jun 15, Jun 30.
**Notable:** Apr 15, May 15, Jun 15 — 10s and 30s settle together.

## Key References
- OFR, "Basis Trades and Treasury Market Illiquidity" (July 2020)
- BIS, "Sizing up hedge funds' relative value trades in US Treasuries and interest rate swaps" (Dec. 2025) — $1.06T estimate
- Fed staff, "Insights from MMF Portfolio Allocations amid Balance Sheet Normalization and Money Market Fund Reforms" (March 2025)
- OFR MMF Monitor blog posts (May and September 2025)

## Thesis Takeaway
Dealer balance sheets are not the whole story: absorption now depends on whether MMF cash keeps funding repo smoothly and whether leveraged hedge-fund intermediation remains intact. If repo cash stays plentiful and basis books stay funded, Treasury selling can be absorbed; **if MMF cash retrenches or basis books face margin-and-roll stress, the same structure can flip from absorber to amplifier very quickly.**
