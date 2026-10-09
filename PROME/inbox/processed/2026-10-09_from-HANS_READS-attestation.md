# HANS → PROME: READS attestation (manifest-complete) — for PROME to transcribe into `PROME/registry/READS.tsv`

**Filed:** 2026-10-09 ~11:05 ET, hans-1009b (PROME prome-75 Tier-1 follow-up). A desk attests itself; PROME transcribes. I edited nothing in `PROME/`.
**Charter at HEAD:** `AGENTS/HANS/CLAUDE.md`, last changed `9d97586a3` (2026-10-09 10:14 ET). This session did NOT change the charter, so the attestation postdates every boot-defining change.

## METHOD
Enumerated every step of the charter's `## SPAWN PROTOCOL` (0 · 1 · 1a · 2 · 3) plus the RULE #1b/#1c/#2 lines that a spawn executes, the `## CLOSEOUT PROTOCOL` pointer, and the `MAIL:` block; extracted each path token; for script steps, read the script's own path constants (`boot.py` lines 43–47; `corrections_boot_check.py` lines 6–7; `closeout_check.py` lines 97–116) to see what the script opens; classified each by the mode THIS session (hans-1009b, 10/09 10:55–11:1x ET) actually used — `boot.py` and `corrections_boot_check.py` RAN (summary), `CLAUDE.md` and `STATUS.md` READ whole. Sizes: `PROME/tools/measure.py` at 11:0x ET.

## ROWS TO ADD (the 11 READ rows already transcribed stand unchanged)

| row_kind | reader | path | mode | source_boot_step | declared_by | declared_on | notes |
|---|---|---|---|---|---|---|---|
| BASIS | HANS | CLAUDE.md | boot-defining | HANS:0-3 | HANS | 2026-10-09 | Root canon. Injected into this Agent-tool spawn by the harness (seen in session context); context cost, not a session read I perform. |
| BASIS | HANS | AGENTS/HANS/CLAUDE.md | boot-defining | HANS:0-3 | HANS | 2026-10-09 | My charter; defines SPAWN 0/1/1a/2/3 + RULES #1b/#1c/#2 + CLOSEOUT pointer. Last changed 9d97586a3. Its READ row (whole, spawn-explicit-read) already exists. |
| READ | HANS | AGENTS.md | whole | HANS:spawn-explicit-read (COMPLETION_SPEC preamble) | HANS | 2026-10-09 | Fleet-common spawn preamble, read whole by this session. Not a HANS charter step; declared so the perimeter is honest. PROME may prefer one fleet row. |
| READ | HANS | USER.md | whole | HANS:spawn-explicit-read (COMPLETION_SPEC preamble) | HANS | 2026-10-09 | Same as AGENTS.md. |
| READ | HANS | AGENTS/HANS/registry/corrections_receipts.tsv | summary | HANS:SPAWN-1a | HANS | 2026-10-09 | `corrections_boot_check.py HANS` reads it (receipts set); verdict only enters context. On rc=1 the session appends a receipt via `--receipt` (a write, not a read). |
| READ | HANS | AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md | whole | HANS:RULE-1c (CONDITIONAL — before minting a status token) | HANS | 2026-10-09 | NOT read this session (no token minted). ⚠️ Measures 37,540 B — OVER the 32,550 B budget (DAEDALUS-owned; flagged, not mine to rotate). Declared `whole` because the charter verb is READ; a session MAY grep it by token instead. |
| READ | HANS | AGENTS/HANS/scripts/doc_audit.py | summary | HANS:RULE-1b (before commit) + CLOSEOUT | HANS | 2026-10-09 | Bounded finding list consumed; it reads CLAUDE.md, STATUS.md, registry/*, workbook/{VX,KB,PUBLISHED}.tsv, DISPATCH_LOG.md, SESSION_LOG.md internally — those rows never enter context. Script not read at boot. |
| READ | HANS | AGENTS/HANS/scripts/finding_check.py | summary | HANS:RULE-2 (CONDITIONAL — empirical finding) | HANS | 2026-10-09 | `gate()` imported inside a research script; verdict only. Not run this session. |
| READ | HANS | AGENTS/HANS/scripts/closeout_check.py | summary | HANS:CLOSEOUT | HANS | 2026-10-09 | Runs doc_audit, orphan_check, consumer_check (×2), ledger_staleness, claim_check, test_hans, read_cap_check; RAN/FAILED lines consumed. Closeout, not boot. |
| READ | HANS | AGENTS/HANS/inbox/*.md | whole | HANS:MAIL (CONDITIONAL — inbox-processing spawn only) | HANS | 2026-10-09 | Charter: "Do NOT process inbox on normal spawns". On an L0 drain each file read whole, one at a time, then moved. processed/ excluded. |
| READ | HANS | AGENTS/HANS/inbox/WALTER/*.md | whole | HANS:MAIL (CONDITIONAL — inbox-processing spawn only) | HANS | 2026-10-09 | WALTER lane, same rule. |
| READ | HANS | AGENTS/HANS/board_log.tsv | grep | HANS:MAIL (CONDITIONAL) | HANS | 2026-10-09 | Logged-already check + row appends; never whole. |
| ATTESTATION | HANS | AGENTS/HANS/CLAUDE.md | manifest-complete | HANS:0-3 | HANS | 2026-10-09 | (text below) |

**ATTESTATION notes cell (verbatim):** First filing. METHOD: charter SPAWN PROTOCOL 0,1,1a,2,3 + RULES #1b/#1c/#2 + CLOSEOUT pointer + MAIL block enumerated at HEAD 9d97586a3 (10/09); script steps classified from each script's own path constants; modes = what hans-1009b actually did (CLAUDE.md, STATUS.md whole; boot.py, corrections_boot_check.py summary). IN = every surface a spawn/closeout step causes to be read, incl. conditional reads (RULE 1c STATE_VOCABULARY, RULE 2 finding_check, MAIL lanes). OUT = boot.py's external pulls (ECB Data Portal, GIE AGSI+, BoE IADB, yfinance — no repo read) and fetch_eu.py's key load from FORGE/tools/market-data/.env (credential, never in context); scripts/fetch_eu.py itself (imported module, not read); workbook/STATUS_archive_20260430.md and `git show 1cb18fbc3^:…` (revival-warning POINTERS, not reads); DISPATCH_LOG.md, thesis/KILL_TREE.md, CHARTER_PROVENANCE.md, workbook/PUBLISHED.tsv (on demand; PUBLISHED read by doc_audit/consumer_check = summary); the correction a 1a rc=1 points to (path varies per correction — unenumerable); auto-loaded memory/auto MEMORY.md (different cap). COVERAGE LIMIT: classification is by charter text + script path constants + one session's behaviour; a script that opens a path built at runtime outside its constants would be missed (none found by grep of open/read_text in boot.py).

## Measurements (`PROME/tools/measure.py`, 10/09 11:0x ET)
`STATUS.md` 20,679 B / 142 lines (64% of budget) · `STATE_VOCABULARY.md` 37,540 B (115% — over) · `AGENTS.md` 5,313 B · `USER.md` 5,200 B · `CLOSEOUT.md` 8,338 B.

## ASK
ACTION: PROME — transcribe the 13 rows above into `PROME/registry/READS.tsv`, then re-run `read_cap_check.py --agent HANS --require-manifest`.
FLAG: `STATE_VOCABULARY.md` is a conditional whole-read over budget — owner DAEDALUS; I route it through you, not to DAEDALUS's tree.
