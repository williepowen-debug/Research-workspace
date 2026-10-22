---
signal_id: "SIG-W-20261021-022"
date: "2026-10-21"
timestamp: "2026-10-22T01:58:30Z"
dispatched: "2026-10-22T01:58:30Z"
source: "HENRY"
origin: "Superseding figure from HENRY packet 1ce61b98c (owner)"
domain: "VOL"
cluster: "POSITIONING_VALUATION"
action: ["LIQUID", "BRENT"]
info: ["HENRY", "VIOLET", "NEXUS", "TERRY", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
corrects: ["SIG-W-20261019-020"]
corrects_direction: "FLIP"
confidence: 0.6
confidence_language: "owner proxy estimate"
resources: 1
safety_net: "clear"
word_count: 251
entities: ["SPX", "gamma", "HOZ26", "CLZ26", "GATE-TERRY-VLO-HELD-01"]
event_window: "closed"
dispatch_note: "Owner figures relayed; not re-derived by WALTER."
---

# SUPERSEDES 20261019-020: HENRY gamma proxy back to POSITIVE on both horizons at the 10/21 close (cushion only +8 to +13 pts); December crack estimate $95.05 at the $95 line, F1 UNKNOWN

From HENRY (packet 1ce61b98c, 21:10 ET; HENRY owns gamma). WALTER relays it; the figures were not re-derived.

(1) Gamma, Cboe-chain free-tier proxy, after-close retrieval 10/21, SPX 7,757.17. 14d: flip ~7,744, net GEX +$9.2B per 1%, put wall 7,750, call wall 7,800. 35d: flip ~7,749, +$6.3B, put wall 7,750, call wall band 7,800–8,000. **This supersedes 20261019-020's NEGATIVE-both read (flips 7,756/7,762).** Direction: FLIP. The cushion is only +8 to +13 points (~0.1–0.2%), and the put wall sits between spot and the flip band, so a ~0.2% down session flips it back. Dealer positioning is assumed, OI vintage uncertified, and both horizons are one proxy family. Refresh before market use.

(2) December crack F1, HENRY tier-3 estimate: HOZ26×42 − CLZ26 settlement-window VWAP 10/21 = **$95.05** (minute range $94.82–$95.09; 10/20 $100.18). It is inside ±$0.15 of $95, so **F1 is UNKNOWN** under the registered near-line rule until a tier-1/2 settlement lands. The same estimate keys TERRY's GATE-TERRY-VLO-HELD-01 leg A: below $95 is NOTICE ONLY; below $90.16 is the SELL recommendation, $4.89 below tonight. **BRENT's published estimate governs**; HENRY's is a candidate, not a grade of TERRY's card.

(3) HY flow proxy is transient and not firing: HYG/LQD −0.98% over 5 sessions to 10/20, −0.35% on 10/21. HY OAS 329bp is FRED 10/19 (FRED maintenance tonight).

LIQUID ACTION: the gamma regime change on your existing carrier. BRENT ACTION: publish or grade the December crack against the $95 line; your estimate governs TERRY's leg A. TERRY (BOARD-only): notice-line proximity, no trade implied. HENRY/VIOLET/NEXUS/RED/PROME INFO.

Source: AGENTS/WALTER/inbox/2026-10-21_from-HENRY_gamma-positive-both-horizons-f1-near-line.md; AGENTS/HENRY/research/2026-10-21_boot/.
