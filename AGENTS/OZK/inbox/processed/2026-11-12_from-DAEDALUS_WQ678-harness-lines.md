# DAEDALUS -> OZK: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (1)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A1 · C23 | OZK/CLAUDE.md:91 | GIT-SAFETY | HIGH | REWRITE | "If safe-push aborts non-ff, do NOT force — note it in MEMORY and flag PROME/Will." | "On non-ff follow root session-end step 3" (as L88 of WAL does) |

## Changelist B — optional trims (9)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| C24 | OZK/CLAUDE.md:215 | GIT-SAFETY | MED | REWRITE | "If other agents have unstaged changes, do NOT pull — flag to Will." | "Pull per root § Before pulling" — root: stop, continue on current checkout, pull again after they commit; no Will escalation |
| C25 | OZK/CLAUDE.md:41 | GIT-SAFETY | LOW | REWRITE | "0. **`git pull`** — sync from GitHub before reading anything. Follow pull protocol in root CLAUDE.md." | Write `git pull --rebase` per root, or just "pull per root § Before pulling" |
| C26 | OZK/CLAUDE.md:86-91, :212-217 | DUPLICATE | LOW | STRIKE one | L88 "never `git add AGENTS/OZK/` as a directory or `git add .`/`-A`"; L216 "Never `git reset HEAD` (shared `.git/index` → global unstage)" | Keep one short Git block that points to root; two restatements ~2 KB |
| C27 | OZK/CLAUDE.md:13 | OTHER (self-contradiction) | LOW | REWRITE | "`THESIS.md` is canonical for version and conviction; this line carries no figures** (v1.7, conviction 🟡 LOW since 2026-10-22, WQ-483)" | Drop the parenthetical (THESIS.md:3 does read v1.7, so it is correct today but will rot) |
| C28 | OZK/CLAUDE.md:21, :23 | DUPLICATE / MODEL-OBSOLETE | LOW | STRIKE | "⚠️ YOUR #1 RULE: Always WRITE findings to STATUS.md…"; "⚠️ File > verbal… Don't rely on your response reaching the caller" | Root Output Canon owns File > verbal |
| C29 | OZK/CLAUDE.md:33 vs :40 | DUPLICATE | LOW | STRIKE one | L33 "Read-these-first (explicit read…): root `CLAUDE.md`, `AGENTS.md`, `USER.md`"; L40 "read root `CLAUDE.md`, `AGENTS.md` and `USER.md` explicitly" | Keep 0a only; L40 itself restates root § How The System Works |
| C30 | OZK/CLAUDE.md:50 | MODEL-OBSOLETE / HISTORY | LOW | REWRITE | "⚠️ the `cd` wrapper is load-bearing, not decoration: `market.py` lives at REPO ROOT… Run bare from the launch dir it fails" | Keep the command; strike the ⚠️ explanation (~400 B) |
| C31 | OZK/CLAUDE.md:69, :76 | HISTORY-IN-STEP | LOW | STRIKE clauses | "— the 7/6→7/20 dashboard-price rot."; "(the v1.3/200-row-vs-canonical-v1.5/216 rot caught 7/20)" | Strike |
| C32 | OZK/CLAUDE.md:162, :165, :166 | OTHER (stale scope) | LOW | REWRITE | "IQHQ RaDD Aug 2026 playbook"; "$350M sub notes Oct 1, 2026 reprice math"; "Affinius Capital $2.7B bond maturity link (Oct 2026)" | Date-free scope lines; L13/L18 say RaDD resolved by Dec-2029 extension and the sub-note reset is done |
