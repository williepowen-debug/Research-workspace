# TERRY catch-up to live data, 2026-11-05
Written 2026-11-05 09:50 EST. Authority: Will 09:42 ET via `inbox/processed/2026-11-05_from-PROME_catch-up-to-live-data.md`. No order, no gate or level changed. Inputs: `crack_pull.json`, `gfs_reads.json`, `gfs_decode.py`, `chain_RSP.txt`, `chain_UNG.txt`.

| Row | Observation | Basis and time | State |
|---|---|---|---|
| GATE-TERRY-VLO-HELD-01 | CME unreachable: curl 92, HTTP/2 INTERNAL_ERROR, twice | www.cmegroup.com 09:45–09:46 EST; FRED control 200 | FIRED-UNEXECUTED, source (1) unread |
| same | 11/4 vendor $88.5110, volumes duplicate 11/3, rejected; ESTIMATE $88.5451 stands | vendor rows pulled 09:45 EST | below $90.16 on an ESTIMATE; exit already established 11/2 |
| same | HENRY confirmed line, basis, arithmetic; not the 11/2 input; HEN-46 no live thesis | packet 09:49 EST | limit closed |
| same | 11/5 pair $91.224 | intraday 09:35 EST, a quote | not an observation |
| GATE-TERRY-RSP-01 | RSP $222.80 −0.24%; outer $9.10, mid $7.50 vs ≤ $4.90 | 09:45–09:46 EST, screening | NOT-FIRED, debit blocks |
| GATE-TERRY-UNG-01 | GFS +0.309821 [11/5 00Z], +0.245778 [11/5 06Z]; UNG $9.32 +0.54%; 12C DEAD | analysed field; 09:46 EST | NOT-FIRED; AEOLUS log required |
| GATE-OP-SCALE-01 | N = 2, −$196.13; R = 4 audited; RED read owed | `../2026-11-07_op-scale/DRAFT_SHRINK_PROPOSAL.md` | draft current, not a grade |
| HYG WQ-513 | HY 340 [11/3] latest; run 0 of 3 | FRED, 09:45 EST; no 11/4 cell | NOT-FIRED |
| ORCL WQ-514 | DTCC 300 [11/3]; ORCL $119.04 −3.79% | LIQUID status; 09:45 EST | NOT-FIRED, NOT-VOIDED |

Small batch: WAL postmortem appended (interim) · CRUISE-MARITIME signal RETIRED · retirement candidate `research/2026-08-27_refiner-XLE-decoupling-distribution.md` NOT eligible: the live analytic card `setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md` travels it · KRE/QQQ map: Artifact read returns the owned live version (1793890064-1d5f) with its files, so the page exists; a browser render was not tested and is not worth more effort, a snapshot through 10/22.

Not done: CAL-0004 resolves 16:00 ET today on BOND's record, CAL-0005 by 11/6 on FERT's; both stay open. B44/D17 review due 11/6 not started; `TRY-COND-TLTPUT-WQ339` sits CONDITIONAL on INDEX with its window ended 10/14 and no ledger row, not changed here.

## Broker capture booked 2026-11-05 10:05 EST
Source: `PROME/data/2026-11-05_broker-capture-TRANSCRIPTION.md`, e22ca99c4, checked against Will's two screenshots. Fidelity only, intraday, not a close. VLO ×1 sold $366.665, proceeds $366.67, realized −$45.33 ($366.67 − $412.00); gate discharged. QQQ 690P holding 0, ×1 at $28.83, other close price UNKNOWN. GLD 18 shares. WAL 70P ×2 and 65P ×4, OZK 40P ×4 unchanged in count. ⚠️ Paper marks taken at 09:39 EST were prior-session prices: WAL 70P $1.07 vs broker $0.45, QQQ 690P $16.245 vs fill $28.83. Finding 5b, not a new defect. OP-SCALE N = 3, −$241.46.

## BOND's weak-refunding ask: NO CARD, 2026-11-05 10:51 EST
Asked: `PROME/inbox/2026-11-05_from-BOND_go-items-prediction-and-terry-ask.md` § 3 (3f084dd28). Test: `refunding_card_test.py`, output `refunding_card_test.out`, read-only on BOND's pools, rolling 12-print bars, all 34 30Y prints with a bar, vendor TLT closes. Control: its 11/12 bars reproduce BOND's frozen 59.95 / 14.74 / 2.29 / 63.89. A first run printed n=0 on wrong key names; the control caught it and it was re-run. Description, not a backtest.

| 30Y print state | n | Median 5d | Median 10d | 5d at −1.6% or worse | 10d low at −1.6% or worse |
|---|---:|---:|---:|---:|---:|
| All | 34 | −0.30% | −0.22% | 4 | 17 |
| I′ fire | 9 | −0.44% | −1.36% | 1 | 6 |
| I′ plus dealer above trailing max | 0 | | | | |
| OLD composition failure | 0 | | | | |

| Screen, 10:49 EST, TLT $81.89 +0.16% | Outer debit | ×1 risk | Breakeven | Move needed |
|---|---:|---:|---:|---:|
| Nov-20 81/79P | $0.39 | $40.30 | $80.61 | −1.56% |
| Dec-18 81/78P | $0.90 | $91.30 | $80.10 | −2.19% |

**Verdict: no card.** (1) BOND's stronger trigger has not printed once in 34, so a card on it has no measured payoff and little chance of firing by the 11/12 print. (2) A bare I′ fire reached the Nov-20 breakeven at 5 sessions 1 time in 9, against 4 in 34 for all prints: no separation. The 10-session figures lean toward it, n = 9, and a low touched is not a price held. (3) These returns start from the auction-day close; root rule #6 wants a green TLT day first, so a real fill is later and likely worse. (4) "30Y fails, belly holds" is a curve view. TLT puts alone are a level bet, and two option legs across TLT and IEF is a poor fit for a $500 card. (5) BOND is flat, WQ-280 NO-ADD stands, X1 is closed, WQ-592 is declined.

**What would change it:** an OLD failure actually printing on the 30Y 11/12, or I′ plus a funding or dealer confirmation with BOND's mechanism read. That is a fresh build on that day's chain, not a pre-arranged card. No new watch or rule. The dealer leg here is the trailing max; a funding confirmation was not tested.

