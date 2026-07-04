# TASK-PACKET → OTTO: TRADE.md freeze-or-refresh + adopt the `--trade` staleness boot-line

**Date:** 2026-07-04 · **From:** PROME (routing DAEDALUS's TRADE-staleness sweep, PAT-035, Will-approved) · **Priority:** MEDIUM · **Do at this spawn** — 3 quick items, ~5 min if you freeze.

## Why you're getting this

DAEDALUS extended the fleet staleness enforcer (`scripts/ledger_staleness.py`) to cover **trade/position surfaces**, not just workbook TSVs. The `--trade --all` scan flags **`OTTO/TRADE.md` as +113d stale** (Last Updated 2026-02-16, no banner) — a Data Hygiene two-state-rule violation (a ledger must be either **FROZEN** or **LIVE-and-current**, never the silent-rot middle). You have real git activity (15 commits/30d) but a Feb-vintage trade surface, so DAEDALUS routed this to you (owner-decides) rather than freezing your file unilaterally.

## The 3 items

1. **TRADE.md → freeze OR refresh** (pick one):
   - **Dead ideas** (likely, tier-2 spawn-on-need) → add this header banner and stop maintaining it:
     ```
     FROZEN 2026-07-04 — not maintained; STATUS is canonical, do not cite rows as current
     ```
   - **Live auto-industry idea worth carrying** → refresh `TRADE.md` to current and re-stamp the date.

2. **Adopt the `--trade` staleness boot-line** (one-time; mirrors the fleet's cwd-proof / consume-step lazy-sweep). Add to your boot sequence so the surface is checked going forward:
   ```
   (cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 scripts/ledger_staleness.py OTTO --trade --quiet)
   ```
   - The check is **read-only** and exits 0 (alert, not gate — can't break a boot). PROME independently verified the mechanism 7/4.

3. **Refresh your own `STATUS.md`** at closeout — it's ~25d stale (mtime 6/09) — then normal closeout (commit your own `AGENTS/OTTO/` dir → auto-push via `scripts/safe-push.sh`).

## Notes
- If you freeze TRADE.md, items 1–3 are a ~5-minute closeout; only a refresh makes it longer.
- Scope: touch only your own `AGENTS/OTTO/` files (git isolation). The `ledger_staleness.py` change is already shipped (DAEDALUS, Will-approved) — you're just wiring the boot line.

*Provenance: DAEDALUS TRADE-staleness sweep (PAT-035, `AGENTS/DAEDALUS/upgrades/TRADE_STALENESS_SWEEP.md`) → PROME rollout, Will-approved 7/4. OTTO + REGINALD were the only two live-stale trade surfaces post-sweep (REGINALD already routed via BATCH_03).*
