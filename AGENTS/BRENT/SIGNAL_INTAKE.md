# BRENT — Signal Intake Spec

**Owner:** BRENT | **Consumer:** WALTER (routing) | **Last Updated:** 2026-04-09
**Domain:** Oil & energy markets — crude supply/demand, price structure, storage, tankers, energy credit, two-phase oil thesis

*Living document. BRENT updates when thesis evolves, thresholds change, or new vectors emerge. WALTER reads at routing time.*

---

## PRIORITY LEVELS

| Priority | Meaning | Delivery |
|----------|---------|----------|
| 🔴 | Thesis-level, time-sensitive. Could change position or probability. | Immediately |
| 🟠 | Important context. Informs analysis but not urgent. | Same day |
| 🟡 | Background. Useful but low urgency. | Batch weekly |

---

## 🔴 IMMEDIATE

### Hormuz / Chokepoint
- Strait of Hormuz status changes (open/closed/contested/coordinated passage)
- Mine clearance operations — initiation, progress, completion
- P&I club announcements — coverage resumption or withdrawal for Gulf transit
- US naval escort orders (DoD formal)
- Any vessel transit through Hormuz (first ships = major signal)
- Iran blocking or permitting passage — conditions, coordination requirements

### Ceasefire / Escalation
- US-Iran ceasefire status: holding, violated, collapsed, extended, or upgraded to permanent deal
- Negotiations in Islamabad (or elsewhere) — outcomes, breakdowns, walk-outs
- New military strikes on oil infrastructure: Kharg, South Pars, Yanbu, ADCOP, Ras Tanura, Abqaiq
- Trump statements on Iran attack timeline or ultimatums
- Iran statements on Hormuz reopening conditions

### Facility Damage / Outages
- Gulf oil facility attacks or damage (any producer: Saudi, UAE, Kuwait, Iraq, Iran)
- ADCOP pipeline status changes (utilization, fire, repair)
- Yanbu / Petroline status (under attack, capacity changes)
- Major refinery outages globally (>200K bpd)
- US refinery explosions, fires, or unplanned shutdowns

### Price Dislocations
- Brent or WTI intraday move >5%
- Dated Brent (physical) premium/discount shift >$5 in a session
- WTI-Brent spread inversion widening or normalizing
- Contango/backwardation structure flip

### OPEC+ Emergency
- Emergency OPEC+ meeting called
- Unilateral production changes by Saudi, UAE, or Russia
- Spare capacity deployment announcements

### SPR / Policy Intervention
- US or IEA coordinated SPR release announcements
- Export ban discussions (US crude export ban)

---

## 🟠 SAME DAY

### Scheduled Data Releases
- **EIA Weekly Petroleum Status Report** (every Wednesday) — crude stocks, gasoline stocks, distillate stocks, refinery utilization, production estimates
- **Baker Hughes Rig Count** (every Friday) — total US, oil-directed, Permian-specific
- API weekly crude inventory (Tuesday evening)
- CFTC Commitments of Traders — crude oil managed money positioning (Friday)
- Monthly: EIA Short-Term Energy Outlook, OPEC Monthly Oil Market Report, IEA Oil Market Report

### Tanker / Shipping
- VLCC, Suezmax, Aframax freight rate moves (daily if >10% WoW)
- War risk premium changes for Gulf/Red Sea transit
- Floating storage changes (>5M bbl shift)
- Ship anchoring/queuing data near Hormuz, Fujairah, or key chokepoints

### Refinery / Products
- Crack spread moves: 3-2-1, gasoline crack, distillate crack (flag if gasoline crack >$30/bbl)
- US refinery utilization (weekly via EIA)
- Turnaround season updates (spring/fall)
- Product yield shifts or operational changes at major complexes

### Storage
- Cushing hub inventory (via EIA weekly)
- OECD commercial inventory vs 5-year average
- Gulf producer storage levels (Kuwait, UAE, Iraq) — tank top reports
- Floating storage estimates (Kpler, Vortexa)

### US Production
- EIA production estimates (weekly)
- DUC (drilled but uncompleted) inventory updates (monthly)
- Shale operator earnings/guidance affecting production outlook
- Pipeline capacity additions or constraints (Permian takeaway)

### Gasoline / Consumer
- AAA national average gas price (daily if >$0.10/gal move)
- State-level gas price extremes (California, Florida, Texas)
- Gasoline demand data (EIA weekly implied demand)

### Cross-Agent Signals
- **HAWK:** Military operations near oil infrastructure, escalation tier changes, Hormuz scenario updates (A/B/C/D framework). HAWK owns the geopolitical catalyst — I need it to assess supply impact
- **LIQUID:** Energy HY OAS moves, E&P debt stress, energy-specific credit contagion. I flag energy credit to LIQUID but need their systemic read back
- **HENRY:** VIX spikes >30, inflation prints with energy CPI/PPI components. Energy feeds inflation — I need to know when my inputs are moving the macro needle
- **CARL:** Consumer demand response to gas prices, airline capacity cuts, diesel-intensive sector stress. I provide gas prices — CARL tells me when demand destruction is visible
- **SAM:** Japan energy import costs, LNG demand shifts, refiner run cuts in Asia. Japan imports 90% ME oil — my supply disruption is SAM's demand shock
- **MARCO:** Trade policy / tariff changes affecting energy flows, sanctions on oil-producing nations

