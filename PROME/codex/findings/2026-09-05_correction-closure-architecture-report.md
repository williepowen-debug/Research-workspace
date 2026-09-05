# Correction Closure as Reconciliation — architecture review and bounded integration brief

**Date:** 2026-09-05 · **Reviewer:** OpenAI Codex, external/cross-vendor instrument · **Audience:** PROME, WALTER, DAEDALUS, Will · **Status:** PROPOSAL FOR PROME ARTIFACT-VERIFICATION — not canon, not an instruction to edit owner files

## Executive conclusion

The fleet does not need a second correction system. It already has the important components: an owner-side retirement block, a pointer-weight central index, per-consumer receipts, `consumer_check`, an ordered consumption vocabulary, and owner-local state. The remaining weakness is the seam between **receipt** and **verified closure**.

The current generic correction checker records receipt IDs without retaining their actions. Consequently, `APPLIED`, `NO-OP`, `DEFERRED`, and `CONTESTED` all clear the same recipient boot warning. Separately, the WALTER register says a row may be retired when all named targets have receipted. Those two rules can make “everyone answered” look like “every stale copy was repaired.” That is a silent-pass risk.

External architecture practice supports a narrow repair:

1. Treat the owner correction as a versioned desired state.
2. Make each consumer reconcile its own projection against that version.
3. Keep receipt/acknowledgment separate from applied-and-evidenced disposition.
4. Close only against the current correction version, with evidence at the affected artifacts.
5. Preserve the old record and link the superseding correction rather than silently rewriting history.
6. Register one valid follow-up test only when unresolved analytical uncertainty survives; otherwise state `NONE` and stop.

The recommended implementation is one action-aware closure mode in the existing checker, a small amendment to the existing correction form and register prune rule, and a three-correction pilot. No new ledger, dashboard, monitor, agent, forum, or recurring cadence is proposed.

## 1. Verified current-state findings

The following are **ARTIFACT-VERIFIED** in the repository on 2026-09-05. PROME should re-check them before acting, consistent with the Codex charter.

### F1 — the owner-side correction form is already strong

`AGENTS/DAEDALUS/BLUEPRINTS/CORRECTION_FORM.md` already requires:

- a contaminated `source × surface × date-range` class;
- a reproducible replacement with instrument, basis, capture stamp, and pull recipe;
- an explicit statement of what survives;
- greppable kill strings;
- a scoped search instrument for absence claims;
- relay and archive propagation.

It also states that the owner retirement block is the substantive record and that the register points to it. This is the correct **index-not-store** architecture. The report does not propose a competing correction record.

### F2 — the vocabulary already distinguishes receipt from closure

`AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` Class 11 orders the lifecycle as:

`ROUTED → DELIVERED → CONSUMED → ENCODE-CONFIRMED → CLOSED-VERIFIED`

It explicitly says that `CONSUMED` does not mean the consumer’s surfaces changed, and that `CLOSED-VERIFIED` requires checking the encode at the artifact. The conceptual rule is therefore already canon. The gap is executable correction-specific enforcement.

### F3 — the correction checker currently proves receipt presence, not applied state

In `scripts/corrections_boot_check.py`, `cmd_check` loads receipts into a `set` containing only `correction_id`. It discards `action` and `note`. Any receipt ID then causes the correction to be skipped for that desk. The writer accepts all four actions, and the note may be empty.

Concrete consequence: a recipient can write `DEFERRED` or `CONTESTED`; subsequent boot checks report no unreceipted named row even though the consumer has not applied the correction. This may be acceptable as a **delivery/triage** check, but it cannot be used as a closure proof.

### F4 — the central prune wording is broader than verified closure

`AGENTS/WALTER/registry/CORRECTIONS.tsv` says WALTER retires a row “when all named targets receipted, or date_cap passed.” The same file defines receipt actions including `DEFERRED` and `CONTESTED`.

The safe distinction is:

- all targets receipted = the distribution/triage phase is accounted for;
- all targets terminal with evidence = the scoped correction is closable;
- date cap passed with incomplete reconciliation = `DEAD-AT-CAP`, not successful closure.

### F5 — an adjacent proposal should be integrated, not duplicated

`AGENTS/DAEDALUS/design/2026-08-28_CORRECTION_CLASS_VALIDATION_PROPOSAL.md` already proposes C1–C5: separate kill from replacement, independently validate correction-born claims, re-pull adjacent dated quantities, grep the old regime on a reversal, and verify that claimed instrumentation exists. PROME’s WQ-109 record assigns P4 a dedicated sitting.

