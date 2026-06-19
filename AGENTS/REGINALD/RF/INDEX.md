# RF — Directory Index

**Role:** Read-through / pattern bank (not a position name).
**Primary purpose:** Consumer DQ leading indicator; Southeast CRE (CORAL overlap); overdraft regulatory exposure; sector scorecard row.

---

## Files

| File | Purpose |
|---|---|
| `STATUS.md` | Pre-earnings baseline + Q1 2026 4-test scorecard with placeholder rows. Primary dashboard. |
| `THESIS.md` | Structural view: why we track RF, signals to watch, connection to position names. |
| `EARNINGS_PREP.md` | Q1 2026 forward prep — watch list, consensus, scenarios, checklists. |
| `INDEX.md` | This file — navigation. |

## Subfolders

| Path | Contents |
|---|---|
| `sources/10k_fy2025/` | FY2025 10-K (EDGAR 0001281761-26-000019, filed 2026-02-24) |
| `sources/q4_2025/` | Q4 2025 press release, supplement, deck (8-K 0001281761-26-000006, filed 2026-01-16) |
| `research/` | Research outputs (empty — populate as needed post-earnings) |

## Cross-References

- **Parent STATUS:** `../STATUS.md` — RF sector scorecard row
- **Cohort comparisons:** `../CFG/`, `../MTB/`, `../PNC/` (all Q1 2026 non-position reporters)
- **Position read-through:** `../WAL/`, `../OZK/` (Apr 21 earnings)
- **Sub-agent intel:** 
  - `../../CORAL/STATUS.md` — FL condo/HOA overlap (RF has 270 FL branches, 21.6% of network)
  - `../../CARL/STATUS.md` — consumer credit transmission (RF is leading indicator with 34% consumer book)
- **Cross-agent:** CFPB overdraft rule tracking (LIQUID / regulatory), CORAL (FL specific)

## Maintenance Rules

- Update `STATUS.md` at each RF earnings cycle — don't accumulate history, replace the snapshot. Archive old snapshots into `research/` if needed for longitudinal study.
- Update `THESIS.md` only when structural view shifts.
- Update `EARNINGS_PREP.md` in the 2 weeks before each earnings release.
- Keep `sources/` organized by fiscal period — never flat.
