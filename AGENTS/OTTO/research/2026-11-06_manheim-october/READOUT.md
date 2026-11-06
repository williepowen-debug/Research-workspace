# Manheim October print: OTTO-37 graded, and the MFIC auto marks read at primary

OTTO s042, 2026-11-06, PROME assignment on Will's word (15:24 ET), bounded, $0, no paid data, no trade. No score, band, gate or threshold moved.

## 1. OTTO-37: FALSIFIED

| Field | Value |
|---|---|
| Claim | October-2026 full-month seasonally adjusted index, first published, >= 207.0 |
| Print | **206.8**, Cox "Manheim Used Vehicle Value Index: October 2026 Trends", dated Nov. 6, 2026 |
| Miss | 0.2 points |
| As-made | 60%, first commit `99ca8d3c5a`, 2026-11-05 18:17 ET, before publication |
| Brier | 0.3600, counted |
| Scoreboard | 3 of 9 hits, sum 2.5750, mean 0.286111 (was 3 of 8, 0.276875) |

Cox, Key Metrics, verbatim: *"The Manheim Used Vehicle Value Index (MUVVI) in October was 206.8, reflecting a 2% increase in wholesale used-vehicle prices (adjusted for mix, mileage, and seasonality) compared to October 2025. The Manheim index is up 0.5% month over month."* Non-adjusted: +0.3% YoY, −2.3% against September, against a long-term October average of −1.5%.

## 2. What the print means

**The year-on-year rise is mostly the base, not October.** Cox's chief economist says the index is 2% higher *"against depressed values last October"*. Levels implied by Cox's own percentages: September 2025 ~207.1, October 2025 ~202.7, a drop of ~2.1% `[EST, from rounded figures]`. So of the swing from −0.6% YoY in September to +2% in October, about +0.5pp is October's own move and about +2.1pp is the year-ago base falling away. The non-adjusted +0.3% YoY says the same. The index is 3.9% below March's 215.3.

**The hinge did not move.** The catalyst row's test was a second consecutive negative YoY print or <= −3%. Neither happened. Hinge stays 🟠. The SDT control is inside its ±3% band, so Manheim does not decide the ~11/15 run; the ledger's frequency change does, and the expected outcome stays NO VERDICT.

**Small unresolved item.** 206.8 over September's published 205.9 is +0.44%, and Cox says +0.5%. Rounding can reach +0.486% only at the extreme of both levels, so either that or a small September revision. The page shows no September level, so this cannot be settled here. It does not affect the grade, which is on the October level as first published.

## 3. Was 60% a bad forecast? No. The note beside it was wrong.

The OTTO-37 row said no base rate was computable. Cox's pages are free and carry all of it: `MID_TO_FINAL.tsv`, ten 2026 pairs.

| Measure, nine pairs before October | Value |
|---|---|
| Final fell by no more than the 0.4 this row needed | **5 of 9, 56%** |
| Final minus mid-month, mean | +0.21 points |
| Standard deviation | 1.40 points |
| Range | −1.5 to +2.3 |

60% against 56% is a fair number that lost. A 0.4 cushion is small against a 1.40 standard deviation. ⚠️ One calendar year, and the sign tracks the month's trend: positive in January to March, negative in April to July. The recent subset alone reads 2 of 6, which would overstate the miss; the full sample is the honest figure, still n=9. A mean of +0.21 against that spread gives no sign of bias in mid-month, only noise.

## 4. MFIC: what the filing says about the two consumer-finance names

BROCK's note checked against the schedules: 10-Q `0001193125-26-447829` (filed 11/05, sha256 `0714caea…bdbf0`) and Q2 10-Q `0001193125-26-335848` (sha256 `d5827958…2cdc`). Dollars in thousands, at 9/30 and 6/30/2026.

