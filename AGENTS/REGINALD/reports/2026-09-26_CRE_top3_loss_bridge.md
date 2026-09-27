# CRE top-3 loss bridge: FLG · EGBN · OZK (2026-09-26, evening)

> ⚠️ **Narrowed 2026-09-26 late evening after CATO's review** (`runs/2026-09-25_2050_wq299-session-direction.md`, b93837935; CATO reproduced the stress totals from the stated assumptions, which verifies the arithmetic, not the filings or the loss rates). Four statements were corrected in place: ① Seattle comparable evidence narrowed; ② no yes/no earnings verdicts, multiples with a time horizon instead; ③ EGBN office also shows a scenario reserve shortfall; ④ the mislabelled "retained earnings" output removed. §5 now carries CATO's recommended direction beside each metric proposal. **All five stay unapplied pending Will's own word.**

**Asked by:** Will, 2026-09-26: reconcile the shortlist with CREED, bridge each bank from exposed loans to additional loss, reserves, earnings and capital, and prioritise three uncertainties.
**Supersedes the loss scenarios in** `reports/2026-09-26_CRE_vulnerability_top3.md` (bannered). The selection there stands.
**Machinery:** `scripts/cre_loss_bridge.py`. Every pool, reserve credit, loss rate and anchor is in the script; re-run it with other rates. The old `cre_loss_scenarios.py` is superseded.
**Evidence packs** (read-only research agents, SEC/FDIC primaries, figures re-verified where noted): `reports/2026-09-26_CRE_top3_dossiers/q2_{FLG,EGBN,OZK}.md`. CREED's test of my first report: `AGENTS/CREED/research/2026-09-26_REGINALD_TOP3_PROPERTY_TEST.md`.

---

## The answer first

- **The shortlist survives CREED's property evidence.** CREED confirms the ranking; its three corrections all changed my loss anchors, and I have adopted them.
- **Each bridge is conditional on the pools it covers and the loss rates assumed.** The capital figures are what happens *if* those loans lose what the scenario says. They are **not** statements that the banks are safe.
- **What the scenarios show:**

| | Stress loss on covered pools | Reserves already held against them | New hit to earnings | ÷ one year of pre-provision revenue (trailing 4Q) | CET1 if the hit lands with no earnings offset |
|---|---:|---:|---:|---|---|
| **FLG** | $1,618M | $113–420M | **$1.2–1.5B** | **8.4–10.5×** | 13.16% → **11.3–11.7%**; **10.9–11.3% if the $250M buyback is also executed** (target 10.5%) |
| **EGBN** | $226M | $6–69M | $156–219M | **1.6–2.3×** | 14.58% → 12.6–13.1% |
| **OZK** | $656M | $19–35M | $620–636M | **0.6×** | 11.80% → 10.7–10.8%; **~10.3% if the $200M buyback is also executed** |

- **Reading the reserve ranges:** the low end credits only loan-specific reserves. The high end also credits each pool's pro-rata share of the general reserve, which banks do not disclose by grade, so that share is my assumption.
- **The single most important caveat:** read the earnings column as **multiples of one year's pre-provision revenue, not a yes/no.** Two banks exceed one year: **FLG by far (8–11×)** and **EGBN (1.6–2.3×)**. OZK's is 0.6×. At FLG's multiple, capital rather than earnings takes most of the scenario loss, and the cushion to its own 10.5% target falls to **~0.4–1.2pp**. How tight it gets depends on reserve credit and on whether the buyback is executed. That is a *conditional* margin, not a solvency finding.

---

## 1. Reconciliation with CREED

