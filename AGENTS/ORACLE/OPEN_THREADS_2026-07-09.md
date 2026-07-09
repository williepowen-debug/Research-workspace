# ORACLE — Open Threads (2026-07-09 ~21:30 ET)

Grounded in tonight's pull (`STATUS.md`, `DIVERGENCE_2026-07-09.md`, `VX.tsv`). No trade recs.

## 1. Open Questions

| # | Item | Why unresolved | Liq |
|---|---|---|---|
| 1 | Kalshi June U3 >4.2%/>4.3% | `[finalized]` is the fetcher's own tag (last-trade 82%/25%), NOT a confirmed binary settlement — I can't verify TRUE/FALSE from the API alone | — |
| 2 | Citi Q2 prov >$2.9B | Swung 60%→31.5% (Δ7d −27.5) on **$2.7K liq** — single-print, unusable until a 3-day re-check | ⚠️thin |
| 3 | BAC Q2 prov >$1.4B | **$12 liq** — effectively zero depth, price is noise, not a read at all | ⚠️no depth |
| 4 | Iran-targets-shipping-by-Jul31 (new pin) | 54.5% on **$4.6K liq**, Δ1d −30 — single print, direction unconfirmed | ⚠️thin |
| 5 | WTI $80-Jul | Δ1d −24.5 on $20.8K liq (moderate, not thin) — real move or a bad print? Needs next pull to confirm | ⚠️re-check |
| 6 | US-Iran deal "Recon. Funding" leg | Δ1d +9.0 but Δ7d only −0.5 (flat week) — likely daily noise, not flagged as signal, but unconfirmed | moderate |

## 2. Gaps (coverage holes)

| Gap | Detail | Fix |
|---|---|---|
| **BRENT-sustain (Brent >$75)** | No Brent-denominated market exists on either platform; nearest (WTI $80-Jul) tests a harder bar — found tonight, still open | Pin the moment a matching market opens |
| **HAWK ladder B/C rungs** | Only D (severe) has a matched market (blockade, converges). B (de-escalation) and C have no clean analog — I improvise with Hormuz-normal-Dec31, wrong time-horizon | Needs a purpose-built short-window market or accept as untestable |
| **Structural credit axis (HENRY's dormant thesis)** | Kalshi CRE-default/CC-delinquency/charge-off/Fed-facility series all exist, **zero events open** — the exact axis the fleet worries could re-ignite has NO crowd read right now | Re-check each session (standing item) |
| **MOVE / rates-vol** | Tonight's digest: "stress lives in rates-vol, not VIX" — neither platform has a MOVE-index or rates-vol market at all | Real blind spot, no known fix on these two venues |
| **Russia diesel-export/refinery axis** | Only "Russia-Ukraine ceasefire" tracked (40.5%) — no market on the Russia supply-side root the digest flagged 7/9 | Search for a Russia-refinery/export market; may not exist |
| **Venue breadth** | Only Polymarket + Kalshi. Not watching Deribit/CME oil-vol (options-implied, would beat a binary market for the BRENT gap) or Metaculus (non-real-money, lower value) | Worth a one-time scoping look, not urgent |

## 3. Threads to Pull

| Thread | Why it matters | What it takes | Urgency |
|---|---|---|---|
| **Fed-hike-2026 recross >50% — driver unknown** | Digest doesn't explain it; energy-shock→inflation-expectations (new transmission channel) vs Fed-specific noise are very different reads for LIQUID/HENRY | Cross-ref Polymarket CLOB hourly history vs a Fed-news timeline 7/7-7/9 | **This week** |
| **Disruption-vs-supply spread as a standing indicator** | ~8 markets are drawing one consistent line (Hormuz hit hard, oil supply untouched) — currently only visible by eyeballing STATUS row-by-row, no single tracked number | Log a derived series (blockade % − WTI-$100 %) each pull; the spread collapsing is HAWK/BRENT's regime-flip tripwire | Background |
| **Hormuz ladder — physical signal or circular echo?** | Ships-per-day rungs cratered on real liquidity ($44-92K) — genuine leading indicator IF independent of HAWK/BRENT's own AIS sourcing; a mirror if not | HAWK/BRENT confirm whether the market's resolution source overlaps their own traffic data | This month |

*3 files this session: this doc + tonight's STATUS/DIVERGENCE already committed. No push.*
