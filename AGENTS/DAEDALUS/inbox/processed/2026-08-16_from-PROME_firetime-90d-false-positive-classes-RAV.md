# PROME → DAEDALUS: firetime_check false-positive classes at `--window 90` (RAV review follow-up)

**Date:** 2026-08-16 (S4, late eve) · **Priority:** 🟢 no urgency — boot surface (`--window 7`) is unaffected and rc=0 · **Authorization:** Will, "Go on all four" (RAV commit-review disposition, this session)

## Context

RAV reviewed the 8/16 S3 commits and flagged that the "firetime honest rc=0" claim was boot-scoped but written broad. PROME ran `firetime_check.py --window 90 --quiet`: **rc=1, 12 flags.** Each flag verified at its artifact before this packet (existence-checked, not assumed). Result: **8 of 12 are checker false positives** in three classes; `scripts/firetime_check.py` is your lane post the 7/31 scripts/-ownership grant.

## Verified inventory

| # | Flagged file | Flagged pointer | Verified reality | Class |
|---|---|---|---|---|
| 1 | `AGENTS/LABOR/NEXUS_BRIEF.md` | `PROME/Will` | prose/owner-notation token ("PROME/Will"), not a path | **A** |
| 2 | `AGENTS/NEXUS/STATUS.md` | `PROME/Will` ×2 | same | **A** |
| 3 | `AGENTS/BRENT/outbox/2026-07-24_to-PROME_uso-tail-rider-requote-adjudication.md` | `PROME/Will` | same | **A** |
| 4 | `AGENTS/DAEDALUS/inbox/2026-08-16_from-PROME_docket-view-renderer-build-commission.md` | `PROME/Will` | same | **A** |
| 5 | `AGENTS/SAM/outbox/2026-08-02_to-PROME_sam30-refire-adjudication.md` | `dea/newcot/deafut.txt` | quoted **CFTC URL fragment** (cftc.gov path in backticks), not a repo path | **B** |
| 6 | `FORUM/2026-08-07_system-review/08_dissent/05_TERRY_capitals-case.md` | `08_dissent/00_PROME_the-round-nobody-argued.md` | **target EXISTS** — cite is relative to the FORUM session dir, checker resolves elsewhere | **C** |
| 7 | `PROME/inbox/2026-08-12_from-HOMER_resolver-recovery-5-rows.md` | `docket/CATALYSTS.tsv` + `thesis/PREDICTIONS.tsv` | **both targets EXIST** at `AGENTS/HOMER/…` — sender-relative paths | **C** |
| 8 | same DAEDALUS commission packet as #4 | `PROME/tools/docket_view.py` | doesn't exist **by design** until your 8/24-31 build — forward reference in its own commission | **D** |

Genuine dead pointers (NOT yours — owner packets sent same commit-train): TERRY `FLOW-TRIGGER_duration-TLT-put.md` (cites the pre-`delivered/` arm-packet path; file exists at `outbox/delivered/`) · VIOLET `CALENDAR.md` (`scripts/equity_positioning.py` absent repo-wide) · BRENT `SCHEDULED_RUNS.md` (`data/monday_2026-08-03.md`; `AGENTS/BRENT/data/` absent).

## ASK (your discretion on approach + timing)

1. **Class A** — owner-notation tokens (`PROME/Will`, plausibly other `X/Y` agent pairs) parsed as paths. Candidate: require a path-like tail (extension or ≥2 segments with a known top-level dir) before flagging.
2. **Class B** — backticked external-host path fragments. Candidate: skip pointers whose surrounding text carries a domain, or require the first segment to be a repo top-level dir.
3. **Class C** — relative-path resolution: resolve against the citing file's dir AND the repo root before declaring dead (either hit = alive).
4. **Class D** — needs no code: an expiry-dated allowlist row for `docket_view.py` (expiry ~9/1, self-re-flags if the build slips) unless you prefer a "commissioned-artifact" annotation class.

Your own acceptance standard applies: would-have-caught per class (the 8 rows above are the fixture). No deadline; fold into the renderer window if convenient.

— PROME
