\# Research Workspace Evaluation

\*\*Repository:\*\* \`williepowen-debug/Research-workspace\`
\*\*Evaluation date:\*\* 2026-08-24
\*\*Scope:\*\* Read-only review of the checked-out GitHub repository, including architecture, governance, representative agent lifecycles, historical calibration, tooling, tests, and operational controls.

\#\# Follow-up update — 2026-08-25

This section records a bounded, read-only reconciliation against current \`master\` one day after the original evaluation. It preserves the August 24 assessment as a point-in-time record rather than silently rewriting it. The checkout was clean and exactly aligned with \`origin/master\` at commit \`b3ecce501\` when these checks were run. No operational cursors were advanced and no repository files were modified.

\#\#\# Findings confirmed

The original report's main conclusions remain supported.

\- **Fleet-wide evaluation is still blocked by structural heterogeneity.** The current tree contains 44 \`PREDICTIONS.tsv\` files in total. Excluding paths explicitly under \`archive/\` or \`_archive/\` leaves 38 live-path ledgers. Their first tabular header rows reduce to **18 exact header shapes**. Differences include identifier names, made/resolution date fields, resolver fields, falsification fields, confidence representation, and whether outcome and status are distinct.
\- **Status diversity is not merely cosmetic.** A bounded mechanical pass over the 38 live-path ledgers found 467 non-empty cells under columns named \`Status\` or \`status\`, containing **78 distinct literal strings**. These include simple states such as \`OPEN\`, \`CONFIRMED\`, and \`FAILED\`; compound judgments; retirement and transfer states; narrative sentences embedded in the status field; and at least two date-like values. This confirms both vocabulary heterogeneity and row-shape/parsing ambiguity. A normalized evaluator cannot safely infer one state machine from these files without explicit adapters and a reviewed mapping contract.
\- **Several ledgers are not ordinary header-first TSV files.** Representative files begin with extensive comment preambles, while others use a header on line one. A robust inventory reader must deliberately skip comments and blanks, identify the actual schema row, preserve preamble provenance, and fail visibly when a row does not match the detected shape.
\- **Repository-wide automated verification is still absent.** \`.github/workflows/feeds.yml\` remains the only workflow found. It is manually triggered, performs a live feed fetch, may commit and push results, and does not run the repository's validators or unit tests.
\- **Test discovery remains fragmented.** On 2026-08-25, \`python3 -m unittest discover -s MESSAGING/tests -p 'test*.py'\` ran 22 tests and all passed. In contrast, \`python3 -m unittest discover -s AGENTS -p 'test*.py'\` discovered zero tests and exited non-zero. The messaging subsystem therefore remains the clearest tested component, while there is still no centrally discoverable agent test lane.
\- **The VIOLET time-sensitive test remains broken.** Direct execution of \`AGENTS/VIOLET/scripts/test_daily_log.py\` passed its first 16 printed checks, then failed with \`IndexError: list index out of range\` in check 8. This updates the failure symptom but not the conclusion: the test is still date-sensitive/non-hermetic and cannot serve as a stable CI control until time is injected and temporary fixtures are isolated from the wall clock.

\#\#\# Current canon reconciliation

The active roster now reports **33 active agents**, while the root \`README.md\` still describes the system as having **21 active agents** in multiple places. The README is therefore confirmed stale as a public/navigation surface, not merely slightly behind.

Root \`AGENTS.md\` contains a live internal contradiction involving FERT. The transmission-chain rule near the top states that potash belongs to FERT at triage depth and says the old “potash is UNOWNED” language is kill-on-sight. The later FERT routing-table row still describes potash as \`EXCLUDED-UNOWNED\`. This is direct evidence that annotated corrections do not reliably eliminate a stale mirrored claim elsewhere in the same canonical document.

The repository is also continuing to evolve faster than static descriptions. Since the original report's snapshot, the visible active tree includes newer lanes such as FLG and CRUISE, and the recent commit history records live operational correction work. This strengthens the recommendation to generate roster counts and other high-churn navigation views from one source of truth.

\#\#\# Prediction compatibility inventory — structural pass

The 38 live-path ledgers fall into six practical compatibility classes. These are ingestion classes, not judgments about research quality.

| Class | Representative files | Compatibility assessment |
|---|---|---|
| Standard nine-column family | LABOR, LIQUID, MARCO, SAM, HANS | Common identity/date/claim/confidence/timeframe/status/resolution fields; no dedicated resolver, falsifier, probability-vintage, or grader fields. |
| Extended invalidation family | CARL, BRENT, HAWK, OSPREY, OZK, RED, REGINALD, WAL | Adds an invalidation field, but status and confidence semantics still vary and several files carry large comment preambles. |
| Explicit-deadline family | BROCK, OTTO, CREED, HOMER, FERT, ZHAO | Carries a deadline-like field under several names; resolution criteria, falsifiers, and result fields remain inconsistent. |
| Typed newer family | MIDAS, VULCAN, WATT | Lower-case typed layout with channel, resolve date, confidence tier, falsifier, criteria, and resolution; closer to a canonical event record but confidence tier is not probability. |
| Sub-agent compact family | MARCO sub-agents | Omits made-at provenance and dedicated outcome/falsifier fields; one ledger has demonstrated shifted rows. |
| Bespoke/minimal | AEOLUS, BOND, HENRY, CRUISE | Agent-specific layouts. HENRY has only five fields and no confidence or made-at column; AEOLUS and BOND include explicit criteria but differ from the rest. |

Across the 38 headers, 37 expose a confidence-like column and 32 expose a made-at-like column. Only 21 expose a dedicated falsifier/invalidation-like column, and only 5 expose a dedicated resolution-criteria/criteria column. Deadline-like fields exist under multiple names in a minority of files. No inspected ledger header carries all of the proposed canonical fields, and none provides a dedicated \`grader\` or \`evidence_commit\` column.

The confidence field is not safely coercible to probability. Observed values include ordinary percentages, percentages annotated as “at resolution,” percentages carrying an earlier value in prose, \`PROVISIONAL\`, \`EMPIRICAL\`, \`ASSUMPTION\`, 4/5 and 5/5 conviction scores, unstated values, em dashes, and multi-branch probability narratives in a single cell. A percentage parser would therefore mix as-made probabilities, current re-marks, retrospective labels, and non-probabilistic epistemic tiers.

The structural scan also found a concrete row-shape defect in \`AGENTS/MARCO/sub_agents/TOURISM/workbook/PREDICTIONS.tsv\`. Rows TOUR-02 and TOUR-04 contain six tab-separated fields against a seven-column header. Their missing confidence cells shift \`RESOLVED\` into the confidence column and the resolution date into status. This explains two of the date-like values observed in the global status vocabulary and demonstrates that permissive parsing can silently manufacture false data.

\*\*Safe automatic mappings at this stage:\*\* source path, owning directory, raw prediction ID, raw claim text, detected header, raw row, and Git blob/commit provenance. These can be preserved without interpretation.

\*\*Conditionally mappable with per-family adapters:\*\* made-at date, current status, resolution date, outcome narrative, deadline, falsifier, and criteria. Each requires header-family rules plus row-width validation.

\*\*Unsafe to normalize without a human-approved semantic contract:\*\* probability, as-made versus current confidence, success/failure outcome, void versus retirement versus transfer, mechanism versus threshold result, amendment lineage, resolver identity, and grader independence.

The evaluator should retain both \`raw_value\` and \`normalized_value\`, attach the mapping-rule version, and refuse scoring whenever a required semantic field is missing, shifted, ambiguous, or retrospectively overwritten.

\#\#\# Draft evaluation contract v1 — for prospective shadow mode

The compatibility evidence supports an event model rather than another mutable master table. The durable record should be append-only JSON Lines validated by JSON Schema; SQLite and Markdown dashboards should be disposable projections rebuilt from that stream. Existing agent ledgers remain authoritative during the pilot.

Every event should carry a common envelope:

\`schema_version\`, \`event_id\`, \`event_type\`, \`prediction_id\`, \`occurred_at\`, \`recorded_at\`, \`actor\`, \`owning_agent\`, \`source_path\`, \`source_commit\`, \`prior_event_id\`, and \`notes\`.

The allowed v1 event types should be deliberately small:

| Event | Purpose | Required semantic payload |
|---|---|---|
| \`REGISTERED\` | Freeze the original forecast terms | claim, forecast family, target, horizon, confidence representation, resolver, resolution rule, falsifier, grader |
| \`AMENDED\` | Record a prospective change without overwriting registration | reason, changed fields, before/after values, effective time, whether scoring eligibility survives |
| \`CHALLENGED\` | Preserve independent or adversarial review | reviewer, challenge claim, requested consequence, disposition |
| \`OWNERSHIP_TRANSFERRED\` | Move operational ownership without duplicating or resolving the prediction | from-agent, to-agent, acceptance evidence |
| \`RESOLUTION_SUBMITTED\` | Owner submits an evidence-backed proposed result | resolver evidence, observed value, proposed outcome, resolution time |
| \`RESOLUTION_VERIFIED\` | Independent grader accepts or rejects the submitted result | grader, verdict, scored outcome, evidence, conflicts |
| \`VOIDED\` | Close a prediction without scoring | controlled void reason, actor, evidence, whether defect existed at registration |
| \`CORRECTED\` | Correct administrative metadata without changing frozen analytical terms | field, erroneous value, corrected value, evidence |

Forecast family must be explicit because scoring rules differ. V1 should allow \`BINARY_EVENT\`, \`DIRECTIONAL\`, \`THRESHOLD\`, \`MULTI_BRANCH\`, \`MECHANISM\`, and \`TRADE_CARD\`. A mechanism call must not be converted into a binary threshold hit after resolution; a trade card must not be pooled with a probability forecast.

Confidence should be represented as a typed object rather than one overloaded field:

\`kind\` ∈ {\`PROBABILITY\`, \`TIER\`, \`SCORE\`, \`UNSTATED\`}, with \`value\`, \`scale\`, \`as_made\`, and optional \`base_rate\`. Only \`PROBABILITY\` values in [0,1] with a binary scorable outcome are eligible for Brier or log scoring. Later re-marks append events and never replace \`as_made\`.

The lifecycle state machine should remain narrower than the event vocabulary:

\`OPEN → PENDING_VERIFICATION → RESOLVED\`
\`OPEN → VOID\`
\`OPEN → CANCELLED\`

Amendments, challenges, and ownership transfers do not themselves change lifecycle state. Terminal states cannot be silently reopened. A substantive new forecast after closure receives a new prediction ID linked by \`related_prediction_id\`; an administrative correction appends \`CORRECTED\` and cannot alter the original claim, probability, horizon, or resolution rule.

Resolution should separate lifecycle from analytical outcome. Suggested scored outcomes are \`TRUE\`, \`FALSE\`, and \`PARTIAL\`, while non-scored dispositions use controlled reasons such as \`UNSPECIFIED_RESOLVER\`, \`UNOBSERVABLE_TARGET\`, \`AMBIGUOUS_RULE\`, \`PREDICATE_DISSOLVED\`, \`INSTRUMENT_ABSENT\`, \`OUT_OF_LANE\`, and \`DATA_UNAVAILABLE\`. Transfer, retirement, no-fire, and downgrade are events or explanatory attributes, not substitutes for a scored outcome.

\*\*Prospective-cohort integrity rules:\*\*

1\. Register before the forecast can resolve and commit the event immediately.
2\. Require a dated horizon, named resolver source, exhaustive resolution rule, falsifier, and named grader.
3\. Freeze scoring eligibility at registration; amendments that change claim, threshold, horizon, probability, or resolver are visible and separately counted.
4\. Require independent verification for terminal scored outcomes. The owner may submit but may not be the sole verifier.
5\. Report amendment, void, unscoreable, and unresolved-aging rates alongside accuracy.
6\. Do not backfill historical records into the prospective score. Historical adapters are diagnostic only.
7\. Preserve raw source text and Git provenance so every projection can be reproduced.
8\. Make parser ambiguity a hard error, never a warning followed by guessed scoring.

A sensible shadow cohort should cover three different operational shapes: one mature percentage-ledger agent, one preamble-heavy thesis ledger, and one newer typed ledger. Selection should be frozen before accepting cohort outcomes and should favor adequate event frequency over perceived agent quality. The trial should run long enough to resolve a useful number of forecasts; a calendar duration alone is insufficient, so the exit condition should include a predeclared minimum resolved-sample count.

\#\#\# Existing kernel-membrane lineage found in the repository

The kernel membrane should not be treated as a greenfield concept. A targeted review found a clear architectural lineage, although no current file is literally named \`kernel membrane\`.

\*\*1\. The June shared-state plan is the broad precursor.\*\*
\`AUDITS/2026-06-09_shared_state_design.md\` proposes two logical layers behind one CLI: a canonical current-values store with single-writer ownership, and an append-only event/signal log with stable IDs and recipient cursors. It explicitly says shared facts should be structured while research judgment remains prose. It also proposes generated HEARTBEAT/STATUS/fleet views, pure-function threshold firing, ownership enforcement, and a storage abstraction that could begin Git-native and later use SQLite. This is substantially the same boundary later described as the membrane.

That plan should be reused as design input, not adopted unchanged. It assumes a June-era separate-clones migration, a persistent VPS option, roughly 14 agent instruction edits, retirement of inbox/outbox, and a broad shared-values migration. Several of those assumptions no longer match current architecture or policy. Its strongest durable ideas are single-writer ownership, append-only events, generated projections, a backend-independent CLI, and the rule that judgment stays outside structured state.

\*\*2\. The July system-report disposition ledger already contains the prediction mandate.\*\*
\`AUDITS/2026-07-25_system_report_DISPOSITIONS.md\` row P3 says to normalize predictions and gates with a minimum common envelope, forward-only, with domain extensions and no historical rewrites. It proposes DAEDALUS blueprint ownership and a SAM/BRENT/HENRY forward cohort. Row P4 makes the evaluation stack depend on P3. As of the inspected file, both remain \`PROPOSED\`, not Will-ruled or in-build. This is the closest existing governance record to the prediction portion of the membrane and must be dispositioned or superseded before implementation.

Rows P1 and P5 propose a read-only operational exception/adjudication view, while G2 is already Will-ruled: exception surfaces must be operator-cleared adjudication queues, never auto-green dashboards. That is a binding membrane design constraint.

\*\*3\. Direct Messaging v1 is the first implemented membrane slice.\*\*
The root \`MESSAGING/\` package already provides stable message and obligation IDs, constrained schemas, sender and receipt ownership, append-only receipt events, lifecycle validation, evidence tiers, idempotency, recipient isolation, fail-closed routing, tests, and rollback boundaries. Its design rationale explicitly recommends a file-native shadow control plane with generated projections and canonical-owner boundaries.

The live boundary remains narrow. \`MESSAGING/config.yaml\` confirms \`write_mode: cohort\` and permits only PROME → BRENT and PROME → SAM. The package README calls this cohort live, and the 22 messaging tests pass. Legacy/WALTER adapters and generated open-work/health projections listed in the implementation plan are not present in the inspected tree. Thus messaging is a proven kernel primitive, not yet a fleet control plane.

\*\*4\. The orchestral-layer design is related but distinct.\*\*
\`PROME/ORCHESTRAL_LAYER_DESIGN.md\` addresses operator cognitive load through fleet scans, ranking, task packets, and revival proxies. It is a reasoning/orchestration layer, not a transactional membrane. Parts are also historically stale: it still describes rebuilding \`PROME/FLEET_SCAN.md\`, while current \`PROME/SYSTEM.md\` marks that file a superseded snapshot that must never be rebuilt. The membrane should supply reliable state and exceptions to orchestration; it should not absorb the orchestral layer's ranking judgment.

\*\*5\. The existing membrane documents themselves exhibit status drift.\*\*
\`MESSAGING/README.md\` correctly says the first cohort is live, while \`DIRECT_MESSAGING_V1_SPEC.md\` still carries the header \`DEFAULTS RATIFIED FOR IMPLEMENTATION — NOT YET LIVE\`, and \`IMPLEMENTATION_STATUS.md\` remains an as-of-2026-07-14 branch-era snapshot. The config file is the strongest inspected runtime evidence. Any membrane program needs one generated capability/status manifest so design status, activation scope, tests, and implemented components do not drift across narrative documents.

\*\*Revised architectural conclusion:\*\* build the prediction pilot as a sibling module using the proven messaging conventions—stable IDs, append-only events, constrained schemas, explicit ownership, evidence-backed terminal transitions, generated non-canonical views, fail-closed validation, and boring rollback. Do not introduce a second generic event framework or a competing CLI without first deciding whether the June shared-state proposal is being revived, narrowed, or formally superseded.

\#\#\# Messaging reconsideration after the live doorbell channel

The August 16–23 cross-session \`SendMessage\`/\`ListAgents\` channel materially changes the case for expanding Direct Messaging v1. For two agents that are simultaneously live, the combination of a committed file packet plus an ephemeral doorbell provides the two essential properties separately: Git carries durable content and provenance; the doorbell supplies low-latency discovery and coordination. The repository records a minutes-versus-roughly-45-hours improvement in the first worked example.

The doorbell is not itself a durable messaging system. It is same-box, lost when a session dies, invisible to future sessions and the other machine, weakly attributed, and one-directional for cloud receivers. Current governance correctly limits it to coordination and requires decisions, thresholds, findings, and other durable content to live in committed artifacts.

Direct Messaging v1 therefore should not be treated as automatically necessary merely because a kernel membrane is being considered. Its remaining unique value is narrower:

\- stable obligation identity across retries, moves, recipients, and sessions;
\- explicit ACTION versus INFO semantics;
\- recipient-owned disposition and blocked/deferred state;
\- evidence-backed integration claims;
\- generated overdue and incomplete-transition views;
\- offline and cross-machine recovery.

Those benefits are real only if the repository needs and uses the structured obligation lifecycle. The current implementation remains a two-route cohort, and its legacy/WALTER adapters and open-work projections were not found. Meanwhile, ordinary committed packets plus the ratified doorbell already solve the dominant live-peer latency problem without requiring YAML envelopes and receipt files.

\*\*Recommendation:\*\* freeze Direct Messaging v1 at its current cohort and do not expand it as part of the prediction membrane. Preserve its code, tests, and two-route history as a reusable prototype. Continue using committed packets as durable content and doorbells as live coordination. Revisit a structured obligation module only after measuring unresolved work that packets plus doorbells cannot handle—for example repeated offline loss, ambiguous multi-recipient ownership, overdue actions with no discoverable state, or inability to reconstruct completion evidence.

If a future jobs module supplies stable IDs, ownership, deadlines, dependencies, dispositions, and completion evidence, it may absorb most of Direct Messaging v1's ACTION semantics. In that architecture, messages remain human-readable artifacts and coordination notices; jobs carry durable obligations. This avoids maintaining two overlapping lifecycle systems.

\#\#\# Prediction shadow-system design

The recommended first module is a narrowly named \`EVALUATION/\` package rather than a generic \`KERNEL/\` tree. This makes its authority legible: it evaluates prospective predictions and does not claim ownership of research, messaging, jobs, positions, gates, or orchestration.

Suggested layout:

\`EVALUATION/README.md\` — authority, non-goals, activation and rollback
\`EVALUATION/config.json\` — \`disabled | shadow | active\`, cohort, schema version
\`EVALUATION/schemas/prediction-event-v1.schema.json\` — documentary machine schema
\`EVALUATION/events/YYYY/MM/<event_id>.json\` — immutable source events
\`EVALUATION/adapters/\` — read-only historical ledger adapters, explicitly non-scoring
\`EVALUATION/tools/prediction.py\` — preview/write/validate/render interface
\`EVALUATION/tools/evaluate.py\` — independent scoring and coverage reports
\`EVALUATION/tests/fixtures/\` — valid and adversarial records
\`EVALUATION/generated/\` — rebuildable projections; never manually edited or canonical

One immutable JSON file per event is preferable to one shared JSONL append target. It preserves append-only semantics while avoiding a hot shared file and reducing concurrent-writer/rebase collisions. A deterministic renderer can sort the files by \`occurred_at\` and \`event_id\` into JSONL, SQLite, TSV, or Markdown projections. SQLite should be a disposable local projection, not committed authority.

The event envelope should use strict JSON objects with \`additionalProperties: false\`. Required common fields:

\`schema\`, \`event_id\`, \`event_type\`, \`prediction_id\`, \`occurred_at\`, \`recorded_at\`, \`actor\`, \`owning_agent\`, \`prior_event_id\`, \`related_prediction_ids\`, \`source_refs\`, and \`notes\`.

\`source_refs\` should point to any human-readable agent artifact underlying the event. The commit that first contains the event file must be **derived from Git after commit**, not required inside the event at creation time; otherwise registration would require claiming a commit that does not yet exist. The evaluator should derive \`registered_commit\`, author time, committer time, and first-parent reachability and report an uncommitted or rewritten event as ineligible.

Identifier forms:

\`PRD-<AGENT>-<YYYYMMDD>-<NNN>\` for predictions
\`EVT-<PREDICTION-ID>-<YYYYMMDDTHHMMSSZ>-<NN>\` for events

Allocation should reuse the messaging package's proven pattern: scan existing IDs, acquire an atomic runtime lock, preview by default, fail on collision, write with exclusive creation, and never commit or push automatically.

CLI surface:

\`prediction.py register --input registration.json [--write]\`
\`prediction.py amend --prediction ID --input amendment.json [--write]\`
\`prediction.py challenge --prediction ID --input challenge.json [--write]\`
\`prediction.py transfer --prediction ID --to AGENT --input transfer.json [--write]\`
\`prediction.py submit-resolution --prediction ID --input evidence.json [--write]\`
\`prediction.py verify-resolution --prediction ID --input verdict.json [--write]\`
\`prediction.py void --prediction ID --input void.json [--write]\`
\`prediction.py validate [--json]\`
\`prediction.py render [--check]\`
\`evaluate.py report [--as-of ISO_DATE] [--json]\`

Writes must be cohort-gated in \`config.json\`; preview and validation remain available fleet-wide. The tool must not edit agent ledgers, infer a resolution, commit, push, ring doorbells, or create jobs.

Generated projections should be few and purpose-specific:

| Projection | Purpose |
|---|---|
| \`prediction_state.tsv\` | One current row per prediction, derived by replay |
| \`exceptions.tsv\` | Invalid transitions, missing evidence, overdue/open, grader conflict, uncommitted events |
| \`cohort_coverage.json\` | Registered/resolved/void/amended/unscoreable counts and aging |
| \`scores.json\` | Eligible Brier/log/hit metrics plus baselines and denominators |
| \`report.md\` | Human-readable evaluation with explicit limitations |
| \`events.jsonl\` | Deterministic ordered export for analysis; generated, not authored |

Every report must include denominators, eligibility exclusions, amendment/void rates, unresolved aging, cohort version, schema version, Git cutoff, and generator commit. A green summary is prohibited; exceptions require explicit disposition in their owner system.

\*\*Fail-closed conditions:\*\* unknown event type; extra or missing field; invalid agent or ID; duplicate/conflicting ID; broken prior-event link; non-monotonic chain; forbidden transition; amendment after terminal state; owner self-verifying where independence is required; missing resolver evidence; shifted/ambiguous adapter row; probability outside [0,1]; binary scoring requested for a non-binary family; event file uncommitted or absent from the evaluated Git history; generated projection differs under \`render --check\`.

Historical adapters must emit raw records plus \`MAPPED\`, \`UNMAPPED\`, or \`INVALID\` and a versioned rule ID. They may populate compatibility and data-quality reports but must never enter the prospective cohort score.

\*\*Cohort recommendation:\*\* three agents representing distinct authoring shapes: one mature percentage ledger, one preamble-heavy thesis ledger, and one newer typed ledger. LABOR, SAM or BRENT, and VULCAN are reasonable candidates. The older P3 proposal names SAM/BRENT/HENRY; because HENRY's current ledger lacks made-at and confidence fields and because using both SAM and BRENT undersamples newer typed records, that cohort should be explicitly reaffirmed or superseded before activation. Selection should be based on expected forecast frequency and family diversity, not perceived quality.

The pilot should stop on a registered sample rule rather than only a calendar: for example, 60–90 days **and** a predeclared minimum number of independently verified resolutions. If the resolution minimum is not met, the output is an operational pilot result, not a performance estimate.

\#\#\# Repository-wide CI design

The first CI lane should be non-mutating, network-free, secret-free, and read-only. It should run on pull requests and selected pushes with \`contents: read\`, bounded timeouts, and no step permitted to commit, push, advance cursors, fetch live data, or rewrite generated files except inside temporary directories.

Recommended jobs:

1\. **Static Python check.** Compile active Python sources while explicitly excluding \`.venv\`, archives, generated caches, private exercises, and fixtures not intended as programs. Print the scan perimeter.
2\. **Unit tests.** Run centrally discoverable root tests, the 22 messaging tests, and new evaluation tests. Convert standalone script-style checks into import-safe \`unittest\` modules or thin wrappers; do not import scripts that execute tests or network calls at module import.
3\. **Evaluation validation.** Validate schemas, event chains, cohort configuration, immutable-path rules, generated projection reproducibility, and adversarial fixtures.
4\. **Canon consistency.** Check roster count claims and explicitly registered canonical→mirror relationships. Begin with demonstrated defects such as README active count and contradictory FERT ownership language. Avoid an unrestricted prose linter.
5\. **Control registry.** Run only existing controls that declare a read-only CI mode, scan perimeter, exit-code contract, and fixture coverage. Checks such as \`board_scan --advance\` are excluded because they mutate operational cursors.
6\. **Result publication.** Combine job results into versioned JSON plus a concise Markdown artifact. Preserve failures and exact exclusions.

Live integrations belong in a separate manually dispatched workflow with explicit network naming and no authority to change repository state. Recorded fixtures should cover normal CI. MARCO/BLS-style live pulls must never be imported by unit discovery.

The VIOLET daily-log test should be repaired before inclusion: inject an explicit clock/date, use an isolated temporary directory, expose assertions through \`unittest\`, and put execution under \`if __name__ == '__main__'\`. The current top-level script execution and wall-clock dependency are both CI hazards.

CI rollout should have two stages. First, report-only on the current baseline so pre-existing debt is visible without normalizing it away. Second, enforce no-new-regressions plus hard failures for deterministic invariants. Existing known failures require expiry-dated, owner-named exceptions; permanent blanket allowlists are prohibited.

The workflow itself should declare what a pass proves and does not prove. A passing CI run proves only the printed perimeter and deterministic contracts; it does not certify research truth, fleet freshness outside scanned surfaces, live integrations, or predictive value.

\#\#\# Implementation checkpoint — 2026-08-25

A first disabled vertical slice was added to the working tree under \`EVALUATION/\`. It is intentionally not activated and contains no live prediction events.

Implemented:

\- disabled cohort configuration with an empty allowlist;
\- documentary JSON Schema and a synchronized manual validator;
\- immutable one-event-per-file layout;
\- validation and preview-only add path, with writes failing closed under current config;
\- lifecycle replay for registration, amendment, challenge, transfer, resolution submission, independent verification, void, cancellation, and administrative correction;
\- independent-grader enforcement against the grader named at registration;
\- terminal-state protection while permitting non-reopening administrative corrections;
\- binary-probability eligibility filtering and Brier scoring;
\- deterministic state, exception, and score projections;
\- explicit README authority and rollback boundaries;
\- a narrow GitHub Actions workflow covering only the declared deterministic perimeter.

Verification at this checkpoint:

\- 12 evaluation tests pass, covering valid scoring, empty state, schema/validator agreement, preview behavior, the disabled write gate, broken chains, invalid probability, self-verification, wrong registered grader, amendment during verification, terminal reopening, and post-terminal administrative correction;
\- all 22 existing messaging tests still pass;
\- evaluation validation reports zero events, zero predictions, and zero errors;
\- generated projections reproduce exactly;
\- all checked implementation files compile;
\- the new workflow parses successfully as YAML.

The slice is not production-ready or a live membrane. It still requires a cohort ruling, P3 governance disposition, event-authoring ergonomics beyond full-event JSON input, deeper per-event payload validation, Git first-commit provenance reporting, historical diagnostic adapters, aging/base-rate reports, and an adversarial review before shadow activation. No agent ledger, roster, PROME state, messaging configuration, or live workflow was changed.

\#\#\# Reconciliation with the kernel design packet — 2026-08-25

After the implementation checkpoint, \`origin/master\` advanced by one commit containing \`PROME/proposals/2026-08-24_kernel-membrane-design-DRAFT.md\`. That 1,204-line packet is the previously missing membrane plan and is materially more complete than the simplified \`EVALUATION/\` spike described above.

The packet makes several load-bearing choices that the spike did not model:

\- separates \`Question\`, \`Forecast\`, and \`Resolution\` rather than storing one combined prediction stream;
\- requires a frozen \`TrialManifest\` before prospective questions open;
\- distinguishes actor submissions from PROME-custodied deterministic command acceptance;
\- gives accepted and rejected commands durable receipts;
\- uses per-stream expected versions and competing-child quarantine rather than timestamp ordering;
\- imports exact native ledger references during shadow mode, with native state remaining authoritative;
\- treats question outcome as objective and scores multiple forecast versions against it;
\- defines separate integrity gates for forecast authority and later scope expansion;
\- proposes neutral top-level \`KERNEL/\` placement, subject to explicit ruling.

These are improvements, not cosmetic differences. Committing the simplified \`EVALUATION/\` implementation alongside that packet would create two competing domain models and two candidate subsystem homes before the packet's 22 blocking decisions are ruled.

\*\*Disposition of the spike:\*\* do not retain it as repository architecture. Preserve its useful findings—one-event-per-file, fail-closed writes, independent-grader tests, deterministic projections, and narrow CI perimeter—as prototype evidence for the eventual kernel build. The untracked \`EVALUATION/\` tree and its draft CI workflow should be discarded before commit. The kernel packet becomes the design-of-record candidate, but remains a draft with no authority until Will rules Phase 0.

\*\*Organization judgment:\*\* the repository should ultimately use \`KERNEL/\` if that location is ruled, keep the design packet under \`PROME/proposals/\` until then, and keep this evaluation under \`AUDITS/\`. It should not carry both \`EVALUATION/\` and \`KERNEL/\` as overlapping top-level systems.

\#\#\# Phase 0 decision update — 2026-08-25

Will ratified the kernel packet's first five recommendations. The resulting boundaries are:

1\. The eventual live subsystem has neutral root-level \`KERNEL/\` placement; Will retains policy authority and PROME's operational custody does not imply ownership of institutional truth.
2\. Version 1 governs \`Question\`, \`Forecast\`, \`Resolution\`, and \`TrialManifest\`, with Actor and Evidence as supporting records. Messaging, theses, and general workflow are excluded from the first governed boundary.
3\. Native ledgers remain authoritative during shadow mode. Shadow imports must reference exact native records, remain explicitly non-authoritative, and report discrepancies instead of silently repairing them.
4\. After an explicit Phase 3 authority switch, one-file-per-event Git history becomes canonical only for admitted prospective cohorts. Historical ledgers remain unchanged and SQLite is only a rebuildable projection.
5\. Version 1 serializes command acceptance through one exclusively locked local process. Agents submit immutable commands, PROME applies deterministic policy, every request receives a durable receipt, and research attribution remains with the submitting actor.

These rulings resolve decisions 1-5 of 22 and authorize further specification work. They do not yet authorize creation of \`KERNEL/\`, activation of a shadow trial, or an authority switch. Decisions 6-22 remain open.

\#\#\# Refined conclusion

The August 24 prioritization should stand, with one refinement: the first implementation artifact should be a **compatibility inventory and explicit mapping contract**, not a fleet-wide historical normalizer. The evidence shows three separate problems that should not be conflated:

1\. **Syntactic variation** — headers, comments, column order, and malformed or shifted rows.
2\. **Semantic variation** — confidence, horizon, resolver, falsifier, and outcome fields mean different things across ledger families.
3\. **Lifecycle variation** — status cells encode state, judgment, transfer, amendment, retirement, and narrative detail in overlapping ways.

The safe sequence is therefore:

1\. Inventory every live-path ledger and classify it into a reviewed schema family.
2\. Define canonical event and transition semantics before mapping legacy values.
3\. Build fail-closed adapters that emit explicit \`UNMAPPED\` or \`INVALID\` results instead of guessing.
4\. Pilot only new prospective predictions in shadow mode while existing files remain authoritative.
5\. Add a non-mutating CI lane that proves parser behavior, schema validity, deterministic tests, and scan perimeter before attempting aggregate scoring.

No defensible fleet-wide performance number can be produced from the current ledgers merely by cleaning column names. The variation is substantive, and some records will remain legitimately unscoreable. Treating “not measurable” as an acceptable result is part of the evaluation discipline.

\#\# Executive assessment

Research Workspace is a serious, unusually transparent analytical operating system. Its strongest qualities are institutional memory, explicit ownership, falsification discipline, and preservation of mistakes. It contains real examples where disagreement changed confidence, trade construction, or thesis state before the outcome was known. This is substantially more rigorous than a collection of research notes or independent chat agents.

The system is not yet a reliably measurable research platform. It is stronger at governing and narrating analytical work than at proving aggregate predictive value. Prediction schemas and resolution labels vary by agent, calibration evidence is fragmented, status surfaces drift, and most controls depend on agents invoking local scripts correctly. The code-and-control layer is sophisticated but has a recurring pattern of guards initially failing outside the case that motivated them.

\*\*Overall judgment: promising and operationally real, but not yet institutionally validated.\*\* Treat its research outputs as governed hypotheses with traceable evidence—not as a statistically demonstrated forecasting edge.

\#\#\# Scorecard

| Dimension | Rating | Assessment |
|---|---:|---|
| Architecture and role design | 4/5 | Clear specialization, ownership, synthesis, and escalation concepts; substantial complexity and some canonical drift. |
| Research rigor and falsification | 4/5 | Strong preregistration examples, explicit kill conditions, and honest preservation of adverse outcomes. |
| Cross-agent synthesis | 4/5 | Evidence of useful challenge and causal deduplication; message transport remains narrow and stale inputs can contaminate synthesis. |
| Calibration and evaluation | 2/5 | Candid local scoreboards exist, but fleet-wide scoring is not defensible under current heterogeneous schemas. |
| Operational reliability | 2.5/5 | Thoughtful safety controls and strong messaging tests; limited CI, fragmented test discovery, stale tests, incomplete scan perimeters. |
| Maintainability | 2.5/5 | Rich documentation and self-correction, offset by large/dense state surfaces, duplicated canon, and high cognitive load. |
| Auditability | 4/5 | Git receipts, frozen cards, failure retention, and explicit findings make retrospective review unusually strong. |

\#\# What the repository is

The repository is a file-backed, multi-agent research institution organized around specialist agents, a coordinating layer, synthesis and challenge roles, durable memory, prediction ledgers, research workbooks, and operational checks. The reviewed checkout contained roughly 10,100 tracked files, dominated by Markdown, with hundreds of TSV and Python files. The active roster reports 33 agents, although the root README still reports 21—a simple example of canonical-surface drift.

The architecture is more mature than its runtime. Responsibilities, provenance, escalation, falsification, and closeout behavior are extensively specified. Execution still largely depends on agents reading the right files, running the right local checks, preserving path discipline, and updating several related surfaces correctly.

\#\# Major strengths

\#\#\# 1\. Disagreement can change decisions

The SAM–RED dialogue is the strongest observed case. RED challenged SAM's yen-positioning thesis, reduced confidence from MED-HIGH to MEDIUM, demanded two explicit falsification legs, and retired an unhelpful channel. When the registered cover condition later fired, SAM reduced the thesis to LOW. Git history confirms that the relevant terms existed before the resolving event.

This is the key sign that the agent network is not merely producing parallel prose: challenge altered the state of a live thesis.

\#\#\# 2\. Trade construction is separated from thesis enthusiasm

TERRY's review of a BRENT USO idea checked portfolio concentration, account constraints, instrument availability, strike liquidity, tenor, payoff path, and expiry. The card expired unfired rather than being chased. That separation between analytical belief and executable construction is a material design strength.

\#\#\# 3\. Failures are retained and discussed candidly

SAM's ledger preserves numerous failed predictions rather than quietly deleting them. LABOR's explicit scoreboard reports 12 resolved calls with an as-made mean Brier score of 0.299—worse than a 0.25 coin-flip benchmark—and notes that calls at or above 60% confidence went 0-for-4. This level of adverse self-reporting is rare and valuable.

LABOR's own results also reveal a useful distinction: mechanism identification appears stronger than thresholded directional forecasting. That is an actionable research finding, not just a poor score.

\#\#\# 4\. Synthesis is causal, not only summarizing

NEXUS attempts to deduplicate common causes across agent outputs and defines system-level falsifiers. RED performs structured adversarial review. These roles provide distinct analytical functions rather than merely restating specialist notes.

\#\#\# 5\. Git history provides meaningful provenance

Several sampled cases had verifiable preregistration receipts. Examples include SAM's CFTC and BOJ calls, RED's grading rubric, and NEXUS preregistration. Frozen cards, immutable history, and retained outcome ledgers make the system substantially more auditable than ordinary conversational workflows.

\#\#\# 6\. The repository learns from operational failures

The controls encode many specific lessons: fast-forward-only push behavior, path-scoped commits, post-push verification, read caps, stale-ledger checks, consumer checks, and completion checks. Messaging v1 is particularly strong: 22 unit tests passed, including contention, idempotency, ownership, invalid transitions, and fail-closed cohort behavior.

\#\# Principal weaknesses and risks

\#\#\# 1\. There is no defensible fleet-wide performance number

The audit found 44 prediction-ledger files, but their schemas and status vocabularies differ materially. Confidence may be numeric, tiered, provisional, or absent. Resolution states include ordinary hit/miss labels plus split, void, retired, precondition, partial, downgrade, no-fire, and agent-specific variants.

Without a canonical event, forecast, probability, resolver, resolution-time, and outcome schema, any aggregate hit rate or Brier score would require subjective recoding. That would create the appearance of precision after the fact.

\#\#\# 2\. Governance surfaces drift and contradict one another

Examples observed during this audit include:

\- The canonical roster reports 33 active agents while the README reports 21\.
\- Root \`AGENTS.md\` contains current FERT triage language near the top but later describes potash as excluded/unowned.
\- Two live memory documents still prescribe patterns prohibited by the current canon.
\- \`safe-push.sh\` retains an older escalation condition (“mid-session recurrence”) while the current coordination canon says escalation should occur only after recurrence persists through a completed rebase-and-repush cycle.

The system recognizes canon drift as a problem, but recognition has not eliminated it.

\#\#\# 3\. Control coverage is broad in prose but narrow in automation

The sampled control scripts total roughly 12,400 lines. Only one GitHub Actions workflow was present, and it is a manually triggered feed-fetch workflow with scheduled execution intentionally disabled. It does not run the repository's validators or tests.

Central test discovery under \`AGENTS\` ran zero tests. Individual tests had to be invoked directly. ORACLE and TERRY standalone tests passed, and the PROME queue parser passed 22 self-tests. MARCO's supposed test attempted a live BLS network call and could not run in the restricted environment. VIOLET's daily-log test currently fails because it hard-codes a July date but relies on the current date in one case; the production date guard behaved correctly, so this is a stale time-dependent test rather than the data-corruption bug the failure initially resembles.

\#\#\# 4\. The guards are useful but not yet independently trustworthy

Recent history records controls that initially produced false greens, incomplete defaults, false positives, or checks against the wrong constraint. Examples include post-push verification matching an older commit with the same subject, falsification scanning with incomplete defaults, a read-cap check targeting the wrong constraint, and multiple consumer-check classification repairs.

This demonstrates healthy self-correction, but also a meta-risk: a sophisticated check can confer more confidence than its tested perimeter warrants. Every check should declare what a pass proves, what it does not prove, and how failure is handled.

\#\#\# 5\. Status and memory surfaces impose high cognitive load

Some agent status files are large and dense, especially in high-activity lanes. NEXUS synthesis quality depends on input freshness; stale briefs can yield well-structured but outdated conclusions. The hot memory index is already at 74% of its cap, and five embedding-pending promises were 24 days stale at review time.

The system has read caps and archival practices, but the amount of procedural and historical material an agent must interpret remains a core source of operational risk.

\#\#\# 6\. Staleness scanning reveals both real debt and incomplete perimeter coverage

The all-agent staleness scan reported material gaps, including surfaces tens of days behind and some ledgers with many intervening writes. The scan itself also explicitly omits many TSV and docket surfaces. A passing result therefore cannot certify fleet freshness.

The falsification scanner similarly found agents without separate falsification surfaces, but manual review showed that some rails were embedded elsewhere. This is both a real consistency problem and an instrumentation-classification problem.

\#\#\# 7\. Evaluation can be contaminated by retrospective specification

LABOR's LAB-10 case illustrates the issue. The methodology card was committed before the claimed data examination and before grading, but roughly five months after the original forecast and only minutes before resolution. That is better than silent post-hoc grading, but it is not equivalent to a fully specified preregistered forecast.

RED's impact ledger reports that 17 of 24 resolvable accepted revisions improved outcomes, 5 were neutral, and 2 harmed them. This is encouraging, but much of RED's impact is graded by RED, and independent spot-checking and conflict flags are incomplete. It should be treated as an internal operating metric rather than independent validation.

\#\# Operational findings

\- The messaging subsystem is the best-tested component reviewed.
\- The completion check passed for the audit date, with no DAEDALUS commits in scope and all eight reader-report pairs accounted for.
\- The memory index resolved all 464 slugs and all were committed.
\- Position-agreement checks passed across agents.
\- Read-cap checks passed, though some mandatory-read sets are close to the cap.
\- Lane coverage reported 20 covered active agents, 6 synthesis exclusions, and 7 informationally uncovered agents relying on manual pulls.
\- The worktree remained clean throughout the read-only audit.

\#\# Recommended program

\#\#\# Priority 0 — Define the evaluation contract

Before adding more agents or controls, establish one canonical prediction event schema. Preserve agent-specific research files if desired, but require an append-only normalized event stream containing at least:

\`prediction\_id\`, \`agent\`, \`made\_at\`, \`as\_of\`, \`claim\`, \`target\`, \`horizon\`, \`probability\`, \`base\_rate\`, \`resolver\`, \`resolution\_rule\`, \`falsifier\`, \`resolved\_at\`, \`outcome\`, \`void\_reason\`, \`evidence\_commit\`, and \`grader\`.

Define the allowed resolution state machine and prohibit retrospective resolver changes except through a separately recorded amendment event. Distinguish forecast-time specification, pre-resolution salvage, and post-resolution interpretation.

\#\#\# Priority 1 — Build a thin, independent evaluation pipeline

Create a read-only evaluator that consumes the normalized event stream and produces:

\- coverage and unresolved-aging reports;
\- calibration curves and Brier/log scores where probability forecasts permit them;
\- hit rates by forecast family, horizon, agent, and confidence bin;
\- void/amendment rates;
\- base-rate and naive-benchmark comparisons;
\- preregistration integrity checks from Git timestamps;
\- separate views for mechanism calls, directional calls, thresholds, and trade cards.

The evaluator should be owned outside the agents it grades. RED may challenge forecasts, but should not be the sole grader of RED's impact.

\#\#\# Priority 2 — Establish a repository-wide verification lane

Add a non-mutating CI workflow that runs on pull requests and selected pushes. At minimum it should:

\- compile Python sources;
\- run centrally discoverable unit tests;
\- run messaging tests;
\- validate canonical references and roster counts;
\- validate prediction schemas and state transitions;
\- run memory-link and position-agreement checks;
\- run bounded stale/falsification scans with explicit perimeter reports;
\- fail on time-dependent tests that do not inject a clock;
\- publish machine-readable results.

Separate unit tests from live integration pulls. Network-dependent scripts should use recorded fixtures in CI and an explicitly named integration mode for live verification.

\#\#\# Priority 3 — Reduce canonical duplication

Choose generated views for roster counts, ownership tables, and repeated Git policy. Canonical documents should hold the rule once; agent documents should link to it and state only exceptions. Add a consistency check for README counts and contradictory ownership vocabulary.

\#\#\# Priority 4 — Make control claims precise

For each checker, maintain a compact registry with:

\- inputs and scan perimeter;
\- what a pass proves;
\- known blind spots;
\- exit-code contract;
\- required response on failure;
\- unit and adversarial tests;
\- owner and last validation date.

Checks with \`--help\` should print help and exit rather than execute a scan. Time must be injectable in every date-sensitive test.

\#\#\# Priority 5 — Run a bounded prospective trial

Freeze a 60- to 90-day cohort before outcomes are known. Select a manageable set of agents and forecast families, preregister the scoring rules, and prohibit schema changes inside the cohort except as versioned amendments. Compare against simple baselines and, where possible, a single-agent or no-challenge control.

The key questions should be:

1\. Does cross-agent challenge improve calibrated accuracy after accounting for amendment and void rates?
2\. Which agent roles add unique information rather than correlated prose?
3\. Are mechanism forecasts genuinely stronger than threshold/directional forecasts?
4\. Does trade-construction review improve payoff quality or mainly reduce execution frequency?
5\. What operational burden is required per resolved forecast?

\#\#\# Priority 6 — Control complexity growth

Pause net-new agent creation unless a new lane has a named decision consumer, distinct information source, explicit overlap analysis, falsification surface, and evaluation path. Prefer simplifying existing agents and generating compact current-state views over expanding status prose.

\#\# Suggested 90-day sequence

\*\*Weeks 1–2:\*\* Freeze schema v1; map existing statuses; identify the prospective cohort; fix the stale VIOLET test; separate MARCO live integration from unit testing; repair current canon contradictions.

\*\*Weeks 3–4:\*\* Implement normalized append-only events and the independent evaluator; add repository-wide CI; make existing tests centrally discoverable.

\*\*Weeks 5–12:\*\* Run the prospective cohort without changing scoring rules; publish weekly operational coverage and unresolved-aging reports, but do not optimize thresholds against interim outcomes.

\*\*End of trial:\*\* Produce a blinded or independently graded comparison against registered baselines. Decide which agent roles to retain, merge, or retire based on incremental information value and operating cost.

\#\# Planned concept: the kernel membrane

The repository can also be understood as an early research operating system. Under this lens, the agents are specialized processes, PROME and the governance documents form a control plane, Git provides durable storage and provenance, messages provide inter-process communication, and catalysts act like interrupts.

The system's present design is largely \*\*cooperative\*\*: agents read written procedures, interpret them, update the correct files, run the correct checks, and notify the next agent. This works surprisingly well, but it depends on attention and correct interpretation. Many important controls are policies rather than mechanically enforced boundaries.

The proposed \*\*kernel membrane\*\* is a small deterministic software layer between agent intentions and durable system state. It would not conduct research or replace agent judgment. It would handle the administrative mechanics surrounding research:

\- keep one official record of current state;
\- assign and track work;
\- enforce agent permissions;
\- validate state changes;
\- preserve original prediction terms;
\- schedule deadlines and catalyst checks;
\- route required messages and reviews;
\- require evidence before work is closed;
\- update generated status views;
\- record a complete audit trail.

The word \*membrane\* is useful because the layer would sit at the boundary between flexible LLM reasoning and controlled repository operations. Agents could reason freely inside their assigned domains, but meaningful state changes would pass through a narrow validated interface.

\#\#\# Simple example

Today, registering a prediction may require an agent to update a ledger, record a falsifier, notify RED, remember a resolver date, later grade the result, update its thesis, and notify NEXUS. Each step depends on the agent following written instructions.

Under the kernel membrane, the agent would submit one structured request:

\`\`\`text
Prediction: Yen positioning remains above the registered threshold
Probability: 65%
Deadline: September 18
Resolver: Weekly CFTC report
Falsifier: Net positioning falls below −108,000
Reviewer: RED
\`\`\`

The membrane would then:

1\. Assign a permanent prediction ID.
2\. Preserve the original terms and timestamp.
3\. Notify RED automatically.
4\. Schedule the resolver check.
5\. Prevent silent threshold changes.
6\. Require dated evidence for resolution.
7\. Notify dependent agents after the result.
8\. Regenerate the relevant dashboards and status views.

The agent would still decide what the evidence means. The membrane would ensure that the process happened correctly.

\#\#\# Core responsibilities

The smallest useful membrane would have three responsibilities.

\*\*One official state record.\*\* Facts such as prediction status, ownership, confidence, and due dates would be stored once in a typed record. README tables, agent status pages, review queues, and dashboards could be generated from that record, reducing contradictory copies.

\*\*Enforced actions and boundaries.\*\* The membrane would know which agents can propose, challenge, approve, or resolve each kind of object. It could prevent a resolved prediction from being silently reopened, stop an agent from writing outside its authorized scope, and require independent review where policy demands it.

\*\*Automatic handoffs.\*\* A data arrival, deadline, message, or state change would generate the next job automatically. For example:

\`\`\`text
CFTC data arrives
        ↓
SAM receives a resolution job
        ↓
SAM submits an evidence-backed outcome
        ↓
RED receives a verification job
        ↓
NEXUS receives the verified change
        ↓
Current-state views regenerate
\`\`\`

\#\#\# What should remain outside the membrane

The membrane should not determine whether a thesis is persuasive, whether two signals share a cause, whether a regime changed, or whether a trade is attractive. Those are research judgments for agents and the human operator.

Its purpose is narrower: ensure that judgments are attributed, timestamped, authorized, evidence-backed, correctly routed, and preserved after amendment.

A useful dividing line is:

\> Agents decide what things mean; the kernel membrane makes sure the process happens correctly.

\#\#\# Minimal first version

The first version should manage only three object types:

1\. \*\*Predictions\*\* — original terms, probability, resolver, falsifier, state, and outcome.
2\. \*\*Messages\*\* — sender, recipient, acknowledgement, deadline, and disposition.
3\. \*\*Jobs\*\* — owner, priority, dependencies, due time, required output, and completion evidence.

It could use an append-only event file plus SQLite for current state, with a small command-line interface such as:

\`\`\`bash
rw prediction register prediction.yaml
rw message send challenge.yaml
rw job claim job\_123 \--agent SAM
rw prediction resolve SAM-40 evidence.yaml
rw system check
rw render
\`\`\`

Git would remain the durable version history. Markdown would remain the human-readable research medium. The membrane would own only structured state transitions and generated current-state views.

\#\#\# Safe adoption path

1\. \*\*Shadow mode:\*\* Mirror a small prospective prediction cohort into structured events while existing files remain authoritative. Compare the two systems and measure discrepancies.
2\. \*\*Messaging first:\*\* Make the already well-tested messaging subsystem the first membrane-owned component. Existing inbox files can become generated views.
3\. \*\*Prospective predictions:\*\* Place only new trial predictions under membrane control; do not attempt to normalize all historical records immediately.
4\. \*\*Scheduling and health:\*\* Turn catalyst dates and resolution windows into jobs, then add one unified health view and an overdue/dead-letter queue.
5\. \*\*Brokered state changes:\*\* Require high-value operations—prediction registration, amendment, resolution, and thesis retirement—to pass validation before being committed.
6\. \*\*Generated canon:\*\* Generate roster counts, ownership tables, queues, and current-state summaries from the authoritative structured state.

\#\#\# Design constraint

The membrane must remain small. It should encode invariants—identity, permissions, transitions, timing, dependencies, evidence, idempotency, and provenance—not the repository's full analytical doctrine.

If it grows into another large interpretive layer, it will reproduce the current complexity in code. Its success should be measured by how much duplicated state, procedural prose, manual checking, and operator coordination it removes.

In practical terms, the kernel membrane would convert the repository from a well-governed organization whose participants follow written procedures into a hybrid system where creative research remains flexible but critical operational rules are enforced by a small trusted core.

\#\# Bottom line

The repository has already crossed the line from an experiment in prompting to a functioning research organization: it has roles, institutional memory, governance, challenge, provenance, and examples of decisions changing under evidence. Its next bottleneck is not more intelligence or more documentation. It is measurement discipline and operational simplification.

If the next phase standardizes forecast events, independently evaluates a prospective cohort, and moves core checks into CI, the system could demonstrate whether its impressive process produces durable analytical value. Until then, its clearest proven achievement is not predictive superiority; it is a high-quality, auditable process for generating, challenging, and remembering research hypotheses.
