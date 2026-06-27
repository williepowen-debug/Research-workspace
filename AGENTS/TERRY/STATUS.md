# TERRY STATUS
**Updated:** 2026-06-27 (boot truth-up: 6/26 toolchain confirmed committed+pushed; logged 7 WALTER INFO signals to new `SIGNALS.tsv` ledger) · **Status:** 🟡 armed — fire-card toolchain built & tested, 0 cards fired live, waiting on a trigger
**Agent:** TERRY — trade construction / tactical execution discipline. Owns the ACTION/card side; never executes. Detection = LIQUID/SENTRY.

> Durable mandate + lessons → `MEMORY.md`. Session-end procedure → `CLOSEOUT.md`. Role/start-here → `README.md`. Risk gates → `RISK_SCORING.md`.

## Live state

**Standing rules (Will 2026-06-26):** fresh capital deploys ONLY on a fired trigger (no mechanical reshape; dry powder). **Max loss = $500 per card.**

| Capability | State | Note |
|---|---|---|
| Trigger→card toolchain | 🟢 BUILT & TESTED | the minutes-not-hours path is live end-to-end |
| `scripts/chain_fetch.py` | 🟢 built, selftest PASS, live-validated | live option-chain CLI; marks matched the bank-put proposal exactly |
| `scripts/grade_print.py` + `grade_config.json` | 🟢 built, selftest PASS | Q2 print grader; 3 mis-grade traps as hard guards; `--tally` rolls path (a)/(b)/(c) |
| Fire cards | 🟢 staged, **0 fired live** | `TRADE_CARD_TEMPLATE_FIRE.md` + 2 pre-filled skeletons (HY≥280 / WAL-EGBN), $500 budget locked |
| Day-trading review loop | 🟢 live | `daytrading/` — Session 2 logged 6/24 (+$2,951.67 realized); read `daytrading/README.md` first |
| Older scripts | 🟢 selftested | boot.py, snapshot.py, risk_calc.py, chain_parse.py, csv_pnl.py |
| Live thesis trade cards | ⚪ none fired | fire cards await a real trigger; POSTMORTEMS template-only (no closed trade yet) |
| Position truth | 🟡 from Will/FORGE only | existing book in FORGE/STATUS; pull live before any fire-card sizing |
| Risk unit for Will | 🟡 open | $/%/R preference unresolved (see MEMORY Standing Decisions) |

## What's pending
- **6/26 toolchain landed** — committed (`1fa1ca23` tooling + `d9498dfd` durable layer) and swept to origin by WALTER's push-train; synced 0/0. No push pending.
- **Awaiting a fired trigger** to exercise a fire card (HY OAS ≥280 sustained, or a Jul 16–30 print grading as transmission).
- **Positioning backdrop (current read):** crowded-long / froth → squeeze risk **elevated on any short**. Evidence + decay tracked in `SIGNALS.tsv` (boot surfaces it; don't re-list rows here). Durable level map worth keeping in front: GS-CTA SPX **7,352 / 7,063 / 6,642** — mechanical-sell window opens <7,352.

## Open questions for Will
- Preferred default risk unit: $ max loss / % portfolio / R?
- Track every considered setup, or approved/rejected only?

## Guardrails
- No execution; Will approval on every trade. No stale prices/option marks in cards (pull live at fire). No position triage without broker/Will truth. No macro re-underwriting — cite the thesis owner.
