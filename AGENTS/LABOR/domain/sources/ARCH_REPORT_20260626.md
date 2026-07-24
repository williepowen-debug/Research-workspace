# LABOR — Architecture Self-Report
**Date:** 2026-06-26 | **Agent:** LABOR | **Template:** Fleet Arch Review v1

---

## 1. Folder Map

| Dir | Purpose | Flag |
|-----|---------|------|
| `archive/` | Prior CLAUDE.md, SKELETON, + Mar artifacts moved today | Healthy — just cleaned |
| `docket/` | `CATALYSTS.tsv` — catalyst source of truth; countdown script reads it | Lean/good |
| `domain/` | Session-scoped research (e.g. `CLAIMS_PREMORTEM_JUN18.md`) | Thin — 1 file; no archival policy |
| `inbox/` | Inbound signals + `WALTER/` delivery lane + `processed/` | Functional; board_log.tsv missing |
| `outbox/` | Outbound signals; `delivered/` subdir for HERMES | Functional |
| `recon/` | `STAGE2_FINDINGS_2026-03-15.md` — one-off March artifact | **Dormant; should archive** |
| `research/` | 17 files, mostly March 2026 | **Heavy/stale — no retirement policy** |
| `scripts/` | `boot.py` + 4 sub-scripts (data refresh, countdown, predictions scan, TX WARN) | Strong |
| `sources/` | 10 analytical framework files (framework docs, deep dives) | Healthy |
| `workbook/` | KB.tsv (99 rows), VX.tsv (~60 rows), FLOW.tsv, PREDICTIONS.tsv + misc | **Heavy/mostly stale** |

---

## 2. Canonical Doc Set

| File | Role | Boot-read? |
|------|------|-----------|
| `CLAUDE.md` | Identity, spawn protocol, domain scope, cross-agent signals | Yes (implicit) |
| `STATUS.md` | Live state — dashboard, convergence matrix, predictions, bottom line | **B1 (primary)** |
| `LESSONS.md` | LABOR-specific mistake patterns | B3 |
| `NEXUS_BRIEF.md` | Standing cross-agent brief; refreshed every closeout | Closeout artifact |
| `TRADE.md` | KELYA position logic (TRADE scope, not LABOR) | Referenced |
| `docket/CATALYSTS.tsv` | Catalyst source of truth; STATUS calendar is its human **mirror** | B2 (via boot.py) |

Owner→mirror: `CATALYSTS.tsv` → `STATUS § MONITORING CALENDAR`. Strict rule: don't let them diverge in event set.

---

## 3. Knowledge/Data Layer

- **KB.tsv (99 rows):** Fact+source+conf (A1/B1/B2/C2/C3)+epistemic+Status+Stale_By. Strong schema; L-04 lesson: almost no one reads it except during research, so it silently rots months behind STATUS. Currently mostly ACTIVE/CONFIRMED rows from Feb-Mar 2026.
- **VX.tsv (~60 rows):** Vector tracking with thresholds and state. Only 4 claims rows are live; ~56 rows are effectively stale. Demote-to-archival decision pending since Jun 14 (recommended YES; never executed).
- **FLOW.tsv:** Transmission pathways. Partially refreshed Jun 16 (3 dangerous rows fixed); remainder stale.
- **PREDICTIONS.tsv:** Falsifiable forecasts with LAB-xx IDs. `predictions_due.py` scans it at boot — solid automation. Controlled vocab (`OPEN`/terminal) required; custom Status values silently drop rows from the scan (L-Jun-16 lesson).

---

## 4. Processes

- **Boot (B0–B5a):** git pull → read STATUS → run `boot.py` (live FRED sweep + catalyst countdown + predictions scan) → read LESSONS → eyeball predictions/catalysts past due → process WALTER inbox. The boot.py automation is the strongest process in the suite.
- **Closeout (C1–C6):** STATUS write-back → resolve predictions/catalysts → workbook sync (C3, chronically deferred) → detail→sources/ → promotion scan → pathspec commit. C3 is the chronic weak link.
- **Inbox/signal:** Separate spawn only. Per-item: read → cross-reference workbook → assess thesis impact → update STATUS if warranted → git mv to processed/. No reply unless new info or error.
- **Research→canonical promotion:** Detail goes to `domain/sources/`; STATUS gets a summary row. Framework docs go to `sources/`; session-scoped docs to `domain/`. No clear policy for `research/` (17-file graveyard).
- **Verification/calibration:** 4-LLM cross-verify on critical data (KB confidence ratings); predictions use `predict-surprise-not-priced` discipline; LAB-15/01 falsifications logged.

---

## 5. Self-Assessment

**STRENGTHS (copy these):**
1. **Boot/closeout symmetry** — every file read at boot is explicitly written back at closeout (STATUS B1→C1, LESSONS B3→C5, predictions B4→C2, catalysts B5→C2). This is the single most reusable pattern in the fleet — it prevents state drift structurally, not by discipline.
2. **`boot.py` automated sweep** — live FRED data + threshold flags + countdown + predictions scan in ~5 seconds. Should be the model for every domain agent.
3. **NEXUS_BRIEF as standing closeout artifact** — refreshed every session so NEXUS reads fresh data, not a stale snapshot.

**FRICTION (worst point):**
**Workbook (VX/KB/FLOW) chronically lags STATUS.** C3 is the only closeout step with no automation — pure manual discipline — and it keeps getting deferred. The ledgers accumulate stale/dangerous rows (L-04, surfaced Jun 14; VX demote recommended Jun 14 but never executed Jun 26). This is the fleet-wide failure mode: STATUS is truth, workbook is a liability.

**GAPS:**
- `board_log.tsv` — referenced in CLAUDE.md B5a (WALTER consumption spec) but the file doesn't exist; WALTER lane is wired but the intake log has never been created.
- `research/` has no retirement policy — 17 files, no rule for when to archive.
- `recon/` subdir is orphaned (single March 2026 file, no active process).

---

## 6. Top 3 Improvements (ranked)

1. **Demote VX/KB/FLOW to frozen-archival now.** The BRENT pattern: single frozen-ledger header banner, stop maintaining stale rows. STATUS is the real truth. This ends L-04 permanently. Cost: one session pass. Benefit: eliminates the worst recurring friction point fleet-wide.

2. **`research/` retirement policy: >60d + not boot-read + not referenced → auto-archive.** One rule, applied each closeout. Would have cleared today's March cruft months ago. Zero cost to implement as a C5 checklist item.

3. **Standing pre-mortem template.** `CLAIMS_PREMORTEM_JUN18.md` was written fresh; it should be a `domain/CLAIMS_PREMORTEM.md` template refreshed on each upcoming print with the decision tree pre-loaded. Preserves history, saves session time, makes the decision tree a standing contract not a one-off.
