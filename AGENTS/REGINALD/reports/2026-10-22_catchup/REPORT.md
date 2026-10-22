# REGINALD — 2026-10-22 catch-up (Will-directed 11:02 ET; PROME assignment 11:1x ET)

Session: Claude Code, Opus 5.5 (`claude-opus-5-5`), session `6c4d79ab`, launched in `AGENTS/REGINALD`, direct Will session. Clock from `date`, 11:02–11:1x ET. Sources, accessions and self-verified figures → `domain/sources/2026-10-22_catchup/RECEIPT.md`. Three extraction readers (EGBN Opus; VLY, BKU Sonnet) worked from local copies of the primaries. Their extracts are saved beside the receipt, and every decisive figure below was re-read by REGINALD at the filing.

## 1. Will's question (SIG-W-20261022-005): does the HY widening transmit to CRE and regional banks?

**Answer: the risk direction is right, but transmission is not visible in any bank instrument yet.** Market-side verdict for 9/21 → 10/20: **BANK-ABSENT, INFERRED, confidence ~0.6** (unchanged from 10/16). The one thing that changed is the composition. Since 10/1 the widening has come only from the weakest borrowers, and that matters for the bank-to-nonbank lending (NDFI) channel, not for deposits.

### 1a. What the spread move is (FRED, first-published values, bp)
| Leg | HY | BB | B | CCC | IG | BBB |
|---|---|---|---|---|---|---|
| 9/21 | 266 | 153 | 270 | 1,077 | 77 | 95 |
| 10/1 | 324 | 204 | 329 | 1,215 | 86 | 106 |
| 10/20 | 333 | 202 | 338 | 1,327 | 87 | 108 |
| **10/21 (new)** | **327** | 198 | 332 | 1,307 | 88 | 109 |
| 9/21→10/1 | +58 (+21.8%) | **+51 (+33.3%)** | +59 (+21.9%) | +138 (+12.8%) | +9 | +11 |
| 10/1→10/20 | +9 (+2.8%) | −2 (−1.0%) | +9 (+2.7%) | **+112 (+9.2%)** | +1 | +2 |

- **Leg 1 (late Sep)** was led proportionally by BB. That is the rate/duration signature: safest junk first, a repricing of all risk.
- **Leg 2 (Oct)** was CCC only, with BB flat. That is credit differentiation: the market is separating out the weakest borrowers.
- CCC/HY = 1,307/327 = **4.00× [10/21]**. VX-REG-18.04's rule is that only a CCC-LED re-cross escalates. The ratio has stayed above 3.6× since before 9/21, so there is no new re-cross. LIQUID owns re-entry.

### 1b. Bank instruments across the same window (yfinance closes; dividend-adjusted where it matters; `reports/2026-10-22_boot/hy_xcheck_closes*.txt`)
| Instrument | 9/21→10/20 | 10/16→10/20 | Reading |
|---|---|---|---|
| Bank pref/jr-sub basket, n=10 (same names as 10/16) | **mean −2.0%** (div-adj), 8/10 down | −0.14%, 4/10 down | Fell **about half as much as broad preferreds** |
| Broad preferreds PFF / PGX (div-adj) | **−3.9% / −3.8%** | +0.03% / −0.49% | Rate-driven (fixed-coupon duration) |
| KRE (regional) | **−1.9%** | +1.2% | **Outperformed** large banks and small caps |
| KBWB / ^BKX (large banks) | −5.7% / −5.9% | +0.4% / +0.3% | Large ≥ regional again |
| IWM / HYG (div-adj) | −3.4% / −1.9% | +2.0% / −0.04% | — |
| SOFR − IORB | −2bp [10/20: 3.88 − 3.90] | — | No funding pressure |

⇒ The bank-specific residual is **positive**: bank credit and regional equities did *better* than the asset classes around them. A bank-transmission story predicts the opposite.

