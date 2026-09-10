---
signal_id: SIG-W-20260910-020
date: 2026-09-10
timestamp: 2026-09-10T23:41:00Z
time_dispatched: 2026-09-10T23:41:00Z
source: WALTER
origin: "Will-Telegram 8-image batch 23:26Z (BM-20260910-06 item 7) — Rory Johnston @Rory_Johnston X.com 2026-09-10 16:49 ET, Bloomberg chart of Generic 1st HO Future (Daily 10SEP2000-10SEP2026)"
domain: ENERGY
cluster: HYDROCARBON_INFRA
precedence: IMMEDIATE
action: ["BRENT"]
info: ["HANS", "FERT", "CARL", "PROME"]
entities: ["Rory-Johnston", "Bloomberg", "US-Diesel-Futures", "1st-HO-Future-Continuous", "Heating-Oil-Futures", "Diesel-Cracks"]
converges_with: SIG-W-20260910-005
confidence: 0.85
confidence_language: BBG-image-verified
signal_type: catalyst
resources: 2
safety_net: watch
word_count: 220
verdict: "Rory Johnston @Rory_Johnston (energy analyst, 2026-09-10 16:49 ET, 115K views): 'At more than $216 per barrel, US diesel futures are now at their highest level in history. We just busted through the prior record set at the height of the 2022 crisis.' Bloomberg chart: Generic 1st HO Future daily. Last Price 216.26; High on 09/10/26 216.26; Average 86.06; Low 12/11/01 21.00. Sits directly on top of SIG-005 (PPI Aug diesel +24.1%). Named continuous — BRENT verifies against a named-month contract before pricing (ADD#23 continuous-roll guard applies)."
---

# US diesel futures busted 2022 record — Rory Johnston: 1st HO continuous at $216.26 all-time high 2026-09-10 [Bloomberg]

## Signal (Bloomberg chart, verbatim per image)

- **Ticker:** *"QI Comdty (Generic 1st 'HO' Future) Daily 10SEP2000-10SEP2026"* (per the chart's own footer)
- **Last Price:** 216.26
- **High on 09/10/26:** 216.26 (today's session = all-time high on this series)
- **Average:** 86.06
- **Low on 12/11/01:** 21.00
- **Chart timestamp:** *"10-Sep-2026 16:47:..."*
- Copyright: **Bloomberg Finance L.P. 2026**.

Rory Johnston commentary: *"At more than $216 per barrel, US diesel futures are now at their highest level in history. We just busted through the prior record set at the height of the 2022 crisis."*

## Why this dispatches IMMEDIATE

- Converges with SIG-W-20260910-005 (PPI Aug 2026, energy +4.2%, **diesel +24.1%**, released 9/10 08:30 ET) — the wholesale-print number and the futures record are ONE story.
- Rory Johnston is a recognised energy analyst (Commodity Context substack), not a wire-echo account.
- **"Prior record set at the height of the 2022 crisis"** ties this to the Russia-invasion-of-Ukraine energy shock as the historical comparable — that comparable is what BRENT's own thesis surfaces should carry.

## Ask

**BRENT (action):** attach $216.26 to your product-vs-crude surface. Grade the 3-2-1 crack (SIG-001 named the Nov 3-2-1 near-trigger Boundary #8) and the diesel-specific crack against the record backdrop. Named-contract discipline (ADD#23): **1st HO continuous rolls between contracts, so a delta across a roll is an artifact** — quote and grade the specific delivery month (HOX26 or later depending on roll date) before pricing at $216.

**HANS (info):** EU energy overlay — TTF at 80.90 (SIG-004), UK gilts + gas-cost complex is the European counterpart.

**FERT (info):** diesel-cost transmission to agriculture supply chain / fertilizer distribution.

## Guards

- ⚠️ ADD#23 continuous-ticker-roll guard applies — verify the named-contract price before quoting the $216 level onward.
- ⚠️ Chart timestamp is 09/10/26 16:47 (~4:47 PM ET) — verify the FRONT-MONTH SETTLE after the 5:00 PM CME close before treating $216.26 as a settle rather than an intraday high.
