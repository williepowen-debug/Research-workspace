# REGINALD retirement moves — 2026-10-22 ~14:1x ET

**Authority:** Will, REGINALD session. 14:09 ET: "Can you handle #4 the old clutter now?" 14:11 ET: "yes I don't care about waiting for 11/20 that seems silly". This lifts the 10/20 cleanup hold on moves (charter line 5 updated). **Rule applied:** root CLAUDE.md Data Hygiene retirement. A file moves only if it is >60 days old AND not boot-read AND not referenced by a live analytical/protocol doc (boot files, TRADE/POSITIONS, matrix, NEXUS brief, research standard, cold STATUS/ROADMAP satellites, SCRATCH, SUB_AGENTS, registry/NOTES, scripts). All moves are `git mv` (history kept); nothing was deleted.

| Moved | From → to | Last commit | Live references | Note |
|---|---|---|---|---|
| ARCH_REPORT_2026-06-26.md | root → `archive/root_retired_2026-10-22/` | 2026-06-26 | none | 13 historical refs elsewhere left as-is |
| CONVERGENCE_RESCALE.md | same | 2026-07-09 | none | eight-channel era |
| CLEANUP_PLAN.md | same | 2026-07-09 | none | superseded by the 10/20 cleanup |
| INBOX.md · OUTBOX.md | same | 2026-07-09 | none | FROZEN HERMES relics (HERMES retired) |
| OPEN_THREADS_2026-07-09.md | same | 2026-07-16 | none | threads closed 9/02 and 10/10 |
| MAY15_DECISIONS.md | same | 2026-07-17 | LESSONS.md "Last reviewed" note only | Path in LESSONS updated in the same commit |
| `MTB/` (6 tracked files + ignored `sources/` PDFs) | → `archive/per-bank/MTB/` | content 2026-04-15 (FROZEN banner added 10/22) | none (no path reference in any live doc) | Joins the CFG/EGBN/FITB/PNC/RF/ZION per-bank archive. Current M&T work → `reports/2026-10-20_MTB_earnings-capacity_and_capital-test.md` |
| 19 outbox packets dated 2026-07-16 → 2026-08-23 | `outbox/` → `archive/outbox_2026-07-16_to_2026-08-23/` | ≤ 2026-08-23 | none | Sender-side copies. Delivery of each is NOT asserted by this move |

**Not moved (rule not met):** the 13 outbox packets dated 2026-08-27 → 2026-10-13 (<60 days old). They stay in `outbox/` until each passes 60 days.

**Known effect:** older reports and peer files that cite the moved paths by their old location now point at a moved file. Those are historical citations, which the root rule does not protect. Find the new home here.
