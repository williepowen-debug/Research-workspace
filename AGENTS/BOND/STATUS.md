# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension; + the sovereign-credibility instrument set per the 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-28 Mon — 16:18→17:4x ET (boot · WALTER ×3 · official 9/28 curve · front-end deep-dive · CATO narrowing · gap review · `rates_context.py` build) · 14:37→15:59 (catch-up) · 10:34→13:15 (live event) · earlier: 9/26 · 9/25 · 9/24

> 📕 **HOT/COLD SPLIT — NOTHING DELETED.** Pre-rotation snapshot (9/28 17:4x ET): `domain/sources/2026-09-28c_STATUS_full-snapshot_pre-rotation.md` (25,020 B, crc32 `1800580424`) — full text of the 9/28 top items this rotation condensed. Older: `…2026-09-28b…` (crc32 `2552442073`), `…2026-09-28_…pre-9-28-rewrite.md`, `…2026-09-24…`. **Budget 32,550 B; rotate-tier ≥75% — rotate, never raise.**

**Canonical elsewhere — no second copy here:** thesis → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalysts → `docket/CATALYSTS.tsv` · gates/positions → `TRADE.md` · learnings → `MEMORY.md` · handoff → `SCRATCH.md`.

---

## 🔴 TOP OF FILE — what changed since 9/24

00000. 🔴 **[9/28 evening] OFFICIAL 9/28 CURVE + WHAT REPRICED** (`KB-BND-350`, `KB-BND-353`, `analysis/2026-09-28_front-end-led-move.md`): 2Y **4.92 (+11)** · 10Y **5.24 (+7)** · 30Y **5.56 (+7)** = 4th straight 2026 high, highest since 2004-06-14; 10Y since 2007-06-12; DFII10 **2.90** last matched 2008-11-24; real-led (10Y BE flat). The move **grew with horizon** (Nov-26 FF +1.5 → 2Y +11 → 1y1y +13) ⇒ terminal/2027 path, not the 10/28 meeting (≈68%). Episode 9/22→9/28 near-parallel (2Y +21 · 30Y +27). **Driver = GAP.** No matrix move.
0000. 🟢 **[9/28 17:3x; v2 18:13 ET] `monitors/rates_context.py`, run every boot** (`KB-BND-354`, `KB-BND-356`; WQ-327): Fed path (**peak of the available strip** 4.855% Nov-27, ≈3.9 hikes, +18bp/5 obs; vendor bar, NOT settlement) · ACM/KW term premium (ACM **+13.9bp/5 obs**) · VX-BND-17 re-arm watcher (**185bp [9/24], inside 180–230, not fired**). **v2 fixes CATO BR1–BR4 + PROME #5** (stale/thin/missing-meeting inputs now GAP + finding; CATO suite 4/12 → 12/12). **Its first issuer-calendar check found the Dec 9 FOMC missing from this docket — added (+ Jan 27).** ⚠️ **Qualification (CATO, dated 18:13 ET): the FF-strip change (9/21–28) and ACM (9/18–25) are different windows and horizons — consistent with both channels, NOT a causal decomposition.**
000. 🟠 **[9/28 afternoon] Corrections + credit.** ① **HY >300 is BOND's row-4 marker, NOT a capital reopen**: X1 CLOSED 8/28 (`KB-BRK-219`); reopens only via BROCK's **10/02** sitting → TERRY + Will (`KB-BND-348`). ② **CCC refi wall:** mechanism real and NARROW (PIMCO: CCC 2027–28 coupons could double; index-level negligible); the aggregate 2028–29 shape is **index-level only**: the CCC/single-name 2026–27 tail is **UNMEASURED, not small**, and concentration in the weakest names is a GAP (narrowed per CATO; `KB-BND-349`). ③ **HY access OPEN for large credits** (SoftBank $11.1B; Paramount ~$12.4B unpriced = next test); **pulled-deal leg a GAP, not a zero** (`KB-BND-346`); Sept issuance vs April = a vintage TIE (`KB-BND-352`).
00. 🔴 **[9/28 AM] Sell-off 4th session, global, credit joined** (`KB-BND-340`, `KB-BND-343`): 10Y +21bp 9/22→9/25 = real +20 / BE +1; credit spread from CCC into all HY **in speed, not level** (CCC +53 · B +29 · BB +20 · IG +4, 3 sessions). Grades = LIQUID's.
1. 🔴 **`BND-27` FALSE (65%, a MISS): CCC 1112 [9/24] ≥ 1100; 1128 [9/25]** (9bp under span max 1137). **HY 293 [9/25], +25bp/3 sessions (~97th-pct velocity), 7bp from 300.** `VX-BND-11` 3→4. Row 4 letter NOT met (level 7bp short). Expression if anything: single-name/CCC, never HYG (`KB-BND-341`).
2. ✅ **WQ-291 + WQ-246 ENCODED (Will 9/26 15:54 ET; ran ~43h late, BOND dark):** 5Y kill dealer leg = FR2004 **3–6Y ≥ +$8.6B** (9/23 5Y MET iff as-of 9/23 ≥ **$56.586B**, prints Thu 10/1) with three riders — **net inventory ≠ proof of warehousing · funding window for the 9/23 fire EXPLICITLY UNGRADED · no predictive claim**; a fired kill = recommendation via TERRY's card + Will. DFII10 sustained = **5 consecutive published closes ≥2.50** (MET: 11 FRED closes 9/10–9/24) — **no add; NO-ADD unchanged.** THESIS v1.2.9, TRADE gate (a), `KB-BND-342`.
3. 🟡 **Funding into quarter-end: SOFR−IORB 0bp [9/25]** (3.90/3.90), up from −3 [9/23]. Not positive; and quarter-end is excluded from the kill's funding leg. The 9/30 settlement of ~$183B on the turn is LIQUID's read (`KB-BND-330`).
4. **Carried (full text in the snapshots):** 9/23 5Y OLD-conjunctive failure → ADD re-arm met, **ADD DECLINED (WQ-280)** · 9/24 7Y `I'` marker · `BND-26` FALSE · FR2004 trade-date basis RESOLVED (`KB-BND-332`) · WQ-157 leg ② PARKED 9/25 · FORUM-7 FINAL Thu 10/1 (`KB-BND-334`)

