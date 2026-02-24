# Google Trends Analysis — Canadian Florida Search Intent

**Data Pulled:** 2026-02-24 00:35 UTC
**Source:** Google Trends (5-year view, Canada)
**Analyst:** Will + Prome

---

## Raw Data Files

- `google_trends_flights_to_florida_canada_5yr.csv`
- `google_trends_florida_travel_canada_5yr.csv`

---

## Key Finding: Boycott Impact Visible, Partial Recovery

### "Flights to Florida" (Canada)

| Period | Index (Feb avg) | vs 2024 | Notes |
|--------|-----------------|---------|-------|
| Feb 2023 | 82.5 | +11% | Post-COVID peak |
| Feb 2024 | 74 | baseline | Pre-boycott |
| **Feb 2025** | **51** | **-31%** | **Boycott trough** |
| Feb 2026 | 63 | -15% | Partial recovery |

**YoY Change:**
- 2024 → 2025: **-31%** (boycott hit)
- 2025 → 2026: **+24%** (partial recovery)
- 2024 → 2026: **-15%** (still impaired)

### "Florida" (Travel category, Canada)

| Period | Index (Feb avg) | vs 2024 | Notes |
|--------|-----------------|---------|-------|
| Feb 2023 | 76 | +7% | Healthy |
| Feb 2024 | 71 | baseline | Pre-boycott |
| **Feb 2025** | **52** | **-27%** | **Boycott trough** |
| Feb 2026 | 54 | **-24%** | Minimal recovery |

**YoY Change:**
- 2024 → 2025: **-27%** (boycott hit)
- 2025 → 2026: **+5%** (barely recovering)
- 2024 → 2026: **-24%** (still heavily impaired)

---

## Interpretation

### The Pattern
1. **Jan 2023 = Peak** — Post-COVID travel surge
2. **Feb 2024 = Healthy baseline** — Normal snowbird season
3. **Feb 2025 = Boycott trough** — Sharp collapse (-27% to -31%)
4. **Feb 2026 = Partial recovery** — Intent returning but still impaired

### Divergence Signal
| Metric | Flights | Florida (general) |
|--------|---------|-------------------|
| Recovery (2025→2026) | +24% | +5% |
| Still below 2024 | -15% | -24% |

**Insight:** Flight searches recovering faster than general "Florida" interest.

**What this means:**
- Some Canadians ARE booking flights (transactional intent up)
- But broader tourism interest (research, planning) remains suppressed
- **Brand damage** — Florida as a destination is less appealing
- Those who go are committed; casual interest collapsed

---

## Thesis Validation

| Vector | Prior Estimate | Actual (Google Trends) | Status |
|--------|---------------|------------------------|--------|
| VX-MARCO-CTI-01 | 0.72 | Consistent (Feb 2026 still -15% to -24% below baseline) | ✅ VALIDATED |
| VX-MARCO-GTR-01 | Pending | Now populated | ✅ BASELINED |

**CTI Correlation:** Google Trends shows -15% to -24% decline in search intent, which aligns with Visit Florida's -14.7% actual visitor decline. **Leading indicator confirmed.**

---

## Next Steps

1. Update VX-MARCO-GTR-01 with actual values
2. Track monthly — is Feb 2026 recovery continuing or stalling?
3. Compare Mar 2026 vs Mar 2025 (was -31% in flights)
4. Watch for divergence narrowing (flights vs general interest)

---

**Filed:** VX-MARCO-GTR-01, VX-MARCO-CTI-01
