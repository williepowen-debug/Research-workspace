# Kernel Membrane Design Packet

**Date:** 2026-08-24

**Status:** DRAFT - concept and implementation plan for review; no live authority granted

**Revision:** v0.3 - architecture review and closeout refinements incorporated

**Last reviewed:** 2026-08-25

**Working name:** Kernel Membrane

**Proposed repository home:** `KERNEL/`

**Initial governed scope:** prospective forecast questions, forecasts, and resolutions only

**Operator:** Will

---

## 1. Decision this packet supports

Whether Research Workspace should add a small deterministic layer between flexible agent reasoning and durable institutional state, and, if so, what that layer must contain before any existing workflow is placed under its authority.

This packet proposes a target architecture and a bounded first implementation. It does **not** authorize creation of a live source of truth, migration of historical ledgers, retirement of existing messaging, or automated trading.

The core operating rule is:

> Agents decide what things mean. The kernel membrane guarantees that consequential state changes are attributed, authorized, evidence-linked, validly transitioned, routed, and preserved.

### Proposed rulings at a glance

The draft recommends, but does not yet authorize:

| Blocking decision | Recommendation |
|---|---|
| Domain model | Separate `Question`, `Forecast`, and `Resolution`; use "prediction" only as an umbrella term |
| First governed workflow | Prospective forecasting only; messaging remains outside membrane authority |
| Shadow direction | Native ledger first, then validated import into explicitly non-authoritative shadow events |
| Command acceptance | Agents submit from owned paths; a PROME-custodied v1 acceptor serializes membrane writes; Git does not coordinate commands |
| Evaluation | Freeze a `TrialManifest`, eligible-resolution target, arm coverage, and stopping rule before the cohort opens |
| Authority switch | Define and pass the switch gate before Phase 3; do not promote shadow history silently |

### Packet map

| Sections | Contents |
|---|---|
| 2-5 | Problem, testable claim, boundary, and principles |
| 6-9 | Architecture, repository placement, objects, commands, and events |
| 10-16 | Forecasting contracts, lifecycles, authority, evidence, obligations, views, and evaluation |
| 17-19 | CLI, Git/storage model, and relationship to existing systems |
| 20-22 | Delivery phases, verification, and risks |
| 23-26 | Design lineage, open decisions, first build slice, and review checklist |

---

## 2. Why this exists

Research Workspace already preserves unusually rich research history, predictions, challenges, decisions, and failures. Its weak point is that many important control loops remain cooperative: agents must remember the right procedure, update the right surface, notify the next owner, and later close the loop.

Documented repository failure classes include:

| Failure class | Current symptom | Membrane response |
|---|---|---|
| Canon drift | Repeated facts and rules disagree across surfaces | Store governed facts once; generate read views |
| Silent overwrite | Original forecast terms can be difficult to distinguish from later interpretation | Append amendments; never replace accepted events |
| Incomplete handoff | Delivery does not guarantee acknowledgement, disposition, or integration | Track communication separately from obligations and completion |
| Missed resolution | Predictions pass their resolver date without a visible next action | Create durable due work and an overdue exception |
| False closure | Work is called integrated without a canonical target or evidence | Enforce closure requirements |
| Concurrency blindness | Agents act from stale sibling state or collide on shared files | Stable identities, expected versions, one event per file, rebuildable views |
| Evaluation contamination | Forecast or grading rules are clarified after outcomes become visible | Preserve registration-time terms and version every later change |
| False green | A control passes outside its actual scan perimeter | Represent `UNKNOWN` separately from `PASS` |

The membrane is not intended to make the agents more intelligent. It is intended to make the institution more reliable and measurable.

---

## 3. The claim it must help test

The unresolved claim is:

> Does the coordinated Research Workspace process produce better-calibrated, more decision-useful forecasts than simpler alternatives after accounting for cost and coordination failure?

The membrane is useful only if it makes that claim testable. Forecast outcomes alone are insufficient. The system must also preserve challenge exposure, revisions, abstentions, annulments and legacy voids, missed handoffs, elapsed time, compute where measurable, and human intervention.

---

## 4. Scope boundary

### Inside the membrane

- Stable identities and roles
- Schemas and controlled vocabularies
- Command validation
- Permissions and separation of duties
- Legal state transitions
- Idempotency and concurrency checks
- Deadlines, dependencies, and required handoffs
- Evidence references and provenance
- Immutable accepted events
- Rebuildable current-state projections
- Evaluation-ready operational metadata
- Explicit overrides and exceptions

### Outside the membrane

- Research analysis and prose
- Whether a thesis is persuasive
- Whether evidence is substantively sufficient
- Causal synthesis and regime interpretation
- Source discovery
- Trade attractiveness and construction
- Hidden chain-of-thought or complete prompt transcripts
- Automatic trade execution

Markdown remains the primary research medium. The membrane governs only the structured administrative state surrounding consequential research judgments.

---

## 5. Design principles

1. **Canonical events are authoritative after the authority switch; current state is a projection.** Shadow events remain explicitly non-authoritative. No separately mutable current-state database becomes a second truth.
2. **Commands are requests; events are accepted facts.** Invalid requests produce no domain-state change.
3. **Accepted history is append-only.** Corrections, withdrawals, overrides, and amendments are new events.
4. **One event per file.** Writers add unique files instead of editing a shared event ledger, but semantic conflicts still require version-chain validation.
5. **Git is the durable archive, not a transaction coordinator.** Version 1 serializes command acceptance in the shared worktree. SQLite is a disposable local projection.
6. **Forward-only adoption.** Historical ledgers are parsed for analysis but not retrospectively rewritten.
7. **Common envelope, domain extensions.** Normalize identity, timing, confidence, and resolution without flattening domain semantics.
8. **Explicit unknowns.** Not checked, not covered, and insufficient evidence never render as healthy.
9. **Fail closed on governed writes.** Validation failure leaves prior valid state unchanged and explains the rejection.
10. **Human override remains possible and visible.** An override is a privileged event, not an invisible escape hatch.
11. **Traces are diagnostic, not canonical truth.** Only validated records cross into institutional state.
12. **The kernel stays small.** It encodes invariants, not the repository's analytical doctrine.
13. **Every command receives a durable receipt.** Rejection changes no domain state but remains visible for audit and cost measurement.
14. **Existing vocabularies are dependencies.** New machine-read states require an explicit crosswalk or a ratified vocabulary extension.

---

## 6. System shape

```text
Agents, humans, and services
             |
             | structured commands
             v
+-----------------------------------+
|          Kernel Membrane          |
|-----------------------------------|
| identity and authorization        |
| schemas and controlled vocabulary |
| deterministic transition rules    |
| evidence and closure requirements |
| idempotency and expected versions |
| routing, deadlines, dependencies  |
+-----------------------------------+
             |
             | accepted events
             v
   Shadow or canonical event history
             |
             +--> current-state views
             +--> open-obligation queue
             +--> exception/dead-letter view
             +--> agent status projections
             +--> evaluation dataset
             +--> disposable SQLite index
```

