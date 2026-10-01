# RC2 evidence receipts — OTTO-10 and OTTO-29 re-read (session 026)

**Written:** 2026-09-30 22:10 ET (`date`) · OTTO s026, PROME spawn on CATO RC2/RC3 (CATO `433084d2b`, PROME packet `6ead07117`).
**What this file is:** the retrieval record that the OTTO-10 and OTTO-29 Result cells in `thesis/PREDICTIONS.tsv` cite. The grades and their reasoning live in those cells and in `thesis/PREDICTIONS_ARCHIVE.md`. This file only says what was fetched, from where, when, and what it contained. Everything here was free; no PACER.

---

## 1. OTTO-10 — Equifax U.S. National Consumer Credit Trends Report, Originations

**The s025 record said** the Jul/Aug/Sep-2026 editions returned 404 (probed 2026-09-30 21:37:48Z at `originations-credit-trends-{jul,aug,sep}-2026.pdf`). **That was a guessed-URL SEARCH-NOT-FOUND, not an absence.** The July and August editions use the full month name.

| URL (base `https://assets.equifax.com/marketing/US/assets/`) | HTTP, 2026-10-01 01:59Z | Data coverage (the report's own footer) | sha256 |
|---|---|---|---|
| `originations-credit-trends-jun-2026.pdf` | 200 | "Originations through March 2026 reported as of May 2026" | `30959c47efa6192693a6dbf77072e491f6bae98f3fb2cc14b18aa118886566b0` |
| `originations-credit-trends-july-2026.pdf` | 200 | "Originations through April 2026 reported as of June 2026" | `b3067eb59ae46aea53cb7e691a1ce23dc60cb5f452044a343b3eaa1d26eb104d` |
| `originations-credit-trends-august-2026.pdf` | 200 | "Originations through May 2026 reported as of July 2026" | `164165a6b204f1409ba3a66de891ea8b6b973cc6f7b5c22f3099f3b220fb53bf` |
| `-jul-2026`, `-aug-2026`, `-sep-2026`, `-september-2026`, `-sept-2026`, `-Sep-2026`, `-September-2026`, `-sep2026`, `-september2026`, `-september-2026-1`, `-report-september-2026`, `-oct-2026`, `-october-2026` | 404 | — | — |

**The September-2026 edition (data through June) is SEARCH-NOT-FOUND at every variant above. It may exist under another name.** By the three editions' own pattern (edition month = data month + 3), the edition covering through **September 2026** would be the **December-2026** edition. That is INFERRED from three points, not a published schedule.

**Readings — "Auto: Total", borrower VantageScore 3.0 below 620, subprime share of originations** (table columns: YTD share; CURRENT MONTH share). Latest-month figures are first prints and may be revised.

| Edition | Through | YTD account share | YTD balance share | Month account share | Month balance share |
|---|---|---|---|---|---|
| Jun-2026 | Mar 2026 | 19.1% | 15.9% | 19.5% (Mar) | 16.3% (Mar) |
| Jul-2026 | Apr 2026 | 18.7% | 15.6% | 17.7% (Apr) | 15.0% (Apr) |
| Aug-2026 | May 2026 | 18.1% | 15.2% | 15.5% (May) | 13.1% (May) |

Same-month prior years, from the August edition's CURRENT MONTH column: May-2024 accounts 15.4% / balances **12.6%**; May-2025 accounts 16.6% / balances 13.5%. **So a monthly balance print below 13% has happened before (May 2024).**

Arithmetic behind the INFERRED note in the OTTO-10 row (August-edition figures, Jun–Sep monthly volume held at May's level): total accounts YTD-May ≈ 1,930.4K / 0.181 ≈ 10.67M; May total ≈ 330.4K / 0.155 ≈ 2.13M. Four more months at that rate gives a YTD-Sep total near 19.2M. A YTD-Sep account share under 13% would need Jun–Sep subprime accounts under ≈ 566K, which is a monthly share near **6.6%**. The lowest monthly account share in these tables is 15.4% (May 2024).

**Not read:** any later edition; Experian or the NY Fed as grading series (different perimeters, already recorded as not-this-instrument on the row).

---

## 2. OTTO-29 — Tricolor Holdings Ch.7, Case 25-33487 (Bankr. N.D. Tex., Judge Larson)

**The s025 record said:** a RECAP search found no distribution plan or motion; RECAP is a partial mirror; PACER unchecked.

### 2a. The claims agent's full docket (free, complete)
- **Source:** Verita Global (Kurtzman Carson Consultants, LLC), the court-appointed claims and noticing agent: docket title of **Dkt 939**, "Order authorizing expanded scope of retention and employment of Kurtzman Carson Consultants, LLC dba Veritas Global as Claims and noticing Agent". URL `https://veritaglobal.net/tricolor/document/list/6384` (form POST, no filters, page size 2000).
- **TLS:** the server sends only its leaf certificate. Verified properly, not bypassed: the missing intermediate (Go Daddy Secure Certificate Authority - G2, from the certificate's own AIA URL `http://certificates.godaddy.com/repository/gdig2.crt`) was added to the system CA bundle; curl `ssl_verify_result` = 0.
- **Retrieved:** 2026-10-01 02:06:20Z. Page sha256 `7623d20bc579c741e2ef688ad41c3f0899ed6c338234a548ecce3382efa09e85`. The 4/15–9/30 window query (02:05Z) has sha256 `7476503074b0260f414def2c8a5d46274011004bcd6a97c1f60ed949254ced46`.
- **Coverage:** TotalRecords 1,448; entry numbers 1–1451. **Absent: 480, 914, 938.** All three are also absent from the CourtListener RECAP index (search, 02:06:47Z). Their neighbours are dated 2025-11-25 and 2026-02-23 to 2026-03-12, so all three fall before this row was made (2026-04-15).
- **Scan:** every title was matched against `distribut|dividend|final report|disburs|interim report|noteholder`, and the 4/15–9/30 window was also matched against `securitiz|9019|compromise|settlement|turnover|release of funds/proceeds/collections|remit|waterfall`.
  - **No** motion or order for a distribution, dividend or disbursement to creditors or noteholders.
  - **No** Trustee's Final Report. The only report is Dkt 1113 (below).
  - **One** Rule 9019 settlement, with an individual (Jody Diaz: Dkt 1242, approved Dkt 1306, 2026-07-10).
  - The turnovers run **to** the estate (Dkt 1130, 1245). The abandonments are of physical property (Dkt 1122, 1189, 1233, 1238).
  - Wilmington Trust, N.A. appeared **"As Indenture Trustee For Each Securitization Transaction Listed On Annex A"** (Dkt 1246, 2026-06-15). Since then the Ch.7 trustee has been taking Rule 2004 discovery from it (motion Dkt 1287, 2026-07-01; stipulations Dkt 1334, 1401 on 8/21, 1432 on 9/03). That discovery is continuing, so no settlement has been reached.
  - Latest entries: Dkt 1450 (Vervent's third motion to continue its interim servicer-fee procedures) and Dkt 1451 (FTI 2004 stipulation), both 2026-09-30.

### 2b. The Ch.7 trustee's own interim report
- **Dkt 1113**, filed 2026-04-30, Form 1 (Individual Estate Property Record and Report), period ending 2026-03-31. Retrieved via DEWEY `recap_pull.py doc … --case 25-33487 --entry 1113`, which returned **VERIFIED: header 25-33487 Doc 1113 Filed 04/30/26**. 4 pp, sha256 `f915516ffbf683811758f2bbdc8be37ee661857f5b138de0dd5ec0b19ed6e433`.
- Text: **"Initial Projected Date of Final Report (TFR): September 30, 2030 · Current Projected Date of Final Report (TFR): September 30, 2030"** (signed Anne Elizabeth Burns, 2026-04-30).
- Asset 48: **"Claims to Estate ownership of Finance Receivables at purported fair values for amounts that could exceed $2.0 billion (u)"**. The estate claims the receivables that back the notes, so any recovery to noteholders runs through this fight.

### 2c. CourtListener RECAP index cross-check (DEWEY `recap_pull.py search`, anonymous, 2026-10-01 02:02–02:04Z)
- `docket_id:71308702` gives 2,004 documents. The latest 19 entries, 1433–1451 (9/09–9/30), are contiguous and line up number for number with Verita's list.
- Description searches: `distribution` returned 0. `"final report" OR "interim distribution" OR dividend` returned 1 (Dkt 1113). `disburse*` returned 1 (a 2/04 hearing on Chu's D&O-proceeds motion). `compromise OR 9019` returned 3 (all Jody Diaz). `Wilmington` returned 81 (latest: 2004 stipulations).

### 2d. What this does not reach
- **PACER itself was not read** (spend). Verita's list is the agent's mirror of it, and three entry numbers are missing from both mirrors.
- **Trust-level pass-through** (an indenture trustee paying noteholders out of trust collections outside the estate) is not observable. Tricolor's ABS were 144A private placements with no public 10-D distribution reports (`research/outputs/RP-OTT-1.6_Tricolor_ABS15G_Diligence_Forensics.md` line 22). Under the row's 4/15 definition that is a different event, and it is not graded either way.
