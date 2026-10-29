# CYPHER — files and their roles

Moved here VERBATIM from `CLAUDE.md` § FILES at 2026-10-29 13:58 EDT (read-cap rotation) [crc32 1840185657]. Added since 10/29: `banking/` (bank cyber / vendor-risk thread; README indexes the rows), `CHARTER_PROVENANCE.md` (build history), `archive/` (rotated STATUS).

## FILES

*(Role tense — pointers name resolution rules, never values that decay. Blueprint §6b.3.)*

| File | Role |
|---|---|
| `STATUS.md` | Live state; its banner is the authority on whether `FIRST_SESSION.md` still applies |
| `FIRST_SESSION.md` | One-time first-session list; spent when the STATUS banner is struck |
| `DATA_ROUTES.md` | Reachability and use of each data route; re-record when a route changes |
| `boot.py` | Boot instrument, 10 legs: wall clock · staleness · predictions-due · catalysts-due · escalation watch · incident re-checks (every live row dated) · matrix/map · KEV (honours `KEV-SEEN:<CVE>@<date>`) · 8-K Item 1.05 (items-filtered) · 8-K Item 8.01 cyber terms (document read; boilerplate shown as info) · **bank-vendor news** (Google News RSS, supplier names x incident terms in the headline; added 10/29 for press-release-only incidents). rc 0 quiet / 1 REVIEW / 2 leg failed |
| `scripts/test_boot.py` | Drill suite for `boot.py` (alert, clean and failure path per leg, on throwaway copies; real files md5-checked). **Run it after any `boot.py` edit**, before commit |
| `workbook/VX.tsv` | Convergence matrix; Score / Kind / band enums and the composite rule in its header; `As_Of` is each row's vintage |
| `workbook/FLOW.tsv` | Transmission map; State enum in its header; every row keyed to a VX vector |
| `TRADE.md` | Declared no-book surface; its banner states the re-arm condition |
| `workbook/INCIDENTS.tsv` | The incident ledger; enums in its header; `Last_Checked` is each row's vintage |
| `workbook/ESCALATION_WATCH.tsv` | Nine rows per wave; `State_As_Of` is each row's vintage |
| `workbook/KB.tsv` | 13-col atomic-claim ledger (schema `AGENTS/FERT/workbook/SCHEMA.tsv`; enums `AGENTS/VOCABULARIES.tsv`; Group `CYBER` provisional until PROME registers it) |
| `workbook/PREDICTIONS.tsv` | Falsifiable forecasts; Status enum in its header |
| `workbook/EXIT_PROTOCOL.md` | Dated kill rail; its `Kill rail re-derived:` stamp is the vintage |
| `docket/CATALYSTS.tsv` | Wake register in PROME's summons schema |
| `board_log.tsv` | WALTER signal consumption log (BOARD_CONSUMPTION_SPEC §8.1) |
| `inbox/` + `PROTOCOL.md` · `outbox/` | Mail |