| CREED finding (9/26 map + property test) | What it means for the shortlist | Status |
|---|---|---|
| 2026 CRE distress is mostly **refinancing failure (B), not weak cash flow (A)**; **multifamily is the one type where cash-flow stress is rising** (Freddie MF DQ 0.64%, 4th rise) | FLG: rent-regulated MF is **A+B** (DSCR 1.01×, 2027 resets). EGBN: MF is **A+B** (DSCR 1.0×; $405M maturing H2-26). OZK: failures are **B→C** (Boston lab matured unpaid; foreclosures). | **Agrees** |
| **DC/NoVA office is the densest new CMBS cluster** (Project James $377.6M) | EGBN office is mostly cleaned up (criticized $287M → $77M). But ~89% of its remaining office LTVs rest on pre-6/30/25 appraisals, and its own re-appraisals ran −14% to −29%. **The market cluster argues the remaining $456M of pass office is under-appraised, not that it is failing.** | **Agrees; that is the office stress leg** |
| **Seattle, Chicago, LA, Boston lab** stress; realized comps −61%/−72% | OZK's foreclosed Seattle, Santa Monica and Atlanta office are carried at **89–100% of appraisal**; OZK's *own* vacant Seattle office sale cleared at **58% of appraisal**. **That is serious adverse comparable evidence. It does NOT establish that every remaining foreclosed office is overvalued:** property characteristics and appraisal dates differ (e.g. Atlanta carries a fresh Jun-26 appraisal; Santa Monica's is 11 months old). The stress applies it as a scenario, not a finding. | **Agrees; drives the OZK OREO stress** |
| **ARI's ~$9B book cleared at 99.7% of par**: strongest contrary fact | Performing books *can* clear at par. It bears on FLG's par payoffs (still ~40% from substandard) and caps how harsh a pass-book stress should be. | **Adopted as the reason pass books are stressed lightly or not at all** |
| **Hotels: 30% of 2026 balances mature**, the most under-watched refinancing book | EGBN holds **$373M of hotel loans**, which my first report missed. It is included in "other income-producing CRE" with a 1% stress on the pass book. | **Gap closed partly** (no hotel-specific grade split is disclosed) |
| CREED's lender table lists **AMTB** among concentrated CRE names | That label came from my matrix. AMTB's score is mostly **non-CRE** credit. | **Disagree → correction packet to CREED** |
| **Fix 1:** OZK RaDD stress 20% vs the OZK desk's **65–70%** | Adopted: the stress uses **65%**; 70% adds ~$28M. | **Accepted** |
| **Fix 2:** FLG office comps were sale-vs-2017-purchase, not vs peak, and not loss rates | FLG CRE pools are now labelled **ASSUMPTION ONLY**, with no market anchor. | **Accepted** |
| **Fix 3:** EGBN 39.6% haircut "probably office", applied to a MF-heavy pool | Adopted the split by type. ⚠️ The EGBN evidence pack found **no office loan went to held-for-sale after 9/30/25**; office was ≤41% of FY-25 transfer value. **So "office-driven" is not established either.** The non-office anchor is EGBN's **13.3%** H1-26 haircut, which is now the base. | **Accepted, with a qualification sent back to CREED** |
| FLG's "~20.5% already recognised" should be **~17.5%** on the original balance | ~~Adopted.~~ ⛔ **WITHDRAWN 9/27: the fix double-counted.** $2,088M is already pre-charge-off (2,088 − 351 = 1,737); (351+76)/2,088 = **20.45%**, confirmed by FLG at deck s16. | ~~Accepted~~ **Rejected on re-check** |

---

## 2. How double-counting is prevented (the rules the script enforces)

1. **One basis per bank:**
   - FLG = the 10-Q, which *is* the bank (holding company merged in Oct-2025).
   - EGBN = the **holding company** for capital and earnings (the listed security); loans and reserves are the same at both levels.
   - OZK = Bank OZK itself. The **loans-only reserve ($461.5M)** is used; the $156.3M unfunded-commitment reserve is not.
2. **Pools are mutually exclusive and carried net of earlier charge-offs.** A loss rate here is *additional* loss on what is still on the books, so losses already recognised cannot re-enter.
   - **FLG:** the deck's "$4.4B NYC rent-regulated criticized" is a **subset** of the 10-Q grade tables. It is carved out once (nonaccrual $1,737M + special mention/substandard $2,665M), and the rest of MF is what remains.
   - **EGBN:** substandard includes nonaccrual, so nonaccrual is carved out. Held-for-sale loans ($49.7M, at fair value with executed contracts) are excluded, as is a $35.4M loan paid off after 6/30.
   - **OZK:** the risk grades sum exactly to total loans. The $147M/$196M special-mention figures are commitments, not balances, and are not subtracted.
3. **Reserves already held are credited pool by pool:** the specific allowance, plus (high end only) a pro-rata share of the general reserve. The credit is **capped at each pool's loss**, with no release assumed. The credits tie to the disclosed segment reserves: FLG $592M = MF $439M + CRE $153M; EGBN office $39.0M and MF $6.7M exactly.
4. **Foreclosed property (OREO) carries no reserve.** Its write-downs go through operating expense, so OZK's OREO losses get **no reserve credit**.
5. **Capital:** the after-tax hit (25%, assumption) with **no earnings offset**, on unchanged risk-weighted assets. Earnings capacity is shown separately, in years.

---

## 3. Bridges

### FLG, 10-Q basis, 6/30/26 ($M)

| Pool (carrying value, net of prior charge-offs) | Balance | Reserve held | Base / stress rate | Anchor |
|---|---:|---:|---|---|
| MF nonaccrual, NYC ≥50% rent-regulated | 1,737 | 76 specific | 8% / 20% | **~20.5%** of original already recognised (charge-offs + specific reserve; corrected 9/27 from a double-counted ~17.5%); the rates take cumulative loss (charge-offs + rate × book) to ~24% / ~34% of original — those totals were already on the right basis. BCB's NJ/NY problem pool sold at ≤79% of face |
| MF nonaccrual, other | 395 | ~7 specific | 8% / 20% | same |
| CRE nonaccrual | 471 | 30 specific | 10% / 25% | **Assumption only**, no market anchor (parent CRE mix is 40% industrial, 22% office) |
| MF special mention + substandard, NYC RR | 2,665 | 134 general | 5% / 15% | 78% LTV, DSCR 1.01×; 49% reset within 18 months; 2027 coupons ~3.9% vs ~8% at reset |
| MF special mention + substandard, other | 4,274 | 41 general | 3% / 10% | Assumption |
| CRE special mention + substandard | 1,367 | 22 general | 3% / 10% | Assumption only |
| MF pass, NYC RR | 4,089 | 48 general | 0% / 1% | Rent freeze reaches FLG's coverage review in Q2-2028 |
| MF pass, other | 13,771 | 133 general | 0% / 0.5% | Stress only (ARI par evidence caps it) |
| CRE pass | 6,406 | 101 general | 0% / 0% | — |

| Bridge | Base | Stress |
|---|---:|---:|
| Additional loss | $520M | $1,618M |
| − reserves held (specific only → + general) | $113M → $309M | $113M → $420M |
| **= new hit to earnings** | **$211–407M** | **$1,198–1,505M** |
| ÷ pre-provision revenue ($143M, trailing 4Q) | 1.5–2.8 years | **8.4–10.5 years** |
| CET1 13.16% → (no earnings offset) | 12.65–12.90% | **11.29–11.67%** |
| … if the $250M buyback is also executed | 12.24–12.48% | **10.87–11.26%** |
| Margin to FLG's 10.5% target | +1.7 to +2.4pp | **+0.4 to +1.2pp** |

**Coverage:**
- **Covers:** all $35.2B of MF and CRE.
- **Does not cover:**
  - business loans ($18.6B, including $3.5B to funds and non-bank lenders, none disclosed as CRE-fund lending);
  - loans that migrate beyond the stated rates;
  - securities losses.

**Conditional conclusion:** *if* problem MF/CRE loans lose 20–25% more and weak-but-accruing ones 10–15%, the hit is 8–11× one year's pre-provision revenue and capital ends within ~0.4–1.2pp of FLG's own target, the low end if the buyback proceeds. Worse loss rates, or losses outside MF/CRE, are not covered by this statement.

### EGBN, holding-company basis, 6/30/26 ($M)

| Pool | Balance | Reserve held | Base / stress | Anchor |
|---|---:|---:|---|---|
| Office pass / SM / SS accruing / nonaccrual | 456.1 / 10.8 / 32.0 / 34.3 | 32.9 / 0.8 / 2.3 general; 3.0 specific | 2/8 · 5/20 · 15/40 · 10/35% | ~89% of LTVs on stale appraisals; EGBN re-appraisals −14% to −29%; Fairfax $22.1M at 96% LTV matures 9/25 |
| MF pass / SM / SS accruing / nonaccrual | 408.6 / 79.2 / 158.6 / 10.9 | 4.2 / 0.8 / 1.7 / 0 | 0.5/3 · 5/15 · **13.3/30** · 20/40% | Appraisals imply a **3.5% cap rate** (6.0% debt yield × 58% LTV). Base = EGBN's own non-office exit haircut; stress = −35% value on 84–88% LTV loans (e.g. Prince George's apartments, DSCR 0.63) |
| Other income-producing CRE (hotel $373M, retail, mixed-use, industrial, other): pass / SM / SS / NA | 1,328.7 / 92.1 / 54.4 / 31.7 | 18.1 / 1.25 / 0.74 general; 3.0 specific | 0/1 · 3/10 · 13.3/30 · 13.3/30% | Hotel maturity concentration (CREED) |
| Owner-occupied CRE, criticized | 64.6 | 0.7 | 8/20% | Assumption |
| Construction pass / criticized | 461.2 / 62.0 | 3.9 / 0.6 | 0/2 · 8/25% | 84% of construction matures within a year |

