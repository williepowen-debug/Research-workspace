# TERRY Paper-Book — DESIGN STUB (backlog, not built)
**Status:** 💡 BACKLOG — Will's idea 2026-07-17, TERRY endorsed. **Not built. Do not act without Will's go.**
**Problem it solves:** PAT-028 — 0 cards fired live → 0 track record → the card product is un-instrumentable. The only "product" so far is the *refusals* (005 gate, book-aware NO-ADD). A paper book manufactures a falsifiable track record without capital risk, and finally gives `RISK_SCORING.md` §5 (calibration/Brier) something to score. Measures **process calibration** (structure / timing / sizing / prioritization) — NOT behavioral/execution edge.

## The core insight — "salary" = opportunity cost
A **fixed/salaried** bankroll (not unlimited paper money) is the key. Infinite paper money only tests per-trade accuracy ("how often right"); a **limited/salaried** book forces *choosing* which setups get paper capital → tests **prioritization judgment** (is 004 worth it over the builder card?), which is the more valuable feedback and mirrors the real tranche-by-tranche capital constraint.

## The 3 failure modes that would make the data LIE (design around all three)
1. **Fill fidelity (THE make-or-break).** Paper fills at mid are fantasy — for a long-premium options book the bid/ask + slippage is a huge chunk of real P&L (DHI front-week spreads ran 50-200%). **RULE: fill buys at the ASK, sells at the BID** (or a penalized mid). Mid-fills systematically flatter and teach the wrong lessons.
2. **Discipline decoupling.** Free paper-trading drifts into setups I'd never propose live → the record becomes a *looser* strategy than the real one, useless for transfer. **RULE: the paper book trades the SAME rules** — same triggers, same $500/card, same approval proxy.
3. **Logging survivorship.** Losers get quietly forgotten → the record flatters itself. **RULE: every paper position logged with entry mark / thesis / invalidation + mark-to-market on a boot cadence** (same staleness discipline as the ledgers; a paper book that isn't marked rots).

## Recommended shape (start narrow, expand only if it earns it)
- **Phase 1 — SHADOW BOOK (the rigorous core).** Every card that reaches *would-fire* state (Will approves, OR it hits its trigger) gets a realistic paper fill and is tracked to close. Purest signal: it's the actual live strategy with paper money, adds no new decisions, can't corrupt the live discipline. Answers "do TERRY's proposed trades work?"
- **Phase 2 — SALARIED DESK (optional).** Notional bankroll (e.g. $10k, or a monthly "salary" tranche), prioritization, running equity curve. More volume + tests prioritization, but clearly labeled SEPARATE and bound by the same-rules guardrail.

## Tooling (mostly exists)
`PAPER_BOOK.tsv` (entry/mark/thesis/invalidation/close) + boot-time mark of open positions (like the ledger-staleness alerts) + monthly review. Reuse: `snapshot.py`/`chain_fetch.py` (marks), `csv_pnl.py` (P&L), the `SETUPS.tsv`/INDEX pattern.

## Standing guardrails
- **Subordinate to the thesis work** (same rule as the day-trading loop) — never displaces core construction.
- **Never an argument for looser real deployment** — it calibrates process, it is not a license to size up. Keep it clearly labeled PAPER.
- Feeds: calibration/Brier rows · structure validation (spreads vs outrights; does the crash-tail actually pay?) · entry-timing validation (does the green-day rule improve fills?) · post-print-vs-pre-print (builder card) · partially lifts the PAT-028 no-track-record ceiling.

## Open questions for Will (when we build it)
- Bankroll size / salary cadence (lump $10k vs monthly tranche)?
- Shadow-book only (phase 1) or straight to the salaried desk?
- Auto-fill on trigger, or only on Will-approved cards (keeps it tied to the real approval gate)?