## L477 contributions (Will 02:55 ET 9/25 — six-question set; dated section, not a regime change)
- **Q3 (HENRY lead) — FORUM-7 §7 co-signed `fb9a9299a`:** no BOND rail keys on the path/premium verdict. B1: the 10/1 FR2004 as-of 9/23 print is also the 9/23 5Y kill's dealer leg (now ruled 3–6Y under WQ-291). → `analysis/2026-09-25_Q3_FORUM-7-section7_BOND-rows.md`.
- **Q4 (LIQUID lead) — CCC isolated vs leading edge, BOND side:** dealer below-IG inventory +$2.2B in 4 weeks to 9/16 (96th pct; short paper) · only CCC is sensitive to the real-yield shock (20-session beta +0.56, 81st pct; B/BB/IG ≈ median) ⇒ **leans (A) weakest-borrowers, with one (B) warning; first dated test = FR2004 Thu 10/1.** Fleet GAP: no HY issuance/refi-wall data. `KB-BND-336` → `analysis/2026-09-25_Q4_CCC-isolated-vs-leading-edge_BOND-side.md`.

## Regime (one-line)

**Real-rate / higher-for-longer — and the policy path is still repricing HAWKISHLY.** C-36 TWO-PART (ruled 9/1): policy-path channel ALIVE · term premium drove the July delta. **9/16 FOMC +25bp to 3.75–4.00 (12–0); the curve priced ABOVE the SEP median (4.125) and then kept going (`BND-26`).** **Auctions: "expensive, not broken" is UNDER TEST — first OLD-conjunctive fire on this desk's LIVE-graded record (KB searched 9/24; out-of-sample base rate 4/224 = 1.8%), on a macro sell-off day, with calm funding.** Full ruling → `thesis/THESIS.md` v1.2.7.

---

## Current Dashboard

