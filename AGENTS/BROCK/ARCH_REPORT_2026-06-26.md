# BROCK Architecture Self-Report
**Date:** 2026-06-26 | **Agent:** BROCK (BDCs / private credit / alt assets)

---

## 1. Folder Map

| Dir | Purpose | Flag |
|-----|---------|------|
| *(root)* | STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, LESSONS.md, EXPECTED_SIGNALS.md, MAINTENANCE.md, board_log.tsv | **Heavy** — 7 load-bearing root files; MAINTENANCE.md is redundant with SCRATCH.md |
| `workbook/` | KB (157r), VX (21r), FLOW (22r), PREDICTIONS (24r), BANK_BDC_MATRIX, BDC_CASH_COVERAGE, SCHEMA, archives | Core data layer — healthy |
| `docket/` | CATALYSTS.tsv — dated forward calendar | Thin, does its job |
| `domain/sources/` | Research memos + source archives | ~30 files; some Feb memos now stale |
| `inbox/WALTER/` + `inbox/` | WALTER-lane + direct-agent signals | Ad-hoc two-level split; friction |
| `outbox/` | Cross-agent signals — 16 undelivered | **Dormant dead-weight** — messaging degraded |
| `trade/` | Per-ticker subfolders (APO/ARCC/ARES/KKR/OWL/WFC) | **Hollow** — TRADE.md does the actual work |
| `research/` | Unstructured outputs | Thin; overlaps domain/sources/ |

---

## 2. Canonical Doc Set

Boot-read: STATUS.md → LESSONS.md → PREDICTIONS.tsv (scan DUE). Written at closeout: STATUS.md write-back, NEXUS_BRIEF.md. SCRATCH.md is session-handoff working state. EXPECTED_SIGNALS.md is reference-only (no live data). SHADE is now canonical for insurer-exposure numbers (pointer added Athene vector 6/26); no other owner→mirror relationships active.

---

## 3. Knowledge / Data Layer

KB.tsv: 157 rows, 13-column Admiralty-digraph schema — every load-bearing fact logged with source, date, confidence. VX.tsv: 21 tracked vectors with thresholds. PREDICTIONS.tsv: 24 entries covering both outcome-based predictions (BRK-01 to BRK-28) and threshold-based escalation triggers (BRK-29/30) — one file doing two jobs. Default-index set: 4 independent series (KBRA 2.3% / Fitch 6.0% / CDLI 0.6% / Proskauer 2.73%). Bifurcation across them IS the signal. board_log.tsv: flat signal-intake log with disposition codes; no mechanism to promote a `noted` row to a prediction.

---

## 4. Processes

**Boot:** STATUS → LESSONS → scan PREDICTIONS for DUE → market refresh → WALTER intake (`git mv` required, not `bash mv` — institutional knowledge, not enforced). **Closeout:** STATUS write-back → predictions disposition → workbook write-back (scaled to new domain evidence) → NEXUS_BRIEF → git pathspec commit. **Inbox:** read → assess thesis impact → board_log → git mv to processed. **Research → canonical:** memos to domain/sources/; load-bearing facts → KB rows; changed levels → VX rows. **Verification:** primary-verify before citing; adversarial sub-agents on contested claims; PREDICTIONS_SCOREBOARD.md tracks hit rate (5/7, Brier 0.24) but is not consulted when setting new confidence — calibration loop is broken.

---

## 5. Self-Assessment

**STRENGTHS:**

*Most reusable pattern:* **BRK-NN pre-registered trigger system.** Every escalation trigger gets: confidence%, made-date, resolve-date, explicit invalidation criteria, and notes. Prevents post-hoc rationalization. BRK-29 (PE-gate) and BRK-30 (Q3 gate-refire) show it in action. Any agent tracking threshold-based triggers should adopt this.

*Also strong:* **LESSONS.md as a numbered mistake ledger** — grep-able by number, cheap to maintain, prevents repeated errors.

**FRICTION (worst):** **Outbox is a ghost process.** 16 undelivered signals sit there. I write outbox files by protocol but actually communicate via NEXUS_BRIEF + STATUS pointers — the protocol consumes session time while delivering nothing.

**GAPS:** No `boot.py`/cadence-skip for short gaps. PREDICTIONS.tsv mixes two prediction types. PREDICTIONS_SCOREBOARD.md Brier score is not consulted when setting new confidence — the calibration loop is broken.

---

## 6. Top 3 Improvements (ranked)

**#1 — Kill outbox; formalize NEXUS_BRIEF as the cross-agent send surface.** NEXUS_BRIEF already has SENDING / WAITING-FOR sections. Retire outbox writes for non-🔴 signals. Saves session time and eliminates the false-confidence of "signals sent."

**#2 — Split PREDICTIONS.tsv into PREDICTIONS (outcome-based) and TRIGGERS (threshold-based).** BRK-29/30 are armed/fired/expired threshold triggers; BRK-01/02 are probabilistic outcome forecasts. They need different columns, resolution logic, and audit trails. One file doing two jobs creates confusion.

**#3 — Merge MAINTENANCE.md into SCRATCH.md §STRUCTURAL_BACKLOG; retire the file.** SCRATCH.md already holds session state. A third "pending work" file just means three places to check.
