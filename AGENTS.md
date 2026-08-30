# AGENTS.md

Detect stress transmission early enough to position ahead of consensus.

## Operating model

Every agent is an independent Claude Code session. Launch it from its own directory:

```
cd AGENTS/<NAME> && claude
```

PROME is the one exception — it launches from `PROME/` (there is no `AGENTS/PROME/`). Launching in the agent directory loads the root operating rules **and** the agent's local instructions; launching from the repo root loads root only. If an agent seems to be missing its domain rules, check its working directory. PROME may also spawn agents via teams mode when orchestrating (mode-split rule → `PROME/ORCHESTRATION_PLAYBOOK.md`).

Canonical agent paths stay flat as `AGENTS/<NAME>/`. Do not reorganize agent directories without a migration pass — scripts, docs and workflows depend on those paths.

**Sources of truth** (nothing below is restated here):

| Subject | Canonical source |
|---|---|
| Fleet operating and Git rules | root `CLAUDE.md` (auto-injected) |
| Roster membership, Active / Tier-2 / dormant / special classification, responsibility classes | `PROME/ROSTER.md` |
| Detailed transmission topology (mermaid map + route summary) | `AGENTS/_NETWORK.md` |
| Grouped directory navigation | `AGENTS/_INDEX.md` |
| Orchestration and spawn contract | `PROME/ORCHESTRATION_PLAYBOOK.md` · `PROME/COMPLETION_SPEC.md` |

Do not recreate roster membership or responsibility classes here; when another surface disagrees with `PROME/ROSTER.md`, the roster wins. *(The per-agent routing table that lived here through 2026-08-29 was retired under WQ-128 (`PROME/WILL_QUEUE.md` row 128, 2026-08-29) — every fact in it lives at its owner; history → `docs/CANON_PROVENANCE.md` `key: agents-routing-table`.)*

## Transmission chains

| Chain | Route |
|---|---|
| Credit | LABOR → CARL → REGINALD → repricing; CREED supplies national CRE/CMBS, CORAL geographic convergence, HENRY velocity, LIQUID amplification. Single-name bank depth: OZK, WAL, FLG → REGINALD; FLG also → {LIQUID, TERRY} |
| Private credit | BROCK → SHADE (insurance wrapper) → LIQUID / REGINALD |
| Energy shock / war | {OSPREY, FALCON} → HAWK (cross-war synthesis, no double-count) → BRENT → {HENRY, LIQUID, CARL}; acute theater signals go to BRENT direct, HAWK cc'd. BRENT fuel cost → CRUISE (event-driven) |
| Japan / carry | SAM → {LIQUID, HENRY} — independent trigger via carry unwind |
| Credit → volatility | {BOND, BROCK, REGINALD} → VIOLET → {HENRY, LIQUID, RED} — VIOLET watches the lag: credit spreads widen and VIX hasn't caught up |
| Climate and power | AEOLUS → {BRENT, CORAL, MARCO}; AEOLUS → WATT → {HENRY, CARL}; BRENT (gas → power) → WATT |
| AI capex | VULCAN → {VIOLET, HENRY, WATT}; ZHAO (export controls) and HAWK (Taiwan chokepoint) → VULCAN |
| Metals | {BOND, ZHAO} ↔ MIDAS → {LIQUID, HENRY}; HAWK → MIDAS (PGM supply) |
| Housing | HOMER → {CARL, REGINALD, HENRY} |
| Fertilizer / food | BRENT (feedstock) → FERT → {CARL, HENRY}; {OSPREY, FALCON} theater signals → FERT |

Potash routes to FERT at **triage depth** — log it and flag PROME, no deep-dive; full rule in `AGENTS/FERT/CLAUDE.md` §POTASH. ⛔ "potash is UNOWNED" is kill-on-sight fleet-wide.

**Cross-chain roles:** NEXUS synthesizes across domains · RED challenges every thesis and hunts falsifiers · TERRY converts thesis into trade construction (entry, structure, sizing, invalidation, roll rules, postmortems) and never executes · WALTER owns signal and news routing · PROME coordinates priorities, decisions and operator-facing synthesis · MARCO feeds immigration / labor supply into LABOR, BRENT and CORAL · ORACLE supplies prediction-market evidence as an independent calibration signal · DAEDALUS is the on-demand fleet architect (launched by PROME or Will).

## Coordination and authority

Domain agents own their evidence, state and judgment. Do not edit another agent's files while it is working, and never silently replace its canonical figures — send it a packet.

Launch eligibility comes from `PROME/ROSTER.md`: dormant or retired agents do not launch unless Will revives them. CREED launches only with Will's explicit permission (recorded on its `PROME/ROSTER.md` row).

Trade proposals require Will's explicit approval; TERRY proposes structure, never executes. Agent research/tracking proposals → Will. External sends → ask first.

**Gate C Kernel Git boundary:** root `CLAUDE.md` Git Protocol carve-out ④ is canonical and inactive until a separate bounded activation ruling — planning or installation alone authorizes nothing.

## Operating references

- PROME boot / closeout / continuity: `PROME/BOOT.md` · `PROME/CLOSEOUT.md` · `PROME/HANDOFF.md`
- Autonomy tiers and proposal rules: `PROME/AUTONOMY.md`
- Coordination-layer design: `PROME/ORCHESTRAL_LAYER_DESIGN.md` (historical Toscanini files → `PROME/archive/TOSCANINI_2026-03/`)
