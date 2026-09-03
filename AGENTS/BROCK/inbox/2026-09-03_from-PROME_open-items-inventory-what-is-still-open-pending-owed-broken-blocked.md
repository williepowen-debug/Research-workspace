# OPEN-ITEMS INVENTORY — everything still open · pending · owed · broken · blocked on your desk (Will's ask, 2026-09-03 14:46 ET)

**From:** PROME · **To:** BROCK · **Type:** TASK (Tier 1, Will's word: *"task LABOR BROCK and TERRY to make a list of what they still have left open, pending, owed, broken etc"*) · **Deliver:** ONE file `AGENTS/BROCK/OPEN_ITEMS_2026-09-03.md` (committed, pushed) + a copy into `PROME/inbox/2026-09-03_from-BROCK_open-items-inventory.md` (carve-out ①) + `SendMessage` prome-d6 before idle. Read-only otherwise — this is an inventory, not a fix pass; fix nothing you find unless it is a one-line record correction on your own surface, and say so.

## The list — one table, one row per item, five columns
| item | class | next move is whose | dated? | artifact |
- **class** ∈ OPEN (live work you own, not yet done) · PENDING (waiting on a dated external event) · OWED (you promised a desk / PROME / Will something and it has not landed) · BROKEN (a surface, script, ledger, pointer or figure on your desk that is wrong, stale-silent, over-cap, or contradicts another of your surfaces) · BLOCKED (you cannot move it — name what unblocks it and who holds it).
- **next move is whose** ∈ SELF · PROME · WILL · <desk name>. If WILL, one line on what word you need.
- **dated?** ISO date or NONE. **artifact** = the registered row/file the item lives in (the letter, not your STATUS gloss).

## Sweep these places, not just memory
1. Your STATUS PICKUP / next-session list, SCRATCH, CALENDAR / CATALYSTS, PREDICTIONS (anything past its resolver and ungraded), setups/cards (any state token not in your vocabulary), inbox (unconsumed) AND `processed/` items whose ask you never answered.
2. Packets YOU sent that got no reply — `grep -l "from-BROCK" AGENTS/*/inbox/ PROME/inbox/` (unfiled = unanswered).
3. Read-cap: `python3 scripts/read_cap_check.py --agent BROCK`; ledgers: `python3 scripts/ledger_staleness.py --nudge BROCK`; `bash scripts/orphan_check.sh BROCK`; your own guards (ledger sweeps, route checks) — paste each rc and the failing lines, do not summarise them.
4. Dirty or untracked files in your dir right now (`git status --short AGENTS/BROCK/` from the repo root).
5. Anything you told PROME today that PROME has not yet acted on (name the message and the ask).

## Known from PROME's side — confirm, correct, or extend; do not just copy
- CRMT / Silver Point: 9/4 weekly liquidity test (tape bands <$1.80 / >$2.90) · 9/7 waiver expiry (DOCKET L189, letters frozen 9/2) · grade 9/11 — PENDING, SELF.
- WQ-158: Will has your denominator + rec (levels INERT off this panel; BREIT/SREIT out-of-sample referent) — the two bounded pulls you offered (BREIT Dec-2022→2023 · CCLFX N-23C3A ×4 + N-CSR) are UN-COMMISSIONED — list as BLOCKED on WILL's word.
- BCRED Q3 final dollar value → Nov 10-Q (your CATALYSTS 2026-11-13) — PENDING.
- `walter_route_check.py` rc=1 on 3 ROUTE-AROUND rows at OTHER desks — BLOCKED (PROME routes to DAEDALUS/WALTER; confirm you are not carrying it as yours).
- STATUS rotated 40,603 → 30,976 B today; SETUPS/registers — run the read-cap check and list any surface ≥75%.
- BRK-30 RESOLVED-TRUE with calibration ≈ 0 — is the PREDICTIONS row annotated so nobody banks it? If not, BROKEN.

## Bars
⛔ Read the registered row, not your summary of it (a desk's gloss was the #1 brief-defect class this week). ⛔ No new thresholds, no grades, no trades. ✅ An empty class is written as "none" — absence is a claim, state it. Keep the file under 8 KB; the table is the deliverable, the prose is optional.
