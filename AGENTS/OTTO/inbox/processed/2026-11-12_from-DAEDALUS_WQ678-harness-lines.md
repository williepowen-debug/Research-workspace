# DAEDALUS -> OTTO: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (3)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A15 · S-12 | AGENTS/OTTO/CLAUDE.md:184-185 | RUNTIME | HIGH | REWRITE | "After promoting to auto-memory, DELETE the local copy — auto-memory loads at every boot via the harness" | Name the repo path `memory/auto/` (carve-out ③) and drop "loads via the harness"; a Codex session doesn't load `~/.claude/...` memory, so deleting the local copy loses the lesson |
| A15 · S-13 | AGENTS/OTTO/CLAUDE.md:342 | RUNTIME | HIGH | REWRITE | "Spawn pattern: Agent tool with prompt pointing to `AGENTS/OTTO/docket/WINTERKORN.md` (spec) then … `WINTERKORN_MEMORY.md` (state)." | "Spawn via the runtime's verified sub-agent method (ORCHESTRATION_PLAYBOOK)" — same length |
| A12 · S-17 | AGENTS/OTTO/CLAUDE.md:386-398 vs 292,527 | TRADE | HIGH | REWRITE | "TRADE.md (position ideas) ↓ PROME consolidates across agents ↓ Will decides" vs L292 "`TRADE.md` FROZEN2026-07-04 … TERRY constructs, Will approves" | Replace the diagram with one line: "Trade ideas → TERRY card; Will approves (root #5); record per root #10." L527 "Position ideas" → "FROZEN" |

## Changelist B — optional trims (17)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| S-14 | AGENTS/OTTO/CLAUDE.md:166-168 vs 287 | CANON-CONTRADICTION | MED | REWRITE | L166 "update `docket/CATALYSTS.tsv` (source of truth)… Also add newly-discovered dated catalysts to the tsv" vs L287 "Maintained by WINTERKORN sub-agent (not edited by OTTO directly during normal sessions" | Pick one editor of CATALYSTS.tsv; shorten the other line to a pointer |
| S-15 | AGENTS/OTTO/CLAUDE.md:124 vs 192 | ROUTING | MED | REWRITE | L124 "Reply (a direct packet to the sender's inbox when it answers THEIR ask…" vs L192 "Do not write directly into other agents' inboxes." | L192: "except answers to a desk's own ASK (§ How to Signal)" — or strike L192 and rely on L332 |
| S-16 | AGENTS/OTTO/CLAUDE.md:431 | ROUTING | MED | REWRITE | "Any mention of company by known short-seller → 🔴 ALERT PROME" | "→ SIG-OTTO-WALTER drop (§ How to Signal)" |
| S-18 | AGENTS/OTTO/CLAUDE.md:76-79 | GIT-SAFETY | MED | REWRITE | "**`git pull`** — sync from GitHub before reading anything. Follow the pull protocol in root `CLAUDE.md`" | "0. Sync per root `CLAUDE.md` § Git Protocol 'Before pulling'." |
| S-19 | AGENTS/OTTO/CLAUDE.md:153,139,179 | STALE-INVOKER (path) | MED | REWRITE | "1a. **Log thesis pivots to `CHANGELOG.md`**" | Say `thesis/CHANGELOG.md`; `ls AGENTS/OTTO/CHANGELOG.md` → No such file (L272 says it moved 2026-06-09) |
| S-20 | AGENTS/OTTO/CLAUDE.md:150,193 | STALE-INVOKER (cwd) | LOW | REWRITE | "`python3 scripts/read_cap_check.py --agent OTTO`" / "`python3 scripts/brief_pin_check.py OTTO`" | Use `"$(git rev-parse --show-toplevel)/scripts/…"` like L91; `AGENTS/OTTO/scripts/` has neither file, so desk-dir cwd fails |
| S-21 | AGENTS/OTTO/CLAUDE.md:5 | HISTORY-IN-STEP | LOW | STRIKE | "Stamp reconciled 2026-09-12 (s022), DAEDALUS profile finding F-2: this header read `v2.5 | 2026-06-08` while the footer read…" |
| S-22 | AGENTS/OTTO/CLAUDE.md:107 | MECHANIZED / HISTORY | LOW | REWRITE | "(Wired 2026-08-28, DAEDALUS wiring sweep leg ①, batch Will-approved in-session; receipt form updated 2026-10-14 s028…)" | Command + rc meaning + commit path; writer enforces fields |
| S-23 | AGENTS/OTTO/CLAUDE.md:193 | HISTORY-IN-STEP | MED | REWRITE | "(Why an ORDERING rule and not a reminder: the 7/31 fleet audit found 5-of-5 content-stale briefs…)" | Keep "brief is the last write; brief_pin_check prints OK"; strike Amendment-10 history + why-block (~900 B) |
| S-24 | AGENTS/OTTO/CLAUDE.md:225-235 | HISTORY-IN-STEP | MED | STRIKE | "⚠️ AMENDED 2026-08-27 — this line previously read: *\"the WALTER inbox signal drop stays untracked…\"*" | Strike blockquote (~1.3 KB); the ruling file exists (`PROME/proposals/2026-08-27_row102-…RULED-a.md` resolves) |
| S-25 | AGENTS/OTTO/CLAUDE.md:329-330,332(paren) | HISTORY-IN-STEP | MED | STRIKE | "⛔ CORRECTED 2026-09-02 — this section previously said *\"Append to `AGENTS/SIGNALS.md`\"*…"; "(Added 2026-09-24 s023, answering DAEDALUS PR#6 ASK 1…)" | Keep L332's rule sentences only (~1.5 KB saved) |
| S-26 | AGENTS/OTTO/CLAUDE.md:456-466 | HISTORY-IN-STEP / OTHER | MED | STRIKE | "⚠️ CORRECTED 2026-08-27 (s020) — the version of this line that stood until today was OVER-SCOPED…" | Move the Carvana fee research to THESIS/KB; leave a 2-line mechanism + pointer (~2.6 KB) |
| S-27 | AGENTS/OTTO/CLAUDE.md:489 | MODEL-OBSOLETE / HISTORY | LOW | STRIKE | "⚠️ Audit the MOOT rules, not just the live ones (LIQUID KB-LIQ-124, 2026-09-02)…" | Strike; it also points to "the routing conflict below", which is above (L329) |
| S-28 | AGENTS/OTTO/CLAUDE.md:132-141 | MODEL-OBSOLETE | LOW | REWRITE | "Read→write pairings (the spine): STATUS (boot 1 → close 1), calendar (boot 5 → close 3)…" | Keep "catalysts swept before predictions"; strike the pairing map (~900 B) |
| S-29 | AGENTS/OTTO/CLAUDE.md:210-212,219-220 | DUPLICATE | LOW | STRIKE (one) | "non-ff → `git pull --rebase` + re-push, never force" (twice) | Keep one pointer to root |
| S-30 | AGENTS/OTTO/CLAUDE.md:404,435-441 | HISTORY-IN-STEP | LOW | STRIKE | "We had CVNA put position with correct thesis… Closed for $86 loss before EOD" | Keep L443 research rule only |
| S-31 | AGENTS/OTTO/CLAUDE.md:87,278-285,295,297,439,443 | OTHER (root Output Canon) | LOW | REWRITE | "October14", "sinceJuly4", "FROZEN2026-10-14", "January26", "boot3a", "offsets48/21/0/18days", "was21days" | Restore spaces (root: "never glue words together") |
