# WORKFORCE STATUS

> ⚠️ **FROZEN 2026-07-02** — dormant sub-agent, not maintained since Apr 2026. Figures below are as-of Apr-21 and STALE (e.g. deportation supply shock re-marked "2.2M CBO" → ~1.0M realized foreign-born LF, thesis v2.6; enforcement funding now law; construction raids active). Top-level `AGENTS/MARCO/STATUS.md` is canonical — do not cite these rows as current.

**Last Updated:** 2026-04-21 | **Status:** 🔴 RED — Ag labor crisis, construction divergence, deportation supply shock, transmission now quantified

---

## SIGNAL DASHBOARD

| Indicator | Value | Date | Status |
|-----------|-------|------|--------|
| Ag Employment | -155K (Mar-Jul 2025) + 2.2M self-deportations | 2025 | 🔴 BREACHED |
| H-2A Certifications | **398,059 certified FY25** (prior "415K" was positions REQUESTED — corrected Apr 2026 via OFLC pull). FY22→25: 371.6K → 378.5K → 384.9K → 398.3K. Apps received +9.3% YoY, 4.1% backlog. FL #1 at 56,818. Red River Valley interviews til July. | Apr 2026 | 🔴 BREACHED |
| Construction Employment | High-immigrant sectors diverging from native | Jan 2026 | 🔴 ACTIVE |
| Latino Employment | -474K plunge, 5.2% unemployment (vs 4.1% white) | Jan 2026 | 🔴 BREACHED |
| ICE Farmworker Arrests | 400+/mo WA state by Oct-Nov 2025 | 2025 | 🔴 BREACHED |
| JOLTS Hires Rate | 3.1% — COVID-low, substitution mechanism broken | Apr 2026 | 🔴 BREACHED |
| Meatpacking Throughput | Hog +1.3% vs baseline, poultry +3-6% YTD — NO labor disruption yet. Cattle -11.1% is 75yr-low herd cycle, NOT labor. | Apr 2026 | 🟢 CLEAN |
| CPI Fresh F&V | +4.0% YoY / **+1.0% MoM** Mar 2026 (annualizing ~12%, 70bps above headline) | Apr 10 2026 | 🔴 BREACHED |
| American Emigration | IRS Q1 2025 renunciations +102% YoY; Brookings net migration negative first time since ~1935 | 2025 | 🟡 ELEVATED |

**Composite: 7 BREACHED, 1 CLEAN, 1 ELEVATED**

---

## THESIS

Workforce displacement is operating through **three simultaneous channels**:

1. **Supply Shock:** 2.2M self-deportations + ICE raids + H-2A bottlenecks
2. **Demand Freeze:** JOLTS 3.1% hires rate = domestic workers not backfilling
3. **Sector Divergence:** Construction, agriculture, services showing immigrant-native employment splits

**Key insight:** The labor market has frozen up broadly. At 3.1% hires rate, the normal substitution mechanism (undocumented leaves → domestic fills at higher wages) is broken. Both supply shock AND demand freeze operating simultaneously.

**Transmission quantified (Santanna/Xu NBER 1930s Mexican Repatriation study):**
- **8.2pp house value decline per 1% Mexican population drop** in a city
- **13.3pp building permit decline per 1 SD repatriation exposure**
- Historical analogs (1929-33, 1954, 2008-11) compress to **2-5yr transmission window** at current scale
- Substitution mechanism requires labor surplus (Great Depression 25% UE) — at UE 4.4% no reserve exists

**Geographic concentration (Banxico reverse-map 2024→2025):** SDL-01 pain is NOT California. Top decliners: AZ -6.1%, TX -5.8% ($659M abs), MI -5.6%. Next cluster CO/MN/GA/WI/IN/FL -4.7 to -5.4%. CA least impacted (-3.5%) — indigenous-corridor composition-protected. Pain cluster metros: Phoenix/Tucson/Yuma, Houston/DFW/RGV/San Antonio, Twin Cities/Milwaukee/Indianapolis.

**Beef-belt consolidation is SEPARATE from SDL-01.** Tyson/JBS/Cargill plant closures 2024-25 (Garden City KS, Schuyler NE, Greeley CO) are driven by 75yr-low cattle cycle, not labor shortage. 1990-wave immigrant meatpacking workers relocate within US (home equity, US-born kids), don't self-deport. Candidate VX-BEEFBELT-01 as distinct vector. Full analysis: `domain/sources/LABOR/BEEF_BELT_CONSOLIDATION.md`.

---

## ACTIVE PREDICTIONS

| ID | Prediction | Timeframe | Confidence |
|----|-----------|-----------|------------|
| WF-01 | Planting-season raid surge → produce spike | Mar-May 2026 | **68%** (↑ 55→68 after Mar CPI F&V +1.0% MoM print Apr 10; NW farm labor not easing; CA blueberry rot) |
| WF-02 | Construction workforce disruption → housing start delays (TX, AZ, FL) | Q2 2026 | **80%** (↑ 70→80 after Santanna/Xu transmission quantified) |
| WF-03 | Ag labor gap wider than modeled due to substitution failure | Q2 2026 | 75% |
| WF-04 | American emigration acceleration | 2026-2027 | 65% |

---

## CROSS-AGENT SIGNALS

| Direction | Signal |
|-----------|--------|
| → LABOR | JOLTS 3.1% compounds ag supply shock; substitution mechanism broken |
| → CARL | Latino employment collapse → consumer stress pipeline |
| → REGINALD | Construction raids → housing start delays; FL triple exposure compounding |
| → BRENT | Diesel surge $5.37/gal + ag labor gap = farm operating cost spike |

---

## DATA SOURCES

- **Primary:** BLS QCEW, JOLTS, DOL OFLC H-2A (live pull via `tools/h2a_pull.py` Wayback fallback)
- **Secondary:** USDA NASS (Crop Progress), ICE arrest trackers, remittance flows
- **Live monitors:** OFLC H-2A monthly (`tools/h2a_pull.py`), USDA slaughter weekly (`tools/slaughter_pull.py`) — hog z-score as labor proxy, cattle cycle-contaminated
- **Alternative:** School enrollment (MIGRATION sub-agent), Google Trends
- **Research docs:** `domain/sources/LABOR/` (H-2A, slaughter, beef-belt), `domain/sources/SDL/` (historical analogs, Banxico geographic)

---

## KEY DATES

| Date | Event |
|------|-------|
| Mar-May 2026 | Planting season — H-2A bottleneck peak |
| May 14 2026 | BLS CPI Apr — Prediction WF-01 flip condition (fresh F&V MoM <0.2%) |
| May-Aug 2026 | Tyson/JBS/Pilgrim's/Smithfield Q1 earnings — beef-belt consolidation spread test |
| Jun 2026 | Banxico Q1 2026 BOP — first clean post-remittance-tax data, expected pothole |
| Jun-Aug 2026 | WA cherry harvest — labor disruption test |
| Jul 2026 | Red River Valley H-2A workers arrive (if interviews clear) |

---

## WORKBOOK

- `KB.tsv` — 22 workforce knowledge entries
- `PREDICTIONS.tsv` — Active falsifiable predictions
- `outbox/` — Signals to LABOR, CARL, REGINALD, BRENT
