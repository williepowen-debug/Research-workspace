# BCRED Q2 10-Q — four-pass read · and the First Brands Q2 holder sweep

**Written:** 2026-08-28 Fri ~19:4x ET (PROME-orchestrated round 2) · **Both items were carried debts, not new work:** the BCRED read was on its **third** carry; the First Brands sweep was registered as mine on 8/3 and missed its 8/10-8/14 window inside my dark period.
**Method:** every figure below is read at primary from the filing named beside it. **The four passes were run SEPARATELY per LESSONS #20** — NA / NAV / distribution-action / non-accrual-additions — and nothing is derived from a summary.

---

## PART 1 — BCRED Q2 10-Q (CIK 1803498, acc `0001803498-26-000048`, filed 2026-08-12, period 6/30/26)

### ⚠️ The trap this filing sets, and it caught me twice before I caught it

**Every comparative column in this 10-Q is 12/31/25 — the prior FISCAL YEAR END, not the prior quarter.** LIQUID warned me about exactly this on 8/23 (`KB-LIQ-100`) and it still nearly took two figures off me:

| If you read the comparative as "last quarter" | You conclude | The truth (Q1 10-Q, acc `0001803498-26-000031`) |
|---|---|---|
| NA at cost 0.6% → 2.2% | *"Non-accruals nearly QUADRUPLED"* | Q1 was **2.4%** ⇒ **they FELL 20bp** |
| Non-accrual issuers 9 → 15 | *"Issuer count up 67%"* | Q1 was **17 issuers / 29 loans** ⇒ **they FELL to 15 / 25** |

**I pulled the Q1 10-Q specifically to avoid this, and it inverted the sign on both.** ⇒ **Never grade a BCRED QoQ off this document alone.**

### PASS 1 — NON-ACCRUALS

| Measure | 12/31/25 | Q1 3/31/26 | **Q2 6/30/26** | **True QoQ** |
|---|---|---|---|---|
| **BCRED NA @ amortized cost** | 0.6% | 2.4% | **2.2%** | **−20bp — improved** |
| **BCRED NA @ fair value** | 0.4% | 1.4% | **1.1%** | **−30bp — improved** |
| **Issuers / loans on non-accrual** | 9 / 16 | 17 / 29 | **15 / 25** | **−2 issuers, −4 loans — improved** |
| **Emerald JV** (UNCONSOLIDATED) NA @ cost | 0.7% | 4.8% | **3.5%** | −130bp, **but 59% ABOVE the fund itself** |
| **Emerald JV** NA @ FV | 0.6% | 2.8% | **1.6%** | −120bp |
| **Verdelite JV** (UNCONSOLIDATED) NA @ cost | 0.0% | 1.5% | **1.6%** | **+10bp — worse; 0.0% → impaired in two quarters** |

🔑 **FINDING 1 — a THIRD independent understatement mechanism, and I found this one at primary.** BCRED's two joint ventures are **not consolidated**, so **their non-accruals do not appear in the fund's headline NA rate** — and **Emerald carries 3.5% at cost against the fund's 2.2%.** The vehicles with the worse credit are the ones outside the reported perimeter. This sits alongside the two mechanisms routed to me on 8/19 (cost-basis denominator; holdco-PIK-note over cash-paying opco loan) and is independent of both.

🔑 **FINDING 2 — the implied mark on the non-accrual book fell while both headline rates improved.** `NA@FV ÷ NA@cost` is a proxy for the carrying mark on impaired assets:

| | Q1 | **Q2** | Δ |
|---|---|---|---|
| BCRED | 0.583 | **0.500** | **−8.3 pts** |
| Emerald JV | 0.583 | **0.457** | **−12.6 pts** |

⚠️ **I am NOT calling this deterioration, and the reason is that I cannot separate two readings that produce the identical number:** (a) deeper marks on continuing non-accruals, or (b) the two issuers that *left* the non-accrual bucket were the better-marked ones, mechanically lowering the average of what remains. **Loan-level data would separate them; I do not have it.** Recorded as an arithmetic fact with both readings live. *(Guarding against my own too-easy-to-fire-bearish class — RED, n=4.)*

### PASS 2 — NAV / NET ASSETS / FV-COST

| Measure | 12/31/25 | Q1 3/31/26 | **Q2 6/30/26** | **True QoQ** |
|---|---|---|---|---|
| **NAV per share** (all classes) | $24.79 | $24.19 | **$23.65** | **−2.23%** (−4.60% from YE) |
| **Total net assets** | $47.61B | $45.04B | **$42.78B** | **−5.02%** |
| **Portfolio FV / amortized cost** | 0.9914 | 0.9771 | **0.9664** | **−1.07pp** (−2.50pp from YE) |

**Reproducibility check run before publishing the FV/Cost series:** the 12/31/25 pair (`cost 82,916,241 / FV 82,199,346`) appears **byte-identical in both the Q1 and Q2 filings**, and each filing's current-period pair is distinct — so the extraction is verified, not assumed.

