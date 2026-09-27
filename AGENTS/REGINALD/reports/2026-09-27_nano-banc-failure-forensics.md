# Nano Banc failure (closed Fri 2026-09-25): forensics, my February call, lookalike screen

**Desk:** REGINALD · **Written:** 2026-09-27 Sun (12:3x–13:xx ET) · **Commissioned:** PROME packet `inbox/2026-09-27_from-PROME_nano-banc-failure-forensics-and-cohort-read.md` (Will-directed; research only, no card, no trade).
**Primary data:** FFIEC CDR Call Report facsimiles, RSSD 3635029, 12 contiguous quarters 9/30/2023 → 6/30/2026 (FFIEC 051 filer; pulled 2026-09-27 via `scripts/mi3_cohort_screen.py` fetch functions) · FDIC financials API (all 4,313 filers, REPDTE 20260630) · FDIC failed-bank list CSV (fdic.gov, pulled 2026-09-27: "Nano Banc, Irvine, CA, 58590, Sunwest Bank, 25-Sep-26, fund 10555").
**Shared fact base:** PROME plan §1 (`PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md`), cited, not re-derived, except where noted as REPRODUCED or CORRECTED.
**Legal/enforcement leg (§1 enforcement rows, §5):** read-only Opus research agent; its evidence file is `reports/2026-09-27_nano-banc_legal-leg.md`.

---

## 0. Answer first

