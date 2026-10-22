# REGINALD Architecture Self-Report
**Date:** 2026-06-26 | **For:** Prome fleet-wide compare/contrast

---

## 1. Folder Map

| Dir | Purpose | Flag |
|-----|---------|------|
| `WAL/` | Active primary bank — FRAUD/, MARKET/, research/, sources/, workbook/ | 🔴 HEAVY (64 files — justified; thesis-primary) |
| `EGBN/` | Active primary bank — workbook only | ⚠️ THIN (9 files; ranked #1 but underbuilt) |
| `ZION/` | Active monitor — FRAUD/, research/, sources/, workbook/ | OK (11 files) |
| `CFG/` | Active monitor | OK (21 files) |
| `FITB/` | Excluded from thesis (confounded cohort) | ⚠️ HEAVY-DEAD (21 files; no live thesis) |
| `MTB/` | Off-matrix (Baltimore CRE thread stalled) | DORMANT (12 files) |
| `RF/`, `PNC/` | Off-matrix entirely | DORMANT (18+9 files; deferred cleanup) |
| `thesis/` | Master THESIS.md + TIMELINE.md + CHANGELOG.md | Boot-lean; correct |
| `workbook/` | Framework docs (CHANNELS, CRE_ARCHITECTURE, CONVERGENCE, NDFI_RESEARCH) | OK |
| `research/` | Drill outputs (CRE_DQ, COHORT_NCO, Q2_GRID, ADVERSARIAL, TRIPWIRE) | GROWING — no pruning rule |
| `board/` | BOARD_LOG.tsv (174 rows; structured signal routing) | OK |
| `registry/` | THRESHOLDS.tsv (REG-T-NN trigger definitions) | OK |
| `inbox/` + `inbox/WALTER/` | Signal intake; processed/ subdir | Fixed today; was backlogged |
| `sub-agents/` | CREED (office) + BELT (mortgage) — RENO/TEX now archived | ⚠️ CREED/BELT stale (last active ~Apr) |
| `domain/` | Shared research (NDFI, WAREHOUSE_EXPOSURE, FL refs) | OK |
| `archive/` | Retired dirs + STATUS history | OK |
| `scripts/`, `session_archive/`, `sources/`, `earnings_briefs/`, `trade/` | Support; thin | OK |

---

## 2. Canonical Doc Set

| File | Role | Boot-read |
|------|------|-----------|
| `STATUS.md` | Live dashboard — thesis, signals, matrix, positions pointer, triggers | YES |
| `MEMORY.md` | Cross-session memory — findings, feedback, session notes | YES |
| `CALENDAR.md` | Forward catalysts + print dates | YES |
| `SCRATCH.md` | Intra-session workspace + next-session items | YES |
| `ROADMAP.md` | Ongoing threads + awaiting-data + resolved | YES |
| `POSITIONS.md` | Canonical position list (STATUS/CALENDAR point here; no duplication) | On-demand |
| `thesis/THESIS.md` | Master thesis (WAL-idiosyncratic framing + vectors) | On-demand |
| `WAL/THESIS.md`, `WAL/SCENARIOS.md` | Per-bank deep state | On-demand |
| `registry/THRESHOLDS.tsv` | Trigger definitions (REG-T-NN) | On-demand |
| `board/BOARD_LOG.tsv` | Signal processing record (9b diff scan) | Diff-only at boot |

No owner→mirror relationships currently. POSITIONS.md is the single-source; STATUS/CALENDAR point to it.

---

## 3. Knowledge/Data Layer

- **WAL KB**: `WAL/KB.tsv` (105 rows, 16 groups) — tab-separated, group headers, free-text evidence. No schema enforcement.
- **Predictions**: `workbook/PREDICTIONS.tsv` (REG-NN series with conf/resolve-date/canonical-measure). Drift risk: STATUS and CALENDAR display copies that desync on updates.
- **Triggers**: `registry/THRESHOLDS.tsv` (REG-T-NN, 8 rows) — cross-ref with BOARD_LOG `signal_role` field.
- **Per-bank structure**: inconsistent. WAL has KB.tsv + SCENARIOS + INDEX + POSITIONS + CHANGELOG. EGBN has workbook/ only. CFG has research/ + workbook/ but no KB.tsv. No fleet standard.
- **BOARD_LOG.tsv**: 11 columns (signal_id / date / category / verify_verdict / disposition / conf / integrated_into / related_signals / tags / name_entities / notes). Proven format; only REGINALD uses it.

---

## 4. Processes

**Boot:** CLAUDE.md → STATUS/MEMORY/CALENDAR/SCRATCH/ROADMAP read → market.py live prices → inbox scan → BOARD 9b diff (new SIG-W rows since last session).

**Closeout:** STATUS header + tape refresh → CALENDAR prune → SCRATCH session entry → MEMORY session notes + next-session items → ROADMAP thread updates → recursive drift-grep for thesis-level changes → commit own-dir pathspec.

**Inbox-signal:** SIG-W delivered to `inbox/WALTER/` → read → board log entry (category / verify_verdict / disposition / conf / notes) → INTEGRATE (STATUS row) or INFO_ONLY or REFER → git mv to `processed/`. *Friction: git mv step often deferred, causing backlog (fixed today: 14 files).*

**Research→canonical:** Question framed in ROADMAP → subagent drill (parallel EDGAR, pre-registered classification rule) → drill doc in `research/` → STATUS row integration + ROADMAP thread marked resolved. Self-curl verification on decisive ratios before integrating.

**Verification-calibration:** Parallel Sonnet subagents per bank (EDGAR primary: 8-K EX-99 supplement first, 10-Q for detail) → verbatim quotes + accession → self-curl decisive ratios. Pre-register classification rule BEFORE reading data (catches motivated-reasoning inversions).

---

## 5. Self-Assessment

**STRENGTHS:**
1. **Multi-bank parallel EDGAR drill with self-curl verify** — validated at 5 banks ~15 min; pre-registration discipline catches inversions. Most reusable pattern in the fleet.
2. **BOARD_LOG.tsv 9b scan** — structured signal routing with verify_verdict + conf fields; prevents both over-integration and signal burial.
3. **POSITIONS.md as single-source** — STATUS/CALENDAR point to it rather than duplicating; fixed a recurring desync class.

**FRICTION:**
1. **Per-bank folder sprawl is the worst friction point.** FITB (21 files), RF (18), MTB (12), PNC (9) have significant file mass but no live thesis weight. Navigating the tree at boot requires mentally filtering ~60 dead files. The model works for WAL (thesis-primary) but creaks badly for off-thesis banks retained as research archives.
2. **STATUS.md is overloaded** (226 lines). The signal dashboard, thesis summary, convergence matrix, predictions, exit rules, and threshold table all live in one file. Boot-read is slow; sections drift apart.
3. **Predictions desync**: `workbook/PREDICTIONS.tsv` is source-of-truth but STATUS.md and CALENDAR.md carry display copies that lag on confidence changes.

**GAPS:**
1. EGBN is ranked #1 but has 9 files and no KB.tsv — severely underbuilt before any position.
2. CREED and BELT sub-agents have not been refreshed since ~April; their signals are stale.
3. No pruning rule for `research/` — drill docs accumulate without retirement criteria.

---

## 6. Top 3 Improvement Ideas (ranked)

1. **Tier the per-bank folders: active-thesis vs research-archive.** Rename dormant bank dirs to `archive/banks/FITB/` etc. Keep only thesis-active banks (`WAL/`, `EGBN/`, `ZION/`, `CFG/`) at the top level. Reduces nav noise ~60 files. *Per-bank model works at depth for one primary bank (WAL) — does not scale to 9 banks maintained in parallel.*

2. **Split STATUS.md into STATUS.md (thesis + matrix + positions, ≤100 lines) + DASHBOARD.md (live signals, tape, triggers, ~80 lines).** Boot reads DASHBOARD.md for the live read; DASHBOARD.md is the high-churn file. STATUS.md becomes more stable and easier to diff for thesis changes.

3. **Inbox auto-sweep in scripts/boot.py:** automatically git-mv any SIG-W files older than 7 days with a board-log entry already present. Eliminates the recurring backlog (today: 14 files manually moved that were already board-logged weeks ago).
