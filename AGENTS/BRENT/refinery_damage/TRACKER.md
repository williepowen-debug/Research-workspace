# Refinery Damage Tracker

**Owner:** BRENT
**Last Updated:** 2026-04-17 (post-verification integration)
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

### Aggregate bpd offline (as of 2026-04-17, post-verification)
Per `INCIDENTS.tsv` `bpd_offline_est` column, summed by status:

| Status | # incidents | Est. bpd offline |
|---|---|---|
| ACTIVE | 19 | ~4.77M bpd (+ LNG) |
| PARTIAL_RESTART | 1 (Port Arthur) | 415K bpd |
| ATTACKED_INFRA_INTACT | 1 (Kharg Apr 7) | 0 (threat event only) |
| DISPUTED | 1 (MRPL Mangalore) | 100K (India, conflicting reports) |
| MONITORING | 2 (Corpus Christi, Nayara Vadinar) | 0 (latent 870K + 400K) |
| RESOLVED (2026 YTD) | 8 | 0 (closed) |
| **TOTAL ACTIVE + PARTIAL** | **20** | **~5.19M bpd** |

**🔻 Apr 17 verification correction:** RF-019 Kharg Apr 7 reclassified from ACTIVE 1.5M → ATTACKED_INFRA_INTACT 0. Apr 7 US restrikes confirmed (CNN/Bloomberg/Air Force Times) but oil infrastructure was AGAIN spared (Mehr News: "continues to operate as normal"). Aggregate ACTIVE bpd drops from ~6.6M to ~5.1M. Iran export capacity still down via RF-002 (Mar 13 sanctions/campaign) but not via physical damage to Kharg.

*Note: "bpd_offline_est" is a working estimate per incident. Aggregate is not independently verifiable — Kpler estimates "hundreds of millions of barrels off market." Treat as directional.*

### By cluster (ACTIVE + PARTIAL only)

| Cluster | Count | Approx bpd offline |
|---|---|---|
| Middle East war-damage | 9 | ~3.9M (Kharg Mar 13, Satorp, Ruwais, Mina Al-Ahmadi, Habshan, Bazan, Ras Laffan LNG, ADCOP pipeline) |
| Russia (Ukraine drone campaign) | 6 | ~650K (Kirishi, Ufa, Tuapse, Nizhny, Ust-Luga port) |
| US mechanical | 1 PARTIAL + 2 STRUCTURAL | 415K (Port Arthur) + 284K (CA closures) + Corpus Christi monitoring |
| International non-war | 2 | 110K (Geelong + Dos Bocas operational impairment) |
| India supply-driven | 1 DISPUTED + 1 MONITORING | 100K disputed (MRPL) + 400K deferred (Nayara) |

### Highest-impact ACTIVE incidents
| ID | Facility | bpd offline | Why it matters |
|---|---|---|---|
| RF-012 | ADCOP Hormuz-bypass pipeline | 1.5M | Eliminates primary Hormuz bypass route — **CONFIRMED Apr 17, A-2 tier** |
| RF-002 | Kharg Island (Mar 13) | 1.5M | 90% of Iran export capacity — standing offline |
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
| 2026-04-17 (PM) | RF-012, RF-019, +RF-031, +RF-032 | Post-verification integration: RF-012 ADCOP confirmed (B-2→A-2, date 3/31→3/30); RF-019 Kharg Apr 7 reclassified (ACTIVE 1.5M→THREAT_EVENT 0 bpd, oil infra spared per CNN/BBG/Mehr); added RF-031 MRPL Mangalore disputed + RF-032 Nayara Vadinar monitoring. Aggregate ACTIVE drops 6.6M→5.1M. See `data/VERIFY_2026-04-17.md`. |

---

## ⚠️ VERIFICATION QUEUE

**✅ Resolved Apr 17 (see `data/VERIFY_2026-04-17.md`):**
1. ~~RF-012 ADCOP pipeline fire~~ — **CONFIRMED** via bne IntelliNews, Caliber.az, Pravda, EnergyNewsBeat + Clash Report satellite imagery. Upgraded B-2 → A-2. Date corrected Mar 31 → Mar 30.
2. ~~RF-002 vs RF-019 Kharg Island~~ — **RECONCILED**: Apr 7 US restrikes hit 50+ military targets but oil infra again spared (CNN/Bloomberg/Air Force Times/Mehr News). RF-019 reclassified threat_event 0 bpd. Mar 13 Kharg damage (RF-002) stands.

**🟡 Still open:**
3. **Russian refinery aggregate bpd** — Syrskyi claim "15 refineries hit in March" is the source. True aggregate bpd offline likely lower than simple sum (many hits are partial, and Russia keeps processing with damaged units). Need Kpler / OilTanking / Vortexa estimates.
4. **European refinery fires Mar-Apr** — likely real gap. Europe averages 14 refinery fire/leak incidents per year (Argus 2023 baseline). Searches returned only structural-closure narrative, no discrete Mar-Apr incidents — probably because they aren't in English-language headline feeds. Need targeted pull from Argus refinery status monthly reports.
5. **India MRPL (RF-031) Reuters vs company denial** — Reuters/Bloomberg reported Mar 4-5 shutdown; MRPL filed regulatory denial Mar 7. Conflicting reporting — need ground-truth from next operational update or refiner data.
6. **China refinery confirmed absence** — verified Apr 17 that no major Chinese refinery incidents surfaced Mar-Apr 2026 in English wire. Re-sweep monthly; China runs-up on discounted Russian/Iranian crude is the operational story, not incidents.

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