| Bridge | Base | Stress |
|---|---:|---:|
| Additional loss | $72M | $226M |
| − reserves held (specific → + general) | $6M → $26M | $6M → $69M |
| **= new hit to earnings** | **$46–65M** | **$156–219M** |
| ÷ pre-provision revenue ($96.2M, trailing 4Q; dividends only ~$1.2M/yr) | 0.5–0.7 years | 1.6–2.3 years |
| CET1 14.58% → (no earnings offset) | 13.98–14.16% | 12.56–13.14% |

**Where the stress loss sits:**

| Book | Stress loss | Reserve held against it |
|---|---:|---:|
| Office | $64M | $39M |
| Multifamily | $76M | $6.7M |

**Both have a scenario reserve shortfall.** Multifamily's is the larger (stress loss ~11× its reserve); office's is ~1.6×. Coverage: all income-producing CRE, construction, and criticized owner-occupied CRE. **Not covered:** owner-occupied pass ($1.6B), business loans ($1.5B, including **$153M of CRE booked as business loans**), and post-6/30 migrations.

**Conditional conclusion:** *if* the office book re-appraises 20–35% lower and weak MF loses 13–30%, the hit is ~1.6–2.3× one year's pre-provision revenue, and capital stays near 12.6–13.1% on this coverage.

