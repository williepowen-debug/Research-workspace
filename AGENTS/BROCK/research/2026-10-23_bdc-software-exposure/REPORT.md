# WQ-511 — Which BDCs hold the AI-disruption software loans, how are they marked, who prints first

> **CORRECTION 2026-10-25 — current use:** FSK's $1.1264B discrepancy reconciles as $1.1110B unfunded offsets plus $15.4M money-market cash. Its **funded-only software debt FV/par is 85.4%, with 25.6% of funded par below80**, superseding the gross 87.0/21.9 figures below. The six-name shared-borrower ±1.4-point conclusion is **WITHDRAWN pending a comparable funded-only rerun**; FSK PIK/rest-of-book ratios are not revalidated. BXSL COST non-accruals3.6%; HTGC liquidity652.9M includes175M LOC, separate from cash/borrowing. GBDC per-name undrawn allocation remains UNKNOWN. Full source bridge and reproduction: [October25 correction](../2026-10-25_bank-and-bdc/REPORT.md). **The remainder is preserved October23 analysis as-made, including Experiment A's original expectation; corrected source/basis governs current use.**

**Desk:** BROCK · **Written:** 2026-10-23 17:0x ET (from `date`) · **Commission:** WQ-511, Will 2026-10-23 16:43 ET, verbatim *"511 approved"* (packet `inbox/processed/2026-10-23_from-PROME_WQ511-RULED-bdc-software-exposure.md`) · **$0 moved; no trade; TERRY constructs; root rule #5.** No threshold, gate or score moved by this report.
**Draft quality, by design:** built in one session so TERRY has the BDC leg before the 10/27 close. Every BDC figure is from the 6/30/2026 10-Q (the latest filed), parsed from the filing's own inline-XBRL schedule of investments (SOI) by `scripts/` in this folder. **Q3 (9/30) marks are not filed yet; this table goes stale at each print.**
**Vendor prices are not official** (fetch.py, 10/23 close, read 16:57 ET).

## 1. The table (as of 6/30/2026 filings; prices 10/23 close)

