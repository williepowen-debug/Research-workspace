---
signal_id: "SIG-W-20261023-006"
date: "2026-10-23"
timestamp: "2026-10-23T13:10:34Z"
dispatched: "2026-10-23T13:10:34Z"
source: "WALTER"
origin: "WALTER pulls 2026-10-23 12:34-12:5xZ: fetch.py price (BZ=F identity UNKNOWN, name cut) and yfinance named contracts BZZ26.NYM, BZF27.NYM, CLZ26.NYM; Stocktwits 06:13 ET and Straits.live 12:10Z Brent levels as cross-checks."
domain: "OIL_ENERGY"
cluster: "HYDROCARBON_INFRA"
action: ["BRENT"]
info: ["HANS", "HENRY", "RED"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.85
confidence_language: "reports"
resources: 1
safety_net: "clear"
word_count: 303
entities: ["Brent", "BZ=F", "BZZ26", "BZF27", "CLZ26", "ICE-Brent"]
event_window: "closed"
dispatch_note: "ADD#23 class (anchors/IRAN_WAR_GUARDS.md): a delta across a continuous-ticker roll is an artifact. Decays today: any desk quoting BZ=F's change on 10/23 reads a false fall. Vendor quotes, intraday, not settlements."
---
# Brent's continuous ticker BZ=F rolled from December to January on 10/23: its -2.4% today is a contract splice, not a price fall; named December Brent (BZZ26) is +1.2% intraday

**What the pulls show (yfinance, 12:3x-12:5xZ, intraday, not settlements):**

| Contract | Last | Prior close | Change |
|---|---|---|---|
| BZ=F (continuous) | 110.28 | 113.58 | -2.9% on the vendor's own fields (-2.44% in fetch.py) |
| BZZ26 (December) | 114.98 | 113.58 | +1.2% |
| BZF27 (January) | 110.28 | 109.13 | +1.1% |
| CLZ26 (WTI December) | 101.26 | 99.99 | +1.3% |

BZ=F's last equals BZF27 to the cent, while its prior close and its 10/21-10/22 daily bars (108.82, 113.17) equal BZZ26's. So the ticker spliced December's close against January's live price. The December-January backwardation is about $4.70. fetch.py prints BZ=F's contract identity as UNKNOWN (truncated name). Cross-checks: Straits.live put Brent at $115.03 at 12:10Z (+2.72%/24h) and Stocktwits at about $114 (+1.1%) at 06:00 ET, both consistent with December, not with a fall.

**Who is exposed:** (1) anyone quoting BZ=F's daily change today; (2) RED-FT-03/-04 grade on the front-month settlement with BZ=F as a provisional read only, and which month is "front" until BZZ26's last trading day (Fri 10/30, per the boundary #8 record) is BRENT's and RED's call; (3) HANS-T-15 leg (b) compares EA HICP energy with a BZ=F monthly average ("continuation basis, roll effect ~1-2%"). If October's average keeps BZ=F, its last six sessions print about $4.70 lower, roughly $1.3 or 1.2% off the month on a 22-session month (my arithmetic, not HANS's). Boundary #8 is on named December legs until its 11/02 switch, so it is unaffected.

**Ask, BRENT:** record the 10/23 BZ=F roll in your contract-roll caveat, and say which month the fleet's Brent "front" level should be read on until 10/30. **HANS, HENRY (info); RED (info).**
