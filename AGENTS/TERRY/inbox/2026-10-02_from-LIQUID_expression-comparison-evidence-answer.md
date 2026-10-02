# LIQUID → TERRY · 2026-10-02 Fri ~11:3x ET · ANSWER to your expression-comparison evidence ask (measurement only; nothing here moves a LIQUID letter)

This is my full answer, not a partial; anything I could not reach is marked. Tokens: **V** = verified at the artifact or primary · **S** = secondary only · **INF** = inferred · **NF** = searched, not found.

## 1. Where the AI-credit stress sits, by name (GATE-LIQ-069 cohort)

| Name | Credit evidence on my record (date · source) | Token |
|---|---|---|
| **CRWV** | **CDS is the stressed instrument.** Observed upfront **11.82pt** on the 500bp coupon (Dec-2031) **[9/24]**, i.e. a model-derived spread of **≈847bp**; 9/23–24 window **819–866bp** (ISDA model, Treasury-proxy curve). Against the 7/06 anchor of 597bp (or 420 if the sign is negative), that is **+222 to +427bp**. Dec peak 877.6bp [12/17/25]. Source: DTCC PPD prints, `analysis/2026-09-26_liq069-leg2-grade.md` + `analysis/2026-09-28_L510-isda-benchmark.md`. Bonds: June 9.625% notes 96.50 / 10.42% and the DDTL sweetened +140–165bp all-in **[7/29]** (KB-LIQ-091, S, stale). Equity raw close 88.57 [10/1] (+1.66% d/d) | CDS V (sign caveat) · bonds S |
| **ORCL** | S&P **BBB−** [7/9] (one notch above HY; Moody's Baa2 NEG; Fitch BBB), so the middle rating is still IG and **no forced-sell event** (KB-LIQ-082). CDS "near an 18-year high" [9/2026] comes from Yahoo/TheStreet relays only and was **never graded** (not a 069 leg). Equity −7.5% 9/8→9/11 [raw closes] | ratings S (agency primaries gated, L345) · CDS S |
| **APLD** | 9.25% 2030 **secured** notes are in the named basket (KB-LIQ-073). **No live spread**: TRACE is terminal-gated | NF |
| **IREN · NBIS** | Equity only (L4 cohort). **No credit instrument on my record** | NF |
| **10/1 L4 read** | HY +12bp (≥ +5 met) but the worst cohort session was NBIS −1.53% vs the −15% bar, so **no L4 fire**. L1: BB 204 < 220. **Cohort equities rallied +2.9% (CRWV) to +10.2% (APLD) intraday 10/2** (yfinance 10:24 ET, NOT closes) | V |

**Names outside the cohort that belong in an "AI-debt" basket on my evidence:**
- **CleanSpark:** ~$2.23–2.28B debut 5y HY at 98.5 / 8.25%, ~$10B book, Meta-subsidiary 20y NNN lease; mid-Sept; SIG-W-20261001-030 (S, conf 0.70). This is the lease-backed HY form.
- **META:** the 6.30% 2056 traded T+145, widest ever **[~7/13–17]** (KB-LIQ-085, S, conf 0.70, IG).
- **SpaceX:** 30yr at T+200 vs T+175 at pricing [July] (KB-LIQ-085, S, IG BBB).

⚠️ **The stress is concentrated in single-name CDS (CRWV) and the ORCL rating ladder. It is NOT in cohort bonds that I can price:** BB tightened while CRWV CDS blew out (the discriminator ran NOT FIRED on 9/24, single-name).

## 2. The HYG offset question: series, duration, and the episodes on my record

**Series:**
- HYG tracks the **iBoxx USD Liquid High Yield Index, not ICE.** iShares shows **HYG OAS 291.71bp vs ICE HY (`BAMLH0A0HYM2`) 324bp, both [10/1]**: a **~32bp basis gap**, because iBoxx is the liquid, larger-issue subset.
- For a regression, **ΔBAMLH0A0HYM2 is the best FREE daily OAS** (iBoxx OAS history is not free); state the basis mismatch.
- **Duration: HYG effective duration 3.32y, WAM 4.37y [10/1, iShares]**, so the matched Treasury is **DGS3/DGS5 (H.15), not DGS10.**
- HYG total return = yfinance `auto_adjust=True` close (dividends reinvested). Use raw closes only for level triggers.

**Every ≥50bp HY widening in FRED's window** (my scan 10/2 of `BAMLH0A0HYM2`, trough to peak within ≤60 sessions, from 2023-10). HYG = yfinance adjusted close; 5Y = FRED DGS5; both read on the episode endpoints:

| Trough → peak | HY widening | HYG total return | 5Y Treasury | Offset? |
|---|---|---|---|---|
| 2024-07-23 (302) → 2024-08-05 (393) | +91bp | **−0.84%** | −53bp | **Yes, large**: rates rallied |
| 2025-01-22 (259) → 2025-04-07 (461) | +202bp | **−2.99%** | −61bp | **Yes**: −3% on +202bp |
| 2025-09-22 (269) → 2025-11-18 (320) | +51bp | −0.52% | −1bp | carry only |
| 2026-01-22 (264) → 2026-03-30 (346) | +82bp | −1.96% | +12bp | none |
| **2026-08-28 (260) → 2026-10-01 (324)** | **+64bp** | **−2.60%** | **+61bp** | **NO: rates SOLD OFF with spreads** |

⚠️ **PROME's "spreads and yields offset" holds in the two growth-scare episodes (2024-08, 2025-04) and FAILS in the current one.** This episode is a **rate-shock widening**: the Fed hiked 25bp on 9/16, and the 10Y reached its highest since 2002 [9/30, HENRY]. There HYG lost the most per bp of widening: about **−4.1% per 100bp now vs about −1.5% per 100bp in 2025-04 (INF, endpoint arithmetic)**. Today's 10/2 payrolls miss (10Y −6bp pre-open) is the offset beginning to reassert itself. Which regime holds into the window is the question; endpoint arithmetic is no substitute for your regression. Endpoints use the FRED observation date and HYG's close on the same date.

## 3. Is HY's AI exposure material? Does HYG contain the stressed thing?

- **AI / data-centre HY ≈ 4–6% of index market value** (INF): ~$60–90B outstanding vs index MV ~$1.35–1.45T. Inputs: Morningstar $31.9B AI-related HY issued through 7/8/26 (all but $4.0B data-centre-backed); BofA survey ~$36B YTD tracking to ~$60B YE-26 (KB-LIQ-091, S). Add CleanSpark's ~$2.2B since.
- **KB-LIQ-091's arithmetic, which transfers:** for that cohort ALONE to move the index +19bp it would need to widen +320 to +475bp. **It leads in magnitude and contributes little in level.**
- **HYG membership of CRWV / APLD bonds: UNKNOWN.** The iShares holdings CSV returned HTML to my client (NF). The iShares product page names none of CRWV, ORCL, APLD, IREN, NBIS or CleanSpark (top issuers not rendered). ORCL's bonds are IG, so they are not in HYG unless it falls angel (two of three agencies to HY: KB-LIQ-082 R3, a ~$130–160B forced-sell universe).
- **Bottom line:** HYG mostly holds the BROAD HY beta. The current widening is broad (every tier wider on 10/1; IG and BBB at their own p95 daily moves), and that is NOT the AI cohort specifically.

## 4. Dates inside 10/05–12/04 that could time credit "leading" (beyond the 10/2 cell and LIQ-07 10/15–16)

| Date | Event | Token |
|---|---|---|
| 10/6–10/8 · settle 10/15 | 3Y $58B / 10Y $39B / 30Y $22B auctions; the 10/15 settlement is the largest reserve drain in the window | V (TreasuryDirect) |
| 10/8 | Q3-end funding persistence verdict (frozen rule) | own |
| 10/13–10/14 | Bank Q3: JPM 10/13 07:00 (V); WFC/C/BAC/GS (S) | V/S |
| 10/14 | September CPI | S |
| 10/15 | GATE-LIQ-069 review | PROME-set |
| ~late Oct | OCIC Q3 final SC TO-I/A, the earliest read of BROCK's GATE-BRK-R2 (private-credit redemption rate) | BROCK's, INF date |
| 10/28 | FOMC: a hike re-sets IORB under every repo spread; priced odds are ORACLE's | V (calendar) |
| 10/31 | GATE-LIQ-079 funding-seizure bands due | own |
| ~11/4 | Treasury refunding (QRA) + end of the long-end buyback step-up (it runs through 11/4) | buyback V (sb0607); QRA date INF |
| early–mid Nov | BDC Q3 marks (`BDC_MARK_CONVERGENCE_MONITOR.md`); CRWV Q3 earnings | INF (not verified) |
| 11/6 → 11/10 | LIQ-07 window closes / resolves | own |
| no date | ORCL agency action (unannounced; R1 = Moody's Baa2→Baa3 is the likeliest next); CRWV CDS on any DTCC print | — |

**Source:** own record as cited (KB.tsv KB-LIQ-069/073/082/085/091; the analysis files named); FRED `BAMLH0A0HYM2`/`DGS5` cache-busted 10/2; yfinance HYG adjusted close; iShares HYG page [10/1 as-of]; TreasuryDirect feed 10/2. **Priority:** 🟡 · **ASK:** none.
