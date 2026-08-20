# ⛔ ARCHIVED 2026-08-20 — Bank Exposure Matrix **v1**, superseded by v2.0

> **HISTORY ONLY. Do not cite any score, ratio or ranking below.**
> Superseded because **its scores were not reproducible**: its own stated method (🔴=3/🟠=2/🟡=1 × 8 channels) computes EGBN **12**, while `STATUS.md` carried EGBN **20** as canonical, and **no derivation of 20 exists anywhere in the repo**. Its tables also disagreed with each other (EGBN 11 vs 12, CFG 8 vs 9, ZION 6 vs 9), **OZK was absent from the scoring table entirely**, EGBN's CRE concentration appeared **twice at 497% and 547%** (both ~2× the primary — the real figure is ~258%), and the Hidden-CRE table ranked on the defective ÷item-4 basis whose rank the basis inverts.
> **Live instrument → `BANK_EXPOSURE_MATRIX.md` v2.0** (2 instrumented channels, stated scale 0-6, arithmetic shown, validated against a company disclosure).
> ⚠️ **The v2 ranking INVERTS v1's: FLG went from last to first; CFG from 3rd to last; WAL from 1st to mid.**

---

# Bank Exposure Matrix — Convergence Channel Analysis

> # 🔓 UNBLOCKED 2026-08-20 — and the worst artifact in this file is now KILLED, not banner-qualified.
> **WAL ruled fence-② does not reach the OZK cell** (`52a74a43c`; WILL_QUEUE row 42 closes on it) — decisive ground: *a fence written against improvising a JUDGMENT must never become the reason a known-false DATUM stays on a live surface.* **The Hidden-CRE Screen table below is struck and replaced with uniform-basis (v1a) figures.** OZK ~~37.6%~~ → **5.46%**; and per this desk's own 8/13 verification the cell says the level FELL, **not** that OZK de-risked (that reading is `UNRESOLVED`).
>
> ⚠️ **THE REST OF THIS FILE IS STILL A FEB-VINTAGE FOSSIL AND THE FULL RE-SCORE IS STILL OWED.** One table was fixed because it carried a *known-false* number with a 🚨 CRITICAL verdict attached; the rest is stale, not false-on-its-face.
>
> 🔴 **DEFECT FOUND WHILE SCOPING THE RE-SCORE, and it is bigger than this file: the convergence scores are NOT REPRODUCIBLE.** `STATUS.md` §Convergence Matrix is canonical for the SCORES (EGBN 20 · WAL 20 · CFG 15 · OZK 13 · SSB 11 · ZION ~8-9 · FLG 8) **but carries no method** — the only derivation of *how a bank earns a 20* lives in this stale document. ⇒ **Anyone citing 'EGBN 20' today cannot reproduce it** (`finding_loadbearing_number_must_be_reproducible`). **This is why this file must be REWRITTEN, not retired like THESIS/TIMELINE were** — those had a live successor that carried everything; this one's successor carries outputs only. Scoped in ROADMAP.
>
> ⚠️ **STALE-VINTAGE — 2026-02-23 (~4.5mo, pre-earnings). Canonical scores live in `STATUS.md` §Convergence Matrix.** Do NOT cite the scores/prices below as current — the Matrix tables here disagree with STATUS AND with each other (EGBN 11 vs 12, CFG 8 vs 9, ZION 6 vs 9; OZK absent entirely). Canonical: **EGBN 20, WAL 20, CFG 15, ZION ~8-9, OZK 13, SSB 11, FLG 8.** ~~The MI3/hidden-CRE ratios (OZK 37.6% / WAL 24.2% / EGBN 23.7%) DO still hold.~~ **⚠️⚠️ THAT VOUCHING LINE IS CONTRADICTED 2026-08-10:** first-ever FFIEC primary runs (8/7, OZK-spawn + WAL-spawn independently) found the screen's denominator defective (item-4-only base; RCON2746 sits in items 4 AND 9). **OZK 37.6% reproduces at NONE of 18 quarters** (live recipe-basis 9.35%); **WAL reproduces (24.24% @ 12/31/25) but is live 21.20%, never ≥25% in 12 quarters**; EGBN unverified. Do not cite ANY MI3 ratio from this file — cohort re-run on a settled basis is REGINALD-owed. **Full re-score scheduled post-Jul-21 print** (flagged 2026-07-10 audit).

>
> ⚠️⚠️ **DATED CONTRADICTION — 2026-07-30 sweep. `EGBN` CRE-concentration appears TWICE IN THIS FILE AT TWO DIFFERENT VALUES: **497%** (§Regulatory Concentration table) and **547%** (§scoring table, score-11 row). Same entity, same metric, ~50pp apart. **NEITHER IS CLEAN — do not pick one.** Both rows are marked inline.
> **Compounding it, the denominator is ambiguous in the same table:** the section header cites **SR 07-1**, whose 300% threshold is CRE ÷ **total risk-based capital**, while the column header reads **"CRE/Tier 1"** — Tier 1 is the *smaller* denominator, so the column over-states concentration relative to the standard it cites (~10-20%).
> **For scale: EGBN's own Q2-2026 disclosure puts CRE concentration at 267.6%** (down from 295.1%) — i.e. *below* the 300% line, against 497%/547% here. Vintage (non-OO CRE −34% YoY) does most of that gap; the denominator wrinkle does the rest.
> **Live guidance until the re-score lands: cite EGBN 267.6% [EGBN Q2-2026 primary, graded 7/25] — NOT any number in this file.**
> **The full re-score (denominator stated per row + the internal inconsistency resolved) is PARKED with PROME as a flagged item with an owner** — this banner is deliberately a *warning, not a fix*, and it carries its own rewrite trigger: **resolve at the next REGINALD build session** ([[finding_banner_is_a_warning_not_a_fix]]). Found by PROME 7/25 at source; bannered 7/30.

*Cross-referencing regional banks against the 8 KRE convergence channels + Municipal/Geographic stress*

**Last Updated:** 2026-02-23 13:50 UTC
**Status:** ✅ UPDATED — Hidden CRE screen integrated + Metropolitan Capital autopsy + Chicago loss severity

---

## CRITICAL FINDINGS

### 🚨 Hidden CRE — The Classification Game (NEW Feb 23, 2026)

