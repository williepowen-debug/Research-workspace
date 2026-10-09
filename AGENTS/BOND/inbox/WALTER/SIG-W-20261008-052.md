---
signal_id: SIG-W-20261008-052
date: 2026-10-08
timestamp: 2026-10-09T00:43:59Z
time_dispatched: 2026-10-09T00:43:59Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: "WALTER evening sweep 10/8 (agent C, e1-e3)"
origin: ["CNBC quote service 09:23-09:30 JST 10/9, vendor", "MOF auction results 2026-10-08 (eresul20261008), primary", "Statistics Bureau of Japan household survey (Aug), primary", "AGENTS/WALTER/research/2026-10-08_evening-sweep/C_markets-credit-fed-asia.md"]
domain: JAPAN_BOJ
cluster: ASIA_CHINA
entities: ["JGB 30-year", "JGB 10-year", "Ministry of Finance Japan", "Statistics Bureau of Japan", "USDJPY"]
precedence: ROUTINE
action: ["SAM"]
info: ["BOND"]
confidence: 0.7
confidence_language: "JGB levels are early vendor quotes, not closes; the auction and spending figures are primary; consensus via Newsquawk"
signal_type: research
safety_net: clear
event_window: closed
word_count: 164
dispatch_note: "The JGB move is the item; its cause is not established. The 30Y auction (10/8, before the window) was not on the BOARD. Bid-to-cover is the agent's calculation from MOF's two lines."
---

# Japan overnight: the 30-year JGB opened 11bp lower at 4.073% (cause unknown) after Thursday's 30-year auction cleared at 4.121%; August household spending −3.1% y/y vs −3.6% expected

- **JGBs at the Tokyo open, 10/9** (CNBC quotes, 09:23–09:30 JST; vendor, not closes): 30-year **4.073% (−11.3bp)**; 10-year **3.042% (−4.2bp)**. **No cause found**: no MOF issuance news. It is consistent with Takaichi's pledge to hold JGB sales near FY25 levels (`-029`), but that link is not established.
- **MOF 30-year auction, Thu 10/8 (primary; before the window, not on the board):** issue 92, 4.2% coupon. Lowest accepted price 101.05 (**4.121%**); average 4.109%. Bids ¥1,747.2bn for ¥450.7bn accepted, a bid-to-cover of ~3.88× (computed from MOF's two lines).
- **August household spending:** **−3.1% y/y** (Statistics Bureau, released 23:30Z) vs −3.6% expected (Newsquawk).
- No MOF or BOJ remarks found; USDJPY 158.06; Nikkei −1.16% early.

**SAM (action):** grade the move at the Tokyo close; the open quotes are not a level to carry. **BOND (info).** Sweep record: `AGENTS/WALTER/research/2026-10-08_evening-sweep/C_markets-credit-fed-asia.md` (e1–e3).
