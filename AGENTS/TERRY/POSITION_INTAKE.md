# POSITION INTAKE — Required for Existing Position Triage

Terry cannot triage an existing position from memory. Fill or paste enough broker truth to answer the fields below.

## Required Fields

| Field | Value |
|---|---|
| Ticker / instrument |  |
| Direction | Long / short / options / spread |
| Quantity / contracts |  |
| Entry price / debit / credit |  |
| Current mark |  |
| Expiry |  |
| Strike(s) |  |
| Current P/L |  |
| Original thesis / source |  |
| Original invalidation, if any |  |
| Upcoming catalyst(s) |  |
| Will's desired action | hold / add / trim / exit / roll / unsure |
| Max additional loss tolerated |  |

## If Any Required Field Is Missing

Terry may give a **conditional** read, but must label it `[POSITION_STATE_INCOMPLETE]` and must not recommend execution. Missing position truth can turn a good roll into hidden over-sizing or accidental doubling-down.

## Existing Position Output

Use a normal trade card, but set:
- **Terry verdict:** `HOLD / TRIM / EXIT / ROLL / ADD / NO ACTION — CONDITIONAL`
- **Data freshness:** include broker truth timestamp
- **Risk:** include current loss if stopped now and max additional loss if held/rolled
