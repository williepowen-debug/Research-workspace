# Property-evidence test of REGINALD's three-bank CRE report (FLG · EGBN · OZK)

**Written:** 2026-09-26 (Sat), CREED, on Will's ask.
**Under test:** `AGENTS/REGINALD/reports/2026-09-26_CRE_vulnerability_top3.md` (commit `fefe57f53`), its dossiers, and `scripts/cre_loss_scenarios.py`.
**Evidence used, in order:** the specialist desks first — `AGENTS/FLG/` (STATUS, THESIS, `workbook/KB.tsv` KB-FLG-017…057), `AGENTS/OZK/STATUS.md`, `AGENTS/HOMER/` (STATUS, workbook) — then CREED's own KB/VX and REGINALD's dossiers. **No new research was run.** The broad refinancing model and the loss ledger are deferred, as asked.
**Scope:** this tests whether *property* evidence supports each bank's proposed loss mechanism, and whether the loss comparables resemble the portfolios. **It grades evidence; it does not re-rank the banks or make a trade call** (trade construction is TERRY's).

---

## Summary

| Bank | Proposed mechanism | Does property evidence support it? | Payment · refinancing · recognized | Comparable fit | Most consequential gap |
|---|---|---|---|---|---|
| **FLG** | NYC rent-regulated MF loses value as the rent freeze meets the 2027 reset wall | **Yes on mechanism, unproven on magnitude.** The freeze is real and dated. But the market is still paying off FLG's substandard borrowers **at par**, and no post-freeze clearing price exists anywhere in the fleet | Mostly **refinancing** (payoff channel) plus a **contractual payment shock** at reset. Payments are currently *improving*. ~17–20% already recognized on the resolved nonaccrual book | **BCB: partial fit** (NJ/NY, 88% CRE/MF, but a pre-selected pool of unknown rent-regulated share). **Office "−61/−72% vs peak": no fit, and mislabelled** | **What NYC ≥50% rent-regulated collateral actually clears at after the freeze** |
| **EGBN** | DC-area multifamily deteriorating while office is done | **Only by EGBN's own loan-level data.** No DC-area multifamily market evidence (rents, supply, collections, sales) exists on any fleet surface. CREED's DC evidence is **office**, not MF | **Payment problem, genuinely** (MF coverage 1.0×; named loans at 0.63× and 0.15×), meeting a **near refinancing wall** (58% of MF matures H2-26). **Barely recognized** (MF reserve ~1%) | **EGBN's own exit haircuts: right bank, probably wrong property type.** The 39.6% FY-25 haircut came from the office-cleanup year and is not shown to be multifamily | **The realized loss severity on EGBN's *multifamily* exits, split from office** |
| **OZK** | Construction / life-science / gateway-office marks too high | **Yes, and REGINALD's stress is too light on the biggest single loan.** Life-science lease-up failure is visible at the property (RaDD ~3.3% leased). But the largest nonaccrual has a **pending sale at ~2× its loan** | **Payment masked** (RaDD interest paid from reserves), **refinancing failed** (matured loans, extensions), **recognized mostly by marks untested by sales** | **"Boston lab vacancy 26.4%" is not a loss comparable.** OZK desk severity for RaDD is **65–70%** vs REGINALD's 20% | **RaDD's real collateral position: Campus at Horton leasing and the extension/recap terms** |

