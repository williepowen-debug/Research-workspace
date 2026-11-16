# FLG -> PROME: inbox drained, due rows, who is paying to extend, read cap

**From:** FLG (Claude Code, Opus 5.5, model id claude-opus-5-5; session spawned by PROME prome-6f) · **Written:** 2026-11-16 14:09 ET (system clock) · **Basis:** PROME's assignment on Will's word in PROME's chat 13:45 ET today.
**Commits (local, NOT pushed, per your instruction; no pull):** `34d6a74649` (record) · `66ec412e03` (NEXUS brief fold) · this packet's own commit.

**Bottom line:** nothing graded moved: no threshold, kill condition, prediction, trigger date or thesis direction. No trade, no card. The new lines say Flagstar itself carries most of the delay on its stressed multifamily loans, and its modification terms run out around late 2027 to early 2028.

## 1. Inbox: 4 packets, all filed to `AGENTS/FLG/inbox/processed/`

| Packet | Disposition | What it changed |
|---|---|---|
| DEWEY 003R full-population refresh (11/11) | LOG, KB-FLG-119 | Nothing in FLG's figures. FLG's $10-100B band: the QoQ trigger is OFF. The $1-10B jump is 69.1% one bank (United Fidelity, about $2.14B of multifamily placed on nonaccrual while current, per its own text). The relay caveats are carried on the row |
| DEWEY 003R placement continuation (11/11) | LOG, same row | Nothing. FLG is not in the six-bank placement and cites none |
| DEWEY 003R six-bank partial (11/11) | LOG, same row | Nothing. Information only, as the packet says |
| DAEDALUS WQ-678 harness lines (11/12) | INTEGRATE | `AGENTS/FLG/CLAUDE.md`: Changelist A had none for FLG. I applied all 7 optional Changelist B trims. C36 was applied in part: I struck the boot-card retelling and kept the one-line provenance pointer in § DENOMINATOR DISCIPLINE, because it is the only path to the archived history. Every struck history line is already verbatim in `archive/CHARTER_HISTORY_2026-10-28.md` §2, §4 and §7. The gate count moved out because STATUS carries it. No authority, route or threshold moved |

Ruling verified at `PROME/proposals/2026-11-12_wq678-RULED.md`. The three DEWEY packets share one KB row, not one each, because they point to one 003R series.

## 2. Own open rows: none due

boot.py came back clean on all three scans: predictions, triggers and quarter-due. The calendar's next dated row is T-12 on 2026-12-31. All DOCKET rows naming FLG are RESOLVED or tombstoned except two:
- **L810 (charter hot/cold split), FLG leg:** done this session by the WQ-678 trims, not by a reference-file split. `AGENTS/FLG/CLAUDE.md` went from 22,837 B to 21,929 B, which is 67% of budget and under the 70% stop. **For you to verify at the diff and mark.** If L810 strictly requires a companion-file split, say so and I will do one.
- **L554:** this is NEXUS's weekly wake, due 11/17. It is not FLG's to grade.

Nothing was pre-graded.

## 3. Who is paying to extend: 5 lines, logging only

These lines move no score, band, gate or trigger. They live in `AGENTS/FLG/workbook/KB.tsv` rows **KB-FLG-120 to 124**, and STATUS § SESSION 2026-11-16 summarises them. **Count: 4 have a named payer and 1 is UNKNOWN. On how long the payer can keep going, 2 are dated, 1 is dated only by the reset, and 2 are UNKNOWN or have no dated limit.**

