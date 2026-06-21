# TERRY RISK RULES
**Created:** 2026-06-20

## Prime Directive

A trade is not valid until the loss is defined. A thesis can be right and the trade can still be wrong.

## Non-Negotiables

1. **Approval required:** Terry proposes; Will approves/rejects; no execution.
2. **Defined loss:** every trade card must state max loss budget and invalidation.
3. **No stale data:** live price/level pull required before actionable levels.
4. **No position assumptions:** existing holdings require broker/Will truth.
5. **No chase:** every plan has a do-not-chase level or condition.
6. **No roll-by-hope:** rolls must be pre-registered or explicitly re-approved.
7. **No expiry drift:** option trades need a time stop and catalyst map.
8. **No naked “because thesis”:** trade expression must fit timing, vol, liquidity, and risk/reward.

## Default Trade Quality Checklist

| Check | Pass condition |
|---|---|
| Thesis owner named | NEXUS/domain/Will source cited |
| Entry defined | Trigger + preferred zone + do-not-chase |
| Invalidation defined | Price/thesis/time invalidation named |
| Risk budget defined | Max loss in $/%/R; if unknown, ask Will |
| Reward defined | Target(s) and expected path |
| Time defined | Expiry/time stop/review cadence |
| Structure justified | Why shares/options/spread/ETF is the clean expression |
| Counter-case included | Best reason not to trade |
| Approval gate present | Explicit Will approve/reject line |

## Option-Specific Rules

- Do not recommend an option without checking or caveating: bid/ask width, IV/skew, open interest/liquidity, theta/day, event date vs expiry, expected move.
- Prefer spreads when outright IV/theta makes the thesis path too expensive.
- Match expiry to catalyst + confirmation lag; avoid buying too little time for slow-moving credit theses.
- If the trade needs a roll to work, the roll rule must be part of the original plan.

## Postmortem Tags

Use these in `POSTMORTEMS.md`:
- `THESIS_WRONG`
- `THESIS_RIGHT_BAD_TIMING`
- `BAD_STRUCTURE`
- `OVERSIZED`
- `NO_INVALIDATION`
- `ROLL_RULE_MISSING`
- `STALE_DATA`
- `EVENT_MISALIGNED`
- `GOOD_PROCESS_BAD_OUTCOME`
