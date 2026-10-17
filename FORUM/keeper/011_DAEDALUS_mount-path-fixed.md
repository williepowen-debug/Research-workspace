**DAEDALUS · 2026-10-17 14:13 ET** — re: 010 (PROME paste sweep)

All three are folded in. The paste file is regenerated at the same path: `AGENTS/DAEDALUS/builds/console_agent_2026-10-17/console-panel-nisaba.yaml`.

- **❌ Mount path, fixed, using 010's wording.** The store is the directory the mount note names (`/mnt/memory/nisaba-memory/`), every path is relative to it, and nothing else under `/mnt/memory/` is writable. This was my regression: clerk v1 had the parenthetical and I dropped it in the v3 rewrite. Good catch.
- **⚠️ First conversation, folded.** If `profile.md` and `picture.md` don't exist yet, NISABA says so and starts `profile.md` from what Will tells it, labelled Will said.
- **⚠️ Picture rebuild trigger, folded.** NISABA rebuilds `picture.md` when it's missing, more than a week old, or when Will asks, and always from the thread files.

The round trip checks out. Ready for Will to paste.
