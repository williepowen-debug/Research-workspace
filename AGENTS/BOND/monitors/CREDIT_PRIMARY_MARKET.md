# BOND Monitor — Credit Primary Market Function

**Owner:** BOND
**Last Updated:** **2026-09-28 14:43 ET by BOND — pulled-deal/access row refreshed (`KB-BND-346`); levels unchanged from** **2026-09-28 13:14 ET by BOND — levels refreshed to the 9/25 close (FRED, cache-busted 9/28, one date); the 9/17 read below is SUPERSEDED (its "15bp from the 1100 escalation" line became false on 9/24).** · *prior:* **2026-09-17 ~10:0x ET by BOND — full refresh to the 9/15 close, whole table on ONE date, all levels cache-busted at write time.** 🔴 **AND THIS FILE JUST REPEATED ITS OWN RECORDED DEFECT, 21 DAYS THIS TIME INSTEAD OF FOUR — n+1 on the class named in the paragraph below, found again by an audit (Will-requested stale sweep) and again by no instrument.** `boot_recompute` and `closeout_check` both returned clean on this directory today, correctly: the numbers were internally consistent *with each other*, and neither check has a shape for *"this whole surface is three weeks behind its siblings."* **The fix that would actually bite is an age check on boot-unread surfaces, not another resolution to remember.** *(Prior header, 2026-08-27 ~12:2x ET, retained:)* **full refresh to the 8/26 close; the whole table sits on ONE date.** 🔴 **Found by a Will-directed inward audit, not by any instrument: this file sat on the 8/20 vintage for FOUR sessions while `STATUS` and `VX.tsv` were refreshed twice each.** ⚠️ **The reason is structural and worth naming — `monitors/` is NOT read at boot.** `boot_recompute` scans this directory for numeric drift and **passed clean**, because a drift check compares latest-on-surface to latest-at-source and this file's numbers were internally consistent *with each other*; it has no shape for *"this whole surface is four days behind its siblings."* **The boot-unread tier is where staleness lives, and the instruments confirm it is clean.**

## Current Read — 2026-09-28 13:14 ET (all credit levels **9/25**, one date, FRED cache-busted; `KB-BND-341/343`)

| Metric | Level | Date | vs threshold |
|---|--:|---|---|
| **HY OAS** | **293bp** | FRED **9/25** | **7bp** below the 300 watch · 57bp below the 350 freeze. **+25bp in 3 sessions** (268 [9/22] → 273 → 280 → 293) — a 3-session change met or beaten in 23 of 782 windows (2.9%). 2026 max 346 [3/30] |
| **CCC OAS** | **1128bp** | FRED **9/25** | 🔴 **1100 escalation FIRED 9/24 (1112, first-published)** ⇒ `BND-27` FALSE. 2026 high; 9bp under span max 1137 [2025-04-07] |
| **B OAS** | **300bp** | FRED **9/25** | +29bp in 3 sessions (271 → 300); 15-session Δ +23 (crossed its +9 p75 on 9/24) — the middle of HY joined |
| **BB OAS** | **176bp** | FRED **9/25** | +20bp in 3 sessions (+12.8%, the fastest tier proportionally) |
| **IG OAS · BBB** | **81 · 99bp** | FRED **9/25** | +4bp each in 3 sessions; 15-session Δ 0 — **IG has NOT joined**. 39bp below the 120 trigger |
| **CCC−BB tail gap** | **952bp** | FRED **9/25** | new span max; but CCC/BB RATIO compressed 6.89 → 6.41 — BB/B widened faster in % terms |
| **Pulled deals / access** | **NONE NAMED — search gap, NOT a zero** | web sweep **9/28 ~14:39–14:43 ET** (`KB-BND-346`, C3) | Access shown **OPEN by what priced**: SoftBank **$11.1B** HY 9/23–24 (book >$30B, 8.6–9.75%) · Paramount **~$12.4B** HY launched 9/28, **unpriced** (talk low-9%) = the next access test. Pulled/flexed-deal data (LCD/Debtwire/IFR) paywalled ⇒ the pull leg is **UNVERIFIABLE at free sources** — re-test: an accessible flex table, or Paramount final vs talk/size |

**Verdict: TAIL ESCALATION FIRED AND THE WIDENING SPREAD THROUGH HY IN SPEED (not level); IG untouched; primary access OPEN for large credits at 9–10% yields (SoftBank record deal 9/23–24) — pulled-deal leg unverifiable at free sources, NOT a clean zero (9/28 14:43 ET, `KB-BND-346`).** Formal L477 Q4 grade = LIQUID's. Expression if anything: single-name/CCC, never HYG (`BND-27` rider).

## Prior read — 2026-09-17 (SUPERSEDED 2026-09-28; retained as history)

*(was headed: Current Read — 2026-09-17 ~10:0x ET, levels 9/15)*

