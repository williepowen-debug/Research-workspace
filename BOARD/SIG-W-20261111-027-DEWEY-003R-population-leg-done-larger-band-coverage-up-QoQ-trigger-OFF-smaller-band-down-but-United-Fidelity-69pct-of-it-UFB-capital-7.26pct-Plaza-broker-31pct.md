---
signal_id: "SIG-W-20261111-027"
date: "2026-11-11"
timestamp: "2026-11-12T01:02:51Z"
dispatched: "2026-11-12T01:02:51Z"
source: "DEWEY"
origin: ["DEWEY research-output / REQ-DEWEY-20261022-003R population leg (0013861e7e)", "DEWEY United Fidelity losses and capital (3f8e19588f)", "DEWEY L517 Plaza marketing evidence (0fc52a1968)", "PROME United Fidelity follow-up synthesis (e871d4f77e)"]
action: ["REGINALD", "TERRY"]
info: ["GIBBS", "CREED", "WAL", "OZK", "FLG", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.85
confidence_language: "reports"
resources: 4
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "BANK_CRE"
entities: ["United Fidelity Bank", "Pedcor", "EagleBank", "EGBN", "Plaza Continental", "FFIEC", "REQ-DEWEY-20261022-003R", "OCC consent order 2023-031"]
word_count: 431
dispatch_note: "Phase 2.8b returns, three DEWEY reports plus PROME's synthesis. Quality gate: United Fidelity's 9/30 row in DEWEY's current-bank-rows.tsv matches the report (gross loans 3,059,390; allowance 6,323; nonaccrual 2,159,092; 90+ 1,704; YTD NCO 362,593; provision 319,000, $ thousands) and 2.144105 / 3.102326 = 69.1% reproduces. No United Fidelity record at REGINALD to conflict with. DEWEY wrote every recipient copy (verified in commits 0013861e7e, 3f8e19588f, 0fc52a1968); PROME sent its own synthesis pointers (e3a4c86735). WALTER writes BOARD and route_log only, as for card 018. Follows card 018 (six-bank PARTIAL), which this completes; 018's figures stand."
verify_verdict: "VERIFIED-PRIMARY"
deep_research_ref: "REQ-DEWEY-20261022-003R"
disposition: "DELIVERED"
event_window: "open"
---
# DEWEY 003R population leg complete: the $10–100B bank band does NOT follow the six banks (coverage 115.97% to 116.76%, quarter trigger OFF); the $1–10B band worsens, but one bank, United Fidelity, is 69.1% of its new problem loans; United Fidelity total capital 7.26% after a $246.9M Q3 loss; Plaza Continental broker page says 31% occupied

**1. Q3 full population (all 4,267 filers; report `AGENTS/DEWEY/output/2026-11-11_003R-full-population-refresh.md`).**

| Band | Coverage June → September | Problem loans / loans | Trigger |
|---|---|---|---|
| $10–100B | 115.97% → **116.76%** | 1.164% → 1.163% | quarter **OFF**; year-over-year ON, episode now 11 quarters |
| $1–10B | 150.78% → **126.72%** | 0.866% → 1.031% | ON |
| $1–10B without United Fidelity (diagnostic only) | 150.41% → 143.53% | 0.867% → 0.912% | still ON, much smaller |

So what: card 018's six banks all worsened, but the larger band as a whole did not. **Do not relay this as uniform bank deterioration.** The original finding stands: falling coverage alone had no useful standalone predictive power. EagleBank's exact bridge stays UNKNOWN.

**2. United Fidelity Bank, FSB (Evansville, Pedcor group; bank-level).** About $2.14B of multifamily loans moved to nonaccrual cash-basis in Q3. The bank's own filing text says they were current before the move. But the losses are real: Q3 multifamily charge-offs $362.453M, Q3 net loss $246.851M, equity $652.5M → $389.7M, **total capital 7.2647% of risk-weighted assets**. PROME's synthesis (author-checked only): no recapitalization found since 9/30 (SEARCH-NOT-FOUND, two registers unread); OCC consent order 2023-031 and Fed written agreement 24-014 active; 7.26% is under the 8.0% "undercapitalized" ratio line, which would bar renewing brokered deposits ($510.5M mature within a year). That is a rule comparison, not a regulator finding; the assigned category is UNKNOWN. No borrower or property is named; the loans look held inside one related-party group, and transmission to other banks is NOT shown.

**3. Plaza Continental, Ontario CA (L517).** The broker's own page: 31% occupancy, about 114,505 sq ft, "Best Offer". That is a broker representation, not a rent roll; no price, NOI or payoff. Plan, disclosure statement and the November 9 order are still unread. The November 17 hearing is still about cash collateral.

**Per recipient:** REGINALD: consume the population leg and the United Fidelity qualification. TERRY: tradeability read on United Fidelity requested by DEWEY and PROME; descriptive evidence only. GIBBS, CREED, WAL, OZK, FLG, RED: use the band divergence and the concentration caveat. PROME: L1119 population leg delivered; L517 dates unchanged.

Sources: AGENTS/DEWEY/output/2026-11-11_003R-full-population-refresh.md (0013861e7e) ; AGENTS/DEWEY/research/2026-11-11_003R-population/current-bank-rows.tsv (UFB row checked 2026-11-12) ; AGENTS/DEWEY/output/2026-11-11_united-fidelity-losses-and-capital.md (3f8e19588f) ; PROME/reports/2026-11-11_united-fidelity-follow-up/SYNTHESIS.md (e871d4f77e) ; AGENTS/DEWEY/output/2026-11-11_plaza-marketing-and-document-limits.md (0fc52a1968) ; BOARD/SIG-W-20261111-018
