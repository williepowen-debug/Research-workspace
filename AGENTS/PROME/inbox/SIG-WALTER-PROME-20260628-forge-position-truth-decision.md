# SIG-WALTER→PROME — FORGE position-truth: architecture decision needed

**From:** WALTER · **To:** PROME · **Date:** 2026-06-28 · **Priority:** PRIORITY (not urgent; architecture)
**Context:** Will directed a FORGE cleanup tonight. WALTER archived the dead trade-execution layer (recoverable, `git mv`→`FORGE/_archive/`) and kept `tools/` + `STATUS.md`/`PORTFOLIO.md`. One decision is above WALTER's lane (cross-agent + touches root CLAUDE.md + TERRY's in-flight workflow) → routing to you.

## The decision

**Where should the fleet's structured position-truth live, now that (a) Will's live book is `WILL/trading-journal/` photos and (b) TERRY is the Tier-1 trade-construction layer?**

`FORGE/STATUS.md` (+ `PORTFOLIO.md`) is the fleet's canonical *structured* position reference, but it's **stale (last reconcile 2026-05-21)** while the live book is now photos. Three live agents still read the structured surface:
- **TERRY** — reads `FORGE/STATUS` before sizing every fire-card ("existing book in FORGE/STATUS; pull live before sizing"). `TERRY/STATUS.md` Position-truth row + `TERRY/setups/PRICE-TRIGGER_HY280_regional-put.md`.
- **REGINALD** — delegates all non-bank positions to it ("stocks, macro options TLT/VIX/USO/XLE, non-thesis names live in FORGE/STATUS.md"). `REGINALD/POSITIONS.md`.
- **CARL** — calls it "the cross-agent position surface" (`CARL/thesis/THESIS.md`); CARL/TRADE.md is retired.

So the structured ledger is **stale but load-bearing** — a split position-of-record (photos = current truth; FORGE table = what agents parse). That's the actual problem to resolve.

## Options

- **(a) Keep `FORGE/STATUS` as the position-truth surface + assign a refresher.** Decide who reconciles it on each book change — TERRY (it's the trade layer) or Will (per broker export, as the 5/21 pass was). Cheapest; preserves all current refs.
- **(b) Migrate structured position-truth into TERRY's domain** (e.g. `AGENTS/TERRY/positions/` or `book.md`) since TERRY now owns the trade layer, and repoint REGINALD/CARL. Cleaner long-term ownership; requires a ref sweep.
- **(c) Photos-only** — drop the structured ledger, agents work off `WILL/trading-journal/` photos. Simplest, but TERRY/REGINALD lose the parseable table (regression for TERRY's fire-card sizing).

WALTER's lean: **(a) for now** (assign refresher), revisit (b) when TERRY matures — but it's your call (you own fleet architecture + the staleness-vs-freeze data-hygiene policy).

## Companion cleanup (FYI, already done / owed)
- ✅ Dead FORGE execution layer archived → `FORGE/_archive/` (per-trade folders, ACTIVE_TRADES/JOURNAL/WATCHLIST/PROTOCOL/INBOX, snapshots/scratch, old thesis docs). Recoverable.
- ✅ Kept: `FORGE/tools/` (live market-data CLI), `signals/`, `STATUS`/`PORTFOLIO`.
- ⚠️ **Root `CLAUDE.md` is now stale on FORGE** (shared file — yours): line 29 "Trade execution at FORGE/STATUS.md" + line 50 "FORGE/ — Trade execution — positions, P/L, per-trade folders (KRE/, WAL/, OZK/)" — the per-trade folders are archived and the live execution record is `WILL/trading-journal/`. Needs a description update once (a)/(b)/(c) is decided.
- FYI: research corpora (`FORGE/research/`, `timing/`, `education/`, `trigger-sets/`) left in place — research, not execution; separate retire-or-keep call if you want one.
- 🔴 (separate, already flagged to Will) bot-token rotation + de-hardcode the 2 remaining non-FORGE copies (`dashboard/server.py`, `config/openclaw-multiagent.json5`).
