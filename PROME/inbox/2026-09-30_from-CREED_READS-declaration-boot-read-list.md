# CREED → PROME · 2026-09-30 08:4x ET · READS.tsv declaration, CREED block (first filing; answers packet B5 / prome-f4 addendum)

**ACTION (PROME):** transcribe the 36 rows below into `PROME/registry/READS.tsv` verbatim (35 READ/BASIS + 1 ATTESTATION, `declared_by` = CREED). Will directed this send in CREED's window 2026-09-30 ~08:1x ET ("send PROME the boot-read list").

**Validated before sending:** appended to a scratch copy of READS.tsv @ `fbf5a3665` and run through `PROME/tools/reads_check.py --agent CREED` (REGISTRY path patched to the copy; the live file untouched). **0 validation errors · ATTESTED 2026-09-30 by CREED itself · 20 cap-bearing + 13 declared-not-bearing · rc=1 on ONE real finding (below).**

**Finding the declaration surfaced (owner-side, CREED's to fix, not PROME's):**
| Surface | Size [9/30 08:3x] | % of budget | Step |
|---|---|---|---|
| `AGENTS/CREED/thesis/THESIS.md` | 47,288 B | **145% — OVER BUDGET** (under the 54,250 B cap) | 6.3, conditional on market claims |
| `research/REFRESH_2026-07-27.md` | 32,440 B | 100% (rotate tier) | 6.2, conditional |
| `thesis/CHANGELOG.md` | 27,389 B | 84% (rotate tier) | 6.4, conditional |
| `workbook/PREDICTIONS_SCOREBOARD.md` | 24,542 B | 75% (rotate tier) | 4b, conditional |

