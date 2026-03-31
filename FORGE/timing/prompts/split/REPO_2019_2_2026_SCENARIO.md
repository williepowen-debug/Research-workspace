# What Does a 2019-Style Repo Crisis Look Like With 2026 Vulnerabilities?

## What I Need

A scenario model: a September 2019-style repo spike happens on or around March 31, 2026 — but under much worse conditions. What breaks, what's the transmission, and can the Fed contain it?

## Context — Why 2026 Is Worse Than 2019

| Factor | Sep 2019 | Mar 2026 |
|--------|----------|----------|
| Reverse Repo (RRP) | ~$200B+ buffer | $0.99B (zero) |
| Reserves | ~$1.5T (declining) | $2.8T but concentrated in G-SIBs, at Waller's $2.7T "problematic" boundary |
| Standing Repo Facility | Did not exist | Exists but $74.6B record usage Dec 31 2025, leaked 38bps above offered rate |
| MMF assets | ~$3.4T | $7.86T (2.3x larger, now intermediate ~50% of repo) |
| Treasury outstanding | ~$22T | ~$36T (+64%) |
| Private credit | No stress | $1.7T+, 7+ funds gated, CCC OAS 1,013 |
| Oil shock | None | Brent $107-108, gas at $4 behavioral breakpoint |
| Inflation | Below target (Fed free to act) | PCE above target (Fed constrained) |
| Basis trade | Smaller | ~$1T in leveraged hedge fund Treasury positions |

**March 31 specific:** Japan FY-end (GPIF rebalancing, life insurer repatriation = dollar selling), US Q1 close (window dressing), 20Y Treasury settlement same day, corporate tax payments, zero RRP release valve.

## Questions

1. If SOFR spikes 50-100bps on March 31 or April 1, what's the cascade?
   - Does a spike trigger margin calls on the ~$1T basis trade? At what SOFR level?
   - If PC funds are simultaneously meeting redemptions, do they sell repo collateral into the spike?
   - If Japanese institutions are repatriating, are they withdrawing dollar liquidity from repo markets?

2. Can the Fed contain it? In 2019, inflation was below target so the Fed acted immediately and aggressively. In 2026 with PCE above target:
   - Can they inject repo liquidity without signaling rate cuts?
   - Is the SRF sufficient? It's limited to primary dealers and certain banks — MMFs, insurers, and hedge funds can't access it directly.
   - Would they need emergency Treasury purchases (like March 2020's $1T+ in 3 weeks)? Can they do that with inflation above target?

3. What's the difference between "contained plumbing stress" (2019 outcome) and "dash for cash" (2020 outcome)? What tips it from one to the other? Specifically: does simultaneous credit stress (PC gating, insurer pressure) turn a plumbing event into a liquidity crisis?

4. What should I monitor in real-time? For each indicator, give me three levels: normal quarter-end, 2019-repeat, and worse-than-2019:
   - SOFR and SOFR-IORB spread
   - SRF daily usage
   - Tri-party repo rates
   - DTCC settlement fails
   - Treasury bid-ask spreads

## What I Want Back

A scenario narrative: what happens hour by hour / day by day if repo spikes under 2026 conditions. Where are the circuit breakers, and are any of them disabled? What's the most likely Fed response and is it sufficient? Give me a monitoring checklist with specific alarm levels.
