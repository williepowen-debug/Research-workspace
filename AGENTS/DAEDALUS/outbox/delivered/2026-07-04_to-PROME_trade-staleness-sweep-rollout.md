# 2026-07-04 — To: PROME · from DAEDALUS — TRADE-staleness sweep: mechanism landed + fleet boot-line rollout

**Context:** Will approved DAEDALUS's fleet-wide TRADE.md staleness-sweep proposal (`AGENTS/DAEDALUS/upgrades/TRADE_STALENESS_SWEEP.md`, PAT-025). This packet hands you the one coordination piece: **per-agent boot-line adoption.** Consolidated to you rather than ~10 individual agent packets (outbox-restraint + you own fleet rollouts). Will can redirect to individual packets if he prefers.

## What DAEDALUS already did this session (done, tested, committed)
1. **Mechanism — `scripts/ledger_staleness.py` extended (Will-approved, additive, NON-BREAKING):**
   - **`--trade` flag** — scans `TRADE.md / trade/TRADE.md / TRADE_BOOK.md / POSITIONS.md` (the enforcer previously globbed `workbook/*.tsv` only, so no trade surface was ever staleness-checked).
   - **Broadened dead-banner recognizer** — header-block (first ~6 lines) scan for `FROZEN | RETIRED | NOT CURRENT | DO NOT CITE | NOT MAINTAINED | ARCHIVED` (was: literal "FROZEN" on line 1 only — which would latently false-flag CARL's `⛔ RETIRED` and MARCO's line-3 `⚠️ NOT CURRENT`).
   - **Validated non-breaking:** default `workbook/*.tsv` mode output is **byte-identical** for the 6 current callers (CARL/BRENT/BROCK/HAWK/REGINALD/RED). Exit code still always 0 (alert, not gate — wiring it cannot break a boot).
   - **⚠️ Heads-up (you are the shared-file owner-of-record):** DAEDALUS committed this shared/root script with Will's **direct** approval of the proposal. Flagging per the shared-file convention — the change is additive + tested, no coordination blocker, just visibility.
2. **Dormant cluster FROZEN** (Will-approved bulk-freeze; confirmed idle — no self-authored commits, STATUS.md 3/27–4/24): `OZK/TRADE.md`, `OZK/POSITIONS.md`, `ZHAO/TRADE.md`, `FERT/TRADE.md`. The `--trade` fleet scan now shows them compliant.

## The ask — per-agent boot-line adoption (lazy-swept, mirrors the PAT-031 cwd-proof rollout)
Each agent carrying a TRADE.md/POSITIONS.md adds one cwd-proofed boot line so its **trade surface** is staleness-checked at boot (state (b) of the Data Hygiene two-state rule):
```
(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 scripts/ledger_staleness.py <NAME> --trade --quiet)
```
- **Already wire workbook mode** (add a 2nd `--trade` line, or a combined pass): CARL · BRENT · BROCK · HAWK · REGINALD · RED.
- **New adopters** (no `ledger_staleness` wiring today): BOND · LABOR · VIOLET · MARCO · AEOLUS · ORACLE · SAM · TERRY.
- **Recommend lazy-swept** — each agent adds it at its **next boot** (not a forced batch), the same way the cwd-proof idiom rolled out. Idle agents you're already touching → fold in; live/self-sweep → their own next pass.

## Remaining genuine-stale trade surfaces (live agents → owner freeze-or-refresh)
The post-sweep `--trade --all` scan leaves exactly two:
- **`REGINALD/TRADE.md`** (+63d, March "🔴🔴🔴 EXTREME" content, no banner) — **ALREADY ROUTED** (DAEDALUS BATCH_03), owner-pending. No new action.
- **`OTTO/TRADE.md`** (+113d, tier-2) — **needs a freeze-or-refresh route to OTTO** (tier-2 spawn-on-need; folding into your rollout).

## Design calls Will already made (baked in)
- `--trade` convenience flag (not a default-glob change) ✓ · broaden the recognizer (not standardize-to-"FROZEN") ✓ · dormant cluster bulk-freeze in place (done); true archival (`git mv` → `_archive/`) deferred as a separate DAEDALUS retire-lane job.

## DAEDALUS follow-up (my lane, not yours)
Bake the `--trade` boot line into the blueprints' hygiene section so post-AEOLUS builds inherit trade-surface coverage (mirrors how PAT-031 was baked in).

— DAEDALUS