### 1c. Mechanism: why junk spreads do not hit regional-bank CRE directly
- A regional bank's CRE loan is usually priced off Treasury/SOFR plus a bank-set margin, not off the junk-bond market. Wider HY does not, by itself, raise a CRE borrower's refinancing rate. The 10Y fell today (^TNX 5.01% vendor quote 11:03 ET; FRED DGS10 5.15% [10/19]).
- **The indirect routes are real**, and each has an owner:

| # | Route | Owner |
|---|---|---|
| ① | CCC borrowers lose refinancing access → losses at the private-credit funds and BDCs that banks lend to (NDFI) | BROCK; one figure with GIBBS |
| ② | Investor appetite for risky CRE debt (CMBS, mezzanine) tends to move with HY | **CREED: UNKNOWN.** Not launched; needs Will's word, WQ-478. I did not read CREED's leg. |
| ③ | Confidence/funding at weak banks | Mine (§1e) |

### 1d. What the Q3 prints show (all primary, self-verified) — not a spread effect, but the thing to watch
| Bank | Problem loans Q2→Q3 | Reserve coverage of problem loans | NCO (annualized) | Note |
|---|---|---|---|---|
| SSB | NPL ratio 0.54→0.57% | ACL/NPL 213.8→199.7% | 0.09% | ACL/loans 1.15→1.13% |
| VLY | nonaccrual 462.6→**511.4M** (+10.6%) | ACL/nonaccrual ≈131→117% (derived) | 0.17→**0.28%** | CRE ACL 1.05→**0.98%** while construction nonaccrual 9.1→**39.3M** |
| HBAN | NAL 1,589→1,697M (+6.8%) | ACL/NAL 213→198% | 0.25→0.31% | ACL/loans 1.78→1.75%; provision 123 < NCO 146 |
| EGBN | nonaccrual 111.1→**166.0M** (+49%) | ACL/NPL **109.0→72.8%** | 2.78→0.25% | Office overlay released: performing-office coverage 7.22→4.86% |
| BKU | NPL 224→264M (+18%, C&I-led) | ACL/NPL 97.1→84.0% | 0.11% | CRE criticized **down** 481.3→427.4M |
| ZION | NPA 0.48→0.50% (Q2 comparator per WALTER -009) | not computed | 0.02% | Classified 3.40%; CRE nonaccrual 34→40M while CRE-specific reserves fell |

⚠️ **Pattern (descriptive, n=6):**
- Problem-loan stocks rose quarter on quarter at **6 of 6** names.
- Reserve coverage of problem loans fell at **5 of 5** names where computed.
- The banks' stated reason is collateral (VLY: the $30.1M construction loan "well-secured … did not require a specific reserve"; EGBN: office indicators improved).
- **This is skepticism, not evidence of misstatement** (Will feedback 10/20). What separates "well secured" from "under-reserved" is the realized loss when these loans resolve. That evidence arrives at resolution and in the 11/07 Call Report pull, not in the releases. It is a pattern already in progress before the spread move, so I do not attribute it to HY.

### 1e. Tonight's H.4.1 (16:30 ET): what the discount-window print needs to show to matter
Primary credit (FRED WLCFLPCL, Wednesday level): **11,044M [10/14]**, the highest since 2023. Path: 6,235 [9/23] → 8,738 → 9,965 → 11,044, 3 consecutive rises. That is about 1/14 of the SVB peak (152,853M [3/2023]).

Weekly-change base rate since 6/2023 (n=175): |Δ| median 322M, p90 1,227M, p95 1,855M, max 4,693M. The longest run of rises is 6 (ending 7/2/2025).

| Tonight's print | What it means |
|---|---|
| ≤ ~11.0B | Persistence or easing. Nothing new. |
| **> ~12.9B** (≥ p95 rise to a new post-2023 high) | Notable on its own. It still cannot separate precautionary use from need, and borrowers are not named. |
| **> ~15.7B** (larger than any weekly rise since 6/2023) | An outlier week. Read Friday's H.8 the same session. |

**It matters for banks only in conjunction:** a rise plus Friday H.8 small-bank deposits falling and borrowings re-accelerating, plus bank preferreds underperforming PFF. One print alone is not transmission.