The membrane is a boundary, not a new analyst. It should be deterministic enough that identical accepted events always rebuild identical state.

---

## 7. Repository placement

The live subsystem, if ratified, should be neutral and top-level:

```text
KERNEL/
|-- README.md
|-- SPEC.md
|-- CHANGELOG.md
|-- schemas/
|   |-- command.schema.json
|   |-- command-receipt.schema.json
|   |-- event.schema.json
|   |-- question.schema.json
|   |-- forecast.schema.json
|   |-- resolution.schema.json
|   |-- trial-manifest.schema.json
|   |-- evidence.schema.json
|   `-- obligation.schema.json
|-- policies/
|   |-- permissions.yaml
|   |-- question-lifecycle.yaml
|   `-- resolution-policy.yaml
|-- registry/
|   |-- actor-mappings.yaml
|   |-- capability-grants.yaml
|   `-- forecast-families.yaml
|-- shadow/
|   `-- events/              # Phases 1-2; non-authoritative
|-- events/
|   `-- YYYY/                # Phase 3 onward; canonical
|       `-- MM/
|           `-- <event-id>.json
|-- audit/
|   `-- commands/            # Rejected-command receipts; accepted receipts are events
|-- views/
|   |-- OPEN_QUESTIONS.md
|   |-- RESOLUTION_QUEUE.md
|   |-- EXCEPTIONS.md
|   `-- CALIBRATION.tsv
|-- tools/
|   |-- rw.py
|   |-- submit.py
|   |-- accept.py
|   |-- validate.py
|   |-- replay.py
|   `-- render.py
|-- tests/
|   `-- fixtures/
`-- migrations/              # Replay migrations; never event rewrites

.rw/                         # gitignored and disposable
|-- projection.sqlite
|-- locks/
`-- logs/

scripts/rw                   # thin command shim
```

Why `KERNEL/`:

- Its institutional truth is not owned by PROME, RED, an individual domain agent, or `MESSAGING/`; operational custody is a separate, explicit role.
- It contains institutional contracts, shadow records, accepted state, and audit receipts, not research judgment.
- It matches the repository's top-level subsystem convention.
- It can later govern messaging adapters without being implemented inside messaging.

This design packet remains under `PROME/proposals/` until the location and authority model are ruled.

---

## 8. Object model

"Prediction" is an umbrella term in this packet, not a stored object. The target system separates the question being resolved, each actor's forecast, and the final outcome:

| Object | Purpose | Represented in v1? |
|---|---|---:|
| Actor | Stable human, agent, evaluator, or service identity | Yes |
| Evidence | Immutable reference to a source or research artifact | Yes |
| Question | Proposition, close terms, and objective resolution contract | Yes |
| Forecast | One actor's estimate for one question at one information cutoff | Yes |
| Resolution | Proposed and verified objective outcome for a question | Yes |
| TrialManifest | Frozen cohort, assignment, baseline, scoring, and cost protocol | Yes |
| Message | Communication from one actor to another | No - existing `MESSAGING/` remains authoritative |
| Obligation | Accountable requirement with owner, due condition, and closure rule | Derived only |
| Job | Scheduled or attempted execution of an obligation | No |

This separation is load-bearing. Several agents may forecast the same question; one agent may revise its forecast; and the question resolves once independently of those forecasts. Scores are calculated by joining forecast values to the verified question outcome.

Stable identifiers should reflect that separation:

```text
question_id     Q-...
forecast_id     F-...          # stable forecast series for one actor/question
forecast_version              # increments on amendment
resolution_id   R-...
trial_id        T-...
```

The target vocabulary is broader than the first implementation. Version 1 represents prospective forecasting and the identities, evidence, and trial contract required to evaluate it.

### Communication, obligation, and execution are different

These concepts must not be collapsed:

| Concept | Example |
|---|---|
| Communication | RED tells SAM that a resolver is ambiguous |
| Obligation | SAM must accept, reject, or amend by a named deadline |
| Execution | A SAM session attempts the required review |

One message may create several obligations. One obligation may require several attempts. A failed attempt does not close or erase the obligation.

---

## 9. Command and event model

Agents submit commands. The membrane either rejects the command without changing domain state or accepts it and emits an immutable event.

| Command | Accepted event |
|---|---|
| `RegisterTrial` | `TrialRegistered` |
| `FreezeTrial` | `TrialFrozen` |
| `RegisterQuestion` | `QuestionRegistered` |
| `AmendQuestionTerms` | `QuestionTermsAmended` |
| `SubmitForecast` | `ForecastSubmitted` |
| `AmendForecast` | `ForecastAmended` |
| `AttachEvidence` | `EvidenceAttached` |
| `CloseQuestion` | `QuestionClosed` |
| `ProposeResolution` | `ResolutionProposed` |
| `VerifyResolution` | `ResolutionVerified` |
| `DisputeResolution` | `ResolutionDisputed` |
| `WithdrawForecast` | `ForecastWithdrawn` |
| `AnnulQuestion` | `QuestionAnnulled` |
| `CorrectResolution` | `ResolutionCorrected` |
| `OverridePolicy` | `PolicyOverridden` |

Every command produces one durable receipt. For an accepted command, the accepted event envelope is also its receipt. A rejected command writes a `CommandReceipt` under `KERNEL/audit/commands/` containing the actor, writer and writer version, command hash, timestamp, policy version, and reason code but no domain event. A generated audit view unifies both forms. This preserves permission failures, stale writes, duplicate retries, and operational cost without requiring an unsafe two-file transaction or polluting domain state.

### Event envelope

Every accepted event should contain at least:

```text
event_id
stream_id
object_id
object_type
event_type
actor_id
writer_id
writer_version
effective_at
submitted_at
recorded_at
caused_by
correlation_id
command_id
command_result
expected_version
stream_version
previous_event_id
schema_version
policy_version
authority_mode
payload
evidence_refs
native_ref
```

`actor_id` owns the submitted judgment; `writer_id` and `writer_version` identify the acceptor implementation that recorded it. `recorded_at` is membrane-assigned UTC. `effective_at` is optional domain time and must never determine acceptance order. `command_id` makes retries idempotent, and an event's `command_result` is always `ACCEPTED`. `expected_version`, `stream_version`, and `previous_event_id` form the per-stream event chain. Question and resolution events share the question stream; each actor/question forecast series has its own forecast stream. `caused_by` and `correlation_id` preserve causality across streams. `authority_mode` is `SHADOW` or `CANONICAL`; shadow records must also carry an exact `native_ref`.

Version checks are meaningful only at a serialized acceptance point. Version 1 uses an exclusive repository-local command lock in the current shared-worktree, serial-machine operating model. If the repository later permits concurrent independent clones, commands must route through one acceptance writer or conflicting event branches must be quarantined during replay. Git alone cannot prevent two disconnected writers from both building from the same stream version.

### Submission and acceptance

Current Git canon does not permit domain agents to commit arbitrary shared-root files. Version 1 therefore separates:

1. **Submission:** an agent validates a command and writes the immutable request under an agent-owned submission path, such as `AGENTS/<NAME>/outbox/kernel/`.
2. **Acceptance:** the membrane custodian reads the request, acquires the command lock, replays the target stream, applies policy, and writes either the accepted event or rejected-command receipt.
3. **Attribution:** the event records both the research `actor_id` and the accepting `writer_id`; operational custody never changes authorship of the judgment.

The working recommendation is PROME as v1 operational custodian because PROME already owns shared coordination surfaces. Will remains policy authority, and the independent grader remains evaluation authority. PROME may accept or reject only by deterministic policy; it may not alter a submitted research payload. A later service can replace PROME as writer without changing command or event contracts.

---

## 10. Forecasting contracts

### Question contract

A question defines what the world will resolve, independently of who forecasts it:

```text
question_id
trial_id
supersedes_question_id
owner
registered_at
claim
outcome_type
forecast_family
opens_at
closes_at or close_condition
resolve_by or resolution_condition
resolver_anchor_type
resolution_rule
resolution_sources
fallback_resolution_source
ambiguity_rule
annulment_rules
resolver
independent_grader
falsifier
mechanism_question_refs
prerequisite_question_ref
schema_version
```

`resolver_anchor_type` must distinguish an immovable deadline from an expected event that can slip and from a deliberately chosen decision date. A negative resolution, such as "no filing appeared," must pre-register the search instrument and later carry a dated search attempt.

### Forecast contract

A forecast is one actor's estimate for one question at one information cutoff:

```text
forecast_id
question_id
forecaster
forecast_version
submitted_at
information_as_of
forecast_value
rationale_ref
evidence_refs
previous_forecast_event_id
intervention_stage
decision_consequence
schema_version
```

`intervention_stage` identifies whether the value is initial, post-challenge, post-synthesis, or a pre-registered final-cutoff forecast. An amendment creates a new immutable version. It never replaces or rescales the original value.

### Resolution contract

A resolution records the objective question outcome, not whether a particular forecast "won":

```text
resolution_id
question_id
outcome_value
proposed_by
proposed_at
resolution_evidence_refs
verification_status
verified_by
verified_at
dispute_reason
correction_of
schema_version
```

The evaluator joins each forecast version to `outcome_value` and applies the trial's scoring rule. `HIT` or `MISS` may be rendered for compatible legacy ledgers, but those labels are not the canonical objective outcome.

### Forecast families

The common envelope should not imply that every forecast can be pooled. Candidate families include:

- Binary event probability
- Categorical outcome probability
- Numerical point estimate
- Numerical interval
- Threshold-crossing event
- Conditional event with an explicit prerequisite and activation rule

A mechanism proposition should be a linked resolvable question, not an unscored note attached to a threshold forecast. Scores and comparisons remain family-aware. Threshold, direction, mechanism, and conditional activation outcomes must not be collapsed.

### Required registration terms

A question does not become `OPEN` until it references a frozen trial manifest and has:

- A stable claim that can be evaluated
- A close time or close condition
- A resolution condition and resolver anchor type
- Named resolution sources or authority
- A named owner, resolver, and any required independent grader
- A declared treatment for ambiguity, missing data, and annulment
- An exact search procedure for negative outcomes

A forecast is not accepted unless its question is `OPEN`, its information cutoff is no later than submission, and its value conforms to the question's family. Draft research remains unconstrained outside the membrane until these conditions are ready.

---

## 11. Lifecycles and outcome vocabulary

Draft questions and draft forecasts remain outside the membrane. A valid registration begins at `OPEN`; there is no intermediate `REGISTERED` state.

### Question workflow

```text
OPEN
  |-- close --------------------------> CLOSED
  |                                      |
  |                               propose outcome
  |                                      |
  |                                      v
  |                           RESOLUTION-PROPOSED
  |                              |             |
  |                           dispute        verify
  |                              |             |
  |                              v             v
  |                           DISPUTED        FINAL
  |                              |
  |                         revise proposal
  |                              |
  |                              +-----> RESOLUTION-PROPOSED
  |
  `-- permitted annulment -----------------> FINAL
```

