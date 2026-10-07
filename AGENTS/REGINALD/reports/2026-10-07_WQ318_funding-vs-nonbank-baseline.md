# WQ-318 — Funding vs non-bank exposure: six-bank June baseline + pre-committed Q3 observation list

**Owner:** REGINALD · **Written:** 2026-10-07 Wed ~11:2x–11:4x ET (cloud session, PROME wave 2) · **DOCKET:** L527 (due 10/05, deliver-by 10/09) · **Approval:** WQ-318, Will 2026-09-28 14:1x ET (verbatim in `inbox/processed/2026-09-28_from-PROME_WQ-318-funding-vs-nonbank-baseline.md`).
**Status of this file: PARTIAL.** Both deliverables are here. Columns 1–4, 6, 8, 9 are filled for all six banks. Column 5 (collateral protection) is UNAVAILABLE for all six. Column 7 (rate sensitivity) is filled for WAL only; the other five are NOT EXTRACTED this session and are owed (see §4). ⛔ No score, threshold, gate or trade moves from this file.
**Out of order, stated:** PROME's packet put my 9/27 write-backs (MEMORY 0-WB) FIRST. They were NOT done this session (60-minute box, the regional-bank selloff took the front of it). 0-WB stays owed.

---

## 0. The question and the answer so far

**Question (CATO 9/28):** which regional banks could lose cheap deposits just as customers and funds draw more credit?
**Answer at the June baseline:** **no bank in the six shows both legs at 6/30.** Cheap deposits were not leaving: non-interest-bearing (NIB) share held or ROSE year on year at 4 of 6 (CUBI +3.0pp, WAL +1.6pp, EGBN +2.5pp, OZK +0.2pp), and NDFI nonaccruals were zero or under $0.2M at 4 of 6 (CUBI and EGBN 0; CFG $0.13M; FLG $0.05M — WAL $122.5M and OZK $25.9M are the exceptions). The exposure is real and concentrated: CUBI and CFG carry the largest undrawn commitments to non-banks relative to deposits (16.6% and 11.9%). The funding changes that DID happen are a **mix shift, not a run**: brokered money fell and uninsured money rose at CUBI, WAL, FLG and EGBN, and CFG's FHLB advances rose three quarters running. **The June data cannot see a run that would start after 9/16 (hike) or 10/7 (today's selloff); Q3 is the first read, and Q3 may well be INCONCLUSIVE** (the 9/16 hike sits only two weeks inside Q3).

## 1. Counter-evidence retained (not a footnote)

| Test | Result | Source |
|---|---|---|
| Did the 8/14+ selloff sort on the private-credit NDFI proxy (M10b+M10c ÷ loans)? | **NO.** | `workbook/NDFI_COHORT.tsv` header (FFIEC 6/30/26, built 8/20) |
| Did the 9/15→9/29 leg sort on it? | **NO — it sorted on SIZE** (14-name ρ −0.72; matrix +0.48). | `reports/2026-09-29_selloff_attribution_and_preprint_observables.md` |
| Does today's intraday move (10/7 ~11:0x ET, unsettled) sort on it across these six? | **NO — Spearman ρ ≈ +0.03** (PC rank CUBI·CFG·OZK·WAL·FLG·EGBN vs move rank WAL −3.76% · OZK −2.56% · FLG −2.29% · CFG −1.90% · CUBI −1.87% · EGBN −1.49%). ⚠️ n=6, intraday, not a close. | FORGE `fetch.py`, 11:06 ET |

Three dates, three non-sorts. The private-credit channel to banks is a **balance-sheet exposure that has not yet priced**, not a priced channel.

## 2. Deliverable 1 — six-bank table at 6/30/2026 (common baseline)

**Source for columns 1–3:** FDIC BankFind financials API (`api.fdic.gov/banks/financials`, Call Report data, bank level), pulled 2026-10-07 11:1x ET, certs CUBI 34444 · CFG 57957 · WAL 57512 · OZK 110 · FLG 32541 · EGBN 34742. **Bank level, not holding company** — holdco debt and holdco cash are outside every figure. FFIEC CDR credentials are not in this cloud container, so BankFind (a different agency pipeline over the same Call Report) is the route; it is the cross-check route named in `MEMORY_REFERENCE.md`. **Column 4 and 6:** `workbook/NDFI_COHORT.tsv` (FFIEC CDR primary, 6/30/26, pulled 8/20).

