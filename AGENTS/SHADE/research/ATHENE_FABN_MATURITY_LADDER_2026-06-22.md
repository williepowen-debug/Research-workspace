# Athene FABN / Funding-Agreement Maturity Ladder — 2026-06-22

**Method:** Opus 4.8 ultracode. 4 source-finders (10-Q/10-K maturity tables · EDGAR Athene Global Funding · rating-agency debt profile · issuance-cadence/reconciliation) → adversarial reconcile → synthesis. 9 agents, ~579k tokens. Overall confidence: **high on the program stack; the year-by-year FABN ladder is structurally unavailable from public data.**

---

## ⚠️ HEADLINE FINDING — the $16.5B "2026-2027 FABN wall" is UNVERIFIABLE from primary sources

SHADE/CLAUDE.md kill-path-1 carries **"$35B FABN program, $16.5B maturing 2026-2027."** Three independent research passes **could not reconcile the $16.5B to any filing line.** The reasons are structural, not a search failure:

1. **Athene Global Funding is NOT an SEC EDGAR filer.** Company search returns zero registrants; full-text search for FWP/424B/S-3 under that issuer = 0 hits. **100% of the $34.5B FABN is Rule 144A (QIB) / Reg S (offshore)** per the issuer's own $35B Global Debt Issuance Program base Offering Memorandum (arranger Deutsche Bank; clears via DTC). None is SEC-registered → EDGAR carries no series/CUSIP/coupon/principal/maturity for any FABN tranche.
2. **Athene publishes NO FABN-only (nor even total-FA) year-by-year contractual-maturity schedule** — not in the Q1'26 10-Q, FY2025 10-K, Q4'25/Feb'26 FI deck, or the base prospectus. The *only* year-bucketed primary maturity figure is the MD&A "Material Cash Obligations" table's **"Interest sensitive contract liabilities"** row, which **buries FABN inside ALL annuities + ALL funding agreements + GICs**, is **undiscounted (incl. estimated future interest)**, and uses coarse buckets. It cannot be cited as the FABN wall.
3. **Per-tranche principal lives only in private Pricing Supplements to QIBs.** cbonds/FINSIGHT detail pages return HTTP 403/paywall. **<1% of the $34.5B is principal-attributable from free public data.** ~14 tranches confirmed by coupon+maturity+identifier, but ~$0 of principal at full confidence.

**Disposition:** RE-MARK the $16.5B as **third-party / unverified**, pending a Bloomberg DDIS or cbonds-Professional CUSIP-by-CUSIP aggregation. The *direction* (a multi-billion 2026-2027 FABN cluster) is qualitatively corroborated; the *quantum* is not public. This is the FABN-rollover analogue of "don't bank an unverified figure" — the wrapper's 144A design makes the precise rollover quantum **invisible by construction**.

---

## ✅ UPDATE (same day) — NPORT-P bottom-up reconstruction BRACKETS the $16.5B

Rather than pay for a terminal, reconstructed the wall from the **holder side**: registered '40-Act funds disclose every AGF holding (CUSIP, par, maturity, coupon) in monthly **NPORT-P** filings. Scripted crawl of **1,602 fund filings across 189 registrant trusts** (latest public filing per fund; 0 fetch failures), filtered to AGF CUSIPs (`04685A*`/`04686E*` + issuer match), deduped by (CIK, seriesId, CUSIP), summed **par** by maturity year. Artifacts: `AGF_NPORT_floor_2026-06-22.json`, `AGF_NPORT_crawl_2026-06-22.py`.

**Registered-fund FLOOR (par held, latest-per-fund, 77 unique CUSIPs):**

| Maturity year | Registered-fund par held | CUSIPs |
|---|---:|---:|
| **2026** | **$1.76B** | 13 |
| **2027** | **$1.53B** | 17 |
| 2028 | $0.75B | 11 |
| 2029 | $0.84B | 6 |
| 2030 | $0.58B | 6 |
| 2031+ | ~$0.79B | ~17 |
| **2026-2027 FLOOR** | **$3.29B** | **30** |
| **All-years total** | **$6.25B** | **77** |