`STUCK` is an exception condition when the registered instrument or resolution path cannot produce an answer. It is not a confidence reduction or a concealed terminal result. Repair requires a forward amendment where still legitimate, a new question, or an enumerated annulment.

Registered policy may annul a question from `OPEN`, `CLOSED`, `RESOLUTION-PROPOSED`, or `DISPUTED`, but never after `FINAL` except through a privileged resolution correction that preserves the earlier record.

### Forecast workflow

```text
ACTIVE -- amend --> SUPERSEDED + new ACTIVE version
ACTIVE -- withdraw -----------------------> WITHDRAWN
ACTIVE -- question closes ----------------> LOCKED
```

All forecast versions remain scoreable under the frozen trial rules. Withdrawal does not erase the submitted value.

### Objective outcome and legacy crosswalk

The question workflow and the outcome value are separate fields. A verified binary question resolves to `YES`, `NO`, `AMBIGUOUS`, or `ANNULLED`. Numerical and categorical questions use their registered outcome types.

The membrane must reconcile, not silently replace, the repository's existing prediction vocabulary in `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` and `FORGE/PREDICTION_DISCIPLINE.md`:

| Membrane fact | Legacy projection |
|---|---|
| Question remains open | `OPEN` |
| Verified binary outcome satisfies the forecast letter | `HIT` |
| Verified binary outcome defeats the forecast letter | `MISS` |
| Question annulled under a registered reason | `VOID (<reason>)` |
| Verified outcome is ambiguous | Apply the registered ambiguity rule; do not infer `HIT`, `MISS`, or `VOID` |
| Resolution instrument/window is broken | `STUCK` |

`CLOSED`, `RESOLUTION-PROPOSED`, `DISPUTED`, `FINAL`, `ACTIVE`, `SUPERSEDED`, `WITHDRAWN`, `LOCKED`, and the replay exception `CONFLICT` are proposed membrane workflow tokens. Phase 0 must register them as a distinct lifecycle vocabulary or replace them with already-ratified equivalents before implementation.

Rules requiring explicit ratification:

1. Question-term amendments are allowed only while `OPEN` and before the first forecast. After any forecast exists, a material term change creates a new question linked by `supersedes_question_id`.
2. Forecast-value changes and question-definition changes are different event types.
3. A material claim or resolver change creates a new question rather than laundering an existing forecast.
4. A binary question cannot be retrospectively relabeled `PARTIAL`; thesis nuance belongs in narrative evaluation.
5. A conditional prerequisite that never fires follows its registered activation and scoring rule; it is not automatically a miss.
6. `ANNULLED` requires an enumerated reason and cannot be used merely because forecasts performed poorly.
7. A final question is never reopened. A privileged correction emits `ResolutionCorrected`, retains the original resolution, and deterministically recomputes affected scores.

---

## 12. Identity, ownership, and authority

The actor registry should assign stable IDs and capabilities such as:

```text
question.register
question.amend_own
question.close
forecast.submit
forecast.amend_own
forecast.withdraw_own
resolution.propose
resolution.verify
resolution.dispute
evidence.attach
command.accept
policy.override
```

`actor-mappings.yaml` must not duplicate roster activity, responsibility class, or domain ownership. During shadow mode, `PROME/ROSTER.md` and existing ownership canon remain authoritative for those facts. The membrane registry supplies only stable actor IDs, actor types, canonical-name mappings, and membrane capabilities, with source references to the existing authority.

Recommended separation of duties:

| Responsibility | Default owner |
|---|---|
| Research judgment | Domain agent |
| Question terms | Question owner under the trial manifest |
| Forecast value | Forecasting actor |
| Adversarial challenge | RED or named reviewer |
| Objective resolution proposal | Named domain resolver |
| Resolution verification | Independent grader for trial cohort |
| Score calculation | Deterministic evaluator |
| Policy override | Will or explicitly delegated authority |

An agent's prompt cannot grant it authority. Authority comes from the registry and policy version active when the command is evaluated.

`command.accept` grants custody, not substantive discretion. The custodian may record a valid command or reject an invalid one with a deterministic reason code; it cannot rewrite the actor's payload, substitute a forecast, or verify an outcome merely because it operates the writer.

---

## 13. Evidence and provenance

An evidence reference should preserve:

```text
evidence_id
submitted_by
source_uri
artifact_repo_path
source_type
source_authority_class
published_at_or_data_as_of
retrieved_at
git_commit
content_hash
locator
access_class
note
```

The membrane should verify that a reference exists, is parseable, and satisfies the transition's provenance requirements. It should not decide whether the evidence is persuasive.

Version 1 treats evidence as a minimal provenance reference, not as a generalized evidence graph, claim ontology, or source-quality engine. Rich evidentiary reasoning remains in agent-authored research files. The membrane stores only what is required to identify the artifact and validate the requested transition.

For dynamic external sources, preserve the retrieved artifact where legally and operationally permitted; otherwise retain enough metadata and hashing to identify the exact observation. Repository paths require a Git commit or content hash. Secrets, credentials, private account data, and unrestricted prompt traces must never enter event payloads.

Resolution evidence should be stricter than ordinary supporting evidence. Trial-manifest rules identify which outcomes require independent verification. Resolution must use the registered source, a documented fallback, or an explicit override. A negative outcome also requires the pre-registered search instrument and a dated search attempt.

---

## 14. Scheduling, routing, and obligations

The first version may generate obligations as a projection without owning the full messaging workflow:

```text
QuestionRegistered
    -> question-contract review obligation, if required by trial

ForecastSubmitted
    -> challenge/review obligation, if assigned by trial

Question resolution condition reached
    -> resolution obligation

ResolutionProposed
    -> independent verification obligation

ResolutionVerified
    -> evaluation update
    -> dependent-agent notification candidates
```

Later versions can connect these obligations to `MESSAGING/` receipts and then to durable jobs. Routing should not become membrane-owned until the existing message cohort and the forecasting contracts both demonstrate stable semantics.

Required failure states include:

- Unacknowledged
- Blocked
- Overdue
- Failed attempt
- Dead-lettered
- Superseded
- Expired
- Rejected
- Completed with evidence

---

## 15. Projections and operator views

The first useful generated views are:

| View | Operator question |
|---|---|
| `OPEN_QUESTIONS.md` | Which questions are open and which forecasts attach to them? |
| `RESOLUTION_QUEUE.md` | What is due, overdue, proposed, or disputed? |
| `EXCEPTIONS.md` | What is blocked, invalid, stale, uncovered, or dead-lettered? |
| `CALIBRATION.tsv` | What can be scored without subjective recoding? |
| Agent current-state view | What must this agent know or do now? |
| Control-perimeter view | What did the latest check actually cover? |

Health must be at least three-valued:

| State | Meaning |
|---|---|
| `PASS` | Verified compliant inside the declared perimeter |
| `EXCEPTION` | Known violation or incomplete transition |
| `UNKNOWN` | Not checked, not covered, or insufficient evidence |

Views are disposable and must include their source event version or generation timestamp. A stale view may never silently outrank newer events.

---

## 16. Evaluation contract

The membrane should collect enough information to compare the coordinated process with simpler alternatives.

### Frozen trial manifest

Every cohort uses a `TrialManifest`. A retrospective mapping manifest freezes before its first import; a prospective trial manifest freezes before its first question opens:

```text
trial_id
protocol_version
evaluation_mode
question_eligibility
forecast_families
participants
treatment_arms
assignment_method
challenge_protocol
synthesis_protocol
forecast_cutoffs
primary_scoring_track
secondary_scoring_tracks
baseline_procedure
annulment_and_exclusion_rules
cost_measurement
minimum_followup
minimum_eligible_resolutions
minimum_per_arm
maximum_trial_duration
stopping_rule
frozen_at
```

`evaluation_mode` is `RETROSPECTIVE-MAPPING` or `PROSPECTIVE-TRIAL`. Phase 1 historical imports use the former and may test schema coverage, replay, and scoring reproducibility, but they cannot support preregistration or causal-performance claims.

Treatment assignment in a prospective trial may be randomized, matched, or observational, but the method must be declared. Observational challenge exposure can support descriptive comparisons; it cannot by itself establish that challenge caused an improvement.

Once `TrialFrozen` is accepted, the manifest is immutable. A protocol change creates a new manifest version. For a prospective trial it applies only to questions that have not opened; it never retroactively changes scoring for an active cohort. For retrospective mapping it begins a new declared import batch rather than rewriting prior mappings.

Calendar duration alone is not a stopping rule. A prospective trial should require both a minimum observation period and a minimum number of eligible, independently resolved forecasts, including pre-registered minimum coverage in each comparison arm. If the maximum duration arrives without sufficient coverage, the result is `INCONCLUSIVE`; the system must not manufacture a conclusion by pooling incompatible families or relaxing exclusions.

### Scoring tracks

All forecast versions remain preserved, but the manifest chooses the primary track before outcomes are known:

| Track | Purpose |
|---|---|
| Original as-made | Measures registration-time calibration and prevents revision credit from replacing the original record |
| Fixed post-intervention | Measures the forecast at a pre-registered point after challenge or synthesis |
| Latest pre-close | Measures the process's final actionable belief before the question closes |
| Revision delta | Compares forecast versions against the same outcome to measure whether a change helped or harmed |

No agent or evaluator may choose the best-performing forecast version after resolution. Time-weighted scoring, aggregation, or ensemble construction is permitted only if defined in the frozen manifest.

### Forecast outcomes

- Brier or log score where applicable
- Calibration by forecast family and confidence band
- Point/interval error for numerical forecasts
- Resolution timeliness
- Amendment, withdrawal, dispute, annulment, and legacy-void rates
- Mechanism, direction, threshold, and prerequisite outcomes kept separate

### Coordination effects

- Whether a forecast received challenge or synthesis
- Forecast at the registered pre- and post-intervention cutoffs
- Whether the revision improved or harmed the eventual score
- Time from challenge or evidence arrival to revision
- Duplicate or correlated agent contributions
- Failed, late, and ignored handoffs

### Cost and decision value

- Elapsed time
- Agent/session count
- Tokens or compute where reliably measurable
- Human interventions
- Files or sources consumed where practical
- Decision changed, avoided, delayed, or left unchanged
- Trade-construction rejection or execution frequency, without automatic execution

### Required baselines

The prospective trial should pre-register at least one simple baseline generated without access to the eventual outcome, such as:

- Base-rate forecast
- Naive persistence forecast
- Single-agent forecast without cross-agent challenge
- Initial forecast before challenge

Baseline values may live in the trial manifest or in separately timestamped baseline events; they should not be mandatory fields supplied by every forecaster. The evaluator must be independent from the agent whose performance it measures. Interim results should not be used to alter scoring, assignment, exclusion, or annulment rules inside the frozen cohort.

---

## 17. Interface sketch

```bash
scripts/rw question register question.yaml
scripts/rw forecast submit Q-123 forecast.yaml
scripts/rw forecast amend F-456 amendment.yaml
scripts/rw question close Q-123
scripts/rw resolution propose Q-123 evidence.yaml
scripts/rw resolution verify R-789

scripts/rw obligation list --agent SAM
scripts/rw system accept-pending --custodian PROME
scripts/rw system check
scripts/rw system exceptions
scripts/rw replay
scripts/rw render
```

Every state-changing command should support validation without writing:

```bash
scripts/rw question register question.yaml --check
```

Human-readable command input may use YAML. Canonical accepted events should use strict JSON validated against versioned schemas.

For ordinary agents, state-changing commands validate and create an immutable request in the actor's permitted submission path. Only a caller with `command.accept` processes pending requests into `KERNEL/`. The CLI should make `SUBMITTED`, `ACCEPTED`, and `REJECTED` visibly different outcomes.

---

## 18. Git and storage model

### Canonical

- During Phases 1-2, `KERNEL/shadow/events/` contains explicitly non-authoritative JSON events imported from exact native references.
- From the Phase 3 authority switch onward, `KERNEL/events/` contains one canonical JSON file per accepted event for newly governed trials, questions, forecasts, and resolutions.
- Events are partitioned by date for navigation, not by owner.
- Event IDs are sortable and globally unique across clones.
- Git commits provide durable provenance but are not substitutes for domain event IDs.
- Accepted event envelopes serve as accepted-command receipts; `KERNEL/audit/commands/` preserves rejected-command receipts without changing domain state.
- Shadow events are never silently copied or promoted into canonical history. The authority-switch ruling names the first canonical cohort and start time.

### Generated

- Markdown and TSV views are deterministic products of replay.
- SQLite is a disposable local index under `.rw/`.
- Deleting `.rw/` and rebuilding must reproduce current state exactly.
- Generated files must never be hand-edited.
- Projection migrations change replay or render logic; they never rewrite historical event files.

### Concurrency

- Version 1 acquires an exclusive `.rw/locks/command.lock`, replays the target stream, validates `expected_version`, and atomically writes either one accepted event or one rejected-command receipt before releasing the lock.
- `stream_version` plus `previous_event_id` exposes forks in the per-stream chain.
- Idempotency keys prevent duplicate events when commands retry.
- Atomic local writes prevent partial event files.
- CI or `rw system check` detects event-ID collisions, competing child events, invalid schemas, broken references, illegal transitions, audit gaps, and stale generated views.
- A forked stream enters `CONFLICT` quarantine and is omitted from ordinary current-state views until explicitly adjudicated; replay never chooses a winner from timestamp or filename order.
- If concurrent independent clones become part of the operating model, an exclusive local lock is insufficient. Commands must then route through a single acceptance writer or equivalent transactional service.

### Integrity boundary

Git history makes accidental edits visible but does not make files physically immutable. During shadow mode, CI detects modifications or deletions under event directories. Before Phase 3 authority, the repository must enforce additions-only event policy through the merge path or a single acceptance writer. Direct edits that bypass `rw` are governance violations until that enforcement exists.

Version 1 assumes cooperative actors and protects against accidental, stale, malformed, or unauthorized-by-policy operations. It does not protect against a malicious writer with direct filesystem and Git access, because that writer can fabricate an event that appears to have passed the CLI. Cryptographic provenance would require events signed by an isolated acceptance service whose key agents cannot access; that is outside v1 unless the threat model later requires it.

Canonical timestamps use UTC in RFC 3339 form. Actor-supplied domain times cannot establish event order. Schema and policy versions referenced by historical events remain replayable; a later schema release may add adapters but may not reinterpret or rewrite the accepted payload silently.

---

## 19. Relationship to existing repository systems

| Existing system | Initial relationship |
|---|---|
| Agent `PREDICTIONS.tsv` files | Remain authoritative during Phases 1-2; each shadow import cites the exact native row/artifact and source commit |
| `MESSAGING/` | Remains authoritative; supplies tested ownership, receipt, transition, and idempotency patterns |
| PROME docket/gates | Read-only inputs or comparison surfaces; no automatic migration |
| RED challenge records | Evidence and trial metadata; RED is not sole grader of RED's effect |
| LABOR scoreboard | Prototype scoring semantics to generalize, not replace retrospectively |
| Agent `STATUS.md` | Agent-authored truth remains; compact membrane views begin as non-authoritative projections |
| Git | Durable archive for shadow events and command receipts; canonical event store only after the Phase 3 authority switch |
| Existing check scripts | Inputs to an eventual unified verification lane; no false claim of full coverage |

The membrane should reuse working contracts. It should not launch a competing message system or rewrite forty-plus heterogeneous historical prediction ledgers.

### Native-first shadow procedure

