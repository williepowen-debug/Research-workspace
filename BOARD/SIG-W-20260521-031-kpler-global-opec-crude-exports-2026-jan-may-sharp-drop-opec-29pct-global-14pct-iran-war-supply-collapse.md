---
signal_id: SIG-W-20260521-031
precedence: PRIORITY
timestamp: 2026-05-22T03:02:00Z
source: WALTER
origin: "Will Telegram image-batch 2026-05-22 02:17 UTC msgs 1933+1934 (paired Kpler charts: Global Crude Exports kbbls/d 2022-2026 multi-year + OPEC+ Crude Exports kbbls/d 2022-2026 multi-year); Kpler primary institutional commodity-flow tracker"

to: BRENT (ACTION)
info: HAWK, SAM, LIQUID, CARL, RED, NEXUS, PROME

signal_type: pattern-match
confidence: 0.85
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: ~240

cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
signal_role: cluster_mediating
event_window: closed

verify_research_verdict: SKIP-VERIFY (Kpler institutional primary commodity-flow tracker; charts directly observable; data source labeled on both charts)
mark_context: Two paired Kpler charts shared in same Telegram image-batch. Global + OPEC+ same time period 2022-2026 yearly overlays. 2026 line (yellow) is the visible step-down from baseline historical bands; data through May 2026.
---

# Kpler Crude Exports 2026 SHARP STEP-DOWN — Global −14% Jan→May (~42K → ~36K kbbls/d) / OPEC+ −29% Jan→May (~25K → ~17.8K kbbls/d); OPEC+ Is Dominant Driver of Global Decline

**Event (Kpler crude-flow tracker; paired charts Will-shared 5/21):**

- **Global Crude Exports:** 2026 (yellow) drops from ~**42,000 kbbls/d** January → ~**36,000 kbbls/d** May = **−6,000 kbbls/d (~−14%)** in 4 months. 2024-2025 baseline band held ~41-43K kbbls/d throughout the year. 2022 trough was ~39.5K kbbls/d. The 2026 May print at 36K is **below the 2022-2025 envelope minimum** for that calendar month.
- **OPEC+ Crude Exports:** 2026 (yellow) drops from ~**25,000 kbbls/d** January → ~**17,800 kbbls/d** May = **−7,200 kbbls/d (~−29%)** in 4 months. 2024-2025 baseline band held ~25-26K kbbls/d throughout the year. **2026 May print is the lowest in the entire 2022-2026 series.**
- **OPEC+ is the dominant driver of the global decline.** OPEC+ accounts for ~−7.2K kbbls/d of the global ~−6K kbbls/d — implying non-OPEC+ exports are slightly UP YoY, partially offsetting the OPEC+ collapse.

## Substance

- **Single-frame snapshot of the Iran-war supply-squeeze on the export side.** Pairs with SIG-W-20260416-001 (Apr 16 Kpler global oil inventory destocking — the inventory-side view of the same mechanic) + SIG-W-20260505-001 (IEA/S&P/Citi inventory drawdown convergence) + SIG-W-20260521-022 (EIA WPSR −17.8MMbbl SPR −9.9MMbbl with exchange-mechanic overlay) + SIG-W-20260505-002 (LNG 33Mt 2-year-low Qatar driver).
- **Non-OPEC+ partial-offset confirms Russia/Iran/Saudi-driven hit, not generalized supply collapse.** Iran-war kinetic + sanctions-enforcement + Hormuz blockade + Iran-permitted-carve-out throttle = the supply-side mechanic. Pairs with anchor 5/21 (partial-thaw on diplomatic side but blockade enforcement at same pace).
- **Pump-side bifurcation visible** — Brent has -10% from peak at the wholesale side (SIG-005) but pump retail is at peak (SIG-030 all-50-$4); exports collapsing while retail demand is inelastic in Memorial Day weekend window. Inventory and export-side substance accumulating while wholesale paper has begun reversal — classic 4-6 week mechanical lag.
- **Implication for Phase 2 oil-thesis:** confirms BRENT thesis substance accumulation on export-flow channel; OPEC+ -29% in 4 months at flow-level is materially below modeled trajectories for diplomatic-thaw recovery; if August reopening assumption holds (SIG-023 Rapidan base case), reverse trajectory needs to begin in May-June print not later.

## Routing rationale

BRENT ACTION (Phase 2 oil-thesis primary; integrate export-flow channel into Phase 2 trigger framework). HAWK INFO (geopolitical-driver continuity; STALE 32d but routing intact via backup-promotion). SAM INFO (USD/JPY × oil cross). LIQUID INFO (stagflation macro). CARL INFO (consumer-stagflation transmission via pump-pass-through). RED INFO (steelman: chart-snapshot vs continuous monthly tracking — is May reading a single bad month or trend?). NEXUS / PROME standard.

## Falsification scan

No threshold fires. Does NOT auto-trigger BURST_WINDOW OPEN (export-flow data is supportive substance not threshold-cross).
