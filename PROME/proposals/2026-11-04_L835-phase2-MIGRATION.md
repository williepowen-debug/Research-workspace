# L835 schema-3 migration and rollback — NOT EXECUTED

Phase 2 authority permits isolated implementation/internal tests only. L835 stays OPEN. This procedure is reviewable preparation, not permission to install, mark a production candidate REVIEWED, advance the baseline, or engage another reviewer.

Baseline implementation: `cf20665b2ecf9c19980e5030bc9e38293b44f25b`. Candidate branch: `prome/l835-phase2-20261104`; candidate commit is identified in the Phase 2 delivery. Shared desktop checkout and rejected candidates remain untouched.

## Cutover, only after subsequent authorization

1. Quiesce only the authorized PROME closeout transition. Record current code commit, exact candidate commit, baseline JSON, schema-2 review JSON, perimeter bytes and SHA256 for each. Preserve the original receipts as immutable historical evidence outside the live receipt path. Preserve any uncommitted work separately; stop on conflicting target edits rather than overwriting them. Do not use a branch-wide reset, stash or merge that sweeps foreign work.
2. Reconfirm accepted candidate tests and the actual Standard consumer against the intended deployment inputs. Inventory policy syntax first; unsupported syntax requires a separately approved rewrite, never translation or fallback. Resolve baseline drift explicitly; never advance it to conceal failed comparison.
3. Install only the authorized candidate source/document paths in one exact-path change. Keep the archived schema-2 receipt unmodified. New tools deliberately return CANNOT-EVALUATE / rc 2 for it. That stop is the safe transitional state, not a failed migration to bypass.
4. Use an explicit delivery/evidence/observation plan and run `argus_scope.py --record-review --contract PLAN`. Parse/hash the same perimeter read. The new schema-3 receipt must bind `argus-path-v1`, exact ordered rules and source digest inside `contract_sha256`; the perimeter mirror must agree. Confirm FROZEN and zero review reuse from schema 2 even for identical content. This is an actual new freeze, not relabeling a receipt.
5. Only an authorized actual review can promote that FROZEN receipt. Record its real receipt, run mark-reviewed, Standard's actual ARGUS check, and the existing delivery/ref/snapshot/push protocol. Never treat these Phase 2 synthetic test promotions as real audits or permission to reuse review. L835 closure remains a separate user decision.

## Rollback

Before delivery, stop on failed controls and retain all diagnostics. Restore exact pre-cutover source bytes through a separately authorized exact-path reversal; preserve candidate and old receipts with their hashes. Never hand-edit schema/version/digest/verdict fields to make tools accept a receipt. Restoring a schema-2 receipt restores historical evidence only, not approval of post-cutover changes. If content, policy, baseline or inventory has moved, fresh authorized verification is required. A rollback to known L835-vulnerable code is not a security repair and must not be advertised as a passing new closeout. Prefer leaving Standard withheld over resuming certification under an incompatible approval.

If candidate delivery has occurred, retain its immutable delivery SHA and all receipts; do not rewrite shared history. Reversing installed code does not reverse delivered work or make an old approval cover it. Reconcile exact changes and review requirements before any new delivery.

## Internal procedure tests

Disposable repositories exercise historical version refusal at verification, observation, promotion, candidate selection/delivery and Standard; archive/restore receipt bytes unchanged; explicit re-freeze gives schema 3 FROZEN with no old review reuse; policy changes also disable reuse; exact old baseline reader rejects schema 3. Tests also check working-tree, commit and snapshot verification. These establish migration wiring and fail-closed behavior, not authorization or universal historical semantic equivalence.
