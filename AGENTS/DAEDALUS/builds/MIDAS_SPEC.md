# BUILD SPEC — MIDAS (precious + industrial metals agent)

> 🗄 **DATED BUILD RECORD — states herein are as-of the build day; do NOT cite as current.** metals_watch.py was BUILT+WIRED day 1 (7/12); registration completed 7/11; MIDAS graded L3 7/22. Current truth = FLEET_MAP row + `upgrades/PRODUCTION_REVIEW_2026-07-22.md`.

**Status:** 🟢 EXECUTED — Will approved 2026-07-11 (name MIDAS, 4 channels M1–I2, Active/always-on, dual-channel monetary+industrial). Phase 3 (final) of the 3-agent build queue (power → semis → **metals**).
**Owner:** DAEDALUS (design + build) / Will (decisions) · **Class:** Market-agent → graded vs `BLUEPRINTS/market-agent.md`
**Name:** **MIDAS** — the golden-touch king. On-the-nose for a metals (esp. gold) agent, pantheon-adjacent, collision-free.
**Session note:** built in the same continuous session as WATT + VULCAN (7/10 night → 7/11); MIDAS files dated 2026-07-11 (accurate date after rollover).

---

## 1. Locked decisions (Will, 2026-07-11)

| # | Decision | Resolution |
|---|---|---|
| Structure | **Dual-channel: monetary + industrial** | 4 channels: gold + silver (monetary) / copper + PGMs (industrial). AEOLUS channel model (empty channel = signal). |
| Cadence | **Active (always-on)** | gold (debasement trade) + copper (Dr. Copper) are live macro tells worth a persistent owner. |
| Name | **MIDAS** | — |

## 2. Mandate (one sentence)

MIDAS owns **metals as two distinct macro signals**: the **monetary channel** (gold/silver as the fiscal-debasement + real-rate + safe-haven stress tell) and the **industrial channel** (copper/PGMs as the global-growth + China-demand + supply-shock gauge).

## 3. The channel set (channels-first — PAT-018; empty channel = signal)

| # | Channel | event → mechanism → repricing | Signal surface | Routes to |
|---|---|---|---|---|
| **M1** | **Gold — debasement / real-rates** | real yields ↓ OR fiscal-debasement / CB-buying ↑ → gold bid → monetary-stress tell | gold spot, 10Y real yield (DFII10), central-bank buying (WGC), ETF flows | **BOND** (real rates, two-way), **LIQUID** (safe-haven) |
| **M2** | **Silver + gold/silver ratio** | monetary demand + industrial demand → GSR as risk-appetite/monetary gauge | silver spot, gold/silver ratio, silver ETF flows | LIQUID (risk-off amplifier), I-channel (industrial overlap) |
| **I1** | **Copper — Dr. Copper / China** | global growth + China demand → copper price + LME inventory → growth gauge | copper spot, LME/COMEX inventory, China imports | **ZHAO** (China demand, two-way), HENRY (growth velocity) |
| **I2** | **PGMs (platinum / palladium)** | auto + industrial demand + SA/Russia supply concentration → PGM price | Pt/Pd spot, auto production, SA/Russia supply | **HAWK** (supply geopol), HENRY (auto/industrial) |

*S5-equivalent (tier-2, not launched): a dedicated mining-supply channel (SA/Russia/Chile concentration, strike/outage risk) — folded into M/I channels for now, promote if supply shocks recur.*

## 4. Boundaries — clean seams (reconcile-to-one-figure, don't silo)

| Neighbor | They keep | MIDAS takes | Seam |
|---|---|---|---|
| **BOND** | US real rates / auctions / rate structure | **gold as the debasement/real-rate tell** | M1 two-way: BOND owns the real-yield level; MIDAS owns what gold's divergence FROM it says (gold bid despite positive real yields = debasement premium). Reconcile the DFII10 figure to one number. |
| **ZHAO** | China macro / capital flows | **copper as the China-demand read** | I1 two-way: ZHAO owns China macro; MIDAS owns copper as its physical-demand thermometer. |
| **LIQUID** | HY/credit spreads / liquidity | **gold/silver safe-haven flow** as a risk-off amplifier | M1/M2: gold spikes on the same stress LIQUID tracks — cross-confirm, one figure. |
| **HAWK** | geopolitical / military | **PGM supply consequence** (SA/Russia concentration) | I2: HAWK owns the geopolitics; MIDAS owns the metals-supply repricing. |
| **HENRY** | macro velocity | copper/PGM as growth/industrial tells feeding velocity | MIDAS supplies the metal read; HENRY owns the macro thesis. |

## 5. Data surfaces (free where it matters)

- **Real yields** — FRED `DFII10` (confirmed live: **2.31, 2026-07-09**), the M1 driver.
- **Spot prices** — gold/silver/copper/PGM via the shared FORGE `fetch.py` (yfinance; ETF proxies GLD/SLV/CPER/PPLT/PALL to validate — futures GC=F errored on test). Gold/silver ratio computable.
- **Central-bank gold buying** — World Gold Council (quarterly, free).
- **LME/COMEX inventory** — copper stocks (free headlines).
- **Honest walls:** granular physical-market / concentrate data is subscriber-only — proxy via price + inventory + ETF flows.

## 6. Blueprint instantiation — same as WATT/VULCAN (market-agent.md §1–§8). Universal 5-pt per channel + local state; banded thresholds (durable rules / live STATUS read); channel-kill vs thesis-kill; PREDICTIONS `MIDAS-NN` (gold real-rate divergence / copper-growth / GSR calls resolve on a clock); NEXUS_BRIEF writeback; boot.py (staleness + predictions-due at launch — **`metals_watch.py` = the priority first-session increment**: real-yield [FRED confirmed] + gold/silver/copper/PGM spot [ETF proxies] + GSR, PAT-041-wired).

## 7. File scaffold (created on approval — mirrors WATT/VULCAN)

```
AGENTS/MIDAS/  CLAUDE.md STATUS.md THESIS.md TRADE.md boot.py SCRATCH.md
               NEXUS_BRIEF.md LESSONS.md workbook/{SCHEMA,KB,VX,FLOW,PREDICTIONS}.tsv
               inbox/ outbox/ sources/
```

## 8. Wiring (gated on approval + idle targets)
1. Scaffold `AGENTS/MIDAS/`.
2. **Routed to PROME** (shared/home-dir files, git rule): ROSTER row + root CLAUDE active-list/chain + AGENTS.md row.
3. **BOND / ZHAO / LIQUID / HAWK / HENRY notes** (inbox): the M1/M2/I1/I2 seams (BOND + ZHAO are the two-way ones).
4. FLEET_MAP row + FLEET_DIRECTORY regen **held until PROME registers ROSTER** (render guard), same as WATT/VULCAN.

## 9. Proposal summary
- **What:** market-class dual-channel metals agent (monetary gold/silver + industrial copper/PGM), 4 channels, systemic macro-tell lens.
- **Why:** two of the tape's best macro tells (gold-debasement, Dr.-Copper) have no owner; gold's divergence from real rates is a live debasement signal, copper is the cleanest China-growth thermometer.
- **Effort:** ~1 session scaffold + wire; metals_watch.py the first content increment.
- **EV:** a continuous monetary-stress + growth-demand read feeding BOND (real rates), ZHAO (China), LIQUID (safe-haven), HENRY (growth), with real-rate-divergence + copper-inflection calls on a resolvable clock.