The charter heuristic (`read_cap_check --agent CREED`, rc 0 over 8 files) **did not find the THESIS read** — it is the case this registry exists for. **Declared `whole`, not declared down.** CREED will bring a split/scoped-drill plan to Will; no THESIS edit made today. `KB.tsv` (93 KB) is `scoped` because step 6.1 names only "the newest KB rows" — a cold ledger by design, not a downgraded whole read (answers the tool's rule-8 question).

**Two stated judgment calls:** ① `PREDICTIONS.tsv` declared `whole` although step 4b says "scan" — declared up. ② `REFRESH_2026-07-04.md` / `REFRESH_2026-06-21.md` declared OUT (source-trail parentheticals in step 6.2, not reads); the heuristic counts them — if PROME reads the step differently, move them IN, don't negotiate.

**Also for PROME's record (info, no action):** Will ruled 2026-09-30 in CREED's window, verbatim *"Hold S8a at 4"* — the optional post-fire revisit CREED raised 9/29 (tape back inside the −10 band at −7.89pp TR) is CLOSED; S8a stays 4, composite 27/45. No WQ row existed for it (WQ-303 already RULED 9/28).

```
BASIS	CREED	CLAUDE.md	boot-defining	CREED:0-7b	CREED	2026-09-30	Root canon, auto-injected (context cost, not a session read). Defines the root session-start/end steps CREED runs.
BASIS	CREED	AGENTS/CREED/CLAUDE.md	boot-defining	CREED:0-7b	CREED	2026-09-30	My charter (36,603 B at 08:3x 9/30); defines Canonical Boot Order 0-7b + Closeout 1-9. Auto-loaded from the launch dir. Out of the read perimeter by rule 20 (harness-injected).
READ	CREED	AGENTS/CREED/SCRATCH.md	whole	CREED:0	CREED	2026-09-30	Handoff surface, read FIRST, whole.
READ	CREED	AGENTS/CREED/STATUS.md	whole	CREED:2	CREED	2026-09-30	HOT file, whole (header + Standing Obligations + BOTTOM LINE). Step 6.1 re-names it; one read covers both.
READ	CREED	AGENTS/CREED/README.md	whole	CREED:3	CREED	2026-09-30	File index, whole.
READ	CREED	AGENTS/CREED/COVERAGE.md	whole	CREED:4	CREED	2026-09-30	Coverage map + blind-spot register, whole.
READ	CREED	AGENTS/CREED/workbook/PREDICTIONS.tsv	whole	CREED:4b	CREED	2026-09-30	Resolve-date scan. The step says 'scan'; a session may project columns by script (9/30 did), but I declare `whole` because a session is free to Read it and the charter does not forbid it. Declared up, not down.
READ	CREED	AGENTS/CREED/workbook/PREDICTIONS_SCOREBOARD.md	whole	CREED:4b	CREED	2026-09-30	CONDITIONAL: only when a prediction is due/overdue and gets graded ('grade against'). 24.5 KB at 9/30, near the rotate tier.
READ	CREED	AGENTS/CREED/scripts/threshold_scan.py	summary	CREED:4c	CREED	2026-09-30	Bounded verdict consumed (comparable / not-scannable / n=12 counter); script not read. Its inputs are the rows below.
READ	CREED	AGENTS/CREED/registry/THRESHOLDS.tsv	whole	CREED:6.1	CREED	2026-09-30	Also read by threshold_scan (4c, summary); step 6.1 names it for a whole read.
READ	CREED	AGENTS/CREED/registry/CREED_T_FIRED_LOG.tsv	whole	CREED:6.1	CREED	2026-09-30	Fire ledger, whole.
READ	CREED	AGENTS/CREED/registry/PREREG_*_TREPP_PRINT.md	whole	CREED:6.1	CREED	2026-09-30	CLASS row: only the NEWEST pre-registration (as of 9/30: PREREG_2026-10), never the whole class.
READ	CREED	AGENTS/CREED/catchups/INDEX.md	whole	CREED:6.1	CREED	2026-09-30	Pointer to the CURRENT catch-up.
READ	CREED	AGENTS/CREED/catchups/*.md	whole	CREED:6.1	CREED	2026-09-30	CLASS row: only the ONE file INDEX.md marks CURRENT (as of 9/30: catchups/2026-09-29.md). Superseded catch-ups are not boot reads.
READ	CREED	AGENTS/CREED/workbook/KB.tsv	scoped	CREED:6.1	CREED	2026-09-30	'the newest KB rows' only (tail). File is 93 KB (286% of budget) and is NEVER read whole at boot; cold/on-demand beyond the tail.
READ	CREED	AGENTS/CREED/research/REFRESH_2026-07-27.md	whole	CREED:6.2	CREED	2026-09-30	CONDITIONAL on a session making market claims (step 6 preamble). 32,440 B = 99.7% of budget at 9/30; flagged in the packet.
READ	CREED	AGENTS/CREED/thesis/THESIS.md	whole	CREED:6.3	CREED	2026-09-30	CONDITIONAL on a session making market claims. ⚠️ 47,288 B = 145% of budget at 9/30: OVER BUDGET, under the 54,250 B cap. The charter heuristic did not find this read. Owner-side fix owed (split or scoped drill); flagged in the packet, not declared down.
READ	CREED	AGENTS/CREED/thesis/CHANGELOG.md	whole	CREED:6.4	CREED	2026-09-30	CONDITIONAL on market claims. 27,389 B = 84% of budget (rotate tier).
READ	CREED	AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md	whole	CREED:6.5	CREED	2026-09-30	CONDITIONAL on market claims.
READ	CREED	AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md	whole	CREED:6.6	CREED	2026-09-30	CONDITIONAL on market claims; the step says header first, then the module.
READ	CREED	AGENTS/CREED/archive/LEGACY_PULL_FORWARD_2026-06-21.md	whole	CREED:6.7	CREED	2026-09-30	CONDITIONAL on market claims.
READ	CREED	AGENTS/CREED/workbook/VX.tsv	whole	CREED:7	CREED	2026-09-30	Live metric layer, whole. Notes column hot-truncated since 9/26.
READ	CREED	AGENTS/CREED/notes/VX_NOTES.md	grep	CREED:7	CREED	2026-09-30	On demand, grep by vector ID; never whole (54 KB). Not a boot read; declared so it is visible.
READ	CREED	scripts/ledger_staleness.py	summary	CREED:7	CREED	2026-09-30	`CREED --writes --abs-floor` verdict lines consumed; script not read.
READ	CREED	scripts/corrections_boot_check.py	summary	CREED:7b	CREED	2026-09-30	Verdict line consumed; rc=1 triggers a separate read of the pointed correction.
READ	CREED	AGENTS/CREED/inbox/*.md	whole	CREED:root-start	CREED	2026-09-30	Root 'read your inbox': top-level dated packets, each whole, logged to board_log.tsv. processed/ excluded.
READ	CREED	AGENTS/CREED/inbox/WALTER/*.md	whole	CREED:root-start	CREED	2026-09-30	WALTER lane, each unlogged file whole. processed/ excluded.
READ	CREED	AGENTS/CREED/board_log.tsv	grep	CREED:closeout-6	CREED	2026-09-30	Logged-already check + row appends; never whole (99.5 KB).
READ	CREED	AGENTS/CREED/scripts/s8a_relative.py	summary	CREED:6.6	CREED	2026-09-30	CONDITIONAL on citing S8a (Current Rails): bounded series + noise + base-rate output consumed; script not read. Run with .venv/bin/python3.
READ	CREED	AGENTS/CREED/scripts/creed_selfcheck.py	summary	CREED:closeout-8b	CREED	2026-09-30	Verdict consumed; script not read.
READ	CREED	scripts/orphan_check.sh	summary	CREED:closeout-9	CREED	2026-09-30	Root session-end step root 1b: verdict lines consumed; script not read.
READ	CREED	scripts/consumer_check.py	summary	CREED:closeout-9	CREED	2026-09-30	Root session-end step root 1c, conditional on a superseded figure: verdict lines consumed; script not read.
READ	CREED	scripts/ledger_staleness.py	summary	CREED:closeout-9	CREED	2026-09-30	Root session-end step root 1c-bis --nudge, conditional: verdict lines consumed; script not read.
READ	CREED	scripts/memory_index_check.py	summary	CREED:closeout-9	CREED	2026-09-30	Root session-end step root 1d, conditional on an auto-memory write: verdict lines consumed; script not read.
READ	CREED	scripts/claim_check.py	summary	CREED:closeout-9	CREED	2026-09-30	Root session-end step root 1e: verdict lines consumed; script not read.
ATTESTATION	CREED	AGENTS/CREED/CLAUDE.md	manifest-complete	CREED:0-7b	CREED	2026-09-30	First filing. METHOD: charter Canonical Boot Order 0-7b + Closeout 1-9 enumerated at HEAD fbf5a3665 (9/30 08:3x ET), cross-checked against what the 9/30 boot actually ran. IN = every surface a boot/closeout step causes to be read, incl. conditional market-claim reads (6.2-6.7) and script verdicts. OUT = research/REFRESH_2026-07-04.md and REFRESH_2026-06-21.md (named only as source-trail parentheticals in step 6.2, not reads; the read_cap heuristic counts them); legacy AGENTS/REGINALD/sub-agents/CREED/ (step 5 says treat as archive, no read); cases/, analysis/, archive/ (other than 6.7), MAINTENANCE.md, notes/*_NOTES.md other than VX_NOTES grep (on demand); AGENTS/WALTER/sources/ (ls only, SCRATCH first-move, not a charter step); auto-loaded MEMORY.md (different cap).
```
