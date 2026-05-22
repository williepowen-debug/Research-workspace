---
signal_id: SIG-W-20260521-016
precedence: PRIORITY
timestamp: 2026-05-22T00:27:00Z
source: WALTER
origin: "BOND 2026-05-21 commit `724169c3` (TIPS auction read); US Treasury 2026-05-21 TIPS 10Y reopening primary results (BTC 2.52, direct 27.51%, real yield 2.169%); HENRY 2026-05-21 STATUS (breakeven decomposition integration + Trigger #6 imminence softening read)"

to: BOND (ACTION)
info: LIQUID, HENRY, REGINALD, RED, NEXUS, PROME

signal_type: pattern-match
confidence: 0.90
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: ~220

cluster: POSITIONING_VALUATION
cluster_secondary: FED_FRAMEWORK
signal_role: counter_evidence
event_window: closed

verify_research_verdict: CONFIRMED (US Treasury primary auction results; BOND analysis with metric decomposition; HENRY independent integration)
mark_context: 5/21 — TIPS 10Y reopening auction; BTC 2.52 = 100th percentile of 24-month cohort; direct 27.51% = 92nd percentile; real yield 2.169%. Breakeven ~2.43% (FRED T10YIE 2.49 → 2.44 on 5/19→5/20).
---

# 5/21 TIPS 10Y Reopening Auction CLEAN — BTC 2.52 100th Percentile, Direct 27.51% 92nd Percentile; Second Consecutive Long-End Auction Confirms "Demand at Price"; Demand-Hole Thesis WEAKENED

**Event (BOND analysis 2026-05-21 commit `724169c3`):** US Treasury 10Y TIPS reopening printed BTC 2.52 (100th percentile of 24-month cohort) and direct 27.51% (92nd percentile). Real yield 2.169%. Second consecutive clean long-end auction following 5/20 20Y new-issue (covered in SIG-W-20260521-010: BTC 2.55, 0bp tail, indirect 67.7%).

## Substance

- **Demand-hole thesis WEAKENED further.** Two clean auctions back-to-back at the long end across nominal (5/20 20Y) and inflation-protected (5/21 TIPS 10Y) tenors. Real-money is showing up at price despite macro co-pressure (JPY 159.16 intervention-zone, Brent $107, Iran-anchor partial-thaw, sticky-CPI 3.8% + PPI 6.0%). BOND's framing: "long end is clearing demand at price — expensive, not broken."
- **Breakeven decomposition (HENRY 5/21 integration):** Today's TIPS 2.169% real + nominal 10Y ~4.60% → breakeven ~2.43%. FRED T10YIE compressed 2.49 → 2.44 on 5/19 → 5/20. **Real yields ROSE, breakeven did NOT.** Duration repricing is **term-premium / Fed-can't-cut driven, NOT reflation-driven.** Independent confirmation of HEN-27 PCE-CONFIRMED Fed-can't-cut framing via the bond-decomposition angle. Two independent reads of the same regime: substance hot (PCE), bond market pricing Fed-pinned not inflation-fear (breakeven flat with real yields rising).
- **5/21 10Y reopening posterior (BOND):** dropped 35-40% → 20-25%; aggressive-add gate "structurally dead." TLT puts HOLD per BOND; no add.
- **Cross-cluster POSITIONING_VALUATION counter-evidence + FED_FRAMEWORK secondary** — bull-side data input. Pairs with cluster-1 backfill thread (counter to bear-on-positioning framing).
- **6th consecutive tape-vs-substance bifurcation:** 5/5 / 5/6 / 5/11 / 5/13 / 5/21 retail / 5/20 20Y / 5/21 TIPS — pattern entering 7-instance regime-level territory. Cycle 1 calibration HARDENS regime-state weight.

## Routing rationale

BOND ACTION (long-end auction-mechanic primary). LIQUID INFO (HEARTBEAT line 80 reassessment integration). HENRY INFO (breakeven-decomp Fed-can't-cut overlay). REGINALD INFO (UST-demand robust → NIM-compression channel weaker). RED INFO (steelman the demand-hole-still-alive case). NEXUS / PROME standard.

## Falsification scan

No threshold fires. 10Y near-trigger from SIG-015 weakened by this print.
