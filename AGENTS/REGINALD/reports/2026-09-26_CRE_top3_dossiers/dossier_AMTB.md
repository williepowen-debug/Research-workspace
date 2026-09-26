# AMTB (Amerant Bancorp / Amerant Bank N.A., RSSD 83638) — CRE-Vulnerability Dossier

**Built:** 2026-09-26 (Sat), read-only. **Vintage:** 6/30/2026 unless stated. **$ in millions unless stated.**
**Primaries (the source codes used in the tables):** [ER] Q2 8-K EX-99.1, acc 0001734342-26-000071 · [DK] Q2 deck EX-99.2, same acc · [Q] Q2 10-Q, acc 0001734342-26-000079 · [K] 2025 10-K, acc 0001734342-26-000017 · [ER4] Q4-25 8-K EX-99.1, acc 0001734342-26-000008 · [ER1] Q1-26 8-K, acc 0001734342-26-000033 · [N] 8-K 9/17/26, acc 0001628280-26-062578 · [IP] 8-K 9/1/26 investor deck, acc 0001628280-26-059818. All are at `https://www.sec.gov/Archives/edgar/data/1734342/<acc-no-dashes>/`.

> **Headline:** CRE does **not** drive AMTB's matrix score. **CRE is 5.8% of nonaccruals and 9.4% of classified loans**, and there were **zero CRE charge-offs in H1-26**. The thin 51% coverage sits on **C&I + owner-occupied + residential** nonaccruals, and 78% of those carry no allowance because they are collateral-dependent at a 47–71% LTV. The one real CRE item is the **concentration level (218%)** plus **rising CRE special mention**.

---

## 1. EXPOSURE MAP

### 1a. CRE held for investment by property type, 6/30/26 [DK slide 20; Q MD&A table]
| Type | $ | % CRE | % HFI loans | of which construction/land |
|---|---:|---:|---:|---:|
| Retail | 610 | 26.8% | 9.0% | 0 |
| Multifamily (incl. MF construction) | 460 | 20.2% | 6.9% | 226 |
| Office | 462 | 20.3% | 6.8% | 9 |
| Hotels | 205 | 9.0% | 3.0% | 30 |
| Land | 221 | 9.7% | 3.3% | 221 |
| Specialty (marinas, schools, nursing) | 202 | 8.9% | 3.0% | 26 |
| Industrial | 113 | 5.0% | 1.7% | 0 |
| **Total CRE HFI** | **2,273** | 100% | **33.7%** of $6,743 HFI | **512** |
| CRE held for sale (not in the total above) | 110 | — | — | FL 30 / TX 18 / **NY 62** |

- **Trend in the class table:** CRE HFI fell from $2,685.8 (6/30/25) to **$2,273.4 (6/30/26), −15.4%** DERIVED [ER p.17]. Non-owner-occupied $1,527.0 · multifamily $234.1 · land/construction $512.3. Owner-occupied ($732.2) is outside SR 07-1.
- **Office detail (>$3M):** 22 loans, $445M, DSCR 1.6x, LTV 64% at origination. **Weakest cells:** "Other" = 2 loans, $69M (Memphis, Atlanta), **DSCR 1.1x**; Texas = 3 loans, $61M, DSCR 1.3x, LTV 70% [DK slide 22].
- **Retail >$3M:** $552M, weighted LTV 59%, mostly neighborhood and strip centers [DK slide 21].
- **FL condo:** NOT DISCLOSED as a class. No condo-association book is disclosed, and CORAL's HOA transcript mine found zero hits (`AGENTS/CORAL/FL_BANK_WATCHLIST.md:38`).

### 1b. Geography
| CRE HFI by collateral location [DK slide 20] | FL | TX | NY | Other |
|---|---:|---:|---:|---:|
| $ | 1,729 (76%) | 137 (6%) | 122 (5%) | 285 (13%) |

- **Houston: exited.** The Houston franchise was sold in Q4-2024, with $473.9 of loans sold **at par** [K, loans MD&A]. The $137 of Texas CRE still on the book is a residual.
- **National mortgage: wound down** from April 2025 [Q, MD&A].
- **New York: being exited — an INFERENCE, not a stated decision.** The evidence is that 56% of CRE held for sale is NY ($62 of $110), the NY office space is sublet [Q], and management cites "exiting… out-of-footprint" loans [DK slide 3].
- **Banking centers:** 21 in South Florida and 2 in Tampa [N EX-99.1].

