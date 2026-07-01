# Architecture Peer-Review — Three-Way Synthesis
**Date:** 2026-06-26 · **Orchestrator:** Prome · **Reviewers:** LIQUID (self vs TERRY), TERRY (self vs LIQUID), SENTRY (neutral, vs REGINALD/CARL baseline)
**Sources:** `PROME/cluster/2026-06-26_{LIQUID,TERRY,SENTRY}_arch_review.md`

## The complementary pattern (all 3 converge)
- **LIQUID = lifecycle-mature + research-deep.** boot.py (557-line, --quick, predictions scan), tiered CLOSEOUT.md, MEMORY split+archive, IDENTITY.md, KB.tsv + thesis/ workbook TSVs, alerts/ gitignored. At/above fleet norm on lifecycle.
- **TERRY = tooling-rich + best-documented.** README, MODES, 6–7 scripts ALL selftested, RISK_SCORING, typed setup files, daytrading/ subsystem. Best docs+tools in the pair.
- **Both independently prescribed the same swap:** TERRY borrows LIQUID's CLOSEOUT/MEMORY pattern; LIQUID borrows TERRY's selftest discipline + trims state bloat.

## High-confidence gaps (≥2 reviewers, or Prome-verified)
1. **LIQUID STATUS.md bloat** (all 3) — 28KB; runaway one-line header stuffed with live numbers (HY/CCC/SOFR/VIX) → diff-hostile, staleness/threshold-drift risk. SENTRY adds: header cites **stale 10Y 4.50** (live 4.39). Matches our own anti-pattern (quotes belong in boot output, not state files).
2. **TERRY no durable layer** (all 3) — no MEMORY.md, no closeout write-back, no structured KB. Cross-session learning is implicit. Clearest drift from fleet norm.
3. **hy_oas_watch.py has NO selftest** (TERRY caught, Prome VERIFIED) — the load-bearing detector lacks a reproducible test; contradicts LIQUID's "selftest PASS" claim. Real gap.

## Neutral-only catches (SENTRY — the independent signal the self-reviews missed)
4. **LIQUID circular-corroboration** — X1/kill framing triplicated across STATUS+MEMORY+HEARTBEAT. Self-reviewer calls it "thorough"; it's the exact contamination risk (one narrative seeds writer AND grader). Matches `finding_circular_corroboration_via_state_file`.
5. **TERRY scaffold is aspirational, not done** — empty .gitkeep dirs, zero live trade cards, STATUS is a "✅ created" checklist not live state. Reads "complete," neutral read = unexercised. (Improving: got its first real exercise THIS session — fire-cards + $500 budget.)
6. **TERRY 4 open config Qs since 6/21** (risk-unit/Kelly) — **partially resolved now**: Will set $500/card max-loss 6/26 (answers the core risk-unit). Kelly/sizing-formula Qs remain.

## Ranked "needs attention" — recommended actions
| # | Fix | Owner | Impact | Effort |
|---|---|---|---|---|
| A | STATUS.md de-bloat — strip live numbers to boot output, trim header, fix stale 4.50→4.39 (kills bloat + staleness + part of #4 in one pass) | LIQUID (own) | High | Low |
| B | Add durable layer — MEMORY.md + CLOSEOUT doc (borrow LIQUID's pattern) | TERRY (own) | High | Med |
| C | Add --selftest to hy_oas_watch.py (the load-bearing detector) | LIQUID (own) | Med | Low |
| D | Dedupe X1/kill framing to one canonical home (overlaps A) | LIQUID (own) | Med | Med |
| E | Exercise the scaffold (resolving naturally as cards get used) | TERRY (own) | Low | — |

All fixes are own-dir (A/C/D = LIQUID, B/E = TERRY) — no cross-edits, clean to parallelize.
