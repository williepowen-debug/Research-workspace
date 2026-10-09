# OZK: testing the OREO and collateral-dependent marks (as of 6/30/2026)

**Registrant = Bank OZK** (cert 110 / RSSD 107244); Call Report = company. REGINALD read-only, 2026-09-26.

**Source keys**
- **10Q** = Q2'26 10-Q, `AGENTS/OZK/raw/Q2_2026_10Q.pdf`. PDF pages.
- **MC2** = Q2'26 Management Comments inside `raw/Q2_2026_8K_bundle.pdf`. Printed page numbers are given.
- **MC1 / MC4 / MC3** = `raw/Q1_2026_mgmt_comments.pdf`, `raw/Q4_2025_mgmt_comments.pdf` and `raw/Q3_2025_mgmt_comments.pdf`.
- **CR** = FFIEC Call Report SDF, RSSD 107244. pulled 2026-09-26 (scratchpad `ozk_sdf_*.txt`); RI items YTD.
- **SEVEN** = `AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md`. **ATR** = `AGENTS/OZK/research/threads/ATRIUM_LIFESCI_ASSET_MAP.md`. **MAP** = `AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md`.

**Tags:** D = DISCLOSED · DV = DERIVED (arithmetic shown) · ND = NOT DISCLOSED · S = secondary or press source

---

## TASK 1 — Per-asset mark table

### 1a. OREO (six RESG assets: $288.0M DV; 10Q p.22 gives $288.1M real estate / $292.7M total)