This closure proposal is the **last-mile companion** to P4, not a replacement or second sitting. C1–C5 governs correction content and validation; this report governs reconciliation and terminal state.

## 2. What established systems do

### 2.1 Kubernetes: desired state, observed state, and generation-aware status

Kubernetes controllers continually compare desired state with actual state and make bounded changes to reconcile them. Its `observedGeneration` field identifies the exact desired-state generation on which a reported status is based; a healthy-looking status attached to an older generation is stale. Sources: [Kubernetes controllers](https://kubernetes.io/docs/concepts/architecture/controller/) and [Pod observed generation](https://kubernetes.io/docs/concepts/workloads/pods/#pod-generation).

**Fleet translation:**

- owner retirement block = desired corrected state;
- correction ID = generation;
- each affected desk = controller over its own files;
- consumer receipt = reported observed state;
- evidence pointer = where actual state can be inspected.

A correction’s meaning should become immutable once routed. If a correction is itself corrected, issue a new correction ID that explicitly supersedes the prior ID. A receipt against the earlier ID cannot close the later correction.

### 2.2 Transactional outbox: make the truth change and its notice one operation

The transactional-outbox pattern addresses the “dual write” failure in which a service updates its database but fails to emit the corresponding message, or emits a message for a transaction that does not commit. The state change and outbound event are recorded atomically; delivery can then be retried, and consumers use stable event IDs to process duplicates idempotently. Sources: [AWS transactional outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) and [Debezium outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html).

**Fleet translation:** the owner’s canonical correction and owner-local retirement/correction notice should land in the same owner commit. WALTER’s register should index or mechanically ingest that owner record rather than become an independently authored statement of correction substance. If routing is retried, the stable correction ID makes the duplicate harmless.

This honors ownership boundaries: the originator writes its own truth and notice; WALTER owns the index and pruning; consumers edit only their own surfaces.

### 2.3 Git and Crossref: publish a linked correction instead of rewriting public history

Git’s public-history model recommends a new revert commit that records the reversal rather than rewriting a published commit. Crossref’s Crossmark practice likewise recommends separate, linked correction/retraction notices for significant changes because in-place corrections obscure the scholarly record; minor editorial changes do not enter the full correction lifecycle. Sources: [Git revert](https://git-scm.com/docs/git-revert), [Git user manual — fixing mistakes](https://git-scm.com/docs/user-manual.html#fixing-mistakes), [Crossref registering updates](https://support.crossref.org/hc/en-us/articles/115000501246-Crossmark-registering-updates), and [Crossmark](https://www.crossref.org/services/crossmark/).

**Fleet translation:** preserve the wrong statement as historical/superseded, link the replacement, and reserve fleet-wide correction machinery for changes that affect interpretation, decisions, live tests, or downstream state. Typography and harmless wording edits should remain ordinary edits.

### 2.4 Kafka: reduce independently maintained copies

Apache Kafka’s compacted-log model retains the latest value for a stable key and uses explicit tombstones for removals, allowing consumers to rebuild current state without turning every historical copy into an independent authority. Source: [Apache Kafka log compaction](https://kafka.apache.org/35/design/design/#compaction).

**Fleet translation:** when a downstream surface does not need to freeze a value, carry a canonical pointer plus the observed correction/version ID instead of copying the number or claim. Generated views should derive from owner state. Necessary cached copies should identify the owner, basis, and observed version. This reduces the number of surfaces that correction propagation must touch.

### 2.5 Google SRE: actionable remediation and measurable closure

Google SRE’s postmortem guidance emphasizes owned, tracked action items with concrete success criteria and warns that vague calls to make people more careful are weaker than system/process changes. It also emphasizes action-item closeout, not only postmortem production. Source: [Google SRE postmortem culture](https://sre.google/workbook/postmortem-culture/).

**Fleet translation:** a surviving next test must name an owner, an observable source/object, a trigger or due date, and a grading rule. “Watch,” “eyeball,” and “verify better” are not closure-capable tests. Conversely, do not mint a prevention project for every correction.

## 3. Proposed correction-closure contract

### 3.1 One immutable transaction key

Use the existing `COR-YYYYMMDD-NN` as the correction generation. Once a correction is routed, do not change its substantive meaning in place. A correction-to-a-correction receives a new ID and names `supersedes=COR-...` in the owner record.

This prevents an old receipt from laundering a later revision and makes duplicate delivery safe.

### 3.2 Owner phase

The originator:

1. Corrects the canonical owner artifact.
2. Adds the existing retirement block, preserving the contaminated claim as superseded rather than deleting history.
3. Records `HOLD`, `WEAKEN`, or `FLIP` for conclusions built on the corrected material.
4. Separates any newly inferred replacement claim under the existing P4/C1 proposal rather than letting it inherit correction authority.
5. Runs `consumer_check --self` or the appropriate literal/regime scan until no unmarked live owner copy remains.
6. Commits the canonical correction and owner retirement notice together.

### 3.3 Routing phase

The originator runs the existing cross-agent scan and names known consumers explicitly. `ALL` may remain a safety broadcast, but it must not imply verified fleet-wide reconciliation. A significant correction with known holders should use named targets.

The register remains a pointer-weight WALTER index. It must not duplicate the correction’s full analytical content.

### 3.4 Consumer reconciliation phase

Each named consumer owns its own disposition. Re-applying the same correction should be harmless.

| Receipt action | Terminal for closure? | Minimum evidence |
|---|---:|---|
| `APPLIED` | Yes | `artifact=<path:line-or-stable-key>` showing the corrected/superseded state |
| `NO-OP` | Yes | `scope=<paths/query>` and reason the consumer did not carry actionable stale state |
| `DEFERRED` | No | `review=<ISO-date>` plus blocker/reason |
| `CONTESTED` | No | dispute basis plus `escalation=<PROME pointer>` |
| missing | No | none |

`NO-OP` is not “I do not want to do it”; it means the target inspected its declared scope and no application was required. Historical copies count as `NO-OP` only when visibly historical/superseded or otherwise excluded by the correction’s contaminated class.

### 3.5 Successor-test phase

Add a conditional field to the owner retirement block:

```text
validation_ref=<owner path:row-or-section> | NONE
```

Use a pointer rather than copying test prose into `CORRECTIONS.tsv`.

If unresolved analytical uncertainty survives, the referenced test contains:

- owner;
- observable source or named object;
- trigger/date;
- grading rule, including what result would preserve, weaken, or kill the surviving claim.

If no valid instrument presently exists, `NONE` is honest closure of the correction transaction; the analytical claim remains `NO VERDICT` or is retired. Do not invent an “eyeball” test merely to fill the field. PROME’s DOCKET receives the successor only when it needs a cross-desk wake-up, dated coordination, or Will decision. Owner-local tests remain owner-local.

### 3.6 Closure invariant

A named-target correction may become `RETIRED` only when:

```text
owner retirement block exists
AND owner live-copy scan is clean
AND every named target's latest receipt is APPLIED or justified NO-OP
AND every APPLIED receipt has an artifact pointer
AND a final scoped stale-copy scan has no unmarked live result
AND validation_ref resolves to an owner artifact or equals NONE
```

Then WALTER may label the chain `CLOSED-VERIFIED` and retire the index row.

`DEFERRED`, `CONTESTED`, and missing remain nonterminal. Expiry with incomplete reconciliation becomes `DEAD-AT-CAP`; it is not success. For `ALL` rows, closure claims must state their verified target scope. A broadcast cannot prove that every desk reconciled.

## 4. Minimal tool amendment

Do not change the existing boot check’s meaning silently. Preserve it as a receipt-presence/triage check and make its output state its perimeter. Add an action-aware mode, for example:

```bash
python3 scripts/corrections_boot_check.py --closure COR-20260905-01
```

Recommended return contract:

- `0 CLOSED-VERIFIED` — all closure invariants the tool can inspect pass;
- `1 OPEN` — one or more named consumers are missing, deferred, contested, or terminal without required evidence;
- `2 CANNOT-EVALUATE` — malformed register/receipt, unknown target, missing owner pointer, ambiguous latest receipt, or invalid evidence syntax.

Implementation properties:

1. Load the **latest append-only receipt per `(agent, correction_id)`**, preserving `action` and `note`; use append order to break equal timestamp ties.
2. Treat only `APPLIED` and evidence-bearing `NO-OP` as terminal.
3. Validate forward-only structured note prefixes (`artifact=`, `scope=`, `review=`, `escalation=`) rather than migrating every existing TSV header.
4. Confirm the owner pointer and evidence paths exist. State explicitly that path existence proves repository disposition, not external truth.
5. Never edit consumer files or auto-retire a row. The tool reports; WALTER performs its owned status-token change after reading the result.
6. Keep correction application idempotent: a duplicate packet or repeated run must not create a second state change.

Recommended fixtures:

- `APPLIED` with valid evidence → terminal;
- `APPLIED` with empty/missing evidence → open or cannot-evaluate, never green;
- justified `NO-OP` with scope → terminal;
- empty `NO-OP` → nonterminal;
- `DEFERRED` with future review → open but not malformed;
- `DEFERRED` without review → cannot-evaluate;
- `CONTESTED` → open and escalation named;
- duplicate receipts `DEFERRED → APPLIED` → latest action governs;
- a receipt for superseded correction A does not close correction B;
- missing evidence path → cannot-evaluate;
- expired unresolved row → `DEAD-AT-CAP`, never `RETIRED`;
- `ALL` row → scope-limited report, never an unqualified fleet-wide close.

## 5. Integration ownership

This should ride the already-approved WQ-109/P4 venue rather than create another governance item.

| Owner | Bounded responsibility |
|---|---|
| **PROME** | Verify this report at artifacts; merge the closure question into the existing P4 sitting; coordinate the pilot; do not create a second store |
| **DAEDALUS** | Reconcile this proposal with C1–C5; amend `CORRECTION_FORM.md` and any vocabulary pointer once Will rules; preserve one-home-per-rule |
| **WALTER** | Amend the `CORRECTIONS.tsv` prune semantics; operate the pointer index and final retirement token |
| **Tool implementer designated by PROME/Will** | Add the action-aware closure report and fixtures to the existing script; no auto-edits |
| **Domain owners** | Correct their canonical records, scan their own surfaces, disposition inbound corrections, and provide evidence from their own artifacts |

## 6. Pilot

Use three recent, different-shaped corrections rather than a fleet-wide migration:

1. **CARL — transplanted date/weekday correction:** tests multi-surface propagation and correction-of-correction handling.
2. **STUE — MOHELA/CFPB validation mechanism:** tests whether the successor is genuinely capable of grading the surviving claim rather than merely dated.
3. **HANS — PMI headline versus active rows:** tests canonical-headline correction with stale internal projections.

For each pilot correction, record only:

- owner-fix time;
- last terminal-consumer time;
- live stale copies found by the final scan;
- whether the correction itself required a new correction within seven days;
- validation pointer or `NONE`.

The pilot succeeds if all three can reach an evidence-backed terminal state without a new ledger, manual dashboard, or continuing discussion thread. A result of `DEAD-AT-CAP` or `CONTESTED` is informative, not a reason to redefine it as success.

## 7. Explicit non-goals and stop rule

Do **not** build:

- a full Saga/workflow engine;
- a second correction/refutation ledger;
- a correction dashboard before the already-registered generated-view trigger fires;
- another monitoring agent;
- a forum thread for routine corrections;
- fleet-wide retroactive receipt migration;
- “exactly once” delivery machinery;
- a mandatory new empirical test for every correction;
- a postmortem or memory promotion for every bad datum.

Once the closure check is green and WALTER retires the row, stop. A broader postmortem or new fleet rule is justified only when the defect:

- escaped into several decision-bearing consumers;
- produced a correction that was itself wrong;
- exposed a silent-pass tool failure;
- or repeated enough to establish a class rather than an anecdote.

## 8. Decisions requested at the P4 sitting

PROME can present the following as one bounded ruling package:

1. **Receipt is not closure.** Ratify the correction-specific mapping to Class 11.
2. **Terminal actions.** `APPLIED` and justified `NO-OP` are terminal; `DEFERRED`, `CONTESTED`, and missing are not.
3. **Immutable correction generation.** A correction-to-a-correction gets a new ID and a supersession link.
4. **Conditional successor.** Every correction names `validation_ref=<pointer>|NONE`; a successor is required only when live uncertainty survives and a valid test exists.
5. **Target-scoped closure.** `ALL` is dissemination, not evidence that all consumers reconciled.
6. **Action-aware closure report.** Add it to the existing checker with fixtures and explicit PASS/NOT-PROVED semantics.
7. **No additional surface.** Preserve owner record → WALTER pointer index → recipient-owned receipts as the complete topology.

## Bottom line

The outside systems converge on a simple idea: **publish an immutable correction, let each owner reconcile its own state, attach status to the version actually observed, and close only on current-state evidence.**

The fleet already has most of this design in prose. The high-value integration is to make the last transition executable:

> A receipt proves delivery or triage. A terminal receipt with an artifact pointer proves a consumer disposition. A corrected owner record, clean scoped consumers, and a valid successor pointer—or `NONE`—prove closure.
