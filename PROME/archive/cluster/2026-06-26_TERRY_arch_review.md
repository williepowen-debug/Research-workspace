# Architecture Peer-Review — TERRY vs LIQUID
**Date:** 2026-06-26 · **Reviewer:** TERRY · **Method:** read-only inspection of both dirs (no edits to LIQUID).

## 1. DIR LAYOUT
| Element | TERRY | LIQUID |
|---|---|---|
| STATUS.md | ✅ (44L) | ✅ (144L) |
| MEMORY split | ❌ none | ✅ MEMORY.md (117L) |
| Identity/role doc | CLAUDE+README+RISK_SCORING | ✅ IDENTITY.md + STRATEGY.md + CLAUDE |
| Closeout doc | ❌ none | ✅ CLOSEOUT.md (196L) |
| KB / domain | RISK_RULES, RISK_SCORING, POSTMORTEMS, TRADE_BOOK | CREDIT_THRESHOLDS, CALENDAR, thesis/, domain/ |
| boot.py | ✅ (140L) | ✅ (557L) |
| scripts/ | ✅ 6 (.py) | ✅ 2 (.py) |
| inbox/outbox | ✅ | ✅ (+delivered/processed) |
| archive | ✅ | ✅ (10+ subdirs) |
| workbook | ✅ | ✅ |
| .gitignore | ✅ | ✅ |
| Specialized | setups/, charts/, daytrading/, templates | alerts/, board_log.tsv, USER.md, .claude/ |

## 2. BOOT/CLOSEOUT
- **TERRY:** read-only boot card (140L). **No closeout doc and boot.py has no write-back/cadence logic** — closeout discipline is implicit (CLAUDE.md), not codified.
- **LIQUID:** richer boot (557L: `--quick` FRED-only mode, CATALYSTS.tsv parsing, malformed-row flagging) + a formal **CLOSEOUT.md** write-back protocol. Stronger boot/closeout loop.

## 3. STATE-FILE HYGIENE
- **TERRY:** STATUS lean (44L), runtime outputs (.cache/, grades/) gitignored, no MEMORY split — durable lessons scattered across POSTMORTEMS + daytrading/. STATUS 1 day stale (6/24 vs LIQUID 6/25).
- **LIQUID:** STATUS fresh (6/25) and MEMORY is split out — good. BUT the STATUS "Last Updated" header is a **runaway single-line paragraph** (~one full screen of inline numbers/thresholds): hard to diff, drift-prone (number-carries-threshold risk). Candidate for a Path-B trim.

## 4. SCRIPTS/TOOLING
- **TERRY:** 6 scripts, **all 6 carry selftests** (boot, snapshot, risk_calc, chain_parse, chain_fetch, grade_print). Strong test discipline.
- **LIQUID:** 2 scripts; only boot.py has a selftest — the load-bearing **hy_oas_watch.py detector has NO selftest** (also leaves a tracked-clean `__pycache__`, already gitignored). Thinner automation, but boot.py itself is more capable than any single TERRY script.

## 5. SELF-DOCUMENTATION
Both document mandate well. LIQUID has a dedicated **IDENTITY.md + STRATEGY.md** (clean single anchor). TERRY's role is spread across CLAUDE.md + README.md + RISK_SCORING.md — adequate but no single identity file.

## 6. NAMING/CONVENTIONS
Both consistent: UPPERCASE docs, lowercase dirs, `*.tsv` ledgers, `scripts/*.py`. No collisions. LIQUID uses dated archive subdirs (good provenance); TERRY archives flatter.

## 7. NEEDS-ATTENTION (ranked)
**TERRY**
1. **[HIGH]** No CLOSEOUT.md + no boot write-back → closeout relies on memory (vs intra-day-closeout-discipline feedback). Adopt LIQUID's CLOSEOUT pattern.
2. **[MED]** No MEMORY.md — add a durable MEMORY split (lessons currently scattered).
3. **[LOW]** STATUS 1 day stale; refresh at next boot.
4. **[LOW]** No single IDENTITY anchor.

**LIQUID**
1. **[HIGH]** STATUS header = runaway one-line paragraph → diff-hostile, threshold-drift risk. Trim to structured lines.
2. **[MED]** hy_oas_watch.py (the detector) has no selftest — add one; it's load-bearing for the HY-280 trigger.
3. **[LOW]** Archive sprawl (10+ subdirs) — confirm retention intentional.
4. **[LOW]** Verify top-level docs (board_log.tsv, CALENDAR, CATCHUP_PUNCHLIST) all current.

**Cross-takeaway:** TERRY leads on tooling/selftests; LIQUID leads on boot/closeout/memory/identity. Each should adopt the other's strength.
