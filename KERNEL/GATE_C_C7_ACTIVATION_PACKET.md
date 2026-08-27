# Gate C C7 Activation Packet

**Prepared:** 2026-08-26

**State:** BLOCKED — NOT PRESENTED FOR ACTIVATION

## Preflight finding

C7 cannot safely be authorized yet. The integrated interface at
`KERNEL/tools/gate_c_boundary.py` accepts only a marked synthetic mirror,
explicitly refuses the live repository tree, exposes only `--dry-run` and
`--apply-synthetic`, and routes durable output through `FixtureResultStore` with
the live repository as its forbidden root. `KERNEL/tools/prepare_pilot.py`
likewise prepares commands only in a marked disposable clone.

This is a correct C3/C6 safety boundary, but it is not an executable live-shadow
writer. No manual copying or invocation of lower-level fixture components may be
used to bypass it. Therefore no time window is fixed and no activation ruling is
requested by this packet.

## Fixed pilot perimeter

The eventual packet remains limited to:

- source commit `1d9400425f7415083a9ffbd10964670bf255abf2`;
- `AGENTS/SAM/thesis/PREDICTIONS.tsv`, locator `Pred_ID=SAM-33`;
- `AGENTS/SAM/thesis/SAM-33_KERNEL_NATIVE_COMPANION.json`, pointers
  `/question` and `/forecast`;
- exactly `CMD-019305f8-ec00-7000-8000-000000000033` followed by
  `CMD-019305f8-ec00-7000-8000-000000000034`;
- PROME as sole active writer, RED dormant, no substitute activation;
- `kernel.schema.1`, `kernel.policy.1`, and checked-in
  `KERNEL/policies/custody-policy.json`;
- one manual operator-attended window; and
- all stop conditions in `KERNEL/GATE_C_READINESS_PLAN.md`.

## Required remediation before C7

1. Design one explicit live mode rather than weakening the synthetic boundary.
2. Require the exact approved repository, commit, two submission paths, policy
   files, event IDs, result paths, and view paths as inputs.
3. Require an activation document carrying Will's exact half-open UTC window and
   command IDs; absence, expiry, mismatch, or ambiguity must fail before a write.
4. Preserve one PROME writer, explicit staging only, no automatic commit or push,
   additions-only durable results, and disposable `.rw/` state.
5. Test live-mode refusal exhaustively in synthetic filesystem/repository
   fixtures, then repeat the complete disposable C6 rehearsal through the exact
   new interface.
6. Obtain independent adversarial review and only then prepare a fresh C7 packet
   with start and end timestamps.

## Operator ruling line

No activation ruling is available in this version. A later packet must state the
exact authorized window and cannot incorporate approval by reference to this
blocked draft.
