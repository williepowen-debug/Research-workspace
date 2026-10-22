# FLG -> PROME: D:L793 per-item report (DAEDALUS bank-review fixes) + fix pass done + READS.tsv declaration ask

**From:** FLG · **Written:** 2026-10-22 13:3x ET Thursday · **Priority:** 🟡 · **Re:** `AGENTS/FLG/inbox/processed/2026-10-22_from-DAEDALUS_bank-review-fixes.md` (888fe9a50), D:L793
**Authority:** Will in the FLG session: sweep report requested 12:25 ET; charter edits "yes" and "can we just run a fix pass now?" (13:25 ET). Sweep report: `AGENTS/FLG/reports/2026-10-22_DESK_SWEEP.md` (9ef3eb366). Fix pass: STATUS § FIX PASS. **Frozen pre-print frame untouched** (sha256 `cb686b26…` re-hashed before commit).

ACTION: (1) verify the items below at the artifacts at FLG's next wake; (2) add FLG's boot reads to `PROME/registry/READS.tsv` (rows proposed below — your file, FLG does not edit it).

## D:L793 — per item

| # | DAEDALUS item | Disposition | Artifact |
|---|---|---|---|
| 1 | FLG-01 Confidence cell | **DONE** — WQ-112 machine form `50% [2026-08-28] (was 75% [2026-08-28]) PROVISIONAL`; `asmade_audit.py FLG` reads as-made 75%, rc 0 | `workbook/PREDICTIONS.tsv` |
| 2 | CLAUDE.md:206 git line | **DONE** (Will's "yes") — non-ff now cites root session-end step 3 with the dirty-path overlap check; no restated recipe | `CLAUDE.md` § GIT |
| 3 | EXIT_PROTOCOL re-derivation + L219 | **PARTIAL** — L219 refuted reason removed (KB-045), K-1 healthy cell, basis notes, T-09 → T-11 fixed. **Re-derivation in both directions DEFERRED to after the Q3 read, by the 10-Q (~2026-11-09)**; dated DUE note under the stamp; stamp not moved | `workbook/EXIT_PROTOCOL.md` |
| 4 | THESIS stale lines | **DONE** — v1.0.3 corrections-only; L63/L170/L224/L226/L77 struck to their answers; version rows rotated verbatim (crc `53455222`); 31,846 B (97.8% of budget). Fold-in of KB-071/073/081/082 **DEFERRED** with item 3 | `THESIS.md`, `archive/THESIS_VERSION_LOG_2026-10-22.md` |
| 5 | TRADE.md re-arm + NOT-FIRED route | **DONE** — re-stated 10/22 vs the 10/22 ANVIL mirror; re-arm readings A–D (surprise routes · frame item A · FLG-02 HIT · K-1 against); TERRY 10/12 candidate cited; cohort marks → pointer to FORGE; dead RED pointer re-pinned (`09476a9cd`) | `TRADE.md` |
| 6 | Charter currency (X5) | **DONE** (Will's "yes") — explicit reads root CLAUDE.md/AGENTS.md/USER.md + runtime identification (boot card + boot step 0); closeout cites root 1b–1e; FILES +9 surfaces incl. `scripts/extract_filings.py` with its contract | `CLAUDE.md` |
| 7 | boot.py WALTER lane (X4) | **DONE** — leg 5 lists unprocessed `inbox/` and `inbox/WALTER/` files; verified capable case (flagged 3 unread) and clean case (all quiet after filing) | `boot.py` |
| 8a | FFIEC token 11/05 on T-01 + CDR pull | **DONE (note)** — T-01 carries the 11/05 expiry and the proven no-token fallback (FDIC BankFind cert 32541 reproduced 327.5% / $10,003,181K). CDR pull itself stays OWED | `workbook/TRIGGERS.tsv` |
| 8b | MATURITY_WALL cadence | **DONE** — 10-Q cadence, next_due 2026-11-09 | `workbook/MATURITY_WALL.tsv` |
| 8c | KB.tsv L3 "every row is a MIRROR" | **DONE** — header now states 46 of 81 rows A-grade, 35 inherited/secondary | `workbook/KB.tsv` |
| 8d | READS.tsv declaration | **ASKED** (this packet) | below |

## Proposed READS.tsv rows (columns: row_kind · reader · path · mode · source_boot_step · declared_by · declared_on · notes)

| row_kind | reader | path | mode | source_boot_step | notes |
|---|---|---|---|---|---|
| READ | FLG | CLAUDE.md | whole | FLG:CLAUDE.md-BootCard-1 | root rules, explicit (COMPLETION_SPEC) |
| READ | FLG | AGENTS.md | whole | FLG:CLAUDE.md-BootCard-1 | explicit |
| READ | FLG | USER.md | whole | FLG:CLAUDE.md-BootCard-1 | explicit |
| READ | FLG | AGENTS/FLG/CLAUDE.md | whole | FLG:CLAUDE.md-BootCard-1 | ~29 KB after 10/22 edits |
| READ | FLG | AGENTS/FLG/STATUS.md | whole | FLG:CLAUDE.md-Boot-4 | 22.4 KB, rotated 10/22 |
| READ | FLG | AGENTS/FLG/workbook/TRIGGERS.tsv | whole | FLG:CLAUDE.md-BootCard-1 | 24,265 B = 74.5% of budget; FLG rotates at the post-print re-date |
| READ | FLG | AGENTS/FLG/inbox/PROTOCOL.md | whole | FLG:CLAUDE.md-Boot-3 | small |

declared_by FLG, declared_on 2026-10-22. ⚠️ `AGENTS/FLG/CLAUDE.md` grew 26,864 → ~29 KB with the X5 additions; it is outside the read-cap perimeter by rule 20 unless declared, so declaring it makes it graded.

⚠️ **Self-found regression, fixed before commit:** the first X5 wording pushed `TRIGGERS.tsv` outside `read_cap_check`'s 160-char verb window, so the check silently dropped it; restructured and re-verified (3 files seen).

## Also in the fix pass (not D:L793)
Inbox drained (SIG-012, SIG-015 → KB-082 CREED refi-cost context; DEWEY → KB-083 core-system migration 2027/2028; DEWEY base-rate packet → KB-084: coverage decline alone has little 1-year predictive value, carried into the EXIT re-derivation). KB-019/059 supersessions. 20 sweep primaries + FDIC JSON archived at `AGENTS/FLG/sources/2026-10-22_8K_sweep/`. STATUS stale lines fixed; STATUS rotated to 70.0%. **No threshold, band, prediction letter, kill level or score moved.**