*Rates rows updated **2026-09-28 16:19 ET to the OFFICIAL 9/28 Treasury par/real cells** (FRED frontier still 9/25). Credit rows pulled live **2026-09-28 10:34–10:43 ET (intraday; B/BBB tiers 10:43–11:11)** via `monitors/boot_recompute.py` + `fetch.py` (cache-busted) + the U.S. Treasury par/real curve CSV for the **9/25 official cells** (FRED frontier is 9/24 for H.15; credit 9/25). Intraday vendor marks are labelled and are NOT official closes. No naked numbers.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.56%** | 🔴🔴 | [CONF **U.S. Treasury par curve 9/28** = H.15 source; FRED 5.49 [9/25]] — **+7bp; 4th straight fresh 2026 high; highest close since 2004-06-14 (5.58)**; run ≥5.00 = 59 on the Treasury cell. 20Y 5.60 |
| 10Y (DGS10) | **5.24%** | 🔴 | [CONF Treasury **9/28**; FRED 5.17 [9/25]] — **+7bp; highest close since 2007-06-12 (5.26)** (BOND computation, FRED full series) |
| 5Y (DGS5) | **5.06%** | 🔴 | [CONF Treasury **9/28**, +8] |
| 2Y · 1Y | **4.92% · 4.59%** | 🔴 | [CONF Treasury **9/28**] — **2Y +11 = the day's largest mover; highest since 2024-05-30**; 1y1y ≈ **5.25** (2×2Y−1Y par approx; 5.12 [9/25]). 2s10s +32, **2s30s +64** (was 68: **bear FLATTENER on 9/28**, front-end-led) |
| **10Y real (DFII10)** | **2.90%** | 🔴🔴 **GATE THROUGH · SUSTAIN MET** | [CONF **Treasury real curve 9/28**, +7; FRED 2.83 [9/25]] — **last matched 2008-11-24; 99.7th pct since 2003**. 30Y real 3.28, 5Y real 2.73. **WQ-246 count: 11 consecutive FRED closes ≥2.50 (9/10–9/24), 12 on the Treasury cell** — met, authorises no add |
| 5Y5Y fwd (T5YIFR) | **2.35%** | 🟡 | [CONF FRED **9/28** (Treasury-curve schedule, a session ahead of H.15)] — **15bp from 2.50** |
| 10Y BE (T10YIE) | **2.34%** | 🟡 | [CONF FRED **9/28**; Treasury par−real 9/28 = 2.34, flat] — **9/28 was real-led again** (real +7, BE 0); Friday 9/25 was not |
| ACM 10Y TP · KW TP | **0.7747** [9/25] · **0.9595** [9/18] | 🟠 ↑ | [NY Fed ACM Daily · FRED `THREEFYTP10`, **now pulled every boot by `monitors/rates_context.py`** (17:38 ET 9/28)] — ACM **+13.9bp over 5 obs**; KW −0.1 over 5 obs (frontier 10d old). *Different window/horizon from the FF strip: consistent with both channels, not a causal split (CATO 9/28).* FORUM-7 P2 (KW 9/21–9/24) = HENRY's lead. **Name the model in any TP claim** |
| **Fed path (FF futures)** | **peak of available strip 4.855% [Nov-27; strip Sep-26→Jan-28]** · 10/28 hike ≈**68%** (hold-or-+25 reading) | 🟠 ↑ | [CBOT ZQ via yfinance, **vendor last trade, NOT settlement**, read 17:38 ET 9/28; EFFR 3.88 [9/25]; every boot via `rates_context.py`] — terminal **+97.5bp ≈ 3.9 hikes**, **+18bp over 5 obs**; Jan-28 −4.5 from peak. HENRY owns the read; BOND consumes |
| **HY OAS** | **293bps** | 🟠 ↑ | [CONF FRED **9/25**] — **+25bp in 3 sessions (~97th-pct velocity)**; 7bp from 300; 2026 max 346 |
| **CCC OAS** | **1128bps** | 🔴 ↑ | [CONF FRED **9/25**; 1112 [9/24] first-published] — **1100 escalation FIRED 9/24**; 9bp under span max 1137 [2025-04-07] |
| IG OAS · BB OAS | **81 · 176bps** | 🟢 · 🟡 ↑ | [CONF FRED **9/25**] — BB +20 in 3 sessions |
| CCC−BB tail gap | **952bp** | 🔴 ↑ | [CONF FRED, BOND computation **9/25**] — new span max (948 [9/24]) |
| **FR2004 long-end** | **$144.4B** [as-of 9/16] | 🟡 | [NY Fed, published 9/24 16:16 ET] — −$1.8B w/w; 11-21Y $68.5B (+1.7), >21Y $40.8B (−2.6). **Next: as-of 9/23 Thu 10/1 ~16:15 = the WQ-291 3–6Y grade (≥ $56.586B)** |
| **SOFR − IORB** | **0bp** | 🟡 ↑ | [CONF FRED SOFR 3.90 · IORB 3.90, **9/25**] — up from −3 [9/23] into quarter-end; not positive. LIQUID owns |
| TLT · MOVE | **$78.62 −0.88%** [9/28 close-area, yfinance 16:19 ET] · **96.00** [vendor ^MOVE 9/25] / 104.58 [VIOLET 9/24] | 🟠 · 🔴 | [yfinance — a MOMENT property, re-pull at any decision, root rule #4] 77P strike **2.0% below spot**, expiry 9/30. MOVE: two sources, VIOLET owns |
| Global 10Y (9/28 intraday) | UK 5.41 · DE 3.63 · FR 4.76 · IT 4.59 · JP 3.10 · CA 3.99 · AU 5.43 | 🟠 `[HANS/SAM own]` | [TE bonds page, fetched 9/28 before 10:43 ET, secondary] — JGB 30Y 4.18, 40Y 4.23. **Name the basis** (UK: BoE IADB par vs TE, `KB-BND-319`) |
| USD/JPY · oil · VIX | **cite SAM · BRENT · VIOLET** | — | this desk keeps no copy (vendor Brent front quote on 9/28 looks like a roll artifact — do not use) |

### Gate distances *(recomputed this session, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — TLT-put add-gate (a)** | 🔴 **THROUGH by 40bp** [2.90, Treasury 9/28] · 33bp [2.83, FRED 9/25] | **Sustain leg MET under WQ-246 (5 consecutive; 11 FRED closes)** — authorises NO add (NO-ADD 7/16 + WQ-280) |
| **Auction re-arm (OLD conjunctive) — TLT-put add-gate** | 🔴 **MET 9/23 (5Y)** | ✅ **ADD DECLINED — WQ-280 RULED 9/24 13:17 ET.** Spent on 004 |
| **Kill dealer leg, 9/23 5Y (WQ-291)** | as-of 9/23 must be ≥ **$56.586B** (PRE $47.986B) | ⏳ prints **Thu 10/1 ~16:15**; funding window for this fire **UNGRADED** by ruling |
| T5YIFR >2.50 | 15bp [9/28] | 🟡 |
| DGS30 >5.00 · DGS10 >4.50 | — | 🔴 BREACHED (run 59, Treasury cell 9/28) · 🔴 BREACHED |
| HY OAS >300 (BOND row-4 marker — **not** a capital reopen; X1 CLOSED 8/28) | **7bp** [9/25] | 🟠 closing fast |
| CCC >1100 escalation | **FIRED 9/24** (+12; +28 on 9/25) | 🔴 `BND-27` FALSE |
| Credit-equity lead (HY +75–100 from the 263 trough, VIX <20) | 45–70bp | 🟡 moving (HY 293; VIX 15.87 intraday 9/28, vendor) |

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **4** = | 🔴 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | Moved 3→4 on 9/23 (fresh DGS30 high WITH weak composition). **Since: 5.47 [9/24] → 5.49 [9/25] = 3rd straight fresh high; 9/28 intraday vendor 5.55; global sell-off 4th session** (`KB-BND-340`) — fresh highs are not the ⇒5 letter | ⇒5: a composition failure on a LONG-END auction (next: 10/7 10Y-R, 10/8 30Y-R) or the paired kill's mechanism leg confirming |
| 2 | Treasury auction health | **3** ▲ | 🟠 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED (tail) | **9/23 5Y: BTC 2.21 < 2.28 cover bar (and <2.3 KEY-THRESHOLD cover marker) + OLD composition failure + `I'`; 7Y `I'` by 0.04pp.** ⛔ `I'` alone = MARKER, no action (WQ-157 ② PARKED 9/25). Paired kill (Sept-4 rule, in force) NOT fired (funding NONE per LIQUID; **FR2004 POST for the 9/23 (Wednesday) 5Y = the 9/23 as-of, ~Thu 10/1 on the trade-date window** — the as-shipped join would use 9/30, ~10/8; read both) | A composition failure with the funding/FR2004 leg CONFIRMED (paired kill) ⇒ 4 |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | FR2004 9/16 long-end $144.4B (−$1.8B; 11–21Y +1.7, >21Y −2.6) — **ADMISSIBLE as absorption evidence: settlement question resolved 9/25, the 9/15 award is in the print (trade-date, `KB-BND-332`)**; next: 9/23 as-of ~10/1 = the 5Y's POST; 5Y dealer 15.77 is the trailing-12 max but ordinary vs 2023–24. **9/24 20–30Y buyback: $4.078B of $6B, F2 0.02% ⇒ OFF-THE-RUN (2 of 2 ops)** | Two consecutive builds on TOTAL with weak composition, or SOFR−IORB positive; F2 ON-THE-RUN fire |
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `VX-BND-11` | **HY 293 [9/25], +25bp in 3 sessions (~97th pct) — the index joined; CCC 1100 FIRED 9/24 (1128 [9/25], `VX-BND-11` 3→4); CCC−BB 952 span max** (`KB-BND-341`). **Primary access OPEN for large credits (SoftBank $11.1B 9/23–24); pulled-deal leg unverifiable (`KB-BND-346`)** | HY >300 with velocity (**7bp short; velocity leg present**), or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 81 [9/25] (+4 in 3 sessions) | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF z20 +1.01 [9/25] — **rate-confounded in this tape; cash OAS is the leg to read** (`KB-BND-345`) | Synthetic leading cash, sustained |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY +30 from the 263 trough; 45–70bp headroom | HY +75–100bp from 263 while VIX <20 |

**Composite: 14/35 — UNCHANGED since 9/24** (▲2 on 9/23–9/24: row 1 3→4 on its registered letter, row 2 2→3 on the pre-registered cover-marker rule). **9/28: no row moves.** Row 4 is the one to watch — its letter needs HY >300 with velocity and the velocity is already there (293, +25bp/3 sessions); the CCC escalation (`VX-BND-11` 3→4) lives beneath the row and does not move it by itself. Distribution: 🔴 1 · 🟠 1 · 🟡 2 · 🟢 3. **Re-summed: 4+3+2+2+1+1+1 = 14 ✅.** `VX-BND-01` write-back done 9/28.

**Outside the composite:** `VX-BND-15` inflation anchoring (2) · `VX-BND-17` MBS relay (1) · `VX-BND-18` FHLB (2) · `VX-BND-19` EZ rates (3 — HANS: ECB T-04 no longer a hawkish lean; German 2027 debt service +38%; "disorderly" UNDEFINED → 10/1) · `VX-BND-20` benchmark UST demand (2, checkpoint 10/6).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 0.** **Resolved 9/28:** `BND-27` **FALSE** (65%, a MISS — CCC 1112 [9/24] ≥ 1100). **9/24:** `BND-25` **TRUE** (55%) · `BND-26` **FALSE** (70%). **Tally: 14 TRUE · 13 FALSE · 1 VOID** — the last two resolutions are both MISSES and both in the hawkish/stress direction (the desk under-called the move it believes in). Archives: `thesis/archive/PREDICTIONS_resolved_*` (BND-25→29 archived 9/28; live file = header only). ⚠️ **No OPEN predictions; the 10/28 FOMC curve-shape row is owed with a base rate by 10/21.**

---

## Trade Interface *(full view → `TRADE.md`; construction is TERRY's lane)*

- **TLT puts (Sep-30 77P ×20 — 5 of 25 sold 9/10, `FORGE/STATUS.md:54`) — HOLD, no add, `$0`.** Both add-gates read through (DFII10 sustain MET under WQ-246; OLD-conjunctive re-arm 9/23) — ⛔ **neither is an add: WQ-280 DECLINED 9/24; 7/16 NO-ADD; root rule #5.** **TLT 78.61 intraday 9/28 ⇒ strike 2.0% below spot with 2 sessions to the 9/30 expiry — harvest/expiry is TERRY's rail; re-pull live before any call.** *Posture, never a direction.*
- **HYG puts — closed at the INDEX level** (HY 293 [9/25], 7bp under BOND's 300 marker). CCC tail FIRED 1100 → expression single-name/CCC, **never HYG**. ⛔ a >300 close is BOND's own marker (matrix row 4 ⇒ 3), **NOT a capital reopen**: the index-protection SIZING question sits behind LIQUID's X1 gate, CLOSED 8/28 (BROCK `KB-BRK-219`, wrapper half NOT ARMED; fail-safe DON'T-SIZE) — a level print does not undo it. It reopens only via BROCK's **10/02 re-adjudication sitting** (DOCKET L494), then TERRY's card + Will. Registered HY lines: RED-FT-01 (RED's) · LIQUID X1 (strict >280 AND BROCK's wrapper conjunct). *(Corrected 2026-09-28 15:22 ET on PROME's relay via Will; verified at `BOARD/SIG-W-20260925-013` + DOCKET L494. This line previously said a >300 close "reopens" the HYG-put question — wrong on the fleet's record.)*
- **Credit-equity lead — inactive.**

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all duration shorts).** WQ-157 leg ① (Will 9/4): **`I'` + a NON-AUCTION mechanism confirmation (FR2004 dealer stock and/or SOFR−IORB)**. 🔴 **9/23 5Y dealer leg RULED (WQ-291, Will 9/26; `KB-BND-342`): FR2004 3–6Y, MET iff as-of 9/23 ≥ $56.586B (Thu 10/1 ~16:15; grader `analysis/2026-10-01_wq291_grade.py`)** — riders: net inventory ≠ proof of warehousing; funding window for this fire UNGRADED; no predictive claim; a fire = recommendation via TERRY's card + Will. Funding leg UNMET (SOFR−IORB −3 [9/23], LIQUID NONE on every observable, `KB-BND-330`) ⇒ **KILL NOT FIRED; dealer leg evaluable 10/1.** 9/15 20Y-R pairing graded 9/24: TOTAL legs NOT met, 11–21Y met (admissible, `KB-BND-332`). Unpaired `I'` fires: 9/15 20Y-R · 9/23 5Y · 9/24 7Y. **Leg ② PARKED (Will 9/25): corrected evidence INCONCLUSIVE (TOTAL >$1B p=0.691, inversion p=0.248; `KB-BND-335`); `I'` ALONE = MARKER, authorizes NO action.** Also: 10Y back below 4.15 ×3 with clean auctions ⇒ spent. Full history → THESIS + the 9/28b snapshot.
- ⚠️ `I'` bars: `monitors/AUCTION_HEALTH.md` §GRADING BASIS. **Grader defect `KB-BND-314` FIXED 9/24 (`71963a7b7`, `grade_auction.cycle_term()`): cross-cycle reopenings now keyed to their cycle; blast radius exactly 2 rows (Jan-26 `91282CGH8`, Feb-25 `91282CGQ8`); no verdict changed.** ⚠️ The 9/2 per-tenor base-rating and the WQ-157 join used the pre-fix pools — not re-run; disclose if re-cited.
- 🔴 Direction disclosed: `I'` is the easier test and its firing confirms this desk's own bear thesis.

