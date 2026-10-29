# Severity comp refresh — 2026 transactions + OZK's own realized losses (TODO C4)

**Date:** 2026-10-28 (OZK; Will-approved work item, "1 2 3 all approved go ahead", 22:44 ET). **Replaces** KB-OZK-177 (Apr-22 bands, stale since 7/31) → KB-OZK-268 (market) + KB-OZK-269 (OZK lender basis).
**Inputs:** web sweep `2026-10-28_SEVERITY_COMPS_2026_SWEEP.md` (17 rows, 31 fetches, sources and verification status per row) · OZK primary disclosures (Q1–Q3-26 MC, FDIC FLNG; rosters in `STATUS.md` and `research/threads/Q2_2026_10Q_READ.md` §2) · DEWEY failed-bank base rate (`AGENTS/DEWEY/output/2026-10-22_reserve-coverage-decline-base-rate.md`).

## Bottom line

**The old band measured the wrong object for half its use.** KB-177 applied property-value declines (−45% to −68% from peak) to OZK's problem book. 2026 shows two different numbers:

1. **Property values** of vacant or partly leased office and lab are down **50–90% from prior sale** in 2026 trades (Chicago office median ≈−75%), as deep as or deeper than the April bands.
2. **OZK's own loss when it takes a loan through foreclosure** has been **≈20–25% of the loan balance** (7–32% range, six 2026 resolutions), because it lends at roughly half of cost.

**The leg not yet observed is the exit:** OZK holds **$416.0M of RESG OREO** at 80–100% of 2025–26 as-is appraisals and **has not priced a single sale**. If those buildings sell 10–30% below carrying, the all-in loss on the original loans becomes **≈29–47%**, which lands back on the old 29–40% band. So the April band is **not refuted; it is now split into an observed leg (~22%) and an unobserved one (OREO exit)**, and THESIS invalidation 7 (≥$100M of OREO sold at ≥95% of carrying) is the test that decides it.

## 1. OZK's own losses on 2026 resolutions — lender basis (KB-269)

| Credit | Type | Resolution | Balance before loss | Loss | **Loss % of balance** | Source |
|---|---|---|---|---|---|---|
| Boston 10 Prospect / USQ D2.1 | Life sci | Sale failed → title, Q3-26 | $169.3M | $37.3M c/o | **22.0%** | Q3 MC p.25 |
| Seattle U District — Chapter I | Office | Foreclosed Jun-26 | $78.4M (DERIVED: OREO $56.1M + c/o) | $22.3M | **28.4%** | Q2 MC; pairing by table order |
| Seattle U District — Chapter II | Life sci | Foreclosed Jun-26 | $52.2M (DERIVED) | $3.7M | **7.1%** | Q2 MC; pairing by table order |
| Atlanta office | Office | Foreclosed Jun-26 | $45.1M (DERIVED) | $8.5M | **18.8%** | Q2 MC |
| Santa Monica 1650 Euclid | Office, 15% leased | Foreclosed Mar-26; OREO marked down Q2–Q3 | $50.1M | $9.3M cumulative (c/o + OREO write-downs to $40.8M) | **18.6%** | KB-192; Q3 MC p.25 |
| Sullivan / 40 Thorndike | Office, vacant | $72.4M c/o Q4-25; recapitalized → pass Q2-26 | $228.8M (DERIVED: $156.4M carrying + c/o) | $72.4M | **31.6%** (24.0% of the $302M commitment) | Q4-25/Q1-26 MC; ⚠️ Boston Globe 7/17 has the buyer assuming ~$232M of debt for $1 — **does not reconcile** with OZK's $156.4M carrying; unresolved |
| **Pooled, six** | | | **$623.9M** | **$153.5M** | **24.6%** (20.5% without Sullivan) | DERIVED |

**Resolved with no or little loss (not pooled):** Pacific Center loan sold at par (Q4-25) · The Jack recapitalized → pass (Q3) · Wauwatosa hotel paid off from a sale (Q3) · San Carlos life sci paid off with a $14.8M c/o (Q2; balance not in hand) · Lincoln Yards land sold $84M vs $126M (−33% vs basis) with "substantially no gain or loss" against carrying (Sep-25).

