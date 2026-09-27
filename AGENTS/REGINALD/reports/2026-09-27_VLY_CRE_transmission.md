# Valley National (VLY): broader CRE stress, a bank-specific problem, or neither? (REGINALD, 2026-09-27)

**Asked by:** Will via PROME, WQ-311 (approved 19:04 ET). **Bounds:** VLY's own filings plus existing desk work. No score, threshold, tool or trade change. CREED challenges the property comparisons after part (1).
**Primary sources (all fetched from EDGAR 2026-09-27):**
- **[ER]** Q2-26 earnings release, 8-K EX-99.1, acc 0000714310-26-000036
- **[DK]** Q2-26 earnings presentation, same accession, slide images read directly (slides 4, 25, 29–32)
- **[10Q]** Q2-26 10-Q, acc 0000714310-26-000041
- **[CR]** FFIEC Call Reports, bank-level, via `workbook/CRE_RCN_COHORT.tsv` (pulled 9/26)

⚠️ **Two bases.** The deck's "CRE $27.9B" = non-owner-occupied + owner-occupied + multifamily, **excluding construction** ($2.5B). The Call Report is bank-level. Figures are labelled by source; do not mix them.

---

## (1) ACTUAL CRE COMPOSITION, as of 6/30/2026 — OBSERVED

### By property type [DK s29]
| Type | $B | Share | Wtd LTV | Wtd DSCR |
|---|---:|---:|---:|---:|
| Apartment & residential (non-co-op multifamily) | 7.1 | 25% | 64% | 1.34× |
| Retail | 4.2 | 15% | 61% | 1.67× |
| Healthcare | 4.1 | 15% | 69% | 1.69× |
| Specialty & other | 3.1 | 11% | 54% | 1.79× |
| **Office** | **3.0** | **11%** | 63% | 1.83× |
| Industrial | 2.9 | 10% | 60% | 2.17× |
| **Co-ops** | **1.8** | 6% | **12%** | 1.50× |
| Mixed use | 1.6 | 6% | 63% | 1.31× |
| **Total (ex-construction)** | **27.9** | | **59%** | **1.67×** |
| Construction (separate) | 2.5 | — | — | — [ER] |

