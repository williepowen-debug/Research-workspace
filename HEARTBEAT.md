# HEARTBEAT.md

## Periodic Checks (Rotate Through)

### 1. Prediction Threshold Check (Weekly)
- Read `PROME/PREDICTIONS_MONITOR.md`
- Check if any IMMINENT predictions have new data
- If threshold breached, alert Will

### 2. Agent STATUS Scan (2x Weekly)
- Quick read of each agent's STATUS.md header
- Flag any status changes (GREEN→YELLOW, etc.)
- Note: Daily crons handle LABOR/CARL/MARCO

### 3. Calendar Check (Daily AM)
- Read `CALENDAR.md`
- Flag events within 48 hours

### 4. Position Check (When Markets Open)
- If major move in KRE, IWM, HYG, SSB → Alert
- Check if any profit-taking thresholds hit

---

## Current Priority
If nothing urgent, reply HEARTBEAT_OK.

Check calendar for:
- Feb 18: Dec TIC Data (ZHAO/LIQUID)
- Feb 19: 20Y JGB Auction + Shunto Electronics (SAM)

---

## Skip Conditions
- Late night (11pm-8am ET): Only alert on urgent
- Weekend: Light monitoring only
