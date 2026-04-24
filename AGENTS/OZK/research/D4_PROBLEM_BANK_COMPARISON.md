# D4: Problem Bank Comparison — OZK vs Industry & Problem Bank Metrics

**Created:** 2026-03-24
**Sources:** FDIC QBP Q4 2025, FDIC API (CERT 110), FFIEC Call Report Q4 2025
**Status:** COMPLETE

---

## The Question

OZK is NOT on the FDIC's 60-bank Problem Bank List (CAMELS 4 or 5). But how do its metrics compare to industry averages and to the thresholds that typically trigger supervisory attention?

---

## OZK vs Industry — Side by Side

| Metric | OZK (Q4 2025) | Industry Avg | Community Bank Avg | OZK vs Industry |
|--------|:-------------:|:------------:|:------------------:|:---------------:|
| **NCO rate (FY)** | **1.18%** | 0.63% | ~0.45% | **1.9x industry** |
| **Noncurrent rate** | **1.07%** | 0.96% | ~0.85% | 1.1x |
| **PDNA rate** | **~1.6%** | 1.56% | ~1.4% | ~1.0x |
| **Reserve coverage (ACL/noncurrent)** | **139%** | 171.2% | 154.3% | **Below both** |
| **CRE concentration / Tier 1** | **358%** (reported) | ~150-200% | ~250% | **1.8-2.4x** |
| **ROA** | **1.71%** | 1.20% | 1.32% | ✅ Strong |
| **NIM** | **4.62%** | 3.39% | 3.77% | ✅ Strong |
| **CET1** | **11.70%** | ~13% | ~14% | Below avg |

---

## The Paradox: Strong Earnings, Weak Credit Quality

OZK's earnings metrics (ROA, NIM) are **best-in-class**. This is why the stock trades at ~$43 and not $30. The market is pricing the earnings power, not the credit deterioration.

But look at the credit metrics:
- **NCO rate 1.9x industry** — OZK is charging off loans at nearly twice the pace
- **Reserve coverage 139% vs industry 171%** — OZK has *less* cushion despite *more* stress
- **CRE concentration 2x+ industry** — the source of the stress is outsized

This is the classic "earn-your-way-through" gamble: OZK generates enough income to absorb losses quarter by quarter, hoping the CRE cycle turns before cumulative losses overwhelm the buffer. It works until it doesn't.

---

## FDIC Problem Bank Thresholds

The FDIC doesn't publish exact cutoffs, but CAMELS downgrades to 4-5 typically involve combinations of:

| Factor | Typical Problem Bank Profile | OZK Q4 2025 | OZK Status |
|--------|:---------------------------:|:-----------:|:----------:|
| Capital adequacy | CET1 <8% or declining fast | 11.70% | ✅ Clear |
| Asset quality (NCO) | >1.5% sustained | 1.18% FY | 🟡 Approaching |
| Asset quality (noncurrent) | >2.5% | 1.07% | ✅ Clear |
| Management | Regulatory actions, MRAs | None public | ✅ Clear |
| Earnings | ROA <0.5% or negative | 1.71% | ✅ Clear |
| Liquidity | FHLB draws >50% of capacity | 0% drawn | ✅ Clear |
| Sensitivity (CRE conc.) | >300% + deteriorating | **358%+ and deteriorating** | 🔴 **Exceeds** |
| Reserve coverage | <100% | 139% | 🟡 Declining fast |

**OZK clears most problem-bank thresholds** — capital and earnings protect it. But it's deteriorating on the dimensions that matter for CRE-concentrated banks: charge-offs approaching elevated territory, reserves declining into stress, and concentration far above guidance.

---

## The CRE Concentration Outlier

FDIC/OCC Joint Guidance (2006, still active) flags banks with:
- CRE / Total Capital > **300%**
- Construction / Total Capital > **100%**

OZK exceeds both:
- CRE / Tier 1: **358%** (reported), **405-420%** (adjusted per D3)
- Construction / Tier 1: estimated **~140%** ($7.8B / $5.5B)

Banks exceeding these thresholds receive "enhanced supervisory scrutiny" — more frequent exams, deeper loan review, potential MRAs (Matters Requiring Attention). OZK almost certainly receives this scrutiny already. The question is whether Q1-Q2 2026 credit migration triggers a formal downgrade.

---

## What Triggers a CAMELS Downgrade?

For OZK to land on the Problem Bank List, you'd need:

| Trigger | Probability | Timeline |
|---------|:-----------:|:--------:|
| NCO rate sustains >1.5% for 2+ quarters | 30% | Q2-Q3 2026 |
| Noncurrent breaches 2.0% | 25% | Q2-Q3 2026 |
| Reserve coverage drops below 100% | 20% | Q3-Q4 2026 |
| FHLB draws begin (liquidity signal) | 10% | Event-driven |
| Formal MRA or consent order | 15% | 6-12 months |

**Combined probability of Problem Bank List within 12 months: ~15-20%**

Not the base case, but not negligible. And the *threat* of downgrade matters more than the actual listing — analysts and sophisticated depositors monitor CAMELS proxies.

---

## The Framing: "Worse Than Problem Banks on the Metrics That Matter"

OZK isn't a problem bank. But:

> OZK's NCO rate (1.18%) is nearly double the industry average (0.63%). Its reserve coverage ratio (139%) is below both the industry average (171%) and the community bank average (154%). Its CRE concentration (358-420%) is 2-3x the regulatory guidance threshold. On the two dimensions most predictive of CRE credit events — concentration and loss trajectory — OZK's metrics are worse than many banks already receiving enhanced supervisory attention. Strong earnings (ROA 1.71%) and capital (CET1 11.70%) are masking credit deterioration that, in a less profitable institution, would already have triggered regulatory action.

---

## The "Earn Your Way Through" Break Point

OZK's pre-provision net revenue (PPNR) = ~$1.0B/year. This is the annual earnings engine before credit costs.

| NCO Rate | Annual NCOs | PPNR Coverage | Result |
|:--------:|:----------:|:-------------:|--------|
| 1.18% (current) | ~$380M | 2.6x | Comfortable — earnings absorb losses |
| 1.50% | ~$485M | 2.1x | Tight but viable |
| 2.00% | ~$645M | 1.6x | EPS compresses to ~$3.00-3.50 |
| 2.50% | ~$805M | 1.2x | Near breakeven — dividend at risk |
| 3.00% | ~$970M | 1.0x | **Breakeven** — all earnings consumed by losses |

NCO rate must nearly **triple** from current levels to zero out earnings. That's the bull argument. The bear argument: the LTV reappraisal data (D1) and maturity wall suggest the path to 2.0-2.5% NCO is shorter than it looks.

---

## Cross-References
- FDIC QBP Q4 2025: `sources/FDIC_QBP_Q4_2025.md`
- D1 LTV Extrapolation: `research/D1_LTV_EXTRAPOLATION.md`
- D3 Shadow CRE Lever: `research/D3_SHADOW_CRE_LEVER.md`
- C3 Capital Absorption: `research/C3_CAPITAL_ABSORPTION_ANALYSIS.md`
- EVIDENCE.md: Credit quality tables
