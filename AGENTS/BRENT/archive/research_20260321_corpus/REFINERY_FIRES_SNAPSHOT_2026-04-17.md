# Refinery Fires & Outages Tracker — Mar–Apr 2026

**Owner:** BRENT
**Created:** 2026-04-17
**Purpose:** Consolidate 6+ weeks of fragmented refinery damage/outage data into one ledger. BRENT had touched individual incidents in inbox signals (Kirishi, ADCOP, Haifa, Corpus Christi) and in `REFINERY_UTILIZATION_MAR2026.md`, but no unified tracker existed. This closes that gap.

**Scope:** Fires, explosions, missile/drone strikes, unplanned mechanical outages. Planned turnarounds excluded (see `REFINERY_UTILIZATION_MAR2026.md` Part 2).

**Source-tag convention:** `[CONF]` = confirmed w/ outlet + date, `[EST]` = estimate or not independently verifiable. Single-source entries flagged.

---

## 1. Middle East — War-damage cluster (Israel–Iran–Gulf)

### Iran (struck)
| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Kharg Island** | NIOC | ~1.5M bpd / 85-95% Iran exports | **Mar 13 (US airstrikes, infra spared)** / **Apr 7 (strike 2, infra hit)** | Bombing raids, Kharg is Iran's primary export terminal | Export capacity severely impaired [CONF] Wikipedia "2026 Kharg Island attack" |
| **South Pars / Asaluyeh** | NIOC / Pars Oil & Gas | ~12% Iran gas production | **Mar 18** | Israeli strike — fires, unit damage | Damaged [CONF] Wikipedia "2026 South Pars field attack" / Al Jazeera |
| **Abadan** | NIOC | ~500K bpd | Not directly hit (as of Apr 12) | — | Iran rebuilding, targets 80% capacity in 2 months [CONF] globalsecurity.org Apr 12 |