*(The deck's pie shows "Apartment & Residential 32%", which includes co-ops; the table splits them.)*

### By geography [DK s29]
| Region | $B | Share | Wtd LTV | Wtd DSCR |
|---|---:|---:|---:|---:|
| Florida / Alabama | 7.8 | 28% | 61% | 1.81× |
| Other (national) | 5.9 | 21% | 66% | 1.65× |
| New Jersey | 5.2 | 19% | 62% | 1.63× |
| Other NYC boroughs | 4.3 | 16% | 56% | 1.45× |
| Manhattan (multifamily 6% + other 4%) | 2.6 | 10% | 41% (60% ex co-ops) | 1.51× |
| New York ex-NYC | 2.0 | 7% | 56% | 1.99× |
| **NYC total** | **6.9** | **25%** | | |

### NYC rent-regulated multifamily: how VLY defines it, and how big it is
- **VLY's own definition** [10Q, loan table note 1]: loans "collateralized by properties that are **greater than 50 percent rent regulated**".
  - **$559M at 6/30/26**, down from $583M [3/26] and $601M [12/25].
  - That is **2.0% of CRE ex-construction** and **1.1% of total loans** ($52.5B).
- **Cross-check against the deck** [DK s30]: NYC non-co-op multifamily is **$3.1B**. By share of rent-regulated units:

| Share of units rent-regulated | Share of the $3.1B | ≈ $M |
|---|---:|---:|
| 0% | 45% | 1,395 |
| 1–20% | 7% | 217 |
| **21–50%** | **30%** | **930** |
| 51–99% | 7% | 217 |
| 100% | 11% | 341 |

  - The last two rows sum to ~$558M. **That reconciles to the 10-Q's $559M.** (DERIVED; slice percentages are read off the chart.)
- ⚠️ **The ">50%" definition leaves out a ~$0.93B band of 21–50% rent-regulated buildings.** Those carry partial rent-freeze exposure. **Broadest reading: ~$1.5B (48% of NYC multifamily) has ≥21% regulated units.** That is still **~1/6 of FLG's** rent-regulated book ($8.9B >50%; `AGENTS/FLG/STATUS.md:71`).
- **NYC non-co-op multifamily metrics** [DK s30]: Manhattan $0.8B, LTV 62%, DSCR **1.24×**. NY ex-Manhattan $2.4B, LTV 66%, DSCR **1.24×**. These are the **weakest coverage ratios in VLY's multifamily book** (Florida/Alabama 1.45×, NJ 1.41×).

### Office [DK s31]
- **$3.0B, 11% of CRE ex-construction**; ~26% owner-occupied; average loan $3.5M; LTV 63%; DSCR 1.83×.
- By region: Florida/Alabama $1.1B · NJ $0.8B · NY ex-Manhattan $0.5B · **Manhattan $0.2B (LTV 74%)** · other $0.4B (LTV 73%).

### Maturities [DK s32]
- **Q2-26 maturities, $1,457M:** retained $1,082M · paid off and left $341M · **modified and other $33M**. Footnote: one office loan of $25.8M moved to nonaccrual; one multifamily loan of $6.8M modified.
- **Next 6 quarters:** 3Q26 $1,408M · 4Q26 $881M · 1Q27 $937M · 2Q27 $576M · 3Q27 $518M · 4Q27 $870M. Weighted DSCR 1.41–1.99×.
- **The wall is 2028–29** ($3.7B per year).

### What drives the SR 07-1 concentration of ~320%
- **Mine:** 319.5% (Call Report, bank-level). **VLY's own ratio:** "CRE / TRBC" **317%** at 6/30/26 [DK s4], defined per regulatory guidance, including CRE held for sale and excluding owner-occupied [10Q glossary].
- **VLY's own trend** [DK s4]: **474% [12/23] → 362% [12/24] → 333% [12/25] → 317% [6/26]**. **Down 157pp in 2.5 years**, from capital growth and non-owner-occupied runoff (NOO −$357M in Q2 alone [10Q]).
- **Components** (Call Report, 6/30): multifamily **$9.0B** (includes the $1.8B of co-ops) + non-owner-occupied **$11.1B** + construction **$2.5B**.
- ⚠️ **About 25pp of the ~320% is co-op lending at a 12% LTV** (DERIVED: $1.8B ÷ implied capital ≈ $7.1B = 317% ⇒ $22.7B / 3.17). **Co-ops are regulated-as-CRE but low-loss** (a blanket mortgage on a cooperative building). **Ex-co-ops the ratio is ~292%, below the 300% line.**
- ⇒ **The concentration is a level inherited from 2023 and falling fast. It is not a sign of new risk-taking.**

---

*Part (1) committed first (6e21a2c37) so CREED could start; parts (2)–(4) below.*

## (2) PROBLEM-LOAN DETERIORATION — what rose, when, where; genuine vs mechanical — OBSERVED

**Mechanical effects: the three candidates, checked first**

| Effect | Present? | Evidence |
|---|---|---|
| **Loan sales / transfers to held-for-sale** | **Negligible.** None in H1-26. | "There were no transfers of loans from held for investment to held for sale during the six months ended June 30, 2026." One $9.1M non-performing CRE relationship (moved to HFS in Q4-25) sold in Q1 at a $767K gain [10Q, Loan Portfolio Sales]. ⇒ **no sale-driven cleanup is flattering 2026 figures.** |
| **Charge-offs removing balances** | **Small, and they understate inflows.** | Q2 gross charge-offs **$27.6M**, "largely partial charge-offs of non-performing CRE and C&I" [ER]. Q2 CRE net charge-offs ≈ **$11.7M** (DERIVED from Call Report YTD: MF 9.4−4.3 + OO 1.5−0.2 + NOO 14.2−8.9 = 5.1+1.3+5.3). ⇒ gross new CRE nonaccrual inflow was **≈ $42M+**, not the net +$30.7M (payoffs and upgrades out of nonaccrual are not disclosed). |
| **Denominator** | **Material for RATIOS, not for DOLLARS.** | CRE ex-construction **+$649.1M in Q2 (+2.4%)**: owner-occupied +$560.6M, multifamily +$445.7M, NOO −$357.2M [10Q MD&A]. Total loans +$1.6B (12.9% annualised). ⇒ **every CRE ratio is flattered by growth.** |

**What actually moved (dollars, so denominator-free)**

| Bucket | 6/25 | 9/25 | 12/25 | 3/26 | **6/26** | Read |
|---|---:|---:|---:|---:|---:|---|
| CRE nonaccrual (ex-construction) [ER] | 193.6 | 235.8 | 236.2 | 225.4 | **256.1** | **+$30.7M (+13.6%) in Q2 — genuine** (sales nil; charge-offs would have *lowered* it) |
| ↳ non-owner-occupied [CR] | 116.9 | 151.6 | 145.4 | 149.0 | **169.8** | **+$20.8M** — the main Q2 nonaccrual mover |
| ↳ owner-occupied [CR] | 14.4 | 13.9 | 14.6 | 13.8 | **24.7** | +$10.9M (the fastest-growing book) |
| ↳ multifamily [CR] | 62.3 | 70.2 | 76.2 | 62.6 | **61.5** | flat |
| Construction nonaccrual [ER] | 24.1 | 48.2 | 9.1 | 9.1 | 9.1 | resolved in Q4-25 (FY25 commercial gross charge-offs $118.7M [10Q]) |
| **CRE 30–59 days past due** [ER] | 42.9 | 26.4 | 72.8 | 69.5 | **106.0** | **+$36.5M; "a few larger CRE loans"** [ER] |
| ↳ **multifamily 30–89** [CR] | 39.2 | 9.5 | 1.6 | 9.4 | **101.5** | ★ **+$92M — the Q2 past-due jump is MULTIFAMILY** (NOO 30–89 went 40.8 → 0, consistent with NOO migrating into nonaccrual) |
| CRE 90+ still accruing [ER] | — | — | 0.2 | — | **5.5** | = one modified CRE loan that re-defaulted [10Q] |
| **CRE modifications to borrowers in financial difficulty, in-quarter** [10Q] | Q2-25: **7.0** | | | | **Q2-26: 116.0** | ★ **$108.2M of it "other-than-insignificant PAYMENT DELAY"**, weighted **8-month deferral**; + $7.7M term extension. **16× the year-ago quarter.** |
| CRE modified in the prior 12 months, stock [10Q] | 6/25: **250.1** | | | | **139.5** | ⚠️ **Down 44% YoY.** Q2's spike follows a quiet H2-25/Q1-26; it is not a rising trend. $5.5M of it re-defaulted. |
| CRE collateral-dependent [10Q] | | | 226.0 | | **250.5** | +$24.6M in H1 |
| **CRE criticized + classified** [DK s25] | **3.7B** | 3.6B | 3.3B | 3.3B | **3.1B** | **−$0.6B YoY: genuine improvement in dollars** ("upgrades and payoffs") |
| CRE classified (sub + doubtful) [10Q] | | | 1,938 | | **1,807** | −$131M in H1 |
| CRE special mention [10Q] | | | 1,034 | | **1,082** | +$48M in H1: a mild inflow at the top of the pipeline |

**Ratio vs dollar, criticized CRE (DERIVED):** 11.10% → 10.36% of CRE (12/25 → 6/30). At a constant 12/25 denominator, 6/30 would read 10.79%. ⇒ **~0.43pp of the 0.74pp improvement is fewer criticized dollars, ~0.31pp (≈40%) is loan growth.**

**Maturity outcomes [DK s32]:** of $1,457M maturing in Q2, **$1,082M (74%) retained** by VLY, $341M paid off and left, $33M modified or other (one $25.8M office loan to nonaccrual; one $6.8M multifamily loan modified). **"Retained" is a VLY renewal, not a third-party refinancing**, so it proves VLY's willingness, not the borrower's market access.

## (3) CONSISTENCY: do reserves, recognised losses and foreclosed property tell one story? — OBSERVED + DERIVED

| Signal | Level / move | Story it tells |
|---|---|---|
| ACL on CRE [ER allocation] | **$268.4M = 0.96%** of CRE; = **105%** of CRE nonaccrual; **15%** of classified CRE | Adequate on recognised problems, thin against the classified pipeline |
| **Q2 provision composition** [ER] | Specific reserves ↑ (collateral-dependent) + economic forecast ↑ + growth ↑, **"partially offset by a decline in quantitative reserves largely within certain CRE loan categories"** | ⛔ **MISMATCH 1: VLY cut the general CRE reserve in the same quarter that CRE nonaccrual rose 13.6%, multifamily past-dues rose ~$92M, and CRE payment-delay modifications rose to $108M.** The model reads the falling criticized book; the leading indicators point the other way. |
| ACL / total nonaccrual [ER] | **163.5% [6/25] → 127.7% [6/26]** | Coverage eroding: the reserve is ~flat (~$590M) while nonaccrual rose +$108M YoY |
| Net charge-offs [ER] | **0.17%** annualised Q2 (Q1 0.14%); CRE H1 ≈ $25M on $27.9B ≈ 0.18% | Low recognised loss |
| OREO [ER] | **$4.1M**; a foreclosure pipeline barely exists | VLY resolves through **retention, modification and partial charge-off, not foreclosure** (opposite of OZK's $288M OREO) |
| ⛔ **MISMATCH 2** | **$108M of 8-month payment deferrals** vs NCO 0.17% and OREO $4M | **A payment-delay modification keeps a loan current and accruing with no charge-off**, so nonaccrual, NCO and OREO can all understate stress **by construction** while deferrals run. The test comes when the deferrals end (~Q1-27 for Q2-26 grants). |
| Contrary to both mismatches | 12-month modified stock down 44%; criticized CRE −$0.6B YoY; classified −$131M in H1 | The *pipeline* is shrinking even as a few large loans deteriorate |

⇒ **The measures do not tell one story. The stock measures (criticized, classified, concentration) say improving. The flow measures (new nonaccrual, multifamily past-due, distress modifications) say a Q2 cluster of larger loans went bad. And the reserve followed the stock measures.**

## (4) JUDGMENT — **NEITHER (not broader transmission; not yet a bank-specific problem at the loss level), with ONE bank-specific early flag worth a single print**

**Why not "broader":**
- VLY's CRE is **diversified by type and region** (Florida/Alabama 28%, national 21%, NJ 19%, NYC 25%). LTV 59%, DSCR 1.67×.
- **Rent-regulated exposure is small**: $559M >50% regulated, ~$1.5B at ≥21%.
- The Q2 moves are **a few large loans** [ER], not a broad migration: criticized CRE fell $0.6B YoY.
- **Across the cohort**, my 6/30 read is aggregate CRE improvement with deterioration at named banks (`reports/2026-09-27_cross-bank_CRE_transmission.md` §A3). VLY does not change that.

**Why not "bank-specific problem":**
- Recognised losses are low (NCO 0.17%).
- Earnings capacity is large: **PPNR $249.6M in Q2** [ER], ≈ $1.0B/yr annualised. That covers a **3.2% loss on the entire CRE book in one year** before reserves (dossier, DERIVED).
- Capital CET1 10.71% [ER]. Concentration is falling (474% → 317%).
- Management is acquiring, not defending (Providence, 8/25).

**The flag:** in Q2, **multifamily past-dues ($9.4M → $101.5M), NOO nonaccrual (+$20.8M) and CRE payment-delay modifications ($108M) all jumped in one quarter, while VLY RELEASED general CRE reserve.** That combination is the early form of a bank-specific problem. It is not yet one.

**Strongest contrary evidence, each way:**
- **Against "neither" (i.e. for stress):** the +$92M multifamily past-due and the $108M of 8-month deferrals appeared in the **same quarter** that the general CRE reserve fell. NYC multifamily carries VLY's weakest DSCR (1.24×). ACL/nonaccrual fell 164% → 128% in a year.
- **Against stress:** criticized CRE **−$0.6B YoY** in dollars (not only ratio). Concentration 474% → 317%. The modification stock is down 44% YoY. H1 had no loan sales dressing the numbers. Low LTV. ~$1B/yr PPNR.

## SCENARIO ASSUMPTIONS
- The deck's rent-regulated band values ($ per band) are **read off a pie chart** (percentages × $3.1B). The >50% sum reconciles to the 10-Q's $559M, which validates the read.
- The co-op share of the concentration (~25pp) uses **VLY's own 317% and implied capital** (DERIVED).
- The Q2 CRE NCO split (~$11.7M) is **Call Report YTD differences**, bank-level, vs consolidated elsewhere.
- **The $101.5M multifamily 30–89 and the $108.2M payment-delay modifications may be the SAME loans or different loans.** Not disclosed. I have not assumed either.

## UNKNOWNS
1. **Where the Q2 multifamily past-dues and the payment-delay loans are** (NYC? which borough? rent-regulated share?). Not disclosed.
2. **Whether they overlap**, and how the Q2-26 deferrals perform when they end (~Q1-27).
3. **Nonaccrual roll-forward** (inflows, payoffs, upgrades): VLY does not publish one. Inflow ≥ ~$42M is a floor from net change + NCOs.
4. **Office nonaccrual by region**: the $25.8M office loan to nonaccrual on maturity [DK s32] is one data point.
5. **Why "quantitative reserves" fell in certain CRE categories**: model inputs are not disclosed.
6. Q3 is not yet reported.

## NEXT OBSERVATION — and which way it moves
| Observation | When | Moves toward |
|---|---|---|
| **VLY Q3 release + deck** — does the Q2 multifamily 30–59 cohort **cure** or **roll** to 60–89 / nonaccrual? CRE nonaccrual vs $256.1M; CRE ACL direction | **Est. Thu Oct 22, 2026** (Q3-25 was Thu 10/23/25; Q2-26 Thu 7/23/26; ⚠️ not announced) | Roll + further general-reserve cut → **BANK-SPECIFIC**. Cure → **NEITHER** confirmed. |
| Q3 10-Q: CRE modifications in-quarter and the 12-month stock; any re-default of Q2 payment-delay loans | ~early Nov | Another >$100M quarter → a **pattern**, not a spike |
| Q3 Call Report: multifamily 30–89 / nonaccrual split | ~late Oct–Nov (my run 11/07) | Same |
| Deferral end on the Q2 grants | ~Q1-27 | Re-default → recognition catches up |
| Cross-bank: other mid-pack names show the same Q3 flow pattern (my cross-bank §D criterion) | Oct 20–28 | **BROADER** only if VLY is one of ≥3 |
