# HAWK Automation Scripts Plan

**Status:** Draft | **Last Updated:** 2026-04-20 | **Reference:** SAM/scripts/ pattern

---

## Overview

HAWK requires automation tooling equivalent to SAM's scripts/ directory to monitor:
1. **Geopolitical developments** (war status, ceasefire durability, diplomatic signals)
2. **Oil market data** (Brent prices, infrastructure status, shipping)
3. **Energy infrastructure** (facility damage, repair timelines, restart status)
4. **Sanctions/shadow fleet** (enforcement actions, insurance rates, tanker tracking)
5. **Catalyst countdown** (key dates: ceasefire checkpoints, OPEC meetings, talks)

---

## Proposed Scripts

### 1. `boot.py` — Master Orchestrator

**Purpose:** One-command morning refresh for all HAWK monitoring.

**Behavior:**
- Runs scripts in priority order (thresholds first, then monitors, then countdown)
- Captures exit codes; failures reported but don't stop sequence
- Skips slow scripts if already run today (idempotent)
- Outputs consolidated brief to terminal + writes to `workbook/BOOT_LOG.md`

**Sequence:**
1. `thresholds.py` — Brent levels, scenario triggers
2. `war_monitor.py` — Daily war developments, scenario probability changes
3. `oil_infrastructure.py` — Facility status check
4. `sanctions_tracker.py` — Shadow fleet, enforcement updates
5. `catalyst_countdown.py` — Days to key dates

**Usage:**
```bash
.venv/bin/python3 AGENTS/HAWK/scripts/boot.py
.venv/bin/python3 AGENTS/HAWK/scripts/boot.py --quick    # skip slow fetches
.venv/bin/python3 AGENTS/HAWK/scripts/boot.py --verbose  # full output
```

**Outputs:**
- Terminal: Color-coded brief with 🔴🟡🟢 status
- `workbook/BOOT_LOG.md` — Timestamped log for session continuity

---

### 2. `war_monitor.py` — War Status & Scenario Tracker

**Purpose:** Track daily war developments and update scenario probabilities (B/C/D framework).

**Data Sources:**
- Web search: "Israel Iran ceasefire" + "Houthi Red Sea" + "Hormuz status"
- News APIs: Reuters, Bloomberg, FT (via RSS or search)
- Social signals: Official statements (Twitter/X accounts)

**Output Format:**
```
HAWK War Monitor — 2026-04-20 08:00 ET
War Day: 51 | Scenario: D 82% / C 12% / B 6%
Ceasefire: Day 8 (Apr 12-13) | Brent: $64.50

Developments (last 24h):
  [🟡] No kinetic incidents reported
  [🟡] Houthi stand-down continues
  [🔴] No mine clearance operations visible

Scenario Shifts:
  D: 82% (unchanged) — Ceasefire holding but fragile
  C: 12% (unchanged) — No escalation triggers
  B: 6% (unchanged) — No permanent deal progress

Alerts: None
```

**Alert Thresholds:**
- 🔴 **Kinetic incident reported** → Immediate alert, D → 95%+
- 🔴 **Ceasefire collapse signal** → Immediate alert, reassess scenarios
- 🟡 **Diplomatic statement from key party** → Log, flag for manual review
- 🟡 **Houthi activity resumes** → C scenario upgrade

**Output Files:**
- `workbook/WAR_LOG.md` — Daily entries
- `workbook/SCENARIO_HISTORY.tsv` — Date, D%, C%, B%, trigger_event

---

### 3. `oil_infrastructure.py` — Facility Status Monitor

**Purpose:** Track status of key Gulf energy infrastructure (damage, repair, restart).

**Facilities Monitored:**
| Facility | Location | Status | Importance |
|----------|----------|--------|------------|
| Fujairah Terminal | UAE | Damaged (assessment pending) | 1.4M bpd export capacity |
| Ras Laffan | Qatar | Damaged (repair: 3-5yr baseline) | LNG export hub |
| ADCOP Pipeline | UAE-Oman | Damaged (Hormuz bypass) | 1.5M bpd bypass route |
| Yanbu | Saudi Arabia | Operational | Red Sea export terminal |
| Al Taweelah/EGA | UAE | Damaged | 4% global aluminium |
| Kharg Island | Iran | Operational | Primary Iran export terminal |

**Data Sources:**
- Web search: facility name + "repair" + "restart" + "damage"
- Industry sources: Energy Intelligence, Platts, Genscape
- Company statements: ADNOC, QatarEnergy press releases
- Satellite imagery: TankerTrackers, Sentinel Hub (optional future)

