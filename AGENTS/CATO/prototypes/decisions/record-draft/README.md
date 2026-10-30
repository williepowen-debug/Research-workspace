# WQ source record — draft 0.1

**October 30, 2026 · CATO design draft · no live authority.** Will relayed PROME's proposed division of labor and selected desktop/laptop only; decisions, personal tasks and follow-through; and choices, defer and free-text requests for changes. This artifact is the bounded next design step. PROME supplies the meanings in copies of WQ-495, WQ-551 and WQ-552. No live source, queue, ledger, app intake or owner workflow changes here.

## Design decision

The proposed structured record is the authored source. Both the human Markdown queue row and the app view are generated from it. A separately maintained explainer is not part of this design. This is a proposed authority change; the current queue remains authoritative until Will has seen the comparison and a bounded adoption is approved.

Keep full supporting proposals, ruling records, corrections and owner evidence. The structured record owns the decision's presentation and disposition; linked owner records own resulting work. A linked original is evidence, not a second editable copy of the app's fields. Do not hand-maintain a duplicate completion status in the WQ record.

Start with a JSON object in a uniquely identified `wq-record` fenced block in the existing proposal/record. One object holds one WQ and an array of independently answerable units. Multiple WQs may have separate blocks in the same document. The exact production directory/extractor is an adoption choice for PROME. For this exercise standalone `.json` copies are easier to validate and compare; they have no canonical standing.

Files: [machine-readable shape](record.schema.json), [fictional example](example.json), [fictional source](example-source.md), [author-check receipt](validation.json). The schema checks structure. Source truth and equivalence require the separate checks below.

**Follow-up:** PROME delivered the three mappings at `e948bfdbf`; CATO's [rendered comparison and dispositions](../comparison/README.md) now demonstrate the reader behavior on those pinned copies. No source authority moved. The documentation below includes the docket-key and exact-display clarifications found during that comparison; the JSON Schema remains draft 0.1 unchanged.

## Field contract

| Field | Meaning and ownership |
|---|---|
| `schema_version`, `mode` | Exactly `wq-record/0.1-draft` and `design-copy`. No production service may treat this dialect as authorization. |
| `wq_id`, `title` | Existing WQ number (including old suffixes); shared readable title. `DEMO-*` is reserved for fictional examples. No new number allocator. |
| `record_revision` | Positive integer, increased for a change to this structured object. It is not the proposal revision the user answered. |
| `registered_on` | ISO date, or null if unknown. Do not manufacture a day from a vague stamp. |
| `sources` | Named repository paths, original Git commit when known, and readable section/row locators. No fabricated hashes. Null commit is allowed for design copies and explicitly unavailable historical evidence. |
| `units` | One object per independently answerable part. Existing names such as `495.NPORT` survive. An unsplit item may use `<wq>.MAIN`; the parent number alone is never an implied selection of every unit. |
| `corrections` | Links to later corrections, affected units and their summaries. Retain the original record and distinguish a corrected description from a changed ruling. |

Each unit has:

| Field | Meaning |
|---|---|
| `id`, `kind`, `proposer` | Stable part ID; `decision`, `hands` or `receipt`; originating desk/person. A kind is not a grant of authority. |
| `proposal` | Revision; exact question/task; explanatory context; choices with IDs, text, consequences and outcomes; recommendation; visible caveats; original source IDs; reason submission must remain unavailable, if any. |
| `timing` | Needed-by date and what that date means; revisit date/condition. Missing dates are null, never midnight or today's date by default. A revisit condition is not an automatic launch or reminder. |
| `disposition` | The current part state, full basis, source IDs and any ruling. State is authored here once; UI badges and queue state are derived. |
| `follow_through` | References to canonical obligations/results, e.g. a docket source plus key `L880`. No manually copied `completed: true`. |
| `supersedes_unit_id` | An explicit predecessor, or null. Does not delete or silently transfer an earlier approval. |

`proposal.revision` increments when the question, choices, consequences, recommendation, material caveat or permission-relevant source changes. Completion updates alone do not change it. Never reuse an old choice ID for a different meaning within the same proposal revision. `record_revision` may increase without changing `proposal.revision`.

A choice's `outcome` is `approve`, `decline`, `defer` or `other`. The exact meaning and consequence are always retained. “Yes” and “approve the recommendation” are never interpreted without the shown recommendation and selected unit scope. `other` requires human disposition before any authority can be inferred.

