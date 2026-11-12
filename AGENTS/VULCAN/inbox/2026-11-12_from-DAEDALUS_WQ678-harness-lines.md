# DAEDALUS -> VULCAN: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — none for this desk

## Changelist B — optional trims (6)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| E-VU1 | VULCAN/CLAUDE.md:51 | CANON-CONTRADICTION (root + internal) / GIT | MED | REWRITE | "or, if a coordinator offers its push train, write `push delegated to PROME <time>` ... Spawned by a coordinator ⇒ do NOT push." | Keep the conditional ("if a coordinator retains push custody, record delegation") as FALCON:32/YURI:95 do; the unconditional "do NOT push" contradicts root (auto-push at closeout) and the sentence before it, and can strand commits unpublished. |
| E-VU2 | VULCAN/CLAUDE.md:72 vs 163, 177 | ROUTING / CARVE-OUT / CANON-CONTRADICTION (internal) | MED | REWRITE | L72 "signal in another agent's domain → write to `outbox/` as a task packet." vs L163 "Outbox = crisis-only (🔴 async)" vs L177 "write packets directly to the target's `inbox/`" | Same one-line fix as E-WA1 (direct to owner inbox, committed under carve-out ①). |
| E-VU3 | VULCAN/CLAUDE.md:133 | STALE-INVOKER (dead pointer) | MED | REWRITE | "KILL_MEMO for any cascade trigger." | `ls AGENTS/VULCAN/KILL_MEMO.md` → no such file (git ls-files finds none; FILES table L204–228 lists none). Strike, or point at `workbook/EXIT_PROTOCOL.md` which exists. |
| E-VU4 | VULCAN/CLAUDE.md:190–202 | MECHANIZED / HISTORY-IN-STEP | LOW | REWRITE | "V1–V3 refuse mismatched unit/model/tier; V4 basis and V5 n-floor produce UNGRADEABLE/ERR; V6 records dispersion without a threshold." | TOOL SAFEGUARDS is 7,561 B of tool behaviour the tools already enforce (refusals, validators, selftests) plus dated state (L194 "next renewal before December 18", L199 "CME review now runs to January 8, 2027", L197 META dates) that belongs in CATALYSTS/STATUS. Keep the run-after-edit test commands; move the rest to tool docstrings/specs. |
| E-VU5 | VULCAN/CLAUDE.md:56, 171 | DUPLICATE | LOW | STRIKE | "Boot↔Closeout symmetry: what you read at boot ... you reconcile at closeout" | Strike both (closeout checklist + closeout_check.py carry it; symmetry check retired WQ-578). |
| E-VU6 | VULCAN/CLAUDE.md:131, 126 | HISTORY-IN-STEP | LOW | REWRITE | "2026-10-20 scoped WQ-441 disposition: Will chose and retained B for Volta ..." | Move the Volta disposition to STATUS/ruling record; keep only the PULLED definition row (L126) minus its first-application history. |
