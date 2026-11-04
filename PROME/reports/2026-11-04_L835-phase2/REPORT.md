# L835 Phase 2 — bounded candidate delivered, NOT INSTALLED

**Internal verification passed; L835 OPEN.** Ready for Sloane's implementation/evidence read. I recommend proceeding to a separately authorized independent acceptance review if that read agrees. No independent reviewer was commissioned, no review approval was converted, and no production cutover or baseline advance occurred.

## Identity and scope

- Baseline: `cf20665b2ecf9c19980e5030bc9e38293b44f25b`.
- Implementation/test candidate: `0fd45aa1b89a8d50ac4b3e44a2b35ca588e0fbc0`.
- Non-operational local branch: `prome/l835-phase2-20261104`.
- Isolated checkout: `/home/willi/l835-phase2`. The subsequent report-only commit does not alter tested source.
- Actual runtime: Codex with native shell/exec; root and PROME instruction files explicitly accessed in the isolated checkout. No helper/reviewer/desk launch or new monitoring obligation.

Phase 2 implements the November 4 design plus the user's explicit uncertainty, migration and visibility requirements. Source/document paths are on this branch only. The shared checkout's three rejected-candidate files were hashed before work and rechecked afterward, unchanged (hashes in `evidence.json`). The existing schema-2 REVIEWED receipt is unchanged: SHA256 `fc2ca6087fe49cc3e8d4a412f30cdef44fda855a5ff5c173a7b532653b779e65`. The original rejected patches/reports and design remain intact.

## Correctness argument

`argus_policy.py` compiles validated, ordered rows into segment-predicate transitions. Concrete classification and descendant queries use those same transitions and first-accepting-rule selection. UNATTRIBUTED is protected. Literal paths, terminal recursive subtrees and finite-depth wildcard paths are the entire language; unsupported syntax rejects the policy before a classification/approval can be issued.

The reversed trie partitions all valid segments by predicate truth. Every segment either ends at a trie node or first exits it. Exact ends carry the matching literals/suffixes; after first exit no new literal or suffix terminal can be reached. Reserved endpoints are excluded, and a valid non-ASCII exit character always exists because trie edges are ASCII. Thus each transition over an atom represents every string in that atom, not a guessed filename. After maximum fixed depth + 1, only dead rules and recursive loops survive, so further extension cannot change classification. Exhausting that finite search proves exclusion; an earlier protected state proves existence. A 100,000-state limit or evaluation error raises uncertainty instead of returning either boolean.

Internal tests support this argument; they are not an independent proof. The partition/depth proof, migration boundaries and consumer propagation are the highest-value targets for the next authorized reader.

## Internal results

**259 current tests PASS**, 26.811 seconds; warnings promoted to errors. **37 historical consumed-move tests PASS against the exact old baseline only**, not the replacement. Final diagnostic-only wording change: eight tier-consumer tests PASS afterward. Python compilation and scoped whitespace checks pass. Durable transcripts: `current-tests.txt`, `historical-moves-tests.txt`, `final-gate-tests.txt`; source hashes and run metadata: `evidence.json`.

Reproduce current tests from this checkout:

```sh
PYTHONPATH=PROME/tools:PROME/tools/tests python3 -W error::ResourceWarning -m unittest \
  test_argus_policy test_argus_contract test_argus_scope test_argus_scope_evidence \
  test_argus_wq583 test_l835_phase2 test_review_mechanism_WQ240b \
  test_closeout_simplification_WQ240 test_external_findings_2026_09_13 \
  test_boot_charter_coverage test_parity_gate_L294_F3
```

| Requirement | Evidence |
|---|---|
| Previously missed `.claude`, desk inboxes and registered scripts | Real nested ignore controls hide protected files (`check-ignore` + NUL inventory); visible controls block freeze/verify/observation; attributes separately guarded. |
| One excluded witness, seven excluded salts, unmatched deeper descendants | Literal/complement and deeper UNATTRIBUTED regressions in `test_argus_policy.py`; no witness machinery exists. |
| Embedded-double-star originals and unrelated false blocking | Original unsupported pattern strings retained as refusal cases; supported `root/*/target` guards, `other/*/target` permits genuinely excluded `root/**`. Actual Standard consumer passes the excluded-directory arrival only with a valid REVIEWED fixture. |
| Overlap/shadowing/suffixes | Exhaustive rule orderings (including duplicate/fully shadowed rules), suffix nesting, current shadowed CLAUDE row. 308 policy lists: 258 exhaustive small cases plus 50 seed-835 larger lists; separate direct reference matcher imports no production parser/partition/transition helper. |
| Compatibility | Differential old matcher comparisons on supported ordinary paths; newline differences explicitly tested. Old patterns are never rewritten to make historical failures appear to pass. |
| Errors/limits | Actual lowered state-limit refusal and injected evaluation errors through working-tree/ref/snapshot verify, freeze, observe, mark-reviewed, deliver, and Standard. Unsupported/missing/malformed policies and pins refuse explicitly. |
| Historical review | The actual baseline schema-2 REVIEWED receipt is byte-preserved and refused by new operational consumers; synthetic migration produces schema 3 FROZEN with no inherited reuse. Both old-reader/new-receipt and new-reader/old-receipt incompatibility tested. |
| Migration/rollback | Disposable end-to-end schema-2 freeze/review, code replacement, schema-3 re-freeze, exact old code/receipt restoration, and renewed new-code refusal. Historical verification in this synthetic drill is not authority for production rollback. |
| Git/delivery protections | Pending, staged, desk-committed, committed-plus-pending controls; force-added hidden paths, tracked/deleted controls, foreign arrivals, immutable candidate edits, actual commit paths and snapshots. Existing 63 contract and 39 WQ-583 tests retained/migrated. |
| Paths | Unicode, dotfiles, newline/CRLF/tab/whitespace/backslash filenames round-trip in inventory/classification; undecodable filenames fail evaluation. Delivery's line-based index format explicitly refuses newline/CR/tab paths. |
| Consumers | Real subprocess ARGUS CLI freeze/verify/mark/ref/snapshot paths, actual `prome_gate.check_review_manifest('standard')` plus its real aggregate, and tier regression tests. This is the actual ARGUS Standard consumer, not a claim that all unrelated Standard closeout checks or a real audit ran. |
| Known concealment limits | Disposable self-ignoring untracked control, `.git/info/exclude`, global excludes and assume-unchanged examples remain invisible and can produce unchanged verification. Tests expose this boundary; none is claimed repaired. |

