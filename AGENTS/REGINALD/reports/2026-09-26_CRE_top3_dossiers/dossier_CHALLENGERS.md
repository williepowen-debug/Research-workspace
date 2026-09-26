# CHALLENGER SCREEN — does any name beat FLG / EGBN / AMTB on CRE vulnerability?

**For:** REGINALD · **Written:** Sat 2026-09-26 · **Mode:** read-only screen. Existing repo work first, plus primary EDGAR pulls for VLY (Q2 8-K EX-99.1, 10-Q, 8/25 8-K) and BCB (five 8-Ks, 9/02–9/25). **No repo file was edited.**
**Short answer:** **OZK beats AMTB on CRE evidence. VLY is the runner-up.** AMTB's score of 5 comes from **non-CRE** credit: CRE is 5.8% of its nonaccruals. BCB is a **price-discovery comparable** and not a slate candidate: it has already recognized its losses and raised capital, and it is ~$3B in assets.

---

## A. CREED SYNTHESIS — what is stressing now, and which cohort banks map onto it

Source: `AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md` (cited below as **MAP:line**), commit b18b3384f, 9/26. CREED's central read (MAP:17) is that **2026 CRE distress is mostly failure to refinance at maturity (B), not weak property cash flow (A)**.

| Stress pocket | CREED figure (date, source) | Mode | Cohort banks that map onto it |
|---|---|---|---|
| **Office, national** | CMBS office DQ **12.00%** / SS **16.90%** [Aug, Trepp] (MAP:25). Sept hard maturities: office $1.48B = 54% of the cohort, **36.5% already in SS** (MAP:25) | B ≫ A | FLG (NYC), EGBN (DC), VLY (office NOT DISCLOSED in text), OZK (Seattle, Santa Monica and Atlanta office in OREO), WAL (office tail) |
| **DC / N. Virginia office** | $377.6M Project James (8 DC-area offices) failed to pay off at its **Aug** maturity. "Densest new cluster in the Aug print" (MAP:42) | B | **EGBN.** CREED names EGBN × DC office explicitly (MAP:117, 126) |
| **NYC** | 111 Livingston and 60 Madison SS transfers (Aug). 1740 Broadway **AAA −26%** loss (MAP:42) | B, C at the tail | **FLG** (rent-regulated MF + office), **VLY** (NYC/NJ), BCB (NJ/NY) |
| **Chicago** | 205 W Randolph **−72%** realized; Aon −58% (a mark, not a sale) (MAP:43) | B + C | OZK (Chicago life-sci OREO $47.5M) |
| **Seattle** | ~37% downtown vacancy. "The clearest genuine cash-flow market" (MAP:45) | A + C | **OZK** (U-District charge-offs $34.5M; Seattle office OREO $56.1M; The Jack $25.9M nonaccrual) |
| **Boston / SF life science** | Boston-Cambridge lab vacancy **26.4% (+610bp)**, driven by new supply. Tied to **2021–22 construction and bridge vintages** (MAP:30) | A (supply-driven) | **OZK** (10 Prospect, Boston $169.3M nonaccrual; life-sci OREO) |
| **LA** | Glendale Plaza sold **−61%** vs 2017 [secondary] (MAP:44) | B + C | OZK (Santa Monica office OREO $44.8M, LA land $54.5M) |
| **Multifamily** | Freddie MF DQ **0.64%** [Aug], **4th straight rise**. The only type where cash-flow stress (A) is the rising leg. Only 13% of MF balances mature in 2026 (MAP:27) | A > B | FLG, VLY (MF $9.03B), BCB. NYC rent-freeze leg: FLG desk |
| **Lodging** | 30% of 2026 hotel balances mature, the largest share of any type (MAP:28) | B by schedule | OZK (Wauwatosa hotel $16.7M) |
| **Florida** | **Zero FL assets named in Jul/Aug Trepp prose.** Spring FL hotel portfolio **cured**. "Quiet on CRE credit" (MAP:49) | — | **AMTB**, BKU, SBCF, SSB, VLY (FL leg) |
| **Industrial / data centre** | DQ 1.14%, SS 1.27% [Aug] (MAP:31) | none | — |
| **Banks, aggregate** | FDIC Q2 reserve coverage 172.7%. **But regional CRE OREO +26.4% QoQ** (MAP:60). T-03 not fired; next test FDIC Q3 QBP ~late Nov | B hidden by extensions | Concentrated, not systemic |

