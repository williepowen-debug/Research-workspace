# WQ-318 — Funding vs non-bank exposure: six-bank baseline (6/30/26) + pre-committed Q3 observation list

**Written:** 2026-10-07 Wed, ~21:5x–22:3x ET (window from `date`), REGINALD, PROME-spawned DOCKET L527 session (Opus).
**Authority:** WQ-318, Will APPROVED 2026-09-28 14:1x ET with riders (verbatim in `inbox/processed/2026-09-28_from-PROME_WQ-318-funding-vs-nonbank-baseline.md`). Delivered **2 days before the 10/09 deadline; 2 days after the 10/05 wake date.**
**Question (CATO, 17b4977fd):** which regional banks could lose cheap deposits just as customers and funds draw more credit?
**Bounds:** existing public disclosures + fleet evidence only. **No score, threshold, ladder level or trade moved.** The Q3 classification lines in Deliverable 2 are lines for THIS observation list only — they are not registered triggers and nothing routes on them. Q3 is allowed to remain inconclusive (Will).

**Sources (all pulled 2026-10-07 unless noted):**
- **[CR]** FFIEC Call Reports, bank level, 6 banks × 5 quarters (6/30/25 → 6/30/26), CDR REST/JWT SDF → `workbook/FUNDING_COHORT_2026Q2.tsv`, written by `scripts/wq318_funding_baseline.py` (formulas and MDRMs in its docstring). **One basis for all six — this is the comparable column set.**
- **[NDFI]** `workbook/NDFI_COHORT.tsv` [FFIEC 6/30/26, pulled 8/20] — RC-C item 9.a + Memo 10 a–e, unfunded, nonaccrual / 30–89 / 90+.
- **[10Q]/[ER]** each holding company's Q2-26 10-Q (Item 3 / MD&A rate risk) and Q2 earnings release / deck (EX-99) — accessions in §1g and §1a. OZK files with the FDIC, not the SEC (Q2 10-Q PDF at `AGENTS/OZK/raw/`). Extraction by five read-only Opus sub-readers (scratch notes, not repo files); every figure below that I relied on for a classification line was cross-checked against [CR] where [CR] carries the same concept (deposit cost: §1a).
- Fleet: WAL packets 9/28 (KB-WAL-212, A1) · BROCK packets 10/02 (KB-BRK-314) · HOMER 9/29 (UWM) · WALTER SIG-W-20260928-004 (Slok), -20261007-008/012 (NYFed visits), -20261007-009 (G.19) · my 9/29 attribution report.

⚠️ **Bank-level Call Report ≠ holding-company 10-Q.** Where both bases exist they are labelled; they are never merged in one cell.

---

## The answer first

1. **The two exposures sit in different banks, and only one name carries both at 6/30: CUBI.** The non-bank draw side is concentrated at **CUBI** (NDFI 34.1% of loans; private-credit slice 19.96%) and **CFG** (14.7% / 10.66%), then OZK and WAL. The deposit-fragility side points at **EGBN** (brokered 32% of deposits), **CUBI** (brokered 21%, uninsured 44%, highest interest-bearing deposit cost of the six at 3.54%, FHLB advances up 72% in a year) and **WAL** (brokered 19%, uninsured 38%). **CUBI is the one bank high on both.** It is also the one with the smallest deposit base of the four NDFI names.
2. **The collision CATO asked about has not started at 6/30.** At all six banks the share of deposits that pay no interest was **flat (within 0.5pp) or up year on year**, and interest-bearing deposit costs **fell 27–52bp over four quarters**. CFG is the only one whose deposit cost rose in Q2 (+4bp, "positioned for Fed moves" — SECONDARY). Nothing in the June baseline shows cheap-deposit flight.
3. **The draw side has room to grow where unfunded lines are large.** Unfunded NDFI commitments equal **~100% of drawn balances at CFG ($22.5B) and OZK ($3.3B)** and 59% at CUBI. Measured against deposits, CUBI's unfunded NDFI is **16.6%** of deposits, CFG's 11.9%, OZK's 9.6%, WAL's 5.9%. This is a derived ratio, not a forecast: a draw needs a reason, and none is observed.
4. **Every bank's own model says net interest income RISES with rates** (+100bp: WAL +5.9%, OZK +4.2%, EGBN +4.1%, CUBI +2.3%, CFG +0.9 to +1.3%, FLG +0.8%). **The figures are not comparable.** They mix static and dynamic balance sheets, shocks and ramps, and different base curves, and four of six state no deposit beta. One figure cuts the other way: **FLG's short-rate-only scenario has NII FALLING 0.24% per +100bp.** The 9/16 hike was a short-end move.
5. **August's negative result stands as counter-evidence.** The 8/14+ selloff **did not sort** on this desk's private-credit NDFI proxy. A −0.559 rank correlation at n=14 collapsed to −0.255 when the sample was extended to n=26 (8/20). The 9/15→9/29 leg sorted on **size** (ρ −0.72), not on NDFI (ρ −0.33, not distinguishable from zero at n=14). **The market has not priced this channel. That is consistent with it being absent, and also with it being unseen.**