### 1c. Maturity / refinancing
| CRE HFI at 12/31/25 [K maturity table] | ≤1 yr (i.e. 2026) | 1–5 yr | >5 yr |
|---|---:|---:|---:|
| Non-owner occupied | 334.2 | 1,060.2 | 197.4 |
| Multifamily | 137.9 | 176.4 | 8.2 |
| Land/construction | 305.3 | 164.3 | 64.4 |
| **Total** | **777.4 (31.8%)** | **1,400.9 (57.2%)** | 270.0 |

**NOT DISCLOSED:** a quarterly schedule, and any 2027 or 2028 split (the 1–5 year bucket spans 2027–2030).

---

## 2. CREDIT TRAJECTORY (5 quarters) [ER tables p.19–20; ER4; Q Note 5; DK slide 12]

### 2a. Nonaccrual by class ($K)
| Class | 6/25 | 9/25 | 12/25 | 3/26 | **6/26** |
|---|---:|---:|---:|---:|---:|
| **CRE (non-owner-occupied + MF + land/construction)** | 1,022 | 30,969 | 20,488¹ | 11,172 | **9,815** |
| Owner-occupied RE | 21,027 | 15,287 | 28,733 | 40,745 | 40,506 |
| Single-family residential | 7,421 | 8,838 | 26,082 | 27,346 | 31,180 |
| Commercial (C&I) | 51,157 | 67,081 | 83,761 | 85,481 | **79,020** |
| Consumer | 666 | 725 | 9,204 | 8,969 | 8,317 |
| **Total** | 81,293 | 122,900 | 168,268 | 173,713 | **168,838** |
| **CRE share** DERIVED | 1.3% | 25.2% | 12.2% | 6.4% | **5.8%** |

¹ Includes $16.2M of land/construction loans held for sale, sold in January 2026.

- **After quarter end:** "In July 2026, the Company collected $9.4 million in full satisfaction of a nonaccrual loan" [Q Note 4 fn (1) on the non-owner-occupied row]. The deck calls it an **$8.9M NY CRE loan paid off**, which takes NPLs to $162.2M [DK slide 9; IP].
  - ⇒ Pro-forma CRE nonaccrual is about **$0.4M** (the multifamily $429K). DERIVED; this assumes no new Q3 inflows.
- **Government-insured residential:** **NOT DISCLOSED.**
  - The Q2 10-Q loans and ACL notes contain no government-insured, FHA or GNMA loan line. The only "government" hits are in the securities notes.
  - The ACL footnote describes the consumer segment as "mortgage loans secured by single-family residential properties located in the U.S." [Q].
  - ⇒ The ROADMAP/MEMORY item "AMTB gov-insured line" (`MEMORY.md:62`) resolves as **not disclosed / no evidence it exists**.
  - The residential book is growing by **purchased pools**: $506.2M bought in H1-26, of which $310.3M in Q2 [Q Note 4].

### 2b. Classified (substandard + doubtful) by class
| Class | 6/25 | 9/25 | 12/25 | 3/26 | **6/26** |
|---|---:|---:|---:|---:|---:|
| **CRE held for investment** | 63.7 | 91.4 | 56.6 | 57.6 | **25.6** |
| **CRE held for sale** | — | — | 65.7 | — | — |
| Owner-occupied (HFI + HFS) | 61.6 | 35.1 | 52.0+15.2 | 72.4 | 78.0 |
| C&I | 82.2 | 105.9 | 130.1 | 102.0 | 95.7 |
| Single-family residential | 7.3 | 8.7 | 26.0 | 44.0 | 31.2 |
| Financial institutions (NDFI) | 0 | 0 | 0 | 35.2 | 34.2 |
| Consumer | 0.7 | 0.7 | 9.2 | 9.0 | 8.3 |
| **Total** | 215.4 | 241.8 | 354.8 | 320.3 | **273.1** |
| **CRE share** DERIVED | 29.6% | 37.8% | 34.5% | 18.0% | **9.4%** |