⛔ These are **descriptive lines for this read, not a registered threshold.** Registering one needs a base-rate pass and Will's word (open question since 10/20, ROADMAP).

### 1f. For FLG's print tomorrow (~06:00 ET, Fri 10/23)
The HY context is a CCC-led widening with bank instruments outperforming. My pre-registered FLG 'weakens if' lines are unchanged (`reports/2026-09-26_CRE_vulnerability_top3.md` §6): MF special mention ≤ $2,757M; modifications < $556M. FLG's ladder `VX-REG-6.03` has been RED since 10/7: 11 settled closes below $11.39, latest **$11.07 [10/21]**, −22.3% vs the FROZEN $14.24. Price is not a matrix input.

**Cohort ranking: unchanged** (FLG 6 · EGBN 5 · AMTB 5 · VLY 3 · OZK/WAL/SSB/BKU/SBCF 2 · ZION/MTB/CUBI 1 · CFG/HBAN 0). Scores move only at the 11/07 re-score. VLY's Q3 adds to its existing bank-specific early flag (§3); it is not a re-score.

## 2. Pre-registered grades

### 2a. REG-27 (GATE-REG-27) — SSB NPL ratio ≥ 0.70% at any release Q3-26..Q2-27
**Q3 release: 0.57% [9/30/26]** (EX-99.1 asset-quality ratios, "Nonperforming loans as a percentage of period end loans"; series 0.63/0.62/0.61/0.54/0.57). **Not met at Q3 → row stays OPEN** (window runs to the Q2-2027 release). Confirm at the Q3 10-Q. No ledger cell changed. NPL = nonaccrual 159,465 + 124,870 plus accruing 90+ 3,642 + 6,987 ($K). Two-route check: ACL 588,918 ÷ 199.66% = $295.0M, and $295.0M ÷ loans $52,053M = 0.567% ✓. The acquired book drove the rise: acquired nonaccrual 99.4 → 124.9M, acquired accruing 90+ 0.8 → 7.0M.

### 2b. FL bank-rail frozen frame (`reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md`)
| Name | Cells graded today | Class (A2 combiner) |
|---|---|---|
| **SSB** | **P = NCO 9bp < 20bp → HOLDS** · Total nonaccrual $284.3M ≤ $340M → **HOLDS** · Classified accrual share (10-Q) UNREAD | **HOLDS, PROVISIONAL** (10-Q cell unread) |
| **BKU** | CRE criticized 481.3 → 427.4M (−$53.9M) → **HOLDS** · P CRE 30-89 + CRE 90+ (10-Q) UNREAD | **HOLDS-PENDING-P** |
| AMTB | prints tonight after close | UNREAD |
| SBCF | Tue 10/27 after close | UNREAD |

Aggregate (A3 overlay): **UNKNOWN**, with AMTB and SBCF missing and the BKU primary and the SSB 10-Q cell unread. *T* = 0.

⚠️ **Disclosed basis note:** the frame's SSB Q2 nonaccrual baseline is $297.2M (10-Q). The release prints Q2 nonaccrual as 171,264 + 99,352 = $270.6M. The cell holds on either basis (bar $340M; +15% on $270.6M = $311.2M; Q3 $284.3M is below both). The frame is unedited.

BKU outside the frame: NPLs rose $40M, all C&I. Ending non-interest-bearing deposits fell $821M (−8%), but the **average was flat** (9,027.4M vs 9,027.6M). The company attributes the drop to seasonal normalization after elevated Q2 inflows. FHLB advances 1,630 → 1,925M. Government-insured resi 90+ dollars are not disclosed.