| Asset | Original loan / commitment | Peak outstanding | Charge-offs taken (before and at foreclosure) | Carrying 6/30/26 | Carrying ÷ peak o/s · ÷ commitment | Appraisal (as-is) | Type / metro / vintage / size | Sale price, LOI or contract | Implied gain/(loss) vs carrying |
|---|---|---|---|---|---|---|---|---|---|
| **Seattle office (Chapter I, U-District)** | commit $106.9M (D, MC1 p.23) | $76.4M at 3/31 (D, MC1 p.23); ~$78.4M incl. implied Q2 advance (DV: 56.1 − (76.4 − 22.3) = +2.0) | $22.3M, Q2'26 (D, MC2 p.24) | **$56.1M** (D) | 71.6% · 52.5% (DV) | 95% of Jan'26 → **$59.1M** (DV 56.1/0.95); Q1 as-stabilized value $128.8M (DV 106.9/0.83) | Office, Seattle, ~2022 loan / ~2024 delivery, 240K SF, vacant (SEVEN §6); **$234/SF** (DV) | None; the buyer withdrew in Q2 (D) | ND |
| **Seattle life-sci (Chapter II)** | commit $89.3M (D, MC1 p.23; deed of trust 6/30/22, ATR row) | $50.4M at 3/31 (D); ~$52.2M (DV, +1.8 implied advance) | $3.7M, Q2'26 (D) | **$48.5M** (D) | 92.9% · 54.3% (DV) | 95% of Dec'25 → **$51.1M** (DV). Atrium as-market $115M, office-conversion $58M (ATR) | Lab, Seattle, 2022 vintage, 149K SF, vacant; **$326/SF** (DV) | None (D) | ND |
| **LA land (8150 Sunset)** | $63.5M construction loan, 2021 (S, SEVEN §9) | ND | ND. OZK took title 3/31/23 (S). $2.5M of forfeited earnest money was applied to carrying in Q3'25 (D, MC3 p.26). A further $12.0M of extension fees and forfeited earnest money was collected in 2024–25 (D, MC2 p.24) | **$54.5M** (D; $54,447K in CR RCON5508) | 85.7% of the $63.5M loan (DV) | 86% of Mar'26 → **$63.3M** (DV) | Entitled land, West Hollywood, 2.5 acres; **$21.8M/acre** (DV) | **LOI** being converted to a contract: "net proceeds equal to or slightly more than our carrying value" (D, MC2 p.24). Price ND | **≈ $0 to small gain** (D, management's claim) |
| **Chicago life-sci (1229 W Concord)** | commit $125.1M, 9/14/21 (ATR) | $65.1M (DV: 59.0 + 5.1 c/o + 1.0 reserves, MC3 p.25) | $5.1M in Q3'25 + $9.0M in Q4'25 = **$14.1M** (D, MC3/MC4). Plus a **$2.5M OREO write-down** in Q2'26 (D, MC2 p.24) | **$47.5M** (D) | 73.0% · 38.0% (DV) | 95% of Jun'26 → **$50.0M** (DV). Prior: May'25 ≈ $73.7M (DV 59.0/0.80) ⇒ **appraisal −32% in 13 months**. Atrium as-market $105.2M, office-conversion $45M | Lab, Lincoln Yards, 2021 loan / 2023 delivery, 320K SF, 100% vacant; **$148/SF** (DV) | Short sale failed; deed-in-lieu Mar'26 (D) | ND |
| **Santa Monica office (1650 Euclid)** | ND. ~$55–60M is an estimate (SEVEN §11) | $55.8M (DV: 50.1 + 5.7) | $5.7M in Q4'25 + $5.0M at transfer in Q1'26 = **$10.7M** (D). A further −$0.3M in Q2 (DV 45.1 → 44.8; cause ND) | **$44.8M** (D) | 80.3% (DV) · ND | 89% of **Aug'25** (11 months old at 6/30) → **$50.3M** (DV) | Creative office, 65K SF, 15% leased; **$689/SF** (DV) | Broker just engaged (D) | ND |
| **Atlanta office (1050 Brickworks, Sterling Bay)** | **$85.5M** OZK loan (S: Connect CRE, week of 7/16/26, via `OZK/research/threads/2026-09-24_CATCHUP_SWEEP.md:137`) | $45.1M (DV: 36.6 + 8.5) | **$8.5M**, Q2'26 (D) | **$36.6M** (D) | 81.2% · 42.8% (DV) | **100% of Jun'26** → $36.6M (D) | Office, Atlanta, vacant; SF ND | Sponsor marketing produced no satisfactory offer (D) | ND |

### 1b. Large collateral-dependent nonaccruals (four RESG loans, $251.9M, D 10Q p.14)

| Credit | Original loan | Peak o/s | Charge-offs | Carrying | Carrying ÷ original / peak | Appraisal | Type / vintage | Sale / LOI | Implied gain/(loss) |
|---|---|---|---|---|---|---|---|---|---|
| **Boston life-sci, 10 Prospect St, Somerville** | **$119.2M note** (D, mortgage Bk 76638 Pg 224, via SEVEN §5) | $169.3M, fully funded (D) | **$0** | **$169.3M**; ALL ≈ $0 (DV: the OCRE nonaccrual no-ALL bucket is $185,955K ≈ Boston + Wauwatosa $186.0M, 10Q p.19) | **142% of original note** · 100% of peak | LTV 91% of **Nov'25** → **$186.0M** (DV). **Cushion to the ALL trigger: $16.7M, 9%** before costs to sell | Lab/office, 194K SF, delivered 2024, unleased (S); **$873/SF** (DV) | **$330M pending sale**, but "diminished assessment of the likelihood of closing"; forbearance expired (D, MC2 p.23) | $0 if it closes. ⚠️ **$330M is 1.77× the appraisal ($1,701/SF). That does not reconcile with a 91% LTV. Treat the sale as non-evidence of value** |
| **Baltimore land (Peninsula)** | ~$66M (S, KB-OZK-119) | $66.1M (DV: 45.2 + 20.9) | $20.9M in Q3'25 + $4.6M in Q4'25 = **$25.5M** (D). $0.7M of interest applied to principal (D) | **$40.0M**; ALL $0 (DV: construction no-ALL bucket $43.9M) | 60.5% (DV) | 67% of **Jun'26** → $59.7–60.0M (D, MC2 Fig 26: 53.1% → 66.7%) ⇒ **appraisal −20% YoY** (DV, from $75.3M) | Land, 212 DPD, matured 12/18/25 | Multi-buyer talks; otherwise take title (D) | ND. There is a **33% equity cushion** (DV) |
| **The Jack, Seattle (Pioneer Square office; debt-on-debt "Other")** | commit $72.5M (D, MC4 p.26) | $56.2M (D) | **$27.7M**, Q1'26 (D, MC1 p.23). $2.6M paydown (D) | **$25.9M**; $0 ALL (D, 10Q p.19 "Other") | 35.7% · 46.1% (DV) | **100%** of Dec'25 → $25.9M (D). Atrium's earlier view: $40–45M (ATR) | Office, 145.5K SF, delivered 2023, 100% vacant; **$178/SF** (DV) | **Recap LOI** with new equity; OZK stays senior at the current balance; close expected Q3 (D, MC2 p.23) | $0 if the recap closes. If it fails: at least the cost to sell (~5–8%, $1.3–2.1M DV), because it is carried at 100% of the appraisal |
| **Wauwatosa hotel (Renaissance Milwaukee West)** | ND | $22.6M (D, MC4) | **$4.7M**, Q1'26 (D) | **$16.7M** (D) | 73.9% of peak (DV) | 96% of Mar'26 → $17.4M (DV) | Hotel, 196 keys, opened 2020 (S); **$85K/key** (DV) | **Sale contract; earnest money now non-refundable**; "net proceeds equal to or slightly exceeding" carrying; close expected Q3 (D) | **≥ $0** (D, management's claim) |

**Prior OREO exits at OZK are the only realized test of its marks. They are small.**
- **Chicago land (Q3'25): sold at carrying, $83.95M** (D, MC3 p.26). That is **−34% vs the ~$128M loan** (S, SEVEN §10).
- **Boston office (Q4'25), $9.36M: carried at 80% of its appraisal.**
- **Seattle 760 Aloha (Q4'25), $6.44M: carried at 58% of a Nov'24 appraisal, after a write-down to the offer.**
- The two Q4'25 sales produced a combined **+$0.3M** net gain (D, MC4 p.25).
- **Pattern: OZK marks to the bid once one exists, then sells at carrying.** Assets without a bid sit at **89–100% of appraisal**.

**H1'26 flows** (10Q p.22 unless noted)

| Item | H1'26 |
|---|---|
| Transfers into OREO | $241.6M |
| Sales | $6.9M |
| Write-downs | $2.983M (Q2 $2.5M Chicago ⇒ Q1 ≈ $0.5M, DV) |
| Net gain/(loss) on OREO sales, CR `RIAD5415` | **−$16K YTD** (Q1 and Q2 both −$16K ⇒ Q2 = $0). FY25 was +$691K |
| OREO expenses, CR `RIADY923` (RI-E 2.l) | **$8.688M YTD**. First populated at Q2'26; it is ND whether the $2.98M of write-downs sits inside it |
| Company "net gains on sales of assets" | $1.773M (10Q p.8/35). All assets, not only OREO |

**Accounting.** Write-downs after foreclosure run through **non-interest expense** (MC2 p.30: "elevated expenses related to nonperforming assets including a $2.5 million write-down"), not through the provision. Fair-value inputs are third-party appraisals, BPOs or DCF, less a management discount (10Q p.25).

---

## TASK 2 — Outside evidence vs the marks

| Asset | CREED / market evidence | How the mark compares | Base extra write-down | Stress extra write-down |
|---|---|---|---|---|
| Seattle office $56.1M | Downtown vacancy ~37%; conversions uneconomic; "clearest genuine cash-flow market" (MAP:25, :45). Vacant Seattle office trades at $100–180/SF (KB-OZK-177). OZK's own 760 Aloha was marked to an offer at 58% of appraisal (a mark to an offer, n=1, not a completed sale; closing UNCONFIRMED — corrected 2026-10-09 per OZK 10/8) | **$234/SF is 30–130% above the vacant band.** Carried at 95% of the appraisal | **15%** ($8.4M): appraisal-to-exit gap of 80%, the Boston-office analog | **40%** ($22.4M): 760 Aloha's 58%-of-appraisal outcome ≈ $180/SF |
| Santa Monica office $44.8M | Glendale Plaza sold −61% vs 2017 (MAP:44, S). Santa Monica availability 34.6% (SEVEN §11) | **$689/SF on a building 15% leased.** Appraisal 11 months old | **20%** ($9.0M) | **45%** ($20.2M) |
| Atlanta office $36.6M | No Atlanta comp in MAP. National office DQ 12.0%, SS 16.9% (MAP:25) | Already **43% of the $85.5M loan** and 100% of a **fresh** Jun'26 appraisal | **10%** ($3.7M): cost to sell plus drift | **35%** ($12.8M) |
| Seattle life-sci $48.5M | Seattle A+C (MAP:45) | **Below Atrium's office-conversion value ($58M)** | **5%** ($2.4M) | **25%** ($12.1M) |
| Chicago life-sci $47.5M | 205 W Randolph −72% realized; Aon −58% (MAP:43). But Chicago lab is "healing" (MAP:30) | Fresh Jun'26 appraisal; ≈ Atrium's office-conversion value ($45M). **$148/SF** | **5%** ($2.4M) | **30%** ($14.3M) |
| **Boston 10 Prospect $169.3M (nonaccrual)** | **Boston-Cambridge lab vacancy 26.4% (+610bp), supply-driven, 2021–22 vintages** (MAP:30). Alexandria's South Boston lab −57% vs 2018 basis (KB-OZK-177) | **$873/SF, $0 ALL, a 7-month-old appraisal and a 9% cushion.** The Concord analog (appraisal −32% in 13 months) wipes out the cushion | **30%** ($50.8M): an appraisal −32% ⇒ $126M less 7% costs ⇒ $118M | **50%** ($84.7M): ~$440/SF, the Alexandria-style comp |
| LA land $54.5M | DTLA stalled entitled land −45% to −68% from peak (KB-OZK-177). No land series in CREED (**NOT IN CREED**) | LOI at or above carrying; 86% of a Mar'26 appraisal; three years in OREO and one failed buyer | **0%** | **30%** ($16.4M; the SEVEN bear case is $30–40M) |
| Baltimore land $40.0M | None in CREED | **33% cushion** on a fresh appraisal; the appraisal fell 20% YoY | **0%** | **15%** ($6.0M) |
| The Jack $25.9M | Seattle vacant office, as above | $178/SF is at the top of the vacant band; carried at 100% of the appraisal | **5%** ($1.3M) | **40%** ($10.4M) |
| Wauwatosa hotel $16.7M | Lodging: 30% of 2026 balances mature; DQ 5.84% (inside the noise band) (MAP:28) | Hard-deposit contract at or above carrying | **0%** | **15%** ($2.5M) |

**Rates by asset class** (DV from the rows above)

| Class | Carrying | Base | Stress | Why |
|---|---|---|---|---|
| **Office OREO** | $137.5M | **15.2%** ($21.1M) | **40.2%** ($55.4M) | Marks sit at 89–100% of appraisal. OZK's own office exits cleared at 58–80% of appraisal. External realized comps are −61% to −72% vs basis |
| **Life-sci** (2 OREO + Boston) | $265.3M | **21.0%** ($55.6M) | **42.1%** ($111.1M) | The two OREO labs are already at office-conversion value. **Boston is the swing asset: $0 ALL on a 91% LTV in the worst lab market** |
| **Land** | $94.5M | **0%** | **23.7%** ($22.4M) | LOI plus a cushion; the entitlement risk is a tail |
| **Hotel** | $16.7M | **0%** | **15%** ($2.5M) | Hard contract |
| **The Jack** (office, "Other") | $25.9M | 5% ($1.3M) | 40% ($10.4M) | |

- **Named book $539.9M:**
  - Base **$78.0M (14.4%)**: OREO $25.9M, which runs through non-interest expense; nonaccrual $52.1M, charged off and then provisioned.
  - Stress **$201.7M (37.4%)**: OREO $98.1M, nonaccrual $103.6M.
- **Against earnings and capital** (DV):
  - Stress = **0.19 × TTM PPNR ($1,082.6M)**, or 0.78 of a quarter.
  - After tax at 22.2% (H1 CR tax/pretax, 94.6/425.4): **$157M ≈ 35bp of CET1 ratio** (11.80% → ~11.45%, before RWA relief). Base ≈ 13bp.
  - **This is an earnings event, not a capital event.**

---

## TASK 3 — Bridge inputs, one basis

**ACL reconciliation (6/30/26):** exact, $0 residual.

| | $K | Source |
|---|---|---|
| ALL for funded loans (CR `RCON3123`) | **461,534** | CR = 10Q p.17 |
| Reserve for unfunded commitments (CR `RCONB557`) | **156,274** | CR = 10Q p.17 |
| **Company ACL** | **617,808** | 10Q p.17 |

**Use $461.5M for the loan pools. Report the $156.3M unfunded reserve separately.** It sits against $17.86B of unfunded commitments, 0.88% (10Q p.46).

**Mutually exclusive problem pools**

| Pool | Balance | Specific / pool reserve | Source |
|---|---|---|---|
| Nonaccrual with ALL | $42.6M | **$13.7M** of ALL allocations (all the ALL on nonaccrual) | 10Q p.19, p.25 fn |
| Nonaccrual with no ALL | **$257.8M** (post charge-off) | **$0** | 10Q p.19 |
| — of which 4 RESG loans | $251.9M | $0 (DV) | 10Q p.14 |
| OREO | $292.7M company / $288.1M CR (**company − CR = C&I $3.2M + consumer $1.4M repossessions**, DV exact) | n/a (fair value less cost to sell) | 10Q p.22; CR 2150 |
| Substandard accrual | $72.8M = Tahoe $29.4M + C&I $40.4M (hardship modification) + other $3.0M (DV) | Tahoe **$7.3M** (MC2 Fig 23; may include its unfunded $13.8M). C&I **ND** | 10Q p.14; MC2 p.23 |
| Special mention | $616.2M = **5 RESG $529.2M** + other $87.0M (DV) | **ND.** No collective reserve by risk grade is disclosed | 10Q p.14 |
| — named SM: condo (LTV 90.4 → **105.6%**) · mixed-use (50.1 → 59.0%) | **$147M · $196M are COMMITMENTS**, not balances | ND | MC2 Fig 26 p.30 |
| RaDD (IQHQ) | $555M funded | Pass; collective only | OZK desk F5, INFERRED-HIGH |
| Collective ALL on everything else | — | ≈ **$440.5M** (DV 461.5 − 13.7 − 7.3) | — |

**Overlap check**
- Pass $31,571.5M + SM $616.2M + substandard accrual $72.8M + substandard nonaccrual $300.4M = **$32,560.97M**, which is total loans (10Q p.14 ✓). The risk grades are exclusive.
- OREO is off the loan book.
- RaDD ($555M) is larger than both the SM five ($529.2M) and the RESG nonaccrual four ($251.9M). The only RESG substandard-accrual loan is Tahoe, so RaDD must be **pass** (by elimination).
- ⚠️ **Do not subtract $147M + $196M from $529.2M.** That mixes commitments with balances. The three unnamed SM credits (office/land) are **ND**; the ~$186M figure is indicative only.

**PPNR** (CR, YTD-differenced; = pretax + provision, cross-checked each quarter; $M)

| | Q3-25 | Q4-25 | Q1-26 | Q2-26 | **TTM** |
|---|---|---|---|---|---|
| Net interest income | 413.9 | 407.0 | 385.6 | 392.1 | 1,598.6 |
| + Non-interest income | 36.1 | 33.6 | 32.5 | 37.9 | 140.1 |
| − Non-interest expense | 159.3 | 161.7 | 164.5 | 170.6 | 656.2 |
| **PPNR** | **290.6** | **279.0** | **253.6** | **259.4** | **1,082.6** |
| Net income | 184.6 | 176.0 | 163.4 | 167.4 | 691.3 |

PPNR already nets out OREO holding costs (`Y923` $8.7M in H1).

**Capital, 6/30/26** (CR RC-R)

| Measure | Value |
|---|---|
| CET1 | **$5,300.5M** |
| RWA | **$44,916.2M** |
| CET1 ratio | **11.80%** |
| Tier 1 | $5,639.5M (12.56%) |
| Total capital | $6,661.7M (14.83%) |
| Leverage | 13.96% |

**Payouts, TTM** (CR RI-A; 10Q p.6, p.57; MC2)

| Item | Amount |
|---|---|
| Common dividends | **$203.9M** (Q2 $51.7M, $0.47/share) |
| Preferred dividends | $16.2M |
| Buybacks, 7/1/25–7/1/26 | **$176.6M** (Q2 $15.5M; Q1 $60.0M DV) |
| **Total payout** | **~$396.7M = 57% of TTM net income** |

A **new $200M buyback** was authorized 6/29/26, effective 7/1/26–7/1/27 (10Q p.57).

---

## BOTTOM LINE
1. **Nothing has sold, so nothing has tested the marks.** H1 OREO sales were $6.9M at a −$16K result (`RIAD5415`). Six RESG assets ($288.0M) are carried at **86–100% of as-is appraisals**. **OZK's only disclosed vacant-Seattle-office data point is a mark to an offer at 58% of appraisal (a mark to an offer, n=1, not a completed sale; closing UNCONFIRMED — corrected 2026-10-09 per OZK 10/8).**
2. **The largest single risk is Boston 10 Prospect ($169.3M).** It has a **$0 allowance**, a 91% LTV on a Nov'25 appraisal, a 9% cushion, sits in a 26.4%-vacancy lab market, and its $330M "sale" does not reconcile. Base loss **$51M**, stress **$85M**.
3. **Office OREO ($137.5M) is marked at $234–689/SF against a $100–180/SF band for vacant Seattle office** and −61% to −72% realized comps. Base **15%**, stress **40%**. The two OREO labs are already near their office-conversion values (base **5%**).
4. **Named book $539.9M:** base **$78M**, stress **$202M**. Stress is **0.19× TTM PPNR ($1.08B)** and **~35bp of CET1** (11.80%). **Earnings drag, not capital.** OREO declines hit non-interest expense, not the provision, so the provision line understates the cost.
5. **The pools are exclusive and the ACL bridges exactly:** ALL $461.5M + unfunded reserve $156.3M = $617.8M. Specific reserves total just **$13.7M (nonaccrual) + $7.3M (Tahoe)**. **The rest of the ~$440M ALL is collective, and its split across the $616M SM / $73M substandard-accrual book is not disclosed.**
