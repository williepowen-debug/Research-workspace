# MTB — NDFI 10-K Analysis & Counterparty Deanonymization Attempt

**Source:** FY2025 10-K (filed Feb 18, 2026, period Dec 31, 2025)
**CIK:** 0000036270 | **Accession:** 0000036270-26-000010
**Methodology:** Applied WAL Apr 14 deanonymization approach (Exhibit Index counterparty names in amendment titles)
**Result:** **DEAD END.** MTB files zero material lending contracts as exhibits. No Master Repurchase Agreements. Exhibit Index is exclusively compensation plans and governance docs. MTB's 10-K is MORE opaque than WAL's on counterparty identity.

---

## NDFI Sub-Breakdown (Table 11, 10-K)

**This is the granular data the earnings call didn't give us.**

| NDFI Sub-Category | Commitment | Outstanding | Notes |
|---|---|---|---|
| **Mortgage credit intermediaries** (a) | **$10.216B** | **$5.610B** | REIT credit facilities + mortgage warehouse + MSR financing. **COMBINED.** |
| **Private equity funds** (b) | **$5.981B** | **$3.287B** | Primarily subscription/capital call lines (fund banking). |
| **Business credit intermediaries** (c) | **$3.288B** | **$1.770B** | Wholesale lender finance + leasing + BDC. |
| **Consumer credit intermediaries** (d) | **$1.145B** | **$0.731B** | Consumer lender finance + leasing. **Not mentioned on Q1 call.** |
| **Other** | **$3.269B** | **$1.139B** | Unclassified. |
| **TOTAL** | **$23.899B** | **$12.537B** | — |

Footnotes from 10-K:
- (a) "Includes real estate investment trust credit facilities, residential mortgage warehouse lines of credit and mortgage loan servicing rights secured financing."
- (b) "Primarily subscription credit facilities."
- (c) "Includes credit facilities to wholesale lender finance and leasing companies and business development companies."
- (d) "Includes credit facilities to consumer lender finance and leasing companies."

---

## Critical Finding: Commitment vs Outstanding

**Total NDFI commitments: $23.9B — nearly DOUBLE the $12.5B outstanding.**

$11.4B in undrawn commitments. If stressed counterparties draw down facilities (classic bank stress: counterparties pull lines as credit tightens), MTB's NDFI book could grow $11.4B without originating a single new loan. This is the contingent exposure the income statement doesn't show.

**Q1 2026 outstanding grew to $13.4B** (from $12.5B Dec 31) — already $0.9B more drawn. Directionally, counterparties are drawing.

## Q1 Sub-Category Growth (Slide 18 vs 10-K Table 11) 🔴 NEW

| Category | Dec 31 (10-K) | Mar 31 (Slide 18) | QoQ Change | Share of Growth |
|----------|--------------|-------------------|------------|-----------------|
| **Mortgage credit intermediaries** | $5.6B | **$6.5B** | **+$0.9B (+16%)** | **100%** |
| Private equity funds | $3.3B | $3.5B | +$0.2B | — |
| Business credit intermediaries | $1.8B | $2.0B | +$0.2B | — |
| Consumer credit intermediaries | $0.7B | $0.6B | -$0.1B | — |
| Other | $1.1B | $0.8B | -$0.3B | — |
| **Total** | **$12.5B** | **$13.4B** | **+$0.9B** | — |

**100% of Q1 NDFI growth came from mortgage credit intermediaries** — the bucket that contains warehouse lending, REIT credit facilities, and MSR secured financing. This is the exact channel where Apollo Atlas SP operates. MTB is growing the riskiest NDFI bucket fastest while the other categories are flat-to-declining.

---

## Key Discoveries

### 1. "Mortgage Credit Intermediaries" Is Three Things
The Q1 call described "three pillars" as 2/3 of NDFI. The 10-K reveals the pillar is labeled **"Mortgage credit intermediaries"** and combines:
- REIT credit facilities (institutional CRE/REIT lending)
- Residential mortgage warehouse lines
- MSR secured financing

**Commitments: $10.2B, Outstanding: $5.6B.** No sub-breakdown within this bucket. This is the biggest NDFI category and we can't see inside it.

### 2. Fund Banking Is Bigger Than Expected
Private equity funds / subscription lines: **$6.0B commitments, $3.3B outstanding.** Bible said "growing to right-size for M&T" — this is a $6B commitment book, not a boutique.

### 3. Consumer Credit Intermediaries — Undisclosed on Call
$1.1B commitments / $0.7B outstanding to consumer lender finance companies. **Not mentioned on the Q1 call at all.** Bible disclosed wholesale lender finance ($700M), leasing ($600M), and BDC ($400M) but skipped this category entirely. What consumer lending companies does MTB lend to? Auto? Fintech? Subprime?

