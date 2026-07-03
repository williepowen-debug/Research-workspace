# BLUEPRINT — Meta-Agent

**Owner:** DAEDALUS · **First worked example:** DAEDALUS itself (extracted 2026-06-27)
**Use for:** agents with **authority to *change* the system's structure** (build/edit/retire agents; orchestrate/task/prioritize) rather than markets — e.g. DAEDALUS, PROME. NOT domain/trade agents, and **NOT review/synthesis *services*** (YEYOU/NEXUS/RED produce a consumed output with no structure-mutation authority → `utility-agent.md`). The discriminator is mutation-authority, not subject-matter (PAT-027). *(DARWIN, archived, was an early meta attempt.)*

> A meta-agent is a deliberate exception to the market template. It does NOT get KB/VX/FLOW, a convergence matrix, exit/falsification rules, or TRADE.md — those are market constructs and forcing them on a meta-agent produces dead, never-filled files (the DARWIN failure). It gets a *meta-shaped* memory instead.

---

## Required sections (CLAUDE.md)

1. **Header** — name, class (`Meta-agent`), reports-to, spawnable-by, link to a design spec.
2. **IDENTITY** — what system-layer it owns; an explicit "where you sit" table vs adjacent meta-agents (no-overlap proof); the `File > verbal` rule.
3. **SPAWN PROTOCOL** — read state → read memory → apply prior lessons → execute → write back → deliver-before-idle. Any *runnable* boot/closeout command must be **cwd-proof** — self-locate via `"$(git rev-parse --show-toplevel)"`, never a bare root- or own-dir-relative path that depends on the incidental launch cwd (PAT-031).
4. **THE JOBS** — its concrete functions, each with its approval gate.
5. **AUTHORITY & SAFETY** — *the load-bearing section for any agent with cross-fleet write power.* Spell out the guards (see below).
6. **MEMORY MODEL** — its meta-shaped files (see below).
7. **OUTPUT RULES** — tables, specificity, proposal format, reference-don't-copy, line cap.
8. **FILES** table.
9. **BOTTOM LINE** discipline.

## Authority guards (if it can touch others' files)

Any meta-agent with write power over other agents MUST state both:
- **Express permission** — every cross-agent mutation gated on Will/PROME approval, **batched** (one changelist, one approval — never drip per-file prompts).
- **Idle target** — only edit an agent that is NOT in a live session; live agents get a task packet routed to their inbox. Permission ≠ concurrency-safe.
Plus: own-dir = free edit; external send / wiring / retirement = ask first; `trash` > `rm`.

## Meta-shaped memory (replaces KB/VX/FLOW)

| File | Role | Market analogue |
|---|---|---|
| `<STANDARD>/` (e.g. `BLUEPRINTS/`) | The canonical artifacts it owns and maintains | — |
| `PATTERNS.tsv` | Sourced, dated lessons & anti-patterns — the learning engine | KB.tsv |
| `EVOLUTION.md` | Changelog + roadmap of its domain-of-responsibility | thesis/CHANGELOG |
| `<MAP>.tsv` (e.g. `FLEET_MAP.tsv`) | Per-target state it tracks over time | per-agent memory |

## Oversight

Stated explicitly: a meta-agent appears in its own map/output like any target (no agent grades only itself); Will + PROME direct and examine it; YEYOU reviews its per-push conformance.

---

## Grading a meta-agent (maturity ceiling)

L3 = its core rubric/checks run + its map current · L4 = its outputs executed/consumed cleanly + PATTERNS accruing · L5 = self-maintaining + roadmap live. (Floor L0–L2 same as all classes.)
