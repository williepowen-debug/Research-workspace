# BRENT file-integrity sweep — 2026-10-04

**Run:** 21:5x–22:21 ET · **Scope:** BRENT-owned current surfaces, maintained ledgers, local readers/tests, Markdown links, dated handoffs and operational debt. This was an integrity sweep, not a new market-data refresh.

## Outcome

| Class | Finding | Disposition |
|---|---|---|
| **FIXED** | `scripts/eia_weekly.py --local` falsely reported the complete saved wk-9/25 EIA report as incomplete. The autonomous report writer had used a natural-language heading and newer row labels the reader did not accept. | Parser now accepts both saved shapes; all required values reproduce. Regression test added. No EIA value changed. |
| **FIXED** | 9 broken relative Markdown links: one `RULINGS.md` line pointer and eight links in historical `workbook/*archive*.md` files. | Repaired; hot-surface + workbook scan now reports **183 checked, 0 broken**. |
| **FIXED** | `STATUS.md` still presented a 10/2 summary that previewed the already-graded 10/4 OPEC+ decision; `NEXUS_BRIEF.md` still named that decision as next. | Old summary rotated verbatim with byte/CRC receipt; current STATUS/NEXUS/SCRATCH/TRACKER re-stamped. |
| **CLEAN** | Python integrity suite; correction/calendar/position-agreement checks; prediction-due and execution-receipt scans; lesson prose/index structure; maintained TSV schemas and key uniqueness. | No actionable break found. Exact closeout results are in the validation section below. |
| **OPEN — incidents** | 4 `ACTIVE` incident rows are more than 60 days old: RF-013 Ufa, RF-014 Mina Al-Ahmadi, RF-022 Tuapse and RF-033 VTTI Fujairah. Nine old `PARTIAL_RESTART`/`MONITORING`/`DISPUTED` rows still use present-tense states: RF-005, 008, 010, 018, 031, 037, 038, 040 and 041. | Kept visible; no status was changed without new evidence. |
| **OPEN — incident coverage** | The ledger header admits the 8/11–12 Novorossiysk/Sheskharis gap. Current notes also still owe distinct successor events for Kirishi 8/30, NORSI 8/26, Perm 8/21 and 9/25, Ryazan 9/6, Jazan 8/18 and 9/7–8, plus older RU coverage holes. | Evidence work required before rows can be added. The 10/2 Kuibyshev and Volgograd additions do not close these separate events. |
| **OPEN — frozen historical ledger** | Frozen [`../../workbook/KB.tsv`](../../workbook/KB.tsv) rows KB-BRT-109, KB-BRT-114 and KB-BRT-117 have 14 fields against a 13-field header because of an extra blank column. | **Not edited:** local rules prohibit writes to the frozen KB. Defect is documented here rather than silently normalized. |
| **OPEN — clock** | [`../../workbook/LESSONS_INDEX.tsv`](../../workbook/LESSONS_INDEX.tsv) is 10 days behind STATUS by the staleness tool. Its own header defines `last_verified` as prose/index reconciliation, not external-data freshness. | No blind date-stamp. Semantic/prose checks pass 27/27; perform a genuine reconciliation before updating the clock. |
| **OPEN — positions** | BRENT/TRADE and FORGE agree on their recorded state, but the last broker capture is 10/1. USO Oct-09 $150C ×1 and VLO ×1 need live broker truth. | Confirm Monday; do not infer no fills from the absence of a receipt. |
| **OPEN — routines** | Four routines were installed 10/2. First-live-run acceptance remains pending for 10/8, 10/9 and 10/14–15; the Thursday routine still has six default connectors to remove in the UI; DST reset is due 11/1. | Operational acceptance debt, not yet a missed run. |
| **OPEN — evidence hygiene** | `outbox/` retains 17 September 8 `.txt/.json` check artifacts; two are explicitly cited from the market-docket owner-read note and the rest are largely unreferenced. | Retained. Moving or deleting evidence was outside this sweep and could break provenance. |
| **OPEN — chronology audit** | The scoped claim checker leaves four real weekday/date advisories in TRACKER's unattended historical table: three instances of “Mon Jul 7” and one “Jul 21 Mon.” It also emits 17 hash advisories on CRC receipts or externally scoped identifiers that resemble commit hashes. | Do not rewrite historical event dates from a weekday linter alone. Reconcile those rows to their source reports before correcting either the date or weekday. |
| **OPEN — archived navigation** | A deliberately broad recursive Markdown scan finds **486 unresolved local targets among 940 links in 123 linked files**. Most are relative-path drift inside moved archive/evidence files (for example, an archived STATUS still points to `research/...` as though it were at the BRENT root). | Current/hot surfaces and `workbook/` archives are clean. Repair the deeper archive corpus as a separate mechanical migration with before/after link receipts; do not mix it into market-state edits. |

## Notes on age and network checks

- A commit-age scan surfaced 39 files older than 60 days. They were frozen records, historical evidence, static specifications/receipts, or still-linked material. File age alone is not evidence of stale content, so no bulk retirement was performed.
- The full-tree claim checker emits 2,488 raw advisories across 1,116 files because it includes frozen archives/evidence and treats CRCs, external identifiers and many backtick paths as claims. That raw count is not a defect count. A current-surface rerun eliminated every pointer advisory and leaves the 17 identifier-shaped hash advisories plus four historical weekday/date items classified above.
- A sandboxed instrument probe failed DNS. That is **non-evidence about source health**. The earlier networked boot in this same session reached the live feeds except the closed-market/stale tanker-liveness path.
- The catalyst docket has 25 rows. Recently graded rows remain inside the one-week retention rule; no safe pruning was due.

## Validation

Closeout should reproduce:

- `python -m unittest discover`: **67 tests, pass**.
- `eia_weekly.py --local`: complete saved report, week ending 2026-09-25 / released 2026-09-30.
- Hot-surface + workbook Markdown links: **183 checked, 0 broken**. Full recursive archive result remains the open debt above.
- Catalyst generated view: matches the 25-row docket.
- Corrections, prediction-due, pending-receipt, lesson and position-agreement checks: clean within their stated scope. The scoped claim check has the 21 classified advisories above; it is not represented as clean.

## Priority order

1. Confirm broker truth Monday before treating the 10/1 position mirror as current.
2. Re-verify the four aged `ACTIVE` incident rows, then the nine aged present-tense rows.
3. Fill incident successor gaps only from counting evidence.
4. Observe the first scheduled runs and remove the six default Thursday connectors.
5. Reconcile `LESSONS_INDEX.tsv` substantively; do not date-launder it.
