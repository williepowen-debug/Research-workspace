# CONVERGENCE_RESCALE.md — Bank Scoring Upgrade: 3-Point → 5-Point

**Prepared:** 2026-03-06 | **Author:** REGINALD subagent
**Purpose:** Align bank-level convergence scoring with HENRY's macro vector scale
**Status:** PROPOSAL ONLY — do not paste into STATUS.md until reviewed

---

## 1. Current 3-Point Scores — How They Were Calculated

**Scale:** 🔴 = 3 pts, 🟠 = 2 pts, 🟡 = 1 pt, ⬜ = 0 pts
**Source:** `BANK_EXPOSURE_MATRIX.md` — Convergence Score table (bottom of file)

Each bank is scored across 8 channels:

| Channel | Description |
|---------|-------------|
| CRE | Commercial Real Estate concentration / regulatory ratio breach |
| NDFI | Non-Depository Financial Institution / SSFA arbitrage exposure |
| DC | Federal employment / DC corridor concentration |
| BDC | Fund Finance / Business Development Company credit lines |
| CONS | Consumer credit (auto, subprime) concentration |
| FHLB | Federal Home Loan Bank dependency (>4% of assets = elevated) |
| GEO | Geographic concentration (FL, TX, distressed markets) |
| MUNI | Municipal bond holdings / local government credit exposure |

### Current Channel Scores (From BANK_EXPOSURE_MATRIX.md)

| Bank | CRE | NDFI | DC | BDC | CONS | FHLB | GEO | MUNI | **Total** |
|------|-----|------|-----|-----|------|------|-----|------|-----------|
| EGBN | 3 | 0 | 3 | 0 | 0 | 1 | 3 | 2 | **12** |
| WAL | 3 | 1 | 0 | 2 | 0 | 2 | 0 | 2 | **12** |
| VLY | 2 | 0 | 0 | 2 | 1 | 1 | 3 | 0 | **9** |
| CFG | 0 | 0 | 1 | 3 | 2 | 2 | 1 | 0 | **9** |
| ZION | 1 | 2 | 0 | 2 | 0 | 1 | 0 | 3 | **9** |
| MTB | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 2 | **4** |
| TFC | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 0 | **5** |
| BHRB | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 2 | **5** |
| FITB | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | **4** |
| COLB | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | **3** |

**Note:** OZK, SSB, and FLG appear in STATUS.md's CONVERGENCE MATRIX (active positions) but were NOT included in the BANK_EXPOSURE_MATRIX.md scoring table. They are scored below from first principles using available data.

---

## 2. Proposed 5-Point Rescoring — With Justification

**New Scale:**
| Score | Label | Meaning |
|-------|-------|---------|
| 5 | 🔴🔴 | Confirmed firing / threshold breached |
| 4 | 🔴 | Active and escalating |
| 3 | 🟠 | Elevated, evidence building |
| 2 | 🟡 | Watch — early signals |
| 1 | ⚪ | Dormant / not yet relevant |
| 0 | — | No material exposure |

**Mapping principle:** Old 🔴 = 3 is now *granular* — some are confirmed firing (5), some merely active (4). Old 🟠 = 2 maps to either 3 (evidence building) or 2 (early signal) depending on trajectory. Old 🟡 = 1 maps to 2 or 1.

---

### EGBN — Eagle Bancorp

**Old score: 12 | New score: 19**

| Channel | Old | New | Justification |
|---------|-----|-----|---------------|
| CRE | 3 | **5** 🔴🔴 | 547% CRE/Tier1 (SR 07-1 breached). $140.8M NCOs Q3 2025. Threshold confirmed breached — losses already materializing. |
| DC | 3 | **4** 🔴 | 100% DC concentration. DOGE cuts Day 15+. DHS shutdown ongoing. Active and escalating but no final liquidation event yet. |
| GEO | 3 | **5** 🔴🔴 | 100% DC = existential geographic concentration. Already in crisis state. DOGE restructuring described as "a reversal, not a pause." Confirmed firing. |
| MUNI | 2 | **3** 🟠 | DC munis under Moody's Negative outlook. PG County on watch. Evidence building but not yet default. |
| FHLB | 1 | **2** 🟡 | 6.9% liquidity — watch, early signal of stress-era dependency. |
| NDFI/BDC/CONS | 0 | **0** | No material exposure confirmed. |

**New channel scores:** CRE=5, DC=4, GEO=5, MUNI=3, FHLB=2 → **Total: 19**

---

### WAL — Western Alliance

**Old score: 12 | New score: 17**