---

## Deliverable 1 — the six-bank baseline (6/30/26 common date; later disclosures separate)

### 1a. Deposit cost — interest-bearing deposits, four quarters (column 1)

| Bank | Q3-25 | Q4-25 | Q1-26 | **Q2-26** | 4-qtr Δ | Company source | [CR] RC-K basis Q2 | [CR] agrees? |
|---|---|---|---|---|---|---|---|---|
| **CUBI** | 4.04% | 3.73% | 3.55% | **3.54%** | −50bp | EX-99.1 avg-balance fn (4), acc 0001488813-26-000082 / -26-000012 | 3.55% | Q1-26 on; **2025 NO** (RC-K average 1.34× period-end IB → 2025 RC-K is INCOMPARABLE) |
| **CFG** | 2.35% | 2.20% | 2.04% | **2.08%** | −27bp | Q2 financial supplement EX-99.3 p.7; Q3/Q4-25 supplements | 2.10% | YES (±2bp) |
| **WAL** | — | — | 2.75% | **2.74%** | — | KB-WAL-102/-122 (Q1 release / Q2 call) | 2.73% (Q3-25 3.18 · Q4 2.96 · Q1 2.74) | YES (±1bp); **4-qtr trajectory from [CR]: −45bp** |
| **OZK** | 3.64% | 3.47% | 3.29% | **3.24%** | −40bp | mgmt comments p.8; Q2 8-K bundle p.13 | 2.90% | **NO** — RC-K average runs ~1.1× period-end IB; [CR] cost INCOMPARABLE |
| **FLG** | 3.60% | 3.34% | 3.13% | **3.08%** | −52bp | EX-99.1 avg-balance tables, acc 0000910073-26-000065 etc. | 3.05% | YES (±3bp) |
| **EGBN** | 3.80% | 3.62% | 3.42% | **3.37%** | −43bp | EX-99.1 avg-balance, acc 0001050441-26-000088 p.9 | 2.75% | **NO** — RC-K average runs ~1.33× period-end IB in every quarter; [CR] cost INCOMPARABLE |

**Read:** all six fell over four quarters; only **CFG rose in Q2** (+4bp). **The company figure is column 1's value.** The [CR] cross-check holds at three banks and fails at three. At CUBI, OZK and EGBN, the RC-K quarterly average sits far above the period-end interest-bearing balance. **The cause is UNRESOLVED.** It could be a reporting-definition gap or intra-quarter balance swings, and I did not chase it. The [CR] cost column is used for nothing at those three banks.
**Total deposit cost (incl. NIB), Q2:** CUBI 2.50% · CFG 1.63% · WAL 1.78% (avg) · OZK 2.86% (rate on all deposits) · FLG NOT STATED · EGBN 2.72%.

### 1b. Deposit mix — NIB share, uninsured, brokered (column 2) — [CR] basis, 6/30/26 (Δ vs 6/30/25)

