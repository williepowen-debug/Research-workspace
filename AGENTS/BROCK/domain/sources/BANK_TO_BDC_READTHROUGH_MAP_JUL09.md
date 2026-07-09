# Bank→BDC Read-Through Map — Packet B (PROME 7/5, deliver-by 7/14)
**Author:** BROCK · **Written:** 2026-07-09 ~17:00 ET · **Status:** BROCK-owned frame BUILT; CARL (consumer) + REGINALD (bank-side) rows PENDING their inputs — refine same-day banks print 7/14, before 7/25-28 ARCC/BDC window.

## Purpose
Bank prints are transparent (mark-to-market); BDC marks are opaque (mark-to-model) and lag ~2 weeks (7/14 banks → 7/25-28 BDC 10-Qs). This map lets BROCK move the BDC-mark prior the *same day* banks report, not wait for 7/28.

## Leading-indicator table (confidence = how tightly the bank line-item predicts BDC-mark direction)

| Bank line-item (7/14-16 print) | Predicts (BDC mark, 7/25-28) | Direction logic | Confidence | Owner |
|---|---|---|---|---|
| Reserve-build **direction** (build vs release), JPM/WFC/C | BDC non-accrual trend (NA up if banks build) | Banks build reserves ahead of realized loss → same credit-cycle information banks see in shared borrowers (sponsor-backed loans, NDFI counterparties) should show up as BDC NA additions 1-2Q later | 🟠 MED — correlated but banks are diversified/first-lien-heavy vs BDC unitranche/2nd-lien; directional not magnitude-transferable | BROCK |
| **NDFI/"lending to non-banks" exposure + commentary** (the closest bank proxy for PC stress) | BDC funding-cost / warehouse-line utilization (liability side) | If banks tighten NDFI underwriting or flag utilization spikes → BDC funding costs rise, forced asset sales more likely → NAV pressure | 🔴 HIGH — most direct read-through; this is literally banks pricing BDC-adjacent credit risk | BROCK (cross-ref REGINALD CRE score) |
| **CRE/C&I credit-cost trajectory + criticized-loan migration** | BDC CRE-adjacent / sponsor-backed portfolio marks (indirect — many BDC borrowers are also bank C&I counterparties) | Rising criticized-loan migration at banks = same-vintage sponsor-backed credits deteriorating → expect matching NA additions at BDCs holding 2nd-lien/unitranche behind bank facilities | 🟡 LOW-MED — CRE is REGINALD's book, not BROCK's; the read-through is via shared-sponsor names, not direct overlap | REGINALD (PENDING input) |
| **Guidance language on "credit normalization"** | Narrative-phase tell (Stage 2→3 confirmation), not a hard number | Soft/hedged language ("normalizing from historically low levels") = benign-base-rate read; explicit "deterioration accelerating" language = hardens the BDC-mark bear case same-day | 🟡 LOW — qualitative, narrative-only | BROCK |
| **SYF/ALLY/COF card NCO/DQ/ACL** (CARL's consumer axis, prints 7/21-22 not 7/14) | BDC **consumer-exposure** marks (Blue Owl/KKR PC-into-BNPL axis, SIG-702-015 — a BROCK watch, not yet a convergence vote) | Rising consumer NCO/DQ = the demand-side confirmation for the PC-into-BNPL migration thesis; direct read-through to any BDC/interval-fund holding consumer paper (Stone Ridge $2-FV exemplar) | 🟠 MED, PENDING CARL's actual thresholds | CARL (PENDING input) |

## Concrete proof-of-concept already in hand (7/6 OZK/Affinius finding)
OZK (regional bank) → Affinius (private-credit/CRE manager) co-lending is now **named and asset-level confirmed** (KB-BRK-174, below): $95M assigned piece of a $118M Square Mile/Affinius construction note (777 Industrial), as-market underwater; plus a ~$100M Affinius junior under OZK's $279.75M Southline senior. This is a live instance of the bank→PC-manager transmission surface this map is trying to generalize — **OZK's own 7/21 Q2 print (MID_JULY_NODE Knot 2 super-cluster) is itself a leading tell for Affinius-adjacent PC stress ahead of the Oct-2026 $2.7B Affinius bond maturity.** Watch OZK's 7/21 commentary on this specific relationship as the cleanest single-name test of the "bank criticized-loan migration → PC-manager stress" row above.

## What's still needed by 7/14
- CARL: SYF/ALLY/COF specific NCO/DQ/ACL thresholds + which BDC consumer-exposure names to map them to.
- REGINALD: bank-side reserve-build magnitude + CRE/C&I criticized-loan migration line-items from the actual 7/14-16 prints (this table is pre-load logic only, no bank data has printed yet).
- BROCK (this session): frame delivered; will overlay real 7/14 bank-print data into this table same-day, synthesize into a single "if banks showed X → BDC read is Y" verdict for PROME before the 7/25-28 window.

**Confidence discipline:** this is a leading-indicator hypothesis map, not a backtested model — no historical bank-print→BDC-mark correlation has been computed. Treat confidence tags as priors to be updated once 7/14 data lands, not settled facts.
