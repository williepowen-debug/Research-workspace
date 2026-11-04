# Historical schema-1/2 workflow tests

The consumed-move test file is preserved byte-for-byte from baseline
`cf20665b2ecf9c19980e5030bc9e38293b44f25b`. Its 37 tests exercise the retired
no-contract freeze and origin-fetch exemption. It is historical evidence, not
an active second interpreter or a schema-3 acceptance test.

Run it against the exact baseline source using `git archive <baseline>
PROME/tools PROME/state/AUDIT_PERIMETER.tsv` extracted into a disposable directory,
then set PYTHONPATH to that directory's PROME/tools and run unittest discovery
on that directory's original test file. Phase 2 did this: 37 passed.

Schema 3 explicitly refuses the old freeze/receipt route. Current byte-identical
move, ownership, candidate, history and delivery protections are exercised by
`test_argus_wq583.py` (39 tests), `test_argus_contract.py`, and the migration/refusal
cases in `test_l835_phase2.py`. No old approval is upgraded by passing these tests.
