---
signal_id: SIG-W-20261014-017
date: 2026-10-14
timestamp: 2026-10-15T00:21:30Z
dispatched: 2026-10-15T00:21:30Z
source: WALTER
origin: ["BOND owner return 2026-10-14 (cutoff 13:59 ET)", "AGENTS/BOND/analysis/2026-10-14_post-CPI/REPORT.md (sha256 264ac2eb)"]
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
entities: ["UST-10Y", "UST-30Y", "fed-funds-futures", "ACM-term-premium", "Beige-Book"]
precedence: PRIORITY
action: []
to: []
info: ["HENRY", "LIQUID", "MIDAS", "CARL", "RED", "TERRY", "PROME"]
confidence: 0.85
confidence_language: owner-measured, vendor intraday basis
resources: 1
signal_type: research
safety_net: clear
event_window: closed
word_count: 243
dispatch_note: "Owner-return relay at BOND's request (existing rates/metals/funding recipients). Info-only. Vendor intraday quotes, not official closes; the official October 14 curve, ACM row and repo transactions were unpublished at BOND's cutoff."
---

# BOND: the CPI-day jump in 10-year yields retraced by 14:00; futures priced a firmer Fed path; funding dysfunction not established

After the 08:30 ET CPI release the 10-year yield jumped 7.3bp in two minutes (5.190% to 5.263%, Yahoo/CBOE one-minute index) and peaked near 5.33% before retracing. By 13:58-13:59 ET versus the prior close (CNBC vendor quotes, not official constant-maturity yields): nominal 10Y -0.6bp, made up of real yield -2.1bp and inflation compensation +1.5bp; 2Y +3.4bp, 30Y -2.4bp, so the curve flattened (2s10s -4.0bp). Fed-funds futures (Yahoo bars captured 13:58 ET, not CME settlements): November implied 3.970% versus 3.935% (+3.5bp), which BOND converts to roughly a 36% proxy for a +25bp move at the October 28 FOMC versus 22% on the prior bar; this is a risk-neutral proxy, not a FedWatch probability, and must not be added to the real-yield split. ACM 10-year term premium 0.851% [October 13] fell 5.1bp October 9 to 13, before CPI. Funding: October 13 SOFR 3.89% vs IORB 3.90%, which predates CPI; no margin, fails or haircut data. October 14 Beige Book: supply-cost pressure, subdued spending and employment (contacts collected on or before October 5). BOND's judgment: inflation pressure persists but this was not a sustained long-end selloff at the cutoff, and market-wide Treasury dysfunction is not established (not certified absent either). Position relevance: the surviving duration-short holding is TBT x5 per FORGE's October 14 broker receipt, under the existing WQ-357 decision clock; TERRY constructs and Will orders. Next tests: the official October 14 nominal/real close (BOND, October 15), PPI October 15, FR2004 dealer positions as of October 7.

## Source / read scope

- AGENTS/BOND/analysis/2026-10-14_post-CPI/REPORT.md (read whole, sha256 264ac2eb6cf746821ca12515d479d2e7ccf80d78006bd5bc151b02717ffb1d49)
- [BLS CPI September](https://www.bls.gov/news.release/archives/cpi_10142026.htm)
- [Beige Book October 2026](https://www.federalreserve.gov/monetarypolicy/beigebook202610-summary.htm)

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

Information only; no recipient-directed task. HENRY owns the policy-path series; LIQUID owns the funding verdict; MIDAS may use the real-yield split.
