# NDFI Exposure — $2.74B Shadow CRE Analysis

**Last Updated:** 2026-04-23 (Q1 2026 update section added; structural analysis below unchanged) | **Sources:** FFIEC Call Report Q4 2025 (RSSD 107244), OZK Q3 2025 + Q1 2026 Earnings Calls, Q1 2026 Management Comments (Figure 17), Deep Research (Gemini/ChatGPT/Perplexity/Claude, Mar 23 2026)

---

## What Is NDFI?

Non-Depository Financial Institutions — entities that lend money but aren't banks. When OZK lends to an NDFI, it's lending to a lender: debt-on-debt. If the NDFI's own borrowers default, the NDFI can't repay OZK. OZK's own glossary defines NDFI as "lender-finance or loan-to-lender exposures, such as **BDCs and similar entities**."

This matters because OZK characterizes its CIB group (which houses most NDFI lending) as "diversification away from RESG." The data says otherwise.

---

## 🆕 Q1 2026 UPDATE — Competitive Displacement on 2 of 4 CIB Lines

**Source:** Jake Munn (CIB President), Q1 2026 earnings call (Apr 22, 2026). **Not in** the written Management Comments PDF — spoken-only disclosure, an asymmetry worth flagging.

### What Munn disclosed

**Fund Finance / capital-call subscription facilities** (touches RCONPV07 bucket, $772M):
> "We've had to pull back a little bit in our capital call subscription facilities just due to increased pressure there, specifically from non-bank lenders and then insurance companies who have really entered that market and pushed down a little bit on pricing."

**Lender Finance Group** (touches RCONPV06 bucket, $1,201M):
> "If we're looking at our lender finance group too, we've seen some pricing and structure compression there too."

**Strategic pivot framing:**
> "If we see a slowdown or an increased competition or decreased pricing, let's say, in ABLG, it affords us the opportunity to push more into our CBSF or NRG business lines."

### What this changes

Two of the four NDFI/CIB sub-segments are in **managed retreat on new originations**. Legacy book is still growing: Fund Finance component of CIB reported **$210M Q1 2025 → $1,275M Q1 2026** (Figure 17, Mgmt Comments p.16). The pullback is at the forward edge; the stock is still there and still earning.

| Pre-Q1 2026 framing | Post-Q1 2026 disclosure |
|---|---|
| OZK as growth-focused Fund Finance supplier | OZK as cyclical market participant losing price/structure discipline |
| "Lends to the lenders" (one-directional relationship) | "Lends to AND competes with the lenders" — losing at the margin in 2/4 sub-segments |
| $2.74B book directionally growing across the board | Book still growing net (legacy roll-in), but pricing power eroded on new originations in Fund Finance + LFG |
| CIB "diversification away from RESG" narrative credible | CIB growth story concentrated in remaining lines (CBSF, NRG, EFG) — narrower than prior depiction |

### Why the asymmetric disclosure matters

Munn's statements did not appear in the written Management Comments PDF, which is the durable investor-facing record. Verbal disclosure reaches attentive call listeners; written disclosure reaches every shareholder and analyst who only reads the deck. Silencing the pullback in writing suggests management discomfort formalizing the competitive problem — consistent with the "extend-and-pretend" posture noted elsewhere in thesis. Pattern to watch: does Q1 2026 10-Q (~May 5) pick this up, or does the silencing persist?

### Thesis implication

**Not a thesis invalidator.** The structural wrong-way-risk analysis below (sub-variant A/B, CRE correlation, Gleason Q3 2025 admission) remains intact. The $2.74B is still on balance sheet, still CRE-correlated, still subject to the same four-channel transmission logic.

**What the update refines** is the NARRATIVE layer: OZK's CIB "diversification away from RESG" story is harder to sustain when 2 of 4 CIB lines are in competitive retreat. The bank is now simultaneously *exposed to* and *losing ground to* the same non-bank / insurance / private-credit ecosystem. That's a specific new form of wrong-way risk: the counterparty cohort that could stress OZK's NDFI book is the same cohort currently displacing OZK from the pricing table.

