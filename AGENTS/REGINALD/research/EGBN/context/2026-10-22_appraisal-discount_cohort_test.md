# Cohort test: how far below appraisal do banks mark troubled collateral? (Will-approved 2026-10-22 12:08 ET)

**Question:** Q3 prints show problem loans up at 6/6 names while reserve coverage fell at 5/5, and banks cite collateral ("well-secured"). Are those collateral marks stale or optimistic? This test builds the Q1 → Q2 2026 baseline from the 10-Q Level 3 nonrecurring fair-value disclosures, so Q3 grades on arrival. No Q3 10-Q from the cohort is on EDGAR at 12:10 ET 10/22.

**Method:**
- **Files:** 26 SEC 10-Qs (13 filers × Q1/Q2 2026; accessions in `domain/sources/2026-10-22_appraisal_discount/list.txt`) plus OZK's FDIC 10-Qs (`AGENTS/OZK/raw/Q{1,2}_2026_10Q.pdf`).
- **Extraction:** sections cut mechanically, then read by three Sonnet extraction readers (per Will 10/15). Their full tables are saved beside this report as `apprdisc_{A,B,C}.md`.
- **Self-verified at source:** SSB 20%/19%, AMTB 0–30% / "typical" 6–7%, and FLG's charge-off sentence.

## 1. Result: the instrument mostly does not exist
| Bank | Discount to appraisal disclosed? | Q1 → Q2 2026 | Best comparable fallback (DERIVED unless noted) |
|---|---|---|---|
| **SSB** | ✅ weighted average | **19% → 20%** (12/31/25 19%; integers, so within rounding) | Individually evaluated loans FV $268.3M → $244.5M. OREO discount 9% → 6% |
| **AMTB** | ⚠️ range + "typical", unweighted, text unchanged | 0–30%, typical **6–7%** both quarters | Appraisals >12 months old: 8 loans ($98.9M) → 12 loans ($74.7M) |
| FLG | ❌ "appraisal values less costs to sell" | — | **H1 MF/CRE gross charge-offs $193M "primarily driven by appraisals received"** (Q2 10-Q, verbatim; Q1 $99M) |
| EGBN | ❌ "management may discount" | — | Individually assessed $90.8M → $92.9M; FV/cost ratio not like-for-like |
| VLY | ❌ "discounting criteria" | — | Collateral-dependent net carrying ÷ amortized cost **57.4% → 55.7%** (deeper; includes taxi medallions) |
| OZK | ❌ "management discount" | — | Nonaccrual held at FV **~95% of gross** both quarters (perimeter caution) |
| WAL | ❌ costs to sell 6–10% only | — | Specific allowance on FV loans 2.4% → **4.6%** of amortized cost |
| BKU · SBCF · ZION | ❌ | — | Balances only (BKU $122.3M → $75.0M, C&I-driven) |
| MTB · CFG · HBAN | ❌ | — | Period fair-value losses ÷ Q2 FV: MTB $51M/$372M ≈ 13.7%; HBAN $51M/$143M ≈ 35.7%; CFG $24M/$123M ≈ 19.5% (each a flow over a stock, indicative) |
| CUBI | ❌ "does not generally discount appraisals" | — | OREO liquidation cost 6–7% |

**Finding 1 (structural):**
- **12 of 14 banks publish no number** for how far below appraisal they mark troubled collateral.
- One (AMTB) publishes boilerplate.
- One (SSB) publishes 19–20%.

The "well-secured" claims behind falling reserve coverage **cannot be checked from filings**; only realized outcomes test them. That fits Will's 10/20 skepticism as a fact about disclosure, not as evidence of misstatement.

## 2. What realized outcomes show: haircuts cluster around 13–22%
| Event (source) | Realized or disclosed haircut |
|---|---|
| OZK Boston 10 Prospect, Q3 failed sale → foreclosure (OZK Q3 comments p25; desk `2026-10-20_backlog-followthrough.md`) | **$37.3M charge-off on ~$169.3M = 22.0%**; OREO booked at **80% of September as-is appraisal** |
| OZK June foreclosures (OZK desk 10/12) | $34.5M losses vs $141.2M retained = **19.6%** |
| EGBN H1-26 non-office loan exits (desk loss bridge, 9/26) | **13.3%** |
| SSB disclosed collateral discount | **20%** |
| FLG H1 MF/CRE charge-offs | "driven by appraisals received" (amount $193M; base not disclosed in that sentence) |

