# YURI boot check — acceptance before implementation

Authority: YURI CLAUDE.md standing boot-resolution duty. DOMAIN mechanism, read-only; no research, routing or threshold authority changes. Reader: YURI at every boot.

Prior art: searched `memory/auto/MEMORY.md`, `memory/auto/INDEX_COLD.md`, `AGENTS/DAEDALUS/PATTERNS_HOT.md` and the body of `memory/auto/finding_hygiene_commit_rearms_the_staleness_lie.md`; PAT-039/044 and that finding apply. Use content dates, not Git time or mtime. The previously specified `scripts/boot.py` does not exist at this boot.

Acceptance: report OPEN rows whose resolve_by has arrived; report an unreviewed YUR-004 checkpoint using the registered letter's calendar and the row's own review date. Do not use an unrelated ledger refresh to clear that checkpoint. Exclude terminal grades. Missing, malformed or future-dated input returns 2, never a clean verdict. Return 1 for work due, 0 only for no work due inside the stated perimeter. Never grade or mutate a row.

Production acceptance inputs: `AGENTS/YURI/workbook/INTENT_LEDGER.tsv` as at the pre-session HEAD, saved verbatim in `/tmp/yuri-pre-session-intent.tsv`; its baseline reading on 2026-10-02 is the clean case, and the same still-unreviewed reading evaluated on 2026-10-12 is the actual overdue-10/09 case. The registered calendar is `research/2026-10-02_YUR-004_REGISTERED.md` §4. Re-run these cases on material edits. Baseline: 4 rows, 0 overdue final dates, 1 missed weekly checkpoint at 2026-10-12 before this session's review.

Neighbour considerations: ordinary = live ledger before and after review; overlap = a newer file/header without a newer row review cannot clear the checkpoint; wrong owner = default paths resolved relative to this script's YURI directory, not cwd; missing information = missing review date or malformed row fails closed; concurrent activity = read-only, never writes owner or shared state. Additional tests: missing file, malformed date, future review date and due final date.

Implementation and observed results are recorded in the actor-review report. Author tests do not establish independent verification.
