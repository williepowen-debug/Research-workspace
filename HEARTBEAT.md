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

### 5. **DAILY Credit Monitoring** (Added Feb 14 — RED Team Priority)
**Purpose:** Detect bifurcation collapse (real economy stress → financial economy repricing)

**Daily Checks:**
- [ ] **HY OAS 5-day change** (ICE BofA US High Yield Index)
  - 🟢 <+25bps: Normal
  - 🟡 +25-50bps: Mild stress (2-3 session hedge window)
  - 🟠 +50-75bps: Severe (0-1 session to equity impact)
  - 🔴 +75+bps: Crisis (no lead time)
  
- [ ] **VIX Basis** (VIX spot vs VIX1M)
  - 🟢 Contango (spot < futures): Normal
  - 🟡 Flat: Caution
  - 🔴 Backwardation (spot > futures): Stress signal

- [ ] **CBRE Price** (track acceleration)
  - Currently: -12%
  - Watch for: Break below -15% (stress accelerating)
  - Rebound to >-5% (stress reversing — falsification signal)

- [ ] **CLO AAA Spreads** (if available via LIQUID)
  - Watch for widening >20bps in 5 days

**Alert Thresholds:**
- **YELLOW:** HY OAS +25bps in 5 days OR VIX backwardation
- **ORANGE:** HY OAS +50bps in 5 days OR CBRE <-15%
- **RED:** HY OAS +75bps in 5 days (bifurcation collapse in progress)

---

## Current Priority — CRITICAL CATALYST WINDOW (Feb 15-20)

**HEIGHTENED MONITORING:** Multiple triggers converging in 5-day window
**RED TEAM RESULT:** 80% thesis confidence — "positioned IN THE MIDDLE of stress, not ahead of it"

### Feb 15 (Saturday):
- [ ] FSK earnings (BDC, PIK 27%) — Watch dividend coverage <1.0x

### Feb 18 (Tuesday):
- [ ] Dec TIC data (China/Belgium UST holdings)

### Feb 19 (Wednesday) — **DUAL JAPAN CATALYST:**
- [ ] Shunto Electronics wage settlement (watch for ≥3.5% = "Strong")
- [ ] 20Y JGB auction (watch for BTC <2.0x = stress)
- **ALERT:** If BOTH fire (Shunto ≥3.5% AND BTC <2.0x) = Path D trigger

### Feb 20 (Thursday):
- [ ] PSEC earnings (BDC, PIK 35%) — Watch dividend coverage or cut
- **ALERT:** If dividend cut = validates shadow defaults, INCREASE positions

### Mid-Feb (TBD):
- [ ] Wright mortgage data update (Nov→Dec, Dec→Jan current→delinquent flows)
- **ALERT:** If >400K/month sustained = acceleration confirmed
- **ALERT:** If >700K/month = INCREASE positions

**Falsification (from RED team):**
- Exit 50% if: Claims <240K through March AND Wright <300K/month
- Exit 100% if: BTFP 2.0 OR HY OAS <260bps OR Japan both fail

**If nothing urgent before Feb 15, reply HEARTBEAT_OK.**

---

## Skip Conditions
- Late night (11pm-8am ET): Only alert on urgent
- Weekend: Light monitoring only