**2 · POSITION-SPECIFIC.** TLT puts: kill on 10Y <4.15 AND 30Y <5.0 ×3 sessions AND a clean refunding (THESIS §2). Expiry 9/30 is TERRY's rail.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal coupons passing both legs (indirect ≥ median AND dealer ≤ median). **Counter 0** (2Y failed the dealer leg 13.19 vs 11.33; 5Y and 7Y failed indirect). Next eligible: 10/6 3Y.

**4 · TIME-BASED.** Quarter-end + PCE + expiry **9/30** · **FR2004 as-of 9/23 = WQ-291 grade + FORUM-7 FINAL, Thu 10/1 ~16:15 (report by the 10/2 boot)** · F2 reads **10/1 · 10/8 · 10/15 · 10/27 · 11/4** · quarterly `I'` refresh + `VX-19` definition **10/1** · `VX-20` **10/6** · FOMC curve-shape row **by 10/21** · FHLB Q3 **11/9** · FRBNY FX **11/13** · US-sov-CDS re-test **12/1**.

⚠️ **RETIRED, NOT REVIVABLE: the auction TAIL.** The 9/23 "2nd biggest tail ever" wire claim is `[med-conf]` and fires nothing.

---

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| ✅ **Mon 9/28 — LIVE** | Global long-end sell-off, 4th session (not docketed — live event) | official 9/28 cells ~evening; HY vs 300 on the 9/28 print (~9/29); Paramount HY pricing (access test) |
| **Wed 9/30** | 🔴 **Quarter-end · Aug PCE + Q2 GDP 3rd (8:30) · TLT 77P expiry** (`BND-27` already resolved FALSE 9/28) | PCE vs the PMI input-price shock; SOFR−IORB across quarter-end (0bp [9/25]); ~$183B settlement on the turn (LIQUID reads) |
| **Thu 10/1** | 🔴 **FR2004 as-of 9/23 (~16:15) = WQ-291 5Y dealer-leg grade (≥ $56.586B) + FORUM-7 FINAL** · H.4.1 week-9/30 · quarterly `I'` refresh · `VX-19` "disorderly" · **10Y–20Y buyback op (F2)** · Oct refunding sizes | MET / NOT MET / GAP with margin by the 10/2 boot; `AUCTION_HEALTH.md` §3d |
| **Fri 10/2** | Sept Employment Situation (8:30) | 2Y / 1y1y reaction |
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

