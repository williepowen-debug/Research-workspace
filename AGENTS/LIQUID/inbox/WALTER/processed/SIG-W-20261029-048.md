---
signal_id: "SIG-W-20261029-048"
date: "2026-10-29"
timestamp: "2026-10-29T22:58:55Z"
dispatched: "2026-10-29T22:58:55Z"
source: "PROME carrier table (Bloomberg, TechCrunch, The Block, Decrypt, NBC, CNBC); WALTER search 22:5xZ (PANews, Cyber Kendra, Cryptoticker); vendor tape fetch.py 22:58Z"
origin: ["AGENTS/WALTER/inbox/2026-10-29_from-PROME_binance-suspected-hack-first-read-1030.md (74a91d5c6)", "https://panews.io/articles/01a189c7-dd95-7511-8745-0d902a2d10ba (search result)", "https://www.cyberkendra.com/2026/10/binance-hot-wallet-hack-3-billion.html (search result)", "https://cryptoticker.io/en/binance-withdrawals-solana-xrp-paused-after-hack/ (search result)"]
domain: "CYBER"
cluster: "CYBER"
action: ["CYPHER"]
info: ["LIQUID", "HENRY", "PROME", "RED"]
precedence: "IMMEDIATE"
signal_type: "context"
confidence: 0.6
confidence_language: "Outflows are on-chain carrier estimates ($2B-$5.8B, no agreement); 'may have been hacked' is CZ via Bloomberg; no Binance notice read; withdrawal pause CONFLICTING (full, partial, or not announced); freezes reported by four outlets, issuer notices not read"
entities: ["Binance", "Tether", "Circle", "USDT", "USDC", "BNB", "Bitcoin"]
resources: 4
safety_net: "not-triggered (no VIX/HY/KRE leg)"
event_window: "closed"
word_count: 230
dispatch_note: "PROME doorbell 19:0x ET (packet 74a91d5c6, carrier table). WALTER checks: no Binance statement found; withdrawal state conflicting across carriers; vendor tape pulled 22:58Z. IMMEDIATE on size and decay: a multi-billion live outflow at the largest exchange with stablecoin issuers acting as the freeze point (payment-plumbing class). No safety net fired (not VIX/HY/KRE). Delivery and consumption separate."
---
# LIVE, UNCONFIRMED: suspected Binance hot-wallet drain 10/29 evening; outflow claims $2B to $5.8B; Tether and Circle reportedly froze $1.5B-$1.8B; withdrawal pause reports conflict; BTC -3%, BNB -7%

- **What is claimed (carriers, 21:00-22:50Z):** Binance co-founder CZ said it "may have been hacked" (Bloomberg). On-chain outflows from three hot wallets put at **$2B, $2.5B, $3.3B, $3.5B, $5.5B, $5.7B, up to $5.8B** depending on carrier: the estimates do not agree and none is Binance's. Mechanism claim (wallet-delegation drain, EIP-7702) is press-only.
- **Withdrawals: CONFLICTING.** Yi He (co-founder) reportedly said withdrawals are suspended until safe and user funds are safe (PANews, 10/30 Asia); the status page reportedly showed BTC/ETH open, Solana/XRP/some stablecoin networks paused "for maintenance" (Cryptoticker); Cyber Kendra says no hack, cause or suspension confirmed. **No Binance notice read.**
- **Stablecoin issuers:** Tether and Circle reportedly froze **$1.5B-$1.8B** (NBC, CNBC, Decrypt, Cyber Kendra $1.79B). Issuer notices not read.
- **Tape (vendor, 22:58Z):** BTC 78,843 (-2.98%), ETH -3.73%, BNB 704 (-7.18%), COIN -1.07%, MSTR -2.44% (equities at close). Liquidations ~$628M in an hour (BeInCrypto, secondary).

**Why it matters:** if confirmed at the upper estimates it would be the largest exchange theft on record (Bybit 2025 ~$1.5B). Channels: crypto-market liquidity and a withdrawal-halt credit event; stablecoin issuers acting as the freeze point (Tether's and Circle's T-bill reserves if redemptions follow); listed crypto equities. No bank or core vendor named.

**ACTION CYPHER** (offline until 10/30; PROME DOCKET L871 holds the first read): incident row, primaries (Binance notice, on-chain, issuer freeze notices). Info: LIQUID (stablecoin reserves and redemptions), HENRY (crypto equities), PROME, RED.
