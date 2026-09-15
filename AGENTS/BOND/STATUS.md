# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension, integrated 7/1; + the sovereign-credibility instrument set per the Will-ruled 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-14 ~13:0x ET (PROME WQ-184 L0 spawn, DOCKET L357 — `BND-22` graded FALSE; markets OPEN) · **Prior:** 2026-09-10 ~12:2x–16:xx ET

> 📕 **THIS FILE IS HOT/COLD SPLIT AND ROTATED. NOTHING HAS EVER BEEN DELETED FROM IT.** Complete pre-split snapshot: `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md` (160,077 B, crc32 `1210262`). **Everything rotated since lives in `domain/sources/` and `archive/`, each file verbatim and crc-stamped in its own header — indexed there, not enumerated here** (the enumeration was itself consuming the budget it exists to protect). **Rotated 9/14:** the 9/10 BOTTOM LINE · the resolved-catalysts line · the FR2004 method (→ `analysis/`).
> **What stays hot: every live value, score, gate, exit criterion and dated catalyst. What rotates: riders, teaching quotes, per-auction evidence essays and superseded BOTTOM LINE blocks.** Canon: `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`. **Budget 32,550 B — never raise it; rotate instead.**

**Canonical elsewhere — this file carries NO second copy:** thesis + full falsification → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalyst source of truth → `docket/CATALYSTS.tsv` · positions/gates → `TRADE.md` · durable learnings → `MEMORY.md` · session handoff → `SCRATCH.md`.

---

## Regime (one-line)

**Real-rate / higher-for-longer.** ★ **C-36 = TWO-PART, RULED 2026-09-01: the policy-path channel is ALIVE AND TRANSMITTING · term premium drove the July delta.** ✅ **`BND-24` TRUE 9/9 (+4bp).** 🔴 **The 9/10 add-gate breach is a THIRD front-led observation (2s +13 > 30s +9) — leg 2 again, n=3, still not a path.** Full ruling + caveats: `thesis/THESIS.md` v1.2.3, `thesis/CHANGELOG.md`.

**The configuration, restated:** the long end is engaged (30Y in a **47-session run ≥5.00%**, 63 days in 2026 of 174, **new 2026 high 5.37 [9/10]**) with **no Fed coupon backstop post-QT** ⇒ absorption is entirely private/foreign/dealer — **though from 9/10 an official 10–20Y buyback bid EXISTS AND HAS RUN, off-the-run, at the weakest cover of n=26 (`KB-BND-272/273`).** **Auctions remain "expensive, not broken" — 21 benign since 7/9; the LAST `I'`-standalone kill evaluation (9/10 30Y-R) fired nothing, by +16.55pp.** 🔴 **Credit is inert at the index and DISPERSING underneath it: CCC−BB 926bp [9/11] = the span max, on the same day HY tightened 5bp.**

---

## Current Dashboard

