# FHLB Q3: what the system's own debt says before the advances figure exists

**REGINALD · 2026-10-10 Sat PM (Will-directed: "more digging into the FHLB situation"). Follows `reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md` (6/30 vintage).**
**New datum:** the FHLBanks Office of Finance (OF) monthly debt files, **updated through 9/30/26** (pulled 2026-10-10 ~14:1x ET). Every figure is labelled with its date.

## 1. Answer

| Question | Answer | Basis |
|---|---|---|
| What did FHLB funding do in Q3? | **It shrank.** Total FHLB debt (bonds + discount notes) **$1,330.8B [6/30] → $1,288.8B [9/30], −$42.1B (−3.2%)**. July −$9.7B, August −$38.6B, **September +$6.2B**. | OF `fhlbanalystdata.xlsx` "Outstandings" (preliminary); `debtstatistics.xlsx` gives the same $1,288.75B "thru 9/30/26" |
| What does that imply for Q3 advances? | **About $770B, down ~5% from $810.7B.** Three fits give $770–778B; ±2 typical misses ≈ **$728–813B**. | §3, quarterly fit of advances on debt, 2020Q2–2026Q2 |
| Could Q3 print ≤ $700B? | **Very unlikely.** It needs a miss of $70–78B; the worst miss in 25 quarters is $39B. **In all 13 quarters since 2020 where debt fell >$25B, advances also fell (0 exceptions).** | §3 |
| What does `REG-T-06` do on that print? | **It FIRES as lettered** (third straight quarter >$700B ⇒ `EARLY-CRISIS`), most likely **in a quarter when FHLB lending shrank.** | `registry/THRESHOLDS.tsv` |
| Did the late-September small-bank borrowing jump come from the FHLBs? | **Mostly not visible in FHLB debt.** Banks' borrowings (Fed H.8, all lenders) rose **+$54.5B in September** (small +$17.1B, large +$37.4B, NSA month-end); FHLB debt rose **+$6.2B**. That gap is the 3rd-largest of 41 months. **Three explanations, which the data cannot separate yet** (§4). | FRED `H8B3094NSMD` / `H8B3094NLGD`; OF |
| How big is the September jump against 2023? | **About one-ninth of SVB's first week.** Small-bank borrowings rose **+$290.0B in one week** (376.1 [3/08/23] → 666.1 [3/15/23], SA); the current move is +$32.9B over three weeks. Large banks moved **+0.9%** (SA) over the same three weeks, so it is a smaller-bank event. | FRED `H8B3094NSMA` / `H8B3094NLGA` |

⚠️ **Correction to my own 10/10 framing:** "the largest 3-week rise in 160 weeks" is true, but the 160-week window starts 9/13/2023, **after** SVB. Since 12/2022 it ranks behind the three SVB weeks (+74.9% / +61.6% / +29.9%). The STATUS row and the WALTER signal carried the 160-week phrase without that scale.

## 2. FHLB system debt, month-end ($B, OF preliminary, by settlement date)

| | Bonds | Discount notes | **Total** | Δ total |
|---|---:|---:|---:|---:|
| Dec-25 | 716.0 | 435.8 | **1,151.8** | |
| Mar-26 | 761.2 | 443.2 | **1,204.4** | +52.7 (Q1) |
| Jun-26 | 817.8 | 513.0 | **1,330.8** | +126.4 (Q2) |
| Jul-26 | 863.1 | 458.0 | **1,321.1** | −9.7 |
| Aug-26 | 887.0 | 395.6 | **1,282.6** | −38.6 |
| **Sep-26** | **905.7** | **383.1** | **1,288.8** | **+6.2** |
| Q3 | +87.9 | −130.0 | **−42.1** | |