**What this implies:** CREED's stress sits in **gateway office (DC, NYC, Chicago, LA, Boston), 2021–22-vintage construction and life-science, and NYC multifamily**. **Florida is the quietest geography on CRE credit.** Two of the default three fit the map: **FLG** (NYC multifamily) and **EGBN** (DC office). **AMTB (Miami) does not.** OZK's problem roster reads almost line for line like CREED's metro list.

---

## B. CHALLENGER TABLE

Matrix columns (SR 07-1 CRE concentration / nonaccrual % / ACL ÷ nonaccrual) are all FFIEC 6/30/2026, from `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md:46-59`.

| Bank | CRE conc | NA % | ACL/NA | Property-type / geography match to CREED | Direction | Indirect exposure via funds / NDFIs (reported, unscored; matrix:159-167) | **Verdict** |
|---|---:|---:|---:|---|---|---|---|
| **OZK** | 259.5% | 0.92% | 154% | **Strongest match in the cohort.** Nonaccrual: Boston life-sci $169.3M (matured 2/13/26), Baltimore land $40.0M, Seattle office $25.9M, hotel $16.7M. OREO: Seattle office $56.1M, life-sci $48.5M, LA land $54.5M, Chicago life-sci $47.5M, Santa Monica office $44.8M, Atlanta office $36.6M (`OZK/STATUS.md:73-76`). **82% of H1 gross charge-offs are 2022-vintage** (:80) | 🔴 **DETERIORATING, with adverse selection.** Classified + criticized $1,215M→**$1,282M** while RESG commitments fell $27.8B→**$25.7B** (:43-44). NPA $451M→**$593M** (1.08→1.42%) (:45). Q2 NCO **0.69%** annualized (:41). Special mention **+$219M to $616.2M**, incl. a $147M condo at 105.6% LTV (:77). OREO H1 inflows $241.6M vs sales $6.9M: foreclosed, **not yet priced** (:76) | PC-NDFI **8.58%** of loans; NDFI nonaccrual $25.9M. Debt-on-debt (`RCON2746`) book $430.3M; **first nonzero CRE-not-secured charge-off in 18 quarters, $42.4M YTD** (:58-59). This is the indirect channel | **DISPLACES AMTB** (see note ①) |
| **VLY** | 319.5% (company-defined 317%, down from 329% in Q1) | 0.88% | 128% | NJ / NYC / Long Island / FL (10-Q). **Rent-regulated (>50%) MF is only $559M** at 6/30 (10-Q loan table note 1), vs FLG's $8.9B (`FLG/STATUS.md:71`). MF $9.03B; NOO $11.15B; construction $2.48B. Office NOT DISCLOSED in text (it is in the slide images). FL office $1.1B = 37% of total office at Q4-25 (`earnings_briefs/VLY_Q1_2026.md:43`) | 🟠 **MIXED.** CRE nonaccrual **$225.4M→$256.1M (+13.6% QoQ)**, driven by **three collateral-dependent CRE loans ($49.6M) carrying $0 allocated reserve**. 30-59 DPD **+$42.6M to $151.0M**, "a few larger CRE loans" (EX-99.1). Against that: NOO runoff −$357.2M QoQ; CRE criticized **$2.97B→$2.89B** (12/31→6/30, DERIVED below); runway **6.63 yr and lengthening** (`workbook/RUNWAY_COHORT.tsv:147`); CO/provision 1.03× (`ACL_ROLLFORWARD_COHORT.tsv:144`) | PC-NDFI 2.73% ($1.43B: M10b $619M + M10c $814M), NDFI nonaccrual $0 (`NDFI_COHORT.tsv:16`) | **RUNNER-UP** (see note ②) |
| **WAL** | 161.1% | 0.86% | 86% | Office tail plus the $99M life-science loan (appraisal pending) (`WAL/STATUS.md:63`) | 🟢→🟡 Management guided 9/16 that NPLs fall **$567M→~$500M** in Q3, NCOs below Q2, and ACL "well over 100%". **B2 source (guidance), not a filing** (:46) | PC-NDFI 7.50%; **NDFI nonaccrual $122.5M. This is an INDIRECT channel, not direct CRE.** New Crestline SPV lending (8-K 9/18, size undisclosed) (:48) | **NOT A CHALLENGER.** Below 200%; direction guided down; the WAL desk owns it |
| **BKU** | 193.9% | 0.95% | 95% | FL (Miami). CREED calls FL quiet | 🟢 **De-risking.** CRE criticized **−14.2%** ($560.9M→$481.3M); CRE 30-89 **$23.4M→$0**; NCO 0.61%→0.11%. The criticized rise is **C&I (+$86.6M)**, not CRE (`reports/2026-07-18_smalltier_FL_CRE-DQ_Q2_watchcard.md:99,109,122`) | PC-NDFI 2.18%; NDFI nonaccrual $25.1M (`NDFI_COHORT.tsv:10`) | **NOT A CHALLENGER.** Coverage just under 100% is its only flag, and that is not CRE-driven |
| **BCB Bancorp (BCBP)**, outside the cohort | NOT DISCLOSED (CRE+MF loans $2,009.9M = **76.3%** of $2,634.9M gross loans, 6/30/26, DERIVED) | 2.73% (DERIVED: $72.0M ÷ $2,634.9M) | 62.5% | NJ/NY CRE + multifamily: **$180.7M of the $205.3M sold (88.0%) is CRE/MF** (8-K 9/25) | ✅ **RECOGNIZED.** Priced problem-loan sale; Q3 provision guided at $112–120M; $98.0M equity raise; dividends suspended; new CEO; auditor changed 9/02 (Wolf → Deloitte, no disagreements) | NOT DISCLOSED | **NOT A CHALLENGER for the slate** (~$3.1B in assets; loss already taken). **High value as a price comparable** for FLG/VLY NJ-NY CRE/MF (§C) |
| AMTB (default, for contrast) | 218.4% | 2.46% | 51% | Miami. **CRE nonaccrual $9.8M of $168.8M total (5.8%, DERIVED)**. CRE-NOO $9.4M; MF $0.4M (`reports/2026-07-25_EGBN_Q2_grade…:170-180`) | De-risking by **loan sales**: classified −14.7%, SM −25.9% (:185-190) | PC-NDFI 0.00% (`NDFI_COHORT.tsv:12`) | **DISPLACED** on the CRE question |

