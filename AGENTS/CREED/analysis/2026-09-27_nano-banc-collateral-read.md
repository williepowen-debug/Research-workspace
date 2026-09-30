# Nano Banc (failed Fri 2026-09-25): what the FDIC kept, what the loss implies, and the comparable CREED will watch for

**Written:** 2026-09-27 (Sun), CREED `creed-ad`, on PROME packet `AGENTS/CREED/inbox/2026-09-27_from-PROME_nano-banc-collateral-read-and-forced-sale-comp.md` (commit `17a205519`, Will-directed session `prome-09`).
**Shared fact base:** `PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md` §1. It is consumed here, not re-derived.
**Research only. No card, no trade.** No bank in Will's book perimeter is named by CREED here.
**State:** ✅ DELIVERED 2026-09-27 (12:4x ET). Inputs consumed at their artifacts: REGINALD §3 and DEWEY's possession-order read (both **uncommitted** at read time), WAL §1–§2 (`75ae6f693`, WAL-local).

---

## §0. Bottom line

1. **What the FDIC kept is undisclosed.** On the bank's 9/22 books the kept pool is **≈ $215M** (not the $260M first estimated), most likely **≈ $190M of loans**: the nonaccrual commercial real estate book and a construction book that was 88% delinquent at 6/30. **INFERRED.** The purchase-and-assumption agreement will settle it.
2. **The loans that can be named are litigated fraud-web credits**, several of them **second liens**, on Inland Empire and LA County **neighbourhood retail, medical office and a small 1964 apartment building**. They are not Laguna Beach hotels (a stale premise, now corrected) and not office towers. **None is confirmed to be in the retained pool.**
3. **The loss:** REGINALD's **desk scenario**, cited: **≈ $120M beyond the bank's own 9/22 books, ≈ 17% of assets** (equity + the FDIC's *estimated* DIF cost — not an FDIC-reported mark). On the retained pool that is ~~a **ceiling of ≤ ~56%**~~ **≈ 51–56% in a zero-adjustment scenario — not a ceiling and not a haircut** (a premium or unpaid junior creditors raise it; a purchase discount lowers it). *[CATO NB1, applied 2026-09-28: REGINALD `2117b2148` relabels 51–56% a zero-adjustment SCENARIO, not a bound — a deposit premium or unpaid junior creditors RAISE it, a purchase discount LOWERS it (e.g. +$10M premium − $5M costs ⇒ ≈58%). The ≈$120M/17% is a desk scenario (equity + the FDIC's ESTIMATED DIF cost), not an FDIC-reported mark.]* It sits inside the 2026 distressed-CRE range (CMBS dispositions 35% all types / ~49% office YTD). But the property types, lien positions and fraud origin do not match any comp, so **it is consistent with the 2026 severity distribution, not confirmation of it.**
4. **The thing to wait for** is the FDIC's sale of the pool, typically 3–9 months out: an actual clearing price on California bank-held CRE. It will be recorded **by lien position**, because a second lien's price is not a property mark. **Draft DOCKET row and WATCH_FOR terms: §3.**
5. **Refinancing at 10Y 5.18%:** at least **27%** of September's maturing CMBS loans fall below 1.0× coverage on any spread assumption. **~51%** do on an amortizing loan at the middle/high spreads (slightly fewer at 175bp); the full-year ~36% is June-vintage and its count-vs-balance basis is unknown. *(Bounded on CATO NB4, 9/27.)* 2027 is not answerable from what is held. A Nano-style sale does not move this read (§4).
6. **No CREED letter, score, band or trigger moves** (§5).

## §1. What is in the assets the FDIC kept (≈$215M on the 9/22 base; ≈$260M on 6/30)

**Bottom line:** the FDIC has not said what it kept. From what is public, the kept pool is **most likely about $190M of loans**, weighted to the **nonaccrual commercial real estate book** and a **stalled construction book**. The loans that can be named are **fraud-web and litigated credits, several of them second liens**, on **Inland Empire and LA County neighbourhood retail and medical-office centres and one small older apartment building**, not office towers. **No named loan is confirmed to be in the retained pool.**

