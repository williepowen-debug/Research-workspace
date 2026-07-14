# Direct Messaging v1 Tools

The validator is read-only. The authoring CLI is feature-gated by `MESSAGING/config.yaml`. The first activation uses `write_mode: cohort`: only `PROME -> BRENT` and `PROME -> SAM` are allowed. Temporary repositories may use `write_mode: test`. All other live routes fail closed.

## Dependency

```bash
python3 -m pip install -r MESSAGING/requirements.txt
```

## Validate records

From the repository root:

```bash
python3 MESSAGING/tools/validate.py --repo-root . path/to/message.md path/to/receipt.md
```

For machine-readable output:

```bash
python3 MESSAGING/tools/validate.py --repo-root . --json path/to/records/
```

The command exits nonzero when any ERROR is present. Warnings do not change the exit code.

## Preview a message

Previewing has no filesystem side effects:

```bash
python3 MESSAGING/tools/msg.py compose \
  --repo-root . \
  --sender PROME \
  --recipient BRENT \
  --role ACTION \
  --urgency NEXT_BOOT \
  --subject "Grade the KOC platform hit" \
  --requested-action "Grade the hit against the current production-infrastructure ladder." \
  --definition-of-done "Record the grade or a sourced NO_CHANGE decision." \
  --expected-target AGENTS/BRENT/STATUS.md
```

`--write` succeeds only for routes explicitly named in the cohort allowlist. WALTER and all other agents remain outside the live scope.

## Receipt engine

The receipt command initializes the recipient-owned receipt if needed, appends one lifecycle event, validates the complete candidate, and atomically replaces the receipt only when valid. In cohort mode, it accepts receipts only for messages whose sender and recipient match the allowlist.

## Multi-obligation composition

`compose-file --spec draft.yaml` accepts a human-readable YAML draft containing multiple obligations. It allocates one message ID, generates recipient-specific obligation IDs, and delivers an identical copy to each addressed inbox. Every route must pass the cohort allowlist. A partial batch write is rolled back.

## Run tests

```bash
python3 -m unittest discover -s MESSAGING/tests -v
```

Current fixtures cover:

- Valid ACTION plus recipient receipt.
- Invalid timestamp rejection.
- INFO hiding an action.
- Integration claims missing evidence.
- Wrong receipt ownership.
- Idempotent duplicate delivery.
- Conflicting duplicate payloads.
- Preservation of all five source items in the historical BRENT compatibility example.
- Preview with zero side effects.
- Locked real-repository writes.
- Monotonic sender/date ID allocation.
- Allocator contention.
- End-to-end accepted → no-change receipt flow.
- Idempotent duplicate receipt events.
- Receipt ownership and repository-provenance enforcement.
- Invalid post-terminal transitions.