| Bank | NIB share of deposits | Uninsured (RC-O M2 ÷ domestic deposits) | Brokered (RC-E M1b ÷ deposits) | Reciprocal (RC-E M1g) | Company-basis notes |
|---|---|---|---|---|---|
| **CUBI** | **32.2%** (29.2%) | **44.3%** (38.9%) ↑ | **21.1%** (32.9%) ↓ | $2.34B | 10-Q: uninsured $9.7B; release: $7.6B / 35% after FHLB letters of credit + affiliates; brokered $ NOT DISCLOSED; **digital-asset ("DA") vertical spot balances $3.8B** (deck s11): **concentrated, the likely-volatile part of NIB** |
| **CFG** | 23.2% (23.3%) | **47.5%** (44.4%) ↑ | 2.6% (3.0%) | $8.92B | Company: NIB 22%; uninsured $89.6B gross / $70.1B adjusted; insured+secured 62% |
| **WAL** | **33.8%** (32.2%) | 38.1% (28.9%) ↑ | 18.8% (26.4%) ↓ | **$15.16B** | ⚠️ much of WAL's NIB is **ECR-bearing mortgage-warehouse deposits** — model beta **70%** (KB-WAL-212): **"non-interest-bearing" is not "cheap" here** |
| **OZK** | **11.6%** (11.4%) — lowest | 32.5% (37.1%) ↓ | 7.4% (8.5%) | $0.52B | Company: public funds $4.11B (12.1%), collateralized 13%; uninsured $11.04B |
| **FLG** | 17.4% (17.8%) | 28.9% (23.5%) ↑ | 9.7% (15.3%) ↓ | $4.39B | Company: "uninsured or not collateralized" $14.5B = 21%; **brokered CDs $2.1–2.2B (three figures in one filing)** vs [CR] total brokered $6.53B: different bases |
| **EGBN** | 19.3% (16.8%) | 27.7% (24.9%) | **31.9%** (37.9%) — highest | $1.42B | Company matches [CR]: brokered $2.6B / 32%; ten largest depositors ~17%; one large payments-processor relationship |

**Read:** **NIB share flat (within 0.5pp: CFG −0.1, FLG −0.5) or up at all six** (no cheap-deposit flight through 6/30). **Uninsured share rose at five of six** (all but OZK); **brokered share fell at all six**. The run-prone share grew while the market-funded share shrank.

### 1c. Wholesale borrowing (column 3) — [CR] RC-M 5 / RC 14, ÷ total liabilities (RC 21), 6/30/26

| Bank | FHLB advances | Other borrowed money total (RC-M 5.c, incl. FHLB) + FF/repo | ÷ liabilities | FHLB Δ QoQ | FHLB Δ 4Q |
|---|---|---|---|---|---|
| CUBI | $2.06B | $2.06B | **8.5%** (5.8% a year ago) | **+$0.50B** | +$0.86B (+72%) |
| CFG | $6.36B | $11.51B | 5.6% (4.0%) | **+$3.85B** (2.51 → 6.36) | +$4.82B |
| WAL | $5.80B | $6.52B | 7.2% (8.1%) | +$0.60B | +$0.20B |
| OZK | **$0** | $0 | **0.0%** (2.3%) | −$0.20B | −$0.80B |
| FLG | $9.90B | $10.49B | **13.2%** (14.5%) — highest | −$0.25B | −$2.25B |
| EGBN | $0.10B (paid off 7/7/26 per 10-Q note 8) | $0.10B | 1.2% (0.8%) | +$0.10B | +$0.05B |

**REG-T-06 decomposition (cite, not re-derive):** system FHLB advances **$810.7B [6/30, FHLB Office of Finance]**, leg 2 of 3. These six banks hold **$24.2B (~3.0%)**. Their net Q2 change is **+$4.6B** against system growth of +$76.7B ($734B → $810.7B): **~6% of the growth**, most of it CFG. **The FHLB build is not happening in this six-bank set.** OZK's $3.97B of FHLB *letters of credit* collateralize public funds; they are not advances and are not in this column.

### 1d. NDFI — drawn, unfunded, private-credit slice (column 4) — [NDFI], FFIEC 6/30/26

| Bank | NDFI drawn (9.a) | % loans | Private-credit slice (M10b+M10c) | M10a mortgage-credit intermediaries | Unfunded NDFI | Unfunded ÷ drawn | Unfunded ÷ deposits (DERIVED) |
|---|---|---|---|---|---|---|---|
| **CUBI** | $6.14B | **34.1%** | **$3.60B = 19.96%** | $2.47B | $3.62B | 59% | **16.6%** |
| **CFG** | $21.99B | 14.7% | $15.91B = 10.66% | $0.30B | **$22.48B** | **102%** | 11.9% |
| **OZK** | $3.26B | 10.0% | $2.79B = 8.58% | 0 | $3.25B | **100%** | 9.6% |
| **WAL** | $15.81B | 24.1% | $4.92B = 7.50% | **$10.90B (shown separately — mortgage warehouse, not private credit)** | $4.88B | 31% | 5.9% |
| FLG *(CRE contrast)* | $3.46B | 5.7% | $1.07B = 1.75% | $1.11B | $1.30B | 38% | 1.9% |
| EGBN *(CRE contrast)* | $0.09B | 1.4% | 0 | $0.09B | $0.08B | 85% | 0.9% |

