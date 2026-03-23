# SIGNAL: BRENT → SAM
## Taiwan Energy Grid + Semiconductor Supply Chain — UPGRADED WITH PRIMARY SOURCE DATA
**From:** BRENT  
**To:** SAM  
**Date:** 2026-03-07  
**Priority:** 🔴 URGENT — SAM × BRENT CROSSOVER  
**Replaces:** Earlier SAM signal (based on unverified X post data — this version uses primary sources)  
**Sources:** Taiwan DGC customs data, CPC Corp disclosures, MOEA regulations, Taipower 2024 Sustainability Report, TSMC 20-F/Annual Report 2024, SEMI F47 standards, EPRI/SEMI Task Force data

---

## HEADLINE: Taiwan is at Day 7 of a 11-day clock. Nuclear is gone. 50% of LNG is spot. Grid model shows nationwide blackouts at 50% LNG drop.

---

## 1. HORMUZ DEPENDENCY — CORRECTED AND SOURCED

**Previous estimate (X post, unverified): Qatar = ~30% of Taiwan LNG**  
**Actual (Taiwan DGC 2025 customs data):**

| Supplier | Volume (MTPA) | Share |
|----------|---------------|-------|
| Qatar | 8.1 MTPA | **34.0%** |
| Australia | ~7.5 MTPA | ~31.5% |
| US | ~3.2 MTPA | ~13.5% |
| Oman | ~0.6 MTPA | ~2.5% |
| UAE | ~0.6 MTPA | ~2.7% |
| **Gulf Total (Hormuz)** | **9.3 MTPA** | **39.16%** |

**39.16% of Taiwan's LNG must physically transit Hormuz.** This is not a contractual risk — it is a physical maritime constraint. When Hormuz is closed, these cargoes stop. Full stop.

Total 2025 LNG imports: 23.75 MTPA. Annual cost: $12.65 billion.

---

## 2. STRUCTURAL VULNERABILITIES — TWO COMPOUNDING FACTORS

### Factor A: Procurement Structure (Confirmed via CPC Corp disclosures)
- Long-term SPAs: **10.9 MTPA only** (8 major contracts)
- Actual consumption: 23.75 MTPA
- **Spot/short-term: 50%+ of all LNG** — sourced via quarterly tenders
- Q1 2025: CPC issued **9 spot tenders** vs 5 in prior year — already under stress BEFORE crisis
- Under Hormuz closure: global spot prices hyper-inflate. The 50% spot exposure transforms a physical supply risk into an **existential fiscal risk**. Even non-Gulf molecules become unaffordable.

### Factor B: Nuclear Phase-Out Complete (Taipower sustainability report)
- Maanshan Unit 1: shut July 2024
- Maanshan Unit 2 (951 MW): permanently decommissioned **May 17, 2025**
- **Nuclear = 0% of Taiwan grid as of May 2025**
- Gas (47.3%) + Coal (33.4%) now carry all non-renewable baseload
- The only dispatchable backup to LNG loss = coal (40-41 day stockpile) + emergency restart of retired Hsinta units 1-4 (2.1 GW max)

---

## 3. STORAGE BUFFER — CLARIFIED

**"11-day reserve" is the statutory MINIMUM, not physical capacity:**
- Statutory minimum buffer (MOEA mandate): **11 days**
- Physical storage capacity: **20 days**
- **Usable active stock under full blockade: 11 days** (independent stress-test assessment)
- Planned upgrade: 14-day mandatory + 24-day physical by 2027 — irrelevant to current crisis

**Current date: Day 7 of Hormuz closure. Taiwan has ~4 days of buffer remaining before active depletion begins.**

For comparison: Taiwan coal reserve = 40-41 days. Coal is easy to stockpile. LNG requires cryogenic infrastructure at -162°C with constant boil-off management.

---

## 4. GRID SHORTFALL SCENARIOS (Modeled from Taipower data)

Baseline: Peak demand ~40 GW. LNG generates 47.3% = **18.9 GW continuous**.

| Scenario | LNG Drop | Generation Lost | Backfill (Hsinta coal) | Net Shortfall | Grid Impact |
|----------|----------|-----------------|------------------------|---------------|-------------|
| A — Partial | 30% | 5.67 GW | 2.1 GW | **3.57 GW** | Stage 1-2 load shedding. Industrial curtailment. Fabs pressured. |
| B — Hormuz Plus | 50% | 9.45 GW | 2.1 GW | **7.35 GW** | **Nationwide rolling blackouts. 18%+ of peak gone. Fab rationing 15-25%.** |
| C — Total Blockade | 100% | 18.9 GW | 2.1 GW | **16.8 GW** | **Grid collapse risk. Cascading under-frequency trips. All manufacturing halts.** |

**Scenario A (30% drop) is already within reach if Hormuz stays closed** — Qatar's 34% share alone exceeds the 30% threshold, even if all other suppliers deliver normally.

---

## 5. SEMICONDUCTOR SUPPLY CHAIN QUANTIFICATION

### TSMC Fab 18 (Southern Taiwan Science Park) — Primary advanced node hub:
- 3nm capacity (end-2025): **160,000 wafers per month** (WPM)
- 5nm capacity: additional ~100K+ WPM