**Discovery:** Banks hide CRE exposure by classifying unsecured CRE loans as "C&I" — exposed via Schedule RC-C Memo Item 3 (RCON2746).

**Metropolitan Capital Bank (Chicago, failed Jan 30, 2026):**
- Labeled as 10.7% CRE, 77.5% C&I
- **Actual:** 61% CRE when including Memo Item 3
- $54.1M hidden CRE in C&I (39.6% of C&I book)
- Charge-offs: $18.1M — **100% were CRE losses**
- NCO rate: **13.3%** — validates Chicago loss severity

**Chicago = Ground Zero (Fox Business, Feb 22, 2026):**
- **70-94% discounts** on actual transactions
- 401 S. State St: $68.1M → $4.2M (**-94%**)
- 311 S. Wacker: $302M → $45M (**-85%**)
- "Values unlikely to rebound to pre-2020 levels"

**Hidden CRE Screen — ⛔ TABLE KILLED 2026-08-20. Every ratio below is DEAD; the screen it came from is retired.**

> 🔴 **This table was the single worst artifact in this file and it is now struck, not banner-qualified.** Its "3 of 7 flag the Metropolitan pattern" headline, its ranking, and its 🚨 CRITICAL verdicts were all produced by the **defective ÷item-4 basis** — `RCON2746` sits in RC-C items **4 AND 9**, so dividing by item 4 alone is a category mismatch whose severity varies by bank. **The basis inverts the rank** (item-9 share of the base runs 5.5%→65.8% across the cohort), so the ORDER below is as dead as the numbers.
>
> **UNBLOCKED to fix on 2026-08-20:** WAL ruled fence-② does not reach this cell (`inbox/processed/2026-08-20_from-WAL_fence-2-RULED...`, commit `52a74a43c`), on the decisive ground that **a fence written against improvising a JUDGMENT must never become the reason a known-false DATUM stays on a live surface.** Row 42 closes on it.
>
> **Replacement, on the uniform v1a basis (÷ item 4 + item 9) — the only basis valid cross-bank, per this desk's own ruling, which WAL adopts as consumer:**
>
> | Bank | old ÷item-4 "ratio" | **v1a [2026Q2]** | MI3 $K [2026Q2] | what actually happened |
> |---|---|---|---|---|
> | **OZK** | ~~37.6%~~ **KILL-ON-SIGHT** | **5.46%** | $430,277 | ⚠️ **37.6% reproduces at NONE of 18 quarters** at the FFIEC primary. Level is far lower — **but this desk's own 8/13 adversarial verification leaves the READING `UNRESOLVED`: all four discriminators failed and ~⅔ of the −64% is ONE quarter (2025Q3, −36% on a flat book).** ⇒ **the level fell; "OZK de-risked" is NOT established and must not be written here.** |
> | **WAL** | ~~24.2%~~ | **8.99%** *(v1 21.20%)* | — | Reproduces at 12/31/25 (24.24%) but **never reached 25% in 12 quarters**; "fastest-growing in cohort" was a 6-quarter two-endpoint artifact. **Rank INVERTS by basis: #1 on v1, #3 on v1a.** |
> | **EGBN** | ~~23.7%~~ | **10.77%** — cohort max on v1a | — | **#4 on v1, #1 on v1a.** Was never independently verified at the time this table was written. |
>
> ⛔ **DO NOT cite any figure from the struck table.** Canonical, reproducible, dual-basis, guarded: **`workbook/MI3_COHORT.tsv`** + `reports/2026-08-13_MI3_cohort_rerun.md` (14 banks × 12 contiguous quarters, 56/56 rows at the primary, step detector, 3 fail-loud guards). ⚠️ **And the screen-level finding that replaced the whole framing: nobody clears 20% on the uniform basis — the ratio's stressed tail is GONE, and the dollars moved UP-CAP** (MTB holds the largest absolute book at $4.95B [2026Q2] at an unremarkable ratio), **where no ratio screen can see them.**
> ✅ **What SURVIVES from the original discovery: the bucket-migration MECHANISM and the three-level masking taxonomy.** A mechanism finding outlives its discredited ratio.

~~| Rank | Bank | Memo3 | Memo3/C&I | True CRE | Trend | Status |~~
~~|------|------|-------|-----------|----------|-------|--------|~~
~~| 1 | **OZK** | $1.29B | **37.6%** | 71.5% | ↓ (structural) | 🚨 CRITICAL — Worse than Metropolitan |~~
~~| 2 | **WAL** | $2.73B | **24.2%** | 59.0% | **↑ GROWING** | 🚨 PRIMARY TARGET — Active relabeling |~~
~~| 3 | **EGBN** | $231M | **23.7%** | 80.9% | ↓ (structural) | 🚨 CRITICAL — Already in crisis |~~
| 4 | VLY | $555M | 7.0% | 72.4% | — | ✅ Below threshold |
| 5 | FBC | $390M | 3.9% | 75.4% | — | ✅ Below threshold |
| 6 | ZION | $257M | 1.8% | 63.1% | — | ✅ Below threshold |
| 7 | **SSB** | $64M | **0.9%** | 78.9% | — | ✅ **Cleanest** — risk is visible |

**Metropolitan Capital Pattern threshold:** Memo3 > 20% of C&I

