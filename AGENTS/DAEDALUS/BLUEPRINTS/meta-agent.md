# BLUEPRINT — Meta-Agent

**Owner:** DAEDALUS · **First worked example:** DAEDALUS itself (extracted 2026-06-27)
**Use for:** agents with **authority to *change* the system's structure** (build/edit/retire agents; orchestrate/task/prioritize) rather than markets — e.g. DAEDALUS, PROME. NOT domain/trade agents, and **NOT review/synthesis *services*** (YEYOU/NEXUS/RED produce a consumed output with no structure-mutation authority → `utility-agent.md`). The discriminator is mutation-authority, not subject-matter (PAT-027). *(DARWIN, archived, was an early meta attempt.)*

> A meta-agent is a deliberate exception to the market template. It does NOT get KB/VX/FLOW, a convergence matrix, exit/falsification rules, or TRADE.md — those are market constructs and forcing them on a meta-agent produces dead, never-filled files (the DARWIN failure). It gets a *meta-shaped* memory instead.

---

## Required sections (CLAUDE.md)

1. **Header** — name, class (`Meta-agent`), reports-to, spawnable-by, link to a design spec.
2. **IDENTITY** — what system-layer it owns; an explicit "where you sit" table vs adjacent meta-agents (no-overlap proof); the `File > verbal` rule.
3. **SPAWN PROTOCOL** — read state → read memory → apply prior lessons → execute → write back → deliver-before-idle. Any *runnable* boot/closeout command must be **cwd-proof** — self-locate via `"$(git rev-parse --show-toplevel)"`, never a bare root- or own-dir-relative path that depends on the incidental launch cwd (PAT-031). Git text = **cite-don't-restate**: pointer to root `CLAUDE.md §Git Protocol` + own pathspec + exceptions only (harness-audit S2, 2026-07-08).
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

## Standing disciplines (added 2026-07-22 — the 7/22 self-sweep found this variant had missed every wave since 7/8)

- **⚡ SPAWNED-MODE BOOT CARD** (top of CLAUDE.md, ~5 lines, shape per `market-agent.md §8`) — meta-agents are the MOST coordinator-spawned class; the card carries the PAT-046 deliver-both-halves clause (files written+committed AND coordinator notified).
- **Registration/lifecycle via the canonical checklist** — every build/promotion/split/retirement sweeps ALL surfaces in `builds/REGISTRATION_CHECKLIST.md` (11 rows + the meta-agent's OWN script registries, row 12 — scanner SKIP/CLASS sets and renderer SPECIAL/DROP sets fail SILENT when a lifecycle change skips them), in PAT-047 co-registration order.
- **Spawn-driver rule (PAT-051):** any standing role a restructure creates (esp. synthesis/coordinator roles with no event trigger) gets its spawn cadence REGISTERED in a durable home (docket row / sweeps registry) at creation — "both siblings moved" has no owner by default.
- **Ledger-append hardening:** meta-agents append to load-bearing TSVs (PATTERNS/MAP/registry) every session — shell-appends only via `scripts/tsv_append.py` fields-as-argv or Python, never bare `printf`/`echo`; wrong-PATH writes are the sibling hazard (PAT-050's misfile instance 7/22: a pattern row written to a stray file = invisible at every boot; verify the target path on append).
- **Cross-session messaging — cite, don't restate (Will-ruled 2026-08-16: open p2p, coordination class; rule 3 ratified):** before first use of harness `SendMessage`/`ListAgents` between independently-launched sessions, read `MESSAGING/CROSS_SESSION_MESSAGING.md` + `PROME/ORCHESTRATION_PLAYBOOK.md` §Cross-session. Core: messages = coordination, artifacts = content; verify peer claims at artifacts; a relayed operator word never clears a Will-gated surface; never route signals around WALTER. Meta-agents run the most cross-agent choreography — the doorbell pattern (commit → message → receiver verifies at artifacts → executes under standing authorizations, naming the trigger in-commit) is the validated shape. Teams-mode spawns out of scope; deliver-before-idle unchanged.
- **Controlled state tokens & STRICT text (PAT-075, 2026-07-31):** NEW state-bearing surfaces (map rows, registry status cells, sweep verdicts) use `BLUEPRINTS/STATE_VOCABULARY.md` canonical tokens; cost-bearing text (packet ACTION lines, script messages, checklist steps) follows `BLUEPRINTS/STRICT_TEXT.md`. Meta-agents are the heaviest writers of machine-read state cells — the token IS the interface. Cite, don't restate; prose out of scope.
- **Self-inclusion (PAT-050):** the meta-agent's own surfaces are IN SCOPE of every sweep it runs; recurring self-sweeps are the mechanism, not discipline. Write-back TAIL rule: processing an inbound write-back (or marking a map row-gap RESOLVED at review time, PAT-058) closes the row AND the originating card/banner AND the outbox copy, same pass.

## Oversight

Stated explicitly: a meta-agent appears in its own map/output like any target (no agent grades only itself); Will + PROME direct and examine it; YEYOU reviews its per-push conformance (waivable-when-dormant per SPEC §5, Will 7/22).

---

## Grading a meta-agent (maturity ceiling)

L3 = its core rubric/checks run + its map current · L4 = its outputs executed/consumed cleanly + PATTERNS accruing · L5 = self-maintaining + roadmap live. (Floor L0–L2 same as all classes.)
