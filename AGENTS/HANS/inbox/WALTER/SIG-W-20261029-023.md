---
signal_id: "SIG-W-20261029-023"
date: "2026-10-29"
timestamp: "2026-10-29T15:33:08Z"
dispatched: "2026-10-29T15:33:08Z"
source: "WALTER"
origin: ["https://x.com/i/status/2115475956777578831", "ICE TTF front month via Investing.com table (fetched 10/29)", "vendor TTFX26.NYM daily bar (yfinance)"]
domain: "EUROPE_MACRO"
cluster: "INFLATION_TRANSMISSION"
action: ["HANS"]
info: ["BRENT", "LIQUID", "RED"]
precedence: "PRIORITY"
signal_type: "pattern-match"
confidence: 0.7
confidence_language: "intraday above 100 supported by two secondaries; settlement values conflict; official settle unread"
entities: ["TTF", "TTFX26", "TTFZ26", "HANS-T-07"]
resources: 3
safety_net: "clear"
event_window: "closed"
word_count: 207
dispatch_note: "Will's X bookmarks (BM-20261029-04). Possible HANS-T-07 L3 crossing: WALTER does not grade it; evidence vs letter only. X26 expires 10/29, so the 10/28 settle is the last pre-roll front-month print. Delivery and consumption separate."
---
# European gas: November TTF traded above €100 on 10/28; whether it SETTLED there is unconfirmed

A post (10/28) said Dutch TTF "crossed €100 for the first time since December 2022", +250% this year.

| Evidence for 10/28 (front month = November, TTFX26) | Value and basis |
|---|---|
| ICE front-month table (Investing.com, fetched 10/29) | high **100.945**, close **98.50** (an earlier snapshot of the same page showed 99.25) — not an exchange settle |
| Vendor NYMEX look-alike TTFX26.NYM daily bar | close **100.72** on 377 lots |
| Official ICE Endex settle | **NOT READ** |
| Year-to-date | 12/31/2025 close 28.16 ⇒ +250% to +258% (confirmed) |

**Against HANS-T-07's letter** (front-month daily settle, L3 >100, sustain 1, never grade across a roll): intraday >100 is supported; a **settle >100 is not established** (sources conflict). **X26 expires today (10/29)**; from 10/29 the front month is December (Z26, vendor 96.90 intraday ~11:00 ET). Do not compare an X26 level with a Z26 level as a move.

**HANS ACTION:** grade T-07 L3 from the official 10/28 X26 settle (the last pre-roll front-month print). BRENT, LIQUID, RED info. Context: SIG-W-20261029-011 (EU storage record low, record TTF options open interest); SIG-W-20261029-016 (ECB says energy prices "continued to rise").
