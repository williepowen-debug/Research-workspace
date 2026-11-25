# CRUISE -> PROME: aged-inbox drain, 2026-11-25

**From:** CRUISE (spawned by PROME prome-77, WQ-206 class, drain only) · **Written:** 2026-11-25 13:4x ET (`date` 13:40:52 ET) · **Runtime:** Claude Code, Opus 5.5 (claude-opus-5-5), Agent-tool spawn from PROME's cwd · **Session cut:** API outage about 13:30 to 13:36 ET; resumed from the working tree (only my untracked research folder existed), no work redone.

**Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 page · `USER.md` 3 pages · `AGENTS/CRUISE/CLAUDE.md` 4 pages. Boot checks: corrections rc 1 at boot (2 NAMED) then rc 0 after receipts; ledger staleness rc 0; read-cap rc 0 (rotation_due=1 advisory, STATUS 28,117 B by `measure.py`, under the 32,550 B cap).

## Result

The inbox held four WALTER cards, not six: the census counts `PROTOCOL.md` and `RECEIPT.md`, which are scaffold files. All four are logged and moved, and both corrections named for CRUISE are receipted NO-OP. WQ-670 A is encoded exactly as ruled. While the desk was dark, Carnival (CCL) closed in ORANGE once, on 11/20 ($26.59, 21.77% under the $33.99 reference). That was a market-wide day, and the stock was back in YELLOW from 11/23, so the desk total at the latest close is still 9/20. The Norwegian revolver reversal window closed on 11/23 with no 8-K, so the NOT SPRUNG grade stands and stays provisional until the 10-K. No score, band, level or trade path changed.

## Disposition table

| # | Item (oldest first) | Disposition | Record |
|---|---|---|---|
| 1 | WALTER SIG-W-20261117-006 (small items 11/16-17) | **noted**: item 10, Elliott raised its Norwegian stake, checked against the primary 13F-HR (filed 11/16): 17,686,000 NCLH shares at 9/30, up from 14,686,000 at 6/30 (+20.4%), $259.3M. Other items are not CRUISE's | KB-CRU-266, board_log |
| 2 | WALTER SIG-W-20261118-010 (HY OAS 343 bp, LIQUID >320 x3 MET) | **noted**: Norwegian is a B-tier issuer (B tier 368 bp on 11/17). This desk measures no Norwegian bond spread, and the card moves no score | KB-CRU-267, board_log |
| 3 | WALTER SIG-W-20261123-008 (Will's bookmarks) | **noted**: item 13, Disney Treasure turned back to Port Canaveral on 11/22. It is a scanner post, unverified, and Disney is not a Big-3 operator. Logged F6 for the port theme. Other items are not CRUISE's | KB-CRU-268, board_log |
| 4 | WALTER SIG-W-20261123-013 (correction of 20261116-005 item 2) | **info-only**: CRUISE used only item 8 of that card | board_log |
| 5 | COR-20261117-02 (Credit Acceptance part of 20261116-005 item 8) | **receipted NO-OP**: CRUISE logged only the NCLH 13G part of item 8 (KB-CRU-261), which the correction does not touch | `AGENTS/CRUISE/registry/corrections_receipts.tsv` |
| 6 | COR-20261123-13 (GPU-loan dates, item 2) | **receipted NO-OP**: no CRUISE record cites item 2 | same |
| — | WQ-735 honest-client-name packet | **Not present.** No such packet was in CRUISE's inbox, and CRUISE is not in the report's source table (`PROME/reports/2026-11-23_honest-name-test/REPORT.md`). CRUISE's only scripted outside source is SEC EDGAR, through `scripts/sec_contact.py` (SEC's required contact string). Nothing to switch, so no one-line reply is owed | — |

## WQ-670 A: verified at the artifact

| Check | Result |
|---|---|
| GREEN cell, `workbook/VX.tsv` row `VX-CRU-01` | "a fall of LESS than 10% from $33.99: any close above $30.591 is GREEN(1); one such close is enough (WQ-670 A, Will 2026-11-11)". This matches the ruling record `PROME/proposals/2026-11-11_wq670-RULED.md` § Consequence (VERIFIED) |
| YELLOW, ORANGE and RED cells, the $33.99 reference, the instrument | Unchanged ("-10 to -20%", "-20 to -35%", ">-35%"; raw 2026-02-06 close; raw Close) (VERIFIED) |
| Re-read at live closes | Done 11/14 (KB-CRU-254): GREEN(1) 11/9-11/11, YELLOW(2) from 11/12. Encoded on 11/14 and verified today; nothing changed in this session. PROME's NOW-page item 5, "CRUISE encodes WQ-670 A", can close |

## Rows, gates and predictions due while dark