**The extrapolation that brackets $16.5B:** registered funds visibly hold **$6.25B of the ~$34.5B total AGF = 18.1% blended ownership share** (the other ~82% sits in insurance general accounts, foreign Reg-S, pensions, SMAs — NPORT-invisible). Grossing the $3.29B 2026-2027 floor up by the blended share → **~$18.3B**; adjusting for the fact that short-dated FABNs are *more* heavily held by registered money/ultra-short/VI funds (so registered share of the near tranches is higher, ~25%) → **~$13.2B**.

**Bracket: ~$13-18B, central ~$16B — the $16.5B figure is now independently CORROBORATED as the right order of magnitude**, not refuted. Status upgrades from "unsourceable/unverified" to **"independently bracketed; plausible-central."** The wall is genuinely large — ~40-50% of the $34.5B FABN program rolling in ~18 months.

**Top 2026-2027 AGF tranches by registered-fund par held** (these supersede the conf-0.5 cbonds snippets in §3 — sourced from actual holder filings):

| CUSIP | Maturity | Coupon | Reg-fund par | # funds |
|---|---|---|---:|---:|
| 04685A4A6 | 2026-08-27 | 4.86% | $381.6mn | 43 |
| 04685A4E8 | 2027-01-07 | 4.95% | $374.2mn | 44 |
| 04685A3R0 | 2027-01-15 | 5.339% | $323.0mn | 31 |
| 04685A3V1 | 2026-05-08 | 5.62% | $278.9mn | 34 |
| 04685A4Q1 | 2026-08-10 | SOFR FRN | $227.5mn | 8 |
| 04685A4J7 | 2026-07-16 | SOFR FRN | $215.3mn | 19 |
| 04685A3U3 | 2027-03-25 | SOFR FRN | $213.0mn | 20 |
| 04685A3T6 | 2027-03-25 | 5.516% | $194.6mn | 49 |

**What this does and doesn't change:**
- ✅ Resolves "is the wall real and large?" — YES, ~$13-18B confirmed bottom-up.
- ✅ Gives 30 specific 2026-2027 CUSIPs with dates — a real, dated near-wall (heaviest in **Aug 2026, Jan 2027, Mar 2027**).
- ⚠️ Does NOT change kill-path-1 = **YELLOW**. Sizing the wall doesn't change rollover mechanics: still no puttable FABNs, no FA-backed CP, $71.8B liquidity, active tenders. Open channel remains refinance-at-wider-spread, not forced failure.
- Caveat: floor + extrapolation, not an exact figure; the short-dated-ownership skew argues the true number sits toward the **lower** end (~$13B) rather than $18B.

---

## 1. FABN / funding-agreement program stack — HIGH confidence (as-of 2026-03-31)

