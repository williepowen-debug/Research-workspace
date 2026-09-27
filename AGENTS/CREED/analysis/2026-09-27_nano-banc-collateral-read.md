# Nano Banc (failed Fri 2026-09-25): what the FDIC kept, what the loss implies, and the comparable CREED will watch for

**Written:** 2026-09-27 (Sun), CREED `creed-ad`, on PROME packet `AGENTS/CREED/inbox/2026-09-27_from-PROME_nano-banc-collateral-read-and-forced-sale-comp.md` (commit `17a205519`, Will-directed session `prome-09`).
**Shared fact base:** `PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md` §1. It is consumed here, not re-derived.
**Research only. No card, no trade.** No bank in Will's book perimeter is named by CREED here.
**State:** ⏳ DRAFT, in progress.

---

## §1. What is in the ≈$260M the FDIC kept

*(pending)*

## §2. The implied CRE mark

### 2a. The shared figure is REGINALD's, and CREED consumes it

*(REGINALD's figure and citation go here when its report lands: `AGENTS/REGINALD/reports/2026-09-27_nano-banc-failure-forensics.md` §3.)*

**What CREED needs that figure to state, because the DIF cost is not a haircut by itself** (sent to REGINALD as questions, not as a second number):
- The **~$114M DIF cost is an FDIC estimate** of the fund's shortfall **after** shareholders' equity is gone. It nets several things together: any **discount** the FDIC gave Sunwest on the ~$476M of assets it bought, any **deposit premium** Sunwest paid, projected losses on the **retained** pool, and receivership costs. Unless the FDIC discloses the bid terms, the DIF cost **cannot be allocated** between the purchased and retained assets.
- **Dividing the DIF cost by the ≈$260M retained pool therefore overstates the retained-pool haircut** if Sunwest bought at a discount, and **understates** the total asset loss, because the equity left at failure (≤ 3% of assets per DFPI; $39M at 6/30) absorbed losses first.
- **Vintage mix:** $736M total assets and the loan classes are **6/30/26 Call Report** figures. The $476M purchased is the FDIC's figure at **closing (9/25)**. "$260M retained" is PROME's subtraction across those two dates (plan §1, correction pass 1). The **$227M of loans assumed is Sunwest's own release** (9/25 19:45 ET), not an FDIC figure.
- **Basis:** CREED can compare a haircut **vs gross UPB** or **vs book net of allowance** ($19.9M allowance at 6/30). Those two differ, and the comps below are vs balance.

### 2b. What a 30–50% mark on SoCal small-balance CRE means against CREED's comps

**Comparable basis only:** loss as a percentage of **loan balance** (CMBS "severity on balance before disposition") or of loan cost. Appraisal-based and purchase-price-based comps are listed separately below and are **not** on the same basis.

| Comp | Date | Loss | Basis | Collateral | Source / tier |
|---|---|---:|---|---|---|
| **CMBS liquidations, all, July 2026** | Jul-26 reporting | **48.8%** ($293.9M on $602.2M, 10 loans) | balance before disposition | 93.3% office by balance | CREFC *Update on CMBS Loan Performance, July 2026* (data: Trepp), **PRIMARY-READ** by CREED (pdfminer, sha256 `8367f2978a82f970…`) |
| **CMBS liquidations, all, August 2026** | Aug-26 reporting | **72.6%** ($103.2M on $142.2M, 7 loans) | balance before disposition | 4 office loans = 47.4% of balance | CREFC *…August 2026* (data: Trepp, Bloomberg), **PRIMARY-READ** (sha256 `319fab5591ebb390…`) |
| **CMBS dispositions, 2026 YTD: office / all types** | YTD to ~Aug | **49.3% / 35.2%** | severity | office vs all property types | JPMorgan CMBS Weekly 8/7/26, **as quoted in** CREFC July. SECONDARY (JPM not read) |
| **CMBS office liquidations, 2026** | 2026 | **~63%** severity; sales **~20% below latest appraisal**; expenses **~13%** of balance | severity + appraisal gap | office | Deutsche Bank Research 8/10/26, **as quoted in** CREFC July. SECONDARY |
| 🟠 **SoCal: Bank of America Plaza, downtown LA** | sold 6/16/26 | **44.0%** ($175.9M on $400.0M) | balance before disposition | 1.43M sf CBD office, 1974, receivership sale at ~$147/sf | CREFC July (Trepp), PRIMARY-READ |
| 🟠 **SoCal: 315 South Beverly Drive, Beverly Hills** | Aug-26 reporting | **100% of balance before disposition** ($19.46M) · 92.7% of securitized $21.0M | balance | urban office | CREFC August (Trepp, Bloomberg), PRIMARY-READ |
| 🟠 **SoCal: La Terraza, Escondido (San Diego County)** | Aug-26 reporting | **31.4%** ($4.15M on $13.23M) · 27.7% of securitized $15.0M | balance | suburban office | CREFC August, PRIMARY-READ |
| Bank exit: EGBN FY-25 problem-loan transfers | FY-25 | **39.6%** (transfer at 60.4% of cost, 7 loans) | loan cost | property type not shown; office ≤ 41% | REGINALD `reports/2026-09-26_CRE_top3_dossiers/dossier_EGBN.md`, via CREED's 9/26 property test |
| Bank note sale: BCB Bancorp | Sep-26 | $43.3M pre-tax loss on $205.3M face | **vs carrying value; price as % of par undisclosed** | problem loans, NJ/NY | CREED 9/26 catch-up §⑦. **Not convertible to a severity** |
| Counter-datum: ARI book → Athene | closed 4/24/26 | **0.3%** (cleared at 99.7% of commitments) | commitments | performing national CRE lending book | `VX-CREED-5.02`, PRIMARY-READ |

**Not on the same basis, listed so they are not mixed in:** OZK Seattle vacant office sold at **58% of appraisal** (appraisal basis) · 205 W Randolph **−72%** and Glendale Plaza **−61%** (sale price vs a **2017 purchase price**) · Aon **−58%** (an appraisal mark, not a sale).

**What CREED reads from the table (it moves no letter):**
1. **A 30–50% loss on a bank's worst loans is in the normal range for 2026 distressed CRE dispositions, not an outlier.** CMBS dispositions run **35% across all property types YTD and ~49% for office** (JPM, secondary). The two monthly prints CREED read at primary are 48.8% and 72.6%.
2. **SoCal's three 2026 CMBS office comps span 31% to 100%.** Location is not the variable. Asset quality, vacancy and how long the workout ran are. **All three are office.** Nano's real-estate book is only partly commercial: $129M nonresidential CRE, $71M multifamily, $47M construction (6/30). The Call Report does not split office out of the nonresidential class, so **CREED does not know Nano's office share** and holds **no SoCal disposition comp on this basis for multifamily, construction or hospitality.**
3. **So the comparison is weaker than it looks.** A 30–50% mark would sit inside the CMBS office range but **above** the 35% all-types average. Nano's property mix is unknown beyond Call Report classes. Its losses began with a governance failure, and these are loans a bank made, not loans a CMBS conduit underwrote. **Read the Nano mark as consistent with, not confirming, the 2026 severity distribution.**
4. **The appraisal-lag finding matters more than the level.** If 2026 distressed sales clear ~20% below the latest appraisal (Deutsche Bank, secondary), then any bank still carrying problem CRE at appraisal carries a mark the market would not pay. That is REGINALD's reserve question, and it is why the FDIC's eventual clearing price (§3) is worth waiting for: it will be a **sale**, not an estimate.

## §3. The forced-sale comp: DOCKET row and WATCH_FOR terms (CREED authors, PROME registers)

**Why it is worth registering.** When the FDIC sells what it kept, it will print a clearing price for Southern-California bank-held CRE loans, and on a pool the FDIC has already marked (the DIF cost). Clearing prices on bank-held small-balance CRE are the scarcest data on CREED's board: every realized comp CREED holds is either CMBS (Trepp liquidations, §2) or a one-off property sale. No comp is a bank loan pool.

**What it will and will not be evidence of (fixed now, before the print):**
- ✅ **S6 evidence** (forced sale / recognition), a `VX-CREED-5.01` comp row, recorded **vs unpaid principal balance (UPB)** and, separately, vs book value if the FDIC discloses it. **Never vs appraisal**, and never mixed with the purchase-price comps (205 W Randolph −72% is vs a 2017 purchase price, a different object).
- ⚠️ **Most likely NOT a `CREED-T-06` member.** T-06 (`> 30%` discount to basis) counts a cluster in **PERFORMING** collateral only. The retained pool is **INFERRED** to be mostly the nonperforming book (§1), so a non-performing-loan (NPL) pool sale below 70% of UPB would be the expected outcome, not a T-06 datum. It qualifies **only** if the FDIC sells a performing pool separately and that pool clears below 70% of UPB.
- ⚠️ **n=1, fraud-origin bank.** One pool from a bank whose losses began with insider self-dealing does not generalise to SoCal CRE. Record it; do not extrapolate.

**Draft DOCKET row** (six columns per `PROME/DOCKET.tsv` L77; PROME registers, CREED authored):

| date | catalyst | owners | state | artifacts_citing | notes |
|---|---|---|---|---|---|
| `on-FDIC-publishing-the-Nano-Banc-asset-sale` *(check-by 2027-06-25)* | FDIC disposition of the ≈$260M of Nano Banc (Irvine CA, failed 2026-09-25) assets retained by the receiver: a loan sale, structured transaction or asset sale prints a clearing price for SoCal bank-held CRE | CREED (S6 comp) · REGINALD info (severity reconcile) | PENDING | `AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md` §3 | Record price as % of UPB by pool, performing vs NPL separately, by property type. S6 comp, NOT a T-06 member unless a PERFORMING pool clears < 70% of UPB. Typical FDIC disposition 3–9 months (PROME plan §2B); check-by = closing + 9 months |

⚠️ **Why a check-by date on an undated row:** DOCKET's header says it carries *dated* catalysts. An event-keyed row with no date never goes overdue, so it can rot silently. The check-by date (closing + 9 months, the plan's outer bound) makes it go overdue if the FDIC has not sold by then, which is itself information. PROME's call whether to use it.

