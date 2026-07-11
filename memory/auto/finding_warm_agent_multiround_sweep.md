---
name: finding_warm_agent_multiround_sweep
description: Keep named domain-agent spawns resident across a session and re-task them in escalating rounds (hygiene sweep → approved fixes → deep threads → execution) — each later round is cheap and high-yield because the agent has just re-read its whole domain; validated 4/4 agents, 72 items, 2026-07-11.
metadata:
  type: project
---

**Pattern (validated 2026-07-11, VIOLET/LIQUID/HENRY/SAM pilot):** instead of one-shot spawns, keep named background agents resident and re-task the SAME agent across escalating rounds: (1) domain sweep, triage-first → (2) Will-approved fix execution → (3) deep threads sweep (missed connections + further threads — the lenses in `PROME/packets/DOMAIN_SWEEP_LENSES.md`) → (4) time-bound execution wave. Round-3 deep sweeps were the highest-signal-per-token work of the day (72 items, 3 structural finds, a convergent cross-agent mechanism) precisely BECAUSE each agent had just re-read its entire corpus in rounds 1-2 — a cold agent doing lens-3/4 work pays that reading cost first.

**Why:** subagent context persists across SendMessage re-tasks within the session; the marginal round costs only the new task, not a re-boot. Round-1 output also lets the operator approve/steer before analytic spend (triage-first → approval → execute), which Will explicitly preferred.

**How to apply:** for fleet catch-up or audit work, spawn the wave once, then ladder rounds via SendMessage with escalating lenses; carry deliver-before-idle + own-dir pathspec commit rules in EVERY round's message (agents don't re-read the original packet). Verify each round's commit scope before the next. Corollary from the same pilot: agents' round-3 self-audits reliably surface record-vs-reality drift (3 catches in one day) and falsification-layer rot (4/4 agents) — [[finding_expiry_dated_suppression_register]], [[finding_status_spine_staleness_under_appended_top]].
