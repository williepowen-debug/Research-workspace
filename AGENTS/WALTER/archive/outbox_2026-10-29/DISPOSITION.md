# Outbox >30-day disposition — 2026-10-29 (WALTER, repairs batch on Will's "Lets work on these next")

Rule applied: root CLAUDE.md § Data Hygiene research/sources retirement — move only a file >60 days old AND not boot-read AND not referenced by a live doc; immutable BOARD cards and filed receipts that cite a path are live references (moving would break them).

| Files (outbox/) | Count | Disposition | Why |
|---|---|---|---|
| 2026-08-28_to-DAEDALUS_P1-read-cap-measured-live-cost.md | 1 | **ARCHIVED here (git mv)** | 62 days; read-only draft whose P1 read-cap work landed as AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md canon; no live reference found (grep over WALTER, PROME, BOARD, DAEDALUS, docs excluding history/archive/research). |
| VERIFY-20260831-iran-weekend-claims.md | 1 | KEEP in place | Cited by BOARD SIG-W-20260831-001/-002 and a PROME processed doorbell; 59 days. |
| 2026-09-08_* (Codex owner catch-up session evidence) | 31 | KEEP in place | 51 days; cited by PROME processed completion packets, BOARD SIG-W-20260908-003/-004/-009/-019, kill_log, design/STATE.md and BOARD_INDEX_GENERATION_DESIGN.md. Misfiled as outbox (session evidence, not packets) but path-cited; do not move. |
| 2026-09-14_boundary-6-8-month-basis-RECOMMENDATION-to-Will.md | 1 | KEEP in place | Ruled 10/09; cited by BOARD SIG-W-20261009-008 and ROUTING_OVERLAYS "the outbox decision record". |
| 2026-09-15_boot-assessment.md | 1 | KEEP in place | 44 days; under the 60-day line. Re-check after 11/14. |
| 2026-09-21_verdict-letter-FALSE-vs-UNSUPPORTED-PROPOSAL-to-Will.md | 1 | KEEP in place | Live open design item (verdict-letter F1/F2, LAST_COMPLETION OPEN DESIGN DECISIONS). |

Total 36 (the earlier "34" was a stale count). Going forward: session evidence belongs in research/<date>_<slug>/, not outbox/.