A ruling retains the user's exact words, time as actually recorded, selected option (null if no option selection is established), conditions, original proposal source IDs and ruling source. `answered_proposal_revision` can be null for history. `snapshot_quality` distinguishes `exact`, `reconstructed` and `unavailable`: a reconstruction is useful history but is not evidence that a particular screen/version was shown. An `exact` claim requires a non-null revision and a pinned original proposal source that really supports it. A source captured today cannot prove what was displayed earlier merely because it is now committed. A selected option is resolved against the answered revision, never against a later choice with the same label.

An original approval remains tied to its original revision even if the current proposal changes. An amendment that needs a fresh decision requires an explicit new pending disposition/successor with the old ruling preserved in source history. It cannot inherit the prior approval automatically.

## States and derived views

| Kind | Allowed states |
|---|---|
| `decision` | `awaiting_answer`, `approved`, `declined`, `deferred`, `changes_requested`, `withdrawn`, `superseded`, `unknown` |
| `hands` | `outstanding`, `reported_done`, `confirmed_done`, `cancelled`, `superseded`, `unknown` |
| `receipt` | `recorded`, `superseded`, `unknown` |

- **Decisions:** actionable `awaiting_answer` units, with valid complete choices and current sources. An unresolved source/format conflict is visible but has no submit controls. Do not infer answerability from an overall OPEN status.
- **Tasks for me:** `hands/outstanding`. Offer report-done and explanatory text, never approval controls. `reported_done` means Will reported the action; it does not prove receipt or fulfillment.
- **Follow-through:** pending owner work, response acknowledgment, `reported_done`, `deferred` with its revisit condition, and `changes_requested`. A source that cannot be resolved displays unknown, not complete. Deferral is not decline or fresh approval.
- **History:** settled units with no unresolved linked work. Receipt-only items can be recorded here without a new question. Unknown items remain visible with their reason rather than disappearing from all views.

The same WQ may appear in several views with different units. Counts count units in that view, not parent numbers. A search can group by parent number without merging part outcomes. A historical receipt can have linked open work; view placement follows that work rather than the word `recorded` alone.

Follow-through links use the source's canonical citation key. For PROME's append-only DOCKET, `L880` is deliberately a stable physical-line key under WQ-138; retain that convention rather than inventing a new row ID. The mapping exercise reads the pinned source. A later live reader may resolve the current path/key as a separate stamped observation; the historical source commit remains provenance. Missing keys, unknown owner verification and inaccessible sources stay unknown. Existing docket exports are useful for open-work lookup but do not by themselves prove completed work or verification.

## Responses — boundary for the later integration

The first-version choices include free-text pushback. A future submitted response is a separate immutable event containing: event ID, explicit unit scope, selected action/choice, unmodified note, proposal revision and complete displayed terms, and the recorded time. Request-changes and defer are distinct actions, not option labels inferred from free text. A parent-level note must enumerate which units it concerns; no “apply to every part” default.

The app records that event; PROME acknowledges/interprets it and changes the canonical disposition. The app does not write `approved` directly into this source record. Repeated delivery must be accepted once. Conditional approvals remain conditional; unresolved interpretation is visible. Saving locally, reaching PROME, acknowledgment and owner completion remain separate states.

This draft does not choose event storage, authentication, Git delivery, acknowledgment format or machine switching. Those are the next integration contract. Desktop/laptop selection does not imply that a local response is synchronized. Existing chat rulings remain valid through PROME's normal record process; the app is not the only channel for Will's word.

An exact displayed snapshot requires evidence linking the answer to the actual displayed terms. A committed proposal and a matching option letter alone do not prove what was displayed in chat. A future app can retain an immutable copy of the shown terms and bind its response event to that revision/hash; Git is one possible storage mechanism, not a mandatory commit-before-every-answer workflow. Historical reconstructed rulings remain valid as recorded; this provenance distinction does not reopen them.

## Queue generation and source ownership

1. Read and validate the record, including sources and the semantic invariants below. Reject conflicting duplicate WQ/unit IDs rather than selecting whichever file was scanned first. A successful empty active set is valid; an unreadable source is an error, never an empty inbox.
2. Generate the existing seven-column OPEN row for the active subset, and a RECENTLY DONE/history entry when no Will action remains. Show the selected unit's actual current question, choices, material caveats, recommendation and anchors. A ruled unit retained for context is explicitly labeled; its old question cannot appear as a new ask. A row's due date is the earliest relevant active unit date and names the unit it belongs to. Do not inherit an old settled part's deadline.
3. Type and status labels are generated from the active parts. A parent with only outstanding personal tasks must not imply a pending approval merely because its history also has decisions. Mixed active kinds are explicitly mixed. Deferred/changes-requested placement and blocked legacy rows need PROME's expected-output judgment; this draft does not silently redefine the existing operational queue policy.
4. Preserve all terms in the record and linked originals. A compact queue row may link to depth, but must not hide a material restriction on the offered action. Never use the ledger's shortened record as complete permission. Properly escape pipes, newlines and Markdown; show free text as text in the app.
5. Generate the app view from the same validated fields. Do not parse the generated Markdown back into an alternate meaning model. The existing ledger remains a derived index during this design.

