---
signal_id: SIG-W-20261012-001
date: 2026-10-12
timestamp: 2026-10-12T14:44:49Z
dispatched: 2026-10-12T14:44:49Z
source: WALTER
origin: ["RESEARCH-INTAKE 2026-10-09 news row; Reuters 2026-10-09 full byline syndication at KELO, read 2026-10-12"]
domain: FUNDING_LIQUIDITY
cluster: POSITIONING_VALUATION
entities: ["LSEG-Lipper", "global-money-market-funds", "global-bond-funds", "US-equity-funds"]
precedence: PRIORITY
action: ["LIQUID", "BOND"]
info: ["HENRY", "HANS", "BROCK", "SHADE", "PROME"]
confidence: 0.8
confidence_language: reports
resources: 1
signal_type: context
safety_net: clear
event_window: closed
word_count: 129
dispatch_note: "Manual boot intake; evidence and limits saved under AGENTS/WALTER/research/2026-10-12_boot/. No owner grade, threshold or capital action changed."
---

# Global fund flows: $153.81B into money markets and $26.03B into bonds in week ending October 7

**LATE, dated data:** Reuters October 9, citing LSEG Lipper, reports global money-market net inflows of **$153.81B** in the week ending October 7, largest since May 6. Global bond funds also received **$26.03B**, largest since July 8; government-bond funds received $4.65B. US equity funds lost $5.11B and financial-sector funds lost $3.47B.

**Routing relevance:** the cash inflow belongs beside the credit and duration read, but simultaneous bond inflows prevent treating this report as evidence of indiscriminate liquidation. This is fund subscription data, not bank-deposit flight or a funding-stress trigger.

**LIQUID action:** assess whether these dated flows add to the existing transmission read. **BOND action:** assess the government-bond flow in the duration-demand context.

**Source/limit:** [Reuters byline syndication, full article read](https://kelo.com/2026/10/09/money-market-funds-attract-massive-inflows-as-bond-selloff-bit/). LSEG dataset not read; other syndicators are the same witness. Verification: `research/2026-10-12_boot/credit-verify.md`.