**Tiers:** PRIMARY-READ = CREED or its research agent opened the regulator's or issuer's own document. SECONDARY = news or aggregator. INFERRED = arithmetic or reasoning, not a filing. Research agent notes (Opus, 2026-09-27, read in full by CREED): `research/2026-09-27_nano-banc-retained-pool-research-notes.md`. ⚠️ An unrelated "$260M" (collateral in the Zions/WAL dispute) circulates in 2025 coverage; it is not the FDIC figure.

### 1a. What the FDIC says: nothing about composition (PRIMARY-READ)
- FDIC press release, failed-bank page and FAQ (all 2026-09-25): *"It will also purchase approximately $476 million of the failed bank's assets. The FDIC will retain the remaining assets for later disposition."* **No breakdown, no loss-share, no purchase-and-assumption (P&A) agreement posted yet.**
- The only clue: the FAQ's *"If you received notice that the FDIC retained your loan…"* ⇒ the retained pool **includes loans** (PRIMARY-READ, by implication).

### 1b. By loan class — INFERRED

| Step | Figure | Basis / tier |
|---|---:|---|
| Loans on the bank's last books, 9/22/2026 | **$419.2M** = held-for-investment $322.1M + held-for-sale $97.1M | DFPI possession order Exh. A (DEWEY, uncommitted draft; research agent also read it) · PRIMARY-READ |
| Loans Sunwest says it assumed | **$227M** | Sunwest release 9/25 19:45 ET. **Not an FDIC figure; date and valuation basis unknown** |
| ⇒ Loans NOT taken by Sunwest | **≈ $192M gross** (≈ $183M net of the $9.2M allowance) | **INFERRED**, subtraction across a 3-day date gap and two sources. Consistent with most of the ≈ $215M retained pool being loans |
| ⚠️ The $97.1M held-for-sale pool | **FDIC or Sunwest? UNKNOWN** | Held-for-sale loans are carried at the lower of cost or market, so this pool was **already partly marked down** before the FDIC arrived. The P&A agreement settles which side it went to |

**What the bad book looked like at the last Call Report (6/30/26)**. It is the best guide to what an acquirer would decline, but it is an inference, not a list:

| Class (6/30) | Balance | Nonaccrual | Nonaccrual % of class | Source |
|---|---:|---:|---:|---|
| Nonfarm nonresidential CRE | $128.7M | **$74.3M** | **~59%** (non-owner-occupied, REGINALD) | FDIC BankFind API (PRIMARY-READ) · REGINALD §2b |
| "All other loans" (CRE finance not secured by real estate) | $87.9M | **$32.7M** | 37% | REGINALD §2b |
| Multifamily | $70.8M | $7.3M | 10% | API · REGINALD |
| Construction & land | $46.9M | $4.0M, **plus $41.4M 30–89 days past due = 88% of the book** | — | REGINALD §2b |
| 1–4 family | $116.2M | ~0 | — | API |
| C&I | $28.3M | $4.9M | 17% | REGINALD §2b |
| **Total noncurrent** | | **$123.2M** (all nonaccrual; 90+ days still accruing = 0; OREO = 0) | | API |

