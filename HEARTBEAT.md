# HEARTBEAT.md

## Periodic Checks (Rotate Through)

1. **Prediction Threshold Check** (weekly) — Read `PROME/PREDICTIONS_MONITOR.md`, alert if IMMINENT predictions have new data
2. **Agent STATUS Scan** (2x weekly) — Skim headers, flag status changes
3. **Calendar Check** (daily AM) — Read `CALENDAR.md`, flag events within 48h
4. **Position Check** (market hours) — Major move in KRE, WAL, TLT, APO, OZK, IWM, HYG → alert

## Credit Monitoring (Daily When Markets Open)

| Indicator | Green | Yellow | Red |
|-----------|-------|--------|-----|
| HY OAS 5d chg | <+25bps | +25-50bps | +75+bps |
| HY OAS level | <300bps | 300-320bps | >320bps (transmission confirmed) |
| VIX Basis | Contango | Flat | Backwardation |
| CBRE price | >-5% | -5 to -15% | <-15% |

## Current Priority

**SCENARIO C ACTIVE.** Execution phase. Jun rolls → Dec on green days. Hamilton framework drives all expiry decisions.

**Next catalysts:**
- Mar 13: Claims + JOLTS — TRIPWIRE
- Mar 14: DHS paycheck miss
- Mar 17-18: FOMC (SEP + dots, Fed trapped)
- Mar 18-19: BOJ — Ueda presser Mar 19
- Mar 20: Kuwait curtailment physical
- Mar 31: Q1 end — WTI close = NOPI

## Daily Check-ins (Weekdays)
LABOR 8:00, CARL 8:15, MARCO 8:30 AM ET

## Skip Conditions
- Late night (11pm-8am ET): Only alert on urgent
- Weekend: Light monitoring only
