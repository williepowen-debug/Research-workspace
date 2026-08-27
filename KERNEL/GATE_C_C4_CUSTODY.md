# Gate C Checkpoint C4 — Custody Mechanism and Synthetic Test

**Date:** 2026-08-26

**Authorization:** Will approved C4 after C3 completion.

**Status:** COMPLETE — RED REGISTERED DORMANT — NOT LIVE

## Implemented contract

`KERNEL/tools/custody.py` provides a deterministic custody state machine:

- one primary writer (`PROME`);
- at least one pre-registered substitute, disabled by default;
- only `WILL` may register or activate a substitute;
- activation fixes one substitute, an exact half-open UTC time window, and one to
  three command IDs;
- the primary is suspended throughout an active substitute window, preserving
  one writer rather than creating concurrent custody;
- expiry or explicit in-window revocation automatically restores primary custody;
- unknown writers, clocks, policies, activation fields, or versions fail closed;
- custody preflight occurs before the integrated acceptance lock or writer, so a
  denied custodian cannot write even a rejection receipt; and
- the first PROME return audit must occur after window closure and reconcile the
  exact command set, substitute `writer_id`, recorded times, and canonical result
  hashes.

No timeout transfers custody. CI is never registered as a writer.

## Synthetic evidence

Fourteen new tests prove:

1. PROME is primary without activation;
2. a substitute is dormant by default;
3. a default-enabled substitute policy fails closed;
4. only Will may register and activate a substitute;
5. substitute custody is bounded by exact command and half-open time window;
6. PROME is suspended during that window and restored afterward;
7. revocation ends substitute custody and restores PROME;
8. unknown writers and invalid clocks fail closed;
9. a complete post-window PROME audit passes;
10. a substitute/self or premature return audit fails;
11. missing, extra, or changed results fail the audit;
12. invalid windows and revocations fail closed;
13. a suspended PROME is blocked before any durable write; and
14. an activated synthetic substitute runs the identical acceptance binary and
    records its own `writer_id`.

The full discoverable baseline is **186 tests passing**.

## Proof limits

This pass proves the custody mechanism and identical-binary path against synthetic
records. It does not name, activate, train, or test a real substitute session. It
does not inspect a real record, activate the C2 carve-out, or authorize C5–C7.

## Operator naming decision

Will approved **RED** as the dormant substitute on 2026-08-26. The inactive policy
is registered at `KERNEL/policies/custody-policy.json`. RED is the active fleet
review/QC agent, has no native research authority through this role, and the
custody binary permits no additional discretion. Registration grants no standing
`command.accept`; activation still requires a separate Will-authored command/time
window.

Alternatives are possible, but the substitute must be a named registered actor
and cannot be PROME, CI, or an automatic timeout recipient.

## Disposition

- C4 technical implementation: **PASS**.
- Dormant substitute identity: **RED — REGISTERED / DISABLED BY DEFAULT**.
- C4: **COMPLETE**.
- Live custody activation: **NOT AUTHORIZED**.
- C5 record selection, C6 rehearsal, and C7 pilot: **NOT AUTHORIZED**.