See `TRANSMISSION.md` §Channel 3 for how competitive displacement amplifies takeout-disappearance mechanics.

[KB-OZK-186 Fund Finance pullback | KB-OZK-187 LFG compression | KB-OZK-188 asymmetric disclosure]

---

## FFIEC Call Report Breakdown (Q4 2025, $000s)

| RCON Code | Category | Amount | % of NDFI | CRE Correlation |
|-----------|----------|--------|-----------|-----------------|
| RCONPV06 | Business credit intermediaries | $1,200,531 | 43.8% | **HIGH** — CEO confirmed CRE debt funds |
| RCONPV07 | Private equity funds | $772,151 | 28.2% | **MODERATE-HIGH** — subscription lines, LP stress = risk |
| RCONPV08 | Consumer credit intermediaries | $48,285 | 1.8% | LOW — immaterial |
| RCONPV09 | Other NDFIs | $721,546 | 26.3% | **MODERATE** — likely BDCs, mortgage REITs, specialty finance |
| **RCONJ454** | **Total NDFI** | **$2,742,514** | **100%** | **Est. 50-75% CRE-correlated** |

[KB-OZK-021]

---

## What Each Category Actually Is

### Business Credit Intermediaries ($1.20B) — RCONPV06
Companies whose business IS lending: bridge lenders, specialty finance, non-bank CRE lenders. OZK's CIB labels this as ABLG (asset-based lending) + CBSF (sponsor finance). But the CEO confirmed a significant portion is actually RESG-managed loans to CRE debt funds. Named counterparties (Acore, Mesa West, Affinius, Related Fund Management) are **all CRE debt funds**. Zero non-CRE entities found in this sub-category.

**Revised CRE correlation: 70-80%.** Conservative given named counterparty composition.

### Private Equity Funds ($772M) — RCONPV07
Subscription line facilities — secured by LP capital commitments, not underlying assets. In theory lower risk (LP commitments are collateral). In practice:
- If LPs face capital calls during a downturn, subscription lines become harder to call
- OZK's relationship base skews heavily CRE — their PE fund clients likely include real estate-focused funds
- OZK attends Fund Finance Association events alongside Ares and Apollo representatives

**Revised CRE correlation: 40-60%.** Not directly CRE-collateralized but counterparty base is CRE-tilted.

### Other NDFIs ($722M) — RCONPV09
The black box. Only confirmed BDC relationship: Prospect Floating Rate Fund ($75M revolving, OZK as facility agent) [KB-OZK-027]. Comprehensive SEC search ruled out ARCC, OBDC, BXMT, KREF, LADR, TRTX, GBDC, Claros, Ready Capital, Arbor. OZK's NDFI book tilts toward mid-market CRE-focused funds, not large institutional BDCs.

Also includes non-CRE CIB relationships: Regents Capital ($150M revolver, equipment leasing), Aequum Capital/Castlelake ($140M syndicated revolver), Mach Natural Resources ($37.2M energy term), Archrock Services ($75M industrial revolver).

**Revised CRE correlation: 40-50%.** Mix of CRE-adjacent and genuinely diversified.

### Consumer Credit ($48M) — RCONPV08
Consumer lenders. Immaterial. Zero CRE linkage.

---

## 🔴 CEO Admission: NDFI = RESG Loans

**George Gleason, Q3 2025 Earnings Call (Oct 17, 2025):**

> "I'm -- you were talking about the NDFI loans, Jake, from your CIB group. But **a chunk of our NDFI loans that show up on our call report are actually RESG loans.** And this goes back to our long-standing relationships with a lot of the debt funds that do commercial real estate lending."

[KB-OZK-022]

**Extended version (Perplexity research):**

> "We compete with those guys, a lot of times, if they win a unitranche deal, they'll **bifurcate it into a senior mezz and we're the senior lender and they're the mezz**, sometimes they want to hold that whole loan on their books, but **leverage it with a loan from us**. And we do a **loan to lenders** or an NDFI loan to those guys."