1. The agent prepares structured question and forecast input and runs `rw ... --check`.
2. The agent records and commits the forecast on its existing authoritative native surface under the repository's existing ownership rules.
3. `rw shadow submit-import` validates the structured input against an exact native path/row and source commit, then writes a command request in the actor's owned submission path.
4. The custodian processes the request and emits an event with `authority_mode: SHADOW` and the required `native_ref`, or a durable rejection receipt.
5. Reconciliation compares the native record and shadow interpretation. Native state wins during Phases 1-2; discrepancies remain visible until corrected by a new native write and shadow amendment.

Where one native ledger row combines a question and its owner's forecast, the importer submits separate idempotent `RegisterQuestion` and `SubmitForecast` commands under one correlation ID. A crash between them leaves a visible incomplete import that can safely resume; it does not require a multi-file transaction. The shadow importer must refuse a missing or non-matching native reference. It does not independently create a second forecast fact. Phase 3 reverses the direction only for newly governed cohorts: canonical events become the source and legacy ledger representations become generated adapters or clearly marked non-authoritative views.

### Repository design lineage

This packet consolidates and narrows ideas already present in:

- [Shared-State Coordination Layer build plan](../../AUDITS/2026-06-09_shared_state_design.md), especially single-writer ownership, append-only events, generated views, and the boundary between shared facts and agent judgment
- [System Analysis Report v2](../../AUDITS/2026-07-22_system_analysis_report_v2.md), especially prospective prediction normalization, independent evaluation, exception views, and contract-gated durable execution
- [System Report Dispositions](../../AUDITS/2026-07-25_system_report_DISPOSITIONS.md), especially forward-only adoption and the merged open-obligation/exception projection
- [Direct Messaging v1 specification](../../MESSAGING/DIRECT_MESSAGING_V1_SPEC.md) and [design rationale](../../MESSAGING/DESIGN_RATIONALE.md), especially recipient ownership, append-only receipts, explicit dispositions, idempotency, and fail-closed cohorting
- [State Vocabulary](../../AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md) and [Prediction Discipline](../../FORGE/PREDICTION_DISCIPLINE.md), whose current prediction-state mismatch must be reconciled before a new membrane vocabulary is registered

The new design choice is to make immutable events the eventual canonical question, forecast, and resolution history while retaining Markdown and TSV as readable research surfaces and generated views.

---

## 20. Delivery plan

### Earned maturity path

The membrane should earn scope in three distinct stages:

| Stage | Phases | What it is |
|---|---:|---|
| Evaluation ledger | 1-2 | Non-authoritative measurement instrument for questions, forecast versions, resolutions, costs, and discrepancies |
| Governed forecast registry | 3 | Canonical source for newly governed forecasting cohorts after operational reliability is demonstrated |
| Operational membrane | 4-5 | Broader obligations, messaging bridges, and durable scheduling only after measured usefulness justifies expansion |

Operational reliability and forecasting superiority are different decisions. Phase 3 may be justified if the registry produces substantially cleaner, cheaper, and more auditable forecast records even when the performance experiment remains statistically inconclusive. Expansion into Phases 4-5 requires separate evidence that the added coordination machinery produces value exceeding its burden.

### Advance and stop gates

Before the prospective cohort opens, the frozen manifest must assign numerical thresholds or explicit adjudication rules for:

- Minimum eligible resolutions overall and per comparison arm
- Maximum missing required-field rate
- Maximum unresolved native-shadow discrepancy rate
- Maximum event-stream conflict rate
- Resolution and independent-verification timeliness
- Command acceptance latency and custodian queue age
- Human intervention and operating-cost ceiling
- Maximum trial duration and treatment of an underpowered result

If operational thresholds fail, simplify or stop rather than promoting the membrane. If sample sufficiency fails at maximum duration, publish `INCONCLUSIVE` and retain the frozen protocol; do not pool incompatible forecast families, relax exclusion rules, or tune thresholds against observed outcomes.

### Phase 0 - Ratify the contract

Deliverables:

- Agree on scope and non-goals
- Freeze the `Question` / `Forecast` / `Resolution` separation
- Freeze forecast families for v1
- Define the question and forecast state machines
- Define amendment, annulment, legacy-void projection, dispute, and correction rules
- Reconcile `STATE_VOCABULARY.md` with `PREDICTION_DISCIPLINE.md` and register any new lifecycle tokens
- Freeze the trial manifest: cohort, assignment, scoring tracks, resolvers, graders, baselines, cost measures, sample requirements, and stopping rule
- Choose event ID and timestamp rules
- Ratify serialized acceptance and conflict-quarantine behavior
- Ratify PROME's narrow v1 custodian role, the required shared-path Git carve-out, and the agent-owned command-submission path

Exit gate:

- A set of fixture cases can be modeled and graded unambiguously by two independent readers, and the same events replay to the same state.

### Phase 1 - Non-authoritative shadow prototype

Deliverables:

- Create the `KERNEL/` shadow skeleton, schemas, agent-owned submission adapter, serialized custodian acceptance, durable receipts, replay engine, fixtures, and tests
- Freeze a `RETROSPECTIVE-MAPPING` manifest and parse selected existing ledgers without changing them
- Generate open, overdue, and calibration shadow views
- Report disagreements rather than resolving them automatically

Exit gate:

- Replay is deterministic; the parser correctly represents the agreed sample; retrospective outputs carry no prospective or causal claim; rejected commands leave durable receipts; no existing authority changes.

### Phase 2 - Prospective shadow cohort

Deliverables:

- Record a small frozen cohort on native authoritative surfaces, then import exact native references through structured shadow commands
- Store shadow events only under `KERNEL/shadow/events/`
- Capture challenges, revisions, resolution evidence, operational failures, and costs
- Compare native and membrane state every cycle

Exit gate:

- The frozen stopping rule is met with sufficient eligible resolutions and arm coverage, and the pre-registered missing-data, conflict, discrepancy, timeliness, and burden gates pass. Otherwise the outcome is an explicit extension, simplification, stop, or `INCONCLUSIVE` result under the frozen rules.

### Phase 3 - Forecast authority

Deliverables:

- Make accepted events authoritative for new cohort questions, forecasts, and resolutions
- Generate human-readable question and forecast views
- Enforce additions-only event integrity and semantic validation through the merge path; require broker signatures only if the threat model expands beyond cooperative actors
- Add CI validation for governed files, command receipts, version chains, and transitions
- Preserve native research files as narrative surfaces

Exit gate:

- No material state requires hand reconciliation for the agreed observation window, and the authority-switch ruling names its cohort and exact start time.

### Phase 4 - Messaging and obligations bridge

Deliverables:

- Map existing message receipts to obligation events
- Produce a unified open-work and exception projection
- Preserve existing inbox readability during transition

Exit gate:

- No obligation is falsely closed; known late, blocked, superseded, and unresolved fixtures are detected.

### Phase 5 - Durable scheduling, only if warranted

Deliverables:

- Scheduled resolver checks and durable retries
- Job attempts, retry policies, and dead-letter handling
- Human approval pauses where policy requires them

