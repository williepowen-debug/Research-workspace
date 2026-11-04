# L835 independent acceptance — PASS within the bounded scope

Date: 2026-11-04. Reviewer: `/root/l835_acceptance`, the single authorized independent reviewer. Runtime: Codex; provider OpenAI; exact model identifier UNKNOWN. Native shell/exec and collaboration messaging were available. No additional reviewer or subagent was launched.

**Verdict: PASS. No confirmed blocking finding. L835 remains OPEN and installation remains WITHHELD.** This is acceptance evidence for the exact candidate below, not a production audit, permission to mark any operational receipt REVIEWED, or installation approval. No repair was made.

- Candidate tested: `5a2edeec2c7414c612478d59e32883bb527cef40`.
- Baseline: `cf20665b2ecf9c19980e5030bc9e38293b44f25b`.
- Candidate checkout: `/home/willi/l835-phase2`; shared operational repository: `/home/willi/Research-workspace`.
- Root CLAUDE.md and AGENTS.md explicitly read; design, migration, actual four source modules, historical acceptance history, COMPLETION_SPEC, runtime mechanics and reviewer charter consulted. Read-only review exemption applied; no domain boot/ownership assumed. The parent assignment limits shared writes to this evidence directory and overrides ordinary owner commit/closeout routines.
- Execution occurred in disposable copies/repositories, not the candidate checkout. `integrity-before.json`, `integrity-after.json` and `tested-copy-integrity.json` establish identical candidate HEAD, clean candidate worktree, unchanged four production source hashes and matching tested copies. No operational manifest, baseline, docket, status, installation or Git index was changed by this reviewer; shared writes were review artifacts in this directory only. No commit or push.

## Independent challenge and mathematical assessment

I wrote `independent_policy.py` separately from the author suite. Its reference matcher uses direct string splitting, exact depth and suffix comparisons; it imports no production parser, partition or transition helper for the oracle. Seed **1104835** generated 150 larger ordered lists in addition to all 400 two-row combinations of ten patterns and two classes. **550 policies, 2,750 descendant queries, 687,394 concrete comparisons PASS.** The reference enumeration uses nine segment values (including Unicode, newline and nested suffixes), and absolute depth five, beyond the largest fixed prefix in this generated domain. Early protected witnesses end positive enumerations; negative enumerations exhaust the finite reference domain. This finite check supplements, rather than proves, unrestricted correctness.

The reversed-trie proof survives inspection: every valid segment read backwards either ends at a trie node or first exits an edge. At an exact end, concrete literal/suffix truths are exact. At first exit, only suffix terminals already traversed remain true; no later suffix or literal can become true. All edges are ASCII, so a valid non-ASCII exit exists at every node. Reserved endpoints are excluded, and first-exit atoms always have valid realizations. Thus the produced vectors cover the valid domain without impossible vectors or missing complementary names. The `any` predicate is constant. First-match classification preserves order and fully/partially shadowed rules.

The depth bound also survives inspection. Let D be maximum fixed-token length. At absolute depth D+1 every exact rule is dead and every surviving recursive rule has consumed at least one tail segment. Subsequent transitions keep those recursive rules looping and dead rules dead. Classification cannot change thereafter. Queries starting deeper still examine one positive extension. Counting repeated reachable states by depth is conservative for the resource budget; exhaustion raises EvaluationError, never an exclusion result.

My new candidate counterexamples, also exercised through real Git visibility and the actual Standard/Light ARGUS consumer, were:

1. **Missed-protection challenge:** `r/*.md EXCLUDED`, then `r/* OWNED`, then `r/*/** EXCLUDED`. A visible `r/.gitignore` hides `r/é`; suffix exclusions must not stand for the complement. The control is guarded and both consumers block (rc 1).
2. **Unnecessary-block challenge:** replace the whole-segment OWNED rule with EXCLUDED; direct children and deeper descendants are now completely excluded. The same visible control and hidden file leave working-tree verification and Standard/Light at rc 0 after a synthetic reviewed fixture. A separate pure-policy case places a later `r/*.x.md OWNED` beneath complete finite/recursive shadowing and still proves exclusion.

`independent_integration.py` additionally checks malformed whole-policy refusal, legacy operational refusal, FROZEN after re-freeze with no legacy reuse, restoration of an earlier schema-3 receipt without delivering changed bytes, and actual old schema-2 code/receipt rollback over newly committed unreviewed work. That last strict `--ref/--snapshot` verification returns rc 1 and preserves receipt bytes. **Four independent integration tests PASS.** Synthetic review marking tests wiring only; none is a real audit.

## Completed / uncompleted matrix

