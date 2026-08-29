# Research Workspace

This repo is two things at once: a 33-agent empirical research system tracking systemic risk transmission across credit, energy, labor, and capital flows — and a working test of whether someone without traditional credentials can build empirical-research capability by sustained iteration with frontier LLMs, at the depth where claims are falsifiable and being wrong has a real cost.

One person + AI here produces output that would traditionally require a small research team — augmenting individual capacity and substituting for team labor at the same time. The goal was to build a lasting, durable framework in which the agents could grow.

## Three exhibits

1. **Architecture in operational use since February 2026.** A multi-agent + persistent-memory + adversarial-RED-team architecture has been running in this repo's daily use since February 1, 2026 (earliest commits in current form; see the day-one memory logs from `memory/2026-02-01.md` onward and dated early briefings under `archive/IRA/briefings/`). ~10,200 commits over seven months is the timestamped operational record. The design problems the field is now publishing on — multi-agent orchestration, durable agent memory, adversarial verification — were the design problems this workflow had been navigating in production for months. The interesting claim isn't priority; it's convergence: a solo-operator workflow arriving at the same structural answers as the labs, on a working clock.

2. **Calibration discipline, not vibes.** Most domain agents maintain a pre-registered predictions ledger (`PREDICTIONS.tsv`) with a public scoreboard (CONFIRMED / FAILED / special-resolved) and a failure-pattern taxonomy. Predictions carry explicit thresholds and time-boxes set before the event, and are graded against the line. Post-hoc rationalization, when it occurs, is explicitly flagged as a calibration failure and tracked in the taxonomy — the catch-and-track loop is the discipline, not an absence of failure modes. See `AGENTS/SAM/thesis/PREDICTIONS.tsv`, `AGENTS/BRENT/thesis/PREDICTIONS.tsv`.

3. **Operational scale and discipline.** 33 active specialist agents. Single-writer coordination protocols developed in daily use (one machine live at a time, desktop ⇄ laptop, concurrent agent sessions on it): pathspec git commits for concurrent-writer races, fail-safe push gating, formal adversarial RED-team integration with documented dialogue logs (e.g. `AGENTS/SAM/V16_RED_DIALOGUE.md` plus the broader `AGENTS/RED/challenges/` corpus), fleet protocol audits, and agent lifecycle management (retirement, promotion, dormant states).

## How it's organized

**33 active agents in five responsibility classes** (descriptive, not authority tiers — canonical list and classification method: `PROME/ROSTER.md`):

