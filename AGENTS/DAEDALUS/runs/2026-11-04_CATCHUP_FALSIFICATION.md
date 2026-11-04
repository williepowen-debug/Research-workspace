# Falsification scanner rc/help repair — 2026-11-04

Authority: Will’s owed-task catch-up; PR9 priority 3, existing owned tool repair. Acceptance written before implementation. No rail discovery, freshness policy, class assignment, label expansion or market judgment changes.

Acceptance:
1. Existing real BROCK no-thesis/no-visible-rail finding returns 1, in prose and TSV. Both outputs name the candidate; this is not proof the owner lacks a rail.
2. Existing clean utility/meta and current surface fixtures still return 0; stale/unstamped/no-rail findings still return 1.
3. --help/-h prints usage and returns 0 without loading directory/map or scanning; unknown options, missing --agent argument and unknown agent return 2.
4. Existing surface rows are byte-identical for pinned inputs; TSV adds only the missing market candidate comment. No consumer receives an rc contract change: existing 0 clean / 1 findings / 2 invocation contract is restored for the omitted bucket.
5. Original source must fail the regression suite; independent review of exact source/test hashes required before publication.

Consumer survey: executable references in repo-root scripts, PROME/tools and AGENTS/*/scripts found only scanner/test module and pipeline_rc_guard name recognition. Invocation remains DAEDALUS sweeps/FALSIFICATION_SWEEP.md; no rc-keyed caller needing a behavior migration found within those paths. Full repository search follows before ship. CHECKS row is the current contract source; its stale perimeter prose will be narrowed to actual guarantees.

## Execution evidence

Before/after (November 4 actual population): BROCK prose 0→1; BROCK TSV 0→1; help 1→0; fleet TSV 1→1; DAEDALUS clean 0→0. All non-comment fleet TSV surface rows byte-identical. Eleven regression tests pass (five CLI methods plus six pre-existing STATUS-rail tests); original source fails six subcases in the five CLI methods. The help test forbids directory loading, not merely scan output. Full tracked executable-reference search found only pipeline_rc_guard regex name recognition in addition to the producer/tests. No rc-based consumer edit required.

Unchanged debt: missing/unreadable class map can still erase classification; group loading error semantics, rail-discovery/label limitations and existing missing-clock behavior remain outside this bounded fix. rc0 is no detected finding in the existing parsed perimeter, not complete rail coverage.

REVIEW: required — rc-based finding behavior and output candidate boundary; independent reader /root/owner_followthrough ACCEPT after HOLD on empty --agent; repaired and re-reviewed at exact hashes in runs/2026-11-04_CATCHUP_FALSIFICATION_REVIEW.md. Scope source CLI/main and CLI regression tests.
