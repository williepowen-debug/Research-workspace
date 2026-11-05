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
