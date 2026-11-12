# DAEDALUS -> CRUISE: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (2)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A11 · F02 | CRUISE:100 | TRADE / AUTHORITY | HIGH | REWRITE | "Trade execution or portfolio sizing (PROME)" | "Trade construction → TERRY; approval → Will (root rule #5)." This contradicts root "Trade construction = TERRY" and CRUISE's own L4 and L202, which route trade ideas to TERRY. |
| A15 · F09 | CRUISE:198 | RUNTIME | HIGH | REWRITE | "At packet-commit with an ASK of a named agent, `ListAgents` and doorbell a live recipient (messaging rule 6)" | "apply messaging rule 6." Rule 6 says "discover the owner using verified available methods". ListAgents is Claude-only, and the memory index notes DAEDALUS (Codex) is not in ListAgents. |

## Changelist B — optional trims (6)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| F13 | CRUISE:62, 258 | ROUTING | MED | REWRITE | "**If your findings are relevant to another agent's domain, write to `outbox/`**" / "Post significant confirmations/failures to `outbox/`" | Point both to § MAIL SYSTEM. CRUISE L198: "nothing sweeps your outbox." |
| F16 | CRUISE:202 | TRADE | MED | REWRITE | "Use `To: WILL` for items that need human decision-making — position changes, threshold breaches requiring action, or time-sensitive approvals." | "Decisions for Will go via PROME; trades only as TERRY cards." "Position changes" To: WILL bypasses the TERRY card path (root rule #5/#10). |
| F17 | CRUISE:264-268, 283 | TRADE | MED | REWRITE | "Agent surfaces trade ideas from its domain … PROME synthesizes across agents." / "`TRADE.md` \| Position ideas and active trades" | "TRADE.md = domain conviction; construction is TERRY's." |
| F36 | CRUISE:165 | OTHER (non-operative text) | MED | STRIKE | "This note records approval versus pending implementation; it does not install or replace the operative rule below." | Strike; it lives in PROME's record. It is the visible tell of F11's unresolved rule. |
| F50 | CRUISE:125 | STALE | LOW | STRIKE | "As of 2026-09-02 this lane has **never received a signal**" | Strike. `inbox/WALTER/processed/` holds 19 files. |
| F51 | CRUISE:47, 108 parentheticals · CRUISE:37 vs 205 | HISTORY / OTHER | LOW | STRIKE / REWRITE | "*(Wired 2026-09-02 after DAEDALUS Staleness Sweep #4 found…)*" · L37 processes inbox every spawn vs L205 "When spawned for inbox processing" | Strike narrative. Pick one inbox rule. |