- **The mix moved:** discount notes −$130B, bonds +$88B (floaters). The total fell.
- **September's short-term activity rose:** overnight discount notes averaged **$18.1B a day**, the 2026 high (Jan–Aug: $12.5–15.4B). Term discount-note issuance was $166.4B gross (Aug $104.9B). That fits some late-month short-term advance demand. Net debt still rose only $6.2B.
- **One independent cross-check:** money-fund holdings of agency/GSE debt (mostly FHLB; OFR `MMF-MMF_AG_TOT-M`) fell **−$40.6B in August** ($1,214.8B → $1,174.1B), matching FHLB debt's −$38.6B. July disagrees in sign (MMF +$6.8B, debt −$9.7B). September is not published yet.

## 3. Nowcast: quarterly advances on quarterly debt

Advances = sum of the 11 FHLBanks' XBRL carrying values (the Q2 report §6 table; ties to the OF combined figure). Debt = OF quarter-end total.

| Fit | n | Correlation | Slope | Typical miss (sd) | Worst miss | **Q3 advances** | ±2 sd |
|---|---:|---:|---:|---:|---:|---:|---|
| All, 2020Q2–2026Q2 | 25 | 0.98 | 0.85 | $20.8B | −$39.3B | **$769.7B** | $728–811B |
| Excluding 2020Q2, 2023Q1–Q2 | 22 | 0.96 | 0.81 | $18.5B | −$35.3B | **$775.8B** | $739–813B |
| 2023Q3–2026Q2 only | 12 | 0.93 | 0.66 | $16.9B | −$27.7B | **$777.5B** | $744–811B |

- To print ≤ $700B, Q3 needs a miss of **−$70B to −$78B**: about twice the worst seen.
- **Sign check, no model:** 13 quarters had debt fall >$25B. Advances fell in all 13.
- **Why debt can diverge from advances:** debt also funds the FHLBanks' liquidity holdings and mortgage assets. A large drawdown of liquidity holdings to fund new advances would make advances outrun debt. That is the main way this nowcast could be wrong, and the Q3 10-Qs (~early–mid Nov) show it.

## 4. September: banks borrowed, the FHLB system barely grew

Month-end (last Wednesday, NSA) change in H.8 borrowings vs FHLB debt:

| Month | Δ FHLB debt | Δ small banks | Δ large banks | Δ both |
|---|---:|---:|---:|---:|
| 2026-07 | −9.7 | −12.0 | −27.1 | −39.2 |
| 2026-08 | −38.6 | −5.9 | −49.6 | −55.5 |
| **2026-09** | **+6.2** | **+17.1** | **+37.4** | **+54.5** |

- Over 45 months the two move together (correlation 0.87; **0.72 excluding Mar–Jun 2023**).
- **September's gap (−$48.3B) ranks 3rd of 41** (excluding Mar–Jun 2023; median −$5.2B, sd $29.2B). Similar gaps: Sep-23 (−$54.9B) and Jan-24 (−$54.5B). **Unusual, not unprecedented.**
- **Three explanations; the data cannot yet separate them:**
  1. Banks borrowed mostly **outside the FHLBs**: repo, fed funds, the discount window (≤ ~$3B of it, all banks).
  2. The FHLBanks funded new advances **from their liquidity holdings** rather than new debt.
  3. **Large members paid down** while smaller ones borrowed, netting out at the system level.
- **What separates them:** the FHLBank Q3 10-Qs (advances vs liquidity holdings, by district) and the 11/07 Call Reports (per-bank FHLB advances, RC-M). The OF's Q3 combined advances figure (~late Oct) can only flag (2): advances well above the ~$770B nowcast would mean the FHLBanks funded lending from liquidity. (1) and (3) look the same at the system level, and a 6/30→9/30 figure cannot isolate September.
- ⚠️ The "small banks borrowed +11.7% in 3 weeks" figure is measured from a 9/09 trough. Month-end to month-end, small banks were **+$17.1B (+5.9%) NSA** in September.

## 5. What the press says, against the filings

