# BDC Cash Coverage Tracking — Methodology Reference

**Purpose:** Track monthly cash NII vs dividend coverage for key BDCs. PIK income is excluded because it inflates reported NII but doesn't generate cash to cover dividends.

---

## Key Metric
**Cash Coverage Ratio = Cash NII / Dividend Declared**
- Cash NII = Total NII - PIK Interest Income
- Ratio <1.00x = burning cash reserves or cutting dividends

## Status Thresholds
- 🟢 GREEN: Cash coverage >1.00x (sustainable)
- 🟡 YELLOW: Cash coverage 0.90-1.00x (tight)
- 🟠 ORANGE: Cash coverage 0.75-0.90x (unsustainable, cut likely)
- 🔴 RED: Cash coverage <0.75x OR dividend cut announced

## Target BDCs (7)
Selected for: monthly reporting, high PIK concentration, bank exposure, tradability.

**Canaries (High PIK Risk):** PSEC, FSK
**Quality Benchmarks:** ARCC (largest), BXSL (senior secured)
**Middle Market:** TCPC, MFIC, GSBD

## Data Sources

### Monthly Reporters
| BDC | Report Timing | Source URL |
|-----|--------------|-----------|
| PSEC | ~20th of month | prospectstreet.com/investor-relations/monthly-portfolio-statistics |
| FSK | ~15th of month | fskkcapital.com/investor-relations |
| TCPC | Mid-month | ir.tcgbdc.com/financial-information/monthly-stockholder-reports |
| MFIC | ~20th of month | ir.midcapfinancial.com/financial-information |
| BXSL | ~15th of month | ir.bxsl.com/financial-information/monthly-reports |

### Quarterly Reporters
| BDC | Report Timing | Source URL |
|-----|--------------|-----------|
| ARCC | ~45 days post-quarter | ir.arescapitalcorp.com |
| GSBD | Quarterly | goldmansachsbdc.com/investor-relations |

## Monitoring Protocol

### Weekly (Monday)
1. Scan for new monthly reports from PSEC, FSK, TCPC, MFIC, BXSL
2. If report released, extract: Total NII, PIK interest, Dividend, Cash Coverage Ratio

### Monthly Deep Dive (First Friday)
1. Update BDC_CASH_COVERAGE.tsv
2. Calculate trend: improving or deteriorating?
3. Flag threshold crossings → update STATUS.md

### Immediate Alerts
- Any cash coverage <0.90x for first time
- Any dividend cut announcement → RED immediately
- Any guidance of "reviewing dividend policy"
- PSEC or FSK coverage <0.80x → sector canary

## How to Extract Cash NII

From monthly reports:
1. Find "Interest Income" breakdown → use "Cash Interest Income"
2. Exclude "PIK Interest Income"
3. Include "Fee Income" (usually cash) and cash "Other Income"
4. If only total NII: Cash NII = Total NII - PIK Income

**Example (PSEC):**
```
Total NII: $25M | PIK: $9M (8.6%) | Cash NII: $16M
Monthly Dividend: $18M ($0.06 × 300M shares)
Cash Coverage = $16M / $18M = 0.89x → YELLOW
```

## Transmission to Bank Thesis

**Direct:** Banks provide warehouse lines/NAV loans to BDCs → dividend cuts → NAV falls → covenants tested → bank exposure: $1.2T to NDFIs
**Indirect:** BDCs lend to middle market = early cycle indicator → PIK spike = companies can't pay cash → bank credit losses lag 2-4 quarters
**Canary sequence:** PSEC cuts → FSK follows → ARCC struggles = credit cycle turned, banks next

**Bank vectors:** CFG (fund finance leader), VLY (BDC + CRE), WAL (fund finance + fraud)

---

*Framework created 2026-02-11. Live data → `workbook/BDC_CASH_COVERAGE.tsv`*
