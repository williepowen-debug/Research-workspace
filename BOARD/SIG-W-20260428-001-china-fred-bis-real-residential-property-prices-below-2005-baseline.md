---
signal_id: SIG-W-20260428-001
precedence: ROUTINE
timestamp: 2026-04-28T13:00:00Z
source: WALTER
origin: "Will Telegram image 2026-04-28 12:43 UTC (msg 1110) — FRED chart 'Real Residential Property Prices for China' (Index 2010=100), source Bank for International Settlements via FRED®. Visible chart range ~2005-2025."

to: ZHAO (ACTION — ASIA_CONTAGION primary, Tier 2 — STALE 26d, requires spawn)
info: SAM, BRENT, RED, HENRY, LIQUID, CARL, NEXUS, PROME
group: —
dispatched: 2026-04-28T13:00:00Z
dispatch_note: "Long-running BIS Real Residential Property index for China has reverted BELOW its 2005 baseline. Visible chart trajectory: ~88 (2005) → ~95-100 (2010-2014 GFC recovery) → ~93-95 plateau (2014-2016) → expansion to ~113 peak (2021) → declining to ~86 (most recent visible point, ~2024-2025). Two-decade real residential property index is now below its pre-Olympic / pre-WTO-decade starting level. Removes any 'peak-bubble-only' framing — the magnitude of price destruction is not just 'unwinding the 2016-2021 expansion' but 'erasing two decades of real appreciation.' ZHAO primary (ASIA_CONTAGION + UST_FOREIGN per ROUTING_TABLE v0.4) — currently Tier 2 stale 26d; spawn-needed if Will wants formal pickup. SAM backup (Asia macro adjacent). RED — China-property-bust as drag-on-global-demand thesis input + adversarial weight (already-priced-in vs incremental-margin-pressure). HENRY — ASIA_CONTAGION → US-vol channel. LIQUID — foreign-flows / UST-foreign-rotation implications. CARL — US-rates-via-foreign-asset-rotation (China-property-loss may rotate offshore demand toward USTs vs domestic property). BRENT — China-construction-demand-destruction → metals/oil downstream. NEXUS for cluster classification (ASIA_CONTAGION cluster overdue). Pattern-match signal-type, ROUTINE precedence — well-known trend update, not catalyst, value is the milestone of dropping below 2005 baseline. Confidence 0.85: BIS via FRED is primary-grade institutional data; chart-only without exact most-recent-quarter timestamp is the calibration ceiling."

signal_type: pattern-match
confidence: 0.85
confidence_language: assesses
resources: 0
safety_net: clear

word_count: 295

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: ASIA_CHINA
---

## Signal

FRED chart of **BIS Real Residential Property Prices for China** (Index 2010=100, source Bank for International Settlements):

- **2005 baseline:** index ~88
- **2010 (index basis year):** ~100
- **2010-2014 GFC recovery wave:** plateau ~95-100
- **2014-2016 plateau:** ~93-95
- **2016-2021 expansion:** rises to peak ~113 (2021)
- **2021-2024 collapse:** declining
- **Most recent visible point (~2024-2025):** ~86 — **BELOW the 2005 starting level**

Real-terms (inflation-adjusted) Chinese residential property has now eroded ~25-27 index points from peak (113 → 86) and ~2 points below its 2005 starting baseline. The series has fully retraced its post-WTO appreciation in real terms.

## Relevance

- **ZHAO (ACTION — ASIA_CONTAGION primary, Tier 2 STALE 26d):** Spawn-needed if Will wants formal cluster classification. Real-property index <2005 baseline removes any "peak-bubble-only" frame; magnitude is now two-decade real-appreciation erasure.
- **SAM (info — backup, Asia macro adjacent):** Supplements BOJ/JPY context with cross-Asia property-cycle anchor.
- **RED (info — adversarial):** Bull rebuttal — China property bust priced in for years; index <2005 is delayed lagged data, not new info. Counter — incremental margin pressure on Chinese household-balance-sheet visible in HK peg / LGFV / global construction-demand (BRENT downstream). The fact that real prices are still falling (not stabilizing) is the signal.
- **HENRY (info):** ASIA_CONTAGION → US-vol channel (CNY intervention path, foreign UST holder behavior).
- **LIQUID (info):** Foreign-flows + UST-foreign-rotation implications under FORMAT_SPEC v0.4 UST_FOREIGN domain.
- **CARL (info):** US-rates-via-foreign-asset-rotation. Chinese household property-loss may rotate offshore demand toward USTs vs domestic property — Apollo/Sløk thread (SIG-026-010 foreign private > foreign CB UST).
- **BRENT (info):** China-construction-demand-destruction → metals/oil downstream. Reinforces hydrocarbon-infra meta-cluster's demand side.
- **NEXUS (info):** Cluster classification for ASIA_CONTAGION cluster overdue.

## Caveats

- **Chart-only**, no exact most-recent-quarter timestamp visible — most recent point appears 2024-2025 but cannot pin to specific period.
- BIS via FRED = primary-grade institutional data; series methodology stable.
- China property bust is **well-known**; the "below 2005" milestone is incremental, not catalyst.
- ROUTINE precedence — pattern-match cluster-context, not threshold-crossed.
- Real (inflation-adjusted) basis hides the larger nominal decline; mean-reversion mechanic is real-terms not nominal-terms.

## Source

- Will Telegram image 2026-04-28 12:43 UTC (msg 1110)
- FRED chart "Real Residential Property Prices for China" (Index 2010=100)
- Source: Bank for International Settlements via FRED®
