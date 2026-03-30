# Layer 3: dashboard.py — Build Plan

**Created:** 2026-03-29
**Status:** ✅ ALL SEGMENTS COMPLETE (Mar 29)
**Goal:** CLI tool that pulls live data, classifies against thresholds, and outputs a color-coded stress dashboard. Runs manually, via cron, or piped as JSON to Telegram/agents.

---

## What Already Works

| Component | Status | Notes |
|-----------|--------|-------|
| `config.py` (Layer 2) | ✅ Approved Mar 28 | 17 series, thresholds, classify(), format helpers |
| `fetch.py` (Layer 1) | ⚠️ Partial | FRED works. yfinance batch download has a parsing bug — `price_fetch()` fails on multi-ticker. Single-ticker via `yf.Ticker().fast_info` works fine |
| FRED API key | ✅ | In fetch.py |
| yfinance | ✅ Installed | v1.2.0 |
| server.py (web dashboard) | ✅ Running | Has its own hardcoded thresholds — should eventually import config.py too, but that's separate scope |

## What Layer 3 Needs To Do

### Core Job
Pull every series in `config.py`, get its current value, classify it (🟢🟡🔴), and present results. That's it. Everything else is incremental.

---

## Build Segments

### Segment 1: Fix fetch + core display
**Goal:** `python3 dashboard.py` prints a working dashboard.

**Tasks:**
1. **Fix `fetch.py` price_fetch()** — switch from `yf.download()` (batch, brittle) to `yf.Ticker(t).fast_info['lastPrice']` (reliable per-ticker). Add `price_single(ticker)` function that config.py series can call directly.
2. **Build `dashboard.py`** — loop through `config.SERIES`, fetch each value (FRED or price based on `source` field), run `classify()`, print table:
   ```
   PROME Market Stress Dashboard
   ══════════════════════════════════════════════════════
   Updated: 2026-03-29 20:30 UTC

   TIER 1 — DECISION DRIVERS
   ┌────────────────┬──────────────┬──────────┬────────┐
   │ Series         │ Value        │ Zone     │ Agent  │
   ├────────────────┼──────────────┼──────────┼────────┤
   │ HY OAS         │ 321bps       │ 🔴 >320  │ REG/LIQ│
   │ Init Claims    │ 210,000      │ 🟢 <225K │ LABOR  │
   │   (shadow adj) │ ~265,000     │          │        │
   │ Brent          │ $112.57      │ 🔴 >100  │ HENRY  │
   └────────────────┴──────────────┴──────────┴────────┘

   TIER 2 — POSITION MONITORING
   ...

   SUMMARY: 4🔴 6🟡 3🟢  |  Stress level: ELEVATED
   ```
3. **Shadow adjustment** — for claims, display raw value + shadow-adjusted estimate on next line (per Will's Mar 28 design decision). Don't use adjusted value for classification.
4. **Stress summary** — count reds/yellows/greens. Simple label: CALM (0-1 red), ELEVATED (2-3 red), CRITICAL (4+ red).

**Exit criteria:** `python3 dashboard.py` prints accurate, readable output with live data.

---

### Segment 2: Filtering + output modes
**Goal:** Agent views, tier filters, JSON output.

**Tasks:**
1. `--tier 1` / `--tier 2` — show only that tier
2. `--agent LABOR` — show only series owned by that agent (uses `config.get_agent()`)
3. `--json` — output structured JSON instead of table (for piping to other tools)
4. `--quiet` — only show 🔴 items (breach-only mode, good for cron)
5. `--compact` — one-line-per-series, no box drawing (for Telegram paste)

**Exit criteria:** All flags work. `python3 dashboard.py --json | jq .` returns valid structured data.

---

### Segment 3: Change detection + alerts
**Goal:** Know when zones change. Fire alerts.

**Tasks:**
1. **State file** — save current classifications to `.cache/last_run.json` after each run
2. **Diff on run** — compare current vs last. Flag transitions: `HY OAS: 🟡→🔴 (was 318, now 321)`
3. **Exit code** — return 0 if no reds, 1 if any reds, 2 if any NEW reds (zone transition). Enables `dashboard.py || notify`
4. **`--alert` flag** — only print output if something changed since last run (silent otherwise)
5. **Telegram integration** — `--notify` sends zone transitions to Telegram (reuse `send_telegram_alert` from server.py, or inline the bot token)

**Exit criteria:** Run twice — first shows baseline, second shows "no changes" or flags transitions. `--notify` delivers to Telegram.

---

### Segment 4: Cron + integration
**Goal:** Runs automatically, feeds into the system.

**Tasks:**
1. **Cron schedule:**
   - Market hours (9:30 AM – 4 PM ET, Mon-Fri): every 15 min
   - Off-hours weekdays: every 60 min
   - Weekends: every 4 hours (futures still move)
   - Skip 11 PM – 8 AM ET (Will's quiet window) for notifications, but still log
2. **Log file** — append each run's summary to `.cache/dashboard_log.jsonl` (timestamp + all values + zones). Enables "what changed while I slept?" queries.
3. **Agent STATUS update** (stretch) — on zone transition, append a line to the relevant agent's STATUS.md inbox or a dedicated `FORGE/tools/market-data/breach_log.md`
4. **Heartbeat hook** (stretch) — if HEARTBEAT.md check runs and dashboard has unacknowledged red transitions, surface them

**Exit criteria:** Cron installed, runs silently, alerts fire on transitions, log accumulates.

---

## Dependencies & Risks

| Risk | Mitigation |
|------|------------|
| yfinance rate limiting | Cache (already built, 5min TTL). Single-ticker calls are lighter than batch |
| FRED data lag (weekly series like gas) | Show date alongside value so staleness is visible |
| Weekend/holiday stale prices | Display market status (open/closed) and last trade date |
| Server.py threshold divergence | Future cleanup: make server.py import config.py too. Out of scope for this plan |

## Estimated Effort

| Segment | Effort | Can ship independently? |
|---------|--------|------------------------|
| Segment 1 | ~30 min | ✅ Yes — immediately useful |
| Segment 2 | ~20 min | ✅ Yes |
| Segment 3 | ~30 min | ✅ Yes |
| Segment 4 | ~20 min | ✅ Yes |

Each segment is independently shippable. Can stop after any one and have something that works.

---

## Open Questions for Will

1. **Compact format for Telegram** — should `--compact` output be something I auto-send as a morning briefing? Or just a tool you invoke?
2. **Stress summary thresholds** — CALM/ELEVATED/CRITICAL cutoffs. Proposed: 0-1 red = CALM, 2-3 = ELEVATED, 4+ = CRITICAL. Or should it weight Tier 1 heavier?
3. **server.py unification** — want me to refactor server.py to import config.py in a future segment, or leave them independent?
