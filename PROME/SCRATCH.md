# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-18 14:00 ET

## What Just Happened

Two pieces of work landed today:

1. **memory-audit-001 — first bounded teams test (executed).** Adversarial-pair (curator + critic, both Opus general-purpose) audited 8 MEMORY draft candidates and landed 3 new MEMORY.md entries + 2 in-place updates + 1 auto-memory route + 5 rejects. Joint decision committed at `49463cf7`; META_EVAL.md committed at `a045c4b6`. Adversarial-pair pattern validated as net-positive for judgment-heavy curation (substrate-in-flux argument for rejecting #3/#5 was the headline win — emerged only from reconciliation DM, not standalone files). Reusable brief template captured in auto-memory `feedback_adversarial_brief_for_pair_teams.md`. Full meta-eval at `PROME/scratch/teams_memory_audit_001/META_EVAL.md`.

2. **Orchestral layer design (theory-crafting only, no execution yet).** Will named the next bottleneck: direction overhead, not execution speed. Designed an orchestral layer where Prome spawns a fleet-scanner subagent to produce `PROME/FLEET_SCAN.md` (heavy reading delegated; Prome's context stays clean), optionally layered with adversarial-pair on top-N refinement and revival proxies for stale agents. Full design at `PROME/ORCHESTRAL_LAYER_DESIGN.md`.

## Current Git State

- Branch: `master`
- HEAD / origin after meta-eval push: `a045c4b6 PROME: meta-eval for memory-audit-001 teams test`
- One additional commit pending for the orchestral layer design doc + this SCRATCH update.

## Next Planned Work

**Top priority next session:** prototype Step 1 of `PROME/ORCHESTRAL_LAYER_DESIGN.md`.

1. Will requests fleet scan (or Prome offers if no other priority displaces it).
2. Prome spawns a `fleet-scanner` subagent (general-purpose, foreground) with the FLEET_SCAN.md template (in the design doc) as its brief.
3. Subagent reads: first 30 lines per `AGENTS/*/STATUS.md`, last 5 commits per agent dir, inbox file counts, HEARTBEAT catalyst calendar, TOSCANINI QUEUE. Writes `PROME/FLEET_SCAN.md` v1. Returns to Prome only a ~10-line summary.
4. Will and Prome review the v1 output; iterate template based on what's useful vs noise.
5. Once template shape is good (likely 2-3 iterations), layer adversarial-pair on the top-N section per Step 3 of the design.

Critical: do NOT read 13 STATUS files into Prome's context directly. The whole point of the design is context discipline via subagent delegation.

## Current Working Model

- BDC/private-credit mark/income stress remains confirmed by FSK; broad public-credit cascade still unconfirmed (HY OAS <300, VIX <20).
- Latest checked dashboard May 17 10:38 ET (likely stale by next session — re-run on boot): HY OAS **276bps**, VIX **18.43**, Brent **$109.26**, gas **$4.50**, USD/JPY **158.73**, BIZD **$12.61**, WAL **$74.42**, KRE **$66.97**.
- BRENT 5/18 update flagged: Iran drone strike on UAE Barakah nuclear plant May 17 (first nuclear-infrastructure attack of the war); US sanctions-waiver report drove Brent $111→$102 intraday; NSC meeting May 19 on potential military action. See `AGENTS/BRENT/demand_destruction/data/monday_2026-05-18.md`.
- REGINALD May 17: WAL Investor Day Bucket E B3 fired; REG-25 65%+; WAL 10-Q integration + MI3/FFIEC PDD status checks still due.
- WALTER May 17: routing-ownership split codified (WALTER routes signals; Prome tasks/synthesizes).

## Cautions

- No trades without Will approval.
- No external/public messages without approval.
- Persistent agents — do NOT spawn: **CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome** (updated per today's MEMORY.md edit).
- Use explicit path staging only; never `git add .` or `git add -A`.
- Fleet-scanner subagent must respect read budget — if it tries to read full STATUS files, context discipline is broken and the design doesn't work.
- If fleet-scanner reveals concurrent activity by other agents (dirty trees in their dirs), follow root CLAUDE.md "Before pulling" protocol; do not commit Prome's work blindly.
