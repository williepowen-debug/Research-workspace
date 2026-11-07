# Three Call Report ledgers refreshed to 9/30, and what that changes, Saturday 2026-11-07

**Desk:** REGINALD, PROME prome-bf task 09:41 ET. **Basis:** bank-level FFIEC Call Reports, pulled 11/07. **Nothing moved:** no score, band, threshold, gate, prediction, trade or judgment word. L180 and the concentrated qualifier were not reopened.

## 1. The answer first

The refresh changes four claims, all wording or instrument claims, none of them a score. The largest: this desk told the FLG desk on 8/20 that Flagstar was an outlier because half its quarters did not tie. That was my test, not Flagstar. The test left out two disclosed lines. With them, 168 of 168 tie.

| Ledger | Rows | Added | Prior rows recomputed from the primary |
|---|---:|---:|---|
| `NDFI_COHORT.tsv` | 52 | 26 at 9/30 | 26 of 26, 0 differences |
| `ACL_ROLLFORWARD_COHORT.tsv` | 182 | 14 at 9/30 | 168 of 168, 0 value differences |
| `RUNWAY_COHORT.tsv` | 182 | 14 at 9/30 | 168 of 168, 0 differences |

The 8/20 ledgers were hand-built with no builder, so the method was recovered from the rows and `scripts/call_report_ledgers.py` now carries it. `recoveries_K` was blank on all 168 rows and is filled from RIAD4605, which changes no other cell. Next due 2027-02-14.

## 2. Claims that change

| # | Claim, where it lives | Result | Consequence |
|---|---|---|---|
| 1 | "FLG ties 6/12 = 50%, an OUTLIER (worst WAL 3/12, CUBI 5/12)", ACL header, 8/20 packet to FLG, `../FLG/THESIS.md:188` | **RETIRED.** As-built identity omits RIAD5523 write-downs on transfer and RIADC233 adjustments. As built 127 of 168; full identity **168 of 168**, and 14 of 14 at 9/30. Of the 41 misses, 20 carry write-downs, 26 adjustments | The hypothesis "major balance-sheet events" is answered: these are disclosed lines. The 8/20 "24.4% non-tying" and "38% of windows" are not unexplained breaks |
| 2 | "FLG's runway has LENGTHENED every quarter since", matrix §3, PROME `DOCKET.tsv` line 52 "lengthened 8 straight qtrs" | **WRONG, and already wrong on 8/20.** 1.29 [3/31/25], 1.59, 1.90, **2.36 [12/31/25]**, 2.25, 2.15, **2.17 [9/30/26]**. Peak, then down 0.19yr in three quarters | Matrix corrected. The FLG desk's "moving AWAY from every cut at ~+0.06yr/quarter, on trend it never arrives" took that from me; the sign since the peak is about −0.06yr/quarter. K-3 stays UNSET; FLG's call |
| 3 | "~$15.9B funded + $22.5B unfunded ≈ $44.5B committed" at CFG, matrix §4, `STATUS_MATRIX.md` | **The sum never worked.** $44.5B is all NDFI, $22.0B funded + $22.5B unfunded. Private credit alone, Memo 10 b+c plus RC-L 1.e.3 b+c: $15.9B + $13.4B ≈ $29.3B [6/30]; $16.2B + $13.6B ≈ $29.7B [9/30], 10.82% of loans funded. All NDFI 9/30: $23.0B + $22.2B = $45.2B | Corrected in both files. CFG stays 2nd by share behind CUBI |
| 4 | "EGBN 0.53yr", lowest runway, matrix §3 table at 6/30 | **1.28yr [9/30]**, still lowest. Q3-2025's $141.1M of charge-offs leaving the window did it, not new reserve: allowance $121.1M → $120.8M | Dated table left at 6/30. The disposition bias note still applies |

## 3. What the 9/30 rows show

| Runway, years | EGBN | WAL | OZK | AMTB | FLG | CUBI | BKU | CFG | MTB | HBAN | VLY | SSB | SBCF | ZION |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6/30/2026 | 0.53 | 1.44 | 1.93 | 1.59 | 2.15 | 2.39 | 2.39 | 2.69 | 3.02 | 5.03 | 6.63 | 7.51 | 11.14 | 6.27 |
| 9/30/2026 | **1.28** | 1.45 | 1.89 | 1.97 | 2.17 | 2.58 | 2.69 | 2.72 | 3.13 | 4.54 | 5.16 | 10.11 | 11.04 | 13.50 |

Cohort, 126 windows: p10 1.43, median 2.95, p90 7.51. ⚠️ HBAN carries $578.3M of adjustments, Cadence (INFERRED from the 10-Q's all-in basis), so its allowance and trailing charge-offs are not like-for-like. Including RIAD5523 moves only FLG 2.17 → 2.12 and WAL 1.45 → 1.41, no rank change.

**Flagstar's reserve stopped falling in Q3.** Allowance $869.000M → $868.998M. Q3 provision $74.1M against charge-offs $83.7M, 1.13× for the quarter; year to date 3.51×, the ledger's YTD basis. H1 was 14.6×. One quarter, and the ledger's method cannot say why; the FLG desk's K-3 primary leg is the place to read it.

**NDFI, all 26 banks.** Funded $962.6B → $1,017.2B (+5.7%); private-credit slice $498.1B → $523.4B (+5.1%). Domestic-office basis at 031 filers.

| 9/30 vs 6/30 | Result |
|---|---|
| WAL nonaccrual, "2nd-largest absolute in the 26" | **Stands.** $122.5M behind WFC $134.0M |
| WAL mortgage-warehouse share | 68.9% → 68.0% |
| CUBI private-credit slice | +12.3%, 21.81% of loans, matches report 11/07 §5 |
| 14-bank nonaccrual | $223.3M → $215.3M, matches report 11/07 §5 |
| ★ **FLG private-credit slice** | **$1,069M → $2,139M, +100.1%.** Business-credit $202M → $673M, private-equity funds $867M → $1,466M; total NDFI +30.5%; unfunded private-credit lines $625M → $1,002M. Reclassification vs new lending not established. Same quarter as FLG's MI3 +54.1% |
| Others up >15% | VLY +22.7%, SSB +18.3%, HBAN +16.3% |
| 26-bank 30-89 past due | $540.4M → $757.3M, mainly BAC $2M → $167M and JPM $343M → $433M; 14-bank $81.8M → $28.5M. 0.07% of the book; nonaccrual fell $505.8M → $479.2M |

Logged under `combo:bank-lending-to-private-credit`, KB ML-REG-292. Logging is not scoring.

## 4. Not changed

Matrix scores; the frozen ranking result; the 14.6× line and the ≥10× tail, still FLG's two 2026 quarters alone; ZION the only release, now 3 of 182; `LESSONS.md` NDFI figures, dated 6/30; FLG-owned files, packet sent.

## 5. Verified, inferred, unknown

- **VERIFIED:** every figure, by command: `claims.out`, `writedown_sensitivity.out`. 12 large-bank RSSDs confirmed by name at FDIC BankFind 11/07, which upgrades the ledger's old MED identity note.
- **INFERRED:** HBAN adjustment is Cadence.
- **UNKNOWN:** why FLG's private-credit slice doubled; whether FLG's Q3 provision is a one-quarter event.
- **⚠️ Basis:** at FFIEC 031 filers the ledger divides nothing across groups but mixes RCON loans and Memo 10 with RCFD unfunded and past-due. Kept for continuity, stated in the header.
