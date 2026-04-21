# MARCO STATUS
**Last Updated:** 2026-04-20 20:15 ET | **Status:** 🔴 RED (DHS shutdown ~Day 61-64, FL condo inventory BREACHED 9.1mo, produce spike live)

---

## SIGNAL DASHBOARD

| Indicator | Value | Status |
|-----------|-------|--------|
| DHS Shutdown | ~Day 61-64, no resolution. Johnson refusing Senate-passed bill; Thune drafting "skinny" reconciliation for ICE/CBP (target late Apr). Trump Jun 1 deadline. | 🔴 BREACHED |
| TSA Disruption | Callout 6.95-8% nationally (down from 12.35% Mar 27 peak); ATL 24.6%, PHL 21.5% still elevated. 300+ quits confirmed. | 🔴 BREACHED |
| ICE Raids | Expanding: +58% arrests CA Central Valley, rural MN meatpacking, 14 custody deaths in 2026 | 🔴 BREACHED |
| FL Net Domestic Migration | 22,517 (93% collapse); Miami domestic migration now **-2.0%** — worse than pre-COVID NYC (Kolko/Census to Jul 2025) | 🔴 BREACHED |
| Canadian Visitors to US | Feb 2026: 1.5M trips, air -17.6% YoY, land -12.9% (14th consecutive decline) | 🔴 BREACHED |
| NFP Feb 2026 | -92K, UE 4.4% | 🔴 BREACHED |
| Mexico Remittances Feb 2026 | Feb +0.4% YoY ($4.377B); Jan-Feb bimester $9.062B, -0.5% YoY. Improvement from Jan (-1.4%) but cumulative still negative. Full-year 2025: -4.6% YoY ($61.8B) | 🔴 BREACHED |
| Ag Employment | -155K + 2.2M self-deportations | 🔴 BREACHED |
| H-2A Certifications | 415K + Red River Valley delays, interviews not til July | 🔴 BREACHED |
| FL Condo Inventory | **9.1mo Mar 2026** (threshold 9.0 breached; Lee 14.6mo, Miami-Dade ~14.1mo) | 🔴 BREACHED |
| E-Verify | ✅ OPERATIONAL | 🟢 ACTIVE |

**Composite: 10 BREACHED indicators, 1 CONFIRMED disruption**

---

## NEXT SESSION FOCUS (set 2026-04-20)

**Tier 1 — do first:**
1. **Process inbox** — OTTO WA ICE tracking (Apr 2) + PROME DHS deal (Apr 3) signals. ~3 weeks stale. OTTO's WA data likely refines Prediction #26 (construction raid housing delays).
2. **Verify HERMES delivery** of 2026-04-20 outbox signals (CARL Miami migration, REGINALD/CORAL condo breach). Prome/OpenClaw degraded — sweep may not be running. Check `outbox/delivered/`; if empty, flag to Will for manual routing.
3. **DHS reconciliation text watch** — Johnson/Thune targeted "middle-to-end of next week" (~late Apr) for skinny ICE/CBP reconciliation blueprint. If text drops, shutdown narrative shifts materially.

**Tier 2 — important, not urgent:**
4. **Build OFLC H-2A data pull** — NASS replacement. Planting-season window Mar-May still live; every session without it = blind through the peak. Framework scoped in `domain/sources/AG_LABOR_ALT_SOURCES_MAR26.md`.
5. **April data prints due early-mid May:**
   - Banxico Mar 2026 remittances (~May 1) — is Feb's +0.4% rebound structural or one-off?
   - FL Realtors Apr 2026 (~May 17) — did 9.1mo hold or extend?
   - BLS CPI Apr 2026 (~May 14) — Prediction #21 flip condition: fresh F&V MoM <0.2% AND H-2A catching up → downgrade; otherwise hold/upgrade.

