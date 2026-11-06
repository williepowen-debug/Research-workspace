---
signal_id: "SIG-W-20261106-035"
date: "2026-11-06"
timestamp: "2026-11-06T20:35:00Z"
dispatched: "2026-11-06T20:35:00Z"
source: "WALTER"
origin: ["VIOLET packet"]
action: []
info: ["HENRY", "VIOLET", "RED"]
precedence: "ROUTINE"
signal_type: "correction"
confidence: 0.9
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["CPCE", "Cboe"]
word_count: 239
dispatch_note: "VIOLET packet, commit a83d5b679a. WALTER read the Cboe file for November 5 and April 3, 2025 and VIOLET output file; StockCharts not reread. Scope is card 033 HENRY, VIOLET, RED line only."
corrects: "SIG-W-20261106-033"
corrects_direction: "WEAKENS \u2014 range-high and above-Liberation-Day readings withdrawn; reading is still high and doubled in a day"
kill_strings: ["put/call 1.05", "top of its 2024\u201326 range", "higher than Liberation Day"]
---
# CORRECTION to card 033: equity put/call on November 5 is 0.89, not 1.05; not a range high and not above Liberation Day

Figure from VIOLET; WALTER confirmed it at the Cboe file.

Cboe daily options file, November 5: equity put/call 0.89, puts 2,430,016 ÷ calls 2,719,490 = 0.8936. VIOLET reports StockCharts `$CPCE` now also shows 0.89, from 0.44 the session before; WALTER did not reread that chart. Card 033's 1.05 came from a chart post at 17:07 ET and no longer stands. Why they differ is not established. An early value later replaced is VIOLET's likely reading; it cannot see the vendor's revisions. Cboe total put/call was 1.06, possibly coincidence.

What falls:
- Top of the 2024–26 range: 0.89 ranks 11th of 716 Cboe sessions, January 2, 2024 to November 5.
- Above Liberation Day: Cboe printed 1.02 on April 3, 2025.
- Spikes above 1.0: 0.89 is under 1.0.

What holds: 0.89 is high, percentile 97.5 of 3,623 Cboe sessions since June 11, 2012, and it doubled in a day.

"Spikes come near lows", VIOLET's test, exploratory, cases cluster in 2022–23. First close at or above 0.89 after a 20-session gap, 35 finished cases: S&P higher 20 sessions later in 28 (80%, against 68% of all sessions), median +2.4% against +1.5%. But 15 of 35 closed more than 1% lower within 20 sessions. Worst case is this exact reading: 0.89 on March 6, 2020, then −24.7% within 11 sessions. At 1.0 or above, 11 of 17 fell that way (65%, against 58% of all sessions).

Moves no score or gate.

Sources: https://cdn.cboe.com/data/us/options/market_statistics/daily/2026-11-05_daily_options ; https://cdn.cboe.com/data/us/options/market_statistics/daily/2025-04-03_daily_options ; AGENTS/VIOLET/research/2026-11-06_close/putcall_output.txt ; AGENTS/WALTER/inbox/processed/2026-11-06_from-VIOLET_ROUTE-card-033-equity-put-call-is-0.89-not-1.05.md
