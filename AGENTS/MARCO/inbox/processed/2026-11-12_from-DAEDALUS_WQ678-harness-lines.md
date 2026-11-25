# DAEDALUS -> MARCO: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (2)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A14 · F05 | MARCO:70 (+83, 263) | CANON-CONTRADICTION / ROUTING | HIGH | REWRITE | "**Outbox:** `outbox/` — ONLY for requests needing PROME action." | "PROME requests → `PROME/inbox/` (root)." Root: "Write to `PROME/inbox/` … to request Prome action; `AGENTS/<NAME>/outbox/*to-PROME*` files are for signal/routing work." |
| A15 · F10 | TOURISM:7 | RUNTIME | HIGH | REWRITE | "Parent `CLAUDE.md` files further up the tree (`MARCO/CLAUDE.md`, `Research-workspace/CLAUDE.md`) will also load." | "If parent charters are loaded, ignore their identity; read root CLAUDE.md for discipline." Under a runtime that does not auto-load parents, "Inherit only the operational discipline from parent files" silently inherits nothing. |

## Changelist B — optional trims (8)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| F06 † | MARCO:93 vs 81 (+191-195) | ROUTING (internal) | HIGH | REWRITE | L93: "**Write a signal when:** a threshold fires, a prediction resolves…" (under L83 "directly to the target agent's `inbox/`") vs L81 "SIGNALS — a registered threshold firing … go to WALTER" | Drop "a threshold fires" from the direct-packet template, or tag it "→ WALTER". The send-table L191-195 names direct recipients for threshold rows. |
| F07 | MARCO:57 | CANON-CONTRADICTION | HIGH | STRIKE clause | "**Check: `python3 scripts/brief_pin_check.py MARCO`** (amendment 11 hash pin; supersedes the A10 timestamp test)." | Strike the check clause and the 7/31-audit history (~1.5 KB line). Schema L108 says amendment 11 "is never shipped as an added closeout step in any desk's instructions." The bare path also resolves only from repo root (`AGENTS/MARCO/scripts/brief_pin_check.py` MISSING). |
| F15 | MARCO:58-59 | CARVE-OUT ③ | MED | REWRITE | "Transferable cross-agent lesson → auto-memory (repo-tracked at `memory/auto/` …" then L59 "commit own files … (pathspec `AGENTS/MARCO/`)" | Replace the symlink/container paragraph with "auto-memory → carve-out ③ (self-commit + memory_index_check)". |
| F34 | MARCO:197-214 | HISTORY-IN-STEP | MED | REWRITE | "**The problem this fixes:** the old rule fired on raw YoY and would have dispatched an **airline bankruptcy** to three desks…" | Keep the seven rules as one-liners (adjusted+raw, CONFOUNDED label, MIA basis, June-2027 expiry, revised-vintage cutoff, enplanements, GEE measured). Strike the narratives and "*(That defect was shipped in this very recipe on 9/19…)*" — the tool now refuses without `--out` (mechanized). 4.9 KB → ~1.5 KB. |
| F35 | MARCO:258-260 | MECHANIZED / HISTORY | MED | REWRITE | "**Standing tsvutil invariant check (boot step, built 2026-08-21 s23)** — the guard that catches…" | One-line purposes. All three tools already run inside `scripts/boot.py` (L60, L68; staleness L48). ~2.8 KB → ~0.4 KB. Keep "write TSVs only via `write_tsv()`". |
| F45 | MARCO:265 | OTHER | LOW | REWRITE | "new facts/claims go here at closeout (step 7)" | "(step 8)". L54 is the workbook step; L53 step 7 is predictions. |
| F46 | MARCO:64 · MARCO:45 · MARCO:25-27 parentheticals | HISTORY | LOW | STRIKE | "**Infrastructure (built — maintain in closeout):** … Remaining maturity gaps:" | Maturity status is DAEDALUS's FLEET_MAP, not a step (~0.5 KB plus parentheticals). |
| F47 | TOURISM:117 | DUPLICATE (self-contradicting) | LOW | STRIKE | "Do not duplicate confidences here — they drift. At a glance (as of 2026-05-31): … TOUR-01 (85%)…" | Strike the at-a-glance sentence. |
