# HEARTBEAT.md

## Periodic Checks (Rotate Through)

### 1. Prediction Threshold Check (Weekly)
- Read `PROME/PREDICTIONS_MONITOR.md`
- Flag if any IMMINENT predictions have new data

### 2. Agent STATUS Scan (2x Weekly)
- Quick read of each agent's STATUS.md header
- Flag status changes (GREEN→YELLOW, etc.)
- Daily crons handle LABOR/CARL/MARCO

### 3. Calendar Check (Daily AM)
- Read `CALENDAR.md`, flag events within 48h

### 4. Position Check (When Markets Open)
- Major move in KRE, WAL, IWM, HYG → Alert
- Check profit-taking thresholds in `FORGE/STATUS.md`

### 5. Credit Monitoring (Daily — RED Team Priority)

| Indicator | 🟢 Normal | 🟡 Caution | 🔴 Crisis |
|-----------|-----------|------------|-----------|
| HY OAS 5-day Δ | <+25bps | +25-50bps | +75+bps |
| VIX Basis | Contango | Flat | Backwardation |
| CBRE Price | >-10% | -10 to -15% | <-15% |
| CLO AAA Spreads | Stable | +10-20bps/5d | +20bps/5d |

---

## Upcoming Catalysts

**Mar 1 — OPEC+ Meeting:** April restart confirmation → 140M barrel flush LOCKED IN
**Mar 5 — ACF LIHEAP Briefing:** No hiring = operational failure confirmed
**Late March — Baltic ice breaks:** EXIT tanker longs, transition to crude shorts
**April — Bank earnings:** KRE catalyst. OZK earnings Apr 16. CVX Q1 (CPC miss expected)
**Apr-May — Crude flush:** Initiate puts if not already positioned
**May 12 — WAL Investor Day**

## Falsification
- Exit 50%: Claims <240K through March AND Wright <300K/month
- Exit 100%: BTFP 2.0 OR HY OAS <260bps OR Ukraine ceasefire deal

## Skip Conditions
- Late night (11pm-8am ET): Only alert on urgent
- Weekend: Light monitoring only
