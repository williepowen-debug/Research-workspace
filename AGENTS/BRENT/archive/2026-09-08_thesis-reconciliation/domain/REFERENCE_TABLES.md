# BRENT — Reference Tables

> **AUDIT 2026-09-08:** spare capacity, deployable bypass ceilings, quotas, breakevens and percentiles are not immutable constants. The March tables are historical baselines, not verified September inputs. Re-source the particular measure before using it; do not compare the March 4.35M OPEC+ figure mechanically with the later EIA effective OPEC series. See [audit A10](../audits/2026-09-08_stale-intel/REPORT.md).


> **⚠️ VINTAGE: March 2026 baseline reference** (stamped 2026-07-21). Structural constants (capacities, quotas, breakevens, spare-capacity adjudication) remain the reference; **dated operational snapshots below (storage runways "Mar 5/6", Jan-2026 production) are [STALE] — do not cite as current.** Live levels → `STATUS.md`; live catalysts → `docket/CATALYSTS.tsv`. Post-March deltas NOT reflected here: Hormuz formal closure 7/11-12, KOC platform hit 7/12 (RF-037), CPC halt 7/18-21 (RF-038), Yanbu bypass now carrying 5→>6 Mbpd [GS 7/20] and itself inside the declared Houthi zone (STATUS 7/21 vector).

## Hormuz Transit Volumes
- ~20M bpd crude + condensate (20% of global supply)
- ~25% of global LNG
- Key exporters: Saudi Arabia, Iraq, UAE, Kuwait, Qatar, Iran

## Gulf Storage Capacity (Estimated)
> ⛔ **The "Runway" and "Status" columns are MARCH-2026 SNAPSHOTS, [STALE], NOT current** — restated in-table 7/31 (audit flag F10) because the column formerly read *"Current Runway"* while carrying Mar-5/6 values, so a reader skimming the table contradicted the file's own header. **Capacity column = structural, still the reference.**

| Country | Capacity (est.) | Runway **[STALE — Mar 2026]** | Status **[STALE — Mar 2026]** |
|---------|----------------|----------------|--------|
| Kuwait | Limited | ~12 days (Mar 6) | 🔴 Curtailing |
| Qatar | Limited | Filling | 🔴 Curtailing |
| UAE | Moderate | ~22 days (Mar 5) | 🟠 Imminent |
| Iraq | Moderate | Weeks | 🟠 Next |
| Saudi Arabia | Large (Ras Tanura, Yanbu pipeline) | Months | 🟡 Buffer |

*Saudi has East-West pipeline (5M bpd capacity) to Red Sea — partial bypass of Hormuz.*

## OPEC+ Spare Capacity — CONFIRMED (Batch 3, Mar 6 2026)
**The 5-6M bpd narrative is a myth. True effective spare = 4.35M bpd. 90% trapped behind Hormuz.**

| Country | Nameplate MSC | Actual Production (Jan 2026) | Effective Spare | Deployable <90 Days | Status |
|---------|-------------|--------------------------|----------------|---------------------|--------|
| Saudi Arabia | 12.11M bpd | 10.28M bpd | **1.84M bpd** | 1.0-1.2M bpd | 🟡 Spare exists but trapped behind Hormuz |
| UAE | 4.28M bpd | 3.60M bpd | **0.67M bpd** | 0.4-0.5M bpd | 🟡 Spare exists; Fujairah drone-struck |
| Kuwait | ~2.8M bpd | 2.50M bpd | **0.30M bpd** | 0.2M bpd | 🔴 Already curtailing |
| Iraq | 5.1M bpd | 4.34M bpd | **0M bpd** | 0 | 🔴 At max; Rumaila shut down |
| Russia | 9.57M quota | ~9.3M bpd | **Negative** (stranded) | 0 | 🔴 Shadow fleet halted, forced shut-ins |
| Kazakhstan | 1.29M quota | 1.31M bpd | Negligible | 0 | 🟠 CPC pipeline constraints |
| **TOTAL OPEC+** | — | — | **~4.35M bpd** | **2.0-2.5M bpd max** | 🔴 90% trapped behind Hormuz |

*Sources: IEA OMR Feb 2026, OPEC secondary sources. Updated Batch 3 Mar 6 2026.*

**Other OPEC+ numbers:**
- Emergency quota increase (Mar 1): 206K bpd for April → <1.4% of 14.5-15M bpd stranded behind Hormuz (symbolic)
- Deferred capacity: ~3.24 mbpd (2.2M + 1.65M voluntary cuts) [CONF] OPEC Feb 2026 JMMC
- Total OPEC production: ~31 mbpd (vs 34+ mbpd pre-cuts) [CONF]