| Question | Answer |
|---|---|
| Did the fleet call it? | **Yes, in direction; no, in timing, cause-mix or severity.** `ML-REG-044` (2026-02-02) said "facing receivership". It is CONFIRMED by the FDIC failed-bank list (closed 2026-09-25). It had no date, no probability and no severity, and it sits in no `PREDICTIONS.tsv` row, so it is an un-scored call. |
| What killed the capital? | **Mostly NOT credit.** FY2025 net loss −$75.3M = **legal fees and expenses $46.3M (61%)** + loan-loss provision $16.7M (22%) + a $12.8M tax *expense* on a pre-tax loss, consistent with a deferred-tax-asset write-off (DTA $14.8M at 6/30/25 → $0 at 9/30/25) (17%). Pre-provision, pre-legal operating earnings were ≈ breakeven (+$0.5M). |
| What made the FDIC loss large? | **The assets.** Equity was gone before closure; the DIF bears asset marks. Implied loss on assets beyond the bank's own 9/22 books ≈ **$120M ≈ 17% of $690.9M** (the base to cite); ≈ $153M ≈ 21% against the 6/30 Call Report, the $33M difference being Q3 losses the bank booked itself (§3). That is a CRE-heavy book: 73% of loans were CRE including CRE-finance loans booked outside the real-estate lines. |
| C&I → RE shift: reclassification or runoff? | **Neither as framed. RE did not grow (RE loans $498M → $363M).** The C&I decline ($228M → $28M) splits into (a) a **quarter-by-quarter transfer out of C&I (item 4) into "other loans" (item 9.b)**, which rose $22M → $88M; (b) C&I charge-offs of ≈$29M (2024–H1'26); (c) ≈$105M of runoff/payoff. The **"hidden CRE" signal was DISCLOSED the whole time**: Memo item 3 (RCON2746, loans to finance CRE *not* secured by real estate) was **$179.6M = 79% of C&I at 12/31/2023**. My 14-bank cohort's maximum on that basis is ~24% (WAL). |
| Lookalikes? | **None of my 14 cohort banks meets ≥2 of the 4 legs.** Nationwide, **Nano was the only lending bank meeting all 4 at 6/30/26, and no other met 3.** Genuine distress pairs are small and outside Will's book perimeter (§4). **No TERRY packet warranted.** |
| Systemic? | **No by size, yes as a pattern tell.** Origin idiosyncratic (founder fraud → litigation), but its *balance sheet* carried two markers my instruments already measure: CRE-finance booked as C&I, and reserves collapsing below nonaccruals. |

---

## 1. Grading my own call: `ML-REG-044` → **CONFIRMED (2026-09-25, FDIC failed-bank list, primary)**

| KB claim (2026-02-02) | Verdict | Evidence |
|---|---|---|
| "Facing receivership" | ✅ **CONFIRMED**: closed 9/25/26, FDIC receiver, Sunwest Bank acquirer | FDIC failed-bank CSV (primary, pulled 9/27) |
| "Capital depletion" | ✅ Right, and it had already started: equity $126.1M [6/24] → $115.2M [12/24] → $100.9M [6/25] → $41.5M [12/25] → $38.8M [6/26] | Call Report RC item 27a |
| "Arbitration liability… extensive damages" as the capital drain | ✅ **Right on mechanism, and the strongest part of the row.** RI-E "Legal fees and expenses" $2.7M [2023] · $5.7M [2024] · **$46.3M [2025]**; accrued expenses (RC-G 1.b) $8.6M [12/24] → **$44.1M [12/25]** → $4.2M [6/26] | Call Report RI-E 2.f, RC-G 1.b |
| "Regulatory strangulation" | ⚠️ Directionally right. The bank fell below *well capitalized* at 12/31/25 (Tier 1 RBC 7.15% < 8%; leverage 4.77% < 5%). Reciprocal deposits went $142.3M [6/25] → $0 [12/25]. | RC-R, RC-E M1.g |
| "Fed C&D March 4, 2025" | ⛔ **WRONG, INVERTED: my row read a TERMINATION as an ISSUANCE.** The Fed C&D against Allegiant United Holdings / Nano Financial Holdings / Nano Banc was issued **2022-01-18** and **terminated effective 2025-03-20**. VERIFIED by me at the Fed primary: the Board release of **2025-04-01** "announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc" (federalreserve.gov/newsevents/pressreleases/enforcement20250401a.htm). Found first by WAL (KB-WAL-204, packet O5). My row's only source was an advocacy page on Issuu ("Save Laguna"). **The error mechanism: 3/4/2025 is the Issuu UPLOAD date** of the Fed documents, not an order date. The Fed's enforcement CSV lists exactly 4 Nano actions: Written Agreement 2021-02-24 (CRE concentration + governance, with no termination shown) · C&D 2022-01-18 (terminated 2025-03-20) · two 2024-11-01 prohibitions (Gressak, with a $75K CMP; Chung). I re-read that CSV at the primary. | Fed release 4/1/2025 (primary) · `archive/research/…/RQ-REG-A02B…md` fn 18 |
| "Found LIABLE for fraudulent inducement" | ⚠️ **Overstated.** Liability was for conspiracy/aiding-and-abetting in **one** forum (Honarkar JAMS award, interim 2/21/2025, partial final 5/23/2025). Nano won a **full defense verdict** in *Security National Guaranty v. Evariste* (OC Superior jury, Hunton release 12/18/2025). | WAL §1 (KB-WAL-204); not re-fetched by me |
| "FBI warrants" (Nano) | ❌ **Not supported.** The FBI searched **Continuum Analytics**, not Nano (Reuters 10/20/2025 via KB-WAL-137). | WAL §1 |
| "Death spiral" via inability to collect Stupin loans | ❌ **Not what the Call Reports show as the capital drain.** Credit provisions were 22% of the 2025 loss. Credit mattered at *resolution* (§3), not in the capital collapse. | RI |
| **What it did NOT predict** | Timing (7½ months out; no date given) · the **15.5% DIF severity** · that the DIF loss would be driven by **asset marks** while the capital loss was driven by **litigation** · that the Fed order was terminated while DFPI escalated (DFPI March-2026 9.5% tangible-equity order per PROME §1). | |
| Scoring | **No back-scored forecast.** There is no `PREDICTIONS.tsv` row; it stays an un-scored KB call. It is also not a calibration datum: a receivership call on a bank found liable for fraudulent inducement is a low-difficulty call. | |

---

## 2. Failure anatomy: Call Reports, 12 quarters ($M; FFIEC 051)

### 2a. The path

| Qtr end | Loans | Nonaccrual | 90+ acc. | **Noncurrent % loans** | ALLL | **ALLL / noncurrent** | MI3 | C&I (item 4) | Other loans (9.b) | CRE + MI3 % loans | CRE conc. % total capital, secured only (**incl. MI3**) | Leverage |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9/30/23 | 744.9 | 19.9 | 24.8 | **6.0%** | 35.4 | 79% | 167.1 | 213.6 | 26.5 | 78% | 299% (**430%**) | 12.6% |
| 12/31/23 | 748.4 | 25.3 | 8.1 | 4.5% | 36.6 | 109% | 179.6 | 227.9 | 22.4 | 78% | 295% (437%) | 12.7% |
| 3/31/24 | 732.3 | 37.9 | 0 | 5.2% | 34.5 | 91% | 170.9 | 217.0 | 18.8 | 78% | 292% (427%) | 12.7% |
| 6/30/24 | 705.8 | 25.6 | 0 | 3.6% | 30.9 | 121% | 145.9 | 180.2 | 18.8 | 77% | 293% (408%) | 13.2% |
| 9/30/24 | 620.4 | 14.6 | 0 | 2.3% | 27.3 | 188% | 118.0 | 124.7 | 15.8 | 77% | 284% (378%) | 11.6% |
| 12/31/24 | 628.6 | 1.0 | 0 | **0.2%** | 26.2 | — | 131.1 | 134.8 | 17.8 | 76% | 291% (402%) | 11.2% |
| 3/31/25 | 655.9 | 11.6 | 0 | 1.8% | 24.6 | 212% | 128.5 | 132.8 | 17.8 | 76% | 310% (418%) | 12.1% |
| 6/30/25 | 612.8 | 62.5 | 0 | 10.2% | 20.4 | **33%** | 127.6 | 105.0 | 35.8 | 76% | 322% (446%) | 10.2% |
| 9/30/25 | 581.1 | 89.4 | 0 | 15.4% | 19.2 | 21% | 121.1 | 101.4 | 32.7 | 74% | 407% (568%) | 7.2% |
| 12/31/25 | 541.4 | 131.5 | 0 | 24.3% | 13.5 | **10%** | 100.5 | 41.7 | 70.2 | 73% | 599% (803%) | 4.8% |
| 3/31/26 | 510.0 | 104.9 | 0 | 20.6% | 13.0 | 12% | 99.5 | 40.8 | 71.1 | 72% | 548% (754%) | 4.8% |
| 6/30/26 | 478.8 | 123.2 | 0 | **25.7%** | 19.9 | 16% | 104.1 | 28.3 | 87.9 | 73% | 529% (755%) | 5.0% |

*CRE (secured) = construction (F158+F159) + multifamily (1460) + owner-occ nonres (F160) + other nonres (F161); the concentration column uses the interagency-guidance numerator: construction + multifamily + non-owner-occupied nonres, then **+ MI3** in parentheses (the 2006 guidance counts loans to finance CRE not secured by real estate). Total capital = RCOA3792. Leverage = RCOA7204.*

⚠️ **CORRECTION to the shared fact base's framing ("0% → 26% in 18 months"):** PROME's quarterly figures REPRODUCE exactly (0.2% [12/24] · 1.8% · 10.2% · 15.4% · 24.3% · 25.7%). The **starting point is not clean**, though. Noncurrent was **4.5–6.0% of loans through late 2023–H1 2024**, about 5–10× a normal community bank. The 0.2% trough at 12/31/24 was produced by **$33.4M of nonaccrual assets SOLD in H2-2024** (RC-N M8, C411) plus an $85M loan-book drop in Q3-24. **The 12/31/24 report was amended 2025-04-18.** Read the path as **"a chronically impaired book, cleaned by a sale, then a second and larger wave"**, not "clean book to 26% in 18 months."

### 2b. Noncurrent by loan class at 6/30/26 ($123.2M, all nonaccrual)

| Class | Balance | Nonaccrual | % of class | Share of noncurrent |
|---|---|---|---|---|
| Other (non-owner-occ) nonres CRE | 126.1 | **74.3** | **59%** | 60% |
| "All other loans" (item 9.b, where the CRE-finance book moved) | 87.9 | **32.7** | 37% | 27% |
| Multifamily | 70.8 | 7.3 | 10% | 6% |
| C&I | 28.3 | 4.9 | 17% | 4% |
| Construction & land | 46.9 | 4.0 | 9% | 3% |
| **Memo:** CRE-finance not secured by RE (MI3, spans 4 + 9.b) | 104.1 | **37.6** (RC-N M2) | 36% | — |

**The next wave was already on the 6/30 report: construction 30–89 days past due = $41.4M = 88% of the construction book** (RC-N F173). Construction balances *rose* $38.3M → $46.9M in H1-26 while that book went delinquent. That is consistent with protective advances into a stalled project; the Call Report cannot determine it.

**Multifamily nonaccrual fell $30.7M → $7.3M in Q2-26 with no multifamily charge-off**, and the 6/30 report carries a **$23.3M "receivable from the sale of other real estate owned"** (RC-F 6.h) plus a $40K OREO-sale gain (RI 5.j). That is **consistent with one ~$23M multifamily loan foreclosed and sold near carrying value in the quarter**. Not every mark on this book was a fire-sale mark (CREED's counterweight class).

### 2c. Losses taken before the failure

| Year | Charge-offs (gross) | Where | Provision | Legal expense | Net income |
|---|---|---|---|---|---|
| 2023 | 6.4 | C&I 2.2 · all other 4.2 | 0.8 | 2.7 | +5.8 |
| 2024 | 16.9 (incl. 8.7 transfer write-down) | **other nonres CRE 13.1** · C&I 2.1 · owner-occ 1.1 · constr 0.4 | 1.8 | 5.7 | −9.6 |
| 2025 | 30.2 (incl. 2.4 transfer write-down) | **C&I 23.2** (of which CRE-finance/MI3 5.7) · other nonres 4.2 · all other 2.9 | 16.7 | **46.3** | **−75.3** |
| H1-26 | 8.0 | C&I 4.0 · other nonres 3.9 | 14.2 | n/a (semiannual item not on the 6/30 051) | −2.2 (Q2 non-interest expense *negative*, −$7.2M, i.e. an accrual reversal) |

**Reserve behaviour is the loud tell, and it is on my matrix instrument.** ALLL covered 109% of noncurrent at 12/23. It then *fell* ($36.6M → $13.5M) while noncurrent rose, reaching **10% coverage at 12/31/25**. My matrix's reserve-vs-nonaccrual leg (v2.0, 8/20) flags any bank below 100% (FLG 29%, AMTB 51%, EGBN 88% at Q2-26). **Nano would have flagged at 33% from 6/30/25, five quarters before failure.** It was never in my cohort (private, $0.9B).

### 2d. C&I → "other loans": the schedules, quarter by quarter

| Quarter | Δ C&I | C&I charge-offs in qtr | Δ Other loans (9.b) | Δ MI3 |
|---|---|---|---|---|
| Q2-25 | −27.8 | 7.8 | **+18.0** | −0.9 |
| Q4-25 | **−59.7** | 12.5 | **+37.5** | −20.6 |
| Q2-26 | −12.6 | ~4.0 (H1) | **+16.8** | +4.6 |

**Reading (decided from the schedules, not the totals):** C&I declines coincide with same-quarter jumps in item 9.b, so this is a transfer between loan categories. It is **not a move INTO real estate**; RE-secured CRE fell in every one of those quarters. Throughout, MI3 was most of the two lines it can sit in: MI3/(item 4 + 9.b) ran **70% → 90%**. So the "hidden CRE" was mostly CRE-finance lending booked in commercial lines, and **the Call Report's own memo line disclosed it every quarter**.
- **The Metropolitan Capital pattern applies in substance** (CRE exposure far above the headline RE share: 53% secured CRE vs 78% including MI3 at 12/23). **It does not apply in form**: at Metropolitan the memo line under-reported, while at Nano the memo line was accurate and large.
- ★ **The regulator named this book.** DFPI's 3/6/2026 consent order (§A) required "reducing the Bank's CRE concentrations **and concentrations in unsecured loans to finance real estate**" (order text, primary, re-read by me). That is the MI3 population, in the supervisor's words, six months before closure.
- **The recategorization out of C&I in 2025–26 coincides with the late amendments** (9/30/25 report last updated 2025-12-31; 12/31/25 report last updated **2026-06-05**; 3/31/26 last updated 2026-07-13). That is consistent with examiner-driven corrections under the DFPI action. **Whether the transfers were corrections or relabels is NOT determinable from the Call Report**; it is a question the Fed OIG Material Loss Review (~late Mar 2027) will answer.
- ⚠️ **Base rate before instrument:** MI3 ≥ ~70% of C&I two years before failure is a striking single case (n=1). I have not screened the national population on it (needs the FFIEC bulk RC-C file, ~4,300 filers). **Do not adopt "MI3 share" as a failure predictor until that base rate is run.**

### 2e. Funding (context, not cause)
Deposits $870M [3/25] → $686M [6/26] (PROME §1, REPRODUCED from RC 13.a: $870.2M → $685.8M). Brokered deposits stayed large ($156.3M at 6/26 = 23% of deposits; $201.0M at 3/26) **after the bank fell below well-capitalized at 12/31/25**. FDI Act §29 restricts brokered deposits for adequately-capitalized banks absent an FDIC waiver. Whether a waiver existed is unknown, so this is **a question, not a finding**. Loans pledged as collateral jumped $170.6M [12/25] → $263.9M [3/26] (RC-C M14), which is liquidity lines being secured. **Uninsured deposits 56%** at 6/26 (DEP − DEPINS = $386.6M, FDIC API; REPRODUCES PROME's ≈57%).

---

## 3. THE SHARED FIGURE: implied loss on assets (REGINALD owns · CREED, WAL and PROME consume)

> ### **CITE THIS: the FDIC expects to lose ≈ $120M on Nano Banc's assets beyond what the bank itself had booked by 9/22/26. That is ≈ 17% of its $690.9M of assets on the bank's last books (net of allowance). Range $110–120M.**
> **Basis:** tangible equity at 9/22/26 ($5.66M, DFPI possession order Exh. A, via DEWEY `output/2026-09-27_nano-banc-primary-documents.md`) + FDIC-estimated DIF cost ($114M, FDIC PR 9/25, an *estimate*; the final figure comes in the Fed OIG MLR ~late Mar 2027). Identity: loss vs a balance sheet = equity consumed + DIF shortfall (+ any general-creditor shortfall).
> **Retained pool:** $690.9M − $476M purchased ≈ **$215M** (9/22 books vs FDIC closing figure, three days apart). **Haircut ceiling ≤ ~51–56%**, UNALLOCABLE without the FDIC's bid terms (CREED §2a). **This supersedes the ~$260M in PROME plan §1**, which was 6/30 arithmetic.

**Two bases, one trajectory. Name the base every time you cite.**

| Base | Balance sheet | Equity | Implied loss (net of allowance) | % of assets | Gross basis (+ allowance) | Retained pool → ceiling | **Who cites it** |
|---|---|---|---|---|---|---|---|
| **9/22/26: bank's books (DFPI Exh. A)** | $690.9M | $5.66M | **≈ $120M** (range $110–120M) | **≈ 17%** | ≈ $129M (+ ACL $9.2M) | ≈ $215M → **≤ ~51–56%** | **CREED** (collateral marks) · **WAL** (mark-contagion to shared collateral) · **PROME's synthesis for Will** (headline). This is the FDIC's mark beyond the bank's own last books, the closest balance sheet to the 9/25 transfer. |
| 6/30/26: last Call Report | $736.2M | $38.8M | ≈ $153M (range $140–153M) | ≈ 21% | ≈ $173M (+ ALLL $19.9M) | ~~$260M~~ superseded | **Trajectory and cross-bank comparison only** (Call Reports are the common basis across banks and are what the MLR will reconcile to). **Not for a collateral mark.** |
| **Difference** | −$45.3M | −$33.1M | **$33.1M = Q3 loss the bank booked itself** (retained earnings −$122.0M at 9/22) | | ACL fell $19.9M → $9.2M in Q3 | | Q3 charge-offs + the $97.1M move to held-for-sale (marked to lower of cost or market) took the book down before the FDIC arrived. |

*Low end of each range = minus ~$5–10M assumed for receivership/admin costs inside the DIF estimate (not an asset mark). The 6/30 base also contains Q3 non-credit operating losses (legal/opex).*

**What the figure does and does not include (both bases):**

| Item | Effect | Direction |
|---|---|---|
| Receivership/admin costs inside the DIF estimate | not an asset mark | overstates → the low ends above |
| Deposit premium paid by Sunwest (if any) | lowers the DIF cost | **understates** the asset loss by the premium |
| General unsecured creditors (e.g. an arbitration award) rank BELOW depositors (12 U.S.C. 1821(d)(11)) and absorb loss before the DIF | not in the DIF cost | **understates**. The 9/22 books carried only $8.4M of other liabilities, so no large award was booked (DEWEY). |
| The $114M is an estimate at closing | — | either way |

**Per CREED §2a (read at `0eac3ffcd` before publishing, adopted in full):** (1) the DIF cost nets any discount given to Sunwest on the ~$476M it bought, so **the loss cannot be allocated between purchased and retained assets without the FDIC's bid terms**; the P&A agreement (DEWEY §3) will settle it; (2) the $227M of loans assumed is **Sunwest's release**, not an FDIC figure; (3) **the ceiling assumes zero purchase discount and no premium**, and any discount lowers it. Cite the retained-pool number as "≤ ~56% (ceiling, 9/22 base, unallocable)", never as a haircut.

**Sanity cross-checks:** Nano's own reserve covered ≈ 13% of the 6/30-base loss (ALLL $19.9M). At 6/30, noncurrent $123.2M + construction 30–89 DPD $41.4M = $164.6M of visibly troubled loans, so the 6/30-base loss is ≈ 85–93% of that troubled set if the performing loans were at par. That is severe, and consistent with fraud-tainted, litigated collateral. **Metropolitan Capital (1/30/26):** DIF $19.6M = 8% of $235M assets (PROME §1). Nano's DIF cost is 15.5% of 6/30 assets (16.5% of 9/22 assets), the highest of the six 2026 failures. **Fence:** this is a mark on a *fraud-tainted, litigated* SoCal book, **not a clean read-through to SoCal CRE marks generally.** CREED's forced-sale comps (S6) are the right instrument for that once the FDIC sells the retained pool.

---

## 4. Lookalike screen (6/30/26 Call Reports, FDIC API, all 4,313 filers)

**Legs:** {noncurrent > 10% of loans · uninsured deposits > 50% · equity/assets < 6% · **CRE concentration > 300% of total capital**}. ⚠️ **Substitution, stated plainly:** PROME's leg 1 was "CRE-concentration **enforcement action on record**". That is not screenable from the API, so I used the regulatory CRE-concentration ratio (construction + multifamily + non-owner-occ nonres ÷ total capital, secured only, which excludes MI3) as the proxy. The enforcement leg was **NOT run** nationwide. "FAU >300% list": **I do not hold the names**; `ML-REG-052` carries counts only (1,788 banks). The national screen replaces it.

**Filters:** excluded insured branches of foreign banks and trust companies (equity field 0 or loans < 20% of assets). 4,151 lending banks remain.

| Result | Count |
|---|---|
| All 4 legs | **1: Nano Banc** (NC 25.7% · uninsured 56% · EQ 5.3% · CRE 529% of capital, **755% incl. MI3**) |
| 3 legs | **0** |
| 2 legs | 43. **35 of them are "CRE > 300% + uninsured > 50%"; 34 of those have NC < 2% (max 5.1%, Touchmark GA), equity 7–15%.** That is a common business-bank profile, not distress. It includes **Sunwest Bank itself** (the acquirer: CRE 327%, uninsured 53%, NC 0.6%, EQ 9.3%). |

**2-leg banks where a distress leg (NC > 10% or thin *regulatory* capital) is one of the pair** (leverage from FDIC API RBC1AAJ; banks with low GAAP equity but leverage > 8% dropped as AOCI-driven: Phenix-Girard AL 11.8%, FNB Lake Jackson TX 11.7%, PBT Bancorp KY 8.2%):

| Bank (cert) | State | Assets | Legs | NC | Uninsured | Leverage | Note |
|---|---|---|---|---|---|---|---|
| First Southern Bank (29332) | AL | $679M | NC + uninsured | 10.9% | 53% | 8.9% | H1-26 loss −$8.7M; CRE 171%. **The closest size analogue; capital intact.** |
| Lamont Bank of St. John (8681) | WA | $51M | NC + EQ | **49.8%** | 8% | **3.0%** | Most distressed on the list; **not CRE** (CRE ≈ 0%). |
| Columbia S&L (28480) | WI | $21M | NC + EQ | 19.5% | 2% | 5.5% | Tiny, not CRE. |
| *Tioga-Franklin SB (33802)* | *PA* | *$68M* | *EQ + CRE (822%)* | *9.2%* | *6%* | *2.1%* | ***Already failed 8/21/26.*** *In-sample check: the screen catches a known failure.* |

**My 14-bank cohort: none meets ≥ 2.** One leg each: **BKU** (uninsured 58%), **FLG** (CRE 328%), **VLY** (CRE 320%). All others meet zero. Noncurrent and equity are nowhere near Nano (cohort high NC = FLG 4.97%, then WAL 2.82%; all EQ ≥ 8.0%).
**Will's book perimeter** (KRE puts · WAL Dec-18 $70P · OZK · FLG): **WAL 0 legs, OZK 0 legs, FLG 1 leg. No lookalike in the book ⇒ no TERRY packet.** KRE constituents appear only in the benign "CRE + uninsured" pair class.

**Peer bank with shared collateral, which no ratio screen finds: Preferred Bank (PFBC, cert 33539, CA, $7.7B).** WAL's verified complaint (8/18/2025, via WAL research §6 O6) puts PFBC as the larger senior deed-of-trust holder on WAL's pleaded Cantor collateral, with DOT face amounts $10.4M, $50.4M, $25.9M, $22.4M. Nano also held 4 senior DOTs there ($28.04M face). American Banker (6/11/2026, **SECONDARY**) puts PFBC's Makhijani-linked nonaccrual at $115M. **Call Report (FDIC API, primary):** PFBC noncurrent **$51M [12/25] → $169M = 2.76% [3/26] → $98M = 1.57% [6/26]**; ALLL $76M; leverage 10.6%; H1-26 net income $64.7M. **Read: the exposure is real and visible in PFBC's own Q1 filing, and PFBC's earnings and capital absorb it (H1 earnings ≈ 0.56× the $115M; reserves ≈ 0.78× noncurrent).** It is a **mark-contagion** channel, not a solvency one: an FDIC sale of Nano's liens on shared properties would print a mark on PFBC's collateral. PFBC meets only the benign pair (CRE 357% + uninsured 50%). **Not in Will's book** except as a possible KRE constituent (membership not verified) ⇒ no TERRY packet.

⚠️ **What this screen cannot see, and it is what killed Nano:** founder fraud, litigation liability, and CRE-finance booked in C&I (MI3). A four-ratio screen found Nano only because Nano was already at 26% noncurrent. **As an early warning at 12/31/2023 it would have scored Nano at 1 leg (CRE 295%, just under 300; NC 4.5%; EQ 13%; uninsured 54% per RCON5597 $406.4M ÷ $750.6M). It was a lagging screen here.** The two leading markers were the reserve-coverage collapse (§2c) and the MI3 share (§2d); both are unscreened nationally.

---

## 5. Contagion to the syndicate exposures

**What receivership does to claims AGAINST Nano (FIRREA).** The FDIC-receiver succeeds to all of Nano's rights and liabilities (12 U.S.C. §1821(d)(2)(A)). Every claim must be filed administratively by the bar date, including suits and awards already pending, or it is lost (§1821(d)(5)(C), (d)(6), (d)(13)(D)). **The bar date is not published as of 9/27.** It must be at least 90 days after first notice (§1821(d)(3)(B)(i)), so an estimate is **late Dec 2026 to early Jan 2027**. Pending suits face a stay of up to 90 days and FDIC substitution or removal (§1821(d)(12), §1819(b)(2)(B)). Side agreements are barred unless they meet §1823(e). Depositor preference (§1821(d)(11)) puts general unsecured claims **behind a depositor class that is itself expected to lose ~$114M**. ⇒ **Claims against Nano are worth ≈ $0.** That covers Honarkar's JAMS award (conspiracy/aiding-abetting; interim 2/21/2025, partial final 5/23/2025; **no confirmed dollar judgment found**) and Marcil's suit over Nano's $19M and $8.5M loans (C.D. Cal. 8:26-cv-01143). The 9/22 books carried only $8.4M of other liabilities (DEWEY), so no award was booked as a liability. **Sunwest takes no borrower-litigation liability** on the FDIC's standard P&A terms (§2.5); the Nano P&A is not yet posted, so **re-check it when it is.**

**Does it change WAL's or ZION's Stupin recoveries? Only at the margin.** Neither bank's recovery runs through a claim against Nano.
- **WAL (the WAL desk owns this leg; figures are its own):** Cantor Group V $98.5M; $26.1M charged off Q1-26, nothing further Q2 (10-Q, via legal leg). Claims run against the guarantors (a §523 complaint against the Stupins was filed 9/15/2026 in their Ch. 11, 8:26-bk-11202, filed 4/17/2026) and the collateral.
- **ZION:** $50M charged off Q3-25; guarantor suit removed into the Stupin Ch. 11 (5/7/2026); no recovery disclosed through the Q2-26 10-Q. **ZION never names Cantor or Stupin in any filing**; that link is SECONDARY (Reuters/CNBC 10/2025).
- **BANC / EFSC:** ⛔ **the "$108M combined" in `ML-REG-039` is mis-transcribed.** Reuters (10/20/2025, SECONDARY) sums **three** lenders, BANC + Enterprise Bank & Trust **+ Nano Banc**. Neither BANC nor EFSC discloses the exposure in any SEC filing (EDGAR full-text search, 6/2025 → 9/27/2026). No primary splits it by bank.
- **Where Nano does matter** is as a **competing lienholder**. Its liens (the Marcil loans, ~$20M on MOM assets, 901 Ocean) keep their priority under the receiver or a loan buyer. A liquidation-minded receiver may sell the ~$215M retained pool faster or cheaper, which is a **mark** on shared collateral: WAL's junior positions, and **PFBC's senior ones** (§4). That is CREED's S6 forced-sale print.
- **The recovery drivers are unchanged:** the Stupin estate (no plan on file as of 9/26), collateral realizations, and Makhijani's criminal case (14-count indictment 6/17/2026, trial **2027-01-12**).
- **PROME premise correction:** MOM CA Investco's Ch. 11 (D. Del. 25-10321) was **dismissed 8/18/2025** and closed 10/20/2025, so it is not a live venue. "$382M" was the debtors' undistressed property value, not debt (WAL §1 agrees).

**No regulator or press source ties Nano's FAILURE causally to the Stupin book.** The possession order makes a capital-only finding (DEWEY), and "self-dealing" appears only in the DFPI press release. The link from Nano's syndicate loans to its losses is **inference**. What the record does show is the **2025 legal expense ($46.3M)** and a **3/6/2026 DFPI order explicitly targeting "unsecured loans to finance real estate."** Evidence and every citation: `reports/2026-09-27_nano-banc_legal-leg.md`.

---

## 6. What changes on my desk (and what does not)

| Surface | Change |
|---|---|
| `workbook/KB.tsv` | **Done:** new row `ML-REG-169` (grade + anatomy + shared figure on the 9/22 base). Resolution notes appended to `ML-REG-044` (CONFIRMED; C&D date inverted; 'liable' and 'FBI' corrected) and `ML-REG-039` ('$108M BANC+EFSC' mis-transcribed: it is three lenders incl. Nano). Original claim text is left as written; notes carry the corrections. |
| Matrix / scores | **None.** Nano was never scored (private). Matrix re-score stays 11/07. |
| Thresholds / triggers | **None fire.** A $736M failure touches no registered REG-T trigger. |
| Instrument candidates (NOT adopted; base-rate first) | (1) national MI3/C&I screen from the FFIEC bulk file; (2) national reserve-vs-nonaccrual < 50% screen. Both leading at Nano; both n=1. |
| Owed forward | Fed OIG Material Loss Review (~late Mar 2027) → grade §2d (correction vs relabel) and §3 (final DIF cost vs $114M). FDIC Q3 QBP (~late Nov) carries the failure. |

*Every figure here is primary Call Report (FFIEC CDR / FDIC API) unless labelled PROME §1 or SECONDARY. Computations reproducible from the pull script in the session scratchpad; the tables above carry the MDRMs used.*