**The Classification Game — Three Levels of Masking:**
1. **Level 1:** Extend-and-pretend (don't force refinancing)
2. **Level 2:** Mark-to-model (don't write down)
3. **Level 3:** **Classification** (call CRE "C&I" if unsecured) ← DISCOVERED

**WAL is ONLY bank with GROWING hidden ratio:**
- Q2 2024: 15.5% → Q4 2025: 24.2% (up 56%)
- $438M single-quarter surge in Q4 2024
- Management said "remixing into higher-return C&I" = relabeling CONFIRMED
- Total hidden: $3.0B (Memo3 $2.73B + off-BS RCON6550 $273M)

**Regulatory Concentration (SR 07-1 — 300% threshold):**
| Bank | CRE/Tier 1 | Construction/Tier 1 | Status |
|------|------------|---------------------|--------|
| EGBN | **497%** ⚠️**[CONTRADICTED — see banner]** | 102% | 🔴 Both breached |
| WAL | **474%** | 76% | 🔴 CRE breached |
| OZK | **415%** | **142%** | 🔴 Both breached |

**Position Implications:**
- **KRE puts:** STRENGTHENED — 3 of 7 constituents have hidden CRE
- **SSB puts:** VALIDATED — cleanest book (0.9%), risk is where we see it
- **WAL:** 🎯 PRIMARY TARGET — only growing hidden ratio + management confirmed relabeling
- **OZK:** Secondary target — worst ratio but structural (not migrating)

---

### Municipal Securities — The Hidden Exposure (RP-REG-3.2)
**Key Bifurcation:** Banks either hold munis as HQLA (MTB, WBS, BHRB) or treat them as a lending vertical (ZION, WAL)

| Bank | Muni Holdings | % of Portfolio | Key Risk |
|------|---------------|----------------|----------|
| **MTB** | $2.84B | 7.7% | **61% NY State concentration** |
| **WBS** | $2.44B | **15%** | Northeast concentration, HTM-heavy |
| **WAL** | $2.28B | **13-15%** | **$1.36B UNRATED in HTM** = shadow loan book |
| **ZION** | **$5.78B total** | N/A | $1.4B securities + $4.36B LOANS + $524M unfunded |
| **BHRB** | $939M | **>50% of AFS** | VA/MD concentration, $54M unrealized loss |
| **VLY** | $225M | <5% | NJ improving (50% pension funded) |
| **FHN** | $216M | 2% | Minimal, TN/FL aligned |
| **EGBN** | $107M | 6% | DC Metro focus |
| **CFG** | **$1M** | <0.1% | **Effectively zero muni securities** |

**Critical finding:** ZION is a municipal LENDER, not just a holder. $5.78B total exposure with $524M unfunded commitments = liquidity risk in stress.

### Texas Border — The "Barclays Void" (RP-REG-3.4)
Global banks (Barclays, Citi, UBS) banned from TX munis due to ESG laws → Regional banks filling gap:
- **Cullen/Frost (CFR):** 100% Texas muni portfolio ($5.2B), 72.6% PSF-backed
- **Texas Capital (TCBI):** Launching public finance to fill void, acquiring healthcare exposure
- **IBC (IBOC):** $16.6B assets, headquartered Laredo, **existential Mexico/trade risk**

**Water crisis:** S&P flagged Laredo: "ongoing water delivery uncertainty intensifies credit pressure on utilities in the Rio Grande Basin"

**Pension stress:** TX border fire/police pensions at 60-75% funded (vs 86-120% for counties)

### DC Corridor — The Municipal Fracture
From RP-REG-3.3 research:
- **DC proper:** Moody's NEGATIVE outlook on Aa1 rating. $140M annual revenue loss projected (withholding tax collapse)
- **Prince George's County:** AAA but Moody's placed on NEGATIVE watch (9% federal workforce)
- **NoVA (Fairfax/Arlington/Alexandria):** AAA maintained — "Defense Shield" from national security contractors
- **Key quote:** "The 2025-2026 DOGE restructuring is fundamentally different. It is not a pause; it is a reversal."

### Florida — The "Doom Loop" (RP-REG-3.5)
**Citizens Property Insurance = $678B "Sword of Damocles"**

The Emergency Assessment mechanism converts weather risk into credit risk:
1. Hurricane → Citizens deficit → 15% surcharge on Citizens policyholders
2. If insufficient → **10% assessment on ALL FL policies** (private included)
3. Can be levied for **as many years as necessary**

**Transmission Chain:**
- Assessment spike → Borrower DTI/DSCR blow out → Defaults rise
- Property values fall → Municipal tax base erodes → Muni credit weakens
- Banks hit BOTH sides: Loan losses + AFS/OCI losses on muni holdings

**Bank FL Exposure:**
| Bank | FL % | FL Loans | Hurricane Prep | Risk |
|------|------|----------|----------------|------|
| **SBCF** | ~100% | $12.6B | None — pure play | 🔴 CRITICAL |
| **VLY** | 27% | $13.4B | Commercial reinsurance dependency | 🟠 ELEVATED |
| **ABCB** | 28% | $4.15B | GA/SC/NC buffer | 🟡 MANAGEABLE |
| **HOMB** | 28% | $4.15B | **$33M hurricane reserve** | 🟢 PREPARED |

**VLY unique risk:** Commercial CRE relies on private reinsurance. If reinsurers exit FL, collateral becomes *uninsurable at any price* — different from residential (Citizens backstop).

### Texas Border — The Absence
From RP-REG-3.1 research:
- **NO major KRE constituent has material TX border exposure**
- **Zions/Amegy:** Houston/Dallas focus only
- **First Horizon:** 7 commercial offices in major metros
- **IBC (IBOC):** Dominates McAllen/Laredo/Brownsville — this is the border play

### SoCal/Imperial Valley — Coastal Only
- **Western Alliance (Torrey Pines):** San Diego/LA coastal, NO Imperial Valley
- **Zions (CB&T):** Coachella Valley/Palm Desert, NO Imperial Valley
- Imperial Valley is a banking desert — no KRE exposure to agricultural stress there

### Stablecoin Deposit Flight — Systemic Channel (RP-REG-4.1)
**Standard Chartered projects $500 billion deposit outflow from US regional banks to stablecoins by 2028.**

This is a **SYSTEMIC** threat, not idiosyncratic single-name exposure:
- Regional banks depend on NIM (60-80% of revenue) vs investment banks (<30%)
- Tether holds 0.02% of reserves in bank deposits; Circle holds 14.24%
- Very little "redepositing" cushion — money leaves banking system entirely
- GENIUS Act (July 2025) legitimizes nonbank stablecoin issuers as competitors

| Bank | Crypto Exposure | Stablecoin Risk | Notes |
|------|-----------------|-----------------|-------|
| **CUBI** (Customers) | 🔴 HIGH | 🟠 ELEVATED | Fed enforcement Aug 2024; Circle partner |
| **MCB** | 🟡 MODERATE | 🟡 MODERATE | Reduced post-2023 |
| **All Regionals** | 🟢 MINIMAL | 🟠 SYSTEMIC | Sector-wide NIM compression risk |

**Key Insight:** Supports KRE basket thesis; does NOT identify new single-name targets.

### Florida HOA/Condo Assessment Crisis (RP-REG-4.2)
**Post-Surfside legislation (SB 4-D) has triggered $10K-$224K+ special assessments on 900,000+ aging condos.**

This **COMPOUNDS** the FL insurance doom loop — same borrowers hit by both:

| Stress Channel | Source | Magnitude |
|----------------|--------|-----------|
| Insurance Assessment | Citizens deficit | 10-15% of premium |
| Insurance Premium | Risk Rating 2.0 | +15-18%/year |
| **Structural Assessment** | SB 4-D compliance | **$10K-$224K one-time** |

**Florida is NOT a super-lien state** — mortgage liens retain priority over HOA liens. Banks protected from direct HOA liability, but borrower stress transmits through:
1. Borrower DTI stress → loan defaults
2. Collateral value impairment → LTV degradation
3. Market dysfunction (56% YoY listing surge) → reduced origination

**Combined FL Risk Assessment:**

| Bank | Insurance Risk | Assessment Risk | MF Stress | Combined | Notes |
|------|----------------|-----------------|-----------|----------|-------|
| **SSB** | 🟠 HIGH | 🟠 HIGH | 🔴 **9.36%** | 🔴 **POSITION** | Lowest capital, MF substandard highest of any CRE |
| **SBCF** | 🔴 CRITICAL | 🔴 CRITICAL | 🟡 | 🟢 SKIP | Fortress balance sheet, M&A target |
| **VLY** | 🔴 VERY HIGH | 🟠 HIGH | 🟠 | 🟠 ELEVATED | NJ/NY is primary market |
| **BKU** | 🔴 HIGH | 🔴 HIGH | 🟡 | 🟢 SKIP | Well-managed, credit improving |
| **FHN** | 🟠 HIGH | 🟠 ELEVATED | 🟡 | 🟠 ELEVATED | TN diversification |

**Key Insight:** Not a new column — sub-channel of existing FL GEO exposure. Same banks, compounded risk.

---

## M&A LANDSCAPE — WHO HAS A FLOOR?

### Recent Regional Bank Deals (2025-2026)

| Announced | Acquirer | Target | Value | Status | Multiple |
|-----------|----------|--------|-------|--------|----------|
| May 2025 | Capital One | Discover | $35.3B | ✅ Closed | — |
| Sep 2025 | PNC | FirstBank | $4.1B | ✅ Closed | ~1.8x TBV |
| Oct 2025 | Fifth Third | Comerica | $10.9B | ✅ Closed | ~1.7x TBV |
| Oct 2025 | Huntington | Veritex | $1.9B | ✅ Closed | ~1.6x TBV |
| Oct 2025 | Huntington | Cadence | $7.4B | Approved | ~1.8x TBV |
| 2025 | Synovus | Pinnacle | MOE | Approved | — |
| Dec 2025 | **BHRB** | LINKBANCORP | $354M | Pending Q2 | ~1.3x TBV |
| Feb 2026 | Santander | **WBS** | $12.2B | Pending H2 | ~2.0x TBV |

**Key Pattern:** Deals at 1.6-2.0x TBV for clean franchises. Distressed names avoided.

### What Acquirers Want vs. Avoid

| ✅ Want | ❌ Avoid |
|---------|----------|
| Low-cost deposit franchise (HSA, etc.) | High CRE concentration |
| Geographic diversification | Single-geography exposure |
| Commercial/middle-market strength | Problem loan books |
| Clean balance sheet | Regulatory overhang |
| Growth market presence (TX, Southeast) | Hurricane/DOGE/recession exposure |

### M&A Risk Assessment for Short Candidates

| Bank | Ticker | Assets | M&A Floor? | Why |
|------|--------|--------|------------|-----|
| **EGBN** | EGBN | $11B | 🟡 MAYBE | DC franchise valuable, but distressed = price discovery. Could be fire sale or left behind. |
| **VLY** | VLY | $60B | 🟢 LOW | $7.4B FL CRE is toxic. Who inherits that? Unattractive to acquirers. |
| **WAL** | WAL | $80B | 🟡 MAYBE | Innovation banking valuable, but fraud overhang deters. If cleaned up, attractive. |
| **ZION** | ZION | $90B | 🟠 MODERATE | "Collection of banks" could be broken up or acquired. Clean-ish. |
| **SBCF** | SBCF | $15B | 🟠 MODERATE | FL exposure BUT fortress balance sheet makes it attractive target. M&A floor risk. |
| **SSB** | SSB | $67B | 🟢 LOW | FL+TX correlation = double hurricane/macro exposure. IBTX integration ongoing. |
| **CFG** | CFG | $220B | 🔴 HIGH | Too big for most, but very clean. Scale advantage. |
| **BHRB** | BHRB | $8B | ⛔ IN DEAL | Already acquiring LINKBANCORP. Don't short active merger names. |
| **WBS** | WBS | $80B | ⛔ BEING ACQUIRED | Santander deal closes H2 2026. Off the table. |

### Implication for Shorts

**Best short candidates (no M&A floor):**
- **SSB** — 🔴 **POSITION ACTIVE** — FL+TX correlation, lowest capital, MF 9.36% substandard
- **VLY** — FL CRE concentration makes it unattractive to acquirers (NJ/NY is primary risk)

**Eliminated from consideration:**
- **SBCF** — Fortress balance sheet (14.4% CET1), M&A target risk
- **BKU** — Well-managed (12.3% CET1), credit improving

**Risky to short (M&A floor possible):**
- **EGBN** — Distressed but DC franchise could attract fire-sale bid
- **ZION** — Clean enough to be broken up or acquired

**Do NOT short:**
- **BHRB** — Active acquirer (LINKBANCORP deal)
- **WBS** — Being acquired by Santander

---

## EXPOSURE MATRIX

### Legend
- 🔴 = HIGH exposure (confirmed, material)
- 🟠 = ELEVATED exposure (confirmed, moderate)
- 🟡 = WATCH (potential exposure, needs verification)
- ⬜ = LOW/NONE or data shows minimal
- ❓ = Research gap — needs data

### Channel Key
1. **CRE** = Commercial Real Estate concentration
2. **NDFI** = Non-Depository Financial Institution / Auto warehouse exposure
3. **DC** = Federal employment / DC corridor exposure
4. **BDC** = Business Development Company / Fund Finance credit lines
5. **CONS** = Consumer credit (auto loans, credit cards)
6. **FHLB** = Federal Home Loan Bank dependency (>5% = elevated)
7. **GEO** = Geographic concentration (FL, TX, distressed markets)
8. **MUNI** = Municipal bond holdings / local government credit exposure

---

## TIER 1: MAXIMUM OVERLAP (4+ channels RED/ORANGE)

| Bank | Ticker | CRE | NDFI | DC | BDC | CONS | FHLB | GEO | MUNI | Score | Notes |
|------|--------|-----|------|-----|-----|------|------|-----|------|-------|-------|
| **Eagle Bancorp** | EGBN | 🔴 547% ⚠️**[CONTRADICTED — see banner]** | ⬜ | 🔴 100% | ⬜ | ⬜ | 🟡 6.9% liq | 🔴 DC | 🟠 DC Muni | **11** | "Value Trap" — $140.8M NCOs Q3, taking pain |
| **Western Alliance** | WAL | 🔴 **474%** | 🟡 8% ex-mort | ⬜ | 🟠 Fund Banking | ⬜ | 🟠 5.63% | ⬜ | 🟠 $1.36B unrated | **12** | 🚨 **$3.0B hidden CRE** + 24.2% Memo3/C&I GROWING + Cantor $98M |
| **Valley National** | VLY | 🟠 475% | ⬜ | ⬜ | 🟠 $85M | 🟡 9.3% | 🟡 4.10% | 🔴 FL $7.4B | ⬜ | **9** | FL CRE = 28% of book. Snowbird concentration |
| **Citizens Financial** | CFG | ⬜ | ⬜ | 🟡 Moderate | 🔴 $10-11B | 🟠 18.7% | 🟠 5.10% | 🟡 FL/CA | ⬜ | **8** | Major fund finance + consumer + FHLB |
| **Zions Bancorp** | ZION | 🟡 | 🟠 9% | ⬜ | 🟠 $60M loss | ⬜ | 🟡 4.70% | 🟡 Houston | ⬜ | **6** | FHLB haircut stress, fraud losses |
| **SouthState** | SSB | 🔴 272% | ⬜ | ⬜ | ⬜ | 🟡 | ⬜ | 🔴 FL+TX 42% | ⬜ | **7** | 🔴 **POSITION** — MF 9.36% substandard, 64% floating, HOA direct |

---

## TIER 2: DC CORRIDOR CONCENTRATED

| Bank | Ticker | DC % | CRE | MUNI | GEO | Verdict | Key Quote |
|------|--------|------|-----|------|-----|---------|-----------|
| **Eagle Bancorp** | EGBN | 100% | 🔴 10.9% Office | 🟠 DC bonds | 🔴 Pure DC | **"VALUE TRAP"** | "$140.8M NCOs in Q3 2025 — taking the pain" |
| **Burke & Herbert** | BHRB | ~35% | ⬜ Minimal DC office | 🟠 $922M munis, $54M unrealized loss | 🟡 Diversified WV/KY | **"SAFE HARBOR"** | "No downtown DC exposure" |
| **Atlantic Union** | AUB | ~25% | 🟡 Sold Sandy Spring CRE | ⬜ | 🟢 Defense-focused | **"APEX PREDATOR"** | "0.00% NCOs, 0.07% NPLs in GovCon" |
| **M&T Bank** | MTB | ~10% | ⬜ | ⬜ | 🟢 Buffalo/Baltimore core | **STABLE** | Top-tier retail, diversified |
| **TowneBank** | TOWN | ~5% | ⬜ | ⬜ | 🟢 Hampton Roads focus | **STABLE** | "#1 Hampton Roads, minimal NoVA" |

**DC Corridor Summary:**
- EGBN is the pure-play stress trade (but already in crisis)
- AUB successfully de-risked via Sandy Spring acquisition marks
- BHRB hedged via Appalachian diversification, but watch muni portfolio
- Suburban NoVA (defense) is holding; DC proper and PG County are stressed

---

## TIER 3: FLORIDA CONCENTRATED

| Bank | Ticker | FL % | FL CRE | FL Branches | Focus | Risk Level |
|------|--------|------|--------|-------------|-------|------------|
| **Valley National** | VLY | ~25% | $7.4B (28%) | 45+ | Miami/Tampa CRE | 🔴 VERY HIGH |
| **First Horizon** | FHN | ~18% | Unknown | 76 | Panhandle + Miami wealth | 🟠 HIGH |
| **Seacoast Banking** | SBCF | >90% | High | Dense | Villages dominance | 🔴 PURE PLAY (SKIP) |
| **SouthState** | SSB | ~23% + TX 19% | **$17.9B (37%)** | 251 total | FL + TX Sunbelt CRE | 🔴 **POSITION** |
| **ServisFirst** | SFBS | ~30% | Moderate | 10 | Panhandle/Central corridor | 🟠 |
| **BankUnited** | BKU | >60% | High | Dense | Miami commercial | 🟢 SKIP (well-managed) |
| **Flagstar** | FLG | ~8% | Moderate | 26 | South FL | 🟡 |
| **Citizens** | CFG | ~5% | Low | Branch-light | Wealth/Commercial only | 🟡 |

### 🔴 SSB DEEP DIVE — POSITION ACTIVE (Feb 11, 2026)

**Position:** 2x $90P Jun 18, 2026 @ $1.86 ($373 risk)

**Why SSB over VLY/SBCF:**
| Factor | SSB | VLY | SBCF |
|--------|-----|-----|------|
| CET1 | **11.4%** (lowest) | 10.2% | 14.4% |
| CRE/Loans | **37%** | 28% | ~25% |
| FL + TX | 42% combined | NJ/NY primary | 100% FL |
| M&A Risk | LOW | LOW | HIGH |
| HOA Direct | **Yes (Assoc. Prime)** | Yes | Counter-cyclical |

**Critical MF Finding:**
- **Substandard: 9.36%** (highest of ANY CRE category at SSB)
- **Non-Accrual: 0.02%** (near zero)
- **Explanation: "Support and Survive"** — borrowers subsidizing negative carry to protect 48% equity stakes
- **Risk:** Sponsor liquidity is finite; if "higher for longer" persists, exhaustion → NPL spike

**MF Portfolio Profile:**
- Total exposure: ~$4.4B (~9% of loans)
- 64% floating rate = massive Fed sensitivity
- Vintage risk: 2021-2023 cohort "broken" (originated 3-4%, now at 8%+)
- Geographic: GA 38%, FL 24%, TX 14% (Atlanta/Austin supply gluts + FL insurance crisis)

**Short Interest & Positioning:**
- 2.43% of float (BELOW peer avg 3.42%) — contrarian position
- 89.76% institutional ownership — "dip-buying floor"
- Beta 0.74 — defensive, "flight to quality"
- Analysts: 11 Strong Buy, 1 Buy, 3 Hold, 0 Sell

**Thesis:** Contrarian MACRO bet. SSB is well-run, but even quality banks have CRE concentration. MF stress already visible (9.36% substandard), masked by "Support and Survive." Higher-for-longer + macro event = sponsor exhaustion.

**Monitor:** Q1 2026 earnings (~late April) — substandard trend, NCO trajectory, NPL migration

**Full thesis:** `../CORAL/research/SSB_THESIS.md`

**Florida Summary:**
- **SSB is the FL single-name play** — lowest capital, highest CRE, MF stress visible
- VLY has FL exposure but NJ/NY is primary market
- SBCF is pure FL but fortress balance sheet + M&A target = SKIP
- BKU well-managed, credit improving = SKIP
- FHN has diversification via Tennessee core
- If Citizens Insurance ($678B exposure) or condo crisis accelerates, VLY/FHN/SBCF hit first

---

## TIER 4: GEOGRAPHIC FOOTPRINT MATRIX

| Bank | Ticker | HQ | Primary States | Top MSAs | DC | FL | TX Border | SoCal |
|------|--------|-----|----------------|----------|-----|-----|-----------|-------|
| **AUB** | AUB | Richmond, VA | VA, MD, NC | Richmond, Hampton Roads, DC Metro | 🟠 | ⬜ | ⬜ | ⬜ |
| **BHRB** | BHRB | Alexandria, VA | VA, WV, KY | DC Metro, Charleston WV, Lexington KY | 🟠 | ⬜ | ⬜ | ⬜ |
| **CFG** | CFG | Providence, RI | MA, PA, NY | Boston, Philly, NYC, Detroit | 🟡 | 🟡 | ⬜ | 🟡 CA |
| **DCOM** | DCOM | Hauppauge, NY | NY only | Long Island, Brooklyn/Queens | ⬜ | ⬜ | ⬜ | ⬜ |
| **EGBN** | EGBN | Bethesda, MD | MD, DC, VA | DC Metro (100%) | 🔴 | ⬜ | ⬜ | ⬜ |
| **FHN** | FHN | Memphis, TN | TN, FL, NC, LA | Memphis, Nashville, New Orleans, Miami | ⬜ | 🟠 | ⬜ | ⬜ |
| **FLG** | FLG | Hicksville, NY | NY, MI, FL | NYC Metro, Detroit, Miami | ⬜ | 🟡 | ⬜ | 🟡 8 loc |
| **HBAN** | HBAN | Columbus, OH | OH, MI, PA, IN, IL, MN | Columbus, Detroit, Cleveland, Chicago | ⬜ | ⬜ | ⬜ | ⬜ |
| **MTB** | MTB | Buffalo, NY | NY, MD, CT, PA, MA | Buffalo, Baltimore, Bridgeport, DC | 🟡 | ⬜ | ⬜ | ⬜ |
| **SFBS** | SFBS | Birmingham, AL | AL, FL, TN, GA | Birmingham, Tampa, Nashville, Pensacola | ⬜ | 🟠 | ⬜ | ⬜ |
| **TOWN** | TOWN | Suffolk, VA | VA, NC | Hampton Roads (#1), Richmond, Charlotte | ⬜ | ⬜ | ⬜ | ⬜ |
| **VLY** | VLY | New York, NY | NJ, NY, FL, AL, CA | NY/NJ Metro, Miami, Tampa, LA | ⬜ | 🔴 | ⬜ | 🟡 5 loc |
| **WAL** | WAL | Phoenix, AZ | AZ, NV, CA | Phoenix, Las Vegas, San Diego, San Jose | ⬜ | ⬜ | ⬜ | 🟠 Coastal |
| **WBS** | WBS | Stamford, CT | CT, NY, MA, RI | Stamford, Westchester, Hartford, Boston | ⬜ | ⬜ | ⬜ | ⬜ |
| **ZION** | ZION | Salt Lake City, UT | UT, CA, TX, AZ, NV | SLC, Houston, LA, Phoenix, Seattle | ⬜ | ⬜ | ⬜ | 🟠 CB&T |

---

## TIER 5: CONSUMER CREDIT CONCENTRATION

| Bank | Ticker | Consumer % | Focus | Risk Level |
|------|--------|------------|-------|------------|
| **Huntington** | HBAN | 44.0% | Auto Finance/Indirect | 🔴 Highest |
| **Popular** | BPOP | 22.1% | Credit Card/Personal | 🟠 |
| **Citizens** | CFG | 18.7% | Auto/Student | 🟠 |
| **Regions** | RF | 16.4% | Direct Auto/CC | 🟠 |
| **Truist** | TFC | 15.8% | Diversified Retail | 🟠 |
| **Ameris** | ABCB | 14.6% | Consumer/Installment | 🟡 |
| **M&T Bank** | MTB | 13.9% | Indirect Auto/Dealer | 🟡 |

---

## TIER 6: FHLB DEPENDENCY (>4% of Assets)

| Bank | Ticker | FHLB Ratio | Risk Level |
|------|--------|------------|------------|
| **Columbia Banking** | COLB | 9.80% | 🔴 Nearly 2x peers |
| **Western Alliance** | WAL | 5.63% | 🟠 |
| **KeyCorp** | KEY | 5.30% | 🟠 |
| **First Citizens** | FCNCA | 5.20% | 🟠 |
| **Citizens Financial** | CFG | 5.10% | 🟠 |
| **UMB Financial** | UMBF | 4.90% | 🟡 |
| **Webster Financial** | WBS | 4.80% | 🟡 |
| **Zions** | ZION | 4.70% | 🟡 |
| **Huntington** | HBAN | 4.50% | 🟡 |
| **East West** | EWBC | 4.40% | 🟡 |
| **Flagstar** | FLG | 4.30% | 🟡 |
| **Valley National** | VLY | 4.10% | 🟡 |

---

## FUND FINANCE / BDC EXPOSURE MATRIX

| Bank | Ticker | Desk/Unit | Products | Activity (2025-26) | Risk |
|------|--------|-----------|----------|---------------------|------|
| **Citizens** | CFG | Citizens Private Bank | SLCFs, GP Co-Invest, Liquidity Lines | Launched PE/VC liquidity lines | 🔴 |
| **Western Alliance** | WAL | Innovation Banking | Fund Banking, Lender Finance | 44% C&I concentration | 🟠 |
| **U.S. Bancorp** | USB | NDFI Specialized Desk | BDC Facilities, Sub Lines | 12% of total loans | 🟠 |
| **First Citizens** | FCNCA | Global Fund Banking | PE/VC Subscription Lines | Ex-SVB leadership | 🟠 |
| **Fifth Third** | FITB | Specialized Lending | BDC Facilities, ABLs | Reviewing after $178M loss | 🟠 |
| **Zions** | ZION | Commercial Banking | Middle Market BDC | $60M charge, VIN verification | 🟠 |
| **KeyCorp** | KEY | Specialty Finance | REITs, CLOs, Fund Lending | Avoiding "esoteric" NDFI | 🟡 |
| **Valley National** | VLY | Commercial | BDC Facilities | $85M Saratoga facility | 🟠 |

---

## CONVERGENCE SCORE: BANKS WITH MAXIMUM OVERLAP

**Scoring: 🔴 = 3 pts, 🟠 = 2 pts, 🟡 = 1 pt**

| Rank | Bank | Ticker | CRE | NDFI | DC | BDC | CONS | FHLB | GEO | MUNI | Total | Key Vulnerabilities |
|------|------|--------|-----|------|-----|-----|------|------|-----|------|-------|---------------------|
| 1 | **Eagle Bancorp** | EGBN | 3 | 0 | 3 | 0 | 0 | 1 | 3 | 2 | **12** | Pure DC play, already in crisis |
| 2 | **Western Alliance** | WAL | 3 | 1 | 0 | 2 | 0 | 2 | 0 | 2 | **12** | 🚨 **$3.0B hidden CRE (24.2% Memo3/C&I, GROWING)** + $1.36B unrated munis + Cantor $98M |
| 3 | **Valley National** | VLY | 2 | 0 | 0 | 2 | 1 | 1 | 3 | 0 | **9** | FL CRE = 28% of book |
| 4 | **Citizens Financial** | CFG | 0 | 0 | 1 | 3 | 2 | 2 | 1 | 0 | **9** | Fund finance concentration + FHLB |
| 5 | **Zions** | ZION | 1 | 2 | 0 | 2 | 0 | 1 | 0 | 3 | **9** | **$5.78B muni exposure** + $524M unfunded + fraud |
| 6 | **M&T Bank** | MTB | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 2 | **4** | **61% NY State muni concentration** |
| 7 | **Truist** | TFC | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 0 | **5** | NDFI + Consumer |
| 8 | **Burke & Herbert** | BHRB | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 2 | **5** | DC exposure + **munis = majority of AFS** |
| 9 | **Fifth Third** | FITB | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | **4** | Direct fraud exposure |
| 10 | **Columbia Banking** | COLB | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | **3** | Extreme FHLB (9.8%) |

---

## SINGLE-NAME SHORT CANDIDATES (FINAL RANKING)

**Incorporating: Convergence Score + M&A Risk + Thesis Expression**

### 🎯 TOP TIER: Best Risk/Reward (High Score + Low M&A Floor)

| Rank | Bank | Ticker | Score | M&A Risk | Thesis | Why Top Tier |
|------|------|--------|-------|----------|--------|--------------|
| **1** | **Western Alliance** | WAL | 12 | 🟡 MAYBE | Hidden CRE + Multi-channel | 🚨 **PRIMARY TARGET** — $3.0B hidden CRE, ONLY bank with growing Memo3/C&I ratio (24.2%), management confirmed "remixing into C&I" = relabeling. Cantor Mar, Q1 Apr, Investor Day May 12. |
| **2** | **Valley National** | VLY | 9 | 🟢 LOW | FL + Multi-channel | $7.4B FL CRE makes it unattractive to acquirers. 4 paths to stress. Not priced for distress. |
| **3** | **Seacoast** | SBCF | N/A | 🟢 LOW | FL Insurance | 100% FL = pure hurricane liability. No rational buyer. Purest FL expression. |

### 🟡 SECOND TIER: Good Thesis, Some M&A Risk

| Rank | Bank | Ticker | Score | M&A Risk | Thesis | Notes |
|------|------|--------|-------|----------|--------|-------|
| 4 | **Eagle Bancorp** | EGBN | 12 | 🟡 MAYBE | DC/DOGE | Highest score, but distressed = fire sale bid possible. Already priced for pain. |
| 5 | **Zions** | ZION | 9 | 🟠 MODERATE | Muni/Multi | $5.78B muni exposure, but clean enough for M&A. Could be broken up. |
| 6 | **Citizens Financial** | CFG | 9 | 🔴 HIGH | Fund Finance | Too big/clean for most acquirers. Scale = defensive moat. |

### ⛔ DO NOT SHORT

| Bank | Ticker | Why |
|------|--------|-----|
| **Burke & Herbert** | BHRB | **Active acquirer** — buying LINKBANCORP (closes Q2 2026) |
| **Webster** | WBS | **Being acquired** — Santander deal closes H2 2026 |
| **Huntington** | HBAN | **Active acquirer** — Veritex + Cadence deals, consolidator mode |
| **Fifth Third** | FITB | **Active acquirer** — Comerica deal just closed |

### Geographic Pure Plays (Outside KRE)

| Bank | Ticker | Region | M&A Risk | Notes |
|------|--------|--------|----------|-------|
| **IBC** | IBOC | TX Border | 🟢 LOW | Only TX border play. Existential Mexico risk. Not in KRE. |
| **BankUnited** | BKU | FL 60%+ | 🟢 LOW | Miami commercial concentration. Same FL thesis as SBCF. |

---

### Summary: Recommended Short Targets

**For KRE convergence thesis:**
1. **VLY** — Multi-channel + FL + No M&A floor
2. **SBCF** — Purest FL insurance expression + No M&A floor

**For specific thesis channels:**
- **IBOC** — MARCO/TX border thesis (outside KRE)
- **WAL** — Multi-channel if willing to accept M&A uncertainty
- **EGBN** — DC/DOGE thesis if willing to accept fire-sale risk

**Current position:** KRE puts capture broad regional stress. Single-name additions (VLY, SBCF) would add leverage to FL thesis specifically.

---

## NOTABLE FINDINGS

### The DC Divergence
The research reveals a **three-tier structure** in DC-exposed banks:
1. **EGBN** — Pure play, already taking pain, "value trap"
2. **BHRB** — Hedged via Appalachian diversification, watch muni portfolio
3. **AUB** — De-risked successfully, "apex predator" positioning

**Actionable insight:** EGBN may be priced for distress already. The *relative trade* might be long AUB / short EGBN if you believe AUB's de-risking worked.

### The Florida Correlation
VLY, FHN, SFBS, SBCF, BKU all have material FL exposure. If the FL property/insurance cycle turns:
- VLY hits hardest (28% CRE concentration in FL)
- SBCF/BKU are pure plays
- FHN has Tennessee hedge
- SFBS has Panhandle focus (different from Miami/Southeast FL dynamics)

### The Texas Border Absence
**No major KRE constituent has TX border concentration.**
- IBOC (IBC Bank) is the only regional with Laredo/McAllen/Brownsville dominance
- MARCO immigration thesis impacts IBOC directly, but minimal KRE-wide transmission
- Border stress → IBOC, not KRE broadly

### The Municipal "Shadow Risk" (RP-REG-3.2)
Two banks have hidden municipal exposure that doesn't show on the securities line:

**ZION — The Municipal Lender:**
- $1.4B in muni securities
- **$4.36B in municipal LOANS** (distinct asset class)
- **$524M in unfunded commitments** (contingent liquidity risk)
- Total: **$5.78B** — makes ZION a quasi-municipal specialist
- **Conduit risk:** $11M in nonaccrual muni loans linked to private entities using municipal pass-throughs

**WAL — The Unrated Book:**
- $1.36B in HTM munis classified as **"Unrated"**
- This isn't junk — it's direct purchases/private placements
- Bank performs internal underwriting, no public rating
- **Shadow loan book** disguised as securities
- Likely heavy LIHTC (low-income housing tax credit) exposure (19.9% of Tier 1 capital)

### Texas Border Municipal Health (RP-REG-3.4)
| Municipality | Rating | Key Risk |
|--------------|--------|----------|
| **El Paso** | AA | Pension stress (75% funded fire/police) |
| **Laredo** | AA | **Water crisis** — S&P flagged explicitly |
| **McAllen** | AA+ | Strong (60%+ reserves) |
| **Brownsville** | AA+ | Turnaround story (SpaceX/LNG) |
| **Webb County** | AA | **115-120% overfunded pension** — fortress |

**The "Barclays Void":** Cullen/Frost and Texas Capital filling gap left by banned global banks. Credit risk concentrating in TX regional balance sheets.

---

## DATA SOURCES

**Research Prompts Completed (All 5):**
- **RP-REG-3.1:** Regional Bank Geographic Footprints (Feb 2026)
- **RP-REG-3.2:** Municipal Securities Exposure Analysis (Feb 2026)
- **RP-REG-3.3:** DC Corridor Bank Analysis (Feb 2026)
- **RP-REG-3.4:** Texas Border Municipal Analysis (Feb 2026)
- **RP-REG-3.5:** Florida Insurance/Banking Nexus (Feb 2026)

**Other Sources:**
- FHLB Dependency: Q4 2025 Call Reports, Capital Advisors Research
- Fund Finance: Reed Smith FFA 2025, Goodwin Fund Finance Report, Bank 10-Ks
- Consumer Credit: JD Power Dealer Financing Study, Experian Auto Finance Report
- NDFI: Capital Advisors "Regional Bank Private Credit Exposure" Nov 2025
- CRE: FAU CRE Screener, REGINALD workbook

---

## UPDATE LOG

| Date | Update | Source |
|------|--------|--------|
| 2026-02-23 13:50 | 🚨 **MAJOR** — Hidden CRE screen (Memo Item 3), Metropolitan Capital autopsy, Chicago loss severity, WAL promoted to PRIMARY TARGET | Prome deep research |
| 2026-02-05 00:20 | **COMPLETE** — FL Insurance/Banking Nexus (RP-REG-3.5) | Will's research |
| 2026-02-04 23:40 | Santander/Webster acquisition noted (M&A context) | News |
| 2026-02-04 23:05 | Municipal securities + TX border research integrated (RP-REG-3.2, 3.4) | Will's research |
| 2026-02-04 22:15 | Geographic + DC corridor research integrated (RP-REG-3.1, 3.3) | Will's research |
| 2026-02-04 20:55 | Full matrix populated with research from Prompts 1-4 | Will's LLM research |
| 2026-02-04 20:47 | Matrix structure created with existing agent data | Prome |

---

## RESEARCH COMPLETE ✅

All 5 geographic/municipal research prompts integrated. Matrix now covers:
- DC Corridor stress (DOGE/federal layoffs)
- Florida insurance "doom loop" (Citizens $678B TIV)
- Texas border municipal health (water crisis, pension stress)
- Municipal securities holdings by bank
- Geographic footprint mapping

---

## TEXAS BORDER BANKING ECOSYSTEM

**The "Domesticated" Credit Risk:**

| Bank | Ticker | Assets | Role | Key Exposure |
|------|--------|--------|------|--------------|
| **IBC** | IBOC | $16.6B | Laredo sovereign | **Existential** Mexico/trade risk |
| **Cullen/Frost** | CFR | $50B+ | TX muni holder | 100% TX portfolio ($5.2B munis) |
| **Texas Capital** | TCBI | $30B+ | Public finance expansion | Filling "Barclays Void" |
| **Prosperity** | PB | $35B+ | RGV consolidator | 30 South TX locations |
| **WestStar** | Private | $3.1B | El Paso dominant | Maquiladora supply chain |
| **Lone Star National** | Private | $3.2B | RGV dominant | Hidalgo County CRE |

**Note:** IBOC is the **only** publicly traded bank with material TX border concentration. If MARCO thesis plays out, this is the single-name expression.

---

*Next: Monitor Q1 2026 earnings for confirmation of stress in Tier A names*
*Watch: Laredo water levels, El Paso pension contributions, IBOC trade finance book*
