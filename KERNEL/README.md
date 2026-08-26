# KERNEL

**Mode:** FIXTURE-ONLY — NOT LIVE — NON-AUTHORITATIVE

This directory contains the approved Gate B implementation workspace for the Kernel v1 operational shadow registry.

No real native record may be imported and no shadow operation is active. The only authorized work in this stage is schema, fixture, validator, replay, renderer, and test implementation.

## Authority

- Approved contract: [`SPEC.md`](SPEC.md)
- Live implementation plan and completed work: [`IMPLEMENTATION_STATUS.md`](IMPLEMENTATION_STATUS.md)
- Design and ruling history: [`../PROME/proposals/2026-08-24_kernel-membrane-design-DRAFT.md`](../PROME/proposals/2026-08-24_kernel-membrane-design-DRAFT.md)
- Hardened Gate A specification: [`../PROME/proposals/2026-08-25_kernel-v1-spec-DRAFT.md`](../PROME/proposals/2026-08-25_kernel-v1-spec-DRAFT.md)

Native agent records remain authoritative. `KERNEL/` has no live authority.

## Current slice

The first slice is read-only and binary-only:

1. validate strict command and event envelopes;
2. validate binary Question and Forecast payloads;
3. replay accepted fixture events deterministically;
4. detect invalid chains and competing children;
5. render byte-stable empty or fixture-backed operator views;
6. verify exact synthetic native references against committed Git blobs; and
7. authorize fixture commands against injected actor and capability registries;
8. inventory explicit fixture commands/results and deterministically plan dependencies.

There is no acceptance writer, lock, SQLite projection, live submission scan, commit automation, or push automation in this slice.

Exact native-reference verification is read-only. TSV locators use the strict form
`<declared-id-column>=<record-id>`; JSON companions use RFC 6901 JSON Pointers.
The verifier reads committed Git objects through an injected repository boundary
and never treats mutable checkout contents as native authority.

Permission verification is also injected and read-only. It validates strict actor
and capability registries, half-open active windows, exact agent-owned submission
paths, payload ownership, referenced actor identity, and command capabilities. It
does not read the live roster or scan an agent submission directory.

Dependency planning accepts commands and minimal durable-result summaries supplied
directly by tests. It separates completed, ready, waiting, and dependency-rejection
classes; uses dependency order followed by `submitted_at` and `command_id`; and
writes nothing. Missing dependencies remain visible and unprocessed.

The exact next increment and remaining Gate B sequence are canonical in `IMPLEMENTATION_STATUS.md`.

## Verification

```bash
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v

fixture_out="$(mktemp -d)"
python3 KERNEL/tools/render.py \
  --events KERNEL/tests/fixtures/events/valid_binary.json \
  --output "$fixture_out" \
  --as-of 2026-08-26T00:00:00.000000Z
python3 KERNEL/tools/render.py \
  --events KERNEL/tests/fixtures/events/valid_binary.json \
  --output "$fixture_out" \
  --as-of 2026-08-26T00:00:00.000000Z \
  --check

python3 KERNEL/tools/verify_native.py \
  <synthetic-command.json> \
  --repository <temporary-synthetic-git-repository>
```
