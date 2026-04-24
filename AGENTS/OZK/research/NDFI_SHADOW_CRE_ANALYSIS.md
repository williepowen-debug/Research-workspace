# OZK NDFI Exposure — Shadow CRE Analysis
**Created:** 2026-03-23 | **Sources:** FFIEC Call Report Q4 2025, OZK Q3 2025 Earnings Call Transcript

---

## NDFI Breakdown (FFIEC Call Report, $000s)

| RCON | Category | Amount | % of NDFI | Likely CIB Sub-Group |
|------|----------|--------|-----------|---------------------|
| RCONPV06 | Business credit intermediaries | $1,200,531 | 43.8% | ABLG (asset-based lending) + CBSF (sponsor finance) |
| RCONPV07 | Private equity funds | $772,151 | 28.2% | Fund Finance (subscription lines, bridge loans) |
| RCONPV08 | Consumer credit intermediaries | $48,285 | 1.8% | Small — consumer lenders |
| RCONPV09 | Other NDFIs | $721,546 | 26.3% | Likely BDCs, mortgage REITs, specialty finance |
| **Total** | **RCONJ454** | **$2,742,514** | **100%** | |

---

## What Are These? (From OZK's Own Definitions)

OZK's Q3 2025 earnings call glossary explicitly defines:
- **NDFI** = "lender-finance or loan-to-lender exposures, such as **BDCs and similar entities**"
- **Fund Finance** = "lending exposures to investment funds, including **subscription facilities, bridge loans**"
- **CBSF** = "targeting **leveraged and sponsored borrowers**"

This is debt-on-debt: OZK lends to entities that themselves lend to or invest in real estate and leveraged corporate borrowers.

### 🔴 CEO CONFIRMS NDFI = RESG (CRE) LOANS

**George Gleason, Q3 2025 Earnings Call (Oct 17, 2025):**
> "I'm -- you were talking about the NDFI loans, Jake, from your CIB group. But **a chunk of our NDFI loans that show up on our call report are actually RESG loans.** And this goes back to our long-standing relationships with a lot of the debt funds that do commercial real estate lending."

The CEO just told us: the NDFI line on the Call Report contains CRE exposure that is managed by RESG, not CIB. These are loans to **CRE debt funds** — entities OZK has "long-standing relationships" with. This is not a thesis inference; it's management's own admission. The NDFI bucket is partially CRE by OZK's own classification.

This significantly narrows the uncertainty in our shadow CRE estimate. If Gleason calls it "a chunk" and specifically ties it to CRE debt funds, the 50-75% CRE correlation on business credit intermediaries ($1.2B) is likely conservative for that sub-category.

---

## Shadow CRE Assessment

