# Refinery Damage Tracker

**Owner:** BRENT
**Last Updated:** 2026-04-17
**Source of truth for structured data:** `INCIDENTS.tsv` (one row per incident, ID = RF-XXX)
**Purpose:** Living ledger of fires, explosions, strikes, and unplanned outages at refineries, export terminals, and major gas-processing facilities globally — Jan 2026 onward.

**Scope:**
- Refineries (crude distillation + secondary units)
- Refined-product export terminals tied to refining
- Gas-processing facilities material to LNG flow
- Crude export terminals where strikes affect refining feedstock

**Out of scope (owned elsewhere):**
- Military operations / kinetic war framework → HAWK (cross-reference only)
- Upstream oil/gas field damage (e.g., South Pars gas field itself, Kharg oilfield) → HAWK
- Planned refinery turnarounds → `research/REFINERY_UTILIZATION_MAR2026.md`

---

## How to use this tracker

**Update workflow:**
1. **New incident:** append a row to `INCIDENTS.tsv` with next ID (RF-031, RF-032…). Always include source tier + URL.
2. **Status change (ACTIVE → RESOLVED / PARTIAL):** edit the row's `status` + `last_verified` columns only.
3. **Narrative changes (thesis impact, patterns):** edit this file — do NOT duplicate structured fields from the TSV.
4. **Pull data for STATUS.md:** reference IDs, not copied values — e.g., "Port Arthur (RF-008) remains at 415K bpd gross impact."

**Status values:**
- `ACTIVE` — currently offline or impaired
- `PARTIAL_RESTART` — partial recovery, key units still down
- `RESOLVED` — capacity restored or incident closed
- `MONITORING` — not yet triggered but material risk (e.g., Corpus Christi water)
- `SUPERSEDED` — later event replaces this one (archive only)

**Source tier:**
- `A-1` — multiple major outlets, named sources
- `A-2` — one major outlet or own analysis from verified data
- `B-2` — single-source (X, Telegram, etc.) pending verification
- `C-3` — rumor / speculation (avoid unless urgent)

---

## 📊 DASHBOARD

### Aggregate bpd offline (as of 2026-04-17)
Per `INCIDENTS.tsv` `bpd_offline_est` column, summed by status:

| Status | # incidents | Est. bpd offline |
|---|---|---|
| ACTIVE | 19 | ~6.2M bpd (+ LNG) |
| PARTIAL_RESTART | 1 (Port Arthur) | 415K bpd |
| MONITORING | 1 (Corpus Christi) | 0 (latent 870K) |
| RESOLVED (2026 YTD) | 8 | 0 (closed) |
| **TOTAL ACTIVE + PARTIAL** | **20** | **~6.6M bpd** |

*Note: "bpd_offline_est" is a working estimate per incident. Aggregate is not independently verifiable — Kpler estimates "hundreds of millions of barrels off market." Treat as directional.*

### By cluster (ACTIVE + PARTIAL only)

| Cluster | Count | Approx bpd offline |
|---|---|---|
| Middle East war-damage | 10 | ~5.4M (Kharg, Satorp, Ruwais, Mina Al-Ahmadi, Habshan, Bazan, Ras Laffan LNG, ADCOP pipeline, etc.) |
| Russia (Ukraine drone campaign) | 6 | ~650K (Kirishi, Ufa, Tuapse, Nizhny, Ust-Luga port) |
| US mechanical | 1 PARTIAL + 2 STRUCTURAL | 415K (Port Arthur) + 284K (CA closures) + Corpus Christi monitoring |
| International non-war | 2 | 110K (Geelong + Dos Bocas operational impairment) |

### Highest-impact ACTIVE incidents
| ID | Facility | bpd offline | Why it matters |
|---|---|---|---|
| RF-012 | ADCOP Hormuz-bypass pipeline | 1.5M | Eliminates primary Hormuz bypass route — **single-source B-2, VERIFY** |
| RF-002 / RF-019 | Kharg Island | 1.5M | 90% of Iran export capacity — verify Mar 13 vs Apr 7 |
| RF-008 | Valero Port Arthur | 415K | **US diesel hydrotreater exposure**; single-point failure for ULSD crack |
| RF-015 | Ruwais | 200K | One of world's largest refineries (UAE) |
| RF-018 | Satorp (Jubail) | 230K | Aramco/TotalEnergies JV, 460K capacity — units halted after Apr 7-8 cluster |
| RF-014 | Mina Al-Ahmadi | 200K | Kuwait primary, multi-unit damage Apr 3 |