American Banker (Kate Berry, 2026-09-16, "Borrowing from Federal Home Loan banks jumped 20% in 2Q") says banks turned to the FHLBs **"to replace deposits."** The article gives **no bank-level deposit data and names no borrower**. Its support is a general description of deposits moving to money funds and a Fed note that does not mention FHLB borrowing. **The filings read (Q2 report, addendum 13:2x) finds the deposit-replacement pattern at PNC only;** Citi, U.S. Bank and Wells Fargo grew deposits. Also from the article: insurers' advances rose $177B → $202B in H1; credit unions and savings institutions contracted slightly.

## 6. Dead ends, recorded so nobody re-runs them

| Route | Result | Evidence |
|---|---|---|
| FHLBank 8-K Item 2.03 (filed twice weekly per district) | **Not a proxy.** Schedule A excludes discount notes ≤1 year issued in the ordinary course; the filer states it "will not enable a reader to track changes in the total consolidated obligations outstanding." | FHLB Pittsburgh 8-K acc 0001330399-26-000131 (10/8) |
| H.8 split of borrowings (from banks vs from others, which holds FHLB) | **Discontinued 2018-01-03.** Only total borrowings by bank size remain. | FRED `BFOSCBW027SBOG` ends 2018-01-03 |
| OFR money-fund agency holdings | **Through 8/31 only;** September not yet published. Agency/GSE combined, not FHLB-only. | OFR API `MMF-MMF_AG_TOT-M` |
| News for a September advances figure | **None found.** | WebSearch 10/10 |

## 7. Caveats (each could change the read)

1. **OF debt figures are preliminary,** by settlement date, exclude master notes, and "may not match aggregate Bank balances due to timing differences" (the file's own notes).
2. **The nowcast is fitted in-sample** on 25 quarters. A quarter in which the FHLBanks draw down liquidity heavily could break it.
3. **Advances are carrying value** (the series the Office of Finance combined figure ties to); par differs by ~$2.6B at 6/30.
4. **H.8 weekly figures are sample estimates,** revisable and later benchmarked to Call Reports.
5. **No bank is named anywhere in §4.** The per-bank read is the 11/07 Call Report retrieval.

## 8. What this does to `REG-T-06` (Will's call, WQ-414, due 10/24)

- **As lettered, it very likely fires on the Q3 print (~$770B) in a quarter when FHLB lending shrank by about $40B.** That is a direct demonstration of the letter not discriminating, on top of the 12-of-26-quarters base rate.
- ⚠️ **WQ-414 says "decide before the figure exists so the choice cannot be fitted to it."** After today the figure is no longer unknown: it can be estimated within about ±$40B. **The estimate does not favour any option** (all three were written assuming a print >$700B), but it is a reason to rule before 10/24 rather than at it.
- Nothing in `registry/` is changed here. The LIQUID / BOND packets stay held until Will rules.

## Method (reproducible)

- **OF files:** `https://cdn.fhlb-of.com/files/Debt%20Statistics/fhlbanalystdata.xlsx` (2026, monthly), `…/fhlbanalystdata_archive.xlsx` (2010–2025), `…/debtstatistics.xlsx` (annual summary, "thru 9/30/26"). Sheets used: Outstandings (last column = total bonds + DN), DNIssuance, DNOutWAM. Linked from `https://www.fhlb-of.com/debt-securities/debt-statistics/`. Downloaded with `curl` into an isolated directory, read with `openpyxl` (`python3 -I`).
- **Nowcast:** OLS of Δ advances on Δ debt by quarter, 2020Q2–2026Q2 (advances from the Q2 report §6 table); Q3 Δ debt = −42.1.
- **H.8:** FRED API, `H8B3094NSMA`/`NSMD` (small, SA/NSA), `H8B3094NLGA`/`NLGD` (large), pulled 2026-10-10 (last updated 10/9). Month-end = last Wednesday of the month.
- **OFR:** `https://data.financialresearch.gov/v1/series/timeseries?mnemonic=MMF-MMF_AG_TOT-M`.
- **Next data:** H.8 Fri 10/16 (week of 10/7) · OF October debt ~early Nov · OF Q3 combined advances ~late Oct (est.) · FHLBank Q3 10-Qs ~early–mid Nov · Call Reports 11/07.