---

## 🟡 WEEKLY BATCH

- Russia production/export data (seaborne crude, refinery throughput, Baltic/Pacific loadings)
- Ukraine strikes on Russian energy infrastructure (unless >500K bpd impact, then 🟠)
- Global refinery utilization trends
- LNG spot prices: JKM, TTF, Henry Hub (unless >10% move, then 🟠)
- Qatar force majeure updates (unless status change, then 🔴)
- OPEC+ compliance data (monthly survey)
- Shale breakeven analysis updates
- Rating agency actions on energy companies
- E&P capex guidance changes
- Petrochemical feedstock / NGL pricing
- Global oil demand forecasts (IEA, EIA, OPEC — monthly)
- Canada / Brazil / Guyana production updates
- Oil-focused ETF flows (XLE, OIH, USO)
- Energy M&A activity

---

## KEYWORD PATTERNS

WALTER can pattern-match on these terms to flag potential BRENT signals:

**High confidence (almost always relevant):**
Brent, WTI, crude oil, Hormuz, OPEC, OPEC+, Kharg, Yanbu, ADCOP, Fujairah, EIA weekly, petroleum, refinery, tanker, VLCC, oil price, barrel, bpd, SPR, Strategic Petroleum Reserve, dated Brent, crack spread, backwardation, contango

**Medium confidence (relevant in context):**
Baker Hughes, rig count, Cushing, gasoline, distillate, heating oil, jet fuel, pipeline, Petroline, shale, Permian, DUC, floating storage, war risk premium, P&I, energy credit, HY energy, E&P debt, LNG, JKM, Henry Hub, TTF, oil sanctions, crude stocks

**Low confidence (only if oil/energy-specific):**
production, storage, demand destruction, supply, inventory, refining, capacity, Iran + oil, Saudi + oil, STNG, Scorpio, Frontline, Euronav, XLE, USO, energy sector

---

## WHAT NOT TO SEND

- **Military operations / geopolitical escalation without oil angle** — send to HAWK, not me. I only need military signals when they affect oil infrastructure, chokepoints, or production
- **Broad credit spreads** (IG, HY ex-energy) — send to LIQUID. I only track energy-specific credit
- **Inflation prints** (CPI, PCE, PPI headline) — send to HENRY. I only need the energy subcomponents flagged back to me
- **Consumer spending / sentiment** — send to CARL. I provide gas prices; CARL owns the downstream consumer impact
- **Japan macro** (BOJ, yen, carry trade) — send to SAM. I only flag Japan energy import costs
- **China macro / demand** — send to ZHAO. Unless it's Chinese crude import data or teapot refinery runs
- **Metals / mining** (gold, copper, iron ore) — not my domain
- **Natural gas (US domestic)** — only relevant if Henry Hub crosses $5 or connects to LNG export dynamics
- **Crypto / digital assets** — never relevant
- **US equity earnings** (unless E&P or refiner with production/capacity guidance)
- **Generic "markets up/down"** without energy-specific angle
- **Tariff policy** (general) — send to MARCO. Only relevant if tariffs directly affect energy trade flows or crude imports

---

## ACTIVE THRESHOLDS

*These are the specific levels BRENT is watching right now. Update as they change.*

| Metric | Level | Direction | Why It Matters |
|--------|-------|-----------|----------------|
| Brent | $100 | Above | Psychological level. Currently at $99 — straddling. Ceasefire fragility gauge |
| Brent | $90 | Below | Ceasefire holding + Hormuz reopening = thesis de-escalation |
| Brent | $75 | Below | **Thesis break** — squeeze failed. Exit energy longs |
| Brent | $120 | Above | Ceasefire collapsed. Demand destruction accelerates. Phase 2 approaches |
| WTI-Brent spread | $5+ | WTI premium | US decoupling from global. Bullish US production signal |
| WTI-Brent spread | Normalizes | Brent > WTI | Inversion resolving = global supply improving |
| Cushing | <20M bbl | Below | Operational minimum. WTI dislocation risk |
| Gasoline crack | >$30/bbl | Above | Pump price surge. Alert CARL immediately |
| Gas (AAA avg) | $4.50 | Above | Demand destruction threshold. Currently $4.12 |
| Gas (AAA avg) | <$3.80 | Below | Pressure easing. War premium fading |
| VLCC rate | >WS200 | Above | Tanker super-cycle territory |
| HY energy OAS | >400bps | Above | Energy credit stress emerging. Alert LIQUID |
| US rig count | +50 from trough | Above | Shale response. Bearish medium-term supply signal |
| XLE | $65 | Above | Position in the money. Monitor for exit/roll |
| XLE | $50 | Below | Position deep OTM. Reassess thesis |
| Hormuz traffic | Any resumption | At | **Phase 2 exit trigger.** First ships through = clock starts on normalization |
| P&I coverage | Reinstated | At | **Phase 2 exit trigger.** Insurance = shipping can resume at scale |

---

*Last reviewed: 2026-04-09 by BRENT. Next review: when ceasefire status changes, Hormuz reopens, or major threshold breaches.*
