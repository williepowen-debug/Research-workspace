# PREDICTIONS MONITOR
**Updated:** 2026-03-03

Quick-reference for predictions closest to resolution. Check daily.

---

## 🔴 IMMINENT (Gap <10% or <2 weeks)

| ID | Prediction | Current | Target | Gap | ETA | Agent |
|----|------------|---------|--------|-----|-----|-------|
| **CARL-16** | Fannie MF DQ >0.80% | 0.75% | 0.80% | **0.05pp** | Q1 2026 | CARL |
| **CARL-11** | CC 90+ DQ >13.74% (GFC) | 12.70% | 13.74% | **1.04pp** | Q2 2026 | CARL |
| **CARL-12** | Student 90+ DQ >10% | 9.5% | 10.0% | **0.5pp** | Q1 2026 | CARL |
| **CARL-14** | Subprime Auto 60+ >7% | **6.9%** | 7.00% | **0.10pp** | **One print away** | CARL |
| **SAM-7** | Shunto tally ≥3.5% | Electronics ¥18K ✅ | 3.5% | — | Mid-Mar tally | SAM |

---

## 🟡 APPROACHING (Gap 10-25% or 1-3 months)

| ID | Prediction | Current | Target | Gap | ETA | Agent |
|----|------------|---------|--------|-----|-----|-------|
| CARL-2 | Auto subprime DQ >7% | 5.21% | 7.00% | 1.79pp | Q3 2026 | CARL |
| CARL-13 | Dave 28DPD >2.10% | 2.00% | 2.10% | 0.10pp | Q2-Q3 | CARL |
| LABOR-1 | Claims >300K sustained | 227K | 300K | 73K | Q2-Q3 | LABOR |
| RENO-1 | Nevada UR >5.6% | 5.2% | 5.6% | 0.4pp | Q2 2026 | RENO |
| LIQUID-4 | 10Y auction BTC <2.30x | 2.39x | 2.30x | 0.09x | Q2 2026 | LIQUID |

---

## 📅 EVENT-DRIVEN (Specific Date Catalysts)

| Date | Event | Prediction | Agent |
|------|-------|------------|-------|
| **Mid-Mar** | Shunto First Tally | ≥3.5% base-up? | SAM |
| **Mar 17** | FOMC + SEP | Dot plot shift? | HENRY |
| **Apr 16** | OZK Q1 Earnings | CRE provisions spike? | REGINALD |
| **Apr 22** | WAL Q1 Earnings | Hidden CRE disclosed? | REGINALD |
| **Apr 23-24** | BOJ MPM | Rate to 0.75%? | SAM |
| **May 12** | WAL Investor Day | CRE strategy questioned? | REGINALD |

---

## ✅ RECENTLY RESOLVED (Last 30 Days)

| ID | Prediction | Result | Date | Notes |
|----|------------|--------|------|-------|
| OTTO-4 | Bank losses >$1B (auto fraud) | ✅ $1.8B | Feb 14 | Tricolor $591M + First Brands ~$1.2B |
| CARL-1 | CC 90+ >8.36% | ✅ 12.70% | Feb 10 | NY Fed Q4 2025 |
| CARL-3 | FL foreclosures +100% | ✅ +190% | Feb 10 | Q4 2025 data |
| SAM-1 | 30Y JGB BTC >2.10x | ✅ 3.64x | Feb 5 | Strong demand |
| SAM-2 | USD/JPY <160 | ✅ 156.25 | Feb 8 | Post-election |
| SAM-3 | Takaichi <260 seats | ❌ 316 | Feb 8 | Supermajority |
| LABOR-4 | KFRC guides down | ⚠️ Partial | Feb 11 | Beat but confirms stagnation |

**Running Score:** 5.5/7 (79%)

---

## 🔍 THRESHOLD CHECK (Quick Scan)

Run this check weekly or when data releases:

### CARL Thresholds
```
[ ] CC 90+ DQ: ___% (RED >13.74%, currently 12.70%)
[ ] Auto 90+ DQ: ___% (RED >5.27%, currently 5.21%)
[ ] Fannie MF DQ: ___% (RED >0.80%, currently 0.75%)
[ ] Freddie MF DQ: ___% (RED >0.50%, currently 0.48%)
[ ] Dave 28DPD: ___% (YELLOW >2.10%, currently ~2.00%)
```

### LABOR Thresholds
```
[ ] Initial Claims: ___K (YELLOW >230K, ORANGE >250K, RED >300K, currently 227K)
[ ] Continuing Claims: ___M (YELLOW >1.9M, currently 1.862M)
[ ] U-3: ___% (RED >5.0%, currently 4.3%)
```

### LIQUID Thresholds
```
[ ] RRP: $___B (RED <$5B, currently ~$10B)
[ ] SOFR-IORB: ___bps (YELLOW >+5, ORANGE >+15)
[ ] Belgium TIC: $___B (ORANGE >$480B, RED >$500B, currently $481B)
```

### SAM Thresholds
```
[ ] 30Y JGB: ___% (YELLOW >3.6%, ORANGE >3.8%, RED >4.0%, currently 3.57%)
[ ] USD/JPY: ___ (Intervention >160, currently ~152)
[ ] Shunto base-up: ___% (Strong ≥3.5%, TBD)
```

### ZHAO Thresholds
```
[ ] Belgium TIC: $___B (ORANGE >$480B, RED >$500B, currently $481B) — PROXY THESIS VALIDATED
[ ] China Official: $___B (ORANGE <$700B, RED <$650B, currently $682.6B) — Near ORANGE
[ ] Belgium YoY Growth: ___% (ORANGE >25%, RED >35%, currently 33%)
[ ] USD/CNY: ___ (YELLOW >7.30, ORANGE >7.40, currently 7.25)
[ ] True Holdings (Adjusted): ~$1.85T — STABLE since 2015 (Setser/CFR)
```

---

## 📊 CALIBRATION STATS

| Metric | Value |
|--------|-------|
| Total Resolved | 6 |
| Correct | 4 |
| Partial | 1 |
| Wrong | 1 |
| **Accuracy** | **75%** |
| Avg Confidence (Correct) | 70% |
| Avg Confidence (Wrong) | 55% |

**Insight:** Higher confidence predictions performing well. Low-confidence calls (55%) are coin flips.

---

## WORKFLOW

### When Data Releases
1. Check threshold list above
2. If threshold breached → Update agent STATUS.md
3. If prediction resolves → Move to RESOLVED in PREDICTIONS.md
4. If close to breach → Flag as IMMINENT here

### Weekly Review (Suggested: Sunday)
1. Run threshold check
2. Update IMMINENT/APPROACHING lists
3. Check calibration stats
4. Flag any predictions that should be revised

### Monthly
1. Review all PENDING predictions for staleness
2. Archive predictions with expired timeframes
3. Update confidence estimates based on new information

---

*This is the quick-reference. Full predictions in PREDICTIONS.md.*
