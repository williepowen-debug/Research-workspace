# Re-modification screen: did the Q2 payment-delay blocks pay off or get modified again?

**Run:** 2026-11-06. **Owner:** REGINALD. **Assignment:** PROME, Will's "go 1, 2, 4", 11:36 ET. No score, threshold or gate change.

## Plain words

**Valley is still alone.** Of the 14 banks, one shows a block that looks re-modified. Three other small blocks were read: two are still held and one looks paid. SouthState and Citizens can't be read either way. Five banks had no payment-delay block as filed, and FLG, CUBI and OZK can't be tested yet. **This is a thin result, and that is the answer.** The name to watch is Flagstar: its modified loans jumped about $202M in Q3 on the Call Report, and its 10-Q isn't filed.

**Update 11/06 17:19 ET.** The three unfiled names are now read, all NO BLOCK: FLG's H1 row is intact at $556M with no payment-delay column, and CUBI and OZK show no CRE modifications. **Count now: RE-MODIFIED 1, STILL HELD 2, PAID 1, NOT DISCLOSED 2, NO BLOCK 8.** Flagstar's $202M jump is mostly a Call Report line, about $77M real → `reports/2026-11-06_close-refresh/REPORT.md` §3, §6. The rest of this page stands as made.

## Method

A loan modified in H1 and still on the books must still appear in the nine-month table. So: H1 as filed in the Q2 10-Q, against H1 now (nine-month minus Q3 three-month). If a block is missing, it left the books or moved into the Q3 row because it was modified again.

**⚠️ Correction to my Valley reasoning.** The pool total cannot separate those two: a $108M payoff plus $108M of new modifications gives the same total as a re-modification. **Only line-level flatness separates them.** So RE-MODIFIED needs the Call Report line that could hold the block to stay flat to within about 10% of the block. PAID needs the block gone, the line down by about the block, and no matching move into late or nonaccrual; even then it is an inference, since a category disappearing does not prove cash came back.

Labels: PROME's three, plus two I added rather than force a reading: **STILL HELD** (block remains in the H1 row) and **NO BLOCK** (none as filed). Sources: Q2 and Q3 10-Q iXBRL and text, read at SEC 11/06; Call Report RC-C Memo 1 and RC-N Memo 1 for the 14, fresh pulls 11/06. $M. CRE classes only.

## Result

| Bank | H1 CRE payment-delay block, then → now | Q3 payment delays | Call Report lines 6/30 → 9/30 | Label |
|---|---|---:|---|---|
| **VLY** | 108.6 → 0.4 | 140.7 | Owner-occ 64.9 → 65.9; other 45.5 → 44.6; MF 23.3 → 96.9 | **RE-MODIFIED (inference)** |
| **BKU** | 29.9 → 29.4 | 35.3 (combination, includes 1.5-year deferral) | Block sits in modified-and-nonaccrual; construction 0 → 35.3 | **STILL HELD**, nonaccrual |
| **EGBN** | 17.8 → 17.6 | 56.0 | Separate case below | **STILL HELD** |
| **SBCF** | 6.2 → 0 | 0 | Other 6.2 → 0.0; late 0 | **PAID (inference)**, small; sale or charge-off not excluded |
| **SSB** | 135.3 → 65.4 | 53.0 | Other 106.1 → 86.4; MF 132.3 → 163.1; late 37.2 → 30.4 | **NOT DISCLOSED.** Class row mixes MF and non-owner; no line flat |
| **CFG** | 124 → 84 (payment-delay rows) | 23 | Other 539.8 → 431.5; construction 177.2 → 203.4; late 218.8 → 265.0 | **NOT DISCLOSED.** $40M left; part moved late |
| **HBAN** | none as filed | none | Stock lines all rose; late 77.6 → 72.4 | **NO BLOCK** |
| **ZION** | none as filed | none | MF 258.2 → 181.5; other 218.5 → 213.1 | **NO BLOCK** |
| **MTB** | none as filed | none | Other 402 → 395; construction 239 → 283; late 226 → 137 | **NO BLOCK.** ⚠️ XBRL tags the "Term Extension" column `PaymentDeferral`; filing text governs |
| **WAL** | none in H1 | 7 | Other 72.7 → 88.2 | **NO BLOCK** |
| **AMTB** | none | one relationship, rate and term | Pool 0 → 15.8 | **NO BLOCK** |
| **FLG** | Q3 10-Q not filed | ? | Pool **411.1 → 613.2**: MF 199.2 → 263.6; other 0 → 128.5; late 208.0 → 221.1 | **NOT DISCLOSED**, pending 10-Q |
| **CUBI** | Q3 10-Q not filed | ? | Pool 0 → 1.8 | **NOT DISCLOSED**, immaterial |
| **OZK** | files at FDIC, not read here | ? | Stock 0; late 40.0 → 0.0 | **NOT DISCLOSED** |

**Count: RE-MODIFIED 1, STILL HELD 2, PAID 1, NOT DISCLOSED 5, NO BLOCK 5.**

- **EGBN, separate case.** Q3's $56.0M term-plus-principal-delay row matches the Prince George's loan (L11), which the deck says was re-extended to 12/21 and moved to nonaccrual. It is new to the modification table, not a block rolled from H1. It is a disclosed extension of a named-bank loan, and I do not count it as spread.
- **Term-extension gaps, not assigned.** CRE term-extension rows also shrank at CFG (399 → 283), HBAN (299 → 154), ZION (257 → 146) and MTB (313 → 210, construction 245 → 207). Short maturity extensions get re-extended routinely, and they aren't payment holidays. No line test separates them here. Logged, not labelled.
- **Valley's inference is unchanged in strength.** Two separate lines each moved about $1M or less per quarter across three quarter-ends, and their sum stayed within $0.1M. A replacement would have to match that. I can't exclude it.

## Q1 2027 timing

Today only Valley's block points at Q1 2027: $140.7M at about 5 months. SouthState's $53.0M runs about 9 months, to mid-2027. BankUnited's $35.3M runs 18 months, to about Q1 2028. So **Q1 2027 is a Valley date, not a group date.**

**If re-deferral spreads,** Q1 2027 stops being a test and becomes a checkpoint: expiry only tests a loan if it can't be re-deferred. On Valley's pattern, an 8-month term replaced after one quarter by about 5 months, each roll adds a quarter or two (my judgment, n=1). The evidence then has to come from the banks' reports: 12/31 Call Reports (~February 2027), 10-Ks, and the Q1 2027 10-Qs in May. Losses would surface later, not smaller.

## Forecast

**REG-35 (70%):** Valley's non-multifamily CRE modified-in-compliance lines (K161 + K162) are at or above $95.0M at 12/31/2026. It tests whether the block stays parked. Reasons, base rate and limits are on the row.

## Limits

14 banks only. 3 of 14 untestable today. Bank-level Call Report vs holding-company 10-Q. iXBRL member names were checked against text only for VLY, MTB, EGBN, SSB and SBCF. Not read: issuer calls, OZK at FDIC. No loan is named anywhere; every label except Eagle's table is an inference from tables.