⇒ **INFERRED:** if Sunwest took mostly current loans, the retained pool holds most of the **$123M nonaccrual book** (60% of it nonresidential CRE, 27% CRE-finance) and likely the **delinquent construction book**. That is roughly **$165M of visibly troubled loans at 6/30** (REGINALD's cross-check), before Q3 charge-offs and the move to held-for-sale shrank it.
⚠️ **Counterweight (REGINALD §2b):** multifamily nonaccrual fell $30.7M → $7.3M in Q2 with **no charge-off and a $23.3M OREO-sale receivable**, consistent with one ~$23M multifamily loan foreclosed and **sold near carrying value**. Not every loan on this book cleared at a fire-sale price.

### 1c. By named loan — KNOWN that Nano made or held it, UNKNOWN whether it is in the retained pool

| Credit | Property / type | Nano lien, original face | Status (latest found) | Tier |
|---|---|---|---|---|
| 23750 Alessandro Blvd, **Moreno Valley** | Alessandro Plaza, **~119K sf strip centre** (retail, restaurants, dental/professional office) | **$9.72M, 1st** | Nano notice of default 5/20/2025. **Owner filed Ch.11 2026-08-18** (C.D. Cal. 26-12516) | lien: WAL verified complaint 8/18/2025 (A2, via WAL §2) · property/status: SECONDARY |
| 3700 Inland Empire Blvd, **Ontario** | Plaza Continental, **~120K sf office/medical + retail**, ~24% available | **$4.33M, 2nd** behind Preferred Bank $25.9M | Nano NOD 5/20/2025. **Owner filed single-asset Ch.11 2026-03-30** (8:26-bk-10986-MH) | same |
| 12233 Central Ave, **Chino** | Part of Chino Towne Center (CVS / 24 Hour Fitness anchored); this address = dental offices | **$5.99M, 2nd** behind Preferred $22.4M | ~~No distress event found~~ **Owner in Ch.11 (8:26-bk-10925-SC; see §6). Corrected 2026-09-29** | same |
| 9826 Cedar St, **Bellflower** (LA County) | Cedar Group Apartments, **30 units, built 1964** | **$8.0M, 2nd** behind Umpqua $6.47M | No sale since 1999. Liens total $14.47M ≈ **$482K/unit** ⇒ Nano's 2nd is **probably badly under-secured (INFERRED)** | same |
| Blackhawk Plaza, **Danville** (Contra Costa) | retail centre | $5M, 2nd | receivership ordered 2026-02-03, stayed by owner's Ch.11 2026-03-18 | SECONDARY |
| Gerald Marcil (guarantor-side loan) | — | $19.18M (2024-12-09) | Nano declared default; **Marcil sued Nano** (C.D. Cal. 8:26-cv-01143, 5/11/2026) | SECONDARY (WAL §3 also) |
| Sand City (Monterey County), Makhijani-linked entity | — | $37M | Nano won a defense verdict 2025-12-18 in the related suit; **loan status not found** | SECONDARY |
| Honarkar / MOM joint venture, **Laguna Beach** | collateral parcel **not identified** | ~$20M (per the arbitrator, it replaced promised equity) | ⚠️ The joint-venture debtors' own motions list six real-property lenders and **Nano is not among them** (PRIMARY-READ). MOM Ch.11 **dismissed 2025** | SECONDARY / PRIMARY-READ (the lender list) |

⚠️ **Do not sum this table.** The amounts are original face at different dates, not current balances. Some of these loans may have been paid down, charged off or sold before 9/25, and the list is what litigation happened to name, not the loan tape.

**What the named book tells the comp work (§2–§3):**
1. **It is neighbourhood retail, medical office and small multifamily in the Inland Empire and LA County.** It is not the Orange County/Laguna hospitality-retail book the packet's premise named (PROME corrected it at 12:3x ET), and it is not office towers.
2. **Several named Nano liens are SECOND liens.** A second lien's sale price measures the lien, not the property. It can clear near zero while the building is worth close to the first mortgage. **An FDIC sale of these liens will overstate any property-value loss** unless lien position is recorded (the §3 rule).
3. **Most named borrowers are already in bankruptcy.** A buyer prices bankruptcy delay and litigation cost, which push a sale price further below property value.

**Not reached (not evidence of absence):** the P&A agreement (not yet posted) · Stupin/Marcil court schedules (PACER/Justia blocked) · the arbitration award text (Jus Mundi 403) · assessor and LoopNet pages (403). DEWEY O1 (were the four deeds of trust still Nano's at 9/25?) is the open item that decides whether §1c is IN the pool.

## §2. The implied CRE mark

### 2a. The shared figure is REGINALD's, and CREED consumes it

> **CITED, REGINALD's desk scenario (9/22 base), not a CREED number and not an FDIC-reported mark:** the FDIC expects to lose **≈ $120M (range $110–120M) beyond what the bank itself had booked by 9/22/2026, ≈ 17% of its $690.9M of assets**, net of allowance (≈ $129M gross, adding the $9.2M ACL). Basis: tangible equity $5.66M (DFPI possession order Exh. A, via DEWEY) + the FDIC's $114M DIF estimate. **Retained pool ≈ $215M. Haircut on that pool: ~~a CEILING of ≤ ~56%~~ ≈ 51–56% in a ZERO-ADJUSTMENT scenario, not a bound; unallocable without the FDIC's bid terms.** Source: `AGENTS/REGINALD/reports/2026-09-27_nano-banc-failure-forensics.md` §3 — **current version `2117b2148`** (CATO NB1 applied); first read at the artifact 2026-09-27 ~12:4x ET uncommitted, then `d8010b97f`. The 6/30 base (≈ $153M, ≈ 21%) is REGINALD's trajectory figure and is **not used here for a collateral mark**.
>
> **How CREED uses it:** ~~*"≤ ~56% (ceiling, 9/22 base, unallocable)"*~~ *"≈ 51–56% (zero-adjustment scenario, 9/22 base, unallocable — not a bound)"*, **never as "a 56% haircut."** Any discount the FDIC gave Sunwest on the assets it bought lowers it; **a deposit premium or unpaid junior creditors raise it** (CATO NB1, applied 2026-09-28).

**The basis questions CREED sent before the figure was published** (read by REGINALD at `0eac3ffcd` and adopted in its §3):
- The **~$114M DIF cost is an FDIC estimate** of the fund's shortfall **after** shareholders' equity is gone. It nets several things together: any **discount** the FDIC gave Sunwest on the ~$476M of assets it bought, any **deposit premium** Sunwest paid, projected losses on the **retained** pool, and receivership costs. Unless the FDIC discloses the bid terms, the DIF cost **cannot be allocated** between the purchased and retained assets.
- **Dividing the DIF cost by the retained pool therefore overstates the retained-pool haircut** if Sunwest bought at a discount, and **understates** the total asset loss, because the equity left at failure absorbed losses first. That equity was $5.66M on 9/22 (0.82% of assets, DFPI order Exh. A via DEWEY), down from $39M at 6/30, so the Q3 loss of roughly $33M is already behind it.
- **Vintage — SUPERSEDED BASE (PROME, 12:4x ET, on DEWEY):** the "$260M retained" was $736M (6/30 Call Report) − $476M (FDIC, closing). DEWEY's read of the **DFPI possession order, Exhibit A, gives a 9/22/2026 balance sheet: total assets $690.9M** ⇒ ~$215M left after the $476M purchase. **CREED consumes REGINALD's 9/22-based figure**, with the 6/30 base beside it. The **$227M of loans assumed is Sunwest's own release** (9/25 19:45 ET), not an FDIC figure.
- **Allowance basis moved too:** the ACL was **$19.9M at 6/30 and $9.2M at 9/22** (2.85% of held-for-investment loans), so "book net of allowance" means different things on the two dates.
- **Basis:** a haircut can be stated **vs gross UPB** or **vs book net of allowance**. Those two differ, and the comps below are vs loan balance.

### 2b. What a mark in the ≈ 51–56% zero-adjustment scenario means against CREED's comps *(heading was "up to the ≤ ~56% ceiling" — narrowed 2026-09-28, CATO NB1)*

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
1. **A loss around the ≈ 51–56% zero-adjustment scenario on a bank's worst loans is inside the 2026 range for distressed CRE dispositions, not an outlier.** ~~The true figure is lower by any discount Sunwest received.~~ The true figure is lower by any discount Sunwest received and **higher** by any deposit premium or unpaid junior creditor claims — **the scenario is not a bound in either direction** (CATO NB1, 2026-09-28). CMBS dispositions run **35% across all property types YTD and ~49% for office** (JPM, secondary). The two monthly prints CREED read at primary are 48.8% and 72.6%. A pool loss at the scenario figure would sit **above the 35% all-types and ~49% office YTD averages and below August's 72.6%**.
2. **SoCal's three 2026 CMBS comps span 31% to 100%, and all three are OFFICE.** Location is not the variable. Asset quality, vacancy and how long the workout ran are. **Nano's named collateral (§1c) is neighbourhood retail, medical office and a small 1964 apartment building**, and CREED holds **no SoCal disposition comp on this basis for any of those types.**
3. **So the comparison is weaker than it looks, for three reasons:** the property types do not match; several Nano liens are **second liens**, which clear far below the property's own loss; and the credits are **fraud-web and litigated, most borrowers in bankruptcy**. **Read the Nano mark as consistent with, not confirming, the 2026 severity distribution.** REGINALD's fence says the same from the bank side: *"not a clean read-through to SoCal CRE marks generally."*
4. **The appraisal-lag finding matters more than the level.** If 2026 distressed sales clear ~20% below the latest appraisal (Deutsche Bank, secondary), then any bank still carrying problem CRE at appraisal carries a mark the market would not pay. That is REGINALD's reserve question, and it is why the FDIC's eventual clearing price (§3) is worth waiting for: it will be a **sale**, not an estimate.

## §3. The forced-sale comp: DOCKET row and WATCH_FOR terms (CREED authors, PROME registers)

**Why it is worth registering.** When the FDIC sells what it kept, it will print a clearing price for California bank-held CRE loans (mostly Inland Empire / LA County by the named book), and on a pool the FDIC has already marked (the DIF cost). Clearing prices on bank-held small-balance CRE are the scarcest data on CREED's board: every realized comp CREED holds is either CMBS (Trepp liquidations, §2) or a one-off property sale. No comp is a bank loan pool.

**What it will and will not be evidence of (fixed now, before the print):**
- ✅ **S6 evidence** (forced sale / recognition), a `VX-CREED-5.01` comp row, recorded **vs unpaid principal balance (UPB)** and, separately, vs book value if the FDIC discloses it. **Never vs appraisal**, and never mixed with the purchase-price comps (205 W Randolph −72% is vs a 2017 purchase price, a different object). 🔴 **Record LIEN POSITION on every loan or pool.** A second lien's price measures the lien, not the building (§1c: four of the named Nano liens are seconds: Ontario, Chino, Bellflower, Danville), so **second-lien prices are excluded from any property-value read** and reported on their own line.
- ⚠️ **Most likely NOT a `CREED-T-06` member.** T-06 (`> 30%` discount to basis) counts a cluster in **PERFORMING** collateral only. The retained pool is **INFERRED** to be mostly the nonperforming book (§1), so a non-performing-loan (NPL) pool sale below 70% of UPB would be the expected outcome, not a T-06 datum. It qualifies **only** if the FDIC sells a performing pool separately and that pool clears below 70% of UPB.
- ⚠️ **n=1, fraud-origin bank.** One pool from a bank whose losses began with insider self-dealing does not generalise to SoCal CRE. Record it; do not extrapolate.

**Draft DOCKET row** (six columns per `PROME/DOCKET.tsv` L77; PROME registers, CREED authored):

| date | catalyst | owners | state | artifacts_citing | notes |
|---|---|---|---|---|---|
| `on-FDIC-publishing-the-Nano-Banc-asset-sale` *(check-by 2027-06-25)* | FDIC disposition of the Nano Banc (Irvine CA, failed 2026-09-25) assets retained by the receiver (≈$215M on the 9/22 base): a loan sale, structured transaction or asset sale prints a clearing price for SoCal bank-held CRE | CREED (S6 comp) · REGINALD info (severity reconcile) · WAL consumes (O7: the four Inland Empire / LA County liens sit ahead of WAL's collateral) | PENDING | `AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md` §3 | Record price as % of UPB by pool, performing vs NPL separately, by property type and LIEN POSITION (second-lien prices never read as property marks). S6 comp, NOT a T-06 member unless a PERFORMING pool clears < 70% of UPB. Typical FDIC disposition 3–9 months (PROME plan §2B); check-by = closing + 9 months |

⚠️ **Why a check-by date on an undated row:** DOCKET's header says it carries *dated* catalysts. An event-keyed row with no date never goes overdue, so it can rot silently. The check-by date (closing + 9 months, the plan's outer bound) makes it go overdue if the FDIC has not sold by then, which is itself information. PROME's call whether to use it.

**Draft WATCH_FOR terms (to WALTER, via PROME's registration):**
```
Nano Banc | Nano Banc receivership | FDIC as receiver for Nano Banc | CREED S6 comp (retained-asset disposition) — DOCKET row on-FDIC-publishing-the-Nano-Banc-asset-sale
FDIC loan sale | FDIC structured transaction | failed bank loan sale | CREED S6 comp — record price vs UPB, performing vs NPL separately
Sunwest Bank | CREED info (acquirer; loss-share or put-back of Nano loans would change what the FDIC kept)
23750 Alessandro Blvd Moreno Valley | 3700 Inland Empire Blvd Ontario | 12233 Central Ave Chino | 9826 Cedar St Bellflower | CREED S6 comp + WAL consumes (WAL O7) — an FDIC sale of Nano's liens prints a mark on WAL's own collateral properties
Honarkar | Laguna Beach (Nano's ~$20M loan, B3) | CREED info + REGINALD (ZION lien collision is REGINALD's lane)
```
⚠️ **`MOM CA Investco` is DROPPED from the terms.** PROME named it, but the MOM Investcos Chapter 11 was dismissed in 2025 (WAL §1, B2, DEWEY to confirm), so it is no longer a live venue for a disposition to print in. The four addresses replace it (PROME premise correction, 2026-09-27, verified at WAL's file §2).

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
- **Below 1.0× on an amortizing refinance at the MIDDLE and HIGH spreads (225bp and 275bp; break-even 8.33% and 8.75%):** the whole debt-yield-<8% bucket, i.e. **51% of the September cohort** and **~36% of the 2026 hard-maturity wall** (June vintage; **count vs balance is an explicit unknown**). ⚠️ **NOT at every spread:** at 175bp the amortizing break-even is 7.93%, so the 7.93–8.00% slice covers at up to ≈ 1.008×. At the low spread the 8% bucket is therefore a slight OVER-count. On interest-only terms the 7–8% slice straddles 1.0× at every spread. *(Corrected 2026-09-27 on CATO NB4, `AGENTS/CATO/runs/2026-09-27_1300_nano-banc-fleet-review.md`, relayed by PROME. The original said "at every spread in the band", which the table's own 7.93% contradicts.)*
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
| **Convergence score (25/45, held pending Will's S8a ruling — *27/45 from 2026-09-28, S8a ruled 4; unrelated to Nano*)** | **No** | — |
| **Any `PRED-CREED-*` row** | **No** | No CREED prediction references a bank failure |

**No CREED letter, score, band or trigger moves on Nano Banc.** What changes is one watch item (§3) and, if REGINALD's severity figure holds (§2), one more data point that small-bank CRE marks in SoCal are deep where the book went bad.

---

## §6. Addendum 2026-09-27 (after delivery): DEWEY committed (`6a90ca732`)

*Appended, not edited above. §1–§5 stand.*

- **Re-check discharged.** The 9/22 balance-sheet figures CREED cited in §1b/§2a are **identical** in DEWEY's committed file ($690.9M · loans held for sale $97.1M · held for investment $322.1M · ACL $9.2M · equity $5.66M). REGINALD's committed §3 (`d8010b97f`) also matches (≈ $120M ≈ 17%; ≈ $215M; ~~≤ ~51–56%~~ ≈ 51–56% zero-adjustment scenario, not a bound — REGINALD's current wording at `2117b2148`). ~~**Nothing above changes.**~~ **The figures match; the "ceiling" framing above was narrowed 2026-09-28 (CATO NB1).**
- **§1c upgraded for two liens (DEWEY §4, from the borrowers' own Ch.11 filings, PRIMARY):** ~~**Ontario (3700 Inland Empire Blvd) and Chino (12233 Central Ave) were STILL NANO's liens less than three weeks before the failure.**~~ **Ontario (3700 Inland Empire Blvd) was still Nano's lien on the evidence dated 9/8–9/11 (under three weeks before failure); Chino on evidence dated 8/26 — 30 days before failure.** Moreno Valley is "leaning still-Nano" and Bellflower is UNKNOWN. That is **still not proof that they are in the retained pool** (the P&A settles it, expected ~10/05–10/09), ~~but it removes the "sold before failure" branch for those two~~ **and a transfer after those dates remains possible — it makes "sold before failure" less likely for those two, it does not remove it.** ⚠️ **Chino identity is unverified:** DEWEY's filing gives **12125** Central Ave, WAL's original collateral list **12233**; the **65.91% TIC/property match is explicitly unverified**, and **no assignment proves WAL's priority.** *(CATO NB6, applied 2026-09-28.)*
- **Debtor-side marks (not FDIC marks; DEWEY §5):** Chino Towne Center, Feb-2025 appraisal ~$29M vs a **2026 broker range of $23.5–26.5M** (−9% to −19%), total liens ~$19.1M. Nano's second lien there ~~looks **covered at the broker range**~~ **would be covered IF the broker range held AND the property match is right** — the broker range is a debtor-side marketing range, **not an established mark on WAL's matched collateral**, and the address/TIC match above is unverified (CATO NB6, 2026-09-28). Bellflower (§1c) does not look covered on any read. Hotel Laguna: a $27.0M first lien (Banc of California) against an $82.0M value (MOM CRO table), a lien CREED does not attribute to Nano.
- **DEWEY's named total is ≈ $93M face/stated** (Marcil $19.18M + $8.5M; MOM JV $20M, which the arbitrator says may be set aside; the Stupin-web liens). ⚠️ **§1c's "do not sum" still applies.** It is face or stated, not current balance.
- **🔴 Observable in 2 days, added to the §3 watch:** the **Plaza Continental hearing, Tue 2026-09-29 1:30 pm (C.D. Cal. Bankr. 8:26-bk-10986, Judge Houle).** If "FDIC as Receiver for Nano Banc" appears for the Ontario lien, that lien is in the **retained** pool. If Sunwest appears, it was **sold**. This is the first per-loan answer to §1, before the P&A. ⚠️ *(CATO, 2026-09-28: the hearing is an evidence **opportunity**, not a guaranteed answer — a generic FDIC or Sunwest appearance may not establish lien ownership. **Record only what the specific filing establishes; UNKNOWN is a valid outcome.**)*

## §7. Addendum 2026-09-29 (evening): the Plaza Continental hearing — ownership of the lien is still UNKNOWN

*Appended, not edited above. §1–§6 stand. Full notes and a 24-attempt retrieval log: `research/2026-09-29_plaza-continental-hearing-notes.md` (read-only Opus research agent, read in full by CREED).*

- **Answer: UNKNOWN.** Nothing reachable shows whether the Ontario $4.33M second lien was retained by the FDIC or sold to Sunwest. As CATO warned (9/28), the hearing was an opportunity to find out, not a guaranteed answer.
- **The document most likely to settle it is unread:** Doc 93, a *Notice of Appearance and Request for Notice*, filed **9/29 5:30 pm PDT, after the hearing**. The filer isn't shown on CourtListener and the PDF is PACER-only. If the caption reads "FDIC as Receiver for Nano Banc", the lien was **RETAINED**. If it names Sunwest, it was **SOLD**. Anyone else settles neither.
- **What IS established (PRIMARY-READ):** debtor = **Plaza Continental Group LLC**. Judge Houle's 9/29 calendar listed four Plaza matters: receiver turnover + § 362(d)(3) adequate protection (Doc 82); the continued Nano/Preferred stipulation (Doc 58; "Nano Banc" there is the **7/30 caption carried forward, not evidence of current ownership**); exclusivity; and the status conference. **No tentative rulings. No minute entry or order as of 6:03 pm PT.** Phone appearances registered by 7:27 am: Preferred, the debtor, its CRO, and an unnamed "Interested Party" (Zarnighian). **None for Nano, the FDIC or Sunwest.** ⚠️ That absence proves nothing either way: in-person appearances aren't listed.
- **Re-check:** Doc 93 (PACER, ~$0.10–0.30, or a CourtListener upload) · the minute entry/order ~**9/30–10/2**, since an order on Doc 82 may name who receives adequate-protection payments on the Nano lien · the FDIC P&A ~10/05–10/09, which probably won't list individual loans.
- **No letter moves.** This remains a per-loan evidence opportunity for §1, not a CREED trigger input.