⚠️ **What these numbers are:** losses at the moment of transfer or recap, against appraisals 80–100% of as-is. They exclude any loss on eventual OREO sale.

## 2. Market evidence, 2026 transactions — property basis (KB-268)

| Type / metro | n | Range vs prior sale | Lender-basis reading | Note |
|---|---|---|---|---|
| Lab, Cambridge (1 Hampshire condos, deed 8/24) | 1 | **−62.5%** vs 2022 | — | Condo units; prior basis may cover more than these units |
| Office, Boston (100 Summer, 72% leased, auction 10/27) | 1 | **−67.7%** vs 2019 | **−44.7%** vs original $470M loan (gross) | Occupied tower; sole bidder was the borrower |
| Office, Seattle | 2 | **−54.2%** (U.S. Bank Center, ~6/2) to −84.2% (901 Fifth, prior unverified) | — | Summary-only sourcing |
| Office, Chicago (Jan–Jun 2026) | 8 | **−56% to −90%**, median ≈−75% | — | 1 N Wacker trophy +17% is the non-distress outlier |
| Office, Santa Monica (Clock Tower, receivership, late Sep) | 1 | **−50.9%** vs 2019 | **≈0%** — price $28.5M above ~$27M CMBS debt | Low-leverage loan: equity took the loss |
| Office, Atlanta (101 Marietta, Q2) | 1 | **−28.1%** vs 2015 | — | 54% leased, older basis |
| CMBS conduit liquidations (JPMorgan via CREFC) | YTD Aug-26 | — | **~42%** avg loss, all types (36% in 2025) | Old high-leverage loans: upper-tail reference |
| CMBS office liquidations (Trepp via CREFC, Sep-26) | 6 loans | — | **79.7%** (DERIVED) | Small sample; worst-case reference |
| Failed-bank C&D loans 2008–13 (DEWEY) | — | — | **53%** weighted; 12% → 72% as workout lengthens | Failed banks; overstates going-concern losses |

**Nothing found in 2026:** San Diego lab, Seattle lab, LA stalled land, Atlanta Midtown/Buckhead distress with a priced basis. Baltimore land not swept. **Spur Phase I** (IQHQ → Apollo deed-in-lieu, South San Francisco, $275M loan, reported 9/17 by TRD relaying the SF Business Times) disclosed **no value or loss** — no severity computable (KB-238 stands).

## 3. What it implies for the Q3 book (DERIVED, desk model)

| Bucket (9/30) | Balance | Loss assumption | Loss ahead (pre-tax) |
|---|---|---|---|
| RESG OREO (7 assets) | $416.0M | Exit 10–30% below carrying (the property comps say values are deep; the as-is appraisals already carry much of it) | **$42–125M** |
| Baltimore land (nonaccrual) | $40.0M | Note under sale contract, "net proceeds substantially equal" to balance | ≈$0 |
| Boston land (substandard accrual) | $105.9M | 0–25% (77% as-is LTV, Dec-25) | $0–26M |
| Lake Tahoe (substandard accrual) | $23.6M | 10–30% (97% LTV) | $2–7M |
| **Named RESG problem book** | **$585.5M** | | **≈$44–158M** |
| Special mention, un-itemized | $303M | If all migrated at the observed ~22% | up to ~$67M |

Against Q3 PPNR of $261.4M a quarter and ACL of $621.1M, that is **an earnings drag, not a capital event**, consistent with THESIS v1.7 (🟡 LOW) and with P-OZK-9's Bear path, which assumed $80–130M of OREO marks. Nothing here moves a weight, prediction or threshold.

## 4. Limits

- The Seattle office/life-sci split of the $26.0M Q2 charge-off follows the Q2 roster's table order; the combined 19.9% is firm.
- Several market rows are summary-only (TRD 403s scripted fetches); the sweep file marks each.
- Prior-sale severities measure owner equity plus debt drawdown, not lender loss. Only the lender-basis column is comparable to OZK.
- The OREO exit discount is an assumption until the first OREO sale prices. That print is the most informative single data point for this refresh.