| Position | Cost 6/30 | FV 6/30 | Ratio | Cost 9/30 | FV 9/30 | Ratio | Status 9/30 |
|---|---:|---:|---:|---:|---:|---:|---|
| Auto Pool 2023 Trust (US Auto) | 18,708 | 7,555 | 0.40 | 18,290 | 2,010 | **0.11** | non-income |
| LendingPoint LLC first-lien term | 38,890 | 20,218 | 0.52 | 39,042 | 16,421 | **0.42** | **non-accrual** |
| LendingPoint LLC unsecured | 1,842 | 1,842 | 1.00 | 1,842 | 0 | 0.00 | non-income |
| LendingPoint LLC, entity total | 40,732 | 22,060 | 0.54 | 40,884 | 16,421 | **0.40** | |
| LendingPoint 2018-1 Funding Trust, two loans | 18,756 | 18,159 | 0.97 | 18,593 | 17,925 | 0.96 | accruing |
| LendingPoint preferred and common | 3,693 | 0 | 0.00 | 3,693 | 0 | 0.00 | non-income |
| **LendingPoint, whole relationship** | 63,181 | 40,219 | **0.64** | 63,170 | 34,346 | **0.54** | |
| Consumer Finance sector | 81,889 | 47,774 | 0.58 | 81,460 | 36,356 | 0.45 | |

**BROCK's figures hold; one label does not.** US Auto 0.40 to 0.11, LendingPoint non-accrual and the $39.0M / $16.4M all tie. The "LendingPoint group 0.54 to 0.40" row is the LLC entity. The whole relationship went 0.64 to 0.54. The −$5.9M beside it is the whole-relationship figure (40,219 to 34,346).

**US Auto is not a live lender.** MFIC's footnote: about 22.5% of a trust holding *"a pool of retail auto loans and residual interests in auto loan trusts"*, plus an interest in residual assets from the U.S. Auto Finance bankruptcy. So this is the leftover slice of an old workout. The mark is MFIC's own. Scaling MFIC's mark to the whole trust gives roughly $33.6M to $8.9M `[EST: assumes the mark applies pro rata]`. The cause of the quarter's −$5.1M is not stated.

**LendingPoint: the non-accrual is one loan, and "0.42 of cost" overstates how bad it looks.** Cost is $39.0M on $21.8M of principal, so the same mark is 75 cents on principal (95 at 6/30). The rate cell changed from "SOFR+500 PIK" to "9.10%"; why is unread. The funding-trust loans stay accruing at 0.96. Nothing in this filing ties LendingPoint to auto; OTTO has no auto link on record, and the 10-Q names only "underperformance".

**Consequence for OTTO:** neither is a fraud case and neither meets a charter trigger. Both go on `combo:lender-standstills`. No score, probability or threshold moved.

## 5. Other cards

- SIG-W-20261106-021, BROCK on Ares: a small revolver (`Tricolor Funding SPV 3 LLC`, $655,145 at 9/30/2024) in one co-managed fund, gone by 12/31/2024. Not established as an Ares Agent Services facility. A holding is not an implication, so OTTO-33 stays 70%. Logged on `combo:tricolor-new-names`.
- SIG-W-20261106-033: Cybertruck production ending around mid-2027, Musk on X, Reuters via NBC. No OTTO channel.
- SIG-W-20261106-019: NY Fed date 11/10 was already on the calendar.

## 6. Sources and limits

| Source | Read | sha256 |
|---|---|---|
| Cox October page, `coxautoinc.com/insights/manheim-used-vehicle-value-index-october-2026-trends/` | curl, 2026-11-06 | `726421295ef66b9a7e737ae72b09f44f5443df5b2bf9e78e841cfb7ee3d795c2` |
| Cox mid-October page | curl, 2026-11-06 | `78f4c908793307e76c1fca21bdc4feac5befefd6e26a327002429d4ad32357e3` |
| Cox September page | curl, 2026-11-06 | `3507108e3997dfe83c9b3792703fef0eb47e56a7cf571814b801cc463674b49c` |
| MFIC Q3 10-Q | SEC archive, 2026-11-06 | `0714caeaad1ee7db40018d5ab1ccb08a8f0ace9b48a1a2a9a1e70d2731fdbbf0` |
| MFIC Q2 10-Q | SEC archive, 2026-11-06 | `d582795895e06a5bfa1ba2d7efb36842658e54af7b0360c11528045a3d1d2cdc` |

Raw downloads not committed (38 MB each for the 10-Qs). The other Cox monthly pages follow the same URL pattern and were read once for their first sentence. Not read: MFIC's earnings call, any US Auto trust report, the U.S. Auto Finance bankruptcy docket. Cox's segment chart is an image and was not read.
