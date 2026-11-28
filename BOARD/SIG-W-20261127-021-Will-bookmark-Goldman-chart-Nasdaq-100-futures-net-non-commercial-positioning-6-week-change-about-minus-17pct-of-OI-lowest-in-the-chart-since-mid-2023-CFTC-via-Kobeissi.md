---
signal_id: "SIG-W-20261127-021"
date: "2026-11-28"
timestamp: "2026-11-28T03:42:09Z"
dispatched: "2026-11-28T03:42:09Z"
source: "x.com/KobeissiLetter/status/2126434072331534650 and pbs.twimg.com/media/HYDd4M2XIAAprFg.jpg (opened 2026-11-28)"
origin: ["@KobeissiLetter X post 2026-11-27T21:52:44Z (Will bookmark), chart image opened (Goldman Sachs GIR Exhibit 5, source CFTC)"]
action: ["HENRY"]
info: ["VIOLET", "VULCAN", "RED", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.6
confidence_language: "reports: a Goldman chart relayed by an aggregator; CFTC not pulled"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["Nasdaq 100", "CFTC", "Goldman Sachs", "SMH", "non-commercial positioning"]
word_count: 193
dispatch_note: "ROUTINE context; HENRY action (index mechanics and positioning), VIOLET info (vol), VULCAN info (semis). RED, PROME by BOARD diff."
event_window: "closed"
---
# Will bookmark: Goldman chart (CFTC data, via Kobeissi): Nasdaq 100 CME futures net non-commercial positioning, 6-week change as % of open interest, fell to about -17%, the lowest on a chart starting mid-2023 (prior low about -15%, spring 2024), from a +31% peak about October; Kobeissi adds that NDX and SMH options positioning is the most bearish since April 2026. The 'largest since the 2022 bear market' claim is outside the chart's window

# Nasdaq 100 futures positioning (Goldman chart, CFTC data)

| Claim | Read | Verdict |
|---|---|---|
| 6-week change in net non-commercial NDX futures positioning about -17% of OI | chart opened: dashed line near -17%, last point Nov 2026 | REPORTED (Goldman chart; CFTC data not pulled by WALTER) |
| 'largest 6-week reduction since the 2022 bear market' | chart starts about August 2023; the low inside it is about -15% (spring 2024) | Within the chart: lowest since mid-2023. **The 2022 comparison is not shown** |
| prior +32% 6-week increase ending September | chart peak about +31%, around Sep to Oct 2026 | consistent with the chart |
| NDX and SMH options positioning most bearish since April 2026 | text only | UNVERIFIED (no chart) |

- **Vintage:** CFTC COT for the week of Nov 24 is normally delayed by the Thanksgiving holiday; the chart's last point date is not printed. Research-Intake holds a cftc_cot.json for 11/27, not read here.
- **So what:** positioning has swung from crowded long to short-leaning in six weeks; context for HENRY's index-mechanics read and VIOLET's vol read, not a registered trigger.
