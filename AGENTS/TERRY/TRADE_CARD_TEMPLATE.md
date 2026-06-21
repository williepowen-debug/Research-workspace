# TRADE CARD TEMPLATE

Copy this into `setups/YYYY-MM-DD_<ticker>_<structure>.md` for every actionable setup.

```markdown
# TRADE CARD — [Ticker / Instrument] — [Direction / Structure]
**Date:** YYYY-MM-DD
**Setup ID:** TRY-XXX
**Thesis owner:** [NEXUS / domain agent / Will]
**Thesis reference:** [file/path + date, or Will prompt]
**Terry verdict:** [CLEAN / CONDITIONAL / BAD STRUCTURE / NO TRADE]
**Confidence in trade structure:** High/Medium/Low
**Data freshness:** [prices as-of; option chain as-of; broker position truth as-of]

## 0. Missing inputs / hard caveats
- [ ] Live price checked
- [ ] Option chain checked OR marked conditional
- [ ] Existing position truth checked OR `[POSITION_STATE_UNKNOWN]`
- [ ] Catalyst dates checked
- [ ] Thesis owner current enough

## 1. One-line setup
[What this trade is trying to express, in trader language.]

## 2. Preconditions
- **Thesis precondition:** [what must be true]
- **Tape precondition:** [price/level/trend/vol/liquidity requirement]
- **Catalyst precondition:** [event/date/confirmation requirement]
- **Do NOT trade if:** [conditions that block]

## 3. Chart / tape read
| Item | Read |
|---|---|
| Current price | [value + as-of] |
| Trend | [up/down/range; daily/weekly] |
| Key support | [levels] |
| Key resistance | [levels] |
| Relative strength | [vs SPY/KRE/HYG/etc.] |
| Vol / gap risk | [VIX/IV/event gaps] |
| Liquidity | [volume / bid-ask / option OI if known] |

## 4. Entry
- **Trigger:** [price/close/level/event]
- **Preferred entry zone:** [range]
- **Do not chase:** [level/condition]
- **If missed:** [wait/reprice/no trade]

## 5. Structure
- **Instrument:** [stock/ETF/options/spread]
- **Expiry / tenor:** [date/window]
- **Strike / spread:** [if options]
- **Alternatives considered:** [shares vs options vs spreads]
- **Why this expression:** [risk/reward/timing/liquidity]

## 6. Risk
- **Risk unit / max loss budget:** [$ / % / R]
- **Sizing proposal:** [contracts/shares/notional; conditional if portfolio unknown]
- **Invalidation:** [price / thesis / time]
- **Stop / hedge / exit rule:** [mechanical rule]
- **Gap/event risk:** [known failure mode]

## 7. Target / management
- **Target 1:** [level / % / event]
- **Target 2:** [optional]
- **Partial exits:** [rule]
- **Roll rule:** [only if pre-defined]
- **Time stop:** [date / catalyst miss]
- **Review cadence:** [daily/weekly/event-driven]

## 8. Why not / counter-trade
[Best reason this is bad timing or bad structure.]

## 9. Decision
- [ ] APPROVE
- [ ] REJECT
- [ ] REWORK with changes: [what]

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
```
