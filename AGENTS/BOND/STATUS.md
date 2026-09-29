# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension; + the sovereign-credibility instrument set per the 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-29 Tue — 12:3x–13:1x ET Will boot + PROME doorbell (live read: session 5, long-end-led, US-originated; WQ-317 same-day PARTIAL) · 10:24 ET PROME spawn (row-4 observation + L0 drain) · 2026-09-28 Mon ×3 sessions (official 9/28 curve · front-end deep-dive · `rates_context.py` build · positions ×15/×1) · earlier: 9/26 · 9/25 · 9/24

> 📕 **HOT/COLD SPLIT — NOTHING DELETED.** Pre-rotation snapshots (`domain/sources/`): **`2026-09-29b_STATUS_full-snapshot_pre-intraday-rotation.md` (crc32 `2392892541`)** · `2026-09-29_…pre-row4-rotation` (`2518256656`) · `2026-09-28e` (`2516058915`) · `2026-09-28d` (`319142979`) · `2026-09-28c` (`1800580424`) · `2026-09-28b` (`2552442073`) · older `2026-09-28_` · `2026-09-24`. **Budget 32,550 B; rotate-tier ≥75% — rotate, never raise.**

**Canonical elsewhere — no second copy here:** thesis → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalysts → `docket/CATALYSTS.tsv` · gates/positions → `TRADE.md` · learnings → `MEMORY.md` · handoff → `SCRATCH.md`.

---

## 🔴 TOP OF FILE — what changed since 9/24