**Tier 3 — watch/background:**
6. TSA April numbers when BTS posts (for Prediction #25 follow-through).
7. Canadian summer (May-Aug) booking capacity — structural boycott payoff window.

**Meta-question to raise:** VX-MARCO-SDL-01 (self-deportation) and VX-MARCO-EMG-01 (emigration) vectors awaiting PROME since before March. PROME degraded. Self-complete, or escalate to Will for routing decision?

---

## ACTIVE SITUATIONS

### DHS Shutdown (~Day 61-64, 🔴 CRITICAL — LONGEST EVER, NO RESOLUTION)
- **~2 months in.** Day count ambiguous across sources (Fox Apr 16 = Day 60 → Day 64 today; MARCO prior Day 59 Apr 18 → Day 61). 3rd paycheck missed.
- **Congress returned Apr 13-14 but did NOT advance either bill.**
  - **House (Johnson) refusing** to floor the Senate-passed DHS-ex-ICE/CBP bill. Floor attention diverted to expiring FISA/spy powers.
  - **Senate (Thune) drafting "skinny" reconciliation** for 3-year ICE/CBP funding. Target "middle to end of next week" per Johnson (~late Apr).
  - **Senate GOP losing patience with Johnson** per The Hill/NOTUS. House Freedom Caucus pushing reconciliation over stopgap.
- **New cliff:** Trump set Jun 1 deadline for reconciliation text.
- **TSA:** Callout 6.95-8% nationally (down from 12.35% Mar 27 peak). ATL 24.6%, PHL 21.5% elevated. 300+ quits confirmed (prior 400+ figure not re-verified). Back pay continues per Mar 31 WH memo.
- ICE/CBP funded separately (OBBBA). TSA remains the unprotected pressure point.

### ICE Construction Raids (🔴 CRITICAL — EXPANDING TO RURAL AG/MEATPACKING)
- Rio Grande Valley: 10-15 raids per company. No-warrant raids taking documented + undocumented workers.
- 57 Concrete: **60% residential volume drop** → filed bankruptcy Dec 2025.
- NYC: Fear effects undermining Dept of Buildings safety enforcement.
- 1-in-3 construction workers foreign-born = systemic, not marginal.
- **NEW (Mar 26-30):** ICE arrests **up 58% in CA Central Valley** vs same period last year (Fresno Bee). Workplace raids in *agricultural areas and hardware stores* in Kern County.
- **NEW:** American Prospect long-form on ICE sweeps in rural MN meatpacking/farming towns — labor displacement beyond metro areas.
- **NEW (Apr 2):** KIRO 7/MyNorthwest: ICE farmworker arrests **surging in WA state**. Workers with legal docs detained. UW Center for Human Rights: WA ICE arrests went from <100/mo early 2025 to **400+/mo** by Oct-Nov. 2025 cherry harvest disrupted — packing houses shut down, fruit rotted. Farmers warning same for 2026 harvest (Jun-Aug). Save Family Farms: "workers with papers in order taken to Tacoma detention for weeks."
- **NEW (Mar 30-31):** NBC tracker updated — ICE arrests have *doubled* since Jan 2025, detention at all-time high.
- **NEW:** 14th ICE custody death in 2026 (José Guadalupe Ramos, Adelanto CA, Mar 25). Reuters/Guardian. Political pressure building.
- **Prediction #26 (housing start delays in border states, Q2 2026, 70% conf)** live.

### Ag Labor Data Gap (🔴 PERMANENT — NEW CRITICAL FINDING)
- **NASS Farm Labor Survey CANCELED** (Aug 28, 2025 announcement; last report May 2025).
  - Zero dedicated federal employer-side ag labor surveys now exist.
- **NAWS (DOL) EFFECTIVELY DEFUNCT** — public data only through FY2014; site now challenge-walled.
- **Net effect:** U.S. has no federal surveys measuring ag labor supply, demand, wages, or workforce composition from either employer or worker side.
- **Data gap is permanent** — this is a structural blind spot for the thesis.
- **Replacement framework established** (→ see `domain/sources/AG_LABOR_ALT_SOURCES_MAR26.md`):
  - PRIMARY: OFLC H-2A Disclosure Data (quarterly + near-real-time job orders)
  - PRIMARY: BLS QCEW NAICS 11 (quarterly, 5-month lag)
  - WEEKLY: NASS Crop Progress Reports (harvest delay as labor proxy, Apr-Nov)
  - MONTHLY: State Dept H-2A Visa Issuances (supply vs. demand gap)
  - LAGGING: CPI Fresh Fruits/Vegetables (price pass-through confirmation)

### H-2A / Ag Labor (Planting Season ACTIVE — NEW BOTTLENECK SIGNAL)
- Emergency wage rules effective Jan 1: lower AEWR, easier hiring.
- UFW lawsuit ongoing (Eastern CA). Admin conceded in court: "there aren't enough Americans."
- FL: 200+ blueberry pickers stuck in State Dept processing → crop loss.
- 2.2M self-deportations in 2025 = underlying supply shock. No replacement survey data.
- **NEW (Mar 27):** Red River Valley (MN/ND) potato growers warning H-2A visa delays threaten 2026 planting. South African workers can't get State Dept interview appointments until **July** — months past planting window. Multiple ag trade outlets reporting.
- **NEW:** Diesel surged to **$5.37/gal** (from $3.89 early March). 640-acre farm fuel bill: ~$17K vs ~$12K a month ago. Energy shock compounding labor shortage for ag sector.
- **NEW:** Mexico launched FINABIEN platform to lower remittance fees. US 1% tax on cash remittances (effective Jan 1) driving digital shift — could change remittance flow patterns.

### Canadian Travel (🔴 STRUCTURAL DECLINE)
- **Jan 2026 StatCan data (released Mar 23):** Canadian return trips from US = **2.1M, -22.0% YoY**
  - Auto: -26.3% | Air: -12.8% | 13th consecutive month of YoY decline
  - **First time since 1972** that overseas returns exceeded US automobile returns.
- Decline moderating in % terms (-28% → -22%) but base effect flatters — absolute volume is depressed.
- Canadian airlines cut **450,000 US-bound seats** in Q1 2026. WestJet/Air Canada shifting to Mexico/Europe.
- US→Canada traffic: -0.3% YoY (essentially flat) — asymmetric boycott, not mutual cooling.
- **Structural boycott entrenched.** No reversal signal.

### JOLTS Feb 2026 + Ag Labor Cross-Reference (🔴 NEW — COMPOUNDING SUPPLY SHOCK)
- **JOLTS Feb 2026 (released Apr 1):** Total hires 4.8M, hires rate **3.1%** — COVID-low level.
- **Cross-reference with MARCO ag labor gap:**
  - Ag sector already facing structural supply shock: 2.2M self-deportations + fear effects + H-2A bottleneck.
  - A COVID-low hiring rate economy-wide means: **the labor market has frozen up broadly.** Ag employers cannot backfill depleted workforce even via non-traditional channels.
  - Normal pattern: when undocumented ag labor leaves, some domestic workers fill in at higher wages. At 3.1% hires rate, that substitution mechanism is broken — domestic workers aren't moving into ag either.
  - **Net effect:** The ag labor gap is wider than the raw deportation/self-deportation numbers suggest. Both supply shock AND demand freeze are operating simultaneously.
  - **Revised labor impact estimate:** Ag labor gap WORSE than modeled. Prediction #21 (planting-season raid surge → produce spike, 55% conf) — consider upgrading confidence given dual-shock.
  - → Flag to LABOR: JOLTS hires at COVID-low compounds ag supply shock. Substitution mechanism broken.

### USDA Prospective Plantings 2026 (Released Mar 31 — Ag Labor Implications)
- **Corn:** 95.3M acres (-3% from 2025)
- **Soybeans:** 84.7M acres (+4%) — record high in WI; increases in AR, IA, KS, MS, NE, SD
- **Wheat:** 43.8M acres (-3%, **record low**)
- **Cotton:** 9.64M acres (+4%)
- **Ag labor demand implications:**
  - Corn→soy shift: soybeans are more mechanized at harvest — marginally *less* labor-intensive than corn. Modestly reduces peak harvest labor demand.
  - Cotton +4%: more labor-intensive in Southeast/TX — partially offsets the corn/soy dynamic at harvest.
  - Wheat record low: less wheat harvest labor needed Jun-Jul 2026 (the traveling harvest crews already under pressure).
  - **Bottom line:** Acreage mix changes are modest (±3-4%). The H-2A bottleneck and deportation supply shock swamp any demand-side shift from acreage reallocation. The gap is about supply, not demand.
  - Planting window NOW — H-2A workers not arriving til July (State Dept interview backlog). **Planting gap is live.**

### StatCan Remittances — Clarification
- **No January 2026 remittance data exists.** StatCan BOP is quarterly, not monthly.
- Q4 2025 BOP released Feb 26: current account deficit narrowed to -$0.7B.
- **Next remittance data: Q1 2026 BOP — May 28, 2026.** Remove from pending.
- Canadian TFWP arrivals down ~3,035 vs Jan 2025; hit 2-year low Nov 2025.

### Florida Triple Exposure (UPGRADED — Miami Migration Now Negative)
- Migration 93% collapse (#1→#8). **NEW: Miami domestic migration -2.0% — worse than pre-COVID NYC (Kolko/Census to Jul 2025).** COVID-era population boom explicitly reversing.
- Canadian tourism structural decline (-22%).
- TSA chaos hitting FL airports during spring break peak — shutdown continues through recess.
- Insurance 4.5x national. Condo inventory **9.1mo Mar 2026 (BREACHED threshold)** — Lee 14.6mo, Miami-Dade ~14.1mo.
- **Miami -2.0% is a leading indicator.** Migration turns before prices. This is the housing demand withdrawal signal CARL needs.
- → CARL cross-post required: Miami migration -2.0% = Path C confirmation (housing demand withdrawal, FL dimension).

---

## PREDICTIONS (Active)

| # | Prediction | Timeframe | Conf | Notes |
|---|-----------|-----------|------|-------|
| 26 | ICE construction raids → housing start delays (TX, AZ, FL) | Q2 2026 | 70% | 60% vol drop = leading indicator |
| 25 | TSA disruption → measurable FL airport delays | NOW | **98%** | ↑ 400+ quit, 40%+ callout at hubs |
| 14 | CA produce prices +15% | H2 2026 | 60% | H-2A wage cuts don't fix bottleneck; no survey data to contradict |
| 8 | ~~FL condo inventory >9 months~~ | Q2 2026 | ✅ | **RESOLVED-CORRECT 2026-04-17**: 9.1mo Mar 2026 print (FL Realtors). Breached early before Q2 midpoint. |
| 22 | OIA flips negative | Q2-Q3 2026 | 70% | |
| 24 | All 3 FL airports negative simultaneously | Q3 2026 | 65% | |
| 11 | H-2A certifications >425K | FY 2026 | 75% | ↑ admin pushing volume |
| 21 | Planting-season raid surge → produce spike | Mar-May 2026 | **68%** | ↑ 55→68 (2026-04-20). CPI fresh F&V +4.0% YoY / **+1.0% MoM** Mar (annualizing ~12%, 70bps above headline). NW farm labor not easing; CA blueberry rot. Hormuz fertilizer additive. |

---

## KEY DATES

| Date | Event |
|------|-------|
| **Mar 28** | ✅ 2nd TSA paycheck missed |
| **Mar 31** | ✅ TSA back pay started per WH memo; USDA Planting Intentions released |
| **Apr 1** | ✅ JOLTS Feb 2026: hires 3.1% (COVID-low) |
| **Apr 10** | ✅ BLS CPI Mar 2026: fresh F&V +4.0% YoY, **+1.0% MoM** — produce spike live (Prediction #21 upgrade trigger) |
| **Apr 13** | ✅ Senate returned — no DHS floor vote taken |
| **Apr 14** | ✅ House returned — no DHS floor vote; attention diverted to FISA/spy powers |
| **Apr 17** | ✅ FL Realtors Mar 2026: condo inventory **9.1mo** (BREACHED 9.0; Lee 14.6mo, Miami-Dade ~14.1mo). Prediction #8 RESOLVED-CORRECT. |
| **Apr 1** | ✅ Banxico Feb 2026 remittances: +0.4% YoY ($4.377B); Jan-Feb -0.5% YoY |
| **~May 2026** | Banxico Mar 2026 remittance release |
| **~May 22** | House stopgap expires (if Senate passes it) — next cliff |
| **Mar-May** | Planting season ACTIVE — H-2A bottleneck peak, no NASS data |
| **May 28** | StatCan Q1 2026 BOP (first remittance data for 2026) |

---

## CROSS-AGENT SIGNALS

| Direction | Agent | Signal |
|-----------|-------|--------|
| → LABOR | 🔴 ICE construction raids = supply shock on demand shock. 1-in-3 foreign-born. Permanent ag data gap. **NEW: JOLTS 3.1% hires = substitution mechanism broken — ag labor gap wider than modeled.** |
| → REGINALD/CORAL | 🟠 **NEW 2026-04-20: FL condo inventory BREACHED 9.1mo Mar 2026** (Lee 14.6mo, Miami-Dade ~14.1mo, supply-driven — not demand collapse). Collateral deterioration Q2-Q3. 🔴 Construction raids → housing start delays. FL triple exposure compounding. Small airport closure risk. |
| → CARL | 🔴 **NEW: Miami domestic migration -2.0% (worse than pre-COVID NYC). COVID population boom reversing. Path C confirmation — housing demand withdrawal, FL dimension. Route this signal.** TSA chaos + spring break disruption continues. |
| → NEXUS | 🔴 10 breached/upgraded indicators. Ag labor black box. JOLTS COVID-low hires compounds supply shock. Miami migration reversal = FL housing leading indicator. |

---

## UNRESOLVED / PENDING

| Item | Priority |
|------|----------|
| VX-MARCO-SDL-01 (self-deportation vector) — awaiting PROME | 🔴 |
| VX-MARCO-EMG-01 (emigration vector) — awaiting PROME | 🟡 |
| Thompson Ag Labor Bill | 🟠 |
| H-2A replacement tracking framework — implement OFLC pulls | 🟡 |

---

## ROLE & DATA SOURCES

**Domain:** Population movement disruptions — international visitor flows, workforce displacement, internal migration.

*Full prediction detail → `PREDICTIONS.md`*
*Ag labor alt sources → `domain/sources/AG_LABOR_ALT_SOURCES_MAR26.md`*
*Full check-in history → `domain/sources/STATUS_archive_20260323.md`*
