# HEARTBEAT Amendment 2 (2026-11-11) — sources, one row per claim

Candidate text: `candidate.md` in this directory (one paragraph, inserted after Amendment 1; the header's "Amendment chain: 1." becomes "Amendment chain: 2."; no base cell is edited, matching Amendment 1's form). `(TIMESTAMP ET)` is replaced from `date` at the edit.

| # | Claim in the candidate | Owner artifact |
|---|---|---|
| 1 | SoftBank 22.5% own basis; 23.4 to 23.9% ABB-inclusive; Arm $181.49; USD/JPY 158.81 Tokyo close 11/11; 25% at about Arm $143 own basis and $156 to $164 ABB-inclusive; +0.04 point per yen of yen strength | `AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-11_TOKYO_SESSION_READ.md` lines 74 to 103 (commit d346a52192) |
| 2 | Superseded figures exist as stated: 22.9%, 23.6 to 24.0%, $159 to $166 in Amendment 1; "near Arm $145" in channel 4 | `HEARTBEAT.md` (current) |
| 3 | SAM's old command prints a warning before any figure; model unchanged | `AGENTS/SAM/research/outputs/2026-11-06_softbank/ltv_lookup.py` (commit 56154ee62d); run `python3 ltv_lookup.py --nd 11.30 --v 71.14 --arm 181.49 --svf2-inside --fx 145` in that directory |
| 4 | 115 headlines; 13 covered, 5 stale, 2 new; Wingspire $407M; Stonebriar $869M; Korea's five big banks; boot scan change | `AGENTS/WALTER/research/2026-11-11_aicapex-review/BACKLOG-TRIAGE.md`; `BOARD/SIG-W-20261111-021-*`; WALTER commit 51f93609ff |
| 5 | SoftBank 5Y CDS 475 [11/11 one trade], 497 [11/9], 496 [11/10]; no rating action found | `PROME/inbox/processed/2026-11-11_from-LIQUID_catchup-softbank-skydance-coreweave-hy-pending.md` lines 19 and 22 |
| 6 | CoreWeave FY2026 capex guide $37 to 39B, low end raised from $35B | `AGENTS/VULCAN/workbook/KB.tsv` KB-VULCAN-417 (and KB-VULCAN-412 for the prior $35 to 39B) |
| 7 | 11/10 HY cell not posted; expected Thu 11/12 about 10:10 ET | same LIQUID packet, lines 9 and 10 |
| 8 | Saudi 10.563 production; 9.203 supply to market; 9.194 secondary sources | `BOARD/SIG-W-20261111-013-*` |
| 9 | Gold 11/10 graded RATE; real 10Y +12 bp to 2.78%; 3.00% line | `PROME/inbox/processed/2026-11-11_from-MIDAS_1110-gold-rate-grade.md` lines 8 to 10 |
| 10 | ORACLE owns December pricing (WQ-671 A); hold 3.5, +25 85.5, +50 or more 11.8, Polymarket 11/11 09:45 ET; futures +28.9 bp vendor last trades | `PROME/proposals/2026-11-11_wq671-RULED.md`; `PROME/inbox/processed/2026-11-11_from-ORACLE_catchup-read.md` lines 12 to 21 |
| 11 | Skydance: deal synergies uncapped in covenant EBITDA; TERRY's four triggers; indentures unread | `PROME/themes/ellison/reports/2026-11-11_skydance-credit-agreement-addbacks.md`; `PROME/inbox/processed/2026-11-11_from-TERRY_skydance-credit-agreement-no-card.md` |
| 12 | Capital One 17.23% to 25.15%; no sourced cause; whole-book 3.74% delinquency and 3.98% net charge-offs better than a year earlier | `AGENTS/DEWEY/output/2026-11-11_capital-one-discover-cause-addendum.md` |
| 13 | Multifamily special servicing 9.22% October, Trepp, 2026 high; Arbor down 61% in 30 sessions, cause unchecked; WQ-675 | `PROME/inbox/processed/2026-11-11_from-HOMER_catchup-live-data.md`; `PROME/inbox/processed/2026-11-11_from-TERRY_japan-tobacco-and-multifamily-tradeability-no-card.md`; `PROME/WILL_QUEUE.md` row 675 |
| 14 | Tricolor meeting moved to 2027-03-17 | `PROME/inbox/processed/2026-11-11_from-OTTO_D-L133-tricolor-341-continued-and-catchup.md` |
| 15 | GATE-FALCON-001 leg 2 NOT MET, 94.9% against 65% or less, review 11/18 | `PROME/inbox/processed/2026-11-11_from-FALCON_weekly-gate-review-card008.md` line 26 |
| 16 | TERRY: eleven tradeability reads, no card | `PROME/reports/2026-11-11_no-card-reads-review.md`; TERRY packets under `PROME/inbox/processed/2026-11-11_from-TERRY_*` |

Not carried into the amendment, on purpose: intraday index and oil levels (not owner grades; BRENT reports after 14:45 ET); Japan Tobacco (one unread primary figure decides it; told to Will in chat); the weekly petroleum report's shift to Thursday.

## Read record

**Candidate read (Opus, `reader-hb-amend2`, returned 13:1x ET; ledger `reader_hb_amend2.md` in the session scratchpad): NOT ACCEPTED on the first candidate, 2 failures, 13 warnings; 19 of 20 figure rows matched their owner files.**

| Finding | Disposition in the revised candidate |
|---|---|
| F1: 22.9% (with the SB7 settlement) was superseded by 22.5% (own basis), a different basis | FIXED: 22.8% with the settlement is stated, and each old figure is paired with its like-for-like successor |
| F2: Amendment 1's kill-on-sight item "SoftBank has 22.7% leverage" was not named | FIXED: named in the supersession list and in the pairing sentence |
| W1 Arm $181.49 undated · W2 the 62% foreign-share assumption · W3 CDS conversion error · W4 delinquency up from Q2 · W5 "unexplained" against "cause not checked" · W7 anonymous sources and the helper · W9 the no-cap reading · W10 "whose last read is 11/8" · W11 HENRY's 11/10 December figures and the ORACLE kill item · W12 delivered, not read by BROCK · W13 the kill string's qualifier | TAKEN in the same fix pass, each a wording change the result read covers |
| W6 the conditional Japan Tobacco long is not in the memo | RESIDUE, left out on purpose: no card exists and one unread primary figure decides it |
| W8 the triage file shows 9 covered rows and "batches from 10/11" where WALTER's card and message say 13 and 10/10 | RESIDUE: the candidate attributes the counts to WALTER; the row-level mapping is WALTER's and was by hand |
| W3 remainder (n = 3, 3-year flat, yen bonds +1.5 bp) | RESIDUE: detail stays in LIQUID's packet |
