# HAWK Scripts — Completion Report

**Date:** 2026-04-20  
**Agent:** HAWK (Geopolitical/Military Risk)  
**Status:** ✅ Complete

---

## Scripts Delivered

All 6 scripts have been implemented following the SAM/scripts/ pattern:

### 1. `boot.py` — Master Orchestrator (P0)
- One-command morning refresh
- Runs all scripts in priority sequence
- Outputs consolidated brief with 🔴 alerts
- Saves log to `workbook/BOOT_LOG.md`

**Usage:**
```bash
python3 AGENTS/HAWK/scripts/boot.py
python3 AGENTS/HAWK/scripts/boot.py --quick    # skip slow scripts
python3 AGENTS/HAWK/scripts/boot.py --verbose  # full output
```

### 2. `thresholds.py` — Brent Price Monitoring (P0)
- Fetches live Brent price via yfinance (`BZ=F`)
- Checks against scenario triggers: $80, $100, $120, $150
- Outputs scenario zone (B/C/D), proximity warnings
- Saves to `workbook/PRICE_BREACHES.tsv`

**Usage:**
```bash
python3 AGENTS/HAWK/scripts/thresholds.py
python3 AGENTS/HAWK/scripts/thresholds.py --save
```

**Sample Output:**
```
BRENT CRUDE: $94.28  (+4.32%)
SCENARIO ZONE: C
🟡 CONTROLLED — Controlled burns framework threshold
```

### 3. `catalyst_countdown.py` — Days to Key Dates (P0)
- Parses `CALENDAR.md` for events
- Calculates calendar/trading days until each catalyst
- Flags 🔴 items within 7 days
- Highlights May 12 ceasefire checkpoint

**Usage:**
```bash
python3 AGENTS/HAWK/scripts/catalyst_countdown.py
python3 AGENTS/HAWK/scripts/catalyst_countdown.py --days 30
```

**Sample Output:**
```
📅 UPCOMING (within 60 days)
  2026-05-12 (Tue)   22d cal / 16d trd  30-Day Ceasefire Checkpoint
⏰ KEY CHECKPOINT: 22 calendar days / 16 trading days remaining
```

### 4. `war_monitor.py` — Daily War Developments (P1)
- Framework for scanning war news (web search ready)
- Tracks scenario probabilities (D/B/C framework)
- Outputs signal summary and probability shifts
- Saves to `workbook/WAR_LOG.md` and `SCENARIO_HISTORY.tsv`

**Usage:**
```bash
python3 AGENTS/HAWK/scripts/war_monitor.py
python3 AGENTS/HAWK/scripts/war_monitor.py --save
```

### 5. `oil_infrastructure.py` — Facility Status (P1)
- Tracks Fujairah, Ras Laffan, ADCOP, Yanbu, Al Taweelah, Kharg Island
- Outputs operational status and repair timelines
- Monitors key signals (mine clearance, insurance, assessments)
- Saves to `workbook/FACILITY_STATUS.tsv` and `INFRASTRUCTURE_LOG.md`

**Usage:**
```bash
python3 AGENTS/HAWK/scripts/oil_infrastructure.py
python3 AGENTS/HAWK/scripts/oil_infrastructure.py --save
```

**Sample Output:**
```
FACILITY STATUS
  🔴 Fujairah Terminal  UAE        DAMAGED      1.4M bpd export
  🔴 Ras Laffan         Qatar      DAMAGED      LNG export hub
  🟢 Yanbu              Saudi Arabia OPERATIONAL
SUMMARY: 4/6 facilities damaged (67%)
```

### 6. `sanctions_tracker.py` — Shadow Fleet/Insurance (P2)
- Tracks shadow fleet metrics (VLCC count, AIS dark activity)
- Monitors enforcement actions (OFAC, seizures)
- Reports insurance market status (war risk premiums, Hormuz coverage)
- Saves to `workbook/SHADOW_FLEET.tsv` and `SANCTIONS_LOG.md`

**Usage:**
```bash
python3 AGENTS/HAWK/scripts/sanctions_tracker.py
python3 AGENTS/HAWK/scripts/sanctions_tracker.py --save
```

---

## File Structure

```
AGENTS/HAWK/
├── scripts/
│   ├── boot.py                 # Master orchestrator ⭐
│   ├── thresholds.py           # Brent price monitoring
│   ├── catalyst_countdown.py   # Key dates countdown
│   ├── war_monitor.py          # War status & scenarios
│   ├── oil_infrastructure.py   # Facility damage/repair
│   ├── sanctions_tracker.py    # Shadow fleet & enforcement
│   └── LAST_COMPLETION.md      # This file
└── workbook/                   # Created on first run
    ├── BOOT_LOG.md
    ├── PRICE_BREACHES.tsv
    ├── WAR_LOG.md
    ├── SCENARIO_HISTORY.tsv
    ├── FACILITY_STATUS.tsv
    ├── INFRASTRUCTURE_LOG.md
    ├── SHADOW_FLEET.tsv
    └── SANCTIONS_LOG.md
```

---

## Dependencies

- `yfinance` — Live price fetching (Brent/WTI)
- Standard library: `argparse`, `datetime`, `pathlib`, `subprocess`

Install:
```bash
pip install yfinance
```

---

## Design Patterns (from SAM/scripts/)

1. **Shebang + executable:** All scripts have `#!/usr/bin/env python3` and are `chmod +x`
2. **Docstrings:** Purpose and usage in module docstring
3. **CLI args:** `argparse` for `--save`, `--verbose`, `--quick`, `--days`
4. **Clean tables:** Formatted terminal output with emoji indicators
5. **Error handling:** Graceful fallbacks for network/API issues
6. **Workbook integration:** Optional TSV/MD logging to `workbook/`

---

## Integration Notes

- **Brent data:** Uses yfinance (`BZ=F`) with fallback to FORGE market data
- **Web search:** Scripts include framework for `openclaw web-search` (currently graceful fallback)
- **Calendar:** Parses `CALENDAR.md` directly
- **Alerts:** All scripts output 🔴🟡🟢 status for boot.py consolidation

---

## Quick Start

```bash
# Daily morning refresh
python3 AGENTS/HAWK/scripts/boot.py

# Individual checks
python3 AGENTS/HAWK/scripts/thresholds.py
python3 AGENTS/HAWK/scripts/catalyst_countdown.py

# Save to workbook
python3 AGENTS/HAWK/scripts/boot.py --verbose  # also saves logs
```

---

**Completed by:** HAWK subagent  
**Verified:** All 6 scripts execute successfully  
**Output:** Clean formatted tables, proper error handling, workbook logging
