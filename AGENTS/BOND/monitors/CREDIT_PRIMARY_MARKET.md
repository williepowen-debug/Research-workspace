# BOND Monitor — Credit Primary Market Function

**Owner:** BOND
**Last Updated:** 2026-08-21 by BOND — **full refresh; the whole table now sits on ONE date (8/20).** ⚠️ **What this fixes is not just staleness — it is a PARTIAL refresh, the defect this desk logged on 8/20 and then shipped again here: HY and IG were carried at **8/14** while CCC had been advanced to **8/19**, and the derived distances (33bp / 83bp) were computed off the older leg. Refresh the SET, and recompute every distance that hangs off it.** ★ **CCC printed a FRESH 2026 HIGH on 8/20.** *(Prior: 2026-08-18 staleness sweep.)* *(Prior: 2026-07-28, itself 27 days stale — the +11bp two-session HY widening landed while this file read "boom, 275, flat".)*
**Purpose:** Track whether HY/IG borrowers can access public debt markets, and when market access closes enough to transmit stress to banks/equities.

## Current Read — 2026-08-21 (all credit levels 8/20, one date, cache-busted)

| Metric | Level | Date | vs threshold |
|---|--:|---|---|
| **HY OAS** | **275bp** | FRED 8/20 | **25bp** below the 300 watch · **75bp** below the 350 freeze line *(read 33/83bp off a stale 8/14 level until today)* |
| **CCC OAS** | **1035bp** | FRED 8/20 | ★ **FRESH 2026 HIGH** — takes out 1034 (7/31). **65bp** below the 1100 escalation. ⚠️ **NOT a series high** — series max **1137 (2025-04-07)**, and **16 prior obs ≥1035 in FOUR SEPARATE EPISODES across three years — 12 in Apr-2025 (4/4–4/22), 2 in Oct-2023 (10/30–31), 1 on 2023-11-01, 1 on 2024-08-05** (`BAMLH0A3HYC` · session closes · 2023-08-22→2026-08-20 · n=787, computed at write time). |
| **IG OAS** | **82bp** | FRED 8/20 | flat; band 79–82 across the whole episode ⇒ **+3bp in four weeks** against a +20bp/wk trigger. No threshold near. |
| **CCC/HY ratio** | **3.76x** | FRED 8/20 | the tail is widening *relative* to the index, not just absolutely |
| **Pulled deals** | **ZERO** | 8/21 | the access test — unimpaired |
| IG primary volume | **~$56B in the week to 8/14** | WALTER `-005`, **wire-level, NOT pulled at primary** | absorbed with no spread disruption |

**Verdict: PRIMARY MARKET ACCESS IS FULLY OPEN, AND THE TAIL IS WIDENING UNDERNEATH IT.** Those are both true and they are not in tension: **the index is inert, IG is flat in a 3bp band, there are zero pulled deals — and the worst credits are repricing.** That is a *quality-tail* event, not a *market-function* event. **The freeze thesis (HY 350) is 75bp away and no closer than three weeks ago; the escalation that IS live is CCC 1100, 65bp away.** ⚠️ **The expression implied, if it ever arms, is single-name/CCC — not HYG, whose index level has round-tripped the entire July widening.**

> ## ⚠️ THE HONEST ENTRY: this desk has made and retired a credit call TWICE in three weeks
>
> | Date | Call | What happened |
> |---|---|---|
> | 7/28 | *"Credit is no longer inert"* — HY +11bp in two sessions, quality-**indiscriminate** | HY ran on to a 287 cycle high (7/29) |
> | 8/15 | *"Credit INVERTED — quality-**discriminating***" — HY retraced to 271 while CCC broke 1000 → 1024 and made new highs | **The index kept tightening to 267 and CCC gave back to 1012** |
> | **8/18** | **Neither call survives at the index level.** HY is **below** where the July episode began; CCC is **off** its high | — |
>
> **What is left is narrow and worth stating precisely:** the **CCC/HY ratio** did make a fresh high at **3.79x** — but **it did so because HY fell faster, not because CCC rose.** A ratio extreme driven by the denominator is not the same claim as a widening quality tail, and this monitor should not report it as one.
>
> **⇒ Credit is not currently a BOND signal.** Saying that plainly is worth more than a third rewrite. **`VX-BND-11` is held at 3 — neither re-raised nor reverted** — and the registered conditions (→1 needs CCC <1000 **AND** HY <280 for 5 consecutive sessions; the HY leg is met, the **CCC leg is not**) will decide it rather than a judgement call.
>
> ⚠️ **`finding_plausible_stale_value_evades_review` applies to the pattern, not just to a value:** each of these three calls was *plausible when written*. The defect is not that any one was wrong — it is that a monthly-to-weekly instrument (index OAS) was being read at a two-session cadence. **Round-trips at that frequency are noise, and the desk has now paid for that lesson twice.** *(Same family as the ACM-monthly-vs-weekly-window defect found today: `finding_instrument_cadence_cannot_resolve_the_claims_window`.)*


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

⚠️ **Vintage discipline:** FRED OAS publishes with a lag of ~1 business day — **never infer a level for a date the series has not printed.** ⚠️ **Corrected 2026-08-20: this line named a SPECIFIC frozen date ("7/24 is the freshest confirmed print; no 7/27 exists yet") and was 25 days stale — it would have told a reader the freshest available credit print was 7/24 when 8/18 was published.** **A vintage rule must state the RULE, not a date. The current freshest print is recomputed every boot by `monitors/boot_recompute.py`; read it there, never here.**

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
