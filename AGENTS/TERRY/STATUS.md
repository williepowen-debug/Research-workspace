# TERRY STATUS
**Updated:** 2026-06-20 (Claude Code conversational surface clarified)
**Agent:** TERRY — trade construction / tactical execution discipline

## Mission

TERRY converts thesis into trade plans with explicit entry, invalidation, sizing, expiry/time stop, target, roll/no-roll rules, and approval gates. Terry does **not** own macro truth and never executes trades.

## Current State

| Area | Status | Note |
|---|---|---|
| Agent scaffold | ✅ created | `CLAUDE.md`, risk rules, trade book, setup tracker, postmortems seeded. |
| Templates/workflows | ✅ added | Trade-card template, position-intake form, and chart/options workflow are now explicit. |
| Scripts/tool access | ✅ added | `boot.py` read-only boot card; `snapshot.py` price/relative-strength; `risk_calc.py` sizing math; `chain_parse.py` pasted chain parser. |
| Live trade cards | None | No setups reviewed yet. |
| Position truth | Unknown | Existing broker/fill/P&L state must come from Will via `POSITION_INTAKE.md` fields before firm triage. |
| Data access | Conditional | Live prices/history via FORGE market-data wrappers; option chains require Will/broker/manual export then `chain_parse.py`. |
| Claude Code surface | ✅ clarified | Will can open Terry directly for conversational trade-desk questions; full trade cards only when actionable. |

## First Useful Tasks

1. **Postmortem old scars:** HYG Jun→Dec roll failure; TLT/FXY/HYG expiry cleanup if Will provides position truth.
2. **Build a live trade-card template on the next actionable thesis:** e.g., HY kill-line / Hormuz tape / WAL-OZK idiosyncratic bank setup.
3. **Define default risk budget conventions:** max loss per idea, max theta bleed, event-risk sizing, no-chase rules.
4. **First live dry run:** produce one conditional Terry card from an existing thesis without executing, using `snapshot.py` for levels, `risk_calc.py` for sizing, and `chain_parse.py` if Will provides option-chain data.

## Open Questions for Will

- Preferred default risk unit: dollar max loss, % portfolio, or “R” unit?
- Should Terry track approved/rejected proposals only, or also every considered setup?
- Preferred chart horizon defaults: daily/weekly for swing trades, intraday only when explicitly requested?

## Guardrails

- No execution; approval required for every trade.
- No stale prices/levels in actionable cards.
- No position triage without broker/Will truth.
- No macro re-underwriting unless asked; cite thesis owner.
