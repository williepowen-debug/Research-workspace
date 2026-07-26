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

## 6. Risk / scoring

### 6a. EFFECTIVE-N — independence audit (MANDATORY; complete before sizing)
> *Size to what is genuinely independent, not to how many reasons you can list. Adopted 2026-07-26 (Will-approved) — see `research/SIGNAL_COMBINATION_2026-07-26.md` SC-03.*

| Field | Entry |
|---|---|
| **Claimed corroborating legs (N_claimed)** | [how many separate reasons/positions support this] |
| **Shared antecedent(s)** | [the ONE event/fact that would kill more than one leg at once — name it, or write "none found"] |
| **EFFECTIVE N (N_eff)** | [the honest independent count + one line of reasoning] |
| **Sizing reference** | **size to N_eff, never to N_claimed** |

- If **N_eff = 1**, say so plainly and size as a single view — however many legs are listed.
- If `N_claimed > N_eff` and the sizing does not reflect the gap, **that is the finding** — flag it before Will sees the card.
- Applies to *book* independence too: does this card share a falsifier with a position already on?

- **Risk unit / max loss budget:** [$ / % / R]
- **Edge estimate:** [qualitative or quantified; if probability-style, p_model vs p_market]
- **Kelly reference:** [if applicable; **0.25× cap or lower, never full Kelly** — and never the `f×(1−CV)` variant, which is looser (SC-05, REJECTED)]
- **Sizing proposal:** [contracts/shares/notional; conditional if portfolio unknown] — **must be consistent with N_eff above**
- **Invalidation:** [price / thesis / time]
- **Stop / hedge / exit rule:** [mechanical rule]
- **Gap/event risk:** [known failure mode]
- **Liquidity / spread check:** [acceptable / conditional / blocks trade]
- **Execution block:** [what must be true before Will could act]

## 7. Target / management
- **Target 1:** [level / % / event]
- **Target 2:** [optional]
- **Partial exits:** [rule]
- **Roll rule:** [only if pre-defined]
- **Time stop:** [date / catalyst miss]
- **Review cadence:** [daily/weekly/event-driven]

## 8. Why not / counter-trade
[Best reason this is bad timing or bad structure. Include `NO TRADE` reason if edge, liquidity, timing, or invalidation is insufficient.]

## 8b. Calibration note, if probability-style
- **Forecast:** [p_model or subjective probability]
- **Market-implied probability:** [if applicable]
- **Outcome to score later:** [binary/resolution criteria]
- **Future Brier row needed?** [yes/no]

## 9. Decision
- [ ] APPROVE
- [ ] REJECT
- [ ] REWORK with changes: [what]

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
```
