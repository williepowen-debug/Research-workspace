# ABS Structural Analysis — CNL Trigger Proximity + Trajectory Math
**Date:** 2026-04-16
**Drill-downs:** #2 (CNL trigger proximity) + #3 (trajectory math)
**Source:** EDGAR 424B5 prospectus supplements for each trust

---

## Data Sources

| Trust | Prospectus | Accession | Filed |
|-------|-----------|-----------|-------|
| SDART 2024-1 | 424B5 | 0001193125-24-008591 | 2024-01-16 |
| EART 2024-2 | 424B5 | 0000929638-24-001285 | 2024-03-28 |
| AMCAR 2024-1 | 424B5 | 0001193125-24-146071 | 2024-05-23 |

---

## SDART 2024-1 (Santander — Subprime)

**Capital Structure:**
| Class | Amount | Initial CE | Break-Even CNL |
|-------|--------|------------|----------------|
| A (all) | $942,440,000 | 42.5% | 42.5% |
| B | $174,650,000 | 31.6% | 31.6% |
| C | $129,570,000 | 23.6% | 23.6% |
| D | $210,060,000 | 10.5% | 10.5% |

- Pool at cutoff: $1,610,000,000
- Initial OC: 9.52% (~$153M), Target: 15.20% of current pool + 2.00% of cutoff
- Reserve: 1.00% of cutoff ($16.1M)
- WAC: 18.52%, Loss severity: 55% (45% recovery)
- DQ Trigger: 24.00% (60+ DQ asset representation review)

**Current (Feb 2026, 26mo):** CNL 8.74%, +0.26pp/mo, pool factor 0.379
**Terminal projection:** 17.6% at current pace (15.8-19.3% range)
**Class D cushion:** 1.8pp → ~7 months to breach at current pace

---

## EART 2024-2 (Exeter — Deep Subprime)

**Capital Structure:**
| Class | Amount | Initial CE | Break-Even CNL |
|-------|--------|------------|----------------|
| A (all) | $277,990,000 | 67.7% | 67.7% |
| B | $152,960,000 | 49.9% | 49.9% |
| C | $151,680,000 | 32.2% | 32.2% |
| D | $124,170,000 | 17.8% | 17.8% |
| E | $87,660,000 | 7.6% | 7.6% |

- Pool at cutoff: $859,340,872
- Initial OC: 7.55% (~$65M), Target: max(17.55% of current pool, 1.50% of cutoff)
- Servicing: 3.00%
- DQ Trigger: 40.00% (deep subprime threshold)
- S&P raised ECL: 20.75% for Exeter 2024 vintage

**Current (Feb 2026, 23mo):** CNL 13.06%, +0.52pp/mo (AGGRESSIVE)
**Terminal projection:** 32.3% at current pace (28.5-36.1% range)
**Class E:** ALREADY BREACHED (13.06% > 7.6%)
**Class D cushion:** 4.7pp → ~9 months to breach
**S&P ECL (20.75%):** Breached in ~15 months at current pace

---

## AMCAR 2024-1 (GM Financial/AmeriCredit — Subprime)

**Capital Structure:**
| Class | Amount | Initial CE | Break-Even CNL |
|-------|--------|------------|----------------|
| A (all) | $1,154,820,000 | 31.1% | 31.1% |
| B | $108,920,000 | 24.6% | 24.6% |
| C | $136,560,000 | 16.4% | 16.4% |
| D | $131,540,000 | 8.6% | 8.6% |
| E | $47,760,000 | 5.7% | 5.7% |

- Pool at cutoff: $1,675,919,178
- Initial OC: 5.75% (~$96M), Target: 14.75% of current pool
- Prospectus base-case CNL: 11.00% lifetime
- DQ Trigger rates: 5.30% (mo 1-12), 6.90% (13-24), 7.20% (25-36), 7.60% (37+) — 60+ DQ

**Current (Feb 2026, 22mo):** CNL 5.339%, +0.24pp/mo, pool factor 0.489
**Terminal projection:** 14.5% at current pace (12.6-16.3% range)
**Class E cushion:** 0.4pp → ~2 months to breach
**Prospectus base CNL (11%):** Breached in ~24 months at current pace

---

## Summary Table

| Trust | Current CNL | Monthly Rate | Class E CE | Class D CE | Terminal CNL | Rating Agency ECL |
|-------|-------------|-------------|------------|------------|-------------|-------------------|
| SDART 2024-1 | 8.74% | +0.26pp/mo | N/A (no E) | 10.5% | 17.6% | ~14-16%* |
| EART 2024-2 | 13.06% | +0.52pp/mo | 7.6% BREACHED | 17.8% | 32.3% | 20.75% (S&P) |
| AMCAR 2024-1 | 5.34% | +0.24pp/mo | 5.7% | 8.6% | 14.5% | ~11% (prospectus) |

*Estimated from comparable SDART vintages. SDART 2021-2 was 16.5%.

---

## Key Findings

1. **EART 2024-2 Class E initial CE (7.6%) ALREADY breached** by CNL (13.06%). Losses eating into excess spread/OC that would otherwise protect Class D. S&P ECL of 20.75% breached in ~15 months. Rating action on subordinate tranches imminent.

2. **AMCAR 2024-1 Class E has only 0.4pp cushion** (5.7% vs 5.3% CNL). Breach in ~2 months at current pace. Excess spread is sole protection for junior tranches.

3. **SDART 2024-1 Class D has 1.8pp cushion** (10.5% vs 8.7% CNL). Breach in ~7 months. Terminal CNL 17.6% well above break-even for Class D.

4. **All three trusts on trajectory to exceed rating agency base-case expectations.** This is the setup for downgrades. EART most urgent, AMCAR imminent, SDART by fall 2026.

---

## Important Caveats

- Break-even CNL is based on **initial hard CE only** (subordination + OC + reserve at issuance)
- Actual current CE is higher because excess spread has been building OC for 22-26 months
- However, the cure collapse pattern (DQ down / CNL up) means excess spread is being consumed by losses rather than building OC to target
- Monthly CNL rates are based on Jan→Feb 2026 single-month change; may fluctuate
- These are 2024 vintage pools; different vintages at same issuer will have different structures

## Thesis Implication

ABS subordinate tranches will show stress BEFORE corporate credit markets (HY OAS at 294bps is complacent). This confirms the "structured credit leads, public credit lags" pattern. When rating agencies downgrade EART/AMCAR/SDART subordinate tranches, it creates forced selling by mandate-constrained investors (CLO managers, insurance companies) — a transmission mechanism to broader credit.
