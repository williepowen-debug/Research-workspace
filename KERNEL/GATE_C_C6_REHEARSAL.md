# Gate C C6 Disposable Rehearsal

**Date:** 2026-08-26

**State:** COMPLETE / AWAITING C7 OPERATOR RULING / NOT ACTIVE

## Boundary

Will authorized C6 only. The rehearsal used the disposable marked clone
`/tmp/kernel-c6-rehearsal.nDMc5l/mirror`, with
`/home/willi/Research-workspace` supplied explicitly as the forbidden live root.
No command, accepted event, rejected receipt, generated view, activation record,
or projection was written to the live repository. The native SAM records were
read from exact commit `1d9400425f7415083a9ffbd10964670bf255abf2`.

The rehearsal inventory contained exactly two SAM-33 commands:

- `CMD-019305f8-ec00-7000-8000-000000000033` — `RegisterQuestion`
- `CMD-019305f8-ec00-7000-8000-000000000034` — `SubmitForecast`

PROME was the writer. RED remained dormant. The run was manual, shadow-only,
binary-probability only, and did not commit or push automatically.

## Evidence

The explicit submission commit was
`3bfd93adfdcbcebd0afdf95c5f00df018cfba258`. Dry-run passed with two planned
outcomes and no durable result. Synthetic apply then produced exactly two
accepted events:

- Question event SHA-256:
  `8dd868f37ee759f2981f485cfecb60042a071595b8bf16cedbbd6217428b5790`
- Forecast event SHA-256:
  `96dc199703598753ba1aa6f0ec7242937fb4e24ba665ad0224db5de85a5658d2`

The four registered views rendered and independently checked:

- `CALIBRATION.tsv`: `f3503c52617a5e38ed0ee5b7378d789ed7be131bdf0586dfd03572bcad847b4f`
- `EXCEPTIONS.md`: `58de5d4798aded50b72250342e4c5e0ab9154ceae4ad3046c4c6fb8634bd3fa4`
- `OPEN_QUESTIONS.md`: `e802ba88072f987cff9a82ac7a3f4cb431519d7e574ff39cefc8b82c9b99191b`
- `RESOLUTION_QUEUE.md`: `cc4f17bc46192ce35037f7e69b23bc2e68b82f20aa8ef34150fb0a2cd66338cf`

Deleting and rebuilding the disposable projection reproduced file SHA-256
`edcaf86d94c37f7a6c08d85418db10a2bcf202f786ceaa7bbfcf71892cb3951a`
both times. The synthetic result/view commit is
`0f5833f2f1113f45716f4910f14c0ab0ddb54fa1`; the audit-boundary repair was
then replayed in the clone as `9c61333d3bea824e8ca8fbf26b5794d91cdb58a7`;
the exact-scope audit repair produced final rehearsal head
`49210773c53dd06e457bf5aa2b3a378a8d33d38d`.

The additions-only audit passed for
`3bfd93adfdcbcebd0afdf95c5f00df018cfba258..49210773c53dd06e457bf5aa2b3a378a8d33d38d`.
The durable-result audit passed with two explicit submissions, two explicit
results, and `pass_reported_success=true`.

## Abort and recovery

A bounded synthetic RED activation was installed only in the clone's disposable
`.rw/` state. A PROME invocation stopped before every write: both commands
reported `CUSTODY_DENIED`, the process returned nonzero, `durable_outcomes=0`,
and the existing event hashes did not change. Removing the activation and
retrying re-ran the full perimeter and returned both prior results as `EXISTING`.
View verification and projection verification remained green. This proves stop
and retry behavior for this exact rehearsal; it does not prove unattended or
multi-writer live operation.

## Defects found and remediated

C6 exposed five integration defects that component tests had not found:

1. The preparation CLI mistook its disposable clone for the live repository.
   The actual live root is now an explicit required input.
2. The lower result writer and acceptance lock repeated that mistaken inference.
   The forbidden live root now propagates through both layers.
3. The custody state machine existed but was not wired into the C3 boundary CLI.
   Optional bounded activation is now enforced before any synthetic write.
4. The additions-only and durable-result audit CLI also inferred its own checkout
   as live. Both audit modes now require the actual live repository root.
5. Independent review showed that durable reconciliation did not reject a valid
   result whose command was absent from the explicit submission inventory. It
   now reports blocking `AUDIT_UNEXPECTED_RESULT`, so additions-only history and
   durable reconciliation jointly enforce the exact packet.

The live implementation commits are `de0551587`, `04772b8a4`, `19663be05`,
`63c9b115b`, `cb66c592b`, and `d398de327`. The complete live test baseline is 191 passing
tests, with Python compilation and whitespace checks passing.

## What C6 proves and does not prove

C6 proves that the exact two-command packet can be prepared, checked, accepted,
rendered, audited, aborted on custody denial, retried idempotently, and rebuilt
inside a disposable clone while the declared live root remains forbidden. It
does not authorize or prove a live run, automated processing, more than these two
commands, a non-binary family, substitute activation, or any authority switch.

Independent adversarial review initially failed C6 on the unexpected-result
audit gap above. After `d398de327`, the review's two-submission/three-result
counterexample returns `EXCEPTION`, the exact clone inventory remains `PASS`,
and the reviewer issued an overall `PASS`. The transient console history from
the original abort/retry/rebuild sequence was not preserved as a durable log;
the reviewer could verify the activation input and resulting durable state but
not independently reconstruct the temporal sequence. This is a disclosed,
non-blocking evidence limitation, not a claim that a live drill occurred.

## C7 activation packet inputs

The proposed live-shadow packet is fixed except for an explicit operator-approved
time window:

- native source commit: `1d9400425f7415083a9ffbd10964670bf255abf2`
- native paths: `AGENTS/SAM/thesis/PREDICTIONS.tsv` and
  `AGENTS/SAM/thesis/SAM-33_KERNEL_NATIVE_COMPANION.json`
- submission paths: the two exact command IDs listed above under
  `AGENTS/SAM/outbox/kernel/submissions/`
- writer: PROME; dormant substitute: RED; no substitute activation
- command maximum: two, in Question then Forecast dependency order
- invocation: one manual, operator-attended window
- stop conditions: every condition in `GATE_C_READINESS_PLAN.md`

C7 must separately fix the start and end timestamps and explicitly authorize
this one bounded live-shadow pilot. Until that ruling, Gate C is not active.
