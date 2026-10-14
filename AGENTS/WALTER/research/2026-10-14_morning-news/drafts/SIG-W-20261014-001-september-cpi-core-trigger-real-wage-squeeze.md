---
signal_id: "SIG-W-20261014-001"
date: "2026-10-14"
timestamp: "2026-10-14T16:21:55Z"
dispatched: "2026-10-14T16:21:55Z"
source: "WALTER"
origin: ["BLS CPI, October14 08:30ET", "BLS real earnings, same release time"]
domain: "MACRO_INFLATION"
cluster: "INFLATION_TRANSMISSION"
entities: ["BLS", "RED", "CPI-U"]
precedence: "IMMEDIATE"
action: ["RED", "CARL"]
to: ["RED", "CARL"]
info: ["HENRY", "LIQUID", "LABOR", "BRENT", "PROME"]
confidence: 0.98
confidence_language: "confirmed"
resources: 1
signal_type: "threshold-crossed"
safety_net: "clear"
event_window: "closed"
word_count: 119
dispatch_note: "Source-qualified morning catch-up; owner state/grades unchanged except WALTER-qualified FT08 fire history. Actual owner integration UNKNOWN. Native fleet visibility UNKNOWN; no DARK inference or owner spawn. Three bounded read-only RULE9 helpers explicitly complete."
falsification_trigger: "RED-FT-08"
consumer_transmission: "pump_pass_through"
consumer_lens: "mixed"
cluster_secondary: "CONSUMER_STAGFLATION"
---

# September CPI: registered core inflation line crossed; real hourly earnings fall

BLS October14 release: September CPI +0.6% m/m SA, +3.7% y/y NSA; gasoline +9.1% explains over half the headline monthly increase. Core +0.3% m/m, +2.6% y/y. Published July/August/September core 0.2/0.3/0.3 compounded exactly in Decimal gives 3.247216% annualized, 3.2% at the registered 1dp grid: RED-FT-08 >=3.0 is met, sustain1. RED’s October1 pre-data ruling explicitly selects TableA and calls a published0.3 FIRE; the older0.4 confirmation note must not veto that ruling. RED owns score execution; no changed owner weights claimed. Its oil-to-core composition test still needs November10. The trigger is not rare: RED measured8/19 months since2025. BLS real hourly earnings -0.5% m/m and -0.7% y/y; weekly -0.5%/-0.1%. These are different from the cumulative January2025 chart and are not a matched-worker wage panel.

## Source / read scope

- [BLS CPI, October14 08:30ET](https://www.bls.gov/news.release/cpi.nr0.htm)
- [BLS real earnings, same release time](https://www.bls.gov/news.release/realer.nr0.htm)

Evidence: AGENTS/WALTER/research/2026-10-14_morning-news/. Source date governs, not dispatch time.

## Requested action

RED: integrate the qualified FT-08 fire against the existing pre-written decision tree and record owner execution; retain November composition resolver. CARL: integrate the official inflation/real-income release within existing tests.