| Item | Disposition, by the desk's own rules |
|---|---|
| `VX-CRU-01` closes 11/17-11/24 | Graded each close: 11/20 **ORANGE(3)** (−21.77%); all other closes YELLOW(2). State at the latest close (11/24, $28.40, −16.45%) is **YELLOW(2)**, Last_Changed 2026-11-23. No cell changed. KB-CRU-264 |
| D:L715 reversal window (an 8-K by Mon 11/23) | **Closed, no reversal.** EDGAR submissions 11/14-11/25: NCLH filed only the 11/16 13G, CCL filed nothing, RCL filed one Form 4. The grade stays NOT SPRUNG, provisional, and the 10-K certifies (L1074). This is CONDITIONAL on press pages, which were not read. KB-CRU-265 |
| KB rows past Stale_By (status ACTIVE) | 9 rows: **8 retired** (155, 158, 163, 222, 244, 249 to STALE; 255, 262 to SUPERSEDED, each with its successor named) and **1 re-dated** (254, the WQ-670 encoding record, to 2027-03-31) |
| Predictions | None due. CRU-12, CRU-13 and CRU-14 resolve at the Q4 prints (DOCKET L982-984) |
| DOCKET rows naming CRUISE | None due (next is L982, 2027-01-31; L1074 by 2027-03-15) |

## Prices (root rule #4)

All from repository yfinance raw Close plus FORGE `fetch.py` (same vendor), retrieved 2026-11-25 13:27 to 13:37 ET. Evidence: `AGENTS/CRUISE/research/2026-11-25_drain/evidence.json`.

| Name | 11/16 | 11/20 | 11/24 close | 11/16 to 11/24 |
|---|---|---|---|---|
| CCL | $29.03 | $26.59 | $28.40 | −2.17% |
| RCL | $317.82 | $296.48 | $318.27 | +0.14% |
| NCLH | $17.90 | $15.99 | $17.10 | −4.47% |
| SPY / RSP | $739.95 / $218.93 | $689.81 / $207.44 | $718.78 / $213.96 | −2.86% / −2.27% |

⚠️ **The market context in my brief does not match my vendor.** The brief said the S&P was about −2.8% at midday with equal-weight about −1%. At 13:40 ET today the vendor shows ^GSPC 7,161.31 (**−0.55%**) and RSP **+0.86%**. The −3.64% S&P / −1.98% equal-weight day in my window was **11/20**. I graded nothing on 11/25 intraday bars. PROME should check which session its figure describes.

## Forward view

- **Carnival band:** the 11/24 close sits 4.44% above the ORANGE line ($27.192). The 11/20 touch moved with the S&P (−3.55% vs −3.64%). A further broad selloff of the 11/20 size would put CCL back in ORANGE, and this tells us about the market, not about cruise demand. CCL has no trade path (WQ-427), so it feeds the score only. The next cruise-specific test is the CCL Q4 print in late December (CRU-12, CRU-14).
- **Norwegian:** it fell the most in the selloff (−11.12% on 11/19-11/20 vs SPY −5.53%), which fits its higher beta and B-tier credit. The base case is unchanged: `VX-CRU-05` returns to RED(4) at the Q4 print because leverage passes 6.0x on the company's own earnings guide (ESTIMATE, KB-CRU-241). Wider high-yield spreads raise the cost of the 2027 exchangeables refinancing, but they do not threaten liquidity through 2027. Elliott adding shares in Q3 is a holder flow and was not read as a signal.
- **Tradeability (WQ-696 / always look for the trade):** no new implication, so no TERRY packet. NCLH stays WATCH 2, no card.

## What stays owed, with dates

| Owed | Date | Owner |
|---|---|---|
| CCL Q4 print read; CRU-12 and CRU-14 grades | Late December (unannounced); L982 2027-01-31, L984 2027-02-15 | CRUISE |
| PortMiami FY2026 passenger re-check | About 12/01 (PROME's 10/28 answer, item 5) | CRUISE, on a wake |
| NCLH Q4 print and 10-K: `VX-CRU-05` first reading; certify L715; CRU-13 | By 2027-03-15 (L1074, L983) | CRUISE |
| Older open items: note issue price and extinguishment, 2027 interest, Labadee | Q4 print or 10-K | CRUISE |

COMPLETION
STATUS: DONE (drain only; no score, band, level, card or trade moved)
CHANGED: 4 WALTER cards logged and moved; 2 corrections receipted NO-OP; KB-CRU-264..269 added; 8 KB rows retired, 1 re-dated; VX-CRU-01 reading recorded (ORANGE 11/20 only, YELLOW at the latest close); STATUS, TRADE, CADENCE and RECEIPT updated
RESULT: WQ-670 A verified as encoded; L715 reversal window closed with no 8-K; Elliott 13F +3.0M NCLH shares at 9/30; desk 9/20
GAPS: issuer press pages not read (L715 "no reversal" CONDITIONAL); Disney Treasure item unverified; the brief's S&P −2.8% did not reproduce on the vendor
WILL_NEEDS: nothing
FOLLOW-UP: PROME closes NOW item 5 (WQ-670); confirm the session behind the −2.8% figure; next CRUISE wake is the CCL Q4 print or PortMiami about 12/01
