# FIRE-READY TRADE CARD TEMPLATE

**Purpose:** collapse "trigger fires → Approve-ready card in hand" from hours to minutes.
Standing rule (Will 6/26): **fresh capital deploys ONLY on a fired trigger**, then we move fast.

This is the *shape*. Each live trigger gets a pre-filled instance in `setups/`
(see `setups/PRICE-TRIGGER_*.md`, `setups/PRINT-TRIGGER_*.md`) with **ZONE 1 already
written**. At fire-time you fill **only ZONE 2** (LIVE MARKS), then present ZONE 3.

> Single default card — NOT a V1/V2/V3 menu. If an alternative structure matters,
> name it once in ZONE 1 "alternatives rejected" and move on.

---

```markdown
# FIRE CARD — [Ticker / Instrument] — [Direction / Structure]
**Setup ID:** TRY-FIRE-XXX · **Trigger class:** PRICE | PRINT
**Thesis owner:** [agent + file] · **Card pre-built:** YYYY-MM-DD · **Fired:** ____ (fill at fire)

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (written in advance; do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Trigger condition (exact):** [the level/event that arms this card — owned by LIQUID/SENTRY]
- **One-line setup:** [what this expresses, trader language]
- **Structure:** [instrument · expiry · strike ladder] — pre-chosen
- **Why this expression:** [duration/convexity/liquidity rationale]
- **Alternatives rejected:** [one line — e.g. "equity put bleeds theta; spread caps convexity"]
- **Max-loss budget:** $500 per card (set by Will 2026-06-26)
- **Invalidation (thesis/price/time):** [what proves it wrong]
- **Kill line:** [the level/event that says STOP]
- **Confirm line:** [the corroborator that says GO bigger / hold]

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (the ONLY block to fill at fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Trigger-level confirm:** [HY OAS ___ / 10Y ___ / print metric ___] — DID IT ACTUALLY HIT? [Y/N]
- **Spot(s):** [from `fetch.py price …`] — as-of ____
- **Green/red day check (rule #6):** [puts on green ✓ / calls on red ✓ / breaking & why]
- **Chain marks:** [from `chain_fetch.py TICKER EXPIRY --type put --no-cache`]
  | Strike | Mark | Spread% | IV% | OI | Moneyness% |
  |---|---|---|---|---|---|
  | | | | | | |
- **Liquidity OK?** [spread/OI acceptable per chain flags — Y/N]
- **Broker position truth:** [existing exposure? POSITION_INTAKE or `[POSITION_STATE_UNKNOWN]`]
- **Sizing (from `risk_calc.py --premium <mark> --max-loss <budget>`):** [contracts/notional]

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] Trigger actually fired (ZONE 2 confirm = Y) — not a near-miss
- [ ] Live marks pulled (prices + chain, < 15 min old)
- [ ] Green/red rule satisfied or break justified
- [ ] Liquidity acceptable
- [ ] Max loss ≤ budget; sizing computed
- [ ] Position truth known (or flagged unknown)

**Terry verdict:** CLEAN / CONDITIONAL / NO TRADE
**Decision:**  [ ] APPROVE   [ ] REJECT   [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
```

---

## Fire runbook (the 3 commands behind ZONE 2)
```
1. python3 FORGE/tools/market-data/fetch.py price <TICKER> --json          # spot + trigger-level context
2. python3 AGENTS/TERRY/scripts/chain_fetch.py <TICKER> <EXPIRY> --type put --no-cache
3. python3 AGENTS/TERRY/scripts/risk_calc.py --premium <mark> --max-loss <budget>
```
Paste outputs into ZONE 2, tick ZONE 3, present. Target: minutes.
