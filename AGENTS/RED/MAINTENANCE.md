# RED Maintenance Log

Reverse-chronological log of **structural** changes to RED's docs, folders, schemas, and tooling. Each entry: what changed, why, files touched, boot-impact.

**Distinct from `thesis/CHANGELOG.md`**, which logs **analytical** changes (confidence shifts, hypothesis re-weighting, challenge resolutions, prediction scoring). If a change moves a number or a probability → CHANGELOG. If it moves a *file, schema, or boot path* → here.

**Conventions (adopted from SAM, S16):**
- Archive-next-to-active-doc where practical; `archive/` root holds legacy/superseded.
- Verify-before-archive: confirm content is captured elsewhere before cutting (lossless by construction).
- Loop-closer: when a structural change adds/moves a file, update `CLAUDE.md`'s FILES tables + boot steps in the same pass, so a future RED knows it exists.

---

## 2026-06-02 (Session 16) — SAM-pattern adaptations: CATALYSTS.tsv backbone + this MAINTENANCE log + boot-slim

**Trigger:** Will — "other agents developed meaningful structure; adapt some for RED." Studied SAM; adopted three patterns.

**(1) New `docket/CATALYSTS.tsv`** (structured forward-catalyst backbone, adapted from SAM `docket/CATALYSTS.tsv`). 28 forward catalysts (imminent→Dec), 9 cols: date / window / event / bear_signal / bull_signal / red_threshold / priority / status / notes. **Now the queryable source of truth for catalyst dates/thresholds** (row-by-row prunable — the fix for *why* CALENDAR went stale: prose tables are hard to update incrementally).
- **`CALENDAR.md` slimmed:** removed the IMMINENT + IMMEDIATE + NEAR-TERM + MEDIUM-TERM date-tables (~85 lines, migrated to TSV) → replaced with a pointer + top-imminent summary. **Also dropped a genuinely stale "IMMEDIATE (May 22-29)" section** (already-past events: Tokyo CPI 5/22, calibration retro 5/25, AFT 5/28, OZK 5/29). CALENDAR keeps the narrative layer: RESOLVED history, FALSIFICATION WATCH, scoring windows, exit backstops.

**(2) New `MAINTENANCE.md`** (this file, adapted from SAM `MAINTENANCE.md`). Splits structural-change logging out of `thesis/CHANGELOG.md` (which was carrying both). Going forward, file/schema/boot changes log here.

**(3) Boot-slim `MEMORY.md`** (adapted from SAM boot-slimming discipline). MEMORY's methodology section had grown to multi-hundred-word bullets read in full every boot. Moved the verbose bodies to `MEMORY_ARCHIVE.md` (lossless), kept one-line lesson + `→ MEMORY_ARCHIVE.md#anchor` pointer inline. Load-bearing lessons stay scannable at boot; full depth one pointer away.

**(4) Loop-closer — `CLAUDE.md` updated** so future-RED finds the new structure: boot step 3 now scans `docket/CATALYSTS.tsv`; boot step 4 notes structural changes live here not CHANGELOG; Core-Files table updated (MEMORY = one-liners + archive; CALENDAR = narrative layer; CATALYSTS.tsv added); new "Reference/archive" table rows for `MAINTENANCE.md` + `MEMORY_ARCHIVE.md`. (Did NOT touch the 3 separately-flagged charter items — dual PREDICTIONS, RED_SKELETON refs, TIMELINE staleness — those await Will.)

**Boot-impact: positive** — CALENDAR ~150→88 lines (15.7→11.3KB); MEMORY 35.7→17.6KB (−50%, methodology bodies → MEMORY_ARCHIVE.md); combined RED-owned boot read ~73→~51KB. CATALYSTS.tsv read selectively (status=pending next ~14d), not in full.

**Also this session (logged in `research/STALENESS_AUDIT_2026-06-02.md`, summarized here for the structural record):**
- **Repaired missing `.venv`** (didn't exist; `python3 -m venv --without-pip` + get-pip bootstrap + `pip install yfinance requests`). Market tool live again. NOTE: `.venv` is gitignored; proper fix is `sudo apt install python3.12-venv` (needs Will's sudo).
- **Dedupe:** removed 5 md5-identical `archive/`↔`challenges/` copies (kept challenges/).
- **Relocated** completed VIOLET skew-recheck bundle (10 files incl 1.78MB CSV) → `archive/violet_skew_recheck_apr2026/`; 3 old-format TSVs → `archive/superseded_workbook/`; loose HAWK signal → `inbox/processed/`.
- **Schema fix:** normalized 2 ragged `workbook/KB.tsv` rows (12/14-col) → all 42 rows uniform 13-col.

---

## Pre-S16 (retroactive note)

Before S16, structural and analytical changes were both logged in `thesis/CHANGELOG.md`. Earlier structural history (folder reorganizations, the Apr 5 RED_SKELETON deletion, workbook 7-col→14-col migration, the May WALTER LIAISON file instantiations) lives in `thesis/CHANGELOG.md`, `MEMORY.md` "Cleanup Done" notes, and git history. This file starts the clean separation.

---

## STANDING HYGIENE CHECKLIST (run periodically — candidate for a future maintenance-steward sub-agent)

- [ ] `workbook/VX.tsv` — review each vector's Last_Reviewed; flip/resolve any whose Flip_If fired; log to VX_HISTORY.tsv. (S16: was 7 weeks stale — don't let it recur.)
- [ ] `workbook/KB.tsv` — review entries past Stale_By; supersede point-in-time facts overtaken by events; extend live themes.
- [ ] `docket/CATALYSTS.tsv` — prune resolved (status→resolved + move to CALENDAR RESOLVED), add upcoming, refresh thresholds vs live anchors.
- [ ] `CALENDAR.md` FALSIFICATION WATCH — refresh spot values vs live (market tool: `.venv/bin/python FORGE/tools/market-data/fetch.py price <tickers>`).
- [ ] `STATUS.md` ≤200 lines; archive detailed reports to `reports/`.
- [ ] Dedupe `archive/` vs `challenges/`; relocate completed research to `archive/`.
- [ ] Cross-file consistency: PREDICTIONS scoring matches across STATUS/CALENDAR/workbook (S16 caught a RED-19 contradiction).
