# Root README revision — PROPOSAL (for Will's read; nothing touches README.md until his word)

**Drafted:** 2026-10-16 18:59 ET (prome-7b) · **Why:** the README is the front door for the fellowship application now that the full repository is offered alongside the demonstration repo. **Figures** are from the commands in the draft's own table, run at `385b0854d`; re-run them on the day of submission. **Root doc ⇒ Will-gated** (PROME/CLAUDE.md § Ask First).

**What changed against the 2026-10-02 README:** figures refreshed (10,200 → 18,563 commits; "33 active" → 34/5/2 from ROSTER; ledgers and findings added) · sections reordered (calibration → failure → architecture) · a five-stop reviewer route added before the deeper view · the demonstration repo cross-linked and the "operating, not curated" boundary stated · "each a Claude Code session" → two runtimes · a "right and wrong about" sentence with the demo's scored case · three limitations added (small numbers · process overhead measured · no external review) and one stated (positions visible) · a ten-term glossary · the My-role row and an authorship sentence in About · the context-siloing detail folded into How it works. Voice and the Why-finance section kept. **Things only Will can answer before publishing:** whether the Brier line (0.17 / 0.19 on fourteen rows, the demo's September figures) should be re-scored on today's ledger; whether the visible-positions limitation is the wording he wants; whether to name the two runtimes as "Claude Code and Codex".

---

# Research Workspace

Research Workspace is an empirical, multi-agent research system for tracking how stress moves through credit, energy, labor, housing, commodities, and capital markets.

It is also proof-of-work: a test of whether one operator without traditional research credentials can build rigorous empirical capability through sustained collaboration with frontier language models. Finance is the testbed because markets impose dated events, falsifiable outcomes, and a real cost for being wrong.

