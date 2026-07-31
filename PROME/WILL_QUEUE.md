# WILL_QUEUE.md — the operator's open-items ledger
**Owner:** PROME (registers, updates, retires rows; reconciles at every boot/closeout) · **Will edits freely** — anything marked/struck here is reconciled at PROME's next touch.
**Last reconciled:** 2026-07-30 (~22:00 ET boot — row 1 DONE: Will in SAM's window pre-BOJ)

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
| 2 | Close REGINALD's window | ACTION | 2026-07-31 | 7/30 | glance at the pane | re-dated at 7/31 closeout (was 7/30, PASSED unreconciled — pane state unknown to PROME); its closeout is committed+pushed, this is only the window itself |
| 3 | Memory-migration date | RULE | 2026-07-31 | 7/29 | **pull to 7/31** | index at 86% of auto-load cap and climbing (2 new memories 7/30); default window 8/1-8/2 |
| 4 | Launch RED | LAUNCH | 2026-07-31 AM | 7/30 | pair with HY print #4 | RED's 2 rulings gate RESHAPE-BC formal confirm + FT-01 un-fire; print #4 publishes ~7/31 and decides if FOMC-day is excluded |
| 5 | BRENT Stage-A dispersion-test replacement | [Approve] | 2026-07-31 (BRENT's window) | 7/30 | — | ⛔ waits: BRENT live window · the STNG veto has zero discriminating power (rose on BOTH real and false de-escalations); flagged OPEN by BRENT's own self-audit `672fc1e5` |
| 6 | scripts/-ownership ruling | RULE | 2026-08-02 | 7/30 | — | closeout-critical tooling (safe-push, env_doctor, ledger_staleness...) lives unowned; DAEDALUS gap (c), PAT-071 next application; the 7/31-8/2 conversation |
| 7 | Launch NEXUS | LAUNCH | 2026-08-03 (before BDC cluster) | 7/28 | sooner is better | 29/31/40 mark is 7/28-vintage; inbox holds FOMC/HY/yen moves; staleness compounds into 8/4-8/6 |
| 8 | QQQFADE approval (`TRY-WILL-QQQFADE`) | [Approve] | none (Sep-18 tenor) | 7/30 | — | TERRY's 2 conditions (re-based premise + Target-1 policy); PROME rider "sell the 675P first" is MOOT (put sold 7/30); register Will-discretionary class on fill |
| 9 | Bank-put reshape disposition | RULE | after RED's ruling | 7/30 | TERRY rebuilds from 7/30 export; no fresh capital absent X1 | ⛔ waits: RED ruling · LIQUID's narrower-thesis brief delivered 7/30; BANK-ABSENT attribution strengthens the narrow framing |
| 10 | Fresh rising-vol registration — go/no-go | RULE | none | 7/30 | — | your own 7/30 AM question; VIOLET owns the proposal on GO; nothing pre-committed |
| 11 | NO_HARVEST_RULE → fleet card templates | RULE | none | 7/30 | **adopt** | build-time check: "is there a path where this is profitable and NO trigger fires?"; already fleet memory; TERRY wires its own templates regardless |
| 12 | HENRY standing boot-rule blessing | RULE | none | 7/28 | mechanical-trigger version | inbox-at-boot rule change, PROME rec on record |
| 13 | FFIEC CDR account | BUY | none | 7/28 | do it (5 min) | DAEDALUS's ask |
| 14 | DEWEY entitlement purchase | BUY | blocked on DEWEY | 7/25 | — | ⛔ waits: DEWEY one-liner · Tier 1 ruled 7/25; DEWEY owes the product/tier/price one-liner first; you spend only on that |
| 15 | RAV charter review → formal ROSTER row | RULE | none | 7/25 | — | DAEDALUS drafted the charter 7/30 (`2b9dbeac`); your review unlocks the registry row |
| 16 | Next broker export + confirms bundle | BROKER | none (next export) | 7/24 | — | one export resolves: off-rail confirms D-1/2/3 (AAPL/GLD/USO→35 ⇒ concentration packets fire), D-6 USO-spread account, D-7 $565+$1,500, D-10 MAIN≟IRA label, tail-rider debit, QQQ 680P figures + strike re-verify, VIXCS timestamped order (settles TERRY's S3 carry) |
| 17 | Repo public flip | ACTION | none | 6/30 | — | all pre-flip blockers closed since 7/4; flip ⇒ delete DESKTOP mirror backup + Phase-5 verify |

## RECENTLY DONE (rolls off ~7d)

| Item | Done | Record |
|---|---|---|
| Launch SAM pre-BOJ (was row 1) | 7/30 ~22:00 | Will confirmed in-session at PROME boot; SAM live in own window, 13 dirty SAM paths incl. the yen packet `git mv`'d to processed |
| QQQ 680P — SOLD for a loss (strike corrected 675→680) | 7/30 | `be7f7bfa`; figures fold into row 16 |
| HEARTBEAT amendments #1 + #2 approved | 7/30 | `d7764309` / `8bb2ff35` |
| env_doctor venv probe approved | 7/30 | `f5a3655c` |
| BRENT LESSONS #21(a) — Option A ratified | 7/30 | `9523b941`; arm expiry ~8/13 docketed |
| LIQUID full closeout + shutdown | 7/30 | HEAVY closeout `1b39f0e6`, terminated 20:47 |
| LIQUID+REGINALD spawn: attribution + inbox passes + stale sweeps | 7/30 | BANK-ABSENT verdict → HEARTBEAT Am.#2 |
