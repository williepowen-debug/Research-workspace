---
signal_id: SIG-W-20260924-006
date: 2026-09-24
timestamp: 2026-09-24T17:16:46Z
time_dispatched: 2026-09-24T17:16:46Z
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane 2026-09-23 news.json NEW_WATCH x4 (Bloomberg, The Edge x2, firstonline), batch BM-20260924-01 item 4", "WALTER web check 2026-09-24: Bloomberg 9/21 ('seeks over $11B'), 9/22 ('over $20B of early interest'), 9/23 ('starts jumbo high-yield sale'); Japan Times 2026-09-24 ('junk-bond debt at record yields'); Seoul Economic Daily 9/23 (tranche yields). Bodies NOT read; figures from headlines and search summaries"]
domain: FUNDING_LIQUIDITY
cluster: AI_INFRA_CAPEX
cluster_secondary: PC_STRESS
precedence: ROUTINE
action: ["LIQUID"]
info: ["VULCAN", "SAM", "BROCK", "HENRY"]
entities: ["SoftBank-Group", "OpenAI", "high-yield-issuance", "AI-financing"]
confidence: 0.70
confidence_language: the deal and its size are multi-outlet with Bloomberg as the origin; tranche yields are from one outlet's summary; WALTER read no deal document
signal_type: context
resources: 1
safety_net: clear
word_count: 300
verdict: "SoftBank priced the largest corporate junk-bond deal on record, ~$11.1B across USD and EUR (9/23), to fund its ~$65B OpenAI commitments. Reported tranche yields: 8.75-8.875% (3.5y, $1B), 9.375-9.5% (5.5y, $4.5B), 9.75-9.875% (7.5y, $4.5B). Early demand >$20B. Goldman strategists (per the same coverage): global AI-related debt issuance >$575B in 2026. Both directions are in it: demand says the HY market is open, and the price says AI financing now costs ~10%."
---

# SoftBank prices a record ~$11.1B junk bond, at up to 9.875%, to fund OpenAI

**Short version:** SoftBank sold the **largest corporate junk-bond deal on record**, about **$11.1B**, at yields up to **~9.9%**, to fund its OpenAI commitments. Investors put in **over $20B** of orders. **Two readings, both true:** the high-yield market is wide open, and AI's funding bill is now being paid at near-10% junk rates.

## The deal (Bloomberg-origin coverage, 9/21–9/24)
| Tranche | Size | Reported yield |
|---|---|---|
| 3.5-year | $1B | 8.75–8.875% |
| 5.5-year | $4.5B | 9.375–9.5% |
| 7.5-year | $4.5B | 9.75–9.875% |
- Dollars and euros, ~$11.1B equivalent. Early demand **>$20B**. Purpose: commitments of about **$65B** to OpenAI, plus AI deal-making.
- Context: Goldman credit strategists put **2026 AI-related debt issuance above $575B** (relayed in the same coverage, not read by WALTER).
- ⚠️ **Tranche yields come from one outlet's summary** (Seoul Economic Daily). The size and record status are multi-outlet.

## Why it routes
- **LIQUID:** HY supply and breadth. A record-size deal clearing with 2× cover is a **calm-credit datapoint**, and it sits beside HY OAS at **273 bp [FRED 9/23]**.
- **VULCAN:** this is the **financing leg** of AI capex. Per the carve-out it routes to credit, with VULCAN on info.
- **SAM:** SoftBank is a Japanese issuer. **BROCK:** AI-financing / private-credit adjacency. **HENRY:** market structure.

## Ask
- **LIQUID (ACTION):** note whether this moves your HY breadth/dispersion read. No registered row is implied.

⛔ **$0. Nothing graded.**