### Israel
| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Bazan / Haifa** | Bazan Group | ~197K bpd (Israel's largest) | **Mar 19-20** | Iranian missile salvo, refinery hit | Damaged [CONF] Al Jazeera, JPost Mar 19-20 |

### Saudi Arabia
| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Ras Tanura** | Saudi Aramco | ~550K bpd | **Mar 2** | Iranian drone, minor damage | Halted ops, rerouting. [CONF] Insurance Journal Apr 7 |
| **Samref (Yanbu)** | 50% Exxon / 50% Aramco | ~400K bpd | **Mar 19** | Drone strike | Damaged [CONF] Bloomberg/NPR |
| **Satorp (Jubail)** | 62.5% Aramco / 37.5% TotalEnergies | **460K bpd** | **Apr 7-8** | Units halted after incident | **Units offline** [CONF] Insurance Journal Apr 7 |
| **Riyadh, Kuwait, UAE** (multiple) | Various | — | **Apr 7-8** | Iranian retaliation cluster for attack on Iranian refinery | Multiple fires [CONF] Haaretz Apr 8 |

### Kuwait
| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Mina Al-Ahmadi** | KPC/KNPC | ~466K bpd | **Apr 3** | Drone attack, fire in multiple operational units | Damaged [CONF] PBS NewsHour |
| **Mina Abdullah** | KPC/KNPC | ~454K bpd | **Mar 19** | Attack → fire, extinguished | Restored per latest |
| (Gulf agg) Kuwait | — | ~2.58M bpd total | Cumulative | Tank tops reached, full shutdown per BRENT STATUS Apr 10 supply table | ~2.58M bpd offline |

### UAE
| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Ruwais** | ADNOC | ~837K bpd (one of world's largest) | **Apr 5** | Multiple fires from air-defense-intercept debris | Fires reported [CONF] Insurance Journal |
| **Habshan** gas-processing | ADNOC | UAE's largest gas processor | **Early Apr** | Attack → fire | Suspended [CONF] Insurance Journal |
| **Habshan-Fujairah pipeline (ADCOP)** | ADNOC | **1.5M bpd** (Hormuz bypass) | **Mar 31** | Pumping station fire | Offline — eliminates primary Hormuz bypass [CONF] BRENT SIG-BRENT-20260331 (single-source @silvertrade) — **REFRESH NEEDED** |
| **Fujairah** | Various | 1.6M bpd | Suspended per BRENT Apr 10 supply table | Aggregate Gulf snapshot |

### Qatar
| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Ras Laffan LNG** (incl. Shell GTL) | QatarEnergy, Shell | ~77 MTPA LNG + GTL | **~Mar** | Iranian missiles → fires, "extensive damage" | **Permanent FM declared** per BRENT STATUS — 13M t/yr removed [CONF] Insurance Journal |

**Middle East sub-total:** ~9-11M bpd crude + massive LNG capacity at least partially offline, per BRENT STATUS supply-disruption snapshot. Cluster is the core Phase-1 supply shock.

---

## 2. United States — Mechanical / non-war cluster

| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Port Arthur, TX** | Valero | **380K bpd** | **Mar 23 2026** | Explosion at 47K bpd diesel hydrotreater #243; blast heard 11 miles | **Partial restart Apr 16**, key hydrotreater still offline; 415K bpd gross impact per WoodMac. Repairs = damaged heater tube [CONF] WoodMac, Marine Link, Reuters via BOE Report |
| **Ardmore, OK** | Valero | 91,500 bpd | **Feb 2026** | Fire → plant-wide shutdown | Resolved [CONF] REFINERY_UTILIZATION_MAR2026 |
| **Whiting, IN** | BP | ~440K bpd (largest PADD 2) | **Early Q1 2026** | Unplanned outage | Created severe PADD 2 tightness [CONF] REFINERY_UTILIZATION_MAR2026 |
| **Borger, TX** | Phillips 66 | 140K bpd | Feb 2026 | Mechanical issues, unplanned unit outages | Resolved |
| **Catlettsburg, KY** | Marathon | 255K bpd | Feb 2026 | Brief unexpected shutdowns | Resolved |
| **Galveston Bay, TX** | Marathon | 631K bpd | **Jan 12 2026** | Alky unit fire (residual HC ignition) | Extinguished; pre-war incident |
| **Corpus Christi (metro)** | Multiple (Valero, Citgo, Flint Hills) | ~870K bpd aggregate | **Mar 26** | Water supply crisis — restrictions possible May | Threat, not yet triggered [CONF] CNN Mar 25 (BRENT SIG) |
| **Wilmington, CA (PADD 5)** | Phillips 66 | 139K bpd | Late 2025 → ongoing wind-down | **Permanent closure** | Structural PADD 5 supply loss |
| **Benicia, CA (PADD 5)** | Valero | 145K bpd | **Announced Apr 2026 idle** | **Permanent idle** | Structural PADD 5 supply loss |

**US sub-total active:** ~415K bpd (Port Arthur) still actively constrained + structural PADD 5 losses. Feb/Jan fires resolved. Corpus Christi water = **latent tail-risk**.

**Important read:** Port Arthur is in the **diesel hydrotreater** — directly supports the ULSD crack spread that has already blown out to $25+/bbl. US diesel market is **unusually exposed** to a single-point failure right now.

---

## 3. International (non-war, non-US)

| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Geelong, Australia** | Viva Energy | 120K bpd (~10% AU supply) | **Apr 15-16 2026** | Significant gas leak → multiple explosions → 60m flames, "mogas" section | Fire contained by noon Apr 16. **Gasoline unit damaged**; jet fuel + diesel isolated valves held. AU fuel-supply concerns raised [CONF] Al Jazeera Apr 16, Argus |
| **Dos Bocas (Olmeca), Mexico** | Pemex | 340K bpd target capacity | **Mar 17 (fatal perimeter fire, 5 dead)** / **Apr 9 (coke warehouse fire)** | 4 safety incidents in 23 days; Mar 17 = vehicle spark on oily flood water | Ongoing safety scrutiny; refinery stays below capacity target [CONF] Mexico Business News, InvestingLive, Hydrocarbon Processing, CGTN Apr 10 |

---

## 4. Russia — Ukrainian deep-strike campaign

Ukraine Commander-in-Chief Syrskyi (Apr 15): **76 Russian industrial targets hit in March, including 15 oil refineries.** Campaign is systematic, not episodic.

| Facility | Owner | Capacity | Date | Incident | Status |
|---|---|---|---|---|---|
| **Kirishi (KINEF), Leningrad** | Surgutneftegaz | ~355K bpd (#2 Russia) | **Mar 26** | 20+ drones overnight | Damaged [CONF] Moscow Times |
| **Ufa, Bashkortostan** | Rosneft | 500K+ bpd hub | **Apr 2** | Drone → major fire | Fire [CONF] search results |
| **Ust-Luga (Baltic export)** | Transneft | Up to 40% Russian oil exports | **Mar 30-31 (4th attack in a week)** | Port + facility hit | Baltic export flow degraded [CONF] Al Jazeera Apr 5 |
| **Nizhny Novgorod / Kstovo** | Lukoil | 330K bpd | **Apr 5** | Drone strike | Damaged [CONF] Al Jazeera, Kyiv Independent |
| **Tuapse, Krasnodar (Black Sea)** | Rosneft | Top-10 Russia | **Apr 16** | Drone strike; "volcano" — 1,400 km from border | Burning [CONF] Kyiv Independent, Moscow Times Apr 16 |
| **Primorsk (Baltic)** | Transneft | — | Pre-period (Mar) | Strike (BRENT inbox) | Tracked |

**Russia sub-total (Mar):** 15 refineries hit. Aggregate impact ambiguous because Russia is opaque; estimated **~1M+ bpd offline at peak**; impacts domestic product supply more than crude export (crude still exported, products constrained).

---

## 5. Cross-cutting observations

### Concentration by cause
| Cause | # of major incidents | Aggregate bpd disrupted (est.) |
|---|---|---|
| War/strike (ME Israel-Iran-Gulf) | 10+ | 9-11M bpd [CONF BRENT STATUS] |
| War/strike (Russia, Ukraine campaign) | 15 (per Syrskyi) | ~1M+ [EST] |
| Mechanical/accident (US) | 6 | 415K active (Port Arthur) + structural |
| Mechanical/accident (intl) | 2 (Geelong, Dos Bocas) | 120K AU + Mexico safety |
| **TOTAL** | **~33+ incidents Mar–Apr** | **~11-12M bpd** aggregate peak |

### Does this change the two-phase thesis?
- **Phase 1 (supply squeeze):** Already priced ~9-11M bpd Gulf offline. The incremental refinery hits (Port Arthur 415K, Geelong 120K, Dos Bocas operational, Russian refined-product degradation) add to **product scarcity**, not crude scarcity. This is why **crack spreads >$28** (already in REFINERY_UTILIZATION_MAR2026) make sense.
- **Phase 2 trigger:** Hormuz reopens → crude floods in, but **refining capacity can't immediately absorb** because of damaged units globally. Expected effect: **crack spreads stay elevated longer than crude price** during Phase-2 transition. Products should outperform crude on the way down.
- **Sequencing implication:** A refining bottleneck supports Phase 1 via product prices (gasoline, diesel, jet) even if crude futures flush on announcement. **Refiner equities (VLO, MPC) may decouple from crude on the downside.**

### Single-source risks to verify
- **ADCOP pipeline fire (Mar 31)** — only source was @silvertrade on X. High-consequence, low-verification. **Refresh needed.**
- **Iran Kharg Apr 7 strike** — BRENT STATUS says "STRUCK Apr 7, 90% Iran export capacity." Was this the Apr 7 Gulf retaliation cluster or a separate event? **Refresh needed** — timing vs Mar 13 US infra-spared raid is important.
- **Russian refinery count (15 in March)** — Syrskyi claim; aggregate bpd impact not independently verified.

### Missing data / research forward
- European refinery incidents — search returned only structural-closure narrative, no discrete Mar-Apr fires. **LIKELY REAL GAP** — Europe has 14 fire/leak incidents per year on average (Argus 2023 data); would expect 2-3 in Mar-Apr window.
- Indian/Chinese refinery status — not searched; these buyers of Russian/Iranian crude are running hot on feedstock but incident data is opaque.
- Japanese/Korean refiners — receiving petitions for strategic reserve access (per BRENT FLOW-BRT-19); any mechanical stress? Not captured.

---

## 6. Cross-agent signal implications

| Target | Reason |
|---|---|
| **HAWK** | Apr 7-8 Saudi/Kuwait/UAE strikes were **retaliatory cluster** per Haaretz — confirms Iran is striking Gulf energy as policy, not one-off. Feeds scenario framework. |
| **HENRY** | Refinery damage → crack spread stickiness → sticky **PPI energy** component even if crude futures fall. Gasoline PPI lag vs crude futures = 3-8 weeks given refining bottleneck. |
| **CARL** | Pump price will stay >$4 longer than crude-futures-implied because Port Arthur diesel + Geelong gasoline + global unit damage persist. Consumer burden extends beyond futures re-rating. |
| **SAM** | Japan fuel import reliance on ME refined products now stressed by Kuwait/UAE/Saudi refiner damage — not just crude. |
| **LIQUID** | HY Energy OAS should be watching Valero, Marathon, ADNOC, Aramco equity → debt transmission. None yet visible but monitor. |

---

## 7. Action items

- [ ] Verify **ADCOP Mar 31 fire** — second source (Bloomberg/Reuters/Argus)
- [ ] Clarify **Kharg Apr 7** — one strike or two separate events (Mar 13 + Apr 7)
- [ ] Quantify **Russian offline bpd** — OilTanking, Kpler, Vortexa estimates
- [ ] Check **European refinery incidents** — Argus/Reuters refinery status monthly reports
- [ ] Add to **CONVERGENCE MATRIX** in STATUS.md: refinery vector is already captured via crack spreads, but Port Arthur + Geelong deserve explicit callout as **product-side** Phase-1 reinforcement

---

## 8. Sources

### Middle East
- [2026 Iran War — Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war)
- [2026 Kharg Island attack — Wikipedia](https://en.wikipedia.org/wiki/2026_Kharg_Island_attack)
- [2026 South Pars field attack — Wikipedia](https://en.wikipedia.org/wiki/2026_South_Pars_field_attack)
- [2026 Strait of Hormuz crisis — Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis)
- [Gulf Energy Infrastructure List — Insurance Journal Apr 7](https://www.insurancejournal.com/news/international/2026/04/07/864740.htm)
- [Iran hits Gulf refineries (PBS Apr 3)](https://www.pbs.org/newshour/world/iran-intensifies-attacks-on-gulf-energy-sites-after-israel-struck-its-key-gas-field)
- [2 U.S. planes down, Iran hits Gulf refineries — NPR Apr 3](https://www.npr.org/2026/04/03/g-s1-116314/iran-hits-gulf-refineries-as-trump-warns-u-s-will-attack-iranian-bridges-power-plants)
- [Iran struck Saudi, Kuwait, UAE in retaliation — Haaretz Apr 8](https://www.haaretz.com/middle-east-news/2026-04-08/ty-article/.premium/iran-reportedly-struck-saudi-arabia-kuwait-and-uae-over-attack-on-refinery/0000019d-6d19-dc9a-a9ff-7f9f1c520000)
- [Israel says Haifa oil refinery hit — Al Jazeera Mar 19](https://www.aljazeera.com/news/2026/3/19/israel-says-oil-refinery-hit-in-iranian-missile-attack-no-major-damage)

### US
- [Valero Port Arthur 415k bpd — WoodMac](https://www.woodmac.com/news/opinion/port-arthur-refinery-explosion-removes-415k-bpd-from-market/)
- [Valero Port Arthur partial restart — yournews Apr 16](https://yournews.com/2026/04/16/6803454/valero-begins-partial-restart-of-major-texas-refinery-after-explosion/)
- [Explosion Shuts Valero Port Arthur — Marine Link](https://www.marinelink.com/news/explosion-forces-shutdown-valeros-port-537213)
- [Valero shuts Texas refinery — US News Mar 24](https://www.usnews.com/news/us/articles/2026-03-24/valero-shuts-texas-refinery-after-explosion-rocks-diesel-unit-sources-say)
- [Marathon Galveston Bay fire (Jan 12)](https://www.sahmcapital.com/news/content/marathon-reports-fire-put-out-at-galveston-bay-texas-refinery-2026-01-14)

### Russia
- [Kirishi drone strike — Moscow Times Mar 26](https://www.themoscowtimes.com/2026/03/26/major-oil-refinery-in-leningrad-region-reportedly-damaged-in-ukrainian-drone-strike-a92341)
- [Tuapse "volcano" — Kyiv Independent](https://kyivindependent.com/ukraine-hits-major-russian-oil-refinery-in-krasnodar-krai-media-officials-report/)
- [Ukraine hits Primorsk + Nizhny Novgorod — Al Jazeera Apr 5](https://www.aljazeera.com/news/2026/4/5/drone-attacks-hit-russian-oil-infrastructure-leak-and-fires-reported)
- [Tuapse + Baltic — Moscow Times Apr 5](https://www.themoscowtimes.com/2026/04/05/ukrainian-strike-damages-central-russian-oil-refinery-baltic-port-oil-facility-a92424)
- [Ukraine drone strike major Russian refinery — PBS News](https://www.pbs.org/newshour/world/ukrainian-drone-strike-sparks-fire-at-one-of-russias-top-oil-refineries)

### International
- [Geelong fire — Al Jazeera Apr 16](https://www.aljazeera.com/news/2026/4/16/fire-breaks-out-at-crucial-australian-refinery-raising-fuel-supply-fears)
- [Geelong fire extinguished — Argus](https://www.argusmedia.com/en/news-and-insights/latest-market-news/2814859-australia-s-geelong-refinery-fire-extinguished-update)
- [Dos Bocas 4th incident in 23 days — Mexico Business](https://mexicobusiness.news/oilandgas/news/fire-dos-bocas-fourth-safety-incident-three-weeks)
- [Dos Bocas 2nd fire in a month — Mexico News Daily](https://mexiconewsdaily.com/news/dos-bocas-refinery-pemex-second-fire/)
- [Dos Bocas ramp-up risk — InvestingLive Apr 9](https://investinglive.com/commodities/massive-dos-bocas-fire-adds-refining-risk-mexicos-flagship-refinery-stays-below-capacity-20260409/)

### Context
- [European Refining Crisis — Ifri](https://www.ifri.org/en/editorials/european-refining-crisis-what-stake-europe)
- [Global refinery closure outlook 2035 — WoodMac](https://www.woodmac.com/news/opinion/global-refinery-closure-outlook-2035/)
