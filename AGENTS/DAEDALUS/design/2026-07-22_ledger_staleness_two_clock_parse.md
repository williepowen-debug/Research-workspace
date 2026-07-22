# ledger_staleness.py two-clock parse — change record (PAT-039 fix)

**By:** DAEDALUS · **Date:** 2026-07-22 · **Status:** ✅ APPLIED + VALIDATED (Will-directed session — item 5 of the 7/22 open-items docket; the gated shared-script change PAT-039 graduated to PROPOSE on 7/10)
**File:** `scripts/ledger_staleness.py` (repo root — shared, 13 CLAUDE.md boot references across the fleet)

## Problem (PAT-039, two observed instances)

The enforcer graded staleness from git-commit time (fallback mtime). Two ways that goes FALSE-CLEAN on genuinely stale data:
1. **Flattened clone** (cloud sessions): history truncation collapses commit dates → everything reads "+0d ok" (OTTO 7/7: KB content Mar-26 read ok).
2. **Hygiene-edit reset**: adding a banner/tag/two-clock header commits the file → git clock resets → the enforcer STOPS flagging the very surface just marked stale (REGINALD 7/10, self-found).

## Change

`file_time()` now prefers an in-content **two-clock header date** — `Last real data refresh: YYYY-MM-DD` (case-insensitive, first ~8 lines, the PAT-044 canonical form) — over git time; git time over mtime, as before. Files WITHOUT the header behave exactly as before. Interface (flags, exit codes, output format) unchanged; no caller edits needed.

## Validation (7/22)

- **Parser unit cases 4/4 PASS** (canonical header · case/spacing variant · no header · hygiene-clock-only line correctly ignored).
- **Fleet before/after diff (`--all --quiet` + `--trade --all --quiet`):** only delta = **REGINALD FLOW.tsv +140d / KB.tsv +103d newly flagged — verified TRUE positives**: their own headers read `Last real data refresh: 2026-03-04 / 2026-04-10` with `Staleness sweep (no new data): 2026-07-10` — the exact laundering case the fix targets, caught on first run. (No new REGINALD task: the headers also say `Next: post-Jul-21 refresh`, already scheduled and gating REGINALD's L5.) BROCK/MARCO/OTTO flags unchanged (no headers — previously-flagged rows stay flagged); HOMER's 4 headered ledgers unchanged (data clock ≈ git clock, consistent).

## Residuals / non-goals

- **STATUS.md anchor stays on git time** — STATUS is the freshest surface by construction; if a STATUS ever carries the header, it wins there too (harmless, intended).
- **Coverage grows with header adoption**, not script changes: PAT-044 headers are already baked into blueprint §8; HOMER shipped with them; OZK's packet (7/22) asks for them. The fix's value compounds as the Staleness Sweep (~7/25) and task packets spread the header.
- Cloud-clone false-cleans remain possible for headerless files — unchanged caveat; the header is the portable cure.
