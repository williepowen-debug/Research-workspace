---
signal_id: "SIG-W-20261022-002"
date: "2026-10-22"
timestamp: "2026-10-22T11:46:02Z"
dispatched: "2026-10-22T11:46:02Z"
source: "X_BOOKMARKS"
origin: "Will X bookmark 2113215401983152439 (@coinbureau, 10:26Z) checked against CoinDesk 04:49 EDT plus WALTER vendor and FRED pulls"
domain: "MARKET_VOL"
cluster: "POSITIONING_VALUATION"
action: ["HENRY"]
info: ["LIQUID", "VIOLET", "SAM", "ZHAO", "VULCAN", "REGINALD", "RED", "PROME"]
precedence: "IMMEDIATE"
signal_type: "context"
confidence: 0.75
confidence_language: "reports"
resources: 1
safety_net: "clear"
word_count: 274
entities: ["Nikkei 225", "Kospi", "Hang Seng", "CSI 300", "SK Hynix", "Samsung Electronics", "SoftBank", "Brent", "VIX", "HY OAS"]
event_window: "closed"
dispatch_note: "Index figures are CoinDesk's (10/22 04:49 EDT); the $1T and 'Black Thursday' are the bookmark's own aggregate and label, unverified. Oil-driver attribution guarded (intercept-to-strike class)."
---
# Asia sold off October22: Nikkei about -3%, Kospi -3.5%, Hang Seng -3%, CSI 300 -2% and 20% below its June peak; Brent December $111.84 overnight (not a settle); HY OAS 333 sits 17bp under REG-T-04

Will bookmarked a Coin Bureau post (10:26Z): Asian markets "wiped out nearly $1,000,000,000,000 across six major markets today", "Black Thursday". The $1T total and the label are the post's own and are UNVERIFIED.

Index moves, CoinDesk 10/22 04:49 EDT: Nikkei 225 about -3%, Kospi -3.5%, Hang Seng -3%, **CSI 300 -2%, taking it 20% below its June peak (bear-market territory)**. Investing.com, relayed through search: chipmakers led, SK Hynix -4%, Samsung Electronics -3.6%, on AI-spending doubts. SoftBank closed ¥4,305, -6.86% (SIG-W-20261022-001).

WALTER pulls at 11:39Z (vendor, overnight session, NOT settlements): Brent December (BZZ26.NYM) $111.84 (+2.78%; the tool's contract label is truncated, so identity rests on the requested symbol); WTI December (CLZ26, identity Dec 2026) $99.21 (+2.12%); ^VIX 18.37 against a Cboe 10/21 close of 16.68. CoinDesk: Brent above $112, highest since May.

Credit, FRED first-published: HY OAS 333 [10/20] (331 [10/16], 329 [10/19]). That is **17bp under REG-T-04 (>350, 3 closes)**, inside 5%: a near-trigger watch, not a fire. RED-FT-02 and REG-T-03 remain in their fired state (exit needs <300 / <=300). CCC OAS 1327 [10/20], up from 1278 [10/15].

⛔ DO NOT CARRY: the search-summary line "Houthi strikes on Saudi oil fields pushed Brent above $111". The Saudi Ministry of Energy reported the 10/21 Shaybah drone as INTERCEPTED, operations unaffected (SIG-W-20261021-007). No 10/22 Saudi field hit was found. The Iran items in the relays are planning and posture reports (SIG-W-20261021-027, SIG-W-20261022-003).

HENRY ACTION: the index-mechanics read into the US open. Your 10/21 gamma flips were ~7,744/~7,749 against SPX 7,757.17 (022, a thin cushion). VIOLET/LIQUID/SAM/ZHAO/VULCAN/REGINALD/RED/PROME INFO; REGINALD owns REG-T-04.

Source: bookmark 2113215401983152439 (post text read; image unread); coindesk.com/markets/2026/10/22/asian-stocks-tumble-bitcoin-retreats-as-china-enters-bear-market; FORGE fetch.py price and fred --first-published, 2026-10-22T11:39Z.
