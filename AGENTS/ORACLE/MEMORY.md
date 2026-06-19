# ORACLE — MEMORY

## 2026-06-18 — REVIVAL (Will-directed audit session)

ORACLE brought back online after 79 days dormant (last touch 2026-04-01 inaugural boot). Audit found it had a strong `CLAUDE.md` but no operational plumbing and stale data.

**Built this session:**
- `scripts/polymarket.py` — reusable fetcher on the Polymarket Gamma API (public, no auth). Subcommands: `search`, `market`, `event`, `pull [--log]`. Bakes in the thin-liquidity guardrail (⚠️ flag < $5K liquidity).
- `watchlist.tsv` — 8 markets (recession, Fed cuts, bank failure, debt default, Iran, AI bubble, NEH), each routed to active agents only.
- `workbook/` — `SCHEMA.tsv` (13-col, from template), `KB.tsv` (6 seed claims), `VX.tsv` (threshold vectors), `ODDS_LOG.tsv` (time-series, seeded 1 pull).
- `STATUS.md` rewritten with live data + divergence map + alerts.
- `TRADE.md`, mail dirs (`inbox/`, `outbox/`), `domain/sources/`.
- 2 outbox signals: Iran de-escalation → HAWK/BRENT (🔴); recession divergence → RED.

**First live pull (`2026-06-19T00:18Z`) — key reads:**
- 🔴 Iran "ends enrichment by Jun 30" **+43pp/7d → 66.5%** ($6M deep) — fast de-escalation, oil-down for BRENT. Corroborates WALTER 6/16.
- Recession **12.5%** (−5/7d) vs thesis ~76% = **63pp divergence, widening** — RED to adjudicate.
- Fed no-cuts **81.9%** — past the 57–70% HENRY anchored to; higher-for-longer confirms.
- "Nothing Ever Happens 2026" 44%→**82.5%** since Apr — complacency surge (pairs with VIOLET).

**Pending / next session:**
- Data-source note: no `POLY` SOURCE_TAG in VOCABULARIES.tsv — propose one to PROME (used free-text "Polymarket" for now).
- Kalshi not wired (needs API key) — recession/Fed/CPI markets there would corroborate Polymarket. Ask Will if he has Kalshi creds.
- Thesis side of the divergence map is the Apr baseline — get a current read from RED/SENTRY.
- Bank-failure Jun-30 market resolves 6/30 — find the next-month replacement before then.
- Re-pull cadence: `polymarket.py pull --log` each session (or schedule). 3-day re-check due ~6/22 on the thin movers per discipline.

**Git:** all changes inside `AGENTS/ORACLE/`. Committed locally; push deferred to a Will-coordinated window (per shared-branch protocol).
