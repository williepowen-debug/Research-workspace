---
signal_id: SIG-W-20261008-036
date: 2026-10-08
timestamp: 2026-10-08T20:31:28Z
time_dispatched: 2026-10-08T20:31:28Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["api.fiscaldata.treasury.gov auctions_query + buybacks_operations (read by WALTER)", "investingLive/Newsquawk (tail)", "three outlets (Musalem)", "CBOE yield indices 14:59 ET", "research/2026-10-08_afternoon-sweep/B_rates-credit-equities.md"]
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
entities: ["US Treasury", "30-year bond", "CUSIP 912810UW6", "Treasury buyback", "Musalem", "St. Louis Fed", "DGS30"]
precedence: PRIORITY
action: ["BOND"]
info: ["ZHAO", "LIQUID", "HENRY", "RED", "TERRY", "PROME"]
confidence: 0.9
confidence_language: confirmed
signal_type: research
safety_net: clear
event_window: closed
word_count: 296
dispatch_note: "Auction high yield/BTC and buyback amounts verified by WALTER at Treasury Fiscal Data; bidder shares are of COMPETITIVE accepted (market convention; 70.45/97.42 of total = 72.32). -030 item is NOT correction-class: -030 was right on FRED data available at 11:57 ET; DGS30 10/7 posted later (T+1). RED-FT-11 not graded here (RED's). ZHAO info: indirect share is UST_FOREIGN composition."
---

# 30-year auction 10/8 at 5.618% — highest since at least 2001 — with indirect demand down and dealers taking 3x September's share; the $6B long-end buyback filled 100%

1. **30Y reopening (Treasury Fiscal Data, primary; WALTER-verified):** CUSIP 912810UW6, 29-yr 10-mo, $22B. High yield **5.618%** (Sept 5.308%); bid-to-cover **2.54** (2.61; 12-auction avg 2.42). Shares of *competitive* accepted: indirect **72.32%** (79.48%), direct 20.89% (18.31%), **dealers 6.79%** (2.21%). Tail +0.1bp vs WI 5.617% (secondary). "Since 1999" is NOT established: Treasury's dataset lacks 2000 auctions.
2. **Buyback (primary; WALTER-verified):** 20Y–30Y bucket, Liquidity Support, **$14.886B offered vs $6.0B max, $6.0B accepted = 100%**, 10 of 34 issues, settles 10/9. First full fill since the cap rose to $6B (9/24: $4.078B, 68%). All into low-coupon 2049–2051 bonds (per the sweep; issue split not re-verified).
3. **`-013` upgrade, not a correction:** Treasury labels the 10/6 bucket "2Y to 3Y" and its max was $4B ⇒ $1.33B accepted = a 33% fill. Every `-013` figure matches.
4. **Fed:** St. Louis Fed's Musalem (~13:57 ET): *"more monetary policy firming will be required,"* 6–9 month horizon, no commitment on October (secondary, three outlets).
5. **Closes:** 30Y 5.606% / 10Y 5.231% (CBOE yield indices, 14:59 ET) — the 30Y closed **below** the auction stop; TLT +0.93%. The midday Trump/Iran post (`-034`) pulled yields with oil: 30Y 5.66% → 5.62% by 12:45 (CBS).
6. **Data update to `-030`:** FRED has since published **DGS30 5.67% for 10/7**, above the 5.66% [10/5] that `-030` called the high. `-030` was right on the data available at 11:57 ET (FRED runs T+1). New high close: **5.67% [10/7]**.

**BOND:** auction/buyback read. RED-FT-11 is RED's to grade (needs the 10/8 FRED close). **ZHAO:** indirect share −7pp is a foreign-demand composition read. Credit: FRED 10/8 HY not yet out; 309bp [10/7] near-trigger stands (`-030`).

> **ADDITIVE CORRECTION — SIG-W-20261008-041:** item 1's "Treasury's dataset lacks 2000 auctions" is FALSE (BOND packet 10/8; WALTER re-queried Treasury Fiscal Data directly). The 2000 auctions are present under non-literal term strings; 5.618% is the highest 30-year stop since 2000-08-10 (5.697%). The headline "since at least 2001" HOLDS; "since 1999" is false. All other figures hold. Immutable handoffs require -041 alongside -036.
