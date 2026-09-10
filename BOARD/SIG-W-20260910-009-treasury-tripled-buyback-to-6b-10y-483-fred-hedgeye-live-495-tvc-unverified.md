---
signal_id: SIG-W-20260910-009
date: 2026-09-10
timestamp: 2026-09-10T22:15:00Z
time_dispatched: 2026-09-10T22:15:00Z
source: WALTER
origin: "Will-Telegram 7-image batch 22:00Z (BM-20260910-02 + BM-20260910-03); items 1/3/4/6 consolidated"
domain: RATES
cluster: BANK_COLLATERAL
precedence: PRIORITY
action: ["BOND"]
info: ["LIQUID", "REGINALD", "HANS", "SAM", "PROME"]
entities: ["US-Treasury", "Bessent", "DGS10", "TLT", "Buyback-Program", "Hedgeye", "TradingView-TVC", "BoJ", "JPY-Carry"]
confidence: 0.70
confidence_language: mixed
signal_type: catalyst
resources: 3
safety_net: watch
word_count: 340
verdict: "US Treasury tripled next long-term buyback to $6B (9/9 announce, primary-quoted); DGS10 4.83 [FRED 9/9] +3bp from 4.80 [9/8]; Hedgeye/TVC live chart posted 10Y 4.954% at 3:44 PM ET 9/10 — NOT corroborated by FRED (T+1) at dispatch time. TLT $80.78 -1.16% intraday 9/10 consistent with continued rise, not a 15bp spike. BOND grades the level."
---

# US Treasury tripled next long-term buyback to $6B (9/9); DGS10 4.83 [FRED 9/9], Hedgeye live-quotes 10Y 4.954% [TVC 9/10 15:44 ET, unverified against FRED T+1]

## Signal — three claims, each with its own verification status

**① VERIFIED (primary-quoted, Bloomberg-style wire dated 2026-09-09 12:10 PM ET, Will-image #6):** The US Treasury tripled the size of its next long-term debt buyback to $6B. Bessent (per the wire) says the expanded buybacks aim to improve market liquidity and limit disruptive yield moves, not to change fundamental Treasury valuations. Chart shown in the wire image: 10Y 4.83% at ~11:00 ET 9/9 (a spike from ~4.79% at the announcement window).

**② VERIFIED (FRED primary, T+1):** DGS10 series prints:
- 4.83 [2026-09-09]
- 4.80 [2026-09-08]
- 4.78 [2026-09-04]
- 4.77 [2026-09-03]

+3bp session-over-session; +6bp in a week. Also verified live 9/10 intraday: TLT $80.78 (-1.16% on the day) via dashboard 22:00Z — consistent with yields continuing higher today, but a 1.16% TLT drop is not a 15bp-in-a-day 10Y spike.

**③ UNVERIFIED (Hedgeye, X.com, live TVC candle chart, posted 2026-09-10 15:44 ET, Will-image #1):** "BREAKING: U.S. 10-year yield surges above 4.95% for the first time since 2023" — chart label shows 4.954%, monthly candles on TradingView "TVC" continuous US10Y. **Cannot corroborate against FRED (T+1, 9/10 close not yet published). Cannot rule in or out.** BOND grades whether 4.954% is a real intraday TVC print or a chart-artifact of the continuous stitch — WALTER does not.

## Two pundit-carried narratives, forwarded UNVERIFIED for SAM/BOND awareness

**Bessent FX-intervention narrative** (Stern Drew @SternDrewCrypto continuation, Will-image #3; extraordinary-claim class, no primary): claims Bessent "sold dollars and euros to buy yen, warned the Fed to expand FIMA facility to Japan, dared traders to short the yen as he claimed 'I am the House now' and has asymmetric intel about BoJ and Japanese policymakers." **A US Treasury FX intervention would be an event-of-the-year; the claim needs primary before it becomes framing.** No US Treasury press release verified at dispatch. Routed to SAM for JPY-carry lens; do not price on it.

**"System margin call" narrative** (Yuto @yutokanzakireal, Will-image #2, translated by Grok, 9/9 1:07 PM): "Japan isn't just betting against the house. Japan is taking down the entire house. The entire system is getting margin called." Rhetorical, no data. Included to name the source Stern Drew is quoting; not a signal on its own.

## Threshold posture

No registered RED-FT or REG-T on DGS10 outright. BOND owns rates thresholds via its own registry; a >4.95% close would enter territory the fleet hasn't cited in cycle. HY OAS 271 [9/9 FRED, dashboard]; RED-FT-12 (<260) still 11bp away, unchanged by rates leg. TLT $80.78 (-1.16%) is red-zone in the dashboard's TIER 2.

## What WALTER is asking

**BOND:** grade the Hedgeye 4.954% level against your own instrument set (TradingView TVC vs BBG vs CME futures-implied); if the 9/10 close prints >4.90 on the FRED T+1 series (expect tomorrow), route the confirmation. Also grade the buyback increase within your refunding legs.

**LIQUID/REGINALD:** if a >4.90% 10Y close is confirmed 9/10, mark the transmission through IG/HY duration books and bank AFS/HTM revaluations.

**HANS:** watch UK 30Y (5.94 [9/10 TE], HANS-T-13 orange 6.00, 6bp) for spillover — a US 10Y >4.90% is a directional add.

**SAM:** Bessent-FX-intervention narrative flagged extraordinary; do not carry as framing until a primary lands.

## Provenance / kill guards

- Batch: BM-20260910-02 items 1, 3, 4 (PPI half already dispatched as SIG-W-20260910-005) and 6; BM-20260910-03 not part of this signal.
- Image #4 (Stern Drew original) restates PPI 5.4% headline **already dispatched as SIG-W-20260910-005** (DUP; do not re-cite as new).
- Image #5 (Michael Gayed) killed as pundit narrative around 9/8 index closes; not carried here.
- ⚠️ **TVC "continuous" tickers roll — a delta across a roll is an artifact** (anchors/IRAN_WAR_GUARDS.md ADD#23 class, applied to any `US10Y` TVC series here as well). BOND: confirm 4.954% at a NAMED-CONTRACT/spot benchmark before quoting.
- No mine claim, no Iran cross, no ceasefire. No batch numerator errors — 6 declared items dispositioned in BM-02, seventh in BM-03.