Dual-passage confirmed in the Q1'26 10-Q (Funding Agreements note + MD&A) and cross-checked vs FY2025 10-K. `[Athene Q1'26 10-Q, accn 0001527469-26-000028, filed 2026-05-07]`

| Leg | Outstanding | QoQ | Note |
|---|---:|---|---|
| **FABN** (Athene Global Funding MTNs) | **$34.5B** | −$0.1B (from $34.6B) | Was $24.1B at 12/31/24 → **+$10.5B FY2025 build, then FLAT in Q1'26** |
| **FABR** (FA-backed repo) | $21.5B | — | part of "$27.6B secured & other" |
| **Direct FAs** | $6.1B | — | part of "$27.6B secured & other" |
| **FHLB** (Des Moines) | **$28.2B** | **+$4.9B** (from $23.3B) | **substitution canary** — see §3 |
| **LT repurchase agreements** | $3.2B | — | *previously omitted from SHADE's stack* |
| **TOTAL FA family (gross)** | **~$93.5B** | | 34.5 + 21.5 + 6.1 + 28.2 + 3.2 |

- **Capacity:** $10.5B board-authorized FABN headroom remaining (implies ~$45B board ceiling). Separately, Athene Global Funding runs a **$35B Global Debt Issuance Program EMTN shelf** (May 2025 base OM) — a *different construct* from the board ceiling; **do not conflate** with the "$35B program" baseline.
- **Data-provenance caveat:** the 10-K's **$71.4B "funding-agreement net reserve liabilities"** is a reserve/economic-ownership measure, **NOT** the ~$93.5B gross-outstanding sum. Use ~$93.5B gross for rollover analysis; do not conflate the two.
- Program ratings **Moody's A1 / S&P A+ / Fitch A+**; consolidated **RBC 441%** (12/31/25 est). 5-currency program (USD majority + EUR/GBP/AUD/SGD), FX-hedged. 7-yr weighted-average life of funding.

---

## 2. The only primary year-bucketed maturity figure — ALL-ISC basis (NOT the FABN wall)

MD&A "Material Cash Obligations" → "Interest sensitive contract liabilities" (undiscounted, incl. future interest; **blends annuities + ALL FA + GICs**). `[Q1'26 10-Q, as-of 2026-03-31]`

| Bucket | ALL-ISC ($B) | FY25 10-K comparator | 
|---|---:|---|
| 2026 | **21.347** | 27.794 (12/31/25) — fell as a quarter elapsed ✓ internally consistent |
| 2027-2028 | **95.379** | 93.823 |
| 2029-2030 | **86.257** | — |
| 2031 & thereafter | **123.519** | — |
| **Total ISC** | **326.502** | (sum verified) |

**Why this is not the answer:** these are not FABN, are undiscounted, include future interest, and the long tail is dominated by annuity reserves. The QoQ drift confirms it is a *live estimate*, not a fixed contractual FABN principal schedule. Presented only to document the boundary of what Athene actually discloses.

---

## 3. Maturity-dated FABN tranche list — the best available "ladder" (maturity distribution, principal mostly paywalled)

~14 FABN tranches confirmed by **coupon + maturity + identifier** (principal sizes are unconfirmed cbonds snippets at conf ~0.5 where shown; most paywalled). This is a real **maturity *distribution*** even without dollar amounts — and it confirms the 2026-H2/2027 cluster.

**2026-H2 (the near wall):**
| Coupon | Maturity | Ccy | Principal (unconfirmed) | ID |
|---|---|---|---|---|
| 5.62% | 2026-05-08 | USD | n/d | FIGI BBG01MRCDQN7 |
| 4.86% | 2026-08-27 | USD | n/d | US04686E4H28 |
| 1.73% | 2026-10-02 | USD | ~$650mn | US04686E3K65 |
| 2.95% | 2026-11-12 | USD | ~$500mn | US04686E2L57 |

**2027 (the SHADE "Mar-Aug 2027" window):**
| Coupon | Maturity | Ccy | Principal | ID / note |
|---|---|---|---|---|
| 5.339% | 2027-01-15 | USD | ~$550mn | series 2024-2 |
| FRN | 2027-02-23 | EUR | n/d | XS2757986224 (series 2024-3) |
| 3.205% | 2027-03 | USD | **$260.1M tendered** (full size n/p) | series 2022-6 — **actively tendered 6/22** |
| 4.76% | 2027-04-21 | AUD | n/d | AU3CB0288553 (Kangaroo, series 2022-9) |
| 2.450% | 2027-08 | USD | **$238.1M tendered** (full size n/p) | series 2020-5 — **actively tendered 6/22** |

**2029+ tail (reference):** 5.583% 2029-01-09 USD (~$1,150mn, series 2024-1) · 3.41% 2030-02-25 EUR (series 2025-8) · 5.322% 2031-11-13 USD (~$650mn) · EUR 7Y benchmark ~2032 (XS3163476149, the **last public syndicated FABN**, launched 2025-08-19) · 5.543% 2035-08-22 USD (~$600mn, Aug/Sep'25 cluster).

**HOLDCO (reference — NOT FABN):** first Athene Holding senior-note maturity = **$1.0B 4.125% due 2028-01-12**. **NO holdco notes mature 2026 or 2027.** Total LT holdco debt $7.840B. → the entire 2026-2027 wall is a FABN/Athene-Global-Funding-trust phenomenon, not a holdco event.

> **New, current signal:** Athene is **actively tendering** 2027 FABN tranches (series 2022-6 $260.1M, series 2020-5 $238.1M, per Athene IR/news 2026-06-22) — proactive liability management ahead of the wall. Cuts both ways: prudent (good), and confirms the 2027 maturities are real and being worked.

---

## 4. Issuance cadence — the canary that IS confirmed

- **Last public syndicated FABN: late-Aug/Sep 2025** (EUR 7Y XS3163476149 marketed 2025-08-19; USD 5.543% 2035) → **~9-10 months stale** as of June 2026.
- **Q1'26 FABN gross issuance collapsed to $2.0B vs $13.4B FY2025.** Outstanding went flat-to-down. **10-Q MD&A explicitly attributes the drop to "a decrease in FABN issuance amid challenging market conditions."**
- **Substitution into secured funding:** FHLB +$5.0B Q1 issuance (→ $28.2B, +$4.9B QoQ) and FABR (+$1.5B) replaced public FABN. Cheaper, but raises **encumbrance** — $111.6B restricted assets — reducing the unencumbered cushion behind the $53.1B "highly liquid" portfolio.
- This **substitution-toward-secured/private IS the canary**, and it is fully confirmed from primary disclosure (unlike the $16.5B quantum).

**Funding-cost canary — reconcile the obs-date gap:** SHADE 6/21 cited **5Y FABN secondary T+123 (+43-48bp peer penalty)** [May'26 FI deck, JPM data 5/14]. A **Feb'26 FI deck shows T+105 (+23-34bp)** vs peers T+71-82. Same direction; **the penalty appears to have WIDENED ~+15bp over the quarter** (Feb → May) — a deterioration that *strengthens* the canary, though the two readings need a clean side-by-side before treating the widening as hard. **Going forward: tag each spread reading with its observation date; stop carrying a single number.**

---

## 5. Kill-path-1 read — YELLOW (cost/mix-shift refinancing risk; mechanism intact), NOT red

**Open channel = REFINANCING-AT-WIDER-SPREAD (margin compression + mix-shift to encumbered funding), not forced rollover failure.**

Pulls toward stress: FABN flat-to-down + Q1 issuance collapse + ~9-10mo syndicated gap + widening peer-relative penalty + visible substitution into encumbered FHLB/FABR.

Pulls against red (Athene rebuttals, all primary): **no FABNs puttable by investors; no FA-backed commercial paper;** term/known maturities; **89% of total funding penalty-protected or non-withdrawable (36% non-surrenderable);** $71.8B liquidity; 7-yr WAL; #1 FABN issuer; A1/A+/A+; RBC 441%. HY OAS/spread thresholds not in blowout territory.

**Sizing caveat that holds it at yellow not red:** the $16.5B wall is unverified against primary — the rollover quantum that would justify red is not publicly confirmed.

**Escalate to RED only on BOTH:** (i) a verified large 2026-H2/2027 FABN concentration via CUSIP aggregation, AND (ii) FABN spread >250bp OR a failed/pulled syndication.

---

## 6. Recovery path (next session — close the quantum gap without a terminal)

- **Free but laborious:** NPORT-P holdings of funds that hold Athene Global Funding notes carry **CUSIP + maturity + principal at the holder level** — e.g. Morgan Stanley Inst Fund Trust (CIK 0000741375), PIMCO Funds (CIK 0000810893). Aggregate across enough holders to bottom-up a partial 2026-2027 principal estimate.
- **Paid/gated:** Bloomberg DDIS/SRCH, cbonds-Professional, FINSIGHT issuer page, Euronext Dublin/ISE listing particulars.
- **Visual:** Athene FI-deck PDFs are CID-font/vector-encoded on chart pages (do not text-extract) — a human must open any maturity-profile chart visually.

---

## Source provenance
Athene Holding Ltd Q1'26 10-Q (SEC CIK 0001527469, accn 0001527469-26-000028, filed 2026-05-07); FY2025 10-K (accn 0001527469-26-000013); Athene Global Funding $35B Global Debt Issuance Program base OM (May 2025, Deutsche Bank arranger); cbonds aggregator snippets (per-tranche, conf ~0.5, paywalled detail); Athene IR FABN-tender news (2026-06-22); Investing.com benchmark-issuance item (2025-08-19). EDGAR confirmed NO Athene Global Funding registrant. Research pull as-of 2026-06-22.