Company-basis cross-reads (not merged): **CFG** 10-Q Table 9: capital-call $9,852M, secured private-credit finance $4,875M, other finance & insurance $5,615M; deck s25 "$22B NDFI" (preliminary). **WAL** 10-Q NDFI $15,812M = **25.9% of HFI** (10-Q basis) vs 24.1% of total loans (FFIEC basis); the deck's "Mortgage Warehouse & MSR" $7.155B is a different measure. **OZK** 10-Q: NDFI funded $3.26B; debt-on-debt $0.43B (Q1: inside NDFI); C&IB chart Fund Finance $1,197M + Lender Finance $873M. **CUBI**: fund finance sits inside "Specialized lending" $7.65B, balance NOT DISCLOSED; mortgage finance $1.73B, unfunded $1.55B. **FLG**: mortgage finance $940M (deck s6); NDFI book NOT DISCLOSED.

### 1e. Collateral protection (column 5)

| Bank | Disclosed | Not disclosed |
|---|---|---|
| CUBI | Lender finance: "secured by diverse collateral pools to private debt funds"; capital call: "collateral pools and limited partnership commitments"; mortgage finance under master repurchase agreements, avg life <30 days, all current, no allowance (10-Q pp.11, 72, 75) | LTV, advance rates, NAV vs subscription split, recourse → **UNAVAILABLE** |
| CFG | Capital call: "backed by uncalled capital commitments from LPs… advance rates in borrowing base determined by credit of LPs", revolving, mostly <1-year; private credit: "senior loans to middle-market credit funds secured by pool of leveraged loans… ability to remark loans… reducing the effective advance rate" (deck s25) | numeric advance rates / LTV / NAV split → **UNAVAILABLE** |
| WAL | Warehouse: management narrative "losses near zero" only | **UNAVAILABLE** |
| OZK | "underwrite… based on the fundamentals of the underlying collateral" | **UNAVAILABLE** |
| FLG | — | **UNAVAILABLE** (no NDFI book disclosed) |
| EGBN | — | **N/A** (no NDFI book; Call Report 9.a = $92M M10a only) |

### 1f. Observed deterioration (column 6)

| Bank | NDFI nonaccrual / 30–89 / 90+ [NDFI 6/30] | Q2 disclosure of criticized NDFI |
|---|---|---|
| CUBI | 0 / 0 / 0 | NOT DISCLOSED by book (C&I-wide: SM $17.6M, SS $131.5M, nonaccrual $22.8M) |
| CFG | $0.13M / 0 / 0 | NOT DISCLOSED by book (C&I criticized $2.2B, commercial-wide) |
| **WAL** | **$122.5M (0.77% of NDFI)** / 0 / 0 | WAL First Brands receivables-financing charge-off $126.4M H1-26 (BROCK; borrower a finance company, not a PC fund) |
| **OZK** | **$25.9M** / 0 / 0 | "Other" category: substandard nonaccrual $25.9M; H1 net charge-offs $43.6M (2.88% annualized). The "two names" attribution (Seattle office $27.7M + San Carlos $14.8M) is **INFERRED from matching amounts**; no primary states it |
| FLG | $0.05M / $13.2M / 0 | NOT DISCLOSED |
| EGBN | 0 / 0 / 0 | N/A |

### 1g. Rate sensitivity — each figure WITH its stated assumptions (column 7). ⛔ INCOMPARABLE across banks; not netted into a label (Will: inputs, not verdicts)

