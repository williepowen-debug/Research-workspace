# Checkpoint 12 Integrated Acceptance Remediation

**Date:** 2026-08-26

**Starting baseline:** `e212bd26b`

**Scope:** Fixture-only. No live records, live submission scans, Git carve-out,
Gate C activation, or authority switch were inspected or exercised.

**Result:** COMPLETE — INDEPENDENT RED-TEAM PASS

## What changed

`KERNEL/tools/acceptance.py` is now the complete fixture acceptance interface. One
locked pass:

1. inventories explicit path-and-command submissions and durable results;
2. plans dependencies deterministically;
3. enforces the next ready command rather than caller-selected order;
4. leaves missing dependencies visible and unprocessed;
5. durably writes planned cycle and dependency rejections;
6. runs schema, permission, exact native-reference, required-hook, and lifecycle
   checks before accepting a ready command;
7. publishes exactly one accepted event or rejected receipt;
8. re-inventories and re-plans after each result;
9. re-checks the printed permission, native, hook, and replay perimeter for an
   accepted same-byte retry;
10. blocks aggregate green on any `EXCEPTION`, `UNKNOWN`, prior rejection, writer
    collision, or selected command left unprocessed; and
11. prints every check's perimeter, status, pass claim, and claim limit.

`FixtureAcceptancePass.accept()` also refuses a command that is not next in the
current dependency plan. The lower-level writer remains a fixture component for
unit tests; it is not the advertised complete acceptance interface.

Successful `render.py --check` now prints the view-reproduction perimeter,
`PASS`, what the pass proves, and what it does not prove. Failures print the same
claim boundary with `EXCEPTION`.

## Adversarial proof

The integrated tests prove:

- a reverse-ordered valid Question/Forecast batch accepts in dependency order;
- an invalid native commit produces one durable `NATIVE_RECORD_MISSING` receipt;
- an unauthorized actor cannot reach an accepted event;
- a failed dependency durably rejects its dependent;
- a missing dependency remains visible and unprocessed;
- cycle members receive durable `DEPENDENCY_CYCLE` receipts without manual caller
  disposition;
- a fresh Forecast against a closed Question receives `QUESTION_NOT_OPEN`;
- same-ID/different-byte retry returns `IDEMPOTENCY_KEY_REUSED` without overwrite;
- an accepted retry re-runs the required printed perimeter and blocks green when
  the supplied path no longer authorizes;
- a prior rejected result cannot return aggregate green;
- an event-ID collision produces a durable `IDENTIFIER_COLLISION` rejection and
  blocks green;
- an injected required-check `UNKNOWN` prevents all acceptance and explicitly
  accounts for every selected command left unprocessed;
- the CLI refuses the live repository as its native Git boundary; and
- the CLI prints aggregate perimeter and claim limits on a complete valid batch.

## Verification

Primary verification and an independent read-only red-team both ran:

```text
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v
Ran 155 tests — OK

python3 -m compileall -q KERNEL/tools KERNEL/tests
PASS

git diff --check
PASS
```

The independent reviewer initially found two defects: accepted retries skipped the
advertised verification perimeter, and a required-hook `UNKNOWN` did not account
for later selected ready commands. Both were corrected, regression-tested, and
cleared in a second review. The final recommendation was **PASS**, with no remaining
checkpoint 12 blocker.

## Remaining declared limitations

- Trusted-history reachability is not enforced beyond resolving the supplied full
  commit in the injected repository.
- `TEXT_ANCHOR` remains deliberately excluded.
- Inputs without minimum receipt transport identity cannot receive an approved
  durable receipt.
- No live submission scan, live view generation, Git carve-out, substitute-custody
  activation, or live shadow operation exists.

These limitations remain visible and do not block the approved binary fixture
slice. They do matter to a later, separately authorized Gate C plan.

## Gate disposition

- Checkpoint 11 integration blocker: **REMEDIATED**.
- Uniform executable check disclosure blocker: **REMEDIATED**.
- Checkpoint 12: **COMPLETE**.
- Gate B technical exit evidence: **SATISFIED**.
- Gate B state: **PASSED / CLOSED BY WILL ON 2026-08-26**.
- Gate C: **NOT AUTHORIZED**.
