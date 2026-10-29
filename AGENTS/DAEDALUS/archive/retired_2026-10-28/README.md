# Retired 2026-10-28 — DAEDALUS document-retirement checkpoint (October 25 queue, run +3d)

Root rule: >60 days old AND not boot-read AND not referenced by a live doc → `git mv` to own `archive/`. Source list: `runs/2026-10-21_STALENESS_EVIDENCE/retirement_dispositions.tsv` (27 RETIRE_CANDIDATE_VERIFIED_HISTORY; 11 moved 2026-10-22 → `archive/retired_2026-10-22/`). Inbound-reference census 2026-10-28: `git grep -l -F <basename>` excluding archives, `_prior/` and the staleness evidence dir; a reference from run evidence (`runs/*.json`, `*.txt`, orphan-check outputs), a processed inbox packet or an inventory TSV is a historical record, not a live doc (root Data Hygiene clause ②).

**Moved (12), relative path preserved under this folder** — every one is bannered closed/history and stands alone:
builds/hawk_split/WP1_REPORT.md · WP2_REPORT.md · WP3_REPORT.md (only inbound: `runs/prome_sweep_2026-10-03/source_tree.tsv`, an inventory) · builds/homer_promotion/WPH2_REPORT.md (only inbound: a CARL processed packet 7/12) · upgrades/PROME_AUDIT_2026-07-28_readers/reader_flow_findings.md · reader_spine_findings.md (inventory only) · reader_rails_findings.md (OTTO `CONSUMERS_RAW.txt` evidence) · reader_tools_findings.md (`runs/2026-09-08_CLOCK_SWEEP_CONSUMERS.json`) · upgrades/MARCO_CARD.md (orphan-check outputs only; PR8 write-back 10/21 recorded on the card, card historic) · upgrades/SAM_BRENT_REVIEW_2026-08-17_READER_REPORTS.md (index stub; closeout JSON/logs) · upgrades/WP4_ECHO_REPORT_2026-07-10.md · upgrades/WP3_MOLD_REPORT_2026-07-10.md (closeout JSON only).

Old path `AGENTS/DAEDALUS/<p>` → new path `AGENTS/DAEDALUS/archive/retired_2026-10-28/<p>`.

**Held (4) — a LIVE doc or script still travels the reference; move only with the pair:**
- `design/2026-08-11_STALENESS_CADENCE_PROPOSAL.md` — cited by `scripts/ledger_staleness.py` (docstring) and `PROME/plans/2026-10-22_terry-falcon-ledger-fix-PLAN.md` (PROME's live plan).
- `upgrades/LABOR_QC_2026-07-22.md` — cited by `scripts/ledger_staleness.py` and `outbox/delivered/2026-07-22_to-PROME_labor-qc-flags.md`.
- `upgrades/DAEDALUS_SELF_AUDIT_2026-08-17.md` — pair with its `_READER_REPORTS.md` (retained-linked) and OTTO 10/25 `CONSUMERS_RAW.txt`.
- `upgrades/REGINALD_CARD.md` — cited by `runs/2026-10-22_BANK_DESK_REVIEW/REGINALD.md` (current review); PR8 write-back 10/21 on the card.
The two script citations are DAEDALUS's to re-point (scripts/ grant) at the next ledger_staleness edit; the PROME plan citation is PROME's.
