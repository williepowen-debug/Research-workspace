# Signal: PSEC PIK Ratio Correction
**Date:** 2026-02-26
**Source:** SEC Filing / PROME audit
**Priority:** HIGH — Data correction

## Finding
Previous BROCK research logged PSEC (Prospect Capital) PIK income ratio at **35%**. This is WRONG.

SEC filing verification shows actual PIK income as percentage of total investment income = **8.6%**.

The 35% figure appears to have been hallucinated or misread from an agent research session. It was never verified against the actual 10-K/10-Q.

## Correction Required
- STATUS.md PSEC PIK entry: Change 35% → 8.6%
- VX.tsv: Correct the PIK ratio vector for PSEC
- LESSONS: Log this as a verification failure

## Implication
PSEC is less stressed on PIK than previously thought. However, PSEC still has other issues (high leverage, non-accruals). PIK correction does NOT make PSEC a buy — it just means one stress metric was overstated.

## Action
INTEGRATE → Correct STATUS.md. Flag as prior research error.
