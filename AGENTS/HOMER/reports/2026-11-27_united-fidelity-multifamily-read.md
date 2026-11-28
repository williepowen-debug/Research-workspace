# HOMER — United Fidelity failure: is bank multifamily stress one bank or a field? (2026-11-27)

**Session:** homer-2026-11-27-8654c74a · Claude Code, Opus 5.5 (`claude-opus-5-5`) · spawned by PROME (prome-80) on WALTER card SIG-W-20261127-020 (IMMEDIATE, action HOMER) · written 2026-11-27 22:55 ET (from `date`).
**Evidence:** `reports/2026-11-27_evidence/` (scripts, their printed output, United Fidelity call-report extracts, SHA-256 of the six bulk pulls). The raw bulk files (6 × ~0.9 MB, api.fdic.gov `banks/financials`, pulled 22:48–22:49 ET, 4,284 to 4,494 banks per quarter) are not committed; the hashes and scripts reproduce them.
**Bank read is REGINALD's; Florida footprint is CORAL's.** This file is the housing/multifamily read only. It moves no band, kill test, count, grade or registered odds.

## Answer in four lines

1. **Without United Fidelity, bank multifamily credit was flat in Q3, not deteriorating.** Past due plus nonaccrual 1.405% → 1.424% (+2bp QoQ, +4.5bp YoY); nonaccrual flat (1.052 → 1.056%); 30–89 days *fell* (0.307 → 0.298%); quarterly net charge-offs fell $338M → $258M (still +19% YoY).
2. **It is one bank plus a handful, not a field, with one soft spot to watch: banks under $10B.** Large banks improved (≥$10B, 1.545 → 1.496%). Banks under $10B rose 1.027 → 1.230%, but five banks carry 68% of that bucket's 30–89-day rise, and breadth is even (161 rates up, 155 down, 410 flat among 726 banks with ≥$50M in MF).
3. **The ~31% loss estimate points at this bank's underwriting and related-party assets more than at a market-wide fall in apartment values** (INFERRED; arithmetic §2). Getting to that loss from the market alone needs roughly twice the apartment price decline the fleet holds.
4. **Forward:** the Q4 industry headline will probably *improve mechanically* when United Fidelity's $2.14B of nonaccruals leave the reporting population. That improvement would not be credit getting better. The ex-bank series is the one to read.

## Claim table