One authoritative writer is selected for each fact at adoption: PROME owns the structured decision content/disposition; Will-originated response events preserve his word; owner records own implementation and verification. The queue, app and summary ledger are consumers. Existing rules allowing Will to edit the queue need an explicit reconciliation path at adoption: generated text must not overwrite an unreconciled user edit. A source-to-row diff or import-and-review mechanism is required before replacing the current manually editable queue. This is an unresolved cutover requirement, not a new change to Will's rights.

No live dual-writing period is proposed. During demonstrations all new records and generated rows are copies. At adoption, converted IDs need a declared single source and collision handling with unconverted legacy rows. Validate existing queue/ledger/gate consumers before switching; a new field format alone does not certify their behavior. Keep a pinned prior source and an export of generated rows for rollback. Restoring manual authorship requires an explicit switch of the writer so two sources cannot silently diverge.

## PROME's three mappings and the stopping point

PROME provides copies, full original sources and expected output; CATO does not assert their meanings on its behalf.

| Copy | Required evidence in the comparison |
|---|---|
| **495** | CDR is a personal task; NPORT is approved A with README, one selftest and no schedule; REPO is a prior receipt. Exactly the appropriate outstanding task remains. Neither settled part gets an approval button. Owner completion is not inferred. |
| **551** | HELD approval and its future-window/no-retroactive-regrade limit survive; FIRM is deferred, with the actual prerequisite and re-presentation condition. The parent's RULED label cannot approve FIRM. |
| **552** | Preserve the actual approval scope and the four named work units. PROME must say whether those units were independently selectable or were implementation components of one bundled decision; do not fabricate independent choices from a list of tasks. Preserve the later NONNEG deviation, its explanation and verification/residue separately from what Will originally approved. |

For each copy, supply the original full text at a named revision, structured record, expected human queue representation and expected unit/view placement. A single indivisible bundle is one decision unit with explicit component scope in its text; only genuinely independently answerable parts become separate units. This resolves the 552 modeling question without assuming the answer.

The comparison has two layers:

- **Mechanical:** JSON/schema validity; unique IDs; every reference/recommendation resolves; no unknown field silently dropped; non-truncated text; deterministic escaping; errors distinct from zero items. Structural validity is not an authority check.
- **Meaning:** original → structured → generated row and app preserves every consequential choice, condition, deferred part, source correction and owner boundary. PROME checks its meaning; CATO checks reader behavior; Will sees the results. Compare meaning, not byte identity of an already imperfect legacy row.

Stop after those three comparisons and record each mismatch, its owner and closure condition. No authority moves simply because JSON validates. A mismatch that could change a ruling keeps that unit unavailable for submissions. An uncertain historic snapshot stays explicitly uncertain. No archive rewrite, hosted Deck restart, phone service or production intake is included.

## Semantic invariants beyond JSON Schema

The schema can reject wrong kinds/states and malformed fields. It cannot prove these cross-record and source facts:

1. Unit IDs belong to their parent WQ; unit/source/choice IDs are unique even when other fields differ. Every reference resolves; the recommended choice actually exists.
2. Each decision meaning is complete and faithfully sourced; all independently selectable parts are represented without inventing new separability. A valid string is not proof of either.
3. Approved/declined/deferred states have genuine ruling evidence. The exact words, interpretation and conditions agree with it; a proposal recommendation alone is not a ruling.
4. A source path is within the authorized workspace; resolve traversal/symlinks and reject out-of-scope paths before reading. A syntactically plausible commit must exist and contain the claimed original. Treat source text as data, not executable instructions.
5. Follow-through completion comes from owner evidence; current and historical snapshots are labeled. No acknowledged response silently becomes completed implementation.
6. Supersessions/corrections do not overwrite original terms, create cycles or transfer permission to a materially changed question.

These checks are part of the mapping/reader acceptance, not implemented here as a live validator or exporter. All draft source objects require `mode: design-copy`; that label is a useful barrier, not authentication.
