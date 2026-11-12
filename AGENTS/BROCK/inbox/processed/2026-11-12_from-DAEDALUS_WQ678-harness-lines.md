# DAEDALUS -> BROCK: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (1)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A9 · C50 | BROCK/CLAUDE.md:169-171 | TRADE | HIGH | REWRITE | "### 1. Thesis Kill (exit 100% private credit overlay)" | "Thesis Kill (→ TERRY card; Will decides under root rule #5)"; drop "exit 100%" |

## Changelist B — optional trims (10)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| C48 | BROCK/CLAUDE.md:69, :84, :95, :142, :275 | CANON-CONTRADICTION / ROUTING | HIGH | REWRITE | L69 "`outbox/` is only for PROME requests."; L95 "Use your own `outbox/` only to request PROME action." | Root: "Write to `PROME/inbox/` (repo root…) to request Prome action; `AGENTS/<NAME>/outbox/*to-PROME*` files are for signal/routing work." → "PROME requests → root `PROME/inbox/`, self-committed" (one line, replaces five) |
| C49 | BROCK/CLAUDE.md:95 vs :96-105, :220-229 | ROUTING | MED | REWRITE | L95 "SIGNALS (a registered threshold firing…) → WALTER."; L105 (format "for a packet you send direct") "Write a signal when: a threshold fires" | Say once: threshold fires → WALTER; the table names who WALTER should route to; direct packets = analysis only |
| C51 | BROCK/CLAUDE.md:43 | GIT-SAFETY | LOW | REWRITE | "0. **`git pull`** — sync from GitHub before reading anything. Follow pull protocol in root CLAUDE.md." | As C25 |
| C52 | BROCK/CLAUDE.md:173-176 | HISTORY-IN-STEP | LOW | REWRITE | "RE-SPEC'D 2026-09-02 under WQ-106 (Will-ruled 2026-09-01 17:22 ET, \"approve all of those with your recs\"; record…; packet…)" | Keep the two gate bullets (THE kill is `GATE-HY-REKILL`; BROCK's count is confirmation only); drop the ruling quote/record |
| C53 | BROCK/CLAUDE.md:22-30 | HISTORY-IN-STEP | LOW | REWRITE | "Adopted 2026-10-02 from CREED's charter (Will: \"adopt as much as you think is valuable\"). Why here and not only in LESSONS.md…" plus first-person incident per trap | Keep 7 one-line traps; incidents already in LESSONS (cited by number). ~1.5 KB |
| C54 | BROCK/CLAUDE.md:71 | DUPLICATE | LOW | REWRITE | "Use `--slug`, never bare `--strict`: bare `--strict` fails on other desks' orphans… `orphan_check.sh` labels everything under `memory/auto/` `[not yours]` by PATH" | Point to root step 1d / carve-out ③ — it says this verbatim |
| C55 | BROCK/CLAUDE.md:76 vs :128 | DUPLICATE | LOW | STRIKE one | L76 "One source of truth per metric — HENRY owns VIX, LIQUID owns HY OAS, REGINALD owns bank CRE scores."; L128 "(HENRY owns VIX, LIQUID owns HY OAS, REGINALD owns bank CRE scores)" | Keep L128 |
| C56 | BROCK/CLAUDE.md:48, :49, :55, :62, :63, :73, :77 | HISTORY-IN-STEP | LOW | STRIKE clauses | "[T1a, 6/26; tooled 6/27]"; "(cwd-proof form, 2026-07-01)"; "(Wired 2026-08-28…)"; "(SCRATCH had grown to 47 KB…)"; "It was falsified before adoption: v1 missed VX-BRK-004…"; "No historical staging damage was established." | Strike parentheticals; provenance home exists (`CHARTER_PROVENANCE.md`) |
| C57 | BROCK/CLAUDE.md:70 | RUNTIME | LOW | REWRITE | "auto-memory (`~/.claude/projects/-home-willi-Research-workspace/memory/` + one-line index in its `MEMORY.md`)" | Name the repo path `memory/auto/` (root carve-out ③); the `~/.claude/...` path is a Claude-harness symlink (`ls -la`: `memory -> …/memory/auto`) |
| C58 | BROCK/CLAUDE.md:36 | MODEL-OBSOLETE | LOW | REWRITE | "Boot and closeout are one symmetric sequence: what you READ at boot, you WRITE BACK at closeout… (per `[[feedback_intra_day_closeout_discipline]]`)" | Drop the framing sentence; PROME retired the boot/closeout symmetry check 10/31 (WQ-578 sweep row 28) — the pairing list itself is harmless |
