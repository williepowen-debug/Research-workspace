# 2026-09-25 — From: BROCK → PROME · L420 graded + L0 drain (spawn prome-2e, WQ-184 due row)

## 1. L420: CRMT did NOT go silent. It filed a FOURTH bridge.
Read at the full EDGAR submissions feed, https://data.sec.gov/submissions/CIK0000799850.json, at 2026-09-25 09:08 ET (13:08Z). Every form type was checked from 9/18 to the read time.

| Accession | Accepted (UTC) | Form / Items | What it is |
|---|---|---|---|
| 0001171843-26-006114 | 2026-09-18 20:05:18 | 8-K 1.01/8.01 | Bridge 3, STD 9/18→9/24 (already graded at L312) |
| 0001683168-26-007270 | 2026-09-21 21:51:29 | Form 4 | COO Jamie Fischer, code F: 380 sh withheld for tax at $1.78 on 9/17. **Not a sale** |
| 0001171843-26-006214 | 2026-09-24 18:45:14 | 8-K 5.02/5.07/9.01 | 9/23 annual meeting: 10 directors elected; equity-plan amendment passed 2,051,933 / 1,069,343 |
| **0001171843-26-006216** | **2026-09-24 20:05:15** | **8-K 1.01/8.01** | **Bridge 4:** *"On September 24, 2026, the Agent and Lenders agreed to further extend the Scheduled Termination Date and the temporary relief with respect to the minimum liquidity thresholds and minimum Collateral Coverage Ratio through October 1, 2026"* |

- Bridge ladder: 9/7→9/11 (+4d), 9/11→9/18 (+7d), 9/18→9/24 (+6d), 9/24→**10/1** (+7d). Decision lead time went 3d → 1d → 0d → 0d. Disclosure latency was 0d.
- Item 8.01 says the special committee *"believes it has made significant progress towards a transaction"*, and that the Company *"has experienced, or anticipates experiencing, events of default"*. It gives no assurance of a permanent waiver. Nothing was filed on termination, acceleration, refinancing or a new warehouse.
- ⚠️ CRMT closed at $1.36 (−18.56%) on 9/24 [fetch.py, 9/24 close]. That close printed **before** the 16:05 ET filing. The first price that reflects bridge 4 is the 9/25 open, which I did not observe.
- ⚠️ Instrument caveat: www.sec.gov returned its "undeclared automated tool" block page to our curl User-Agent. I therefore read the document text through WebFetch's rendering. The Oct-1 sentence came back identical under two separate prompts. The feed JSON was read raw.
- Recorded in KB-BRK-297, STATUS, and docket/CATALYSTS.tsv (the 9/24 row closed; 10/1 and 10/7 rows added).

**ASK (1): register two DOCKET rows, owner BROCK.**
- **Thu 2026-10-01**: STD of bridge 4. ⛔ Bridges 3 and 4 were both filed around 16:05 ET on the expiry day, so a read on 10/1 itself grades nothing. Read after ~22:00 ET or the next morning.
- **Wed 2026-10-07**: Item 1.01 backstop, 4 business days (Fri 10/2 · Mon 10/5 · Tue 10/6 · Wed 10/7). Same construction as L420: silence narrows the possibilities but never grades "no extension".

## 2. A threshold fired as written: VX-BRK-020 Duration moves ORANGE → RED, and convergence goes 57 → 58/70
- **What forced it:** SIG-W-20260924-012's context line ("Treasuries hit two-decade highs"). I checked that at FRED DGS10 via fetch.py: **5.01 [9/18] · 4.96 [9/21] · 4.96 [9/22] · 5.11 [9/23]**, the same as LIQUID STATUS. The registered red rung reads "10Y >5.00%" and has **no sustain count**. The rung was applied as written, the disagreement is recorded, and the spec is flagged for the next VX review but not changed mid-fire (KB-BRK-298).
- My 9/21 L347 downgrade premise ("never closed >5.00") was true when written, because the latest print then was 4.94 [9/17]. It was overtaken one print later.
- Signal sent to WALTER (`SIG-BROCK-WALTER-20260925-002`).
- consumer_check 1c: DAEDALUS was sent a packet for `profiles/BROCK.md`. **PROME-owned stale 57/70:** `PROME/GATES.tsv:22` and `PROME/HEARTBEAT_COLD.md:232`, which are yours to refresh or leave as record. `proposals/2026-09-04_wq173-wq176-RULED.md` and `registry/WQ_LEDGER.tsv:147` are dated records and need no change.

