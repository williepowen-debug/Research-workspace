# SHADE — ARI attribution match: AAIA 4/24/2026 loans vs ARI's own loan tables · 2026-10-01

**Task:** PROME touch 2 (`prome-0c`, Will "go for the six" 12:49 ET). **Rails:** no trade proposal, no threshold move.

## 0. MATCH RULE — PRE-REGISTERED (written and committed BEFORE any ARI table was fetched or read)

**Population (A):** every AAIA Q2-2026 statutory Schedule B Part 2 row with Date Acquired = **04/24/2026** in the commercial (0499999) or mezzanine (0699999) subsections, i.e. the 62 rows totalling **$7,405,267,470** (actual cost at acquisition). Fields available: loan number (Athene's own), city, state/country, rate, actual cost, value of land and buildings. **No borrower name, no property type, no maturity** in Part 2.

**Reference (R):** ARI's own loan-level disclosure from its latest periodic filings before the sale closed (10-K FY2025, 10-Q Q1-2026 if it lists loans) and the sale proxy/8-K, from SEC EDGAR, each with accession number and date.

**A loan a ∈ A MATCHES an ARI loan r ∈ R iff ALL of:**
1. **LOCATION:** same city (or the borough/metro ARI names, e.g. "Manhattan" ↔ NEW YORK) AND same US state or same country.
2. **SIZE:** a's actual cost is within **±15%** of r's carrying value / amortized cost / principal at the most recent ARI report date, **or** within ±15% of r's funded balance where ARI reports commitment and unfunded separately. (Partial-funding and FX moves since the report date are the reason for the band.)
3. **RATE (only where both sides report one):** a's rate within **±75bp** of r's coupon or all-in rate. Where one side lacks a rate, condition 3 is skipped and the match is labelled SIZE+LOCATION only.

**Assignment:** one-to-one. If several ARI loans satisfy 1–2 for one AAIA row (or vice versa), assign by smallest absolute size gap; ties stay AMBIGUOUS.
**Labels:** **MATCH** (1+2+3, or 1+2 where 3 unavailable) · **LOCATION-ONLY** (1 met, 2 failed) · **UNMATCHED**.
**Verdict rule (fixed now):**
- **CONFIRMS** "these are the ARI loans" if **≥75% of A's dollars** are MATCH **and** no AAIA 4/24 row ≥ $100M is UNMATCHED without an explanation from the ARI side (e.g. a loan ARI says was excluded).
- **REFUTES** if **<25% of A's dollars** are MATCH (location+size coincidence would be expected to give few matches if the loans came from elsewhere).
- **UNDETERMINED** otherwise, or if ARI's tables do not disclose loans at a granularity that permits rule 1 for most of the book.

**Known limits stated in advance:** location+size cannot prove identity (a coincidental same-city, same-size loan from another seller would MATCH); conversely, ARI loans restructured, paid down or split between report date and 4/24 can fail rule 2 while being the same loan. Neither side reports borrower names in this pairing.

---
*Everything below was written AFTER the rule above was committed (`0b2eeb897`, 2026-10-01 12:50 ET).*

## 1. Sources (all fetched 2026-10-01)
| Doc | Filing | Use |
|---|---|---|
| AAIA Q2-2026 NAIC quarterly statement | ir.athene.com statutory page, `…/22562/pdf/2Q+2026+AAIA+Statement.pdf` (PDF dated 2026-08-13; sha256 `96a8d3c4…`) | Population A: Schedule B Part 2 rows dated 04/24/2026 |
| **ARI 10-Q Q1-2026** (portfolio table as of **2026-03-31**) | **acc 0001193125-26-187094, filed 2026-04-28** | **Primary R**: 52 senior + 2 subordinate loans, amortized cost **$8,918M** |
| ARI 10-K FY2025 (table as of 2025-12-31; Schedule IV) | **acc 0001193125-26-044725, filed 2026-02-10** | Secondary R; **Schedule IV is the only per-loan RATE source** (Loan A Office/UK **6.6%** principal $658,703K · Loan B Hotel/Various Europe **5.3%** $342,338K · Loan C Office/NYC **3.0%** $267,169K) |
| ARI 8-K, sale closing | **acc 0001193125-26-177686, filed 2026-04-24**, Item 2.01 | *"sold its commercial real estate loan portfolio (other than loans that were repaid prior to closing or are expected to be repaid in May) to Athene [Holding Ltd.] … cash consideration of approximately $8.6 billion … 99.7% of the total commitment amount"*. **No loan list** (schedules omitted under Reg S-K 601(a)(5)). |
| AANY Q2-2026 statement | same IR page, `…/22561/…AANY…` (367 pp) | Where did the remainder go? |
| ALRe Q2-2026 statutory FS | same IR page, `…/22564/…ALRE…Q2'26.pdf` (8 pp) | Same |

⚠️ **Extraction correction disclosed:** the first strict run read six NY rows that have no loan number as city "YORK" (a parse defect). It was fixed BEFORE the verdict below, and the fix moved the strict result from 30.7% to 31.4%. The rule itself was not changed.

## 2. STRICT RESULT, by the pre-registered rule
| Reference table | MATCH rows | MATCH $ | % of A's $7,405,267,470 |
|---|---:|---:|---:|
| **ARI 3/31/2026 (Q1 10-Q)** | **16 of 62** | **$2,328,729,691** | **31.4%** |
| ARI 12/31/2025 (10-K) | 19 of 62 | $2,893,094,060 | 39.1% |

**Rate condition (only 2 loans testable):** ARI Loan A London office **6.6%** ↔ AAIA LONDON GBR **6.600%** $668.3M (+3.9% vs 3/31 balance) — **exact rate**. ARI Loan C NYC office **3.0%** ↔ AAIA NEW YORK NY **3.000%** senior $262.9M + mezz $6.3M sharing one collateral value ($640M) = $269.1M (−0.7%) — **exact rate**. ARI Loan B (Hotel/Various Europe, 5.3%, $333M at 3/31): **no AAIA row at that rate or size**, so it is not at AAIA.
**Unmatched AAIA rows ≥ $100M:** several (e.g. "Delaware" DEU $261.5M, Green Oaks IL $191.7M, El Paso TX $180.0M, Woodland Hills CA $123.2M) with no ARI loan in that city.

### ⇒ VERDICT BY THE LETTER: **UNDETERMINED** (31.4%, which is ≥25% and <75%; large unmatched rows remain). Not CONFIRMED, not REFUTED.

## 3. Why the strict rule could not reach a verdict — POST-HOC, NOT part of the test, evidence-graded
1. **ARI discloses ~$3.1B of its $8.9B book only as "Various, US / UK / Europe / Germany / Sweden"** (16 loans). Rule 1 needs a city, so those loans cannot MATCH by construction. Several AAIA cities with no ARI city loan (El Paso, Green Oaks, San Bernardino, Woodland Hills, Flushing, Stockholm, Leicester, Essex, "Seven Beach") are **consistent with** being collateral under those portfolio loans. **Consistent is not proven.**
2. **Tranches.** AAIA books senior and mezz pieces as separate rows sharing one collateral value. 🔑 **The strongest identity evidence in the set:** ARI footnote (2) says #11 ($112M) and subordinates Sub1 ($28M, risk 5, net of specific CECL) and Sub2 ($23M) are *"secured by the same property"* in Manhattan. AAIA shows **three rows with identical collateral value ($1,130,000,000), all at rate 0.001%: $114.5M + $28.7M + $24.0M = $167.2M vs ARI $163M (ratio 1.026)**, each tranche within 2–5% of its ARI counterpart. A coincidental seller would not reproduce a three-tranche, same-property, non-accruing structure.
3. 🔑 **A BIMODAL SIZE RATIO — the §2.8 split showing its SHAPE.** Of the **12 cities where the pairing is unambiguous** (one AAIA position, one ARI loan, no assignment freedom), AAIA's cost over ARI's 3/31 balance is **0.636 · 0.789 · 0.794 · 0.800 · 0.805 · 0.806 · 0.808 · 0.995 · 1.000 · 1.008 · 1.024 · 1.033**. **Five loans sit at ~100% and six at 0.79–0.81.** Across all same-city one-to-one pairs within 0.75–1.10: **29 AAIA rows, $4,115.4M = 55.6% of A**, split **14 rows / $2,007.4M at ~1.0** and **15 rows / $2,108.0M at ~0.8** (11 of those 15 in 0.789–0.809). ⚠️ **Selection caveat:** in the all-pairs count, ties were broken toward 0.8, which inflates that cluster. The 12-pair unambiguous subset carries no such bias, and it shows the same two modes.
   **Reading (INFERRED):** on roughly half the loans AAIA took the whole loan; on the other half AAIA took **~80% and ~20% went to some other holder** — the Purchase Agreement's §2.8 "all or any portion" designation, operating as a **pro-rata split**. Implied elsewhere on the ~0.8 cluster alone: **~$0.5B**.
   **Where the ~20% did NOT go:** **AANY** — Q2 Schedule B Part 2 = **"NONE"** (zero mortgage acquisitions in the quarter). **ALRe** — mortgage loans on real estate **$907,960K → $1,056,765K** across the WHOLE first half (+$149M; unconsolidated BMA basis), far short of the ~$0.5B. **Not identified.** The remaining named candidates under §2.8 are ACRA 1/2 (63% third-party ADIP-owned), other affiliates, or Apollo managed accounts — **none of which publishes loan-level detail on this page.**
4. **Non-accruing loans bought at about ARI's impaired mark.** AAIA rows at rate **0.001%** (INFERRED: non-accrual coding) total **$265,554,918**. They pair to ARI's non-accrual and specifically reserved positions: **Cincinnati Retail(1), risk 5, $96M net of specific CECL ↔ AAIA "LIBERTY TOWNSHIP OH" $98.3M (1.024)** *(the city alias is INFERRED: ARI's Cincinnati retail loan is the Liberty Center mall in Liberty Township)*, plus the Manhattan three-tranche structure above. **AAIA's cost is 102–103% of ARI's carrying value NET of its specific allowance.** Athene took no discount below ARI's own impaired mark. Whether that is par on principal is not visible.

## 4. In plain words
- **What it tells us:** ARI's loan book very likely now sits, as a legal matter, mostly inside Athene's Iowa insurer — the post-hoc evidence (two exact-rate matches on ARI's largest loans, a three-tranche structure reproduced exactly, and a ratio pattern no coincidence produces) is strong. **The pre-registered test still grades UNDETERMINED**, because ARI disclosed a third of its book only as "Various" and because half the matched loans sit at AAIA at ~80%, which a ±15% band was not built to see. **The test is not upgraded after the fact.**
- 🔑 **The new fact:** the §2.8 designation was used, and its shape is visible — **whole loans to AAIA on some, ~80/20 splits on others.** Where the 20% went is **not** in any document Athene publishes on its statutory page (AANY none, ALRe too small).
- **What it does NOT tell us:** who bears the **economics**. AAIA cedes quota share and modco business to its Bermuda parent (AARe), whose consolidated group includes ACRA (63% owned by Apollo's ADIP funds). Legal holding at AAIA ≠ risk retained at AAIA. **Leg (b) stands: AARe's FY2025 related-party note discloses no allocation, and nothing here contradicts that.**
- **No trade read, no threshold move, no score move.** It is a visibility finding: the loans are now traceable quarter by quarter at AAIA (Schedule B Part 3 shows disposals and repayments; Q3 statement ~mid-November).

## 5. Next tests (named, not run)
① Pull AAIA's Q2 **Schedule B Part 1-equivalent / annual Schedule B** at FY2026 for carrying value vs cost on the 0.001% rows (does AAIA mark them below cost?). ② Search the ARI DEFM14A (acc 0001193125-26-119995, 2026-03-23) for any loan-level annex — not read today. ③ ACRA: whether Athene/Apollo filings name ACRA as a designee for the ARI portfolio.
