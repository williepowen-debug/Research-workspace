# BOND Monitor — Credit Primary Market Function

**Owner:** BOND
**Last Updated:** 2026-07-01 by BOND
**Purpose:** Track whether HY/IG borrowers can access public debt markets, and when market access closes enough to transmit stress to banks/equities.

## Core Thresholds

| Metric | Green | Yellow | Red | Why it matters |
|---|---:|---:|---:|---|
| HY OAS | <300 | 300-350 | >350 | >350 = issuance freeze / refinancing wall pressure |
| HY weekly issuance | Normal / strong | Below seasonal avg | <$3B for 2 weeks or <50% YoY | Access closure |
| IG OAS weekly move | stable | +10bps/wk | +20bps/wk | IG repricing / broad funding stress |
| Pulled deals | isolated | multiple lower-quality | blue-chip or clustered HY pulls | Primary market dysfunction |

## Current Read

**🟢 Primary market in BOOM, not freeze — Apr–Jun ran the mechanism in reverse (resolves BND-02 FAILED).** April HY priced **$40B** (2nd-highest month since 2021, pricings on 68% of business days; LCD/PitchBook via Wayback), May opened at a "heady pace," late June ran ~$7B in a single week, and June IG set a **record ~$175–187B** (Nvidia $25B upsized on $85B orders; SpaceX debut $89B books). Zero pulled deals found 6/20–7/1. The AI-capex borrowing wave is the driver. Residual watch: CCC OAS (970) widened into the 6/24–26 equity risk-off and did **not** retrace while headline HY did (283→275) — the PIMCO default-cycle bifurcation lives in the tail, not in market access. SIFMA YTD-through-May: $1,226.8B combined IG+HY (monthly split gated).

## Rolling Table

| Week / Date | HY OAS | IG OAS | HY / Corporate issuance | Pulled/repriced deals | Read | Source |
|---|---:|---:|---:|---|---|---|
| 2026-03-26 | 319bps | ~87bps | Janus Henderson pulled / loan deal pulled | Multiple stress anecdotes | 🟠 activating then | BOND Mar seed / FT |
| 2026-05-08 | 281bps | 79bps | Corp issuance $1,013.9B through Apr, +28.2% YoY | No broad freeze confirmed | 🟢 functional | FRED / SIFMA search result May 2026 |
| 2026-06-30 | 275bps (283 peak 6/26) | 76bps | Apr HY $40B; June IG record ~$175-187B; late-June HY ~$7B/wk | **None found 6/20–7/1** | 🟢 **boom** | FRED + LCD-via-Wayback + KB-BND-063 |

## Cross-Agent Use

- Signal **REGINALD** when public issuance freeze means banks may need to absorb refinancing demand.
- Signal **HENRY/VIOLET** when credit widening leads equity/vol complacency.
- Signal **BROCK** when public credit either confirms or contradicts private-credit stress.

## Next Data Need

Weekly HY/IG split, not just aggregate corporate issuance. Current SIFMA headline is enough to reject “broad freeze,” but not enough to classify HY-only issuance quality.