Exit gate:

- Demonstrated need exceeds what cron plus exception views can reliably provide.

No Temporal, LangGraph, hosted state service, or other durable runtime is required before Phase 5.

---

## 21. Verification strategy

### Unit and property tests

- Every legal and illegal question, forecast, and resolution transition
- Duplicate command idempotency
- Stale `expected_version` rejection
- Competing-child fork detection and quarantine
- Exclusive-lock behavior under concurrent local commands
- Actor permission boundaries
- Evidence requirements
- Durable accepted and rejected command receipts
- Additions-only accepted event integrity
- Deterministic replay
- Schema-version compatibility
- Explicit clock injection for date-sensitive tests

### Adversarial fixtures

- Forecast amended after question close
- Question terms materially changed after a forecast exists
- Resolver changed after outcome visibility
- Duplicate event ID
- Same command submitted twice
- Two actors race from the same version
- Two event files claim the same parent version
- Resolution without registered evidence
- Owner attempts to verify own protected outcome
- Prerequisite never fires
- Ambiguous source result
- Annulment used to conceal a poor forecast
- Negative resolution lacks a dated search attempt
- Shadow import lacks an exact native reference
- Generated view is stale or hand-edited
- Check has incomplete perimeter

### Shadow verification

- Manual and generated open counts match
- Every discrepancy has a named classification
- Every shadow event carries `authority_mode: SHADOW` and an exact native reference
- Native and membrane question and forecast terms match at import
- Every `native_ref` source commit exists and its referenced content matches
- Recorded timestamps use the injected UTC clock and never rely on Git commit order
- Rebuild from an empty `.rw/` produces byte-stable outputs where designed

---

## 22. Risks and controls

| Risk | Control |
|---|---|
| A second source of truth | Native-first import; `SHADOW` authority field and banner on every Phase 1-2 event/view |
| Over-structuring research | Restrict schemas to administrative invariants |
| False comparability | Forecast families and family-specific scoring |
| Agents register only easy forecasts | Track coverage, abstention, and forecast-family mix |
| Retrospective specification | Immutable original terms and versioned amendments |
| Evaluator conflict of interest | Independent grader and deterministic scoring |
| Selection bias mistaken for challenge benefit | Frozen trial arms and assignment method; label observational comparisons honestly |
| Git semantic race | Serialized v1 acceptance; version chains and fork quarantine; central writer if independent clones arrive |
| Custodian becomes a substantive gatekeeper or bottleneck | Custodian cannot alter payloads; deterministic reasons only; track queue age and acceptance latency |
| Actor/ownership registry drift | Store only stable ID/capability mappings and cite existing roster/ownership authority |
| Generated-view drift | Replay check and prominent generation metadata |
| Operational burden exceeds value | Measure human intervention, elapsed time, and failure rates |
| Kernel grows into a platform | Phase gates and an explicit non-goal list |
| Sensitive trace capture | Store minimal validated events; keep diagnostic traces separate |
| Governance bypass | Begin with detection in CI; enforce writes only after shadow validation |

---

## 23. Concepts borrowed, not platforms adopted

| Source concept | Membrane use |
|---|---|
| Event sourcing / CQRS | Immutable events, validated commands, rebuildable projections |
| Durable workflows | Idempotency, retries, deadlines, resumable work, approval waits |
| Agent runtimes | Structured handoffs, guardrails, traces, state inspection |
| Agent governance | Stable identity, registry, capability-based permissions, audit |
| Forecasting platforms | Frozen terms, close/resolution rules, resolver authority, scoring |

Relevant primary references:

