# L781 — Key Ratios #2/#4 encoded; first readings under the adopted letter (DLIC FY2025, AAIA FY2025); L784 holder cell; inbox drain

**Written:** 2026-10-29 ~00:30 ET by SHADE (PROME spawn prome-92, Claude Code, Opus 5.5). **DOCKET L781** (due 2026-10-28) + **L784** (SHADE cell). Authority: WQ-473 A and WQ-474 A (Will 2026-10-21 22:46 ET). $0; no trade; no threshold, score or prior grade changed.

## 1. Charter edits (Will-ruled letter, transcribed, not improved)

| Charter line(s) after edit | Was | Now |
|---|---|---|
| `CLAUDE.md` L34–L48 (Key Ratio #2) | L34 "Illiquidity Ratio = (Mortgages + Schedule BA + illiquid ABS) / Admitted assets (>30% = red flag)" | Adopted GA formula + ruling stamp + verbatim core: CONFIRMED-ILLIQUID rule, T/R/E "when" cells, L1 bullet, three published numbers, grading rule (L726 lines 13, 30, 34–36, 39, 67–70, 72–76) |
| `CLAUDE.md` L50–L54 (Key Ratio #4) | L36 "TSR Ratio (Gober's metric) = Higher-risk off-balance-sheet assets / Reported statutory surplus" | L727 line 62 verbatim (TSR UNAVAILABLE + two named diagnostics, never summed, no band) + "no R + T sum" ruling stamp + verbatim surplus, SHADE-R v1 and SHADE-T v1 definitions (L727 lines 30, 44, 56) |
| new `instruments/KEY_RATIOS_2_4_ADOPTED_LETTER.md` | — | Governing text: L726 lines 9–89 (§1–§5) and L727 lines 26–62 byte-for-byte, with a runnable `diff` check (VERBATIM-OK at write). L727 line 64 (R + T option) omitted because WQ-474 A rejected it. |

⚠️ **Scope note for PROME:** PROME's packet said "byte-faithful to L726 §1–§4"; the record's own ruling request 1 asked adoption of **§1–§5** (§5 = the four no-double-counting rules, which the numerator needs to be computable). The letter file carries §1–§5. If PROME reads WQ-473 A as §1–§4 only, §5 is the one section to strike. Nothing else in the charter moved (no authority, route or threshold). Charter 27,230 B (`measure.py`), under the 32,550 B budget.

## 2. DLIC FY2025 under the adopted Key Ratio #2 — **NOT RED (CEILING 28.68% ≤ 30%)**

Single filing: DLIC FY2025 original annual statement (issuer file `2025_DLIC_Annual_Statement_Final.pdf`, SHA256 `cc9acf23…a9d`, 484 pages; machine-local store). All five inputs from that one file at dollar precision; valuation date 2025-12-31. ⚠️ The jurat page is not in the issuer-posted body (cannot be cited); "amended" SEARCH-NOT-FOUND in the front pages; the June 26, 2026 audited statement reproduces the same four amounts to the thousand.

| Term | Source line | USD |
|---|---|---:|
| Mortgages | Page 2 L3.1 + L3.2, col 3 | 2,874,147,323 |
| Schedule BA | Page 2 L8, col 3 | 1,601,744,585 |
| All ABS (D-1-2 line 1909999999 BACV) | Sch D-1-2 PDF pp. 278–313 | 10,441,030,493 |
| GA net admitted | Page 2 L26, col 3 | 45,903,192,677 |

**Holding-level classification** (1,591 D-1-2 holdings parsed; every one of 18 subtotal rows reconciles holding sum = filer subtotal; grand total = 10,441,030,493 ✓). Table: `research/L781_scripts/DLIC_FY2025_D12_CLASSIFIED.tsv`.

| Bucket | Rule applied | Holdings | BACV USD |
|---|---|---:|---:|
| **C** confirmed-illiquid | Restricted Asset Code `R`: **none** (codes found: `CF` 368 holdings $1,781,344,273; `C` 60 holdings $307,481,118; none `R`, `M` or `O` — matches the 10/21 token tally). T(b)/R/E documents: none obtained. | 0 | **0** |
| **L** evidenced-liquid | **L1** agency lines 1019999999 $590,337,648 + 1029999999 $128,214,642 + 1039999999 $796,594,492 + 1049999999 $234,711,346. L2 (30-day executed trade): no data, unavailable. | 353 | **1,749,858,128** |
| **P** private-ABS proxy | SVO symbol PL $1,689,936,500 / Z $861,694,625 / PLGI $66,021,000 (affiliated Woodmere) / non-financial full-analysis lines and not-self-liquidating lines (incl. FE) $517,484,058. Private Security Code and Level 3 not available per holding. | 284 | **3,135,136,183** |
| **U** unclassified | Everything else (FE-designated $4,763,660,369; no symbol $732,655,091; other $59,720,722) | 954 | **5,556,036,182** |

| Published number | Value |
|---|---:|
| **FLOOR** (M + BA + C) / GA | **9.7507%** |
| **PROXY-INCLUSIVE** (label, never a grade) | 16.5806% |
| **CEILING** (M + BA + all ABS − L) / GA | **28.6844%** |
| **Grade under the adopted rule** | **NOT RED** (CEILING ≤ 30%) |
| Headroom: CEILING to 30% | $603,893,530 |
| Confirmed-illiquid ABS needed to breach (unchanged) | $9,295,065,895 (89.02% of the ABS book) |
| ENCUMBRANCE companion (not illiquidity) | `CF` $1,781,344,273 · `C` $307,481,118 |

⚠️ **What carries the grade:** the CEILING clears 30% **only because L1 (agency category, INFERRED, not a per-CUSIP test) is accepted** — $1,749.9M against a $1,146.0M need. With L1 struck, the reading would be INDETERMINATE 9.75%–32.50%. Margin is $604M (1.32pp of GA). This is the **first** reading under the adopted letter (the 10/21 9.75%–32.50% was an illustration, never a grade) — not a retrospective regrade. The E-test (D Part 4 sales below carrying value) was not run: it can only raise FLOOR (C), never the CEILING, so it cannot change this grade.

## 3. SHADE-R v1 / SHADE-T v1 — named diagnostics, no band, never summed, never TSR

| Component (letter line) | DLIC FY2025 USD | % surplus | AAIA FY2025 USD | % surplus |
|---|---:|---:|---:|---:|
| R1 ABS 1909999999 | 10,441,030,493 | 272.0% | 73,463,901,478 | 1,782.3% |
| — memo: affiliated ABS 1899999999 (inside R1) | 66,021,000 | 1.7% | 28,986,680,362 | 703.3% |
| — memo: non-agency (R1 − agency lines) | 8,691,172,365 | 226.4% | ~72,687,398,244 ⚠️ | ~1,763.5% |
| R2 affiliated ICO 0499999999 | 13,591,000 | 0.4% | 9,904,385,159 | 240.3% |
| R3 affiliated preferred 4409999999 + common 5979999999 | 246,200,970 + 35,840,285 | 7.3% | 74,999,980 + 508,708,831 | 14.2% |
| R4 Schedule BA Part 1 total BACV | 1,619,337,469 (unaff 1,229,901,951 / aff 389,435,518) | 42.2% | 17,461,797,562 (unaff 6,247,599,030 / aff 11,214,198,532) | 423.6% |
| **SHADE-R v1** | **12,356,000,217** | **321.9%** | **101,413,793,010** | **2,460.4%** |
| T1 reserve credit to affiliates, Sch S Pt3 Sec1 col 9 (0799999 + 1899999 + 2999999 + 4099999) | 62,230,134 (0799999 only) | 1.62% | 966,132,734 + 1,192,259,638 + 0 + 65,263,421,108 = 67,421,813,480 | 1,635.7% |
| T2 modco reserve with affiliates, col 14 (same rows) | 0 | 0% | 0 + 110,346,917,726 + 0 + 5,745,785,654 = 116,092,703,380 | 2,816.6% |
| **SHADE-T v1** | **62,230,134** | **1.62%** | **183,514,516,860** | **4,452.3%** |
| Surplus, Page 3 L38 col 1 | 3,838,481,434 | | 4,121,783,748 | |

**Ties checked:** AAIA Page 2 bonds 158,852,395,199 = D-1-1 + D-1-2 BACV ✓; preferred 1,450,140,021 ✓; common 1,594,391,561 ✓; BA 17,461,797,563 vs Part 1 17,461,797,562 ($1 rounding). AAIA Sch S col sums reconcile to line 4599999 (col 9 74,345,535,505; col 14 116,092,703,380; col 15 66,695,003,878) ✓. DLIC col 9 1199999 = 388,305,493 + 62,230,134 ✓. AAIA source: `AAIA_4Q_2025_Statement_-_FINAL.pdf` (ir.athene.com statutory page), 9,612 pages, 221,368,204 B, SHA256 `6580cd4c9b539f8f7ee17d4c176b2c5b041b5fe8923cf3baf6f5b7ddca1e562a` = the 6/15 manifest file; pages rotated 270°, read by character-coordinate reconstruction (`research/L781_scripts/rot.py`).

⚠️ **Caveats that travel with these numbers:**
1. **Letter-vs-filing line numbers:** the letter names Schedule BA lines 7899999/7999999/8099999 (2026 instructions); both FY2025 filings number the same rows 6899999/6999999/7099999 ("Total - unaffiliated / affiliated / Totals"). Mapped by label, not by number. All other letter line numbers matched the FY2025 filings.
2. **AAIA's affiliate cessions are almost all to Athene Annuity Re Ltd (Bermuda), largely on a funds-withheld basis:** col 15 funds withheld under coinsurance with affiliates $66,695,003,878 against T1 $67,421,813,480 — i.e., most of the assets backing the ceded reserves stay on AAIA's own balance sheet. T measures reliance on affiliate reinsurance, not assets that left. Modco (T2) likewise keeps assets with the cedent by construction.
3. **AAIA agency memo is approximate (±$19M):** the 1019999999 subtotal row has a blank cell and the BACV column is ambiguous on the rotated page ($21,601,484 taken). Immaterial to R1.
4. **Key Ratio #1 read-across, not re-scored:** T1/surplus is #1's numerator over #1's denominator. AAIA reads **1,636%**, far above #1's existing ">100% = critical" marker; DLIC reads 1.62% (unchanged from the 10/1 reading). The charter has carried Athene's $70.79B affiliate reserve credit since June, so vector scores already embed this structure; **no score moved** (composite 20/30). Flagged to PROME as a visible fact, not a new fire.
5. Separate-account cessions (AAIA SA unauthorized non-U.S. affiliates modco $52,198,633,311) excluded — the letter is GA only.

## 4. Clear Spring (WQ-422)

No Clear Spring statutory documents are in SHADE's inbox (checked 2026-10-29); the classification was not run on Clear Spring. Not chased (Will's hands).

## 5. L784 — insurer / bond-holder cell for CORAL

Delivered: `AGENTS/CORAL/inbox/2026-10-29_from-SHADE_L784-insurer-bond-holder-cell.md`. FHCF $0 and Citizens $0 at both insurers (name SEARCH-NOT-FOUND in D-1-1); Florida municipal-line holdings DLIC $9,199,973 / AAIA $22,905,000; AAIA Florida issuers in other lines: Space Florida $97,311,580, Orlando Health $24,727,172. 12/31/2025, BACV, two insurers only, holder leg for the market UNKNOWN.

## 6. Inbox evidence recorded (dispositions in `board_log.tsv`)

- **Cyber (DEWEY base rates, CYPHER P1 KEV fire, WALTER -025):** five past waves, insured loss $0.09B to >$3B per event; PCS designations above $250M industry loss; Guy Carpenter 1-in-200 $15.6–33.4B (DEWEY 10/22). KEV listed CVE-2026-109618/-109619 on 10/26 with no named victim. SHADE consequence = NONE in the insurer-wrapper channel (rows 6/7 NOT-FIRED, no insurer or rating statement). n=5 base rate; pre-disclosure exploitation means "none confirmed" is weak.
- **Data-center ABS/CMBS (DEWEY v2):** insurer exposure documented for Athene only (~$0.5B DC ABS, ~$2.4B all DC assets, 12/31/25); others UNKNOWN, not small. SHADE now holds AAIA and DLIC FY2025 Schedule D in parsed form, so a CUSIP match is feasible — not run (would be a new task; needs a DC CUSIP list).
- **American Equity → Brookfield loans (WALTER -028/-033):** VERIFIED at the Iowa exam by SHADE — $415.3M (6/28/2024) + $165.0M (12/30/2024) = $580.3M originated; current balances unknown. REFERENCE §5.
- **Insurer CRE lending (WALTER -066):** MSCI-attributed H1-2026 insurer origination LTV 62.7% (+2.5pp) vs 65.9% all lenders (newsletter, MSCI dataset not reached; mix effect can raise the average without more risk). "30% of insurer RE lending to data centers" primary-unverified. Recorded, causality not adopted; CREED owns the series.
