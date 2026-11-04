# L835 — one bounded correction, NOT ACCEPTED / NOT INSTALLED

Will, 2026-11-04, verbatim: "accept the four completed repairs, leave L835 explicitly open, and authorize one carefully bounded correction—not another general maintenance sweep."

WQ-594–596 and L910 are accepted by Will. L835 stays OPEN. One correction was prepared in a disposable overlay; live dirty code/tests/contract were preserved untouched. No further review, owner launch or general maintenance performed. Approval does not erase the previous NOT ACCEPTED verdict or review history.

## Correction

The witness walker does not implement embedded `**` crossing a directory separator. In `_wholly_excluded`, any earlier non-EXCLUDED rule with embedded `**` now prevents a proof that the whole subtree is excluded. An earlier whole-subtree EXCLUDED rule still wins. No API, matcher, perimeter or live-fleet policy changes.

This is deliberately conservative: even an unrelated earlier embedded-double-star rule can cause a guard rather than an advisory result. It does not claim exact overlap analysis. That false-positive cost is declared for any future acceptance review, not silently hidden or corrected by a broader rewrite.

Tests add the original prefix case and suffix/infix variants, each with OWNED and SHARED classification, both ignore and attributes controls, and an earlier-whole-exclusion precedence case. Before correction, 71 contract tests ran with 6 failing subtests reproducing the defect. Existing fixtures cover working-tree, committed/ref, missing rules and ordinary exclusions in isolated Git repositories.

## Durable candidate

Adjacent `2026-11-04_L835-bounded-correction.patch` is a cumulative, NON-OPERATIONAL candidate against commit `b24422282`, containing the previously uncommitted L835 code/tests/contract plus this one correction and regression tests. It is stored for review, not applied to the shared runtime. The bounded new code is only the conservative embedded-double-star overlap predicate; prior source changes remain attributable to the interrupted repair. No live manual re-edit. Candidate SHA-256 by path:

```json
{
  "PROME/tools/argus_contract.py": "dfdbc099cde2e433806d835e331d9d49890ea5af7a3bfe7aedb4b2c746051299",
  "PROME/tools/tests/test_argus_contract.py": "09199e67d551d7616edc6bbd4c438f334216dc712300dbefade318b088ae4026",
  "PROME/tools/ARGUS_CONTRACT.md": "8c17013617076a133e3409a8e8536aac66c4a027da2daefb71a511704af1dd48"
}
```

Acceptance and exact scope were recorded before edits in `PROME/tools/tests/ACCEPTANCE_L835_nested_ignore_scope_2026-11-04.md`. Further independent acceptance remains required before operational installation; this instruction did not name another review exception.

Verification result: 71 contract + 34 scope + 37 consumed-move tests = 142 PASS in disposable overlay. Original failure reproduced before correction (6 failing subtests). IMPLEMENTED IN CANDIDATE / TESTED; NOT INDEPENDENTLY VERIFIED; L835 OPEN and operational patch WITHHELD. Live dirty implementation/tests/contract left unchanged. No further review round.

Durability verification: applying the cumulative patch to the three files from b24422282 reconstructs the tested overlay byte-for-byte. Live files do not contain this bounded correction or its new tests. Table, decision-ledger, done-row and weekday checks pass. No broad boot, inbox sweep or Standard ARGUS closeout was run for this bounded correction; the earlier PARTIAL closeout status remains. No scope expansion, extra review or claim of operational repair.
