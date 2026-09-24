# Cohort AOCI Exposure — 14 banks, Q2-2026 Call Reports + Q3 rate scenario

**Date:** 2026-09-24 (Thu). **Author:** REGINALD, Will-directed.
**Source:** FFIEC CDR Call Reports (SDF, bank-level, not holdco), 6/30/26 with 3/31/26 and 6/30/25 comparatives, pulled 9/24. Treasury yields from FRED DGS2/5/10.
**Codes:** B530 AOCI · 1772/1773 AFS amortized cost/fair value · 1754/1771 HTM · P859 CET1 · A223 RWA · P838 AOCI opt-out · P844/P846/P847/P848 RC-R 9a/9c/9d/9e AOCI adjustments.
**Check:** computed CET1 ÷ RWA equals the filed P793 ratio for **14 of 14** banks.
⚠️ **A first pass mis-mapped P865/P866** (Additional Tier 1 / Tier 2 capital) as AOCI adjustments and produced nonsense pro-formas (OZK +178bp). It was caught against the SDF's own line descriptions and recomputed. Nothing from the bad pass is used here.

## 1. Where the cohort stands at 6/30/26 ($M)

**All 14 banks OPT OUT of AOCI** (P838 = 1), so **reported CET1 is unaffected by any of this today.** AOCI bites through two channels: (a) tangible book value and equity valuation, now; (b) the pending proposal to include AOCI in CET1 for Cat III/IV (≥$100B), later.

| Bank | Assets $B | Secs/assets | AOCI | AFS unreal. (pre-tax) | HTM unreal. (pre-tax, NOT in AOCI) | AOCI / CET1 | CET1 reported | CET1 incl. AOCI¹ | Δ bp | + after-tax HTM | AOCI Δ QoQ | AOCI Δ YoY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **ZION** | 89.0 | 19.9% | −1,867 | −1,157 | −37 | **−22.3%** | 11.83% | **9.26%** | **−257** | 9.22% | +69 | +297 |
| CFG | 232.5 | 19.4% | −2,242 | −1,461 | −854 | −10.7% | 11.92% | 10.80% | −112 | 10.43% | −173 | +378 |
| HBAN | 283.1 | 17.5% | −2,195 | −2,351 | −1,707 | −8.7% | 11.82% | 10.87% | −95 | 10.27% | −154 | +31 |
| **WAL** | **98.6** | 20.8% | −448 | −667 | −179 | −5.9% | 11.58% | 10.90% | −68 | 10.70% | +5 | +32 |
| SSB | 68.8 | 12.4% | −310 | −418 | −315 | −4.7% | 12.17% | 11.60% | −57 | 11.17% | +16 | +62 |
| OZK | 41.7 | 10.2% | −27 | −35 | 0 | −0.5% | 11.80% | 11.74% | −6 | 11.74% | +21 | +41 |
| MTB | 218.8 | 17.0% | −86 | −125 | **−791** | −0.4% | 11.81% | 11.79% | −2 | 11.44% | −158 | −305 |
| VLY | 66.2 | 12.2% | −99 | −125 | −390 | −1.5% | 12.28% | 12.09% | −19 | 11.54% | −2 | +20 |
| BKU | 34.9 | **26.7%** | −217 | −282 | 0 | −6.5% | 13.01% | 12.19% | −82 | 12.19% | −14 | +14 |
| FLG | 87.7 | 18.9% | −547 | −737 | 0 | −6.9% | 13.16% | 12.25% | −90 | 12.25% | −19 | −5 |
| AMTB | 10.3 | 24.8% | −25 | −33 | 0 | −2.5% | 12.91% | 12.59% | −32 | 12.59% | −3 | +1 |
| SBCF | 21.3 | **26.9%** | −84 | −112 | −98 | −4.3% | 13.55% | 12.97% | −59 | 12.46% | −5 | +34 |
| CUBI | 26.5 | 12.2% | −58 | −71 | −56 | −2.5% | 13.55% | 13.26% | −29 | 13.02% | −4 | +13 |
| EGBN | 9.6 | 17.5% | −93 | −80 | −83 | −7.7% | 14.95% | 13.87% | −108 | 13.10% | −4 | +15 |

¹ "CET1 incl. AOCI" = CET1 + RC-R 9a (AFS) + 9d (pension) + 9e (HTM amounts in AOCI). **Cash-flow hedges (9c) excluded**, as in the US proposals. "+ after-tax HTM" adds HTM unrealized loss × 0.75 (25% tax, an ASSUMPTION). That is an economic view, not a proposed rule.

### What stands out
1. **ZION is the cohort outlier: AOCI is 22% of CET1, and including it takes CET1 from 11.83% to 9.26%.** Most of it (−$1,117M, line 9e) is HTM securities transferred from AFS with the loss frozen in AOCI. That loss **amortizes back** over time: ZION's AOCI improved $297M YoY. So ZION's burden is large but shrinking, and it is mechanically insensitive to new rate moves (HTM does not re-mark).
2. **WAL sits at $98.6B of bank-level assets, $1.4B under the $100B Category IV line**, with the largest AFS book relative to capital in the mid-size group ($18.8B AFS vs $7.7B CET1). Crossing $100B would bring Cat IV requirements and the proposed AOCI inclusion (phased).
   - ⚠️ The regulatory test is **holdco four-quarter-average consolidated assets**, not this bank-level spot figure. This is a **proximity flag, not a determination.**
   - WAL-desk scope; not restated beyond this.