### 2a. Funding side (columns 1–3)

| Bank | (1) Cost of IB deposits, annualised: Q3-25 → Q4-25 → Q1-26 → **Q2-26** | (2) NIB share of deposits 6/30/26 (6/30/25) | (2) Uninsured share 6/30/26 (6/30/25) | (2) Brokered share 6/30/26 (6/30/25) | (3) FHLB ÷ liabilities 6/30/26 (6/30/25) | (3) All other borrowed money ÷ liabilities 6/30/26 |
|---|---|---|---|---|---|---|
| **CUBI** | 4.14 → 3.71 → 3.44 → **3.52%** | **32.2%** (29.2) | **44.3%** (38.9) | **21.1%** (32.9) | **8.5%** (5.8) · $2.06B | 8.5% |
| **CFG** | 2.35 → 2.21 → 2.00 → **2.08%** | **23.2%** (23.3) | **47.5%** (44.4) | **2.6%** (3.0) | **3.1%** (0.8) · $6.36B | 5.6% · $11.51B |
| **WAL** | 3.23 → 2.96 → 2.68 → **2.73%** | **33.8%** (32.2) | **38.1%** (28.9) | **18.8%** (26.4) | **6.4%** (7.1) · $5.80B | 7.2% |
| **OZK** | 3.63 → 3.48 → 3.22 → **3.16%** | **11.6%** (11.4) | **32.5%** (37.1) | **7.4%** (8.5) | **0.0%** (2.3) · $0 | 0.0% |
| FLG *(CRE contrast)* | 3.60 → 3.36 → 3.07 → **3.06%** | **17.4%** (17.8) | **28.9%** (23.5) | **9.7%** (15.3) | **12.4%** (14.5) · $9.90B | 13.2% · $10.49B |
| EGBN *(CRE contrast)* | 4.08 → 4.08 → 3.57 → **3.59%** | **19.3%** (16.8) | **27.7%** (24.9) | **31.9%** (37.9) | **1.2%** (0.5) · $0.10B | 1.2% |

**Method and limits, column 1 (read before citing):**
- Cost = quarterly interest expense on deposits (`EDEP`, RI item 2.a, de-cumulated from year-to-date) × 4 ÷ the average of beginning and ending interest-bearing deposits (`DEP − DEPNIDOM`). **Two-point average, not the daily average a 10-Q prints.**
- **Resolution check against WAL's own printed figure:** my method gives WAL Q2-26 **2.73%** vs WAL-reported **2.74%** (KB-WAL-102/-122), and Q1-26 **2.68%** vs reported **2.75%**. ⇒ **resolution is about ±7bp.** The +2 to +8bp Q1→Q2 upticks at CUBI, CFG, WAL and EGBN are INSIDE that error and are **not** a finding (WAL's own figure moved −1bp). The four-quarter declines (CUBI −62bp, FLG −54, WAL −50, EGBN −49, OZK −47, CFG −27) are well outside it.
- Q2-26 is **before** the 9/16 hike. None of this column sees the hike.
- **INCOMPARABLE across banks as a vulnerability rank:** cost level reflects product mix (OZK is a CD funder at 11.6% NIB; CFG is a large retail franchise). Compare each bank's CHANGE, not levels across banks.