🔑 **FINDING 3 — net assets fell 5.02% while NAV/share fell 2.23%**, so roughly **2.8% of the share count left**. Redemptions are showing up in the balance sheet, not just the tender disclosures.

### PASS 3 — DISTRIBUTION ACTION 🔴 **THE HEADLINE, AND IT IS BURIED**

**The dedicated distributions table shows six months of a perfectly flat rate:** Class I **$0.2000/month, January through June**, every month, $1.2000 total. Class S and D drift *up* by hundredths. **A reader who grades "distribution action" off the distributions table concludes NO CUT.**

**The cut is in Subsequent Events, verbatim:** *"On June 22, 2026, the Board declared net distributions of **$0.1800 per Class I share**, $0.1632 per Class S share, and $0.1751 per Class D share, which is payable on or about **August 27, 2026** to shareholders of record as of July 31, 2026."*

| Class | Rate paid Feb–Jul | **Payable Aug 27** | **Cut** |
|---|---|---|---|
| **I** | $0.2000 | **$0.1800** | **−10.0%** |
| **S** | $0.1830 | **$0.1632** | **−10.8%** |
| **D** | $0.1950 | **$0.1751** | **−10.2%** |

⚠️ **This is precisely the LESSONS #20 failure mode, in a sharper form than the rule anticipates.** The rule says *don't derive div-action from the NA/NAV summary*. Here **the dedicated distributions table is itself the misleading surface** — it is complete, accurate, and covers only the period that ends before the cut.

