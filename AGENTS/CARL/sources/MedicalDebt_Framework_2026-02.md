# Medical Debt Tracking Framework
**Created:** 2026-02-12
**Status:** Framework + Available Metrics

---

## THE PROBLEM

Medical debt is the **largest category of collections** on credit reports, yet systematically undertracks because:
1. No centralized reporting (unlike CC, auto, student loans)
2. Pre-collections debt invisible ($50-100B)
3. Complex billing chains (provider → parent company → collector)
4. Pricing opacity and billing errors common

---

## AVAILABLE DATA (CFPB/NY Fed)

| Metric | Value | Source | Date |
|--------|-------|--------|------|
| **Medical collections on credit reports** | **$88B** | CFPB | 2022 |
| **Pre-collections medical debt** | **$50-100B** | CFPB estimate | 2022 |
| **Credit reports with medical collections** | **43 million** | CFPB | 2022 |
| **Households with medical debt** | **~20%** | CFPB | 2022 |
| **Share of collections that are medical** | **58%** | CFPB | 2021 |

**Note:** Post-2022, credit bureaus removed medical collections <$500 and <1 year old. This REDUCED visible medical debt but didn't reduce actual debt.

---

## DEMOGRAPHIC CONCENTRATION

| Group | Medical Debt Rate | Index |
|-------|-------------------|-------|
| Black households | 28% | 1.65x |
| Hispanic households | 22% | 1.29x |
| White households | 17% | 1.0x (baseline) |
| Asian households | 10% | 0.59x |

**Geographic:** Higher in Southeast and Southwest (Medicaid non-expansion states)

---

## CROSS-LINKS TO CARL THESIS

### Medical Debt → Consumer Stress Transmission

1. **Medical event = double shock**
   - Direct cost ($5K-$50K+ depending on event)
   - Lost income (patient + caregiver)
   - CARL "Caregiver Multiplier": 50% MORE income lost than patient's contribution

2. **Medical debt → Credit score destruction**
   - Collections tank credit score
   - Reduced access to credit
   - Higher rates on CC/auto
   - Spiral accelerates

3. **60%+ can't cover deductible**
   - Average deductible: $1,735 (individual), $3,467 (family)
   - Any medical event = instant debt creation for majority

---

## PROXY INDICATORS (What We Can Track)

Since direct medical debt data is limited, we track proxies:

| Indicator | Source | Frequency | What It Signals |
|-----------|--------|-----------|-----------------|
| **Hospital bad debt provisions** | Hospital earnings (HCA, THC, UHS) | Quarterly | Uncompensated care trends |
| **Medical bankruptcy filings** | PACER/Court data | Monthly | Severe distress |
| **CFPB medical complaints** | CFPB database | Monthly | Collection pressure |
| **GoFundMe medical campaigns** | GoFundMe API/scrape | Ad hoc | Desperation indicator |
| **Charity care applications** | Hospital reports | Annual | Demand for assistance |
| **Google Trends: "medical debt help"** | Google Trends | Monthly | Search stress signal |

---

## KEY COMPANIES TO MONITOR

### Hospital Systems (Bad Debt Trends)
- **HCA Healthcare (HCA)** — Largest for-profit
- **Tenet Healthcare (THC)** — Urban/suburban
- **Universal Health Services (UHS)** — Behavioral + acute
- **Community Health Systems (CYH)** — Rural focus

### Medical Debt Collectors
- **R1 RCM (RCM)** — Revenue cycle management
- **Ensemble Health Partners** — Private
- **Conifer Health Solutions** — Tenet subsidiary

### Medical Credit Products
- **CareCredit (Synchrony)** — Medical financing
- **Prosper Healthcare Lending** — Elective procedures

---

## VECTORS TO ADD

| Vector ID | Name | Current | Threshold | Source |
|-----------|------|---------|-----------|--------|
| VX-CARL-MED-01 | Medical Collections Volume | $88B | >$100B | CFPB |
| VX-CARL-MED-02 | CFPB Medical Complaints (Monthly) | TBD | +20% YoY | CFPB |
| VX-CARL-MED-03 | Hospital Bad Debt % Revenue | ~3-4% | >5% | HCA/THC earnings |
| VX-CARL-MED-04 | Google Trends "medical debt help" | Baseline TBD | +30% YoY | Google Trends |

---

## TRANSMISSION PATH

```
Medical event (illness, accident, chronic condition)
    ↓
Out-of-pocket costs exceed buffer (60%+ can't cover deductible)
    ↓
Debt creation ($5K-$50K+)
    ↓
Provider → Collections (6-12 months)
    ↓
Credit score destruction
    ↓
CC/Auto rates increase
    ↓
Debt service burden rises
    ↓
Consumer spending pulls back
    ↓
REGINALD → Bank losses
```

---

## LIMITATIONS

1. **No real-time aggregate data** — CFPB data is 2+ years lagged
2. **Credit bureau changes** — Post-2022 removal of small debts obscures trends
3. **Pre-collections invisible** — $50-100B never hits credit reports
4. **Pricing complexity** — Same procedure = wildly different bills

---

## NEXT STEPS

1. Add "medical debt help" to monthly Google Trends check
2. Monitor HCA/THC earnings for bad debt provisions
3. Track CFPB complaint trends quarterly
4. Cross-reference with GIG (medical debt + gig worker = catastrophic)

*Medical debt is the "dark matter" of consumer credit — massive, consequential, but hard to measure directly.*
