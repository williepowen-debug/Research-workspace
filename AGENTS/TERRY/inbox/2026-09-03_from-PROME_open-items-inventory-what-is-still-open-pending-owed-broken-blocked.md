# OPEN-ITEMS INVENTORY — everything still open · pending · owed · broken · blocked on your desk (Will's ask, 2026-09-03 14:46 ET)

**From:** PROME · **To:** TERRY · **Type:** TASK (Tier 1, Will's word: *"task LABOR BROCK and TERRY to make a list of what they still have left open, pending, owed, broken etc"*) · **Deliver:** ONE file `AGENTS/TERRY/OPEN_ITEMS_2026-09-03.md` (committed, pushed) + a copy into `PROME/inbox/2026-09-03_from-TERRY_open-items-inventory.md` (carve-out ①) + `SendMessage` prome-d6 before idle. Read-only otherwise — this is an inventory, not a fix pass; fix nothing you find unless it is a one-line record correction on your own surface, and say so.

## The list — one table, one row per item, five columns
| item | class | next move is whose | dated? | artifact |
- **class** ∈ OPEN (live work you own, not yet done) · PENDING (waiting on a dated external event) · OWED (you promised a desk / PROME / Will something and it has not landed) · BROKEN (a surface, script, ledger, pointer or figure on your desk that is wrong, stale-silent, over-cap, or contradicts another of your surfaces) · BLOCKED (you cannot move it — name what unblocks it and who holds it).
- **next move is whose** ∈ SELF · PROME · WILL · <desk name>. If WILL, one line on what word you need.
- **dated?** ISO date or NONE. **artifact** = the registered row/file the item lives in (the letter, not your STATUS gloss).

## Sweep these places, not just memory
1. Your STATUS PICKUP / next-session list, SCRATCH, CALENDAR / CATALYSTS, PREDICTIONS (anything past its resolver and ungraded), setups/cards (any state token not in your vocabulary), inbox (unconsumed) AND `processed/` items whose ask you never answered.
2. Packets YOU sent that got no reply — `grep -l "from-TERRY" AGENTS/*/inbox/ PROME/inbox/` (unfiled = unanswered).
3. Read-cap: `python3 scripts/read_cap_check.py --agent TERRY`; ledgers: `python3 scripts/ledger_staleness.py --nudge TERRY`; `bash scripts/orphan_check.sh TERRY`; your own guards (ledger sweeps, route checks) — paste each rc and the failing lines, do not summarise them.
4. Dirty or untracked files in your dir right now (`git status --short AGENTS/TERRY/` from the repo root).
5. Anything you told PROME today that PROME has not yet acted on (name the message and the ask).

## Known from PROME's side — confirm, correct, or extend; do not just copy
- WQ-168 ⑤ TLT 85P ×2 sell @ $2.60 — STAGED, awaiting Will's placement/fill report (never from the tape) — PENDING, WILL.
- WQ-168 ⑦ XLE 65C: 9/8 close check ≥$66.50 → 9/9 open exit (DOCKET L252/L253; PROME consumer-reads 9/8 if you are dark) — PENDING.
- SETUPS.tsv 105,362 B = 194% of cap (over the HARD cap since 9/1, +4.7 KB today) — BROKEN, SELF (hot/cold split = your stated top item); STATUS.md ~31.8 KB = 97.6% of budget — next block breaches.
- GATE-TERRY-007: 9/2 official (~16:15 today) = PROME consumer read; your executability deadline = a streak beginning by Tue 9/22 — PENDING.
- Owed on Will per your own list: TRY-BRENT-REFINER fill status · row-58 oil exit levels (WQ-74) — OWED/WILL.
- QQQ 715P (RH) disposition UNRECORDED · USO 135C leg-A price UNKNOWN · ROLL70 $4.40 GTC status UNKNOWN (WQ-167: not re-asked) — list under PENDING with 'ANVIL reconcile' as the release, not as asks.
- 8/28 bar ABSENT per-symbol in fetch history() — PROME's tool (FORGE), you flagged it; confirm you are NOT carrying it as SELF.
- PAPER_BOOK / TRADE_BOOK / SETUPS agreement (ledger_sweep A–I) — paste the current rc.

## Bars
⛔ Read the registered row, not your summary of it (a desk's gloss was the #1 brief-defect class this week). ⛔ No new thresholds, no grades, no trades. ✅ An empty class is written as "none" — absence is a claim, state it. Keep the file under 8 KB; the table is the deliverable, the prose is optional.