**① Why OZK displaces AMTB.**
- **The matrix under-scores OZK. The credit leg reads nonaccrual `RCON1403`, which excludes OREO.** OZK has moved **$292.7M** of problem CRE into foreclosed assets.
- **Re-cut on nonaccrual + OREO:** ($300.4M + $292.7M) ÷ $617.8M ACL → ACL covers **104%**. **DERIVED:** 617.8 ÷ 593.1. That is still above 100%, so the score does not flip, but the 154% cushion mostly disappears.
- **$257.8M of the $300.4M nonaccrual carries $0 allowance** (`OZK/STATUS.md:74`). The reserve therefore sits on the performing book, not on the problem loans.
- ⚠️ **Caveat — coverage overlap.** OZK has a dedicated desk (`AGENTS/OZK/`) that already covers single-name depth. REGINALD's added value on OZK is **cohort-level**: the matrix's OREO blind spot, and the life-science and gateway-office read-across. It is not a second thesis.

**② Why VLY is only the runner-up.**
- It is the **only other name above the 300% line**, and its CRE nonaccruals rose 13.6% QoQ with zero allocated reserve on the new migrants.
- **But:** its rent-regulated book is **~6% of FLG's** ($559M vs $8.9B); CRE criticized is falling; runway is the cohort's third-longest; and management is **acquiring**, not defending (Providence Financial, $1.6B in assets, $247M consideration, 8-K 8/25/26, acc 0001193125-26-364239).
- **DERIVED — VLY CRE (ex-construction) criticized, 10-Q risk-rating table:**
  - 6/30/26: SM $1,082.1M + Sub $1,761.0M + Doubtful $45.8M = **$2,888.8M = 10.36%** of $27,873.7M.
  - 12/31/25: $1,033.8M + $1,895.1M + $42.9M = **$2,971.8M = 11.10%** of $26,772.7M.
  - Classified (Sub + Doubtful) **$1,806.7M vs a CRE-line ACL of $268.4M** (EX-99.1 allocation table).