### OZK, Bank OZK basis, 6/30/26 ($M)

| Pool | Balance | Reserve held | Base / stress | Anchor |
|---|---:|---:|---|---|
| **Boston 10 Prospect (life-sci), nonaccrual** | 169.3 | **0** | 30% / 50% | 91% LTV on a Nov-25 appraisal; a comparable Chicago lab's appraisal fell 32% in 13 months. **Upside case: the pending $330M sale closes → $0** (but $330M doesn't reconcile with a ~$186M appraisal, so it isn't counted as evidence) |
| Baltimore land / The Jack (Seattle office) / Wauwatosa hotel, nonaccrual | 40.0 / 25.9 / 16.7 | 0 | 0/15 · 5/40 · 0/15% | Appraisal cushion / OZK's own Seattle exit at 58% of appraisal / hard-deposit contract |
| Other nonaccrual | 48.5 | 13.7 specific | 10% / 25% | Assumption (composition not disclosed) |
| **OREO: office** (Seattle, Santa Monica, Atlanta) | 137.5 | **none (expense)** | 15% / 40% | Carried at 89–100% of appraisal vs OZK's own exits at 58–80% |
| **OREO: life-sci** (Seattle, Chicago) / **LA land** | 96.0 / 54.5 | none | 5/27.5 · 0/30% | Near office-conversion value / LOI at or above carrying |
| Tahoe substandard accruing | 29.4 | 7.3 specific | 10% / 25% | Assumption |
| Special mention | 616.2 | 8.4 general | 3% / 12% | Includes a condo at 105.6% LTV |
| **RaDD life-science, pass-rated** | 555.0 | 7.6 general | **0% / 65%** | OZK desk severity 65–70%; ~3.3% leased; interest paid from reserves |

