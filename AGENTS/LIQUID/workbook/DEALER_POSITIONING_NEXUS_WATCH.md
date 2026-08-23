# Dealer-Positioning Nexus Watch — registered 2026-07-11 (Sat ~18:00 ET)
**Owner:** LIQUID (credit-plumbing side; HENRY covers rates→equity — reconcile on contact, one figure per shared metric) · **Status:** ARMED-WATCH (a monitoring conjunction, **NOT a prediction of the CPI print** — the print branch lives in `CPI_20260714_CREDIT_PREREG.md`) · **Born from:** threads-sweep TOP-1 (7/11), Will-approved.

## The mechanism (why these three belong in one file)

A hot CPI 7/14 landing on a completed arm-#2 (10Y 5-of-5 ≥4.50 if Mon holds) hits three pre-loaded surfaces at once: front-end repricing forces P&L on the record leveraged SOFR short → cover flow amplifies rates vol (the MOVE leg) → duration-sensitive credit paper reprices into a dealer book that is **structurally short exactly the long-end IG bucket** → gap-pricing, not orderly repricing. My HY>280 X1 line could then be *reached by amplification rather than credit substance* — KB-LIQ-062's beta-vs-substance discriminator and KB-LIQ-074's acute funding rows are the check when this fires. This is the load-bearing scenario the mandate-extension SIG named: the HY>280 trigger assumes dealers can reprice; this watch monitors whether they can.

## The three legs (all fresh-pulled Sat 7/11 from free primaries — vintages stamped)

| Leg | Latest | Trend / context | Source |
|-----|--------|-----------------|--------|
| **1. Positioning** — SOFR-3M futures, leveraged-fund net | **−2,872,406 contracts [as-of Tue 7/7, released Fri 7/10]** ≈ **−$700B notional-equiv** (convention band $690-720B: $2,500 × IMM price ≈ $241K/contract → $692B; the cruder $250K shorthand → $718B — *corrected 7/11 PM from the single-convention round-4 figure*) | Record zone INTACT and RECENT: build −306K [12/23/25] → ~−0.9M Jan-Apr plateau → May-Jun acceleration → **−2,943,898 [6/30] = the record ≈ −$710B** → −2,872,406 [7/7] (+71,492 w/w = FIRST meaningful cover since mid-June, marginal). **Structure (7/11 deep-dive):** asset managers net-short the SAME side (−501,067 [7/7], persistently since 5/5) and **dealers are the mirror long +3,317,752** — a lev+AM −3.37M short warehoused ~1:1 by dealer books; 185 distinct lev short traders (window high = broad), top-4 net short 12.1% of OI. Companions same-direction: SOFR-1M −283,695; 10Y ERIS SOFR swap −135,113 ≈ −$13.5B [all 7/7] | CFTC TFF via publicreporting.cftc.gov API (futures-only, `gpe5-46if`); full decomposition → `research/2026-07-11_sofr-deep-dive.md` |
| **2. Dealer warehouse** — corp-bond net positions | IG >10y (G10): **−$9,402mm [as-of Wed 7/1]**. IG 5-10y (G5L10): **−$213mm [7/1]** | ⚠️ **CORRECTION to my 6/17-based framing:** the G5L10 −$825mm [6/17] flip did NOT persist — +$365mm [6/24], −$213mm [7/1] = **oscillation around zero**, not a sustained no-bid flip. The real structural datum is the LONG end: G10 2026 mean **−$10.0B** vs 2025 mean −$3.96B, 2024 −$0.59B, 2023 −$0.15B — a multi-year ~6x deepening; 2026 range −$6.7B to −$11.7B. HY buckets small/mixed: BELG5L10 −$1,734mm [7/1, widest of the 8-wk window], BELG10 +$366mm | NY Fed PD stats API (`markets.newyorkfed.org/api/pd/`), weekly, ~8d lag; next as-of-7/8 release ~Thu 7/16 |
| **3. Rates-vol** — MOVE vs VIX | MOVE **72.41 [7/9]**, 3 sessions up unreversed; VIX 15.51 [7/9] calm | Rates-led vol signature (VIOLET find, PROME canon 7/9; ^MOVE now in FORGE SERIES per 7/11 commit `34999644` — pull live from Mon) | VIOLET-owned read; FORGE fetch.py ^MOVE |

