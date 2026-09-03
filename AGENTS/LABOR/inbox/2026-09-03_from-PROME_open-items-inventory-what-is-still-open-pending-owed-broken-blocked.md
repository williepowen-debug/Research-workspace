# OPEN-ITEMS INVENTORY — everything still open · pending · owed · broken · blocked on your desk (Will's ask, 2026-09-03 14:46 ET)

**From:** PROME · **To:** LABOR · **Type:** TASK (Tier 1, Will's word: *"task LABOR BROCK and TERRY to make a list of what they still have left open, pending, owed, broken etc"*) · **Deliver:** ONE file `AGENTS/LABOR/OPEN_ITEMS_2026-09-03.md` (committed, pushed) + a copy into `PROME/inbox/2026-09-03_from-LABOR_open-items-inventory.md` (carve-out ①) + `SendMessage` prome-d6 before idle. Read-only otherwise — this is an inventory, not a fix pass; fix nothing you find unless it is a one-line record correction on your own surface, and say so.

## The list — one table, one row per item, five columns
| item | class | next move is whose | dated? | artifact |
- **class** ∈ OPEN (live work you own, not yet done) · PENDING (waiting on a dated external event) · OWED (you promised a desk / PROME / Will something and it has not landed) · BROKEN (a surface, script, ledger, pointer or figure on your desk that is wrong, stale-silent, over-cap, or contradicts another of your surfaces) · BLOCKED (you cannot move it — name what unblocks it and who holds it).
- **next move is whose** ∈ SELF · PROME · WILL · <desk name>. If WILL, one line on what word you need.
- **dated?** ISO date or NONE. **artifact** = the registered row/file the item lives in (the letter, not your STATUS gloss).

## Sweep these places, not just memory
1. Your STATUS PICKUP / next-session list, SCRATCH, CALENDAR / CATALYSTS, PREDICTIONS (anything past its resolver and ungraded), setups/cards (any state token not in your vocabulary), inbox (unconsumed) AND `processed/` items whose ask you never answered.
2. Packets YOU sent that got no reply — `grep -l "from-LABOR" AGENTS/*/inbox/ PROME/inbox/` (unfiled = unanswered).
3. Read-cap: `python3 scripts/read_cap_check.py --agent LABOR`; ledgers: `python3 scripts/ledger_staleness.py --nudge LABOR`; `bash scripts/orphan_check.sh LABOR`; your own guards (ledger sweeps, route checks) — paste each rc and the failing lines, do not summarise them.
4. Dirty or untracked files in your dir right now (`git status --short AGENTS/LABOR/` from the repo root).
5. Anything you told PROME today that PROME has not yet acted on (name the message and the ask).

## Known from PROME's side — confirm, correct, or extend; do not just copy
- NFP 2026-09-04 08:30 on `docket/GRADING_CARD_20260904_NFP.md` (T-03 fires on flat 58.9 EPOP → route CARL + HENRY same day; LEG A ≥+303K; T-06 U-3 ≥4.3%; T-04 ≤58.8) — PENDING, SELF.
- PARKED to 9/5 (your STATUS PICKUP #7): obligation-diff on the BD-25 split; DAEDALUS route-around fix at CLAUDE.md L121/L291 — OPEN, SELF.
- B2a spine_check read CANNOT-VERIFY this boot before your ISO-token fix — confirm it resolves next boot or list as BROKEN.
- Attribution bar (no demand-vs-supply attribution before NFP is graded) — a standing constraint, list it under PENDING with its release condition.

## Bars
⛔ Read the registered row, not your summary of it (a desk's gloss was the #1 brief-defect class this week). ⛔ No new thresholds, no grades, no trades. ✅ An empty class is written as "none" — absence is a claim, state it. Keep the file under 8 KB; the table is the deliverable, the prose is optional.
