# KRE shares outstanding — one-, two- and three-month review

**Date:** 2026-11-03 12:52 ET; three-month extension added after the initial review
**Question:** Are recent KRE redemptions unusual, and do they show a sustained investor exodus?

## Answer

The three-month view shows a genuine net contraction, but not a steady or one-way exodus. Shares outstanding fell **4.30M (−7.45%)** over three months, with most of the net decline in August and September; October partly reversed it. The two-month share count is almost flat and the one-month count is higher. Large creations and redemptions occurred throughout.

| Window through 2026-11-02 | Net share change | Net % | Creation days | Redemption days | Gross shares created | Gross shares redeemed |
|---|---:|---:|---:|---:|---:|---:|
| Three months, from 2026-07-31 | −4,300,000 | −7.45% | 30 | 35 | 54.00M | 58.30M |
| Two months, from 2026-09-02 | −300,000 | −0.56% | 18 | 24 | 40.80M | 41.10M |
| One month, from 2026-10-02 | +2,550,000 | +5.01% | 9 | 12 | 22.70M | 20.15M |

Shares outstanding were 57,752,585 on 2026-07-31, 53,752,585 on 2026-09-02, 50,902,585 on 2026-10-02 and 53,452,585 on 2026-11-02.

## Month-by-month path

| Observation | Shares outstanding | Change from prior row |
|---|---:|---:|
| 2026-07-31 | 57,752,585 | Baseline |
| 2026-08-31 | 54,502,585 | −3,250,000 (−5.63%) |
| 2026-09-30 | 53,702,585 | −800,000 (−1.47%) |
| 2026-10-30 | 55,602,585 | +1,900,000 (+3.54%) |
| 2026-11-02 | 53,452,585 | −2,150,000 (−3.87%) |

The three-month high was 61,952,585 on 2026-08-17 and the low was 47,452,585 on 2026-10-08. These are large swings around a smaller net decline, so a single daily redemption is a weak trend indicator.

## Latest completed day and base rate

State Street's 2026-11-02 observation shows shares outstanding falling **2.15M (−3.87%)** from 2026-10-30. At that day's $73.687961 NAV, the redeemed shares represented approximately **$158M**.

That was the **ninth-largest decline among 65 daily changes** in the three-month window and **sixth-largest among 42** in the two-month window. Five completed days in the shorter window had larger share reductions:

| Date | Daily share change | Daily % |
|---|---:|---:|
| 2026-09-29 | −5.30M | −9.23% |
| 2026-10-23 | −4.40M | −7.36% |
| 2026-09-17 | −3.45M | −6.08% |
| 2026-10-08 | −2.50M | −5.00% |
| 2026-11-02 | −2.15M | −3.87% |

Large creations also occurred: 2026-10-16 +8.10M (+16.53%), 2026-10-09 +4.90M (+10.33%), and 2026-09-28 +4.10M (+7.69%). The series is therefore two-way and volatile, not a one-way redemption wave.

## Instrument caveat

The 2026-11-03 boot monitor estimated a separate **2.2%** decline using Yahoo's `totalAssets / NAV`. State Street's official completed series ends at 2026-11-02 and gives a different level and daily change. These are different vintages/derivations; the vendor estimate is **not treated here as an official 2026-11-03 redemption**. It needs the next State Street observation for confirmation.

Share-count changes do not identify the authorized participant, its clients, or their motive. Creations and redemptions in KRE do not remove deposits or capital from the underlying banks.

## Source and reproducibility

- State Street Global Advisors, official KRE NAV history: `https://www.ssga.com/library-content/products/fund-data/etfs/us/navhist-us-en-kre.xlsx`
- Retrieved 2026-11-03; latest completed observation 2026-11-02; 5,129 valid dated rows in the full file.
- Download: `data/kre_navhist.xlsx`; SHA-256 `d9113ec7823fff4dd35625e0e2ad22031a2c6d22ae9cfd11f58e23e4baf2fefe`.
- Three-month extract: `data/kre_shares_2026-07-31_to_2026-11-02.csv` (66 rows: baseline plus 65 daily changes).
- Two-month extract: `data/kre_shares_2026-09-02_to_2026-11-02.csv` (43 rows: baseline plus 42 daily changes).
- Daily percentage = current shares outstanding / prior completed observation − 1. Gross creation/redemption figures are the sums of positive/negative daily share changes, not issuer-reported dollar flows.
