# ABS MONITORING — QUICK REFERENCE CARD

**For:** Monthly ABS data collection and analysis  
**Updated:** 2026-02-11

---

## MONTHLY CHECKLIST (15th of Each Month)

### 1. DATA COLLECTION
- [ ] Check EDGAR for new Form 10-D filings (search by trust name)
- [ ] Download raw data from SEC or issuer IR site
- [ ] Save to `domain/sources/ABS/[Trust]_YYYY-MM.xlsx`

### 2. EXTRACTION
- [ ] Extract Payment Rate, DQ rates (30/60/90+), Charge-off, Pool Balance
- [ ] Add to `domain/sources/ABS/ABS_EXTRACTED_BASELINE.tsv`
- [ ] Note any disclosure changes or data quality issues

### 3. ANALYSIS
- [ ] Calculate MoM change vs prior month
- [ ] Calculate 3-month moving average
- [ ] Compare to thresholds (see below)
- [ ] Check for cross-trust divergences

### 4. UPDATE TRACKING
- [ ] Update `VX.tsv` Current_Value and Status for relevant vectors
- [ ] Add `ML.tsv` entry if significant findings
- [ ] Update `STATUS.md` if any status changes (GREEN→YELLOW, etc.)

### 5. ALERT CONDITIONS
- [ ] Payment rate drop >2% MoM across 3+ trusts → ESCALATE
- [ ] 30+ DQ breaches ORANGE on 2+ major trusts → ESCALATE
- [ ] Divergence from NY Fed trend → NOTE FOR ANALYSIS

---

## PRIORITY TRUSTS (Phase 1)

| Trust | CIK | Focus | Priority |
|-------|-----|-------|----------|
| **Discover Card Master Trust I** | 0000894329 | Credit Card | 🔴 CRITICAL |
| **Capital One MAET** | 0000927628 | Credit Card (Mix) | 🔴 CRITICAL |
| **Santander Drive Auto** | 0001567338 | Subprime Auto | 🔴 CRITICAL |

---

## THRESHOLDS (Quick Ref)

### Credit Card
| Metric | 🟢 GREEN | 🟡 YELLOW | 🟠 ORANGE | 🔴 RED |
|--------|---------|----------|----------|---------|
| Payment Rate | >20% | 18-20% | 15-18% | <15% |
| 30+ DQ | <4% | 4-5% | 5-7% | >7% |
| Charge-off | <5% | 5-7% | 7-10% | >10% |

### Subprime Auto
| Metric | 🟢 GREEN | 🟡 YELLOW | 🟠 ORANGE | 🔴 RED |
|--------|---------|----------|----------|---------|
| Payment Rate | >4% | 3.5-4% | 3-3.5% | <3% |
| 30+ DQ | <10% | 10-12% | 12-15% | >15% |
| Charge-off | <8% | 8-10% | 10-12% | >12% |

---

## WHERE TO FIND DATA

### SEC EDGAR (Primary)
1. Go to: https://www.sec.gov/edgar/searchedgar/companysearch.html
2. Search: Trust name or CIK
3. Filter: Form type "10-D"
4. Open: Most recent filing → Exhibit 99.1 or Servicer Certificate

### Issuer IR Sites (Secondary, Often Earlier)
- **Discover:** investor.discover.com → Fixed Income → ABS
- **Capital One:** investors.capitalone.com → Credit Card ABS
- **Santander:** santanderconsumerusa.com/investor-relations

---

## VECTORS TO UPDATE

| Vector ID | Metric | Trust |
|-----------|--------|-------|
| VX-CARL-ABS-01 | Payment Rate | Discover CC |
| VX-CARL-ABS-02 | 30+ DQ | Discover CC |
| VX-CARL-ABS-03 | Charge-off | Discover CC |
| VX-CARL-ABS-05 | Payment Rate | Capital One CC |
| VX-CARL-ABS-06 | 30+ DQ | Capital One CC |
| VX-CARL-ABS-07 | Charge-off | Capital One CC |
| VX-CARL-ABS-08 | Payment Rate | Santander Auto |
| VX-CARL-ABS-09 | 30+ DQ | Santander Auto |
| VX-CARL-ABS-10 | Charge-off | Santander Auto |

---

## ALERT ESCALATION

**Immediate escalation to PROME if:**
- ⚠️ Payment Rate drops >2% MoM across 3+ trusts
- ⚠️ 30+ DQ breaches ORANGE (>5% CC, >12% auto) on 2+ major trusts
- ⚠️ Subprime auto DQ >15% (Santander or Exeter)
- ⚠️ ABS shows stress NOT visible in NY Fed data (divergence signal)

**Routine reporting:**
- 📊 Monthly status update in STATUS.md
- 📝 ML.tsv entry if notable trends
- 📅 FL.tsv check for upcoming catalysts

---

## INTEGRATION CHECKS

### vs LABOR
- [ ] Check LABOR status for UI claims trends
- [ ] FL stress should predict ABS payment rate drops 30-60 days later

### vs NY Fed
- [ ] When NY Fed quarterly report releases, compare to ABS 3-month trend
- [ ] ABS should show stress 30-60 days earlier

### → REGINALD
- [ ] ABS stress predicts bank NCO warnings 60-90 days later
- [ ] Flag to REGINALD if major issuer ABS deteriorates

---

## FILES REFERENCE

- **Framework:** `domain/workbook/ABS_TRACKING_FRAMEWORK.md`
- **Protocol:** `domain/workbook/ABS_BASELINE_PROTOCOL.md`
- **Vectors:** `domain/workbook/VX.tsv`
- **Master Log:** `domain/workbook/ML.tsv`
- **Calendar:** `domain/workbook/FL.tsv`
- **Data:** `domain/sources/ABS/ABS_EXTRACTED_BASELINE.tsv`

---

*Keep this card handy for monthly monitoring cycles.*
