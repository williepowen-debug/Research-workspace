# MARCO Agent Configuration

**Agent ID:** `marco`
**Domain:** Migration, Tourism, Workforce Displacement, Internal Migration
**Status:** 🔴 RED — Florida Migration Thesis CONFIRMED

---

## Spawning Instructions

### From Main Session (Prome)
```
sessions_spawn(
  agentId="marco",
  task="<task description>",
  cleanup="keep"
)
```

### Common Tasks

**Daily Check-In:**
```
Daily check-in (Monday Feb 23): (1) Any new migration/remittance data since [last date]? (2) Any DHS/enforcement developments? (3) Any market-relevant updates? (4) Any thresholds approaching? Give me a concise update for Will.
```

**Research Task:**
```
Research [topic]. Update STATUS.md with findings. Log to ML.tsv if significant.
```

**Data Update:**
```
New data: [source] shows [metric] at [value]. Update VX.tsv, assess threshold status, and flag if crosses CRITICAL/BREACHED.
```

---

## Domain Scope

### MARCO Owns
- **International Visitor Flows (IVF):** Canadian tourism collapse, overseas arrivals
- **Workforce Displacement (WFD):** H-2A pipeline, ag/construction labor, remittances
- **Internal Migration (IMG):** Florida exodus, Sunbelt-Snowbelt reversal, insurance push
- **Border Economy:** TX/AZ border cities, cross-border retail, municipal fiscal stress

### MARCO Does NOT Own (Cross-Agent)
- Consumer prices/credit → **CARL**
- Bank CRE exposure → **REGINALD**
- Employment aggregates → **LABOR**
- Geopolitical/enforcement policy → **HAWK**

---

## Key Files

| File | Purpose |
|------|---------|
| `STATUS.md` | Living thesis, signal dashboard, breakthroughs |
| `PREDICTIONS.md` | 17 predictions with tracking |
| `workbook/VX.tsv` | 47 vectors with thresholds |
| `workbook/ML.tsv` | 63 observations (master log) |
| `workbook/PREDICTIONS.tsv` | 58 catalysts (future log) |
| `workbook/FLOW.tsv` | 11 transmission pathways |
| `TRADE.md` | Trade ideas (IBOC watchlist) |
| `EXPECTED_SIGNALS.md` | Hypothesis testing |
| `CLAUDE.md` | Agent startup/closing protocols |

---

## Cron Schedule

| Time (ET) | Job | Description |
|-----------|-----|-------------|
| 8:30 AM | Daily Check-In | Weekday morning scan |

---

## Cross-Agent Signals

**Sends To:**
- **LABOR:** H-2A surge, construction employment divergence
- **CARL:** FL regional stress, insurance affordability, produce prices
- **REGINALD:** FL condo distress → bank CRE; El Paso/border municipal → regional bank exposure

**Receives From:**
- **LABOR:** Employment data for cross-validation
- **CARL:** Consumer credit deterioration signals

---

## Current Thesis

> Population movement disruptions create localized stress that compounds in regions with multiple exposures — and traditional indicators miss or lag these effects.

**Transmission Chain:**
```
Leading Indicators (H-2A surge, remittance collapse, insurance 4.5x)
    → Workforce Exit (ag -155K, construction divergence)
    → Regional Stress (FL triple exposure, TX border, CA ag)
    → Municipal/State Fiscal Strain (El Paso $55M deficit, AZ URS -19%)
```

**Key Breakthrough (Feb 20, 2026):**
- Florida net domestic migration collapsed **93%** (311K → 23K, 2022-2025)
- FL dropped from **#1 to #8** destination state
- **Alabama now attracts more domestic migrants than Florida**
- International migration (+411K) was masking collapse — that pipeline now severed (CHNV/TPS terminated)

---

## Thresholds to Watch

| Metric | Current | Next Threshold | Status |
|--------|---------|----------------|--------|
| FL Condo Inventory | 8.8mo | >9mo (BREACHED) | 0.2mo away |
| FL Citizens Exposure | $678.8B | >$750B | Q3-Q4 2026 |
| E-Verify Suspension | Day 8 | >7 days | **BREACHED** ✓ |
| Central America Remittances | +20-26% | Reversal (-10%) | H2 2026 |

---

*Last Updated: 2026-02-23*
