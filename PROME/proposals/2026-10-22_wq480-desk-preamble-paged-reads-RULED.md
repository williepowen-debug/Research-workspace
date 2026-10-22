# WQ-480 — desk agent preamble reads charters in bounded pages (RULED APPROVE rec B, Will 2026-10-22 09:55 ET, verbatim "480 approve your rec")

**Owner:** PROME (84affa50) · **Class:** process change #1 of the session (ceiling 5; `PROME/CLAUDE.md` § Session Process Controls) · **Reads:** plan read on THIS record before the edit, result read on the edited file after (WQ-178 classes); residue declared below.

## Why
A desk PROME spawns with the Agent tool is not harness-injected: `.claude/agents/desk.md` § Boot makes it READ root `CLAUDE.md`, `AGENTS.md`, `USER.md` and `AGENTS/<NAME>/CLAUDE.md` with the Read tool, which truncates silently past the harness single-read cap (25,000 tokens ≈ 54 kB; `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` rule 1) and whose 60% budget is 32,550 B. Measured 2026-10-22 (`wc -c AGENTS/*/CLAUDE.md`): 13 charters over the budget; NEXUS 71,849 B over the cap; LABOR 53,025 B within 2% of it. READ_CAP rule 20 exempts the charter only because injection delivers it whole — that premise fails in spawn mode. Option B fixes the READER, not the charters.

## The edit (ONE edit, both copies byte-identical — the boot gate's root↔PROME parity check is BLOCKING)
Files: `.claude/agents/desk.md` and `PROME/.claude/agents/desk.md`, § Boot, the paragraph that begins "Resolve the repository root".

BEFORE (verbatim):
> Resolve the repository root (`git rev-parse --show-toplevel`). Explicitly read root `CLAUDE.md`, `AGENTS.md` and `USER.md`, then `AGENTS/<NAME>/CLAUDE.md` and that desk's boot instructions. Resolve all repository-root paths from the repository root. Do not assume instructions, hooks or tools loaded from the launch directory. Report missing dependencies and continue independent authorized work. Run `date` before writing any timestamp.