## Fire conditions (watch → write-up, NOT a position trigger)

| ID | Condition | Meaning |
|----|-----------|---------|
| W1 *(re-worded 7/11 PM)* | SOFR-3M lev net beyond **−2,950,000** contracts (new record past the **−2,943,898 [6/30]** peak) **OR** a one-week **cover >300,000** contracts (~4x the largest cover in the 30-wk history; largest weekly build was −379K [6/2]) | Pin deepening / unwind starting (either direction is information) — **but read any cover through the basis-vs-directional discriminator below before calling it systemic** |
| W2 | G10 net-short **< −$12.0B** (beyond the 2026 extreme −$11.66B) **OR** G5L10 **< −$800mm two consecutive weeks** (the persistence the 6/17 print lacked) | Warehouse bid withdrawing at the duration end / mid-curve flip turning real |
| W3 | **MOVE >85 while VIX <20** | Rates-led vol regime confirmed (VIOLET's figure governs) |
| **CONJUNCTION** | **Any 2 of W1/W2/W3 inside a rolling 2-week window** | Same-session write-up → PROME + NEXUS (+HENRY seam); re-run KB-LIQ-074 acute rows (SOFR 99pct tail, SRF) and read any concurrent HY move through KB-LIQ-062 (amplification ≠ substance) |

## Basis-vs-directional caveat (added 7/11 PM deep-dive — load-bearing for interpretation)

The directional/RV split of the short is **not knowable from free data** (CFTC doesn't tag strategy; per-expiry positioning unpublished — front-vs-deferred strip placement is a labeled unknowable). Observable structure leans **substantially directional** (build tracks the hike-repricing exactly; asset managers same-side short since 5/5; 185 traders = broad; press/analyst framing = higher-for-longer), with a **real but unsizable RV component** (dealer mirror-long = warehoused hedging flow; record SOFR-FF spread volumes). Consequences: (a) the squeeze mechanic runs on the *directional share only* — a soft CPI puts the short offside and the cover bid lands in the FRONT-END/STIR complex; transmission to the 10Y is indirect (steepener impulse), so "forced cover caps the 10Y" over-claims; (b) **at any W1 cover, check swap spreads / SOFR-FF spread concurrently: spreads stable while shorts cover = directional squeeze confirmed; spreads moving with the cover = RV unwind, less systemic.** Full evidence table → `research/2026-07-11_sofr-deep-dive.md` §3.

## ★ GRADED — Sun 2026-08-23 (the overdue leg-(a) pass; covers 7/21 → 8/18 CFTC, → 8/12 NY Fed PD, → 8/21 MOVE)

**Overdue since 7/25** — carried on the owed list through five closeouts. Graded tonight off a purpose-built reusable fetcher, `scripts/cftc_tff_rates.py` (CFTC TFF **raw files**, not Socrata; as-of dates are TUESDAYS, files publish Fri ~15:30 ET).

**Verdict: CONJUNCTION NOT MET — 0-of-3.** No joint PROME/NEXUS write-up owed. **But the shape is the finding: two legs printed their CLOSEST-EVER approach in this window while the third moved decisively the other way.**

| Leg | Grade | Data [as-of] | vs terms |
|-----|-------|--------------|----------|
| **W1 — SOFR-3M lev net** | **NOT FIRED** — *closest approach on record* | net **−2,530,893 [8/18]** (L 1,052,967 − S 3,583,860). Weekly ΔNET across the window: +92,780 [7/21] · **+248,236 [7/28]** · −86,148 [8/04] · −27,730 [8/11] · +28,923 [8/18] | (a) new record past −2,950,000? **NO** — moving *away*, 413K less short than the −2,943,898 [6/30] peak. (b) one-week cover >300,000? **NO** — but **248,236 [7/28] is the LARGEST single-week cover in the series, 83% of the line**, 51,764 short of firing. It landed in **FOMC week** (7/28-29) and reads directional/policy-path, not RV — the expected signature per the §Basis-vs-directional discriminator |
| **W2 — dealer warehouse** | **NOT FIRED** — *and moving decisively AWAY from the line, in the direction that matters* | **G10 −$6,929mm [8/12]**, the least-short print of the window (7/15 −9,319 · 7/22 −9,735 · 7/29 −8,855 · 8/05 −9,157 · **8/12 −6,929**). **G5L10 +$1,921mm [8/12]** — 7/29 +793 · 8/05 +508 · **8/12 +1,921** | G10 < −$12.0B? **NO** (−$6.9B; ~$5.1B of room, and the 2026 extreme −$11,663 [6/10] is receding). G5L10 < −$800mm ×2 consecutive? **NO** — it never reached −800 once, and the last **three** prints are strongly **positive**. Source: NY Fed PD API `PDPOSCSBND-G10`/`-G5L10`, series break **resolved at runtime** (`SBN2024`) — ⚠️ a stale break returns a valid 200 whose data stops in mid-2024, and a mis-cased code returns an EMPTY 200; both traps hit me tonight before the fix (BOND's `fr2004_fetch.py` documents them) |
| **W3 — rates-vol** | **NOT FIRED** — *closest approach* | **MOVE 73.40 [8/21]**, window max **83.02 [7/31]** (also 80.48 [8/03], 80.08 [7/23]); **VIX 15.13 [8/21]** | MOVE >85 while VIX <20? **NO** — but 83.02 is **1.98 points** under the line **with the VIX condition satisfied**, the nearest W3 has come. VIOLET-owned figure |

### ★ THE FINDING — W1 IS BLIND TO THE BEHAVIOUR IT WAS BUILT TO WATCH (→ KB-LIQ-097)

**The pin has materially unwound and W1 could never have said so.**

| SOFR-3M lev net | as-of | contracts |
|---|---|---:|
| peak | 6/30 | **−2,943,898** |
| now | 8/18 | **−2,530,893** |
| **cumulative** | 7 weeks | **+413,005 covered (−14.0%)** |

At the spec's own $240–250K/contract band that is **≈ −$100B of notional pin removed** (≈$707–736B → ≈$607–633B). **413,005 exceeds W1's own 300,000 trigger by 38% — and no weekly print came close**, because it arrived as a **seven-week bleed averaging ~59K/week.**

> **W1 keys on a WEEKLY delta. The position is exiting on a MULTI-WEEK drift. A weekly-delta trigger cannot see a cumulative one — it is shaped to catch a squeeze and is blind to an orderly exit, which is the more likely way a record position actually leaves.**

This is the time-dimension twin of KB-LIQ-095/084/080: an instrument that cannot see the thing it was built for because of how it aggregates. **⚠️ Route-out owed to PROME — GATE-LIQ-076's W1 wording needs a cumulative leg. I do not edit GATES.tsv.** Suggested, not adopted: *"OR cumulative net change ≥300,000 over any rolling 8-week window."* On the current tape that leg would have fired ~8/04 and would be firing now.

**Directional-vs-RV read on the 248,236 cover [7/28] (discriminator applied):** it is 8.4% of the position and landed in **FOMC week**. Same class as the 7/14 cool-CPI cover, one size up: a **directional/policy-path** trim, not an RV unwind and not a squeeze. Consistent with W2 moving the *opposite* way — a genuine funding-stress unwind would push dealer warehouse short *wider*, and it went from −$9.6B to −$6.9B while the 5–10y bucket flipped **net long**.

**Cross-read that matters more than the grade:** W2's direction independently corroborates BOND's benign dealer read *and* my 8/23 KB-BND-092 refutation. **Dealers are ADDING inventory, not shedding it** — a withdrawing warehouse bid is the one thing all three theses would have needed, and it is absent in the series built to measure it.

**Next graded read:** CFTC TFF Fri **8/28** (as-of Tue **8/25**) — ⚠️ **this is also the 8/26 5Y auction's positioning read, and it publishes two days AFTER the auction (KB-LIQ-096). Do not grade the 8/26 auction's basis leg on 8/26.** NY Fed PD ~Thu **8/27** (as-of 8/19).

---

## GRADED — Sat 2026-07-18 (post-CPI COT [as-of 7/14] + PD [as-of 7/8], primary files)

**Verdict: CONJUNCTION NOT MET — 0-of-3 legs fired.** No joint PROME/NEXUS amplification write-up owed. The hot-print-into-loaded-book scenario did not materialize: CPI 7/14 printed COOL, so the loaded short was not squeezed and dealer capacity was never tested.

| Leg | Grade | Data [as-of] | vs terms |
|-----|-------|--------------|----------|
| **W1 — SOFR-3M lev net** | **NOT FIRED** | **−2,786,954 ct [7/14]** (L 1,108,561 − S 3,895,515), an **85,452-ct COVER** off −2,872,406 [7/7]; ≈ **−$680B** (band $669B @$240K/ct → $697B @$250K) — still record-zone | (a) new record past −2,950,000? **NO** (less short than the −2,943,898 [6/30] peak). (b) cover >300,000? **NO** (85,452). Source: raw CFTC TFF `FinFutWk.txt` futures-only, released Fri 7/17 3:30 ET — **graded off the raw file, NOT Socrata** (which lags releases). Reconciled to prior via change columns (ΔLong +61,925 / ΔShort −23,527 = +85,452 net cover ✓) |
| **W2 — dealer warehouse** | **NOT FIRED** | **G10 IG >10y −$9,589mm [7/8]** (vs −$9,402mm [7/1]; w/w −$187mm more short), ~$2.4B from the line. **G5L10 +$168mm [7/8]** (vs −$213mm [7/1], back positive) | G10 < −$12.0B? **NO** (−$9.6B; 2026 extreme was −$11,663 [6/10]). G5L10 < −$800mm ×2 consecutive weeks? **NO** — still oscillating (−825[6/17]→+365[6/24]→−213[7/1]→+168[7/8]). Source: NY Fed PD API `PDPOSCSBND-G10`/`-G5L10` |
| **W3 — rates-vol** | **NOT FIRED** | **MOVE 68 / VIX 18.71 [7/17 close]** | MOVE >85 while VIX <20? **NO** (MOVE 17bp under the line). VIOLET-owned figure |

**Directional-vs-RV read on the W1 cover (discriminator applied):** the 85,452-ct cover (3% of the position) landed into a COOL CPI 7/14 — a cool print puts the substantially-directional short modestly offside → a small front-end/STIR cover bid. This is the *expected directional signature* (cover tracks the disinflation surprise), **not** an RV unwind and not a systemic squeeze. The short remains **near-record** (−2.79M ≈ −$680B, ~5% off the −$736B/−2.94M [6/30] peak) — the pin is intact, marginally trimmed. No swap-spread cross-check needed for grading since W1 did not fire; had it fired on the cover, the check would be: swap spreads stable = directional squeeze, moving = RV unwind (§ Basis-vs-directional caveat).

**WALTER structural-why caveat carried (alongside, not instead of, the mechanical verdict):** the leveraged short is a 28-yr record (first since 1998) warehoused ~1:1 by a dealer mirror-long — the sourced 'why' leans **structural** (hedging/warehouse flow + higher-for-longer repricing), NOT directional bear conviction. A near-record short that is structural is not itself a fresh bear signal; the conjunction gate is the discipline that keeps positioning magnitude from being over-read as transmission.

**Next graded read:** CFTC TFF Fri 7/24 (as-of Tue 7/21); NY Fed PD ~Thu 7/23 (as-of 7/15). Rolling 2-week conjunction window resets — the 7/11-registration window closes with 0-of-3.

## Cadence + next prints

- **CFTC TFF:** Fridays ~3:30 ET; next = 7/17 carrying **as-of Tue 7/14 = the post-CPI positioning read** (does the short cover into a hot print?).
- **NY Fed PD:** weekly Thu; next release ~7/16 (as-of Wed 7/8).
- **MOVE:** daily via FORGE from Mon 7/13.
- Feeds: KB-LIQ-074 (slow-lead leg), ES-LIQ-02/04 (tracker cross-refs), NEXUS CPI-week read. Registered in KB as **KB-LIQ-076**.