**Output Format:**
```
HAWK Infrastructure Monitor — 2026-04-20

Facility Status:
  Fujairah Terminal    🔴 DAMAGED    — No repair timeline announced
  Ras Laffan           🔴 DAMAGED    — 3-5yr repair baseline, no update
  ADCOP Pipeline       🔴 DAMAGED    — Hormuz bypass offline
  Yanbu                🟢 OPERATIONAL
  Al Taweelah/EGA      🔴 DAMAGED    — Aluminium supply shock ongoing
  Kharg Island         🟢 OPERATIONAL

Key Signals:
  [⏳] No mine clearance visible (Hormuz)
  [⏳] No insurance reinstatement
  [⏳] No QatarEnergy restart timeline

Alert: None
```

**Alert Thresholds:**
- 🔴 **New facility strike reported** → Immediate alert, Brent spike expected
- 🔴 **Restart timeline announced** → B scenario upgrade signal
- 🟡 **Assessment/inspection reports** → Log, update facility notes

**Output Files:**
- `workbook/FACILITY_STATUS.tsv` — Facility, status, last_update, notes
- `workbook/INFRASTRUCTURE_LOG.md` — Chronological updates

---

### 4. `sanctions_tracker.py` — Shadow Fleet & Enforcement Monitor

**Purpose:** Track sanctions enforcement, shadow fleet activity, and insurance market changes.

**Data Sources:**
- Web search: "shadow fleet" + "tanker seizure" + "sanctions"
- US Treasury: OFAC announcements
- EU/G7: Price cap enforcement updates
- Insurance markets: Lloyd's List, P&I club statements
- Tanker tracking: MarineTraffic, TankerTrackers (AIS data)

**Metrics Tracked:**
- Shadow fleet size (tankers >15 years, opaque ownership, AIS gaps)
- Enforcement actions (seizures, designations, penalties)
- Insurance rates (war risk premiums, P&I coverage status)
- Russian oil price cap compliance
- Iranian oil export volumes (estimates)

**Output Format:**
```
HAWK Sanctions Tracker — 2026-04-20

Shadow Fleet:
  Estimated VLCCs: ~XXX (+/- X vs last week)
  AIS dark activity: X incidents (7-day)

Enforcement (last 7 days):
  [None] No new OFAC designations
  [None] No tanker seizures reported

Insurance Market:
  Gulf war risk premium: $X/barrel (unchanged)
  Hormuz coverage: 🔴 SUSPENDED (no reinstatement)

Alert: None
```

**Alert Thresholds:**
- 🔴 **Major tanker seizure** (G7 enforcement) → Supply disruption risk
- 🔴 **Insurance reinstatement announced** → B scenario upgrade, shipping normalization
- 🟡 **New OFAC designations** → Log, assess shadow fleet impact
- 🟡 **War risk premium spike >X%** → Shipping cost inflation signal

**Output Files:**
- `workbook/SHADOW_FLEET.tsv` — Date, vlcc_count, dark_activity, notes
- `workbook/SANCTIONS_LOG.md` — Enforcement actions, policy changes

---

### 5. `thresholds.py` — Brent & Scenario Threshold Monitor

**Purpose:** Pull live oil prices and check against HAWK thesis thresholds.

**Data Sources:**
- yfinance: `BZ=F` (Brent), `CL=F` (WTI)
- FORGE market data: `python3 FORGE/tools/market-data/fetch.py price BRENT`

**Thresholds:**
```python
THRESHOLDS = [
    # Scenario D triggers (escalation)
    ("BZ=F", "above", 150.0, "risk", "D confirmed — Kharg strike or Hormuz closure"),
    ("BZ=F", "above", 120.0, "risk", "Severe escalation — multi-facility strikes"),
    ("BZ=F", "above", 100.0, "risk", "Escalation signal — ceasefire collapse likely"),
    
    # Scenario C/B triggers (de-escalation)
    ("BZ=F", "below", 70.0, "thesis", "C scenario — controlled burns framework"),
    ("BZ=F", "below", 60.0, "thesis", "B scenario — deal/stand-down confirmed"),
    
    # WTI-Brent spread (Hormuz bypass indicator)
    ("CL=F", "above", "BZ=F", "stress", "WTI > Brent — Hormuz supply squeeze"),
]
```

**Output Format:**
```
HAWK Threshold Monitor — 2026-04-20 08:00 ET
Brent: $64.50 (-44.6% from peak) | WTI: $XX.XX

BREACHES: None

Proximity Warnings:
  [🟡] Brent $64.50 — Within 10% of B scenario threshold ($60)

Scenario Alignment:
  Current: D 82% — Brent collapse reflects demand destruction, not supply recovery
  Signal: Price normalized, physical supply chain still damaged
```

**Alert Thresholds:**
- 🔴 **Brent >$100** → Ceasefire collapse signal, reassess scenarios
- 🔴 **Brent >$120** → Full escalation confirmed, D → 95%+
- 🟡 **Brent <$60** → B scenario threshold, check physical restart progress
- 🟡 **WTI > Brent** → Hormuz bypass stress, supply squeeze signal

