# OTTO catch-up, 2026-11-05 (s041): Exeter September collections and two lender reads

**Bottom line:** the Exeter recovery drop is real at the filing, one Exeter pool re-crossed the registered 28% line, and the monthly series is far noisier than the Severity-Divergence Test (SDT) assumed. One month is not a regime. The more important result is about the instrument: the SDT compares two single months, so its verdict can swing by 16 points on a two-month window shift.

**Sources:** four Exeter Ex-99.1 exhibits (10-D filed 2026-10-29, September collection period, saved in `sources/` with `SHA256SUMS`); CPS Ex-99.1 (October 22, saved); Credit Acceptance 10-Q accession `0000885550-26-000201` (filed 2026-10-29, sha256 `5877102f690d83aea20526c47f71f299cfdc89db6be95a97a989d27636a79a5d`, not stored; passages quoted below).

## 1. Exeter September collections, tied to the exhibits

`recovery_pct` = Net Liquidation Proceeds ÷ Receivables becoming Liquidated Receivables, line 93 ÷ line 92. Recomputed from the saved exhibits: all four match the panel to the cent of a percentage point.

| Deal | Liquidated $ | Net proceeds $ | Recovery Sep-26 | Aug-26 | Sep-25 | 60+ DQ Sep-26 | Sep-25 | Extension Sep-26 | Aug-26 | Sep-25 | CNL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EART 2022-2 | 2,629,951.38 | 503,488.09 | **19.14** | 25.17 | 38.18 | 15.60 | 13.21 | 5.60 | 4.49 | 7.12 | 27.25 |
| EART 2022-3 | 3,303,409.69 | 518,662.40 | **15.70** | 24.58 | 34.04 | 14.77 | 12.92 | 5.96 | 4.73 | 7.06 | 28.66 |
| EART 2023-1 | 2,880,989.29 | 606,084.79 | **21.04** | 24.79 | 37.36 | 12.26 | 10.83 | 6.42 | 5.29 | 7.00 | 23.54 |
| EART 2024-1 | 5,615,920.59 | 1,488,978.02 | **26.51** | 29.78 | 37.30 | 10.22 | 9.29 | 6.83 | 5.44 | 6.96 | 18.95 |

- **Recovery trigger:** 4 of 4 below 28%. EART 2024-1 is the new crossing in this episode (it held 29.57 to 31.00 from June to August, while the other three were below). **It is a re-crossing, not a first: it read 26.21 in December 2025 and 23.22 in January 2026.** Re-fire rule met; routed to WALTER.
- **Charter 🔴 band (<25%):** three deals are below it (two in August). STATUS holds the row at 🟠 for the reason in section 2. The disagreement is recorded here, not smoothed: the mechanical band reads hotter on one month's reading, and STATUS is the operative read.
- **Matched-month delinquency:** all four worse YoY, so September coverage is 9 of 9 deals worse and the available count is 48 of 48 deal-months since April. Those are repeated deal-months, not independent credits.
- **Extensions:** up month over month on all four (+1.11 to +1.39pp), still below the year-ago 6.96 to 7.12%. 60+ DQ rose on the two 2022 deals and fell on the 2023 and 2024 deals (12.32 to 12.26; 10.89 to 10.22), so the delinquency move this month is not uniform. Extensions rising and DQ falling on the younger deals is the pairing the desk rule exists to catch: this data cannot separate servicing from borrower quality.

## 2. How much of the drop is noise

| Measure (four-deal recovery, simple means, `[EST]` OTTO arithmetic on panel rows) | Reading |
|---|---|
| Monthly panel mean, Sep-25 to Sep-26 | 36.7, 24.9, 27.1, 24.2, **19.2**, 27.8, 27.0, 28.4, 25.1, 27.0, 26.2, 26.1, **20.6** |
| Standard deviation of that series | 4.15pp; 2.81pp without the Sep-25 spike |
| Per-deal SD, same 13 months | 3.86 to 5.34pp |
| Six months to Sep-26 vs prior six, per deal | 24.12 vs 23.36 · 23.08 vs 22.95 · 24.56 vs 24.12 · 30.41 vs 29.73: **flat to slightly up** |
| July to September YoY, per deal | 22.09 vs 26.37 · 21.27 vs 26.04 · 24.67 vs 31.30 · 29.10 vs 35.20: **down 4 to 7pp, inflated by the Sep-25 spike** |

The closest precedent is January 2026 (panel mean 19.2), which rebounded to 27.8 the next month. The dollar base is small: $2.6M to $5.6M liquidated per deal per month. Recovery fees paid to the servicer did not fall in step with proceeds, which pulls the net rate down in a thin month: EART 2022-3 fee $203,553 against gross $722,215 (28%), versus $321,433 against $2,104,744 (15%) in Sep-25. That is a mechanical observation about the measure, not a finding about servicer conduct.

**Comparison from another lender, different definition:** CPS reports Q3 net recovery on repossessed collateral sold at wholesale auction of **32.0% vs 28.7%** a year ago. That is auction proceeds only; Exeter's measure also carries liquidated balances with no auction sale, so the levels cannot be compared, but the direction differs. WALTER's card did not carry this line; it is in the primary release.

## 3. Instrument defect: the SDT is a two-point test

