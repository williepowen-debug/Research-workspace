# DAEDALUS -> VIOLET: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (1)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A15 · M66 | VIOLET/CLAUDE.md:183, :185-194 | RUNTIME | HIGH | REWRITE | "republish by passing **`url=<the artifact's existing URL>`** to the Artifact tool. A session that did not publish it otherwise mints a new URL" | Add nothing new; shorten to "Republish to the existing URL (needs the Claude Artifact tool; without it, edit the HTML and flag the republish as owed)" — or drop the trigger list and the provenance (L187, L194) to net shorter |

## Changelist B — optional trims (12)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| M67 | VIOLET/CLAUDE.md:170 vs :104 | TRADE / OTHER (internal contradiction) | MED | REWRITE | L170 "`TRADE.md` \| VIX-linked positions, vehicles, sizing, live decision frameworks" vs L104 "Position sizing → TERRY" | Drop "sizing" from L170 |
| M68 | VIOLET/CLAUDE.md:53, :106, :122 | ROUTING | MED | REWRITE | L122 "Delivery mechanism: … NEXUS_BRIEF CROSS-DOMAIN (primary, every session); `outbox/` signal file only for 🔴-acute" | "Signals (L116-120 triggers) → WALTER; synthesis → NEXUS_BRIEF." |
| M69 | VIOLET/CLAUDE.md:54 | RUNTIME / CARVE-OUT | MED | REWRITE | "auto-memory (`~/.claude/projects/-home-willi-Research-workspace/memory/` …) … auto-memory loads at every boot via the harness" | Name `memory/auto/` and "self-commit it (carve-out ③)"; drop the auto-load claim |
| M70 | VIOLET/CLAUDE.md:63 | GIT-SAFETY / DUPLICATE | MED | REWRITE | "non-ff → `git pull --rebase`, never force" | "Commit per root Git Protocol (pathspec `AGENTS/VIOLET/`); push via `scripts/safe-push.sh`." |
| M71 | VIOLET/CLAUDE.md:52 | HISTORY-IN-STEP | MED | REWRITE | "Re-pointed 2026-09-06 on Will's direct approval — PROME flagged it as a consumer of the spec re-key, but a `CLAUDE.md` edit needs the operator's own word" | Keep the action (dated memo to `PROME/inbox/`, COMPLETION block, method 2, self-commit under carve-out ①); strike the ~1.2 KB parenthetical → MAINTENANCE.md |
| M72 | VIOLET/CLAUDE.md:53 | HISTORY-IN-STEP / DUPLICATE | MED | REWRITE | "Why this is an ORDERING rule and not a reminder to refresh: the 7/31 fleet audit found 5-of-5 content-stale briefs" | "Fold NEXUS_BRIEF last (after the final STATUS write); As-of + STATUS hash minimum." Story lives in NEXUS schema L107 |
| M73 | VIOLET/CLAUDE.md:46, :47, :61 | HISTORY-IN-STEP / MECHANIZED | MED | REWRITE | L47 "this line used to say "validate enums against `workbook/SCHEMA.tsv`" and was a ritual with no mechanism, performed as often as someone remembered, i.e. never" | L46 → "…regime status, positions, `## BOTTOM LINE`"; L47 → "enums enforced by `validate_workbook.py` (boot); read its verdict"; L61 → "rc=1 at closeout = not finished: fix or record why on the surface" (~1.8 KB saved) |
| M74 | VIOLET/CLAUDE.md:49 | STALE-INVOKER (uncertain) | LOW | — (verify) | "`scripts/forward_calendar_check.py` blocks the closeout guard and packets PROME when the window is empty (DOCKET L667" | If WQ-578's retired "handwritten-calendar coverage" check is this one, strike the sentence and its `closeout_guard.py` L115 entry; else KEEP |
| M75 | VIOLET/CLAUDE.md:69, :71 | DUPLICATE / MODEL-OBSOLETE | LOW | STRIKE | "⚠️ Critical: Always WRITE to STATUS.md / SCRATCH.md / KB.tsv. Do not just report findings back verbally." | Strike both (root File > verbal; step 8 already says log to workbook) |
| M76 | VIOLET/CLAUDE.md:21 | GIT-SAFETY | LOW | REWRITE | "`git pull` — sync from GitHub before reading anything. Follow pull protocol in root CLAUDE.md." | "Pull per root (`git pull --rebase`)." |
| M77 | VIOLET/CLAUDE.md:18, :24, :35, :40, :65, :187, :194, :196, :200 | HISTORY-IN-STEP | LOW | REWRITE | L196 "Its archive copy was deleted with the whole `VIOLET/archive/` dir in the 2026-06 public-prep prune" | Strike dated provenance; keep commands and rules (~1.5 KB saved) |
| M78 | VIOLET/CLAUDE.md:138-148 | DUPLICATE | LOW | STRIKE | "5-point scoring scale (universal across all agents)" | Cite the blueprint (`AGENTS/DAEDALUS/BLUEPRINTS/market-agent.md`) |
