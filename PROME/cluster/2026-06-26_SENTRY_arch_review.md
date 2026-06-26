# SENTRY Architecture Review — LIQUID + TERRY
**2026-06-26 · read-only · neutral third-party (SENTRY owns no folder)**
Baseline peek: REGINALD/ + CARL/ (fleet norm). Rubric mirrors the other two reviewers.

## 1. DIR LAYOUT
**LIQUID** — full fleet stack: STATUS, MEMORY (split + `archive/MEMORY_through_20260612`), `thesis/` (THESIS/CHANGELOG/TIMELINE), `workbook/` TSVs (KB/CATALYSTS/PREDICTIONS/FLOW/VX), `domain/sources/`, `scripts/`, `alerts/` (gitignored), inbox/outbox, IDENTITY/STRATEGY/USER/CALENDAR. No standalone SYSTEM.md/BOOT.md — CLAUDE.md carries the SPAWN PROTOCOL (acceptable; matches norm).
**TERRY** — executor stack: README (LIQUID has none), CLAUDE, RISK_RULES, RISK_SCORING, templates, `scripts/`, `daytrading/` subsystem, setups/charts/postmortems/workbook (mostly `.gitkeep` empty), inbox/outbox. **Missing: MEMORY.md** (no durable layer); no `thesis/` (correct — doesn't own thesis).

## 2. BOOT / CLOSEOUT
**LIQUID** — `scripts/boot.py` (live 3-dashboard sweep + `--selftest`); dedicated tiered `CLOSEOUT.md` (Bounce/Light/Standard/Heavy, auto-memory trigger, live-event override). Strong.
**TERRY** — `scripts/boot.py` (read-only card + `--selftest`); closeout is the lighter **WRITE-BACK** section embedded in CLAUDE.md — fine for an executor, but no auto-memory step and no dedicated doc.

## 3. STATE-FILE HYGIENE
**LIQUID** — runtime `alerts/` correctly gitignored; MEMORY split + archived; CREDIT_THRESHOLDS.md properly stamped HISTORICAL. **Drift risk:** STATUS.md is 28KB of dense narrative; the same X1/kill framing is duplicated across STATUS+MEMORY+HEARTBEAT (circular-corroboration vector). STATUS header still cites **10Y 4.50** (now 4.39); `CATCHUP_PUNCHLIST.md` 12-day stale (6/13).
**TERRY** — `.cache/`+`grades/` gitignored (good). **STATUS.md is a scaffold-status checklist** ("✅ created/added") rather than live operating state; 4 "Open Questions for Will" (risk-unit, Kelly cap) unresolved since 6/21. No MEMORY = lessons live only in POSTMORTEMS.

## 4. SCRIPTS / TOOLING
**LIQUID** — boot.py + `hy_oas_watch.py`; selftests present; alert labels tied to actual thesis triggers (not invented). Inherits FORGE fetch.py.
**TERRY** — richer toolset: boot/snapshot/risk_calc/chain_parse/chain_fetch/csv_pnl/grade_print, all carrying selftest/asserts. Read-only by design. Strongest tooling of the two.

## 5. SELF-DOCUMENTATION
**LIQUID** — IDENTITY.md + CLAUDE.md mandate clear. **TERRY** — README + CLAUDE IDENTITY/HARD BOUNDARIES/MODES/TERRY STANDARD; role best-documented in fleet. Both pass.

## 6. NAMING / CONVENTIONS
Both consistent with fleet (UPPERCASE state docs, scoped pathspec commits, inbox/WALTER + processed/delivered). TERRY uses README as file-map (CARL/REGINALD don't) — net positive. LIQUID `CREDIT_THRESHOLDS.md` vs `workbook/KILL_MEMO` naming slightly split but flagged inline.

## 7. NEEDS-ATTENTION (ranked)
**LIQUID**
1. STATUS narrative bloat + cross-file framing duplication → staleness/circular-corroboration risk (a self-review would call it "thorough" — flag it). Trim to dashboard + pointer.
2. STATUS header 10Y 4.50 stale vs 4.39; refresh load-bearing levels.
3. `CATCHUP_PUNCHLIST.md` 12-day stale — resolve or archive.
4. CREDIT_THRESHOLDS retained-historical: OK, leave (properly flagged).

**TERRY**
1. **No MEMORY.md** — clearest drift from fleet norm; add a durable layer (or formally declare POSTMORTEMS+SETUPS the substitute).
2. STATUS = setup checklist, not live state; rewrite as current-state once exercised.
3. Scaffold largely **un-exercised** — empty `.gitkeep` dirs, zero live trade cards (a self-review would mark "complete ✅"; neutral read = aspirational). Maturity ≠ usage.
4. 4 open config Qs (risk unit / Kelly cap) unanswered 5 days — blocks first live card.

**Net:** LIQUID = mature, at/above norm; main risk is state-doc bloat. TERRY = best-documented + best-tooled, but thin on durable memory and unexercised.
