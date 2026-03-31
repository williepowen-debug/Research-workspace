# Prompt: Dealer Balance Sheet Capacity vs. Treasury Supply — The Absorption Bottleneck

## Context

The US Treasury market has grown enormously while primary dealer capacity to intermediate has not kept pace:
- Treasury debt outstanding: ~$36T (up ~139% since 2010)
- Primary dealer net positions in Treasuries: grew only ~29% over the same period
- Harvard Business School finding (Vissing-Jorgensen): Treasury demand is now **5x more inelastic** than pre-2010 — 9bps yield move per 1% supply increase vs 2bps historically
- Federal Reserve: no longer a marginal buyer (QT ongoing, balance sheet declining)
- Foreign official sector: Japan life insurers structurally withdrawing ($50-120B annual swing from buyer to neutral/seller), China diversifying, Gulf recycling broken by war

**The concern (March 2026):**

Multiple large holder classes may become forced sellers simultaneously:
1. **Private credit funds** liquidating to meet redemptions (7+ funds gated, Goldman projects $45-70B outflows)
2. **PE-controlled insurers** selling liquid Treasuries to meet FHLB/FABN obligations and cover illiquid PC losses
3. **Japan** — life insurers reducing UST holdings (hedge ratio collapsed 60%→45.7%, hedged UST return now -0.34% vs JGB 2.27%). FY-end Mar 31 + BOJ hike expected May 1
4. **China/Gulf** — structural demand withdrawal ($70-135B/mo combined selling estimated)
5. **Banks** — may need to sell Treasuries to meet quarter-end liquidity requirements (already experienced in Mar 2023 SVB episode)

If all five sell into a market where dealers can only absorb a fraction of pre-2010 volumes, spreads blow out and the Treasury market becomes the transmission mechanism rather than the safe haven.

**Current plumbing stress indicators:**
- Fed's Perli (Mar 26): reserve ampleness metrics at **Q1 2019 levels** — the quarter before the Sep 2019 repo crisis
- Reverse repo (RRP): effectively zero ($0.99B) — no buffer
- Standing Repo Facility (SRF): $74.6B record usage (Dec 31, 2025), 38bps above SRF rate
- Reserves: $2.8T at Waller's $2.7T "problematic" boundary, concentrated in G-SIBs
- MMF assets: record $7.86T, now intermediate ~50% of repo transactions
- SOFR: 3.63, with quarter-end spike expected Mar 31

## Questions

1. **Quantify dealer intermediation capacity.** What's the actual balance sheet capacity of the 24 primary dealers to absorb Treasury selling? How much can they warehouse at any given time? What's the binding constraint — leverage ratios (SLR), VaR limits, or balance sheet size? How has the Volcker Rule / Basel III / SLR affected their capacity vs pre-2010?

2. **What happens when selling volume exceeds dealer capacity?** In theory, prices adjust until buyers appear. In practice:
   - Oct 2014 flash crash: 12-minute, 37bp move in 10Y with no fundamental catalyst
   - Mar 2020 Treasury market seizure: $1.6T in selling, bid-ask spreads blew out 8-10x, Fed bought $1T+ in weeks
   - Sep 2019 repo crisis: overnight repo spiked to 10% because reserves were maldistributed
   
   For each episode: how much selling triggered the dislocation, and how does that compare to potential 2026 forced selling volumes?

3. **Model the simultaneous seller scenario.** If private credit funds ($45-70B), insurers (unknown — help me size this), Japan ($50-120B/yr), and China/Gulf ($70-135B/mo) all reduce Treasury holdings in the same quarter:
   - What's the total quarterly selling volume?
   - How does this compare to dealer capacity?
   - What yield adjustment would be needed to attract replacement buyers?
   - At what yield level do other buyers (pensions, retail, SWFs) step in?

4. **The MMF intermediation problem.** MMFs now intermediate ~50% of repo transactions. They parked cash at the Fed's RRP facility, which is now effectively zero. Where does that $7.86T go? If MMFs shift from RRP → dealer repo → Treasury financing, does this help or hurt? What happens if MMFs themselves face redemptions (because their FABN holdings get downgraded, or because investors rotate to T-bills directly)?

5. **Treasury issuance schedule.** The Treasury has shifted heavily toward T-bill issuance ($195B → $352B in 12 weeks, exceeding COVID peak). Is this deliberate front-loading to avoid long-duration auctions during stress? What's the upcoming auction schedule for 10Y, 20Y, 30Y through June 2026? Any particularly large settlements that could strain the system?

6. **The "buyer of last resort" question.** In 2020, the Fed stepped in as buyer of last resort within 2 weeks of Treasury market seizure. In 2026:
   - PCE is above target (3.1%+). Can the Fed buy Treasuries without re-igniting inflation?
   - Would they use the SRF (lending against Treasuries) rather than outright purchases?
   - Is there a scenario where the Fed is forced to choose between Treasury market stability and inflation mandate?
   - What's the political/legal framework for emergency Treasury purchases when inflation is above target?

7. **Cross-reference with SOFR/repo stress.** If Treasury market liquidity deteriorates:
   - SOFR spikes (Treasury collateral worth less in repo)
   - Basis trades blow up (leveraged Treasury positions unwind)
   - Hedge funds forced to sell (they hold ~$1T in leveraged Treasury positions via basis trade)
   - This ADDS to selling pressure — a feedback loop
   
   How large is the basis trade currently? At what Treasury yield move do basis trade unwinds become forced?

## What I Want Back

- Dealer capacity estimates ($ terms) with binding constraints identified
- Historical dislocation data: selling volume → price impact for Oct 2014, Mar 2020, Sep 2019
- Simultaneous seller scenario: total volume estimate and yield impact model
- MMF flow analysis: where does $7.86T go without RRP?
- Assessment of Fed capacity to intervene given inflation constraint
- Basis trade size and unwind thresholds
- Any papers from BIS, OFR, Fed staff, or TBAC on Treasury market liquidity and dealer capacity
