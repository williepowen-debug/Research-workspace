# Delaware Life Q2-2026 statutory statement — W1 leg (a) resolved, and the flow figure I said did not exist

**SHADE · 2026-08-28 · primary-verified**
**Instrument:** *Quarterly Statement as of June 30, 2026 of the Delaware Life Insurance Company*, NAIC Life/A&H Association Edition, **barcode `79065202620100102`**, **NAIC cocode 79065, group 4794, state of domicile DE**, statutory home office 1209 Orange Street Wilmington DE, main administrative office 10555 Group 1001 Way, Zionsville IN.
**Retrieved 2026-08-28 from the issuer's own site** (see §1). **PDF sha-independent identity confirmed on the jurat page before any figure was read.**

---

## 1. 🔑 W1 LEG (a) IS RESOLVED — AND THE ANSWER IS THAT THE GATE DOES NOT EXIST

**The FORUM-5 obligation named three routes to Delaware Life's quarterly statutory statement: NAIC InsData · state-DOI · AM Best–CapIQ.** Tested from this box, 2026-08-28:

| Route | Result | Evidence |
|---|---|---|
| **AM Best** | ❌ **BLOCKED** | `web.ambest.com` redirects to a **Radware bot-manager challenge** (`validate.perfdrive.com`). Not a paywall — an automation wall. CapIQ is a separate paid S&P terminal. |
| **NAIC InsData** | ⚠️ **PAID, and it is the wrong product to have named** | NAIC's own page: "electronic delivery of the most up-to-date financial statement data", account + login required, pricing document on request (`idp@naic.org`). |
| **NAIC CIS** *(the free tier InsData's page points to)* | ✅ **OPEN and machine-queryable — but it is a DIRECTORY, not financials** | The CIS company dashboard is a Tableau workbook whose **CSV export works unauthenticated**: `https://tableau.naic.org/views/CIS-WB-CompanyResults-pantheonsite-live/CompanyResultsDashboard-pantheon.csv?:embed=y` → **5,262 companies, 1.89 MB.** This is where **cocode 79065** was established, along with the licensed-jurisdiction list. **It carries no statutory line items.** |
| **Delaware DOI** | ⚠️ **PARTIALLY open — exam reports, not statements** | Publishes **financial/market-conduct examination reports** (e.g. `insurance.delaware.gov/wp-content/uploads/sites/15/2025/06/DelawareLifeInsuranceCo2023web.pdf`, exam as of 2023-12-31) and filing *requirements*. **It does not publish the statements themselves.** |
| 🔑 **THE ISSUER'S OWN WEBSITE** | ✅ **FULLY OPEN — quarterly AND annual, free, no login, going back to 2022** | **`https://www.delawarelife.com/content/business-highlights`** |

### ⚠️ SELF-CORRECTION, RECORDED NOT SMOOTHED — my registered claim was WRONG

**On 2026-08-28 (touch 1) I registered, in STATUS §0l/§6 and in the packet to PROME, that the ~11/15 Q3 instrument is "GATED — my proven route is EDGAR N-VPFS, which is ANNUAL; the quarterly needs NAIC InsData / state-DOI."**

**That is false. The quarterly is published by the issuer, free, and has been all along.** Q1-2026 and Q2-2026 were both on the page while I was writing that the figure was unreachable.

**The defect is in the ENUMERATION, not in the routes.** W1 asked me to enumerate the *gated* routes, and I enumerated three gated routes and then treated that list as exhaustive — **I never asked whether an UNGATED route existed.** An opacity enumeration that only lists the gates will always conclude the thing is gated. `[[finding_unfetched_is_not_unavailable]]` — **second instance on this desk in 15 days** (the first was `fetch.py --history` on 8/13, where I declared a capability absent after mis-invoking it). **Same shape both times: a failed or unattempted lookup written up as an absence in the world.**
⇒ **Rule adopted:** *before recording a figure as gated, search for the issuer's own publication of it.* A regulated entity that wants to be sold by banks has its own reasons to publish statutory financials.

### The pull path, written down so it is reproducible

1. **Index:** `https://www.delawarelife.com/content/business-highlights` — lists DLIC quarterly (Q1–Q3) and annual statements, 2022→present.
2. **Direct assets (Brandfolder CDN, no auth, `curl -L` with a browser UA):**
   - **Q2-2026:** `https://cdn.bfldr.com/RVAMRK5C/at/vj8hnfkhth7kb7xn59pv96mt/DLIC_Quarterly_Statement_-_Q2_2026.pdf`
   - **Q1-2026:** `https://cdn.bfldr.com/RVAMRK5C/as/p8xjqzrzbkk4mtfhtbpgtft/DLIC_Quarterly_Statement_-_Q1_2026`
   - **FY2025 annual:** `https://cdn.bfldr.com/RVAMRK5C/at/593vjttrssmhjkcp9p7pcn/2025_DLIC_Annual_Statement_Final.pdf`
   ⚠️ **The CDN keys are opaque and per-asset — do NOT construct a Q3 URL by pattern.** Re-read the index page at ~11/15.
3. **Extract:** `pdfminer.high_level.extract_text`. **Verify the jurat page first** — barcode `79065<YEAR><Q>`, cocode 79065, "AS OF <date>" — before reading any figure.
4. ⚠️ **DLAC (Delaware Life and Annuity Company, cocode 17466) is NOT on this page.** Clear Spring is a separate filer. **This route covers DLIC only.**

⇒ **The ~2026-11-15 Q3 instrument is NOT gated. The "partially blind" qualifier STANDS** (Q3 covers 7/1–9/30; the pause surfaced 8/28), **but "behind a gate" is withdrawn.**

---

## 2. THE FLOW FIGURE — the pre-pause baseline, which I said did not exist

**Exhibit 1, Direct Premiums and Deposit-Type Contracts** (and cash-flow / Summary-of-Operations cross-reads). **1H-2026 = six months to 6/30/26, i.e. entirely BEFORE the 8/28 distribution pause.**

| Line | 1H-2026 | 1H-2025 | Δ YoY | FY2025 |
|---|---:|---:|---:|---:|
| Individual annuities (direct) | **$4,645,112,433** | $4,188,389,259 | **+10.9%** | $10,589,636,261 |
| Group annuities (direct) | $313,502,290 | $168,578,177 | +86.0% | $1,132,691,395 |
| Individual life | $8,392,944 | $9,530,060 | −11.9% | $16,822,682 |
| Group life | $(1,540,641) | $(3,042,801) | — | $503,109 |
| **Subtotal, direct premiums** | **$4,965,467,026** | $4,363,454,695 | **+13.8%** | $11,739,653,447 |
| Deposit-type contracts | $1,760,850,000 | $1,540,008,624 | +14.3% | $3,934,486,270 |
| **TOTAL direct premiums + deposit-type** | **$6,726,317,026** | **$5,903,463,319** | **+13.9%** | **$15,674,139,717** |

**Cross-reads (independent lines, same statement):** premiums collected net of reinsurance (Cash Flow L1) **$5,222,370,122 vs $4,321,012,422 = +20.9%** · net deposits on deposit-type contracts (L16.4) **$1,476,686,177 vs $1,222,669,445 = +20.8%** · net cash from operations **$3,447,262,388 vs $2,967,538,498 = +16.2%**.

### 🔑 AND THE OTHER SIDE OF THE FLOW — surrenders are growing ~3× as fast as inflows

| | 1H-2026 | 1H-2025 | Δ YoY |
|---|---:|---:|---:|
| **Surrender benefits and withdrawals** (SoO L15) | **$2,060,811,753** | $1,424,689,759 | **+44.6%** |
| Benefit and loss related payments (CF L5) | $3,106,777,909 | $2,401,428,614 | +29.4% |
| Annuity benefits (SoO L12) | $277,353,438 | $255,272,466 | +8.6% |
| Death benefits (SoO L10) | $78,952,801 | $85,874,059 | −8.1% |
| **Surrenders ÷ (direct premiums + deposit-type)** | **30.6%** | **24.1%** | **+6.5pp** |

**⇒ THE HONEST READ, in both directions:**
- **Gross inflows were still growing strongly into the pause (+13.9% YoY).** The channel Truist and Fifth Third closed was an **actively growing** one, not a dying one — which makes the pause *more* consequential, not less.
- **But outflows grew three times faster than inflows**, and the surrender-to-inflow ratio moved **24.1% → 30.6%**.
- **Net operations remain strongly positive and improved** ($3.45B vs $2.97B). **This is not a liquidity event.**

### ⛔ WHAT THIS DOES *NOT* DO — the relay framing is still not confirmed
The stripped relay phrase was *"flows are going the wrong way."* **This data does not confirm it, and must not be reported as confirming it:**
1. **It ends 6/30/26 — two months BEFORE the pause surfaced.** It says **nothing** about post-pause flows. The pause's effect is a **Q3/Q4** question.
2. **A rising surrender rate in a fixed/indexed annuity book is not per se distress** — surrender-charge periods expire on a schedule set 5–10 years ago, and the rate environment drives the rest. **No cohort or surrender-charge-period data is disclosed**, so the mechanical and behavioural components cannot be separated here.
3. **Net cash from operations rose.** A book in flight does not do that.
⇒ **Carry as: a primary PRE-PAUSE baseline showing inflows growing +13.9% and surrenders growing +44.6%. Nothing more.**

---

## 3. THE REMEDIATION PLAN IS NOT VISIBLY SHRINKING THE BOOK — and the share and the dollars disagree

**Note 5 / Note 10, verbatim:** *"The Company has private credit investments with certain counterparties in which the investment return is predominantly contingent on the performance of affiliates."*

| Component | **6/30/2026** | **12/31/2025 (Restated)** | Δ |
|---|---:|---:|---:|
| Short-term investments | $3,393,811,269 | $3,242,904,607 | +$150.9M |
| **Bonds** | **$13,090,915,234** | **$12,619,338,036** | **+$471.6M** |
| Other invested assets | $337,500,000 | $509,702,487 | −$172.2M |
| **Subtotal** | **$16,822,226,503** | **$16,371,945,130** | **+$450.3M (+2.75%)** |
| SAFA-linked (separate-account funding agreements) | $308,269,000 | $308,269,000 | flat |
| Trust notes (GA funding agreements + private-credit pool) | $512,787,235 | $326,225,000 | **+$186.6M (+57.2%)** |
| **TOTAL affiliate-contingent** | **$17,643,282,738** | **$17,006,439,130** | **+$636.8M (+3.74%)** |

✅ **TWO FIGURES I HAVE CARRIED SINCE 7/27 ARE NOW CONFIRMED EXACTLY, from an independent document:** the FY2025 affiliate-contingent book **$16.37B** (`$16,371,945,130`) and the bond leg **$12.62B** (`$12,619,338,036`). *(My carried "$17.24B related-party / 37.6% of GA" is the broader **Note 10 related-party** perimeter — a different, wider measure than this affiliate-contingent subset. **Do not conflate the two.**)*

### ⚠️ THE SHARE AND THE DOLLARS POINT OPPOSITE WAYS — report the PAIR

General-account net admitted assets grew **$45,903,192,677 → $51,249,394,609 (+11.6%)** in the same six months.

| Basis | 12/31/2025 | 6/30/2026 | Direction |
|---|---:|---:|---|
| **Affiliate-contingent, DOLLARS** | $16,372M | **$16,822M** | 🔴 **UP +2.75%** |
| **Affiliate-contingent ÷ GA net admitted, SHARE** | 35.67% | **32.82%** | 🟢 **DOWN 2.85pp** |

**Both are true. The denominator grew 11.6% while the numerator grew 2.75%, so the ratio fell while the book got bigger.** This is **exactly** the share-vs-quantity trap I adopted from WALTER/CREED's `-20260819-021-CORRECTION` earlier today — and it landed on my own primary vector within hours. ⇒ **Never quote the share alone, and never the dollars alone.**

**Consequence for §5 open question ③ ("does the remediation plan force sales — size/timetable/asset list?"):** **as of 6/30/26, NO net reduction is visible in dollars.** S&P's negative outlook cited *a remediation plan to reduce affiliated exposure*; six months in, **the affiliate-contingent book is larger in dollars and smaller as a share.** ⚠️ **A carrying-value increase is not necessarily net new purchases** (accretion, marks, reclassification are not separable here), and **the plan's own metric is not public** — if it is expressed as a ratio, it is being met; if in dollars, it is not. **Both readings stay live.**

---

## 4. CHARTER KEY RATIOS — what a QUARTERLY can and cannot support

| Charter ratio | Status | Value |
|---|---|---|
| **#2 Illiquidity Ratio** = (Mortgages + Schedule BA + illiquid ABS) / admitted assets, **>30% = red flag** | ⚠️ **FLOOR ONLY** | Mortgage loans **$3,289,484,998** (first liens $3,092,758,590 + other $196,726,408) + Schedule BA / other invested assets **$1,863,325,486** = **$5,152,810,484 ÷ $51,249,394,609 GA net admitted = 10.05%.** ⛔ **The illiquid-ABS leg is MISSING** — Schedule D asset-class detail is an **ANNUAL** schedule, and the bond line is **$33,715,375,268** with **$13.09B of it affiliate-contingent private credit**. ⇒ **10.05% is a FLOOR, not the ratio. I CANNOT say the illiquidity ratio is below 30% — only that the measurable components reach 10.05%.** |
| **#1 Affiliated Reinsurance Ratio** = reserve credit from affiliates / surplus, **>100% critical** | ❌ **NOT COMPUTABLE from a quarterly** | Requires **Schedule S**, an annual schedule. *Do not substitute the modco reserve component ($7,404,606,290 inside the $36.75B aggregate life reserve) — modco is not ceded reserve credit.* **Compute from the FY2025 annual statement, now known to be available (§1).** |
| **#4 TSR (Gober)** = higher-risk off-balance-sheet assets / surplus | ❌ **NOT COMPUTABLE, and the metric is under-specified** | Needs annual schedules **and** a definition of "higher-risk off-balance-sheet" that Gober has not published in testable form. **Allegation-grade metric — do not report a number for it.** |
| **#3 Capital Leakage** = fees to PE parent + intercompany notes | ⚠️ **PARTIAL** | Payable to parent/subsidiaries/affiliates **$87,748,549** · receivable from same **$3,050,325** net admitted (gross $9,402,513) · **GPIM (Guggenheim Partners Investment Management) manages $2,524,679,990** of DLIC investments (12/31/25: $2,566,569,758) and **$3,371,491** of its related-party investments. **Fee quantum not disclosed quarterly.** |

**Balance sheet, 6/30/2026, for the record:** total assets net admitted **$70,463,756,039** (GA **$51,249,394,609** + separate accounts **$19,214,361,430**) · total liabilities **$66,435,647,613** · **capital and surplus $4,028,108,426** (12/31/25: $3,838,481,434, +4.9%) · surplus notes $390,212,683 · AVR $582,613,409 · net income 1H26 $165,762,949.
✅ **Cross-check that validates my 7/27 read:** the prior-year column carries GA net admitted **$45,903,192,677** and total **$64,700,107,722** — **the "$45.90B general account" and "$64.7B admitted" figures I have carried since 7/27, confirmed exactly from an independent document.**

**Affiliate-contingent as a multiple of capital and surplus: 4.18×** (12/31/25: 4.27×). ⛔ **THIS IS A CONCENTRATION MEASURE, NOT A LEVERAGE RATIO, and it does not resurrect the retracted 12×** (`SIG-W-20260727-021`; the filing leverage figure is 5.1×). Reported because charter ratio #1's *form* is exposure-to-surplus; **do not relabel it.**

---

## 5. TWO CLEAN NEGATIVES, verified rather than assumed

1. ✅ **GOING CONCERN — NEGATIVE.** Note 1.D verbatim: *"There are no conditions or events, considered in the aggregate, that raise substantial doubt about the Company's ability to continue as a going concern."* ⚠️ **Recorded because I nearly got this backwards:** the phrase `raise substantial doubt` first surfaced as a bare fragment with its negation cut off by the extractor. **A truncated boilerplate negative reads as its own opposite.** Verified against the full sentence before writing.
2. ✅ **NO STATE PRESCRIBED OR PERMITTED PRACTICES.** Note 1.A reconciliation: *State Prescribed Practices* **N/A**, *State Permitted Practices* **N/A**; **NAIC SAP surplus = company state-basis surplus = $4,028,108,426**, no reconciling items. **Permitted practices are a registered SHADE mechanism** (the Athene Vermont captive failed RBC *without* one) — **for DLIC, at this date, that mechanism is NOT in use.** A clean negative on a standing suspicion, which is worth as much as a positive.

---

## 6. WHAT THIS SESSION DID NOT ESTABLISH

- **Post-pause flows.** The pause surfaced 8/28; this statement ends 6/30/26. **Q3 (~11/15) is the first instrument that sees any of it, and it sees at most one month.**
- **Clear Spring Life's own figures.** Separate filer, not on this page. **Still open.**
- **Whether the affiliate-contingent increase is new purchases** vs accretion/marks/reclassification. Not separable from a quarterly.
- **The remediation plan's own metric** (dollars or ratio). Not public — and it decides which of §3's two readings is the operative one.
- **NAIC SVO override count.** Not in this instrument; a separate NAIC surface. **Not attempted this session — recorded as owed, not as zero.**