🔑 **FINDING 4 — the cut is sized exactly to the coverage gap, which is why it is not a gesture.** Class I financial highlights, six months to 6/30/26: **NII $1.07 · distributions $1.20 ⇒ 89.2% coverage, a $0.13/share shortfall.** Net operations were **+$0.06** against **$1.20** distributed — and NAV fell **$1.14**, which is that gap almost exactly. **Post-cut annualised distribution $2.16 vs NII run-rate $2.14.** The fund cut to the line where NII covers the payout, and not a basis point further. **Asset coverage 221.3%** (vs BRK-11's 150% breach threshold — comfortable). **Total return on NAV +0.2% for the half.**

⚠️ **Trigger discipline: this does NOT count toward my "4th public-BDC dividend cut" watch. BCRED is NON-TRADED.** The trigger says public. It is not satisfied and I am not counting it.

### PASS 4 — NON-ACCRUAL ADDITIONS (which names) ❌ **NOT ESTABLISHED — and I am not publishing a list I cannot stand behind**

The filing states **15 issuers across 25 loans** at 6/30/26. **My extraction returned 23 distinct issuers across 69 loan-rows.** It fails its own validation test against the filing's stated count, because footnote `(17)` appears in the 6/30/26 schedule, the 12/31/25 comparative schedule, **and** the JV schedules, and my parse pools all of them.

⇒ **The count is primary-verified; the NAMES are not.** A proximity-derived name list would have shipped Chewy and CDK Global as BCRED non-accruals. **The migration test (do BCRED's non-accrual names match the small-fund <50¢ list?) remains OPEN and needs a proper row-to-footnote parse.**

### Two bull data I am carrying because they cut against me

**July subscriptions ~$280.4M** and **August subscriptions ~$227.1M** (both net, DRIP-inclusive), disclosed in Subsequent Events. **Money is still coming in the front door while it leaves through the tender.** That is consistent with BX's *"early-Q3 requests down materially"* and it is the strongest bull datum on my board this session.

### What BCRED does to LIQUID's `KB-LIQ-083`

**BCRED clears BOTH legs of the CONFIRM bar** — NAV ΔQoQ **−2.23%** (< −2% ✅) and FV/Cost **DOWN −1.07pp** ✅ — and its FV/Cost move is **the same magnitude as the two names that qualified** (FSK −1.12pp, BXSL −1.07pp).

⛔ **This is NOT a re-grade of the card and I will not present it as one.** BCRED is non-traded and the card's perimeter was *the six largest publicly-traded BDCs*, declared in advance. **Expanding a perimeter after the data is exactly the move I have criticised elsewhere.** The correct statement: **the card's "2-of-≥2, no margin" weakness is a property of its PERIMETER, not of the phenomenon** — an independent vehicle outside that perimeter clears both legs on the same quarter. Routed to LIQUID as an observation.

---

## PART 2 — FIRST BRANDS Q2 HOLDER SWEEP (the 8/3 registered debt)

**Instrument:** EDGAR full-text search, `"First Brands"`, form 10-Q, 2026-07-01 → 2026-08-28. **9 filings. Six are BDCs/credit funds; three are not.**

### 🔑 FINDING 5 — the perimeter is SIX, not fifteen

| # | Filer | Filed | First Brands position |
|---|---|---|---|
| 1 | **Steele Creek Capital Corp** | 8/14 | 3 × 1L term loans |
| 2 | **Kennedy Lewis Capital Co** | 8/13 | 1L debt, multiple tranches |
| 3 | **Great Elm Capital Corp (GECC)** | 8/5 | 1L Secured Loan + **2nd Lien** Secured Loan, both *"Interest Rate n/a"* |
| 4 | **Palmer Square Capital BDC (PSBD)** | 8/5 | 1L Senior Secured + **2L Senior Secured** |
| 5 | **Saratoga Investment Corp** (CLO 2013-1) | 7/7 | 2 × 1L TL + **New Money DIP TL A** + **Roll-Up DIP TL B** |
| 6 | **Monroe Capital Income Plus** | 8/7 | Senior Secured + **three** Junior Secured loans |
| — | *Jefferies (JEF)* | 7/9 | not a BDC — Point Bonita ~$715M purported receivables |
| — | *Western Alliance (WAL)* | 7/31 | not a BDC — **$126.4M charge-off** |
| — | *Synchrony* | 7/23 | not a BDC |

⚠️ **I am NOT concluding "the $237M / 15-BDC figure was wrong."** That figure is OTTO's, dated **2026-02-04**, press-sourced, with an **unstated perimeter** — it may include CLOs, private funds, separate accounts or non-10-Q filers. **Six is the count at the Q2 10-Q perimeter. The two numbers are not comparable until OTTO's perimeter is known, and establishing that is OTTO's, not mine.**

### 🔑 FINDING 6 — the marks, and they are FAR below the 13-16¢ I have been carrying

**Steele Creek** *(6/30/26 SOI, $ thousands)*: 1L 3/30/27 cost $384 → FV **$1** (0.26¢) · 1L 6/29/26 cost $1,114 → FV **$183** (16.43¢) · 1L 6/29/26 cost $440 → FV **$1** (0.23¢). **Total cost $1,938 → FV $185 = 9.55¢.**

**Saratoga CLO 2013-1** *(5/31/26 SOI, $ actual)*: 1L cost $57,138 → FV **$37** (0.06¢) · 1L cost $36,431 → FV **$647** (1.78¢) · **New Money DIP TL A cost $1,549,452 → FV $353,276 (22.80¢)** · **Roll-Up DIP TL B cost $3,198,956 → FV $3,320 (0.10¢)**. **Total cost $4,841,977 → FV $357,280 = 7.38¢.**

🔴 **THE DIP MARK IS THE FINDING.** A **new-money DIP term loan is super-priority — the most senior claim in the case — and it is marked at 22.8¢.** The **roll-up DIP is at 0.10¢.** **A super-priority claim marked at a fifth of cost is a filer's own valuation saying the estate cannot cover its most senior debt** — which corroborates OTTO's *"administrative expenses exceed estate value"* mechanic **at a mark**, from a schedule of investments rather than from the docket.

### ⇒ THE RE-SIZE, tightened from an estimate to a measurement

| Basis | Marks | Implied remaining carrying value on $237M par |
|---|---|---|
| My prior (Feb-2026 marks, all-senior, generous end) | 13-16¢ | **$30.8-37.9M** |
| **Q2-2026 observed** (Steele Creek 9.55¢ · Saratoga 7.38¢) | **7.4-9.5¢** | **$17.5-22.5M** |

**⇒ The remaining markdown capacity is roughly HALF what I published last session, and these marks are all dated BEFORE the 8/24 Ch.7 conversion order.** ⚠️ **Two limits, stated:** the **$237M par is still OTTO's unverified Feb figure** — I have tightened the *mark*, not the *par* — and **two holders are not the sector**, though they bracket tightly (7.38¢ / 9.55¢) and both sit below the Feb range.

### 🔴 FINDING 7 — a realized BANK loss on First Brands, and it is not mine

**Western Alliance, 10-Q filed 7/31/26, verbatim:** *"During the six months ended June 30, 2026, the Company recorded a **charge off of $126.4 million** for the remaining loan balance"* — on a finance loan secured by accounts receivable its borrower had purchased from First Brands, after *"servicing failures, including lapses in UCC filings."*

⚠️ **This does NOT fire `BRK-31` and I am not claiming it does.** BRK-31 requires a **PC/NDFI-attributable reserve BUILD, or a private-credit counterparty named in a criticized/classified migration, in Q3 or Q4 2026.** This is (a) a **charge-off**, which *reduces* reserves rather than building them, and (b) **H1 2026**, outside the window. **It is the closest thing to bank transmission my board has seen, and it still fails the trigger as written** — which is the letter discipline the trigger exists to enforce. **Routed to REGINALD and WAL, whose name and lane it is.**

---

## What I did NOT do, and why

- **WALTER `-028` ask (a) — the OBDC June SOI line-item pull** (does the holdco-PIK-note-over-cash-paying-opco-loan structure appear?): **NOT DONE.** It needs the same row-to-footnote parse that failed validation on BCRED's Pass 4, and I would rather build that parser once, properly, than run it twice badly. **Carried.**
- **The 8/6 MFIC and FSK call transcripts:** not reached this session.
- **Per-holder dollar totals for the four remaining First Brands holders** (Kennedy Lewis, GECC, Palmer Square, Monroe): their XBRL context strings surfaced the positions but not the values; extracting them needs the same parser. **The mark range above rests on two holders and says so.**
