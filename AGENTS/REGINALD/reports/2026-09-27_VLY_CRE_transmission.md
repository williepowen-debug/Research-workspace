# Valley National (VLY): broader CRE stress, a bank-specific problem, or neither? (REGINALD, 2026-09-27)

**Asked by:** Will via PROME, WQ-311 (approved 19:04 ET). **Bounds:** VLY's own filings plus existing desk work. No score, threshold, tool or trade change. CREED challenges the property comparisons after part (1).
**Primary sources (all fetched from EDGAR 2026-09-27):**
- **[ER]** Q2-26 earnings release, 8-K EX-99.1, acc 0000714310-26-000036
- **[DK]** Q2-26 earnings presentation, same accession, slide images read directly (slides 4, 25, 29–32)
- **[10Q]** Q2-26 10-Q, acc 0000714310-26-000041
- **[CR]** FFIEC Call Reports, bank-level, via `workbook/CRE_RCN_COHORT.tsv` (pulled 9/26)

⚠️ **Two bases.** The deck's "CRE $27.9B" = non-owner-occupied + owner-occupied + multifamily, **excluding construction** ($2.5B). The Call Report is bank-level. Figures are labelled by source; do not mix them.

---

## (1) ACTUAL CRE COMPOSITION, as of 6/30/2026 — OBSERVED

### By property type [DK s29]
| Type | $B | Share | Wtd LTV | Wtd DSCR |
|---|---:|---:|---:|---:|
| Apartment & residential (non-co-op multifamily) | 7.1 | 25% | 64% | 1.34× |
| Retail | 4.2 | 15% | 61% | 1.67× |
| Healthcare | 4.1 | 15% | 69% | 1.69× |
| Specialty & other | 3.1 | 11% | 54% | 1.79× |
| **Office** | **3.0** | **11%** | 63% | 1.83× |
| Industrial | 2.9 | 10% | 60% | 2.17× |
| **Co-ops** | **1.8** | 6% | **12%** | 1.50× |
| Mixed use | 1.6 | 6% | 63% | 1.31× |
| **Total (ex-construction)** | **27.9** | | **59%** | **1.67×** |
| Construction (separate) | 2.5 | — | — | — [ER] |

*(The deck's pie shows "Apartment & Residential 32%", which includes co-ops; the table splits them.)*

### By geography [DK s29]
| Region | $B | Share | Wtd LTV | Wtd DSCR |
|---|---:|---:|---:|---:|
| Florida / Alabama | 7.8 | 28% | 61% | 1.81× |
| Other (national) | 5.9 | 21% | 66% | 1.65× |
| New Jersey | 5.2 | 19% | 62% | 1.63× |
| Other NYC boroughs | 4.3 | 16% | 56% | 1.45× |
| Manhattan (multifamily 6% + other 4%) | 2.6 | 10% | 41% (60% ex co-ops) | 1.51× |
| New York ex-NYC | 2.0 | 7% | 56% | 1.99× |
| **NYC total** | **6.9** | **25%** | | |

### NYC rent-regulated multifamily: how VLY defines it, and how big it is
- **VLY's own definition** [10Q, loan table note 1]: loans "collateralized by properties that are **greater than 50 percent rent regulated**".
  - **$559M at 6/30/26**, down from $583M [3/26] and $601M [12/25].
  - That is **2.0% of CRE ex-construction** and **1.1% of total loans** ($52.5B).
- **Cross-check against the deck** [DK s30]: NYC non-co-op multifamily is **$3.1B**. By share of rent-regulated units:

| Share of units rent-regulated | Share of the $3.1B | ≈ $M |
|---|---:|---:|
| 0% | 45% | 1,395 |
| 1–20% | 7% | 217 |
| **21–50%** | **30%** | **930** |
| 51–99% | 7% | 217 |
| 100% | 11% | 341 |

  - The last two rows sum to ~$558M. **That reconciles to the 10-Q's $559M.** (DERIVED; slice percentages are read off the chart.)
- ⚠️ **The ">50%" definition leaves out a ~$0.93B band of 21–50% rent-regulated buildings.** Those carry partial rent-freeze exposure. **Broadest reading: ~$1.5B (48% of NYC multifamily) has ≥21% regulated units.** That is still **~1/6 of FLG's** rent-regulated book ($8.9B >50%; `AGENTS/FLG/STATUS.md:71`).
- **NYC non-co-op multifamily metrics** [DK s30]: Manhattan $0.8B, LTV 62%, DSCR **1.24×**. NY ex-Manhattan $2.4B, LTV 66%, DSCR **1.24×**. These are the **weakest coverage ratios in VLY's multifamily book** (Florida/Alabama 1.45×, NJ 1.41×).

### Office [DK s31]
- **$3.0B, 11% of CRE ex-construction**; ~26% owner-occupied; average loan $3.5M; LTV 63%; DSCR 1.83×.
- By region: Florida/Alabama $1.1B · NJ $0.8B · NY ex-Manhattan $0.5B · **Manhattan $0.2B (LTV 74%)** · other $0.4B (LTV 73%).

### Maturities [DK s32]
- **Q2-26 maturities, $1,457M:** retained $1,082M · paid off and left $341M · **modified and other $33M**. Footnote: one office loan of $25.8M moved to nonaccrual; one multifamily loan of $6.8M modified.
- **Next 6 quarters:** 3Q26 $1,408M · 4Q26 $881M · 1Q27 $937M · 2Q27 $576M · 3Q27 $518M · 4Q27 $870M. Weighted DSCR 1.41–1.99×.
- **The wall is 2028–29** ($3.7B per year).

### What drives the SR 07-1 concentration of ~320%
- **Mine:** 319.5% (Call Report, bank-level). **VLY's own ratio:** "CRE / TRBC" **317%** at 6/30/26 [DK s4], defined per regulatory guidance, including CRE held for sale and excluding owner-occupied [10Q glossary].
- **VLY's own trend** [DK s4]: **474% [12/23] → 362% [12/24] → 333% [12/25] → 317% [6/26]**. **Down 157pp in 2.5 years**, from capital growth and non-owner-occupied runoff (NOO −$357M in Q2 alone [10Q]).
- **Components** (Call Report, 6/30): multifamily **$9.0B** (includes the $1.8B of co-ops) + non-owner-occupied **$11.1B** + construction **$2.5B**.
- ⚠️ **About 25pp of the ~320% is co-op lending at a 12% LTV** (DERIVED: $1.8B ÷ implied capital ≈ $7.1B = 317% ⇒ $22.7B / 3.17). **Co-ops are regulated-as-CRE but low-loss** (a blanket mortgage on a cooperative building). **Ex-co-ops the ratio is ~292%, below the 300% line.**
- ⇒ **The concentration is a level inherited from 2023 and falling fast. It is not a sign of new risk-taking.**

---

*Parts (2)–(4) follow below. Part (1) was committed first so that CREED could start.*
