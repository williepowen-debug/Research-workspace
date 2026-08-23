> # ⛔ BUILT ON A DEAD RATIO — do not cite the MI3 figures here (banner added 2026-08-23)
>
> This document's central metric is the **Memo-Item-3 / C&I "shadow CRE" ratio at 37.6%.** That figure **reproduces at no quarter on four independent paths** (OZK's own 18-quarter FFIEC series on either basis · REGINALD's 14-bank × 4-quarter cohort re-run, 56/56 sourced · the **FDIC's own API at a different agency** · the 14-quarter FDIC ratio series). Live: **9.35% at Q2-2026**, *below the screen's own >20% flag for two straight quarters.* And **"worst in the screen" was formally RETRACTED by the screen's owner** — OZK ranks **5th of 14 on both bases**.
>
> **What dies and what does not.** The **ratio** and every ranking built on it are dead. The **mechanism** this document reasons about — CRE-purpose lending carried under a C&I label, and the debt-on-debt/note-assignment book — **survives, and is now better evidenced than when this was written**: `RCON2746` ties the Q1'26 10-Q's ~$490M book at the dollar across two independently-prepared filings, and that book **began charging off in H1-2026** (`RIAD5409` $42,437K, first nonzero in 18 quarters). `[[finding_claim_outlives_its_discredited_instrument]]` — **scope the impeachment to the ratio, not to the idea.**
>
> ⚠️ **Scope fence:** MI3 is CRE **NOT secured** by real estate. RESG, IQHQ/RaDD, the classified balance and all 11 tracked credits are in the **secured** book and are untouched.
>
> Current state → `THESIS.md` §MEMO ITEM 3 · `MI3_2025Q3_ADJUDICATION.md` · `workbook/CALL_REPORT_SERIES.tsv` · KB-OZK-226.

# D3: The Shadow CRE Lever — A Novel Concentration Metric

**Created:** 2026-03-24
**Sources:** FFIEC Call Report Q4 2025, OZK Q3 2025 Earnings Call, Deep Research (4 models, 23 named counterparties)
**KB Rows:** 021–027 (SHADOW_CRE), 018–020, 087 (MEMO_ITEM_3) | **Nav:** `../workbook/KB_INDEX.md`
**Status:** COMPLETE
**Dependency:** `NDFI_SHADOW_CRE_ANALYSIS.md` (full counterparty data)

---

## The Claim

**OZK's true CRE concentration is 405-420% of Tier 1 capital, not the reported 358%.**

No sell-side analyst has published this number. It requires combining three regulatory data sources that are never read together:
1. RC-C Part I Item 1 (direct CRE loans)
2. RC-C Part I Item 4 → Memo Item 3 (CRE hidden in C&I)
3. RC-C Part I Item 9a (NDFI loans to CRE debt funds)

---

## The Three Layers of CRE

### Layer 1: Reported CRE — $19.9B (358% of Tier 1)
What regulators and analysts see. Construction, multifamily, office, life science — all on the label.

### Layer 2: Memo Item 3 — $1.289B hidden in C&I
Loans classified as C&I (commercial & industrial) that are **secured by real estate**. FFIEC requires disclosure via RCON2746, but it's buried in a memo line nobody reads. OZK's ratio: 37.6% of C&I is actually RE-linked. This was the Memo Item 3 discovery (confirmed via FFIEC CDR, Q4 2025).

### Layer 3: NDFI Shadow CRE — $1.25-1.75B
$2.74B in loans to non-depository financial institutions. CEO Gleason confirmed on Q3 2025 call: **"a chunk of our NDFI loans that show up on our call report are actually RESG loans... debt funds that do commercial real estate lending."**

Deep research across 4 AI models identified **23 named counterparties — 19 of 19 in the CRE-managed book are CRE debt funds.** Zero non-CRE entities found in the RESG-managed NDFI portfolio. Applying conservative CRE correlation (50-75% by sub-category) yields $1.25-1.75B in shadow CRE.

---

## The Stack

| Layer | Amount | CRE / Tier 1 | Source |
|-------|-------:|:------------:|--------|
| **1. Reported CRE** | $19,876M | 358% | Call Report RC-C |
| **2. Memo Item 3** | $1,289M | +23% | RCON2746 |
| **3. NDFI Shadow CRE** | $1,250-1,750M | +23-32% | RCONJ454 + CEO admission + counterparty analysis |
| **TOTAL** | **$22,415-22,915M** | **405-420%** | |

For context, regulatory guidance flags CRE/Total Capital >300% for enhanced supervision. OZK is 100-120 percentage points above that — before you even count unfunded commitments ($18.0B).

---

## Why This Is Wrong-Way Risk, Not Just Concentration

Concentration alone is a known issue — analysts debate whether 358% is manageable. The shadow CRE argument is different: **OZK's "diversification" is correlated with its core risk.**

### The Transmission Chain