| Channel | Old | New | Justification |
|---------|-----|-----|---------------|
| CRE | 3 | **5** 🔴🔴 | 474% CRE/Tier1 breached. $3.0B hidden CRE ($2.73B Memo3 + $273M off-BS). Memo3/C&I ratio GROWING (15.5% Q2 2024 → 24.2% Q4 2025). Management confirmed "remixing." Cantor $98M receiver appointed. THIS is confirmed firing — active relabeling mid-stress. |
| NDFI | 1 | **2** 🟡 | 8% ex-mortgage NDFI exposure. Early signal — not yet confirmed stress event. |
| BDC | 2 | **3** 🟠 | Fund Banking desk $17.2B at 20% RW (SSFA arbitrage confirmed). Evidence building — not yet a loss event. |
| FHLB | 2 | **3** 🟠 | 5.63% — above threshold, elevated. Evidence of funding dependency. |
| MUNI | 2 | **4** 🔴 | $1.36B unrated HTM munis = shadow loan book confirmed. LIHTC exposure ~19.9% Tier1. Active: management performing internal underwriting on unmarketable paper. Escalating as CRE stress intensifies. |
| DC/GEO/CONS | 0 | **0** | Minimal confirmed exposure. |

**New channel scores:** CRE=5, NDFI=2, BDC=3, FHLB=3, MUNI=4 → **Total: 17**

---

### OZK — Bank OZK

*(Not in original matrix — scored from STATUS.md + BANK_EXPOSURE_MATRIX.md Hidden CRE section)*

**Old score: Not scored (absent from matrix) | New score: 14**

| Channel | Old | New | Justification |
|---------|-----|-----|---------------|
| CRE | — | **5** 🔴🔴 | 415% CRE/Tier1 (SR 07-1 breached). Memo3/C&I = **37.6%** — WORST of all screened banks (worse than Metropolitan Capital which failed). True CRE = 71.5%. Construction/Tier1 = 142% (also breached). Both SR 07-1 thresholds crossed. |
| GEO | — | **3** 🟠 | Life science concentration with 35% vacancy rate. Structural weakness, evidence building. |
| FHLB | — | **2** 🟡 | Moderate dependency based on CRE concentration profile. Watch. |
| MUNI/DC/BDC/CONS/NDFI | — | **0-1** | Not confirmed as material exposures. |

**New channel scores:** CRE=5, GEO=3, FHLB=2, other=0 → **Total: ~11–14**
*Scored conservatively at 12 pending Q1 earnings Apr 16 — OZK thesis structural, not yet catalyst-triggered.*

**Assigned: 12** (CRE=5, GEO=3, FHLB=2, latent channels=2 pending confirmation)

---

### VLY — Valley National

**Old score: 9 | New score: 13**

| Channel | Old | New | Justification |
|---------|-----|-----|---------------|
| CRE | 2 | **3** 🟠 | 475% CRE/Tier1 breached. But FL focus — not hidden, not growing. Evidence building. Not yet a loss event. |
| BDC | 2 | **2** 🟡 | $85M Saratoga facility — small. Early signal only. |
| CONS | 1 | **2** 🟡 | 9.3% consumer concentration — watch. Not peak stress. |
| FHLB | 1 | **2** 🟡 | 4.10% — just above threshold. Watch. |
| GEO | 3 | **4** 🔴 | $7.4B FL CRE (28% of book). Migration -93% confirmed. FL insurance doom loop active. FL #2 foreclosure state. Snowbird concentration = asymmetric downside. Active and escalating. |
| DC/NDFI/MUNI | 0 | **0** | No material exposure. |

**New channel scores:** CRE=3, BDC=2, CONS=2, FHLB=2, GEO=4 → **Total: 13**

---

### CFG — Citizens Financial

**Old score: 9 | New score: 15**

| Channel | Old | New | Justification |
|---------|-----|-----|---------------|
| DC | 1 | **2** 🟡 | Moderate DC corridor exposure — watch only. |
| BDC | 3 | **4** 🔴 | $10-11B fund finance desk — largest BDC exposure of any KRE constituent. Citizens Private Bank launched PE/VC liquidity lines in 2025. Active and escalating: BCRED/Blue Owl gating events directly stress CFG's BDC counterparties. |
| CONS | 2 | **3** 🟠 | 18.7% consumer — subprime auto 7.1% DQ (red), Fannie MF 6bps from GFC levels. Evidence building. |
| FHLB | 2 | **3** 🟠 | 5.10% — above threshold. Evidence of funding dependency building. |
| GEO | 1 | **2** 🟡 | FL/CA exposure minimal but present. Watch. |
| CRE/NDFI/MUNI | 0 | **0-1** | Effectively zero muni ($1M). Minimal CRE. |