**Column 2 limits:** uninsured = Call Report RC-O estimate at bank level (`DEPUNINS`); it includes collateralised and affiliate deposits that companies often exclude in their own "adjusted uninsured" figure (WAL's prior figure on file, KB-WAL-049, is do-not-cite for a basis defect). **A company-adjusted uninsured figure and this one are INCOMPARABLE.**

**Column 3 limits:** FHLB = `OTHBFHLB`; "all other borrowed money" = `OTHBRF` (includes FHLB). Repo (`FREPP`) is 0 at all six. **CFG's FHLB path:** $1.54B [6/25] → $0.01B [9/25] → $2.01B [12/25] → $2.51B [3/26] → **$6.36B [6/26]**, three straight rises. **CUBI:** $1.20B → $1.20B → $1.33B → $1.56B → **$2.06B**. FLG and OZK paid down. System context — not re-derived: `REG-T-06` FHLB system advances **$810.7B [6/30/26]**, leg 2 of 3; a Q3 print >$700B fires (late Oct / early Nov). Of these six, **CFG and CUBI are the two adding to that system figure.**

### 2b. Non-bank exposure side (columns 4–6)

| Bank | (4) NDFI drawn, $M (% of loans) | (4) of which private credit (M10b+M10c), $M (% of loans) | (4) M10a mortgage intermediaries, $M | (4) Unfunded NDFI commitments, $M | Unfunded NDFI ÷ deposits *(derived, mine)* | (5) Collateral protection | (6) NDFI nonaccrual / 30–89 / 90+, $M |
|---|---|---|---|---|---|---|---|
| **CUBI** | 6,143 (34.1%) | **3,596 (19.96%)** | 2,466 | 3,622 | **16.6%** | UNAVAILABLE | 0 / 0 / 0 |
| **CFG** | 21,993 (14.7%) | **15,908 (10.66%)** | 305 | **22,475** (exceeds drawn) | **11.9%** | UNAVAILABLE ¹ | 0.1 / 0 / 0 |
| **WAL** | 15,812 (24.1% FFIEC basis; 25.9% of HFI on the 10-Q basis — name the basis) | 4,917 (7.50%) | **10,895** (68.9% of NDFI) | 4,884 | 5.9% | UNAVAILABLE ² | **122.5 (0.77% of NDFI)** / 0 / 0 |
| **OZK** | 3,264 (10.0%) | 2,793 (8.58%) | 0 | 3,252 | 9.6% | UNAVAILABLE | 25.9 / 0 / 0 |
| FLG | 3,458 (5.7%) | 1,069 (1.75%) | 1,108 | 1,299 | 1.9% | UNAVAILABLE | 0.05 / 13.2 / 0 |
| EGBN | 92 (1.4%) | 0 (0%) | 92 | 78 | 0.9% | UNAVAILABLE | 0 / 0 / 0 |

¹ CFG "capital-call + secured private-credit finance" **$12.85B, +2–3% QoQ** (BROCK, aggregate, unnamed borrowers; KB-BRK-195/225) is a PRODUCT label, not advance rates or LTVs. Capital-call (subscription) lending against investor commitments is structurally different from NAV lending; the split is not disclosed in anything read here.
² WAL: management narrative only ("warehouse losses near zero"; WAL packet 9/28). No advance rates read.
**Column 5 is UNAVAILABLE for all six, not "none".** No 10-Q was read for advance rates or LTVs this session.
**Observed deterioration beyond the Call Report (later, from BROCK 10/02):** WAL **$126.4M First Brands receivables-financing charge-off, H1-26** (10-Q 7/31; the borrower is a finance company, not a private-credit fund) · OZK debt-on-debt book **$1.20B → $0.43B**, H1 charge-offs **$42.4M** (INFERRED sum match; fund borrowers unnamed).

### 2c. Rate sensitivity (column 7) — inputs, not verdicts

| Bank | NII sensitivity as stated | Stated assumptions + horizon | Source |
|---|---|---|---|
| **WAL** | Parallel shock: −200 **(8.6)%** · −100 **(5.2)%** · +100 **+5.9%** · +200 **+11.8%**. Gradual 12-month ramp: (5.1)% / (2.7)% / +3.2% / +6.3%. EVE: +4.4% / +2.7% / (4.4)% / (10.5)%. | **Dynamic** balance sheet · **12-month** horizon · forward-curve base · non-term deposit beta 45–86% by product, **average 53%** (Q1 55%) · ECR-eligible deposit beta **70%** (Q1 74%) · all non-maturity incl. ECR **59%** (Q1 62%) | Q2-26 10-Q acc 0001628280-26-051418, Item 3 pp.88–89, via WAL packet 9/28 (KB-WAL-212). One figure, both desks. |
| CUBI · CFG · OZK · FLG · EGBN | **NOT EXTRACTED this session** | — | Owed: each bank's Q2-26 10-Q Item 3 (OZK's 10-Q is FDIC-filed, cert 110 — not on EDGAR). |

⛔ No bank here is labelled "asset-sensitive" or "liability-sensitive". WAL's own model says NII rises with rates while EVE falls; both depend on a 53% average beta that a deposit run would break.

### 2d. Later disclosures, post-6/30 (column 8) — kept separate from the June baseline