**Net effect on REGINALD's conclusions:**
- **FLG:** "reserve and earnings strain, not solvency" **survives**, but the magnitude rests on assumptions no property comparable supports yet.
- **EGBN:** "capital ample, reserve not" **survives**, but the stress haircut is borrowed from office.
- **OZK:** the stress loss equals **~0.6 years of pre-provision earnings** (REGINALD's original: 0.36 years). *[Narrowed 2026-09-26 per CATO WR29: this was written as "earnings can absorb it — survives". With no absorption horizon or stressed earnings path, the model gives a relative multiple, not a yes/no.]* "Smallest threat to capital" and "0.79× reserve" **do not survive**. With the specialist desk's RaDD severity the stress loss is **$615–643M, 1.3–1.4× the reserve**, and CET1 lands at ~10.75% against the 10% floor REGINALD assumes (CREED rerun of REGINALD's own script inputs).

---

## 1. FLG — NYC rent-regulated multifamily

### The mechanism, split three ways

| Mode | Evidence | Direction |
|---|---|---|
| **Payment (cash flow)** | Criticized NYC ≥50% rent-regulated pool: **1.01× coverage, 78% LTV** (FLG deck, 6/30). **40% of nonaccrual loans are current on contract** (KB-FLG, STATUS). The loan pays; the collateral math fails. 30–89-day delinquencies **fell 63%** in H1 ($986M → $368M; MF −60%) (KB-FLG-038). MF net charge-off rate **flat at 1.17%** YoY (KB-FLG-034). Management's own freeze model: **NOI −7–8% over 3 years** for >70%-regulated buildings (KB-FLG-055) | **Today: stable to improving.** Forward: the freeze erodes NOI slowly, reaching the coverage review in **Q2-2028** (KB-FLG-052) |
| **Contractual reset (a payment shock, not a refinancing)** | **$7,038M of 2027's $8,503M wall is Option loans hitting a rate reset in place**, from a ~3.9% coupon; modified borrowers had faced ~8% (KB-FLG-046; REGINALD). On a 1.01× pool, a reset of that size breaks coverage without any outside lender being involved | **The sharpest forward risk.** It turns a refinancing problem into a payment problem on a known date |
| **Refinancing (exit channel)** | **87.5% of nonaccrual outflow is payoff/disposition; cures 1.6%** (KB-FLG-029/041). **$1.1B a quarter of CRE payoffs at par, ~40–44% of them substandard** (dossier s13). The FLG desk's thesis: *"the durability of an exit channel, not a stock of bad loans"* | **Open as of Q2.** Every improving metric depends on outside lenders and buyers taking these loans out at par. The 10-year's +80bp since late June narrows that channel |
| **Recognized** | NYC ≥50% RR nonaccrual carries **16.8% cumulative charge-offs + 4.38% reserve ≈ 20.5%** (REGINALD, derived). ⚠️ **Basis note [⚠️ CORRECTED 2026-09-27 — REGINALD packet + FLG KB-FLG-062]:** $2,088M is *already* the pre-charge-off/original balance (2,088 − 351 NCOs = 1,737 book), so **(351+76)/2,088 = 20.45% of original stands.** The earlier "~17.5%" here double-counted the charge-offs into the denominator ((351+76)/(2,088+351)) and is **withdrawn — there is no level shift.** Specific reserve on all nonaccrual: **$163M = 5.8%**; **$1,571M carries no allowance** because collateral is said to cover it (KB-FLG-031) | Recognition on the **resolved** book is real. On the unresolved book it rests on **appraisals, 70% of them dated since 1/1/24**, i.e. mostly **before** the June 2026 freeze and the September rate move |

### Strongest supporting evidence
1. **The freeze is enacted and dated** (RGB Order #58, leases starting 10/1/26–9/30/27). The court declined a stay on 9/24 and the merits are due by year-end (HOMER board_log; FLG STATUS). FLG booked **$18M of Q2 provision explicitly for it** (KB-FLG-032).
2. **FLG says it in its own 10-Q:** repricing rent-regulated loans face debt service that, "combined with inflationary pressure on operating costs and limits on the ability to increase rental rates," approaches unsustainable levels (FLG THESIS §stage 1).
3. **Stale appraisals bias the 78% LTV downward.** Values set before the freeze and the rate move are more likely too high than too low.

### Strongest contrary evidence
1. **Par payoffs of substandard loans (~$0.4–0.5B a quarter).** An outside lender or buyer paying 100 cents on a substandard rent-regulated loan is direct market evidence that the collateral covers that loan. **This is the best property-level price evidence in the whole file, and it points against large losses.**
2. **Payment performance is improving**, not deteriorating (30–89 −63%; MF charge-offs flat).
3. **$4.6B of the ≥50%-regulated book is pass-rated at ~1.5× coverage** (KB-FLG-055).
4. **The freeze may not survive.** The litigation is live; an annulment removes the 2026 leg.
5. *(Weak, disclosed as untestable by the FLG desk, KB-FLG-048)* "~93% of 2026 repricings are current or paid off."

### Do REGINALD's loss comparables resemble this portfolio?

| Pool (script) | Stress rate | Anchor cited | Fit | Verdict |
|---|---|---|---|---|
| MF + CRE nonaccrual ($2.6B) | 8% / 20% | NYC RR already ~20.5% recognized; **BCB NJ/NY problem pool ≤79% of face** | **Partial.** BCB: $205.3M face, **88% CRE/MF**, NJ/NY, **~21% pre-tax loss** (8-K 9/25). Same region and broadly the same asset class, but a small bank's **self-selected sale pool** with an **unknown rent-regulated share**; the true price is undisclosed (≤79% is a ceiling). REGINALD's own dossier limits it to classified buckets, and the script complies | **Acceptable as a classified-book cross-check, not as evidence of the rent-regulation mechanism.** Total implied severity (**~20.45% taken** + 8–20% more ≈ 28–40%; ≈24–34% on the bridge's charge-offs+rate×book basis) runs at/above BCB's realized ~21%, so the base case is not contradicted — if anything conservative vs the one comp *(the "~17%" here corrected 2026-09-27, see L34)* |
| MF substandard **accruing** ($4.2B) | 5% / 15% | 78% LTV, 1.01×, 3.9% → ~8% resets | **Property-specific and reasonable in kind**: it is the pool's own LTV and coverage, not a distressed sale transferred in. But **no sale comparable supports the magnitude** | Keep, and label as assumption-only. The par payoffs argue the base is not too low; the reset argues the stress is not too high |
| **CRE substandard accruing ($991M)** | 5% / 15% | *"office ACL 3.0%; Chicago/LA office sales −61% to −72% vs peak (CREED, secondary)"* | **No fit, and the citation is wrong.** CREED's record (REFRESH_2026-07-04:63) defines 205 W Randolph's −72% as a **sale price vs its 2017 purchase price** on a **1922, 207.5k sf** Chicago building. Glendale's −61% is also **sale vs 2017 purchase** (secondary). Neither is "vs peak", and neither is a loss rate on a loan; the CMBS loss on 205 W Randolph was **$12.2M on $16.7M**. FLG's non-MF CRE ($8.2B) is led by **industrial $3.3B (40%)**, with office only **$1.8B (22%)**; this pool's own property mix is **not disclosed**, and it is **accruing** | **Transfers distressed old-office sale declines to a performing book whose mix is undisclosed and whose parent is 78% non-office.** Replace with FLG's own office/CRE charge-off history, or state it as assumption-only. (The 15% itself is far below the comps, so the *number* isn't inflated; the *justification* is invalid) |
| MF pass ($17.9B) | 0% / 0.5% | freeze reaches review in Q2-2028 | n/a | Reasonable as stress-only |

### ⇒ The most consequential FLG evidence gap
**What NYC ≥50% rent-regulated multifamily collateral actually clears at after the freeze.** Two sources would close it:
- **(a) FLG's own discounted exits.** No prices are disclosed, and the **$133M of H1 charge-offs outside the nonaccrual schedule** (REGINALD's open question to the FLG desk) may be discounts taken at "par" payoffs.
- **(b) Market transactions and loan sales in NYC rent-stabilized buildings dated after June 2026.** No fleet record carries **any** NYC rent-stabilized sale price. The FDIC's 2023 Signature Bank rent-regulated loan-portfolio sale is the obvious historical comparable, **and it is not in any fleet record**. It would need pulling at primary.

Every loss number for FLG sits between "par payoffs are happening" and "78% LTV on pre-freeze appraisals". Only a clearing price decides between them. **Owner: the FLG desk. HOMER has no NYC rent-regulated data** (its board_log routes the freeze to FLG; its workbook has no NYC geography).

---

## 2. EGBN — DC-area multifamily

### The mechanism, split three ways

| Mode | Evidence (EGBN dossier; 10-Q/deck Q2-26) |
|---|---|
| **Payment — the genuine one** | MF weighted **coverage 1.0×, debt yield 6.0%, LTV 58%** (deck s21). **41% of the $693M MF book is criticized**, up from $175M to $284M in Q2 (+62%). Named loans: **Prince George's County apartment $56.0M substandard, LTV 88%, coverage 0.63×**; **DC apartment $20.5M, coverage 0.15×**; DC mixed-use $15.9M at **LTV 154%, still accruing** (deck s25). These are income failures, not maturity failures |
| **Refinancing** | **$405M (58% of MF) matures in H2-26** ($141M Q3, $263M Q4). At 1.0× coverage and a 6.0% debt yield against a 10-year at 5.18%, a new lender will not refinance these without new equity. The **seven criticized >$10M loans ($249M) mature Aug–Dec 2026 below 1.0×** |
| **Recognized** | **MF reserve $6.7M ≈ 1%** of MF (fell from $7.5M while criticized rose 62%). MF charge-offs ~$41M over 4 quarters, part possibly sale marks. **The recognition gap is the largest of the three banks relative to its problem pool** |

### Strongest supporting evidence
1. EGBN's own loan-level coverage (0.15×–1.0×) and the +62% criticized migration in one quarter: **payment distress at the property**, visible in the bank's own disclosure.
2. Nationally, the GSE multifamily book shows payment deterioration: **Freddie MF DQ 0.64% [Aug], fourth straight rise** (HOMER, issuer primary). That is consistent with cash-flow stress in multifamily generally.
3. Downgrades into criticized accelerated ($160M → $216M), so migration is ongoing, not a one-off.

### Strongest contrary evidence
1. **Collateral cushion: weighted MF LTV 58%.** Even on a payment default, severity should be modest if values hold. The problem loans are the higher-LTV tail (88%, 154%), not the book average.
2. **Recent exits cleared at 101–103% of post-mark carrying value** (Q1–Q2 2026). EGBN's marks have held when tested.
3. **National CMBS MF DQ is flat at 7.69%**; MF has the **smallest 2026 maturity share** of any major type (13%, MBA, secondary).
4. **CREED's DC evidence is office, not MF.** Project James and the other DC/NoVA delinquencies in the August Trepp print are office. **No fleet surface carries DC-area multifamily market data** (rents, vacancy, new supply, collections or sales). HOMER's workbook has no metro geography. So the "DC-area MF" framing rests entirely on EGBN's own 34-loan book (median $9.5M).

### Do REGINALD's loss comparables resemble this portfolio?

| Pool | Rate | Anchor | Fit | Verdict |
|---|---|---|---|---|
| Substandard held-for-investment ($460M, incl. $111M nonaccrual) | **16.5% base / 39.6% stress** | EGBN's own realized exit haircut, Q2-26 and FY-25 | **Right bank; property type not shown.** The FY-25 haircut (7 loans; transfer at **60.4% of cost**) ~~comes from the year office criticized fell $287M → $113M … so it was very likely **office-dominated**~~ *[⚠️ CORRECTED 2026-09-26 (REGINALD evidence pack `q2_EGBN.md` §A5): office was **≤$82M (≤41%)** of FY-25's $201.4M transfer value, and **no office loan went to held-for-sale after 9/30/25**. So 'office-driven' is **not established**; CREED's 'very likely' was wrong in direction. The fix stands for the narrower reason: the haircut came from a **different book mix** than today's MF-heavy substandard pool. REGINALD now uses EGBN's 13.3% H1-26 non-office haircut as base.]* The substandard book it is applied to is now **MF-heavy** (MF criticized $284M) | **Transfers a haircut from a different, mixed book (office ≤41%, per the correction) to a multifamily book at 58% average LTV.** For a 58%-LTV loan, a 39.6% loss implies the property value fell ~65%. Nothing in the fleet shows that for DC-area apartments. **Defensible only on the high-LTV tail** (88%, 154%). Split the pool by property type and LTV before applying it |
| Special mention ($274M) | 2% / 10% | downgrade pace | n/a | Reasonable |
| Uncriticized MF maturing H2 (~$200M) | 0% / 5% | coverage 1.0×, MF reserve $6.7M | **Performing loans**, so this is a refinancing-failure probability, not a sale haircut | Reasonable at 5%, as stress only |

### ⇒ The most consequential EGBN evidence gap
**The realized loss severity on EGBN's *multifamily* exits, split from office.** REGINALD's own analysis says the haircut, not the charge-off pace, swings reserve coverage from **2.0× to 0.67×**. The only haircuts on file are portfolio-wide and probably office. Two sources would close it:
- **(a)** A property-type split of EGBN's held-for-sale transfers and sales (10-Q notes; Q3 10-Q ~early Nov).
- **(b)** Whether the Aug–Dec criticized MF maturities (the PG County and DC apartments) pay off, move to held-for-sale, or go nonaccrual. **Their resolution *is* the first multifamily comparable.**

*Secondary, and not owned anywhere:* DC-area multifamily market data. HOMER is the natural owner and has no metro layer.

---

## 3. OZK — construction, life science, gateway office

### The mechanism, split three ways

| Mode | Evidence (OZK desk STATUS; REGINALD dossier) |
|---|---|
| **Payment — masked** | **RaDD ($555M, pass-rated) is ~3.3% leased** (one 50K sf tenant, 5/2025; nothing larger found through 9/24), and **its interest is paid from pre-established reserves** (7/22 call). A construction loan paying interest out of its own reserve is a **payment problem the rating cannot see yet**. Boston lab vacancy **26.4% (+610bp) on new supply** (KB-CREED-009); downtown Seattle ~37% office vacancy (KB-CREED-014) |
| **Refinancing — failed** | **10 Prospect, Boston ($169.3M) matured 2/13/26**, and Baltimore land ($40.0M) matured 12/18/25: maturity defaults. RaDD is in a **multi-year extension and recap** negotiation. Special mention rose +$219M to $616M, which management calls extension churn. **Life-science takeout finance is closed:** IQHQ handed its **vacant 330K sf S. San Francisco lab to its lender by deed-in-lieu** on 9/17 (single-source) |
| **Recognized — by marks, untested by sales** | **$257.8M of the $300.4M nonaccrual carries $0 allowance** (marked to collateral). **OREO $288M, with H1 inflows $241.6M vs sales $6.9M.** Q2 partial charge-offs $49.3M; **82% of H1 gross charge-offs are 2022 vintage** |

### Strongest supporting evidence
1. **Property-level lease-up failure** on the largest exposure (RaDD 3.3% leased) and **sponsor give-backs** in the same asset class (IQHQ).
2. **CREED's map overlays OZK's problem roster almost line for line:** Boston lab oversupply, Seattle office, Santa Monica, Atlanta and Chicago office, and 2021–22 construction vintages.
3. **Adverse selection:** criticized and classified rose while RESG commitments shrank $27.8B → $25.7B.

### Strongest contrary evidence
1. **The biggest nonaccrual has a pending sale at ~2× its loan:** 10 Prospect, **$330M sale pending vs $169.3M loan** (OZK desk). Buyer financing is uncertain. If it closes, the largest problem loan recovers in full, and the "$0 allowance" mark would be *vindicated*, not stale.
2. **Two more nonaccruals have exit paths:** The Jack (recap LOI, Q3 close) and the Wauwatosa hotel (sale contract, hard earnest money, Q3 close).
3. **Life science is bifurcated, not collapsing:** Chicago and Denver are healing (KB-CREED-009). Boston and SF are worsening on **supply**, not tenant loss.
4. **Earnings capacity:** PPNR ~$1.0B a year.

⚠️ **Cuts the other way — added 2026-09-26 from REGINALD's bridge report §1:** OZK's **own vacant Seattle office sale cleared at 58% of appraisal**, while its foreclosed Seattle, Santa Monica and Atlanta offices are carried at **89–100% of appraisal**. **That is serious adverse comparable evidence for OZK's office OREO marks**, and it weighs against contrary point 1. ⚠️ *[Narrowed 2026-09-26 per CATO: it was written as "direct evidence the OREO marks are high".]* **It is one sale.** It does not establish that each remaining foreclosed office (Seattle, Santa Monica, Atlanta) is overvalued: property characteristics and appraisal dates differ, and those need a matched asset-by-asset read. 10 Prospect is a lab asset with a buyer, and the Seattle sale is office without one; the two do not cancel.

### Do REGINALD's loss comparables resemble this portfolio?

| Pool | Rate | Anchor | Fit | Verdict |
|---|---|---|---|---|
| Nonaccrual ($300M) | 10% / 30% | "$257.8M carries $0 allowance; **Boston lab vacancy 26.4%**" | **A vacancy rate is not a loss severity.** The only price evidence on this pool, the **$330M pending sale vs a $169.3M loan**, points to *low* incremental loss on the biggest name | Replace the vacancy anchor with the pending-sale and LOI evidence; stress the **failure to close**, not a vacancy-derived haircut |
| OREO ($288M) | 10% / 25% | "marks untested by sales" | **No comparable at all** in the original script. ⚠️ Superseded 9/26: REGINALD's bridge now anchors it on OZK's own Seattle office sale at **58% of appraisal**, a same-bank, same-type comparable and the right kind. **One sale**; matched appraisal dates and property characteristics decide whether it transfers to each foreclosed office (CATO 9/26) | Acceptable as a labelled assumption. **OREO sale prices are the test** |
| Special mention ($616M) | 3% / 12% | incl. **$147M condo at 105.6% LTV** | Property-specific, reasonable in kind | Keep. The condo alone is already underwater on its appraisal |
| **RaDD ($555M, pass)** | **0% / 20%** | "extension + recap in negotiation; stress only" | **Too light against the specialist desk's own evidence.** The OZK desk holds **65–70% severity** in the still-empty branch (STATUS open item 1). Justification: the collateral is **~3.3% leased**, interest is carried by reserves, and a peer sponsor is handing back vacant lab. That is property evidence, not a borrowed sale haircut, so a high severity **on a performing loan is justified here** | **Material.** CREED rerun of REGINALD's inputs with RaDD at 65–70%: stress loss **$615–643M = 1.33–1.39× ACL**, **0.60–0.63 years of PPNR**, CET1 **~10.75%** (vs REGINALD's 11.19%; floor assumed 10%). *Stress loss = 0.60–0.63 years of PPNR (a multiple, not a yes/no absorption verdict — narrowed per CATO WR29); "smallest threat to capital" and "0.79× ACL" do not survive* |

### ⇒ The most consequential OZK evidence gap
**RaDD's real collateral position: whether Campus at Horton has signed any material lease, and whether the extension/recap brings new sponsor equity or only more time.**
- **Why it matters:** RaDD's severity (0% vs 65–70%) moves the stress loss by ~$250M, more than every other OZK pool combined.
- **Status:** the leasing check has been owed on the OZK desk since late July.
- **When it resolves:** management's promised report-back at the Q3 call (mid/late October).
- **Owner:** the OZK desk.

---

## 4. Cross-cutting findings for REGINALD's method

1. **Anchor by the pool's own property evidence, not by the nearest distressed sale.**
   - The two valid anchors in the script are **FLG's own LTV/coverage** and **EGBN's own exits**. The second is valid only once it is split by property type.
   - The two invalid ones are the **office-sale declines applied to FLG's accruing non-office-majority CRE**, and **a vacancy rate used as a severity at OZK**.
2. **The best price evidence on file points *against* large losses on two of the three:**
   - FLG's substandard par payoffs.
   - OZK's 10 Prospect pending sale at ~2× the loan.
   - Neither appears as a contrary anchor in the scenarios. It should, because both can fail: the payoff channel can close, and the sale can fall through.
3. **Performing loans get a distressed haircut only with collateral-specific evidence.**
   - RaDD **qualifies**: the collateral is empty.
   - FLG's accruing CRE and EGBN's 58%-LTV multifamily **do not yet qualify**.
4. **Recognition ratios need one basis.** *[⚠️ CORRECTED 2026-09-27 — REGINALD packet + FLG KB-FLG-062]* FLG's NYC RR recognized figure is **20.45% of original** ((351 NCOs + 76 specific)/2,088; $2,088M is already pre-charge-off, 2,088−351=1,737 book). The earlier "~17.5% on the original basis" **double-counted the charge-offs and is withdrawn — there is no level shift.** The general point stands: name the denominator.

**What does NOT change:** the ranking (FLG, EGBN, OZK), the no-solvency-breach conclusion at FLG and EGBN, and the Q3 prints as the test. No CREED band, score or trigger moves.

---

## 5. Sources
- **FLG desk:** `AGENTS/FLG/workbook/KB.tsv` (KB-FLG-017, 029, 031, 032, 033, 034, 038, 041, 046, 048, 052, 055), `STATUS.md`, `THESIS.md`. FLG 10-Q/deck Q2-26 via `dossier_FLG.md` (s13, s15, s16).
- **EGBN:** `dossier_EGBN.md` (deck s3/s16/s20/s21/s25; 10-Q S2/S5). MF geography: DC $297M / VA $201M / MD $150M.
- **OZK desk:** `AGENTS/OZK/STATUS.md` lines 21, 49, 74–80, 92, 117 (IQHQ Spur deed-in-lieu single-source; RaDD severity is the desk's model, conditional on the empty branch).
- **HOMER:** STATUS (Freddie MF 0.64% Aug, issuer primary; CMBS MF 7.69%); board_log 9/24 (freeze: no stay, merits by year-end).
- **CREED:** REFRESH_2026-07-04:63 (205 W Randolph definition), KB-CREED-009/014/033, the 2026-09-26 vulnerability map.
- **BCB:** 8-K 9/25/26, acc 0001193125-26-402710, via `dossier_CHALLENGERS.md` §BCB.
- **Rerun:** REGINALD's `cre_loss_scenarios.py` OZK inputs, RaDD varied 20% → 65% / 70%. The 20% case reproduces REGINALD's $365M exactly.
