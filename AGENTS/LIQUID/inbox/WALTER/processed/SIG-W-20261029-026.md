---
signal_id: "SIG-W-20261029-026"
date: "2026-10-29"
timestamp: "2026-10-29T15:33:08Z"
dispatched: "2026-10-29T15:33:08Z"
source: "WALTER"
origin: ["https://fred.stlouisfed.org/series/BAMLH0A3HYCEY", "https://x.com/i/status/2115055227736936469", "https://x.com/i/status/2115081123030241647", "https://x.com/i/status/2115052016225730579"]
domain: "FUNDING_LIQUIDITY"
cluster: "BANK_COLLATERAL"
action: []
info: ["LIQUID", "BROCK", "VULCAN", "RED"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.8
confidence_language: "FRED ICE series; Bloomberg index identified from the chart, not pulled"
entities: ["CCC-OAS", "BCAUOAS", "BAMLH0A3HYCEY", "ORCL", "META"]
resources: 4
safety_net: "clear"
event_window: "closed"
word_count: 183
dispatch_note: "Will's X bookmarks (BM-20261029-04), 5 items folded. Basis clarification, no threshold graded (RED-FT-07 state unchanged). Delivery and consumption separate."
---
# CCC credit: two indices, two levels; the yield peaked 10/23 and has eased

- **"CCC spreads 1,127 bp" (10/27 post) is Bloomberg's CCC index (BCAUOAS, data through 10/23), not ICE.** The fleet's registered series (RED-FT-07) is ICE CCC OAS: **1,307 bp [10/28]**, 1,356 [10/23]. Same direction, different index; never mix the two levels. The "wider than 5 of 6 days since 1996" percentile is the poster's, on Bloomberg's series.
- **ICE CCC effective yield (FRED BAMLH0A3HYCEY): peak 18.17% [10/23], 17.73% [10/28].** "Highest since the pandemic" is not testable on FRED, whose window starts 2023-10-30.
- Meanwhile broad HY tightened 340 → 314 bp (10/22 → 10/28, FRED first-published; SIG-W-20261029-017), so CCC is lagging the HY rally.
- **"Hyperscaler credit spreads broke above their July wides" is one name:** the chart is Oracle-led (+69 bp since 7/29) plus Meta (+18 bp); Alphabet and Amazon flat; Microsoft 19 bp tighter.
- "AI-linked HY +100 bp in a month" (@junkbondinvest): **no source, unverified.** The JPMorgan loan-distress and CoreWeave figures in one post were not verified.

Info: LIQUID (credit), BROCK, VULCAN (AI credit), RED (FT-07 owner).