*Every value pulled live via `monitors/boot_recompute.py`, cache-busted **2026-09-14 13:03 ET**, unless tagged. **No naked numbers.***

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.35%** | 🔴 | [CONF FRED **9/11**] — off the 5.37 [9/10] 2026 high by 2bp; **100.0th pctile post-2010**. 48-session run ≥5.00 |
| 10Y (DGS10) | **4.96%** | 🔴 | [CONF FRED **9/11**] — 100.0th pctile post-2010. `GATE-TERRY-007` counter stays **0 of 5** (counts closes <4.50), distance **46bp** |
| 2Y (DGS2) | **4.63%** | 🟠 ↑ | [CONF FRED **9/11**] — 4.43 → 4.56 → **4.63**, +7bp more on 9/11; the front keeps leading |
| **10Y real (DFII10)** | **2.60%** | 🔴 **GATE THROUGH** | [CONF FRED **9/11**] — breach EXTENDED, now **10bp ABOVE the 2.50 add-gate** (2.55 [9/10] → 2.60). `BND-22` FALSE; `BND-28` TRUE. **98.7th pctile full series (n=5,928), 100.0th post-2010** |
| 5Y5Y fwd (T5YIFR) | **2.34%** | 🟡 = | [CONF FRED **9/14**] — publishes ahead of the nominals (H.15 split, `KB-BND-178`); 16bp from its bar |
| 10Y BE (T10YIE) | **2.37%** | 🟡 ↓ | [CONF FRED **9/14**] — 2.40 [9/10] → 2.36 → 2.37: **breakevens fell while the real leg rose ⇒ the 9/10–9/11 move is REAL-led** (`KB-BND-276`) |
| **ACM 10Y term premium** | **0.7073** | 🟠 | [CONF NY Fed `ACMTermPremium` **`ACM Daily` sheet, 9/9**] — ⚠️ **UPGRADED 9/10 from the MONTHLY series this row carried at `+0.73% [Jul-2026]`. A DAILY series exists and publishes AHEAD of our FRED nominals.** 2026 max **0.8935 [8/17]**, min 0.4602 [6/29]. Risk-neutral leg **ACMRNY10 4.1146** |
| **ACM decomposition — the C-36 discriminator, daily** | **9/4 payroll: ΔTP −7.7bp vs Δrisk-neutral +9.2bp** | 🟢 | [CONF NY Fed `ACM Daily`, computed 9/10] — **an INDEPENDENT model confirmation of `BND-24`**: the payroll session was policy-path, not term premium, decomposed rather than proxied off 2s-vs-30s. *(Prior monthly Jul reads 0.8363 now, not the 0.73 this desk carried — ACM is re-estimated, so history revises: a vintage effect, not necessarily an error.)* |
| Kim-Wright 10Y TP (daily) | **0.8892** | 🟠 | [CONF FRED `THREEFYTP10` **9/4**] — 2026 high **0.8996 [9/1]**; +8.1bp on the 9/4 payroll session (one session, recorded not interpreted) |
| **HY OAS** | **265bps** | 🟢 ↓ | [CONF FRED `BAMLH0A0HYM2` **9/11**] — TIGHTENED 5bp on 9/11 (271 [9/9] → 270 [9/10] → 265); still inert at the index |
| **CCC OAS** | **1076bps** | 🟠 ↑ | [CONF FRED `BAMLH0A3HYC` **9/11**] — **another fresh 2026 high** (1064 [9/9] → 1070 [9/10] → 1076). Ratio 4.06x. **BB 150 [9/11] ⇒ CCC−BB 926bp = the MAX of the whole available span** (2023-09-15→9/11, n=785) — see the tail row below |
| IG OAS | **80bps** | 🟢 = | [CONF FRED `BAMLC0A0CM` **9/11**] — September IG supply forecast **~$215B = a record month** [Bloomberg 9/3 poll, secondary]; zero pulled deals |
| 🔴 **CCC−BB tail gap** | **926bp** | 🔴 **SPAN MAX** | [CONF FRED, BOND's own computation **9/11**] — monotonic 5 sessions: 900 → 901 → 906 → 915 → **926**. ⚠️ **On 9/11 the INDEX tightened 5bp, CCC widened 6bp and BB tightened 5bp ⇒ the GAP moved 11bp on a 6bp CCC widening — dispersion, not market function. Name leg, gap and index separately** (`KB-BND-277`) |
| **FR2004 11–21Y** | **$66.8B** [as-of **9/2**] | 🟡 | [CONF NY Fed API `SBN2024`, BOND's own pull **9/14**] — **the 9/2 as-of HAS PUBLISHED** (STATUS carried 8/26 for 4 days; `boot_recompute` part C caught it). +$1.8B w/w = a BUILD |
| SOFR−IORB | **−3bp** | 🟢 | [CONF FRED SOFR 3.62 **9/11** / IORB 3.65 **9/14**] — funding EASIER, not tighter; no auction-stress relay (LIQUID owns) |
| TLT | **$81.19 +0.40%** | 🟠 | [LIVE yfinance **2026-09-14 13:0x ET** — a MOMENT property, re-pull at any decision (root rule #4)] |
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
| **DFII10 ≥2.50 — the ONLY live TLT-put add-gate** | 🔴 **THROUGH by 5bp** [2.55, **9/10**] | 🔴 **THE LEVEL LEG HAS FIRED — FIRST TIME IN THE POSITION'S LIFE.** Breach protocol steps 1–5 executed below. ⛔ **The LEVEL leg firing authorises NO add:** this gate's letter is **"≥2.50 SUSTAINED"** and sustain is **1 of an UNDEFINED count** — see the 🔴 spec defect under the matrix. Will's 7/16 NO-ADD governs, root rule #5, `$0` moved. `BND-22` **RESOLVED FALSE** |
| T5YIFR >2.50 (inflation-unanchor) | 18bp [9/11] | 🟡 |
| DGS30 >5.00 (long-end level) | — | 🔴 **BREACHED**, **47-session run, 63 days in 2026 of 174** [9/10]; **5.37 = new 2026 high** |
| DGS10 >4.50 (arm-#2 line) | — | 🔴 **BREACHED** |
| HY OAS >300 (reopen HYG) | 35bp [9/11] | 🟢 |
| CCC >1100 escalation | **24bp** [9/11] | 🟠 closing fast (36 [9/9] → 30 [9/10] → 24) |
| Credit-equity lead reactivate (HY +75–100 from the 263 trough) | 73–98bp [9/11] | 🟢 inactive |

### 🔴 ADD-GATE BREACH — LEVEL leg through, breach EXTENDED 9/11

**`DFII10` 2.60 [9/11 official] = +10bp through the 2.50 gate** (2.55 [9/10] → 2.60; the breach EXTENDED, it did not fade). **Published sessions ≥2.50: 2 (9/10, 9/11).** ⛔ **Authorises NOTHING:** "sustained" has **no defined session count** (**WQ-246, with Will**), Will's 7/16 NO-ADD governs, root rule #5 backstops. **`$0` moved.**
> 🔴 **SPEC DEFECT ON THE ONLY GATE THAT GOVERNS MONEY — found 9/14, NOT self-repaired.** The gate reads *"DFII10 >2.5% sustained"* with no session count ⇒ unfireable, and it does NOT fail safe (it converts silently to "never add"). `KB-BND-278`.
> **Crowding rider LIVE:** the **9/16 FOMC is TOMORROW** with a hike modal ⇒ **a HOLD is the dovish surprise** and the short-duration consensus covers into it.
> 📌 **Full 9/14 protocol run (steps 1–5, decomposition, TERRY routing) rotated verbatim → `domain/sources/2026-09-15_STATUS_rotated_add-gate-breach-protocol_9-14.md` (crc32 `708486834`); reasoning at `analysis/2026-09-14_add-gate-breach_BND-22-FALSE.md`.**

### FR2004 dealer stock — **9/2 as-of, PUBLISHED and pulled 9/14** (STATUS carried 8/26 for four dark days); the 8/19→8/26 essay is archived verbatim at `monitors/DEALER_CAPACITY_9-4_vintage_note.md`

**One-line state:** 11-21Y **$66.8B (+$1.8B w/w)**, >21Y **$47.0B**, 7-11Y **$30.9B**. **The 11-21Y bucket BUILT for a second consecutive week** — the monitor's *"two consecutive builds on TOTAL"* trigger is the one to watch and is **not yet met on TOTAL**; `VX-BND-04` **HOLDS AT 2** pending the 9/9 as-of. Funding leg **−3bp** (easier). ⚠️ A build into a week whose auctions cleared strongly is **ordinary distribution**, not warehousing — the discriminator needs weak composition or positive SOFR−IORB and has **neither**.

> 🟢 **WQ-157 leg ② PREMISES CLOSED 9/14, BOTH FAVOURABLY** — ceiling **n=244** (VERIFIED); **SBN2022/SBN2024 pooling DEFENSIBLE ⇒ the 2022–23 stress half is NOT lost** (INFERRED, not VERIFIED). ⛔ **THE JOIN ITSELF IS UNBUILT, dated 9/18 — and a live `I'` fire (9/15) now sits on the other side of that gap, so the paired kill is UNEVALUABLE with one leg already lit.** 📌 Detail rotated verbatim → `domain/sources/2026-09-15_STATUS_rotated_WQ157-premises_9-14.md` (crc32 `1106882184`); reasoning at `analysis/2026-09-14_FR2004_SBN2022-SBN2024_comparability-probe.md`.

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **3** = | 🟠 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | **30Y 5.37 [9/10] = a NEW 2026 HIGH**, 47-session run ≥5.00, 63 of 174; **DFII10 2.55 = THROUGH the gate, 98.5th pctile full / 100.0th post-2010**; KW TP 0.8892 [9/4] | DFII10 ≥2.50 sustained, or a fresh DGS30 high with weak composition |
| 2 | Treasury auction health | **2** = | 🟡 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED | **21 consecutive benign since 7/9.** The 9/10 30Y-R was the **strongest composition print in the n=45 corpus** (ind 79.48, +16.55pp; dealers 2.21% = lowest of 45) — **the LAST `I'`-standalone kill evaluation, NOTHING FIRED**; full evidence in the rotated 9/10 BOTTOM LINE | A composition failure (kill spec), or 3 consecutive auctions passing both legs (counter = **2** — 9/9 10Y-R, 9/10 30Y-R; **9/15 20Y-R is the third**) |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | **FR2004 9/2 [pulled 9/14]: 11-21Y $66.8B, +$1.8B w/w = a SECOND consecutive bucket build**; SOFR−IORB −3bp. First long-end buyback op RAN 9/10: **1.748× cover, the weakest of n=26** | A further 11-21Y build **with** weak auction composition or SOFR−IORB positive | ⚠️ **INFERENCE CORRECTED 9/14 — the cap did NOT bind ($813M left unused vs $5.3B tenders rejected) ⇒ `tendered/cap` is not a demand stat here; 'official bid weakened' → AMBIGUOUS. `KB-BND-285`**
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `VX-BND-11` | HY **265 [9/11] TIGHTER**, zero pulled deals, primary open; **CCC 1076 = fresh 2026 high, CCC−BB 926 = span max**, ratio 4.06x | HY OAS >300 with velocity, or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 81; **September supply forecast ~$215B = a RECORD month**, IG yields >5.5% pulling issuers forward (`KB-BND-259`) | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF 0.8585, z20 +1.28, 97th pctile of 3mo = credit-excess RICH, no divergence [9/8] | Synthetic leading cash on a sustained basis |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY 71bp below the reactivation band | HY +75–100bp from the 263 trough while VIX <20 |

**Composite: 12/35 — UNCHANGED for a THIRTEENTH consecutive scoring session** (… 9/9 · 9/10 · **9/14**). ⚠️ *The hold is now the HARDER call: the add-gate LEVEL is through and the 30Y made a new 2026 high — but row 1's trigger reads **"≥2.50 SUSTAINED"**, sustain is **1 session with the next cell unpublished**, and the qualifier has **no defined count**. ⛔ **The same undefined qualifier that blocks the ADD blocks this UPGRADE** — held at 3 on a technicality, not judgement, and stated rather than resolved by picking a number. The other branch (new DGS30 high **with weak composition**) fired its first half only: the 9/10 30Y-R was the corpus's STRONGEST composition print.* Distribution: 🟠 1 · 🟡 3 · 🟢 3 · 🔴 0.
**Re-summed and verified against the vector scores this session: 3+2+2+2+1+1+1 = 12.** ✅

**Tracked OUTSIDE the composite** (they enter the matrix only when they earn weight): `VX-BND-15` inflation-expectations anchoring (2) · `VX-BND-17` MBS / housing-finance relay (1, re-armed 9/4) · `VX-BND-18` FHLB advances (2) · **`VX-BND-19` eurozone rates / ECB shock (3)** — ECB hiked 25bp to 2.50% DFR 9/10; ⚠️ **spec defect, logged not fixed: "OAT-Bund >85bp" is AT its bar and "Bund >3.25 DISORDERLY" has its level met with the qualifier UNDEFINED ⇒ unfireable — define at the 10/1 refresh (`KB-BND-256`). Same defect class as the add-gate's above, now found twice on this desk.** · **`VX-BND-20` benchmark-driven structural UST demand (2)** — NBIM's 9/1 GPFG proposal (US govt 34.1%→21.9% ≈ −$80B; USD share unchanged ⇒ rotation into US MBS, **not** de-dollarization). Checkpoint **10/6**, expert group 2027-01-25. **Full surface → `monitors/BENCHMARK_DEMAND.md`.** Zero effect on the refunding.

> ⚠️ **OPEN MIRROR DIVERGENCE, un-reconciled (5th session): `VX-BND-05` = 4 and `VX-BND-16` = 4 in `workbook/VX.tsv` vs matrix rows 3 and 2 — the COMPONENTS are HOTTER than the matrix, i.e. the divergence runs toward UNDER-stating risk.** Flagged, not silently reconciled (`[[finding_reconcile_mismatch_does_not_say_which_side_is_wrong]]`). Full notice archived (crc32 `2218422141`) at `domain/sources/2026-09-04_STATUS_archive_mirror-divergence-notice.md`.

⚠️ **It held against evidence pushing BOTH ways this session:** bearish — CCC made another 2026 high, the 30Y run reached 45 sessions, Bund/OAT/BTP at 2011-era highs into an ECB hike, the 10Y-R stopped at a 2007-era yield. Bullish/neutral — the 3Y and 10Y-R were clean on both definitions (the first kill evaluation fired nothing), the add-gate backed off to 7bp, SOFR−IORB is negative, dealer stock rebuilt, September IG supply is a record. **Nothing crossed a pre-registered line.** Downgrade counter **1** (the 10Y-R; the 3Y's below-median indirect did not qualify; TIPS never count).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

✅ **OPEN: 4** — `BND-25` (belly-led FOMC session, 55%) · `BND-26` (1y1y fwd <4.95 thru 9/23, 70%) · `BND-27` (CCC <1100 thru 9/30, 65%) · `BND-29` (≥3 of the first 5 published `DFII10` sessions ≥2.50, 70%). 🟢 **`BND-28` RESOLVED TRUE 2026-09-15 at 80% ⇒ a HIT** — FRED published the 9/11 `DFII10` cell (2.60), dated cache-busted check inside the window; the four-day H.15 stall was a RELEASE ARTIFACT, as its registration reasoning argued. ⚠️ **`BND-29` advances to 2-of-2 (9/10 2.55, 9/11 2.60) and stays OPEN** — calling a 5-session letter at 2-of-2 is the mirror of the error its session-set clause prevents. 🟠 **`BND-27` is in-window from today and momentum runs AGAINST the TRUE side**: CCC 1064→1070→1076, three consecutive sessions, **24bp** from the 1100 line.
**Live file holds `BND-25` → `BND-29` (all OPEN); `BND-22`→`BND-24` rotated verbatim 9/14 to `thesis/archive/PREDICTIONS_resolved_BND-22_to_BND-24.tsv` (crc32 `2391597581`) under the read cap**; `BND-01` → `BND-17` and (9/9, under the read cap) `BND-18` → `BND-21` rotated verbatim to `thesis/archive/PREDICTIONS_resolved_BND-01_to_BND-17.tsv` and `…_BND-18_to_BND-21.tsv` (crc32 `3942345676`). Resolved tally across all archive files: **12 TRUE · 11 FALSE · 1 VOID.**

---

## Trade Interface *(full view → `TRADE.md`; positions are TERRY's construction lane)*

- **TLT puts — HOLD, NO ADD.** 🔴 The only live add-gate (**DFII10 ≥2.50 sustained**) is **THROUGH ON ITS LEVEL LEG for the first time — 2.55 [9/10], +5bp**; the SUSTAIN leg is **1 session, undefined count, next cell unpublished**. **A LEVEL FIRING IS NOT AN ADD.** Gates (b)/(c)/(d) **RESOLVED-AND-DEAD**; the OLD conjunctive test governing the ADD re-arm (WQ-99) did NOT fire at the 9/8 3Y or 9/9 10Y-R. ⛔ **Will's 7/16 NO-ADD governs; root rule #5; harvest/roll/sizing are TERRY's.** *POSTURE, never a direction.*
- **HYG puts — stay closed at the INDEX level.** HY **265 [9/11] — it TIGHTENED**; access unimpaired, zero pulled deals, record IG month. Reopen only on **HY OAS >300 with velocity** (35bp). **Residue = the CCC tail: 1076, CCC−BB 926 = span max, on the day the index tightened.** Tail-widening under an inert index is a **repricing of the worst credits, not market function** ⇒ if it arms: single-name/CCC, never HYG.
- **Credit-equity lead — inactive.** 73bp headroom [9/11].

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all).** 🔴🔴 **WQ-157 LEG ① RULED 2026-09-04 (Will: *"Approve 157 with your rec"*) — THE LEG IS TIME-SPLIT:**
> ### `I'` STANDALONE THROUGH 2026-09-10; PAIRED THEREAFTER — PAIRING INSTRUMENT OWED (FR2004 weekly join, DATED 9/18).
✅ **BOTH STANDALONE EVALUATIONS DONE, NEITHER FIRED** (9/9 +14.13pp · 9/10 +16.55pp). 🔴 **THE STANDALONE WINDOW CLOSED 9/10 — from 9/11 `I'` is PAIRED** with a non-auction confirmation (FR2004 stock and/or SOFR−IORB), owed **9/18**. ⛔ **Until it lands the kill leg CANNOT BE EVALUATED AT ALL** — a dated gap, and **it spans the 9/15 20Y-R and the 9/16 FOMC**. Ceiling n=244 + comparability: FR2004 block above (`KB-BND-234/279`).

🔴 **A composition failure at any coupon auction — TWO definitions dual-printed through 9/10:**
- **NEW (Will-ruled 8/27), graded 8/27 forward:** **indirect below that tenor's own trailing-12 15th PERCENTILE, SUFFICIENT ALONE**; dealer take dropped as bearish (>18% = contrarian-**BULLISH**). ★ **Bars FROZEN 9/2 — canonical at `monitors/AUCTION_HEALTH.md` §GRADING BASIS.** 🔴 **FIRST LIVE FIRE 2026-09-15 (20Y-R, −9.25pp) — and the first print where this test and the OLD one DISAGREE IN VERDICT**, which is the strongest evidence yet that the 8/27 ruling changed something real. Next: 9/22 2Y · 9/23 5Y · 9/24 7Y (re-freeze at the 9/17 announcement).
- **OLD (retained for the dual-print):** indirect below trailing-12 min **AND** dealer above trailing-12 max, same tenor.
- ⛔ **NAMED EXCEPTION — the TLT-put ADD re-arm in `TRADE.md` runs on the OLD, STRICTER test** (WQ-99, Will 9/1). Never loosen an add gate as a side effect of a definition reconcile.
- 🔴 Direction disclosed: the new test is STRICTLY EASIER TO FIRE, and its firing CONFIRMS this desk's own bear thesis. Percentages are of **competitive accepted**; never reuse another tenor's numbers.

**2 · POSITION-SPECIFIC.** TLT puts: **kill on 10Y <4.15 AND 30Y <5.0 for 3 sessions AND a clean refunding** (THESIS §2 letter), or the thesis kill. ⚠️ *Corrected 9/9: this line read "DFII10 <2.00 sustained 5 sessions" from the 9/1 read-cap compression onward; that exit was never in THESIS. One spec now, on all three surfaces.* Expiry 9/30 and the 60-DTE rail are TERRY's.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal-coupon auctions passing **both** legs (indirect at/above median **and** dealer at/below median). **Counter = 0 — RESET by the 9/15 20Y-R**, which failed both legs (ind 52.47 < median 64.95; dlr 16.85 > median 9.88). It had reached **2** (9/9 10Y-R, 9/10 30Y-R); the 9/8 3Y did not qualify; **TIPS do not count.**

**4 · TIME-BASED.** FR2004 weekly join **9/18** (WQ-157 leg ②). Quarterly percentile-snapshot refresh + `VX-19` "disorderly" definition **10/1**. `VX-20` review **10/6**. FHLB Q3 report **11/9**. FRBNY FX report **11/13**. US-sovereign-CDS re-test **12/1** (L17 answered 9/9: exists at S&P Global, paywalled; no free primary found on 9/9, `re-test: 2026-12-01` — `KB-BND-261`).

⚠️ **RETIRED AND NOT REVIVABLE: the auction TAIL (>2bp)** — TreasuryDirect publishes no when-issued ⇒ unscoreable by construction. Wire tails are `[med-conf]` and may never fire anything.

---

## Immediate Catalysts *(source of truth = `docket/CATALYSTS.tsv`; this is the human twin and must not diverge in event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| ✅ **Thu 9/10 1PM** | **30Y-R `912810UW6` $22B — GRADED CLEAN, refunding leg 3, the LAST `I'`-standalone evaluation** | **BTC 2.61 · ind 79.48 · dir 18.31 · dlr 2.21 · HY 5.3080.** `I'` NOT FIRED **+16.55pp** (alt +19.21) · OLD NOT FIRED both legs · cover NOT FIRED. **Resolved `BND-23` TRUE.** Counter 1→2. `KB-BND-271`. |
| **Fri 9/11** | **August MTS** ✅ **re-dated 9/10→9/11 at the FiscalData primary** — the calendar-artifact test | Does August give back most of July's +48.5% YoY spike (FYTD +1.3%)? If not, the calendar explanation dies. Net interest FYTD $931.4B. `KB-BND-260`. |
| **Fri 9/11** | **PROME 8/21 hyperscaler long-dated IG issuance SHARE** — scheduled 9/2 (a second miss ⇒ DECLINE, `KB-BND-227`) | Core MSFT/GOOGL/META/AMZN/ORCL; USD IG tenor ≥10y, 2026 YTD, same perimeter both sides; size first. The record September (~$215B) is the live perimeter. |
| ✅ **Tue 9/15 1PM — GRADED** | **20Y-R `912810UX4` $13B — 🔴 THE FIRST `I'` FIRE** | **BTC 2.57 · ind 52.47 · dir 30.68 · dlr 16.85 · HY 5.4200.** `I'` pooled 61.72 → **FIRED −9.25pp**; alt 64.66 → FIRED −12.20pp — **both conventions agree.** OLD conj **NOT fired** (dealer leg −0.74pp). Cover not fired (+0.21). **Counter RESET 2 → 0.** ⛔ **🟠 MARKER, NOT A KILL** (paired since 9/11; FR2004 leg ② unbuilt). 🔑 **ind = lowest 20Y in the feed WHILE dir = highest of the modern series ⇒ bid SUBSTITUTED, mechanism did NOT fail.** → `analysis/2026-09-15_GRADE_20Y-R_912810UX4.md` |
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

**Recently resolved** → rotated verbatim 9/14 to `domain/sources/2026-09-14_STATUS_archive_recently-resolved_through-9-10.md`. **9/8 3Y · 9/9 10Y-R · 9/10 30Y-R all CLEAN.**

---

## BOTTOM LINE

**[2026-09-15 Tue ~13:0x–13:4x ET — PROME WQ-184 Tier-1 L0 spawn on DOCKET L316. Markets OPEN. FOMC TOMORROW.]**
*(9/14 block rotated verbatim → `domain/sources/2026-09-15_STATUS_archive_bottomline_9-14.md`, crc32 `2991186258`.)*

🔴 **THE `I'` COMPOSITION TEST FIRED FOR THE FIRST TIME — AND IT IS A 🟠 MARKER, NOT A KILL, BY A RULE WRITTEN BEFORE THE PRINT.** The 9/15 20Y-R `912810UX4` ($13B) printed **indirect 52.47%** against a bar of **61.72** frozen 2026-09-09 — **−9.25pp**, and −12.20pp against the reopening-only alt, so **both conventions agree and this is not the ambiguous case.** **From 9/11 the kill is PAIRED** (`I'` **AND** a non-auction mechanism confirmation) and the pairing instrument — the **FR2004 join, 9/18** — **is UNBUILT.** The ceiling was registered in the pre-print record committed **10:06:44 ET, before the auction existed**, precisely so a bearish print could not be promoted afterwards. **No position action. `$0`.**

🔑 **THE BID WAS SUBSTITUTED, NOT WITHDRAWN — AND THAT IS THE READ THAT MATTERS.** Indirect **52.47% is the LOWEST on any 20Y in the TreasuryDirect feed** while **direct 30.68% is the HIGHEST of the modern series (n=78)**, in the same print. Dealers took 16.85% — elevated, but **below** the trailing-12 max (17.59) and below the 18% contrarian-bullish line. **BTC 2.57, fully covered.** ⇒ **THE MECHANISM DID NOT FAIL.** And the high yield **5.4200% is the richest any 20Y has ever cleared at in the modern series** — the indirect bid stepped back at a record yield and *domestic real money took the other side.*

⚠️ **ATTRIBUTION IS NOT SETTLED, AND MY OWN PRE-REGISTRATION BINDS ME.** I wrote before the print that a WEAK result today would be **FOMC-confounded** (a buyer facing a dot plot in 24h can just wait) and that the STRONG result was the high-information one. **The weak one arrived, so I do not now get to promote its informativeness.** But the signature does **not** match pure deferral — deferral predicts weak cover and stuffed dealers; instead cover held and direct hit a record. **"Indirect declined at 5.42% the day before a dot plot" and "indirect is structurally stepping away" both remain live, and this print does not separate them.** The instrument that would is the FR2004 join — the same gap the verdict ceiling rests on.

⬜ **THE OLD CONJUNCTIVE TEST DID NOT FIRE, BY 0.74pp ON THE DEALER LEG — AND IT BEHAVED EXACTLY AS NAMED AT AUTHORSHIP.** It is calibrated to reproduce **one** auction (2026-02-18, ind 55.17 **and** dlr 17.59, both legs from that single print). Today was **worse on indirect, better on dealer**, so the repeat-detector saw no repeat. **This is the first live print where the two tests DISAGREE IN VERDICT** — the strongest evidence yet that the 8/27 ruling changed something real rather than relabelling it. ⛔ **The TLT-put ADD re-arm keys on the OLD test, so this print does NOT re-arm the add either.**

⬜ **CONVERGENCE-DOWNGRADE COUNTER RESET 2 → 0.** No trim signal. 🔴 **And the counter's value was itself a finding**: at boot it read **0 / 1 / 2 across three surfaces**, and the two that were WRONG were the two a cold session would ACT on — an exit rule and a monitor rail. Adjudicated at the TreasuryDirect primary, **not by majority — 2-of-3 would have returned the wrong answer.** `KB-BND-287`.

🔴 **`DFII10` 2.60 [9/11] — THE ADD-GATE BREACH EXTENDED, +10bp THROUGH, and still authorises nothing.** The H.15 four-day stall cleared and **`BND-28` resolved TRUE at 80%**. **2 published sessions ≥2.50.** "Sustained" still has **no session count** (**WQ-246, with Will**); Will's 7/16 NO-ADD governs; root rule #5 backstops.

🔴 **INSTRUMENT DEFECT FOUND IN LIVE USE ON THE KILL LEG:** `grade_auction.py` **silently skipped the governing `I'` test** outside the repo venv (bare `except` on the numpy import) and printed a confident verdict from the RETIRED test reading *"does NOT meet the failure test"* — a clean, wrong-referenced, **false-negative** exit, under exactly the condition a grader is run in a hurry. Patched to fail loud; **IMPLEMENTED and TESTED, NOT independently verified** — the tool has **no `--selftest`**, so the repair has no regression guard. `KB-BND-292`.

**Position: TLT puts HOLD, no add, `$0`. Composite 12/35, fourteenth consecutive.** Live at fire-time: TLT **$80.52** (−0.51%), TLH $94.68. Grade → `analysis/2026-09-15_GRADE_20Y-R_912810UX4.md`; pre-print record → `analysis/2026-09-15_PREPRINT_20Y-R_912810UX4_and_TIPS-R_91282CRE3.md`.

**Next dated:** 🔴 **9/16 FOMC 14:00 ET + SEP/dot plot — TOMORROW. The hike is ~85% PRICED (`C3`), so THE DECISION IS NOT THE EVENT; THE PATH IS.** The curve already prices ~115–130bp more tightening (terminal ~4.75–4.95, no cut in 3yrs), so a hawkish plot must beat ~4.95 to surprise while a **dovish** plot is a large repricing that would unwind the very move that fired our add-gate (`KB-BND-283`). **Pre-registered falsifier: a SEP median terminal ≥~5.00% with the curve unchanged means the hawkish path was NOT fully priced and my asymmetry read is WRONG.** · 🟠 **9/17 10Y TIPS-R `91282CRE3` $19B** (bars frozen 9/9: ind <56.08 AND dlr >17.79 · cover <2.20; **no `I'` bar, TIPS never count toward the counter**) + the 9/17 announcement **re-freeze of the 2Y/5Y/7Y bars** · 🔴 **9/18 FR2004 JOIN — the kill leg is UNEVALUABLE until it lands, and a live `I'` fire is now sitting on the other side of that gap** · 9/22–24 cluster · **October docketed 9/15** (3Y 10/6 → QRA 11/4, 7 rows).
