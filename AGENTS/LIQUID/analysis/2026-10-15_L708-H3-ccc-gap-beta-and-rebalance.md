# L708 — LIQUID's leg: is the CCC−B gap widening index mechanics (H3), is a sector split reachable, and how far is CCC moving beyond its beta to B?

**LIQUID · Thu 2026-10-15 08:34 ET · PROME `prome-73` Tier-1 wake (WQ-184) · commission: Will via NEXUS, 2026-10-14 21:21 ET (`AGENTS/LIQUID/inbox/2026-10-14_from-NEXUS_commission-what-is-widening-the-CCC-tier-alone.md`; spec `AGENTS/NEXUS/research/2026-10-14_commission_CCC-gap_consumer-attribution.md`).** $0. No gate, no threshold, no trade words. The spec's sessions are used as written: primary = the 7 published sessions 10/2→10/13, secondary = the 5 sessions 9/25→10/1; the 10/12 ICE holiday carry-forward is excluded.

## Answer

| Question | LIQUID's answer | Confidence |
|---|---|---|
| **H3, rebalance arm:** does the widening concentrate in the 9/30→10/1 rebalance session? | **No.** 10/1 = +23 of the +124bp gap widening 9/25→10/13 (**18.5%**). The **primary window (10/2→10/13) contains no rebalance and the gap still widened on 7 of 7 sessions (+64bp)**. | VERIFIED (FRED, first-published = latest-revised in window) |
| **H3, migration arm:** could B→CCC downgrades adding wider names explain it? | **Not inside the primary window, by construction.** ICE fixes constituents between month-end rebalances; a bond downgraded mid-month stays in its old tier until the next rebalance (FRED's ICE methodology note, quoted in §3). So 10/2→10/13 is a **fixed basket repricing**, and migration can act only at 10/1 (next: the 10/31 rebalance). | VERIFIED (methodology text) · the application is INFERRED |
| **H3, few-names arm:** is it ≤3 names? | **NO_INSTRUMENT.** No constituent data for the ICE CCC index is reachable from this box. One named distressed event sits inside the window: **Getty Images** (NYSE suspension 9/29, OTC from 9/30, prepackaged Chapter 11 plan announced 10/12; secondary sources, §4). Its index weight and contribution are unmeasurable here. | NO_INSTRUMENT |
| **Sector split of the CCC index** | **NO_INSTRUMENT — confirmed again.** ICE sector sub-indices are terminal-only and TRACE is gated. **New, partial:** a *proxy* is reachable **forward only**. BlackRock's HYG fund download lists every bond with sector, price and yield-to-worst, but returns only the latest date (`asOfDate` ignored, tested 10/15 08:3x ET), so it cannot reconstruct 10/2→10/13. | NO_INSTRUMENT (index) · proxy reachable from 10/13 on |
| **Beta read, CCC vs B** | **CCC is moving well beyond its beta to B.** The fit is ΔCCC = 1.245 × ΔB (R² 0.69, residual sd 6.5bp). Over the primary window, B −12bp implies CCC −15; **CCC actually moved +52**. The excess was positive on **7 of 7** sessions and ≥ 1 sd on **5 of 7**. A run of 7 of 7 occurred in **7 of 750** historical 7-session windows (0.9%, overlapping). | VERIFIED as a fit; the cause is not identified by this |
| **H2, one line** | VULCAN's four CCC names, equity only: **rule-4 MIXED** (no name beyond z ≤ −1.0 on ≥ 4 of 7 sessions; none within \|z\| ≤ 0.3 on ≥ 4 of 7). Substantively there is **no AI-disrupted-CCC equity signal on the widening days**; Getty's own distress is the exception (§6). | equity proxy; Getty's z unreliable (OTC, sub-$0.10) |
| **H1 verdict token (LIQUID's lane)** | **NO_INSTRUMENT.** Under spec §3 rule 1, LIQUID names **0** consumer-exposed issuers with a verified rating and reachable daily data. CARL and OTTO own the issuer test. | — |

**What the tier data adds for NEXUS:** it rules out the two cheap explanations. **(a) Beta:** a CCC move scaled from B cannot widen the gap on B-tightening days, and here it did so on all three (10/2, 10/6, 10/9). **(b) Index plumbing:** the primary window has a fixed basket. What remains is a **price move inside a fixed CCC basket, beyond beta**. That is consistent with H1, H2-at-other-names, H3's few-names arm or H4-in-the-weakest-names, and tier data cannot choose among them.

## 1. Data and basis

- **Series:** FRED ICE BofA `BAMLH0A2HYB` (B) · `BAMLH0A3HYC` (CCC & lower) · `BAMLH0A1HYBB` · `BAMLH0A0HYM2`. Values are percent × 100, rounded to whole bp. Pulled via FORGE `fetch.py` 10/15 ~08:3x ET. History runs 2023-10-16 → 2026-10-13 (785 published observations, FRED's rolling ~3 years, a calm window).
- **Vintage:** `fred_fetch_vintage` (ALFRED first-published) equals latest-revised on all four series for the 39 observations 8/20→10/13: **0 mismatches** (windowed claim).
- **Holiday rows:** 15 carry-forward rows (all four series unchanged) are excluded, among them 10/12. Each change is measured against the previous non-carry observation, so 10/13's change runs from 10/9.
- **Fit window:** 2023-10-17 → 2026-09-23 (756 daily changes), so the graded window sits out of sample. Same method as my 10/9 B-vs-BB read (`analysis/2026-10-09_wq341-LIQ07-attribution.md`).
- **Reproduction:** `research/2026-10-15_L708-ccc-gap/` holds the scripts, their printed outputs and the source bytes (`fred-pull.json.gz`, `hyg-download-2026-10-14-holdings.xls.gz`, sha256 `2e41621c…6319` before gzip). The 10/13 holdings copy is the 10/14 session's `research/2026-10-14_credit-funding-refresh/hyg-download.xls.gz`. Script paths point at this session's scratchpad; re-point them to the preserved files to re-run.

## 2. CCC beyond its beta to B, per session (bp)

Fit: ΔCCC = **1.245** × ΔB, no intercept, residual sd **6.53**, R² **0.693**, n = 756. With an intercept: α +0.44, β 1.246, sd 6.53; every excess below moves by ≤ 0.5bp. **Excess** = ΔCCC − 1.245·ΔB. Each percentile ranks the excess against the fit residuals.

| Session | ΔBB | ΔB | ΔCCC | ΔHY | CCC−B gap | Δgap | β·ΔB | **Excess** | pct (signed) |
|---|---|---|---|---|---|---|---|---|---|
| *9/24 (pre-window)* | +5 | +8 | +19 | +7 | 826 | +11 | +10.0 | +9.0 | 95 |
| 9/25 | +12 | +14 | +16 | +13 | 828 | +2 | +17.4 | **−1.4** | 36 |
| 9/28 | +7 | +9 | +18 | +9 | 837 | +9 | +11.2 | **+6.8** | 91 |
| 9/29 | +6 | +7 | +11 | +6 | 841 | +4 | +8.7 | **+2.3** | 67 |
| 9/30 (quarter-end; still the September basket) | +5 | 0 | +22 | +4 | 863 | +22 | 0.0 | **+22.0** | 99 |
| **10/1 (rebalance session)** | +10 | +13 | +36 | +12 | 886 | +23 | +16.2 | **+19.8** | 99 |
| 10/2 (B tightened) | −13 | −17 | −13 | −14 | 890 | +4 | −21.2 | **+8.2** | 93 |
| 10/5 | +2 | +2 | +9 | +2 | 897 | +7 | +2.5 | **+6.5** | 90 |
| 10/6 (B tightened) | −8 | −12 | +3 | −9 | 912 | +15 | −14.9 | **+17.9** | 98 |
| 10/7 | +4 | +6 | +15 | +6 | 921 | +9 | +7.5 | **+7.5** | 93 |
| 10/8 | +5 | +7 | +23 | +6 | 937 | +16 | +8.7 | **+14.3** | 97 |
| 10/9 (B tightened) | −6 | −5 | +1 | −4 | 943 | +6 | −6.2 | **+7.2** | 92 |
| 10/13 (vs 10/9) | +3 | +7 | +14 | +5 | 950 | +7 | +8.7 | **+5.3** | 86 |

| Window | Sessions | Σ Δgap | Gap up | Σ ΔB | β-implied ΣΔCCC | Actual ΣΔCCC | Σ excess | Excess > 0 | Excess ≥ 1 sd |
|---|---|---|---|---|---|---|---|---|---|
| **Primary 10/2→10/13** | 7 | **+64** | 7/7 | −12 | −14.9 | **+52** | **+66.9** | **7/7** | **5/7** |
| Secondary 9/25→10/1 | 5 | +60 | 5/5 | +43 | +53.5 | +103 | +49.5 | 4/5 | 3/5 |

**Rarity in the fit history** (overlapping windows, so a frequency and not an independent probability): a 7-session run with positive excess every day = **7 of 750** windows; the gap widening on 7 consecutive sessions = 16 of 750; on 12 consecutive sessions = **0 of 745**. The 12-observation gap change, **+124** (9/24→10/13), exceeds every 12-observation change in the fit window (maximum +121).

⚠️ **Limits:** one linear daily model on a calm 3-year history. A positive excess says CCC moved more than B's move predicts, and it does not say why. Index OAS is market-cap weighted (FRED's ICE note), so a few large, deeply discounted names can drive it. That is the H3 few-names arm, which tier data cannot see.

## 3. H3: the rebalance and migration arms

**ICE's rule (FRED series notes for `BAMLH0A0HYM2`, retrieved 10/15 via the FRED API; the CCC series note describes it as a subset of that index):** *"The Index is rebalanced on the last calendar day of the month, based on information available up to and including the third business day before the last business day of the month. Issues that meet the qualifying criteria are included in the Index for the following month. Issues that no longer meet the criteria during the course of the month remain in the Index until the next month-end rebalancing at which point they are removed from the Index."* The CCC note: *"This subset includes all securities with a given investment grade rating CCC or below… An OAS index is constructed using each constituent bond's OAS, weighted by market capitalization."*

- ⇒ **Intra-month, the tier baskets are fixed.** A B-rated bond downgraded to CCC on, say, 10/5 stays in the B index until the 10/31 rebalance. **Migration can enter the CCC series only at a month turn.** The application to the rating sub-indices is INFERRED from the rule's general wording; ICE's full rulebook is not reachable from this box.
- **The rebalance session was large, but it is not the story.** 10/1's +23 is the **largest month-turn gap change in the 35 month turns of the fit window** (previous maximum +20, 2025-06-02). Month turns usually lift the gap: mean +2.8bp, up on 74% of them, against +0.3bp on other days. Even so, 10/1 is 18.5% of the 9/25→10/13 widening. **With 9/30 added it is +45 of +124 (36%).** 9/30 is quarter-end, still on the September basket, so it is a pricing or marking session and not a composition change.
- **H3 rebalance/migration arm: NOT SUPPORTED** as the explanation of the commission's primary window. It is **partly consistent with the secondary window**, where 9/30 and 10/1 together are 45 of 60bp.

## 4. H3: the few-names arm — NO_INSTRUMENT, with one named event

- I have no constituent-level price, weight or OAS for the ICE CCC index (terminal-only; TRACE gated; STATUS §5 standing caveat). **The arm is neither supported nor excluded.**
- **Named distressed event inside the window (SECONDARY-SOURCED, not verified at the primary filing):** **Getty Images** (VULCAN: CCC). NYSE suspended trading and began delisting on 9/29 for an "abnormally low selling price"; the stock trades OTC Pink as GETY from 9/30. On 10/12 Getty announced a plan for an expedited prepackaged Chapter 11 in which Getty-family affiliates and Koch Equity Development take 100% ownership and unsecured noteholders agree to retire $270M of notes. Total debt ~$2.1B [6/30]. Sources: [panabee](https://www.panabee.com/news/getty-images-delisted-from-nyse-transitions-to-otc-pink) · [stocktwits](https://stocktwits.com/news-articles/markets/equity/after-failed-shutterstock-merger-and-nyse-delisting-getty-plans-chapter-11-bankruptcy/cZxBE7YRBoR) · [ppc.land](https://ppc.land/nyse-suspends-getty-images-with-1-47bn-of-debt-and-12-cent-shares/) · SEC 8-K [ea0307245](https://www.sec.gov/Archives/edgar/data/0001898496/000121390026105790/ea0307245-8k_getty.htm) (listed, not read). Equity raw closes: $0.240 [9/22] → $0.083 [9/28] → $0.042 [10/2] → $0.019 [10/12]. ⚠️ **Its bond did not collapse.** In HYG's holdings, Getty Images 11.25% 2030 is evaluated at **90.00 / YTW 15.17% [10/13] → 89.16 / 15.52% [10/14]**. This is a single-name equity wipe, and whether it moved the CCC index is unmeasured.
- The deeply discounted CCC paper visible in HYG on 10/13 (CSC Holdings/Optimum bonds 16–46, YTW capped at 50; iHeart 2030 at 56.7) is the kind of paper that can dominate a market-cap-weighted OAS. **I hold no history for it across 10/2→10/13**, so no contribution is claimed.

## 5. Sector decomposition — NO_INSTRUMENT for the index; a proxy, forward only

- **ICE CCC index sector split: NO_INSTRUMENT** (as on 10/9). FRED carries tiers, not sectors.
- **Proxy found this session:** BlackRock's HYG fund download (`varnish-api … component=fundDownload`, the endpoint the 10/14 session used for share counts) carries a **Holdings sheet**: 1,332 bonds with name, iShares sector, price, YTW and weight. **The latest date only:** requests with `asOfDate=20261001` and `20261013` both returned the 10/14 file. It is usable going forward only if someone snapshots it each day. HYG tracks **iBoxx** (not ICE) and has **no rating column**, so "CCC" would be a yield/price proxy.
- **One-session demonstration, OUTSIDE the commission's sessions and not used in any verdict** (10/13 file preserved 10/14 → today's 10/14 file; price-only, accrual excluded): HYG's price contribution was −0.39%. The YTW ≥ 12% sleeve (102 bonds, 5.2% of weight) contributed 16% of that, with a weighted return of −1.21%. **Within that sleeve, CoreWeave alone was 28%** of the loss (four bonds: 9.25% 2030 89.37→85.76; 9.00% 2031 84.85→81.70; 9.75% 2031 82.46→81.00; 9.625% 2032 79.75→77.03, YTW 14.98→15.83%). The top three issuers (CoreWeave, JetBlue, Connect Holding II) were 46%. By sector, "Other" (incl. CoreWeave) was 36%, Consumer Cyclical 20% and Transportation 16%. This shows the instrument can see few-name concentration. It says nothing about 10/2→10/13.

## 6. H2 — one line

Equity total return, z = (r − β·SPY)/σ, with β and σ fitted 2026-03-02 → 09-23 (VULCAN's method), on the 7 primary sessions. **GETY** z: −4.93, −0.38, +2.09, −0.95, +0.76, −0.13, 0.00. **OPTU** (Optimum Communications): −0.39, +0.83, −0.39, +0.50, −0.10, −0.72, −0.35. **RXT:** +0.41, −0.60, +0.14, −0.30, −0.41, +0.52, −0.11. **IHRT:** −1.64, +0.79, −0.55, +0.18, −0.30, −0.67, −0.47.
- Names beyond z ≤ −1.0 on ≥ 4/7 sessions: **0 of 4** (maximum 1/7).
- Names within \|z\| ≤ 0.3 on ≥ 4/7: **0 of 4** (maximum 2/7).
- ⇒ rule-4 **MIXED** by analogy with the H1 rule, which NEXUS's spec writes for H1, not H2.
- **Plainly: no sign that VULCAN's AI-disrupted CCC names led the widening days**, except Getty's own bankruptcy path (10/2 −47.5% equity), which is an idiosyncratic dated event.
- ⚠️ GETY is an OTC stock under $0.10 with σ ≈ 10%/day, so its z is unreliable. Equity is a proxy; bonds and CDS for these names are unreachable.

## 7. What this read does NOT establish

- Which issuers or sectors carried the primary-window move. That is CARL's and OTTO's issuer test, plus a constituent source nobody here has.
- That consumer names did or did not drive it (H1). LIQUID's lane is NO_INSTRUMENT on H1.
- Anything about funding. `LIQ-07`'s S1/S2 funding branch is graded separately on its own letter, on 10/16.
- Calibration. The base rates rank against a calm 2023–26 window with no 2020/2022 stress.

**H1 verdict token (LIQUID): NO_INSTRUMENT**
