# BUFFER Expected Signals

**Agent:** BUFFER
**Created:** 2026-01-27 (PROME 004)

---

## DEPLETION SIGNALS (Buffer Weakening)

### DS-BUF-001: Fed Cuts Below Neutral
- **Trigger:** Fed funds rate < 3.0% (below estimated neutral)
- **Meaning:** Fed consuming rate-cut ammunition; less room for future response
- **Action:** Update VX-BUF-1.01; alert LIQUID

### DS-BUF-002: SRF Usage Spike
- **Trigger:** SRF usage > $50B sustained
- **Meaning:** Funding stress real but being absorbed; buffer working but depleting
- **Action:** Update VX-BUF-1.03; alert LIQUID, PROME

### DS-BUF-003: FHLB Capacity > 80%
- **Trigger:** FHLB outstanding > $1.2T (approaching $1.5T system capacity)
- **Meaning:** Bank buffer nearing exhaustion; REGINALD dependency becoming systemic
- **Action:** Update VX-BUF-2.02; alert REGINALD, PROME; ESCALATE

### DS-BUF-004: FDIC Fund < 1.0%
- **Trigger:** DIF reserve ratio drops below 1.0%
- **Meaning:** Deposit insurance buffer thinning; confidence risk
- **Action:** Update VX-BUF-2.03; alert REGINALD, PROME

### DS-BUF-005: Aggregate Savings Rate < 2%
- **Trigger:** Personal savings rate falls below 2%
- **Meaning:** Household buffer nearing exhaustion across ALL income levels
- **Action:** Update VX-BUF-4.01; alert CARL, PROME; CRITICAL

### DS-BUF-006: Buyback Halt (S&P 500)
- **Trigger:** Quarterly buybacks decline > 30% YoY
- **Meaning:** Structural bid weakening; corporate cash being conserved
- **Action:** Update VX-BUF-3.08; alert HENRY, PROME

### DS-BUF-007: Forbearance Invoked
- **Trigger:** OCC/FDIC/FHFA announces accounting or timeline flexibility for CRE
- **Meaning:** Regulators acknowledge stress; buffer ACTIVATED (extend-and-pretend extended)
- **Action:** Update VX-BUF-5.02; alert CREED, REGINALD; paradox: confirms stress BUT extends timeline

### DS-BUF-008: GPIF/Japan Forced Selling
- **Trigger:** GPIF reports net sales of foreign equities > $50B/quarter
- **Meaning:** International buffer depleting; SAM thesis transmitting
- **Action:** Update VX-BUF-6.06; alert SAM, HENRY, PROME

---

## CONTAINMENT SIGNALS (Buffer Holding / Strengthening)

### CS-BUF-001: Fed Holds Rates Steady Through Stress
- **Trigger:** Market stress (VIX > 25) but no Fed cut
- **Meaning:** Fed preserving ammunition; containment without tool usage
- **Action:** Positive for runway; stress agents may be overstating severity

### CS-BUF-002: Bank Capital Ratios Stable/Improving
- **Trigger:** Aggregate CET1 > 12.5% for 2+ consecutive quarters
- **Meaning:** Banking system absorbing losses without capital erosion
- **Action:** REGINALD thesis weakened for system-level impact

### CS-BUF-003: Savings Rate Stabilizes or Rises
- **Trigger:** Savings rate > 4% for 3 consecutive months
- **Meaning:** Household buffer rebuilding; consumer stress may be peaking
- **Action:** CARL thesis challenged on transmission timing

### CS-BUF-004: Passive Flows Accelerate
- **Trigger:** Monthly passive inflows > $50B sustained
- **Meaning:** Structural bid strengthening; market can absorb more selling
- **Action:** HENRY crash thesis weakened; MKT buffer runway extending

### CS-BUF-005: Home Prices Continue Rising
- **Trigger:** Case-Shiller YoY > 3% for 6+ months
- **Meaning:** Largest household asset appreciating; equity cushion growing
- **Action:** HH buffer strengthening; CREED residential thesis challenged

### CS-BUF-006: China Stimulus Effective
- **Trigger:** China PMI > 52 sustained; property market stabilizing
- **Meaning:** International demand buffer strengthening; global recession less likely
- **Action:** INT buffer holding; SAM thesis modified (less amplification risk)

---

*BUFFER Expected Signals v1.0 | Created: 2026-01-27*