## Hormuz Bypass Infrastructure — CONFIRMED (Batch 3)
| Route | Operator | Design Capacity | Real Operational Ceiling | Current Status (Mar 2026) |
|-------|---------|----------------|------------------------|--------------------------|
| Petroline (East-West) | Saudi Aramco | 5.0M bpd (7.0M bpd NGL burst) | **3.3-3.5M bpd** (Yanbu terminal loading limit + 1.0M bpd domestic refinery consumption) | 🟡 ACTIVE — 2.5M bpd loading rate (tripled from pre-war); ramping |
| ADCOP (Habshan-Fujairah) | ADNOC | 1.5-1.8M bpd | **Intermittent** (~0.3-0.5M bpd) | 🔴 DAMAGED — Fujairah drone-struck Mar 3; tank farm fires; unreliable |
| Kirkuk-Ceyhan (Iraq-Turkey) | SOMO/Turkey | 1.6M bpd (design); 300-400K bpd actual | **0 bpd** | 🔴 SUSPENDED — Kurdistan production fully halted Mar 3; Ceyhan tanks full |
| **Combined Realistic Max** | — | 8.8M bpd nameplate | **~4.0-4.5M bpd** | Net shortfall vs 20M bpd Hormuz normal: **~13-14M bpd** |

*Sources: Saudi Aramco, ADNOC, Argus Media, Kpler, Rudaw Mar 2026.*

## US Production
- Weekly (wk ending Feb 27): **13.696 mbpd** [CONF] EIA Weekly Mar 6
- Official Dec 2025: **13.65 mbpd** (423.3M total bbl) [CONF] EIA PSM
- EIA 2026 forecast: **13.6 mbpd avg**; Q2 projected 13.51 mbpd [CONF] EIA STEO Feb 2026
- SPR: ~350M bbl (historic low post-2022 release)
- Cushing operational minimum: ~20M bbl
- **US Oil Rig Count: 411** (oil-directed) / 551 total [CONF] Baker Hughes Mar 6 2026
- Rig trend: -7% YoY; flat through entire war period
- **DUC inventory: 5,015 wells** (Jan 2026) — down 41% from 8,504 peak (Feb 2019) [CONF] EIA Drilling Productivity Report
- Permian rigs: 240 (43.6% of US total); -65 YoY
- Max 90-day production surge (DUC pathway): ~200-240K bpd
- Capital discipline: Zero majors announced capex increase post-war [CONF] Mar 2026

## Shale Breakevens (Approximate)
| Basin | Breakeven (WTI) |
|-------|----------------|
| Permian (Midland) | $40-50 |
| Permian (Delaware) | $45-55 |
| Eagle Ford | $50-60 |
| Bakken | $55-65 |
| DJ/Niobrara | $50-60 |

*At $88 WTI, all major basins profitable. Capital discipline, not economics, limits response.*

## Crack Spread Data — CONFIRMED (Batch 3, Early March 2026)
| Spread | Current Level | 10-yr Avg | Historical Percentile | Trend |
|--------|-------------|----------|----------------------|-------|
| 3-2-1 Gulf Coast LLS | **$28.91/bbl** | $10.50/bbl | **>95th percentile** | 🔴 Near-record |
| Gulf Coast ULSD (GY) | **$25.83/bbl** | ~$12/bbl | >90th percentile | 🔴 Extreme distillate tightness |
| Gulf Coast Gasoline (GCC) | **$22.36/bbl** | ~$9/bbl | >85th percentile | 🔴 Summer-blend transition tightening |
| Jet Fuel (US Gulf Coast) | **~$92/bbl implied** ($4.13/gal spot) | ~$15/bbl | ALL-TIME territory | 🔴🔴 Crisis level |
| Singapore Jet vs Dubai | **$145.07/bbl** | ~$12/bbl | **ALL-TIME RECORD** | 🔴🔴 Airlines facing existential margin |

*Sources: EIA, CME, Argus Media, S&P Global Mar 2026. Jet crack: implied from $4.13/gal × 42 minus ~$81 WTI.*

## Pump Price Transmission Model (Batch 3)
| Scenario | Brent | Crack | Projected Retail | Timeline | Consumer Impact |
|----------|-------|-------|-----------------|----------|----------------|
| Current baseline | $90 | $28.91 | $3.70/gal | ~20 days (by ~Mar 25) | Tight but below demand destruction |
| Escalation | $95 | $32.00 | **$3.89/gal** | By late March | Approaching demand destruction |
| Full breach | $95+ | $32+ | **$4.00+/gal** | April 2026 | **DEMAND DESTRUCTION THRESHOLD** |

