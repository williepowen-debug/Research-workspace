# Kernel v1 Implemented Contract

**Status:** GATE B CLOSED; GATE C PLANNING ONLY — live shadow activation unauthorized

The complete approved contract is maintained with its ruling context at:

`PROME/proposals/2026-08-25_kernel-v1-spec-DRAFT.md`

Gate A was approved by Will on 2026-08-25 and recorded at commit `9bbf9c041b1b0fae68084ca7f8ec408b9f7a426d`.

This file is the implementation boundary notice, not a competing restatement. If implementation and the approved proposal disagree, the approved proposal wins and implementation fails closed until reconciled.

Gate state and the open legs are canonical in `KERNEL/IMPLEMENTATION_STATUS.md`; the build chronology and its increment sequence are frozen at `PROME/archive/KERNEL_IMPLEMENTATION_CHRONOLOGY_FROZEN_2026-09-09.md`.

Authorized now:

- fixture-only schemas, validation, replay, rendering, and tests;
- binary-probability Question, Forecast, and Resolution lifecycle fixtures;
- adversarial invalid fixtures;
- generated views containing fixture data only.

Unauthorized now:

- real agent submissions or native-record imports;
- live shadow events or receipts;
- a live-operation Git carve-out;
- canonical authority or an authority switch.