| Bank | What is on file | Grade |
|---|---|---|
| WAL | CEO at Barclays 9/16: deposits moved **off balance sheet $1.4B in Q2 + $2.5B in Q3** (≈$4B vs a $3B FY goal); Q3 NIM "down maybe about a basis point"; warehouse/MSR lending "probably won't be as active"; deposit-growth guide cut $8B → $6B (Q2 call); WAL joined a Deutsche Bank-agented private-credit SPV facility as a lender (Crestline 8-K 9/23, $350M → $550M, WAL share undisclosed). | B2 transcript (unverified at primary) / A1 8-K — via WAL packet 9/28 |
| OZK | Sub-notes reset 10/1: coupon ≈6.19% (CME 3M Term SOFR + 209bp), **≈+$12.3M/yr pre-tax** — a wholesale funding cost, holding-company-level Tier 2. | OZK packet 10/01, KB-OZK-241 (benchmark VERIFIED, fixing INFERRED) |
| FLG | NYC rent freeze in force 10/1 (GATE-FLG-T08 FIRED) — a CRE credit mechanism, not funding. | FLG packet 10/01 |
| CFG · CUBI · EGBN | Nothing found — **not searched** this session (not "quiet"). | — |
| Fleet, not one of the six | JPMorgan-agented FSK revolver **tightened** (commitments −13.8%, margin +12.5bp, Amendment No. 1 5/8/26) while ARCC's lenders expanded — tightening goes to the weakest BDC, expansion to the strongest; **no attributable bank loss found.** | BROCK 10/02, KB-BRK-314 |
| Fleet, mechanism | WALTER -0928-004 (Slok, "agentic bank run"): rate-seeking automation pulling NIB balances faster than past cycles. **A named hypothesis, not an instrument.** The per-bank observable is column 2's NIB share at each quarter-end (and intra-quarter H.8 small-bank deposits). At 6/30 NIB share was flat or up at all six except FLG (−0.4pp YoY) and CFG (−0.1pp). | Mechanism SINGLE (Slok); observable mine |

### 2e. Next disclosure (column 9)

| Bank | Q3 release | Q3 10-Q / Call Report | Grade of the date |
|---|---|---|---|
| CFG | **Fri 10/16**, before the open, call 9:00 ET | 10-Q ~early Nov; Call Report 9/30 ~10/30 | CFG's own pre-announced 2026 schedule (Business Wire 2024-10-28, via finviz headline) — not read at CFG IR; **register on PROME's read** |
| CUBI | **UNCONFIRMED** (late Oct by pattern) | early Nov | not searched this session |
| WAL | **UNANNOUNCED** as of 10/7 11:1x ET (no 8-K since 9/25, EDGAR; no release found). Vendor estimate Tue 10/20 AMC (earningswhispers, unconfirmed). L170 window 10/13–10/22. | 10-Q statutory deadline Mon 11/9 (L171) | TRY-FIRE-002 stays NOT LOCKABLE |
| OZK | est. 10/20–21 (L520), not confirmed here | FDIC-filed 10-Q ~early Nov | estimate |
| FLG | est. ~10/23 (L522) | 10-Q ~11/9 est. | estimate |
| EGBN | est. ~Wed 10/21 AMC (L35) | early Nov | estimate |
| All six | Call Report 9/30/26 public ~early Nov; `NDFI_COHORT.tsv` re-pull due **11/07** (scheduled); BankFind refresh ~mid/late Nov | | |

## 3. Deliverable 2 — the pre-committed Q3 observation list (written 2026-10-07, BEFORE any Q3 print)

**Shortlist object:** a bank moves UP the funding-vulnerability shortlist only when BOTH legs move the wrong way in the same quarter — the funding leg (cheap money leaving or being replaced by dear money) AND the non-bank leg (non-banks drawing, or non-bank credit deteriorating). One leg alone is INCONCLUSIVE. This is the question as CATO asked it, and it is why a mix shift alone does not count.

