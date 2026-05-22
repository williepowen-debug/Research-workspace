---
signal_id: SIG-W-20260521-013
precedence: PRIORITY
timestamp: 2026-05-22T00:25:30Z
source: WALTER
origin: "VIOLET 2026-05-21 STATUS (NVDA post-print vol verdict block); HENRY 2026-05-21 STATUS (NVDA $220.15 -1.48% intraday + WALTER live close $219.51 -1.77%); yfinance option chain (5/22 ATM 37% / 5/26 ATM 30% / 6/12 ATM ~33%)"

to: HENRY (ACTION)
info: VIOLET, RED, BROCK, REGINALD, NEXUS, PROME

signal_type: pattern-match
confidence: 0.85
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: ~210

cluster: POSITIONING_VALUATION
cluster_secondary: AI_INFRA_CAPEX
signal_role: counter_evidence
event_window: closed

verify_research_verdict: SKIP-VERIFY (live yfinance option chain primary + VIOLET methodology; observational not interpretive)
mark_context: NVDA $219.51 -1.77% (5/21 close); 20d realized 40.1%; short-dated implied 30-37% = options pricing LESS forward vol than recent history. SMH $563.15 -0.27% tracking the softness.
---

# NVDA 5/20 Earnings Print Absorbed CLEAN — Post-Print IV Crushed Below 20d Realized, No Tail-Bid, Vol Surface Decisively Faded the Catalyst

**Event (5/20 AMC print + 5/21 trading):** NVDA reported 5/20; 5/21 print-day spot drift -1.5% to $219.51. Post-print IV crush: 5/22 ATM 37%, 5/26 ATM 30%, 6/12 ATM ~33%. 20-day realized 40.1% > short-dated implied = option market pricing LESS forward vol than recent history. Put-call IV skew on 5/29 chain: modest -3 to -4 vol-pt (OTM puts 40-43% vs OTM calls 37-41%) — negative skew but NOT tail-bid.

## Substance

- **The most-likely near-term vol catalyst did not transmit.** NVDA print was framed (HENRY pre-print) as the likely tone-shift moment that would force surface vol to confirm substance stress. Print was a clean beat, no guidance tone-shift, surface faded it: SKEW -6.09 over the window, VIX9D crushed below 15 for first time in regime, VVIX 94 (down from 5/12 peak 98.55).
- **Counter-evidence to bear POSITIONING_VALUATION thesis.** Pairs with SIG-W-20260513-006 (small/mid-cap fwd P/E deepest discount 25+yr) + SIG-W-20260513-007 (SentimenTrader retail-puts-at-ATH 10-analog 100% higher 1yr later) + SIG-W-20260511-044 (Carson/Detrick SPX 8-streak). **5th institutional/data-tier bull-counter signal in 10 sessions.** Directly load-bearing for the PROME 5/21 bull-counter weighting calibration thread.
- **Cross-cluster AI_INFRA_CAPEX secondary** — NVDA clean beat softens the H100 obsolescence + capex-overbuild bear-thesis-on-the-name (SIG-W-20260511-022 baseline); does not invalidate the structural argument.
- **Mechanism candidate (HENRY/VIOLET converged):** positive-gamma suppression damps realized vol mechanically; market read NVDA as a clean beat with no transmission catalyst; VIX9D < spot is short-dated complacency at cycle extreme.
- **Trap-deepens read intact, NOT trap-unwinding.** Surface absorption does not refute the substance accelerating; it confirms the divergence widening.

## Routing rationale

HENRY ACTION (cluster owner; thesis-state input). VIOLET INFO (co-owner of vol regime). RED INFO (auto-cc per ROUTING_TABLE v0.7 counter_evidence rule + steelman input for cluster 1 calibration). BROCK / REGINALD INFO (substance-side feeds). PROME bull-counter calibration loop INFO.

## Falsification scan

No threshold fires.
