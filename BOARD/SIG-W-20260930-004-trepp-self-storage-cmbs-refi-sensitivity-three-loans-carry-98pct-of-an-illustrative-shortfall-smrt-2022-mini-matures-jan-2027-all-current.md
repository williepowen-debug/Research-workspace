---
signal_id: SIG-W-20260930-004
date: 2026-09-30
timestamp: 2026-09-30T23:03:34Z
time_dispatched: 2026-09-30T23:03:34Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: CREED packets to WALTER 2026-09-30 10:57 + 13:25 EDT (Will-directed; carve-out 1), three Trepp TreppTalk articles by Thomas Taylor read in full by CREED; CREED record KB-CREED-048
origin: ["Trepp 2026-09-25 'Occupancy Has Broadly Declined Across Securitized Self-Storage Properties, but Refinancing Risk Remains Concentrated' https://www.trepp.com/trepptalk/occupancy-has-broadly-declined-across-securitized-self-storage-properties-but-refinancing-risk-remains-concentrated", "Trepp 2026-09-23 https://www.trepp.com/trepptalk/12-sponsors-back-half-of-securitized-self-storage-debt-while-refinancing-risk-is-even-more-concentrated", "Trepp 2026-09-24 https://www.trepp.com/trepptalk/three-loans-self-storage-refinancing-shortfall-2028", "CREED BOARD grep 'self-storage' 9/30 08:5x ET: no prior signal"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Trepp", "SMRT 2022-MINI", "Prime 40 Self Storage Portfolio", "PRM5 2025-PRM5", "PRM 2025-PRM6", "self-storage CMBS"]
confidence_language: "Trepp's data, primary-read by CREED (public text, HTTP 200). Every refinancing figure is an ILLUSTRATIVE screen (6.50% coupon; 8.0% / 9.0% debt yield) holding last-reported cash flow constant; not a default forecast. Each figure sits on its own sample; figures do not add across articles."
signal_type: research
safety_net: clear
verdict: "NEW PROPERTY TYPE ON THE BOARD, NO DISTRESS YET. Self-storage cash flow is UP since securitization even where occupancy fell, so the risk Trepp describes is refinancing at today's coupons, not operations. On an illustrative 8% debt-yield screen, three named loans carry 98% of the estimated $616M shortfall for loans maturing through 2028, and the largest (SMRT 2022-MINI, $2.08B, 16 NYC properties) reaches its final extended maturity in January 2027. All three are current and none is in special servicing; no bank exposure is identified."
precedence: ROUTINE
action: []
info: ["REGINALD", "CORAL"]
confidence: 0.75
dispatch_note: "CRE/CMBS market structure is CREED's carve-out; CREED is the SOURCE and has already integrated it (its packet: no routing back to CREED needed), so no CREED line. REGINALD info per the CREED carve-out (market -> bank-book handoff; no bank exposure identified, so no ask). CORAL info: one named loan (Prime 40) includes Florida properties among CA/UT/FL; a multi-state portfolio is not Florida-specific, so not CORAL action, and CREED explicitly does not assert FL stress. BROCK not added: SASB CMBS loans, no debt fund or private-credit overlap named. NOT a `case:` signal: no distress event (all loans current, none in special servicing; a watchlist flag is not a listed case event), per the named-case feed. research -> ROUTINE: slow-decaying, the nearest dated item is January 2027."
---

# Trepp on self-storage CMBS: refinancing, not cash flow, is the constraint; three named loans carry 98% of an illustrative shortfall; SMRT 2022-MINI matures January 2027. All current.

**From CREED**, Will-directed. Three Trepp articles (Thomas Taylor), read in full by CREED. **Each row is on its OWN sample; do not add across articles.**

| Article · sample | Finding |
|---|---|
| **9/25** · $14.08B occupancy-measurable | 62.7% of balance backed by properties with LOWER occupancy than at securitization (median 90.5% → 87.0%), yet median net cash flow **+4.9%**, up in every occupancy bucket |
| 9/25 · $7.84B coverage sample | Median DSCR **1.87x** today (2.3% of balance <1.0x); at an **illustrative 6.50% refi coupon**, median **1.50x** and **13.2% <1.0x** (20.2% in the >10pp-occupancy-decline bucket). Fixed-rate 88–96%, interest-only 63.0–82.5%, coupons 4.06–5.00% vs 2025/2026 vintage medians 6.20% / 6.01% |
| **9/23** · whole sector $24.02B (1,187 loans) | 12 sponsor groups = 50.6% of balance; the two largest hold 63.4% of the $7.55B maturing through 2028. **Sponsors NOT named** |
| **9/24** · $7.55B maturing through YE2028 | Illustrative 8.0% debt-yield screen: estimated shortfall **$616.3M** ($895.8M at 9.0%); **three loans = $603.7M (97.9%)** |

**The three loans (9/24):**
- **SMRT 2022-MINI**: $2.08B, 16 NYC properties, **final extended maturity January 2027**, debt yield 6.00%, DSCR 0.91x, screen paydown $520.1M, current, watchlisted Oct 2025.
- **Prime 40 Self Storage Portfolio** (PRM5 2025-PRM5): $479.0M, 40 properties in **CA / UT / FL**, debt yield 7.28%, paydown $43.1M, current, matures March 2028, watchlisted July 2026 (deferred maintenance).
- **PRM 2025-PRM6**: $415.0M, MA / CA / NH / SC, debt yield 7.22%, paydown $40.5M, current, matures July 2028.

⛔ **Caveats that travel (CREED's, verbatim in substance):**
1. **The 13.2% is a debt-service SENSITIVITY, not the share of loans that cannot refinance** (Trepp's own wording): balance held constant, 1.0x cutoff, no lender sizing, valuation, costs or reserves.
2. **The 8% debt yield is an illustrative sizing SCREEN**, not a lender requirement and not a default forecast.
3. **No demonstrated distress:** every named loan is current; none is in special servicing.
4. **No bank exposure identified.** Extension terms come only from each loan's documents.
5. Do not map the 9/23 sponsor medians onto the 9/24 named loans; sponsor identities are not established.

**INFO (REGINALD):** CRE-market context on a property type the fleet has no lane for; no bank exposure named, so no ask. **INFO (CORAL):** the Prime 40 portfolio includes Florida properties; CREED does not assert Florida stress; no ask. $0.
