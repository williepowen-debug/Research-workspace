# Prompt: What's the 2026 Equivalent of LIBOR-OIS?

## Context

In 2007-2008, the LIBOR-OIS spread was THE key indicator of interbank stress. It went from ~10bps pre-crisis to 70bps on Aug 9 (BNP Paribas), then above 100bps by September, and eventually spiked to 364bps after Lehman. It told you in real-time that banks didn't trust each other.

LIBOR no longer exists (replaced by SOFR in 2023). I'm trying to identify what spread or indicator plays the same role today — specifically, what would tell us that financial institutions are starting to doubt each other's solvency or refuse to lend to each other.

## Current Market Context (March 2026)

- SOFR: 4.30%
- Fed Funds: 4.33%
- HY OAS: 342bps (widening)
- CCC OAS: 1,013bps
- VIX: ~30
- The Fed's Reverse Repo (RRP) facility is effectively at zero ($0.99B)
- Bank reserves are at $2.8T (4-year low), concentrated in G-SIBs
- Quarter-end (March 31) is tomorrow — SOFR typically spikes at quarter-ends
- Private credit funds are gating redemptions; insurance companies under scrutiny

## Questions

1. **What specific spread or indicator replaces LIBOR-OIS as the counterparty risk signal in 2026?** Candidates I'm considering:
   - SOFR vs Fed Funds effective rate
   - SOFR vs IORB (Interest on Reserve Balances)
   - FRA-OIS spread
   - Cross-currency basis swaps (USD/JPY, USD/EUR)
   - Bank CDS spreads (individual or index)
   - Commercial paper spreads vs T-bills
   
   Which of these is the best real-time signal? Why?

2. **What are the current levels of each candidate spread, and what levels would indicate stress?** Give me a table with: indicator, current level, "watch" level, "alarm" level, and the 2007-08 equivalent peak.

3. **LIBOR-OIS spiked on August 9, 2007 (BNP Paribas) and never fully normalized until after massive Fed intervention.** What would be the equivalent "spike day" trigger in the current environment? A private credit fund freeze? A CLO manager halt? A repo market seizure?

4. **The Standing Repo Facility (SRF) was created post-2019 repo crisis as a backstop.** In December 2024, banks drew $74.6B from SRF at quarter-end. If SRF usage spikes significantly above that level at tomorrow's quarter-end, is that a LIBOR-OIS equivalent signal? Or is SRF usage "normal plumbing" that shouldn't be read as stress?

5. **In 2007, LIBOR-OIS distinguished between a credit problem and a liquidity problem.** High LIBOR-OIS = banks won't lend to each other (credit risk). In 2026, where is the line between "normal tightening" and "counterparty risk is being priced"?

6. **Cross-currency basis swaps** — in 2007-08, the EUR/USD and JPY/USD basis swaps blew out as non-US banks scrambled for dollar funding. Is this happening now? Japan is at FY-end, and Japanese banks are major dollar borrowers. Would a spike in the JPY/USD cross-currency basis swap be an early warning?

## What I Want Back

- A ranked list of the best LIBOR-OIS replacement indicators for 2026, with current levels
- Specific threshold levels that would indicate we've entered a stress regime
- The trigger scenario most likely to cause a spike
- Any indicators that are ALREADY showing stress that most people aren't watching
- If there's academic work on post-LIBOR interbank stress measurement, cite it
