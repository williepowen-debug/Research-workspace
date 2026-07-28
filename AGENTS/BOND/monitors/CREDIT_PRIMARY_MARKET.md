# BOND Monitor — Credit Primary Market Function

**Owner:** BOND
**Last Updated:** 2026-07-28 by BOND *(27 days stale — the +11bp two-session HY widening landed while this file read "boom, 275, flat")*
**Purpose:** Track whether HY/IG borrowers can access public debt markets, and when market access closes enough to transmit stress to banks/equities.

## Core Thresholds

| Metric | Green | Yellow | Red | Why it matters |
|---|---:|---:|---:|---|
| HY OAS | <300 | 300-350 | >350 | >350 = issuance freeze / refinancing wall pressure |
| HY weekly issuance | Normal / strong | Below seasonal avg | <$3B for 2 weeks or <50% YoY | Access closure |
| IG OAS weekly move | stable | +10bps/wk | +20bps/wk | IG repricing / broad funding stress |
| Pulled deals | isolated | multiple lower-quality | blue-chip or clustered HY pulls | Primary market dysfunction |

## Current Read (7/28) — **ACCESS intact, but "credit is inert" is RETIRED**

**🟡 The primary market is still open — but spreads have re-activated after a month flat, and this file carried the flat read for 26 days.** HY OAS **268 [7/22] → 277 [7/23] → 279 [7/24] = +11bp in two sessions**, out of a nine-session range (7/10–7/22) that never moved more than 5bp. CCC **996** (4bp from 1000), IG **80**.

**The discriminator that matters: the widening is quality-INDISCRIMINATE.** All four series moved near-identically in absolute terms — **BB 157→168 (+11) · single-B 285→296 (+11) · CCC 981→996 (+15) · index 268→279 (+11)** — and *proportionally* the move is **largest at the TOP of the stack** (BB +7.0% > single-B +3.9% > CCC +1.5%). A credit-discriminating selloff does the opposite. **⇒ Read this as a broad repricing (rates/FOMC positioning/duration), NOT as a default-cycle or market-access signal.** Live alternatives for the same move: the 30Y's run above 5% and FOMC positioning.

**Market ACCESS is unimpaired:** zero pulled deals, primary open, HY still 21bp below the 300 watch and 71bp below the 350 freeze line. **BND-02 stays FAILED** — the freeze mechanism is not running.

⚠️ **Vintage discipline:** FRED OAS publishes with a lag — **7/24 is the freshest confirmed print; no 7/27 exists yet.** Do not infer a 7/27-28 level.

---

### Prior read (7/01, superseded — retained for the issuance record)

**🟢 Primary market in BOOM, not freeze — Apr–Jun ran the mechanism in reverse (resolves BND-02 FAILED).** April HY priced **$40B** (2nd-highest month since 2021, pricings on 68% of business days; LCD/PitchBook via Wayback), May opened at a "heady pace," late June ran ~$7B in a single week, and June IG set a **record ~$175–187B** (Nvidia $25B upsized on $85B orders; SpaceX debut $89B books). Zero pulled deals found 6/20–7/1. The AI-capex borrowing wave is the driver. Residual watch: CCC OAS (970) widened into the 6/24–26 equity risk-off and did **not** retrace while headline HY did (283→275) — the PIMCO default-cycle bifurcation lives in the tail, not in market access. SIFMA YTD-through-May: $1,226.8B combined IG+HY (monthly split gated).

## Rolling Table

| Week / Date | HY OAS | IG OAS | HY / Corporate issuance | Pulled/repriced deals | Read | Source |
|---|---:|---:|---:|---|---|---|
| 2026-03-26 | 319bps | ~87bps | Janus Henderson pulled / loan deal pulled | Multiple stress anecdotes | 🟠 activating then | BOND Mar seed / FT |
| 2026-05-08 | 281bps | 79bps | Corp issuance $1,013.9B through Apr, +28.2% YoY | No broad freeze confirmed | 🟢 functional | FRED / SIFMA search result May 2026 |
| 2026-06-30 | 275bps (283 peak 6/26) | 76bps | Apr HY $40B; June IG record ~$175-187B; late-June HY ~$7B/wk | **None found 6/20–7/1** | 🟢 **boom** | FRED + LCD-via-Wayback + KB-BND-063 |
| 2026-07-10→22 | **268–273, range-bound** | 78 | (not re-pulled) | None reported | 🟢 flat | FRED direct (back-filled 7/28) — *nine sessions, never >5bp of movement* |
| **2026-07-24** | **279bps** | **80bps** | Not re-pulled; **GS + JPM each launched 18-name AI-credit baskets 7/23 @ ~319bp avg** | **None reported** | 🟡 **widening, quality-indiscriminate** | FRED direct + WALTER SIG-W-20260727-016 / -018 (KB-BND-090/093) |

## Cross-Agent Use

- Signal **REGINALD** when public issuance freeze means banks may need to absorb refinancing demand.
- Signal **HENRY/VIOLET** when credit widening leads equity/vol complacency.
- Signal **BROCK** when public credit either confirms or contradicts private-credit stress.

## Next Data Need

Weekly HY/IG split, not just aggregate corporate issuance. Current SIFMA headline is enough to reject “broad freeze,” but not enough to classify HY-only issuance quality.
