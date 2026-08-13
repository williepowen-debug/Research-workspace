> ⚠️ **FROZEN 2026-07-17 (audit) — Feb-2026 vintage, no live upkeep. BELT is a dormant sub-agent shell; do not cite rows as current.**

# BELT STATUS
**Last Updated:** 2026-02-17 | **Status:** 🟡 MONITORING | **Check-in:** On-demand (no daily cron)

---

## PURPOSE

Geographic diffusion tracker for Sun Belt and stressed states **not covered by dedicated sub-agents**.

**Covered elsewhere:**
- FL → CORAL
- TX → TEX

**BELT tracks:**
- AZ, NV, GA (traditional Sun Belt)
- MD/DC (federal worker / DOGE concentration)
- MS, LA, OK, IN (emerging stress hotspots)

---

## STATE DIFFUSION DASHBOARD

### Mortgage Delinquency (MBA/ICE Q4 2025)

| State | DQ QoQ Δ | DQ YoY Δ | Foreclosure Trend | Key Driver | Status |
|-------|----------|----------|-------------------|------------|--------|
| **MS** | **+109 bps** | TBD | TBD | Baseline poverty | 🔴 #1 nationally |
| **LA** | **+89 bps** | TBD | TBD | Energy sector + poverty | 🔴 #2 nationally |
| **MD** | **+87 bps** | +16.4% YoY | TBD | **DOGE / federal workers** | 🔴 Watch |
| **OK** | **+86 bps** | TBD | TBD | Energy sector | 🟠 |
| **IN** | **+86 bps** | TBD | TBD | Manufacturing belt | 🟠 |
| **AZ** | +29 bps (Q3) | TBD | TBD | Supply overhang | 🟡 |
| **NV** | TBD | TBD | TBD | Gaming / tourism | 🟡 |
| **GA** | TBD | TBD | TBD | Mixed / Atlanta | 🟡 |

**Source:** MBA National Delinquency Survey Q4 2025, ICE Mortgage Technology

### Metro-Level Hotspots (Cotality Sep 2025)

| Metro | State | DQ Change | Notes |
|-------|-------|-----------|-------|
| Odessa | TX | +1.3 pp | Energy corridor — note for TEX |
| San Angelo | TX | +1.0 pp | Energy corridor — note for TEX |
| Cape Coral | FL | Rising | Note for CORAL |
| Lakeland | FL | Rising | Note for CORAL |

---

## MD/DC — FEDERAL WORKER STRESS (Priority Watch)

**Why elevated:**
- +87 bps QoQ mortgage DQ (Q4 2025) — #3 nationally
- +16.4% YoY noncurrent rate (ICE November)
- **DOGE layoffs** hitting DC-area federal workforce
- **DHS shutdown** (Feb 12+): 234K workers unpaid, concentrated in DMV area
- DC office vacancy: **23%** (highest major market)

**Transmission path:**
```
DOGE layoffs → Federal worker income shock → MD mortgage stress
                                          → DC office vacancy ↑
                                          → Regional bank exposure (PNC, Truist)
```

**Cross-agent links:**
- LABOR: Federal layoff tracking
- CREED: DC office stress
- CARL: DHS shutdown consumer impact

---

## REGIONAL BANK EXPOSURE MAPPING

*To be populated — which regional banks have concentrated exposure to BELT states?*

| Bank | MS/LA | MD/DC | AZ/NV | GA | Notes |
|------|-------|-------|-------|-----|-------|
| Regions (RF) | High | Low | Low | Med | MS/LA footprint |
| Truist (TFC) | Med | High | Low | High | DC/GA footprint |
| PNC | Low | High | Low | Low | DC metro |
| Zions (ZION) | Low | Low | High | Low | AZ/NV footprint |
| TBD | | | | | |

---

## INSURANCE CRISIS DIFFUSION

*Track insurance market stress spreading beyond FL*

| State | Homeowner Premium Δ | Availability Crisis | Notes |
|-------|---------------------|---------------------|-------|
| LA | +30%+ (est) | 🟠 Citizens growing | Post-hurricane stress |
| AZ | TBD | 🟡 | Wildfire risk |
| NV | TBD | 🟡 | |
| GA | TBD | 🟡 | Coastal exposure |

---

## DATA SOURCES

- **MBA National Delinquency Survey** — Quarterly (~6 weeks after quarter end)
- **ICE Mortgage Technology First Look** — Monthly (~last week of month)
- **ICE Mortgage Monitor** — Monthly (first week of following month)
- **Cotality/CoreLogic** — Monthly metro-level
- **State insurance commission filings** — Ad hoc

---

## FINDINGS LOG

| ID | Date | Finding | Source | Implication |
|----|------|---------|--------|-------------|
| BELT-001 | 2026-02-17 | MS/LA/MD/OK/IN top 5 QoQ DQ increases Q4 2025 | MBA NDS | Geographic stress NOT concentrated in expected Sun Belt (TX/FL/AZ) |
| BELT-002 | 2026-02-17 | MD +16.4% YoY noncurrent — DOGE connection | ICE Nov 2025 | Federal worker stress materializing in mortgage data |

---

## RESEARCH GAPS

- [ ] NV state-level DQ data (gaming/tourism exposure)
- [ ] GA state-level DQ data (Atlanta metro vs rest of state)
- [ ] Regional bank exposure mapping by state
- [ ] Insurance premium data by state (non-FL)
- [ ] AZ foreclosure trends (supply overhang markets)

---

## CROSS-AGENT LINKS

| Agent | Connection |
|-------|------------|
| CORAL | FL-specific (BELT excludes) |
| TEX | TX-specific (BELT excludes) |
| CREED | CRE stress by geography |
| CARL | Consumer/mortgage stress national |
| LABOR | Federal layoffs (MD/DC link) |

---

*Next update: When new geographic data arrives (ICE Jan 2026, MBA Q1 2026) or stress diffuses to new states*
