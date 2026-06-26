# CARL Architecture Self-Report
**Date:** 2026-06-26 | **Agent:** CARL | **Requestor:** Prome fleet review

---

## 1. Folder Map

| Dir | Purpose | Flag |
|-----|---------|------|
| `thesis/` | THESIS.md + PREDICTIONS.tsv + CHANGELOG.md | Core / heavy |
| `workbook/` | KB.tsv (297 rows) + domain ledgers (ABS, FLOW, VX, STATE_DIFFUSION) | 2 ledgers stale |
| `board/` | BOARD_LOG.tsv (325 rows) signal disposition log | Append-only |
| `inbox/` | WALTER queue + processed/ archive | Swept today |
| `outbox/` | Cross-agent signals; `delivered/` subdir | **Stale — Apr 17 items undelivered (messaging overhaul hold)** |
| `docket/` | CATALYSTS.tsv + CALENDAR.md forward catalyst queue | Lean / critical |
| `domain/sources/` | Research files, CVNA, ABS analyses | Light |
| `sub_agents/` | 8 domain KB dirs (DOC, GIG, HOMER, PHAN, POLLY, POP, STUE) | Mixed activity |
| `handoff_RED/` | Counter-evidence package for RED | Semi-dormant |
| `scripts/` | Python monitoring scripts | Rarely run |
| `archive/` | Old trade analyses, snapshots | Dormant |

---

## 2. Canonical Doc Set

Boot-read (every session): `CLAUDE.md`, `STATUS.md`, `SCRATCH.md`, `MEMORY.md`, `NEXUS_BRIEF.md`

On-demand: `thesis/THESIS.md`, `thesis/PREDICTIONS.tsv`, `docket/CATALYSTS.tsv`

**Owner→mirror:** STATUS.md owns signal data; NEXUS_BRIEF.md mirrors VIEW/CALIBRATION/CROSS-DOMAIN. Convergence matrix in THESIS.md mirrors into STATUS.md — two places requiring sync.

---

## 3. Knowledge/Data Layer

- **KB.tsv** (297 rows): append-only numbered knowledge items; no expiry, no per-entity structure.
- **PREDICTIONS.tsv** (25 rows): pre-registered binaries with Confidence / Timeframe / Status / Invalidation / Notes. Best-structured file in the system.
- **BOARD_LOG.tsv** (325 rows): signal disposition record; no CARL-domain-tag column.
- **FLOW.tsv / VX.tsv**: domain ledgers — FLOW 66d stale, VX 10d stale.
- Sub-agent KBs: HOMER/GIG/STUE most active; PHAN/POP/POLLY rarely spawned.

---

## 4. Processes

- **Boot:** read 5 canonical files → git status → scan inbox + outbox for pending items.
- **Closeout:** update STATUS.md → refresh NEXUS_BRIEF.md → update SCRATCH.md → prune CATALYSTS.tsv → pathspec commit; no push.
- **Inbox-signal:** read WALTER SIGs → INTEGRATE (git mv to processed/) or KILL-with-memo.
- **Research→canonical:** spawn research-only sub-agents → CARL synthesizes → STATUS.md DANGER WINDOW rows + KB.tsv; thesis changes go to thesis/ with CHANGELOG entry.
- **Verification-calibration:** primary-source verify before STATUS update; PREDICTIONS.tsv falsifiers force pre-commit on thesis claims.

---

## 5. Self-Assessment

**STRENGTHS — most reusable pattern:**
PREDICTIONS.tsv format: pre-registered binaries with explicit falsifiers, confidence, and position-action commitments. Every agent tracking forward theses should copy this structure.

**FRICTION — worst point:**
STATUS.md line-1 header bloat. Three sessions of "prior session" digests are appended inline — the header string now exceeds 2,500 characters. Makes boot orientation slow and edits fragile (single-line match on a giant string).

**GAPS:**
- No auto-staleness alerts for ledgers (FLOW/VX stale discovered via SCRATCH notes, not boot).
- BOARD_LOG missing domain-tag column; 325 entries require grep to find CARL-relevant signals.
- Outbox stale with Apr-17 undelivered signals — hygiene broken pending messaging overhaul.

---

## 6. Top 3 Improvement Ideas

1. **Migrate STATUS.md header digest → CHANGELOG.md.** Keep STATUS line-1 to ≤80 words (version + score + regime). Prior-session digests belong in CHANGELOG. Would make STATUS boot-readable and edit-safe. **(Highest impact — affects every session.)**

2. **Boot-time ledger mtime check** in boot.py: surface "FLOW.tsv stale 66d" as a boot warning, not a discovered-at-closeout note.

3. **BOARD_LOG domain-tag column** (`carl_relevant: Y/N`): enables fast filtering without grep; makes sweep audits machine-checkable.