**[2026-09-28 Mon, updated 16:2x ET on the official close.]** **The bond sell-off is in its fourth day and global; what is extreme is how high yields are and how long it has lasted, not any single day.** The official 30-year closed **5.56% today** (+7bp; the fourth record-for-the-year close in a row and the highest since June 2004); the 10-year closed 5.24%, its highest since June 2007. **Today's twist: short-term yields led** (2-year +11bp to 4.92%), which means markets are pricing more Fed hikes, not just demanding extra pay for long bonds. The rise is in real (after-inflation) yields, not inflation pricing.

**Credit joined, but the door is still open.** Junk spreads widened 25bp in three days to 293bp (7bp from 300bp — BOND's own warning marker; it does **not** reopen index hedging, which stays shut by the 8/28 X1 ruling until BROCK's 10/02 sitting says otherwise, then TERRY's card and your approval), and the lowest-rated tier crossed this desk's 1,100bp alarm line — my 65% call that it wouldn't was wrong. **But big borrowers are still getting deals done:** SoftBank sold a record $11.1B junk deal last week with over $30B of orders, and Paramount launched ~$12.4B today. **Caveat that matters:** I could not check whether smaller deals were pulled — the trackers that record that are paywalled — so "open" is shown for large issuers only, not proven for the weak ones.

**Auction warning still unconfirmed.** The 9/23 auction weakness needs dealer balance-sheet confirmation; that test prints **Thursday 10/1 ~4:15 PM** (5Y-bucket dealer inventory ≥ $56.586B = met), and the grading script is built and dry-run. It lands after Wednesday's option expiry.

**Position: TLT Sep-30 77P ×20 HOLD, no add, `$0`, expiry 9/30 (strike ~2% below TLT 78.6 intraday 9/28 — TERRY's rail; re-pull live). Composite 14/35 (unchanged). Counter 0. OPEN predictions 0.**
