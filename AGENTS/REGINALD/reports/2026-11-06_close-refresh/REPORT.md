# Close refresh, Friday 11/06: H.8, three late 10-Qs, data through the close

**Run:** 2026-11-06 ~17:10 ET. **Owner:** REGINALD. **Assignment:** PROME relaying Will 17:08 ET, "boot up and update with the latest data as of market close". Bounded: no new research thread, no spawns, no trade or card. **No score, band, threshold, gate or prediction moved; no registered letter required it.**

## Plain words

**Flagstar's multifamily stress is still building, and its modifications fell hard, which is the mixed result its 10-Q was going to settle.** Loans rated special mention, the first step below pass, rose $244M to $3,001M and substandard rose $246M to $4,428M. That fails my "concern weakens" line, which needed special mention flat and substandard falling. New modifications dropped 76% to $96M, re-defaults stayed flat at $96M, and nonaccrual with no allowance fell. The $202M jump in its modified pool that I flagged this morning was mostly a Call Report line, not a Q3 event. **Valley is still alone on the re-modification screen.**

One row needs a question: Flagstar's nine-month re-default total is **lower** than its six-month total as filed, $221M vs $385M. A cumulative row should not fall. I do not know why.

Small-bank borrowing rose again in the latest H.8 week, with deposits up more. Lending to non-banks fell. Nothing here is a run, and put refuter 6 stays not met.

## 1. Data through the close

| Item | Latest | Basis |
|---|---|---|
| WAL, KRE, FLG, 11/06 | $75.55, $72.20, $10.52 | **Vendor, not settled.** Yahoo bar only; Nasdaq historical had no 11/06 row at 17:16 ET. `settled_bars.py` excludes today's bar. NOT GRADED |
| WAL, KRE, FLG, last settled | $75.88, $72.31, $10.60 [11/05] | Yahoo and Nasdaq agree |
| HY OAS | 348 [11/05] | FRED. **11/06 cell not published; about 10:10 ET Mon 11/09** |
| CCC, B, BB | 1,320, 367, 213 [11/05] | FRED. CCC/HY 3.79× |
| 10Y, 30Y | 4.84%, 5.25% [11/05] | FRED DGS10, DGS30 |
| VIX | 28.18 [11/05 VIXCLS]; 25.64 [11/06 vendor, not Cboe or FRED] | |
| SOFR less IORB | +2bp [11/05: 3.92 − 3.90] | FRED |
| Overnight RRP | $0.150B [11/06] | FRED RRPONTSYD |
| Financial stress | STLFSI4 −0.522, NFCI −0.459 [10/30] | ⚠️ NFCI revises: 10/23 now reads −0.467, was −0.487 in STATUS |
| Claims, primary credit | 189K [w/e 10/31], $9.219B [11/04] | Unchanged; next prints Thu 11/12 |
| KRE shares | 55.36M | Vendor, flat vs this morning |

BOARD: 0 selected of 136 unlogged since 11/03. Inbox and WALTER lane empty. WAL and OZK channels: nothing above my ACK. Corrections: 0 unreceipted. Ledgers clean.

## 2. H.8, released 11/06

**Primary:** https://www.federalreserve.gov/releases/h8/20261106/, Tables 2 and 8, seasonally adjusted, $B. Latest week ending 10/28. The comparator is the revised 10/21 in this same release.

| Small domestically chartered banks | w/e 10/21 | w/e 10/28 | Change |
|---|---:|---:|---:|
| Borrowings | 305.2 | **309.7** | +4.5, +1.5% |
| Deposits | 5,687.0 | **5,701.7** | +14.7, +0.26% |
| Large time deposits | 741.5 | 740.6 | −0.9 |
| Cash assets | 491.0 | 498.3 | +7.3 |
| C&I loans | 741.6 | 742.0 | +0.4 |
| Non-bank lending (NDFI) | 200.5 | **199.2** | −1.3, −0.65% |

All commercial banks: NDFI $2,111.0B, −$7.8B (−0.37%); C&I $2,999.2B, +$2.2B.

Borrowings remain $3.5B under the $313.2B [10/14] week. Deposits rose more than borrowings and cash rose too, so this is not a deposit run. The earlier 10/21 borrowings figure of $305.3B revised to $305.2B. **Refuter 6 stays NOT MET** on a second week: small-bank non-bank lending fell again, not re-accelerating. Descriptive, no registered line.

## 3. Flagstar 10-Q

**Source:** SEC acc 0000910073-26-000084, accepted 16:15 ET 11/06; comparators Q2 10-Q acc 0000910073-26-000068. $M.

**Reading table from `reports/2026-11-05_FLG_late-loan-review.md` §5. Those bars are my reading guide, not frozen rules or FLG desk grades.**

| Cell | 6/30 | 9/30 | Band |
|---|---:|---:|---|
| Multifamily special mention | 2,757 | **3,001** (+244, +8.9%) | **Contained** on level, under ~$3.2B. "Mostly market units" is a call statement; the 10-Q has no rent-regulated split, so the Worse limb is UNREAD |
| Q3 modifications | 401 | **96** (−76.1%) | **Harmless** on level |
| Re-defaults in the quarter | 93 | 96 | No jump. See the cumulative row below |
| Past maturity footnote | 132 | 119 | **Harmless** |
| 90+ accruing | 51 | **107** (MF 50, CRE 53) | **Contained.** Unnamed; "ongoing engagement"; $44M "resolved" by 10/27, undefined; $63M left |
| Nonaccrual with no allowance | 1,571 | 1,548 | **Harmless** |
| Late-loan narrative | none | none | **Contained, silent.** See below |

