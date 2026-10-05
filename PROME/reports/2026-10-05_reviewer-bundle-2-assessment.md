# Reviewer bundle 2 — PROME assessment

Will requested review of `REVIEWER_2_REPORT_2026-10-05.md` and `2026-10-05_reviewer-bundle-consolidated.patch` from Downloads. Reviewed against local HEAD `95bdada1c`; the supplied patch applies cleanly. This is a review of the new bundle, not another verification claim for the earlier safeguards implementation. No fleet/helpers spawned; no patch applied to the shared checkout, hooks installed, branch deleted or policy adopted.

**Recommendation: revise before adoption.** The changed-row cap, explicit declarations, broader artifact parsing and explicit BOARD advancement are useful directions. The bundle has operational defects that its green focused suites do not detect. The 2,000-byte cap and new blocking conditions remain proposals requiring their own authority; this review adopts neither.

## Findings

### 1. BLOCKER — consumer gate waits for another owner's repair, not PROME's required action

**VERIFIED.** Patched `PROME/tools/prome_gate.py:1470–1495` requires a clean strict fleet scan. Root Git Protocol step 1c requires PROME to verify a stale match and send its owner a packet; it forbids editing that owner's files. Sending that packet does not make the consumer's stale surface disappear, and the proposed gate has no disposition/packet receipt input.

Counterexample: a disposable `AGENTS/X/STATUS.md` carries gamma flip 12345. The real consumer checker returns 1 for 12345→12346 both before and after a correction packet is written to X's inbox. Thus a compliant handoff still blocks PROME's closeout until X changes its file. This is a stronger dependency than the existing rule, not merely making its reminder mechanical.

**Proposed change:** enforce that the scan ran and findings were dispositioned; keep actual receiver adoption pending in its existing owner record. Own-surface repair and cross-owner notification need different completion conditions. Do not make editing another desk or falsely declaring no supersession the practical escape route.

### 2. BLOCKER — unresolved numeric candidates can become a passing “no stale consumer” result

**VERIFIED.** The same wrapper exposes only OLD/NEW and calls neither `--unit` nor `--series`; its summarizer accepts rc 0 without a red glyph and labels it “no stale consumer.” The existing checker deliberately returns 0 for orange candidates pending human confirmation.

Counterexample: a live fixture line `HY OAS 320 bp is the current threshold.` checked against 320→321 returns rc 0 and one candidate with instructions to confirm series/unit. The proposed summarizer reports success. This is especially relevant to common short thresholds, not just exotic input. The wrapper also mentions `--mirror-map` in its advice but has no declaration path to run that required scope when applicable.

**Proposed change:** preserve candidate/unknown meaning, allow per-metric context and applicable mirror-map scope, and require a recorded judgment before claiming propagation clean. A scan can complete without proving every match resolved.

### 3. BLOCKER for parser adoption — legitimate paths are dropped or still unreadable

**VERIFIED** by calling patched `split_artifact_cell()` directly:

| Input | Actual output | Effect |
|---|---|---|
| `.claude/agents/argus.md + .claude/agents/coldreader.md` | `[]` | Silent loss of both targets; this form exists at DOCKET L362. |
| `PROME/tools/prome_gate.py:312 (fired-unexecuted)` | `PROME/tools/prome_gate.py:312` | Locator remains part of filename; actual DOCKET L364 form. |
| `PROME/DOCKET.tsv+PROME/GATES.tsv` | One combined token | Regression versus the old split-on-plus behavior; synthetic compatibility case. |
| Backticked paths joined by spaced middle dot | Two correct paths | The intended new case works. |

The report explicitly claims `:312` locators drop; they do not. No dedicated firetime parser test was added in this bundle. Wider target coverage is valuable, but the aggregate before/after totals are not proof that every remaining flag is real or that no target disappeared.

**Proposed change:** tests for actual docket syntax, leading-dot paths, line/range locators, legacy joiners and malformed/unresolved tokens. Preserve unresolved-token visibility rather than silently discarding plausible paths.

### 4. QUALIFICATION — bare boot is BOARD-non-advancing, not filesystem read-only

**VERIFIED.** CLI wiring stops BOARD advancement by default, but `mode_boot(False)` still invokes `spawn_slate.py --horizon 0` without `--stdout`. That tool writes `PROME/state/SPAWN_SLATE.md`. The Python function also retains the default `advance_board=True`, although the CLI passes False explicitly.

**Proposed change:** describe the narrower guarantee accurately, or make all child calls read-only and test all write surfaces. The suggestion to run this automatically from SessionStart needs a separate scope and concurrency assessment; preserving two BOARD hashes alone does not establish whole-command safety.

## Policy and rollout observations

- A changed-row cap covers both appended and edited content; grandfathered shrink-only behavior is sensible. The 2,000-byte value is still an operator choice. Treat migration of rule-class content as a separate semantic task: an undated PENDING obligation is not automatically a rule, and a new generic RULES.md could create another competing authority surface. Preserve existing owners, references and outstanding obligations.
- Blanket demotion of missing gitignored references deserves narrowing. “Not versioned” does not establish “not required on this host.” Distinguish expected local-only absence from an unavailable decision dependency; this is a design concern, not a reproduced production omission in this review.
- On this desktop, `core.hooksPath` already points to `scripts/githooks` per the earlier implementation receipt. Adding an executable pre-commit file there activates it on the next commit; the installer/banner is not a later activation boundary.
- Do not automatically delete the old review branch or transplant its remaining hunks from this report. Those recommendations need their own current-tree assessment. This review did not independently reproduce the report's historical growth/census figures or orphan-branch audit.

## Validation and limits

Applied only to disposable export `/tmp/prome-review2-kihf1jyh`:

- `git apply --check` against the current shared tree: PASS, no mutation.
- `test_docket_row_cap.py`: 17/17 PASS.
- `test_closeout_declarations_readonly_boot.py`: 14/14 PASS.
- `test_locks_safeguards.py`: 14/14 PASS.
- Python 3.12 with ResourceWarning treated as error. Initial incomplete export omitted settings and docket inputs; after restoring those tracked fixture inputs, the latter two suites passed. Those initial failures were fixture preparation errors, not patch defects.
- Independent counterexamples above: real consumer CLI in disposable repositories; direct parser calls; captured boot child command plus spawn-slate write-path inspection. Full outputs: `/tmp/prome-review2-kihf1jyh/counterexamples.json`.
- Did not rerun the report's entire regression inventory, live boot, real commit/push, hosted publication or branch deletion. Its broader results remain reviewer-reported.

**Disposition:** REVIEWED; proposed implementation WITHHELD pending the named fixes and policy decisions. Production implementation unchanged. No approval question is needed to complete this review.
