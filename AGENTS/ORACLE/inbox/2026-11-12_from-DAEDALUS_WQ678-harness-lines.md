# DAEDALUS -> ORACLE: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (1)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A1 · U-O01 | ORACLE/CLAUDE.md:56 | GIT-SAFETY | HIGH | REWRITE | "non-ff → `git pull --rebase` + re-push, never force — note it in SCRATCH and flag PROME/Will if it recurs" | Weaker than root session-end 3: omits the incoming/dirty-path overlap check before rebasing, and escalates a bare recurrence (root: "bare recurrence is ordinary traffic"; escalate only on conflict outside own dir or non-ff persisting through a completed cycle). Replace with "non-ff → root session-end step 3 in full". Shorter. |

## Changelist B — optional trims (10)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| U-O02 † | ORACLE/CLAUDE.md:240–255 (+ :284) | CARVE-OUT / ROUTING | HIGH | REWRITE | "`outbox/` ← outbound signals for other agents ... `delivered/` ← signals the target has picked up (agents poll directly; HERMES retired 2026-06)" | Root carve-out ①: a packet goes into the recipient's `inbox/` and the author must commit it. `outbox/` holds 2026-08-27 and 2026-09-24 packets to HAWK/BRENT/FALCON, LIQUID/BOND/HENRY/RED never moved to `delivered/`; ORACLE's recent packets go to `PROME/inbox/` and `CATO/inbox/` instead. Replace MAIL SYSTEM with "send = carve-out ① inbox packet". ~0.6 KB. |
| U-O03 | ORACLE/CLAUDE.md:32 | CANON-CONTRADICTION | MED | REWRITE | "**Check `inbox/`** (+ `inbox/WALTER/`) — process pending signals; `git mv` processed → `inbox/processed/`." | WALTER handoffs are consumed to `inbox/WALTER/processed/` (WALTER BP L171 verbatim Rule 10; RED L48 explains the lane archive is what WALTER's delivery audit reconciles). Say "each lane's own `processed/`". |
| U-O04 | ORACLE/CLAUDE.md:221 | HISTORY-IN-STEP | MED | REWRITE | "this line previously read 'creds PRESENT on this box' as if standing — which conflicted with MACHINE_LOCAL and cost real time in the 8/20 T6 thread" | The ~3.6 KB Kalshi paragraph carries three incident stories (creds, search fix, removed examples). Keep: creds path, `kalshi.py status` rc meaning, OI = depth, VIX gap unverified, quarterly re-check date. ~2.5 KB. |
| U-O05 | ORACLE/CLAUDE.md:99–127 | OTHER (dead template) | LOW | STRIKE | "### Tier 1 — Direct Thesis Relevance (check every spawn)" | Three tables whose every Current/Thesis/Gap cell is "—"; `watchlist.tsv` / `kalshi_watchlist.tsv` are the real pull lists (L268–269). ~1.4 KB. |
| U-O06 | ORACLE/CLAUDE.md:213–219 | MECHANIZED | LOW | REWRITE | "`--all` drops the domain filter; `--tracked` includes watchlist markets. Catches news-reactive markets the watchlist misses (e.g. surfaced the Iran-shipping re-escalation" | Subcommand flag docs + first-run anecdotes belong in `polymarket.py --help`; keep one line per subcommand. ~2 KB. |
| U-O07 | ORACLE/CLAUDE.md:191 | TRADE / CANON | LOW | REWRITE | "route to TERRY only if liquidity/resolution/fees survive discounts." | USER.md (2026-11-10): material findings go to TERRY for a tradeability read unasked; "no card" is an answer. Drop "only if…"; TERRY applies the discounts. |
| U-O08 | ORACLE/CLAUDE.md:50, :67 | DUPLICATE | LOW | STRIKE (one) | L50 "rewrite the live dashboard (alerts to top, <250 lines)" / L67 "**Compress.** STATUS.md under 250 lines." | Keep one. |
| U-O09 | ORACLE/CLAUDE.md:16, :37, :59, :173, :248, :276 | HISTORY / STALE | LOW | STRIKE | L173 "We're at 82% D scenario, but Polymarket 'Iran ceasefire by April' is at 60%." / L276 "T6 pin ledger for Kalshi `KXFED-26SEP-T3.75`" | Provenance parentheticals, a stale April example, a September-2026 FOMC pin tool row (that meeting has passed). |
| U-O10 | ORACLE/CLAUDE.md:42 | OTHER (pointer) | LOW | REWRITE | "(memory `boot_protocol_live_event_override`, `intra_day_closeout_discipline`)" | Bare slugs; the second resolves only as `feedback_intra_day_closeout_discipline.md`. Drop (provenance only). |
| U-O11 | ORACLE/CLAUDE.md:65 | DUPLICATE | LOW | REWRITE | "**Output canon → root CLAUDE.md §Output Canon** (tables > prose · numbers > narrative · source+date every claim · file > verbal" | Drop the parenthetical. |