```
CRE downturn hits
    ├── Layer 1: Direct CRE loans go nonaccrual ($341M and climbing)
    ├── Layer 2: C&I loans secured by RE also deteriorate (hidden — Memo Item 3)
    └── Layer 3: NDFI counterparties can't repay because:
         ├── Their CRE borrowers are defaulting (same downturn)
         ├── Their NAVs are declining → redemption gates (Bridge, Belpointe, Blue Owl)
         ├── Their bond maturities are approaching (Affinius $2.7B, Oct 2026)
         └── Their exit capacity is shrinking → OZK construction loans can't refi
```

**All three layers are hit by the same macro shock simultaneously.** This is the definition of wrong-way risk: the "diversification" fails precisely when you need it.

### The Double-Exposure Problem

OZK may be on **both sides** of the same deal:
- **RESG** originates a $100M construction loan to a developer
- **CIB/NDFI** lends $50M to the debt fund providing mezzanine on the same project

If the project fails, OZK loses on the construction loan AND on the NDFI loan. This double-counting risk is unquantifiable from public data but structurally present given the overlapping counterparty network.

---

## The Novel Metric: "Adjusted CRE Concentration"

### Definition
> **Adjusted CRE / Tier 1** = (Reported CRE + Memo Item 3 + NDFI Shadow CRE) / Tier 1 Capital

### Why No One Has Published This
1. **Memo Item 3** requires reading FFIEC Call Report field RCON2746 — buried in memo lines
2. **NDFI → CRE linkage** requires the CEO admission (Q3 2025 call) + counterparty identification (deep research across syndicated loan docs, UCC filings, SEC filings)
3. **Call Report categories** (C&I vs CRE vs NDFI) are designed to separate these buckets — combining them is a novel analytical step

### Replicability
Any analyst can reproduce this:
- Pull RCON2746 from cdr.ffiec.gov (RSSD 107244)
- Listen to Q3 2025 earnings call (Gleason admits NDFI = CRE)
- Apply conservative 50% CRE correlation to NDFI business credit intermediaries
- Add: reported CRE + Memo Item 3 + shadow NDFI

---

## Six Stressed Counterparties

Of 19 named CRE debt fund counterparties, **6 are under active stress:**

| Entity | Stress | OZK Risk |
|--------|--------|----------|
| **Affinius Capital** | $2.7B bond maturity Oct 2026 | Most frequent co-lending partner (7+ deals) |
| **Blue Owl** | Redemption gates, forced loan sales | **Exit counterparty** — takes out OZK construction loans |
| **Bridge Investment Group** | NAV plunge, redemption gates | $367M construction JV |
| **Belpointe PREP** | NAV collapse, gated | Past borrower (paid off) |
| **Starwood Property Trust** | Dividend cut | $400M construction co-lending |
| **Square Mile Capital** | Bioterra $203M now vacant | Most prolific historical partner (5 deals, $1.5B+) |

Blue Owl is the critical one: it's an **exit counterparty** whose $335M bridge loan refinanced OZK's $215M Wynwood Plaza. If Blue Owl can't fund new bridges, OZK construction loans can't exit at maturity → the $7.0B interest reserve book has nowhere to go.

---

## The Paragraph

> Bank OZK reports CRE concentration of 358% of Tier 1 capital — already well above the 300% regulatory guidance threshold. But this understates the real exposure. An additional $1.3B in C&I loans are secured by real estate (FFIEC Memo Item 3, RCON2746), and $1.25-1.75B of OZK's $2.74B in loans to non-depository financial institutions flow to CRE debt funds — a fact CEO Gleason confirmed on the Q3 2025 call when he stated that "a chunk of our NDFI loans are actually RESG loans... debt funds that do commercial real estate lending." Deep research across syndicated loan documents and SEC filings identified 19 CRE debt fund counterparties, six under active stress including Blue Owl (redemption gates, OZK exit counterparty) and Affinius Capital ($2.7B bond maturity October 2026). Adjusting for all three layers, OZK's true CRE concentration is 405-420% of Tier 1 — and critically, all three layers are correlated. The "diversification" into CIB and NDFI lending doesn't reduce CRE risk; it amplifies it through wrong-way exposure to the same credit cycle.

---

## Cross-References
- Full counterparty data: `NDFI_SHADOW_CRE_ANALYSIS.md`
- Memo Item 3 methodology: `../EVIDENCE.md` (lines 280-295)
- C1 Reclassification Rebuttal: `C1_RECLASSIFICATION_REBUTTAL.md`
- Source reports: `raw/llm_outputs/GEMINI_NDFI_DEEP_RESEARCH.docx`, `raw/llm_outputs/CHATGPT_NDFI_DEEP_RESEARCH.md`, `raw/llm_outputs/PERPLEXITY_NDFI_DEEP_RESEARCH.md`, `raw/llm_outputs/CLAUDE_NDFI_DEEP_RESEARCH.md`
- CEO quote: OZK Q3 2025 Earnings Call, Oct 17, 2025
