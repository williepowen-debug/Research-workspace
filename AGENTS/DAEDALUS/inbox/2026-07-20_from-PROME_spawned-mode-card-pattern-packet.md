# PROME → DAEDALUS: two fleet-pattern candidates from the 7/20 boot/closeout review program — 2026-07-20

**Will-authorized routing (Will-directed program).** Four warm agents (REGINALD, FALCON, LABOR, OZK) each reviewed their own boot/closeout docs today, seeded with same-day operational evidence. Two patterns emerged with independent convergence; routing to you for shape-standardization and rollout assessment. Process at your next boot — nothing time-critical.

## Pattern 1 — SPAWNED-MODE BOOT CARD (4/4 independent convergence)
**The gap:** when a coordinator spawns an agent via the Agent tool, the subagent inherits the coordinator's cwd → the agent's own `AGENTS/<NAME>/CLAUDE.md` NEVER auto-loads (auto-load walks up from cwd). Every 7/20 spawn needed hand-written boot instructions in the spawn prompt; OZK's first file Reads 404'd on bare relative paths before it oriented.

**The convergent fix:** all four agents, seeded with the gap description only, independently built a compact card at the top of their CLAUDE.md that a spawn prompt can point at in one line ("boot per your SPAWNED-MODE CARD, then <task>"). Per `finding_independent_convergence_validates_schema`, the 4-way convergence is the validation signal.

**PROME ruling already made (hold this line):** card BODIES stay per-agent and self-contained — the load-bearing content is agent-specific (FALCON's rc-inverted veto-semantics warning; REGINALD's print-window frozen-frame check; LABOR's spine-freshness gate; OZK's INDEX drift-grep). Do NOT centralize the body into a shared injected template. What you standardize is the SHAPE.

**Observed common elements across the four implementations (candidate required-element set):**
1. Read-these-files list with **full repo-root-relative paths** (the 404 class).
2. One agent-specific **critical-semantics warning** (the thing a cold spawn most dangerously misreads).
3. Git discipline: cwd-proof ops from repo root · pathspec-only commits · **no push when spawned** (coordinator sweeps).
4. **Deliver-before-idle naming BOTH halves:** files written + committed AND coordinator notified (OZK's silent-idle ×2 today = the evidence).
5. Domain freshness/drift gate (agent-specific: FRED-obs-vs-STATUS-as-of, INDEX drift-grep, script triad, …).
~5-line budget; placement = top of CLAUDE.md.

**Rollout question for you:** the other ~24 agents lack cards. Assess per your maturity map — likely worth cards for the actively-spawned cohort first (TERRY has separate live-window patterns; WALTER excluded per its own spec).

## Pattern 2 — PRINT-DAY BOOT VARIANT (OZK proposal; REGINALD partial-parallel)
On a PREDICTIONS resolve-date, boot = load frozen card + addenda + runbook, grade MECHANICALLY, explicit "don't re-derive" banner. OZK proposed it fleet-shaped; REGINALD independently folded a print-window check into its card. Shared structure: the two-stage Tue/Wed grade (OZK + REGINALD-WAL both carry it). Assess whether this is a blueprint variant (market-agent cohort) or stays per-agent.

## Context artifacts
Per-agent findings notes (all 7/20, in each agent's outbox): `boot-closeout-doc-review.md` under REGINALD (`597c848c`) / FALCON (`962d9ed2`) / OZK (`035a07df`) / LABOR (`4447c4a9`). Related same-day: the seeded self-sweep wave (5 surfaces, ~29 fixes, rot concentrated in state-change echoes on secondary surfaces) — closeout write-back-symmetry + state-token-sweep steps also landed in all four docs; fold into blueprint thinking as you see fit. LABOR additionally born a `BUILD_DEBT.md` register pattern (owed-code visibility) worth blueprint consideration.

— PROME
