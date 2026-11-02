# FLG → PROME: Q3-2026 Call Report — T-01 ingested at the primary, WALTER card 026 verified, M3 step reconciled to a named 10-Q gap

**Date:** 2026-11-01 23:3x ET (Sun) · **From:** FLG (PROME C9 spawn on WALTER SIG-W-20261031-026) · **Commits:** `33500007c` (desk) · `e9f170314` (→ REGINALD) · `0367b4b20` (→ RED) · this memo + NEXUS brief in the delivery commit.

**Boot receipt.** Runtime Claude Code (Agent SDK), model Opus 5.5 (`claude-opus-5-5`), session ID UNKNOWN (not exposed), repo `/home/willi/Research-workspace` on `master`. Bounded reads to `eof: true`: root `CLAUDE.md` 5 pages (pages 3–5 fetched to EOF with metadata only — text consumed from the harness-injected copy of the same file, sha256 `065546be…`), `AGENTS.md` 1 page, `USER.md` 2 pages, `AGENTS/FLG/CLAUDE.md` 4 pages. `boot.py` rc 1 (inbox only); corrections check rc 0. `ListAgents` is not exposed in this session, so the REGINALD packet carries no MESSAGING rule-6 doorbell. Not pushed: FLG charter boot card item 3 says no push when spawned (coordinator sweeps).

## 1. T-01 at the primary (FFIEC CDR facsimile, RSSD 694904, pulled by FLG 23:18 ET; bank = issuer since 2025Q4)

The Q3 report was filed 10/30 (CDR last-update stamp), 15 days before the T-01 rule date. Pulled with a new FLG-only script (`scripts/ffiec_pull.py`); the Q2 facsimile re-pulled byte-identical to the 10/28 copy (no amendment). `MI3_FLG.tsv` 9/30 row ingested (PRIMARY); T-01 re-dated to the Q4 report, 2027-02-14.

| Ratio (numerator / denominator, $K) | 6/30/26 | 9/30/26 |
|---|---:|---:|
| SR 07-1: construction + multifamily + non-owner-occupied NFNR / total risk-based capital | 32,762,602 / 10,003,181 = 327.52% | **31,580,906 / 9,804,386 = 322.11%** |
| Non-accrual rate, Call Report basis (RC-N 1403 / loans 2122) | 4.88% | **4.81%** |
| Non-accrual rate, matched to issuer (ex GNMA rebooked, ex HFS / loans HFI) | 2,800,467 / 60,987,303 = 4.59% | **2,817,443 / 61,944,570 = 4.55%** |
| Coverage, Call Report basis (ACL 3123 / 1403) | 29.09% | **29.07%** |
| Coverage, matched basis (ACL / non-accrual ex GNMA, HFS) | 31.03% | **30.84%** |

The buyback cut total capital $199M and on its own would have lifted SR 07-1 to 334.16%; the CRE numerator fell 3.61% and more than offset it. No FLG routing line crossed (300% line, coverage ±10pp, non-accrual ±100bp). FLG-02 is graded only on the 10-Q ratio; 30.84% is a preview consistent with HIT (<31.04%).

## 2. WALTER's FLG figures, one by one (KB-FLG-100)

| WALTER figure | Primary | Verdict |
|---|---|---|
| Bank equity −6.10% (−$496.183M) | 8,140,809 → 7,644,626 | AGREE |
| RI-A: OCI −$291.966M; net treasury stock −$215.839M | B511, B510 YTD differences | AGREE. The bridge also needs income +12,117, stock +11,858 and dividends −12,353; with them it closes to $0 |
| CET1 13.1575% → 12.3821% | RCFAP793 | AGREE |
| Quarterly bank income $34.463M → $12.117M | RIAD4340 | AGREE |
| Quarterly NCO $99.415M → $74.116M | C079 − 4605 | AGREE |
| Provision $14.415M → $74.114M | RIAD4230 (loans and leases) | AGREE. Basis: loans only. Adding off-balance-sheet MG93 (+4,000 / +2,000) gives +$57.7M, which reproduces the release's "+$58 million" |
| RCFD2746 $440.610M → $679.072M (+54.12%) vs loans +1.50% | 2746, 2122 | AGREE |
| NDFI $3.457706B → $4.511574B (+30.48%) | RCFDJ454 | AGREE. MI3 ledger carries RCONJ454 = 4,511,572 (a $2K basis difference) |

The traps reproduce exactly: $2,989,320K − GNMA $167,641K − HFS $4,236K = $2,817,443K, which is the issuer's $2,817M. All three of WALTER's traps were adopted. Of the equity drop, 59% is OCI and 43% is the buyback, net of +2% from income and stock. It is neither a credit-loss nor a securities-loss figure.

## 3. K-1 leg 1 at 9/30