3. **Covered-size banks (≥$100B): HBAN, CFG, MTB.** Including AOCI costs them 2-112bp. All stay above 10.4% even with after-tax HTM added. **Not binding** against a ~7% minimum plus buffer. Their HTM losses (HBAN −$1.7B, CFG −$0.85B, MTB −$0.79B) are the larger, unrecognized piece.
4. **The FL small names carry the most securities per dollar of assets** (BKU 26.7%, SBCF 26.9%, AMTB 24.8%), so they are the most rate-sensitive in bp of capital. They also start from the highest CET1.
5. **Q2 already moved the big three the wrong way** (CFG −$173M, MTB −$158M, HBAN −$154M QoQ), while the 5Y rose only 27bp.

## 2. Q3 scenario: the rate move since 6/30 (NOT a forecast)

Rates since the 6/30 snapshot: **5Y 4.19% → 4.83% (+64bp) and 10Y 4.44% → 4.96% (+52bp) at 9/22 [FRED]**, before a further ~+15bp on 9/23 (^TNX close 5.11%). **Q3 is already more than twice Q2's move, and marks close 9/30.**

**Method (ASSUMPTION, stated plainly):** ΔAOCI ≈ −D × AFS fair value × 64bp × (1 − 25% tax), with D = 3 and D = 5 years as a typical AFS effective-duration band. ⚠️ **I tried to calibrate D per bank from the Q2 moves and it failed.** Implied durations came out between −2.5 and +2.0, which is impossible for an unhedged bond book, because hedges (pay-fixed swaps), pull-to-par and portfolio changes dominate a 27bp quarter. **So D is not measured per bank, and banks with fair-value hedges (not identified here) will show LESS than this.**

| Bank | CET1 incl. AOCI now | ΔAOCI D=3 ($M) | ΔAOCI D=5 ($M) | CET1 incl. AOCI, Q3 D=5 | Δ bp (D=5) | ΔAOCI as % CET1 (D=5) |
|---|---:|---:|---:|---:|---:|---:|
| ZION | 9.26% | −133 | −222 | 8.95% | −31 | −2.7% |
| CFG | 10.80% | −539 | −899 | 10.29% | −51 | −4.3% |
| HBAN | 10.87% | −507 | −845 | 10.47% | −40 | −3.4% |
| WAL | 10.90% | −271 | −452 | 10.22% | −68 | −5.9% |
| SSB | 11.60% | −95 | −158 | 11.31% | −29 | −2.4% |
| OZK | 11.74% | −61 | −102 | 11.52% | −23 | −1.9% |
| MTB | 11.79% | −365 | −609 | 11.43% | −36 | −3.1% |
| VLY | 12.09% | −62 | −103 | 11.90% | −19 | −1.6% |
| BKU | 12.19% | −134 | −223 | 11.32% | **−88** | **−6.7%** |
| FLG | 12.25% | −238 | −397 | 11.59% | −66 | −5.0% |
| AMTB | 12.59% | −37 | −61 | 11.80% | −79 | −6.1% |
| SBCF | 12.97% | −75 | −124 | 12.11% | −85 | −6.3% |
| CUBI | 13.26% | −37 | −62 | 12.90% | −36 | −2.6% |
| EGBN | 13.87% | −13 | −22 | 13.60% | −27 | −1.8% |

**Cohort total at D=5: roughly −$4.3B of after-tax AOCI in Q3** if rates hold at 9/22 levels through 9/30 (−$2.6B at D=3). Largest dollars: CFG, HBAN, MTB, WAL. Largest hit relative to capital: BKU, SBCF, AMTB, WAL, FLG.

## 3. So what

- **No capital ratio breaks.** Reported CET1 does not move for any of the 14 (all opt out). Even the scenario-plus-inclusion view keeps every bank ≥ ~9%.
- **What does move is tangible book value.** A 2-7% hit to CET1-equivalent equity in one quarter shows up in Q3 tangible book value per share. That is the price-to-tangible-book denominator the equity market trades on. **This is the mechanism under the 9/15-9/23 KRE drift**, and it becomes a filed number at the ~Oct 20-28 prints.
- **Watch items for Q3 grading:** (a) WAL's asset trajectory vs $100B. ⚠️ **CORRECTED 9/24 (WAL desk, KB-WAL-196/198, verified at their KB): management EXPECTS to cross $100B ORGANICALLY by end-Q1 2027** (9/16 Barclays transcript; Q3 assets guided ~$98B). The four-quarter average clears ~Q3-2027 on WAL's illustrative path. My packet's inference that WAL was "managing below the line" was WRONG in direction: I drew it from a secondary summary that omitted this line. **Read the crossing as PLANNED, so AOCI inclusion becomes a when, not an if (phase-in permitting).** (b) ZION's AOCI should keep improving through amortization even with rates up (a falsifier if it doesn't); (c) any bank selling AFS securities at a loss to reposition, which realizes AOCI into earnings; (d) HTM losses at HBAN/CFG/MTB, where the economic hit is larger than the reported one.
- ⛔ BOND owns the curve. The AOCI-inclusion rule timing lives in `CALENDAR.md` (H2-2026 / Q1-2027 finalization, 5-yr phase-in). WAL's thesis is `../WAL/`-owned.

*Machine-readable: `workbook/AOCI_COHORT_2026Q2.tsv`. Raw SDFs are cached in the session scratchpad only, and are re-pullable with `scripts/mi3_cohort_screen.py`'s `facsimile()`.*