*$4.00/gal = hard psychological barrier. Consumer trip consolidation, discretionary travel cuts, retail spending diverted.*

## Key Spreads to Monitor
| Spread | What It Shows |
|--------|--------------|
| Brent-WTI | Global vs US pricing (>$5 = US decoupled) |
| Brent M1-M6 | Backwardation depth (>$5 = severe squeeze) |
| 3-2-1 Crack | Refinery margin (>$30 = pump surge → CARL) |
| Gasoline crack | Consumer impact |
| Distillate crack | Industrial/trucking impact |
| Jet crack | Airline impact (→ AAL position) |

## Tanker Rate Benchmarks
| Route | Metric | Super-cycle Level |
|-------|--------|-------------------|
| VLCC (ME→Asia) | WS rate | >WS200 |
| Suezmax (WAF→Europe) | WS rate | >WS200 |
| Aframax (Med) | WS rate | >WS250 |
| Clean (gasoline/jet) | $/ton | Varies |

## EIA Weekly Report — What to Watch
1. Crude inventories (Cushing specifically)
2. Gasoline inventories + implied demand
3. Distillate inventories
4. Refinery utilization %
5. US production estimate
6. Imports/exports (shows global flow shifts)

## LNG Price Benchmarks (March 2026)
| Benchmark | Price | Change vs Pre-War | Source | Updated |
|-----------|-------|------------------|--------|---------|
| JKM (Asia LNG spot) | $15.105/MMBtu | +40.8% sustained (+47% peak) | CME/ICE/Platts | Mar 4 2026 |
| TTF (European gas) | ~$16.80/MMBtu (53.385 EUR/MWh) | +24-28% | ICE | Mar 6 2026 |
| Henry Hub (US domestic) | $2.83/MMBtu | Flat (insulated) | CME/AGA | Mar 6 2026 |
| JKM-HH spread | ~$12.28/MMBtu | Massive arbitrage for US LNG exporters | Derived | Mar 6 2026 |

*Qatar force majeure: ~10 Bcf/day removed; ME LNG exports down 70% for March (2.3 Mt vs 8.1 Mt planned).*
*Venture Global: 41% of 2026 output at spot. Cheniere: 5-10% spot via marketing arm.*

## High-Yield Energy Credit (March 2026)
| Metric | Value | Source | Updated |
|--------|-------|--------|---------|
| HY Energy OAS | 300 bps | [CONF] ICE BofA / FRED Mar 5 2026 | Mar 6 |
| Broad HY OAS | 308 bps | [CONF] ICE BofA Mar 5 2026 | Mar 6 |
| Energy vs Broad HY differential | -8 bps (energy TIGHTER) | [CONF] | Mar 6 |
| Pre-war baseline (Q3 2025) | ~280 bps broad HY | [CONF] | Mar 6 |
| Distress threshold | >600 bps | Historical standard | — |
| OXY implied CDS (5-yr) | 50-70 bps (investment grade-like) | [CONF] OXY tender spreads Mar 5 | Mar 6 |
| Historical 2020 peak | 1,087 bps | ICE BofA Mar 23 2020 | — |

*E&P credit is a LAGGING indicator of price reversal. Phase 2 warning emerges in: (1) refiner spreads, (2) EM sovereign CDS, (3) CCC-rated E&P decoupling, (4) RBL drawdowns.*

## Kirishi Refinery (KINEF) — Key Facts
| Parameter | Value |
|-----------|-------|
| Owner | Surgutneftegaz (KINEF / Kirishinefteorgsintez subsidiary) |
| Location | Kirishi, Leningrad Oblast, Russia |
| Capacity | ~360–420K bpd crude processing |
| Key unit | CDU-6: ~160K bpd (~40% of total) |
| Status | **ONLY refinery in Northwestern Russia** — zero redundancy |
| Products | ULSD diesel (primary), fuel oil, naphtha, jet fuel, LPG |
| Export route 1 | Transnefteproduct pipeline → Primorsk port (diesel/ULSD) |
| Export route 2 | Rail → Ust-Luga port (diesel) |
| Prior strike | Oct 2025: CDU-6 struck, ~160K bpd offline 1+ month |
| New strike | Mar 26, 2026: Ukrainian drones. "Sky glowing red." Scope TBD |
| Strategic role | Source of ALL Russian NW refined product exports. Feeds both major Baltic ports. |