**This is the operating repository, not a curated one.** Nothing here is edited for a reader; it is the working state of the system as it stands at the latest commit, positions included. The curated companion, nine case studies with offline checks you can run, is [Selected Agents Open Demonstration](https://github.com/williepowen-debug/Selected-Agents-Open-Demonstration). Read that first if you have fifteen minutes; read this if you want to check it.

## At a glance

| | |
|---|---|
| **Operated** | since February 1, 2026: 18,563 commits on 253 of 258 days |
| **Scale** | 41 agents with live state files: 34 active, 5 spawned as needed, 2 dormant ([roster](PROME/ROSTER.md)); run as Claude Code and Codex sessions |
| **Forecasts** | 653 registered rows across 52 prediction ledgers, each with a threshold, a window and a resolution rule |
| **Failure record** | 487 catalogued failure findings, each a dated file naming what went wrong and what procedure changed |
| **Notes** | 207 daily session notes |
| **My role** | I designed and operate the system, set its direction and decision rules, and make every consequential call; agents produce the analysis, code and most of the prose under my direction |

Counts are from the commands below, run at commit `385b0854d` (2026-10-16 18:59 ET). Commit counts include automated state writes, so they measure activity, not quality.

| Metric | Command |
|---|---|
| Commits · commit-days | `git rev-list --count HEAD` · `git log --format=%ad --date=short \| sort -u \| wc -l` |
| Agents with live state | `ls AGENTS/*/STATUS.md \| wc -l` |
| Forecast rows · ledgers | `find AGENTS -name PREDICTIONS.tsv -exec awk 'FNR>1 && $0!~/^#/ && NF>2' {} \; \| wc -l` · `find AGENTS -name PREDICTIONS.tsv \| wc -l` |
| Failure findings | `ls memory/auto/finding_*.md \| wc -l` |
| Daily notes | `ls memory/2*.md \| wc -l` |

## Start here: a route for a reader with thirty minutes

Five stops, in order. Each line says what you will see and what it is evidence of.

1. **A scored forecast record.** [`AGENTS/BRENT/thesis/PREDICTIONS.tsv`](AGENTS/BRENT/thesis/PREDICTIONS.tsv), the energy desk's ledger, beside the demonstration repo's [case 9](https://github.com/williepowen-debug/Selected-Agents-Open-Demonstration/tree/main/cases/09_brent-calibration-record), which scores its resolved rows twice, on the current marks and on the first calls. You will see dated claims with probabilities, windows and outcomes, misses kept as misses. Evidence that forecasts are registered before outcomes and graded afterward.
2. **The failure catalogue.** [`memory/auto/`](memory/auto/) holds 487 files named `finding_*.md`; the index is [`INDEX_COLD.md`](memory/auto/INDEX_COLD.md). Open one: [`finding_adoption_is_not_validation.md`](memory/auto/finding_adoption_is_not_validation.md) or [`finding_record_of_an_action_is_not_the_action.md`](memory/auto/finding_record_of_an_action_is_not_the_action.md). Each names how a frontier model went wrong at a judgment, the dated instances, and the procedure that changed. Evidence that failure is classified rather than narrated.
3. **The rules forecasts must obey.** [`FORGE/PREDICTION_DISCIPLINE.md`](FORGE/PREDICTION_DISCIPLINE.md): how a threshold is specified so it cannot be re-tuned once the answer is visible, which mark a re-marked forecast is scored on, when a registered invalidation resolves a row. Every rule is one line and points at the failure that produced it. Evidence that method is written down and dated.
4. **The human overruling the system.** [`PROME/proposals/2026-09-25_wq299-prome-self-correction-reform-RULED.md`](PROME/proposals/2026-09-25_wq299-prome-self-correction-reform-RULED.md): the ruling that froze the coordinator's own rule growth after the system measured its overhead, with the authority model in [`PROME/AUTONOMY.md`](PROME/AUTONOMY.md) and the open decisions in [`PROME/WILL_QUEUE.md`](PROME/WILL_QUEUE.md). Evidence of where the human sits and that the system's complexity is a tracked cost, not an accident.
5. **One ordinary day.** [`memory/2026-10-16.md`](memory/2026-10-16.md), a session account, beside the fire ledger [`PROME/GATES.tsv`](PROME/GATES.tsv) and its rules [`PROME/GATES_README.md`](PROME/GATES_README.md). Evidence of what the operation does between the interesting days.

## What this project demonstrates

### 1. Calibration rather than narrative confidence

Most domain agents maintain pre-registered prediction ledgers with explicit thresholds, defined time windows, resolution criteria, CONFIRMED, FAILED and special-resolution outcomes, and failure-pattern tracking. Representative ledgers: [`AGENTS/SAM/thesis/PREDICTIONS.tsv`](AGENTS/SAM/thesis/PREDICTIONS.tsv) and [`AGENTS/BRENT/thesis/PREDICTIONS.tsv`](AGENTS/BRENT/thesis/PREDICTIONS.tsv).

What it has been right and wrong about so far is small in number and stated plainly: the energy desk's fourteen resolved binary forecasts score Brier 0.17 against a 0.25 chance baseline, and 0.19 on the marks as first written. Fourteen is suggestive, not proof.

The system does not claim to eliminate error or post-hoc reasoning. It attempts to catch, grade and learn from those failures.

### 2. Failure made classifiable

The 487 findings in [`memory/auto/`](memory/auto/) are the research asset. They are not a list of bugs. They are named failure modes of model judgment under real stakes, with instance counts where a mode recurred: a passing test mistaken for validation, a clean instrument pointed at the wrong referent, a correction pass carrying a higher defect rate than the work it corrected, a check that only advises being overridden downstream. The procedures in this repository are the residue of those findings.

### 3. An architecture in operational use

The system's git history records the development of specialist research agents, persistent memory, cross-domain synthesis, adversarial review and file-based coordination. The important claim is not that every design is novel. It is that these structures emerged through repeated use: failure, diagnosis, revision and another live test.

The architecture includes domain-specific ownership and persistent state, a signal-routing layer, cross-agent synthesis, formal adversarial review, pre-registered trade-construction rules, agent lifecycle management, scoped Git protocols for concurrent sessions, and fail-safe, non-force push handling. The verified roster lives in [`PROME/ROSTER.md`](PROME/ROSTER.md); the transmission topology in [`AGENTS.md`](AGENTS.md). Early operating history is in [`memory/2026-02-01.md`](memory/2026-02-01.md) and the dated briefings under [`archive/IRA/briefings/`](archive/IRA/briefings/).

## How the system works

Each specialist runs from its own directory and maintains a focused set of operating instructions, current state, durable memory, evidence and thesis history. A few roles organize the system:

- **PROME** coordinates priorities, decisions and operator-facing synthesis.
- **WALTER** ingests and routes signals and news.
- **NEXUS** synthesizes findings across domains.
- **RED** challenges theses and searches for falsifiers.
- **TERRY** converts research into proposed trade structures and risk rules. It does not execute trades.

Domain agents remain responsible for their own evidence and judgment. Agents load their own domain context rather than the entire repository; at closeout they publish compressed `NEXUS_BRIEF.md` files for cross-domain consumption, and boot-loaded files carry a script-enforced size cap. The isolation is maintained by operating convention and repository structure rather than by a distributed technical runtime.

## Why finance

Finance is the forcing function, not the endpoint. Markets provide public evidence, dated catalysts, measurable outcomes and adversarial feedback. That makes them a useful environment for developing a broader empirical method built around pre-registration, calibration, source verification, adversarial review, transmission-chain reasoning and explicit decision thresholds. The same method can apply to other research problems with external data and falsifiable claims.

## Known limitations

- **Small numbers.** The calibration record rests on a few dozen resolved forecasts per desk at most. It beats chance; it does not establish skill.
- **Process overhead is a measured cost.** The coordinator's rulebook grew faster than it earned its keep; a September ruling froze it and an October review cuts it. The record is in the ruling linked above. A reader who finds the procedure heavy is reading something the system also found.
- **Serial rather than distributed.** Multiple sessions can operate on the current machine, but only one machine should write at a time.
- **Broker reconciliation is manual.** Position truth remains with the operator and broker. [`FORGE/STATUS.md`](FORGE/STATUS.md) is a dated mirror and can be stale between reconciliations.
- **No externally audited performance.** The repository exposes calibration records and research process. It does not claim independently verified investment returns, and the book is small.
- **No external review yet.** The only reviewer so far is another model acting read-only. No human expert has audited the system.
- **Agent maturity varies.** [`AGENTS/DAEDALUS/FLEET_DIRECTORY.md`](AGENTS/DAEDALUS/FLEET_DIRECTORY.md) tracks the differences.
- **Source hallucination remains possible.** Trade-relevant claims require verification against primary sources. The system treats hallucination as a tracked failure mode, not a solved problem.
- **Positions are visible.** The operator's holdings and account state appear in the working files. That is deliberate: it is the ground truth the forecasts are scored against.

## Deeper view

- [`CLAUDE.md`](CLAUDE.md) and [`PROME/CLAUDE.md`](PROME/CLAUDE.md), the fleet-wide rules and the coordinator's charter. Dense by design; read after the route above.
- [`AGENTS/BRENT/CLAUDE.md`](AGENTS/BRENT/CLAUDE.md) and [`AGENTS/BRENT/TRADE.md`](AGENTS/BRENT/TRADE.md), a full domain specification and trade framework.
- [`AGENTS/VIOLET/MEMORY.md`](AGENTS/VIOLET/MEMORY.md) and [`AGENTS/MARCO/MEMORY.md`](AGENTS/MARCO/MEMORY.md), desk-level correction and characteristic-error tracking.
- [`AGENTS/RED/challenges/`](AGENTS/RED/challenges/), the adversarial-review corpus.
- [`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md`](AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md), the cross-agent synthesis interface.
- [`PROME/ORCHESTRAL_LAYER_DESIGN.md`](PROME/ORCHESTRAL_LAYER_DESIGN.md), coordination-layer design; [`AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md`](AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md), a specification for building a new agent.

## Glossary

- **Agent, desk:** one specialist with its own directory under `AGENTS/`, run as a model session. Its `STATUS.md` is its current state and the canonical truth for its domain.
- **PROME:** the coordinator. **WALTER:** signal routing. **NEXUS:** synthesis. **RED:** adversarial review. **TERRY:** trade construction.
- **Prediction ledger:** a `PREDICTIONS.tsv` file of dated, falsifiable claims with a confidence, a window and a resolution rule.
- **Gate:** a pre-registered trigger in `PROME/GATES.tsv` with a condition and a consequence. **FIRED / NOT FIRED:** whether its condition has been met on the named data.
- **DOCKET row, `L` number:** a dated obligation in `PROME/DOCKET.tsv`, cited by its line number.
- **WQ row:** a decision only the operator can make, numbered in `PROME/WILL_QUEUE.md`.
- **Finding:** a file in `memory/auto/` recording a failure mode and the procedure that changed.
- **HEARTBEAT:** the coordinator's dated regime memo. Never a source of current prices.
- **Packet:** a file one agent writes into another's `inbox/`. Coordination is file-based.
- **Boot, closeout:** the start and end procedures of a session, each with mechanical checks.

## About

This project grew from self-directed experiments with persistent memory and identity continuity in ChatGPT and Claude interfaces beginning in May 2025. The git-versioned multi-agent system took its current form in February 2026. I have a literature background and am self-taught across trading, systems design and AI orchestration. Every agent, protocol and workflow here was developed through iteration with AI as a research and systems-design partner; the direction, the decision rules and the failures in how it was built are mine.
