# Q4 — Is CCC weakness an isolated problem or the leading edge? (LIQUID, lead)

**Asked by:** Will 02:55 ET 9/25, relayed by PROME (`c29e4ca60`; DOCKET L477). **BOND (bond-d3) supplies the dealer and sovereign side** in `AGENTS/BOND/analysis/2026-09-25_Q4_CCC-isolated-vs-leading-edge_BOND-side.md`. **Not yet received when this was committed: a named gap.** I agreed with BOND that the tier figures live here only, so there is one set, not two.
**Data:** FRED ICE BofA OAS, latest-revised, bp; 15-session changes ranked against their own history 2023-10-02..2026-09-23 (KB-LIQ-128 method). Latest obs **9/23**. The 9/24 cells publish ~9/25 16:15 ET and are the first data point for both explanations.
⚠️ **Caveat, stated once:** FRED carries only a rolling ~3 years of ICE history (earliest 2023-09-25). Every percentile and episode count below comes from a calm window with no 2020 or 2022 stress, and n is small (8 complete episodes).

## Today [obs 9/23]

| | IG | BBB | BB | B | CCC | CCC−B | CCC−BB | B−BB |
|---|---|---|---|---|---|---|---|---|
| Level | 77 | 95 | 159 | 278 | 1,093 | 815 | 934 | 119 |
| 15-session change (9/2→9/23) | −4 | −4 | +6 | +2 | **+40** | **+38** | **+34** | −4 |
| Own p90 of that change | +6 | +7 | +19 | +28 | +57 | +45 | +47 | +12 |

**The isolated-CCC state** (CCC 15-session change ≥ its p80 of +38 while B is below its p75 of +9) **first appeared on 8/03 and has held on and off since.** It has now run **37 sessions without B following** (a fresh episode start is counted at 9/04).

## The two explanations side by side

| | **(A) Isolated: deterioration in the weakest borrowers** | **(B) Leading edge of broader credit repricing** |
|---|---|---|
| **Mechanism** | Idiosyncratic and refinancing stress concentrated in CCC: software/AI-disruption names in the CCC bucket (KB-LIQ-066), PC-adjacent borrowers, names near a maturity; the tail reprices default risk, not the cycle | The rate and funding shock (hike 9/16, 10Y 5.11 [9/23], real-yield-led) reaches the weakest borrowers first and then moves up the ladder |
| **Evidence FOR it today** | Three-week isolation: CCC +40 while B +2 · BB +6 · BBB −4 · IG −4. **The rate shock of 8/26→9/16 (2Y +55, 10Y +35) widened nothing above CCC (KB-LIQ-127).** Primary market open: SoftBank ~$11.1B HY priced inside talk with >$20B demand on 9/23. IG 77, near its 2026 low. **The current episode has outlasted every in-sample "B followed" lag** (below) | CCC 1,093 and CCC−BB 934 are 2026 highs [9/23], and CCC−BB is up from 864 [8/18]. **9/23 reached one rung up for one day:** B +7 (90th pct of days), BB +3, on a +15bp real-yield-led 10Y day, the first such day to reach B in this window. Equity side of private credit: APO $120.69 [9/24] under $130; OWL −13.9% (9/04→9/16). Hiking Fed; reserves −$83.6B [9/23] |
| **In-sample record** | Of 8 complete isolated-CCC episodes, **B did NOT follow in 4** (2023-11-02 · 2024-04-30 · 2025-06-04 · 2026-08-03) | **B followed to its p90 within 30 sessions in 4 of 8** (2024-01-08 → 1/17 · 2024-08-20 → 9/06 · 2025-11-12 → 11/14 · 2026-03-04 → 3/09). **Every follow came within 2–13 sessions of the episode start** |

## Dated discriminators

| # | Observable | Under (A) | Under (B) | By when |
|---|---|---|---|---|
| **D1 (decisive)** | **B 15-session change ≥ +28bp (its p90) on 3 consecutive obs with CCC still widening** (the Q2 test, `LIQ-07`) | Does not happen | Happens. **And BB ≥ +19, BBB ≥ +7, IG ≥ +6 move the same day or within days:** in-sample, 6 of 7 B triggers found BB/BBB/IG already at their p90 | **Every in-sample follow came within 13 sessions of the episode start.** Counted from the 9/04 re-start, that point was ≈9/23 and has passed; counted from 8/03, it passed in August. The 30-session episode window from 9/04 closes ≈10/16. **Registered resolution 11/6** (`LIQ-07` window) |
| D2 | **Which stronger tier moves next** | None beyond noise: B stays under its p75 (+9) on the 15-session change | **B and BB together**, not B alone. B led BB only once in-sample (2026-02-12, by 16 days) | Same as D1 |
| D3 | **CCC−B gap** | Keeps widening or holds (15-session change ≥ 0) while B is flat | **Not a reliable separator in this sample.** 30 sessions after the episode start it moved +10 / −157 / −1 / +2 in the followed cases and −23 / +17 / −46 / +69 in the not-followed ones, so it overlaps completely | Read it; do not decide on it |
| D4 | **CCC−BB and B−BB gaps** | CCC−BB widens ≈ one-for-one with CCC−B; B−BB flat | **Also not a separator.** B−BB changed −12 / +3 / −9 / −17 over 30 sessions even when B followed, because BB widened with B | Read it; do not decide on it |
| D5 | **Funding and dealers** | Overnight rates quiet (z < 4); dealer inventory unchanged | Under (B) with a feedback loop: sofr-dispersion z ≥ 4 off-calendar, 079 ARM, or SRF ≥ $50B (the `LIQ-07` S1 legs). **BOND carries dealer inventory and the sovereign driver: GAP until BOND's file lands** | Q3-end persistence verdict **10/8** (KB-LIQ-136) · `LIQ-07` to 11/6 |

**Plain reading:** only D1 separates the two explanations in this data. The gap paths (D3, D4) look like discriminators but did not separate the cases that followed from the ones that did not. Under (B), the next move is not a gentle climb one tier at a time. It has been B, BB, BBB and IG crossing their own 90th percentiles within days of each other.

## Where the weight sits today

**Leaning (A), isolated, at roughly 70/30.** The same prior is registered on `LIQ-07` (P(S4 CONTAINED) = 70%). Three reasons:
1. The isolation is measured, not assumed: three weeks of CCC +40 against IG/BBB −4.
2. In-sample, a follow-through came within 13 sessions or not at all, and the current episode is at 37 sessions from its 8/03 start.
3. The primary market is open to a record-size HY deal.

**What keeps (B) alive:** the 9/23 one-day reach into B on a rate-shock day, the 2026-high tail, and a hiking Fed. **The first data point is the 9/24 cells at ~16:15 ET today**, graded on the 9/25 rule (report `2026-09-25_credit-transmission-persistence.md` §1c).

## Issuance and refinancing data on the fleet

**No public-HY CCC maturity-wall or issuance series exists on the fleet.** The nearest are:
- BROCK's private-credit and BDC walls: KB-BRK-007 "$162B maturity wall due 2026" and KB-BRK-114 "BDC unsecured maturing 2026 $12.7B (+73% vs 2025)". Both are **dated March 2026, six months stale, and a different market** (private credit / BDC, not public CCC).
- REGINALD's $875B 2026 wall is all-CRE (MBA), fenced as not CMBS-only. It is not HY.
- The only live issuance datum is the SoftBank deal (primary open).

**This is a gap: (A)'s refinancing-wall mechanism is ASSUMED, not measured.**
