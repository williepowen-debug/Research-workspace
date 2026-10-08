---
signal_id: SIG-W-20261008-009
date: 2026-10-08
timestamp: 2026-10-08T12:12:40Z
time_dispatched: 2026-10-08T12:12:40Z
source: WALTER
origin: ["Census/BEA August trade release 2026-10-06 via TradingEconomics chart (@macropaperr bookmark)", "@jackprandelli 2026-10-06 composition read", "@LHMacro 2026-10-07 CPI breadth chart"]
domain: TARIFF_TRADE
cluster: INFLATION_TRANSMISSION
cluster_secondary: AI_INFRA_CAPEX
entities: ["US trade balance", "Census Bureau", "BEA", "CPI"]
precedence: PRIORITY
action: ["CARL"]
info: ["HENRY", "VULCAN", "RED", "PROME"]
confidence: 0.8
confidence_language: reports
signal_type: research
safety_net: clear
event_window: closed
word_count: 190
dispatch_note: Release read at chart level, not the Census PDF. Composition figures are a secondary thread's, not verified. RED on info for RED-FT-08 (core CPI 3-mo, graded at the 10/14 release). No gate or trade changed.
---

# August US trade deficit −$105.6B, widest since the early-2025 tariff front-running — oil and AI-hardware imports; plus August CPI breadth (11 of 21 components >3% y/y) ahead of the 10/14 CPI

**Trade (released Tue 10/6, August data):** goods-and-services balance **−$105.572B** (TradingEconomics chart), the widest since the early-2025 pre-tariff import surge and ~$33B wider than July (~−$72B on the chart). A secondary thread (not verified at Census): **imports +4.3%, exports +1.4%**; **industrial supplies imports +16.6%, led by petroleum** (Brent near $100); **capital-goods imports +4%** after computers/accessories jumped $13.5B in July — the AI-hardware build is imported; July bilateral gap with Taiwan ($18.1B) exceeded China ($15.2B). Through July the YTD deficit was 29.6% below 2025, which was inflated by front-running.

**So what:** an oil-price and AI-capex leak in the GDP arithmetic (net exports subtract), and evidence the tariff regime is not narrowing the gap while Brent stays ~$100.

**CPI breadth (LHMacro chart, 10/7):** in **August CPI, 11 of 21 major components (52%) rose >3% y/y and 4 (19%) >5%**; the >3% share averaged 22% in 2017–19 and peaked at 95% in Aug 2022. Headline 3.4%. **September CPI prints Tue 10/14** — RED-FT-08 (core 3-month annualised ≥3.0%) is graded manually at that release.

**CARL (action):** fold the deficit composition into the tariff/consumer read; flag whether breadth changes your CPI expectations. VULCAN: capital-goods import leg.

> **ADDITIVE CORRECTION — SIG-W-20261008-016 (2026-10-08):** "Tue 10/14" above is wrong — 2026-10-14 is a **Wednesday**. Date, figures and the RED-FT-08 grading day are unchanged. Caught by HENRY (claim_check). Original text preserved unedited.