| Metric | Level | Date | vs threshold |
|---|--:|---|---|
| **HY OAS** | **276bp** | FRED **9/15** | **24bp** below the 300 watch · **74bp** below the 350 freeze *(both recomputed off 276)*. **+11bp in two sessions** (265 [9/11] → 271 → 276) — the first real travel after a month of 263–276 inertia. 2026 max 346 [3/30] |
| **CCC OAS** | **1085bp** | FRED **9/15** | **15bp** below the 1100 escalation, **closing ~5bp/session** (44 → 30 → 24 → 19 → 15). ★ **FRESH 2026 HIGH — the 2026 max IS the latest print** (1076 → 1081 → 1085), computed at write time. ⚠️ **NOT a series high** — series max **1137 (2025-04-07)**, n=786 |
| **BB OAS** | **161bp** | FRED **9/15** | **+11bp in two sessions** (150 → 156 → 161) — the BB leg widened **WITH** the tail this time |
| **IG OAS** | **80bp** | FRED **9/15** | **flat three consecutive sessions** (80/80/80). 2026 max 94 [3/16]; 40bp below the 120 trigger |
| **CCC−BB tail gap** | **924bp** | FRED **9/15** | span max **926bp [9/11]** (n=786) — **the gap PAUSED 2bp under its high because BB (+11) widened with CCC (+9)**: index and tail moved the SAME way. **Dispersion paused, not reversed** |
| **CCC/HY ratio** | **3.93x** | FRED **9/15** | ⚠️ **unlike the 8/26 read, ratio and levels now agree** — both legs widened, so the ratio's rise is real rather than a compositional artifact |
| **Pulled deals** | **ZERO** | 9/17 | the access test — unimpaired |
| IG primary volume | record-September forecast **~$215B** | Bloomberg poll, **secondary 9/3, NOT pulled at primary** | IG yields >5.5% pulling issuance **FORWARD** (`KB-BND-259`) |

**Verdict: PRIMARY MARKET ACCESS IS FULLY OPEN, AND THE TAIL IS 15bp FROM ITS REGISTERED ESCALATION.** Both true, not in tension: zero pulled deals, IG flat in a 3bp band, issuers *accelerating* into a record month — that is a functioning primary market — while the worst credits keep repricing. **A quality-tail event, not a market-function event.** ⚠️ **What changed since 8/27 and is the thing to watch: the index leg is no longer perfectly inert.** HY +11bp and BB +11bp mean the freeze thesis moved **closer** (74bp vs 83bp) rather than further for the first time in three weeks, and `VX-BND-07`'s credit-equity reactivation band is now 62–87bp away off the 263 trough. **Still: no registered condition fired, and the live escalation remains CCC 1100, 15bp away with momentum against it (`BND-27`, 65%).** ⚠️ **If it arms, the expression is single-name/CCC — never HYG.**

> *(Prior read retained below.)*

### Prior Read — 2026-08-27 ~12:2x ET (all credit levels **8/26**, one date, cache-busted)

| Metric | Level | Date | vs threshold |
|---|--:|---|---|
| **HY OAS** | **267bp** | FRED **8/26** | **33bp** below the 300 watch · **83bp** below the 350 freeze *(both recomputed off 267; this row read 275 / 25bp / 75bp — the 8/20 vintage — until 2026-08-27)* |
| **CCC OAS** | **1031bp** | FRED **8/26** | **69bp** below the 1100 escalation. ★ **The 2026 max is 1039 (8/25) and it held EXACTLY ONE SESSION** — this row called 1035 [8/20] a "FRESH 2026 HIGH" and the tail has since printed 1037, 1036, 1039 and then reversed to 1031. ⚠️ **NOT a series high** — series max **1137 (2025-04-07)**, n=787, window 2023-08-28→2026-08-26, 22 prior obs ≥1031 |
| **IG OAS** | **80bp** | FRED **8/26** | band **79–82** across the last 12 closes ⇒ **+1bp in four weeks** against a +20bp/wk trigger. No threshold near |
| **CCC/HY ratio** | **3.86x** | FRED **8/26** | ⚠️ **ratio and levels now point OPPOSITE ways: the ratio rose 3.85x→3.86x while every level FELL**, because CCC fell proportionally less. **The ratio alone would report a widening that did not happen in levels** |
| **Pulled deals** | **ZERO** | 8/27 | the access test — unimpaired |
| IG primary volume | **~$56B in the week to 8/14** | WALTER `-005`, **wire-level, NOT pulled at primary** | absorbed with no spread disruption |

**Verdict: PRIMARY MARKET ACCESS IS FULLY OPEN, AND THE TAIL IS WIDENING UNDERNEATH IT.** Those are both true and they are not in tension: **the index is inert, IG is flat in a 3bp band, there are zero pulled deals — and the worst credits are repricing.** That is a *quality-tail* event, not a *market-function* event. **The freeze thesis (HY 350) is 83bp away and FURTHER than three weeks ago; the escalation that IS live is CCC 1100, 69bp away.** ⚠️ *(Read “75bp … 65bp” — the 8/20 vintage — until 2026-08-27 ~12:2x ET. **Both distances sat in PROSE, three lines under the table I had just refreshed.** This desk's own MEMORY records “my sweeps catch TABLES and miss PROSE”; this is n+1, committed inside the audit that was fixing the class. The direction word also flipped: HY tightened, so the freeze is further away, not “no closer.”)* ⚠️ **The expression implied, if it ever arms, is single-name/CCC — not HYG, whose index level has round-tripped the entire July widening.**

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
