# DAEDALUS -> LIQUID: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — none for this desk

## Changelist B — optional trims (17)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| C75 | LIQUID/CLAUDE.md:76, :215 vs LIQUID/CLOSEOUT.md:102, :149, :185 | CANON-CONTRADICTION / ROUTING | HIGH | REWRITE | CLAUDE L76 "`outbox/` is reserved for PROME-action requests."; L215 "`outbox/` \| PROME-action requests ONLY." vs CLOSEOUT L149 "PROME requests → root `PROME/inbox/`; `outbox/` = optional sender copy." | Make CLAUDE.md match CLOSEOUT.md and root ("PROME requests → root `PROME/inbox/`"); one line each |
| C76 | LIQUID/CLAUDE.md:52 vs :76 | OTHER (self-contradiction) | LOW | REWRITE | L52 "Outbox: `outbox/` — not a delivery lane"; L76 "`outbox/` is reserved for PROME-action requests." | Resolves with C75 |
| C77 | LIQUID/CLAUDE.md:81-89 | HISTORY-IN-STEP | LOW | STRIKE | "PERIMETER DEFECT ON THE `Second private credit fund gate` ROW — CLOSED 2026-09-12… The history, kept because the LESSON is the durable half" | Strike the four paragraphs (~3.3 KB); the live rule "read BROCK's count; do not keep a second one" is already at L147 |
| C78 | LIQUID/CLAUDE.md:33-35 | HISTORY-IN-STEP | LOW | REWRITE | "The old text said only \"not yet logged\", naming NO operation…"; "(it was 175,581 B / 324% when this line was written on 2026-09-17…)"; "Measured on this file 2026-09-17: 2 duplicate `signal_id`s…" | Keep the grep loop + "grep only, never read whole, never rotate". ~2 KB |
| C79 | LIQUID/CLAUDE.md:75 and LIQUID/CLOSEOUT.md:102 | HISTORY-IN-STEP | LOW | STRIKE | CLAUDE L75 "⛔ CORRECTED 2026-09-03 — this line pointed AROUND WALTER and was never exercised…"; CLOSEOUT L102 "⛔ CORRECTED 2026-09-03 (DAEDALUS route-around census…)" | Keep only the corrected rule (L76 / CLOSEOUT step 2). ~1.4 KB across both |
| C80 | LIQUID/CLAUDE.md:215 | HISTORY-IN-STEP | LOW | REWRITE | "⛔ CORRECTED 2026-09-03 (DAEDALUS route-around census, `walter_route_check.py`): this row read \"HERMES retired…\" — a ROUTE-AROUND instruction that survived…" | Row → "PROME requests → `PROME/inbox/` (see C75); signals → WALTER; analysis → recipient inbox" |
| C81 | LIQUID/CLAUDE.md:24 | GIT-SAFETY | LOW | REWRITE | "0. **`git pull`** — sync from GitHub before reading anything. Follow pull protocol in root CLAUDE.md." | As C25 |
| C82 | LIQUID/CLAUDE.md:16 | DUPLICATE / MODEL-OBSOLETE | LOW | STRIKE | "⚠️ YOUR #1 RULE: Always WRITE findings to STATUS.md. If it's not in the file, it doesn't persist." | Root Output Canon "File > verbal" |
| C83 | LIQUID/CLAUDE.md:112, :114, :128 | HISTORY-IN-STEP | LOW | REWRITE | "(named lane on the FUNDING_LIQUIDITY row, WALTER ROUTING_TABLE v0.27, Will-authorized 2026-08-18; a ratification of existing practice…)"; "(seam registered 2026-07-12, DAEDALUS per PROME 7/11…)" | Keep the scope line + the "terminal-gated, say so" caveat; drop ratification provenance |
| C84 | LIQUID/CLAUDE.md:198, :200, :203 | OTHER (stale file roles) | LOW | REWRITE | "THESIS v2.0 (5/19)"; "Forward-only Active Branch Points (8 decision windows, Jun 20 → YE…)"; "Q2 marks ~7/25 = NEXUS R3 credit-bifurcation transmission test" | Role-tense rows (as FLG/GIBBS FILES tables do) |
| C85 | LIQUID/CLAUDE.md:147 | HISTORY-IN-STEP | LOW | REWRITE | "⛔ ~~Second private credit fund gate~~ RETIRED-AND-REPOINTED 2026-09-12… ≥3 consecutive sub-100% satisfaction quarters…" | Strike the row; restating BROCK's gate letter contradicts its own "do not keep a second, coarser one here" |
| C86 | LIQUID/CLAUDE.md:156-160 | OTHER | LOW | STRIKE | empty `---` blocks | strike |
| C87 | LIQUID/CLOSEOUT.md:160-164 | MODEL-OBSOLETE / DUPLICATE | LOW | STRIKE | "Read before editing — never `Edit` without `Read` in the same turn"; "`trash` over `rm` for deletions" | Root Critical Rules #1 and #11 own both; the brief names read-before-edit hand-holding as model-obsolete |
| C88 | LIQUID/CLOSEOUT.md:160 vs :64 | OTHER (self-contradiction) | LOW | REWRITE | L160 "Behavior-language over hash-pinning in state files (hashes go stale within 48h)"; L64 "using `STATUS commit: \`<hash>\`` with that STATUS commit" | Scope L160 to exclude the NEXUS pin, or strike it |
| C89 | LIQUID/CLOSEOUT.md:30 | OTHER (dead pointer) | LOW | REWRITE | "Did I touch positions/proposals? → STATUS Active Positions/Proposals" | STATUS.md has six sections (`grep '^## '`: NOW · GATES · OWED · CARRIED · CAVEATS · POINTERS); no such section. Point to §3 OWED or drop |
| C90 | LIQUID/CLOSEOUT.md:51, :62 | HISTORY-IN-STEP | LOW | STRIKE clauses | "(Aligned 2026-09-29 to the six-section STATUS layout; the old \"3 dashboards…\" list described the pre-restructure file…)"; "L836 repair, 2026-10-25 (PROME's existing Will-directed packet):" | Strike |
| C91 | LIQUID/CLOSEOUT.md:89, :182 | OTHER (stale trigger) | LOW | REWRITE | "Q1 BDC marks landed or new mark divergence"; "Only if Q1 marks landed" | "a quarter's BDC marks landed" |