| Bridge | Base | Stress |
|---|---:|---:|
| Additional loss | $104M | $656M, of which RaDD $361M |
| − reserves held | $8–16M | $19–35M |
| **= new hit to earnings** | **$88–96M** | **$620–636M** |
| ÷ pre-provision revenue ($1,083M, trailing 4Q) | 0.1 years | **0.6 years** |
| CET1 11.80% → (no earnings offset) | 11.64–11.65% | 10.74–10.77% |
| … if the $200M buyback is also executed | 11.19–11.21% | **~10.3%** |

**Coverage:** named problem assets, special mention, and RaDD's **funded** $555M. **Not covered:**
- RaDD's **~$360M unfunded commitment**;
- the pass RESG book (~$14.7B of construction and non-owner-occupied CRE, less named credits);
- the $430M loans-to-CRE-lenders book (first charge-offs $42.4M YTD), except where already nonaccrual.

**Conditional conclusion:** *if* RaDD fails at the OZK desk's severity and the foreclosed marks fall to where OZK's own sales have cleared, the hit is ~0.6× one year's pre-provision revenue (before provisions on the rest of the book and taxes). What happens to capital then depends on whether OZK keeps paying out ~57% of net income and executes the buyback.

---

## 4. The three priority uncertainties

### ① FLG's "$133M" charge-off difference: ~~**explained as presentation, not hidden loss (high confidence on the mechanism, the split undisclosed)**~~ ⛔ **NARROWED 2026-09-27 after the FLG desk's answer (`inbox/processed/2026-09-27_from-FLG_ANSWER-…md`, a2df32296): NOT DETERMINABLE FROM DISCLOSURE.** Still true: no loss is hidden from the ACL, so the bridge's dollars are unaffected. **No longer supported: "high confidence" and "no evidence any payoff was below par".** FLG first read it as **loss taken at exit**, then withdrew that ranking the same day on my counter-point (KB-FLG-066, `8f7152096`: gap/payoffs runs 11%–350% across FY23–Q2-26, 3.5× the exits in FY23), so **neither reading leads** (the charge-off is booked while the loan leaves the nonaccrual schedule through "payoffs, including dispositions"). Evidence: the Q2 deck's $352M NCO figure is explicitly "for loans **remaining** in the portfolio", and one refinanced-out performing loan took a ~6.0% discount (Bisnow 4/27/26, n=1). The alternative is appraisal write-downs on accruing substandard loans. The gap runs **50–73% of gross charge-offs in every period FY2023 → Q2-26** (FY24 $682M). ⚠️ **My counter-point stands and is unanswered:** the gap does not scale with payoff volume (Q1 payoffs $646M vs Q2 $190M; gap $73M vs $60M). That argues against a pure exit-discount reading, so neither reading is established. **What this changes:** the FLG dossier's "deliberate reduction" reading carries less weight, because some "par payoffs" may not have been at par.
- **9/27 add (FLG desk, KB-FLG-067, cd03d16be; press-grade, NOT issuer-confirmed):** the Q1 "single borrower relationship in bankruptcy" is very likely **Pinnacle**. About 5,100 NYC rent-stabilized units sold to Summit for **$451.3M**, closing 3/31/26, against Flagstar debt of >$564M (Multifamily Dive) / >$600M (The Real Deal). **Flagstar financed the buyer $338.5M (~75%).** So Q1's "payoff" leg contains one loss-bearing disposition, and part of the exposure **stayed on the books as a new loan** rather than leaving. The Q1 loss is not computable (prior write-downs and carrying value undisclosed). It does not explain Q2's $60M gap, where there was no such event.
- **Both schedules cover the same scope:** six-month, held-for-investment, all loan types. That rules out a scope, period or basis mismatch.
- **The gap is structural:** **$40–81M in every one of the last six quarters, $264M in FY25.**
- **At least $93M of it is MF/CRE charge-offs that never pass through the nonaccrual schedule's "charge-offs" line.** Either loans were written down as they entered nonaccrual (so they are recorded net), or a Q1 bankruptcy note sale's loss sits inside "payoffs, including dispositions". **FLG does not disclose which.** Up to ~$40M may be non-CRE.
- **Refuted:** transfers to held-for-sale (none in 2026) and material charge-offs on accruing MF (only $2M cumulative on the NYC rent-regulated special-mention/substandard pool).
- ~~**"Par payoffs":** no evidence that any were below par.~~ *(withdrawn 9/27, see heading)* The gap does not move with payoff volume.
- **What it changes:** nothing in the bridge. Losses already charged off are excluded by construction, whichever route they took. What stays open is only the precise split. The FLG desk has the question (packet `b7269b2b7`).