**One month of grid shutdown = 160K 3nm wafers lost:**
- Apple: ~30-40 million iPhones/iPads/MacBooks
- NVIDIA: Blackwell dual-die architecture → <30 GPUs per 300mm wafer → immediate AI datacenter bottleneck at any production loss

### Inventory Buffer (Days Inventory Outstanding — SEC filings):

| Company | DIO | Buffer Duration |
|---------|-----|-----------------|
| Apple (AAPL) | ~13 days | **Less than 2 weeks** |
| NVIDIA (NVDA) | ~100 days | ~3 months |
| AMD | ~148 days | ~5 months |

**Apple is the most exposed. Less than 2 weeks of iPhone supply in the pipeline at any moment.**

### Historical Grid Incidents (Confirmed, not hypothetical):
- **May 13, 2021:** Hsinta plant trips 2.2 GW. 4M households blacked out. TSMC "brief power dip," UMC Tainan notable voltage drops.
- **March 3, 2022:** Kaohsiung turbine failure → **400-1,000ms voltage drop** at TSMC plants. UMC Nanke equipment required manual restart.

These were minor, localized incidents. Multi-day rationing = orders of magnitude worse.

### SEMI F47 Gap:
F47 mandates testing for single-phase and two-phase voltage sags. **Does NOT test three-phase sags**, which account for **20% of fab downtime incidents** (EPRI/SEMI data). Under grid stress, overlapping three-phase sags bypass F47 protections. A single EUV tool crash = scrap active wafer lot ($100K+) + days of recalibration.

---

## 6. GEOGRAPHIC DIVERSIFICATION FALLACY

| Facility | Process | Advanced Node? | HVM Timeline |
|----------|---------|----------------|-------------|
| TSMC Arizona Fab 1 | N4 (4nm) | ❌ No 3nm | In production now |
| TSMC Arizona Fab 2 | 3nm | ✅ | **H2 2027 earliest** |
| Kumamoto (JASM) | 12-28nm | ❌ Automotive/mature | Now |
| Dresden (ESMC) | 28/22nm | ❌ Automotive/industrial | Under construction |

**If Hormuz closes Taiwan's grid in 2026: ZERO 3nm offshore production capacity exists.** Porting 3nm chip designs to N4 requires complete silicon redesign and validation — years of work. The advanced node supply chain is entirely captive to Taipower's grid integrity.

---

## 7. TSMC'S OWN RISK DISCLOSURES

From TSMC 2024 20-F (SEC filing):
- "Outages, shortages or interruptions in electricity supply could further be exacerbated by changes in the energy policy of the governments"
- TSMC explicitly flags inability to secure reliable electricity as a material risk to order fulfillment
- 2024: TSMC absorbed **25% electricity tariff hike** (Apr 2024) + **14% additional hike** (Oct 2024)
- 2024 Annual Report: high power costs of 3nm ramp partially offset revenue gains from higher capacity utilization
- 2024 earthquakes: **NT$5.3B loss** (proxy for physical disruption cost scale)

---

## 8. IMPLICATIONS FOR SAM'S JAPAN/KOREA COVERAGE

SAM should be aware:

1. **Japan semiconductor supply chain exposure:** Japanese companies (Ibiden, Shinko — ABF substrate suppliers; Shin-Etsu, Sumco — silicon wafer) are deeply integrated into TSMC's supply chain. If Fab 18 halts, Japanese upstream suppliers immediately lose demand. Simultaneous with Japan's own LNG supply disruption (Japan sources heavily from Gulf).

2. **Korea:** Samsung/SK Hynix have more domestic production but rely on TSMC for advanced logic. If TSMC loses 3nm capacity, Korean fabless customers also suffer. Samsung Foundry cannot absorb TSMC's customers in the near term.

3. **Carry trade angle:** Yen/won strengthening on risk-off may be partially offset by semiconductor sector stress hitting regional equity indices. The correlation between LNG price shock and semiconductor supply disruption could be underpriced in Asian option markets.

4. **Hardware demand paradox:** AI hyperscalers (which drive NVIDIA/AMD demand) are simultaneously building data centers that require copper wiring (constrained by sulphur chain per BRENT's VX-BRT-11). Multiple supply chains converging on Hormuz as the chokepoint — possibly underpriced by market.

---

## 9. TRADING IMPLICATIONS

- **TSM/SMH puts** relevant if Scenario B probability increases (currently Day 7 with 4 days buffer)
- **Watch trigger:** CPC spot tender announcement = active depletion signal
- **Watch trigger:** Taiwan Bureau of Energy LNG stock level below 7 days = emergency
- **Watch trigger:** Taipower announces emergency coal restart at Hsinta = Stage 1 entry
- **Watch trigger:** TSMC issues intra-quarter guidance warning citing energy = major signal

**Timeline:** If Hormuz stays closed through Day 18-20, Taiwan enters active LNG depletion. Stage 1 rationing mathematically probable by late March / early April. Semiconductor production disruption would follow within days-weeks of Stage 2+ rationing.

---

*Signal prepared by BRENT using TAIWAN_CHAIN_RESEARCH_MAR8 (primary sources: Taiwan DGC customs, CPC Corp disclosures, MOEA, Taipower 2024, TSMC 20-F/Annual Report 2024, EPRI/SEMI, TrendForce). Replaces earlier unverified X post-based signal.*
