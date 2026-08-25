# Kernel fixture boundary

These records are synthetic and non-authoritative. UUIDs, Git commits, paths, locators, and hashes exist only to exercise schema, replay, conflict, and rendering behavior.

They are not validated native imports and must never be copied into `KERNEL/shadow/events/`.

`events/valid_binary.json` is the file-backed happy-path Question plus Forecast event set used by renderer and CLI tests.

`events/orphan_forecast.json` is an adversarial set whose Forecast references a missing Question. Replay must omit it from current state and render `ORPHAN_FORECAST` in exceptions.