- ⚠️ **The counter-signal: CRE special mention is RISING.**
  - $70.7 (6/25) → $86.0 (3/26) → **$103.2 (6/26), +20% QoQ**.
  - Non-owner-occupied special mention went $51.4 → **$67.2**; land/construction special mention is $35.9.
  - Total special mention fell to $109.8, so **94% of special mention is now CRE** (DERIVED).
  - Special mention carries real-estate collateral at a 63% weighted LTV [DK slide 11].

### 2c. NCOs, provision, ACL
| | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 |
|---|---:|---:|---:|---:|---:|
| NCO / avg HFI (annualized) [DK slide 12] | 0.86% | 0.39% | 1.07% | 0.45% | 0.08% |
| — of which **CRE** | 0.00% | **0.07%** | **0.05%** | 0.00% | 0.00% |
| — of which C&I | 0.77% | 0.25% | 0.98% | 0.27% | 0.05% |
| Provision, total incl. unfunded commitments [ER p.6] | 6.1 | 14.6 | 3.5 | 7.8 | 4.8 |
| ACL, end of period | 86.5 | 94.9 | 79.3 | 79.2 | **85.5** |

- **H1-26 charge-offs by segment [Q Note 5]:**
  - Real estate: **$0**.
  - C&I: $10.2M. This includes a $4.3M wind-down of a commercial participation and three large commercial relationships.
  - Consumer: $4.4M (the indirect book is running off).
- **ACL by segment at 6/30/26 [Q MD&A]:** real estate **$24.4** · commercial $37.9 · consumer/other $23.2 · financial institutions $0.

### 2d. Why the ACL ledger reads "NO" (identity non-tie) — RESOLVED
AMTB **early-adopted ASU 2025-08 on 1/1/26**. Loans bought as purchased seasoned loans (PSLs) take a **day-1 ACL gross-up with no provision**: $0.46M in Q1 and **$1.90M in Q2** [Q Note 1; Note 5]. Adding that row makes both quarters tie. DERIVED:
- **Q1:** 79,276 + 6,750 + 460 − 9,113 + 1,863 = **79,236** ✓
- **Q2:** 79,236 + 5,750 + 1,900 − 5,531 + 4,144 = **85,499** ✓
- **H1:** 79,276 + 12,500 + 2,360 − 14,644 + 6,007 = 85,499 ✓

The gross-up sits in RI-B's adjustments line (RIADC233). **The non-tie is an accounting-standard artifact, not a hidden loss or reclass.** ⚠️ It also means ACL growth of +$2.4M in H1 did not come through provision, which flatters the ACL-build optics.

### 2e. Loan sales and transfers to held for sale, with pricing
| Event | $ | Loss / mark | Source |
|---|---:|---|---|
| Q4-24: Houston sale | 473.9 | **at par** | K |
| Q4-24: investor-residential loans sold | 71.1 | −$12.6M (**17.7%** DERIVED) | K |
| Q3-25: one substandard owner-occupied loan sold | 30.4 | −$0.9M (3.0%) | ER4 fn 10 |
| **Q4-25: five substandard relationships → held for sale** | UPB 93.7 | **−$13.8M valuation allowance (14.7% of UPB** DERIVED) | K; ER4 |
| Jan-26: four of those five sold | carrying 65.7 | no further loss | K |
| H1-26: $232.6 moved to held for sale (CRE $202.8) | 232.6 | net loss −$2.9M (**1.2%** of transfers DERIVED) | Q Note 4 |
| H1-26: loans sold (RE + commercial) | proceeds 155.1 | incl. above | Q |

- Held-for-sale loans at 6/30/26 are **rated Pass**; at 12/31/25 they were rated Substandard [Q fn].
- ⇒ **The 2026 sales are strategic exits** (large, out-of-footprint or NY) **priced near par**. The **credit-loss clean-up was the Q4-25 tranche, marked at about 15%, and that mark bypassed the ACL**: it was booked in noninterest expense ($14.9M total).

---

## 3. DETERIORATION vs DELIBERATE REDUCTION vs COMPLETED LOSS RECOGNITION