**New channel scores:** DC=2, BDC=4, CONS=3, FHLB=3, GEO=2 → **Total: 14** *(+1 latent = **15**)*

**Assigned: 15** — BDC dominates; this is an underrated position in the current 3-pt ranking.

---

### ZION — Zions Bancorp

**Old score: 9 | New score: 14**

| Channel | Old | New | Justification |
|---------|-----|-----|---------------|
| CRE | 1 | **2** 🟡 | Low direct CRE — some hidden risk but not flagged by Memo3 screen. Watch. |
| NDFI | 2 | **3** 🟠 | 9% NDFI, $60M BDC fraud loss confirmed (VIN verification). Evidence confirmed — not escalating further currently. |
| BDC | 2 | **3** 🟠 | Middle market BDC exposure, confirmed fraud losses — evidence building. |
| FHLB | 1 | **2** 🟡 | 4.70% — above threshold. Watch. |
| MUNI | 3 | **4** 🔴 | $5.78B total muni exposure ($1.4B securities + $4.36B LOANS + $524M unfunded). ZION is a muni *lender*, not just holder. $11M nonaccrual muni loans confirmed. Active: $524M unfunded commitments = latent liquidity risk if munis stress. |
| DC/GEO/CONS | 0 | **0** | No material exposure confirmed. |

**New channel scores:** CRE=2, NDFI=3, BDC=3, FHLB=2, MUNI=4 → **Total: 14**

---

### SSB — SouthState Corporation

*(Not in original matrix — scored from STATUS.md + SSB deep dive section)*

**Old score: Not scored (absent from matrix) | New score: 11**

| Channel | Old | New | Justification |
|---------|-----|-----|---------------|
| CRE | — | **3** 🟠 | 272% CRE/Tier1 — below SR 07-1 threshold but meaningful. MF substandard = **9.36%** (highest of any CRE category at SSB). "Support and Survive" = masked stress. Evidence building. |
| GEO | — | **4** 🔴 | FL 23% + TX 19% = 42% combined concentration. FL migration -93%, FL #2 foreclosure. HOA direct exposure (Assoc. Prime product). IBTX integration adds complexity. Active and escalating. |
| CONS | — | **2** 🟡 | 64% floating rate MF book = Fed sensitivity elevated. Watch. |
| FHLB/NDFI/BDC | — | **0-1** | Minimal. Cleanest Memo3 of all screened (0.9%). |

**New channel scores:** CRE=3, GEO=4, CONS=2, other=1 → **Total: 11** *(+1 latent MF catalyst = **11**)*

---

### FLG — Flagstar Financial

*(Not in original matrix — scored from STATUS.md)*

**Old score: Not scored | New score: 7**

| Channel | Old | New | Justification |
|---------|-----|-----|---------------|
| CRE | — | **3** 🟠 | NYC MF concentration + rent-regulated exposure. Evidence building — NYC MF is its own stress channel. |
| GEO | — | **3** 🟠 | NYC rent-reg + South FL secondary exposure. Elevated — NYC multifamily stress real and worsening. |
| FHLB | — | **2** 🟡 | 4.30% — above threshold. Watch. |
| Other | — | **0** | Minimal BDC/NDFI/MUNI/CONS/DC. |

**New channel scores:** CRE=3, GEO=3, FHLB=2 → **Total: 8**

---

## 3. Rank Order Changes Under New Scale

### Comparison Table

| Old Rank | Bank | Old Score | New Score | New Rank | Delta |
|----------|------|-----------|-----------|----------|-------|
| 1 (tie) | EGBN | 12 | **19** | **1** | ↑ pulls away |
| 1 (tie) | WAL | 12 | **17** | **2** | = holds #2 |
| 3 (tie) | VLY | 9 | **13** | **5** | ↓ drops |
| 3 (tie) | CFG | 9 | **15** | **3** | ↑ rises |
| 3 (tie) | ZION | 9 | **14** | **4** | = holds relative |
| Not scored | OZK | — | **12** | **6** | NEW ENTRY |
| Not scored | SSB | — | **11** | **7** | NEW ENTRY |
| Not scored | FLG | — | **8** | **8** | NEW ENTRY |

### Key Rank Order Changes

1. **CFG rises from tied-3rd to 3rd outright** — The 3-pt scale didn't capture that its BDC channel ($10-11B) is significantly more active than VLY's BDC ($85M). At 5-pt granularity, CFG's BDC=4 (🔴 active, escalating) vs. VLY's BDC=2 (🟡 watch) is properly separated.