| | **ARCC** | **BXSL** | **FSK** | **GBDC** | **HTGC** | **OBDC** |
|---|---|---|---|---|---|---|
| Software label (the BDC's own) | Software and Services | Software | Software & Services | Software | Application + System Software | Internet software and services |
| Software at fair value | **$6.45B** | **$2.52B** | **$2.02B** ⚠️a | **$2.14B** | **$1.50B** | **$1.73B** |
| % of portfolio FV | 22.0% | 18.9% | 17.7% | 26.0% | 32.8% | 11.6% |
| **% of NAV** | 46.4% | 42.5% | 39.5% | 57.6% | **66.0%** | 24.6% |
| Software FV ÷ cost | 0.950 | 0.913 | 0.904 ⚠️a | 0.978 | 0.982 | 0.994 |
| **Software debt mark (FV ÷ par)** | 95.8 | 90.4 | **87.0** | 97.5 | **98.7** | 98.2 |
| Share of software debt par marked <90 | 11.6% | 24.5% | 36.7% | 0.8% | 2.3% | 1.0% |
| Share marked **<80** (issuers <80) | 4.2% (3) | 17.1% (3) ⚠️b | **21.9%** (4) | 0.5% (3) | 2.3% (3) | 1.0% (3) |
| Rest-of-book debt mark (non-software) | 95.9 | 96.7 | 89.3 | 96.9 | 100.1 | 94.9 |
| Same-borrower test: mark vs peers on shared software names | +1.3 pts (29 names) | −0.7 (30) | −0.4 (10) | +0.7 (36) | n/a (no overlap) | −1.4 (28) |
| PIK-bearing share of software FV ⚠️c | 25.4% | 17.9% | 6.7% | 24.5% | **44.5%** | 22.6% |
| Unfunded commitments, total | $4.98B (XBRL-tagged gross) | $1.4B | $1.11B debt + $0.07B equity + $0.43B to COPJV | $0.58B (incl. $0.23B revolvers) | $0.41B | $1.49B |
| …of which to software names | $1.08B | $0.29B | $0.38B | not tagged | $0.06B | $0.25B |
| Liquidity (undrawn, subject to borrowing base) | $3.86B revolver + $0.38B cash | $2.6B + $0.27B cash | $3.05B | $1.73B (JPM facility) | $48M cash + facilities (not extracted) | $4.14B |
| Non-accruals, latest (basis) | 2.4% cost / 1.4% FV | 6 issuers (8 loans); % not extracted | 3.8% FV | 2.9% cost / 1.9% FV | 0.3% cost | 0.8% FV |
| NAV/share 6/30 | $19.35 | $25.53 | $18.30 | $14.25 | $12.15 | $14.26 |
| Price 10/23 close (vendor) | $18.64 | $23.33 | $10.44 | $12.12 | $16.41 | $10.05 |
| **Price ÷ 6/30 NAV** | 0.963 (−3.7%) | 0.914 (−8.6%) | **0.570 (−43.0%)** | 0.851 (−14.9%) | **1.351 (+35.1%)** | 0.705 (−29.5%) |
| Illustrative NAV hit if software debt were marked at the syndicated software average (88) ⚠️d | 3.1% | 1.1% | 0% (already below) | 5.2% | **7.1%** | 2.4% |
| **Next print (company-announced)** | **Tue 10/27 before open; call 12:00 ET** | Wed 11/04 morning; call 09:30 ET | Thu 11/05 before open; call 09:00 ET | Tue 11/17 after close; call Wed 11/18 10:00 ET (FY Q4, 10-K) | **Thu 10/29 after close; call 17:00 ET** | Wed 11/04 after close; call Thu 11/05 10:00 ET |
| **One-line read: software book vs the loan index** | **In line** with its own book, ~8 pts above the syndicated average; bellwether, prints first | **Mostly marked**: 90.4, Medallia at 49.5 does the work | **Ahead** (marked below the syndicated average) | **Behind**: 97.5, near-zero <80, but 15% discount already covers it ~3× | **Behind and not discounted**: 98.7 on 66% of NAV at a 35% premium | **Behind on its label**, but its label leaks (see caveat e); discount is about the rest of the book |

**Index side (DEWEY's REQ-003, `AGENTS/DEWEY/output/2026-10-23_ccc-and-under-80-loans-three-way-split.md`, d0d5463a7 + correction 23209b69f — cited as DEWEY's):** leveraged loans priced ≤80: **$139.8B**, of which **technology 39% ($54.4B)** (JPM 10/6, via reprint), named credits PE-owned software (CDK, Qlik, Quest); software is ~10–13% of the loan index ⇒ ~3× over-represented. **Average syndicated software loan price ~88 vs ~96 non-software (PIMCO 10/14; ~10-point gap already in June).** The ~88 is the comparator in the table. My estimate, not DEWEY's: if software is ~10–13% of a ~$1.5T index, roughly 28–36% of syndicated software/tech par sits ≤80 [EST; index size is my assumption and "technology" is wider than software]. **Against that, every BDC's software book except FSK's has ≤4.2% of par below 80 and BXSL's 17.1% is mostly one name.**

## 2. Pick, trap, falsifier

**Pick: HTGC (Hercules Capital).** It's the sharpest single expression of "the AI-disruption loan bucket is under-marked and the market hasn't priced it":
- largest software share of NAV (**66.0%**);
- highest software mark (**98.7** of par; 2.3% of par below 80);
- highest PIK-bearing share of the software book (**44.5%**);
- the only name trading **above** NAV (**+35.1%** on 6/30 NAV).

A mark to the syndicated average would cut NAV ~7%, and the premium can compress on top of that. Its borrowers are venture-backed growth software (seat-priced SaaS, the cohort most exposed to AI substitution), and they depend on follow-on venture equity. WALTER 008 (Slok/Ramp) says venture money is concentrating in AI. That's a mechanism hypothesis, not a measured flow. It prints second: **Thu 10/29 after the close**.
- ⚠️ **What argues against it, and stays with the pick:** venture debt isn't syndicated LBO debt. HTGC loans are short-dated, amortising, low loan-to-value, with warrants and exit fees, so the 88 comparator is weakest here. HTGC has held a premium through past cycles (no premium base rate computed this session). Non-accruals are 0.3% of cost. **A short here is as much a bet on premium compression as on marks.** TERRY sizes and judges that.

**Trap: FSK.** It's already marked and already discounted:
- software debt marked **87.0**, below the syndicated average;
- **21.9%** of software par below 80 (Medallia 50.1, Tangoe 72.5, Solera 76.9);
- the whole book is weak (rest 89.3) and it trades at **0.570× NAV**.

The markdown the thesis predicts is already in both the NAV and the price. **Second trap: OBDC (0.705×).** Its discount is about the non-software book (94.9) and the Blue Owl wrapper story, not its 11.6% software label.

**Falsifier for the pick at the Q3 print (Thu 10/29 after close):** **HTGC's 9/30 Application + System Software book is still marked ≥97% of cost, non-accruals stay ≤1.0% of cost, and NAV/share is ≥$12.15.** If all three hold, the AI-disruption stress hasn't reached venture-software marks this quarter. The premium is then defended by the books, and the trade has no mark catalyst before Q4.
- Read it from the 10-Q SOI, not the press release: the release won't carry the software-book mark.
- The same SOI parse (`scripts/`) re-runs on the Q3 filing in minutes.

**Earlier read for TERRY's 10/27 card: ARCC prints Tue 10/27 before the open.** ARCC is the largest software book ($6.45B, 46% of NAV), marked in line with its own book. On shared software names it marks +1.3 pts above peers, the most generous of the six. The read: if ARCC's Q3 software FV/cost falls from 0.950 by ≥2 points, or its software <80 share rises from 4.2% to ≥8%, the under-mark thesis has its first confirmation from the bellwether before HTGC. If neither happens, the thesis waits for HTGC (10/29). These are reading guides, not registered thresholds.

## 3. What this does NOT show (caveats that travel)

- **a. FSK reconciliation gap.** FSK's own SOI section totals sum to $12.54B FV / $13.73B cost. Its balance sheet shows $11.42B / $12.61B, and the gap is identical at cost and FV ($1.126B). Its software rows sum to $2.40B, against its industry table's $2.02B. I use the industry table ($2.02B, 17.7%) for exposure and the SOI rows only for mark ratios. The reconciliation is UNKNOWN.
- **b. BXSL's <80 share is one name.** Medallia is $395M par at 49.5. Ex-Medallia, BXSL's software <80 share is ~3.4% (~$81M of ~$2,390M par).
- **c. PIK basis.** "PIK-bearing share" is the FV of positions with any tagged PIK rate. It is **not** PIK income as a share of total investment income (my REGIME-line basis). ARCC on the income basis, Q2'26, non-controlled/non-affiliate segment: PIK interest $51M + PIK dividends $63M = 18.4% of that segment's $620M income. HTGC: PIK receivable ~2% of debt investments (10-Q).
- **d. The 88 comparison is illustrative, not a forecast.** Private loans aren't syndicated loans: different borrowers, tighter documents, model-based marks. The ~88 is a syndicated average (PIMCO via DEWEY), at 10/14 against 6/30 marks. The gap was already ~10 pts in June, so timing doesn't explain it.
- **e. Labels leak, and they are not like-for-like.** OBDC holds Pluralsight (44.7) and Cornerstone OnDemand (57.5), but **outside** its software label. ARCC's and FSK's GICS "Software & Services" is broader than "Software". Each column measures the BDC's own label.
- **f. The same-borrower test cuts against "lenient manager" stories.** On 53 software names held by ≥2 of the six, marks agree within ±1.4 pts par-weighted (Medallia: BXSL 49.5 / FSK 50.1). The dispersion between BDC software marks is **mix, not lenience**. "Under-marked" is a claim about the private market against the syndicated market, not about one manager. Tranches can differ under one issuer name, and the 2-word name match can conflate issuers.
- **g. Mark basis.** FV ÷ par is used for USD debt; non-USD debt uses FV ÷ cost (XBRL principal is in local currency). Equity is excluded from the debt mark.
- **h. Unfunded "to software names"** matches company names between the commitment contexts and software positions; GBDC doesn't tag per-position commitments. These are 6/30 figures; ARCC's is XBRL-tagged gross before its "unavailable commitments" adjustment.
- **i. Totals reconcile exactly** to each filing's total investments at FV for ARCC ($29,349.3M), BXSL ($13,364.3M) and OBDC ($14,955.0M). HTGC is within 0.5% after excluding 28 company-subtotal contexts. GBDC is within 0.5%, and its software subtotal matches XBRL ($2,135.05M) within $2.4M. FSK: see (a).
- **j. Not covered:** BBDC/GSBD/OCSL/NMFC/MAIN, which have smaller software dollars per DEWEY's table. BIZD weights. Q3 marks.

## 4. Sources

- **SEC 10-Q (6/30/2026) accessions** (DEWEY's list, re-fetched from EDGAR by BROCK 2026-10-23 16:47–16:51 ET; XBRL instance + primary HTML): ARCC 0001628280-26-050307 · BXSL 0001736035-26-000016 · FSK 0001628280-26-053783 · GBDC 0001476765-26-000048 · HTGC 0001280784-26-000042 · OBDC 0001655888-26-000056. Non-accrual, unfunded and liquidity sentences are quoted from each 10-Q's text; NAV/share and total FV/cost come from its XBRL.
- **Print dates:** company announcements.
  - ARCC: [release](https://www.bdcinvestor.com/arcc/202610/ares-capital-corporation-schedules-earnings-release-for-the-third-quarter-ended-september-30-2026); one estimate calendar says 10/28, but the company says 10/27.
  - HTGC: [release](https://www.bdcinvestor.com/htgc/202610/hercules-capital-announces-date-for-release-of-third-quarter-2026-financial-results-and-conference-call).
  - BXSL: [release](https://www.bdcinvestor.com/bxsl/202610/blackstone-secured-lending-announces-third-quarter-2026-earnings-release-and-conference-call).
  - GBDC: [8-K](https://www.sec.gov/Archives/edgar/data/0001476765/000147676526000072/earningscallnotification-e.htm).
  - OBDC: [8-K](https://www.sec.gov/Archives/edgar/data/0001655888/000165588826000063/exhibit991pressrelease-sch.htm).
  - FSK: issuer 10/8 (KB-BRK-334).
  - These are web-search summaries of the releases; the release bodies were not opened.
- **Index side:** DEWEY REQ-003 (above), and through it JPM 10/6, PIMCO 10/14 and Janus 10/15. CCC context is from DEWEY's `2026-10-23_ccc-concentration-optimum-altice.md`: the rated-CCC basket is 0% AI builders and ~5.9% software. **The software stress is a loan/BDC story, not a CCC-bond story** (WALTER 039 correction applied).
- **Prices:** `FORGE/tools/market-data/fetch.py price`, 2026-10-23 16:57 ET, as-of 2026-10-23 (vendor, unofficial).
- **Reproduce:** `scripts/soi.py <TK> <10-Q.htm> <10-Q_htm.xml> 2026-06-30 <outdir>` → `scripts/metrics.py` → `scripts/cross.py`. Outputs are in `metrics_2026-06-30.json`. The downloads are not committed (≈175 MB); re-fetch them by accession.
