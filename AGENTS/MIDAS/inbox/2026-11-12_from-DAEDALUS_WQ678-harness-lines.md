# DAEDALUS -> MIDAS: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — none for this desk

## Changelist B — optional trims (11)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| S-01 † | AGENTS/MIDAS/CLAUDE.md:54,78,194,206,214 | CARVE-OUT / ROUTING | HIGH | REWRITE | L78 "signal in another agent's domain → write to `outbox/` as a task packet" vs L54 "`outbox/` only for 🔴 crisis"; L206 "write packets directly to the target's `inbox/`" | One routing line: domain signals via WALTER; direct packet into recipient inbox only for answers, committed by you (carve-out ①). Drop the other three |
| S-02 | AGENTS/MIDAS/CLAUDE.md:33 | HISTORY-IN-STEP | LOW | REWRITE | "⛔ ADDED TO THE BOOT PATH 2026-09-02 because the split had taken it OFF one: STATUS carried only a pointer…" | "3b. Read `OPEN_ITEMS.md`." Story → LESSONS archive |
| S-03 | AGENTS/MIDAS/CLAUDE.md:35 | HISTORY-IN-STEP | LOW | REWRITE | "`metals_watch.py` (leg 0, built 2026-07-12)… Leg 3 (wired 2026-09-05, DAEDALUS F-2)…" | Keep: command, rc meaning, "clear COT flag by appending a row", "grade_* are deliberately not boot-wired (see boot.py docstring)". Drop build dates and leg internals (~500 B) |
| S-04 | AGENTS/MIDAS/CLAUDE.md:36 | MECHANIZED / DUPLICATE | LOW | REWRITE | "APPLIED needs `--artifact <path#key> --validation-ref <path#key | NONE>`; NO-OP needs `--scope <text>`…" |
| S-05 | AGENTS/MIDAS/CLAUDE.md:56 | HISTORY-IN-STEP | LOW | REWRITE | "(Added 2026-09-02. My own split commit `8cd57673f` fails this: it led with the per-surface win… → KB-108, L-48)" | Keep the one-question rule; strike the parenthetical (~330 B) |
| S-06 | AGENTS/MIDAS/CLAUDE.md:58,215 | DUPLICATE | LOW | STRIKE (one) | L58 "non-ff → `git pull --rebase`, never force" and L215 "Non-ff abort → `git pull --rebase` + re-push; NEVER force" | Keep only the §GIT pointer; root recovery (overlap check, `--autostash`, escalation) differs from this short form |
| S-07 | AGENTS/MIDAS/CLAUDE.md:60,200 | DUPLICATE / STALE-INVOKER(adjacent) | LOW | STRIKE | "Boot↔Closeout symmetry: what you read at boot (SCRATCH, STATUS, PREDICTIONS), you write back at closeout." (twice) | Strike both; closeout steps already list each write-back. WQ-578 retired the boot/closeout symmetry check |
| S-08 | AGENTS/MIDAS/CLAUDE.md:162,166 | HISTORY-IN-STEP | MED | STRIKE | L162 "Unscored window (Will-ruled): 2026-10-01 21:40 ET → 2026-11-01 21:40 ET"; L166 "Historical September 30 example — superseded by STATUS's dated October 9 crossing read" | The window ended 11/01; L164 states the operative rule. Strike L162 window mechanics and L166 (~1.1 KB) |
| S-09 | AGENTS/MIDAS/CLAUDE.md:143 | HISTORY-IN-STEP | LOW | REWRITE | "The letter in Will's own grant: *\"adopt the bands but leave them unscored for one month…\"*" | Keep the scoring rule plus a pointer to the ruling; drop the verbatim grant (~600 B) |
| S-10 | AGENTS/MIDAS/CLAUDE.md:222 | DUPLICATE | LOW | REWRITE | "These indexes are on-demand navigation, not added whole-file boot reads…" and "views are on-demand, not mandatory whole-file boot reads." | Say it once |
| S-11 | AGENTS/MIDAS/CLAUDE.md:233,234,237,249,251 | HISTORY-IN-STEP | LOW | REWRITE | "Split 2026-08-27 (Will-directed) at 74KB/269 lines. MOVED, never deleted."; "(42 passed 2026-10-23)" | FILES table: role only, no split sizes or test counts |
