# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension, integrated 7/1; + the sovereign-credibility instrument set per the Will-ruled 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-02 ~19:3x–21:xx ET (PROME-spawned Tier-1, bond-28) · **Prior:** 2026-09-01 ~21:0x–23:xx ET

> 📕 **THIS FILE IS HOT/COLD SPLIT AND ROTATED. NOTHING HAS EVER BEEN DELETED FROM IT.** Complete pre-split snapshot: `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md` (160,077 B, crc32 `1210262`). Rotated since, each verbatim and crc-stamped: the 9/1 BOTTOM LINE (`domain/sources/2026-09-02_STATUS_archive_bottomline_9-1.md`) · the 9/2 BOTTOM LINE (`domain/sources/2026-09-04_STATUS_archive_bottomline_9-2.md`) · the FR2004 8/19→8/26 vintage essay (`monitors/DEALER_CAPACITY_9-4_vintage_note.md`) · **this banner's own full text** (`archive/2026-09-04_STATUS_split-banner_9-1.md`, crc32 `4116880519`) — **the notice explaining the byte problem had become part of it.**
> **What stays hot: every live value, score, gate, exit criterion and dated catalyst. What rotates: riders, teaching quotes, per-auction evidence essays and superseded BOTTOM LINE blocks.** Canon: `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`. **Budget 32,550 B — never raise it; rotate instead.**

**Canonical elsewhere — this file carries NO second copy:** thesis + full falsification → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalyst source of truth → `docket/CATALYSTS.tsv` · positions/gates → `TRADE.md` · durable learnings → `MEMORY.md` · session handoff → `SCRATCH.md`.

---

## Regime (one-line)

**Real-rate / higher-for-longer.** ★ **C-36 = TWO-PART, RULED 2026-09-01: the policy-path channel is ALIVE AND TRANSMITTING · term premium drove the July delta.** Decided on HENRY's pre-registered branch, resolved on published data (the 8/28 print is monotonically front-led, Δ2Y +14.0 > Δ10Y +6.0 > Δ30Y +3.0). **A one-part label over-reads the evidence in EITHER direction.** ⚠️ **This SPLITS the label — it does NOT move C-36 "toward term premium"; the 8/10 forum guard-rail stands.** ⚠️ **One session is not a path.** **Full ruling narrative + all four caveats: `thesis/THESIS.md` v1.2.0 and `thesis/CHANGELOG.md` (canonical); the STATUS-resident version is archived verbatim at `domain/sources/2026-09-04_STATUS_archive_C36-ruling-narrative.md`, crc32 `3875636201`, nothing deleted.** Live out-of-sample corroboration: `BND-21` TRUE (9/2); `BND-24` OPEN, resolving 9/5.

**The configuration, restated:** the long end is engaged (30Y in a **42-session run ≥5.00%**, 58 days in 2026 [9/2]) with **no Fed coupon backstop post-QT**, so long-end absorption is entirely private/foreign/dealer. **Auctions remain "expensive, not broken" — 18 consecutive benign resolutions since 7/9**, no composition failure at any tenor on either live definition. Credit is inert at the index with a live CCC tail.

---

## Current Dashboard