---

## 🧠 THESIS LAYER

### Why refinery damage matters to the two-phase thesis

**Phase 1 (supply squeeze):** Already priced ~9-11M bpd Gulf crude offline (BRENT STATUS supply table). Incremental refinery damage = **product-side** shock on top of crude shock. Effect: crack spreads (3-2-1 $28.91, ULSD $25.83, jet $92+) are already at 95th+ percentile and damage keeps them stuck there.

**Phase 2 trigger (Hormuz reopens, crude floods):** Global refining capacity can't immediately absorb the returning barrels because damaged units (Port Arthur, Geelong, Satorp, Ruwais, Kuwait, Russian fleet) take weeks-to-months to restore. Expected outcome:
- **Crack spreads stay elevated LONGER than crude price** on Phase-2 unwind
- **Refiner equities (VLO, MPC) may decouple from crude on the way down** — a potential alpha lane
- **Pump prices stay >$4 longer than crude-futures-implied** — CARL/consumer transmission extends
- **Diesel stays tightest** because of Port Arthur single-point + global distillate stocks 3% below 5-yr avg

**Risk that inverts:** if refineries restart faster than expected (insurance claims pay, OEMs supply parts quickly), product-side relief comes faster than modeled. Watch for restart announcements in the 2-6 week horizon.

### Cross-agent implications

| Agent | Signal | Why |
|---|---|---|
| **HENRY** | Sticky PPI energy, CPI gasoline 3-8 wk lag | Crack spread stickiness decouples pump from crude futures |
| **CARL** | Pump >$4 persistence even on crude flush | Product-side shock sustains consumer burden past Phase-2 |
| **HAWK** | Apr 7-8 retaliatory cluster (Haaretz) = policy, not one-off | Iran is systematically striking Gulf energy; scenario framework |
| **SAM** | Japan fuel-import stress from ME refined products, not just crude | Kuwait/UAE/Saudi refiner damage affects refined exports to APAC |
| **LIQUID** | Monitor VLO/MPC/ADNOC/Aramco equity-to-debt transmission | Energy HY OAS still stable but refiners are the Phase-1 beneficiaries; mean reversion on Phase-2 could crack credit |

---

## 🗓 UPDATE LOG

| Date | IDs changed | Note |
|---|---|---|
| 2026-04-17 | RF-001 through RF-030 | Initial tracker build from 6 weeks of fragmented inbox signals + research + Apr 17 web sweep |

---

## ⚠️ VERIFICATION QUEUE (high priority)

1. **RF-012 ADCOP pipeline fire (Mar 31)** — single-source `@silvertrade` on X. Eliminates 1.5M bpd Hormuz bypass if true. Need Bloomberg / Reuters / Argus second source before using in thesis.
2. **RF-002 vs RF-019 Kharg Island** — BRENT STATUS text says "STRUCK Apr 7 — 90% Iran export capacity." Wikipedia 2026 Kharg attack article puts strike on **Mar 13** but notes US deliberately spared oil infra. Are these the same event, sequential events, or is one wrong? Critical for supply-disruption snapshot integrity.
3. **Russian refinery aggregate bpd** — Syrskyi claim "15 refineries hit in March" is the source. True aggregate bpd offline likely lower than simple sum (many hits are partial, and Russia keeps processing with damaged units). Need Kpler / OilTanking / Vortexa estimates.
4. **European refinery fires Mar-Apr** — likely real gap. Europe averages 14 refinery fire/leak incidents per year (Argus 2023 baseline). Searches returned only structural-closure narrative, no discrete Mar-Apr incidents — probably because they aren't in English-language headline feeds. Need targeted pull from Argus refinery status monthly reports.

---

## 📁 FILE STRUCTURE

```
AGENTS/BRENT/refinery_damage/
├── TRACKER.md           # This file — thesis + dashboard + process
├── INCIDENTS.tsv        # Structured source of truth — one row per incident
└── data/                # Source articles, screenshots, detail dumps (empty for now)
```

---

## 🔗 RELATED FILES

- `research/REFINERY_FIRES_SNAPSHOT_2026-04-17.md` — original research artifact that seeded this tracker (retained as dated snapshot)
- `research/REFINERY_UTILIZATION_MAR2026.md` — planned turnaround schedule + crack spread model (Feb-Apr 2026)
- `demand_destruction/TRACKER.md` — template pattern this tracker mirrors
- `../STATUS.md` — Refining bottleneck row in convergence matrix references this tracker