**Draft WATCH_FOR terms (to WALTER, via PROME's registration):**
```
Nano Banc | Nano Banc receivership | FDIC as receiver for Nano Banc | CREED S6 comp (retained-asset disposition) — DOCKET row on-FDIC-publishing-the-Nano-Banc-asset-sale
FDIC loan sale | FDIC structured transaction | failed bank loan sale | CREED S6 comp — record price vs UPB, performing vs NPL separately
Sunwest Bank | CREED info (acquirer; loss-share or put-back of Nano loans would change what the FDIC kept)
MOM CA Investco | Honarkar | Laguna Beach hotel (named assets per §1) | CREED S6 + REGINALD — collateral disposition of the named Laguna Beach assets
```
*(The last line's property names are filled from §1's KNOWN rows.)*

## §4. Rates to refinancing, at the curve on file

**Inputs, cited, not re-measured.** 10-year Treasury **5.18%**, 10-year real **2.85%** at the 9/24 close (`AGENTS/HENRY/research/2026-09-25_rates-move-and-hike-alignment.md`, Item 2 table). On the split of the move, BOND's ACM column (`AGENTS/BOND/analysis/2026-09-25_rates-move-TP-columns_and_FR2004-timing-RESOLVED.md` §2, via HENRY) assigns the 9/15→9/23 window net to expected policy path, but about half of the 9/23 day (+7.0bp) to term premium. Either way, a borrower refinancing today pays the level, whatever its cause.

**⚠️ Two limits, stated first:**
1. **This is arithmetic on two debt-yield buckets CREED already holds. It is NOT the refinancing-gap model, which Will deferred on 2026-09-26.** It gives a bound, not a distribution.
2. **The CRE lending spread is an ASSUMPTION, not a measurement.** CMBS conduit spread data is blocked on a data source (STATUS obligation 5). A declared band of **175–275bp** over the 10-year is used, with each end shown.

**The arithmetic.** Debt service coverage ratio (DSCR) at refinance = debt yield (NOI ÷ loan) ÷ the new loan's annual debt-service constant, **at the same loan balance**. DSCR falls below 1.0× when the debt yield is below the constant.

| Spread over 10Y 5.18% | Coupon | Break-even debt yield, interest-only | Break-even debt yield, 30-yr amortizing | Debt yield a lender needs at 1.25× (amortizing) |
|---|---:|---:|---:|---:|
| 175bp | 6.93% | 6.93% | 7.93% | 9.91% |
| 225bp | 7.43% | 7.43% | 8.33% | 10.42% |
| 275bp | 7.93% | 7.93% | 8.75% | 10.93% |

**Read against the buckets CREED holds** (CMBS hard maturities only):

| Cohort | Debt yield < 6% | Debt yield ≤ / < 8% | Source, vintage, tier |
|---|---:|---:|---|
| **2026 full-year hard maturities ($76.6B)** | not held | **36%** (≤ 8%) | Trepp, carried in `research/REFRESH_2026-06-21.md` L17/L96 (June vintage; **whether 36% is by loan count or balance is not stated**) |
| **September 2026 cohort ($2.74B)** | **26.96%** | **50.56%** (< 8%) | TreppTalk "September 2026 CMBS Hard Maturities" (9/2), `VX-CREED-3.02` notes |
| **2027** | not held | not held | CREED holds **no 2027 debt-yield distribution** in any shape. Not claimed |

⇒ **Answer, bounded:**
- **Below 1.0× on ANY assumption in the band (interest-only or amortizing):** at least the debt-yield-<6% bucket. That is **27% of the September cohort**. No full-year figure is held.
- **Below 1.0× on an amortizing refinance at every spread in the band:** approximately the debt-yield-<8% bucket. That is **~36% of the 2026 hard-maturity wall** (June-vintage figure, count-vs-balance unstated) and **51% of the September cohort**. On interest-only terms the 7–8% slice straddles 1.0×, so this is an upper-side reading for IO.
- **Cannot refinance at the same balance at a normal 1.25× lender test:** everything below a ~9.9–10.9% debt yield. That is **more than half the September cohort by construction**, but CREED holds no <10% bucket, so the true share is **not measurable from what is on file**. These loans need cash-in paydowns, extensions, or they default at maturity. That is the maturity mechanism behind `CREED-T-02` and the August special-servicing transfers.
- **2026–2027 combined: NOT answerable.** No 2027 cohort data is held.

**Perimeter (trap #5):** these are **CMBS hard maturities**, CREED's slice. They are not REGINALD's $875B all-lender MBA wall, and they are not bank-held small-balance loans like Nano's.

**Does a Nano-style forced sale move this read? No, not the DSCR read.** DSCR at refinance is NOI and coupon arithmetic, and a failed bank's asset sale changes neither. It could move the **other** refinancing constraint, loan-to-value, **for Southern California only**: a clearing price well below appraisal would be local evidence that appraisals lag executable prices (the July CREFC/Deutsche Bank read is 20% below the latest appraisal on 2026 office liquidations, §2), which would shrink the loan a lender will size on SoCal collateral. **One NPL-heavy pool from a fraud-origin bank would be n=1 on that too.**

## §5. What this does NOT touch — written, not inferred

| CREED letter / trigger | Moved by Nano Banc? | Why |
|---|---|---|
| **S3 / `CREED-T-03`** (FDIC nonfarm-nonresidential CRE PDNA, **banks > $250B**, quarterly QBP) | **No, by construction** | A $736M bank is not in the > $250B cell the trigger reads. The Q3 QBP (~late Nov, DOCKET L514) will carry the failure in the small-bank cells and in the failed-bank count, **not** in T-03's cell |
| **S6 / `CREED-T-06`** (> 30% discount to basis, cluster in PERFORMING collateral) | **No, today.** Possibly one comp later (§3) | Nothing has been sold yet. The DIF cost is an FDIC estimate, not a sale. The likely sale is an NPL pool, which T-06 excludes |
| **S6 / `CREED-T-06b`** (open-end fund gates) | **No** | A bank failure is not a fund gate. Count stays 1 (SREIT) |
| **S1 / `CREED-T-01a`, `T-01b`** (office CMBS DQ / SS) | **No** | Bank-held loans are not in Trepp's CMBS universe |
| **S2 / `CREED-T-02`** | **No** (spent) | — |
| **S4 / `CREED-T-04`** (modifications) | **No** | No modification data in the fact base |
| **S5** (multifamily) | **No CREED vote.** HOMER-owned | Nano's $71M multifamily book is HOMER's to score, if at all |
| **S8a / `CREED-T-08a`, S8b / `CREED-T-08b`** | **No** | Nano Banc had no public equity; it is not in the mortgage-REIT cohort |
| **Convergence score (25/45, held pending Will's S8a ruling)** | **No** | — |
| **Any `PRED-CREED-*` row** | **No** | No CREED prediction references a bank failure |

**No CREED letter, score, band or trigger moves on Nano Banc.** What changes is one watch item (§3) and, if REGINALD's severity figure holds (§2), one more data point that small-bank CRE marks in SoCal are deep where the book went bad.