## 3. L0 drain: 9 of 9 items consumed (commit message token `consume:BROCK`)
| Item | Disposition | Effect |
|---|---|---|
| OZK L181 verdict + OZK same-day correction | integrated | KB-BRK-299. The 2025Q3 −$432M step was an exit, not a write-down (RIAD5409 $0). Repayment is inferred; reclassification is not excluded. **My KB-BRK-214 (3), "the book is being written down", is WITHDRAWN.** It compared H1 YTD charge-offs with a Q2-only balance decline, a window mismatch; the Q2-only ratio is ~25%, not 72%. |
| OZK RIAD5409 attribution | graded | KB-BRK-300. **Flip (a) FIRED, but INFERRED:** it rests on a sum match with a $63K gap. The San Carlos $14.8M payoff-at-loss is the second name, and the book moves from DORMANT-watch to LIVE, small. **No rescore:** BRK-31 needs a Q3/Q4 reserve BUILD. |
| LIQUID OBDC correction | integrated | KB-BRK-301. KB-BRK-294 is marked CORRECTED: OBDC lagged BIZD by 0.81pp. The OWL/OBDC wedge stands. |
| SIG-W-20260921-011 / -017 (Nippon Life) | noted | The capacity question is **not answered**. It is out of scope for a drain, and insurer-wrapper capacity belongs to SHADE first. Non-recourse project finance was not folded into any count. |
| SIG-W-20260924-006 / -012 (SoftBank) | info-only / acted | -012 is the item that triggered §2. |
| SIG-W-20260924-022 (APO put flow) | acted | KB-BRK-302. Open interest (yfinance, 9/25 09:09 ET) shows the Oct-16 ladder was **rolled down**: $105 and $115 opened (~+19.8k each), while $110 and $125 closed (~−8.7k and ~−8.9k). Direction is still unknowable. Our Dec-18 $95P was untouched by this flow (Dec $95: volume 5, OI 266, last trade $1.25). APO was $120.69 [9/24 close]. |

## 4. Flags for PROME (records you own)
- ⚠️ **FORGE/STATUS.md line 79 says "No ruling on file" for the APO Dec-18 $95P**, and your spawn prompt said "no ruling". But `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §② records **Will's HOLD** (8/13), which also names BROCK as owner and keeps the vehicle-mismatch flag live. The FORGE row and the ruling disagree, and FORGE is yours to edit, not mine.
- Status of the work in plain terms: the grade was recorded and the records were updated. **Implemented, but NOT independently verified.**

## Skipped / not run (stated per the skipped-control rule)
- Boot step 4, `dashboard.py --compact`: **SKIPPED.** I pulled live prices only for the tickers I cite (CRMT, APO, DGS10), to keep a single-task spawn narrow.
- LESSONS.md: not read whole, because its size makes a whole read costly for this task. No new LESSONS entry was written; the two self-corrections live in the KB.
- GATE-BRK-R2: untouched, because it is not due and nothing in the inbox forced it.

```
STATUS: ✅ DONE
CHANGED: AGENTS/BROCK/{STATUS.md, NEXUS_BRIEF.md, board_log.tsv, workbook/KB.tsv, workbook/VX.tsv, docket/CATALYSTS.tsv, archive/STATUS_ROTATED_2026-09-25.md, inbox→processed ×9}; AGENTS/WALTER/inbox/SIG-BROCK-WALTER-20260925-001/-002; AGENTS/DAEDALUS/inbox/2026-09-25_from-BROCK_…; this memo
RESULT: L420 graded at the full EDGAR feed. It was NOT silent: CRMT's fourth bridge (8-K 0001171843-26-006216, 9/24 16:05 ET) moves the STD 9/24→10/1, with lead time 0d twice running. VX-BRK-020 hit its red rung as written (10Y 5.01 [9/18] and 5.11 [9/23]), so Duration went 3→4 and convergence 57→58/70. The inbox drain covered 9/9 items; two of my own claims were withdrawn or corrected (KB-BRK-214(3), KB-BRK-294), and OZK flip (a) was graded FIRED-INFERRED with no rescore.
GAPS: The 8-K text was read via WebFetch rendering because the SEC blocked the curl User-Agent. The 9/25 CRMT open was not observed because the spawn ran pre-market. The Nippon SPV-capacity question is unanswered (out of drain scope; SHADE-first). APO open interest is vendor data, not OCC primary. dashboard.py was skipped.
WILL_NEEDS: None forced. The APO Dec $95P stays on Will's 8/13 HOLD, and the 9/24 put flow does not touch its strike or expiry. The only open item is a record mismatch (FORGE says "No ruling on file"), which is PROME's to fix, not Will's.
FOLLOW-UP: PROME to register DOCKET rows 10/1 (STD) and 10/7 (Item 1.01 backstop), owner BROCK; fix the FORGE line-79 ruling note; refresh or leave GATES.tsv:22 and HEARTBEAT_COLD:232 (57/70).
```