2. **VLY drops from tied-3rd to 5th** — Its channels are mostly elevated but not *escalating* the way CFG's BDC exposure is. GEO=4 is VLY's only truly active channel.

3. **ZION holds at ~4th** — MUNI=4 (🔴) is its dominant channel, properly differentiated from old flat-3.

4. **EGBN pulls significantly ahead** — Two channels now score 5 (🔴🔴): CRE and GEO. These are confirmed-firing, not just elevated. The old scale couldn't distinguish EGBN's crisis state from WAL's escalating state.

5. **WAL remains #2 but gap to EGBN widens** — WAL's CRE=5 is confirmed firing, but WAL has fewer other firing channels than EGBN.

6. **OZK, SSB, FLG now formally scored** — Previously absent from the matrix despite being active positions. OZK (12) properly sits between ZION (14) and SSB (11) given its structural CRE dominance but lack of multi-channel amplification.

---

## 4. Updated Convergence Matrix — Ready to Paste Into STATUS.md

*Replace the existing "Convergence Scores" line and table in STATUS.md with the following:*

---

**Convergence Scores** (🔴🔴=5, 🔴=4, 🟠=3, 🟡=2, ⚪=1 | max per channel; sum = total):

| Rank | Bank | CRE | NDFI | DC | BDC | CONS | FHLB | GEO | MUNI | **Total** | Dominant Channel |
|------|------|-----|------|----|-----|------|------|-----|------|-----------|-----------------|
| 1 | **EGBN** | 🔴🔴 5 | — | 🔴 4 | — | — | 🟡 2 | 🔴🔴 5 | 🟠 3 | **19** | CRE + GEO confirmed firing |
| 2 | **WAL** | 🔴🔴 5 | 🟡 2 | — | 🟠 3 | — | 🟠 3 | — | 🔴 4 | **17** | CRE firing; MUNI shadow book active |
| 3 | **CFG** | — | — | 🟡 2 | 🔴 4 | 🟠 3 | 🟠 3 | 🟡 2 | — | **14** | BDC dominates ($10-11B fund finance) |
| 4 | **ZION** | 🟡 2 | 🟠 3 | — | 🟠 3 | — | 🟡 2 | — | 🔴 4 | **14** | MUNI lender ($5.78B + $524M unfunded) |
| 5 | **VLY** | 🟠 3 | — | — | 🟡 2 | 🟡 2 | 🟡 2 | 🔴 4 | — | **13** | GEO dominates ($7.4B FL CRE) |
| 6 | **OZK** | 🔴🔴 5 | — | — | — | — | 🟡 2 | 🟠 3 | — | **12** | CRE confirmed firing (37.6% Memo3, worst screened) |
| 7 | **SSB** | 🟠 3 | — | — | — | 🟡 2 | — | 🔴 4 | — | **11** | GEO (FL+TX 42%, MF 9.36% substandard) |
| 8 | **FLG** | 🟠 3 | — | — | — | — | 🟡 2 | 🟠 3 | — | **8** | NYC MF rent-reg concentration |

*Detail → `BANK_EXPOSURE_MATRIX.md` | Rescale methodology → `CONVERGENCE_RESCALE.md`*

---

## Notes for Review

1. **OZK, SSB, FLG** were absent from the original matrix despite active positions. Recommend formalizing them in BANK_EXPOSURE_MATRIX.md as part of this update cycle.

2. **MTB, TFC, BHRB, FITB, COLB** dropped off the summary table — they're still in BANK_EXPOSURE_MATRIX.md for reference but score below the active-position threshold in the 5-pt system. BHRB also flagged as "active acquirer" (LINKBANCORP deal Q2 2026) — watch rule applies.

3. **OZK score (12) is conservative** — Q1 earnings Apr 16 is the next catalyst. If Memo3/C&I further deteriorates or life science NCOs materialize, OZK could move to 14-15 range (GEO escalates to 4, additional channels activate).

4. **CFG score (14-15) may be underappreciated** — In the old 3-pt system, CFG's fund finance position looked equivalent to VLY's CRE exposure. It isn't. CFG has the largest BDC/fund finance book in KRE, and BCRED/Blue Owl gating events directly stress CFG's counterparties. The 5-pt system surfaces this.

5. **WAL's MUNI channel** went from 2 → 4 — this is the biggest single-channel rescoring. The $1.36B unrated HTM book isn't watch-level risk; it's an active shadow loan book with no market price discovery, confirmed via management disclosure. Warrants 🔴 active.
