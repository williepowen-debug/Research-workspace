---
signal_id: "SIG-W-20261126-007"
date: "2026-11-27"
timestamp: "2026-11-27T03:45:50Z"
dispatched: "2026-11-27T03:45:50Z"
source: "search summaries 2026-11-26 ET of fxstreet.com/news/japanese-yen-softens-after-soft-tokyo-core-cpi-inflation-data-202611270027, investinglive.com, actionforex.com, mlq.ai; Statistics Bureau of Japan not read"
origin: ["fxstreet.com 202611270027 (search result)", "investinglive.com, actionforex.com, mlq.ai (search summaries)"]
action: ["SAM"]
info: ["LIQUID", "BOND", "ORACLE", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "indicator"
confidence: 0.7
confidence_language: "reports: several secondary outlets agree; issuer release not read"
resources: 1
safety_net: "clear"
cluster: "ASIA_CHINA"
domain: "JAPAN_BOJ"
entities: ["Tokyo CPI", "Statistics Bureau of Japan", "Bank of Japan", "USD/JPY"]
word_count: 187
dispatch_note: "PRIORITY by the v0.53 secondhand rule (flash-class figure from secondary pages). Calendar catch-up 7i: release elapsed 18:30 ET, neither record before this card. RED, PROME by BOARD diff."
event_window: "open"
---
# Tokyo November CPI (secondary pages; Statistics Bureau not read): core ex-fresh-food 2.9% y/y from 2.6%, a 16-month high, vs 3.0% expected; core-core ex-food-and-energy eased to 2.5% from 2.6%; energy 9.5% from 2.2% as electricity and gas subsidies ended

# Tokyo CPI, November 2026 (released Fri 11/27 08:30 JST = Thu 11/26 18:30 ET)

| Measure | November | October | Expected | Basis |
|---|---|---|---|---|
| Core (ex fresh food), y/y | **2.9%** | 2.6% | 3.0% | search summaries of fxstreet, investinglive, actionforex, mlq.ai; issuer page NOT read |
| Core-core (ex fresh food and energy), y/y | **2.5%** | 2.6% | not stated | same |
| Energy, y/y | 9.5% | 2.2% | - | same; driver: temporary end of government electricity and gas subsidy payments |

- **Secondhand-release rule (ROUTING_TABLE v0.53):** PRIORITY until the figure is read at the Statistics Bureau of Japan; upgrade then.
- **Context in the same summaries (not WALTER's read):** markets expect a BoJ hike to 1.5% at the 12/17 to 12/18 meeting; the national November CPI lands the same week; yen reaction reported both ways, USD/JPY near 160 (SAM's theme `usdjpy-160-intervention`).
- **So what:** the headline rise is energy from subsidies ending, while the underlying measure eased: a split read for the December hike case. SAM grades; ORACLE owns any priced odds of the BoJ move.