**Finding 2:**
- When a troubled CRE loan actually resolves, the loss typically runs **~13–22% below the appraisal-based value**.
- Against that, OZK carried its nonaccrual book at ~95% of gross at 6/30, and VLY placed a $30.1M construction loan on nonaccrual with **no specific reserve**. Both are consistent with marks that resolution may later correct. **Indicative only:** the perimeters differ, and prior partial charge-offs are not netted.

## 3. Correction to my 12:06 ET implication: recognition is NOT simply deferred to 2027
- My earlier read was that extensions push losses into 2027, so Q4 looks calm.
- **That is too strong.**
  - Eagle's stated policy is that appraisals refresh "on upcoming maturity **or modification**" (deck s18).
  - FLG's 10-Q ties its H1 charge-offs directly to new appraisals.
- So **extending a loan at maturity can still trigger a re-appraisal and a reserve or charge-off.**
- **Revised read:** the Q4 maturity wall (sector-wide, not just Eagle) is likely to produce **appraisal-driven write-downs in Q4–Q1** even where loans are extended. Outside cash exits stay rare. Timing is uncertain, not simply deferred.

## 4. Applied to Eagle's Q4 wall (`reports/2026-10-22_EGBN_Q4_maturity_wall.md`)
- A **13–22% realized haircut** sits between my "holds" and "−20%" rows: about **$8–20M** on the $146.9M criticized four, ≈ $0.27–0.64 of the $38.00 TBV/share before tax and existing reserves.
- **The realistic case is the middle row, not the severe one.**

## 5. Trade read (EGBN): **no trade from this desk's evidence.** TERRY constructs; Will decides.
- **Bear/put case: not available, and not supported.**
  - EGBN options are effectively untradeable. Put open interest is ~2 contracts across all expiries; most strikes have no bid; Nov $30P quoted $0.25/$1.75 (yfinance 12:11 ET).
  - The realistic wall loss is ~$0.3–0.6/share.
  - The stock already trades at ~0.84× TBV (~$31.7 vendor quote, intraday) after doubling from $15.80 [11/17/2025].
  - No catalyst before the ~late-Jan Q4 release.
- **Long case: plausible but not this desk's edge.**
  - CET1 14.99%; criticized down $111M QoQ; TBV $38.00 ≈ 20% above the price.
  - Risks: 43% of multifamily criticized; criticized = 53.5% of Tier 1; NIM 2.60%; Q4 appraisal refreshes (§3).
  - Stock trades ~$8.4M/day (3-month average), so small-size stock positions are feasible; options are not.
  - **If Will wants a long evaluated, that is a TERRY card**, with the §3 appraisal-refresh risk as its named invalidation input.

## 6. What to do with this (no new monitor)
- **At the Q3 10-Qs (~early Nov):** re-read only the two banks that publish a number (SSB, AMTB). Add **realized haircut at resolution** (charge-off ÷ pre-write balance, OREO ÷ appraisal) for each disclosed foreclosure or sale to the **existing** `workbook/WORKOUT_OUTCOME_BRIDGE.tsv`. That ledger is the instrument that can test "well-secured".
- **FLG prints tomorrow ~06:00 ET.** It is the one bank that ties charge-offs to new appraisals in its own words. Its Q3 MF/CRE charge-offs plus any appraisal language are the first Q3 read of §3. FLG's desk owns the grade; this is context.

**Sources (primary):** cohort 10-Qs as listed; EGBN Q3 8-K acc 0001050441-26-000110 (s18); OZK Q3 bundle via OZK desk / `reports/2026-10-20_backlog-followthrough.md`; FRED and yfinance pulls per session receipts. Extraction files: `domain/sources/2026-10-22_appraisal_discount/`.
