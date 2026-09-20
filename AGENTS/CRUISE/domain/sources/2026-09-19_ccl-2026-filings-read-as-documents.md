# CCL — every 2026 filing re-read as a DOCUMENT (the method-defect sweep)

**Run:** 2026-09-19 Sat, CRUISE, Will-directed · **Closes the 🔴🔴 method defect** logged at KB-CRU-065/066
**Population:** all **35 non-Form-4 CCL filings of 2026** (CIK 0000815097), from the full submissions feed — not the 8-K index, and **not the `items` field**.
**Why:** this desk had been reading the submissions feed's **`items` tag** — filer-supplied header metadata — instead of the filings. A tag is not a document.

> ## ⚖️ THE SWEEP FOUND FOUR THINGS THIS DESK DID NOT HOLD, AND ONE OF THEM ARGUES AGAINST ITS OWN TRADE ROW
> **The single biggest is a $2.5B share buyback that has been running since April and had $2.11B left at the last disclosure.** It appears **nowhere** in `STATUS.md`, `TRADE.md`, `WATCHLIST_CCL_PREANNOUNCE.md` or `VX.tsv` — verified by grep, zero hits in all four.
> **The method defect is confirmed as the cause, exactly as predicted:** the Q1 earnings 8-K's own body says nothing but *"a press release … is furnished as Exhibit 99.1."* **All the content — the buyback, PROPEL, the whole quarter — is in the exhibit.** Reading the 8-K, or its `items` tag (`2.02,9.01`), returns nothing.

---

## ① 🔴 THE $2.5 BILLION BUYBACK — RUNNING, ACCELERATING, AND UNDERWATER

Board-approved **2026-03-27**; could not start until after the **2026-04-17** shareholder meetings (DLC unification voting period); **no expiration date.**

| Period | Shares (M) | Avg price | Remaining authorisation |
|---|---:|---:|---:|
| Mar 2026 | — | — | $2,500M |
| Apr 2026 | 3.4 | $26.56 | $2,410M |
| **May 2026** | **11.7** | **$25.65** | **$2,110M** |
| **Q2 total** | **15.1** | **$25.85** | |

**Spend accelerated ~$90M (Apr) → ~$300M (May).** Cash-flow statement shows **$381M** of share repurchases in H1 FY26 against **$390M** in the equity statement — a settlement-timing difference, both disclosed.

**Alongside it: $414M of dividends paid in H1** ($0.15/quarter), with **">$800 million in total dividend distributions expected this year."**

### Why this matters, and it cuts against this desk's own row
- **`TRADE.md` row 2 is CCL puts (WATCH, conviction 2). An unexpired $2.11B authorisation, executing at an accelerating pace into a 52-week low, is a structural bid under the stock.** That is a **material adverse fact for a put thesis** and the desk has never held it. It does not by itself refute anything — but it must be on the row.
- ⚠️ **It is NOT an unambiguous bull signal either.** The average price paid is **$25.85 against a $21.84 close — the repurchased stock is 15.5% underwater**, and the cash went out while fuel costs rose 29% YoY. **Buying your own shares 15% higher than today is evidence of conviction OR of poor timing; the filings cannot distinguish them.**
- **⛔ Jun–Aug activity is UNKNOWN and undisclosed.** No 8-K reports buybacks, and CCL has filed none since 8/5. **The 2026-09-29 print is the first disclosure of Q3 repurchases** — a specific, dated thing to read off it.

### 🔑 AND IT CONFOUNDS `CRU-08`, WHICH IS THIS DESK'S LOAD-BEARING TEST
`CRU-08` computes the fuel-attributable EPS hit as CCL's **$56M per 10% fuel move ÷ 1,377M adjusted diluted shares = $0.041/share per 10% overshoot**, and asks whether the hit is ≤$0.10.

**But 1,377M is CCL's own 3Q guide share count, set before an unknown quarter of repurchases.** Scenario arithmetic on a fixed $1.86B adjusted net income:

| Further shares retired | 3Q adj diluted | EPS uplift |
|---:|---:|---:|
| 15.1M (one more Q2-sized quarter) | 1,361.9M | +1.11% (~+$0.015) |
| 30.0M | 1,347.0M | +2.23% (~**+$0.030**) |
| 37.5M (May's pace sustained) | 1,339.5M | +2.80% (~+$0.038) |

**⇒ A 30M-share retirement is worth about as much EPS as a 7–8% fuel overshoot costs.** The buyback can **mask most of a 10% fuel overshoot in the EPS line.**

⛔ **`CRU-08` IS NOT BEING RE-TUNED. It is OPEN and inside its window, and this desk does not re-spec a live prediction on new information** — the CRU-05 precedent. The row resolves exactly as written, on CCL's published fuel/mt and its own sensitivity table. **This is registered as a DISCLOSED CONFOUND to be recorded at resolution**, and the remedy is to read the **dollar** fuel line and the **share count** separately rather than inferring fuel from an EPS beat or miss.

---

## ② 🔴 THE FY26 YIELD GUIDE WAS ALREADY CUT 100bp — AND THE EPS GUIDE WAS NOT

This desk held the Q2 numbers but never the Q1 ones, so it never saw the **trajectory**:

| FY2026 guidance | Q1 (2026-03-27) | Q2 (2026-06-23) | Δ |
|---|---:|---:|---:|
| **Net yields, constant currency** | **~+2.75%** | **~+1.75%** | **−100bp** |
| Adjusted EBITDA | ~$7.19B | ~$7.11B | −$80M |
| Adjusted net income | ~$3,070M | ~$3.07B | flat |
| **Adjusted EPS, diluted** | **~$2.21** | **~$2.22** | **+$0.01** |
| Fuel + FX hit *in the quarter* | $54M / **$0.04** | $73M / **$0.06** | +$19M |

**🔑 CCL cut its revenue-quality guide by a full point and its EPS guide went UP a cent** — held together by cost efficiency and a shrinking share count. **That is precisely the configuration in which a Q3 EPS beat can coexist with continued yield deterioration**, and it is the strongest reason to grade the print on the **yield line**, not the EPS line.

**Consequence for exit rule 1:** the K-shape kill needs *"CCL and RCL both guide FY yields DOWN."* **CCL has already done so once** — the second limb is **half-satisfied before the print**, which the desk did not know.

**Fuel is biting but is not the swing factor CCL names:** *"The net impact of fuel prices and currency on the company's June guidance compared to prior guidance was less than $0.01 per share."* And **fuel consumption per ALBD fell 4.7% in Q1** — efficiency partially offsetting price per tonne, a lever absent from this desk's $/mt-only framing.

---

## ③ 🟠 CCL REDEPLOYED AWAY FROM ARABIAN GULF VOYAGES — THE `VX-CRU-04` CAVEAT, NOW WITH A NUMBER

CCL's Q2 bridge: FY net yields **+1.75% CC, "2.25 percent after reflecting the impact of the summer 2025 close-in decision to redeploy away from the previously planned first quarter 2026 Arabian Gulf voyages** and the impacts of loyalty program accounting."

**⇒ A Big-3 operator withdrew from Gulf deployment and it is worth roughly 50bp of full-year net yield.**

⚠️ **This does NOT trip `VX-CRU-04` and I am not moving the score.** The band counts **newly announced** Big-3 Gulf/Red Sea/Suez cancellations or reroutes **since 2026-07-02**; this decision was taken in **summer 2025** and therefore sits before the cutoff. The literal count of 0 stands.

**But it is the concrete, dollar-quantified instance of exactly the defect CATO R4 named** — *"a start date after the withdrawals can read zero because the disruption already happened."* The GREEN(1) is measuring *no new announcements* while CCL carries a **quantified, named yield drag from a prior Gulf withdrawal.** ⇒ **The "establish scheduled exposure before reading zero as low stress" item is no longer hypothetical; it has a 50bp price tag.**

---

## ④ 🟢 THE $500M SECURED NOTE REDEMPTION — CONFIRMED AT PRIMARY, AND IT SETTLES THE RATING QUESTION

**8-K 2026-08-05 (item 7.01), verbatim:** notice of redemption for **all $500,000,000 of the 7.000% First-Priority Senior Secured Notes due 2029**, redeemed **2026-08-15 at 103.50% of principal**, interest paid to holders of record 7/31.

> *"On June 25, 2026, pursuant to the indenture governing the 2029 Notes, **the collateral securing the 2029 Notes fell away upon the Company's receipt of a second investment grade credit rating**, resulting in the 2029 Notes becoming unsecured."*

**✅ This is primary confirmation of a read this desk had only from secondaries:** Moody's action on the *unsecured* notes was **mechanical notching after collateral release**, not a credit view. CCL's own filing says why.

**Cash and P&L, all inside Q3 FY26 (quarter ended 8/31):** ~**$517.5M** out (principal + 3.5% call premium ≈ **$17.5M**), against ~**$35M/year** of interest saved at 7.0%. The call premium is a debt-extinguishment charge — ordinarily excluded from **adjusted** EPS but present in **GAAP**. ⇒ **Another reason a GAAP-vs-adjusted gap at the print will not be about fuel.**

---

## ⑤ Q1 FY26 — A WHOLE QUARTER THE DESK DID NOT HOLD

Verified: `KB.tsv` held NCLH's and RCL's Q1 FY26 but **no CCL Q1 entry**.

Headline: *"ACHIEVES RECORD FIRST QUARTER OPERATING RESULTS AND RECORD BOOKINGS."* Diluted EPS **$0.19**, adj EPS **$0.20** (+50% YoY), record revenues **$6.2B**, record net yields **+2.7% CC** (beat guidance by >1pt), adj EBITDA **$1.3B**, adj cruise costs ex-fuel/ALBD **+5.3% CC**, customer deposits a Q1 record **~$8B (+~10% YoY)**, **"nearly 85 percent of 2026 already on the books"** (93% by Q2), bookings for 2026 **up double digits**, demand extending into **2028** sailings. Delivered **despite** a **$54M ($0.04)** fuel+FX hit versus guidance.

**PROPEL** (announced 3/27, targets to 2029): **>50% adjusted EPS growth from 2025**, **>40% of cash from operations distributed to shareholders (~$14 billion)**, highest adjusted EBITDA per ALBD in almost two decades, alongside an ROIC target.

---

## ⑥ The rest of the population — checked, nothing thesis-moving

| Filing | Read as | Finding |
|---|---|---|
| 8-K 2026-02-12 (1.01/3.03/9.01) | document | ADR Deposit Agreement Amendment No. 1 — plumbing for the DLC unification. No thesis content. |
| 8-K 2026-02-20 (1.01/9.01) | document | The **Unification Agreement** itself and its conditions. Structural. |
| 8-K 2026-04-20 (5.07) | document | Shareholder vote results — the meetings that released the buyback. |
| 8-K 2026-05-07 (nine items) | document | **DLC unification completed; redomiciled Panama → Bermuda as "Carnival Corporation Ltd."** Already held (KB-CRU-066), now read rather than stumbled on. |
| 10-K 2026-01-27 · 10-Q 2026-06-26 | already read | Unhedged verified at both. Unchanged. |
| S-4 / S-4-A / DEFM14A / 424B3 / POSASR / S-3DPOS / S-8s | scanned | Unification registration mechanics. |
| DEF 14A · ARS · SD · 13G/A | scanned | Governance, annual report, conflict minerals, passive holders. |

---

## What changes, and what deliberately does not

**Changes:** `TRADE.md` row 2 gains the buyback as a named adverse fact · `VX-CRU-03` gains the 100bp FY yield cut as a **dated prior** rather than a single reading · the `VX-CRU-04` denominator caveat gains a **number** · exit rule 1's second limb is **half-satisfied** · the watchlist's Q3 questions are re-based to read the **yield line and the share count**, not the EPS headline.

**Does NOT change:** no score moves, no band re-cuts, **`CRU-07` and `CRU-08` are untouched and stay OPEN as written** — both resolve on CCL's published figures, and the buyback is registered as a disclosed confound to record at resolution, not as grounds to re-spec a live row inside its window.