## 3. D:L521 — VLY Q3 (printed today before the open, call 08:30 ET; call not heard)
| Pre-registered question | Answer at the release/deck |
|---|---|
| MF 30–59 cohort (Q2 MF past dues $101.5M): cure or roll? | **NOT DISCLOSED by bucket.** Three CRE loans ($24.7M net of $9.1M partial charge-offs) **rolled 30–59 → nonaccrual**. One $10.9M CRE relationship moved into 60–89 (from nil). A $4.0M CRE loan moved to 90+. CRE 30–59 72.6M vs 106.0M. Property types of these loans are not stated. |
| CRE nonaccrual vs $256.1M | **253.1M** (−$3.0M) ex-construction; **construction 9.1 → 39.3M** (one $30.1M loan, "well-secured", no specific reserve); total nonaccrual 462.6 → 511.4M |
| Q3 modifications; re-default of ~$108M payment-delay mods; the $5.454M loan | **NOT DISCLOSED** (10-Q) |
| Direction of quantitative CRE reserves | **Down again:** "a decline in quantitative reserves largely within certain CRE loan categories, including construction". CRE ACL 319.1 → 299.4M (1.05 → 0.98%); construction ACL 50.6 → 46.5M while construction nonaccrual rose 4×. |
| Bluevine deposit migration | "early 2027" close only; $2.1B, Coastal Community Bank, TBV dilution **not discussed**. Indirect deposits 5.3B flat. |

**Checkpoint result: the Q2 early flag STRENGTHENS (bank-specific).** For the second straight quarter, problem CRE rose while quantitative CRE reserves were released. This is a checkpoint, not a resolution: deferrals run to ~Q1-27 and modifications/re-defaults are 10-Q items (~11/10). NCOs 0.17 → 0.28%. CET1 10.71% unchanged. The stock was +4.6% intraday at 11:03 ET (vendor quote, not settled; price is not an input).

## 4. EGBN — the four named loans (WOB008/009/013/014) and L35 (RED's CHG-027 grade is RED's)
| Loan | Q3 outcome (deck s19/s20/s21, read by REGINALD) | Cash / exit |
|---|---|---|
| **008 Prince George's apartments $56.0M** | **Moved to NONACCRUAL** (#1 nonaccrual loan, 33.7% of $166.0M). Still substandard. **Maturity extended again, to 12/21/2026** (was 8/21). LTV 88% on a 3/9/2026 $63.7M appraisal; DSCR 0.74 [8/31/26] (Q2: 0.63). Variable rate 7.40%. | **No principal received; no outside exit; continued bank support plus recognition.** Loan-level reserve not disclosed. The "single multifamily loan = 76.0% of $73.7M inflow" equals $56.0M (arithmetic match; the company does not name it). |
| 013 Montgomery self-storage $56.196M → **$56.062M** | Special mention, accruing; matures 2/10/2027; appraisal dated 7/27/2022; DSCR 0.90 | Small amortization only |
| 009 Fairfax office $22.072M | **Not identifiable.** A different Fairfax office loan ($18.5M, matured 2/28/2026, DSCR −0.56) is nonaccrual #2, plus a $5.9M Fairfax office nonaccrual. | **UNKNOWN** |
| 014 Anne Arundel self-storage $14.996M | **Not identifiable** in the >$10M criticized, >$5M nonaccrual or Top-25 lists | **UNKNOWN**; absence is not a payoff |

Also:
- **$265.7M of income-producing multifamily matures in 4Q26.** That book is $574.8M, 43.1% criticized and 11% nonaccrual (s16).
- Criticized >$10M maturing in 4Q26 sums to **$146.9M**, including a $20.5M DC apartment loan at **LTV 152%, DSCR 0.24**, maturing 12/30/2026.
- Held-for-sale sales were $34.6M with nil gain/loss. NCOs 0.25%. CET1 14.99%.

⇒ **The open question is answered for one of four loans:** Prince George's got continued support, not outside cash. The other three remain UNKNOWN. The Q4 maturity wall is now the binding test. The 10/22 10:00 ET call has not been heard (no transcript read).

