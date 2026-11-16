# DEWEY -> PROME: United Fidelity brokered-deposit funding, Call Report read

**From:** DEWEY (dewey-61, Claude Code, Opus 5.5) | **To:** PROME prome-6f | **Date:** 2026-11-16 ~11:20 ET
**Authority:** PROME assignment on Will's word, 11:05 ET today ("Lets look into these"). Research only. It moves no gate, level, band, score, card or charter. Completing it is not a trading signal.
**Report:** `AGENTS/DEWEY/output/2026-11-16_ufb-brokered-funding-call-report.md` (commit a0f5f80727)

## Plain words (for Will as written)

1. The $510.5M figure is a real number from the bank's own Call Report, but it is not "brokered CDs maturing within a year". It also includes brokered savings and sweep balances that have no maturity date. The brokered CDs that actually come due within a year are at most about $363M.
2. Whether the bank has been rolling brokered money since its 2023 order cannot be settled from the filings alone, but there are signs it did. In Q2 2024 its long-dated brokered CDs went UP by $88M, which should not happen if it could take no new brokered money.
3. The bank also reported zero "brokered reciprocal" deposits every quarter while holding $825M to $1,032M of reciprocal deposits. Under the FDIC rule, that is allowed for a bank in its position mainly if it held an FDIC waiver. REGINALD's rule reading agrees a waiver is the most likely explanation. It is inferred, not confirmed: misreporting would also explain it, and no waiver record is public.
4. If there was a waiver, it stopped working on 10/30/2026, when the bank's Q3 filing put it in the "undercapitalized" category by rule. That would bar renewals of both the brokered deposits and the reciprocal deposits above the cap.
5. The bank replaced its brokered money mostly with its own CDs and larger uninsured deposits, not with loans from the Federal Home Loan Bank, where it has borrowed nothing since 12/2024.
6. At 9/30 it held about $239M of cash plus unpledged securities, against up to $363M of brokered CDs due within a year. That is a gap of about $124M if none can be renewed, or about $271M if the brokered sweep balances also leave. Most of its securities, $1.23B, are already pledged.
7. One caveat changes the picture: part of the 2026 decline in brokered deposits was the same sweep money relabeled as non-brokered, about $196M in Q1 2026, not money leaving the bank.

## Detail

| Item | Finding | Status |
|---|---|---|
| Quarterly table, 12/2023 to 9/2026 | 16 columns with schedule, item and MDRM code for each (report §1). 99 of 99 cells agree with the FDIC BankFind API copy. 9/30/2026 comes from DEWEY's own SDF file. | VERIFIED, primary |
| Items the form does not report | Brokered deposits maturing in three months or less: not on the form; HK07 and HK12 cover all time deposits. Brokered reciprocal deposits: RC-O item 9, RCONG803, 0 every quarter to 6/2026 and blank at 9/30/2026. | VERIFIED |
| $510.5M | RC-E memo 1.d.(1), RCONHK06 = $510,526 thousand at 9/30/2026. The instructions (RC-E-10) put ALL brokered demand and savings deposits of $250k or less in this item. Brokered sweeps are estimated at $147.5M (MT87 + MT89 + MT91 + MT93 − MT95), so brokered CDs within a year are at most about $363.0M. | Number VERIFIED; label CORRECTED; sweep split INFERRED |
| Run-off test | Q2 2024: brokered with more than a year left rose +$87.9M (direct sign of new or renewed long-dated brokered CDs). 2024: either $372M or more of non-sweep brokered balances held steady, or renewals took place. 2025 to 9/2026: close to consistent with run-off. Q1 2026: about $196M of the decline was sweep relabeling. | Mixed; the aggregate CANNOT be told from the form |
| Waiver | Zero brokered reciprocal while reciprocal was above the $626.9M pre-order average (or $727.85M on a Q1 2024 trigger). Under 12 CFR 337.6(e)(2)(i)(B), that fits a waiver. REGINALD's relayed reading: a waiver is most probable, alternatives weaker; a 2026 amendment, (e)(4), helps the bank only from 2026. | UNKNOWN; waiver INFERRED |
| Replacement | Brokered −$1,519.4M; non-brokered deposits +$1,389.3M; CDs over $250k +$469.0M; uninsured deposits +$401.9M; FHLB advances $80.0M to $0 (peak $200.0M at 3/2024). | VERIFIED cells; composition partly INFERRED |
| Q3 2026 | Assets −$577.9M, cash −$281.8M, deposits −$252.7M (reciprocal −277.1), pledged securities +$293.7M with no new borrowing on the form. Whom the collateral is pledged to is not on the form. | VERIFIED; pledgee UNKNOWN |
| Four-quarter arithmetic | Up to about $363.0M of brokered CDs due against about $239.1M of cash plus unpledged securities (book basis). HTM fair value is 85.6% of amortized cost. Timing within the year is not on the form. | Arithmetic only, no forecast |

**Trade-shaped:** none proposed. Will's standing instruction is that material findings go to TERRY for a tradeability read. That is PROME's routing call. DEWEY names no instrument.

**Not reached or skipped:**
- The September 2026 instruction update and the glossary entries were not read.
- No search was made for an FDIC waiver record.
- **SKIPPED:** the standard DEWEY WALTER handoff and recipient stubs. This assignment specified one packet, to PROME.
- Pull at boot was refused by Git because CORAL's tracked files were dirty; origin had no new commits.

**Open:** REGINALD is committing its own reading, and its hash goes to DEWEY. DEWEY is HOLDING open until PROME asks it to close.
