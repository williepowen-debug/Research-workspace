---
signal_id: SIG-W-20261001-030
date: 2026-10-01
timestamp: 2026-10-01T21:13:56Z
time_dispatched: 2026-10-01T21:13:56Z
timestamp_note: stamped from `date -u` at write, not typed
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane 2026-10-01 news batch: NEW_WATCH 'junk bond' -> LIQUID, Yahoo Finance 2026-09-17 'Meta-Tied Data Center Taps US Junk Bonds for the First Time'", "WALTER search 2026-10-01 ~21:2xZ: cryptobriefing.com (two pieces), briefs.co, itiger.com relays; the originating wire (Bloomberg, per the Yahoo syndication) NOT read"]
domain: FUNDING_LIQUIDITY
cluster: AI_INFRA_CAPEX
cluster_secondary: PC_STRESS
entities: ["CleanSpark", "Meta", "Anviran-LLC", "Sandersville-GA", "AI-data-center-HY"]
confidence: 0.70
confidence_language: deal terms come from secondary relays that agree with each other; the wire was not read; dated mid-September, so this is LATE
signal_type: research
safety_net: clear
verdict: "CleanSpark (a bitcoin miner) sold a debut ~$2.23-2.28B five-year high-yield bond to fund a 175 MW AI data-center campus in Sandersville, Georgia, leased for 20 years triple-net to Anviran LLC, a Meta subsidiary. Relays report ~$10B of orders, pricing at 98.5 and a yield of 8.25%. Reported as the first time US junk bonds have financed a Meta-linked data center. Mid-September, two weeks late to the BOARD."
precedence: ROUTINE
action: ["LIQUID"]
info: ["VULCAN", "BROCK", "HENRY"]
dispatch_note: "Financing leg of AI capex -> LIQUID per ROUTING_TABLE AI_CAPEX row and the VULCAN substance-vs-financing carve-out; VULCAN info. Not on BOARD or at any desk (grep CleanSpark/Sandersville/Anviran: 0 hits). Related but distinct: SIG-W-20260924-024 (AI-linked junk supply, CoreWeave). LATE: the item is ~2 weeks old; ROUTINE for that reason."
---

# CleanSpark's $2.2B junk bond for a Meta-leased data center: the first Meta-linked high-yield deal (mid-September, late to the board)

**Short version:** CleanSpark, a bitcoin miner, sold a **debut five-year high-yield bond of about $2.23–2.28B** to build a **175 MW AI data-center campus in Sandersville, Georgia**. The campus is leased for **20 years, triple-net, to Anviran LLC, a Meta subsidiary**. Relays report **~$10B of orders**, pricing at **98.5**, a **yield of 8.25%**. It is reported as **the first time US junk bonds have financed a Meta-linked data center.**

## Why LIQUID
This is the **financing leg** of AI capex reaching the high-yield market through a single-tenant lease structure, which is the shape `SIG-W-20260924-024` (CoreWeave) flagged. The credit is the lease, not CleanSpark. Demand was ~4x covered at an 8.25% yield, so the market is pricing it at a spread, not at Meta's rating.

## Caveats
- **Secondary relays only.** WALTER did not read the originating wire. The relays give the deal size as both $2.227B (launch) and ~$2.28B (priced).
- **Mid-September.** The lane surfaced it 9/17 and it reached the BOARD on 10/01. Treat the market read as two weeks stale.

## Requested action
LIQUID: log it against your AI-financing / HY-supply lines. VULCAN, BROCK, HENRY: information only.
