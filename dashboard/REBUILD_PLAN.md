# Dashboard Rebuild Plan

**Created:** 2026-03-15
**Goal:** Fully dynamic dashboard — zero hardcoded content, everything parsed from workspace files via API.

## Architecture

**Server:** Python HTTP server (same stack), new parsing endpoints
**Frontend:** Single `index.html`, all content from API, auto-refresh 60s
**Access:** Tailscale, port 8080, bind 0.0.0.0

## Segments

### SEGMENT 1: Server rewrite + API layer ✅ COMPLETE (Mar 15)
- Rewrite `server.py` with new parsing endpoints:
  - `/api/positions` — parse positions table from `PROME/STATUS.md`
  - `/api/scenario` — parse scenario probabilities, Hamilton refs, current state from `PROME/STATUS.md`
  - `/api/catalysts` — parse dates table from `PROME/STATUS.md`
  - `/api/agent/<name>` — return parsed header + key metrics from any agent STATUS.md
  - Add Brent/WTI to `/api/prices`
- Keep working endpoints: `/api/prices`, `/api/fred`, `/api/bls`, `/api/sec`, `/api/predictions`, `/api/alerts`, `/api/subagents`
- Serve minimal placeholder `index.html` that dumps API responses
- **Exit state:** Server runs, all APIs return correct data parsed from workspace files
- **Test:** `curl localhost:8080/api/positions` returns structured JSON

### SEGMENT 2: Core frontend — Overview tab ✅ COMPLETE (Mar 15)
- Build real `index.html`: design system (CSS vars, dark theme, layout grid)
- Overview tab: scenario hero, positions table, metrics strip, agent grid, catalysts
- All API-driven, auto-refresh 60s
- **Exit state:** Dashboard loads, shows live data, one tab fully works

### SEGMENT 3: Remaining tabs ✅ COMPLETE (Mar 15)
- Data tab (domain sections per agent — LABOR, CARL, SAM, HENRY, LIQUID, REGINALD, energy)
- Network graph (full 18-agent roster, updated connections)
- Predictions tab (already API-driven, verify parser)
- Calendar tab
- **Exit state:** All tabs functional

### SEGMENT 4: Polish + new features ✅ COMPLETE (Mar 14)
- ✅ Energy/War tab: scenario hero + oil prices, scenario probabilities, Hamilton framework, Taiwan LNG + TSMC chain + escalation indicators, fertilizer calendar + feedback loop, exit rules (binary vs protracted) with protocols, cross-agent transmission matrix, key agent summaries (HAWK/BRENT/SAM/LIQUID)
- ✅ Mobile responsive: all layouts flex/wrap on ≤768px (header, tabs, scenarios, metrics, grids, modals)
- ✅ Agent detail modals: status bar (color-coded), table rendering, markdown formatting (headers/bold/code/hr)
- ✅ `/api/energy` endpoint: aggregates scenarios + hamilton + taiwan + fertilizer + exit rules + cross-agent + agent summaries + oil prices
- ✅ Agent status parser: handles `**Overall Status:**`, `**Signal Status:**` variants
- ✅ New parsers: tsmc_chain, taiwan_escalation, fertilizer_loop, fertilizer_header, exit_protocol_a/c, exit_template, scenario_c_duration
- **Exit state:** Production-ready

## Key Files
- `dashboard/server.py` — backend
- `dashboard/index.html` — frontend
- `dashboard/network.html` — standalone network view (fold into main or keep)
- `PROME/STATUS.md` — primary data source for positions, scenarios, catalysts, agents

## Parsing Targets in STATUS.md
- **Positions section:** Markdown table/list with ticker, strike, expiry, qty, P/L %
- **Agents table:** `| Agent | St | Key State | Upd |`
- **Dates table:** `| Date | Event |`
- **Convictions table:** `| # | Trade | C | Hamilton |`
- **Scenario table:** `| Scenario | Prob | Change | Description |`
- **Pending table:** `| Action | Pri |`

## Design Principles
1. Dashboard NEVER hardcodes data that exists in workspace files
2. If you update STATUS.md, dashboard reflects it on next refresh
3. Server parses markdown tables → JSON (regex-based, simple)
4. Frontend is a dumb rendering layer
5. Fail gracefully — if a section can't parse, show "No data" not crash