Failures encountered and disposition: the first contract run had 5 failures/15 errors because old fixtures omitted policies or expected legacy strict fallback. Those fixtures now pin explicit policies or assert rc 2, without relaxing production validation. Initial integration tests had two expectation errors: post-freeze working edits do not move the immutable WQ-583 candidate, and an empty observation has no descendant decision to exercise; the tests now check actual delivery and an observed control whose analysis is required. A global-exclude test initially removed its temporary exclude file too early; retaining that control for the asserted observation fixed the fixture. CLI migrations exposed old UNATTRIBUTED/working-copy/baseline-message expectations; they now test OWNED arrivals, immutable candidate bytes and explicit schema-3 refusal. These were normal bounded implementation/test migrations. No unresolved test failure or algorithm counterexample remains in the listed suite. No repository-wide test-pass claim is made.

## Complexity and affected files

Production source totals across scope, contract, policy and gate: **3,570 → 3,379 lines, net −191**. The new pure policy module is 197 lines, dependency-free. Scope shrinks 886 → 513; contract 847 → 829; gate 1,837 → 1,840. Test/evidence volume is larger than the implementation.

Removed: regex glob translation, direct-child ignore probe, legacy operational review verification and origin-fetch consumed-move exemption, legacy freeze emission and dead baseline helper. Rejected witness/salt/whole-exclusion candidate logic was never copied from the shared dirty files. `_match` is only a thin adapter to the same compiler, not a parallel interpretation. The retired 37-test no-contract move suite is preserved byte-for-byte under `tests/fixtures/schema12_history/`; current contract move/delivery tests remain active. Existing external-finding tests are migrated to real schema-3 fixtures; the explicit-path escape around broken inventory/baseline is refused.

Changed implementation: `PROME/tools/{argus_policy.py,argus_scope.py,argus_contract.py,prome_gate.py}`. Contract/consumer documentation: `PROME/tools/ARGUS_CONTRACT.md`, `PROME/CLOSEOUT_PROCEDURES.md`. Tests: policy, Phase 2 integration, contract, scope, review CLI, external findings, closeout simplification and historical-fixture disposition. New migration document and this evidence directory complete the deliverable. No live perimeter rows, review receipt, baseline, owner attribution rules or Git inventory sources changed.

One narrowly necessary consumer change: Standard/Heavy preserve rc 2 instead of collapsing uncertainty to rc 1. Light may omit review if no receipt exists; an existing incompatible/invalid receipt or verifier error now returns rc 2, preventing uncertainty from becoming permission. Ownership, commit attribution, evidence and immutable delivery controls otherwise remain.

The symbolic implementation stayed within the approved architecture; no general glob engine, new inventory system or persistent monitor was required. The original 2–3 engineer-day estimate was provisional. Actual complexity is a small policy module plus compatibility/consumer wiring and substantial fixture migration; completion is established by the recorded checks, not elapsed assistant time.

## Decision boundary and remaining uncertainty

Migration/cutover and rollback procedure: `PROME/proposals/2026-11-04_L835-phase2-MIGRATION.md`. It has been exercised only in disposable repositories. A real cutover still requires explicit authorization, preserved historical receipts, an actual schema-3 re-freeze, and an authorized review. Reuse is limited to equal schema-3 policy bindings on the same baseline; historical approvals cannot migrate automatically.

Git visibility remains bounded by the existing inventory. Policy predicates do not solve hidden control files, global/local excludes or index concealment. Large policy searches may return CANNOT-EVALUATE; no fallback is offered. The finite tests and internal correctness argument need independent challenge before release. **Recommendation: candidate ready for Sloane's read and consideration of authorized independent acceptance; not ready for installation by this Phase 2 authority. L835 remains OPEN.**
