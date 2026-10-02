# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension; + the sovereign-credibility instrument set per the 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-10-02 Fri — 11:43→12:xx ET PROME spawn `prome-96` (Tier-1 follow-up WQ-357: grade the kill letter on the 10/2 post-NFP tape; FedWatch dated read; Jefferson 10/01 thesis read; G7 oil-stock-release rates read; HENRY FORUM-7 co-sign) · prior: 2026-10-01 Thu 16:05→17:1x ET `prome-2f` (WQ-291 dealer leg MET → REC PENDING WILL, WQ-357)

> 📕 **HOT/COLD SPLIT — NOTHING DELETED.** Pre-rotation snapshots (`domain/sources/`): **`2026-10-01_STATUS_full-snapshot_pre-refresh-rotation.md` (crc32 `735109674`)** · `2026-09-29b_…pre-intraday-rotation` (`2392892541`) · `2026-09-29_…pre-row4-rotation` (`2518256656`) · `2026-09-28e` (`2516058915`) · `2026-09-28d` (`319142979`) · `2026-09-28c` (`1800580424`) · `2026-09-28b` (`2552442073`) · older `2026-09-28_` · `2026-09-24`. **Budget 32,550 B; rotate-tier ≥75% — rotate, never raise.**

**Canonical elsewhere — no second copy here:** thesis → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalysts → `docket/CATALYSTS.tsv` · gates/positions → `TRADE.md` · learnings → `MEMORY.md` · handoff → `SCRATCH.md`.

---

## 🔴 TOP OF FILE — what changed since 9/29

⛔ **NEXT BOND SESSION — IN ORDER (dated 2026-10-02 12:xx ET):** ① **Record Will's WQ-357 ruling** on STATUS/TRADE/THESIS + token `posture=` if the book changes — root rule #10 closes only on his word · ② **official 10/2 Treasury par/real curve** (phase 2 release ~16:00–16:30 ET 10/2) → KB row + rates rows · ③ **10/1 F2 10Y–20Y buyback read** → RED (carried from 10/1, still not started) · ④ **10/6 3Y · 10/7 10Y-R · 10/8 30Y-R** on the 10/1 frozen bars (`AUCTION_HEALTH.md`; tie-band alignment first).
0. 🟠 **[10/2 11:5x ET] WQ-357 GRADED on the 10/2 post-NFP tape (`KB-BND-385`): REAFFIRM EXIT per the Will-ruled kill letter · analytical read = THESIS INCREMENTALLY STRENGTHENED by today.** Grade delivered to PROME `PROME/inbox/2026-10-02_from-BOND_WQ-357-grade-on-10-2-tape.md`. **Mechanism named:** weak Sept NFP (+29K vs ~90K consensus; Jul/Aug revised −60K; U-3 4.2%) rallied the 10Y 5.24 → 5.18 pre-open → **5.24 at 11:16 ET → 5.26 at 11:46 ET (fetch.py `^TNX`)**; TLT $77.62 (−0.11%), TBT $42.39 (+0.47%), 30Y 5.62. **The payroll miss failed to rally duration; the long end is HIGHER than pre-NFP.** FedWatch dated 11:47 ET 10/2 (CBOT ZQ, `rates_context.py`): **Oct 28 ≈ 20% hike** (down from 36% on 9/30, ~26% on undated WALTER-035); Dec 9 ~56% conditional; peak 4.715 in Nov-27 = +83.5bp. Front strip −10–11bp / 5 obs while long end + ACM TP (+24.2bp / 5 obs) ran hotter — **the C-36 TWO-PART regime's signature divergence**. Jefferson 10/01 "energy predominant / no Oct commit" explicitly names the term-premium channel. **Procedural rec stays EXIT (per the MET-ruled kill letter); analytical case for staying short STRENGTHENED. Will's override is his judgment, not BOND's.** TERRY card `MGMT-DURSHORT-EXIT-WQ291` lean A window still open at 11:5x ET (deadline 15:00 ET). Position unchanged.
00. 🔴 **[10/1 16:15 ET] WQ-291 DEALER LEG MET ⇒ THE SEPT-4 KILL LETTER IS MET for the 9/23 5Y `I'` fire** (`KB-BND-383`). FR2004 3–6Y (`PDPOSGSC-G3L6`) as-of 9/23 = **$60.079B** vs bar **$56.586B** ⇒ margin **+$3.493B**; PRE as-of 9/16 reproduced **$47.986B** unrevised; Δ **+$12.093B** vs the +$8.6B letter. Published between 16:13:01 ET (absent) and 16:15:20 ET (present) 10/1; grader rc=0 twice. Riders verbatim: ① 3–6Y build NOT proof of auction warehousing ② funding window UNGRADED ③ operational rule, not predictive. Dealer DURATION FELL w/w (long-end TOTAL $140.5B, −$3.8B; 6–7Y $23.199B, −$4.646B); 3–7Y combined +$7.4B. Matrix: row 2 3→4 · row 1 4→5 ⇒ **17/35**. Token `kill=MET-REC@2026-10-01`; THESIS v1.2.11. **Downstream, verified at the artifacts 17:0x ET 10/1 (`KB-BND-384`):** PROME WQ-357 (`9c30a8bb8`; L478 RESOLVED) · TERRY exit card `MGMT-DURSHORT-EXIT-WQ291` (`8f9e6b7d1`): A sell both Fri 10/2 from ~09:45, by 15:00 ET · B 82P only · C hold to 10/14 · ANVIL EOD reconcile `d97eba708` (sleeve unchanged). **STATE: REC PENDING WILL.**
000. 🗓️ **Post-delivery lines of 14:2x ET 10/1 — ROTATED 17:0x ET (read cap), verbatim at `git show 1b4b7c6f0:AGENTS/BOND/STATUS.md` item 000:** R3 WATCH_FOR landed · L410/L532 RESOLVED · HANS Bund-rally correction (`KB-BND-379`) · LIQUID LIQ-07 FIRED on the 9/30 cell (`KB-BND-382`) · WQ-339 conditions: BND-30 ✅ · BND-31 ✅ · FR2004 now MET.
0a–3. *Phase-1 items of 10/1 (9/30 official curve · BND-30/31 TRUE · WQ-317 UNDETERMINED · L410 grader repair + I′ re-freeze · credit 9/30) — rotated 10/1, verbatim at `git show 1b4b7c6f0:AGENTS/BOND/STATUS.md` items 0–3.*

