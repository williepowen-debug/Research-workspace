---
signal_id: "SIG-W-20261029-049"
date: "2026-10-29"
timestamp: "2026-10-29T23:44:20Z"
dispatched: "2026-10-29T23:44:20Z"
resources: 2
safety_net: "clear"
event_window: "closed"
signal_type: "context"
source: "x-bookmarks (Will) x8: @TreeNewsFeed, @adamscochran, @Kalshi_Crypto, @FaytuksNetwork, @Kalshi, @WatcherGuru, @crypto_banter, @spreekaway (20:32-21:18Z)"
origin: ["x-bookmarks 2115906842412875959, 2115908225010749885, 2115915354081833234, 2115916297817018621, 2115909167667990686, 2115913607644860593, 2115907468689559643, 2115904721856651382"]
domain: "CYBER"
cluster: "CYBER"
action: ["CYPHER"]
info: ["LIQUID", "HENRY", "PROME", "RED"]
precedence: "PRIORITY"
confidence: 0.55
confidence_language: "Aggregator and analyst posts; on-chain transaction cited but not traced by WALTER; Lazarus attribution is one analyst's pattern read; 'CZ confirms' conflicts with Bloomberg's 'may have been hacked'"
entities: ["Binance", "Circle", "Tether", "Tornado-Cash", "Lazarus"]
word_count: 132
dispatch_note: "Update to SIG-W-20261029-048 from eight Will bookmarks (folded into one card). Adds the per-issuer freeze split and the wallet/initiator detail; does not change 048's precedence or routing. Delivery and consumption separate."
---
# Binance update (to 048): one hot wallet ('Binance 14') reportedly drained of ~$2.53B in 60+ tokens to a fresh address whose initiator was funded through Tornado Cash; Circle froze $823M and Tether $971M (= $1.79B); 'CZ confirms hack' is one aggregator's line, Bloomberg had 'may have been'

New detail since 048 (all from posts, 20:32–21:18Z):
- **Wallet:** a single Binance hot wallet ("Binance 14") sent ~**$2.53B** across **60+ tokens** on Ethereum to a fresh address; the transaction was initiated by an address funded via **Tornado Cash** (a coin mixer), with no test transactions (@crypto_banter, @TreeNewsFeed, @spreekaway; tx hash cited, not traced by WALTER). Other outflow posts: "near $3B" (@Kalshi).
- **Freezes, split:** **Circle $823M** (USDC) and **Tether $971M** (USDT) = **$1.794B**, matching the $1.79B total in 048.
- **Attribution:** "fits the pattern of North Korea's Lazarus" is one analyst's read (@adamscochran), **not an attribution**.
- **Binance's word:** @FaytuksNetwork says CZ "confirms Binance has been hacked"; Bloomberg's earlier line was "may have been hacked". **Unresolved; no Binance notice read.**

Routing unchanged from 048. ACTION CYPHER; info LIQUID, HENRY, PROME, RED.