0000000. 🔴 **[9/29 OFFICIAL, published 15:55 ET] SESSION 5 — BEAR STEEPENER, LONG END LED, PATH FELL** (`KB-BND-367`): 30Y **5.59** (+3; **5th straight fresh 2026 high, highest close since 2004-05-14**; run ≥5.00 = **60**) · 20Y 5.64 (+4; since 2002-07-05) · 10Y **5.26** (+2; **matches 2007-06-12, does not exceed it**) · 5Y 5.06 (0) · **2Y 4.89 (−3)** · DFII10 **2.91** (+1) · 10Y BE 2.35 (+1). **2s30s 64→70.** The priced Fed path fell ~5bp in the afternoon (10/28 ≈50%, was 68%; `KB-BND-365`) while the long end held ⇒ the day's net move is duration, not hikes — TP-consistent, **graded by `BND-30`** (ACM 9/29 row). Same-day attribution PARTIAL (`KB-BND-362`): **US-ORIGINATED** — Bund −3, gilt +1, JGB flat, oil down, consumer confidence 81.9 (weakest since 2014) at 10:00 with the 30Y +2bp into it; EXPORTING untested until Tokyo 9/30 (`BND-31`); Fed-speaker and supply cells SEARCH-NOT-FOUND (WALTER). **Book (`KB-BND-363/365`): TLT 78.24 [15:56 ET] → BE 76.89 needs ≈+10–11bp on the 20+Y yield by the 9/30 close; base rate ~5%. No BOND action; no rec.** ⛔ No matrix move: row 1 stays 4 (fresh highs are not the ⇒5 letter; that needs a long-end composition failure 10/7–10/8).
000000. 🟠 **[9/29 10:2x ET] ROW 4 MET → 3 — composite 14 → 15/35** (`KB-BND-359`; FRED direct, first-published 9/28 cells, read 10:24 ET). **Letter (matrix row 4 Upgrade Trigger): "HY >300 with velocity."** HY OAS **302 (+9)** > 300 ✅ · velocity **+29bp/3 sessions (9/23→9/28) = 98th pct** of 782 three-session windows since 2023-09-30 ✅. ⛔ **A BOND marker only — NOT a capital reopen** (X1 CLOSED 8/28; BROCK's 10/02 sitting, DOCKET L494 → TERRY + Will). ⚠️ One first-published cell, 2bp over the line; ICE cells can revise — a revision to ≤300 re-grades. **Next observations (15-session, LIQUID's letters — LIQUID grades):** B **+32** (≥ +28 ✅, 1st qualifying obs of D1's 3) · BB +28 · **IG +2 (< +6) · BBB +3 (< +7) → NOT met.** **Broad repricing: STILL NOT SHOWN on the letter** — but IG/BBB 3-session speed (+6/+7, ≈97th pct) is the first move beyond high yield. CCC **1146 = new 3y-span max** (was 1137 [2025-04-07]). HY yield **8.03%** (+16).
00000. 🔴 **[9/28] Official curve + what repriced** (`KB-BND-350`, `KB-BND-353`, `KB-BND-357`): 30Y **5.56** (highest since 2004-06) · 10Y 5.24 · 2Y 4.92 (+11) · DFII10 2.90; real-led; repricing grew with horizon (terminal/2027 path); driver WIRE-ATTRIBUTED (oil/Iran, hike odds, global sell-off), oil **not in breakevens**. No matrix move.
0000. 🟢 **[9/28] `monitors/rates_context.py` every boot** (`KB-BND-354`/`356`; WQ-327 v2): Fed path · ACM/KW TP · VX-17 watcher; FF strip vs ACM ≠ a causal split (CATO). Found Dec 9 FOMC missing → docketed.
000. 🟠 **[9/28] Corrections + credit:** ① HY >300 = row-4 marker, NOT a capital reopen (`KB-BND-348`) · ② CCC refi wall narrow, 2026–27 tail UNMEASURED (`KB-BND-349`) · ③ HY access OPEN for large credits, pulled-deal leg a GAP (`KB-BND-346`).
1. **L477 Q3/Q4 contributions (9/25)** → `KB-BND-336` + snapshot `2026-09-29b` · **Carried 9/24–9/26** → snapshot `2026-09-28d` (BND-27 FALSE · WQ-291/246 encoded · WQ-280 ADD DECLINED · BND-26 FALSE · FR2004 trade-date basis `KB-BND-332`).

## Regime (one-line)

**Real-rate / higher-for-longer — and the policy path is still repricing HAWKISHLY.** C-36 TWO-PART (ruled 9/1): policy-path channel ALIVE · term premium drove the July delta. **9/16 FOMC +25bp to 3.75–4.00 (12–0); the curve priced ABOVE the SEP median (4.125) and then kept going (`BND-26`).** **Auctions: "expensive, not broken" is UNDER TEST — first OLD-conjunctive fire on the live-graded record (9/23 5Y), calm funding; dealer leg prints 10/1.** Full ruling → `thesis/THESIS.md`.

---

## Current Dashboard

*Rates rows updated **2026-09-28 16:19 ET to the OFFICIAL 9/28 Treasury par/real cells** (FRED frontier still 9/25). Credit rows pulled live **2026-09-28 10:34–10:43 ET (intraday; B/BBB tiers 10:43–11:11)** via `monitors/boot_recompute.py` + `fetch.py` (cache-busted) + the U.S. Treasury par/real curve CSV for the **9/25 official cells** (FRED frontier is 9/24 for H.15; credit 9/25). Intraday vendor marks are labelled and are NOT official closes. No naked numbers.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.59%** | 🔴🔴 | [CONF **U.S. Treasury par curve 9/29**, published 15:55 ET = H.15 source; FRED 5.49 [9/25]] — **+3bp; 5th straight fresh 2026 high; highest close since 2004-05-14**; run ≥5.00 = **60** on the Treasury cell; 5 consecutive up closes. 20Y **5.64** (+4; since 2002-07-05) |
| 10Y (DGS10) | **5.26%** | 🔴 | [CONF Treasury **9/29**; FRED 5.17 [9/25]] — **+2bp; MATCHES the 2007-06-12 close (5.26), does not exceed it** (BOND computation, FRED full series) |
| 5Y (DGS5) | **5.06%** | 🔴 | [CONF Treasury **9/29**, unch] |
| 2Y · 1Y | **4.89% · 4.58%** | 🔴 | [CONF Treasury **9/29**] — **2Y −3 (front end RALLIED as the priced path fell ~5bp)**; 1y1y ≈ **5.20** (2×2Y−1Y par approx; 5.25 [9/28]). 2s10s +37, **2s30s +70** (was 64: **bear STEEPENER on 9/29**, long-end-led) |
| **10Y real (DFII10)** | **2.91%** | 🔴🔴 **GATE THROUGH · SUSTAIN MET** | [CONF **Treasury real curve 9/29**, +1; FRED 2.83 [9/25]] — **17 sessions ever ≥ it, last 2008-11-24; 99.7th pct since 2003**. 30Y real 3.29, 5Y real 2.72. **WQ-246 count: 11 consecutive FRED closes ≥2.50 (9/10–9/24), 13 on the Treasury cell** — met, authorises no add |
| 5Y5Y fwd (T5YIFR) | **2.35%** | 🟡 | [CONF FRED **9/28**] — **15bp from 2.50** |
| 10Y BE (T10YIE) | **2.35%** | 🟡 | [Treasury par−real **9/29** = 2.35 (+1); FRED T10YIE 2.34 [9/28]] — **9/29 at the 10Y: +1 real +1 BE = flat/mixed**; 9/28 was real-led (real +7, BE 0) |
| ACM 10Y TP · KW TP | **0.7747** [9/25] · **0.9595** [9/18] | 🟠 ↑ | [NY Fed ACM Daily · FRED `THREEFYTP10`, **now pulled every boot by `monitors/rates_context.py`** (17:38 ET 9/28)] — ACM **+13.9bp over 5 obs**; KW −0.1 over 5 obs (frontier 10d old). *Different window/horizon from the FF strip: consistent with both channels, not a causal split (CATO 9/28).* FORUM-7 P2 (KW 9/21–9/24) = HENRY's lead. **Name the model in any TP claim** |
| **Fed path (FF futures)** | **peak of available strip 4.855% [Nov-27; strip Sep-26→Jan-28]** · 10/28 hike ≈**68%** (hold-or-+25 reading) | 🟠 ↑ | [CBOT ZQ via yfinance, **vendor last trade, NOT settlement**, read 17:38 ET 9/28; EFFR 3.88 [9/25]; every boot via `rates_context.py`] — terminal **+97.5bp ≈ 3.9 hikes**, **+18bp over 5 obs**; Jan-28 −4.5 from peak. HENRY owns the read; BOND consumes |
| **HY OAS** | **302bps** | 🟠 ↑ | [CONF FRED **9/28**, first-published, read 10:24 ET 9/29] — **+9; +29bp in 3 sessions (98th pct, 3y span)**; **through 300 by 2bp = row 4 MET**; 2026 max 346. HY yield 8.03% |
| **CCC OAS** | **1146bps** | 🔴 ↑ | [CONF FRED **9/28**] — +18; **new 3y-span max** (was 1137 [2025-04-07]); 1100 escalation FIRED 9/24 |
| IG · BBB · BB · B OAS | **83 · 102 · 183 · 309bps** | 🟢 · 🟢 · 🟡 ↑ · 🟡 ↑ | [CONF FRED **9/28**] — 15-session: IG +2 · BBB +3 · BB +28 · B +32 |
| CCC−BB tail gap | **963bp** | 🔴 ↑ | [CONF FRED, BOND computation **9/28**] — new span max (952 [9/25]) |
| **FR2004 long-end** | **$144.4B** [as-of 9/16] | 🟡 | [NY Fed, published 9/24 16:16 ET] — −$1.8B w/w; 11-21Y $68.5B (+1.7), >21Y $40.8B (−2.6). **Next: as-of 9/23 Thu 10/1 ~16:15 = the WQ-291 3–6Y grade (≥ $56.586B)** |
| **SOFR − IORB** | **0bp** | 🟡 ↑ | [CONF FRED SOFR 3.90 · IORB 3.90, **9/25**] — up from −3 [9/23] into quarter-end; not positive. LIQUID owns |
| TLT · MOVE | **$78.10 −0.67%** [9/29 12:3x ET intraday, yfinance; 78.62 close-area 9/28] · **106.80 +4.9%** [vendor ^MOVE 9/29 12:3x ET; 96.00 vendor 9/25 / 104.58 VIOLET 9/24] | 🟠 · 🔴 | [yfinance — a MOMENT property, re-pull at any decision, root rule #4] 77P strike **1.4% below spot**, expiry **TOMORROW 9/30**. MOVE: two sources disagreed last week, VIOLET owns |
| Global 10Y | → HANS (EU/UK) · SAM (JGB) | `[HANS/SAM own]` | 9/29 same-day secondary snapshot in `KB-BND-362` (Bund −3 · gilt +1 · JGB flat); the dated cross-market read is the **WQ-317 page (10/2)**. Name the basis (`KB-BND-319`) |
| USD/JPY · oil · VIX | **cite SAM · BRENT · VIOLET** | — | this desk keeps no copy (vendor Brent front quote on 9/28 looks like a roll artifact — do not use) |

### Gate distances *(recomputed this session, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — TLT-put add-gate (a)** | 🔴 **THROUGH by 41bp** [2.91, Treasury 9/29] · 33bp [2.83, FRED 9/25] | **Sustain leg MET under WQ-246 (5 consecutive; 11 FRED closes)** — authorises NO add (NO-ADD 7/16 + WQ-280) |
| **Auction re-arm (OLD conjunctive) — TLT-put add-gate** | 🔴 **MET 9/23 (5Y)** | ✅ **ADD DECLINED — WQ-280 RULED 9/24 13:17 ET.** Spent on 004 |
| **Kill dealer leg, 9/23 5Y (WQ-291)** | as-of 9/23 must be ≥ **$56.586B** (PRE $47.986B) | ⏳ prints **Thu 10/1 ~16:15**; funding window for this fire **UNGRADED** by ruling |
| T5YIFR >2.50 | 15bp [9/28; FRED 9/29 cell posts ~9/30] | 🟡 |
| DGS30 >5.00 · DGS10 >4.50 | — | 🔴 BREACHED (run **60**, Treasury cell 9/29) · 🔴 BREACHED |
| HY OAS >300 (BOND row-4 marker — **not** a capital reopen; X1 CLOSED 8/28) | **THROUGH by 2bp** [302, 9/28] | 🟠 **MET 9/29 → row 4 = 3** |
| CCC >1100 escalation | **FIRED 9/24** (+12; +28 on 9/25) | 🔴 `BND-27` FALSE |
| Credit-equity lead (HY +75–100 from the 263 trough, VIX <20) | 36–61bp | 🟡 moving (HY 302 [9/28]; VIX → VIOLET) |

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **4** = | 🔴 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | Moved 3→4 on 9/23 (fresh DGS30 high WITH weak composition). **Since: 5.47 [9/24] → 5.49 [9/25] = 3rd straight fresh high; 9/28 intraday vendor 5.55; global sell-off 4th session** (`KB-BND-340`) — fresh highs are not the ⇒5 letter | ⇒5: a composition failure on a LONG-END auction (next: 10/7 10Y-R, 10/8 30Y-R) or the paired kill's mechanism leg confirming |
| 2 | Treasury auction health | **3** ▲ | 🟠 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED (tail) | **9/23 5Y: BTC 2.21 < 2.28 cover bar (<2.3 marker) + OLD composition failure + `I'`; 7Y `I'` by 0.04pp.** ⛔ `I'` alone = MARKER (WQ-157 ② PARKED 9/25). Paired kill NOT fired (funding NONE per LIQUID); **FR2004 POST for the 9/23 5Y = the 9/23 as-of, Thu 10/1** (trade-date basis `KB-BND-332`) | A composition failure with the funding/FR2004 leg CONFIRMED (paired kill) ⇒ 4 |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | FR2004 9/16 long-end $144.4B (−$1.8B; 11–21Y +1.7, >21Y −2.6), admissible (trade-date, `KB-BND-332`); next: 9/23 as-of Thu 10/1 = the 5Y's POST; 5Y dealer 15.77 = trailing-12 max but ordinary vs 2023–24. **9/24 20–30Y buyback $4.078B of $6B, F2 0.02% ⇒ OFF-THE-RUN (2 of 2 ops)** | Two consecutive builds on TOTAL with weak composition, or SOFR−IORB positive; F2 ON-THE-RUN fire |
| 4 | HY market function | **3** ▲ | 🟠 | `VX-BND-02` · `VX-BND-11` | **▲2→3 9/29 on its letter: HY 302 [9/28] >300 with +29bp/3 sessions (98th pct)** (`KB-BND-359`); CCC 1146 span max; CCC−BB 963. ⛔ marker only, not a capital reopen. **Primary access OPEN for large credits (SoftBank $11.1B 9/23–24); pulled-deal leg unverifiable (`KB-BND-346`)** | ⇒4: HY >350 (issuance-freeze line) or a verified pulled-deal cluster. *(⇒3 letter was: HY >300 with velocity, or a pulled-deal cluster (def. `CREDIT_PRIMARY_MARKET.md` §Core Thresholds — no count/window: verified in-scope withdrawals can support it, partial coverage never shows zero; numeric spec with Will)* |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 81 [9/25] (+4 in 3 sessions) | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF z20 +1.01 [9/25] — **rate-confounded in this tape; cash OAS is the leg to read** (`KB-BND-345`) | Synthetic leading cash, sustained |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY +39 from the 263 trough [9/28]; 36–61bp headroom | HY +75–100bp from 263 while VIX <20 |

**Composite: 15/35 — ▲1 on 9/29** (row 4 2→3 on its registered letter, HY 302 [9/28] >300 with velocity). Prior: 14 since 9/24 (row 1 3→4, row 2 2→3). Distribution: 🔴 1 · 🟠 2 · 🟡 1 · 🟢 3. **Re-summed: 4+3+2+3+1+1+1 = 15 ✅.** `VX-BND-01` write-back done 9/28.

**Outside the composite:** `VX-BND-15` inflation anchoring (2) · `VX-BND-17` MBS relay (1) · `VX-BND-18` FHLB (2) · `VX-BND-19` EZ rates (3 — HANS: ECB T-04 no longer a hawkish lean; German 2027 debt service +38%; "disorderly" UNDEFINED → 10/1) · `VX-BND-20` benchmark UST demand (2, checkpoint 10/6).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 2 — `BND-30` (70%: 9/29 leg = term premium, ACM 9/29 share ≥0.50; base 51–62%) · `BND-31` (65%: Tokyo 9/30 JGB 30Y < +4.0bp = no export; base 31% conditional) — pre-registered 9/29 13:1x ET, page §6.** **Resolved 9/28:** `BND-27` **FALSE** (65%, a MISS — CCC 1112 [9/24] ≥ 1100). **9/24:** `BND-25` **TRUE** (55%) · `BND-26` **FALSE** (70%). **Tally: 14 TRUE · 13 FALSE · 1 VOID** — the last two resolutions are both MISSES in the hawkish/stress direction (the desk under-called the move it believes in). Archives: `thesis/archive/PREDICTIONS_resolved_*`. The 10/28 FOMC curve-shape row is owed by 10/21.

---

## Trade Interface *(full view → `TRADE.md`; construction is TERRY's lane)*

- **TLT puts (Sep-30 77P ×15 [qty ×20→×15 9/28: 5 SOLD @ $0.06, net $28.45 — FORGE `b997a01ce` D-31; posture unchanged]; 5 of 25 sold 9/10, `FORGE/STATUS.md:55`) — HOLD, no add, `$0`.** Both add-gates read through (DFII10 sustain MET under WQ-246; OLD-conjunctive re-arm 9/23) — ⛔ **neither is an add: WQ-280 DECLINED 9/24; 7/16 NO-ADD; root rule #5.** **TLT 78.61 intraday 9/28 ⇒ strike 2.0% below spot with 2 sessions to the 9/30 expiry — harvest/expiry is TERRY's rail; re-pull live before any call.** *Posture, never a direction.*
- **HYG puts — closed at the INDEX level.** HY 302 [9/28] = BOND's 300 marker MET 9/29 — **analytical only, NOT a capital reopen**: the index-protection SIZING question sits behind LIQUID's X1 gate, CLOSED 8/28 (BROCK `KB-BRK-219`, wrapper half NOT ARMED; fail-safe DON'T-SIZE); it reopens only via BROCK's **10/02 re-adjudication sitting** (DOCKET L494), then TERRY's card + Will. CCC tail FIRED 1100 → expression single-name/CCC, **never HYG**. Registered HY lines: RED-FT-01 (RED's) · LIQUID X1. *(Corrected 9/28 15:22 ET on PROME's relay; provenance → snapshot `2026-09-29b`.)*
- **TLT Oct-16 82P ×1** (×2→×1 9/28: 1 SOLD @ $3.60, net $359.34 — FORGE `b997a01ce`; ITM) — **TERRY's management card** (`AGENTS/TERRY/setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md`); BOND carries no posture on it.
- **Credit-equity lead — inactive.**

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all duration shorts).** WQ-157 leg ① (Will 9/4): **`I'` + a NON-AUCTION mechanism confirmation** (FR2004 dealer stock and/or SOFR−IORB). 🔴 **9/23 5Y dealer leg RULED (WQ-291, Will 9/26; `KB-BND-342`): FR2004 3–6Y as-of 9/23 ≥ $56.586B (PRE $47.986B) — prints Thu 10/1 ~16:15; grader `analysis/2026-10-01_wq291_grade.py`.** Riders: net inventory ≠ proof of warehousing; funding window for this fire UNGRADED (quarter-end excluded by the letter); no predictive claim; a fire = recommendation via TERRY's card + Will. Funding leg UNMET (SOFR−IORB 0bp [9/28], LIQUID NONE, `KB-BND-330`) ⇒ **KILL NOT FIRED; dealer leg evaluable 10/1.** Leg ② PARKED (Will 9/25; `I'` ALONE = MARKER, `KB-BND-335`). Unpaired `I'` fires: 9/15 20Y-R · 9/23 5Y · 9/24 7Y. Also: 10Y back below 4.15 ×3 with clean auctions ⇒ spent. `I'` bars → `monitors/AUCTION_HEALTH.md` §GRADING BASIS (grader fix `KB-BND-314`, disclose if pre-fix pools are re-cited). 🔴 Direction disclosed: `I'` is the easier test and its firing confirms this desk's own bear thesis. Full history → THESIS + snapshots `2026-09-28d` / `2026-09-29b`.

**2 · POSITION-SPECIFIC.** TLT puts: kill on 10Y <4.15 AND 30Y <5.0 ×3 sessions AND a clean refunding (THESIS §2). Expiry 9/30 is TERRY's rail.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal coupons passing both legs (indirect ≥ median AND dealer ≤ median). **Counter 0** (2Y failed the dealer leg 13.19 vs 11.33; 5Y and 7Y failed indirect). Next eligible: 10/6 3Y.

**4 · TIME-BASED.** Quarter-end + PCE + expiry **9/30** · **FR2004 as-of 9/23 = WQ-291 grade + FORUM-7 FINAL, Thu 10/1 ~16:15 (report by the 10/2 boot)** · F2 reads **10/1 · 10/8 · 10/15 · 10/27 · 11/4** · quarterly `I'` refresh + `VX-19` definition **10/1** · `VX-20` **10/6** · FOMC curve-shape row **by 10/21** · FHLB Q3 **11/9** · FRBNY FX **11/13** · US-sov-CDS re-test **12/1**.

⚠️ **RETIRED, NOT REVIVABLE: the auction TAIL.** The 9/23 "2nd biggest tail ever" wire claim is `[med-conf]` and fires nothing.

---

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| **Wed 9/30** | 🔴 **Quarter-end · Aug PCE + Q2 GDP 3rd (8:30) · TLT 77P expiry** (`BND-27` already resolved FALSE 9/28) | PCE vs the PMI input-price shock; SOFR−IORB across quarter-end (0bp [9/25]); ~$183B settlement on the turn (LIQUID reads) |
| **Thu 10/1** | 🔴 **FR2004 as-of 9/23 (~16:15) = WQ-291 5Y dealer-leg grade (≥ $56.586B) + FORUM-7 FINAL** · H.4.1 week-9/30 · quarterly `I'` refresh · `VX-19` "disorderly" · **10Y–20Y buyback op (F2)** · Oct refunding sizes | MET / NOT MET / GAP with margin by the 10/2 boot; `AUCTION_HEALTH.md` §3d |
| **Fri 10/2** | Sept Employment Situation (8:30) · **WQ-317 cross-market page DUE** (PARTIAL delivered 9/29; HANS legs owed) · BROCK's X1 re-adjudication sitting (index-hedge sizing — not BOND's) | 2Y / 1y1y reaction; IMPORTING / EXPORTING / SHARED / UNDETERMINED |
| **10/6 · 10/7 · 10/8** | 3Y `91282CRQ6` · 10Y-R `91282CRF0` · 30Y-R `912810UW6` + 20–30Y op (F2) · `VX-20` review | bars frozen at the 10/1 announcement; **10/7–10/8 are the long-end auctions that can fire row 1's ⇒5 letter** |
| **Wed 10/14 · 10/15** | Sept CPI (8:30) · 10–20Y op (F2) | breakevens on input-supported cells only |
| **10/21 · 10/22 · 10/26–29** | 20Y-R · 5Y TIPS · month-end cluster | bars at each announcement |
| **Wed 10/28 2:00 PM** | 🔴 **October FOMC** (~70% hike priced, TE secondary) · ECB 10/29 | register a curve-shape row by 10/21 |
| **10/27 · 11/4** | 20–30Y op · **QRA + 10–20Y op (F1/F3 resolve; sb0607 window ends)** | carrier + `VX-BND-16` |
| **Wed 12/9 2:00 PM · Wed 2027-01-27** | 🔴 **December FOMC + SEP** · January FOMC (docketed 9/28 on `rates_context`'s first issuer-calendar check) | curve-shape rows with base rates by 12/2 · 1/20 |
| **11/9 · 11/13 · 12/1 · 2027-01-25** | FHLB Q3 · FRBNY FX · US-sov-CDS re-test · Norwegian MoF expert group | as docketed |
| **— STANDING —** | MOF FX intervention · Warsh task force · FR2004 weekly · credit weekly · F2 carrier every boot | `FL-BND-11` · `VX-04` · `VX-02/11` · `VX-16` |

---

## BOTTOM LINE

**[2026-09-29 Tue, official close published 15:55 ET; updated 15:5x ET.]** **The bond sell-off is in its fifth day, and today the long end moved alone.** The official 30-year closed **5.59%** (+3bp), the fifth record-for-the-year close in a row and the highest since **May 2004**; the 20-year 5.64% is the highest since July 2002; the 10-year closed 5.26%, matching its June 2007 high without exceeding it. The 2-year **fell** 3bp to 4.89%, and futures took back about 5bp of expected Fed hikes across the whole path in the afternoon (October is now a coin flip, from 68% this morning), with no cause anyone has found. A long end that rises while the expected rate path falls is duration itself being repriced, the term-premium shape this desk's thesis rests on. **That call is registered as a bet (BND-30, 70%), graded on the ACM model when it publishes today's row, not asserted.** Real yields led the week; today's 10-year split was flat (+1 real, +1 inflation).

**Today's move started in the US and stayed there** (German yields −3bp, British flat, Japanese flat, oil down; consumer confidence printed its weakest since 2014 at 10:00 and the 30-year rose 2bp into it). Whether the world follows is tonight's test in Tokyo (BND-31). European figures are second-hand until HANS reports; today's Fed speakers were not captured. Credit was soft and orderly; today's junk-spread cell prints tomorrow. **No matrix move.**

**Yesterday's official close (9/28):** 30-year 5.56% (highest since June 2004), 10-year 5.24%, 2-year +11bp to 4.92% led; real-yield-led; driver wire-attributed only (oil/Iran, hike odds, a global sell-off). **Junk spreads crossed BOND's 300bp warning line** (302bp, +29bp in three sessions, a top-2% pace) — the high-yield row moved up one notch (composite **15/35**). A warning marker only: it does **not** reopen index hedging (shut by the 8/28 X1 ruling until BROCK's 10/02 sitting, then TERRY's card and your approval). Big borrowers still get deals done (SoftBank $11.1B; Paramount ~$12.4B launched, unpriced); smaller pulled deals cannot be fully checked, so "open" is proven for large issuers only.

**Auction warning still unconfirmed.** The 9/23 auction weakness needs dealer balance-sheet confirmation; that test prints **Thursday 10/1 ~4:15 PM** (5Y-bucket dealer inventory ≥ $56.586B = met; grader built and dry-run). Tomorrow is quarter-end, PCE, and the option expiry.

**Position: TLT Sep-30 77P ×15 HOLD, no add, `$0`, expires TOMORROW 9/30.** At TLT 77.96 (12:49 ET) the fees-in breakeven of $76.89 needs the 20-year-plus yield to rise about **9bp more by Wednesday's close** (roughly a 30-year at 5.70%); a two-day move that size has happened about 5% of the time over the past year, and about 4% of the time after four straight up days. **A grind pays zero; only a fast shock pays.** Harvest/expiry is TERRY's rail, re-pull live before any call. Nothing today becomes a recommendation from this desk; the one thing that could this week is Thursday's dealer-inventory print. Composite 15/35 (▲1 9/29, row 4). Counter 0. OPEN predictions 0.