This confirms two structural sub-variants:

| Sub-Variant | Structure | OZK Risk |
|-------------|-----------|----------|
| **A: Co-lending** | OZK senior + fund mezz on same project | No fund-level exposure — OZK has direct lien on property |
| **B: Back-leverage (Note-on-note)** | Fund pledges its entire loan to OZK as collateral | **Direct fund-level credit exposure** — if fund fails, OZK takes impaired CRE loan as collateral |

Sub-variant B is the dangerous one. If a CRE debt fund can't repay OZK, OZK inherits the fund's loan — which may itself be impaired CRE.

---

## Shadow CRE Estimate

### Conservative (Low CRE Assumption)
| Category | Amount | CRE % | Shadow CRE |
|----------|--------|-------|------------|
| Business credit intermediaries | $1,201M | 50% | $600M |
| PE funds | $772M | 30% | $232M |
| Other NDFIs | $722M | 30% | $217M |
| Consumer credit | $48M | 0% | $0 |
| **Total** | | | **$1,049M** |

### Aggressive (High CRE Assumption — post-counterparty-identification)
| Category | Amount | CRE % | Shadow CRE |
|----------|--------|-------|------------|
| Business credit intermediaries | $1,201M | 80% | $960M |
| PE funds | $772M | 60% | $463M |
| Other NDFIs | $722M | 50% | $361M |
| Consumer credit | $48M | 0% | $0 |
| **Total** | | | **$1,784M** |

### Central Estimate: $1,250M–$1,750M shadow CRE via NDFI

---

## Adjusted CRE Concentration (Including Shadow NDFI + Memo Item 3)

| Metric | Reported | + Shadow CRE + MI3 |
|--------|---------|-------------------|
| CRE / Tier 1 | 358% | **411-420%** |
| CRE / Total RBC | 302% | ~340-350% |

[KB-OZK-013]

OZK's reported 358% CRE/Tier 1 understates true CRE exposure by ~55-62 percentage points. The bank is not diversifying away from CRE through CIB — it's adding another layer of CRE exposure through intermediaries.

---

## Wrong-Way Risk

The critical issue isn't just the dollar amount — it's **correlation**. In a CRE stress scenario, all four NDFI channels are hit by the same macro shock:

1. OZK's direct CRE loans go nonaccrual (already happening — $256.7M noncurrent)
2. Bridge lenders OZK lent to ($1.2B) can't collect from the same stressed CRE borrowers
3. PE funds ($772M) face NAV declines and LP reluctance to fund capital calls
4. BDCs/specialty finance ($722M) face their own credit stress

This is **positively correlated risk** masquerading as diversification. OZK's NDFI book amplifies CRE exposure when it should be hedging it.

---

## What We Still Don't Know

1. **Specific subscription line clients** — confidentiality agreements protect fund names
2. **Sub-variant A vs B split** — how much is co-lending (lower risk) vs back-leverage (higher risk)
3. **Double-counting** — OZK may finance both the CRE project (RESG) AND the debt fund on the same project (NDFI). This would be double exposure to a single asset.
4. **NDFI noncurrent status** — $2,703K C&I noncurrent is tiny vs $3.4B book, but fund defaults are binary (gate, margin call), not gradual [KB-OZK-027]

---

## Structural Mitigants

OZK's loan-to-lender model uses:
- **Low attachment points:** OZK finances senior 50-60% of property value; fund equity/mezz acts as buffer
- **Lock boxes:** Cash flows directed to OZK-controlled accounts
- **Third-party servicers:** Independent collateral verification

These protections are real but erosion-prone. Office LTV reappraisals jumping 52.9% → 98.9% [KB-OZK-015] show the senior buffer can be consumed faster than expected.

---

*Counterparty details → `COUNTERPARTY_WATCH.md` | Transmission mechanics → `TRANSMISSION.md` | Source research → `../research/NDFI_SHADOW_CRE_ANALYSIS.md`*
