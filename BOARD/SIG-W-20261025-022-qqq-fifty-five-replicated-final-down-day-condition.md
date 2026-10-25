---
signal_id: "SIG-W-20261025-022"
date: "2026-10-25"
timestamp: "2026-10-25T20:41:19Z"
dispatched: "2026-10-25T20:41:19Z"
source: "primary-verification"
origin: "Will requested investigation of uncertain bookmark claims; BM-20261025-03, no new scan or mark"
domain: "MARKET_VOL"
cluster: "POSITIONING_VALUATION"
action: ["HENRY"]
info: ["VIOLET", "LIQUID", "RED"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.8
confidence_language: "primary evidence and bounded verification; remaining claim limits stated in body"
resources: 1
safety_net: "clear"
word_count: 231
entities: ["QQQ", "OddStats", "Bespoke", "S&P-500", "MacroCharts", "Bloomberg"]
event_window: "closed"
dispatch_note: "Verification UPDATE: earlier uncertainty was explicit; resolves/adds evidence without changing a previously certified figure. No R1 row. Sunday outside WQ-515 sample window."
---
# QQQ 55-event count reproduces with a final-down-day condition; breadth supports concentrated weakness

## Signal

Verification follow-up to the already processed October 25 bookmarks. Material delta from prior card(s): 006; QQQ independently computed, current breadth located at publisher.

## Data

Using [Yahoo daily QQQ data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ?period1=915148800&period2=1792800000&interval=1d) from inception, the original count reproduces exactly: rolling five sessions contain at least two returns ≤−2.5%, at least two ≥+1%, **and end on a ≤−2.5% session**. Annual counts: 2000:21, 2001:10, 2002:8, 2003:1, 2008:4, 2009:1, 2016:1, 2018:2, 2020:4, 2022:2, 2026:1; total **55**. Raw and dividend-adjusted prices match. Without the final-session condition, **155** overlapping windows qualify. October 16 lies marginally through −2.5%; rounding matters.

[Bespoke October 23 recap](https://www.bespokepremium.com/morning-lineup/bespokes-morning-lineup-semis-at-the-200-dma-10-23-26/) reports October 22 S&P constituent breadth **337 up/165 down**, average stock **+0.7%**, while cap-weighted index fell >1%. Original historical constituent dots were not independently reconstructed. It is not NYSE-wide breadth.

Short-ETF constituent universe/normalization remain unrecovered; turnover is not positioning. Bloomberg G10 excess-liquidity conceptual method was recovered from its author's interview, but exact 2026 construction, smoothing and six-month shift remain unreproduced.

## Relevance

**HENRY ACTION:** replace the count-unreplicated limitation with the explicit event definition; retain clustered/overlapping sample and no forward-return test. Breadth supports concentrated index weakness. VIOLET/LIQUID receive context, with no crash probability or liquidity forecast established.

## Source

Full claim-level evidence and access limits: AGENTS/WALTER/research/2026-10-25_verify/RESULTS.md and its linked helper reports. Retrieval October 25; observation and publication dates above remain distinct.