| # | Stressed credit | Who is paying to extend | How long, on the evidence held |
|---|---|---|---|
| 120 | NYC multifamily non-accrual book (MF NAL $2,125M; $1,548M of whole-bank NAL has no allowance; 10-Q 9/30) | Flagstar, which holds the loans at appraised value instead of selling them (call: no note sale "on the table"). Borrowers also pay: about 42% of NALs are performing (deck 9/30) | The bank's clock is the re-appraisal and the Q2 review each year: Q2-2027, with the freeze year reviewed in Q2-2028. Its capacity is total risk-based capital of $9,804M and CET1 of 12.38% (Call Report 9/30). Borrowers' capacity is UNKNOWN |
| 121 | Multifamily modified loans ($471M 12-month stock, 43.9% past due, 9/30) | Flagstar, through lender modification: in Q3, $79M at 8.87% → 4.97% plus 1.5 years; in Q2, $259M at 7.68% → 5.17% plus 1.2 years | About 1.2 to 1.5 years of added term, so roughly late 2027 to early 2028 (derived from averages, not loan-level). Next read: the 10-K, about 3/1/27 |
| 122 | NY rent-regulated option loans ($8.5B; $3.0B reprice within 12 months) | The borrower's property cash flow at the reset rate. The loan stays on the book by contract, and the freeze caps rent growth at 0% | Capacity UNKNOWN (no DSCR disclosure). The dated item is the reset itself, $3.0B by about 9/30/27 |
| 123 | 2027 multifamily fixed-rate maturities ($1,581M) plus $119M past maturity | **UNKNOWN**: not disclosed per loan. Outside lenders are funding exits today (Q3 MF par payoffs $837M, 39% substandard) | UNKNOWN. The maturities fall through 12/31/27 |
| 124 | Flagstar itself | In 2024, rescue equity: $1.05B led by Liberty 77, which still holds board seats. Today there is no outside payer, and the bank is returning capital (about $216M buyback in Q3) | No dated limit on the evidence held. The 5.90% 2028 and 4.125% 2030 notes sit in Tier 2, and their sizes are not yet read (10-K) |

⚠️ **Caveat that must travel:** lines 121 and 122 rest on issuer weighted averages and on the contract structure of the loans, not on loan-level data. Line 124's 2024 raise figure comes from TERRY's EDGAR-verified relay (KB-FLG-097), which FLG did not re-pull this session.

## 4. Read cap (`scripts/read_cap_check.py --agent FLG`): rc 0, nothing over the 75% line now

| File | Before | After | How |
|---|---|---|---|
| `workbook/TRIGGERS.tsv` | 27,943 B, **86%** (rotate tier) | 21,630 B, 66% | 6 superseded segments moved verbatim, each with a crc32, to `archive/TRIGGERS_NOTES_ARCHIVE_2026-11-16.md`: the header's prior-refresh chain, T-03/T-07/T-08/T-12 notes, and the RETIRED T-13 row. Each one leaves a pointer behind. A segment-by-segment check found nothing lost, and boot.py still parses 12 rows with none due |
| `CLAUDE.md` (FLG) | 22,837 B, 70% | 21,929 B, 67% | WQ-678 trims (item 1) |
| `STATUS.md` | 22,025 B, 68% | 21,668 B, 67% | The 11/07 block moved verbatim to `archive/STATUS_ARCHIVE_2026-11-16.md` (crc32 `ce872535`), keeping STATUS under 75% after today's block |

FYI, not mine: root `CLAUDE.md` measures 23,756 B, which is 73% of budget with 656 B of headroom before the 75% trigger.

## Trade read

**No finding for TERRY. No direction:** every line restates figures already filed and graded on 11/07 and 11/11, and none of them moves a score or threshold. No price was cited.

## Notes

- **Runtime:** Claude Code, Opus 5.5, Linux (WSL2). Tools were available as needed (shell, file edit, SendMessage via the deferred-tool loader). These MCP connectors failed to connect: pdf-viewer, Prisma-Local, Definite and MT Newswires. None was needed.
- **Commission delivery:** PROME's "who is paying to extend" commission packet went to HOMER and BROCK (and per its text OZK). No FLG copy is in my inbox; I worked it from your spawn brief.
- **Git:** no pull and no push (GitHub name lookups are failing today). I committed only explicit paths under `AGENTS/FLG/` plus this packet (carve-out ①). The boot banner showed the branch AHEAD by 4 before this session. Other desks' dirty files (CREED, WAL) were left untouched. Closeout steps 1c and 1d do not apply: no figure was superseded and no memory was written. Step 1e claim check: clean. Step 1b orphan check: only other desks' files, labelled not mine.
- HOLDING open until PROME asks for closeout.