| Bank | NII % change, 12 months (6/30/26) | EVE % | Stated assumptions | Prior vintage |
|---|---|---|---|---|
| **WAL** (10-Q acc 0001628280-26-051418 pp.88-89; KB-WAL-212) | Parallel: −200 (8.6) · −100 (5.2) · +100 **+5.9** · +200 +11.8. Ramp: (5.1) · (2.7) · +3.2 · +6.3 | +4.4 · +2.7 · (4.4) · (10.5) | **Dynamic** balance sheet; 12-month; forward-curve base; non-term deposit beta 45–86%, **avg 53%**; ECR-eligible beta **70%**; all NMD incl. ECR **59%** | 3/31: parallel (7.1)/(4.2)/+6.0/+11.6 |
| **CFG** (10-Q acc 0000759944-26-000148 Table 15 p.25) | Gradual: −200 (1.8) · −100 (0.9) · +100 **+0.9** · +200 +1.7. Instant: (4.0) · (1.6) · +1.3 · +1.8 | not disclosed numerically | 12-month; **forward-curve base**; incorporates balance-sheet mix changes (**dynamic INFERRED**, not stated); hedges included ($60.2B); **beta NOT STATED** (realized cumulative IB down-beta ~48%, deck s9) | 12/31/25 gradual +1.0/+2.0 |
| **CUBI** (10-Q acc 0001488813-26-000095 Item 3 pp.88-89) | Instant parallel: −300 (3.7) · −200 (2.0) · −100 (0.6) · +100 **+2.3** · +200 +4.3 · +300 +5.9 | +100 (3.2) · +200 (7.0) · +300 (11.1) | 12-month; instantaneous parallel on forward-implied base; **static/dynamic NOT STATED**; **beta NOT STATED** (realized cumulative IB 65% / total 58%, deck s13); model changed in 2025 | 3/31: +1.7/+3.7 |
| **OZK** (Q2 10-Q pp.53-55, FDIC) | **Ramp** over 12 months: −200 (4.1) · −100 (2.7) · +100 **+4.2** · +200 +9.0 | +100 (3.1) · +200 (7.0) · −100 +3.3 | **Dynamic** balance sheet; **base = no change in rates**; ratable 12-month ramp; **beta NOT STATED** (only "expected changes in administered rates"); 30% of variable loans at their floor | 3/31: +3.3/+7.6 |
| **FLG** (10-Q acc 0000910073-26-000068 p.15) | Instant parallel: −200 (3.9) · −100 (1.7) · +100 **+0.8** · +200 +1.4. ★ **Short-rate-only: −100 short → +0.72%; +100 short → (0.24)%** | +100 (3.6) · +200 (7.7) | **Static** balance sheet; 12-month; instantaneous parallel; base curve NOT STATED; betas NOT STATED (EVE model "incorporates… deposit decay rates and betas") | 3/31: +0.7/+1.1; short-only +100 (0.56)% |
| **EGBN** (10-Q acc 0001050441-26-000096 p.73) | Instant shock: −200 (7.6) · −100 (3.7) · +100 **+4.1** · +200 +8.2 | +100 (2.3) · +200 (4.3) | **Static** ("no change in deposit portfolio size or mix"); 12-month; parallel, floored at 0; base NOT STATED; IB deposit rates move less than market, floor 0, **some deposits contractually 100% beta**; numeric beta NOT STATED; **model updated Q1-26** (deposit duration 22 → 13 months), so QoQ moves are partly methodology | 3/31: +3.2/+6.4 |

**What can be said without netting:** each bank's own model has NII rising in a parallel up-shock. **The 9/16 hike (+25bp) was a short-end move, and only FLG publishes a short-rate-only scenario. That scenario has the opposite sign.** WAL's model rests on deposit betas of 53–70%. If actual betas run hotter, the +5.9% shrinks. That is the observable to read at Q3 (§2). EVE falls in up-shocks at all five that disclose it, so the capital channel runs the other way from NII (cf. `reports/2026-09-24_cohort_AOCI_exposure.md`).

### 1h. Already-available LATER disclosures, post-6/30 — SEPARATE column (column 8), never merged into 1a–1g

