# Architecture Peer-Review — LIQUID vs TERRY
**2026-06-26 · read-only · reviewer: LIQUID · rubric-ordered**

## 1. DIR LAYOUT
**LIQUID:** STATUS, MEMORY, IDENTITY, CLAUDE, CLOSEOUT, STRATEGY, CALENDAR, CREDIT_THRESHOLDS + `thesis/` (THESIS/CHANGELOG/TIMELINE), `workbook/` (KB.tsv + CATALYSTS/PREDICTIONS/FLOW/VX TSVs + framework .md), `scripts/`, `inbox`+`outbox` (with processed/delivered), `domain/sources`, `.gitignore`. **Missing:** README, SYSTEM/BOOT.
**TERRY:** STATUS, README, CLAUDE, RISK_RULES/RISK_SCORING, TRADE_BOOK, TRADE_CARD_TEMPLATE(+FIRE), POSITION_INTAKE, POSTMORTEMS, SETUPS.tsv, grade_config.json + `scripts/`, `setups/`, `postmortems/`, `charts/`, `daytrading/` (own README/JOURNAL/LEDGER/PROFILE), inbox/outbox, `.gitignore`. **Missing:** MEMORY, CLOSEOUT, IDENTITY, KB.
Both have scripts/, inbox/outbox, .gitignore. Complementary gaps: LIQUID lacks README/self-map; TERRY lacks MEMORY/KB/CLOSEOUT.

## 2. BOOT/CLOSEOUT
Both ship a real `boot.py` (read-only health card). LIQUID's is richer (3-dashboard live FRED+yf sweep, catalyst/prediction due-scan, `--selftest/--quick/--verbose`). TERRY's boot validates a REQUIRED-file manifest + open setups + optional snapshot. **LIQUID has a dedicated CLOSEOUT.md** (write-back protocol); **TERRY has none** — closeout cadence lives implicitly in CLAUDE.md + daytrading JOURNAL. LIQUID = explicit boot↔closeout loop; TERRY = boot strong, closeout informal.

## 3. STATE-FILE HYGIENE
LIQUID: structured **KB.tsv (13-col, 64 rows, ID-validated in selftest)** — strong. BUT **STATUS.md is 28KB** with a massive single-bold-paragraph header stuffed with live numbers (HY/CCC/SOFR/VIX) — readability + staleness risk (state files shouldn't carry quotes). MEMORY.md 19KB, single file, no durable/session split — growing. Runtime gitignore ✅ (`alerts/`).
TERRY: STATUS lean (3.7KB) ✅; `.gitkeep` placeholders keep empty dirs in git (cleaner than LIQUID's bare `domain/sources`); runtime gitignore ✅ (`scripts/.cache/`, `grades/`). No KB — POSTMORTEMS substitutes but unstructured. SETUPS.tsv tiny (261B) vs richer `setups/*.md`.
Both fresh (LIQUID 6/25, TERRY 6/24).

## 4. SCRIPTS/TOOLING
TERRY broader: 7 scripts (boot, snapshot, chain_fetch/parse, risk_calc, csv_pnl, grade_print) — **all carry selftests**. LIQUID: 2 (boot.py w/ selftest; hy_oas_watch.py new P1b, systemd-timed, no selftest — minor, ~120 lines). LIQUID deeper per-tool; TERRY wider coverage + uniform selftest discipline.

## 5. SELF-DOCUMENTATION
TERRY **wins**: README is a numbered "start here" map + crisp mandate; mission restated in STATUS. LIQUID has no README/SYSTEM — mandate split across IDENTITY.md (role) + CLAUDE.md (15KB spec); a cold reader lacks a single entry map.

## 6. NAMING/CONVENTIONS
Both: ALLCAPS .md, lowercase TSV, parallel inbox/outbox, parallel runtime gitignore comments. TERRY's typed setup prefixes (`PRICE-TRIGGER_`/`PRINT-TRIGGER_`) are a nice convention LIQUID lacks. Note convergence: `TERRY/setups/PRICE-TRIGGER_HY280_regional-put.md` consumes the exact HY>280 line LIQUID's new watcher guards — clean cross-agent contract.

## 7. NEEDS-ATTENTION (ranked)
**LIQUID**
1. STATUS.md bloat + live-numbers-in-header — trim to pointers; quotes belong in boot.py output, not state.
2. No README/SYSTEM — add a "start here" map (TERRY's is the template).
3. MEMORY.md 19KB unsplit — split durable vs session (per `finding_subagent_memory_split`).
4. `domain/sources` bare; add `.gitkeep`; hy_oas_watch.py add a `--selftest`.

**TERRY**
1. No CLOSEOUT.md / no MEMORY — closeout write-back + cross-session learning are implicit; formalize.
2. No structured KB — POSTMORTEMS is prose-only; consider a KB.tsv if recurring lessons accrue.
3. SETUPS.tsv near-empty vs `setups/*.md` — reconcile to one source.
