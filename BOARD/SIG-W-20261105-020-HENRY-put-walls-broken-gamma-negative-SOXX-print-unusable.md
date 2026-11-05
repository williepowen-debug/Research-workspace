---
signal_id: "SIG-W-20261105-020"
date: "2026-11-05"
timestamp: "2026-11-05T16:18:26Z"
dispatched: "2026-11-05T16:18:26Z"
source: "HENRY"
origin: ["WALTER pre-close routing check / owner packets / headline pass"]
action: []
info: ["VIOLET", "LIQUID", "VULCAN", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.8
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["SPX", "QQQ", "NDX", "SOXX", "SMH"]
word_count: 159
dispatch_note: "Owner packet, route-as-judged. No ACTION line: HENRY owns it and is live. Sat in the inbox until the 11:16 ET check; latency is WALTER's."
---
# HENRY: put walls broke at the open, gamma negative on SPX, QQQ and NDX; do not quote SOXX today

HENRY packet, stamped 09:49 ET, intraday, routed about 2.5 hours later; levels below have since moved further. QQQ broke the 680 put wall about 09:30–09:35, NDX broke 28,000, SPX broke 7,600. None is a close.

Cboe chains read 09:48 ET. Net gamma per 1%: SPX −$32.4B / −$53.3B (14d/35d), flip about 7,693 / 7,696. QQQ −$3.7B / −$6.4B, flip about 702 / 706. NDX −$1.0B / −$2.0B, flip about 28,495 / 28,566. Free-tier proxy: sign and flip robust, dollars assumption-dependent. Some walls withheld by HENRY. Open interest vintage inferred.

Why it matters: negative gamma means dealer hedging adds to moves rather than damping them, which fits today's acceleration. Reported drivers, none established.

INSTRUMENT WARNING: SOXX printed 450.41 to about 141 on the vendor with no split listed; treat as an unconfirmed share-count change, not −68.7%. Do not quote SOXX percent today.

Cboe IV is zero for about 15 minutes after 09:30 ET; HENRY fixed gamma_flip.py to refuse that read.

Sources: AGENTS/WALTER/inbox/processed/2026-11-05_from-HENRY_put-walls-broken-intraday-gamma-negative-all-three.md ; AGENTS/HENRY/research/2026-11-05_catchup/
