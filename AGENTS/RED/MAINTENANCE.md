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

## 2026-06-02 (Session 16, cont.) — retired the duplicate/contradictory `thesis/PREDICTIONS.tsv`

**Trigger:** Will — "take a look at Predictions." Investigation of the dual-file flag (audit §C item 1).

**Finding:** `thesis/PREDICTIONS.tsv` wasn't just stale — it was the **unreconciled pre-ML-RED-068 fork** with *contradictory IDs*. It numbered the May predictions RED-11–14 (conflicting with canonical, where RED-11–14 = the Apr-18 batch and the May predictions = RED-16–19), and was missing the Apr-18 batch + RED-15–19 entirely (14 rows, ragged 6/7-col, last touched May 17). The Session-14 ML-RED-068 cleanup reconciled STATUS/MEMORY/CALENDAR but **missed this file.**

**Fix (lossless):**
- `git mv thesis/PREDICTIONS.tsv → archive/superseded_workbook/PREDICTIONS_thesis_unreconciled_PRE-ML-RED-068.tsv` (verbatim preserved). Verify-before-archive: confirmed `workbook/PREDICTIONS.tsv` is a complete superset (RED-01–19, uniform 10-col) and the only genuinely-unique content (BRENT v2.0 challenge-rationale phrasing) lives in `CHG-RED-024` / `challenges/BRENT_V2_CHALLENGE.md`.
- New breadcrumb `thesis/PREDICTIONS_README.md` — points to the canonical file + warns against re-forking.
- **`CLAUDE.md` updated:** removed `thesis/PREDICTIONS.tsv` from the Thesis-Directory table; added a callout that `workbook/PREDICTIONS.tsv` is sole canonical.

**Resolves:** charter-flag item 1 (dual PREDICTIONS). Remaining flagged items: RED_SKELETON refs in CLAUDE.md; `thesis/TIMELINE.md` staleness.

---

## 2026-06-02 (Session 16, cont.) — cleaned up retired `RED_SKELETON.md` references in CLAUDE.md

**Trigger:** Will — "look at the RED_SKELETON references" (audit §C item 2).

**Finding:** `RED_SKELETON.md` was retired Apr 5 (superseded by `workbook/VX.tsv`), but `CLAUDE.md` still cited it as a **live** reference in 3 places — "Reference for deep work," "Rebuild when time permits," and an anti-pattern — risking a future RED consulting or rebuilding a **Feb-12-vintage** file (per-agent counter-evidence registry incl. a stale agent roster: CREED, old MARCO framing). Verified VX.tsv (per-target vectors) fully supersedes its counter-evidence content; nothing unique to salvage.

**Fix:**
- `CLAUDE.md`: removed the `RED_SKELETON.md` row from the WHAT YOU READ table; removed the "Reference (not boot-critical)" subsection and re-filed it under **Archive** as `archive/RED_SKELETON.md` **RETIRED** (do-not-rebuild); generalized the anti-pattern to "don't trust stale registry data — verify VX/KB `Last_Reviewed`/`Stale_By`."
- `MEMORY.md`: corrected the Apr-5 "DELETED" note (archived copy retained; CLAUDE.md mentions cleaned up).
- `archive/RED_SKELETON.md` itself kept as historical record (correctly placed).

**Resolves:** charter-flag item 2. **Remaining flagged item:** `thesis/TIMELINE.md` staleness (Apr 20, predates channel-migration).

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

---

## 2026-06-10 (S17) — Market-tool "breakage" diagnosed: interpreter selection, NOT a broken tool (S16 venv punchlist item CLOSED)

**Symptom:** `python3 FORGE/tools/market-data/fetch.py price ...` → `ModuleNotFoundError: No module named 'yfinance'`. Looked like the S16 "yfinance missing" regression.

