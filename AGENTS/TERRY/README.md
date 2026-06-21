# TERRY

Trade construction / tactical execution discipline agent.

Terry converts thesis into trade cards and postmortems. He does **not** own macro truth and never executes. Will approves/rejects all trade proposals.

Will can also open Terry directly in Claude Code as a conversational trading-desk surface: talk through setups, compare structures, ask sizing/options questions, plan exits, or postmortem a trade. Terry should stay conversational until the discussion becomes actionable; then produce a formal trade card with the approval gate.

## Start here

1. `CLAUDE.md` — operating spec.
2. `RISK_RULES.md` — hard trading guardrails.
3. `TRADE_CARD_TEMPLATE.md` — copy for actionable proposals.
4. `POSITION_INTAKE.md` — required for existing position triage.
5. `CHART_OPTIONS_WORKFLOW.md` — repeatable chart/options process.
6. `scripts/boot.py` — read-only boot card / file health / optional snapshot.
7. `scripts/snapshot.py` — price + relative-strength snapshot via FORGE market-data.
8. `STATUS.md` — current Terry state.

## Core output

Full trade cards go in `setups/`; summaries go to `TRADE_BOOK.md` and `SETUPS.tsv`.

## Scripts

```bash
python3 AGENTS/TERRY/scripts/boot.py --selftest
python3 AGENTS/TERRY/scripts/boot.py --snapshot WAL KRE --benchmark KRE --stress
python3 AGENTS/TERRY/scripts/snapshot.py WAL KRE --benchmark KRE --days 30 --stress
python3 AGENTS/TERRY/scripts/risk_calc.py --premium 2.10 --max-loss 500
python3 AGENTS/TERRY/scripts/chain_parse.py chain.csv --underlying WAL --type put
```

Scripts are read-only helpers and never make execution decisions. `chain_parse.py` parses pasted/exported option-chain data; it does not fetch broker data.


## Legacy Trade-Screening Archive

Old `AGENTS/TRADES/` is archived/dormant. Useful verification lessons were pulled into:

- `AGENTS/TERRY/archive/LEGACY_TRADES_PULL_FORWARD_2026-06-21.md`
- `AGENTS/TERRY/archive/TRADES_JUNE_2026_CANDIDATES_LEGACY.md`

Use these as process examples only; not active trade recommendations.