**Common lines (read for every bank; 9/30/26 vs 6/30/26):**
- **F1 NIB share** = RC-E noninterest-bearing deposits ÷ total deposits (BankFind `DEPNIDOM`/`DEP`); the company release's "noninterest-bearing deposits" line gives it ~2 weeks earlier. **Wrong way = falls ≥1.0pp QoQ.**
- **F2 IB deposit cost** = the company's printed "cost of interest-bearing deposits" (daily average) where printed; else my two-point method (±7bp). **Wrong way = rises ≥15bp more than the six-bank median change.** ⚠️ The 9/16 hike is in only the last 2 weeks of Q3, so F2 will mostly NOT see it — **F2 alone can never move a bank UP in Q3.**
- **F3 Wholesale** = (FHLB + other borrowed money) ÷ liabilities (RC-M 5.a; RC item 16) or the release's "borrowings" line. **Wrong way = rises ≥1.5pp QoQ.**
- **F4 Uninsured** = RC-O Memo 2 ÷ deposits. **Wrong way = FALLS ≥3pp QoQ** (uninsured money leaving is the run signature; a rise is mix shift and is not counted against the bank).
- **N1 NDFI utilisation** = drawn ÷ (drawn + unfunded) from RC-C 9.a/Memo 10 and the RC-L NDFI unfunded line (same MDRM chain as `NDFI_COHORT.tsv`). **Wrong way = rises ≥3pp QoQ.**
- **N2 NDFI deterioration** = RC-N NDFI nonaccrual + 30–89 days. **Wrong way = rises to ≥0.5% of NDFI drawn, or any new NDFI charge-off disclosed in the release.**
- **Grading rule:** **UP** = at least one of F1/F3/F4 wrong way AND at least one of N1/N2 wrong way. **DOWN** = none of F1/F3/F4 wrong way AND neither N1 nor N2 wrong way. **INCONCLUSIVE** = anything else, or the needed line is not printed by the grading date (the Call Report then closes it ~early Nov). Q3 is allowed to remain INCONCLUSIVE (Will).