### ② EGBN remaining office risk and multifamily loss assumptions
- **Office:**
  - $533M left: 85.5% pass, 61% LTV, 1.3× DSCR.
  - **~89% of those LTVs rest on appraisals older than 6/30/25.** EGBN's own recent re-appraisals fell **−14% to −29%**.
  - At 61% LTV, values must fall ~34% before the average loan loses, so the loss sits in the high-LTV tail: a $60M Montgomery loan at 80%, and Fairfax at 96% maturing 9/25.
  - **Stress $64M vs the $39M office reserve: 1.6×.**
  - **Office also shows a scenario reserve shortfall:** ~$64M stress loss against $39M of allocated office reserve. The driver is appraisal vintage. **Multifamily's shortfall is larger** ($76M vs $6.7M), but it is not the only one.
- **Multifamily:**
  - The loss rates now use **EGBN's own non-office exit haircut (13.3%)** as the base, not the office-era 39.6%.
  - The MF charge-offs I had read as ~5% a year of the book (~$41M over four quarters) are **at least $15M sale-linked**, and probably mostly so. **So they are not a clean retained-book MF loss rate.**
  - The binding facts are loan-level: **four criticized MF loans ($155.8M) mature Aug–Dec 2026 with DSCRs of 0.15–0.89**, and appraisals implying a 3.5% cap rate.
  - **Stress $76M vs a $6.7M MF reserve.**
- **What would settle it:** EGBN's Q3 10-Q (~early Nov). It carries the MF criticized table and the reserve by collateral type, and it will show whether the Aug–Oct maturities paid off, extended, or went to held-for-sale, and at what haircut.

### ③ OZK's untested collateral / foreclosed-property marks
- **H1 foreclosures were $241.6M; sales were $6.9M.** The six foreclosed assets ($288M) are carried at **86–100% of appraisal**.
- OZK's only comparable disposals:
  - vacant Seattle office at **58% of appraisal**;
  - Boston office at **80%**;
  - Chicago land sold at carrying, but **−34% vs the loan**.
