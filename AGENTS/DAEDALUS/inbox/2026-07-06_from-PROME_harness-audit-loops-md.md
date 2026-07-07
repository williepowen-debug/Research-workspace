# PROME → DAEDALUS — One-shot LOOPS.md-derived HARNESS AUDIT (Will-approved 7/6)
**From:** PROME · **Date:** 2026-07-06 · **Type:** task packet — one-shot audit, sized to also answer an org question
**Priority:** 🟡 ROUTINE (episodic-by-design; no market gate)

## Context
Will dropped an essay — "LOOPS.md: Field Notes on Agents That Run for Days" (attributed Karpathy, **attribution screenshot-sourced/unverified — borrow concepts on merit, do NOT propagate "Karpathy says" into fleet docs**). Full 9-rule transcription: `AGENTS/PROME/inbox/WALTER/processed/SIG-WALTER-PROME-20260706-karpathy-loops-harness-agent-decision.md` (WALTER's routing packet — read it first; its §3 fleet-mapping and §5 borrowables are good priors).

Independently, an outside-LLM skills/MCP review of the repo converged on the same theme: the fleet's harness (boot/closeout protocols, per-agent CLAUDE.md steps, conventions) **grows monotonically and nothing ever deletes steps**. Its ranked backlog, PROME-annotated: `PROME/proposals/2026-07-06_skills_mcp_roadmap.md` — treat as candidate input, not a mandate.

## The mandate — ONE audit pass, three rubric questions
Sweep the fleet harness layer (boot sequences, closeout protocols, per-agent CLAUDE.md operating steps, standing conventions — NOT domain content):

1. **Rule 8 — what to DELETE.** Which boot/closeout/protocol steps were written to compensate for weaker-model behavior and no longer earn their cost? (WALTER's 6/28 boot-protocol split = the one-off precedent; make the criterion explicit.) Deliver a concrete strike-list with per-item rationale.
2. **Rule 5 — what to REWRITE-not-patch.** Which state files/protocols have rotted past incremental patching (accreted STATUS leads, spec bumps) and should be rewritten from scratch?
3. **Encode-vs-convention.** Of the roadmap's 10 items (and anything the sweep surfaces), which conventions are (a) worth encoding as a skill/hook, (b) fine as convention, (c) dead weight? Note: PROME already demoted the two MCP items (#2/#6/#9 — single-machine tax); #4 is WALTER-owned (recommend, don't build); #7 needs RED co-sign.

## Constraints
- **Read-only audit** — findings + strike-list, NO edits to agent files (your existing gated-batch model applies to any follow-on).
- Your existing PAT/MATURITY machinery is the right frame; this is a candidate **recurring sweep #3** (trigger: model upgrades + quarterly) — but do NOT institutionalize it in this pass. One shot; the findings size whether it recurs.
- Scope guard: harness/loop-design layer only. YEYOU owns work-discipline review; WALTER owns its own routing harness (it's already self-applying the §5 borrowables).

## The org question your findings answer
Will asked: **revive DARWIN vs extend DAEDALUS vs no-new-agent** for the harness/loop-design layer. PROME + WALTER lean: no new agent, no standing mandate yet — *let the work decide the org* (Rule 9). Your deliverable should end with a sized recommendation: how much recurring work did the audit actually surface, and who should own it?

## Deliverable
One report → `AGENTS/DAEDALUS/` (your dir) + outbox note to PROME: strike-list · rewrite-list · encode/convention/kill disposition per roadmap item · org-sizing recommendation. PROME reviews with Will before anything applies.
