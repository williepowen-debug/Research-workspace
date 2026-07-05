# TASK → BROCK · from DAEDALUS · 2026-06-28 · BANK_BDC_MATRIX staleness (BATCH_01 item 5)

**Context:** Will + PROME approved DAEDALUS BATCH_01 (structural handles for BROCK/SHADE/CREED). Items 3 (matrix Independence map) + 4 (PREDICTIONS if-falsified ACTION column) were applied directly to your idle files this session. **Item 5 is yours to action** — it's a data-liveness call only you can make.

**The gap (root data-hygiene + PAT-023):** `workbook/BANK_BDC_MATRIX.tsv` is flagged-stale in your CLAUDE.md ("owner to confirm freeze-vs-refresh") but carries **no banner** — the silent-rot middle. Root `CLAUDE.md` Data Hygiene (now naming position/ledger surfaces, per PROME 6/28) requires every ledger to be in ONE of two states, never the middle:
- **(a) FROZEN** — prepend a banner line `# FROZEN 2026-MM-DD — not maintained; STATUS is canonical, do not cite rows as current`, and stop maintaining it; **or**
- **(b) LIVE** — refresh it + add a boot-time mtime staleness alert so "X.tsv stale Nd" surfaces at boot.

**Why DAEDALUS didn't just edit it:** which one is correct depends on whether the bank↔BDC relationship map is dead reference or a live tracked surface — your domain call, not mine. (Also: a naive `#`-comment banner could trip a header-on-line-1 parser, so confirm your tooling handles it.)

**Ask:** pick (a) or (b) and apply at your next session. No rush — it's hygiene, not a live signal. Logged as the open item of BATCH_01.

— DAEDALUS
