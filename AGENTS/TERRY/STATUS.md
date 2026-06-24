# TERRY STATUS
**Updated:** 2026-06-23 (day-trading review system added; Session 1 logged)
**Agent:** TERRY — trade construction / tactical execution discipline

## Mission

TERRY converts thesis into trade plans with explicit entry, invalidation, sizing, expiry/time stop, target, roll/no-roll rules, and approval gates. Terry does **not** own macro truth and never executes trades.

## Current State

| Area | Status | Note |
|---|---|---|
| Agent scaffold | ✅ created | `CLAUDE.md`, risk rules, trade book, setup tracker, postmortems seeded. |
| Templates/workflows | ✅ added | Trade-card template, position-intake form, chart/options workflow, and risk-scoring/calibration module are now explicit. |
| Scripts/tool access | ✅ added | `boot.py` read-only boot card; `snapshot.py` price/relative-strength; `risk_calc.py` sizing math; `chain_parse.py` pasted chain parser. |
| Live trade cards | None | No thesis-trade setups reviewed yet. |
| Day-trading review | ✅ live | `daytrading/` — recurring feedback loop on Will's discretionary day-trading. Rulebook `PROFILE.md` (5 rules), `JOURNAL.md` (narrative), `LEDGER.tsv` (trend metrics). **Session 1 (6/16–6/23) logged 6/23.** On boot, if reviewing day-trades, read `daytrading/README.md` first. |
| Legacy TRADES archive | ✅ absorbed | Old `AGENTS/TRADES/JUNE_2026_CANDIDATES.md` preserved as TERRY archive/playbook; TRADES is dormant. |
| Risk scoring | ✅ added | `RISK_SCORING.md` covers pre-trade risk gates, edge scoring, fractional Kelly reference, Brier calibration, and loss taxonomy. |
| Position truth | Unknown | Existing broker/fill/P&L state must come from Will via `POSITION_INTAKE.md` fields before firm triage. |
| Data access | Conditional | Live prices/history via FORGE market-data wrappers; option chains require Will/broker/manual export then `chain_parse.py`. |
| Claude Code surface | ✅ clarified | Will can open Terry directly for conversational trade-desk questions; full trade cards only when actionable. |

## First Useful Tasks

1. **Postmortem old scars:** HYG Jun→Dec roll failure; TLT/FXY/HYG expiry cleanup if Will provides position truth.
2. **Use legacy TRADES verification pattern:** candidate idea → primary-source check → aggregate check → trend check → no-trade or trade-card decision.
2. **Build a live trade-card template on the next actionable thesis:** e.g., HY kill-line / Hormuz tape / WAL-OZK idiosyncratic bank setup.
3. **Define Will-specific default risk budget conventions:** max loss per idea, max theta bleed, event-risk sizing, no-chase rules. `RISK_SCORING.md` now provides the framework; Will still needs to choose preferred risk unit.
4. **First live dry run:** produce one conditional Terry card from an existing thesis without executing, using `snapshot.py` for levels, `risk_calc.py` for sizing, and `chain_parse.py` if Will provides option-chain data.

## Open Questions for Will

- Preferred default risk unit: dollar max loss, % portfolio, or “R” unit?
- Should TERRY use 0.25x Kelly as the default ceiling for probability-style setups, or an even lower cap unless Will overrides?
- Should Terry track approved/rejected proposals only, or also every considered setup?
- Preferred chart horizon defaults: daily/weekly for swing trades, intraday only when explicitly requested?

## Guardrails

- No execution; approval required for every trade.
- No stale prices/levels in actionable cards.
- No position triage without broker/Will truth.
- No macro re-underwriting unless asked; cite thesis owner.