**Output Files:**
- `workbook/PRICE_BREACHES.tsv` — Date, price, threshold, breach_type

---

### 6. `catalyst_countdown.py` — Key Dates Tracker

**Purpose:** Countdown to critical catalysts (ceasefire checkpoints, OPEC meetings, talks).

**Data Source:**
- `workbook/CATALYSTS.tsv` — Date, event, category, priority, notes

**Key Catalysts:**
| Date | Event | Priority |
|------|-------|----------|
| May 12-13 | 30-Day Ceasefire Checkpoint | 🔴🔴 |
| TBD | US-Iran Talks (Next Round) | 🔴 |
| TBD | OPEC+ Ministerial Meeting | 🟡 |
| TBD | Mine Clearance Operations | 🔴 |

**Output Format:**
```
HAWK Catalyst Countdown — 2026-04-20 (45-day horizon)

UPCOMING CATALYSTS:
  🔴🔴 May 12  — 30-Day Ceasefire Checkpoint (22 days)
       Signal: Extension vs collapse; mine clearance status
       
  🔴 TBD     — US-Iran Talks (Next Round)
       Signal: Framework → concrete agreements
       
  🟡 TBD     — OPEC+ Ministerial Meeting
       Signal: Production policy, spare capacity assessment

PAST CATALYSTS:
  ✅ Apr 12-13 — Ceasefire Declared (8 days ago)
```

**Alert Thresholds:**
- 🔴 **Within 5 trading days** → Flag for intensive monitoring
- 🔴 **Within 1 day** → Alert all agents, prepare scenario reassessment
- 🟡 **Within 30 days** — Include in daily brief

**Output Files:**
- Terminal output (primary)
- `workbook/CATALYST_LOG.md` — Historical record

---

## File Structure

```
AGENTS/HAWK/
├── scripts/
│   ├── boot.py                 # Master orchestrator
│   ├── war_monitor.py          # War status & scenarios
│   ├── oil_infrastructure.py   # Facility damage/repair
│   ├── sanctions_tracker.py    # Shadow fleet & enforcement
│   ├── thresholds.py           # Brent price thresholds
│   └── catalyst_countdown.py   # Key dates countdown
├── workbook/
│   ├── CATALYSTS.tsv           # Catalyst date registry
│   ├── FACILITY_STATUS.tsv     # Infrastructure status
│   ├── SCENARIO_HISTORY.tsv    # D/C/B probability history
│   ├── SHADOW_FLEET.tsv        # Shadow fleet metrics
│   ├── PRICE_BREACHES.tsv      # Threshold breach log
│   ├── BOOT_LOG.md             # Boot sequence history
│   ├── WAR_LOG.md              # Daily war developments
│   ├── INFRASTRUCTURE_LOG.md   # Facility updates
│   └── SANCTIONS_LOG.md        # Enforcement actions
└── CALENDAR.md                 # Forward catalyst table
```

---

## Implementation Priority

| Priority | Script | Rationale |
|----------|--------|-----------|
| P0 | `boot.py` | Entry point; unifies all tools |
| P0 | `thresholds.py` | Immediate market signal (Brent) |
| P0 | `catalyst_countdown.py` | Time-sensitive (May 12 checkpoint) |
| P1 | `war_monitor.py` | Core HAWK function (ceasefire monitoring) |
| P1 | `oil_infrastructure.py` | Physical supply chain tracking |
| P2 | `sanctions_tracker.py` | Secondary signal (shadow fleet) |

---

## Dependencies

```bash
# Python packages (add to requirements.txt)
yfinance          # Price fetching
requests          # Web APIs
beautifulsoup4    # HTML parsing
feedparser        # RSS feeds

# External tools
FORGE/tools/market-data/fetch.py  # Live price fallback
web_search / web_fetch            # OpenClaw built-ins
```

---

## Integration with Other Agents

| Script | Output To | Signal |
|--------|-----------|--------|
| `thresholds.py` | BRENT, HENRY, LIQUID | Brent price breaches |
| `war_monitor.py` | RED, NEXUS, ALL | Scenario probability changes |
| `oil_infrastructure.py` | BRENT | Facility restart signals |
| `sanctions_tracker.py` | BRENT, LIQUID | Shipping/insurance normalization |
| `catalyst_countdown.py` | ALL | Catalyst proximity alerts |

---

## Notes

- Pattern follows SAM/scripts/ architecture for consistency
- All scripts should be runnable standalone OR via `boot.py`
- Output should be Telegram-friendly (compact mode flag)
- Idempotent: running twice same day shouldn't duplicate data
- Fail gracefully: network errors → warning, not crash
