# ORACLE — MAINTENANCE (structural-change log + watchlist upkeep)

Structural changes only (docs / scripts / protocol — the "why is ORACLE organized this way" record). Analytical changes go to STATUS/KB. Peer convention (VIOLET/OTTO template).

## Watchlist upkeep routine (recurring — the load-bearing maintenance)

Polymarket slugs **rot**: markets resolve at their end-date and drop off. Every `pull` flags `⏳<N>d` (resolves ≤7d) and `⛔RESOLVED`, and prints a maintenance block listing them.

- On `⏳` / `⛔`: run `python3 scripts/polymarket.py search "<topic>"`, pin the next-period slug in `watchlist.tsv`, re-pull.
- **Month-boundary markets** (bank-failure, named-bank, Iran, both WTI rungs) resolve ~Jun 30 / Jul 1 — roll to July/next-period.
- Drop markets below readable liquidity (e.g. `june-unemployment-rate-734` = $63 vol — noise; replace with a liquid labor market or remove).
- Grouped events (`type=event`) only surface the top sub-market — fine for named-bank (worst name) and unemployment (modal), but price ladders lose strike context; for WTI we pin **specific rungs** as `market` rows instead.

## Structural log

### 2026-06-18 — REVIVAL (Will-directed audit, session 1)
- **Trigger:** agent dormant 79d (last 2026-04-01); Will revived + audited.
- **Built:** `scripts/polymarket.py` (Gamma-API fetcher), `watchlist.tsv` (8 mkts), `workbook/{KB,VX,SCHEMA,ODDS_LOG}`, `STATUS`/`TRADE`/`MEMORY`, `inbox`/`outbox`.
- **Files:** all within `AGENTS/ORACLE/`. Committed + pushed (`a647b97`).

### 2026-06-18 — gap-audit hardening (session 2)
- **Trigger:** Will "audit what else is missing" → found coverage holes + fleet-invisibility.
- **Coverage:** +6 markets → watchlist 8→14 (bailout, named-bank event, WTI-$70-low, WTI-$100-high, MicroStrategy, June-unemployment).
- **Fetcher:** added slug-expiry detection (`⏳`/`⛔` + maintenance block); readable event-ladder display (shows strike + slug).
- **Fleet integration:** added `NEXUS_BRIEF.md` (primary cross-agent surface — NEXUS reads it), `SIGNAL_INTAKE.md` (WALTER subscription spec), `inbox/WALTER/` delivery lane (WALTER Routing v2), `SCRATCH.md` (session handoff), this file.
- **Flagged to PROME** (`outbox/…to-PROME…`): wire ORACLE into FLEET_SCAN/HEARTBEAT/dashboard; WALTER refresh REGISTRY row → ACTIVE + subscribe; NEXUS pull the brief; route the 2 stranded outbox signals.
- **Known limits:** Kalshi unwired (needs API key); thesis-side divergence numbers are Apr baseline (RED refresh owed); `RECEIPT.md` intentionally skipped (file-mail being deprecated per fleet direction).

### 2026-06-21/22 — boot + audit + coverage sweep (Will-directed)
- **Trigger:** first boot; Will "make sure other figures are accurate" then "sweep for other relevant markets."
- **Audit:** refreshed fleet-thesis baselines vs current domain state (workflow) → RETRACTED the recession/bank "divergences" (stale Apr strawmen; fleet converged toward crowd). Iran de-escalation alert reversed → stalemate. LIQUID July-hike figure-check delivered to LIQUID/inbox.
- **New capability:** `history` subcommand — daily CLOB `prices-history` backfill (Δ30/90d, range, sparkline, ⚡spiky/round-trip flag) → `workbook/HISTORY.tsv`. The durable trajectory view (survives stale point-in-time baselines).
- **Coverage:** +13 (sweep) then +6 (Will a+b) → **watchlist 15→34**. New themes: Fed-funds-dist, inflation>5%, unemployment-ladder, Taiwan, US-invade-Iran, Hormuz (Dec+June), Iran-leadership, Russia-Ukraine, China-GDP, China-Philippines, BOJ-July, BTC-dip-$40K, risk-appetite; + July catalysts (June CPI, Citi/BAC Q2 provisions) + FL hurricane Cat-4/Cat-5 season-watch.
- **Fetcher fix:** `resolved` now trusts the authoritative `closed` field, NOT a past `endDate` (some live distribution-event rungs carry stale Jan endDates → false RESOLVED). Added `⏮stale-date` flag. Corrected the boot-time mis-drop of the (live) unemployment market.
- **Roll watch:** near-dated adds resolve mid-July (CPI 7/15, Citi/BAC provisions 7/14) and 6/30 (June Hormuz) — drop/roll after resolve.
- **Gaps (no liquid market — domain-call only):** private credit/BDC/HY-spread, CRE/CMBS, single-name regionals (WAL/OZK), US NFP/PCE, VIX/vol (→Kalshi), year-end oil/Brent, and most of Florida (only Safepoint IPO + Cat-4/5 hurricanes exist, all thin).