*Every value pulled live this session via `monitors/boot_recompute.py` (cache-busted) unless tagged otherwise. **No naked numbers** — source + date on every row.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.27%** | 🔴 | [CONF FRED **9/2**] — flat 9/1→9/2. ⚠️ **CORRECTED 9/4: this row read “ties the 2026 max (5.27, 7/31)” and the 2026 max is **5.31 [8/17]** (full-series pull, n=169 2026 sessions). 5.27 is the joint-3rd highest close of 2026 (7/31, 8/21, 9/1, 9/2), **not** the high. A carried figure, corrected at the primary.** |
| 10Y (DGS10) | **4.79%** | 🔴 | [CONF FRED **9/2**] — flat 9/1→9/2; the 9/1 move was +4.0bp = real +0.0 + BE +4.0 |
| 2Y (DGS2) | **4.39%** | 🟠 = | [CONF FRED **9/2**] — flat 9/1→9/2 |
| **10Y real (DFII10)** | **2.45%** | 🟠 ↑ | [CONF FRED **9/2**] — **+1.0bp on 9/2** (2.44 → 2.45). **97.0th pctile full series (n=5,922), 99.8th post-2010.** `BND-21` resolved TRUE on the 9/1 observation |
| 5Y5Y fwd (T5YIFR) | **2.33%** | 🟡 = | [CONF FRED **9/2**] — +2.0bp on 9/1, flat 9/2. Publishes one date ahead of the nominals (H.15 partial split, `KB-BND-168`) |
| 10Y BE (T10YIE) | **2.34%** | 🟠 ↓ | [CONF FRED **9/2**] — +4.0bp on 9/1, **−1.0bp on 9/2**. Publishes one date ahead |
| ACM 10Y term premium | **+0.73%** | 🟠 | [CONF NY Fed, **Jul-2026 monthly — NOT daily**] |
| Kim-Wright 10Y TP (daily) | **0.8682** | 🟠 ↑ | [CONF FRED `THREEFYTP10` **8/21** — model output, not a market price] |
| **HY OAS** | **266bps** | 🟢 ↑ | [CONF FRED `BAMLH0A0HYM2` **9/2**] — +1bp on 9/2 |
| **CCC OAS** | **1053bps** | 🟠 ↑ | [CONF FRED `BAMLH0A3HYC` **9/2**] — +4bp on 9/2, another fresh 2026 high (series max 1137, 2025-04-07) |
| IG OAS | **81bps** | 🟢 = | [CONF FRED `BAMLC0A0CM` **9/2**] |
| **FR2004 11–21Y** | **$65.0B** [as-of **8/26**] | 🟡 ↓ | [CONF NY Fed API `SBN2024`, pulled **9/4** via `monitors/fr2004_fetch.py`] — **NEW VINTAGE: −$3.9B w/w, the 8/19 duration-extension partly GAVE BACK.** Long-end total **$151.8B, +$5.4B w/w** |
| SOFR−IORB | **+3bp** | 🟡 | [CONF FRED SOFR 3.68 / IORB 3.65, **8/31** — month-end; **9/1 SOFR not yet on FRED at 19:4x ET 9/2**, `re-test: 2026-09-03`] |
| TLT | **$81.95 +0.10%** | 🟠 = | [CONF yfinance **9/2 close**, pulled 9/2 ~19:4x ET] |
| ^MOVE (rates vol) | **77.88** | 🟡 | [CONF yfinance **9/1** — not re-pulled 9/2] |
| JGB 10Y | **2.987%** | 🟠 ↑ | [CONF **MOF primary**, **9/1**, BOND's own pull — wires report 3.00%, first since 1996] |
| JGB 30Y | **4.131%** | 🟠 ↑ | [CONF MOF primary, **9/1**] |
| EA AAA 10Y | **3.340%** | 🟠 ↑ | [CONF ECB SDW, **8/31**] — wire 3.364 on 9/1, highest since Apr-2011 |
| UK 10Y | **5.025%** | 🟠 ↑ | [CONF BoE IADB, **8/27** — BoE's own lag; 8/31 a UK bank holiday] |
| USD/JPY | **cite SAM** | 🟠 | [**SAM owns** — read the level at `AGENTS/SAM/STATUS.md`. This desk keeps NO copy] |
| Brent | **cite BRENT** | 🟠 | [**BRENT owns** — read at `AGENTS/BRENT/STATUS.md`. BOND needs the DIRECTION for the breakeven read, not a level of its own] |
| Fed b/s (WALCL) | **$6.746T** [8/19] | 🟢 = | [CONF FRED, 8/19] |

### Gate distances — the numbers that drive decisions *(recomputed every boot, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — the ONLY live TLT-put add-gate** | **5bp** [9/2] | 🔴 **+1bp on 9/2 ⇒ CLOSEST OF THE ENTIRE EPISODE.** Path 2.32 [8/25] → 2.42 [8/28] → 2.44 [8/31] → 2.44 [9/1] → **2.45 [9/2]** |
| T5YIFR >2.50 (inflation-unanchor) | 17bp [9/3] | 🟡 |
| DGS30 >5.00 (long-end level) | — | 🔴 **BREACHED**, **42-session run, 58 days in 2026** [9/2] |
| DGS10 >4.50 (arm-#2 line) | — | 🔴 **BREACHED** |
| HY OAS >300 (reopen HYG) | 34bp [9/2] | 🟢 |
| CCC/HY ratio >1100 escalation | 47bp [9/2] | 🟠 **closing** |
| Credit-equity lead reactivate (HY +75–100 from the 263 trough) | 72–97bp [9/2] | 🟢 inactive |

🔴 **THE ADD-GATE MOVED 12bp TOWARD FIRING WHILE THIS DESK WAS DARK, and every BOND surface said 18bp until this session.** True path: 2.32 [8/25] → 2.34 → 2.34 → **2.42 [8/28] → 2.44 [8/31]**. **Position UNCHANGED — Will's standing 7/16 NO-ADD governs, root rule #5 backstops, and no add executes without [Approve].**

### FR2004 dealer stock — live row on the dashboard above; **the 8/19→8/26 vintage turn and its consequences are archived VERBATIM** at `monitors/DEALER_CAPACITY_9-4_vintage_note.md` (crc32 `4184183995`, 2077 B, nothing deleted; rotated 9/4 under the read cap)

**One-line state:** 8/26 as-of — **11-21Y $65.0B (−$3.9B w/w)** but **total long-end $151.8B (+$5.4B w/w)** ⇒ the long-end drawdown **NARROWED to −13.3 percent** and the *"still widening"* clause four surfaces carried is **FALSE**. The rebuild sits across the 8/25–27 auction cluster, i.e. ordinary takedown. **Two vintages point opposite ways ⇒ ambiguous by the monitor's own discriminator, no pre-registered trigger fired, `VX-BND-04` HOLDS AT 2.**

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **3** = | 🟠 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | 30Y 5.27 [9/2] in a **42-session run ≥5.00**, 58 days in 2026 (2026 max **5.31, 8/17**); DFII10 **2.45 = 97.0th pctile full / 99.8th post-2010** | DFII10 ≥2.50 sustained, or a fresh DGS30 high with weak composition |
| 2 | Treasury auction health | **2** = | 🟡 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED | **18 consecutive benign resolutions since 7/9.** 8/27 7Y: BTC 2.50, ind 60.78% (+3.54pp clear of the `I'` bar), dlr 12.26% — clean on BOTH live definitions | A composition failure (see kill spec), or 3 consecutive auctions passing both legs (counter = **0**) |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | **FR2004 8/26 [new 9/4]: long-end −13.3% off peak (drawdown NARROWED, +$5.4B w/w), 11-21Y −$3.9B w/w** — the 8/19 duration-extension partly reversed; rebuild sits across the 8/25–27 cluster | A further 11-21Y build **with** weak auction composition or SOFR−IORB positive |
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `VX-BND-11` | HY 263 inert, zero pulled deals, primary open every session; **CCC tail 1042 and rising** | HY OAS >300 with velocity, or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 80, ~$56B priced the week of 8/11 without disruption | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | No sustained divergence | Synthetic leading cash on a sustained basis |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY 71bp below the reactivation band | HY +75–100bp from the 263 trough while VIX <20 |

**Composite: 12/35 — UNCHANGED for a NINTH consecutive scoring session** (8/15 · 8/18 · 8/20 · 8/21 · 8/27 · 9/1 · **9/2**). Distribution: 🟠 1 · 🟡 3 · 🟢 3 · 🔴 0.
**Re-summed and verified against the vector scores this session: 3+2+2+2+1+1+1 = 12.** ✅

**Tracked OUTSIDE the composite** (they enter the matrix only when they earn weight, so the composite stays comparable across sessions): `VX-BND-15` inflation-expectations anchoring (2) · **`VX-BND-17` MBS / housing-finance relay (1) — 🔵 RE-ARMED 9/4 FROM DORMANT, score deliberately UNCHANGED** · `VX-BND-18` FHLB advances (2) · `VX-BND-19` eurozone rates / ECB shock (3) · 🆕 **`VX-BND-20` benchmark-driven structural UST demand (2) — OPENED 9/4 at Will's direction.**

### 🆕 `VX-BND-20` — Benchmark-Driven Structural UST Demand *(opened 2026-09-04 at Will's direction · **full surface: `monitors/BENCHMARK_DEMAND.md`** · channel `FL-BND-14` LATENT)*

**Live object — GPFG (NBIM → Norwegian MoF, submission 2026-09-01, read at the primary):** government subindex **70%→50%** · **US govt 34.1%→21.9% ≈ −$80B of ~$215B** · non-govt **30%→50%** (MBS ~13% of the new index) · JGB 4.6%→7.4% · **USD currency share UNCHANGED at "just over 50%"**.
🔴 **⇒ ~$80B out of USTs ≈ ~$82B [EST] INTO US MBS — a Treasury→spread rotation INSIDE the dollar bloc, NOT de-dollarization.** Opposite of the coverage. Derivation and every caveat: the monitor.
🔴 **"TWISTING THE KNIFE" FRAME (Bloomberg MLIV video, 9/4) TESTED AND IT FAILS:** GPFG's UST holdings went **$100B (6.9% of fund, 2021) → $158B (8.7%, 2024) → $199B (9.4%, Dec-2025) → ~$215B (Jun-2026)** — **more than doubled in five years, share up EVERY year, +$18B in H2-2025 alone**, US assets 52.4%→52.9% of the fund. **The most consistent incremental UST buyer among large sovereign allocators, right up to the proposal week.** ⚠️ **The hostile frame is at the HEADLINE layer — both commentaries read in full concede the USD share is unchanged and that "no single actor is dumping Treasuries."** ⚖️ The **direction** does reverse a five-year trend; what fails is the **motive** reading. ★ **NBIM's stated rationale is a TERM-PREMIUM argument — a sovereign allocator saying it wants to be *paid a premium* to hold DM government duration (bears on C-36 / `VX-BND-12`).** `KB-BND-244`.
**Score 2 (WATCH).** 🟡 a SECOND mandated holder >$250B AUM proposes a govt-subindex/UST cut. 🔴 an ADOPTED MANDATE at a >$150B UST book implementing inside 12 months. ⬇ MoF rejects or dilutes.
⛔ **PROPOSAL — expert group reports 2027-01-25. Zero effect on 9/8–9/10.** ⛔ **No prediction registered: no base rate exists and this desk refuses a gate below n=6.** **Scope: BOND owns the mechanics + MBS leg; ZHAO owns flows/TIC/holdings; SAM owns JGB.** Why it was opened: `VX-BND-17` was DORMANT and `VX-BND-13` is auction-shaped, so **nothing would have caught this.** `KB-BND-236`/`237`/`241`.

> ⚠️ **OPEN MIRROR DIVERGENCE, found by `kb_lint` this session and NOT papered over: `VX-BND-05` (Yield Curve / Long-End Duration) carries score **4** in `workbook/VX.tsv` while the matrix row it rolls into carries **3**, and `VX-BND-16` (Treasury Buyback Posture) carries **4** against a dealer-absorption row of **2**.** A roll-up legitimately differs from its components — the composite counts each vector once — but **the direction here is that the components are HOTTER than the matrix**, i.e. the divergence runs toward under-stating risk. **It predates this session; it is flagged, not silently reconciled, and is owed a ruling next session.** Reconciling it by editing whichever number is convenient is exactly the failure `finding_reconcile_mismatch_does_not_say_which_side_is_wrong` describes.

⚠️ **It held against evidence pushing BOTH ways this session:** bearish — the add-gate closed 12bp, the 11-21Y dealer bucket re-built, CCC made a fresh high, and 9/1 was a synchronised global selloff. Bullish/neutral — the 8/27 7Y was clean on both definitions and Japan moved LEAST of four DM sovereigns 8/13→8/27. **Nothing crossed a pre-registered line.** The auction-health downgrade counter is **0**, not 1 (TIPS do not count toward it).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 2 — `BND-22` (add-gate does not fire 9/1→9/11, 55%, resolves on the 9/14 publication) and `BND-23` (`I'` fires at none of the three refunding legs, 55%, base rate 51%, registered 9/2 with the bars).** ✅ **`BND-21` RESOLVED TRUE 9/2 — `DFII10` [9/1] 2.44, +0.0bp, margin 2.0bp under the ≤2.46 bar, beside `T10YIE` +4.0bp: `FL-BND-12` passes its second out-of-sample test, in the opposite direction from the first.**
**Live file holds `BND-18` → `BND-22`**; **`BND-01` → `BND-17` rotated verbatim** to `thesis/archive/PREDICTIONS_resolved_BND-01_to_BND-17.tsv` under the same read-cap ruling as this file — **22 rows conserved, 5 + 17, nothing deleted.** Resolved tally across both files: **10 TRUE · 10 FALSE · 1 VOID.**

---

## Trade Interface *(full view → `TRADE.md`; positions are TERRY's construction lane)*

- **TLT puts — HOLD, NO ADD.** The only live add-gate (**DFII10 ≥2.50 sustained**) is **5bp away [9/2]** — **the closest approach of the entire episode**, +1bp on 9/2. Gates (b), (c), (d) are all **RESOLVED-AND-DEAD**. ⛔ **Will's standing 7/16 NO-ADD governs; root rule #5 means no add executes without [Approve]; harvest/roll/sizing are TERRY's calls on TERRY's rules.** *This bullet states POSTURE, never a direction — it has been corrected for a wrong direction word twice.*
- **HYG puts — stay closed at the INDEX level.** HY 263, access unimpaired, zero pulled deals. Reopen only on **HY OAS >300 with velocity** (34bp away [9/2]). **The live residue is the CCC tail at 1053 [9/2] — another fresh 2026 high, NOT a series high** (series max 1137, 2025-04-07). Tail widening with an inert index is a **repricing of the worst credits, not a market-function event** ⇒ if it ever arms, the expression is single-name/CCC, never HYG.
- **Credit-equity lead — inactive.** 72bp of headroom [9/2].

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all).** 🔴🔴 **WQ-157 LEG ① RULED 2026-09-04 08:44 ET (Will verbatim *"Approve 157 with your rec"*) — THE LEG IS NOW TIME-SPLIT:**
> ### `I'` STANDALONE THROUGH 2026-09-10; PAIRED THEREAFTER — PAIRING INSTRUMENT OWED.
**Through the refunding: unchanged, dual-printed, a bare `I'` fire moves NOTHING. After it: `I'` + a NON-AUCTION MECHANISM confirmation (FR2004 dealer stock and/or SOFR−IORB). `I'` stays the 🟠 marker permanently; RETIRE rejected.** The rec was BOND's, made against its own book, on BOND's own finding that `I'` fires 23.2% pooled with **no separation**. ⚠️ **LEG ② OPEN, blocked on BOND's FR2004 weekly join — DATED 9/18, never a silent wait.** 🔴 **Join ceiling found 9/4: the 11-21Y and >21Y buckets DO NOT EXIST before 2022-01-05 at the issuer (empty on SBN2015/SBN2013 while 7-11Y returns 365/92 rows) ⇒ n=243 weekly prints, no deeper. `KB-BND-234`.**

🔴 **A composition failure at any coupon auction — and TWO definitions are deliberately live until the kill next evaluates (~9/8–9/10), dual-printed:**
- **NEW (Will-ruled 8/27, `PROME/proposals/2026-08-27_matrix-v2-kill-scope-RULED.md`), governs auctions graded 8/27 forward:** **indirect below that tenor's own trailing-12 15th PERCENTILE, SUFFICIENT ALONE.** Dealer take is **dropped as a bearish criterion** (descriptive only; >18% is contrarian-**BULLISH**). ★ **ALL SEVEN BARS FROZEN 2026-09-02 (FRN-clean; `monitors/AUCTION_HEALTH.md` snapshot 9/2): 2Y 54.82 · 3Y 58.90 · 5Y 60.27 · 7Y 57.24 · 10Y 65.05 · 20Y 61.72 · 30Y 62.93** — refunding legs: **3Y <58.90 · 10Y-R <65.05 · 30Y-R <62.93**. 🔴 **BASE-RATED (the 9/4 deliverable, early): `I'` fires 15.6–28.1%/auction by tenor out-of-sample with NO TLT-5d separation (hit 50.0% vs 53.2%; median +0.14% vs −0.12%; deeper margins worse) ⇒ P(≥1 fire across 9/8–9/10) ≈ 49% on base rate alone. As the 🟠 marker it stands; as a KILL leg it cannot discriminate — Will-gated question via PROME, NOTHING MOVED** (`analysis/2026-09-02_MATRIX_V2_per-tenor-base-rating.md` §5, `KB-BND-222`). ⚠️ **2Y bars published 8/27 were FRN-contaminated (43 FRN rows in the pool); fixed in `grade_auction.py`, no verdict changed (`KB-BND-221`).**
- **OLD (retained for the dual-print):** indirect below trailing-12 min **AND** dealer above trailing-12 max, same tenor.
- 🔴 **Direction disclosed: the new test is STRICTLY EASIER TO FIRE, and the kill firing is what CONFIRMS this desk's own bear thesis.** History was NOT re-scored. Percentages are of **competitive accepted**; never reuse another tenor's numbers.
- ⛔ **NAMED EXCEPTION — the TLT-put ADD re-arm in `TRADE.md` is governed by the OLD, STRICTER test** (WQ-99, Will 2026-09-01 17:22 ET). An ADD authorization must never loosen as a side effect of a definition reconcile. Harmonize only by fresh word with TERRY in the loop.
- ⚠️ **`monitors/grade_auction.py` still computes the OLD test — deliberately.** Until the kill next evaluates, its print **IS** the old-definition half of the dual-print: **useful, NOT the authority.** Patch owed before the old print retires.

**2 · POSITION-SPECIFIC.** TLT puts: exit on a decisive break of the real-rate regime — **DFII10 <2.00 sustained 5 sessions** — or on the thesis kill. 60-DTE mandatory review is TERRY's rail.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal-coupon auctions passing **both** legs (indirect at/above median **and** dealer at/below median). **Counter = 0** — the 8/19 20Y failed the condition and reset it; **TIPS do not count.**

**4 · TIME-BASED.** ✅ MATRIX_V2 per-tenor base-rating **DELIVERED 9/2** (due 9/4). Quarterly percentile-snapshot refresh in `monitors/AUCTION_HEALTH.md` due **10/1**. FHLB Q3 combined report **11/9**. FRBNY quarterly FX report **11/13**.

⚠️ **RETIRED AND NOT REVIVABLE: the auction TAIL (>2bp).** A tail needs the when-issued yield at the bid deadline and **TreasuryDirect does not publish it** ⇒ unscoreable by construction. **No gate, threshold or pre-registration may be keyed on a tail**; wire-reported tails are `[med-conf]` and may never fire anything.

---

## Immediate Catalysts *(source of truth = `docket/CATALYSTS.tsv`; this is the human twin and must not diverge in event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| 🔴 **Tue 9/8** | **3Y auction `91282CRL7`** — September refunding leg 1 | **BARS FROZEN 9/2:** `I'` <58.90 · OLD ind <56.50 AND dlr >19.50 · BTC <2.53. `BND-23` leg 1. |
| 🔴 **Wed 9/9** | **10Y REOPENING `91282CRF0`** ("9-Year 11-Month") — refunding leg 2 | **BARS FROZEN 9/2 (pooled governs):** `I'` <65.05 · OLD ind <63.95 AND dlr >13.38 · reopening-only alt 66.32 (65.05–66.32 = CONVENTION-DEPENDENT, graded both ways). **First KILL evaluation on the dual-print — an `I'` fire alone is NOT a kill until Will rules on `KB-BND-222`.** |
| 🔴 **Thu 9/10** | **30Y REOPENING `912810UW6`** ("29-Year 11-Month") — refunding leg 3 | **BARS FROZEN 9/2 (pooled governs):** `I'` <62.93 · OLD ind <59.95 AND dlr >14.74 · alt 60.28 (60.28–62.93 = CONVENTION-DEPENDENT). The long-end referendum. |
| 🔴 **Wed 9/9 → Wed 11/4** | **sb0607 stepped-up buyback window — F2 goes live at the first op (9/9)** | **STANDING OBLIGATION, EXTERNAL DEPENDENCY: route the F2 read to RED as the ops publish — do NOT batch to a closeout.** `RED-FT-11` v1.1 is an ex-ante conditional **gated on BOND's F2** and **RED will not rebuild it.** Their pre-registered response: off-the-run ⇒ they add a butterfly leg at the next NON-FIRED window; on-the-run ⇒ no change. |
| **Wed 9/9 – Thu 9/10** | **ECB Governing Council** (Berlin, presser 9/10) — ✅ date verified at the ECB primary 8/19 | 2nd 2026 hike? QT language. **EZ Aug HICP 3.3%, a 9/10 hike ~99% priced** (WALTER 9/1). Trigger: **BTP-Bund >200 sustained** — ⚠️ last read 83bp [7/17], **46 days stale, refresh before the meeting.** |
| **Thu 9/10** | **August MTS** — the calendar-artifact test | July's −$432.3B was +48.5% YoY inside an FYTD **+1.3%**, consistent with 8/1 falling on a Saturday. **If August does NOT give back most of the spike, the calendar explanation dies and it becomes a deterioration signal.** Net interest FYTD $931.4B (+10.8% YoY). |
| 🟠 **Tue 9/8** | **CANADIAN RETALIATORY TARIFFS TAKE EFFECT** (dollar-for-dollar vs the US 50% tariff on ~$28B, effective 8/21) | **BREAKEVEN LEG ONLY.** T10YIE / T5YIFR across 9/8 vs the pre-date close, **with DFII10 beside them** to separate a real-yield move from an inflation-expectations one. ⚠️ **NO threshold registered and none is being invented** — the standing insulation claim (`FL-BND-12`, `KB-BND-091`) is the thing under test. A T10YIE move materially larger than its recent daily dispersion **without** a matching real-yield move would qualify it. The $28B basis is UNSTATED in the source. |
| 🟠 **from Fri 9/11** | **`docket_check` BLIND SPAN 9/11 → 9/22 — hand-verify against the Treasury QRA** | The feed reaches ~5 days for coupons and the forward schedule is a QRA **PDF outside TA_WS**, so **no API path closes it.** The tool declares the span UNVERIFIED every run and **deliberately refuses to adjudicate it.** This row is the owed human action. |
| **Tue 9/15 – Wed 9/16** | **SEPTEMBER FOMC — decision + SEP land 9/16** ✅ verified at the Fed primary 8/21 | 🔴 **THE 65–68% FIGURE IS WITHDRAWN AS UNSOURCED-AS-TO-VENUE (settled 9/4 ~14:0x ET) — it is NOT restored and NOT re-asserted as an error.** ORACLE diagnosed it in the morning as a by-October cumulative contract biased hawkish ~10pp; **ORACLE WITHDREW that diagnosis the same afternoon** after WALTER re-verified at source that **CME FedWatch had the September MEETING at 67%→62% and CNBC wrote "a 61% chance of a move"** — a meeting-specific figure from a third venue sitting inside 65–68%. **BOND traced its own provenance and the answer is NEITHER explanation:** `SIG-W-20260901-006` line 42 reads *"Warsh at Jackson Hole (a **Sept-16** hike ~65–68% priced)"* — **meeting-specific by wording, but NO VENUE AND NO INSTRUMENT NAMED ANYWHERE.** ⇒ unciteable either way; withdrawn, same disposition as WALTER's retracted gold −2.35%. ★ **RULE, SHARPENED — STATE THE VENUE *AND* THE HORIZON: this figure HAD the horizon and lacked the venue, so the horizon rule alone would NOT have caught it.** **What this desk carries instead, each venue-named: Polymarket Sept-meeting hike 52.5% · Kalshi 57.0% [CONF ORACLE 9/4 12:42Z] · CME FedWatch ~62–67% [relayed via WALTER from icrypex/CNBC 9/3 — NOT read at CME by any desk].** ⚠️ **If the CME leg holds, the live object is a 17–22pp CROSS-VENUE SPREAD on one meeting (CME systematically most hawkish) — ORACLE's instrument class, flagged not claimed.** ✅ **The 9/3 "Fed 50bp CUT ~74.5%" relay is REFUTED AND SIGN-INVERTED and that finding is UNTOUCHED** (WALTER `SIG-W-20260904-002`: neither CNBC article contains "50bp", "cut" or "74.5"; both describe a hike). **BOND's 9/4 contradiction flag is CLOSED — freezing rather than picking a side was right, and it survived a correction that was itself wrong.** `KB-BND-242` supersedes `KB-BND-238`. Resolver context for the Fed-path arm. Rest of 2026: 10/27-28 · 12/8-9 (SEP). |
| **~Wed 9/16 · ~Thu 9/17** | **20Y · 10Y TIPS** — PATTERN-EXPECTED, **NOT verified** | 🔴 **Inside `docket_check`'s BLIND SPAN (9/11→9/22) — the feed cannot see them.** Confirm at the Treasury QRA / tentative schedule by hand before docketing. |
| **~Tue 9/22 – Thu 9/24** | **month-end 2Y/5Y/7Y cluster** — PATTERN-EXPECTED, **NOT verified** | Same blind span. Same hand-verification owed. |
| ✅ ~~Fri 9/4~~ **done 9/2** | **MATRIX_V2 per-tenor base-rating** DELIVERED · **US-sovereign-CDS** DECLINED TO BUILD (exists at Markit/ICE; free-primary pullability SEARCH-NOT-FOUND; re-test 12/1, `KB-BND-228`) | Bars for the refunding frozen (Exit §1). Kill-leg question with Will. |
| **Fri 9/11** | **PROME 8/21 hyperscaler long-dated IG issuance SHARE** — scheduled 9/2 (was ~9/3) | Core MSFT/GOOGL/META/AMZN/ORCL; USD IG tenor ≥10y, 2026 YTD, same perimeter both sides; size first. A second miss ⇒ DECLINE (`KB-BND-227`). |
| **Mon 11/9** | **FHLB Q3-2026 combined financial report** | `REG-T-06` leg 3 fires if system advances >$700B (REGINALD's, at leg 2 of 3). `VX-BND-18` re-scores. Carries the base rate the escalation-leg retune needs. vs $810.7B [6/30/26]. |
| **Fri 11/13** | **FRBNY quarterly FX report Q3** | **The definitive public record of the 7/30-31 operation** — ESF-vs-SOMA split, size via Table 1. **Until it prints, `FL-BND-11`'s "intervention = mechanical UST reserve selling" must NOT be restated as automatic.** |
| **— STANDING —** | MOF FX intervention · Warsh task force (end-2026) · buyback accept-cap | UST reserve selling = `FL-BND-11` fires · 2027 lane · YCC-lite tell |

**Recently resolved:** ✅ **`BND-21` TRUE 9/2** (DFII10 [9/1] +0.0bp vs BE +4.0) · ✅ **8/27 7Y `91282CRJ2` CLEAN** (BTC 2.50 · ind 60.78% · dlr 12.26%) — 18th consecutive benign resolution; `I'` did NOT fire on its first live test, **+3.54pp clear**. ✅ **8/25–8/27 cluster all clean.** ✅ **T6 = NO-VERDICT** (trigger never fired, PROME-graded 8/30). ✅ **HEN-42 = DENY** (HENRY, FINAL 8/28). ✅ **MOF monthly 8/31 → intervention ¥15,399.3B ≈ $96B** (SAM owns the figure).

---

## BOTTOM LINE

**[2026-09-04 Fri ~08:3x ET — boot session on Will's Swedish-pension question. Three corrections and a new dealer vintage; nothing moved the book.]**

🔴 **CORRECTED ~09:4x ET AFTER A FULL SWEEP — THE BLOCK BELOW WAS RIGHT ABOUT ALECTA AND WRONG ABOUT THE TOPIC.** Will said he read it *today*, and he was right: **NBIM's submission to the Norwegian Ministry of Finance is dated 2026-09-01 and hit the wires 9/4.** **GPFG government subindex 70% → 50%; US government 34.1% → 21.9% = ~$80B off ~$215B of USTs — ~9× the entire discretionary pension cluster combined.** 🔴 **AND THE FINDING IS THE OPPOSITE OF THE HEADLINE: NBIM SAYS THE USD CURRENCY SHARE STAYS "JUST OVER 50%", UNCHANGED.** Non-government goes **30% → 50%** with **MBS ~13% of the new index** ⇒ the ~$80B leaving Treasuries is **almost exactly offset by ~$82B [EST] going INTO US MBS**. A Treasury→spread-product rotation **inside the dollar bloc**, not de-dollarization. ⛔ **It is a PROPOSAL: Ministry response → expert group reports 2027-01-25 → mandate → gradual. ZERO effect on 9/8–10; no vector moves, no trigger fires, frozen bars and kill spec untouched.** **BOND owns ONE leg — the ~$82B phased MBS bid (`VX-BND-17`, NOT re-scored: a proposal is not a fired trigger).** JGB leg (≈+$18B) → SAM; sweep → ZHAO. **My error was generalising from one instance to the topic — three searches keyed on "Swedish pension" returned January, and that was read as "the topic is January."** Working: `analysis/2026-09-04_SWEEP_pension-and-sovereign-UST-divestment.md`, `KB-BND-236`/`237`.

★ **THE ALECTA HALF, WHICH STANDS AS WRITTEN: NO, THIS DESK DID NOT HAVE IT — AND THAT STORY IS ~7.5 MONTHS OLD.** The "Swedish pension cutting US Treasuries" item is **Alecta**, reported by **Dagens Industri / Bloomberg on 2026-01-21** — not September. Alecta held ~SEK 100B (**~$11B**) of USTs at end-2024 and sold ~SEK 70–80B (**~$7.7–8.8B**) in stages **since early 2025**. Companions in the same January cluster: Danish **AkademikerPension** (all USTs, ~$100M) and Dutch **ABP** (−$12B during 2025). **It is not size** — $8.8B over ~18 months is **~7% of one quarterly refunding**, and Alecta's entire former UST book is smaller than the 9/8 3Y leg. 🔴 **And reconciled to the owner's number it cuts against its own headline:** ZHAO's `KB-ZHAO-122` has June TIC foreign **OFFICIAL** selling **$45.4B** while foreign **NON-OFFICIAL bought $23.2B** — and Alecta is non-official, i.e. inside the bucket that was **net buying**. **No BOND vector moved, no trigger fired**; BOND's instrument for foreign step-away is auction composition, and that has printed **18 consecutive benign resolutions since 7/9**. Logged `KB-BND-229`, routed to ZHAO (their lane; BOND keeps no foreign-holdings copy). **SEARCH-NOT-FOUND named so it is closable: three passes found no September-2026 Nordic item; an AP-fund or Alecta H1-2026 report is the unchecked primary, and it is ZHAO's.**

🔴 **THE ADD-GATE IS NOW 5bp AWAY [DFII10 2.45, 9/2] — THE CLOSEST APPROACH OF THE ENTIRE EPISODE**, +1bp on 9/2, at the **97.0th percentile full-series / 99.8th post-2010**. **`BND-22` (no ≥2.50 close 9/1→9/11, 55%) is live and this is its narrowest margin.** ⛔ Position **UNCHANGED** — Will's standing 7/16 NO-ADD governs, root rule #5 backstops, no add without [Approve].

🔴 **THREE CARRIED FIGURES CORRECTED AT THE PRIMARY, all found by `boot_recompute` rc=1:** ① STATUS said 30Y 5.27 **"ties the 2026 max (5.27, 7/31)"** — **the 2026 max is 5.31 [8/17]**; 5.27 is joint-3rd. ② The add-gate read **6bp** on three surfaces; it is **5bp**. ③ **FR2004 was four surfaces stale** at the 8/19 as-of. **New 8/26 vintage pulled: the 8/19 duration-extension PARTLY REVERSED** — 11-21Y **$68.9B → $65.0B (−$3.9B)**, but total long-end **$146.3B → $151.8B (+$5.4B)**, so the long-end drawdown **NARROWED to −13.3%** and the surfaces' *"still widening"* clause is now **false**. The rebuild sits **across the 8/25–27 auction cluster**, i.e. it looks like ordinary takedown. **Two prints now point opposite ways; ambiguous by the monitor's own discriminator, no pre-registered trigger fired ⇒ dealer absorption HOLDS AT 2.**

*(The 2026-09-02 BOTTOM LINE block — the MATRIX_V2 base-rating and the 2Y FRN contamination finding — is archived **VERBATIM** at `domain/sources/2026-09-04_STATUS_archive_bottomline_9-2.md`, **crc32 `2419246656`, 2718 B, nothing deleted** [rotated 9/4 under the read cap]. Its findings are live and canonical at `analysis/2026-09-02_MATRIX_V2_per-tenor-base-rating.md`, `KB-BND-221`/`222` and THESIS v1.2.1.)*

*(The two 9/1 blocks — the selloff grade and the first-boot-after-dark read — are archived VERBATIM at `domain/sources/2026-09-02_STATUS_archive_bottomline_9-1.md`; the selloff grade's working stays at `analysis/2026-09-01_GRADE_the-9-1-global-selloff.md`.)*

**Next dated:** 🔴 **BEFORE 9/8 — WQ-162 (PROME, in inbox): confirm each of the seven frozen `I'` bars names its TreasuryDirect field + vintage + the FRN exclusion rule, or the refunding grade is NO-VERDICT.** 🔴 **BEFORE 9/9 — acknowledge RED's FT-11 v1.1 §3: the `≤ −4bp` cut you chose is NON-STRICT and the tie atom at exactly −4 carries 23 of 661 windows, so the leg fires 8.5%/6.2% not 5.0%/3.8%; RED asks only whether that changes the call.** · 9/4 re-test SOFR−IORB + re-run `dm_cross_section.py` · **9/8–9/10 the refunding on the FROZEN bars, dual-print as ruled, `BND-23`** · 9/9 F2 goes live, **route to RED as ops publish** · 9/9–10 ECB (BTP-Bund 46d stale — refresh) · 9/10 August MTS · 9/11 hyperscaler share · 9/16 FOMC.