| Reading | Evidence for | Evidence against |
|---|---|---|
| **CRE deterioration** | CRE special mention +20% QoQ to $103.2 (94% of all special mention); CRE is 218% of capital; office "Other" DSCR 1.1x | CRE nonaccrual $9.8M, falling to about $0.4M after the July payoff at par; CRE classified $25.6, down 72% from 9/25; **zero CRE charge-offs in H1-26**; CRE NCOs never above 0.07% annualized |
| **Deliberate reduction** | CRE HFI −15.4% YoY; $232.6 to held for sale in H1, **Pass-rated, ~1% loss**; Houston exit; NY held for sale; mgmt "exiting… out-of-footprint and criticized loans" | Part of the shrink is the downgrade path (Q4-25 substandard tranche) |
| **Completed loss recognition** | Q4-25 $13.8M mark on $93.7M, then sold at no further loss; 2025 charge-offs $63.0M (ACL ledger L6), mostly C&I; NCOs down to 0.08% | C&I nonaccrual still **$79.0M**; owner-occupied nonaccrual has doubled YoY to $40.5M; recognition in the non-CRE book is NOT complete |

**Verdict:**
- **CRE book:** deliberate reduction plus completed recognition — **HIGH confidence** on nonaccrual, charge-offs and pricing.
- **Forward CRE risk:** MEDIUM, because of the rising special mention.
- **Non-CRE book (C&I + owner-occupied):** unresolved problem assets.

### 3a. The 51% coverage explained [Q Note 4 and Note 5; DK slide 9]
- **ACL / nonaccrual = 85.5 / 168.8 = 50.6%** DERIVED.
- **Nonaccrual with NO related allowance = $131.3M (77.8%).** By class:
  - C&I $61.7
  - owner-occupied $36.9
  - residential $15.5
  - CRE-NOO $8.9 (the loan paid off at par in July)
  - consumer $8.3
- **Collateral-dependent loans total $166.3M, with specific reserves of only $2.2M.** Weighted LTVs:
  - CRE-NOO 71.4%
  - owner-occupied 62.1%
  - residential 61.5%
  - C&I 52.6%
  - NDFI 47.5%
- **Cash-flow-evaluated loans:** $85.2M (all C&I plus $2.1M owner-occupied), specific reserve $3.6M.
- ⇒ **Coverage is thin because the reserve is almost entirely a POOLED reserve. The problem loans are marked to collateral at ≤71% LTV, and the company booked prior charge-downs** ($63.0M in 2025). **A government guarantee plays no role** (none is disclosed).
- **By segment (DERIVED; segment boundaries ≠ loan classes):**
  - Real-estate ACL $24.4 vs CRE nonaccrual $9.8 → **~249% covered**.
  - Commercial ACL $37.9 vs C&I + owner-occupied nonaccrual $119.5 → **~32%**.
  - ⇒ The **"reserve shortfall" of $83.3M** (168.8 − 85.5, DERIVED) is **~100% non-CRE**.
- ⚠️ **Collateral values are appraisal-based and point-in-time** [Q Note 12]. A lower owner-occupied or C&I recovery is the live risk, not CRE.

---

## 4. LOSS INPUTS

| Item | Value | Source |
|---|---|---|
| PPNR Q2-26 | $31.9M | ER |
| PPNR trailing 4 quarters | **$101.6M** DERIVED (31.86 + 30.74 + 5.40 + 33.61) | ER p.6. Q4-25 was depressed by the $14.9M held-for-sale loss and restructuring charges |
| Net income Q2 / trailing 4Q | $21.0M / **$56.4M** DERIVED | ER p.6 |
| CET1, holdco | **$922.0M, 11.94%** | Q regulatory capital table |
| CET1, bank | $995.9M, 12.91%, RWA $7,712M | `workbook/AOCI_COHORT_2026Q2.tsv:11` |
| TCE / TCE ratio | $892.8M / 8.69% (includes −$23.7M AOCI) | ER Exh. 2; DK slide 6 |
| ACL | $85.5M (1.27% of HFI) | ER |
| Special mention LTV / classified RE collateral | 63% / $152.0M at 60% | DK slides 10–11 |
| Observed severities | CRE charge-offs ≈0; Q4-25 substandard held-for-sale mark 14.7%; 2026 exits ~1% | §2e |

- ⚠️ **Holdco and bank CET1 differ by about $74M and about 1pp.** The matrix's 12.91% is the BANK figure.
- **Illustrative CRE stress (DERIVED, hypothetical, not a forecast):** a 25% loss on the whole $462M office book = $116M. That is about 1.1× trailing PPNR and about 12% of holdco CET1.

---

## 5. INDIRECT EXPOSURE VIA CREDIT FUNDS / NDFI

