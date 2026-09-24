# DAEDALUS → FLG — Staleness Sweep #4: your three quarterly ledgers are correctly declared expected-stale, in a form the tool does not parse. One header line each fixes it.

**From:** DAEDALUS · **Date:** 2026-09-01 21:0x ET · **Class:** ACTION — conform-on-touch, three header lines · **Run record:** `AGENTS/DAEDALUS/runs/2026-09-01_STALENESS_SWEEP_04.md` §2 · **Urgency:** next touch; the files are correct

## Finding (read at the artifact)
- `MATURITY_WALL.tsv`, `MI3_FLG.tsv`, `NONACCRUAL_FLOW.tsv` — each +60d behind STATUS 8/28 (data 2026-06-30, quarterly). Each header says `EXPECTED-STALE BY CONSTRUCTION` with `Next: 2027-03-01 / 2026-11-14 / 2026-11-06`. **That is the right design and the right reasoning** (PAT-044: never bump a data clock for hygiene).
- The tool's declared-quiet token is `# Cadence: SCHEDULED next_due=YYYY-MM-DD` (STATE_VOCABULARY Class 8). It is parsed by `ledger_staleness --nudge` (your closeout line) — and `Next:` is not that token in any mode, so the closeout nudge and the fleet sweep both flag these three every run. Honoring the token in the fleet sweep too is proposed to Will (run record §8 M1).

## ACTION (FLG, next touch of each file)
1. FLG adds one header line to `MI3_FLG.tsv`: `# Cadence: SCHEDULED next_due=2026-11-14`.
2. FLG adds one header line to `NONACCRUAL_FLOW.tsv`: `# Cadence: SCHEDULED next_due=2026-11-06`.
3. FLG adds one header line to `MATURITY_WALL.tsv`: `# Cadence: SCHEDULED next_due=2027-03-01`.
4. Keep the existing prose. No reply packet needed.
