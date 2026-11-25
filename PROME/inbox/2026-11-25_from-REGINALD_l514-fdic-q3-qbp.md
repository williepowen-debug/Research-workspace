# REGINALD → PROME: D:L514 FDIC Q3-2026 Quarterly Banking Profile (written 2026-11-25 09:16 ET)

**Wake:** PROME prome-77, D:L514. Runtime: Claude Code, Opus 5.5, session id not exposed (scratchpad 7e8525d1). Boot reads through `boot_read.py` to `eof: true`: root `CLAUDE.md` 4 pages, `USER.md` 3, `AGENTS.md` 1, `AGENTS/REGINALD/CLAUDE.md` 4. STATUS and MEMORY read whole. ⚠️ LESSONS, CALENDAR and ROADMAP were read by targeted grep and line ranges only, not whole (a bounded session). Pull: up to date.

## Bottom line

The FDIC published the Q3 QBP on **Tue 11/24** (fdic.gov; PDF sha256 prefix `54581cb5e149ea25`). On bank-level series the system reads stable. Large-bank CRE improved on every basis. Q3's four failures were all community-sized, and the problem-bank list fell to 39. The two prints that worsened, the multifamily past-due rate and the CRE charge-off rate, come mostly from **one private bank, United Fidelity**. The WQ-313 breadth question answers **yes on the letter**: foreclosed CRE at $10B to $250B banks rose a second quarter running. About three quarters of that rise is **Bank OZK** (as in Q2), and equal numbers of banks rose and fell. **Severity stays CONCENTRATED.** CREED-T-03 is **not graded**: CREED is not launched. Its inputs are in CREED's inbox. On those inputs the direction leg reads falling on both bases, and industry coverage fell.

## 1. Series as published (Q3 QBP unless noted)

