# KRE shares outstanding — one- and two-month review

**Date:** 2026-11-03 12:52 ET  
**Question:** Are recent KRE redemptions unusual, and do they show a sustained investor exodus?

## Answer

Not on the completed official history. KRE has had large two-way creation/redemption swings, but almost no net change in shares outstanding over two months. The latest completed official decline was meaningful rather than unprecedented, and the one-month net share count is higher.

| Window through 2026-11-02 | Net share change | Net % | Creation days | Redemption days | Gross shares created | Gross shares redeemed |
|---|---:|---:|---:|---:|---:|---:|
| One month, from 2026-10-02 | +2,550,000 | +5.01% | 9 | 12 | 22.70M | 20.15M |
| Two months, from 2026-09-02 | −300,000 | −0.56% | 18 | 24 | 40.80M | 41.10M |

Shares outstanding were 53,752,585 on 2026-09-02, 50,902,585 on 2026-10-02 and 53,452,585 on 2026-11-02.

## Latest completed day and base rate

State Street's 2026-11-02 observation shows shares outstanding falling **2.15M (−3.87%)** from 2026-10-30. At that day's $73.687961 NAV, the redeemed shares represented approximately **$158M**.

That was the **sixth-largest decline among 42 daily changes** in the two-month window. Five completed days had larger share reductions:

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
- Two-month extract with daily changes: `data/kre_shares_2026-09-02_to_2026-11-02.csv` (43 rows: baseline plus 42 daily changes).
- Daily percentage = current shares outstanding / prior completed observation − 1. Gross creation/redemption figures are the sums of positive/negative daily share changes, not issuer-reported dollar flows.