- OZK's pattern is to **mark to the bid once a bid exists, then sell at carrying**. So the true test is the *next bid* on each asset, not the booked mark.
- **Boston 10 Prospect ($169.3M, no reserve, 9% cushion) is the swing asset.** Its "$330M sale" does not reconcile with the ~$186M implied appraisal, so it counts as neither support nor loss.
- **What would settle it:** any Q3 OREO sale price vs carrying; the Boston sale closing or failing; the RaDD report-back on the Q3 call.

---

## 5. Metric changes — RECOMMENDED, NOT APPLIED (each needs a decision; none changes a score today)

*CATO's directions are a reviewer's recommendations relayed to me. They are **not** Will's approval, so nothing here is applied. The one change made is the M2 **wording** clarification in the matrix header, which describes the existing measure's scope and moves no score. CATO's timing (second note): **score changes and permanent new instruments can wait; accurate matrix labelling (done) and EGBN's existing sale-adjusted diagnostics (M3) are useful now.** Q3 is the next test of the analysis, not a reason to defer everything. Using M3 as the desk's measure still needs Will's own word.*

| # | Recommendation | Why | Cost / risk | CATO's recommended direction (9/26) |
|---|---|---|---|---|
| M1 | **Matrix credit leg: coverage on nonaccrual + OREO**, not nonaccrual alone | OZK's coverage falls from 154% to 78% when its $288M OREO is counted; WAL's $126M OREO is also invisible | Data is already in `workbook/CRE_RCN_COHORT.tsv`. Would move OZK's score (+1). Needs a re-score, not a patch | Make OREO visible, but **hold the automatic score change**; distinguish loan-reserve coverage from total problem assets and property losses. OREO valuation losses do **not** run through the loan-loss allowance, so a combined ratio is a screen only (FDIC reporting guidance) |
| M2 | **Add a CRE-specific credit leg** (RC-N nonaccrual by property type), or state in the matrix header that its credit leg is bank-wide | AMTB's 3 points are mostly non-CRE; the matrix is being read as a CRE ranking | Changes what the matrix *is*; a Will-level choice | **Clarify the existing measure's bank-wide scope now; defer a new scoring component** |
| M3 | **Replace EGBN's "runway" (reserve ÷ trailing charge-offs)** with (a) runway on retained-book charge-offs and (b) reserve ÷ (substandard × the bank's own realised exit haircut) | ≥67% of EGBN's trailing charge-offs were sale marks | Needs per-bank disposition splits, which not every bank discloses | Use the sale-adjusted measures **for EGBN**, with their disclosure limits explicit |
| M4 | **Adopt the loss bridge as a quarterly instrument** for the top names, re-run at each Q3/Q4 print with actual marks | It is the only surface that nets reserves and routes OREO correctly | Loss rates stay assumptions; it must never be quoted without its coverage line | **Update this analysis at Q3** before adopting a permanent recurring instrument |
| M5 | **Track "OREO carrying ÷ latest appraisal" and "realised exit ÷ appraisal"** per bank | This is the only direct test of untested marks (OZK 86–100% vs 58–80%) | Hand-collected from bank disclosures | Focus on **OZK's named assets** rather than a fleet-wide series now |

---

## Caveats that could change a decision
- **Loss rates are assumptions.** Most have a disclosed anchor. **FLG's CRE pools have no market anchor at all**, and the pass-book rates are judgment capped by the ARI par evidence.
- **The general-reserve credit is my allocation.** No bank discloses reserves by risk grade. The "specific only" end of each range is the conservative bound.
- **Earnings-coverage figures assume pre-provision revenue continues at the trailing rate.** For FLG that was $143M, and one of those quarters was negative.
- **EGBN's MF-vs-Call-Report basis** (company $693M vs Call Report $806M) does not fully reconcile. The bridge uses the company figure.
- **Nothing here is a trade view.** Trade construction is TERRY's.