- Microsoft Azure Architecture Center, [Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
- Temporal, [Documentation](https://docs.temporal.io/)
- LangGraph, [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- OpenAI Agents SDK, [Tracing](https://openai.github.io/openai-agents-python/tracing/)
- Microsoft, [Agent 365 governance and auditability](https://learn.microsoft.com/en-us/windows-365/agents/governance-auditability)
- Metaculus, [Question writing](https://www.metaculus.com/question-writing/) and [FAQ](https://www.metaculus.com/faq/)

The proposed contribution is not inventing those mechanisms. It is applying them to an epistemic workflow that preserves what was believed, when, under what terms, what changed it, who resolved it, and whether coordination improved the result.

---

## 24. Decisions required before implementation

| # | Decision | Working recommendation | Status |
|---:|---|---|---|
| 1 | Repository home | Root-level `KERNEL/` | RATIFIED 2026-08-25 |
| 2 | Initial governed objects | `Question`, `Forecast`, `Resolution`, plus required Actor/Evidence/TrialManifest support | RATIFIED 2026-08-25 |
| 3 | Shadow authority | Native ledger first; exact-reference import to `KERNEL/shadow/events/` | RATIFIED 2026-08-25 |
| 4 | Canonical authority | Git event files for cohorts beginning after the Phase 3 switch | RATIFIED 2026-08-25 |
| 5 | Command acceptance | Exclusive local serialization under the current operating model | RATIFIED 2026-08-25 |
| 6 | Future multi-clone model | Single acceptance writer; do not treat Git merge as a transaction | RATIFIED 2026-08-25 |
| 7 | Event granularity | One chained JSON file per accepted event | RATIFIED 2026-08-25 |
| 8 | Command audit | Durable receipt for every accepted or rejected command | RATIFIED 2026-08-25 |
| 9 | Local projection | Disposable SQLite under `.rw/` | RATIFIED 2026-08-25 |
| 10 | Historical migration | None; read-only parsing only | RATIFIED 2026-08-25 |
| 11 | Lifecycle vocabulary | Ratify membrane workflow tokens and crosswalk existing prediction vocabularies | OPEN |
| 12 | First forecast families | Binary, threshold, and conditional; numerical interval only if the cohort requires it | OPEN |
| 13 | Trial contract | Freeze assignment, scoring tracks, baselines, exclusions, and costs before opening | OPEN |
| 14 | Independent grader | Name per trial; forecast owner cannot verify protected outcomes alone | OPEN |
| 15 | Trial stopping rule | Minimum duration plus eligible-resolution and per-arm counts; maximum duration yields `INCONCLUSIVE`, not relaxed rules | OPEN |
| 16 | Messaging sequence | Reuse patterns now; bridge after the forecast shadow trial | OPEN |
| 17 | Generated views in Git | Decide whether committed snapshots are required for cross-session consumption | OPEN |
| 18 | Runtime escalation | No durable engine until contract stability and need are demonstrated | OPEN |
| 19 | Authority switch gate | Define acceptable discrepancy, conflict, and missing-data rates before Phase 3 | OPEN |
| 20 | Threat model | Cooperative-actor integrity in v1; defer cryptographic signing unless direct-write adversaries enter scope | OPEN |
| 21 | Operational custody | PROME accepts/rejects v1 requests by deterministic policy under a narrow `KERNEL/` Git carve-out; Will owns policy authority | OPEN |
| 22 | Expansion gate | Phases 4-5 require measured coordination value above burden, separate from the Phase 3 integrity gate | OPEN |

### Ratified rulings

Will ratified decisions 1-5 on 2026-08-25:

1. **Repository home:** The live subsystem will use neutral root-level `KERNEL/` placement. Will retains policy authority; operational custody does not make the kernel PROME-owned.
2. **Initial governed objects:** Version 1 will govern `Question`, `Forecast`, `Resolution`, and `TrialManifest`, with Actor and Evidence as required supporting records. Messaging, theses, and general workflow remain outside the first governed boundary.
3. **Shadow authority:** During shadow phases, native ledgers remain authoritative. Shadow events are explicitly non-authoritative, reference exact native records, and surface discrepancies rather than silently repairing them.
4. **Canonical authority:** After an explicit Phase 3 authority switch, one-file-per-event Git history becomes canonical only for admitted prospective cohorts. Historical ledgers are not rewritten, and SQLite remains a rebuildable projection rather than a second authority.
5. **Command acceptance:** Version 1 uses one exclusively locked local acceptance process. Agents submit immutable commands; PROME applies deterministic accept/reject policy; every command receives a durable receipt; attribution remains with the research actor.

These initial rulings authorized specification work within the stated boundaries. They did not create `KERNEL/` or activate a trial, and decisions 6-22 remained open at that point.

Will ratified decisions 6-10 on 2026-08-25:

6. **Future multi-clone model:** If independent clones enter the operating model, all commands must route through one acceptance writer or equivalent transactional point. Git merge is not a transaction mechanism; fork detection and quarantine remain mandatory defensive controls.
7. **Event granularity:** Each accepted event is stored as one immutable JSON file chained by stream version and previous event ID. Date partitioning aids navigation but never determines semantic order.
8. **Command audit:** Every command leaves a durable result. An accepted event envelope doubles as its receipt; a rejected command produces a standalone receipt without changing domain state; a generated audit view unifies both forms.
9. **Local projection:** SQLite under gitignored `.rw/` is a disposable local index only. Deleting it and replaying the same events must reproduce identical state; it never becomes canonical or committed.
10. **Historical migration:** Existing ledgers will not be converted into canonical history. Read-only, provenance-preserving retrospective mappings may test compatibility and scoring reproducibility, but remain non-authoritative and support no preregistration or causal-performance claim.

Together, decisions 1-10 establish the system boundary, authority progression, write path, durable storage, and historical treatment. They still do not create `KERNEL/`, activate a trial, or settle decisions 11-22.

---

## 25. Proposed first build slice

If the decisions above are ratified, the first code slice should contain only:

```text
KERNEL/
|-- README.md
|-- SPEC.md
|-- schemas/
|   |-- command.schema.json
|   |-- command-receipt.schema.json
|   |-- event.schema.json
|   |-- question.schema.json
|   |-- forecast.schema.json
|   |-- resolution.schema.json
|   |-- evidence.schema.json
|   `-- trial-manifest.schema.json
|-- policies/
|   |-- permissions.yaml
|   |-- trial-lifecycle.yaml
|   |-- question-lifecycle.yaml
|   `-- resolution-policy.yaml
|-- registry/
|   |-- actor-mappings.yaml
|   |-- capability-grants.yaml
|   `-- forecast-families.yaml
|-- shadow/
|   `-- events/
|       `-- .gitkeep
|-- audit/
|   `-- commands/
|       `-- .gitkeep
|-- views/
|   `-- .gitkeep
|-- tools/
|   |-- rw.py
|   |-- submit.py
|   |-- accept.py
|   |-- replay.py
|   `-- render.py
`-- tests/
    |-- fixtures/
    |-- test_trial_manifest.py
    |-- test_submission_acceptance.py
    |-- test_question_lifecycle.py
    |-- test_forecast_versions.py
    |-- test_evidence_requirements.py
    |-- test_permissions.py
    |-- test_idempotency.py
    |-- test_conflict_detection.py
    `-- test_replay.py

scripts/rw                    # thin CLI shim
.gitignore                    # add `.rw/`
```

The slice should prove nine things before adding features:

1. A mapping manifest freezes before import, a prospective manifest freezes before its first question opens, and neither can be retroactively edited.
2. An ordinary agent can submit from its owned path but cannot directly accept into `KERNEL/`.
3. A valid native question and forecast can be imported into shadow state with an exact source reference.
4. Invalid, unauthorized, or insufficiently evidenced transitions are rejected without changing domain state.
5. Accepted and rejected commands both leave durable receipts.
6. Retried commands do not duplicate events.
7. Competing children of one event version are quarantined rather than ordered arbitrarily.
8. Replay reconstructs the same question, forecast versions, and resolution state deterministically.
9. Shadow history can generate an open-question view with an explicit non-authoritative banner.

No generalized evidence graph, source-quality engine, message migration, job scheduler, hosted service, agent-status generator, dashboard framework, or broad historical conversion belongs in that slice.

---

## 26. Review checklist

- [ ] The purpose and non-goals are correct.
- [ ] `KERNEL/` is the right neutral home.
- [ ] Question, Forecast, and Resolution are the right first governed objects.
- [ ] Their envelopes are sufficient but not over-specified.
- [ ] Forecast families preserve important domain distinctions.
- [ ] The lifecycle and outcome crosswalk handle amendment, dispute, correction, withdrawal, annulment, and `STUCK` correctly.
- [ ] Authority and separation-of-duty rules match actual operating practice.
- [ ] Shadow mode cannot create an ambiguous second truth.
- [ ] Command serialization and fork quarantine match the actual Git operating model.
- [ ] The trial manifest prevents retrospective selection of scoring versions or baselines.
- [ ] The stopping rule requires sufficient eligible resolutions and comparison-arm coverage, not duration alone.
- [ ] The prospective evaluation can test calibration **and** coordination cost.
- [ ] Phase 3 operational authority and Phases 4-5 scope expansion use separate evidence gates.
- [ ] The first build slice is small enough to discard or revise cheaply.

---

## Bottom line

Research Workspace already has most of the behavioral ingredients: durable files, agent ownership, prediction ledgers, adversarial challenge, messaging receipts, Git provenance, and retained failures. The membrane should not replace those strengths. It should turn their most consequential administrative rules into a small deterministic contract.

The recommended first move is not to build a general research operating system. It is to build an evaluation instrument: freeze the Question/Forecast/Resolution and TrialManifest contracts, implement native-first shadow events with durable command receipts and deterministic replay, and run a cohort bounded by both time and eligible resolution count. Operational evidence may justify a Phase 3 forecast-registry authority switch; only separate evidence of coordination value above burden should justify expansion into messaging, obligations, scheduling, or broader state governance.
