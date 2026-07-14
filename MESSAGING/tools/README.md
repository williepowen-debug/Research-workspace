# Direct Messaging v1 Validator

The validator is read-only. It does not deliver, edit, commit, push, escalate, or reassign messages.

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

