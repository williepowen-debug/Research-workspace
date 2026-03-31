# Prompt 4B: Simultaneous Seller Scenario — Treasury Market as Transmission Mechanism

## Your Task
Model what happens when multiple large holder classes sell Treasuries simultaneously into constrained dealer capacity in Q2-Q3 2026. I need a flow-of-funds scenario with numbers.

## Context You Need (confirmed from prior research)

**Potential forced sellers in 2026:**

| Seller Class | Estimated Quarterly Selling | Mechanism | Confidence |
|---|---|---|---|
| **Private credit funds** | $15-25B | Liquidating to meet redemptions; 7+ funds gated; Goldman projects $45-70B annual outflows | Medium-high |
| **PE-controlled insurers** | $10-30B | Selling liquid Treasuries to cover FABR/FABN gaps and illiquid PC losses; $48B combined funding gap at Athene alone if FABN market closes | Medium |
| **Japan life insurers** | $12-30B | Structural withdrawal; hedge ratio collapsed 60%→45.7%; hedged UST return now -0.34% vs JGB 2.27%; $50-120B annual swing | High |
| **China/Gulf sovereign** | $20-45B | Structural demand withdrawal; Ghalibaf UST-buyer targeting; Gulf recycling broken; $70-135B/mo combined | Medium |
| **Hedge fund basis unwind** | $50-200B | ~$1T leveraged positions; margin calls on yield spike force unwind; 50-100x leverage | Conditional on yield spike |

**Dealer constraints:**
- Primary dealer net Treasury positions: ~$65-85B (far below pre-2010 capacity relative to market size)
- SLR treats Treasuries same as corporate bonds for leverage ratio
- VaR limits bind when volatility spikes (MOVE index)
- Dealers stepped BACK in March 2020 — they didn't absorb, they widened spreads

**Plumbing already stressed:**
- Reserves at $2.8T (Waller's $2.7T boundary), concentrated in G-SIBs
- RRP buffer: zero
- SRF already leaked 38bps above offered rate on Dec 31 2025
- SOFR elevated, quarter-end spike expected

**Fed constrained:**
- PCE above target (~3.1%+), oil shock pushing higher
- In 2020, Fed bought $1T+ Treasuries in weeks — politically impossible with inflation above target
- SRF can lend against Treasuries but doesn't remove selling pressure (temporary liquidity, not absorption)
- "Choose between Treasury market stability and inflation mandate" scenario is live

## Questions

1. **Size the quarterly selling.** Sum the forced sellers above. What's a plausible Q2 2026 scenario? What's the worst case? Compare to: normal quarterly Treasury market turnover, the $1.6T that broke the market in March 2020, and dealer capacity.

2. **Model the price impact.** Using Vissing-Jorgensen's 9bps/1% supply elasticity and historical dislocation data: if net selling exceeds dealer capacity by $X billion, what yield adjustment is needed to attract replacement buyers? At what yield level (10Y) do the following buyer classes step in?
   - US pension funds (currently underfunded, would buy duration at the right price)
   - Retail / TreasuryDirect
   - Sovereign wealth funds (non-adversarial — Norway, Singapore, etc.)
   - Banks (if SLR is temporarily exempted again)

3. **The cascade feedback.** Treasury yield spike → basis trade unwind → more selling → wider spreads → dealers step back → more yield spike. Map this feedback loop. How much additional selling does the basis trade generate? Is there a natural stopping point, or does this require Fed intervention?

4. **Fed response options under inflation constraint.** Rank these by likelihood and effectiveness:
   - SRF expansion (lending against Treasuries, not buying)
   - Temporary SLR exemption for Treasuries (frees dealer capacity)
   - Targeted Treasury purchases (specific maturities, sterilized?)
   - Twist operation (sell bills, buy bonds — neutral balance sheet)
   - Emergency rate cut (nuclear option — signals panic, worsens inflation)
   - New facility (BTFP 2.0 for Treasury collateral)
   
   Which combinations are most likely? What's the political barrier to each?

5. **The "safe haven breaks" scenario.** In every prior crisis, Treasuries rallied as the safe haven. What happens in a crisis where Treasuries ARE the problem? Where does the flight-to-safety money go? Gold? Swiss francs? JGBs? Cash? If Treasuries lose safe-haven status even temporarily, what are the second-order effects on collateral chains, margin requirements, and bank capital?

6. **Timeline.** Give me an hour-by-hour / day-by-day scenario for how a Treasury market dislocation unfolds in Q2 2026, from first stress signal to Fed intervention. Include specific trigger points (auction fails, SOFR spike, MOVE index level, basis trade margin calls).

## What I Want Back

- Quarterly selling volume estimate (base case and stress case, $ terms)
- Yield impact model: selling volume → 10Y yield → buyer step-in levels
- Feedback loop map: Treasury stress → basis unwind → dealer withdrawal → more stress
- Fed response ranking: option → likelihood → effectiveness → political barrier
- "Safe haven breaks" scenario: capital flow map if Treasuries lose haven status
- Day-by-day timeline: trigger → cascade → intervention → resolution
- The key question: **is the Treasury market the circuit breaker (absorbing stress) or the amplifier (transmitting it) in 2026?**
