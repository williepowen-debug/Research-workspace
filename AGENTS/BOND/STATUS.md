# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension; + the sovereign-credibility instrument set per the 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-10-01 Thu — 12:50 ET PROME spawn `prome-0c` (DOCKET L410 · L478 · L532), phase 1 of 2: L0 drain 9/9 · L410 tool repair + quarterly `I'` re-freeze · WQ-317 page · 9/30 official curve · BND-30/31 TRUE · pre-print WQ-291 letter restated. **Phase 2 (FR2004 grade) after ~16:15 ET on PROME's re-ping.** · prior: 2026-09-29 Tue ×3 (Will session · closeout protocol rebuilt) · 2026-09-28 Mon ×3

> 📕 **HOT/COLD SPLIT — NOTHING DELETED.** Pre-rotation snapshots (`domain/sources/`): **`2026-10-01_STATUS_full-snapshot_pre-refresh-rotation.md` (crc32 `735109674`)** · `2026-09-29b_…pre-intraday-rotation` (`2392892541`) · `2026-09-29_…pre-row4-rotation` (`2518256656`) · `2026-09-28e` (`2516058915`) · `2026-09-28d` (`319142979`) · `2026-09-28c` (`1800580424`) · `2026-09-28b` (`2552442073`) · older `2026-09-28_` · `2026-09-24`. **Budget 32,550 B; rotate-tier ≥75% — rotate, never raise.**

**Canonical elsewhere — no second copy here:** thesis → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalysts → `docket/CATALYSTS.tsv` · gates/positions → `TRADE.md` · learnings → `MEMORY.md` · handoff → `SCRATCH.md`.

---

## 🔴 TOP OF FILE — what changed since 9/29