### 4. "Other" Is $3.3B
$3.3B in NDFI commitments classified as "Other" — 14% of total. Completely undescribed.

---

## Bayview — Much Larger Than Previously Understood

The NON_BANK_EXPOSURE.md (from the call) described Bayview as a 20% equity stake with $33M Q1 distribution. The 10-K reveals a **massive, multi-dimensional related-party relationship:**

| Dimension | Amount | Change |
|-----------|--------|--------|
| **Lending commitments** | **$984M** ($635M outstanding) | Up from $404M outstanding (FY2024). +57% YoY. |
| **Sub-servicing UPB** | **$156.9B** | Up from $111.5B (+41%). Added $51.7B in Feb 2025. |
| **Sub-servicing revenue** | **$224M** (FY2025) | Up from $123M (+82%). Nearly doubled. |
| **Deposits from Bayview** | **$3.5B** | Up from $2.2B (+59%). |
| **Equity stake** | 20% (zero carrying value) | Unchanged. |
| **MBS held (HTM)** | $32M | Down from $37M. |

**Bayview Financial = Bayview Financial Holdings, L.P. + affiliates** (includes Bayview Asset Management, Blackstone minority stake from 2008, Lakestar Finance).

**Concentration risk assessment:**
- $635M lending + $3.5B deposits + $157B sub-servicing + $224M revenue = MTB has a **deep, growing, multi-vector dependency on one related-party counterparty.**
- If Bayview had trouble: deposits flee ($3.5B), lending takes losses ($635M), sub-servicing revenue drops ($224M), equity value already zero.
- The $51.7B sub-servicing addition in Feb 2025 was a DELIBERATE decision to deepen the relationship.

**Note:** The "new mortgage subservicing" Bible described on Q1 call ($30-40M annual revenue, FHA-focused, starting 2H26) appears to be ADDITIONAL to the existing $224M Bayview sub-servicing. Total sub-servicing revenue could be ~$260M+ by 2H26.

---

## Tricolor — Trustee Exposure (10-K Litigation Disclosure)

**New finding not previously tracked.**

- **Wilmington Trust, N.A.** (MTB subsidiary) served as corporate custodian and trustee for multiple Tricolor Holdings warehouse facilities and ABS securitization transactions **since 2018.**
- No loans or commitments outstanding to Tricolor from either Wilmington Trust or M&T Bank.
- **Jan 12, 2026:** Noteholders filed civil complaint against Wilmington Trust for unspecified damages — breach of contract and fiduciary duty.
- MTB disclosure: "may incur losses... not possible to estimate... not expected to be material."

**OTTO crosslink:** Tricolor is the auto fraud ring OTTO tracks. MTB isn't in the ring as a warehouse lender (unlike JPM $170M, FITB $170-200M, Barclays nine-figure, Regions $68M). But as **trustee**, Wilmington Trust has fiduciary liability exposure. The noteholder lawsuit ($230M+ Janus Henderson, One William Street, Ellington) is a real claim. If ABS recovery is <10¢ on the dollar (OTTO finding), and Wilmington Trust as trustee failed its fiduciary duties during the fraud period, damages could be material even if MTB says otherwise.

---

## Deanonymization Verdict

| Approach | Result |
|----------|--------|
| **Exhibit Index** (WAL methodology) | **DEAD END.** No material lending contracts filed. No EX-10 series for facilities. |
| **Note disclosures** | Sub-category level only. No individual counterparty names. |
| **Master Repurchase Agreements** | Zero matches in 10-K. Not filed as exhibits. |
| **Subsidiary list** | Checked EX-21.1 — standard banking subsidiaries, no warehouse SPV names visible. |

**MTB's NDFI counterparty opacity is WORSE than WAL's.** WAL at least filed some facility amendments as exhibits (enabling the Apr 14 deanonymization). MTB files nothing.

**Remaining paths to counterparty identification:**
1. **FFIEC Call Report RC-C Item 9** (filed to regulators, not publicly granular)
2. **Investor deck Slide 19** (Q1 2026 deck, not yet obtained)
3. **Q2 earnings call Q&A** (Jul 2026) — press management for names
4. **Counterparty 10-Ks** — work backwards from non-bank servicer filings (PFSI, LDI, COOP, RITM) to see if any name MTB as a warehouse lender. *PFSI's 10-K (already pulled Apr 14) names Atlas SP + 12 G-SIBs — no MTB. LDI names BofA, JPM, Citi, Nomura, UBS, Atlas SP, BMO — no MTB. Not definitive (MTB could be in anonymized "other" buckets).*

---

*Sources: M&T Bank FY2025 10-K (SEC EDGAR, filed Feb 18, 2026). Table 11: NDFI commitments. Note 23: Bayview relationship. Litigation section: Tricolor/Wilmington Trust. Cross-referenced with NON_BANK_EXPOSURE.md (Q1 2026 call data).*