## 5. Inbox / BOARD dispositions (11-column rows in `board/BOARD_LOG.tsv`; files → processed/)
| Item | Disposition |
|---|---|
| SIG-W-20261021-009 ZION Q3 | INTEGRATED. Verified NCO 0.02%, NPA $315M (0.50%), classified $2.1B (3.40%). **ZION ranking stays 1**, with nothing in the print to support a Zions-specific credit thesis. The one mild adverse item is CRE nonaccrual 34 → 40M with the CRE reserve released. Book context: ZION $65.80 [11:03 ET vendor quote] vs Will's $62.5 put strike. Construction and any action are TERRY's; Will decides. |
| SIG-W-20261021-013 EGBN Q3 | INTEGRATED (§4). |
| SIG-W-20261021-025 OCC GENIUS final rule | INTEGRATED, read at the primary (nr-occ-2026-92a.pdf): the statutory issuer yield ban stays; the proposed **rebuttable presumption on affiliate/third-party payments is ELIMINATED**, and the OCC keeps its anti-evasion authority. Third-party "rewards" are not presumed violations, so the deposit-competition leg stays open structurally. Effective 1/18/2027 (OCC release via search; date not re-read in the PDF). No grade, no near-term bank-stress reading. |
| SIG-W-20261022-002 Asia selloff | INFO_ONLY. REG-T-04 (>350 ×3) is **23bp away at 327 [10/21]**, not in play. |
| SIG-W-20261022-005 Will's HY question | INTEGRATED (§1). |
| GIBBS 10/21 large-bank Q3 comparison | INTEGRATED. The IB-deposit-cost rise is industry-wide (10/10 large banks), so funding pressure is not regional-specific; PNC CRE is the one large-bank deterioration read. Consistent with §1. |
| HANS 10/21 euro-bank selloff | INFO_ONLY. SX7E −8.0% (9/18 → 10/21) vs KRE −1.9% (9/21 → 10/20): US regionals did not follow. Cause unestablished per HANS; BNP 10/28 is HANS's test. |
| PROME 10/21 WQ-454.REGT06 RULED B | CONSUMED. Leg 3 grades **11/13 from the Combined Financial Report** as the letter says; the 10/30 Highlights are context only. Any instrument change is a pre-registered amendment for the next quarter. |

| SIG-W-20261022-008 (post-boot) big banks restricting third-party AI agents | INFO_ONLY. Anonymous rogue-agent claim; Morgan Stanley disputes it; no loss reported; regionals not named. Context for Will's AI-agent docx analysis (§7). |
| SIG-W-20261022-011 (post-boot) WALTER bank sweep | INTEGRATED; agrees with my primary reads. WALTER's "SSB does not show thinning" is true of ACL/loans, but on ACL/NPL SSB **does** thin (213.8 → 199.7%). |

⚠️ **Index-sweep incident (flagged to PROME, not repaired):** my eight staged `git mv` inbox renames were committed inside WALTER's `5854ecb98` ("WALTER -> REGINALD, FLG, WAL +6: 011 bank sweep"). That happened because the shared index was swept between my stage and my commit. Content is correct (pure renames, 0 lines changed). Attribution is wrong. I am not rewriting another desk's commit.

## 6. Market / threshold refresh (settled = Yahoo + Nasdaq agree; `reports/2026-10-22_boot/`)
- **WAL:** $75.55 settled [10/21]. REG-T-02 exit 0-of-3; log row 36.
- **KRE:** $70.62 settled [10/21]. REG-T-01 un-fired.
- **HY:** 327 [10/21]; 6 consecutive >320 (325/323/331/329/333/327 for 10/14–10/21).
- **Claims:** 194K [w/e 10/17, FRED, first print 10/22].
- **SOFR:** 3.88 [10/20]; IORB 3.90; RRP $0.227B [10/20].
- **Stress indices:** STLFSI4 −0.721 [10/9]; NFCI −0.502 [10/9].
- **Vendor quotes, 11:03 ET (not settled):**

| | Quote | Move |
|---|---|---|
| VIX | 19.31 | +15.8% |
| SPY | — | −1.3% |
| QQQ | — | −2.4% |
| KRE | — | +1.6% |
| EGBN | — | +10.4% |
| VLY | — | +4.6% |
| BZ=F | $111.41 | — |
| ^TNX | 5.01% | — |

Today's tape is AI/tech-led, and regionals are up.