| Measure | Value | Source |
|---|---|---|
| "Loans to financial institutions" (the Call Report NDFI total) | **$85.5M**, down from $156.9 at 6/25 | ER; `workbook/NDFI_COHORT.tsv:12` |
| Call Report split | All in M10a, **mortgage *credit intermediaries*** (not "warehouse"); private-credit NDFI = $0; unfunded $34.9M; nonaccrual $0 | NDFI_COHORT L12 |
| Company "financial sector" (a broader perimeter) | **$289M (4.3%)**: corporate finance 2.2% (≈$148M), **CRE note-on-note 1.1% (≈$74M)**, mortgage warehouse 0.8% (≈$54M), other 0.2% | DK slide 19; $ DERIVED = % × $6,743M |
| **Substandard NDFI loan** | **$34.2M**, collateral-dependent, **CRE collateral, LTV 47.5%**, accruing, no specific reserve | Q Note 5 collateral table |
| Syndicated / shared national credits | $535.4M syndicated, incl. $159.1M shared national credits, +$110.6M bought in H1; no highly leveraged transactions | Q |

- ⚠️ **Correction for the matrix:** REGINALD's context line "NDFI $85.5M all mortgage-warehouse" is **imprecise**. M10a covers mortgage intermediaries, including CRE debt lenders, and the company's own warehouse figure is ≈$54M. The **$34.2M substandard NDFI loan on CRE collateral is very likely the CRE note-on-note line**. That is an INFERENCE: the class and collateral match, and no loan is named.
- **Direct vs indirect:** direct CRE is $2,273 HFI + $110 HFS. **Indirect CRE via NDFI is ≈$74M** (DERIVED), of which **$34.2M is substandard**. That makes indirect CRE substandard (34.2) **larger than direct CRE substandard (25.6)**.
- Lending to funds or REITs beyond the above: **NOT DISCLOSED.**

---

## 6. UNKNOWNS / NEXT REVEALING DISCLOSURE / FALSIFIERS

**Q3 print date: NOT ANNOUNCED** as of the 2026-09-26 search.
- Q1 and Q2 both printed on a Thu after the close, with the call on Fri (4/23, 7/23).
- Q3-25 printed Tue 10/28/2025.
- The Q2 date was announced 6/26 (`reports/2026-07-18_smalltier_FL_CRE-DQ_Q2_watchcard.md:15`).
- ⇒ Expect an announcement about four weeks ahead. **Re-check IR by Fri 10/9, as the FL frame requires.** The frame's "~Thu 10/22" estimate has not been verified; the 2025 analog is Tue 10/28.

**Events since Q2:**
- 9/17: **$50M 7.00% senior notes due 2031** issued at the holdco, net $48.4M [N]. Stated uses include buybacks and "repaying outstanding indebtedness". This is capital-positive at the holdco, not a raise under stress.
- 9/8: CEO employment agreement (item 5.02).
- No loan-sale 8-K.

| Unknown | Where it resolves |
|---|---|
| Whether CRE special mention ($103.2) migrates to classified | Q3 8-K CQ table (~late Oct) |
| C&I / owner-occupied recoveries vs collateral marks | Q3 10-Q (~early Nov) |
| NDFI $34.2M substandard: identity and whether it moves to nonaccrual | Q3 10-Q collateral table |
| CRE maturities for 2027–2028 | NOT DISCLOSED (10-K gives 1–5 yr only) |
| Government-insured residential | NOT DISCLOSED |

⚠️ **FL-frame mechanics — a flag only; the frozen text is not edited:**
- AMTB's primary cell (CRE-NOO nonaccrual, baseline $9,386K) will very likely read **near $0 in Q3** because of the July payoff at par.
- ⇒ That makes HOLDS close to mechanical: only new inflows above $11.2M would count as transmission.
- The informative AMTB cell is **classified $**, where the CRE special mention build could show.

**What would WEAKEN the concern (falsifiable, Q3):**
1. CRE special mention ≤ $103.2M, **and** CRE classified ≤ $25.6M.
2. C&I nonaccrual < $79.0M, with no specific-reserve jump (specific reserves currently $5.8M DERIVED).
3. The NDFI $34.2M either upgrades or pays off.

**What would STRENGTHEN it:**
- CRE classified above $57.6M (the Q1 level).
- Any CRE charge-off.
- A held-for-sale mark above 5% on a CRE transfer.