| Bank | Disclosure | Date | Tier |
|---|---|---|---|
| CUBI | Q2 release: FY26 guidance reaffirmed (NII $800–830M; deposit and loan growth 8–12% each); "low-cost deposit… pipelines expected to drive margin expansion" | 7/23 | P |
| CUBI | 2.875% senior notes reset to 3M SOFR + 235bp from 8/15 | 10-Q | P |
| CUBI | ">$600M of less-strategic deposits" remixed at ~150bp better pricing; 3.17% NIM "expected low point" (call summaries) | 7/24 | **S, UNVERIFIED** |
| CFG | Q2 deck guide: Q3 NII "Up 2.5–3.5%"; Q4-26 NIM 3.22–3.27% | 7/16 | P |
| CFG | Series J preferred issued (7/31 8-K); Series G redeemed 10/6; exiting the CoreCivic/GEO credit facilities (7/17); prime to 7.00% eff. 9/17 | 7/17–9/16 | P |
| CFG | Barclays 9/14: deposit costs rose 4bp in Q2 "as customers and the bank positioned for Federal Reserve rate moves"; FY NII on track to exceed 10–12% | 9/14 | **S** (AI-assisted write-up) |
| WAL | CEO at Barclays: deposits moved OFF balance sheet **$1.4B (Q2) + $2.5B (Q3) ≈ $4B vs a $3B goal**; Q3 NIM "down maybe about a basis point"; warehouse/MSR lending "probably won't be as active" | 9/16 | **S** (third-party transcript, KB-WAL-196) |
| WAL | Q2: deposit-growth guide cut $8B → $6B; "deposit optimization strategy" initiated in Q2 (10-Q MD&A p.60) | 7/21–7/31 | P |
| WAL | Lender in a Deutsche Bank-agented private-credit SPV facility (Crestline), $350M → $550M; WAL share undisclosed | 9/23 (Crestline 8-K) | P (third-party filer) |
| WAL | Q3 date: Mon 10/19 AMC, call Tue 10/20 12:00 ET | 10/6 | P (issuer release via syndication) |
| OZK | H2-26 NII to increase only modestly; NIM "slightly less than" 4.20%; **"the quarter just ended is likely an inflection point in our COIBD"** (i.e. deposit cost expected to turn UP) | 7/21 (8-K bundle pp.10, 13, 14) | P |
| OZK | $350M sub-notes reset ~6.19% from 10/1 ⇒ ≈+$12.3M/yr pre-tax (OZK desk; reset scheduled-uncontradicted, not filing-confirmed). No FDIC filing since 8/5 | 10/1 | P (indenture) / OZK |
| FLG | Guidance cut: 2026 NII $1.86–1.96B (from $1.95–2.05B), NIM 2.20–2.30%; $250M buyback | 7/24 | P |
| FLG | Barclays: IB deposit cost 3.05%, spot total ~2.52%; "keep costs relatively flat" with a 3.75% APY promotion; continued FHLB reductions (replay up to 10/13) | 9/15 | **S, UNVERIFIED** (AI summary) |
| FLG | NYC rent freeze (RGB Order #58) in force 10/1 — T-08 FIRED (FLG desk); $8.9B exposure | 10/1 | P (FLG) |
| EGBN | FHLB $100M paid off at maturity 7/7; 2026 avg-deposit guide −10 to −13%; NIM target 2.60–2.70% (Q2 2.52% "below range"); CEO Curley (ex-WAL) eff. 7/6, Risk Committee 9/14 | 7/6–9/14 | P |
| Fleet | **BROCK (10/02): one named bank facility to a PC vehicle TIGHTENED.** That is JPMorgan's FSK revolver: commitments −13.8%, margin +12.5bp. Counter-evidence at the same depth: ARCC's SMBC/BNP lines EXPANDED. **No attributable bank loss; none of the six is the lender.** | 10/2 | BROCK (10-Q notes, P) |
| Fleet | **NYFed private-credit visits to JPM/WFC/Barclays/MS since spring** (Semafor 10/5). Focus: collateral and valuation. Official confirmation **INDETERMINATE**. **None of the six is named.** CFG's remark-trigger private-credit book is the closest analogue in this set | 10/5 | S (WALTER -20261007-008/012) |
| Fleet | UWM: Fitch BB- → B+ (8/7); Citi MSR line $1.875B drawn vs $900M at year-end. Context for WAL's warehouse/MSR column. **WAL's UWM exposure is UNDISCLOSED** | 8/7 | HOMER (S for Fitch) |

### 1i. Next disclosure (column 9) — weekdays checked with `date -d`

| Bank | Q3 release | Call | Q3 10-Q / Call Report | DOCKET |
|---|---|---|---|---|
| **CFG** | **Fri 10/16** (pre-open INFERRED) | Fri 10/16 09:00 ET | 10-Q ~early Nov | (none; this report registers it) |
| **WAL** | **Mon 10/19 after close** | Tue 10/20 12:00 ET | EDGAR ≥ ~10/26, deadline Mon 11/9 | L170 |
| **OZK** | **Tue 10/20 after close** | Wed 10/21 08:30 ET | FDIC 10-Q ~early Nov | L520 |
| **EGBN** | **Wed 10/21 after close** (company IR 10/7) | Thu 10/22 10:00 ET | ~early Nov | L35 (RED re-dates) |
| **FLG** | **NOT ANNOUNCED** (secondary estimates Fri 10/23 or Mon 10/26) | — | ~11/9 est. | L522 |
| **CUBI** | **NOT ANNOUNCED** (pattern: Thu 10/22 AMC / Fri 10/23 call — ESTIMATE) | — | ~early Nov | (none) |
| All six | Q3 **Call Report** (RC-E, RC-K, RI, RC-O, RC-C Memo 10) due ~10/30; my run **11/07** | | ⚠️ **FFIEC JWT expires 11/05** (Will action) | CALENDAR |

---

## Deliverable 2 — PRE-COMMITTED Q3 observation list (written 2026-10-07, before any of the six has printed)

**What "the funding-vs-nonbank shortlist" means here:** a bank moves **UP** when its Q3 shows **cheap funding leaving (leg F)** at the same time as **non-bank credit being drawn (leg N)**. It moves **DOWN** when neither leg moves. Everything else is **INCONCLUSIVE**, and so is any case where the named line is not printed.
**Common leg definitions** (QoQ, Q2 → Q3, graded on the bank's own release/deck first, confirmed by [CR] at the 11/07 run):
- **F1** average NIB deposits fall >5%, or NIB share of period-end deposits falls ≥2pp.
- **F2** cost of interest-bearing deposits rises **≥10bp**. *Basis for the 10bp:* the 9/16 hike (+25bp) touched ~2 of Q3's 13 weeks. At betas of 50–70% that is ≈2–3bp on the quarterly average, so ≥10bp is ≈4× the hike mechanics.
- **F3** brokered deposits or FHLB advances rise ≥15%, or uninsured share rises ≥2pp.
- **N** NDFI / fund-finance drawn balance rises >5%, or a disclosed NDFI criticized/nonaccrual increase.
- **UP** = ≥2 of F1–F3 **and** N. **DOWN** = no F leg and no N. **INCONCLUSIVE** = one leg family only, or a management-declared deliberate move explains the F leg (named per bank below), or the line is not printed.
- ⛔ A Slok-type "agentic bank run" (SIG-W-20260928-004) is **a candidate mechanism, not an observed one**. Its observable is F1. At 6/30, NIB share was flat or up at all six, so **there is nothing to grade yet.**

| Bank | Exact lines read at Q3 | **UP** if | **DOWN** if | **INCONCLUSIVE** if |
|---|---|---|---|---|
| **CUBI** (release est. ~10/22, NOT announced) | EX-99.1 avg-balance table fn (4) "cost of interest-bearing deposits" (Q2 3.54%) and NIB average; deposit table NIB $6.91B / 31.8%; deck "DA Vertical spot balances" ($3.8B); "Specialized lending" balance ($7.65B) + deck loan-growth bridge (fund finance); FHLB advances (EX-99.1 balance sheet) | F: NIB avg falls >5% **or** DA spot balances < $3.42B (−10%), **plus** FHLB up ≥15% (> $2.37B) or IB cost ≥3.64%; **and** N: specialized lending up >5% (> $8.03B) | IB cost ≤3.54%, NIB ≥31.8%, FHLB flat/down, specialized lending ≤ +5% | Fund-finance balance still undisclosed (likely, since it is not broken out) ⇒ N **ungradeable from the release** ⇒ grade N at the 11/07 Call Report (Memo 10b+10c vs $3.60B). DA balance moves alone = INCONCLUSIVE (crypto-cycle driven) |
| **CFG** (Fri 10/16) | Financial supplement avg-balance table: IB deposit cost (Q2 2.08%), total 1.63%, avg NIB ($39.9B); 10-Q Table 9 capital call ($9,852M) + secured PC finance ($4,875M); deck NDFI slide (s25 equivalent); FHLB / other borrowings (balance sheet) | F: IB cost ≥2.18% **or** NIB share ≤20% of deposits (company basis, Q2 22%) **or** avg NIB < $37.9B (−5% from $39.88B), **plus** borrowed funds up ≥15% (FHLB > $7.32B [CR]); **and** N: capital call + secured PC > $15.46B (+5% on $14.73B) | IB cost ≤2.08%, NIB ≥22% (company basis), capital call + PC ≤ $15.46B | The Q3 deck guide was "NII up 2.5–3.5%". A rise in IB cost **inside the guide**, with no N, is INCONCLUSIVE. The 10-Q Table 9 lands ~early Nov ⇒ N may grade late |
| **WAL** (Mon 10/19 AMC; frame owner = WAL desk, L170) | Release "cost of interest-bearing deposits" (Q2 2.74%) and total (1.78%); deposit-composition slide (NIB, ECR-related); 10-Q NDFI table (Q2 $15,812M / 25.9% HFI); 10-Q Item 3 table (beta assumptions 53% / 70% / 59%) | F: IB cost ≥2.84% **or** NIB (ex the ~$2.5B Q3 off-balance-sheet move management announced) down >5%, **plus** brokered/FHLB up ≥15%; **and** N: NDFI > 25.9% of HFI **in a business-credit or PE-fund line**, not warehouse | IB cost ≤2.74%, NDFI share ≤25.9%, betas unchanged | A deposit decline **inside the announced ~$4B optimization** = INCONCLUSIVE on F1, by declaration. A warehouse-only NDFI rise (seasonal mortgage flow) = INCONCLUSIVE on N. ⚠️ **Model beta assumptions RAISED at Q3 (e.g. avg >53%) = a separate fact: report it, do not classify on it** |
| **OZK** (Tue 10/20 AMC) | Management comments "COIBD" (Q2 3.24%) and rate on all deposits (2.86%); NIB $3.95B / 11.6%; brokered $2.52B / 7.4%; C&IB chart Fund Finance ($1,197M) + Lender Finance ($873M); FDIC 10-Q NDFI funded ($3.26B) | F: COIBD ≥3.34% (**beyond** the "inflection" management flagged) **plus** brokered ≥15% up or any FHLB advance drawn; **and** N: Fund + Lender Finance > $2,174M (+5%) or NDFI funded > $3.42B | COIBD ≤3.24%, brokered ≤7.4%, NDFI ≤ $3.26B | COIBD +1 to +9bp = **pre-announced inflection + hike**: INCONCLUSIVE. NDFI rising while debt-on-debt keeps running off is a mix shift and is read as such. The FDIC 10-Q may post after the print |
| **FLG** *(CRE contrast; NDFI leg N/A by construction — PC slice 1.75%)* | EX-99.1 IB deposit cost (Q2 3.08%); "Wholesale borrowings" FHLB-NY ($9.9B); brokered CDs (~$2.1B); uninsured-or-not-collateralized (21%) | F only (FLG cannot reach the top of a funding-vs-NONBANK list): IB cost ≥3.18% **plus** FHLB > $9.9B (paydown reversed) or deposits −3% | IB cost ≤3.08% ("keep costs relatively flat", S) and FHLB < $9.9B | Anything else. ⚠️ A FLG funding move would matter to **the CRE thesis**, not to this list: route it to the FLG desk, do not score it here |
| **EGBN** *(CRE contrast; NDFI leg N/A — no NDFI book)* | EX-99.1 IB deposit cost (Q2 3.37%); brokered $2.6B / 32%; uninsured coverage "over 183%"; avg deposits vs the −10 to −13% guide | F only: brokered share >32% **or** uninsured coverage <150% **or** IB cost ≥3.47% | brokered share keeps falling (36% → 32% → lower), IB cost ≤3.37% | Average-deposit decline inside the −10 to −13% guide = INCONCLUSIVE (deliberate shrink). EGBN's Q3 decider is CRE (L35/RED), not funding |

**Grading mechanics:** grade each row within one session of its print. Grade from the named line only; if the line is absent, write "line not printed → INCONCLUSIVE", never infer it. Confirm F1/F3/N at the 11/07 Call Report run. **Expected modal outcome, stated in advance so it can be wrong:** *most rows INCONCLUSIVE*. Two management-declared deposit programs (WAL, EGBN) and one pre-announced cost inflection (OZK) absorb the most likely F moves. N needs a 10-Q or Call Report at four of six.

---

## What this does NOT do

- **No score, threshold, ladder level, trade or REG-T row moved.** If a Q3 row grades UP, I write a dated note to PROME; any threshold idea is a proposal to Will, not an edit.
- **Not a recurring study** (Will). [CR] file is a one-off baseline; Q3 is read once for this list.
- **Not a named-facility study.** CATO step 2 is BROCK's (L494, delivered 10/02, consumed above).
- **The [CR] deposit-cost divergence at CUBI (2025), OZK and EGBN is UNRESOLVED.** I did not chase it. The company figure carries column 1 there.

## Residue / gaps (named, not hidden)

1. FLG and CUBI Q3 dates NOT ANNOUNCED (10/7).
2. Collateral terms UNAVAILABLE at all four NDFI banks. Numeric deposit betas UNAVAILABLE at five of six (only WAL states them; EGBN states a qualitative floor rule; CFG and CUBI give realized cycle betas from their decks, not model inputs).
3. CUBI fund-finance balance NOT DISCLOSED (inside "Specialized lending").
4. OZK Q4-25 total-deposit rate not on disk.
5. Barclays-conference remarks (CFG, WAL, FLG) are SECONDARY. FLG's replay expires 10/13.
6. The "agentic bank run" mechanism has no observation to grade (F1 is flat or up at all six at 6/30).
7. **FFIEC JWT expires 11/05**, two days before the 11/07 run that confirms F1/F3/N. Regeneration is a Will action.