| Bank | June standing (from §2) | Moves UP if (in addition to the common rule) | Moves DOWN if | INCONCLUSIVE if | Exact disclosure lines |
|---|---|---|---|---|---|
| **CUBI** | Largest private-credit share (19.96%) and largest unfunded ÷ deposits (16.6%); uninsured 44.3%, up 5.4pp YoY as brokered fell 11.8pp; FHLB rising 4 quarters | Common rule; **specific tell:** NIB share below **31.2%** at 9/30 together with NDFI drawn up | NIB ≥32.2%, FHLB ÷ liabilities ≤8.5%, NDFI nonaccrual still 0 | Release omits a deposit-mix table and the Call Report is not yet out | Q3 release deposit-composition table (NIB, interest-bearing demand, time, brokered) · loan table (mortgage warehouse; fund finance / capital call) · Call Report RC-E, RC-O M2, RC-C M10, RC-N 9.a |
| **CFG** | Largest absolute private-credit book ($15.9B); unfunded NDFI ($22.5B) EXCEEDS drawn; FHLB 0.8% → 3.1% of liabilities, three straight rises; uninsured 47.5% | Common rule; **specific tell:** FHLB/borrowings up again (≥ +1.5pp) while capital-call/secured PC balance (BROCK's $12.85B line) grows | FHLB falls back below ~2% of liabilities and NIB share holds ≥23% | — | **Fri 10/16** release + financial supplement: average-balance table (NIB deposits; cost of IB deposits), "Borrowed funds / FHLB advances" line, commercial loan detail for capital call / PC finance · Call Report RC-M 5.a, RC-L NDFI unfunded |
| **WAL** | NDFI 25.9% of HFI (68.9% mortgage intermediaries); NIB 33.8%; deposit optimisation moving ~$4B off balance sheet BY DESIGN; uninsured 38.1% (+9.2pp YoY) | Common rule, **but net of the designed outflow:** a total-deposit fall ≤ the guided $2.5B with a stable mix is NOT wrong way. UP needs NIB share to fall ≥1pp AND N1 or N2 wrong way (10-Q NDFI table vs 25.9%, WAL's own 10-Q frame §5) | NIB ≥33%, IB cost ≤ 2.74% + 15bp, NDFI share ≤25.9% with nonaccrual ≤0.77% | Deposits fall by about the guided off-balance-sheet amount and nothing else moves — **the designed path reads INCONCLUSIVE, not DOWN** | Q3 release: "non-interest bearing deposits", "cost of interest-bearing deposits" (2.74% Q2), deposit-by-type and (if printed) ECR-related deposits; Q3 10-Q NDFI table (frames `AGENTS/WAL/Q3_PRINT_GRADING_FRAME_2026-09-24.md`, `Q3_10Q_GRADING_FRAME_2026-09-24.md`) — WAL desk grades its own frames; this list reads their outputs |
| **OZK** | Cheap-deposit leg ABSENT (NIB 11.6% — a CD funder; nothing cheap to lose); zero FHLB; uninsured falling (37.1 → 32.5%); debt-on-debt book shrinking | FHLB reappears (>2% of liabilities) or brokered >10% of deposits, AND N2 wrong way (NDFI nonaccrual above $25.9M / 0.79%) | No FHLB, brokered ≤8%, NDFI nonaccrual flat or down | Default if only the sub-notes reset cost shows (a known +$12.3M/yr, not new information) | Q3 Management Comments deposit table + Financial Supplement; FDIC-filed 10-Q (cert 110); Call Report RC-M 5.a, RC-E M1.b, RC-N 9.a |
| FLG *(contrast)* | Highest wholesale (FHLB 12.4% of liabilities, paying down from 14.5%); NDFI small (PC 1.75%); uninsured up 5.4pp as brokered fell 5.6pp | FHLB ÷ liabilities RISES ≥1.5pp (the paydown reverses) or uninsured FALLS ≥3pp — **the non-bank leg is too small to qualify, so FLG cannot move UP on this list; a wrong-way funding print goes to the CRE/FLG lane instead** | Wholesale keeps falling, NIB ≥17% | — | Q3 release (~10/23 est.) deposit + "wholesale borrowings" lines; Call Report RC-M 5.a, RC-O M2 |
| EGBN *(contrast)* | Highest brokered (31.9%, down from 37.9%); NIB rising (16.8 → 19.3%); NDFI ~nil | **Cannot move UP on this list** (no non-bank leg). Note only: brokered share RISING ≥3pp or NIB falling ≥1pp is a funding deterioration for the CRE lane (EGBN Q3 frames L35) | Brokered keeps falling, NIB holds | — | Q3 release (~10/21 est.) deposit table (brokered / core); Call Report RC-E M1.b |

**What this list does NOT do:** it registers no REG-T threshold and no gate (the bars above are observation rules for one shortlist, registered here, graded at the prints). It moves no matrix score. If a Q3 read would change a REG-T threshold, it goes to PROME as a proposal.

## 4. Owed (not done this session — named, not dropped)

1. **Column 7 for CUBI, CFG, OZK, FLG, EGBN** — each Q2-26 10-Q Item 3 NII table with its stated beta, balance-sheet and horizon assumptions (OZK from the FDIC-filed 10-Q). Must land **before CFG's 10/16 print**, or CFG's row grades without it.
2. **Column 5 for all six** — advance rates / LTV / subscription-vs-NAV split where the 10-Qs disclose them; UNAVAILABLE otherwise.
3. **CUBI and EGBN Q3 dates** — confirm at company IR; CFG's 10/16 at CFG IR primary.
4. **MEMORY 0-WB write-backs (9/27)** — PROME sequenced them first; still owed.
5. `KB.tsv` rows for this file's new figures — **added this session** as ML-REG-170..172 (pointer rows; the figures live here).

## 5. Provenance

- FDIC BankFind: `https://api.fdic.gov/banks/financials?filters=CERT:(57512 OR 110 OR 32541 OR 34444 OR 34742 OR 57957) AND REPDTE:[20250630 TO 20260630]&fields=CERT,REPDTE,ASSET,LIAB,DEP,DEPDOM,DEPFOR,DEPNIDOM,DEPIDOM,DEPUNINS,BRO,OTHBFHLB,OTHBRF,FREPP,EDEP,EINTEXP,LNLSGR,LNNDEPD` (30 rows, index `risview_20260819185831`). `DEPFOR` = 0 at CFG and FLG (the two foreign-office filers), so domestic NIB ÷ total deposits is complete for both.
- Cross-tie: BankFind `LNNDEPD` for WAL = **15,812,034** = `NDFI_COHORT.tsv` NDFI_total_K for WAL (FFIEC CDR) — two pipelines, same figure.
- Certs resolved by RSSD via BankFind `institutions` (FLG = cert 32541 Flagstar Bank, N.A.; the old NYCB cert 16022 is inactive).
- Intraday sort in §1: FORGE `fetch.py price`, 2026-10-07 11:06 ET.
