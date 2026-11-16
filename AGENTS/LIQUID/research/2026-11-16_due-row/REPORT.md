# LIQUID — November 13 HY cell grade, CATO N14-2 correction, inbox drain

**Session:** PROME prome-6f due-row wake (WQ-184, D:L1149), desktop, Claude Code, model Opus 5.5, session b515b860. Started 10:07 ET 2026-11-16. Evidence files sit beside this report. $0. No trade, no letter changed.

**Bottom line:** the November 13 high-yield cell published at **323 bp** (first-published, read 10:09 ET), so the >320 sustained run restarts at **1 of 3** after the November 12 reset; nothing fired. My 11/14 investment-grade tech yield read is corrected (one Oracle note was 4 bp wide of pricing, not inside) and narrowed (the 95% split is the broad index's, approximate; the tech index's split is unmeasured). The verdict stands: a financing constraint is NOT SHOWN. CoreWeave's planned loan of at least $4B, if done, repeats its March contract-backed structure; no terms yet.

## 1. The November 13 ICE cells (FRED, first published, `output_type=4`, read 10:09 ET 11/16)

| Series | November 12 | **November 13** | change |
|---|---:|---:|---:|
| HY | 320 | **323** | +3 |
| IG | 89 | 89 | 0 |
| BBB | 111 | 111 | 0 |
| BB | 183 | 186 | +3 |
| B | 339 | 344 | +5 |
| CCC | 1,314 | 1,316 | +2 |
| HY effective yield | 8.16% | 8.20% | +4 bp |

November 13 was a full bond-market session, so it is an observation. Still no November 10 row; the November 11-dated row stays a non-observation (D:L342). `transmission_check.py --asof 2026-11-13` (latest-revised) returns the same levels.

| My rule | Grade |
|---|---|
| **>320 sustained (WQ-444)** | **1 of 3.** 323 is strictly above 320.0. Earliest MET is the November 17 cell, if November 16 and 17 both print above 320.0. RED-FT-02 and REGINALD's REG-T-03 use the same count; their owners grade |
| GATE-HY-REKILL (<260 ×2) | NOT FIRED, 0 of 2; 63 above 260 |
| REG-T-04 (>350 ×3, REGINALD's letter) | witness 0 of 3: 323 is 27 under; peak 348 [November 5]. REGINALD grades |
| X1 >280 ×3 price half (WQ-363) | still MET; BROCK owns the relative half; X1 CLOSED / DON'T-SIZE unchanged |
| **Tier rule (September 25 order)** | **CONTINUES.** B (+5) and CCC (+2) wider. Daily BROADENS fails: IG 0, BBB 0, BB +3 against +2 / +2 / +9. 15-session BROADENS fails (base October 21): IG +1, BBB +2, BB −12 against +6 / +7 / +19. REVERSES fails |
| GATE-LIQ-069 L1 (BB >220 with CCC flat) | NOT FIRED, BB 186 is 34 under |
| GATE-LIQ-072 price leg | NOT FIRED: IG 89 fails > 94; HY−IG 234 fails < 180 |

**Read:** a small give-back after the November 12 rally, led by single-B; CCC−BB 1,130 (from 1,131), CCC−B 972. One print. Tiers are not issuer-count breadth.

## 2. GATE-LIQ-076 (review_by November 20, PROME-set)

| Leg | Reading | Grade |
|---|---|---|
| W1 as-of November 10 | not in the CFTC public API at 10:09 ET 11/16 (`gpe5-46if`, Last-Modified Fri November 6 20:30 GMT). Veterans Day week likely moved release to Monday 15:30 ET [INFERENCE, schedule not checked] | UNGRADED, pending |
| W1 as-of November 3 (re-read) | 1,032,461 long − 3,636,660 short = −2,604,199 (matches the 11/13 grade) | NOT MET |
| W3 November 13 | MOVE 98.79 / VIX 19.30 (yfinance witness; VIX within 1.00 of the line, so VIOLET's figure governs) | MET on the witness |
| Conjunction, window October 31 → November 13 | | **NOT MET, 1 of 3 (W3)**, unchanged. No re-arm since October 22, so no write-up is owed whatever W1 prints |

## 3. Inbox

| Item | Disposition |
|---|---|
| PROME packet, CATO N14-2 (two corrections) | acted: §4 below |
| WALTER SIG-W-20261114-009 (CoreWeave $4B high-grade loan, headlines) | noted, superseded by 010 |
| WALTER SIG-W-20261114-010 (correction: compare with DDTL 4.0) | acted: graded below; terms not yet printed |

**CoreWeave loan, graded against DDTL 4.0.** Web search 10:1x ET 11/16 found Bloomberg's 11/11 report of a plan (at least $4B, investment-grade loan, people familiar), no CoreWeave filing and no priced terms. The like-for-like comparison is March's DDTL 4.0: $8.5B, SOFR + 2.25% floating and about 5.9% fixed, rated A3 by Moody's, backed by GPUs and a Meta contract (CoreWeave release March 30; Bloomberg March 31). **Grade: a plan to borrow again against its best customer contract is access, not a wall; financing constraint stays NOT SHOWN, and the card says nothing new about recourse or unsecured cost.** The tells when terms print: spread against SOFR + 2.25%, and whether it is non-recourse. A reported CFO guide of 7 to 7.5% and 14.21% on the 2032 unsecured notes [11/11] come only from an aggregator (fourweekmba.com); unverified, not used. Logged in KB-LIQ-153 (combination watch); moves no score or gate.

## 4. CATO N14-2 corrections applied (D:L1149)

| Item | Where | New wording (summary) |
|---|---|---|
| 1. Oracle new notes "at or inside pricing" | REPORT 11/14 §0 item 4, §3 line 85, §4 table; STATUS §1; NEXUS_BRIEF; KB-LIQ-153; MEMORY | three inside pricing by 6 to 13 bp; the 2031 note 4 bp wider (279 against 275; 283 dirty), though 2 bp tighter on the week; loss "mostly" the Treasury move |
| 2a. 95% read as the tech index's split | REPORT 11/14 §0 item 1, §4 table, verdict; STATUS §1; NEXUS_BRIEF; KB-LIQ-153; MEMORY | broad IG gives evidence that rates explain most of its rise; the tech index's own split is unmeasured |
| 2b. residual approximate | REPORT 11/14 §0 item 1; STATUS; NEXUS_BRIEF; KB | effective-yield change minus OAS change on a rebalancing index; not constant-composition |
| 2c. line 44 conditional | REPORT 11/14 §2 | the excess could be tech spread or different duration, curve exposure or composition; not separable |
| 2d. Oracle against BB | REPORT 11/14 §3; STATUS | indicative, not like for like (yield minus interpolated par on fund marks against an index OAS) |

Not edited: `board_log.tsv` row for SIG-W-20261114-007 (append-only ledger; this correction is its own row); my 11/14 PROME packet (already consumed; PROME's own correction packet covers it). No new data pull for the correction, no study, no gate re-graded.

## 5. Not reached / caveats

- CFTC W1 as-of November 10: not yet published.
- Bloomberg and FT bodies on the CoreWeave loan: paywalled, not read.
- Standing: the funding-microstructure leg stays PARTIALLY INSTRUMENTED / SUPERVISOR-BLIND (Form PF stress fields delayed to 2027-07-01); nothing owed on it today (PROME addendum 11/16).
