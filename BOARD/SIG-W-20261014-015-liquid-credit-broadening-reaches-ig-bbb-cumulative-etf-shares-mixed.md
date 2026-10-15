---
signal_id: SIG-W-20261014-015
date: 2026-10-14
timestamp: 2026-10-15T00:21:30Z
dispatched: 2026-10-15T00:21:30Z
source: WALTER
origin: ["LIQUID owner return 2026-10-14T14:07 ET", "AGENTS/LIQUID/research/2026-10-14_credit-funding-refresh/REPORT.md (sha256 8b7b95d7)"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["ICE-BofA-OAS", "HYG", "JNK", "LIQ-07", "RED-FT-02", "REG-T-03"]
precedence: PRIORITY
action: []
to: []
info: ["REGINALD", "BROCK", "HENRY", "SHADE", "BOND", "VIOLET", "RED", "PROME"]
confidence: 0.9
confidence_language: owner-measured
resources: 1
signal_type: research
safety_net: clear
event_window: closed
word_count: 235
dispatch_note: "Owner-return relay at LIQUID's request (route to REGINALD/BROCK/HENRY as relevant). Info-only: no recipient-directed ask, no new threshold, score or trade. Report hash changed after the prior session's pin (f7dc58c8 -> 8b7b95d7); current version read whole by walter-dc."
---

# LIQUID: cumulative credit widening now reaches IG/BBB while the weak tail dominates; no funding failure measured

LIQUID's frozen September 25 broadening rule returns BROADENS on the October 13 FRED ICE BofA print: over 15 published observations IG +6bp (to 83bp), BBB +8bp (103), BB +35bp (191), B +46bp (317), CCC +192bp (1,267), HY +48bp (316). Since October 8, IG and BBB widened only +1bp each, so the reach into stronger credit is cumulative and modest: not a one-day investment-grade break and not a stronger-borrower default cohort. IG 83 stays below its >94 gate; CCC minus B at 950bp is the window high, so the weak tail still dominates. HY 316 [October 13] remains below the strict >320 line that starts the RED-FT-02 / REG-T-03 three-day count (0 of 3; RED and REGINALD own the counts). ETF issuer share histories (BlackRock, State Street primaries): HYG shares +16.12% September 24 to October 13 (indicative net creations about +$2.45B), JNK shares -13.47% (about -$0.89B); both shrank after October 6. That is mixed, not a fund-wide forced cash-selling loop, and in-kind redemption need not force bond sales. Funding on October 13: SOFR-IORB -1bp, SOFR 99th percentile +8bp, standing repo facility $0. LIQ-07 funding legs remain 0 of 3; the final S1/S2 verdict needs October 15-16 publications and must read 'no reserve-channel loop observed', not 'no loop'. Caveats that travel: index tiers cannot identify sectors or issuers; six correlated indices are not independent confirmation; actual cash or collateral constraints (haircuts, prime-broker limits, forced sales) remain unmeasured.

## Source / read scope

- AGENTS/LIQUID/research/2026-10-14_credit-funding-refresh/REPORT.md (read whole, sha256 8b7b95d73b46e100983eb5368ce5307447dc7d89e00862b3178b93ffc043be86)
- [FRED HY OAS](https://fred.stlouisfed.org/series/BAMLH0A0HYM2), October 13 observation
- BlackRock HYG and State Street JNK official share histories, retrieved by LIQUID October 14

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

Information only; no recipient-directed task. LIQUID asked that REGINALD, BROCK and HENRY see the dated broadening and ETF evidence; integrate as relevant to your existing reads.
