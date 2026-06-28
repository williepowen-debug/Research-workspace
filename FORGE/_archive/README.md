# FORGE/_archive — retired trade-execution layer

Archived **2026-06-28** (Will-directed, WALTER executed). FORGE's trade-execution
ledger went dormant once the **live book moved to `WILL/trading-journal/` (photos, current)**
and **trade-construction moved to TERRY** (the Tier-1 thesis→trade-plan agent). The
markdown execution ledger here was last meaningfully maintained 2026-03/05 and was the
"silent-rot middle" (read as current, wasn't), so it was moved out of the active tree.

**Recoverable** — these are `git mv`d, not deleted; full history preserved (`git log --follow`).

Archived:
- Per-trade folders: `KRE/`, `WAL/`, `OZK/` (Mar 17 historical)
- `ACTIVE_TRADES.md` (self-flagged stale since Mar 25), `JOURNAL.md`, `WATCHLIST.md`, `PROTOCOL.md`, `INBOX.md`
- `snapshots/`, `scratch/`
- One-off thesis/screen docs: `CF-trade-thesis.md`, `OIL_OPTIONS_SCREEN.md`, `AAL_VULNERABILITY_SCREEN.md`, `ENTRY_THESIS_BACKFILL.md`, `oil-shock-position-timing.md`, `DEBATE_FRAMEWORK.md`, `UNCTAD-hormuz-data-mar10.md`, `downstream-impacts-detailed-mar10.md`

**KEPT live in FORGE/** (NOT archived): `tools/` (market-data CLI — the fleet's shared
data source, actively maintained), `signals/`, plus `STATUS.md` + `PORTFOLIO.md` — the
fleet's structured **position-truth surface** that live agents (TERRY/REGINALD/CARL) still
read. The "where does structured position-truth live now" decision was routed to PROME
(`AGENTS/PROME/inbox/SIG-WALTER-PROME-20260628-forge-position-truth-decision.md`).
The research corpora (`research/`, `timing/`, `education/`, `trigger-sets/`) were left in
place — they're research, not execution, and out of scope for this cleanup.
