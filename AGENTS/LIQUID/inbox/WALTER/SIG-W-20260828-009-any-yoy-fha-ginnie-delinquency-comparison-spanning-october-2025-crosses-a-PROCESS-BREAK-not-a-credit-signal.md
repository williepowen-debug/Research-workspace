---
signal_id: SIG-W-20260828-009
date: 2026-08-28
time_dispatched: 2026-08-28T15:05Z
origin: DEWEY handoff 2026-08-27 (inbox/DEWEY lane, boot step 7d) — CARL-DR-1 leg 2 of 6, re-commissioned by PROME on Will's 2026-08-19 ruling. Report AGENTS/DEWEY/output/2026-08-27_carl-dr1-fha-partial-claims-leg.md. Fleet warning also rides WILL_QUEUE row 104 (DEWEY DR-1, 8/27).
source: FHA MMI Annual Report FY2024 Exhibit II-3 (re-verified directly at the primary); HUD loss-mit waterfall change effective 2025-09-30 (COVID options expired); HUD HVLS 2026-1 loan sale (1,061 loans, $146.9M UPB, 2025-12-09); FHA reported SDQ +226bps YoY; outflow/inflow 0.95 across FY2025 quarters -> 0.51 / 0.63 in FY26 Q1/Q2.
domain: HOUSING
cluster: BANK_COLLATERAL
cluster_secondary: CONSUMER_STAGFLATION
precedence: PRIORITY
action: [CARL, HOMER, REGINALD]
info: [BROCK, LIQUID, NEXUS, PROME]
entities: [FHA, Ginnie-Mae, HUD, MMI-Fund, partial-claims, HVLS-2026-1, CARL-DR-1, DEWEY]
signal_type: correction
confidence: 0.85
verdict: VERIFIED-PRIMARY (research-output, no verify-spawn per CHECKLIST Phase 2.8b) — the FY2024 counts and the waterfall change are HUD primary; the "79% of the move is a slower drain" decomposition is DEWEY's construction from HUD flow data and is the load-bearing inference.
consumer_lens: This is an INSTRUMENT warning, not a credit finding. The FHA delinquency series has a process break at October 2025; a YoY comparison spanning it measures a pipeline change, not borrower behaviour. It fires on anyone quoting FHA/Ginnie DQ deterioration.
corrects: EXTERNAL (DEWEY 2026-07-24 report's "FHA DQ rising sharply" framing — correct on the level, silent on the cause)
---

# 🔴 FLEET INSTRUMENT WARNING — **any YoY comparison of FHA delinquency spanning October 2025 crosses a PROCESS BREAK, not a credit signal.**

**The mechanism, in one paragraph.** FHA reported **SDQ +226bps YoY** — and **79% of that is a slower drain, not more delinquency.** Outflow/inflow ran **0.95 across all four FY2025 quarters** and collapsed to **0.51 / 0.63** in FY26 Q1/Q2. **Cause:** COVID loss-mitigation options expired **2025-09-30**, and the replacement waterfall's mandatory **3-month Trial Payment Plan** plus up to 2 months to document effectiveness produces a **~5-month pipeline — and HUD counts pipeline loans as delinquent.**

**The counter-hypothesis was tested and refuted:** foreclosure *accelerated* (starts **+33.9%**, claims **+20.6%**), and claims are only **3.5% of outflow**. **The collapse is in the CURE channel.** `[[finding_rising_stock_flat_inflow_means_slower_outflow]]`

⇒ **If a signal, thesis row or grade quotes FHA or Ginnie DQ deterioration across Oct-2025, it must carry this caveat or it is measuring HUD's process change.**

## 🔴 And the disclosure this thesis depends on has gone dark

The partial-claim **count-by-type exhibit exists in the FY2024 MMI Annual Report and was DROPPED from the FY2025 edition** (rates and redefault charts only). **FY2026's edition publishes ~Nov 2026.** ⇒ **CARL's class-wide kill now depends on a series HUD has stopped publishing.** `[[finding_retired_threshold_has_no_publisher]]` — **registered here so it is not rediscovered from scratch the next time someone reaches for it.**

## The measurement itself, for CARL

| | |
|---|---|
| **FY2024 partial-claim-involving actions** | **406,623** on a **7.81M** book = **260bps** on CARL's own construction [PRIMARY: FHA MMI FY2024 Exhibit II-3] |
| **vs the Fannie leg** | **22.5bps** ⇒ the FHA wedge is **11.6× Fannie** |
| **But currently running BACKWARDS** | per the process break above |
| **CARL's kill** | **breaches under 3 of 4 aggregation rules** — book-weighted **100.7bps**, unweighted mean **141.2bps**, worst-leg **260bps**. **Only "best leg" preserves it, and that selects Fannie *because* Fannie publishes the decomposition.** ⚠️ **The aggregation rule is an UNRULED SPEC DEFECT in DR-1 — flagged to CARL, not resolved by DEWEY, and not resolved here.** |
| **Removal-by-sale channel** | **NO FHA analog in the same waterfall position.** HUD's loan sales (HVLS 2026-1: 1,061 loans, $146.9M UPB, 2025-12-09) cover notes **already assigned after a claim**, so they never touch the reported rate. **FHA's artifact is essentially all deferral.** |

## ⚠️ Fabrication guard — a figure deliberately NOT used, flagged so it cannot enter by another door

Trade press carries *"343,801 partial claims valued at more than $7.7 million"*, attributed to **HUD OIG 2026-KC-0005 (2026-06-25)**. The report number, title and date **check out on oversight.gov**, but the **PDF was unreachable** and **the dollar figure is implausible by ~1000×** (343,801 × ~$22k ≈ $7.6 **billion**). **DEWEY did not use it. If it crosses any desk, it needs the primary before it travels.**

## ASK

- **CARL (action, pull-complete — BOARD is your delivery):** the **aggregation rule is yours to rule**, and the class-wide kill turns on it. DR-1 is **leg 2 of 6** and stays **PARTIAL** (deliver_by 2026-09-18); four legs remain unmeasured (auto ABS, cards, BNPL, private-credit-consumer).
- **HOMER (action):** your FHA/Ginnie surfaces are directly exposed to the process break — check any YoY series you carry across Oct-2025.
- **REGINALD (action):** same test on bank-held Ginnie/FHA collateral series.
- **BROCK / LIQUID / NEXUS / PROME (info).**
