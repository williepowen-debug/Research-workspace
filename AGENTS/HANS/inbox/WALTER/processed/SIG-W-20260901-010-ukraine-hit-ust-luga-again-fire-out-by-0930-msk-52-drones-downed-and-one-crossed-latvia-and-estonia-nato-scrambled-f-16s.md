> **WALTER handoff — SIG-W-20260901-010** · role: **INFO** · precedence: PRIORITY
> Source batch: BM-20260901-02 item  (Will-requested news sweep).
> Move this file to `inbox/WALTER/processed/` when consumed.

---

---
signal_id: SIG-W-20260901-010
date: 2026-09-01
time_dispatched: 2026-09-01T21:52Z
origin: Will-requested news sweep 2026-09-01 ~22:1xZ (BM-20260901-02 item 4); TradingEconomics had already named Ust-Luga as a secondary driver of today's Brent move (carried, unmerged, in SIG-W-20260901-005). Moscow Times body read at the primary; Euromaidan/Ukrainska Pravda/OilPrice for the NATO leg.
source: The Moscow Times 2026-09-01 https://www.themoscowtimes.com/2026/09/01/ukrainian-drone-attack-sparks-fire-at-ust-luga-port-a93612 ; Euromaidan Press 2026-09-01 (Latvia/Estonia incursion, NATO F-16s); Ukrainska Pravda 2026-09-01; OilPrice 2026-09-01. Prior strike on the same facility: 2026-08-14 (Moscow Times).
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: [OSPREY]
info: [BRENT, HAWK, HANS, RED]
entities: [Ust-Luga, Leningrad region, Baltic Sea, Novorossiysk, Latvia, Estonia, NATO, Turkish F-16, Russian crude exports, Russian product exports]
signal_type: catalyst
confidence: 0.80
verdict: A Ukrainian drone attack early Tuesday 9/1 set fire to the Ust-Luga port area — Russia's largest Baltic terminal (~700 kb/d crude; 32.8 Mt of refined products exported in 2025; second only to Novorossiysk). Russian air defence claims 52 drones downed over Leningrad region in a four-hour assault; the fire was out by ~09:30 Moscow time. One drone crossed Latvian and Estonian airspace and NATO scrambled Turkish F-16s. No loading suspension or resumption statement was found. It is the second strike on the facility in 18 days (8/14) and part of a week of Baltic-port strikes.
consumer_lens: The Baltic export leg is now being hit on a cadence, on the same day Russia was shown tolling crude through Kazakhstan for lack of refining (SIG-W-20260901-002) — the crude-long/product-short state is being attacked at both ends. The NATO airspace leg is a separate object (HAWK/HANS), not an oil fact. Anti-theater-merge: this is OSPREY's theater and touches no Hormuz gate.
---

# ⚠️ PRIORITY — Ukraine hit Ust-Luga again: fire out by 09:30 MSK, 52 drones downed, one crossed Latvia and Estonia and NATO scrambled F-16s

## What is established
- **Attack:** early Tuesday 2026-09-01, ~4-hour assault; **52 drones** intercepted over Leningrad region (Russian claim). **Fire in the Ust-Luga port area, extinguished ~09:30 Moscow time** (Moscow Times). Terminal/operator/tank specifics **not** reported; **no statement on loading suspension or resumption** found.
- **Scale of the asset (Moscow Times):** *"Ust-Luga handles 700,000 barrels of crude oil per day"*; *"more than 32.8 million metric tons of refined products were exported through the port"* last year. Russia's largest Baltic terminal, second nationally after Novorossiysk.
- **Cadence:** second strike since **8/14**; Ukraine has hit Baltic ports **multiple times in the past week** (Euromaidan/OilPrice), explicitly framed as denying Russia the windfall from the oil rally.
- **NATO leg (Euromaidan):** one drone crossed **Latvian and Estonian** airspace; **NATO scrambled Turkish F-16s.** Not corroborated at a NATO/Estonian MoD primary here — carry as reported.

## Not established
- Physical damage to loading infrastructure; any throughput loss; whether tankers diverted. **Do not carry a bpd-offline figure — none exists.**
- Whether the "52 drones" is a downed count or a launched count — Russian MoD phrasing.

## Cross-desk
- Same-day companion: **`SIG-W-20260901-002`** (Russia tolling crude via Kazakhstan's Kondensat because its own refining is down) — export terminal hit + refining deficit = both ends of OSPREY's crude-vs-products channel in one day.
- **BRENT:** TradingEconomics named Ust-Luga a secondary driver of today's +5% (primary = the Iran campaign) — kept separate per the anti-theater-merge guard.
- **HAWK / HANS:** the airspace incursion + NATO scramble is the cross-war/European item; Sheskharis/Novorossiysk (8/14) was the last Black Sea analogue.

**Confidence 0.80** — multi-outlet on the event and the fire timing; single-outlet (Euromaidan) on the NATO scramble; throughput figures are the outlet's, not operator data.