- **Organizing / service (3)** — **PROME** (chief of staff; decision rails, state, operator-facing synthesis), **WALTER** (signal & news routing — the most active agent in the system), **NEXUS** (cross-agent synthesis; reads each domain agent's NEXUS_BRIEF).
- **Review / QC (1)** — **RED** (formal adversarial red-team; challenges every thesis).
- **Domain active (17)** — SAM (Japan / BOJ / carry), LIQUID (HY / credit spreads / funding plumbing), VIOLET (vol / VIX), BRENT (oil / energy), HENRY (macro velocity), CARL (consumer credit), LABOR (claims / JOLTS / NFP), BROCK (private credit / BDCs), HAWK (geopolitics → energy), TERRY (trade construction — proposes only, never executes), REGINALD (regional banks), MARCO (migration / labor / FL sub), ORACLE (prediction-market diagnostics — independent calibration signal), BOND (US rates / auctions), CORAL (Florida — whole state, 10 pillars), SHADE (insurer-lender / PE-insurance-captive), ZHAO (China / capital flows).
- **Provisional active (7)** — AEOLUS (climate → economy), WATT (power / grid), VULCAN (AI-capex / semis), MIDAS (metals), OSPREY (Russia/Ukraine theater), FALCON (Iran/Gulf theater), HOMER (housing).
- **Event-driven specialist (5)** — OZK, WAL, FLG (single-bank specialists), CRUISE (CCL vehicle), FERT (fertilizer / food-CPI).

Plus DAEDALUS (fleet architect meta-agent; cross-agent structural maintenance, on demand) and a Tier-2 bench spawned on demand.

Each agent runs as an independent Claude Code session with its own CLAUDE / STATUS / MEMORY tree, plus `thesis/` and `TRADE.md` files where applicable. Verified-active roster + classification methodology: `PROME/ROSTER.md`.

**Operational context siloing.** Each agent's boot sequence loads only its own domain files plus the root operating rules; cross-agent coordination flows through `NEXUS_BRIEF.md` — a compressed write-once-read-many surface each agent emits at every closeout — rather than raw STATUS reads. The discipline is enforced by operational convention, not technology. That convention is the architectural answer to the context-window erosion that kills most multi-agent attempts: silos keep each agent coherent on its domain over months of operation; the brief layer carries the cross-agent synthesis at a compressed grain. Cost economics fall out — focused boot contexts keep every session cheap; a hard read-cap per boot surface (32,550 B) is enforced by script.

## Guided tour

**5 minutes:**

- This README
- `CLAUDE.md` — operating rules for any Claude Code session in this repo
- `PROME/CLAUDE.md` — chief-of-staff role; the "one Prome, files are truth" discipline
- `AGENTS/SAM/STATUS.md` — one representative domain agent (thesis version, decomposed probability model, calibration scoreboard)

**15 minutes:**

- `AGENTS/BRENT/CLAUDE.md` + `AGENTS/BRENT/TRADE.md` — full agent spec including the "anti-trades" discipline
- `AGENTS/VIOLET/MEMORY.md` — epistemic-discipline log (anchor naming, metric semantics, calibration corrections)
- `AGENTS/MARCO/MEMORY.md` — explicit characteristic-error catalog ("single-mechanism over-attribution")
- `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` — the cross-agent write-once-read-many surface, in spec form
- `PROME/ORCHESTRAL_LAYER_DESIGN.md` — coordination layer

**Depth:**

- `AGENTS/` — 33 active agents, each with own CLAUDE / STATUS / MEMORY tree (+ thesis/, TRADE.md where applicable)
- Multi-version thesis evolution in each agent's `thesis/CHANGELOG.md`
- Adversarial RED dialogue logs — e.g. `AGENTS/SAM/V16_RED_DIALOGUE.md`; the formal challenge corpus lives at `AGENTS/RED/challenges/`
- `AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md` — meta-agent specifying how to build a new agent. Recursive architecture in production.

## Why finance

Finance is the forcing function, not the point. Markets generate ground truth on a daily schedule — falsifiable outcomes, dated events, real cost to being wrong — which made finance the right domain in which to develop the methodology (pre-registration, calibration, adversarial verification, transmission-chain reasoning) the project actually exists to develop. The methodology generalizes to any empirical research problem with external data, dated events, and adversarially-verifiable claims.

## What's incomplete

A calibration-honest list, because the doc claims this discipline:

- **Serial, not distributed.** The auto-push and pathspec-commit protocols are tuned for ONE live machine at a time (desktop ⇄ laptop, switching checklist in `PROME/MACHINE_LOCAL.md`) with multiple concurrent Claude Code sessions on it. Two machines writing at once would require per-agent branches; the push gate refuses non-fast-forward pushes but the architecture is not built for concurrent writers.
- **Broker reconciliation is manual and lags.** Live position truth lives in operator broker exports; the parseable mirror (`FORGE/STATUS.md`) carries its own reconcile vintage in its header and stales between exports; it requires operator reconciliation before any trade-state inference.
- **No published P&L attribution.** The operation is calibration-graded (predictions ledgers, RED dialogue, scoreboards) but dollar-outcome attribution isn't externally audited and isn't claimed here.
- **Agent maturity varies.** `AGENTS/DAEDALUS/MATURITY_MAP.md` ranks the fleet against a structured rubric — some agents are mature, others earlier-stage. The map is a hygiene input, not a capability scoreboard.
- **Data-source hallucination is a tracked failure mode, not eliminated.** Root rule #3 — "Agent data can be hallucinated. Verify against SEC filings before trading. (PSEC PIK was 8.6%, not 35%.)" — encodes a real, repeated failure mode the calibration discipline is designed to catch.

## About

Working solo with LLMs since May 2025. Earlier experiments — persistent-memory + identity-continuity designs on ChatGPT and Claude.ai web UIs — developed the conceptual frame; the git-versioned multi-agent workflow in this repo formalized it starting February 2026. Every agent, protocol, and operational pattern was developed by iteration — failure → diagnosis → revised approach — with Claude as a build partner.
