> # ⛔ FROZEN 2026-08-27 — historical only, not maintained
>
> **This file stopped being updated on 2026-07-09 and is not coming back.** It is a
> **revival log** from ORACLE's 2026-06-18 rebuild, and it reads as a live state file,
> which is why it was flagged in the Will-directed sweep.
>
> **It was superseded rather than neglected.** Durable, transferable learning now goes
> to **fleet auto-memory** (`memory/auto/`, indexed in `MEMORY.md` at the repo root),
> and session-to-session state lives in **`SCRATCH.md`** — the canonical handoff. Both
> are read at every boot; this file is read by nobody.
>
> **Do not cite any figure below as current** — every number is a 2026-06/07 vintage.
> Some entries were already self-corrected in the 7/09 sweep and are kept that way on
> purpose: the corrections are part of the record.
>
> **Live homes:** `SCRATCH.md` (handoff) · `STATUS.md` (dashboard) · `MAINTENANCE.md`
> (structural log) · `workbook/KB.tsv` (claims) · `memory/auto/` (fleet-transferable).

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

**Pending / next session (as of 6/18 — see status notes below, corrected 2026-07-09 self-sweep):**
- Data-source note: no `POLY` SOURCE_TAG in VOCABULARIES.tsv — propose one to PROME (used free-text "Polymarket" for now). *(Still using free-text as of 7/9; low priority.)*
- ~~Kalshi not wired~~ — **RESOLVED 2026-06-27**: `scripts/kalshi.py` built + wired, creds present, corroboration lane LIVE (see MAINTENANCE.md 6/27 entry).
- Thesis side of the divergence map is the Apr baseline — get a current read from RED/SENTRY. *(Still owed as of 7/9 — RED carried since 6/13; not urgent, crowd & fleet both calm.)*
- ~~Bank-failure Jun-30 market resolves 6/30~~ — **RESOLVED 6/30, rolled 7/2** (roll-watch: no clean single-binary July replacement exists yet; named-bank-EOY event carries the cluster).
- Re-pull cadence: `polymarket.py pull --log` each session (or schedule) — **standing practice since**, both platforms, every session.
- ~~Push deferred to a Will-coordinated window~~ — **SUPERSEDED 2026-06-27**: auto-push at closeout via `scripts/safe-push.sh` is now the fleet standard (see MAINTENANCE.md 6/27 entry); this file's original git note below is historical only.

**Git (historical, 6/18):** all changes inside `AGENTS/ORACLE/`. Committed locally; push deferred to a Will-coordinated window (per shared-branch protocol). *(See correction above — superseded 6/27.)*