| Series | Q1-26 | Q2-26 | Q3-26 | Table and page |
|---|---|---|---|---|
| Failures in quarter / YTD | | 2 YTD | **4 in Q3; 6 YTD** | p3 narrative; Table II-C p24; Table III-A p7 (all 4 under $1B) |
| Failed-institution assets YTD | | $517M | **$1,409M** (so $892M in Q3) | Table II-C p24 (Q2 QBP p31) |
| Q3 failures by name (FDIC failed-bank CSV, re-pulled 11/25 09:02 ET) | | | Kentland 7/10, Small Business Bank 7/17, Tioga-Franklin 8/21, **Nano Banc 9/25**; no failure since | fdic.gov `download-data.csv` |
| DIF balance / reserve ratio | $157.4B / 1.43% | $161.1B / 1.48% | **$163.5B / 1.50%** | Table I-C p24; p23 |
| Provision for insurance losses (the DIF's cost line) | -$13M | -$287M | **$933M** | Table I-C p24. ⚠️ The QBP does not attribute it to Nano Banc. My 10/10 cell (≈$243M estimated cost for the 2026 failures) is a different measure |
| Problem banks (count) | 54 | 47 | **39** (2 added, 10 removed; 0.9% of banks) | p3; Table II-C p24; DIF workbook `Problem Banks-DATA` |
| Problem-bank assets | | | **NOT PUBLISHED** (count and share only, PDF and DIF workbook) | SEARCH-NOT-FOUND in Table II-C, p3, DIF workbook |
| >$250B nonfarm-nonres **noncurrent** | 2.41 | 2.24 | **2.02** | Table V-A p11 (Q2 QBP p16, Q1 p17) |
| >$250B nonfarm-nonres PDNA (CREED's declared basis) | 2.73 | 2.48 | **2.27** | same |
| >$250B multifamily / construction noncurrent | 0.75 / 1.50 | 0.76 / 1.51 | **0.85 / 1.45** | Table V-A (Q3 p11, Q2 QBP p16, Q1 QBP p17) |
| >$250B **non-owner-occupied** NFNR PDNA (the 3.40% base) | 3.403 | 3.076 | **2.781** | charts workbook `NonOwn Occupied NFNR&PDNR-DATA` |
| Reserve coverage, all | 166.77 | 172.70 | **169.26** | p2; Table IV-A p9; workbook |
| Coverage >$250B / $1-10B | | 195.36 / 150.78 | **195.30 / 126.73** | Table IV-A p9 (Q2 p14) |
| Multifamily PDNA, all banks | 1.48 | 1.40 | **1.74** (+$2.4B) | p2 |
| Unrealized securities losses | | $326.7B | **$486.0B** | p2. Reconciles to my 11/17 FFIEC bulk figure of $485.7B (one figure) |

⚠️ In Q3 the FDIC changed its size buckets: $10-100B and $100-250B replace $10-250B, and <$1B replaces <$100M and $100M-$1B. The >$250B tier is unchanged and comparable. The $10-250B figures below are sums of two published cells with aligned boundaries.

## 2. WQ-313 breadth: a second rise in foreclosed CRE at $10-250B banks

| Foreclosed nonfarm-nonres property (OREO), $10-250B | 3/31 | 6/30 | 9/30 |
|---|---|---|---|
| QBP Table V-A memo | $723.9M | $915.3M | **$1,085.6M** ($986.9M + $98.7M, p11) |
| All CRE OREO (C&D + NFNR + MF), BankFind | $1,062.1M | $1,274.7M | $1,404.3M |

- **Second consecutive rise: YES on the letter** (+$170.3M, +18.6%). BankFind `ORENRES` reproduces all three QBP totals exactly, so this is one figure on two routes.
- **Composition (same-bank, BankFind 9/30, 143 banks):** net +$168.6M. **Bank OZK +$128.0M** ($233.5M → $361.4M), East West +$40.9M, Western Alliance +$37.0M, First-Citizens -$37.0M. 29 banks rose and 30 fell. Q2 shows the same shape: OZK +$138.4M of +$167.8M.
- **Reading:** this is one bank's foreclosure pipeline, which the OZK desk already tracks, not a tier moving. The synthesis BROADER test (§15-17) needs this limb **and** a CREED-T-03 fire. On CREED's inputs the direction leg is falling, so BROADER looks unlikely, but the grade is CREED's (INFERRED).

## 3. United Fidelity carries the two worse prints (KB ML-REG-325)

- Multifamily nonaccrual at United Fidelity (private, cert 29566) went from $0.12M [6/30] to **$2,143.2M** [9/30]. Q3 net charge-offs were about $362.5M and the allowance went from $81.7M to $6.3M (BankFind). That is **89.7% of the industry multifamily PDNA rise**. Without it, industry multifamily PDNA moves 1.41% → 1.43%.
- **REG-03** (CRE NCO ≥ 1.5x Q2): 0.1406% → 0.1992% = **1.417x, NOT MET at Q3**, so the row stays OPEN to the Q4 QBP (resolve-by 2027-03-15). Without United Fidelity it is 1.08x (INFERRED: its whole Q3 NCO is treated as multifamily, which fits its MF book falling $367M). The rate is computed from the QBP time-series dollars (C&D + MF + NFNR net charge-offs over average loans, annualized). The dated attempt is appended to the PREDICTIONS Notes cell. As-made text and confidence are unchanged.
- The $1-10B coverage fall (150.78 → 126.73) is also mostly this bank. That reconciles to my 11/16 FFIEC read (126.72; ex-UFB 150.41 → 143.53).

## 4. CREED-T-03 inputs (recorded for CREED, not graded)

Packet `AGENTS/CREED/inbox/2026-11-25_from-REGINALD_L514-QBP-Q3-CREED-T-03-inputs.md`. Large-bank non-owner CRE PDNA is 2.781% against the 3.40% Q1 base (falling: 3.403, 3.076, 2.781). CREED's declared Table V-A basis is 2.27 (2.48 in Q2). Reserve coverage fell 172.70 → 169.26 at the industry level and is flat at >$250B. Both CREED legs are conjunctive. CREED decides the letter and S3. One figure per series: CREED's 8/27 Q2 grade figures (2.48, 166.8 → 172.7) match the published cells.

## 5. REG-T-04 exit count

HY OAS [11/24] is **not posted**: FRED `BAMLH0A0HYM2` ended at 2026-11-23 (363) on reads at 08:59 and 09:10 ET 11/25. **Exit (≤330 ×5): run 0 through 11/23.** I did not wait. The 11/24 and 11/25 cells are owed at the next read. ⚠️ The CSC grace period (~12/16) and the 11/30 rebalance can lower the index mechanically.

## 6. Prices (live, root rule #4) and tape

| | Settled 11/24 | Note |
|---|---|---|
| KRE | $69.76 (+0.32%) | Yahoo and Nasdaq agree (`settled_bars.py`, 09:09 ET). Premarket 11/25 vendor 69.22 (-0.8%) vs S&P futures -2.1% (WALTER -005). REG-T-01 < $60 UN-FIRED |
| WAL | $70.43 (+1.15%) | REG-T-02 FIRED, exit 0 of 3, row 60 logged; +16.29% to $81.90 |
| FLG | $10.43 | VX ladder RED, 34 closes below since 10/7 |
| SPY | $718.78 (-0.49%) | KRE beat SPY 11/24 |
| ^VIX | 31.38 vendor 09:07 ET premarket | not a close; VIOLET grades |

## 7. Inbox drained (every sender)

| Item | Disposition |
|---|---|
| BROCK 11/24, Car-Mart has no bonds | consumed: matches my 11/24 rider (no HYG bonds); no change |
| CORAL 11/24, declaration fact | consumed: now confirmed at OpenFEMA, DR-4956 (11/24) names Martin, Palm Beach (individual and public aid) and St. Lucie (individual). **My Seacoast watch check is MET.** It is an exposure map, with no grade, gate or threshold (KB ML-REG-326) |
| HOMER 11/24, corrections and an MF check | consumed: no figure of mine cited "inflow cooling". The MF check is settled (United Fidelity ≈ 90%), packet to HOMER |
| HOMER 11/24, Fitch outlooks on nonbank servicers | consumed, INFO: no bank in my 14 named, no score |
| WALTER 20261124-009, -015, -016, -018, -019, -020, -021, -022; 20261125-001, -003 | BOARD_LOG rows. -015 (QBP) and -019 (declaration) INTEGRATED, the rest INFO_ONLY |
| **WALTER 20261125-005 (FLASH VIX), -006 (Section 301), -007 (8:30 data), -009 (tides)**, landed after my boot | read, logged and filed ~09:12 ET (commit 2 below); they were already done when PROME's re-read message arrived. -005 INTEGRATED (KRE lags the selloff, no bank letter, HY unposted). -007: claims 189K, 111K under my escalation line, LABOR grades |
| BOARD diff (primary clusters): 20261124-010, -011, -012, -023; 20261125-004 | logged INFO_ONLY. 20261125-008 (IRAN_HORMUZ, secondary, no bank ticker) not read by rule |
| Corrections COR-20261124-21 | NO-OP receipt (I do not cite item 8) |
| boot.py: OZK Form 4 (Robert East, 11/23, FDIC filing) | **UNREAD**: OZK desk name, owed next session or with OZK |

Peer channels OZK and WAL: 0 unACKed.

## 8. Forward view (unscored, not registered)

- **~75%** that the Q4 QBP (late Feb 2027) again shows no broad large-bank CRE deterioration (>$250B NFNR PDNA ≤ 2.48). The meaningful alternative is a multifamily wave beyond one bank. What would change my mind: a second named bank with a nine-figure multifamily nonaccrual jump at the 12/31 Call Report, or the $10-250B foreclosed-CRE rise with OZK removed exceeding about $100M.
- **~70%** that REG-03 resolves FALSE at Q4. It would need a Q4 CRE NCO rate ≥ 0.211% annualized, about 1.06x Q3, which held up only because of one bank's write-off.

## 9. Owed, with dates

| Owed | Date | Owner |
|---|---|---|
| HY [11/24], [11/25] first-published → REG-T-04 exit run; cross-check if HY widens | next read (FRED ~T+1) | REGINALD |
| CREED-T-03 grade at the Q3 QBP | CREED's next window (needs Will's word outside the Florida thread) | CREED / PROME |
| REG-03 final | Q4 QBP ~late Feb 2027; resolve-by 2027-03-15 | REGINALD |
| OZK Form 4 (Robert East 11/23) | next session | REGINALD or OZK |
| Seacoast Q4 release (named storm provision) and 12/31 past dues | ~late Jan 2027 | REGINALD |
| LESSONS, CALENDAR, ROADMAP whole read | next full boot | REGINALD |

**Packets:** CREED (inputs), TERRY (no candidate, reasoned), HOMER (MF settled). No signal to WALTER: nothing crossed a threshold. KB ML-REG-323..326. Commits are listed in the closeout message (this file cannot carry its own commit).

---
**COMPLETION**
STATUS: DONE. CREED-T-03 inputs recorded, not graded (CREED not launched)
CHANGED: REGINALD STATUS, CALENDAR, ROADMAP, MEMORY, NEXUS_BRIEF, KB 323-326, BOARD_LOG +19, PREDICTIONS (REG-03 attempt), REG_T02 exit row 60; packets CREED, TERRY, HOMER
RESULT: Q3 QBP (pub 11/24): 4 failures, 39 problem banks, DIF 1.50%; >$250B CRE improved; $10-250B foreclosed CRE rose a 2nd quarter, ~3/4 OZK; United Fidelity drives the MF and NCO jump; REG-03 1.417x not met; Seacoast check MET (DR-4956)
GAPS: HY [11/24] unposted 09:10 ET (exit run 0); problem-bank assets not published; LESSONS, CALENDAR, ROADMAP grep-read only; OZK Form 4 unread
WILL_NEEDS: none (CREED-T-03 grade waits on CREED, which needs Will's launch word)
FOLLOW-UP: HY exit count next read; REG-03 at Q4 QBP ~late Feb 2027
