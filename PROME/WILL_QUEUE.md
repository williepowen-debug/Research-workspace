# WILL_QUEUE.md — the operator's open-items ledger
**Owner:** PROME (registers, updates, retires rows; reconciles at every boot/closeout) · **Will edits freely** — anything marked/struck here is reconciled at PROME's next touch.
**Last reconciled:** 2026-07-31 (~10:50 ET — row 3 DONE: memory migration executed same-session on Will's pull-forward ruling)

**Rules (v1, deliberately dumb — one markdown table until real use earns more structure):**
- **Only items where WILL is the actor.** Types: `LAUNCH` (agent windows) · `[Approve]` (trade/proposal) · `RULE` (canon/disposition) · `BROKER` (exports/confirms) · `BUY` · `ACTION` · `READ`. Fleet work lives on DOCKET + agent boards — the moment an item stops needing Will, it leaves this file.
- Dated rows first (soonest). Hard dates are ISO in the Needed-by column — `prome_gate` reads them (boot+closeout advisory: flags passed dates and a stale reconcile stamp; adopted at birth per `finding_hygiene_commit_rearms_the_staleness_lie` — a schedule decays like any surface).
- **This is the ONLY live copy.** SCRATCH operator card carries a 3-line pointer view; HANDOFF "Open for Will" entries are dated history, not the live list.
- **Blocked rows** carry `⛔ waits: <who>` at the start of Notes — they are NOT Will-actionable, are excluded from the cap, and the blocker must itself exist as a packet/DOCKET item (never a silent wait). *(DAEDALUS W3.)*
- **Hand-off rule:** when a DOCKET catalyst produces an action only Will can take, PROME opens a row here AT THE SAME TOUCH and cross-references both ways. *(DAEDALUS W4.)*
- DONE rows: one line, **durable anchor (commit hash / named record) REQUIRED at write** — then roll-off after ~7d is always safe; the gate flags overdue roll-offs. *(DAEDALUS W5.)*
- Soft cap **20 ACTIONABLE rows** (dated + unblocked); undated unblocked rows get a **21d age tripwire** instead — an old undated row means the item needs a date, a decline, or a re-scope, not that Will is behind. *(DAEDALUS W2.)*
- ⚠️ Needed-by runs at **DAY resolution** — time-of-day text (`~22:00 ET`) is for the reader; the gate parses dates only.

## OPEN

| # | Item | Type | Needed by | Since | PROME rec | Notes |
|---|---|---|---|---|---|---|
| 8 | QQQFADE approval (`TRY-WILL-QQQFADE`) | [Approve] | none (Sep-18 tenor) | 7/30 | — | TERRY's 2 conditions (re-based premise + Target-1 policy); PROME rider "sell the 675P first" is MOOT (put sold 7/30); register Will-discretionary class on fill |
| 9 | Bank-put reshape disposition — **UNBLOCKED 7/31**: RED confirmed the sustain (policy-day prints count; robust on both branches, print #4 = 284) + FT-01 un-fired | RULE | none (no fire-clock; BDC marks 8/4-8/6 = nearest context) | 7/30 | TERRY rebuilds from 7/30 export; no fresh capital absent X1 | level-leg fire on the NARROWER thesis; BANK-ABSENT attribution of record; NOT X1; LIQUID's brief + §3 framing already with you |
| 10 | Fresh rising-vol registration — go/no-go | RULE | none | 7/30 | — | your own 7/30 AM question; VIOLET owns the proposal on GO; nothing pre-committed |
| 12 | HENRY standing boot-rule blessing | RULE | none | 7/28 | mechanical-trigger version | inbox-at-boot rule change, PROME rec on record |
| 13 | FFIEC CDR account | BUY | none | 7/28 | do it (5 min) | DAEDALUS's ask |
| 14 | DEWEY entitlement purchase | BUY | blocked on DEWEY | 7/25 | — | ⛔ waits: DEWEY one-liner · Tier 1 ruled 7/25; DEWEY owes the product/tier/price one-liner first; you spend only on that |
| 15 | RAV charter review → formal ROSTER row | RULE | none | 7/25 | — | DAEDALUS drafted the charter 7/30 (`2b9dbeac`); your review unlocks the registry row |
| 16 | Next broker export + confirms bundle | BROKER | none (next export) | 7/24 | — | one export resolves: off-rail confirms D-1/2/3 (AAPL/GLD/USO→35 ⇒ concentration packets fire), D-6 USO-spread account, D-7 $565+$1,500, D-10 MAIN≟IRA label, tail-rider debit, QQQ 680P figures + strike re-verify, VIXCS timestamped order (settles TERRY's S3 carry) |
| 17 | Repo public flip | ACTION | none | 6/30 | — | all pre-flip blockers closed since 7/4; flip ⇒ delete DESKTOP mirror backup + Phase-5 verify |

## RECENTLY DONE (rolls off ~7d)

| Item | Done | Record |
|---|---|---|
| scripts/-ownership (was row 6) — RULED: DAEDALUS owns repo-root scripts/ (maintenance/break-fix/standards); enforcer patch TRANSFERS with it; PROME keeps PROME/tools/ only | 7/31 | grant packet AGENTS/DAEDALUS/inbox 2026-07-31; PAT-074 = the precedent Will accepted |
| NO_HARVEST_RULE (was row 11) — ADOPTED fleet-wide: mandatory build-time card field | 7/31 | ruling packet AGENTS/TERRY/inbox 2026-07-31; PROME mirrors in own scaffolds at next touch |
| Close REGINALD's window (was row 2) — RESOLVED: pane no longer exists (tmux list-panes verified 7/31 ~13:40; live panes = prome/red/nexus/daedalus only) | 7/31 | tmux verification in-session; RED+NEXUS panes flagged safe-to-close to Will |
| Launch RED (was row 4) — ran + CLOSED OUT: both rulings executed (policy-day COUNTS → RESHAPE-BC formal confirm; FT-01 UN-FIRED, HOLD 70→72) + S27/S27b | 7/31 | `976ca277` closeout; rulings packet PROME/inbox → processed; GATES row synced |
| Launch NEXUS (was row 7) — ran + CLOSED OUT: inbox drained, schema amendment 9 RATIFIED (Will-approved in-window), own closeout-doc audit 8 findings/5 fixed | 7/31 | `6a8067d9` / `89ec17df` / `a4d4c0db` |
| BRENT audit rulings ×4 — F3 pointer-replacement · F4 crack-line RETIRE · C2 index-carries-prose + checker opens prose · C6 stamps=agreement-checks; BRENT implements post-COT in the closeout pass | 7/31 | relay on BRENT's record ~12:50; implementation anchor = BRENT's closeout commit (verify at artifact) |
| REMAINING RULINGS BATCH — H1 announcement-anchored day+9 (was 5c; BRENT post-COT) · HENRY ×6 (magnitudes demoted, 0DTE dropped, ECI-row retired, TRADE.md=macro per recorded feedback, USD/JPY defer-to-SAM, stamp pattern adopted) · LABOR ×4 (quarterly cards, B5b-no-gate, spawn-floor/push docs, PUBLISHED.tsv build) · PROME mechanisms → DOCKET 8/6-8/9 row | 7/31 | ruling packets: LABOR+HENRY inboxes 2026-07-31_from-PROME_remaining-rulings; BRENT relay in-window |
| Memory-migration date (was row 3) — RULED pull-to-today, EXECUTED same session | 7/31 | `7b7727f0` (index split) + `5cce6942` (embeds); hot index 62% of cap |
| BRENT Stage-A (was row 5) — RATIFIED both legs + leg-(a) CLOSE basis, implemented+verified | 7/31 | `0832c484` (STAGE-A v4 in TRADE.md; STNG veto retired; follow-ups → row 5b) |
| Stage-A defect-② + sizing (was row 5b) — RULED C1 + half/half, implemented+verified; entry_timing contradiction resolved by phase-separation | 7/31 | `aede1959` *(hash remapped by the 11:46 rebase — was f459d824)* (v5: entry {(i)+(T)+(C)}, transit→Stage-B kill leg 2; local, push queued) |
| Launch SAM pre-BOJ (was row 1) | 7/30 ~22:00 | Will confirmed in-session at PROME boot; SAM live in own window, 13 dirty SAM paths incl. the yen packet `git mv`'d to processed |
| QQQ 680P — SOLD for a loss (strike corrected 675→680) | 7/30 | `be7f7bfa`; figures fold into row 16 |
| HEARTBEAT amendments #1 + #2 approved | 7/30 | `d7764309` / `8bb2ff35` |
| env_doctor venv probe approved | 7/30 | `f5a3655c` |
| BRENT LESSONS #21(a) — Option A ratified | 7/30 | `9523b941`; arm expiry ~8/13 docketed |
| LIQUID full closeout + shutdown | 7/30 | HEAVY closeout `1b39f0e6`, terminated 20:47 |
| LIQUID+REGINALD spawn: attribution + inbox passes + stale sweeps | 7/30 | BANK-ABSENT verdict → HEARTBEAT Am.#2 |