---

## C. LOSS-INPUT BLOCKS

### VLY — Valley National Bancorp (CIK 0000714310)
| Item | Value | As-of | Source |
|---|---|---|---|
| CET1 ratio (holdco) | **10.71%** (Q1 10.91%) | 6/30/26 | Q2 8-K EX-99.1, acc 0000714310-26-000036 |
| CET1 $ / RWA (bank-level, Call Report) | **$6,527.1M** / $53,158.7M → 12.28%; AOCI-adjusted with HTM 11.54% | 6/30/26 | `REGINALD/workbook/AOCI_COHORT_2026Q2.tsv:15` |
| CET1 $ (holdco) | NOT DISCLOSED in the release text | — | — |
| ACL for loans (incl. unfunded) | **$606.9M** (1.16% of loans) | 6/30/26 | EX-99.1 |
| ACL on CRE / construction | $268.4M (0.96%) / $50.6M (2.05%) | 6/30/26 | EX-99.1 allocation table |
| Nonaccrual: total / CRE / construction | **$462.6M / $256.1M / $9.1M** | 6/30/26 | EX-99.1 |
| NCO Q2 / Q1 | $22.0M (0.17%) / $17.5M (0.14%) | Q2-26 | EX-99.1 |
| PPNR, quarterly | **$249.6M** Q2-26 · $230.4M Q1-26 · $210.9M Q2-25 | — | EX-99.1 |
| PPNR, trailing | H1-26 **$480.0M**. TTM NOT DISCLOSED in this release (Q3/Q4-25 not pulled). **DERIVED annualized: $480.0M × 2 = $960.1M** | H1-26 | EX-99.1 |
| CRE by type | NOO **$11,146.7M** · MF **$9,034.2M** · OO $7,692.9M · construction $2,475.1M · total **$30,348.8M** | 6/30/26 | EX-99.1 loan table |
| Rent-regulated (>50%) collateral | **$559M** ($583M Q1, $601M Q4-25) | 6/30/26 | 10-Q acc 0000714310-26-000041, loan table note 1 |
| Office | NOT DISCLOSED in text (in earnings-deck images). FL office $1.1B ≈ 37% of office at Q4-25 | 12/31/25 | `earnings_briefs/VLY_Q1_2026.md:43` |
| Sale prices | Q1-26: one $9.1M non-performing CRE relationship sold from HFS at a **$767K net gain** over its HFS mark. % of par NOT DISCLOSED | Q1-26 | 10-Q, Loan Portfolio Sales |
| **Stress sizing** | **DERIVED:** annualized PPNR $960M covers a **3.2% loss** on the full $30.3B CRE book in one year before touching the reserve (960 ÷ 30,349). Or a **53% loss** on the $1.81B of classified CRE (960 ÷ 1,807) | — | arithmetic |