00. ⏳ **[10/1 ~16:15 ET] FR2004 as-of 9/23 = the WQ-291 kill dealer-leg grade — letter restated PRE-PRINT** (`PROME/inbox/2026-10-01_from-BOND_phase-1-L410-L532-L478-preprint.md` §1): **3–6Y alone governs a 5Y fire; MET iff as-of 9/23 ≥ $56.586B (Δ ≥ +$8.6B, inclusive)**; long-end TOTAL + 6–7Y **reported, never graded** (the 9/25 "AMBIGUOUS BY BUCKET" intent was SUPERSEDED by Will's 9/26 approval of exactly that conflicting-bucket treatment, `KB-BND-337`); revised PRE / unpublished / cross-break = GAP, no fire. A MET = **recommendation** via TERRY's card + Will, never an action. Duration shorts today: TLT Oct-16 82P ×1 + TBT 10 sh.
0. 🔴 **[9/30 OFFICIAL] SESSION 6 — 30Y 5.64 (+5), the US long end ROSE ALONE** (`KB-BND-372`): 6th straight fresh 2026 high, **highest DGS30 close since 2002-07-08**; **10Y 5.29 now EXCEEDS the 2007-06-12 5.26 → highest since 2002-05-14**; 20Y 5.68; 5Y 5.09 (+3); 2Y 4.88 (−1); DFII10 **2.93** (highest since 2008-11-24); BE 2.36. 2s30s 70→76, bear steepener 2nd day. Same day Bund −4, AAA −2.6, JGB 30Y −2.8. Cause NOT attributed (quarter-end/PCE). **10/1 Europe: Bund RALLIED ~8–9bp while France/Italy/Spain widened** (HANS correction, `KB-BND-379`) — a flight-to-quality day, opposite sign to a global duration sell-off.
1. ✅ **[10/1] BND-30 TRUE** (ACM 9/29 TP share 2.36, TP-DOMINANT, `KB-BND-373`) · **BND-31 TRUE** (JGB 30Y −2.8bp on 9/30 = not exported, `KB-BND-374`) · **WQ-317 page DELIVERED: UNDETERMINED** on closes (JGB cash ruled out as 9/22–23 source; no ACGB lead; SHARED and US-lead both fit; EXPORTING fits poorly; `KB-BND-375`, `analysis/2026-10-01_WQ-317_cross-market-attribution-page.md`).
2. ✅ **[10/1] L410:** `grade_auction.py` — `I'` NOT DEFINED for TIPS (tool brought to the registered spec; no scope change) + degenerate-row guard (`KB-BND-376`; independent read found 2 defects, fixed + re-tested, fix not re-read) · **quarterly `I'` re-freeze + 10/6–10/8 bars FROZEN** (`KB-BND-377`, `monitors/AUCTION_HEALTH.md` 10/1 block) · **9/23 5Y OLD fire CONFIRMED on a clean pool** (dealer MAX 15.61 = a 5Y new issue). Credit 9/30: HY **312** · CCC **1179** (span max) · IG 84 (`KB-BND-381`) — row 4 stays 3.
3. *Carried 9/24–9/29* → snapshot `2026-10-01_…pre-refresh-rotation` (9/29 session 5 · row 4 MET 9/29 · 9/28 curve + `rates_context.py` · corrections).

## Regime (one-line)
<!-- bond-state: thesis=v1.2.10; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=NOT-FIRED; posture=HOLD-NO-ADD -->

**Real-rate / higher-for-longer — and the policy path is still repricing HAWKISHLY.** C-36 TWO-PART (ruled 9/1): policy-path channel ALIVE · term premium drove the July delta. **9/16 FOMC +25bp to 3.75–4.00 (12–0); the curve priced ABOVE the SEP median (4.125) and then kept going (`BND-26`).** **Auctions: "expensive, not broken" is UNDER TEST — first OLD-conjunctive fire on the live-graded record (9/23 5Y), calm funding; dealer leg prints 10/1.** Full ruling → `thesis/THESIS.md` **v1.2.10** (banner reconciled 9/29).

---

## Current Dashboard

*Rates rows = the **OFFICIAL 9/30 Treasury par/real cells** (read 12:57 ET 10/1; FRED H.15 frontier 9/29). Credit = FRED **9/30** first-published cells via `boot_recompute.py` (cache-busted 12:50 ET 10/1). FF/TP via `rates_context.py` the same run. 10/1 official cells post ~16:00–16:30 ET (phase 2). No naked numbers.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.64%** | 🔴🔴 | [CONF **U.S. Treasury par curve 9/30**; FRED 5.59 [9/29]] — **+5bp; 6th straight fresh 2026 high; highest DGS30 close since 2002-07-08 (5.66)** (BOND computation, FRED full series, last close ≥ level); run ≥5.00 = **61**. 20Y **5.68** (+4; = 2002-06-12) |
| 10Y (DGS10) | **5.29%** | 🔴 | [CONF Treasury **9/30**; FRED 5.26 [9/29]] — **+3bp; EXCEEDS the 2007-06-12 5.26 → highest since 2002-05-14 (5.32)** |
| 5Y (DGS5) | **5.09%** | 🔴 | [CONF Treasury **9/30**, +3; highest since 2007-07-06] |
| 2Y · 1Y | **4.88% · 4.54%** | 🔴 | [CONF Treasury **9/30**] — 2Y −1; 2s10s +41, **2s30s +76** (70 [9/29]): **bear STEEPENER 2nd day, long-end-led** |
| **10Y real (DFII10)** | **2.93%** | 🔴🔴 **GATE THROUGH · SUSTAIN MET** | [CONF **Treasury real curve 9/30**, +2; FRED 2.91 [9/29]] — **highest since 2008-11-24 (3.11)**; 99.7th pct since 2003 [9/29]. 30Y real 3.33, 5Y real 2.73. WQ-246 sustain met; authorises no add |
| 5Y5Y fwd (T5YIFR) | **2.36%** | 🟡 | [CONF FRED **9/30**] — **14bp from 2.50** |
| 10Y BE (T10YIE) | **2.36%** | 🟡 | [Treasury par−real **9/30** = 2.36; FRED T10YIE 2.36 [9/30]] — 9/30 at the 10Y: +2 real, +1 BE (real-led) |
| ACM 10Y TP · KW TP | **0.8467** [9/29] · **1.0203** [9/25] | 🟠 ↑ | [NY Fed ACM Daily · FRED `THREEFYTP10`, via `rates_context.py` 12:50 ET 10/1] — ACM **+5.4bp on 9/29, +27.1bp over 5 obs**; 9/29 TP share 2.36 ⇒ **`BND-30` TRUE** (`KB-BND-373`). Different window/horizon from the FF strip: not a causal split (CATO 9/28). **Name the model in any TP claim** |
| **Fed path (FF futures)** | **peak of available strip 4.740% [Jan-28; still rising at the horizon end]** · 10/28 hike ≈**28%** | 🟠 ↓ | [CBOT ZQ via yfinance, **today's EVOLVING vendor bar, NOT settlement**, 12:51 ET 10/1; EFFR 3.88 [9/30]] — Nov −2.5 / Jun-27 −14 on the day, **−10 to −16.5bp over 5 obs**: the priced path keeps FALLING while the long end rises. HENRY owns the read |
| **HY OAS** | **312bps** | 🟠 ↑ | [CONF FRED **9/30**, first-published] — 302 [9/28]; above BOND's 300 row-4 marker (row 4 = 3; ⇒4 needs >350) |
| **CCC OAS** | **1179bps** | 🔴 ↑ | [CONF FRED **9/30**] — **new 3y-span max** (1146 [9/28]); 1100 escalation FIRED 9/24 |
| IG · BBB · BB · B OAS | **84** [9/30] · 102 · 183 · 309bps [9/28] | 🟢 · 🟢 · 🟡 ↑ · 🟡 ↑ | [CONF FRED; IG 9/30, tiers 9/28 — tier 9/30 cells not read this session] |
| CCC−BB tail gap | **963bp** [9/28] | 🔴 ↑ | [CONF FRED, BOND computation **9/28**; 9/30 BB cell not read] |
| **FR2004 long-end** | **$144.4B** [as-of 9/16] | 🟡 | [NY Fed, published 9/24 16:16 ET] — −$1.8B w/w; 11-21Y $68.5B (+1.7), >21Y $40.8B (−2.6). **Next: as-of 9/23 Thu 10/1 ~16:15 = the WQ-291 3–6Y grade (≥ $56.586B)** |
| **SOFR − IORB** | **0bp** | 🟡 ↑ | [CONF FRED SOFR 3.90 · IORB 3.90, **9/25**] — up from −3 [9/23] into quarter-end; not positive. LIQUID owns |
| TLT · TBT | **$77.93 +0.19%** · **$42.03 −1.07%** [10/1 13:02 ET, `fetch.py`] | 🟠 | [yfinance — a MOMENT property, re-pull at any decision, root rule #4]. Sep-30 77P expired 9/30 (sold 9/30 per PROME). MOVE → VIOLET |
| Global 10Y | → HANS (EU/UK) · SAM (JGB) | `[HANS/SAM own]` | WQ-317 page (`KB-BND-375`) carries the 9/21→9/30 table; 10/1 Bund rallied ~8–9bp (HANS correction). Name the basis (`KB-BND-319`) |
| USD/JPY · oil · VIX | **cite SAM · BRENT · VIOLET** | — | this desk keeps no copy (vendor Brent front quote on 9/28 looks like a roll artifact — do not use) |

### Gate distances *(recomputed this session, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — TLT-put add-gate (a)** | 🔴 **THROUGH by 43bp** [2.93, Treasury 9/30] · 41bp [2.91, FRED 9/29] | **Sustain leg MET under WQ-246 (5 consecutive; 11 FRED closes)** — authorises NO add (NO-ADD 7/16 + WQ-280) |
| **Auction re-arm (OLD conjunctive) — TLT-put add-gate** | 🔴 **MET 9/23 (5Y)** | ✅ **ADD DECLINED — WQ-280 RULED 9/24 13:17 ET.** Spent on 004 |
| **Kill dealer leg, 9/23 5Y (WQ-291)** | as-of 9/23 must be ≥ **$56.586B** (PRE $47.986B) | ⏳ prints **Thu 10/1 ~16:15**; funding window for this fire **UNGRADED** by ruling |
| T5YIFR >2.50 | 14bp [2.36, FRED 9/30] | 🟡 |
| DGS30 >5.00 · DGS10 >4.50 | — | 🔴 BREACHED (run **61**, Treasury cell 9/30) · 🔴 BREACHED |
| HY OAS >300 (BOND row-4 marker — **not** a capital reopen; X1 CLOSED 8/28) | **THROUGH by 12bp** [312, 9/30] | 🟠 **MET 9/29 → row 4 = 3** |
| CCC >1100 escalation | **FIRED 9/24** (+12; +28 on 9/25) | 🔴 `BND-27` FALSE |
| Credit-equity lead (HY +75–100 from the 263 trough, VIX <20) | 26–51bp | 🟡 moving (HY 312 [9/30] = +49 from 263; VIX → VIOLET) |

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **4** = | 🔴 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | Moved 3→4 on 9/23. **Since: 6 straight fresh DGS30 highs → 5.64 [9/30], highest since 2002-07-08; 10Y 5.29 > its 2007 high; 9/29–9/30 the US long end rose ALONE** (`KB-BND-372`) — fresh highs are not the ⇒5 letter | ⇒5: a composition failure on a LONG-END auction (**10/7 10Y-R, 10/8 30Y-R — bars frozen 10/1**, `KB-BND-377`) or the paired kill's mechanism leg confirming (**FR2004 grade 10/1 ~16:15**) |
| 2 | Treasury auction health | **3** ▲ | 🟠 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED (tail) | **9/23 5Y: BTC 2.21 < 2.28 cover bar (<2.3 marker) + OLD composition failure (CONFIRMED on a clean pool 10/1, `KB-BND-377`) + `I'`; 7Y `I'` by 0.04pp.** ⛔ `I'` alone = MARKER (WQ-157 ② PARKED 9/25). Paired kill NOT fired (funding NONE per LIQUID); **FR2004 POST for the 9/23 5Y = the 9/23 as-of, Thu 10/1** (trade-date basis `KB-BND-332`) | A composition failure with the funding/FR2004 leg CONFIRMED (paired kill) ⇒ 4 |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | FR2004 9/16 long-end $144.4B (−$1.8B; 11–21Y +1.7, >21Y −2.6), admissible (trade-date, `KB-BND-332`); next: 9/23 as-of Thu 10/1 = the 5Y's POST; 5Y dealer 15.77 = trailing-12 max but ordinary vs 2023–24. **9/24 20–30Y buyback $4.078B of $6B, F2 0.02% ⇒ OFF-THE-RUN (2 of 2 ops)** | Two consecutive builds on TOTAL with weak composition, or SOFR−IORB positive; F2 ON-THE-RUN fire |
| 4 | HY market function | **3** = | 🟠 | `VX-BND-02` · `VX-BND-11` | **▲2→3 9/29 on its letter** (HY 302 [9/28] >300 with velocity, `KB-BND-359`); **HY 312 · CCC 1179 (span max) [9/30]** (`KB-BND-381`). ⛔ marker only, not a capital reopen. **Primary access OPEN for large credits (SoftBank $11.1B 9/23–24); pulled-deal leg unverifiable (`KB-BND-346`)** | ⇒4: HY >350 (issuance-freeze line) or a verified pulled-deal cluster. *(⇒3 letter was: HY >300 with velocity, or a pulled-deal cluster (def. `CREDIT_PRIMARY_MARKET.md` §Core Thresholds — no count/window: verified in-scope withdrawals can support it, partial coverage never shows zero; numeric spec with Will)* |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 84 [9/30] | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF z20 +1.01 [9/25] — **rate-confounded in this tape; cash OAS is the leg to read** (`KB-BND-345`) | Synthetic leading cash, sustained |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY +49 from the 263 trough [9/30]; 26–51bp headroom | HY +75–100bp from 263 while VIX <20 |

**Composite: 15/35 — ▲1 on 9/29** (row 4 2→3 on its registered letter, HY 302 [9/28] >300 with velocity). Prior: 14 since 9/24 (row 1 3→4, row 2 2→3). Distribution: 🔴 1 · 🟠 2 · 🟡 1 · 🟢 3. **Re-summed: 4+3+2+3+1+1+1 = 15 ✅.** `VX-BND-01` write-back done 9/28.

**Outside the composite:** `VX-BND-15` inflation anchoring (2) · `VX-BND-17` MBS relay (1) · `VX-BND-18` FHLB (2) · `VX-BND-19` EZ rates (3 — HANS: ECB T-04 no longer a hawkish lean; German 2027 debt service +38%; "disorderly" UNDEFINED → 10/1) · `VX-BND-20` benchmark UST demand (2, checkpoint 10/6).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 0.** **Resolved 10/1:** `BND-30` **TRUE** (70%; ACM 9/29 TP share 2.36, `KB-BND-373`) · `BND-31` **TRUE** (65%; JGB 30Y −2.8bp, `KB-BND-374`). 9/28: `BND-27` FALSE. 9/24: `BND-25` TRUE · `BND-26` FALSE. **Tally: 16 TRUE · 13 FALSE · 1 VOID.** Archives: `thesis/archive/PREDICTIONS_resolved_*`. **Owed: the 10/28 FOMC curve-shape row by 10/21** (OPEN = 0).

---

## Trade Interface *(full view → `TRADE.md`; construction is TERRY's lane)*

- **TLT Sep-30 77P — GONE** (sold 9/30 per PROME's spawn brief; FORGE/TERRY carry the fill). **The duration-short sleeve today = TLT Oct-16 82P ×1 + TBT 10 sh; NO-ADD holds (WQ-280).** Both add-gates read through and **neither is an add** (WQ-280 · 7/16 NO-ADD · root rule #5). *Posture, never a direction.*
- **HYG puts — closed at the INDEX level.** HY 302 [9/28] = BOND's 300 marker MET 9/29 — **analytical only, NOT a capital reopen**: the index-protection SIZING question sits behind LIQUID's X1 gate, CLOSED 8/28 (BROCK `KB-BRK-219`, wrapper half NOT ARMED; fail-safe DON'T-SIZE); it reopens only via BROCK's **10/02 re-adjudication sitting** (DOCKET L494), then TERRY's card + Will. CCC tail FIRED 1100 → expression single-name/CCC, **never HYG**. Registered HY lines: RED-FT-01 (RED's) · LIQUID X1. *(Corrected 9/28 15:22 ET on PROME's relay; provenance → snapshot `2026-09-29b`.)*
- **TLT Oct-16 82P ×1** (×2→×1 9/28: 1 SOLD @ $3.60, net $359.34 — FORGE `b997a01ce`; ITM) — **TERRY's management card** (`AGENTS/TERRY/setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md`); BOND carries no posture on it.
- **Credit-equity lead — inactive.**

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all duration shorts).** WQ-157 leg ① (Will 9/4): **`I'` + a NON-AUCTION mechanism confirmation** (FR2004 dealer stock and/or SOFR−IORB). 🔴 **9/23 5Y dealer leg RULED (WQ-291, Will 9/26; `KB-BND-342`): FR2004 3–6Y as-of 9/23 ≥ $56.586B (PRE $47.986B) — prints Thu 10/1 ~16:15; grader `analysis/2026-10-01_wq291_grade.py`.** Riders: net inventory ≠ proof of warehousing; funding window for this fire UNGRADED (quarter-end excluded by the letter); no predictive claim; a fire = recommendation via TERRY's card + Will. Funding leg UNMET (SOFR−IORB 0bp [9/28], LIQUID NONE, `KB-BND-330`) ⇒ **KILL NOT FIRED; dealer leg evaluable 10/1.** Leg ② PARKED (Will 9/25; `I'` ALONE = MARKER, `KB-BND-335`). Unpaired `I'` fires: 9/15 20Y-R · 9/23 5Y · 9/24 7Y. Also: 10Y back below 4.15 ×3 with clean auctions ⇒ spent. `I'` bars → `monitors/AUCTION_HEALTH.md` §GRADING BASIS (grader fix `KB-BND-314`, disclose if pre-fix pools are re-cited). 🔴 Direction disclosed: `I'` is the easier test and its firing confirms this desk's own bear thesis. Full history → THESIS + snapshots `2026-09-28d` / `2026-09-29b`.

**2 · POSITION-SPECIFIC.** Duration shorts (Oct-16 82P ×1, TBT): kill on 10Y <4.15 AND 30Y <5.0 ×3 sessions AND a clean refunding (THESIS §2). The 82P card is TERRY's (sell-or-roll rail, Will's 9/30 standing practice).

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal coupons passing both legs (indirect ≥ median AND dealer ≤ median). **Counter 0** (2Y failed the dealer leg 13.19 vs 11.33; 5Y and 7Y failed indirect). Next eligible: 10/6 3Y.

**4 · TIME-BASED.** **FR2004 as-of 9/23 = WQ-291 grade, Thu 10/1 ~16:15 (report by the 10/2 boot)** · 10/6–10/8 refunding (bars frozen 10/1) · F2 reads **10/8 · 10/15 · 10/27 · 11/4** · `VX-19` 'disorderly' qualifier (NOT done 10/1; re-dated 10/8) · `VX-20` **10/6** · FOMC curve-shape row **by 10/21** · Oct-16 82P expiry (TERRY) · FHLB Q3 **11/9** · FRBNY FX **11/13** · US-sov-CDS re-test **12/1** · next `I'` re-freeze **2027-01-04**.

⚠️ **RETIRED, NOT REVIVABLE: the auction TAIL.** The 9/23 "2nd biggest tail ever" wire claim is `[med-conf]` and fires nothing.

---

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| **Thu 10/1** | 🔴 **FR2004 as-of 9/23 (~16:15) = WQ-291 5Y dealer-leg grade (3–6Y ≥ $56.586B) + FORUM-7 FINAL feed** · official 10/1 curve (~16:00–16:30) · ✅ done in phase 1: L410 tool repair + `I'` re-freeze + 10/6–10/8 bars · WQ-317 page · 10Y–20Y buyback op (F2, results ~14:15) | MET / NOT MET / GAP with margin by the 10/2 boot (outcome table pre-stated in the phase-1 memo) |
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

**[2026-10-01 Thu, phase 1 written ~13:1x ET.]** **The long-end sell-off ran a sixth day on 9/30, and for two days it has been American-only.** The official 30-year closed **5.64%** (+5bp), the highest close since July 2002; the 10-year's 5.29% passed its 2007 high to the highest since May 2002; real 10-year yields (2.93%) are the highest since November 2008. On both 9/29 and 9/30 German, euro-area and Japanese yields **fell** while ours rose, and futures kept taking Fed hikes **out** of the path (October now ~28%). A long end that rises while the expected rate path falls is duration being repriced: the NY Fed's ACM model put 9/29's whole move in term premium (BND-30 TRUE), and Tokyo did not follow it (BND-31 TRUE). **Who started the 9/22–9/28 episode is UNDETERMINED** on daily closes (WQ-317 page): Japan is ruled out for the first two days and Australia did not lead, but a shared global driver and a US lead that Europe followed the same morning fit equally.

**Today's one decision-relevant event is 4:15 PM: the dealer-inventory print that grades the thesis kill on the 9/23 auction.** The rule is fixed: 5-year-bucket dealer inventory as of 9/23 at or above **$56.586B** = the kill's dealer leg MET, which becomes a **recommendation** to exit the duration shorts through TERRY's card and your approval, never an action by this desk; below it = no change. Divergent buckets do not make it ambiguous (you ruled the 5-year bucket governs on 9/26); a revised or missing print is a GAP. **Book: TLT Oct-16 82P ×1 + TBT 10 sh, no add.** The auction tool was repaired and the October refunding bars frozen (10/6 3Y · 10/7 10Y · 10/8 30Y — the last two can move the long-end row to its top score). Junk spreads 312bp, CCC a new 3-year wide (1179bp); still a marker, not a hedge reopen. Composite **15/35**, counter 0, OPEN predictions 0.
