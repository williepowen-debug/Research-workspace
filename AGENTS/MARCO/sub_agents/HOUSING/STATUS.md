# HOUSING STATUS
**Last Updated:** 2026-04-21 | **Status:** 🔴 RED — FL condo BREACHED 9.1mo, Sunbelt housing stress, transmission now quantified

---

## SIGNAL DASHBOARD

| Indicator | Value | Date | Status |
|-----------|-------|------|--------|
| FL Condo Inventory | **9.1mo Mar 2026** (BREACHED 9.0 threshold; Lee 14.6mo, Miami-Dade ~14.1mo). Prediction HSG-01 precursor RESOLVED-CORRECT Apr 17. | Apr 17 2026 | 🔴 BREACHED |
| Florida Insurance Crisis | 4.5x national rates; Citizens exposure $678.8B | Jan 2026 | 🔴 BREACHED |
| Miami Domestic Migration | -2.0% (worse than pre-COVID NYC) — housing demand withdrawal leading indicator | Jul 2025 | 🔴 BREACHED |
| Texas Housing Inventory | Austin +47% YoY, Houston +28% YoY | 2025 | 🔴 BREACHED |
| California Housing | Coastal resilience, inland stress | 2025 | 🟡 ACTIVE |
| Arizona/Nevada Housing | Snowbird decline impact; Canadian travel -22% sustained | 2025-26 | 🟡 ELEVATED |
| Construction Labor | 1-in-3 foreign-born, ICE raid impact; 57 Concrete 60% volume drop → bankrupt Dec 2025 | 2026 | 🔴 BREACHED |

**Composite: 5 BREACHED, 2 ACTIVE/ELEVATED**

---

## THESIS

Sunbelt housing faces **triple pressure**:

1. **Demand withdrawal:** Migration collapse (MIGRATION sub-agent) + Canadian tourism decline (TOURISM)
2. **Supply constraints:** Insurance crisis (FL 4.5x national) + construction labor shortages
3. **Inventory buildup:** Austin +47%, Houston +28% = supply/demand imbalance

**Key insight:** The Sunbelt housing boom was driven by migration inflows. With migration reversing, the demand foundation is eroding. Insurance and labor constraints prevent supply adjustment.

**Transmission quantified (Santanna/Xu NBER 1930s Mexican Repatriation study):**
- **8.2pp house value decline per 1% Mexican population drop** in a city
- **13.3pp building permit decline per 1 SD repatriation exposure**
- 2010-20 baseline was a ~10yr transmission window; 2025-26 SDL-01 scale (~11% undocumented workforce reduction) compresses this to **2-5yr**
- Prediction HSG-03 (TX starts decline) timeline now anchored by historical template

**Geographic pain cluster (via Banxico reverse-map of remittance sender flows):**
- **Arizona:** Phoenix, Tucson, Yuma (AZ #1 decliner at -6.1%; compounds AZ URS fiscal stress)
- **Texas:** Houston, DFW, RGV, San Antonio (-5.8%, $659M abs — cleanest structural signal)
- **Midwest meatpacking belt:** Twin Cities, Milwaukee, Indianapolis, Detroit
- **NOT California:** CA least impacted (-3.5%) — indigenous-corridor composition-protected. Existing CA exposure models don't need SDL-01 adjustment.

**FL compounding stack:** 9.1mo condo inventory + Miami migration -2.0% + Citizens $678.8B + Canadian tourism -22% + SDL-01 geographic signal (-4.7 to -5.4%) = quad-exposure. Lee/Miami-Dade carrying 14+mo condo inventory.

---

## ACTIVE PREDICTIONS

| ID | Prediction | Timeframe | Confidence |
|----|-----------|-----------|------------|
| HSG-01 | FL condo prices down >10% from peak | Q2-Q3 2026 | **70%** (↑ 60→70 after condo BREACHED 9.1mo Apr 17 + Lee/Miami-Dade 14+mo) |
| HSG-02 | Austin housing inventory >6 months | Q2 2026 | 70% |
| HSG-03 | Texas housing starts decline >15% YoY | H2 2026 | **75%** (↑ 65→75 after Santanna/Xu permit elasticity confirmed historical template) |

---

## CROSS-AGENT SIGNALS

| Direction | Signal |
|-----------|--------|
| → CARL | Housing demand withdrawal → consumer stress pipeline |
| → REGINALD | FL insurance crisis → regional bank exposure (SSFA) |
| → WORKFORCE | Construction labor shortage → housing supply constraint |
| → MIGRATION | Migration reversal = housing demand destruction |

---

## DATA SOURCES

- **Primary:** Census building permits, Redfin/Zillow inventory data, insurance rate filings, FL Realtors monthly
- **Secondary:** Regional MLS data, construction employment (WORKFORCE)
- **Validation:** CARL consumer credit, REGINALD bank exposure
- **Research docs:** `domain/sources/SDL/SDL_HISTORICAL_ANALOGS.md` (Santanna/Xu transmission template), `domain/sources/SDL/BANXICO_STATE_REVERSE.md` (geographic pain cluster methodology)

---

## KEY DATES

| Date | Event |
|------|-------|
| May 17 2026 | FL Realtors Apr 2026 — did 9.1mo condo hold or extend? |
| Monthly | Redfin/Zillow housing market updates |
| Quarterly | Census building permits, state-level data |
| Q2 2026 | FL hurricane season = insurance stress test |

---

## WORKBOOK

- `KB.tsv` — 4 housing knowledge entries (TX, CA, AZ, NV, FL)
- `PREDICTIONS.tsv` — Active falsifiable predictions
- `outbox/` — Signals to CARL, REGINALD, WORKFORCE, MIGRATION
