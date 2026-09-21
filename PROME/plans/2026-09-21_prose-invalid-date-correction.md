# Recognized invalid handwritten dates — bounded correction

Will relayed CATO's `86f809f8a` follow-up after authorizing Phase 1 implementation. This correction addresses its surviving coverage defect only; no Phase 2 work.

## Acceptance written before code edits

- Recognized impossible handwritten M/D dates remain visible as unassessed, including invalid-only input, mixed valid/invalid segments, and a valid and invalid date within one segment. No such scope is labeled EMPTY or accepted by the gate summary.
- Truly empty handwritten scope remains EMPTY. Valid dated claims retain their existing assessment. Generated content remains excluded and its freshness verdict independent.
- Preserve the shared prose rc contract: malformed M/D coverage is explicitly unassessed with rc=0 unless another existing divergence makes rc=1; the gate's advisory fails on unassessed coverage. Invalid ISO dates retain their existing detectable rc=2 behavior. No expanded date vocabulary.
- Carry malformed recognition through bold date headers and inherited context; a malformed date after a bold header also remains visible. Existing section and explicit ignore exclusions remain in effect; ignored is reported, never assessed.
- Only fixture state may be mutated in tests. Preserve foreign ARGUS baseline; no production boot rerun.

Neighbour cases: ordinary valid/empty; overlap valid+invalid in separate/same segments and generated+prose; wrong scope generated blocks/other sections; missing knowledge invalid dates without a usable date value; concurrency N/A for this in-memory parsing correction (existing generated snapshot checks unchanged).

Implementation: retain invalid M/D parser sentinels through segmentation; avoid weekday operations on invalid dates; count and identify malformed segments as unassessed before matching. Reuse existing structured fields and gate summary. Consequential-tool result review must invent an independent counterexample before completion is claimed. No canon amendment or broad transformation, so no additional plan cold read is needed for this narrow follow-up to CATO's reviewed correction.

## Completion

- IMPLEMENTED: invalid M/D recognition survives both inline and bold-header segmentation, including inherited context and header remainders. Malformed segments print their file/line and remain unassessed; the existing gate summary flags them. ISO validation also covers header remainders. Generated freshness and gate code are unchanged.
- TESTED: `python3 -B -W error::ResourceWarning -m unittest PROME/tools/tests/test_boot_coverage.py PROME/tools/tests/test_prome_gate_gates.py PROME/tools/tests/test_capability_class_WQ239.py` passed 63 tests. Public-CLI cases cover invalid-only, separate and same-segment mixtures, bold headers, inherited context, genuinely empty and valid controls, explicit ignore/section/generated exclusions, independent generated freshness, and invalid ISO dates inline/after headers. Calendar selftest passed 24/24; `git diff --check` passed. All changed state was confined to temporary fixtures.
- INDEPENDENTLY VERIFIED: read-only `prose_date_review` found no blocking findings or new advisories. Its independently designed fixtures covered leap-day/month/day-zero failures, table and header contexts, a malformed claim beside a real date divergence (rc=1 retained), empty/valid controls, and generated independence. Additional ISO fixtures verified the latest header-remainder correction. All passed at the producer and gate-summary boundary. Reviewer explicitly closed out with no repository edits, commits or live stateful checks; receipt in ORCH_LOG.
- STILL UNRESOLVED: existing HANDOFF budget breach and older manifest attestation; Phase 2 remains deferred.
