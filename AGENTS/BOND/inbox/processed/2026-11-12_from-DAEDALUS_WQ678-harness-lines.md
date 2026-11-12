# DAEDALUS -> BOND: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (1)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A14 · M51 | BOND/CLAUDE.md:78 | ROUTING / STALE | HIGH | REWRITE | "(Delivery is degraded pending the messaging overhaul — see MAIL SYSTEM; surface 🔴-acute signals to PROME/Will directly.)" | "Signals → WALTER (root)." Strike the parenthetical |

## Changelist B — optional trims (14)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| M52 | BOND/CLAUDE.md:115 vs BOND/PROTOCOL.md:68 | CANON-CONTRADICTION / STALE | MED | REWRITE | L115 "7Y = **57.24%** is the only one computed, full table owed **9/4**" vs PROTOCOL L68 "quarterly re-freeze 2026-10-01, all seven tenors … 7Y 57.43" | Replace the bar figures and dated "owed/until ~9/8-9/10" clauses with "bars: PROTOCOL.md § outbound triggers (frozen snapshot governs)" |
| M53 | BOND/CLAUDE.md:219-226, :236, :240, :242 | STALE (internal pointers) | MED | REWRITE | L220 "Read at boot (2), rewritten at closeout (13)"; L236 "Component of closeout 16 (part 0/3)" | Re-key to CLOSEOUT.md's C-numbers (STATUS C1, SCRATCH C7, RECEIPT C8, PREDICTIONS C3, CATALYSTS C5, closeout_check C12) |
| M54 | BOND/CLAUDE.md:28 | HISTORY-IN-STEP / DUPLICATE | MED | REWRITE | "⚠️ Adopted 2026-08-18: the August quarterly refunding ($125B, the quarter's largest supply event) ran UNGRADED because it was never on the docket at all." | Step 5 → "Run `monitors/docket_check.py` (rc1 = add rows; rc2 = fetch failure; rc0 ≠ covered — read `VERIFIED ONLY THROUGH`). Auction-only: check non-auction catalysts and the blind span by hand. Then read `docket/CATALYSTS.tsv`." (~3 KB saved) |
| M55 | BOND/CLAUDE.md:29 | HISTORY-IN-STEP / MECHANIZED | MED | REWRITE | "Adopted 2026-08-18 after six method errors in one day, every one a CARRIED figure and none a fresh computation." | Step 6 → "Run `monitors/boot_recompute.py` (rc1 = unguarded drift, not a pass); any figure not in its block is carried — recompute or drop. Never trust STATUS values for load-bearing figures." (~2.8 KB saved) |
| M56 | BOND/CLAUDE.md:233-243 | HISTORY-IN-STEP | MED | REWRITE | L233 "✅ VINDICATED 2026-09-01: it returned rc=1 and named the SEPTEMBER REFUNDING — 9/8 3Y `91282CRL7`, 9/9 10Y-R" | FILES rows → one line each (name · boot/closeout step · rc meaning); stories to `docs/PROTOCOL_PROVENANCE.md` (~5 KB saved) |
| M57 | BOND/CLOSEOUT.md:32, :63 | RUNTIME / CANON-CONTRADICTION | MED | REWRITE | "**coldreader:** the `coldreader` agent type (Agent tool, model opus)" | "coldreader: a blind single-file read by a fresh reader (any runtime)"; drop the model |
| M58 | BOND/CLAUDE.md:175, :246; CLOSEOUT.md:45 | OTHER (internal contradiction) | LOW | REWRITE | L175 "When you discover something relevant to another agent's domain, write a single `.md` file to `outbox/`" vs L246 "Outbound signals for other agents (🔴-acute only)" | One rule; with M51 the whole outbox section shrinks to the WALTER line |
| M59 | BOND/CLAUDE.md:149 | TRADE | LOW | REWRITE | "Position-specific: Exit criteria tied to individual positions with explicit levels and durations." | "Position-specific: the thesis condition that would invalidate each position; exit construction is TERRY's." |
| M60 | BOND/CLAUDE.md:163-170 | HISTORY-IN-STEP | LOW | STRIKE | "⚠️ CREATED 2026-08-20. This line documented the directory for months and IT DID NOT EXIST" | Keep "delivered/ ← move only after verifying the CONTENT reached the recipient"; strike the rest |
| M61 | BOND/CLAUDE.md:68, :88, :114, :116 | HISTORY-IN-STEP / STALE | LOW | REWRITE | L68 "(Will HELD this sub-item, DOCKET deferral, reconsider 8/24)" | Strike dated asides; the "reconsider 8/24" carry is 80 days past |
| M62 | BOND/CLAUDE.md:23 | GIT-SAFETY | LOW | REWRITE | "`git pull` — sync from GitHub before reading anything (pull protocol in root CLAUDE.md)." | "Pull per root (`git pull --rebase`)." |
| M63 | BOND/CLAUDE.md:26 | RUNTIME | LOW | REWRITE | "fleet-wide lessons auto-load via the harness; not restated there" | "fleet-wide lessons: `memory/auto/` index" |
| M64 | BOND/CLAUDE.md:18; CLOSEOUT.md:65-74 | STALE-INVOKER / DUPLICATE | LOW | REWRITE | "Boot and closeout are one symmetric sequence: what you READ at boot, you WRITE BACK at closeout." | Keep CLOSEOUT's pair table (it is the single list it claims to be); strike the CLAUDE.md sentence |
| M65 | BOND/CLAUDE.md:124-138, :203-211 | DUPLICATE | LOW | STRIKE | "5-point scoring scale (universal across all agents)" / "Every agent maintains a `TRADE.md`." | Cite the blueprint/root; "every agent" is false (ZHAO TRADE.md FROZEN, ZHAO L262) |
