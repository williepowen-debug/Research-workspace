# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension, integrated 7/1; + the sovereign-credibility instrument set per the Will-ruled 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-10 ~12:2x–16:xx ET (Will-spawned; the 30Y-R + first long-end buyback op, live) · **Prior:** 2026-09-09 ~21:2x–22:xx ET

> 📕 **THIS FILE IS HOT/COLD SPLIT AND ROTATED. NOTHING HAS EVER BEEN DELETED FROM IT.** Complete pre-split snapshot: `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md` (160,077 B, crc32 `1210262`). Rotated since, each verbatim and crc-stamped: the 9/1, 9/2 and **9/4** BOTTOM LINE blocks (`domain/sources/2026-09-02_…bottomline_9-1.md` · `2026-09-04_…bottomline_9-2.md` · **`2026-09-09_STATUS_archive_bottomline_9-4.md`, crc32 `551641974`**) · the FR2004 8/19→8/26 essay (`monitors/DEALER_CAPACITY_9-4_vintage_note.md`) · the 9/1 split banner (`archive/2026-09-04_STATUS_split-banner_9-1.md`) · **the `VX-BND-20` block** (`domain/sources/2026-09-09_STATUS_archive_VX-20_block.md`, crc32 `896693574`) · **the Fed-figure provenance catalyst cell** (`domain/sources/2026-09-09_STATUS_archive_fed-figure-provenance-cell.md`, crc32 `562960837`).
> **What stays hot: every live value, score, gate, exit criterion and dated catalyst. What rotates: riders, teaching quotes, per-auction evidence essays and superseded BOTTOM LINE blocks.** Canon: `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`. **Budget 32,550 B — never raise it; rotate instead.**

**Canonical elsewhere — this file carries NO second copy:** thesis + full falsification → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalyst source of truth → `docket/CATALYSTS.tsv` · positions/gates → `TRADE.md` · durable learnings → `MEMORY.md` · session handoff → `SCRATCH.md`.

---

## Regime (one-line)

**Real-rate / higher-for-longer.** ★ **C-36 = TWO-PART, RULED 2026-09-01: the policy-path channel is ALIVE AND TRANSMITTING · term premium drove the July delta.** ✅ **`BND-24` RESOLVED TRUE 9/9 (+4bp): the 9/4 payroll session was FRONT-LED (2s +3 / 10s +1 / 30s −1) — leg 2's SECOND out-of-sample observation. n=2 is not a path; the label stands exactly as ruled.** Full ruling + caveats: `thesis/THESIS.md` v1.2.3, `thesis/CHANGELOG.md`.

**The configuration, restated:** the long end is engaged (30Y in a **45-session run ≥5.00%**, 61 days in 2026 [9/8]) with **no Fed coupon backstop post-QT**, so long-end absorption is entirely private/foreign/dealer — **and from Thu 9/10 an official 10–20Y buyback bid EXISTS AND HAS RUN — $5.187B of a $6.0B cap, 75.1% into low-coupon deep-discount OFF-THE-RUN paper (`KB-BND-272`).** **Auctions remain "expensive, not broken" — 21 consecutive benign resolutions since 7/9; the LAST `I'`-STANDALONE KILL EVALUATION (9/10 30Y-R) FIRED NOTHING, by +16.55pp.** Credit is inert at the index with a live CCC tail at a fresh 2026 high.

---

## Current Dashboard

