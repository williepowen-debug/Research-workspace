---
signal_id: SIG-W-20260720-004
dispatched: 2026-07-21T00:05:00Z
origin: WALTER today-sweep (Will-directed, 2026-07-20 ~23:45Z) — Iran/oil news agent (non-Iran item, flagged as Russia/Ukraine theater)
source: WALTER news-sweep agent, 2026-07-20 (WebSearch quota exhausted — WebFetch-only)
source_tag: WALTER-SWEEP
signal_type: catalyst
domain: GEOPOL_ENERGY
cluster: HYDROCARBON_INFRA
event_window: closed
precedence: PRIORITY
to: [OSPREY]
info: [HAWK, BRENT, RED]
confidence: 0.65
verify_verdict: >
  not-spawned; sweep-degraded (WebSearch quota exhausted, WebFetch-only). A discrete executed event (drone hit a tanker at the terminal, loading halted) but single-lineage in the sweep → OSPREY should confirm the terminal, the loading-halt duration, and volume impact against a primary (CPC/Reuters/Kpler) on pickup. Do NOT conflate with the Iran cluster — this is a Russia/Ukraine-theater event.
routing_note: >
  OSPREY (action — Russia/Ukraine war theater, energy-strike campaign + crude-vs-products channel). A drone hit a tanker at the **Caspian Pipeline Consortium (CPC) Black Sea export terminal** on 7/20, **halting loading.** CPC carries mainly Kazakh crude (~1.3-1.5M bpd, a major non-OPEC export route) to the Black Sea — a loading halt is a real (if usually short-lived) supply-side interruption and a continuation of the R/U energy-strike campaign OSPREY tracks. **Explicitly NOT an Iran-cluster event** (the sweep agent flagged it separately to avoid conflation with the Hormuz/Bab-el-Mandeb thread). BRENT info (oil supply — a CPC halt is a real barrels-offline risk, distinct from the Iran risk-premium move; size + duration determine materiality). HAWK info (cross-war synthesis). RED info (adversarial — CPC loading halts have historically been brief; quantify barrels-days lost vs the headline).
---

# CPC (Caspian Pipeline Consortium) Black Sea terminal — drone hits a tanker, loading halted (7/20) — Russia/Ukraine theater

From WALTER's Will-directed today-sweep (2026-07-20). **Source:** WALTER news-sweep agent (⚠️ WebSearch quota exhausted → WebFetch-only, single-lineage in the sweep).

## What happened
- A **drone struck a tanker at the CPC Black Sea export terminal** on 7/20, **halting loading operations.** CPC is the primary export route for Kazakh crude (~1.3-1.5M bpd), a major non-OPEC supply artery.

## Why it matters / read
- **OSPREY owns it** — this is the Russia/Ukraine energy-strike campaign extending to a crude-export chokepoint (the CPC terminal has been hit before in this war). A loading halt is a **real, executed supply-side interruption** — distinct in kind from the Iran cluster's *risk-premium* move (where zero barrels are lost). **The materiality is size × duration**: CPC halts are often short; OSPREY/BRENT size the barrels-days.
- **⚠️ Do NOT conflate with the Iran cluster** — the sweep agent explicitly separated this from the Hormuz/Bab-el-Mandeb thread. Two different theaters, two different owners (OSPREY vs FALCON).
- BRENT info: a genuine CPC supply interruption is additive to (not part of) the Iran risk premium — worth tracking on the physical-barrels side.

**Routing:** OSPREY (action) / HAWK, BRENT, RED (info). Domain GEOPOL_ENERGY (Russia/Ukraine theater). Cluster HYDROCARBON_INFRA. PRIORITY. Confidence 0.65.