Bank multifamily (RCON1460, the series behind EXIT_PROTOCOL's healthy cell): **$26,922M → $25,965M, −$957M, −3.56% QoQ** (prior −5.63%, −3.95%, −3.36%). Run-off continued and the instrument is alive (it moved, inside the −3% to −6% band). Leg 1 is not satisfied. The release's MF HFI is $25,948M; the $17M difference is HFS. **Contribution to the post-10-Q re-derivation (not done now):** (a) a fifth Call Report point for leg 1; (b) the counter-thesis routing row, which is keyed on TOTAL loans, fired literally (+0.88%, +1.50%) while multifamily fell, so the old 8/28 K-1 form WOULD have fired here on C&I growth, which is evidence that the re-cut was right; (c) K-2's 9/27 note re-checked at both levels: numerator −3.61%, denominator −1.99%, so K-2 stays RESOLVED; (d) new pipeline observables to weigh (below).

## 4. The M3 step (+54% vs loans +1.5%): new lending, not reclassification. Which line holds it is a named gap (KB-FLG-101)

- **NDFI step = new lending, vertical-identified (Call Report Memo 10):** private-equity funds +$599M (+69%), business credit intermediaries +$470M (+233%). These match the issuer's Funds Finance / Lender Finance verticals (Specialized Industries +$1,417M). The issuer's "C&I +$2,016M" equals Call Report C&I + NDFI + municipal + leases (+$2,029M).
- **M3 total exposure grew +12.1%, not +54%.** Unfunded commitments for CRE finance not secured by real estate (RC-L 1.c.(2)) fell $910.8M → $836.4M. Funded + unfunded went from $1,351M to $1,515M, and utilisation from 32.6% to 44.8%. About a third of the funded step is draw-down of existing lines.
- **No reclassification signature:** no RC-C line falls to offset the step except secured-CRE run-off, which is a different object. The MDRM and prefix are the same in both quarters.
- **Unresolved:** which line holds the +$238M (C&I vs NDFI, e.g. lines to REITs, real-estate funds or CRE lenders). The Call Report does not cross-tabulate M3. The release and deck are silent. The IR-site "conference call" PDF is only the call announcement. My 10/28 call read (KB-092..094) has no passage on it. **Registered on T-02 (the 10-Q wake, check 11/09)**, not T-07/T-08 as the brief named: T-07 is the price ladder and T-08 the freeze trigger, while the 10-Q row is T-02. The ask: the MD&A C&I discussion by vertical (Funds / Lender / Sponsor Finance) and any loans-to-REITs or real-estate-fund disclosure. If silent, record "not disclosed — not resolvable from public filings" and stop.

## 5. L52 scope-checkpoint inputs (PROME/Will grade; FLG does not)

**Rent-regulation mechanism — still NOT instrumented at the transmission link.** (1) The Call Report has no rent-regulated split, so the RR book exists only in the issuer deck (≥50% RR ACL 2.87% → 2.97%) and in `MATURITY_WALL.tsv` / `RGB_GUIDELINES.tsv`. (2) Nothing measures rent → DSCR → default on the frozen collateral quarterly; the first borrower financials carrying a freeze year come in the Q2-2028 review (T-11). (3) New candidate observable from this print, not RR-specific: MF 30–89 days past due $233M → $392M.

**Bear case on this print — did not soften further; the early pipeline firmed modestly, the big levels did not.** Firmer: bank income $34.5M → $12.1M; MF 30–89 PD +68% (but Q1 was $676M, n=3, so not a trend); modified MF loans in compliance $199M → $264M and modified MF on non-accrual $153M → $207M; CET1 −77bp from the buyback. Softer or flat: SR 07-1 down to 322.11%; non-accrual flat at $2,817M; NCO down $99.4M → $74.1M; MF run-off continuing.

## 6. Inbox drained (whole: 2 items + PROTOCOL.md)

WALTER SIG-W-20261031-026 → **ACTED** (KB-100/101; `board_log.tsv` row; `git mv` to `processed/`). PROME FFIEC-token packet → **INTEGRATED** (T-01 note, KB-103; the 11/05 expiry lines refreshed). ⚠️ The new expiry, 2027-01-31, falls **14 days before** T-01's next check (2027-02-14).

**Thesis line for the held FLG Mar-19-2027 $10 put ×1:** this print leaves the thesis intact and adds no catalyst. Earnings are thinner and early multifamily delinquency rose, while concentration and the non-accrual level did not worsen. Construction stays TERRY's and the decision Will's (root rule #5). `TRADE.md` re-stated from the FORGE mirror.

**No prediction, threshold, kill cell or score moved.** Routing: REGINALD `e9f170314` (MI3/M3 adjudication inputs + total-loans routing) · RED `0367b4b20` (counter-thesis routing). Untracked `AGENTS/REGINALD/reports/2026-11-01_Q3-call-report_VLY-EGBN-HBAN/` is REGINALD's, not FLG's, so it was left unswept.

## COMPLETION — FLG — 2026-11-01
STATUS: ✅ DONE
CHANGED: AGENTS/FLG/{STATUS.md, TRADE.md, CALENDAR.md, NEXUS_BRIEF.md, board_log.tsv, workbook/MI3_FLG.tsv, workbook/KB.tsv (KB-099..103), workbook/TRIGGERS.tsv, archive/STATUS_ARCHIVE_2026-11-01.md, archive/TRIGGERS_NOTES_ARCHIVE_2026-11-01.md, scripts/ffiec_pull.py, sources/ffiec_2026-11-01/*, inbox→processed ×2}; packets REGINALD, RED; this memo
RESULT: Q3 Call Report pulled at FFIEC CDR and ingested (T-01 consumed, re-dated 2027-02-14): SR 07-1 322.11% (6/30 327.52%), non-accrual 4.81% CR / 4.55% matched, coverage 29.07% CR / 30.84% matched. WALTER's 8 FLG figures all AGREE. Multifamily −3.56% QoQ (K-1 not firing). M3 step = new fund/lender-finance lending, +12.1% on total exposure, no reclass signature.
GAPS: Which line holds the +$238M M3 step is undisclosed → T-02 10-Q ask (11/09). Issuer call transcript not on the IR site. ListAgents not exposed (no rule-6 doorbell). Not pushed (FLG charter: no push when spawned).
WILL_NEEDS: None now. FFIEC token (exp 2027-01-31) must be renewed before the Q4 Call Report (~2027-02-14), and pasted on the desktop at the next switch.
FOLLOW-UP: 10-Q wake ~11/6–11/9 (FLG-02/03 grade, M3 line, EXIT_PROTOCOL re-derivation in both directions); T-13 FDM read check 11/10.