`severity_divergence.py` subtracts the first month from the last. THESIS states a noise floor of 2×SE = 1.23pp at n=12 on a pooled SD of 2.12pp. That arithmetic describes a 12-month average, and the script does not average. The panel-mean SD measured above is 2.81 to 4.15pp, so the difference of two single months has a 2-SD range of about 8 to 12pp. The +2.00pp CONFIRM line sits well inside that range. (The 2.12 was measured on five calm months, March to July 2026, per the script's own header.)

**Proof by example:** a read-only run on tonight's ledger with Manheim −0.6% returns panel ΔSeverity **+16.12pp**, ΔFrequency **+1.65pp**, **NO VERDICT** (first filing 10/28/2025, last 10/29/2026). The August reading on a window two months earlier was ΔSeverity **+0.06pp**, REFUTE. The severity move between those runs is mostly the endpoints changing: the first month is the Sep-25 spike and the last is this drop.

**What this does and does not change:**
- This run is a preview. It is not the second quarterly observation, which stays ~11/15 under the registered rule. No grade is recorded.
- ⚠️ The ledger cannot change before ~11/15, because the next Exeter filing is ~11/30. If October Manheim is inside ±3%, the 11/15 run will return this same NO VERDICT; if outside, NO VERDICT again. So the "three consecutive REFUTEs" consequence cannot complete on the original sequence.
- That NO VERDICT is not support for the Invisible Exit. CONFIRM needs ΔFrequency ≤ +0.50 and frequency rose +1.65. The six-month comparison above shows no severity trend.
- ⚠️ The August 14 REFUTE was produced by the same two-point method, so its "+0.06, no movement" is weaker than the thesis says. The grade stands as registered. General conviction stays LOW because six-month recovery is flat and the delinquency chain is visibly working, not because that single reading was precise.
- Registered terms are unchanged. Altering a test after seeing data earns no calibration credit, and OTTO-35's boundary stays as written. A redesign, if any, must be proposed before the next window with the change stated and no credit taken for it; no new checker is added here.

## 4. OTTO-34 path

EART 2022-3 CNL 28.66%, +0.26 on the month (prior +0.29, +0.25). Needs +0.34 across the October and November collections. Every two-month sum in the last 14 months was at least +0.51. At the recent pace the November print is about 29.18% `[EST]`. Remaining risks: a bulk recovery month, and the filing landing outside December. Current estimate 85%; as-made 60% is what scores.

## 5. Consumer Portfolio Services (SIG-W-20261031-018), integrated

`[CONF CPS Ex-99.1, October 22]` Contracts purchased $815.3M vs $391.1M (+108.5%). Total delinquencies including repossession inventory 12.29% vs 13.96%. Annualized net charge-offs 7.26% vs 8.01%. Auction net recovery 32.0% vs 28.7%. Portfolio $4.71B, +25%.

**Read:** company-specific counterevidence to a blanket credit shutdown. A portfolio growing 25% lowers ratio denominators, so falling delinquency and charge-off percentages are partly a growth effect, and a loan book that doubled originations has new loans not yet old enough to go bad. "Selective" is management's word. This does not resolve the 2022 to 2024 loss evidence at Exeter or Bridgecrest.

## 6. Credit Acceptance (SIG-W-20261104-008), integrated, and the card understates it

`[CONF 10-Q, accession above]` The $291.2M forecast cut has two parts: an **ordinary decrease of $106.0M (1.0%)** and a **methodology adjustment of $185.2M (1.5%)** that raised provision by $143.7M. The company says, verbatim: *"Prior to our making the adjustment in the third quarter of 2026, we had observed small but consistent quarterly underperformance of these Consumer Loans relative to forecasted cash flows and had made corresponding adjustments to our forecast each quarter."* It adds that underperformance was *"most pronounced in the case of Consumer Loans in lower scorecard bands."*

| Assignment year | Forecast collection rate 9/30/26 | Change vs 6/30/26 | Variance vs initial forecast |
|---|---:|---:|---:|
| 2022 | 59.2% | −0.1 | −8.3 |
| 2023 | 62.4% | −0.5 | −5.1 |
| 2024 | 63.6% | −1.5 | −3.6 |
| 2025 | 64.9% | −2.0 | −2.1 |
| 2026 | 65.3% | −1.8 | −1.8 |

**Read:** WALTER is right that this is not a realized $291.2M shortfall. But "methodology" here is the company's own label for catching up with a run of misses, so it is not separate from credit performance. The biggest quarterly cuts landed on 2024 to 2026 loans, the newer cohorts, which agrees in direction with the Ally newer-cohort remark (secondary call read, s037). Vintage-maturation language in THESIS that treats this as a 2022 story alone is too narrow. No fraud implication. Funding continued: unit assignments +37.7%, dollar assignments +51.0%, company-reported $1.2B available liquidity.

## 7. Context items, no consequence

- ARCC/MFIC (SIG-W-20261029-019) and BROCK's BDC data packet: info-only; a whole-company equity price is not a loan mark.
- FCA motor-finance guidance (SIG-W-20261104-041): UK redress process, no US auto-credit link. Logged.
- DEWEY `recap_pull.py` feed mode: consumed; used by WINTERKORN tonight.

## 8. Limits

No primary audio for any call. Six-month and YoY comparisons are simple means of deal percentages, not dollar-weighted, and they are descriptive, not a registered test. Exeter is deep subprime, not known to be immigrant-concentrated. Nothing here identifies why any borrower defaulted.