| # | Claim | Source | Date | State |
|---|---|---|---|---|
| 1 | Closed by OCC; FDIC receiver; First-Citizens assumes substantially all deposits and buys substantially all assets; $5.9B assets, $5.4B deposits at 9/30; DIF cost $1.83B; 22 branches IN, IL, FL, CO, USVI | FDIC press release (fdic.gov/news/press-releases/2026/first-citizens-bank-trust-company-raleigh-north-carolina-assumes), read by HOMER | 2026-11-27 | VERIFIED |
| 2 | Release states no loss-share, no retained-asset list, no purchase price | same release | 2026-11-27 | VERIFIED (absence on that page only) |
| 3 | DIF cost / assets = 30.9% ($1.83B / $5,915.5M) | release + call report | 9/30 | VERIFIED (arithmetic) |
| 4 | UF 9/30: MF loans $2,721.6M of $3,059.4M gross loans (89%); MF nonaccrual $2,143.2M (79% of its MF book); allowance $6.3M (was $81.7M); equity $389.7M (was $652.5M); 2026 MF net charge-offs $362.5M; securities $1,359.3M, HTM fair value $92.8M under cost | api.fdic.gov financials cert 29566 | 9/30 | VERIFIED |
| 5 | Industry MF past due + nonaccrual 1.735% Q3, 1.398% Q2 (QBP prints 1.742 / 1.404) | HOMER sum, api.fdic.gov, 4,284 banks | 9/30 | VERIFIED (reproduces QBP within 1bp) |
| 6 | Ex-UF table in §1 | same pull, HOMER sum | 9/30/25 to 9/30/26 | VERIFIED (HOMER arithmetic) |
| 7 | "UF ≈ 90% of the Q3 MF past-due rise" | HOMER's figure is ~89%: REGINALD's computation (UF nonaccrual +$2,143M over the industry's ~$2.4B PDNA rise), confirmed by HOMER at api.fdic.gov 11/25; lives in `workbook/MULTIFAMILY.tsv` rows 130–131 and `NEXUS_BRIEF.md`, **not STATUS** | 11/25 | VERIFIED; re-run tonight: 2,143 / 2,389 = 90% (aggregate) or 86% (same-bank panel, 2,143 / 2,498) |
| 8 | "Bank MF charge-offs ex-UF +21% to $784M" | HOMER sum (`MULTIFAMILY.tsv` row 138); **nine months 2026 vs nine months 2025**, not Q3; Q3 alone is $258M (+19% YoY, −24% QoQ) | 9/30 | VERIFIED; WALTER's card drops the period |
| 9 | Five banks = 68% of the <$10B ex-UF MF 30–89 rise (Preferred, BankPlus, American Momentum, MainStreet, CFG) | HOMER sum | 9/30 | VERIFIED (arithmetic) |
| 10 | UF book: 256 MF loans 2021–25, $4.176B, all retained, 117 first and 139 second liens; borrowers tie to two related sponsor groups (46% of dollars matched); debt 85% of the bank's own origination values, 1.54× county values on 23 matched rows | PROME SYNTHESIS 2026-11-11 (HMDA recomputed by PROME; the rest researcher and report reads) | 11/11 | RELAYED, not re-read |
| 11 | $1.032B real-estate venture investments + $146.7M related-party development-fee receivable on UF's balance sheet | PROME SYNTHESIS (researcher's read of the 9/30 filing) | 9/30 | RELAYED; the ~$1.39B of "other assets" in the call report is consistent (INFERRED) |
| 12 | Loss arithmetic in §2 (scenarios A to C) | HOMER | — | INFERRED |
| 13 | Q4 headline falls mechanically when UF leaves the population | reporting mechanics; First Citizens' treatment of bought loans (fair value, purchased-credit-deteriorated) not read | — | INFERRED |
| 14 | HUD partial claims did not end; permanent home-retention options limited to once per 24 months from 2025-10-01, disaster areas excepted | HUD Loss Mitigation Options Q&A PDF (page footer dated /18/2025), text extracted by HOMER | 2025-09 | VERIFIED (DEWEY's correction confirmed) |

## 1. Bank multifamily credit with United Fidelity removed

All insured banks, multifamily (5+ unit) real-estate loans, $ millions; rates as % of MF loans. Source api.fdic.gov call-report fields LNREMULT, P3REMULT, P9REMULT, NAREMULT, NTREMULT (year-to-date, so quarters are differenced). Pulled 2026-11-27 22:48–22:49 ET.

| Ex-United-Fidelity | Q3-25 | Q4-25 | Q1-26 | Q2-26 | **Q3-26** | Q3 vs Q2 | Q3 vs Q3-25 |
|---|---|---|---|---|---|---|---|
| MF loans | 650,847 | 659,150 | 665,088 | 667,281 | **675,442** | +1.2% | +3.8% |
| 30–89 days past due | 0.284% | 0.403% | 0.409% | 0.307% | **0.298%** | −0.9bp | +1.4bp |
| 90+ days (still accruing) | $403 | $309 | $353 | $307 | **$480** | +$173 | +$77 |
| Nonaccrual | 1.033% | 0.996% | 1.018% | 1.052% | **1.056%** | +0.4bp | +2.3bp |
| **Past due + nonaccrual** | 1.379% | 1.446% | 1.479% | 1.405% | **1.424%** | **+1.9bp** | **+4.5bp** |
| Net charge-offs in the quarter | $217 | $184 | $189 | $338 | **$258** | −24% | +19% |
| Same, annualized rate | 0.13% | 0.11% | 0.11% | 0.20% | **0.15%** | | |
| *Including UF: past due + nonaccrual* | *1.372%* | *1.439%* | *1.472%* | *1.398%* | ***1.735%*** | *+34bp* | *+36bp* |

**Splits (ex-UF, past due + nonaccrual):**

| Cut | Q3-25 | Q2-26 | Q3-26 | Read |
|---|---|---|---|---|
| Banks ≥$10B assets ($494B MF) | 1.596% | 1.545% | **1.496%** | improving; 30–89 0.320 → 0.240% |
| Banks <$10B ($182B MF) | 0.820% | 1.027% | **1.230%** | rising: +20bp QoQ, +41bp YoY; 30–89 0.272 → 0.454% |
| Ex-UF ex-Flagstar ($649B) | 0.964% | 1.089% | **1.086%** | flat QoQ, +12bp YoY |

**Concentration and breadth (same-bank panel, Q2 → Q3):**
- Ex-UF net change +$355M = $1,722M of increases less $1,367M of decreases. The five largest increases (Wells Fargo +$203M, Flagstar +$164M, Santander +$146M, Preferred Bank +$133M, NexBank +$52M) sum to $697M. Without them the rest *fell* $342M. JPMorgan (−$145M) and KeyBank (−$115M) led the falls.
- Banks <$10B: the 30–89-day rise was +$343M, of which $234M (68%) came from five banks: Preferred +$80M, BankPlus +$45M, American Momentum +$40M, MainStreet +$34M, CFG +$34M. The rest was +$109M. Nonaccrual in the bucket rose only +$78M net; the five largest rose +$151M and the rest fell.
- Breadth: among 579 ex-UF banks with ≥$100M of MF loans, 170 rates rose, 173 fell and 236 were flat QoQ. Year over year 203 rose and 150 fell, a mild tilt toward worse.

**Read:** multifamily stress at banks in Q3 was **one bank (United Fidelity) plus a handful of names**, not a field. The year-over-year drift (+4.5bp ex-UF, +12bp ex-UF-ex-Flagstar) is slow. The only segment moving the wrong way at speed is **community banks (<$10B)**. Their rise is in the 30–89-day bucket, the early, noisy stage, and is concentrated in five banks. Preferred Bank was already a member of HOMER's combination watch KB-HOMER-043, where REGINALD read it as real but contained.

## 2. What a ~31% loss on a multifamily-heavy lender implies, and what it does not

**Balance sheet at 9/30 (call report, $M):** assets 5,915.5 = cash 109.2 + securities 1,359.3 + net loans 3,053.1 (MF 2,721.6) + other ~1,393.9. Liabilities: deposits 5,369.7, other borrowings 50.1, other ~106. Equity 389.7.

**What the FDIC's estimate implies (INFERRED; the estimate is preliminary and its make-up is not published):** First Citizens took all deposits, so the Deposit Insurance Fund covers the gap between liabilities paid and what the assets realize. Assets would have to realize about $5,526M − $1,830M ≈ **$3,696M**, which is **~$2.2B, or 37.5%, below the 9/30 book value**. Q4 operating losses (net interest income has been negative since 2023, per the synthesis) and resolution costs would make the asset write-down somewhat smaller than this.

| Where the ~$2.2B could sit (INFERRED) | Scenario A | Scenario B | Scenario C |
|---|---|---|---|
| Held-to-maturity securities, marked to fair value | −$93M | −$93M | −$93M |
| Related-party real-estate ventures + fee receivable (~$1.18B, RELAYED) | written to 0 | 50% | 0% loss |
| Implied write-down left for the loan book ($3,053M) | ~$950M (31%) | ~$1,540M (50%) | ~$2,130M (70%) |
| **MF loss including the Q3 charge-off, % of the 6/30 MF book ($3,089M)** | **~42%** | **~61%** | **~81%** |

**What the arithmetic implies:**
- **Even in the most benign split (A), the multifamily loans lose about 40% or more.** On loans written at about 85% of the bank's own appraised values, a 40%+ loss means realizable values roughly 45–50% below those origination appraisals once sale costs and the bulk-buyer discount are counted (INFERRED).
- **The market move the fleet holds is about half that.** It is the Green Street apartment index, 19–22% below its 2022 peak (RELAYED: search snippets, PROME synthesis). The 1.54× debt-to-county-value marker on 23 matched loans (RELAYED) fits the larger gap.
- **The likely reading (INFERRED, medium confidence): the loss mostly measures this book.** It points to origination values set by a bank that was also developer, owner and fee-earner; stacked first and second liens (139 of 256 loans were second liens); interest-only balloons from 2021–23 at 2.78–3.35% coupons; and related-party equity-like assets. It does not mainly measure a fall in apartment collateral everywhere.

**What it does NOT establish:**
- Market apartment values or cap rates. No appraisal, sale price or First Citizens bid is public, and the FDIC estimate is preliminary.
- How the $1.83B splits across loans, ventures, securities and the deposit franchise, or which assets (if any) the FDIC kept. The release names neither a loss-share nor a retained-asset list.
- Losses at any other lender. Section 1 says the rest of the bank book was flat in Q3.
- Transmission. The fleet's 11/11 read stands: an in-house concentration with related sponsors, and containment **not established**. 53.6% of UF's origination dollars were never matched to a sponsor (SYNTHESIS).
- Fraud or misconduct. Nothing read says so, and HOMER does not infer it.

## 3. Read-through to HOMER's rows, gates and theses (observations only; nothing graded)

| Row / thesis | Effect | Action |
|---|---|---|
| Thesis C2 (CMBS + GSE multifamily realization) | Bank-held MF is a third book and never grades C2. The C2 count stays 0/3 and 0/3; the formal grade is 2027-02-20 | none |
| Thesis §1 paragraph ("building and converting; early, not settled" for bank MF) | Supported. The failure converts one bank's stress into a realized loss, and the ex-bank series is flat | wording unchanged |
| HOM-05 (Trepp Nov MF DQ <8.09%) · HOM-11 (Freddie MF Nov ≥0.62%) | Different books; no mechanical link. Odds frozen | none |
| Freddie/Fannie MF bands (RED / AT ORANGE) | Unaffected | none |
| Rent-decline breadth (39/100 Oct) | UF's book is affordable housing to related sponsors, not a market-rent read | none |
| KB-HOMER-043 combination watch ("MF lateness spreading to bank lenders?") | New member: ex-UF the bank book is flat, but community-bank 30–89 rose, concentrated in five banks; Preferred again | logged 11/27 (KB_LIVE) |
| Agency lending channel | No read-through. UF's loans were bank-retained, not agency | none |
| Supply | Nothing new; Q3 residential investment multifamily ≈ 0 (BEA, held 11/25) | none |

## 4. Forward view (Will 11/19); unscored, no row registered

**Horizon:** to about 2027-02-28. That covers Q4 call reports (due 2027-01-30), the Q4 FDIC Quarterly Banking Profile (~late February) and the mid-January Q4 earnings of public names (Preferred PFBC, Flagstar, Valley, EagleBank, MainStreet).

| Outcome for the ex-UF bank MF past-due + nonaccrual rate at Q4 (vs 1.424%) | HOMER odds |
|---|---|
| Flat, within ±10bp | **65%** |
| Rises more than 10bp | 25% |
| Falls more than 10bp | 10% |

- **Why flat is the base case.** Large banks are improving; the leading 30–89-day stage fell in aggregate; quarterly charge-offs fell; and the year-over-year drift is ~1bp a quarter. Mortgage rates at 7.21% (PMMS 11/25) keep refinancing pressure on balloon loans, which is why the upside tail is fatter than the downside.
- **The meaningful alternative (25%).** The community-bank 30–89 rise (0.454%) migrates to nonaccrual in Q4. Three of five past Preferred episodes migrated (KB-HOMER-043). For a field reading, the Q4 rise would also have to be spread across more than ten banks rather than five.
- **The headline trap.** The *including-UF* industry rate will probably fall back toward ~1.4–1.5% in Q4 because UF's $2.14B leaves the population. Odds about 80%; the 20% is First Citizens reporting the bought loans as nonaccrual or past due. **A Q4 headline improvement is mechanical, not credit**, and should be reported against the ex-UF series.
- **What would change my mind:**
  - toward "field": ex-UF Q4 above 1.55% with the rise spread across many banks; a second bank failure or enforcement order tied to multifamily; or First Citizens disclosing marks on the bought MF book far below par for first liens.
  - toward "healing": community-bank 30–89 back under 0.30% with no migration.

## 5. Tradeability

A facts packet goes to TERRY (`AGENTS/TERRY/inbox/2026-11-27_from-HOMER_united-fidelity-ex-bank-mf-facts.md`). **The finding is material as a negative:** it lowers the odds that bank multifamily stress is broad. TERRY already read the failure NO CARD (b521f8025b). This adds the ex-bank table and names the five community banks whose early lateness rose. HOMER constructs no trade.

## 6. Inbox drain (all eight, every sender)

| Item | Disposition |
|---|---|
| WALTER SIG-W-20261127-020 (ACTION) | This report; attribution correction to WALTER by packet |
| WALTER SIG-W-20261125-043 (NYC rent-freeze ruling, titles only) | INFO-LOGGED: FLG's rent-regulated book; no HOMER row moved |
| WALTER SIG-W-20261126-001, -20261127-003, -20261127-017 (St. Johns flood gauges) | INFO-LOGGED: CORAL/AEOLUS own the read; Volusia and Seminole are already on HOMER's ZHVI flood baseline (KB-HOMER-048); forecasts, not losses; no HOMER row moved |
| DEWEY 11/26 partial-claims correction | APPLIED: correction row appended to `workbook/PIPELINE.tsv` (HUD Q&A verified by HOMER); KB-CARL-014 is CARL's file, not edited |
| DEWEY 11/26 edgar_doc interface stable | Noted; no action (filing_reader's control stays the hand-reading `check`) |
| LABOR 11/26 construction jobs record-only | Noted; LABOR's three figures match HOMER's 11/25 row exactly |
