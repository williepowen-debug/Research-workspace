# FDIC 2023 Signature Bank loan sale — transaction economics, and whether it can inform any FLG loss rate

**Written:** 2026-09-27 (Sun), CREED, on PROME task **WQ-309** (Will 17:44 ET; scope `PROME/plans/2026-09-27_signature-sale-relevance-SCOPE.md`, `6102d9336`). Parent synthesis §8 item 4.
**Sources:** **PRIMARY FDIC press releases only**, fetched at fdic.gov 2026-09-27 (secondary press used solely to locate the primaries). URLs are the FDIC's canonical identifiers; the small-model fetch did not reliably read the on-page PR-number field, so each fact is cited to the URL I actually opened, not to a transcribed release number.
**Mandate limits (Will, verbatim):** *"establish the transaction economics first … 'No usable loss-rate comparison' is a valid result. If the FDIC disclosures are insufficient, identify exactly what is missing and return before expanding the research. No model or loss-rate changes."* Nothing here is asserted from memory. **No CREED or bridge loss rate, score, threshold, tool or trade changes.**

---

## §0. The answer first

1. **It was not a whole-loan sale. It was a series of joint ventures in which a private partner bought a *minority equity interest* (5% or 20%) and the FDIC-Receiver retained the majority (80–95%).** The FDIC kept most of the recovery upside and, on the market-rate venture, also *lent* the venture ~$6B (50% of its value). (pr23071, pr23105, pr23106, pr23107.)
2. **⇒ The headline dollar figures ($1.2B / $1.1B / $129M+$42M) are levered minority-equity checks, not clearing prices, and cannot be read as a loss rate.** Dividing a price by a loan balance ($1.1B ÷ $9.0B ≈ 12%) is meaningless — it is a 20% equity stake, not a price of the loans.
3. **The single value you *can* impute — and only for the WRONG property type.** The market-rate venture (Blackstone) disclosed its leverage, so its equity sale grosses up to an **implied venture value ≈ $12B on $16.8B of loans ≈ 71% of book (~29% implied discount)**. That is office/retail/**market-rate** multifamily — **explicitly excluding** rent-stabilized loans — so it does **not** inform FLG's rent-regulated pools. For the two **rent-stabilized** ventures the FDIC did **not** disclose leverage, so **no equivalent implied price is computable** from what is public.
4. **For FLG:** the closest collateral match (NYC rent-stabilized multifamily) is in the **CPC and Santander ventures**, which match FLG's NYC rent-regulated pools on **type, market and (presumed) lien** — but yield **no loss rate**, are priced **Dec-2023** (before the June-2026 NYC rent freeze and the 2026 rate move), and disclose **no performing/non-performing, vintage, or count split.** **Verdict: qualitative/directional relevance only; DOES NOT INFORM a loss rate for any FLG pool.** This is Will's "valid result."
5. **What is missing to make it a loss rate is named in §UNKNOWNS** — chiefly the FDIC's *realized receivership recoveries* on these ventures over 2024–2026, which live in FDIC receivership/DIF financial reporting, not in the 2023 sale releases.

---

## §A. OBSERVED — the transactions, from primary FDIC disclosures

### A1. What was marketed (pr23071, **Sept 5, 2023** — https://www.fdic.gov/news/press-releases/2023/pr23071.html)
- **"approximately $33 billion Commercial Real Estate (CRE) loan portfolio"** retained in the Signature Bank receivership.
- **"The majority of the CRE loan portfolio being marketed is comprised of multifamily properties, primarily located in New York City."**
- **"approximately $15 billion"** are multifamily loans **"that are rent stabilized or rent controlled."**
- Structure stated up front: **"the FDIC will retain a majority equity interest in the JV"**; **"the winning bidders, or partners, will act as the managing member … responsible for the management, servicing and ultimate disposition."**
- **Not disclosed:** loan count, performing vs non-performing, vintage, lien position.

### A2. The four completed ventures (Dec 2023)

| Venture (release) | Loan balance | Collateral | Partner | Partner equity | **FDIC-Receiver retained** | Price paid | FDIC financing to venture |
|---|---:|---|---|---:|---:|---:|---|
| **Market-rate CRE** (pr23105, **Dec 14**) | **$16.8B** | office, retail, **market-rate** MF; **"does not hold any … rent-stabilized or rent-controlled"** | Hancock JV Bidco (Blackstone-controlled) | **20%** | **80%** | **$1.2B** for the 20% | **YES — "financing equal to 50 percent of the Venture's value," a purchase money note ≈ $6B** |
| **Rent-stabilized (CPC set)** (pr23106, **Dec 15**) | **$5.8B** | rent-stabilized / rent-controlled MF | Community Preservation Corporation (nonprofit) | **5%** (in each of two ventures) | **95%** | **$129M and $42M** | **not stated in the release** |
| **Rent-stabilized (Santander)** (pr23107, **Dec 20**) | **$9.0B** | rent-stabilized / rent-controlled MF | SBNA Investor LLC (Santander Bank) | **20%** | **80%** | **$1.1B** for the 20% | **not stated in the release** |

- URLs: pr23105 https://www.fdic.gov/news/press-releases/2023/pr23105.html · pr23106 …/pr23106.html · pr23107 …/pr23107.html
- **Reconciliation (mine, arithmetic):** $16.8B + $9.0B + $5.8B = **$31.6B** ≈ the $33B marketed; rent-stabilized $9.0B + $5.8B = **$14.8B** ≈ the "$15B" marketed. The two rent-stabilized figures are **separate ventures**, not the same loans double-counted.
- **CPC's role** (pr23106): CPC is the **managing member** — "responsible for the management, servicing and liquidation of each Ventures' respective assets," a mission-driven partner buying a **5%** check ($129M+$42M). Whether CPC also manages the Santander venture is **not established** by the releases I read.

### A3. How the reported price was computed
- Each price is stated **"for a [5%/20%] equity interest"** in a named venture holding the loans — i.e. a price of an **equity stake in a JV**, not a price of the loans.
- The **only** venture whose leverage is disclosed is the market-rate one: partner equity $1.2B for 20% → 100% equity ≈ $6.0B; plus the ~$6B purchase-money note (= 50% of venture value) → **implied venture value ≈ $12B on $16.8B loans ≈ 71% of book.** This is an **implied strike valuation the FDIC used to sell 20%**, net of its retained 80% upside — **not a realized clearing price.**

---

## §B. SCENARIO ASSUMPTIONS — six-dimension transfer grade against each FLG pool

> **Overarching cap:** because the transaction yields **no loss rate** (§A3, §0.2–3), every verdict below is about **directional/qualitative** resemblance at best. **No pool can take a Signature-derived loss *rate*, because none exists.** The grade answers "does the Signature collateral resemble this pool?", which is the ceiling on any future use if a *recovery* figure ever becomes available (§Next observation).

Legend: ✓ match · ~ partial · ✗ no match · **?** not disclosed by FDIC. Reference set for a match = the **rent-stabilized ventures** (CPC $5.8B + Santander $9.0B), Dec-2023 pricing.

| FLG pool (10-Q 6/30/26) | type | market | vintage | appraisal/price date | lien | perf/def | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **MF nonaccrual, NYC ≥50% rent-regulated ($1,737M)** | ✓ | ✓ | ~ | ✗ (Dec-23, pre-freeze) | ~(presumed 1st) | **?** | **PARTIAL / directional only.** Best collateral match (NYC rent-stabilized MF). But no loss rate; Signature priced 18 months before the June-2026 freeze and the 2026 rate move; Signature's performing/NPL split is undisclosed, so it can't be matched to *nonaccrual*. |
| **MF criticized, NYC rent-regulated ($2,665M)** | ✓ | ✓ | ~ | ✗ | ~ | **?** | **PARTIAL / directional only.** Same as above; "criticized-accruing" cannot be isolated in the Signature pool. |
| **MF pass, NYC rent-regulated ($4,089M)** | ✓ | ✓ | ~ | ✗ | ~ | **?** | **PARTIAL / directional only.** A Dec-2023 *willingness to bid* on NYC rent-stabilized (under FDIC leverage/retained equity) is weak positive evidence a performing book has value; it is not a mark. |
| **MF nonaccrual, other ($395M)** | ~ | ✗ | ~ | ✗ | ~ | **?** | **DOES NOT INFORM.** "Other" = non-NYC and/or not ≥50% regulated; Signature is NYC rent-stabilized. |
| **MF criticized, other ($4,274M)** | ~ | ✗ | ~ | ✗ | ~ | **?** | **DOES NOT INFORM.** Wrong market/regulation profile. |
| **CRE nonaccrual ($471M)** | ✗ | ~ | ~ | ✗ | ~ | **?** | **DOES NOT INFORM.** FLG CRE is 40% industrial / 22% office; the Signature rent-stabilized ventures are multifamily. (The market-rate Blackstone venture holds office/retail, but its ~29% implied discount is a levered equity strike, not a loss rate, and is blended across types.) |
| **CRE criticized ($1,367M)** | ✗ | ~ | ~ | ✗ | ~ | **?** | **DOES NOT INFORM.** Same as above. |

**The expectation in the scope — "relevance likeliest for the NYC rent-regulated pools, least for CRE" — holds on collateral resemblance, but the loss-rate relevance is zero for all seven because the transaction is not a loss event.**

---

## §C. UNKNOWNS — exactly what the FDIC disclosures do NOT contain (so it cannot be a loss rate)

1. **Loan count** — not in any release.
2. **Performing vs non-performing split** — not disclosed for any venture. Without it, the Signature pool cannot be matched to FLG's nonaccrual / criticized / pass tiers.
3. **Vintage distribution** — not disclosed (loans originated pre-March-2023; no seasoning detail).
4. **Lien position** — not explicitly stated; presumed first-mortgage bank loans, **not confirmed at primary.**
5. **The "≥50% rent-regulated" cut** — the FDIC published "rent-stabilized or rent-controlled" ($15B), not FLG's "≥50% regulated by units" definition. The definitional overlap is close but **not identical.**
6. **Leverage on the rent-stabilized ventures** — the CPC and Santander releases do **not** state whether the FDIC provided a purchase-money note (the market-rate venture explicitly did, ~$6B / 50%). Without it, no implied venture value — and hence no implied price — is computable for the rent-stabilized loans.
7. **The venture asset carrying/contribution values** — not disclosed, so even the equity prices cannot be grossed to a per-loan value on the rent-stabilized side.
8. **Any realized recovery to date** — the FDIC retained 80–95% equity, so the *actual* loss (or gain) on these loans is realized over the workout and reported in **FDIC receivership / DIF financial statements**, not in the 2023 sale press releases. **This is the disclosure gap that matters most.**

Per the mandate, I am **stopping here rather than widening** into secondary reconstructions of any of the above. Items 1–8 are what FLG (and any future loss-rate use) would need, and item 8 is where it would have to come from.

---

## The next observation that would change the conclusion — named, with direction

**The FDIC's realized receivership recoveries on the SIG CRE / SIG RCRS rent-stabilized ventures**, as reported in FDIC receivership financial reporting or DIF financial statements over 2024–2026 (and, secondarily, any FDIC OIG review of the Signature loan sales). This is the **only** path from this transaction to a loss rate.
- **If those recoveries print materially below the loans' contributed value** → weak-to-moderate corroboration that NYC rent-stabilized bank loans of this vintage lose value in a workout → would *support* (not set) a stress on FLG's NYC rent-regulated pools. **Direction: toward higher loss.**
- **If recoveries print at or near contributed value** → corroborates the "par payoffs are happening" contrary evidence in CREED's 9/26 property test → **direction: toward the base, lighter stress.**
- **Caveat that would survive either way:** the Signature workout runs under FDIC-retained-majority economics, mission-driven servicing (CPC), and Dec-2023 pricing — a *different regime* from FLG's own book under the June-2026 freeze. It corroborates direction, never a transferable rate.

---

## Sources (all primary FDIC, fetched 2026-09-27)
- pr23071 (2023-09-05) — marketing announcement, $33B / ~$15B rent-stabilized / JV majority-equity structure: https://www.fdic.gov/news/press-releases/2023/pr23071.html
- pr23105 (2023-12-14) — market-rate venture, Blackstone/Hancock, $16.8B, 20% for $1.2B, FDIC 80%, ~$6B FDIC financing: https://www.fdic.gov/news/press-releases/2023/pr23105.html
- pr23106 (2023-12-15) — rent-stabilized, CPC, $5.8B, 5% for $129M+$42M, FDIC 95%: https://www.fdic.gov/news/press-releases/2023/pr23106.html
- pr23107 (2023-12-20) — rent-stabilized, Santander/SBNA, $9.0B, 20% for $1.1B, FDIC 80%: https://www.fdic.gov/news/press-releases/2023/pr23107.html
- Locator only (secondary, not relied on for any figure): FDIC 2023 press-release index; a govdelivery FDIC bulletin; trade-press headlines.
