# HAWK Script Fixes - Completion Report

**Date:** 2026-04-20  
**Agent:** HAWK (geopolitical/military risk)  
**Task:** Fix script issues identified in audits

---

## 1. thresholds.py — Added --quick flag ✅

**Changes:**
- Added `get_cached_price()` function to read last known price from `workbook/PRICE_BREACHES.tsv`
- Added `--quick` argument to argparse
- When `--quick` is passed, script skips yfinance fetch and uses cached price
- Falls back to live fetch if no cache exists
- Shows `[QUICK MODE: Using cached price]` indicator

**Test Results:**
```bash
$ python3 AGENTS/HAWK/scripts/thresholds.py --quick

======================================================================
  HAWK Threshold Monitor — 2026-04-20 17:56 ET
======================================================================

  [QUICK MODE: Using cached price]

  BRENT CRUDE: $94.28  (+0.00%)
  vs Peak:     -19.0%  (peak: $116.38)

  SCENARIO ZONE: C
  ------------------------------------------------------------
  🟡 CONTROLLED — Controlled burns framework threshold
  ...
```

---

## 2. war_monitor.py — Fixed web_search implementation ✅

**Changes:**
- Replaced stub `run_web_search()` with working implementation using Google News RSS
- Added `fetch_rss_feed()` helper for direct RSS fetching
- Updated `search_war_news()` to use both Google News RSS and direct RSS feeds (BBC, Reuters)
- Implements keyword filtering for relevant articles
- Graceful error handling with try/except blocks
- 10-second timeout on all HTTP requests

**Test Results:**
```bash
$ python3 AGENTS/HAWK/scripts/war_monitor.py

======================================================================
  HAWK War Monitor — 2026-04-20 17:56 ET
======================================================================

  War Day: 50 | Ceasefire Day: 8 (Apr 12-13)
  Baseline Scenario: D 82% / C 12% / B 6%

  🔍 Scanning for developments...

  SIGNAL SUMMARY (last 24h)
  ------------------------------------------------------------
  🟢 Diplomatic progress indicators
     Impact: B +5%
     Details: Keywords: 3 de-escalation mentions

  SCENARIO PROBABILITY SHIFTS
  ------------------------------------------------------------
  🔴 D: 82% → 77% (↓ -5%)
  🟡 C: 12% → 12% (→ unchanged)
  🟢 B: 6% → 11% (↑ +5%)

  INTERPRETATION
  ------------------------------------------------------------
  🟢 De-escalation momentum — watch for deal framework

  ALERTS
  ------------------------------------------------------------
  ✅ No active alerts
```

---

## 3. sanctions_tracker.py — Fixed web_search implementation ✅

**Changes:**
- Replaced stub `run_web_search()` with working implementation using Google News RSS
- Added `fetch_rss_feed()` helper for direct RSS fetching
- Updated `search_sanctions_news()` to use both Google News RSS and direct RSS feeds (Reuters)
- Implements keyword filtering for relevant articles (tanker, sanctions, oil, fleet, etc.)
- Graceful error handling with try/except blocks
- 10-second timeout on all HTTP requests

**Test Results:**
```bash
$ python3 AGENTS/HAWK/scripts/sanctions_tracker.py

======================================================================
  HAWK Sanctions Tracker — 2026-04-20 17:56 ET
======================================================================

  SHADOW FLEET
  ------------------------------------------------------------
  Estimated VLCCs:        ~350 vessels
  AIS dark activity (7d): 12 incidents
  Trend:                  🟡 Stable (no significant change)

  🔍 Scanning for enforcement actions...

  ENFORCEMENT (last 7 days)
  ------------------------------------------------------------
  🔴 Enforcement: Detected in news flow

  INSURANCE MARKET
  ------------------------------------------------------------
  Gulf war risk premium:  $2.5/barrel
  Hormuz coverage:        🔴 SUSPENDED

  ...
```

---

## Implementation Details

### Web Search Approach
All scripts now use a hybrid approach:
1. **Google News RSS** - Primary source via `news.google.com/rss/search?q={query}`
2. **Direct RSS feeds** - Fallback to Reuters, BBC for specific domains
3. **XML parsing** - Using Python's built-in `xml.etree.ElementTree`
4. **Keyword filtering** - Articles filtered for relevance before display

### Error Handling
- All HTTP requests wrapped in try/except
- 10-second timeout on all network calls
- Graceful fallback to empty results on any error
- No stack traces exposed to user

### Files Modified
- `AGENTS/HAWK/scripts/thresholds.py`
- `AGENTS/HAWK/scripts/war_monitor.py`
- `AGENTS/HAWK/scripts/sanctions_tracker.py`

---

## Status: COMPLETE ✅

All three audit issues have been resolved and tested successfully.
