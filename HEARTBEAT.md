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

## Current Priority — UPDATED Feb 18

**KEY INSIGHT:** Feb-Mar is SETUP. April-June is EXECUTION.

### IMMEDIATE (Feb 19-21):

**Feb 19 (Wednesday) — DUAL JAPAN CATALYST: ✅ RESOLVED**
- [x] Shunto Electronics: ¥18,000 = "Strong" ✅
- [x] 20Y JGB auction: BTC 3.08 = PASSED (strong demand) ✅
- **RESULT:** Path D did NOT fire — JGB auction showed strength, not stress

**Feb 21 (Friday):**
- [ ] German flash PMI
- **ALERT:** If <48.0 → March US ISM sub-49 near-certain (per HANS)

### NEAR-TERM (Feb-Mar):

**Mar 1 — OPEC+ Meeting:**
- Watch for April restart confirmation
- If confirmed → 140M barrel flush thesis LOCKED IN

**Mar 5 — ACF LIHEAP Briefing:**
- If no hiring announced → operational failure confirmed
- Escalates Winter 26-27 risk

**Late March:**
- Baltic ice breaks → EXIT TNP/TNK tanker longs
- Transition to crude shorts

### APRIL-JUNE (Execution Window):

**April:**
- Bank earnings (KRE catalyst)
- CVX Q1 earnings (CPC miss expected)
- ISM reality check (sub-49 expected)

**April-May:**
- 140M barrel crude flush arrives
- Initiate crude puts if not already positioned

### New Trades to Monitor:

| Trade | Entry | Exit Trigger |
|-------|-------|--------------|
| TNP/STNG longs | Consider now | Ice breaks (late March) |
| CVX short | April | After crude peaks |
| Crude puts | Late March/April | May expiry |

### Falsification (from RED team):
- Exit 50% if: Claims <240K through March AND Wright <300K/month
- Exit 100% if: BTFP 2.0 OR HY OAS <260bps OR Ukraine ceasefire deal
- Exit 100% if: BTFP 2.0 OR HY OAS <260bps OR Japan both fail

**If nothing urgent before Feb 15, reply HEARTBEAT_OK.**

---

## Skip Conditions
- Late night (11pm-8am ET): Only alert on urgent
- Weekend: Light monitoring only