AFTER (verbatim, v3 — v1 was never committed: the plan read reviewed an uncommitted draft, and the first commit 58a872743 already carried v2; v2→v3 changed one clause, "most charters are over the read budget" → "several … at least one is over the cap", on the ARGUS closeout audit's ❌ (13 of 43 is not "most"); revised earlier for the plan read's ❌ A and, on the reader's recommendation at the plan stage, its ⚠️ 1 and the restart clause):
> Resolve the repository root (`git rev-parse --show-toplevel`). Explicitly read root `CLAUDE.md`, `AGENTS.md` and `USER.md`, then `AGENTS/<NAME>/CLAUDE.md` and that desk's boot instructions. **Read each of those four files with the bounded reader, one document per call: `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_read.py <path>`, then `--offset <next_offset> --sha256 <sha256>` until `eof: true`; a changed-source refusal (rc 2) means restart that document at offset 0.** A whole-file Read truncates silently past the harness cap; several charters are over the read budget and at least one is over the cap — the count is the instrument's, `wc -c AGENTS/*/CLAUDE.md` (WQ-480 B, Will 2026-10-22). Your delivery memo names the page count you read for each of the four files; a read not carried to `eof: true` is incomplete — say so there, and do not act on an instruction you have not read. Resolve all repository-root paths from the repository root. Do not assume instructions, hooks or tools loaded from the launch directory. Report missing dependencies and continue independent authorized work. Run `date` before writing any timestamp.

Nothing else in the file changes: frontmatter (`model: opus`), § Git, § Scope, § Deliver before idle are untouched.

## Invariants the reads check
1. The only diff between BEFORE and AFTER is the inserted run (one bold sentence plus two plain sentences) after "boot instructions." — no word elsewhere changes.
2. Both copies are byte-identical after the edit (`cmp .claude/agents/desk.md PROME/.claude/agents/desk.md`).
3. `boot_read.py` accepts an arbitrary repository path and returns `next_offset`/`sha256`/`eof` as the sentence describes (it did for `/tmp/prome-boot-84affa50/gate.txt` and `HEARTBEAT.md` this morning).
4. The sentence tells a desk what to do when a read is cut short (say so), not to stop.
5. No authority, route, model, threshold or delivery contract moves.

## Acceptance (in the defect's terms)
- A spawned NEXUS reading `AGENTS/NEXUS/CLAUDE.md` (71,849 B) reaches `eof: true` across ~13 reader pages (6,000 chars each, plan reader's measurement) — verified at the next NEXUS spawn by the page counts the AFTER text now requires in its delivery memo (❌ A fixed: sentence and acceptance agree).
- A spawned desk whose charter fits one reader page (6,000 chars; today only ATHENA 3,493 B and BARON 5,018 B) sees one call and `eof: true`; every other desk sees ≥2 calls per file — the cost of the fix, disclosed.
- Neighbours (WQ-229): ordinary = a small charter (one page) · overlap = PROME's own boot already uses the reader, unchanged · wrong owner = N/A (PROME owns both copies) · missing information = a desk that cannot find `boot_read.py` reports the missing dependency and continues (existing sentence) · concurrent = two desks reading the same file concurrently share nothing (reader is read-only).

## Follow-through
NEXUS flagged to DAEDALUS PR#8 by packet `AGENTS/DAEDALUS/inbox/2026-10-22_from-PROME_WQ480-NEXUS-charter-over-cap.md` (written after the plan read; ❌ B fixed) — the one charter over the hard cap even with paging is still a context-cost finding; DAEDALUS owns the blueprint class.

## Reads
- Plan read: DONE 2026-10-22 10:00 ET (coldreader, Sonnet): SCORE 11 ✅ · 6 ⚠️ · 2 ❌; verdict "edit with the named ❌ fixed". ❌ A (acceptance asked for a page count the sentence never required) → sentence v2 requires it. ❌ B (DAEDALUS packet named as sent but absent) → written and committed. Ledger: session scratchpad `wq480_plan_read.md`.
- Result read: DONE 2026-10-22 10:01 ET (coldreader, Sonnet, on the edited `.claude/agents/desk.md`): SCORE 8 ✅ · 4 ⚠️ · 0 ❌; verdict RELEASE. Installed text = AFTER v2 verbatim; only the one hunk per file; both copies byte-identical (3,869 B); the command ran verbatim from `PROME/` and the rc 2 restart clause was confirmed live. Ledger: session scratchpad `wq480_result_read.md`. Episode: two reads, early stop at ❌ = 0 (no third read).

## Declared residue (plan read ⚠️, WQ-178 — not fixed unless named)
1. ⚠️ cwd ambiguity (verbatim command failed from `PROME/`) — FOLDED into v2 (`cd "$(git rev-parse --show-toplevel)" &&`), on the reader's plan-stage recommendation.
2. ⚠️ "each of those files" scope — FOLDED: v2 says "those four files"; files a charter then tells the desk to read whole are governed by the charter's own READ_CAP perimeter, not this sentence.
3. ⚠️ `PROME/COMPLETION_SPEC.md` § Required spawn brief carries the brief-level preamble and now says less than `desk.md` (no bounded-read rule for a brief-only spawn, e.g. a Codex runtime). NOT fixed here — a second shared-contract file is outside this ONE edit; DOCKET row registered for the next process pass to align the two carriers (same words in both, or COMPLETION_SPEC pointing at desk.md as the mechanic's home).
4. ⚠️ time-bound "thirteen charters" in a standing prompt — FOLDED: v2 says "most charters" and names the instrument (`wc -c`).
5. ⚠️ cost (≈20 calls for a spawned NEXUS; page size 6,000 chars) undisclosed — disclosed in Acceptance above and in the DAEDALUS packet; not in the prompt sentence by design (the desk does not need the figure).
6. ⚠️ "2%" / "under one page" bases — stated in Acceptance (2.3%; one page = 6,000 chars).
Counterexamples the reader devised (path error read as truncation · concurrent edit mid-read · acting on a half-read charter) are each answered by a v2 clause (cd prefix · restart at offset 0 · "do not act on an instruction you have not read").

## Declared residue (result read ⚠️ — none fixed; the file is byte-stable after the read)
7. ⚠️ Missing-reader fallback unspecified: if `boot_read.py` is absent, "report missing dependencies and continue independent authorized work" meets "do not act on an instruction you have not read" with no stated path (paged Read vs stop). Carried to the COMPLETION_SPEC alignment row (DOCKET, next-PROME-process-pass) as a clause to settle in both carriers.
8. ⚠️ "those four files" vs "that desk's boot instructions": whether a separate boot file (where one exists) gets the bounded reader is unstated. Same row.
9. ⚠️ "WQ-480 B, Will 2026-10-22" is opaque to a desk; `eof: true` is JSON `"eof": true`. Cosmetic; not fixed.
10. ⚠️ `desk.md` frontmatter description still says the file carries the COMPLETION_SPEC preamble (now a superset). Same row as residue 3.

## ARGUS closeout audit (2026-10-22 10:20 ET) — third correction pass, disclosed
ARGUS (session 84affa50 closeout) graded the installed sentence ❌: "most charters" is false (13 of 43 over the budget). Fixed in both copies and in the AFTER text above (v3) AFTER the result read, so the fix is UNREVIEWED by that read; a read-only execution check (the procedure exception, third read of the episode) is owed on the installed file after this pass — its result is recorded below. ARGUS ❌ on this record: "v1 is in git at the plan-read commit" was false — corrected in the AFTER heading above. This is the record's third correction pass (two-correction stop tripped at the result-read residue append); the independent read it requires is the execution check named here.
- Execution check (third read): DONE 2026-10-22 10:23 ET (coldreader, Sonnet, run from `PROME/` as a spawned desk would): SCORE 6 ✅ · 3 ⚠️ · 0 ❌ — root CLAUDE.md 4 pages, AGENTS.md 1, USER.md 2, AGENTS/NEXUS/CLAUDE.md 13, all to `eof: true`, 20 calls, no rc≠0; rc 2 restart clause confirmed; 13 charters over the budget, NEXUS alone over the cap; both copies identical. Verdict EXECUTES AS WRITTEN. ⚠️ residue: the sentence states neither the cap nor the budget figure (relies on `wc`); a separate boot file would have no read instruction (none exists today); root-relative paths elsewhere in the file depend on the "resolve from the repository root" sentence. Ledger: session scratchpad `wq480_execution_check.md`. ARGUS re-review of the seven closeout fixes: 6 ✅, 1 ❌ = the "was run" wording above, corrected in this same edit.
