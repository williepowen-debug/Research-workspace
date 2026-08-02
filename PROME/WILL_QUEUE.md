# WILL_QUEUE.md — the operator's open-items ledger
**Owner:** PROME (registers, updates, retires rows; reconciles at every boot/closeout) · **Will edits freely** — anything marked/struck here is reconciled at PROME's next touch.
**Last reconciled:** 2026-08-02 (phone session, branch `claude/prome-startup-docs-hpdy52` — row 18 CLOSED via SAM proxy spawn + Will disposition; ⚠️ merge branch before next desktop boot reads this file). Prior: 2026-07-31 (~16:45 ET closeout — FULL artifact-check swept all rows; 9 rows closed; row 18 added)

**Rules (v1, deliberately dumb — one markdown table until real use earns more structure):**
- **Only items where WILL is the actor.** Types: `LAUNCH` (agent windows) · `[Approve]` (trade/proposal) · `RULE` (canon/disposition) · `BROKER` (exports/confirms) · `BUY` · `ACTION` · `READ`. Fleet work lives on DOCKET + agent boards — the moment an item stops needing Will, it leaves this file.
- Dated rows first (soonest). Hard dates are ISO in the Needed-by column — `prome_gate` reads them (boot+closeout advisory: flags passed dates and a stale reconcile stamp; adopted at birth per `finding_hygiene_commit_rearms_the_staleness_lie` — a schedule decays like any surface).
- **This is the ONLY live copy.** SCRATCH operator card carries a 3-line pointer view; HANDOFF "Open for Will" entries are dated history, not the live list.
- **Blocked rows** carry `⛔ waits: <who>` at the start of Notes — they are NOT Will-actionable, are excluded from the cap, and the blocker must itself exist as a packet/DOCKET item (never a silent wait). *(DAEDALUS W3.)*
- **Hand-off rule:** when a DOCKET catalyst produces an action only Will can take, PROME opens a row here AT THE SAME TOUCH and cross-references both ways. *(DAEDALUS W4.)*
- DONE rows: one line, **durable anchor (commit hash / named record) REQUIRED at write** — then roll-off after ~7d is always safe; the gate flags overdue roll-offs. *(DAEDALUS W5.)*
- Soft cap **20 ACTIONABLE rows** (dated + unblocked); undated unblocked rows get a **21d age tripwire** instead — an old undated row means the item needs a date, a decline, or a re-scope, not that Will is behind. *(DAEDALUS W2.)*
- ⚠️ Needed-by runs at **DAY resolution** — time-of-day text (`~22:00 ET`) is for the reader; the gate parses dates only.
- **Artifact-verify per presentation (adopted 2026-07-31, the QQQFADE lesson):** any row that mirrors ANOTHER AGENT'S card/proposal state must be re-verified at the owning artifact BEFORE each presentation to Will — reconciles check dates; this rule checks VERDICTS. A row carrying a superseded verdict manufactures decisions the operator already made.

## OPEN

| # | Item | Type | Needed by | Since | PROME rec | Notes |
|---|---|---|---|---|---|---|
| 12 | HENRY standing boot-rule blessing | RULE | none | 7/28 | mechanical-trigger version | artifact-checked 7/31: WALTER-lane inbox step ALREADY exists (CLAUDE.md 3a); the open half is the GENERAL inbox at boot — bless the mechanical version of that half only |
| 13 | FFIEC CDR account | BUY | none | 7/28 | do it (5 min) | artifact-checked 7/31: still live + load-bearing — DAEDALUS STATUS names it the Will-side blocker that UNBLOCKS WAL MI3 (WAL wired a boot reminder waiting on it) |
| 15 | RAV charter review → formal ROSTER row | RULE | none | 7/25 | — | DAEDALUS drafted the charter 7/30 (`2b9dbeac`); your review unlocks the registry row |
| 16 | Next broker export + confirms bundle | BROKER | none (next export) | 7/24 | — | one export resolves: off-rail confirms D-1/2/3 (AAPL/GLD/USO→35 ⇒ concentration packets fire), D-6 USO-spread account, D-7 $565+$1,500, D-10 MAIN≟IRA label, tail-rider debit, QQQ 680P figures + strike re-verify, VIXCS timestamped order (settles TERRY's S3 carry) |
| 17 | Repo public flip | ACTION | none | 6/30 | — | all pre-flip blockers closed since 7/4; flip ⇒ delete DESKTOP mirror backup + Phase-5 verify |

## RECENTLY DONE (rolls off ~7d)

| Item | Done | Record |
|---|---|---|
| Launch SAM (was row 18) — RESOLVED via phone-session PROXY spawn (Will-directed 8/2, real-SAM integrates next boot): GATE-SAM-30 adjudicated VALID (own primary re-pull reproduced −163,412 = 90.8%), MEDIUM→MED-HIGH v1.6.11 provisional on 8/7; **Will APPROVED wait-for-8/7 + TERRY re-mark Mon 8/3**; GATES row RESOLVED, DOCKET 8/7 resolver row added, TERRY+HENRY packets dispatched | 8/2 | `22bcdf2f` (SAM proxy, 14 files) + disposition commit; adjudication memo `AGENTS/SAM/outbox/2026-08-02_to-PROME_sam30-refire-adjudication.md`; ⚠️ on branch `claude/prome-startup-docs-hpdy52` — merge before next desktop boot |
| Rising-vol go/no-go (was row 10) — RULED: GO, Option 1 trigger-gated; VIOLET commissioned (design at next session; entry keyed to her measurable signals; strikes deferred to TERRY at fire-time; 3 gates remain) | 7/31 | commission packet AGENTS/VIOLET/inbox 2026-07-31; pairs w/ the DAEDALUS ratchet packet |
| DEWEY entitlements (was row 14) — RULED: paste-path ADOPTED, buy nothing (DEWEY's own rec 1; $0; rider-2 review generates the escalation evidence; RatingsXpress quote = only-if-review-proves-slow, Will's form) | 7/31 | ruling packet AGENTS/DEWEY/inbox 2026-07-31; DEWEY memo 7/28 = the basis |
| Bank-put reshape disposition (was row 9) — RULED by Will 7/31 in-session: rebuild-no-fresh-capital (the standing rec), implementation = Mon 8/3 TERRY spawn | 7/31 | DOCKET 2026-08-03 row; deployment stays Will-gated on X1/wrapper |
| QQQFADE (was row 8) — RETIRED FROM QUEUE: the card's own operative verdict is ⏸️ PARKED/DO-NOT-ACTION (Will-directed 7/30 ~11:40, superseding the conditional verdict this row mis-carried since 7/30 — PROME error, owned 7/31 when Will asked for provenance). Card stays on TERRY's file; any future fade = fresh re-mark + thesis owner | 7/31 | `AGENTS/TERRY/setups/WILL_qqq-downtrend-putspread_2026-07-30.md` header verdict; live-mark check 7/31 (~$361, ~6.9:1) recorded in-session |
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