*Every value pulled live this session via `monitors/boot_recompute.py` (cache-busted 9/9 21:21 ET) unless tagged otherwise. **No naked numbers** — source + date on every row.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.25%** | 🔴 | [CONF FRED **9/8**] — 2026 max **5.31 [8/17]**; 5.27 (9/1–9/2) was joint-3rd. `^TYX` 5.29 intraday 9/9 [yfinance, not a settle] |
| 10Y (DGS10) | **4.80%** | 🔴 | [CONF FRED **9/8**] — 10Y-R stopped at 4.834% on 9/9 (wire: highest since Aug-2007, `[med-conf]`) |
| 2Y (DGS2) | **4.39%** | 🟠 = | [CONF FRED **9/8**] — 4.34 → 4.37 → 4.39 across 9/3–9/8 |
| **10Y real (DFII10)** | **2.43%** | 🟠 | [CONF FRED **9/8**] — path 2.45 [9/2] → 2.42 → 2.43 → **2.43**. **96.2nd pctile full series (n=5,925), 99.4th post-2010** |
| 5Y5Y fwd (T5YIFR) | **2.33%** | 🟡 = | [CONF FRED **9/9**] — publishes one date ahead of the nominals (H.15 split, `KB-BND-178`) |
| 10Y BE (T10YIE) | **2.37%** | 🟡 | [CONF FRED **9/9**] — +2bp across the 9/8 Canadian counter-tariff date, DFII10 flat ⇒ inside dispersion, insulation re-test NULL (`KB-BND-249`) |
| ACM 10Y term premium | **+0.73%** | 🟠 | [CONF NY Fed, **Jul-2026 monthly — NOT daily**] |
| Kim-Wright 10Y TP (daily) | **0.8892** | 🟠 | [CONF FRED `THREEFYTP10` **9/4**] — 2026 high **0.8996 [9/1]**; +8.1bp on the 9/4 payroll session (one session, recorded not interpreted) |
| **HY OAS** | **271bps** | 🟢 = | [CONF FRED `BAMLH0A0HYM2` **9/9**] — inert, 263–275 for a month |
| **CCC OAS** | **1064bps** | 🟠 ↑ | [CONF FRED `BAMLH0A3HYC` **9/9**] — **another fresh 2026 high** (prior 1056 [9/8], 1053 [9/2]; series max 1137, 2025-04-07). Ratio 3.93x |
| IG OAS | **81bps** | 🟢 = | [CONF FRED `BAMLC0A0CM` **9/9**] — September IG supply forecast **~$215B = a record month** [Bloomberg 9/3 poll, secondary]; zero pulled deals |
| **FR2004 11–21Y** | **$65.0B** [as-of **8/26**] | 🟡 | [CONF NY Fed API `SBN2024`, pulled 9/4, **re-confirmed latest 9/9**] — −$3.9B w/w; long-end total **$151.8B, +$5.4B w/w**. 9/2 as-of owed ~9/10–11 |
| SOFR−IORB | **−1bp** | 🟢 | [CONF FRED SOFR 3.64 / IORB 3.65, **9/8**] — the +3 of 8/31 was month-end, fully reversed (`KB-BND-254`) |
| TLT | **$81.73 −0.57%** | 🟠 | [CONF yfinance **9/9 close**] |
| ^MOVE (rates vol) | **76.74** | 🟡 | [CONF yfinance **9/9**] |
| JGB 10Y | **2.891%** | 🟠 | [CONF **MOF primary**, **9/9**, BOND's own pull] — episode high **3.006 [9/2]**, the first close above 3.00 in the held series. SAM owns the level |
| JGB 30Y | 4.131% | ⚪ `[STALE 9/1]` | [MOF 9/1 — not re-pulled 9/9; SAM owns] |
| EA AAA 10Y | **3.378%** | 🟠 | [CONF ECB SDW, **9/8**] — 2Y 2.920 / 30Y 3.762; 9/1→9/8 front-led FLATTENING into the 9/10 ECB |
| UK 10Y | **5.108%** | 🟠 | [CONF BoE IADB, **9/7** — BoE's own lag] |
| Bund / OAT / BTP 10Y | 3.40 / 4.26 / 4.29 | 🟠 | [TradingEconomics **9/9**, SECONDARY] — BTP-Bund ~89bp, OAT-Bund ~86bp; Bund = highest since Apr-2011 |
| USD/JPY · Brent | **cite SAM · BRENT** | 🟠 | [owners' STATUS files — this desk keeps NO copy] |
| Fed b/s (WALCL) | **$6.737T** [9/2] | 🟢 = | [CONF FRED, 9/2] |

### Gate distances — the numbers that drive decisions *(recomputed every boot, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — the ONLY live TLT-put add-gate** | **7bp** [9/8] | 🟠 Closest approach of the episode **5bp [2.45, 9/2]**; path since 2.45 → 2.42 → 2.43 → 2.43. **9/9 implied ≈2.47 `[EST]`** (10Y 4.84 yfinance close − T10YIE 2.37 FRED 9/9; the FRED print lands 9/10 ~4:15 PM and an estimate fires nothing — `TRADE.md` breach protocol). `BND-22` live, 3 sessions left |
| T5YIFR >2.50 (inflation-unanchor) | 17bp [9/9] | 🟡 |
| DGS30 >5.00 (long-end level) | — | 🔴 **BREACHED**, **45-session run, 61 days in 2026 of 172** [9/8] |
| DGS10 >4.50 (arm-#2 line) | — | 🔴 **BREACHED** |
| HY OAS >300 (reopen HYG) | 33bp [9/8] | 🟢 |
| CCC >1100 escalation | **36bp** [9/9] | 🟠 closing (was 44 [9/8], 47 [9/2]) |
| Credit-equity lead reactivate (HY +75–100 from the 263 trough) | 71–96bp [9/8] | 🟢 inactive |

⛔ **Position UNCHANGED — Will's standing 7/16 NO-ADD governs, root rule #5 backstops, no add executes without [Approve].** *(The 9/4 "5bp AWAY" carried on this file and SCRATCH was a level-correct, vintage-stale derived distance — caught by `boot_recompute` part C and corrected by pattern, `KB-BND-252`.)*

### FR2004 dealer stock — **8/26 as-of, still the latest [re-pulled 9/9]**; the 8/19→8/26 essay is archived verbatim at `monitors/DEALER_CAPACITY_9-4_vintage_note.md`

**One-line state:** 11-21Y **$65.0B (−$3.9B w/w)**, long-end total **$151.8B (+$5.4B w/w)** ⇒ drawdowns off the 6/24 peaks **−16.0% / −13.3%** — the total NARROWED, the *"still widening"* clause is retired on every surface (`KB-BND-251`). Rebuild sits across the 8/25–27 cluster = ordinary takedown. **Two vintages point opposite ways ⇒ ambiguous by the monitor's own discriminator; the 'two consecutive builds on TOTAL' trigger has ONE build; `VX-BND-04` HOLDS AT 2.** Funding leg −1bp.

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **3** = | 🟠 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | 30Y 5.25 [9/8] in a **45-session run ≥5.00**, 61 days in 2026 (max 5.31, 8/17); DFII10 **2.43 = 96.2nd pctile full / 99.4th post-2010**; KW TP 0.8892 [9/4] | DFII10 ≥2.50 sustained, or a fresh DGS30 high with weak composition |
| 2 | Treasury auction health | **2** = | 🟡 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED | **21 consecutive benign since 7/9.** 9/9 10Y-R ind **79.18 (+14.13pp)** · **9/10 30Y-R ind 79.48 (+16.55pp clear pooled / +19.21pp alt), BTC 2.61, dlr 2.21 — the LOWEST dealer take of all 45 nominal 30Y auctions in the corpus (2023-01-12 forward) and indirect ABOVE the trailing-12 max; end users took 97.79%** — **the LAST `I'`-standalone kill evaluation: NOTHING FIRED** | A composition failure (kill spec), or 3 consecutive auctions passing both legs (counter = **2** — 9/9 10Y-R, 9/10 30Y-R; **9/15 20Y-R is the third**) |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | **FR2004 8/26 [latest 9/9]: long-end −13.3% off peak (NARROWED, +$5.4B w/w), 11-21Y −$3.9B w/w**; SOFR−IORB −1bp. ⚠️ `VX-16` carry corrected: **first stepped-up long-end op is 9/10 (10–20Y, max $6B), not 9/9** | A further 11-21Y build **with** weak auction composition or SOFR−IORB positive |
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `VX-BND-11` | HY 267 inert, zero pulled deals, primary open; **CCC 1056 = fresh 2026 high**, ratio 3.96x | HY OAS >300 with velocity, or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 81; **September supply forecast ~$215B = a RECORD month**, IG yields >5.5% pulling issuers forward (`KB-BND-259`) | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF 0.8585, z20 +1.28, 97th pctile of 3mo = credit-excess RICH, no divergence [9/8] | Synthetic leading cash on a sustained basis |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY 71bp below the reactivation band | HY +75–100bp from the 263 trough while VIX <20 |

**Composite: 12/35 — UNCHANGED for a TWELFTH consecutive scoring session** (8/15 · 8/18 · 8/20 · 8/21 · 8/27 · 9/1 · 9/2 · 9/4 · 9/9 · **9/10**). ⚠️ *Held deliberately: the 9/10 30Y-R was the strongest composition print in the corpus and the buyback landed off-the-run — both BULLISH for market function — but no pre-registered line moved, and a vector is not re-scored on strength any more than on weakness.* Distribution: 🟠 1 · 🟡 3 · 🟢 3 · 🔴 0.
**Re-summed and verified against the vector scores this session: 3+2+2+2+1+1+1 = 12.** ✅

**Tracked OUTSIDE the composite** (they enter the matrix only when they earn weight): `VX-BND-15` inflation-expectations anchoring (2) · `VX-BND-17` MBS / housing-finance relay (1, re-armed 9/4) · `VX-BND-18` FHLB advances (2) · **`VX-BND-19` eurozone rates / ECB shock (3)** — EA AAA curve flattening front-led into the 9/10 ECB (consensus 25bp to 2.50% DFR, "second and final"); ⚠️ **spec observation logged, not fixed: the yellow leg "OAT-Bund >85bp" is AT its bar and the red leg "Bund >3.25 DISORDERLY" has its level met (3.40) with an undefined qualifier — define it at the 10/1 refresh (`KB-BND-256`)** · **`VX-BND-20` benchmark-driven structural UST demand (2)** — live object = NBIM's 9/1 GPFG proposal (US govt 34.1%→21.9% ≈ −$80B, USD share unchanged ⇒ rotation into US MBS, not de-dollarization); expert group **2027-01-25**, review checkpoint **10/6**; **full surface `monitors/BENCHMARK_DEMAND.md`**, the STATUS block archived verbatim 9/9 (crc32 `896693574`). Zero effect on the refunding.

> ⚠️ **OPEN MIRROR DIVERGENCE, un-reconciled (5th session): `VX-BND-05` = 4 and `VX-BND-16` = 4 in `workbook/VX.tsv` vs matrix rows 3 and 2 — the COMPONENTS are HOTTER than the matrix, i.e. the divergence runs toward UNDER-stating risk.** Flagged, not silently reconciled (`[[finding_reconcile_mismatch_does_not_say_which_side_is_wrong]]`). Full notice archived (crc32 `2218422141`) at `domain/sources/2026-09-04_STATUS_archive_mirror-divergence-notice.md`.

⚠️ **It held against evidence pushing BOTH ways this session:** bearish — CCC made another 2026 high, the 30Y run reached 45 sessions, Bund/OAT/BTP at 2011-era highs into an ECB hike, the 10Y-R stopped at a 2007-era yield. Bullish/neutral — the 3Y and 10Y-R were clean on both definitions (the first kill evaluation fired nothing), the add-gate backed off to 7bp, SOFR−IORB is negative, dealer stock rebuilt, September IG supply is a record. **Nothing crossed a pre-registered line.** Downgrade counter **1** (the 10Y-R; the 3Y's below-median indirect did not qualify; TIPS never count).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 1 — `BND-22` ONLY** (add-gate does not fire 9/1→9/11, 55%; closest approach 5bp [9/2]; **🔴 the 9/10 session is a live threat to it — implied real ≈2.51–2.56 `[EST]`, see the gate row**; resolves on the 9/14 publication of the 9/11 close — do NOT resolve early). ✅ **`BND-23` RESOLVED TRUE 9/10** — `I'` fired at NONE of the three refunding legs: **+3.25pp / +14.13pp / +16.55pp**. Registered base rate 51%. *The margin sequence is the finding: demand STRENGTHENED across the refunding rather than fading into the long end — the opposite of the supply-indigestion shape the bear thesis predicts.* ✅ `BND-24` TRUE 9/9 (+4bp).
**Live file holds `BND-22` → `BND-24`**; `BND-01` → `BND-17` and (9/9, under the read cap) `BND-18` → `BND-21` rotated verbatim to `thesis/archive/PREDICTIONS_resolved_BND-01_to_BND-17.tsv` and `…_BND-18_to_BND-21.tsv` (crc32 `3942345676`). Resolved tally across all three files: **12 TRUE · 10 FALSE · 1 VOID.**

---

## Trade Interface *(full view → `TRADE.md`; positions are TERRY's construction lane)*

- **TLT puts — HOLD, NO ADD.** The only live add-gate (**DFII10 ≥2.50 sustained**) is **7bp away [9/8]**; closest approach of the episode 5bp [9/2]. Gates (b), (c), (d) are all **RESOLVED-AND-DEAD**. **The OLD conjunctive test that governs the ADD re-arm (WQ-99) did NOT fire at the 9/8 3Y or the 9/9 10Y-R.** ⛔ **Will's standing 7/16 NO-ADD governs; root rule #5; harvest/roll/sizing are TERRY's.** *This bullet states POSTURE, never a direction.*
- **HYG puts — stay closed at the INDEX level.** HY 267, access unimpaired, zero pulled deals, a record IG month in progress. Reopen only on **HY OAS >300 with velocity** (33bp away [9/8]). **The live residue is the CCC tail at 1056 [9/8] — another fresh 2026 high, NOT a series high** (1137, 2025-04-07). Tail widening with an inert index is a **repricing of the worst credits, not a market-function event** ⇒ if it ever arms, the expression is single-name/CCC, never HYG.
- **Credit-equity lead — inactive.** 71bp of headroom [9/8].

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all).** 🔴🔴 **WQ-157 LEG ① RULED 2026-09-04 (Will: *"Approve 157 with your rec"*) — THE LEG IS TIME-SPLIT:**
> ### `I'` STANDALONE THROUGH 2026-09-10; PAIRED THEREAFTER — PAIRING INSTRUMENT OWED (FR2004 weekly join, DATED 9/18).
**Through the refunding: dual-printed, a bare `I'` fire moves NOTHING. After it: `I'` + a NON-AUCTION MECHANISM confirmation (FR2004 dealer stock and/or SOFR−IORB). `I'` stays the 🟠 marker permanently; RETIRE rejected.** ✅ **BOTH STANDALONE EVALUATIONS ARE DONE AND NEITHER FIRED: 9/9 10Y-R +14.13pp, 9/10 30Y-R +16.55pp. THE STANDALONE WINDOW IS NOW CLOSED — from 2026-09-11 `I'` is PAIRED**, and the pairing instrument (FR2004 weekly join) is owed **9/18**. Until it lands the kill leg cannot be evaluated at all; that is a known, dated gap, not a silent one.** Join ceiling: n=243 weekly prints, 2022-01-05 forward (`KB-BND-234`); SBN2022/SBN2024 comparability verdict owed out loud.

🔴 **A composition failure at any coupon auction — TWO definitions dual-printed through 9/10:**
- **NEW (Will-ruled 8/27), auctions graded 8/27 forward:** **indirect below that tenor's own trailing-12 15th PERCENTILE, SUFFICIENT ALONE.** Dealer take **dropped as bearish** (descriptive; >18% = contrarian-**BULLISH**). ★ **ALL SEVEN BARS FROZEN 2026-09-02 (FRN-clean; `monitors/AUCTION_HEALTH.md` §GRADING BASIS): 2Y 54.82 · 3Y 58.90 · 5Y 60.27 · 7Y 57.24 · 10Y 65.05 · 20Y 61.72 · 30Y 62.93.** Remaining: **30Y-R 9/10 <62.93 (alt 60.28) · 20Y-R 9/15 <61.72 (alt 64.66) · 2Y/5Y/7Y 9/22–24 re-freeze at the 9/17 announcement.** 🔴 Base-rated: `I'` fires 15.6–28.1%/auction by tenor with NO TLT-5d separation ⇒ as a KILL leg it cannot discriminate (`KB-BND-222`) — hence the time-split. ✅ **`grade_auction.py` now PRINTS the `I'` line (patched 9/9) and reproduces the frozen bars exactly; the 9/2 snapshot stays the authority.**
- **OLD (retained for the dual-print):** indirect below trailing-12 min **AND** dealer above trailing-12 max, same tenor.
- ⛔ **NAMED EXCEPTION — the TLT-put ADD re-arm in `TRADE.md` runs on the OLD, STRICTER test** (WQ-99, Will 9/1). Never loosen an add gate as a side effect of a definition reconcile.
- 🔴 Direction disclosed: the new test is STRICTLY EASIER TO FIRE, and its firing CONFIRMS this desk's own bear thesis. Percentages are of **competitive accepted**; never reuse another tenor's numbers.

**2 · POSITION-SPECIFIC.** TLT puts: **kill on 10Y <4.15 AND 30Y <5.0 for 3 sessions AND a clean refunding** (THESIS §2 letter), or the thesis kill. ⚠️ *Corrected 9/9: this line read "DFII10 <2.00 sustained 5 sessions" from the 9/1 read-cap compression onward; that exit was never in THESIS. One spec now, on all three surfaces.* Expiry 9/30 and the 60-DTE rail are TERRY's.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal-coupon auctions passing **both** legs (indirect at/above median **and** dealer at/below median). **Counter = 1** (9/9 10Y-R); the 9/8 3Y did not qualify; **TIPS do not count.**

**4 · TIME-BASED.** FR2004 weekly join **9/18** (WQ-157 leg ②). Quarterly percentile-snapshot refresh + `VX-19` "disorderly" definition **10/1**. `VX-20` review **10/6**. FHLB Q3 report **11/9**. FRBNY FX report **11/13**. US-sovereign-CDS re-test **12/1** (L17 answered 9/9: exists at S&P Global, paywalled; no free primary found on 9/9, `re-test: 2026-12-01` — `KB-BND-261`).

⚠️ **RETIRED AND NOT REVIVABLE: the auction TAIL (>2bp)** — TreasuryDirect publishes no when-issued ⇒ unscoreable by construction. Wire tails are `[med-conf]` and may never fire anything.

---

## Immediate Catalysts *(source of truth = `docket/CATALYSTS.tsv`; this is the human twin and must not diverge in event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| ✅ **Thu 9/10 1PM** | **30Y-R `912810UW6` $22B — GRADED CLEAN, refunding leg 3, the LAST `I'`-standalone evaluation** | **BTC 2.61 · ind 79.48 · dir 18.31 · dlr 2.21 · HY 5.3080.** `I'` NOT FIRED **+16.55pp** (alt +19.21) · OLD NOT FIRED both legs · cover NOT FIRED. **Resolved `BND-23` TRUE.** Counter 1→2. `KB-BND-271`. |
| ✅ **Thu 9/10 1:40–2:00PM** | **FIRST STEPPED-UP LONG-END BUYBACK OP — RAN** | **$5.187B accepted of the $6.0B cap (86.5%), 23 of 40 issues; 75.1% into low-coupon deep-discount legacy paper ⇒ OFF-THE-RUN decisively.** F2 flip does NOT trigger; YCC-lite NOT re-adjudicated on n=1. ⚠️ **Offer-to-cover NOT computable** — offered figure null at the primary, `re-test: 2026-09-11`. Packeted to RED. `KB-BND-272`. |
| ✅ **Thu 9/10** | **ECB HIKED 25bp** — deposit facility **2.50%**, MRO 2.65, marginal lending 2.90, effective 9/16; cited Middle East energy inflation | Consensus MET. Guidance **verbatim unchanged**. HANS graded **TACTICAL not regime, 3-1** (comp/employee 3.5→3.3%, ULC 3.5→2.6%, unit PROFITS 0.3→2.2% ⇒ margin channel, not wage channel). **Bund 3.44–3.49 = Apr-2011 high; periphery did NOT widen** (IT–DE +1.6bp, FR–DE +2–4.6bp vs a pre-registered >25bp test). Next GovC **10/29**. `KB-BND-267/268`. |
| **Fri 9/11** | **August MTS** ✅ **re-dated 9/10→9/11 at the FiscalData primary** — the calendar-artifact test | Does August give back most of July's +48.5% YoY spike (FYTD +1.3%)? If not, the calendar explanation dies. Net interest FYTD $931.4B. `KB-BND-260`. |
| **Fri 9/11** | **PROME 8/21 hyperscaler long-dated IG issuance SHARE** — scheduled 9/2 (a second miss ⇒ DECLINE, `KB-BND-227`) | Core MSFT/GOOGL/META/AMZN/ORCL; USD IG tenor ≥10y, 2026 YTD, same perimeter both sides; size first. The record September (~$215B) is the live perimeter. |
| 🔴 **Tue 9/15 1PM** | **20Y REOPENING `912810UX4`** (size 9/10; settles 9/18) — ✅ docketed 9/9 off `docket_check` rc=1 | **BARS FROZEN 9/9:** `I'` <61.72 (alt 64.66) · OLD ind <55.17 AND dlr >17.59 (⚠️ both legs from ONE auction, 2/18) · cover BTC <2.36. **The first long-end auction AFTER the official 10–20Y bid exists — does composition normalize?** (pre-op baseline: 8/19 ind 62.93, −2.03pp vs median). |
| **Tue 9/15 – Wed 9/16** | **SEPTEMBER FOMC — decision + SEP land 9/16** ✅ verified at the Fed primary 8/21 | 2Y as the policy-path leg vs DFII10/30Y as the term-premium leg — the C-36 discriminator. Venue-named pricing only: Polymarket 52.5% / Kalshi 57.0% [ORACLE 9/4 12:42Z]; CME ~62–67% [relayed, not read at CME]. **The unsourced 65–68% is withdrawn (`KB-BND-242`); the provenance cell is archived (crc32 `562960837`).** Rest of 2026: 10/27-28 · 12/8-9 (SEP). |
| 🟠 **Thu 9/17 1PM** | **10Y TIPS REOPENING `91282CRE3`** (size 9/10; settles 9/30) — ✅ docketed 9/9 | **BARS FROZEN 9/9 (10Y TIPS, n=12):** ind <56.08 AND dlr >17.79 · cover BTC <2.20 · median ind 66.94. **No `I'` bar; TIPS do not count toward the downgrade counter.** A real-yield referendum vs the 2.50 add-gate. |
| 🔴 **Fri 9/18** | **FR2004 WEEKLY JOIN — the pairing instrument WQ-157 leg ② is blocked on** (PROME WQ 157 · DOCKET L271) | Join coupon auctions to the contemporaneous FR2004 long-end print (+ SOFR−IORB); base-rate `I'` + mechanism confirmation. **State the SBN2022/SBN2024 comparability verdict.** n ≤ 243. Goes to Will only after it lands. |
| **Tue 9/22 · Wed 9/23 · Thu 9/24** | **2Y · 5Y · 7Y month-end cluster** (+ 2Y FRN-R 9/23, excluded from every bar) — ✅ **dates VERIFIED at the Treasury tentative auction schedule PDF 9/9; CUSIPs/sizes at the 9/17 announcement** | 9/2-snapshot bars 54.82 · 60.27 · 57.24 — **re-freeze trailing-12 strictly prior on 9/17.** Last coupons before quarter-end (SOFR−IORB distortion window). |
| ✅ **9/11 blind span** | **9/11→9/30 HAND-VERIFIED at the issuer PDF 9/9 — DISCHARGED for September**; re-arms for October at the next `docket_check` (feed reach ~5d). Oct: 3Y 10/6 · 10Y-R 10/7 · 30Y-R 10/8 | `KB-BND-262`. |
| **Thu 10/1** | **Quarterly `I'` snapshot refresh** + RED's positive boundary fixture + **define `VX-19`'s "disorderly"** | `monitors/AUCTION_HEALTH.md` §3d rail. |
| **Tue 10/6** | **`VX-BND-20` review** — close the agency-vs-non-agency question on GPFG's ~13% MBS leg at the NBIM primary | Decides whether the ~$82B [EST] is BOND's lane (`VX-17`) or credit's; may revise DOWN (`KB-BND-245`). |
| **Mon 11/9 · Fri 11/13** | **FHLB Q3 combined report** (`REG-T-06` leg 3; `VX-18` re-score) · **FRBNY Q3 FX report** (the 7/30-31 operation's record) | vs $810.7B [6/30/26] · ESF-vs-SOMA split; until it prints `FL-BND-11`'s "intervention = mechanical UST selling" is NOT automatic. |
| **Tue 12/1 · Mon 2027-01-25** | **US-sovereign-CDS re-test** (declined to build; L17 answered) · **Norwegian MoF expert group reports** — the GPFG decision point (`VX-20` hard checkpoint) | Re-test only if a primary series appears · 🔴 upgrade to 4 = an ADOPTED mandate inside 12 months. |
| **— STANDING —** | MOF FX intervention · Warsh task force (end-2026) · buyback accept-cap (FIRED 8/19; F1/F3 at the 11/4 QRA) · FR2004 weekly · credit weekly | UST reserve selling = `FL-BND-11` fires · 2027 lane · YCC-lite tell · `VX-04` · `VX-02/11` |

**Recently resolved** *(rows pruned from the docket 9/9 under the read cap → `domain/sources/2026-09-09_CATALYSTS_rows_pruned.md`, crc32 `2773346310`)*: ✅ **9/8 3Y `91282CRL7` CLEAN** (BTC 2.72 · ind 62.15 · dlr 10.91; 19th benign) · ✅ **9/9 10Y-R `91282CRF0` CLEAN on both conventions** (BTC 2.71 · ind 79.18 · dlr 4.31; 20th benign; **first kill evaluation fired nothing**) · ✅ **`BND-24` TRUE 9/9** · ✅ **9/8 Canadian counter-tariffs — breakeven re-test NULL** (`KB-BND-249`) · ✅ MATRIX_V2 base-rating DELIVERED 9/2 (prune after 9/11) · ✅ `BND-21` TRUE 9/2 · ✅ 8/27 7Y CLEAN.

---

## BOTTOM LINE

**[2026-09-10 Thu ~12:2x–16:xx ET — Will-spawned. Live event day: PPI, the 30Y-R, the first long-end buyback op and the ECB all inside four hours.]**

🟢 **THE REFUNDING CLEARED ON ALL THREE LEGS, AND THE LAST `I'`-STANDALONE KILL EVALUATION FIRED NOTHING BY THE WIDEST MARGIN OF THE THREE.** The 9/10 30Y-R printed **indirect 79.48% (+16.55pp clear), BTC 2.61, dealers 2.21%, high yield 5.3080%**. Against the full corpus (**n=45 nominal 30Y auctions, 2023-01-12 forward** — the window is stated because a superlative without one is this desk's logged error class): **dealer take is the LOWEST of all 45**, indirect is **2nd highest** and **above the trailing-12 max**, BTC is 3rd highest, and **end users took 97.79% of competitive accepted**. `BND-23` **RESOLVED TRUE** against a registered 51% base rate. **21 consecutive benign since 7/9. Downgrade counter 1 → 2; the 9/15 20Y-R is the third chance.**

🔴 **AND IT CUTS AGAINST THIS DESK'S OWN POSITION — said plainly rather than buried.** The auction cleared at **essentially the 2026 DGS30 high on a session the long end sold off hard**. That is *expensive, not broken* in its purest instance yet: the threshold is extreme and the mechanism is not merely intact but **the strongest print in the corpus**. **Level and mechanism are pointing in opposite directions on the same day** — exactly the configuration the frame exists to keep separate, and the direction of the error does not flatter the book.

🟠 **THE ADD-GATE IS THE LIVE QUESTION AND IT IS UNRESOLVED AT WRITE TIME.** August PPI ran **5.4% YoY vs 5.3% expected** — but **core +0.2% MISSED the +0.3% forecast**, so the tape traded a headline whose composition is softer than the print (`KB-BND-264`). The selloff was **front-led** (5s +2.28% / 10s +1.84% / 30s +1.17%) — the policy-path signature, not term premium. Implied DFII10 ≈ **2.51–2.56 `[EST]`**, at or through the 2.50 gate. **Per the breach protocol pre-registered 9/9, an estimate fires NOTHING**; FRED's print decides. **Position UNCHANGED — TLT puts HOLD, no add, $0.** Will's standing 7/16 NO-ADD governs, root rule #5 backstops, and a breach day is a red TLT day ⇒ any add is a root-rule-#6 break needing the measurement on the card first.

🟢 **THE OFFICIAL BID IS REAL AND IT IS OFF-THE-RUN.** The first stepped-up long-end op took **$5.187B of a $6.0B cap (86.5%)**, 23 of 40 issues, with **75.1% concentrated in low-coupon deep-discount legacy paper** (top 3 CUSIPs = 71.3%). **F2 flip does NOT trigger; YCC-lite is NOT re-adjudicated on n=1.** ⚠️ **Offer-to-cover is NOT computable** — the offered figure is null at the primary; `re-test: 2026-09-11`. The unused $813M is **not** evidence of thin offers.

🟠 **Europe:** **ECB hiked 25bp to a 2.50% DFR** on Middle East energy inflation, guidance **verbatim unchanged**; HANS graded it **TACTICAL, 3-1** (the **margin** channel is carrying the pass-through — unit profits 0.3→2.2% while ULC fell 3.5→2.6%). **Bund at an Apr-2011 high with periphery NOT widening.** **UK 30Y gilt 5.94% = a post-1998 high**, 6bp under HANS's band — near-trigger, **not a fire**. Credit: **CCC 1064 = another fresh 2026 high** while HY sits inert at 271.

**Next dated:** 🔴 **9/10 ~4:15PM FRED DFII10 — the gate decides** · 9/11 CPI + MTS + hyperscaler share + FR2004 9/2 as-of (not yet published) · 9/14 `BND-22` resolves · 9/15 20Y-R (counter's third chance) · 9/16 FOMC · 9/17 TIPS-R + BoE gilt-QT pace · **9/18 FR2004 join — the kill leg is UNEVALUABLE until it lands** · 9/22–24 cluster.
