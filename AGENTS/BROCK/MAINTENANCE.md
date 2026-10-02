# BROCK Maintenance Log

Reverse-chronological log of **structural** changes to BROCK's docs, folders, scripts, and SPAWN/closeout protocol — plus the **modernization backlog**. Each change-log entry: **Trigger / What changed / Files touched / Boot-impact / Lessons**. Answers *"why is BROCK organized this way, and what's left to build?"*

**Distinct from:**
- `STATUS.md` — live dashboard (analytical state, rewritten each session).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every closeout; structural notes there do NOT persist — they persist HERE).
- (BROCK has no `thesis/CHANGELOG.md` yet — see backlog item. Until then, analytical thesis pivots are traced in STATUS prose + this file's change-log where structural.)

> **This is a consult-on-structural-work doc, NOT a per-session ritual.** Do not wire it into the every-session closeout (that would be the process-bloat BROCK's tiered protocol exists to avoid; BRENT runs fine without one). Touch it only when a session changes BROCK's *structure* — a doc/folder/script created/retired/moved, a schema or protocol amendment — or when the backlog ranking shifts. Cap: archive to `archive/` if this grows past ~300 lines (SAM cautionary tale: 636).

---

## 2026-10-02 — CREED structural adoption: STATUS hot/cold + catchups/, SCRATCH reset, always-loaded traps, selfcheck, LEDGER_GLOB

- **Trigger:** Will, 10/2: *"I would like you to adopt as much as you think is valuable"*, after the read-across `research/2026-10-02_CREED-read-across.md` (12 items ranked). The decisive evidence: VX-BRK-004 still read "three vehicles at 2 [9/3]" after GATE-BRK-R2 (a) had fired twice.
- **What changed:**
  1. **Propagation fix:** VX-BRK-004, CATALYSTS rows 40/44/51 and the register's 9/3 run-state now carry both fires.
  2. **`workbook/LEDGER_GLOB`** = `workbook/*.tsv docket/*.tsv`.
  3. **STATUS hot/cold split:** 29,437 → 22,242 B (90% → 68%). New §Standing Obligations; session narrative → `catchups/2026-10-02.md` (verbatim, crc per block) with `catchups/INDEX.md` naming the CURRENT one; pre-split bytes at `archive/STATUS_PRESPLIT_2026-10-02.md` (crc32 `d78e04c9`). Audited by OBLIGATION: 28 owed-item tokens present after the split. Five stale lines corrected.
  4. **SCRATCH reset:** the 47 KB appended file (never a boot read) → `archive/SCRATCH_PRESPLIT_2026-10-02.md`. Its 12 live debts moved to STATUS, including the FORUM-5 W2 standing test, which had been invisible at boot. The new SCRATCH is overwrite-only and is boot step 0b.
  5. **`scripts/brock_selfcheck.py`** (closeout 6c), adapted from CREED's selfcheck. v1 MISSED VX-BRK-004 on the pre-fix files and was replaced before adoption (segment-level history stripping). v2: 10 findings on pre-fix, CLEAN on current, planted count/NF faults caught, missing surface rc=2.
  6. **Charter:** ALWAYS-LOADED §STANDING TRAPS (7 write-time traps); boot 0b SCRATCH, boot 1 STATUS + §Standing Obligations + CURRENT catch-up; closeout 6 bytes-not-lines + catchups + audit-by-obligation; 6b SCRATCH rewrite; 6c selfcheck; 7b propagation; stale byte figures removed (PREDICTIONS 48,681 / board_log 89,476 B had gone stale); Doc Ownership + FILES tables.
  7. **LESSONS rotation:** #23–#30 verbatim → `archive/LESSONS_ROTATED_2026-10-02.md`; 30,841 → 21,535 B (95% → 66%).
- **Deliberately NOT adopted, with reasons:**
  - Boot-time threshold scan: most BROCK triggers are filing events, not numeric bands.
  - VX/PREDICTIONS notes hot/cold split: PREDICTIONS is a declared scoped read, so not a breach.
  - VX_HISTORY Role/Basis rebuild: there is no base-rating need yet.
  - Predictions scoreboard and evals: low value now.
  - CREED's cases/ ledger and Trepp tools: CRE-specific.
  - CREED's `boot.py`: retired by CREED (it keyed freshness on mtime).
- **Boot-impact:** new boot reads `SCRATCH.md` (0b), `catchups/INDEX.md` + the CURRENT catch-up (1). `PROME/registry/READS.tsv` rows owed → PROME packet.
- **Lesson:** the tool built to catch the defect missed it on its first run. Falsifying against the real pre-fix files, not a synthetic fixture, is what showed it.

## 2026-06-15 — Tier-1 structure modernization (Phase-3 split) + ORC verification round

**Trigger:** Will-directed catch-up after a 7-day dark window + Opus-4.8 switch. STATUS had drifted to 272 lines with forward-state (10-Q calendar, FOLLOW-UP tiers, watch order, SESSION LOG) inline — over the 250 cap and past the ≥280 SCRATCH-split mandatory trigger's approach. Fleet parity gap: BROCK lacked the `docket/CATALYSTS.tsv` + `SCRATCH.md` + schema-conformant `NEXUS_BRIEF.md` surfaces that BRENT/SAM/VIOLET/HENRY all run.

**What changed:**
- **Created `docket/CATALYSTS.tsv`** (FASTOW 8-col schema: date/event/what_to_check/threshold_signal/priority/who_cares/notes/date_class) — Q1 10-Q verdicts + forward catalyst docket. Migrated the Q1 calendar out of STATUS; added a `📅 CATALYST CALENDAR` human-twin in STATUS. `date_class` aligned to BRENT-canonical `confirmed/modeled` (post-ORC; was confirmed/estimated/scheduled/window).
- **Created `SCRATCH.md`** — session-handoff surface (NEXT-BOOT FIRST MOVES / CHANGES-SINCE / WATCH ORDER / FOLLOW-UP tiers / SESSION LOG / WORKBOOK-MAIL-GIT health). Migrated FOLLOW-UP + watch order + SESSION LOG out of STATUS.
- **Converted `NEXUS_BRIEF.md`** from free-form to fleet-standard schema (R3 + amendment 7: VIEW / CALIBRATION / CROSS-DOMAIN / NEXT DECISION POINT / FORWARD CATALYSTS).
- **STATUS trimmed 272→198 lines**; deduped SIGNAL DASHBOARD (dropped rows now in LIVE TAPE); foregrounded LESSONS #12 in REGIME line.
- **ORC post-push verification round** caught two real errors, both fixed: (a) STATUS footer OPEN-count 16→15; (b) EXIT-RULES/thesis-kill subsection carried stale 14/15bps cushion + falsified "6/5 cracked" narrative while the surface said 11bps/re-diverged — the downstream-propagation gap. HY OAS provenance relabeled `[FRED]`→`[ref LIQUID]` (owner's metric; primary FRED unreachable).

**Files touched:** `docket/CATALYSTS.tsv` (new), `SCRATCH.md` (new), `NEXUS_BRIEF.md` (new→schema), `STATUS.md`, `MAINTENANCE.md` (new — this file), `workbook/KB.tsv` (+KB-BRK-154→158), `workbook/PREDICTIONS.tsv` (BRK-28 resolved), `trade/TRADE.md`.

**Boot-impact:** boot now reads SCRATCH (handoff) + CATALYSTS (docket) + STATUS in sequence; STATUS is leaner. No automated boot kit yet — data pull is still manual (`dashboard.py --compact` + web fallback). Commits `437bbddf`→`5aef28df`, all on origin/master.

**Lessons:** (1) refreshing a doc's *surface* (header/dashboard/BOTTOM LINE) does NOT refresh its *derivative* subsections — the EXIT-RULES cushion contradiction hid in the one section that drives the 100%-exit call (`[[finding_verification_correction_downstream_propagation]]`). (2) "Done, not declared" — pointer lines go in the SAME commit as the files they point to, never ahead (ORC's own header-bug catch, avoided here). (3) Cross-review by recomputation (not description) caught two load-bearing errors a self-edit could not.

---

## MODERNIZATION BACKLOG

The maturity-gap survey vs BRENT/SAM/VIOLET (2026-06-15). Ranked by **leverage ÷ effort × tack-on-fit**, not raw leverage — a low-effort high-fit item beats a high-leverage build that needs its own session.

| # | Item | Leverage | Effort | Fit | Status / gate |
|---|------|----------|--------|-----|---------------|
| 1 | **PREDICTIONS archive + calibration scoreboard** | MED | **LOW** | HIGH | **Do first (incremental).** Notes already bloating (BRK-28 is 3 audit-stamps deep). Pattern: condense closed-row Notes to one-line lesson + `#brk-NN` anchor → `workbook/PREDICTIONS_ARCHIVE.md`; add a boot-read calibration scoreboard preamble (SAM pattern). |
| 2 | **`scripts/boot.py`** | **HIGH** | HIGH | needs design | **Highest raw leverage, but DESIGN-GATED — do not start cold.** Decide first: agent-local script (BRENT/SAM/VIOLET pattern) vs a thin BROCK-profile wrapper around the shared `FORGE/tools/market-data/dashboard.py` + a predictions-due scan + catalyst countdown. Needs live-data testing (venv + FRED) impossible to do well mid-session. Own session. |
| 3 | **`thesis/` versioned layer** (`THESIS.md` + `CHANGELOG.md`) | MED | MED | — | Deferred Tier-2 (ORC-flagged). ~200-line extraction of "Private Credit's Public Reckoning" from STATUS prose into a versioned doc w/ major/minor bumps + old-view→new-view logging. Own pass. |
| 4 | **MAINTENANCE.md** | — | — | — | ✅ **DONE (this file).** Was correctly judged "ceremony" earlier this session when there was no content; the need materialized (a backlog + a structural change-log that otherwise evaporate from SCRATCH). Same subtraction test, different answer. |
| 5 | **FASTOW-style catalyst steward (sub-agent)** | LOW | MED | **premature** | **NOT YET — last.** Building a sub-agent to maintain a `CATALYSTS.tsv` that is one session old is infrastructure ahead of need. Run the docket by hand for several sessions, learn where maintenance actually hurts, *then* build the steward to fit. Premature stewarding is its own anti-pattern. |

**On par / no action:** git pathspec discipline (strong, divergence well-documented); predictions-due boot scan (BROCK has it manually — BRENT's is still a pending boot.py enhancement); doc-ownership table + one-source-of-truth overlay; ALWAYS/SCALED closeout tiering + live-event override (most explicit of the four — a lead, not a gap).

**Recommended sequence:** #1 (cheap, do soon) → decide #2's design → #2 build → #3 → revisit #5 only after the docket has shown real maintenance pain.
