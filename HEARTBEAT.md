# HEARTBEAT.md

## Periodic Checks (Rotate Through)

1. **Prediction Threshold Check** (weekly) — Read `PROME/PREDICTIONS_MONITOR.md`, alert if IMMINENT predictions have new data
2. **Agent STATUS Scan** (2x weekly) — Skim headers, flag status changes
3. **Calendar Check** (daily AM) — Read `CALENDAR.md`, flag events within 48h
4. **Position Check** (market hours) — Major move in KRE, WAL, IWM, HYG → alert

## Credit Monitoring (Daily When Markets Open)

| Indicator | Green | Yellow | Red |
|-----------|-------|--------|-----|
| HY OAS 5d chg | <+25bps | +25-50bps | +75+bps |
| VIX Basis | Contango | Flat | Backwardation |
| CBRE price | >-5% | -5 to -15% | <-15% |

## Current Priority

**KEY:** Feb-Mar = SETUP. April-June = EXECUTION.

**Next catalysts:**
- Mar 1: OPEC+ meeting (140M barrel flush confirmation?)
- Mar 6: NFP
- Mar 13-14: BOJ meeting
- Mar 17-18: FOMC (SEP)

## Skip Conditions
- Late night (11pm-8am ET): Only alert on urgent
- Weekend: Light monitoring only