### BCB Bancorp (BCBP, CIK 0001228454) — the priced comparable
| Item | Value | As-of | Source |
|---|---|---|---|
| Problem-loan sale, face value | **$205.3M UPB** (CRE+MF $180.7M · C&I $14.8M · construction $9.8M), 6 buyers, agreements signed 9/21–24; 5 of 6 closed | UPB as of 6/30/26 | 8-K 9/25/26, acc 0001193125-26-402710 |
| Pre-tax loss on the sale | **$43.3M**, booked in Q3 | Q3-26 | same |
| Implied price, % of par | **NOT DISCLOSED.** **DERIVED ceiling: ≤ ~78.9% of UPB** ((205.3 − 43.3) ÷ 205.3), assuming carrying value = UPB. Any prior partial charge-offs mean the true price is **lower** | — | arithmetic |
| Wider marketed pool | The 9/16 guide put **$87M** of pre-tax loss on the $210M sale plus a **$96M** HFS transfer ($27M CRE + $69M cannabis loans) | 9/16/26 | 8-K acc 0001193125-26-393183 |
| Q3 guide | Provision **$112–120M**; **net loss $126.2–136.1M**, incl. a ~$50M full DTA valuation allowance | Q3-26 | same |
| Capital raise | **12.65M shares at $7.75 = $98.0M gross** (overallotment exercised), closed 9/18 | 9/18/26 | 8-K acc 0001193125-26-395743 |
| CET1 | NOT EXTRACTED (not in the text pulled) | — | — |
| ACL / nonaccrual / ACL÷NA | $45.0M / $72.0M / 62.5% | 6/30/26 | Q2 8-K acc 0001193125-26-329536 |
| Criticized + classified | **$367.4M = 13.94% of gross loans** (CEO on the 8/03 call: "still pretty shockingly high") | 6/30/26 | same; call transcript acc 0001193125-26-339642 |
| PPNR, quarterly | NOT DISCLOSED. **DERIVED from the Q3 guide:** NII ~$23M (Q2 $23.3M) + non-interest income $5.1–5.7M − non-interest expense $17.9–18.5M ≈ **~$10M per quarter** | Q3-26 guide | arithmetic |

⚠️ **Scope limit on BCB:** a ~21% loss on a **pre-selected problem pool, most of it criticized or classified**, is a severity reading on bad loans. It is **not** a mark on a performing NJ/NY CRE book. As a comparable for FLG/VLY, apply it only to their classified buckets.

---

## D. THE STRONGEST ARGUMENT AGAINST THE DEFAULT SLATE

**AMTB's place in the top three is not a CRE finding.**
- Of AMTB's **$168.8M** of nonaccruals at 6/30/26, only **$9.8M (5.8%) is CRE** (CRE-NOO $9.4M + MF $0.4M; construction $0).
- The rest is C&I ($79.0M), owner-occupied ($40.5M), single-family residential ($31.2M) and consumer ($8.3M) (`reports/2026-07-25_EGBN_Q2_grade_plus_FL_smalltier_watchcard_fill.md:172-181`, Q2 8-K acc 0001734342-26-000071).
- AMTB's 3 credit points (2.46% nonaccrual, 51% coverage) are therefore **C&I / owner-occupied / residential stress scored as if it were CRE vulnerability.** Its only CRE contribution is 2 points for a 218.4% concentration.
- Its Miami geography is the one CREED calls **quiet on CRE credit** (MAP:49).
- The Q2 direction was **de-risking via loan sales** (classified −14.7%).
- **OZK is the opposite case.** It scores only 2, because the matrix's credit leg cannot see **$292.7M of foreclosed CRE** or **$257.8M of zero-reserve nonaccruals**, and its problem book sits in exactly the metros and vintages CREED flags.