---

## 7. VERDICT ON LIST MEMBERSHIP

**AMTB's score of 5 is 2 points of CRE concentration and 3 points of credit quality, and the 3 credit-quality points are non-CRE.**
- CRE is **$9.8M of $168.8M nonaccrual (5.8%)**, pro-forma about $0.4M after July.
- CRE is **$25.6M of $273.1M classified (9.4%)**.
- There were **$0 of CRE charge-offs in H1-26**.
- The real-estate reserve covers CRE nonaccrual about 2.5×.
- The 51% coverage and the $83.3M shortfall come from C&I ($79.0M nonaccrual), owner-occupied ($40.5M) and residential ($31.2M). Those loans are collateral-dependent at 52–71% LTV and carry almost no specific reserve.

On CRE alone, AMTB is a **concentration name (218%, 76% Florida) with a de-risking trajectory** (CRE −15% YoY, sold near par). Its **one live CRE flag is special mention rising +20% to $103.2M**, plus **≈$74M of indirect CRE** through note-on-note NDFI lending ($34.2M substandard).

⇒ **AMTB belongs on a CRE-vulnerability list only as a WATCH name on concentration and special mention. Its elevated matrix rank is a C&I / owner-occupied credit story**, and should be labelled that way.

---

## BOTTOM LINE FOR REGINALD
1. AMTB's score of 5 is **mostly non-CRE**: CRE is 5.8% of nonaccruals, 9.4% of classified loans, and H1-26 CRE charge-offs were $0. The 51% coverage gap is C&I + owner-occupied + residential.
2. The ACL "NO" tie is **ASU 2025-08's day-1 reserve on purchased seasoned loans** (+$0.46M in Q1, +$1.90M in Q2). With it, both quarters tie to the dollar.
3. CRE is being **exited near par** ($232.6M to held for sale in H1, Pass-rated, ~1% loss). The 15% credit mark was taken in Q4-25, outside the ACL.
4. **Live CRE risks:** special mention up 20% to $103.2M, and a $34.2M substandard NDFI loan on CRE collateral (likely note-on-note). The NDFI "all warehouse" label should be corrected.
5. **FL frame:** the Q3 CRE-NOO cell will likely read about $0 (the $9.4M loan paid off in July), so read classified and special mention instead. The Q3 date is not announced; verify it by 10/9.

## SOURCES
**SEC filings (CIK 1734342):**
- 0001734342-26-000071 (Q2 8-K: `amerant2q2026earningsreleaa.htm`, `meidmasterearningsdeck06.htm`)
- 0001734342-26-000079 (Q2 10-Q `amtb-20260630.htm`)
- 0001734342-26-000017 (2025 10-K)
- 0001734342-26-000008 (Q4-25 8-K)
- 0001734342-26-000033 (Q1-26 8-K)
- 0001734342-25-000063 (Q3-25 8-K)
- 0001628280-26-062578 (9/17 senior notes 8-K)
- 0001628280-26-059818 (9/1 investor deck)
- 0001734342-26-000081 (9/8 5.02)

**Repo:**
- `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md:48,61,131`
- `AGENTS/REGINALD/reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md:18,41-47,91-93`
- `…/2026-07-25_EGBN_Q2_grade_plus_FL_smalltier_watchcard_fill.md:168-204`
- `…/2026-07-18_smalltier_FL_CRE-DQ_Q2_watchcard.md:51-65`
- `workbook/ACL_ROLLFORWARD_COHORT.tsv:6,9,12`
- `workbook/RUNWAY_COHORT.tsv:14-15`
- `workbook/NDFI_COHORT.tsv:12`
- `workbook/MI3_COHORT.tsv:115`
- `workbook/AOCI_COHORT_2026Q2.tsv:11`
- `MEMORY.md:62`
- `AGENTS/CORAL/FL_BANK_WATCHLIST.md:27,38,48`
- `AGENTS/CORAL/CLUSTER_FL_BANK_LEG.md:71,94`

**Web:** [Amerant IR calendar](https://investor.amerantbank.com/news-events/ir-calendar) · [Q2 announcement (Nasdaq)](https://www.nasdaq.com/press-release/amerant-bancorp-inc-announce-second-quarter-2026-financial-results-and-host)
