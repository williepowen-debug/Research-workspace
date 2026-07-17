# TERRY

Trade construction / tactical execution discipline agent.

Terry converts thesis into trade cards and postmortems. He does **not** own macro truth and never executes. Will approves/rejects all trade proposals.

Will can also open Terry directly in Claude Code as a conversational trading-desk surface: talk through setups, compare structures, ask sizing/options questions, plan exits, or postmortem a trade. Terry should stay conversational until the discussion becomes actionable; then produce a formal trade card with the approval gate.

## Start here

1. `CLAUDE.md` — operating spec.
2. `RISK_RULES.md` — hard trading guardrails.
3. `RISK_SCORING.md` — pre-trade risk gates, edge scoring, fractional Kelly reference, calibration/Brier tracking, execution-block checklist.
4. `TRADE_CARD_TEMPLATE.md` — copy for actionable proposals.
5. `POSITION_INTAKE.md` — required for existing position triage.
6. `CHART_OPTIONS_WORKFLOW.md` — repeatable chart/options process.
7. `scripts/boot.py` — read-only boot card / file health / optional snapshot.
8. `scripts/snapshot.py` — price + relative-strength snapshot via FORGE market-data.
9. `STATUS.md` — current live Terry state.
10. `MEMORY.md` — durable mandate + accrued lessons/decisions (lean cross-session layer).
11. `CLOSEOUT.md` — session-end write-back protocol (tiered).

## Fire-ready execution (trigger → card in minutes)

- `setups/FIRE_CARDS_LADDER.md` — **side-by-side index of all staged fire cards** (comparison table + July print calendar + monoline→regional gate link). Start here for the fire-card overview.
- `TRADE_CARD_TEMPLATE_FIRE.md` — single default card; only the LIVE-MARKS block is filled at fire.
- `setups/PRICE-TRIGGER_HY280_regional-put.md`, `setups/PRINT-TRIGGER_WAL-EGBN-build.md`, `setups/PRINT-TRIGGER_monoline-COF-SYF-ALLY.md` — pre-filled trigger skeletons ($500/card).
- `scripts/chain_fetch.py` — live option-chain CLI (rule #4; never cite stored option marks).
- `scripts/grade_print.py` + `grade_config.json` — Q2 bank-print grader; paths a/b/c (regional) + **m (monoline un-mask)**; `--tally` rolls path diagnostics.

## Trade-construction context ledger (decay-tracked)

`SIGNALS.tsv` — durable home for any input that shapes how I time/size/structure a trade *without being the thesis itself*. The `source` column spans:
- **WALTER** — routed positioning/timing INFO signals.
- **TERRY-chart** — my own observations: key levels, IV percentile, expected move, vol/tape reads (use a local id like `TERRY-CHART-YYYYMMDD-NN`).
- **thesis-owner timing notes** — REGINALD/CARL/LIQUID/SAM/etc.'s *timing/structure scaffolding* (print dates, repricing lags, detection triggers), never their thesis truth.

Each row: `source` · `as_of` · `decay` · `conf` · `status` (PIN / LIVE / LIVE-WEAK / DECAYING / PARKED / RETIRED) · `bears_on` · `key_level` · `ref`.

- **PIN** = the NEXUS regime denominator — one pinned row (risk-on/off, vol, bull/bear) that conditions every timing read; *refreshed, not streamed*. `boot.py` surfaces it first and flags it UNSET/stale.
- `boot.py` surfaces PIN + active rows and flags any active row past 21d for re-verify/retire (anti-rot).
- **Out of scope (don't duplicate here):** thesis truth (owned by domain agents/NEXUS — reference, don't copy) and the raw event/catalyst calendar.
- **STATUS holds only the one-line current read + pointer — evidence rows live here, not in STATUS.**

New context → add a row; recall the cluster at fire-time when sizing a card.

## Core output

Full trade cards go in `setups/`; summaries go to `TRADE_BOOK.md` and `SETUPS.tsv`.

Before any actionable proposal, apply `RISK_SCORING.md`: define edge, max loss, invalidation, liquidity, event risk, and execution block. Kelly is a capped sizing reference only, never an instruction.

## Scripts

**Run from the repo root (PAT-031).** Paths are root-relative; TERRY launches from `AGENTS/TERRY/`, so a bare `python3 AGENTS/TERRY/scripts/…` resolves to `AGENTS/TERRY/AGENTS/TERRY/…` and fails. Either `cd "$(git rev-parse --show-toplevel)"` once per shell, or wrap each call as shown:

```bash
cd "$(git rev-parse --show-toplevel)"   # do this once, then:
python3 AGENTS/TERRY/scripts/boot.py --selftest
python3 AGENTS/TERRY/scripts/boot.py --snapshot WAL KRE --benchmark KRE --stress
python3 AGENTS/TERRY/scripts/snapshot.py WAL KRE --benchmark KRE --days 30 --stress
python3 AGENTS/TERRY/scripts/risk_calc.py --premium 2.10 --max-loss 500
python3 AGENTS/TERRY/scripts/chain_parse.py chain.csv --underlying WAL --type put

# …or one-shot, cwd-independent:
(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/boot.py)
```

Scripts are read-only helpers and never make execution decisions. `chain_parse.py` parses pasted/exported option-chain data; it does not fetch broker data.


## Legacy Trade-Screening Archive

Old `AGENTS/TRADES/` is archived/dormant. Useful verification lessons were pulled into:

- `AGENTS/TERRY/archive/LEGACY_TRADES_PULL_FORWARD_2026-06-21.md`
- `AGENTS/TERRY/archive/TRADES_JUNE_2026_CANDIDATES_LEGACY.md`

Use these as process examples only; not active trade recommendations.
