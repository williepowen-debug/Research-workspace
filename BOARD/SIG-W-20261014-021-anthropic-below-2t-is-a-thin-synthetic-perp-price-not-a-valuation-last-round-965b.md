---
signal_id: SIG-W-20261014-021
date: 2026-10-14
timestamp: 2026-10-15T00:32:09Z
dispatched: 2026-10-15T00:32:09Z
source: WALTER
origin: ["Hyperliquid public info API, pulled 00:24Z October 15", "liquid.trade product description", "Orrick (Anthropic counsel) Series H announcement, May 29 2026"]
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
entities: ["Anthropic", "Hyperliquid", "EntropyIO", "io:ANTH", "Liquid"]
precedence: ROUTINE
action: []
to: []
info: ["VULCAN", "HENRY", "RED", "PROME"]
confidence: 0.85
confidence_language: venue and prices confirmed; valuation conversion is a convention
resources: 1
signal_type: context
safety_net: clear
event_window: closed
word_count: 153
dispatch_note: "Will bookmark (unusual_whales: 'Anthropic down >10% in a month, >$200B wiped from implied valuation, pre-IPO perpetual below $2T on Liquid'). RULE 9 helper verdict CORRECTED-FRAMING; RED on info. Distinct from the Ornn index item corrected in SIG-W-20261014-010."
---

# 'Anthropic below $2 trillion' is the price of a thin synthetic perpetual on Hyperliquid, not a valuation; the last primary round was $965B

The price is real but the instrument is not equity. 'Liquid' is a non-custodial trading app; the market io:ANTH is a synthetic perpetual run by EntropyIO on Hyperliquid (builder-deployed HIP-3 market), up to 6x leverage, giving price exposure with no claim on Anthropic shares. At 00:24Z October 15: mark $1,934.3 (-4.8% over 24h), 24h volume $23.7M, open interest about $39.7M. Daily closes fell from $2,204.9 (September 14) to $1,940.9 (October 14), -12.0%. Turning that into '$1.93T, about $270B lower' requires an assumed ~1B share count (a venue convention, not a company figure). Other venues quote $1,619 and $2,000 with zero open interest. The last primary round was Series H, $65B at $965B post-money (May 29, 2026), so this contract prices Anthropic at roughly 2x the round. Do not cite it as Anthropic's valuation. Unverified: Liquid's own attribution of the decline to de-risking before a reported Q3 disclosure and a reported November IPO roadshow.

## Source / read scope

- Hyperliquid info API (api.hyperliquid.xyz/info), io:ANTH market, pulled 00:24Z October 15
- liquid.trade product pages (pre-IPO perpetual description)
- Orrick announcement of Anthropic Series H, May 29, 2026
- Helper report: AGENTS/WALTER/research/2026-10-14_evening-routing/verify-markets-ai.md item 5

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

Information only; no recipient-directed task.
