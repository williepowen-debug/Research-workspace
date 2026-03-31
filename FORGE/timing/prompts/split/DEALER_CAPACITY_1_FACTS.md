# Prompt 4A: Primary Dealer Intermediation Capacity — Factual Reconstruction

## Your Task
Quantify the actual balance sheet capacity of US primary dealers to absorb Treasury selling in 2026. I need hard numbers, not narratives.

## Context You Need

The US Treasury market has grown ~139% since 2010 (to ~$36T outstanding) while primary dealer net positions grew only ~29%. Harvard's Vissing-Jorgensen found Treasury demand is now **5x more inelastic** than pre-2010 — a 1% supply increase moves yields 9bps vs 2bps historically. Meanwhile, the Fed is still running QT and multiple large holder classes may become forced sellers simultaneously in 2026.

**Current plumbing stress (as of March 2026):**
- Fed's Perli (Mar 26): reserve ampleness metrics at **Q1 2019 levels** — the quarter before the Sep 2019 repo crisis
- Reverse repo (RRP): effectively zero ($0.99B) — no buffer
- Standing Repo Facility (SRF): $74.6B record usage (Dec 31, 2025), 38bps above offered rate leaked
- Reserves: $2.8T at Waller's $2.7T "problematic" boundary, concentrated in G-SIBs
- MMF assets: record $7.86T, now intermediate ~50% of repo transactions

## Questions

1. **What is primary dealer aggregate balance sheet capacity for Treasuries?** Give me: total net positions (latest FR 2004 data), gross long/short, how this has evolved since 2010. What's the maximum they've ever held? What's the binding constraint on expansion — SLR, VaR limits, internal risk limits, or balance sheet size?

2. **How did Basel III / SLR / Volcker Rule change dealer capacity?** Before 2010, dealers could warehouse Treasuries more freely. Quantify the capacity reduction. The SLR treats Treasuries identically to corporate bonds for leverage ratio purposes — how much capacity does this specifically remove? There was a temporary SLR exemption in 2020 — what was its impact on dealer activity, and what happened when it expired?

3. **Historical dislocation data.** For each episode, give me: the selling volume that triggered it, the price impact, the duration, and how dealers responded:
   - **Oct 15, 2014 Treasury flash crash**: 37bp move in 10Y in 12 minutes
   - **Sep 16-17, 2019 repo crisis**: overnight repo to 10%
   - **Mar 2020 Treasury market seizure**: $1.6T in selling, bid-ask blew out 8-10x
   - **Oct 2023 term premium repricing**: 10Y to 5%, auction tails

4. **The basis trade.** Hedge funds hold an estimated ~$1T in leveraged Treasury basis positions (long cash, short futures). How large is this currently? What's the leverage (typically 50-100x)? At what yield move do margin calls force unwinds? How much additional selling does a basis trade unwind generate? What happened to basis trades in March 2020?

5. **MMF as intermediary.** MMFs now handle ~50% of repo. With RRP at zero, where does $7.86T in MMF cash go? If MMFs shift from RRP → dealer repo → Treasury financing, does this add to or subtract from dealer capacity? What happens if MMFs face redemptions themselves?

6. **Treasury issuance composition.** T-bill issuance surged $195B→$352B in 12 weeks (exceeds COVID peak). Is this deliberate front-loading to avoid long-duration stress? What's the upcoming 10Y/20Y/30Y auction schedule through June 2026? Any outsized settlements approaching?

## What I Want Back

- Primary dealer aggregate position data ($ terms, time series if available)
- Binding constraint analysis: which regulation caps capacity and by how much
- Table of historical dislocations: trigger volume → price impact → duration → resolution
- Basis trade: current size, leverage, unwind threshold (bps move), estimated selling on unwind
- MMF flow map: RRP depletion → where cash goes → implications for repo/Treasury market
- Upcoming auction calendar with sizes
- Any OFR, BIS, Fed staff, or TBAC papers on Treasury market liquidity and dealer capacity constraints
- NY Fed Liberty Street blog posts on market functioning
