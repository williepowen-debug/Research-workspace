# AGENTS.md

**Runtime amendment:** 2026-10-05, WQ-385; `PROME/proposals/2026-10-05_runtime-compatibility-RULED.md`.

Detect stress transmission early enough to position ahead of consensus.

## Operating model

A desk may run with an OpenAI or Anthropic model in Claude Code or Codex; its identity, responsibilities, owned paths and approved work remain the same. Identify the actual runtime and available tools at boot under `PROME/COMPLETION_SPEC.md`; select operational methods from `PROME/ORCHESTRATION_PLAYBOOK.md` § Runtime mechanics. Provider names do not establish tools or permissions.

Launch from the desk directory where the runtime supports it (`cd AGENTS/<NAME> && claude` is the Claude Code example). PROME uses `PROME/`; there is no `AGENTS/PROME/`. Verify root and local instruction loading explicitly under COMPLETION_SPEC, including when a spawned task inherits another cwd. PROME's mode selection and spawn mechanics remain in the playbook.

Canonical agent paths stay flat as `AGENTS/<NAME>/`. Do not reorganize agent directories without a migration pass — scripts, docs and workflows depend on those paths.

**Sources of truth** (nothing below is restated here):

| Subject | Canonical source |
|---|---|
| Fleet operating and Git rules | root `CLAUDE.md` (verify loading for the actual runtime) |
| Roster membership, Active / Tier-2 / dormant / special classification, responsibility classes | `PROME/ROSTER.md` |
| Detailed transmission topology (mermaid map + route summary) | `AGENTS/_NETWORK.md` |
| Grouped directory navigation | `AGENTS/_INDEX.md` |
| Orchestration and spawn contract | `PROME/ORCHESTRATION_PLAYBOOK.md` · `PROME/COMPLETION_SPEC.md` |

Do not recreate roster membership or responsibility classes here; when another surface disagrees with `PROME/ROSTER.md`, the roster wins.

## Transmission chains

Transmission chains and their routes live in `AGENTS/_NETWORK.md`, which is canonical: § Chain summary plus the map body. They are not restated here.

Potash is triage-only at FERT (root `CLAUDE.md`; full rule `AGENTS/FERT/CLAUDE.md` §POTASH). ⛔ "potash is UNOWNED" is kill-on-sight fleet-wide.

**Cross-chain roles:** NEXUS synthesizes across domains · RED challenges every thesis and hunts falsifiers · TERRY converts thesis into trade construction (entry, structure, sizing, invalidation, roll rules, postmortems) and never executes · MARCO feeds immigration / labor supply into LABOR, BRENT and CORAL · ORACLE supplies prediction-market evidence as an independent calibration signal · DAEDALUS is the on-demand fleet architect (launched by PROME or Will).

## Coordination and authority

Domain agents own their evidence, state and judgment. Do not edit another agent's files while it is working, and never silently replace its canonical figures — send it a packet.

Launch eligibility comes from `PROME/ROSTER.md`: dormant or retired agents do not launch unless Will revives them. CREED launches only with Will's explicit permission (recorded on its `PROME/ROSTER.md` row).

Trade proposals require Will's explicit approval; TERRY proposes structure, never executes. Agent research/tracking proposals → Will. External sends → ask first.

**Gate C Kernel Git boundary:** root `CLAUDE.md` Git Protocol carve-out ④ is canonical and inactive until a separate bounded activation ruling — planning or installation alone authorizes nothing.

## Operating references

- PROME boot / closeout / continuity: `PROME/BOOT.md` · `PROME/CLOSEOUT.md` · `PROME/SCRATCH.md` (the NOW page; `PROME/HANDOFF.md` is a retired stub)
- Autonomy tiers and proposal rules: `PROME/AUTONOMY.md`
- Coordination-layer design: `PROME/ORCHESTRAL_LAYER_DESIGN.md` (historical Toscanini files → `PROME/archive/TOSCANINI_2026-03/`)