### $1.2B Business Credit Intermediaries (RCONPV06)
These are loans to companies whose business IS lending — bridge lenders, specialty finance, non-bank CRE lenders. If their borrowers default (e.g., CRE sponsors can't pay bridge loans), the intermediary can't repay OZK.

**CRE linkage: HIGH.** OZK is the largest US construction lender. Their network of borrowers includes CRE bridge lenders and specialty finance firms. The ecosystem is self-referential — OZK lends to the construction borrower AND to the bridge lender who might provide mezzanine or takeout financing.

### $772M Private Equity Funds (RCONPV07)
Subscription line facilities — secured by LP capital commitments, not by underlying assets. In theory, low risk (LP commitments are the collateral). In practice:
- If LPs are themselves stressed (capital calls during a downturn), subscription lines become harder to call
- If the underlying fund holds CRE assets (real estate PE funds), the fund's NAV and LP willingness to fund are both CRE-correlated
- OZK's own relationship base skews heavily CRE — their PE fund clients likely include real estate-focused funds

**CRE linkage: MODERATE-HIGH.** Not directly CRE-collateralized, but counterparty and LP base likely CRE-correlated given OZK's network.

### $722M Other NDFIs (RCONPV09)
This is the black box. Could be BDCs (like ARCC, OBDC — our BROCK thesis targets), mortgage REITs, CLO managers, or other specialty finance. OZK's own glossary says NDFI = "BDCs and similar entities."

**CRE linkage: MODERATE.** BDCs are mostly corporate middle-market lending, not CRE. But some hold real estate debt. Mortgage REITs are directly CRE-linked. Without knowing the specific names, we estimate 30-50% CRE correlation.

### $48M Consumer Credit (RCONPV08)
Consumer lenders. Minimal CRE linkage. Immaterial.

---

## True CRE Exposure Estimate (Including Shadow NDFI)

### Conservative Estimate (Low CRE assumption for NDFI)
| Category | Amount | CRE % | Shadow CRE |
|----------|--------|-------|------------|
| Business credit intermediaries | $1,201M | 50% | $600M |
| PE funds | $772M | 30% | $232M |
| Other NDFIs | $722M | 30% | $217M |
| Consumer credit | $48M | 0% | $0 |
| **Total shadow CRE** | | | **$1,049M** |

### Aggressive Estimate (High CRE assumption)
| Category | Amount | CRE % | Shadow CRE |
|----------|--------|-------|------------|
| Business credit intermediaries | $1,201M | 75% | $900M |
| PE funds | $772M | 50% | $386M |
| Other NDFIs | $722M | 50% | $361M |
| Consumer credit | $48M | 0% | $0 |
| **Total shadow CRE** | | | **$1,647M** |

### Adjusted CRE Concentration

| Metric | Reported | + Shadow CRE (Conserv.) | + Shadow CRE (Aggr.) |
|--------|---------|------------------------|---------------------|
| CRE exposure | $19,876M | $20,925M | $21,523M |
| CRE / Tier 1 | 362% | **381%** | **392%** |
| + Memo Item 3 ($1.289B) | — | **405%** | **416%** |

🔴 **Including shadow NDFI + Memo Item 3, true CRE/Tier 1 is 405-416%** — not the reported 358%.

---

## Key Risk: Correlation in Stress

The critical issue isn't just the dollar amount — it's **correlation**. In a CRE stress scenario:
1. OZK's direct CRE loans go nonaccrual (already happening — $256.7M)
2. Bridge lenders OZK lent to ($1.2B) can't collect from the same stressed CRE borrowers
3. PE funds OZK lent to ($772M) face NAV declines and LP reluctance to fund capital calls
4. BDCs/specialty finance ($722M) face their own credit stress

All four channels are hit by the same macro shock. This is **wrong-way risk** — OZK's NDFI exposure is positively correlated with its direct CRE exposure when it should be diversifying.

OZK management characterizes CIB as "diversification away from RESG." The data suggests it's partial diversification at best — $2.74B in NDFI loans to entities whose businesses depend on the same credit cycle OZK's RESG is exposed to.

---

## NAMED COUNTERPARTIES — Deep Research (Gemini, Mar 23 2026)

Source: Gemini Deep Research analysis of syndicated loan docs, UCC filings, trade publications, SEC filings. Full report → `sources/GEMINI_NDFI_DEEP_RESEARCH.docx`

### Confirmed CRE Debt Fund Relationships

| Counterparty | Relationship | Example Deal | Source |
|-------------|-------------|-------------|--------|
| **Acore Capital** | Senior-mezzanine co-lending | $117M office loan, 4204 Glencoe Ave, LA (Nov 2022) | traded.co |
| **Mesa West Capital** (Morgan Stanley sub) | Construction co-lending | $413M Bridge Point Tacoma logistics ($263M OZK senior + $150M Mesa West mezz, Mar 2024) | perecredit.com |
| **Affinius Capital** (fka Square Mile/USAA RE) | Construction co-lending | $135M Perris Gateway industrial (Sep 2024) | decaco.com |
| **Related Fund Management** | Deep strategic alliance, co-origination | $54.7M West Adams office; $380M Riverwalk SD construction (with Hines) | traded.co, perecredit.com |
| **Blackstone (BREDS)** | Co-operator in large urban markets | Jersey City, NYC projects | perecredit.com |

### Additional CRE Counterparties (ChatGPT Deep Research)

| Counterparty | Relationship | Example Deal | Source |
|-------------|-------------|-------------|--------|
| **Starwood Property Trust (STWD)** | Construction co-lending | $400M, 1001 S Broad St Philadelphia (~2020) | ChatGPT |
| **Bridge Investment Group (BRG)** | Construction JV | $367M Stacks DC mixed-use (Apr 2022) | ChatGPT |
| **Belpointe PREP (OZ)** | Construction lender | Aster & Links, St. Petersburg FL (mid-2022, paid off Jun 2024) | ChatGPT |
| **Regents Capital** | $150M revolver (upsized Nov 2025) | Specialty finance, likely CRE-adjacent | ChatGPT |
| **Mack Real Estate / Claros** | Construction/dev lender | Mack Innovation Park, Deer Valley Phoenix (~Jul 2025) | ChatGPT |
| **Blue Owl Capital** | Exit counterparty | $335M bridge refi'd OZK's $215M Wynwood Plaza (Mar 2026) | ChatGPT |
| **Innovo / Affinius + PIMCO** | $250M senior mortgage | Bronx industrial (May 2023) | ChatGPT |

**Combined named CRE counterparties across both models: 11 entities, all CRE debt funds or CRE-focused PE/REITs.** Zero non-CRE NDFIs found in the RESG-managed NDFI book.

### Additional Counterparties (Perplexity Deep Research)

| Counterparty | Relationship | Example Deal | Source |
|-------------|-------------|-------------|--------|
| **3650 Capital** | RESG co-lending | $32M mezz / $59M OZK senior, Stamford CT multifamily (Sep 2025) | connectcre, perecredit |
| **PGIM Real Estate** (Prudential) | RESG co-lending | $24M mezz / $58M OZK senior, N Fort Worth multifamily (Aug 2025) | Commercial Observer |
| **GoldenTree / TZ Capital** | RESG co-lending | ~$125M mezz / ~$475M OZK senior, South Flagler House luxury condos, WPB | bridgeloanguy |
| **Aequum Capital** (Castlelake) | CIB Lender Finance, syndicated revolver | OZK participant in $140M facility (Jul 2024) | prnewswire |

### Affinius Capital — ELEVATED STRESS (Perplexity finding)
Affinius has **$2.7B in Amazon-warehouse-backed bonds** (issued 2021 at ~2%) now trading at **81 cents on the dollar**. Mandatory principal repayment deadline: **October 2026**. Hard interest step-up clauses activate on miss. Fortress faced identical structure on $2B and missed its July 2025 deadline. If Affinius is also a back-leverage borrower (note-on-note) from OZK — not just a co-lender — this becomes direct NDFI credit exposure.

### Full Gleason Mechanism Quote (Perplexity found extended version)
> "We compete with those guys, a lot of times, if they win a unitranche deal, they'll **bifurcate it into a senior mezz and we're the senior lender and they're the mezz**, sometimes they want to hold that whole loan on their books, but **leverage it with a loan from us**. And we do a **loan to lenders** or an NDFI loan to those guys."

This confirms two sub-variants:
- **Sub-variant A (Co-lending):** OZK senior + fund mezz on same project. OZK has no fund-level exposure.
- **Sub-variant B (Back-leverage / Note-on-note):** Fund pledges its entire loan to OZK as collateral. OZK has **direct fund-level credit exposure** — if fund can't repay, OZK takes the loan collateral (which may be impaired CRE).

## MASTER COUNTERPARTY LIST — All Three Models Combined

### RESG CRE Co-Lending Partners (15 confirmed entities)

| # | Counterparty | Deals Found | Stress | Sources |
|---|-------------|------------|--------|---------|
| 1 | **Affinius Capital** | 7+ deals (most frequent partner) | 🔴 $2.7B Amazon bond stress, Oct 2026 deadline | All 3 models |
| 2 | **Acore Capital** | 2 deals (LA office, Winchester VA industrial) | 🟡 LA office impaired | Gemini + ChatGPT + Perplexity |
| 3 | **Mesa West / Morgan Stanley** | 2 deals ($413M Tacoma, $88M Alexandria) | 🟢 Low | All 3 models |
| 4 | **Related Fund Management** | 2+ deals ($380M Riverwalk SD, $54.7M West Adams) | 🟢 Low | Gemini + ChatGPT |
| 5 | **Starwood Property Trust (STWD)** | $400M construction, Philadelphia | ⚠️ Dividend cut 2023 | ChatGPT |
| 6 | **Bridge Investment Group (BRG)** | $367M Stacks DC (Apr 2022) | 🔴 NAV plunge, redemption gates | ChatGPT |
| 7 | **Belpointe PREP (OZ)** | Construction, St. Petersburg FL | 🔴 NAV plunged, gated | ChatGPT |
| 8 | **3650 Capital** | $91M Stamford CT multifamily | 🟢 Low | Perplexity |
| 9 | **PGIM Real Estate** (Prudential) | $82M Fort Worth multifamily | 🟢 Low | Perplexity |
| 10 | **GoldenTree / TZ Capital** | ~$600M South Flagler House WPB | 🟢 Low | Perplexity |
| 11 | **Mack Real Estate / Claros** | Industrial, Phoenix | 🟡 Claros (CMTG) distressed refi | ChatGPT |
| 12 | **Innovo / PIMCO** | $250M Bronx industrial | 🟢 Low | ChatGPT |
| 13 | **Blackstone (BREDS)** | Jersey City/NYC co-operations | ⚠️ Down >20% YTD | Gemini |
| 14 | **Blue Owl** | $335M bridge refi'd OZK's $215M Wynwood (Mar 2026) | 🔴 Redemption gates, OBDC div suspended | ChatGPT |
| 15 | **Related (San Diego/Hines)** | $380M Riverwalk construction | 🟢 Low |
| 16 | **Square Mile Capital** | 5 deals incl Bioterra $203M (VACANT), One Chicago $735M | 🔴 Bioterra vacant |
| 17 | **Cain International** | Aman New York $750M ($300M OZK) | 🟢 Low |
| 18 | **JVP Management** | 50 W 66th St NYC $967M ($800M OZK) — largest known loan | 🟡 Monitor |
| 19 | **Prospect Floating Rate Fund** | $75M revolving credit, OZK facility agent (SEC 8-K) | 🟡 Non-traded BDC | Gemini + ChatGPT |

### CIB Lender Finance / Non-CRE (3 confirmed)

| # | Counterparty | Facility | Stress |
|---|-------------|---------|--------|
| 16 | **Regents Capital** | $150M revolver (equipment leasing) | 🟢 Low |
| 17 | **Aequum Capital** (Castlelake) | Participant in $140M syndicated revolver | 🟢 Low |
| 18 | **Mach Natural Resources** | $37.2M term (energy) | 🟢 Low |
| 20 | **Archrock Services** | $75M of $1.1B revolver (industrial) | 🟢 Low |

### Stressed Counterparties Summary: 6 of 19 CRE partners under stress

| Entity | Stress Type | OZK Risk Channel |
|--------|-----------|-----------------|
| **Affinius** | $2.7B bond maturity Oct 2026 | If back-leverage borrower (Sub-variant B), direct NDFI exposure |
| **Blue Owl** | Redemption gates, forced loan sales | Exit counterparty — takes out OZK construction loans |
| **Bridge Investment Group** | NAV plunge, redemption gates | Past co-lender (2022 deal) |
| **Belpointe PREP** | NAV collapse, gated | Past borrower (paid off Jun 2024) |
| **Starwood Property Trust** | Dividend cut | Co-lender on $400M Philly construction |
| **Square Mile Capital** | Bioterra $203M now vacant | Most prolific historical partner (5 deals, $1.5B+) |

### Additional Counterparties (Claude Deep Research)

| Counterparty | Relationship | Example Deal | Source |
|-------------|-------------|-------------|--------|
| **Square Mile Capital** | RESG co-lending — **most prolific historical partner** (5 deals, $1.5B+) | One Chicago Square $735M ($475M OZK); **Bioterra SD $203M (Dec 2022, NOW VACANT)**; SF life sci $373M | Commercial Observer |
| **Prospect Floating Rate Fund** (Prospect Capital) | **Direct BDC lending — $75M revolving credit, OZK as facility agent** | SEC 8-K filing Aug 13, 2025. Replaced prior Sumitomo facility. SOFR+250bps, matures Aug 2029. | SEC EDGAR — **only confirmed BDC direct lending from SEC filings** |
| **Cain International** | RESG co-lending | Aman New York $750M ($300M OZK senior, ~2019) | Commercial Observer |
| **JVP Management** | RESG co-lending | 50 West 66th St NYC (Extell) $967M ($800M OZK senior, Feb 2022) — **OZK's largest known single loan** | Commercial Observer |

**Key finding:** Square Mile Capital is the **Bioterra co-originator** ($203M, Dec 2022, Sorrento Mesa SD). This closes audit gap B5 — we now have a sourced co-lender for the $202M vacant life science campus. Square Mile described OZK as "a trusted and reliable partner in the construction lending space."

**Personnel connection:** David Dancer moved from Bank OZK RESG to Acore Capital (per Acore leadership page). Revolving door between OZK and its NDFI counterparties.

**What Claude ruled out:** Comprehensive SEC search found NO OZK lending relationships with ARCC, OBDC/OBDE, BXMT, KREF, LADR, TRTX, GBDC, Claros, Ready Capital, Arbor, or any major institutional BDC/mortgage REIT. These entities use money-center banks (JPM, GS, WF, MS, DB) for warehouse lines. OZK's NDFI book tilts toward **mid-market CRE-focused funds**, not the large alts managers.

### Confirmed Non-CRE NDFI Relationships (CIB)

| Counterparty | Relationship | Amount | Source |
|-------------|-------------|--------|--------|
| **Prospect Floating Rate Fund** (Prospect Capital) | $75M revolving credit, OZK facility agent | $75M | SEC 8-K (Aug 2025) |
| **Mach Natural Resources LP** | Syndicated credit facility — OZK as "New Lender" + Co-Syndication Agent | ~$37.2M initial term | SEC filing (Sep 2025) |
| **Archrock Services LP** | Revolving credit facility — OZK as "New Lender" | $75M of $1.1B facility | Justia contracts (Aug 2024) |

### Fund Finance / Subscription Lines

OZK attends Fund Finance Association Global Symposium alongside Ares Management and Apollo Global Management representatives. Markets subscription financing as core CIB offering. Specific fund names shielded by confidentiality. Fund finance group saw "a little bit of a dip" in Q3 2025 as OZK "shed legacy borrowers" with low utilization (Hamblen, Q3 call).

### Stressed Counterparty Exposure

| Entity | Stress Signal | OZK Linkage | Source |
|--------|-------------|-------------|--------|
| **Blue Owl** | Redemption gates (OBDC II, OTIC, OCIC); sold $1.4B in loans; OBDC dividend suspended 2023 | 🔴 **DIRECT:** Blue Owl's $335M bridge loan (Mar 2026) refinanced OZK's $215M Wynwood Plaza construction loan. Blue Owl is an OZK exit counterparty. | ChatGPT (perecredit) |
| **Bridge Investment Group (BRG)** | NAV plunge, redemption gates 2023 | $367M Stacks DC construction JV with OZK (Apr 2022) | ChatGPT |
| **Belpointe PREP (OZ)** | NAV plunged, gated redemptions 2023 | OZK was construction lender on Aster & Links, St. Petersburg FL (mid-2022, paid off Jun 2024) | ChatGPT |
| **Starwood Property Trust (STWD)** | Dividend cut 2023 | $400M construction co-lending, 1001 S Broad St Philadelphia | ChatGPT |
| **Arbor Realty Trust** | Targeted by Viceroy & Ningi short reports | Contagion risk to bridge sector. Direct exposure not confirmed. | Gemini |
| **Blackstone (BREDS)** | Down >20% YTD early 2026 | Confirmed co-operator Jersey City/NYC | Gemini |

### 🔴 Blue Owl as OZK Exit Counterparty — Key Systemic Risk

Blue Owl's $335M bridge loan refinancing OZK's $215M Wynwood construction loan (Mar 2026) reveals a critical dependency: **Blue Owl is one of the entities taking out OZK's maturing construction loans.** If Blue Owl's liquidity crisis deepens (more redemption gates, inability to fund new bridge loans), OZK loses a key exit channel for its construction book. This is the same construction book where $7.0B sits on interest reserves waiting for maturity/refi.

The transmission chain: Blue Owl stress → fewer bridge loan takeouts → OZK construction loans can't refi at maturity → forced extensions or nonaccrual conversion → the cliff we're modeling in the bear case.

### Key Structural Insight: The "Look-Through" Model

Gemini identified that OZK's loan-to-lender model uses:
- **Low attachment points:** OZK finances only senior 50-60% of property value; fund's equity/mezz acts as buffer
- **Lock boxes:** Cash flows from underlying loans directed to OZK-controlled accounts
- **Third-party servicers:** Independent verification of collateral in multi-asset facilities

This means OZK's NDFI exposure is NOT unsecured lending to funds. It's asset-backed, with OZK in the senior position. **However**, in a systemic CRE downturn, the senior position still takes losses once the mezz/equity buffer is consumed — and the LTV reappraisal data (52.9% → 98.9%) suggests that buffer is eroding on office properties.

---

## Updated CRE Correlation Assessment

With named counterparties identified, we can now upgrade the CRE correlation estimate:

| Category | Amount | CRE Correlation | Basis |
|----------|--------|-----------------|-------|
| Business credit intermediaries | $1,201M | **70-80%** | Named counterparties (Acore, Mesa West, Affinius, Related) are all CRE debt funds. Gleason confirmed "RESG loans." |
| PE funds | $772M | **40-60%** | Subscription lines to funds at Fund Finance Association events; some CRE PE, some not |
| Other NDFIs | $722M | **40-50%** | Likely includes bridge lenders in Arbor/Blackstone ecosystem |
| Consumer credit | $48M | 0% | Immaterial |
| **Revised shadow CRE** | | | **$1,250-1,750M** |

### Revised True CRE Concentration

| Metric | Reported | + Shadow CRE + MI3 |
|--------|---------|-------------------|
| CRE / Tier 1 | 358% | **411-420%** |

---

## What We Still Don't Know

1. **Specific subscription line clients** — Confidentiality agreements protect fund names
2. **Blue Owl direct exposure amount** — Suspected but not quantified
3. **Overlap/double counting** — OZK may finance both the CRE project (via RESG) AND the debt fund co-lending on the same project (via NDFI). This would be double exposure to the same asset.
4. **NDFI noncurrent status** — $2,703 C&I noncurrent is tiny vs $3.4B book. But fund defaults are binary (gate, margin call), not gradual.

---

*Sources: FFIEC Call Report RSSD 107244 Q4 2025. OZK Q3 2025 Earnings Call (Oct 17 2025). Gemini Deep Research report (Mar 23 2026) — full report in `sources/GEMINI_NDFI_DEEP_RESEARCH.docx`. Individual deal sources cited in table above.*