## Regime (one-line)
<!-- bond-state: thesis=v1.2.11; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=HOLD-NO-ADD -->

**Real-rate / higher-for-longer — and the policy path is still repricing HAWKISHLY.** C-36 TWO-PART (ruled 9/1): policy-path channel ALIVE · term premium drove the July delta. **9/16 FOMC +25bp to 3.75–4.00 (12–0); the curve priced ABOVE the SEP median (4.125) and then kept going (`BND-26`).** **Auctions: "expensive, not broken" is UNDER TEST — first OLD-conjunctive fire on the live-graded record (9/23 5Y); its WQ-291 dealer leg printed MET 10/1 (3–6Y +$12.1B) ⇒ kill letter MET ⇒ recommendation via TERRY + Will — **REC PENDING WILL (WQ-357)**; funding window UNGRADED.** Full ruling → `thesis/THESIS.md` **v1.2.11**.

---

## Current Dashboard

*Nominal/real rates rows = the **OFFICIAL 9/30 Treasury par/real cells** (read 12:57 ET 10/1; FRED H.15 frontier 9/29) + the **vendor intraday ^-ticker reads 10/2 11:46 ET via `fetch.py`** labelled accordingly. Credit = FRED **9/30** first-published cells via `boot_recompute.py` (cache-busted 12:50 ET 10/1). FF/TP via `rates_context.py` 11:47 ET 10/2. 10/2 official cells post ~16:00–16:30 ET (phase 2). No naked numbers.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30 · ^TYX) | **5.64%** [9/30] · **^TYX 5.62% +0.21%** [10/2 11:46 ET] | 🔴🔴 | [CONF Treasury par 9/30; `fetch.py` vendor 10/2] — long end round-tripped the NFP rally; 11:46 ET read is ~flat on the day. 9/30 was 6th straight fresh 2026 high, highest DGS30 close since 2002-07-08 (5.66); run ≥5.00 = **61**. 20Y **5.68** 9/30 |
| 10Y (DGS10 · ^TNX) | **5.29%** [9/30] · **^TNX 5.26% +0.36%** [10/2 11:46 ET] | 🔴 | [CONF Treasury 9/30; `fetch.py` vendor 10/2] — **pre-NFP 5.24 → post-NFP 5.18 → 5.24 at 11:16 ET → 5.26 at 11:46 ET: FULLY ROUND-TRIPPED and marginally HIGHER than pre-NFP**; 9/30 close exceeded the 2007-06-12 5.26 → highest since 2002-05-14 |
| 5Y (DGS5 · ^FVX) | **5.09%** [9/30] · **^FVX 5.03% +0.50%** [10/2 11:46 ET] | 🔴 | [CONF Treasury 9/30; `fetch.py` 10/2] — belly rallied ~6bp on NFP (the only tenor where the rally stuck); 9/30 close highest since 2007-07-06 |
| 2Y · 1Y · 3M | **4.88% · 4.54%** [9/30] · **^IRX 3.98% +0.08%** [10/2 11:46 ET] | 🔴 | [CONF Treasury 9/30; `fetch.py` 3M 10/2] — 2Y −1 on 9/30; 2s10s +41, **2s30s +76** (70 [9/29]); 10/2 curve shape = **bull-flattened front, long end flat/firmer** post-round-trip |
| **10Y real (DFII10)** | **2.93%** | 🔴🔴 **GATE THROUGH · SUSTAIN MET** | [CONF **Treasury real curve 9/30**, +2; FRED 2.91 [9/29]] — **highest since 2008-11-24 (3.11)**; 99.7th pct since 2003 [9/29]. 30Y real 3.33, 5Y real 2.73. WQ-246 sustain met; authorises no add |
| 5Y5Y fwd (T5YIFR) | **2.36%** | 🟡 | [CONF FRED **9/30**] — **14bp from 2.50** |
| 10Y BE (T10YIE) | **2.36%** | 🟡 | [Treasury par−real **9/30** = 2.36; FRED T10YIE 2.36 [9/30]] — 9/30 at the 10Y: +2 real, +1 BE (real-led) |
| ACM 10Y TP · KW TP | **0.8876** [9/30] · **1.0203** [9/25] | 🟠 ↑ | [NY Fed ACM Daily · FRED `THREEFYTP10`, via `rates_context.py` 11:47 ET 10/2] — ACM **+4.1bp 1obs, +24.2bp / 5 obs**; 9/29 TP share 2.36 ⇒ `BND-30` TRUE (`KB-BND-373`). Different window/horizon from the FF strip: not a causal split (CATO 9/28). **Name the model in any TP claim** |
| **Fed path (FF futures)** | **peak 4.715% [Nov-27; +83.5bp vs EFFR = 3.3 × 25bp cumulative]** · **10/28 hike ≈ 20%** (down from 36% 9/30; ~26% WALTER-035 undated 10/1) | 🟠 ↓ | [CBOT ZQ via yfinance, **today's EVOLVING vendor bar, NOT settlement**, 11:47 ET 10/2; EFFR 3.88 [9/30]] — Nov −1.0 / Dec +0.0 on the day; **−10 to −11bp over 5 obs**: NFP miss (+29K) priced out Oct hike while long end held firm. Dec ≈ +19bp vs EFFR ≈ 56% hike conditional on Oct hold. **HENRY owns the series; BOND consumes** |
| **HY OAS** | **312bps** | 🟠 ↑ | [CONF FRED **9/30**, first-published] — 302 [9/28]; above BOND's 300 row-4 marker (row 4 = 3; ⇒4 needs >350) |
| **CCC OAS** | **1179bps** | 🔴 ↑ | [CONF FRED **9/30**] — **new 3y-span max** (1146 [9/28]); 1100 escalation FIRED 9/24 |
| IG · BBB · BB · B OAS | **84** [9/30] · 102 · 183 · 309bps [9/28] | 🟢 · 🟢 · 🟡 ↑ · 🟡 ↑ | [CONF FRED; IG 9/30, tiers 9/28 — tier 9/30 cells not read this session] |
| CCC−BB tail gap | **963bp** [9/28] | 🔴 ↑ | [CONF FRED, BOND computation **9/28**; 9/30 BB cell not read] |
| **FR2004 long-end** | **$140.5B** [as-of 9/23] | 🟡 | [NY Fed, published 10/1 between 16:13 and 16:15 ET] — **−$3.8B w/w**; 7-11Y $34.2B (−0.9), 11-21Y $68.5B (0.0), >21Y $37.8B (−3.0). **3–6Y $60.079B (+$12.093B) = WQ-291 MET** (`KB-BND-383`); 6–7Y $23.199B (−4.646). Next: as-of 9/30 Thu 10/8 |
| **SOFR − IORB** | **0bp** | 🟡 ↑ | [CONF FRED SOFR 3.90 · IORB 3.90, **9/25**] — up from −3 [9/23] into quarter-end; not positive. LIQUID owns |
| TLT · TBT | **$77.62 −0.11%** · **$42.39 +0.47%** [10/2 11:46 ET, `fetch.py`] | 🟠 | [yfinance — a MOMENT property, re-pull at any decision, root rule #4]. Essentially flat on the day post-round-trip. MOVE → VIOLET |
| Global 10Y | → HANS (EU/UK) · SAM (JGB) | `[HANS/SAM own]` | WQ-317 page (`KB-BND-375`) carries the 9/21→9/30 table; 10/1 Bund rallied ~8–9bp (HANS correction). Name the basis (`KB-BND-319`) |
| USD/JPY · oil · VIX | **cite SAM · BRENT · VIOLET** | — | this desk keeps no copy (vendor Brent front quote on 9/28 looks like a roll artifact — do not use) |

### Gate distances *(recomputed this session, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — TLT-put add-gate (a)** | 🔴 **THROUGH by 43bp** [2.93, Treasury 9/30] · 41bp [2.91, FRED 9/29] | **Sustain leg MET under WQ-246 (5 consecutive; 11 FRED closes)** — authorises NO add (NO-ADD 7/16 + WQ-280) |
| **Auction re-arm (OLD conjunctive) — TLT-put add-gate** | 🔴 **MET 9/23 (5Y)** | ✅ **ADD DECLINED — WQ-280 RULED 9/24 13:17 ET.** Spent on 004 |
| **Kill dealer leg, 9/23 5Y (WQ-291)** | 🔴 **MET by +$3.493B** [3–6Y $60.079B vs $56.586B, as-of 9/23] | ✅ **KILL LETTER MET 10/1 ⇒ RECOMMENDATION — TERRY card `MGMT-DURSHORT-EXIT-WQ291` written; REC PENDING WILL (WQ-357, by Fri 10/2); no action**; funding window **UNGRADED** by ruling |
| T5YIFR >2.50 | 14bp [2.36, FRED 9/30] | 🟡 |
| DGS30 >5.00 · DGS10 >4.50 | — | 🔴 BREACHED (run **61**, Treasury cell 9/30) · 🔴 BREACHED |
| HY OAS >300 (BOND row-4 marker — **not** a capital reopen; X1 CLOSED 8/28) | **THROUGH by 12bp** [312, 9/30] | 🟠 **MET 9/29 → row 4 = 3** |
| CCC >1100 escalation | **FIRED 9/24** (+12; +28 on 9/25) | 🔴 `BND-27` FALSE |
| Credit-equity lead (HY +75–100 from the 263 trough, VIX <20) | 26–51bp | 🟡 moving (HY 312 [9/30] = +49 from 263; VIX → VIOLET) |

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **5** ▲ | 🔴🔴 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | **▲4→5 10/1 on its letter: the paired kill's mechanism leg CONFIRMED (WQ-291 3–6Y MET, `KB-BND-383`).** 6 straight fresh DGS30 highs → 5.64 [9/30], highest since 2002-07-08; 10Y 5.29 > its 2007 high (`KB-BND-372`) | Top score. Watch: 10/7 10Y-R, 10/8 30Y-R (bars frozen 10/1, `KB-BND-377`) |
| 2 | Treasury auction health | **4** ▲ | 🔴 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED (tail) | **▲3→4 10/1 on its letter: composition failure (9/23 5Y, OLD + `I'`, clean pool `KB-BND-377`) with the FR2004 leg CONFIRMED (WQ-291 MET, `KB-BND-383`).** BTC 2.21 < 2.28 cover bar; 7Y `I'` by 0.04pp. ⚠️ net inventory ≠ proof of warehousing; funding window UNGRADED | ⇒5: a second composition failure with a confirmed mechanism leg |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | FR2004 9/23 long-end TOTAL $140.5B (**−$3.8B**; 2nd straight fall) ⇒ this row's letter NOT met; the 3–6Y build (+$12.1B) is the kill leg, not this row. **9/24 20–30Y buyback F2 0.02% ⇒ OFF-THE-RUN (2 of 2 ops)** | Two consecutive builds on TOTAL with weak composition, or SOFR−IORB positive; F2 ON-THE-RUN fire |
| 4 | HY market function | **3** = | 🟠 | `VX-BND-02` · `VX-BND-11` | **▲2→3 9/29 on its letter** (HY 302 [9/28] >300 with velocity, `KB-BND-359`); **HY 312 · CCC 1179 (span max) [9/30]** (`KB-BND-381`). ⛔ marker only, not a capital reopen. **Primary access OPEN for large credits (SoftBank $11.1B 9/23–24); pulled-deal leg unverifiable (`KB-BND-346`)** | ⇒4: HY >350 (issuance-freeze line) or a verified pulled-deal cluster. *(⇒3 letter was: HY >300 with velocity, or a pulled-deal cluster (def. `CREDIT_PRIMARY_MARKET.md` §Core Thresholds — no count/window: verified in-scope withdrawals can support it, partial coverage never shows zero; numeric spec with Will)* |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 84 [9/30] | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF z20 +1.01 [9/25] — **rate-confounded in this tape; cash OAS is the leg to read** (`KB-BND-345`) | Synthetic leading cash, sustained |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY +49 from the 263 trough [9/30]; 26–51bp headroom | HY +75–100bp from 263 while VIX <20 |

**Composite: 17/35 — ▲2 on 10/1** (row 1 4→5 and row 2 3→4, each on its registered letter, on the WQ-291 dealer leg MET, `KB-BND-383`). Prior: 15 since 9/29. Distribution: 🔴🔴 1 · 🔴 1 · 🟠 1 · 🟡 1 · 🟢 3. **Re-summed: 5+4+2+3+1+1+1 = 17 ✅.** `VX-BND-01` / `-05` written back 10/1.

**Outside the composite:** `VX-BND-15` inflation anchoring (2) · `VX-BND-17` MBS relay (1) · `VX-BND-18` FHLB (2) · `VX-BND-19` EZ rates (3 — HANS: ECB T-04 no longer a hawkish lean; German 2027 debt service +38%; "disorderly" UNDEFINED → 10/1) · `VX-BND-20` benchmark UST demand (2, checkpoint 10/6).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 0.** **Resolved 10/1:** `BND-30` **TRUE** (70%; ACM 9/29 TP share 2.36, `KB-BND-373`) · `BND-31` **TRUE** (65%; JGB 30Y −2.8bp, `KB-BND-374`). 9/28: `BND-27` FALSE. 9/24: `BND-25` TRUE · `BND-26` FALSE. **Tally: 16 TRUE · 13 FALSE · 1 VOID.** Archives: `thesis/archive/PREDICTIONS_resolved_*`. **Owed: the 10/28 FOMC curve-shape row by 10/21** (OPEN = 0).

---

## Trade Interface *(full view → `TRADE.md`; construction is TERRY's lane)*

- **TLT Sep-30 77P — GONE** (sold 9/30 per PROME's spawn brief; FORGE/TERRY carry the fill). **The duration-short sleeve today = TLT Oct-16 82P ×1 + TBT 10 sh; NO-ADD holds (WQ-280).** Both add-gates read through and **neither is an add** (WQ-280 · 7/16 NO-ADD · root rule #5). *Posture, never a direction.*
- **HYG puts — closed at the INDEX level.** HY 302 [9/28] = BOND's 300 marker MET 9/29 — **analytical only, NOT a capital reopen**: the index-protection SIZING question sits behind LIQUID's X1 gate, CLOSED 8/28 (BROCK `KB-BRK-219`, wrapper half NOT ARMED; fail-safe DON'T-SIZE); it reopens only via BROCK's **10/02 re-adjudication sitting** (DOCKET L494), then TERRY's card + Will. CCC tail FIRED 1100 → expression single-name/CCC, **never HYG**. Registered HY lines: RED-FT-01 (RED's) · LIQUID X1. *(Corrected 9/28 15:22 ET on PROME's relay; provenance → snapshot `2026-09-29b`.)*
- **TLT Oct-16 82P ×1** (×2→×1 9/28: 1 SOLD @ $3.60, net $359.34 — FORGE `b997a01ce`; ITM) — **TERRY's management card** (`AGENTS/TERRY/setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md`); BOND carries no posture on it. **10/1: BOND's kill rec ⇒ TERRY exit card `MGMT-DURSHORT-EXIT-WQ291` (A both Fri 10/2 · B 82P only · C hold to 10/14) — WQ-357, PENDING WILL.**
- **Credit-equity lead — inactive.**

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all duration shorts).** WQ-157 leg ① (Will 9/4): **`I'` + a NON-AUCTION mechanism confirmation** (FR2004 dealer stock and/or SOFR−IORB). 🔴 **9/23 5Y dealer leg RULED (WQ-291, Will 9/26; `KB-BND-342`): FR2004 3–6Y as-of 9/23 ≥ $56.586B (PRE $47.986B) — ✅ MET 10/1: $60.079B, margin +$3.493B (`KB-BND-383`).** Riders: net inventory ≠ proof of warehousing; funding window for this fire UNGRADED (quarter-end excluded by the letter); no predictive claim; a fire = recommendation via TERRY's card + Will. Funding leg UNMET (SOFR−IORB 0bp [9/28], LIQUID NONE, `KB-BND-330`) — the dealer leg alone satisfies the "and/or" ⇒ **KILL LETTER MET 10/1 ⇒ RECOMMENDATION "exit all duration shorts" via TERRY's card (`MGMT-DURSHORT-EXIT-WQ291`) + Will's [Approve] (WQ-357) — REC PENDING WILL; no action by this desk.** Leg ② PARKED (Will 9/25; `I'` ALONE = MARKER, `KB-BND-335`). Unpaired `I'` fires: 9/15 20Y-R · 9/23 5Y · 9/24 7Y. Also: 10Y back below 4.15 ×3 with clean auctions ⇒ spent. `I'` bars → `monitors/AUCTION_HEALTH.md` §GRADING BASIS (grader fix `KB-BND-314`, disclose if pre-fix pools are re-cited). 🔴 Direction disclosed: `I'` is the easier test and its firing confirms this desk's own bear thesis. Full history → THESIS + snapshots `2026-09-28d` / `2026-09-29b`.

**2 · POSITION-SPECIFIC.** Duration shorts (Oct-16 82P ×1, TBT): kill on 10Y <4.15 AND 30Y <5.0 ×3 sessions AND a clean refunding (THESIS §2). The 82P card is TERRY's (sell-or-roll rail, Will's 9/30 standing practice).

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal coupons passing both legs (indirect ≥ median AND dealer ≤ median). **Counter 0** (2Y failed the dealer leg 13.19 vs 11.33; 5Y and 7Y failed indirect). Next eligible: 10/6 3Y.

**4 · TIME-BASED.** **WQ-357 ruling by Fri 10/2 (record it — rule #10)** · 10/6–10/8 refunding (bars frozen 10/1) · F2 reads **10/8 · 10/15 · 10/27 · 11/4** · `VX-19` 'disorderly' qualifier (NOT done 10/1; re-dated 10/8) · `VX-20` **10/6** · FOMC curve-shape row **by 10/21** · Oct-16 82P expiry (TERRY) · FHLB Q3 **11/9** · FRBNY FX **11/13** · US-sov-CDS re-test **12/1** · next `I'` re-freeze **2027-01-04**.

⚠️ **RETIRED, NOT REVIVABLE: the auction TAIL.** The 9/23 "2nd biggest tail ever" wire claim is `[med-conf]` and fires nothing.

---

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| **Thu 10/1 ✅ FIRED** | 🔴 **FR2004 as-of 9/23 = WQ-291 5Y dealer leg: MET** ($60.079B vs $56.586B) ⇒ kill letter MET ⇒ rec → TERRY card (`MGMT-DURSHORT-EXIT-WQ291`) + WQ-357 · official 10/1 curve owed · F2 10Y–20Y op read owed | TERRY's card; Will's [Approve] |
| **Fri 10/2** | **WQ-357 ruling (exit rec; TERRY lean A: sell both from ~09:45, by 15:00 ET)** · Sept Employment Situation (8:30) · BROCK's X1 re-adjudication sitting (index-hedge sizing — not BOND's) | 2Y / 1y1y reaction; record the WQ-357 ruling |
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

**[2026-10-01 Thu, phase 1 ~13:1x ET; second paragraph rewritten ~16:2x ET on the FR2004 print.]** **The long-end sell-off ran a sixth day on 9/30, and for two days it has been American-only.** The official 30-year closed **5.64%** (+5bp), the highest close since July 2002; the 10-year's 5.29% passed its 2007 high to the highest since May 2002; real 10-year yields (2.93%) are the highest since November 2008. On both 9/29 and 9/30 German, euro-area and Japanese yields **fell** while ours rose, and futures kept taking Fed hikes **out** of the path (October now ~28%). A long end that rises while the expected rate path falls is duration being repriced: the NY Fed's ACM model put 9/29's whole move in term premium (BND-30 TRUE), and Tokyo did not follow it (BND-31 TRUE). **Who started the 9/22–9/28 episode is UNDETERMINED** on daily closes (WQ-317 page): Japan is ruled out for the first two days and Australia did not lead, but a shared global driver and a US lead that Europe followed the same morning fit equally.

**The 4:15 PM dealer-inventory print graded the thesis kill on the 9/23 auction, and it came in MET.** Dealers' 3-to-6-year Treasury inventory as of 9/23 rose to **$60.1B**, $3.5B above the **$56.586B** line you ruled on 9/26 (up $12.1B on the week). The kill rule needs a weak auction plus one non-auction confirmation, and this is it — so BOND **recommends exiting all duration shorts** (today TLT Oct-16 82P ×1 + TBT 10 sh, per the 10/1 mirror). That is a recommendation going to TERRY for the card and to you for approval, not an action. ⚠️ **What the number does not show:** a jump in net dealer inventory is not proof that dealers were stuck with the auction; the funding test for that auction was never graded; and the rule makes no forecast. The same print shows dealers' longer holdings **fell** (long end −$3.8B, 6–7 year −$4.6B), so the build sat in the short-intermediate bucket rather than in duration overall. **Book unchanged until you rule: TERRY's card leans to selling both lines Friday after the jobs report (from ~09:45, by 3 PM ET), with keep-TBT and hold-to-10/14 as the alternatives; it is WQ-357, due Friday.** Composite **17/35** (long end at the top score, auctions 4), counter 0, OPEN predictions 0. Next: the 10/6–10/8 refunding auctions (bars frozen).