**What a defender of the slate would say:**
- AMTB's 51% coverage is real reserve weakness whatever the collateral type.
- OZK is already deep-covered by its own desk.
- Q3 prints (AMTB ~10/22) could reverse the picture.

⇒ **Evidence-ranked slate for CRE vulnerability: FLG · EGBN · OZK.** First alternate: **VLY**, the only other name above the 300% line. It has rising CRE nonaccruals with $0 reserve on the new migrants, but NYC rent-regulated exposure is small and every other trend is de-risking.
⇒ **If desk overlap is disqualifying, the slate is FLG · EGBN · VLY.** Either way, AMTB is the name to drop.

Why the other two defaults survive:
- **FLG:** its $8.9B NYC rent-regulated MF book and **29% coverage** remain the cohort's strongest single CRE signal.
- **EGBN:** it is a DC CRE lender, and DC is CREED's densest new office cluster. Its Q2 was de-risking via disposition, CET1 14.58% (`reports/2026-07-25_EGBN…:93`), so it is the weakest of the three survivors on *direction*.

---

## E. SOURCES

**Repo (read-only):**
- `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md:23-171`
- `AGENTS/REGINALD/earnings_briefs/VLY_Q1_2026.md`
- `AGENTS/REGINALD/workbook/{ACL_ROLLFORWARD_COHORT,RUNWAY_COHORT,NDFI_COHORT,AOCI_COHORT_2026Q2}.tsv`
- `AGENTS/REGINALD/reports/2026-07-25_EGBN_Q2_grade_plus_FL_smalltier_watchcard_fill.md`
- `AGENTS/REGINALD/reports/2026-07-18_smalltier_FL_CRE-DQ_Q2_watchcard.md`
- `AGENTS/REGINALD/reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md`
- `AGENTS/REGINALD/STATUS_MATRIX.md:17-19`
- `AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-…md`
- `AGENTS/CREED/STATUS.md`
- `AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md`
- `AGENTS/CREED/catchups/2026-09-26.md`
- `AGENTS/OZK/STATUS.md:41-80`
- `AGENTS/WAL/STATUS.md:46-77`
- `AGENTS/FLG/STATUS.md:31,71`

**SEC EDGAR primaries (fetched 9/26/26):**
- VLY Q2 8-K EX-99.1: https://www.sec.gov/Archives/edgar/data/714310/000071431026000036/exhibit991earningsrelease0.htm
- VLY Q2 10-Q: https://www.sec.gov/Archives/edgar/data/714310/000071431026000041/vly-20260630.htm
- VLY 8/25 8-K (Providence acquisition): https://www.sec.gov/Archives/edgar/data/714310/000119312526364239/d149125dex991.htm
- BCB 9/25 loan sale: https://www.sec.gov/Archives/edgar/data/1228454/000119312526402710/d185663dex991.htm
- BCB 9/16 Q3 update: https://www.sec.gov/Archives/edgar/data/1228454/000119312526393183/d156244dex991.htm
- BCB 9/16 pricing: https://www.sec.gov/Archives/edgar/data/1228454/000119312526393461/d153277dex991.htm
- BCB 9/18 close: https://www.sec.gov/Archives/edgar/data/1228454/000119312526395743/d112674dex991.htm
- BCB 9/02 auditor change: https://www.sec.gov/Archives/edgar/data/1228454/000119312526381867/d157361d8k.htm
- BCB Q2 release: https://www.sec.gov/Archives/edgar/data/1228454/000119312526329536/d149798dex991.htm
- BCB Q2 call transcript: https://www.sec.gov/Archives/edgar/data/1228454/000119312526339642/d155268dex991.htm

**Not pulled:**
- VLY earnings-deck slides (office by metro).
- VLY Q3/Q4-25 releases (TTM PPNR).
- BCB CET1.
- OZK primaries (FDIC filer; consumed from the OZK desk instead).