**`reports/2026-09-26_CRE_vulnerability_top3.md` §6, "weakens if":** MF special mention ≤ $2,757M with substandard still falling: **NOT MET.** Substandard rose 4,182 → 4,428 (+246, +5.9%). H2 modifications < $556M: on course at $96M, closes at the 10-K. Total nonaccrual $2,817M stays above $2,675M.

Not in any band, recorded because it moved: CRE special mention 376 → 571 (+195). Multifamily special mention, substandard and nonaccrual together 9,071 → 9,554, 33.7% → 36.8% of the multifamily book; ⚠️ the book shrank 26,931 → 25,948, so part of that share rise is the denominator.

**⚠️ The filing's late table misleads on its face.** It compares 9/30 with year-end, so multifamily 30-89 reads −33% ($392M vs $588M). The quarter's move was +68% ($233M → $392M), and the 10-Q says nothing about it.

**The pool jump is mostly not a Q3 event.** Call Report pool 411.1 → 613.2 is +202.1: multifamily +64.4, other +128.5, late +13.1. The 10-Q's prior-twelve-months table ties to five of six cells: 9/30 multifamily 264, CRE 129, late 221; 6/30 multifamily 199, late 208. The sixth does not: the **10-Q shows $128M of CRE current at 6/30 where the Call Report line read 0**. Q3 has no CRE modifications at all. So the +$128.5M looks like a Call Report line filled in, not new Q3 workouts (INFERRED; I did not re-open the 6/30 schedule). My morning line called the $202M the name to watch; about $77M of it is real movement. Inside the 10-Q's own pool, 12-month modified loans 599 → 688, and 90+ past due 220 → 276, multifamily 153 → 207 of 471, 43.9%.

**Re-modification screen:** no payment-delay column in the table, and the H1 row is intact: $556M as filed, $556M now (652 − 96). Multifamily 364 → 380, CRE 159 → 142, a $16–17M move between classes. Columns moved too: combination 59 → 11, rate 328 → 338, term 169 → 207. **Label NO BLOCK.**

**⚠️ OPEN, cause not assigned: re-default row.** H1 as filed $385M (Q1 292, Q2 93). Nine months now $221M, less Q3 $96M, leaves H1 at **$125M, $260M lower**; multifamily 286 → 124, CRE 69 → 0. The 2025 rows cumulate normally, $11M → $18M. Payoffs leaving the table, re-modification ending the "default", or a changed basis all fit. Payment default here means 30+ days past due. The Q3 table also dropped the Q2 "Principal Forgiveness" column. It is a question for the FLG desk, not a finding about the book.

Q3 multifamily modifications carried a rate cut from 8.87% to 4.97% with a 1.5-year weighted term.

## 4. Customers Bancorp 10-Q

**Source:** SEC acc 0001488813-26-000105, accepted 16:34 ET 11/06. No CRE modifications in Q3 or nine months; total modified $2.1M and $13.3M, personal instalment and C&I. **Label NO BLOCK.** N still grades from the Call Report at the 11/07 run.

## 5. Bank OZK 10-Q

**Source:** FDIC FLNG id 12040, attachment 1, posted 16:49 ET 11/06. Read for my four §6 lines and the modification table only. **The OZK desk owns the full read; its open legs (where the −$313M went, RaDD, Sullivan, debt-on-debt) are not graded here.** No filing text names RaDD; I searched that word and nothing else.

| Line | Result |
|---|---|
| OREO sold near carrying value | **STILL UNTESTED.** $10.6M sold in nine months vs $420.4M stock, 2.5%. No sale-vs-carrying figure. Write-downs $7.4M, Q3 $4.4M |
| Special mention falls | **MET.** $303.5M vs ~$616M; two RESG credits are $209.9M of it |
| NPA stops rising | **MET on the total, by mix.** $509.5M vs $593M [6/30, OZK desk]; nonaccrual $89.1M, OREO $420.4M |
| No new RESG loan to nonaccrual or OREO | **NOT MET, known since the release:** Boston life science sale failed, $132M into OREO in Q3 (`reports/2026-10-20_backlog-followthrough.md`). The 10-Q's largest nonaccrual is a $40.0M RESG land credit; when it went on is not checked |

Foreclosed assets carry a management discount of 0–20%, 10% weighted. **Modifications: no CRE. Q3 is one C&I term extension, $44.9M, 0.7% of the class.** Label NO BLOCK.

## 6. Screen count, updated

Original count stands as made in `reports/2026-11-06_re-modification-screen.md`. **Now: RE-MODIFIED 1, STILL HELD 2, PAID 1, NOT DISCLOSED 2 (SSB, CFG), NO BLOCK 8.** Valley alone.

## 7. Not done

- WAL 11/06 row in `registry/REG_T02_EXIT_LOG.tsv`: not graded, second route empty at 17:16 ET.
- FLG desk and OZK desk reads, GDOT (no filing since 10/20 at SEC), PFBC 10-Q (FDIC, most likely Mon 11/9): open.
- No Call Report run, no ranking test; those stay for 11/07.
