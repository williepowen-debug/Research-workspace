# Kernel fixture boundary

These records are synthetic and non-authoritative. UUIDs, Git commits, paths, locators, and hashes exist only to exercise schema, replay, conflict, and rendering behavior.

They are not validated native imports and must never be copied into `KERNEL/shadow/events/`.

`events/valid_binary.json` is the file-backed happy-path Question plus Forecast event set used by renderer and CLI tests.

`events/orphan_forecast.json` is an adversarial set whose Forecast references a missing Question. Replay must omit it from current state and render `ORPHAN_FORECAST` in exceptions.

`native/` contains synthetic Git-committed source files for exact-reference tests. The
tests copy these files into temporary repositories and never inspect a real agent
ledger. `predictions.tsv` and `companion.json` are happy paths; the other files
exercise duplicate records, repeated headers, shifted rows, and ambiguous JSON.

`permissions/` contains a synthetic actor registry and policy-versioned capability
grants. They exercise identity, owned submission paths, half-open active windows,
payload ownership, and custody separation without reading the live roster or any
agent submission directory.