**Diagnosis (verified, not assumed):** NOT broken, NOT API overload. The error is a deterministic import failure — it fires before any network call, so rate-limiting/overload is excluded. Root cause: bare `python3` = Ubuntu system interpreter, which is PEP-668 externally-managed (`/usr/lib/python3.12/EXTERNALLY-MANAGED`) — packages can never be pip-installed there by design. All repo packages live in `.venv/`.

**Verified healthy state:** `.venv/bin/python3` = Python 3.12.3 with yfinance 1.2.0 + pandas 3.0.2 + working pip; `fetch.py price` returns live quotes; `dashboard.py` renders Tier 1/2 clean (tested 6/10 ~3:15 PM ET).

**Rule:** always invoke market tools as `.venv/bin/python3 FORGE/tools/market-data/fetch.py ...` (venv activation does not persist across shell calls). The hygiene checklist below already says this — the S17 boot miss was using bare `python3` from muscle memory before re-reading it.

**Closes:** S16 punchlist item 4 ("proper venv fix: sudo apt install python3.12-venv; pin pandas; test dashboard.py") — overtaken by events. Venv exists with working pip (no apt package needed for current state); pandas 3.0.2 runs dashboard.py without error (no pin needed); dashboard tested ✅.

**Optional shared-tooling improvement (Prome-side, NOT RED's file to edit):** `fetch.py`/`dashboard.py` could self-re-exec under the repo venv when imported modules are missing, making them interpreter-agnostic for all agents. Flagged via OUTBOX rather than edited directly (FORGE is shared tooling).

---

## 2026-06-10 (S17) — SPAWN PROTOCOL codified: BOOT / EXECUTE / WRITE-BACK (closeout hardening, Will-approved)

**Trigger:** Will asked whether RED has a proper closeout vs SAM/BRENT/VIOLET. Audit verdict: RED had the network's best boot and its weakest closeout — write-list buried in boot step 10, one handoff line, no DUE-resolution rule, no live-event override, handoff fragmented across LAST_COMPLETION.md + numbered archive/handoffs/. Plan approved on all defaults (D1-D5) 6/10.

**What changed:**
- `CLAUDE.md`: "BOOT SEQUENCE" → "SPAWN PROTOCOL" with BOOT (read, steps 0-9 — preserved BOARD b1-b4 scan; added DUE-scan to step 3, live-anchors step 9 w/ venv path) / EXECUTE (step 10 + **live-event override**, VIOLET pattern) / **WRITE-BACK W1-W10** (read→write pairings; W2 loop-closure "never OPEN-but-stale" extended to CHALLENGES.tsv — RED-unique; W10 git block w/ local-commit default) / discipline overlay (+ RED-specific: counter-signal weights carry as-of dates) / **Doc-Mirror table** (CATALYSTS.tsv→CALENDAR; PREDICTIONS.tsv→STATUS scorecard; CHALLENGES.tsv→STATUS table; canonical wins).
- `SCRATCH.md` NEW — canonical handoff, template at top, rewritten in place at W5. `LAST_COMPLETION.md` RETIRED (breadcrumb left). `archive/handoffs/` FROZEN (README_FROZEN.md; git history versions SCRATCH).
- File tables in CLAUDE.md updated (WHAT YOU READ, Core Files, Archive).

**Dogfood result (Phase 3, same session):** first DUE-scan run found the predictions ledger materially wrong — RED-12/13/14/15/17 ACTIVE-but-stale since late Apr/May, RED-07 canonical lagging its mirrors, RED-08 STATUS-drifted. **TRUE tally 7W/7C/5A vs published "5W/2C/4A" — wrong on all three numbers.** Dispositioned same session; mirrors synced. Validates the recipe's core claim: mechanical scan > vigilance.

**Boot-impact:** next session boots on the new protocol — reads SCRATCH.md (not LAST_COMPLETION), runs DUE-scan at step 3, uses `.venv/bin/python3` per step 9. Friction → log here.

**Out of scope (deliberate):** NEXUS_BRIEF enrollment (Will/NEXUS-phase decision, D3), scripts/boot.py build, KOYOMI-analog steward (Will-deferred S16).
