# Retired 2026-10-22 — DAEDALUS document-retirement checkpoint (October 25 queue, run early on Will's word 17:41 ET)

Root rule: >60 days old AND not boot-read AND not referenced by a live doc → `git mv` to own `archive/`.
Source list: `runs/2026-10-21_STALENESS_EVIDENCE/retirement_dispositions.tsv` (27 RETIRE_CANDIDATE_VERIFIED_HISTORY).

**Moved (11), relative path preserved under this folder** — every one is bannered closed/history and stands alone:
design/2026-08-03_RAV_QC_002_SHARED_INDEX_RECIPE_REVIEW.md · design/2026-08-03_HAWK_SUNSET_ADJUDICATION.md · builds/FERT_RECHARTER_2026-08-16.md · upgrades/ZHAO_CARD.md · upgrades/YEYOU_CARD.md · upgrades/TERRY_ARCHITECTURE_AUDIT_2026-07-30.md · upgrades/CODEX_CROSS_REVIEW_2026-07-12.md · upgrades/ORACLE_CARD.md · upgrades/AEOLUS_QC_2026-07-22.md · upgrades/DAEDALUS_SELF_SWEEP_2026-07-22.md · upgrades/CORAL_CARD.md
Old path `AGENTS/DAEDALUS/<p>` → new path `AGENTS/DAEDALUS/archive/retired_2026-10-22/<p>`. Remaining references sit in history records (processed inboxes, FLEET_MAP_HISTORY, run evidence) and were left as written.

**Kept in place (16) — package-aware rule, not eligible as isolated moves:**
| Kept | Why |
|---|---|
| builds/hawk_split/WP1–WP3_REPORT.md | package: MANIFEST_A/B/C retained |
| builds/homer_promotion/WPH2_REPORT.md | package: MANIFEST_D, WPH1, PROMOTION_REVIEW retained |
| upgrades/PROME_AUDIT_2026-07-28_readers/ (4) | reader set of the retained PROME_AUDIT_2026-07-28.md synthesis |
| upgrades/DAEDALUS_SELF_AUDIT_2026-08-17.md | pair: its READER_REPORTS retained |
| upgrades/SAM_BRENT_REVIEW_2026-08-17_READER_REPORTS.md | pair: SYNTHESIS not in the eligible set |
| upgrades/WP3_MOLD_REPORT / WP4_ECHO_REPORT_2026-07-10.md | series: WP1_TALOS retained |
| design/2026-08-11_STALENESS_CADENCE_PROPOSAL.md | live reference: PROME/plans/2026-10-22_terry-falcon-ledger-fix-PLAN.md |
| upgrades/LABOR_QC_2026-07-22.md | live reference: scripts/ledger_staleness.py provenance comment |
| upgrades/REGINALD_CARD.md | cited by runs/2026-10-22_BANK_DESK_REVIEW; REGINALD whole-profile refresh queued |
| upgrades/MARCO_CARD.md | written 2026-10-21 (PR8 write-back) — no longer >60 days |
A whole-package retirement of the kept packages is a later, separate decision.
