# Research Workspace

Research Workspace is an empirical, multi-agent research system for tracking how stress moves through credit, energy, labor, housing, commodities, and capital markets.

It is also proof-of-work: a test of whether one operator without traditional research credentials can build rigorous empirical capability through sustained collaboration with frontier language models. Finance is the testbed because markets impose dated events, falsifiable outcomes, and a real cost for being wrong.

## What this project demonstrates

### 1. An architecture in operational use

The current system has operated continuously since February 2026 — roughly 10,200 commits over seven months. Its git history records the development of specialist research agents, persistent memory, cross-domain synthesis, adversarial review, and file-based coordination.

The important claim is not that every design is novel. It is that these structures emerged through repeated use: failure, diagnosis, revision, and another live test.

Early operating history can be found in [`memory/2026-02-01.md`](memory/2026-02-01.md) and the dated briefings under [`archive/IRA/briefings/`](archive/IRA/briefings/).

### 2. Calibration rather than narrative confidence

Most domain agents maintain pre-registered prediction ledgers with:

- Explicit thresholds
- Defined time windows
- Resolution criteria
- CONFIRMED, FAILED, and special-resolution outcomes
- Failure-pattern tracking

The system does not claim to eliminate error or post-hoc reasoning. Instead, it attempts to catch, grade, and learn from those failures.

Representative ledgers:

- [`AGENTS/SAM/thesis/PREDICTIONS.tsv`](AGENTS/SAM/thesis/PREDICTIONS.tsv)
- [`AGENTS/BRENT/thesis/PREDICTIONS.tsv`](AGENTS/BRENT/thesis/PREDICTIONS.tsv)

### 3. Operational discipline at research-team scale

The repository supports 33 active specialist agents, each a Claude Code session, working through one shared research system.

The architecture includes:

- Domain-specific ownership and persistent state
- A signal-routing layer
- Cross-agent synthesis
- Formal adversarial review
- Pre-registered trade-construction rules
- Agent lifecycle management
- Scoped Git protocols for concurrent sessions
- Fail-safe, non-force push handling

The verified roster and responsibility model live in [`PROME/ROSTER.md`](PROME/ROSTER.md). The transmission topology lives in [`AGENTS.md`](AGENTS.md).

## How the system works

Each specialist runs from its own directory and maintains a focused set of operating instructions, current state, durable memory, evidence, and thesis history.

A few roles organize the system:

- **PROME** coordinates priorities, decisions, and operator-facing synthesis.
- **WALTER** ingests and routes signals and news.
- **NEXUS** synthesizes findings across domains.
- **RED** challenges theses and searches for falsifiers.
- **TERRY** converts research into proposed trade structures and risk rules. It does not execute trades.

Domain agents remain responsible for their own evidence and judgment.

### Context siloing

Agents load their own domain context rather than the entire repository. At closeout, they publish compressed `NEXUS_BRIEF.md` files for cross-domain consumption.

This write-once, read-many layer allows the system to share important findings without forcing every agent to ingest every other agent's raw state. Boot-loaded files also have a script-enforced size cap (32,550 B per surface) to control context growth.

The isolation is maintained by operating convention and repository structure rather than by a distributed technical runtime.

## Guided tour

### Five-minute view

- [`CLAUDE.md`](CLAUDE.md) — fleet-wide operating rules
- [`PROME/CLAUDE.md`](PROME/CLAUDE.md) — chief-of-staff role and authority
- [`AGENTS/SAM/STATUS.md`](AGENTS/SAM/STATUS.md) — a representative domain state
- [`PROME/ROSTER.md`](PROME/ROSTER.md) — verified agent roster and classifications

### Deeper view

- [`AGENTS/BRENT/CLAUDE.md`](AGENTS/BRENT/CLAUDE.md) and [`AGENTS/BRENT/TRADE.md`](AGENTS/BRENT/TRADE.md) — a full domain specification and trade framework
- [`AGENTS/VIOLET/MEMORY.md`](AGENTS/VIOLET/MEMORY.md) — epistemic and measurement corrections
- [`AGENTS/MARCO/MEMORY.md`](AGENTS/MARCO/MEMORY.md) — characteristic-error tracking
- [`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md`](AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md) — cross-agent synthesis interface
- [`PROME/ORCHESTRAL_LAYER_DESIGN.md`](PROME/ORCHESTRAL_LAYER_DESIGN.md) — coordination-layer design
- [`AGENTS/RED/challenges/`](AGENTS/RED/challenges/) — adversarial-review corpus
- [`AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md`](AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md) — specification for building a new agent

## Why finance

Finance is the forcing function, not the endpoint.

Markets provide public evidence, dated catalysts, measurable outcomes, and adversarial feedback. That makes them a useful environment for developing a broader empirical method built around:

- Pre-registration
- Calibration
- Source verification
- Adversarial review
- Transmission-chain reasoning
- Explicit decision thresholds

The same method can apply to other research problems with external data and falsifiable claims.

## Known limitations

- **Serial rather than distributed.** Multiple sessions can operate on the current machine, but only one machine should write at a time. True simultaneous multi-machine operation would require a different branching model.
- **Broker reconciliation is manual.** Position truth remains with the operator and broker. [`FORGE/STATUS.md`](FORGE/STATUS.md) is a dated mirror and can become stale between reconciliations.
- **No externally audited P&L attribution.** The repository exposes calibration records and research process, but it does not claim independently verified investment performance.
- **Agent maturity varies.** Some domains have long operating histories; others remain earlier-stage. [`AGENTS/DAEDALUS/MATURITY_MAP.md`](AGENTS/DAEDALUS/MATURITY_MAP.md) tracks those differences.
- **Source hallucination remains possible.** Trade-relevant claims require verification against primary sources. The system treats hallucination as a tracked failure mode, not a solved problem.

## About

This project grew from self-directed experiments with persistent memory and identity continuity in ChatGPT and Claude interfaces beginning in May 2025. The git-versioned multi-agent system took its current form in February 2026.

Every agent, protocol, and workflow in the repository was developed through iteration with AI as a research and systems-design partner.