| Check | Status and evidence |
|---|---|
| Current grammar, ordinary classification, Unicode/newline, suffix overlap, reserved names, malformed rows and unsupported syntax | PASS: independent scripts plus `regressions.log`; current perimeter and shadowed CLAUDE row covered. |
| Reversed-trie completeness, depth bound, missed protection, unnecessary blocking, overlaps and unmatched deeper descendants | PASS within reviewed grammar: independent argument and differential experiment above; author regressions include historical salts/probes and supported analogues. |
| Limits/errors propagate as CANNOT-EVALUATE / rc 2 | PASS: actual lowered state limit independently exercised; existing suite exercises actual limit and injected exceptions across operational entry points and consumer. Production 100,000-state worst-case stress is not a performance certification. |
| Actual Git controls: pending/staged/desk-committed/overlap, before/after freeze, force-added paths, deletions, foreign arrivals; attributes separately | PASS: current integration regressions plus independent real ignore/hidden-file cases. NUL-safe inventory verifies which names remain visible. |
| Actual Standard and Light ARGUS consumer | PASS: actual `check_review_manifest` plus `aggregate_rc`, not a copied predicate. Standard rejects FROZEN and legacy; valid REVIEWED fixtures pass; relevant malformed/unknown receipt paths retain rc 2. |
| ARGUS subprocess freeze/verify/mark, working tree/ref/snapshot, observe and candidate delivery | PASS: existing integration and adjacent regression suites; independent legacy rejection and new-work rollback challenge. |
| Schema 2 refusal/schema 3 re-freeze; missing/unknown schema/pin; policy binding/mirror mutation; policy changes disable reuse; old reader rejects new receipt | PASS: current regressions and independent migration checks. Exact historical receipt tested and preserved. |
| Review/rollback cannot certify newly committed unreviewed content | PASS: independent schema-2 actual-code and schema-3 receipt restoration checks, strict ref/snapshot refusal; migration drill additionally preserves unchanged historical bytes. Working-tree success may describe an older immutable candidate, never approval of later edits. |
| Byte-identical moves, authorship, immutable candidate, reuse, hooks/index safeguards | PASS: current contract/WQ-583/evidence/closeout suites. No claim that retired schema-1 move APIs remain live. |
| Existing current regressions | **259 PASS**, 26.968 seconds; warnings promoted to errors; `regressions.log`. |
| Historical consumed-move suite | **37 PASS**, 2.729 seconds, against exact old baseline only; `historical.log`. Historical code is deliberately distinct from replacement acceptance evidence. |
| Exact candidate/source integrity | PASS: before/after JSON and tested-copy comparison. |
| Full unrelated Standard/Light closeout command and production deployment inputs | NOT RUN: consumer-specific bounded review, no production execution/installation authorized. |
| Production migration, operational review promotion, delivery, baseline advancement, installation | NOT PERFORMED / WITHHELD. L835 remains OPEN. |
| Universal generated-policy testing or general glob semantics | NOT CLAIMED. Grammar is intentionally narrow; unsupported original patterns are refused, not reinterpreted. |

## Historical findings and remaining boundaries

The old witness failures (one exclusion, seven salts, first-match shadowing, deeper UNATTRIBUTED paths), embedded-double-star missed protection, and subsequent unrelated-pattern false blocking were read in preserved acceptance history and considered against the new grammar. Unsupported original patterns now receive explicit syntax refusal; supported equivalents exercise both blocking and wholly excluded cases. The interrupted fourth historical review remains incomplete; it is not counted as a pass or a confirmed finding.

The known inventory blind spots remain: `.git/info/exclude`, global excludes, index flags such as assume-unchanged/skip-worktree, and self-ignoring untracked control files can leave no inventory trace. Current tests reproduce self-ignoring controls, local/global excludes and assume-unchanged; skip-worktree was not separately replayed here. This review does not certify their absence or claim they are repaired. The exact descendant decision only guards a control the inventory observes. Attributes were tested as guard inputs, not represented as ignore mechanisms.

No release-blocking cross-document semantic drift was found in the reviewed candidate/design/migration surfaces. Historical acceptance records intentionally retain earlier broader-language expectations and failures; they are not the new grammar's specification.

## Reproduction and review conduct

Run from anywhere:

```sh
python3 /home/willi/Research-workspace/PROME/reports/2026-11-04_L835-acceptance/reproduce.py /home/willi/l835-phase2
```

The driver archives exact candidate inputs into disposable directories, fetches baseline objects into that disposable repository for old-reader fixtures, and runs independent scripts, the listed 259-test suite, and old-baseline historical tests. It stops on a failed invocation for inspection. Replays write `replay-*.log` here. The driver consolidates the commands used; the durable execution evidence for this review is the non-replay logs. `scratch.txt` and `historical-scratch.txt` identify retained temporary copies.

Initial harness attempts omitted archived perimeter/agent-definition/docket inputs, and one independent assertion compared Git's default quoted Unicode output to an unquoted name. These are reproducible harness errors, not candidate findings. Their logs are retained as `*-setup-error.log`, `*-quoting-error.log` and `regressions-docket-setup-error.log`; the harness copies/quoting were corrected, then complete runs passed. No candidate code was changed to obtain those passes. No confirmed blocking finding arose, so the stop-on-first-blocker instruction was not triggered.

COMPLETION: authorized acceptance evidence delivered; no installation approval; L835 OPEN. Awaiting the parent's explicit closeout ask. Notification is not recipient consumption or closeout.
