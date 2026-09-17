# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension, integrated 7/1; + the sovereign-credibility instrument set per the Will-ruled 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-17 ~08:2x ET → (PROME WQ-184 L0 spawn `prome-ae`, DOCKET **L404** TIPS-R grade + **L401** F2 carrier; markets OPEN; **TIPS-R prints 1:00 PM**) · **Prior:** 2026-09-15 ~10:0x–13:4x ET

> 📕 **THIS FILE IS HOT/COLD SPLIT AND ROTATED. NOTHING HAS EVER BEEN DELETED FROM IT.** Complete pre-split snapshot: `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md` (160,077 B, crc32 `1210262`). **Everything rotated since lives in `domain/sources/` and `archive/`, each file verbatim and crc-stamped in its own header.** **Rotated 9/17:** the 9/15 BOTTOM LINE · the add-gate breach block · the "held against evidence" paragraph · the fired 9/10–9/16 catalyst rows → `domain/sources/2026-09-17_STATUS_archive_rotated_9-15-blocks.md` (crc32 `1463914424`).
> **What stays hot: every live value, score, gate, exit criterion and dated catalyst.** Canon: `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`. **Budget 32,550 B — never raise it; rotate instead.**

**Canonical elsewhere — this file carries NO second copy:** thesis + full falsification → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalyst source of truth → `docket/CATALYSTS.tsv` · positions/gates → `TRADE.md` · durable learnings → `MEMORY.md` · session handoff → `SCRATCH.md`.

---

## Regime (one-line)

**Real-rate / higher-for-longer.** ★ **C-36 = TWO-PART (ruled 9/1): the policy-path channel is ALIVE AND TRANSMITTING · term premium drove the July delta.** 🔑 **9/16 FOMC: +25bp to 3.75–4.00 (12–0), SEP median terminal 4.125 — 60–85bp BELOW the curve's own priced terminal — and the curve did not reprice down (`KB-BND-293`). The priced path is a MARKET view, not a guidance view.** Full ruling + caveats: `thesis/THESIS.md` v1.2.7, `thesis/CHANGELOG.md`.

**The configuration, restated:** the long end is engaged (30Y **50-session run ≥5.00%**, 66 days in 2026 of 177; 2026 high 5.37 [9/10]; 5.36 [9/15]) with **no Fed coupon backstop post-QT** ⇒ absorption is private/foreign/dealer — **plus an official 10–30Y liquidity-support bid that has run ONCE at scale (9/10, 1.75× cover — AMBIGUOUS on normalisation, `KB-BND-285`).** **Auctions remain "expensive, not broken": the 9/15 20Y-R fired `I'` (−9.25pp) as a 🟠 MARKER with the mechanism intact (bid substituted, BTC 2.57); the kill is PAIRED and its FR2004 leg lands TOMORROW 9/18.** 🔴 **Credit: HY +11bp in two sessions to 276 while CCC 1085 makes another 2026 high; CCC−BB 924 (span max 926 [9/11]).**

---

## Current Dashboard

*Every value pulled live via `monitors/boot_recompute.py`, cache-busted **2026-09-17 08:27 ET**, unless tagged. **No naked numbers.***

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.36%** | 🔴 | [CONF FRED **9/15**] — 1bp off the 5.37 [9/10] 2026 high; **100.0th pctile post-2010**; 50-session run ≥5.00. Vendor `^TYX` 5.349 [9/16] |
| 10Y (DGS10) | **5.00%** | 🔴 | [CONF FRED **9/15**] — 100.0th pctile post-2010. `GATE-TERRY-007` counter **0 of 5** (closes <4.50), distance **50bp**; vendor 5.006 [9/16] |
| 2Y (DGS2) · 1Y (DGS1) | **4.67% · 4.39%** | 🟠 ↑ | [CONF FRED **9/15**] — 4.56 → 4.63 → 4.65 → **4.67**; **1y1y (2×2Y−1Y) = 4.95 = `BND-26`'s line, one day before its window opens** |
| **10Y real (DFII10)** | **2.62%** | 🔴 **GATE THROUGH** | [CONF FRED **9/15**] — **+12bp above 2.50**; 2.55 · 2.60 · 2.60 · **2.62** = **4 published sessions ≥2.50 ⇒ `BND-29` TRUE**. 98.8th pctile full (n=5,930), 100.0th post-2010 |
| 5Y5Y fwd (T5YIFR) | **2.31%** | 🟡 ↓ | [CONF FRED **9/16**] — −4bp on FOMC day; 19bp from its bar |
| 10Y BE (T10YIE) | **2.33%** | 🟡 ↓ | [CONF FRED **9/16**] — 2.38 → **2.33** on FOMC day: **breakevens FELL while TIP −0.38% ⇒ the 9/16 move is REAL-led again** (`KB-BND-293`); Brent −7% on 9/17 morning pushes the same way (BRENT's lane) |
| ACM 10Y TP · KW TP | 0.7073 [9/9] · 0.8892 [9/4] | 🟠 `[STALE 9/17]` | [NY Fed `ACM Daily` · FRED `THREEFYTP10`] — not re-pulled this session; 2026 max 0.8935 [8/17] / 0.8996 [9/1] |
| **HY OAS** | **276bps** | 🟢 ↑ | [CONF FRED `BAMLH0A0HYM2` **9/15**] — 265 [9/11] → 271 → **276**: +11bp in two sessions, still inert at the index (2026 max 346) |
| **CCC OAS** | **1085bps** | 🟠 ↑ | [CONF FRED `BAMLH0A3HYC` **9/15**] — **fresh 2026 high** (1076 → 1081 → 1085); ratio 3.93x; **15bp from the 1100 line** |
| IG OAS | **80bps** | 🟢 = | [CONF FRED `BAMLC0A0CM` **9/15**] — zero pulled deals; record-September supply forecast (~$215B, secondary 9/3) |
| CCC−BB tail gap | **924bp** | 🟠 | [CONF FRED, BOND's computation **9/15**] — BB **161** (+11bp in two sessions) widened WITH CCC (+9) ⇒ the gap paused 2bp under the 926 span max; **index and tail moved the SAME way this time** — dispersion paused, not reversed |
| **FR2004 11–21Y** | **$66.8B** [as-of 9/2] | 🟡 `[STALE]` | [NY Fed `SBN2024`, re-pulled **9/17 09:1x**] — **the 9/9 as-of is NOT YET PUBLISHED (latest 9/2; checked at the API 9/17; re-test: 2026-09-18 with the join)**; long-end TOTAL $144.7B (−$7.1B w/w) even as 11-21Y built |
| IORB · DFF | **3.90 [9/17]** · 3.63 [9/15] | 🟢 | [CONF FRED] — the hike in the administered rate; SOFR not re-pulled (LIQUID owns) |
| TLT · TIP · ^MOVE | **$80.88 +0.21%** · $105.39 −0.38% · 80.73 | 🟠 | [yfinance **9/16 close**, via the repo venv — a MOMENT property, re-pull at any decision (root rule #4)] |
| JGB 10Y · EA AAA 10Y · UK 10Y · Bund/OAT/BTP | 2.891 [MOF 9/9] · 3.378 [ECB 9/8] · 5.108 [BoE 9/7] · 3.40/4.26/4.29 [TE 9/9, secondary] | 🟠 `[STALE 9/17]` | Not re-pulled this session; SAM / HANS / LIQUID own the levels |
| USD/JPY · Brent · VIX | **cite SAM · BRENT · VIOLET** | — | owners' STATUS files — this desk keeps NO copy (Brent −7.05% / VIX −11% at 08:3x cited for the breakeven confound only) |

### Gate distances — the numbers that drive decisions *(recomputed every boot, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — the ONLY live TLT-put add-gate** | 🔴 **THROUGH by 12bp** [2.62, **9/15**], 4 published sessions | 🔴 **LEVEL leg fired 9/10 and has HELD** (`BND-29` TRUE). ⛔ **Authorises NO add:** "sustained" has no session count (**WQ-246, with Will**); 7/16 NO-ADD; root rule #5; `$0`. Spec defect `KB-BND-278` unchanged. 🔑 **The dovish SEP that was the named threat to this breach ARRIVED (terminal 4.125) and reals rose anyway.** Protocol record → `domain/sources/2026-09-15_STATUS_rotated_add-gate-breach-protocol_9-14.md` |
| T5YIFR >2.50 (inflation-unanchor) | 19bp [9/16] | 🟡 |
| DGS30 >5.00 (long-end level) | — | 🔴 **BREACHED**, 50-session run, 66 days of 177 [9/15] |
| DGS10 >4.50 (arm-#2 line) | — | 🔴 **BREACHED** (5.00) |
| HY OAS >300 (reopen HYG) | 24bp [9/15] | 🟢 (was 35 on 9/11) |
| CCC >1100 escalation | **15bp** [9/15] | 🟠 closing ~5bp/session (24 → 19 → 15) |
| Credit-equity lead reactivate (HY +75–100 from the 263 trough) | 62–87bp [9/15] | 🟢 inactive |

### FR2004 dealer stock — 9/2 as-of [re-pulled 9/17 09:1x: the 9/9 as-of is NOT YET PUBLISHED; re-test: 2026-09-18]
11-21Y **$66.8B (+$1.8B w/w, second consecutive bucket build)**, >21Y $47.0B, 7-11Y $30.9B; **long-end TOTAL $144.7B, −$7.1B w/w and −9.2% off the 7/29 peak** — the bucket built while the total fell. `VX-BND-04` **holds at 2** — the trigger is two consecutive builds on TOTAL, and a build into a strongly-cleared week is distribution, not warehousing. 🟢 **WQ-157 leg ② premises CLOSED 9/14** (ceiling n=244 VERIFIED; SBN2022/SBN2024 pooling DEFENSIBLE, INFERRED). ⛔ **THE JOIN ITSELF IS UNBUILT AND DUE TOMORROW 9/18 — a live `I'` fire (9/15) sits on the other side of it; the paired kill is UNEVALUABLE until it lands.** Detail → `domain/sources/2026-09-15_STATUS_rotated_WQ157-premises_9-14.md`; probe → `analysis/2026-09-14_FR2004_SBN2022-SBN2024_comparability-probe.md`.

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **3** = | 🟠 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | 30Y 5.36 [9/15], 1bp off the 2026 high, 50-session run ≥5.00; **DFII10 2.62 = +12bp through the gate, 4 sessions (`BND-29` TRUE)**; **the dovish SEP did not unwind it**; KW TP 0.8892 [9/4 stale] | DFII10 ≥2.50 sustained (count = WQ-246), or a fresh DGS30 high with weak composition |
| 2 | Treasury auction health | **2** = | 🟡 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED | **9/15 20Y-R: FIRST `I'` FIRE (−9.25pp) — 🟠 MARKER, mechanism intact** (bid substituted, BTC 2.57, dealers 16.85 < max); OLD conjunctive NOT fired; kill PAIRED, FR2004 leg due 9/18. **9/17 TIPS-R ⏳ 1PM (no `I'`, never counts).** Downgrade counter **0** | A composition failure with the FR2004/funding leg confirmed (paired kill), or 3 consecutive nominal coupons passing both legs (counter **0**) |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | FR2004 9/2: 11-21Y $66.8B (+$1.8B, 2nd build) but long-end TOTAL $144.7B (−$7.1B) [9/9 as-of unpublished at the 9/17 check]. **Buybacks: 9/10 10–20Y $5.187B/$6B, OFF-THE-RUN (F2 read routed); 9/15 TIPS op $0.5B/$2.088B; 9/17 7Y–10Y op $4B cap TODAY — both outside the F2 letter; F2 carrier LIVE (`buyback_f2.py`), next in-scope op 9/24 20–30Y** | A further 11-21Y build **with** weak composition or SOFR−IORB positive; F2 ON-THE-RUN fire (>50% newest-quartile, base rate 0/52) |
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `VX-BND-11` | HY **276 [9/15], +11bp/2 sessions**, zero pulled deals, primary open; **CCC 1085 = fresh 2026 high, 15bp from 1100 (`BND-27` 65% no-breach, momentum against it)**; CCC−BB 924 | HY OAS >300 with velocity (24bp), or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 80; record-September supply forecast, issuers pulling forward (`KB-BND-259`) | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF 0.8585, z20 +1.28 [9/8, STALE] — credit-excess RICH, no divergence | Synthetic leading cash on a sustained basis |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY 62bp below the reactivation band [9/15] | HY +75–100bp from the 263 trough while VIX <20 |

**Composite: 12/35 — UNCHANGED for a FIFTEENTH consecutive scoring session** (… 9/10 · 9/14 · 9/15 · **9/17**). *Held: row 1's trigger reads "≥2.50 SUSTAINED" and the count is Will's (WQ-246) — 4 sessions is the factual input, not a ruling; row 2's `I'` fire is a marker by the 9/11 pairing rule; row 3's official bid ran once and its cover is ambiguous on normalisation. Nothing crossed a pre-registered line this session; the TIPS print at 1PM cannot move any of them by rule.* Distribution: 🟠 1 · 🟡 3 · 🟢 3 · 🔴 0.
**Re-summed and verified against the vector scores this session: 3+2+2+2+1+1+1 = 12.** ✅

**Tracked OUTSIDE the composite:** `VX-BND-15` inflation-expectations anchoring (2) · `VX-BND-17` MBS / housing-finance relay (1) · `VX-BND-18` FHLB advances (2) · `VX-BND-19` eurozone rates / ECB shock (3 — ECB 2.50% DFR eff. 9/16; **"disorderly" qualifier UNDEFINED, define at the 10/1 refresh, `KB-BND-256`**) · `VX-BND-20` benchmark-driven structural UST demand (2 — GPFG proposal; checkpoint **10/6**; `monitors/BENCHMARK_DEMAND.md`).

> ⚠️ **OPEN MIRROR DIVERGENCE, un-reconciled (9th session): `VX-BND-05` = 4 and `VX-BND-16` = 4 in `workbook/VX.tsv` vs matrix rows 3 and 2 — components HOTTER ⇒ the divergence UNDER-states risk.** Flagged, not silently reconciled. Notice archived at `domain/sources/2026-09-04_STATUS_archive_mirror-divergence-notice.md` (crc32 `2218422141`).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

✅ **OPEN: 3** — `BND-25` (belly-led FOMC session, 55% — **grades on the 9/16 H.15 cells, ~16:15 ET 9/17**; vendor proxies point TRUE: 5Y +3.3 vs 10Y +1.0, 30Y −1.5, 3M +1.0 — NOT resolved on proxies) · `BND-26` (1y1y fwd <4.95 thru 9/23, 70% — **the 9/15 cell computes to EXACTLY 4.95, one day before the window; the 9/16 cell decides whether the row is dead on day 1**) · `BND-27` (CCC <1100 thru 9/30, 65% — **15bp away, closing ~5bp/session, momentum against the TRUE side**). 🟢 **`BND-29` RESOLVED TRUE 2026-09-17 at 70% ⇒ a HIT** (DFII10 2.55/2.60/2.60/2.62 = 4-of-4 ≥2.50; the sustain SUBSTANCE, not the count — WQ-246 unchanged). 🟢 `BND-28` TRUE 9/15 (80%).
**Live file holds `BND-25` → `BND-29`; `BND-22`→`BND-24` archived 9/14 (`thesis/archive/PREDICTIONS_resolved_BND-22_to_BND-24.tsv`, crc32 `2391597581`); `BND-01`→`BND-21` in `thesis/archive/…BND-01_to_BND-17.tsv` and `…BND-18_to_BND-21.tsv` (crc32 `3942345676`).** Resolved tally: **13 TRUE · 11 FALSE · 1 VOID.**

---

## Trade Interface *(full view → `TRADE.md`; positions are TERRY's construction lane)*

- **TLT puts — HOLD, NO ADD.** 🔴 The only live add-gate (**DFII10 ≥2.50 sustained**) is **through on its level leg for 4 published sessions (2.62 [9/15], +12bp)**; the sustain COUNT is undefined (WQ-246). **A LEVEL FIRING IS NOT AN ADD.** 🔑 **The 9/16 SEP was the named dovish threat and it did not unwind the move; `GATE-TERRY-007` is 50bp away (DGS10 5.00) and the dovish-rally route delivered nothing** — TERRY's lane, stated not proposed. ⛔ **Will's 7/16 NO-ADD governs; root rule #5; harvest/roll/sizing are TERRY's (expiry 9/30).** *POSTURE, never a direction.*
- **HYG puts — stay closed at the INDEX level.** HY **276 [9/15]** (+11bp in two sessions; still 24bp from the 300 reopen line); access unimpaired, zero pulled deals. **Residue = the CCC tail: 1085, 15bp from 1100** — if it arms: single-name/CCC, never HYG.
- **Credit-equity lead — inactive.** 62bp headroom [9/15].

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all).** 🔴🔴 **WQ-157 LEG ① (Will 9/4): `I'` STANDALONE THROUGH 9/10; PAIRED THEREAFTER — pairing instrument = the FR2004 weekly join, DUE 9/18 (TOMORROW).** Both standalone evaluations done, neither fired (9/9 +14.13pp · 9/10 +16.55pp). 🔴 **The 9/15 20Y-R FIRED `I'` (−9.25pp pooled / −12.20pp alt) INSIDE the paired window with the pairing instrument UNBUILT ⇒ the kill leg is UNEVALUABLE until the join lands.** Ceiling n=244 + comparability: FR2004 block above.
- **NEW test (Will-ruled 8/27):** indirect below that tenor's own trailing-12 15th percentile, SUFFICIENT ALONE (dealer descriptive; >18% = contrarian-bullish). **Bars canonical at `monitors/AUCTION_HEALTH.md` §GRADING BASIS; 2Y/5Y/7Y RE-FROZEN 9/17 for 9/22–24 — 54.82 / 60.27 / 57.24, unchanged.**
- **OLD (dual-print, retained):** indirect below trailing-12 min **AND** dealer above trailing-12 max, same tenor. ⛔ **The TLT-put ADD re-arm in `TRADE.md` runs on the OLD, STRICTER test** (WQ-99, Will 9/1). Never loosen an add gate as a side effect of a definition reconcile.
- 🔴 Direction disclosed: the new test is STRICTLY EASIER TO FIRE and its firing CONFIRMS this desk's own bear thesis. Percentages are of **competitive accepted**; never reuse another tenor's numbers.

**2 · POSITION-SPECIFIC.** TLT puts: **kill on 10Y <4.15 AND 30Y <5.0 for 3 sessions AND a clean refunding** (THESIS §2 letter, one spec on all three surfaces since 9/9), or the thesis kill. Expiry 9/30 and the 60-DTE rail are TERRY's.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal-coupon auctions passing **both** legs (indirect at/above median **and** dealer at/below median). **Counter = 0 — RESET by the 9/15 20Y-R** (failed both legs). **TIPS never count: the 9/17 print cannot move it.** Next eligible: 9/22 2Y.

**4 · TIME-BASED.** FR2004 weekly join **9/18** (WQ-157 leg ②). **F2 per-op reads: 9/24 · 10/1 · 10/8 · 10/15 · 10/27 · 11/4 (carrier `monitors/buyback_f2.py`, every boot).** Quarterly percentile-snapshot refresh + `VX-19` "disorderly" definition **10/1**. `VX-20` review **10/6**. FHLB Q3 report **11/9**. FRBNY FX report **11/13**. US-sovereign-CDS re-test **12/1** (`KB-BND-261`).

⚠️ **RETIRED AND NOT REVIVABLE: the auction TAIL (>2bp)** — TreasuryDirect publishes no when-issued ⇒ unscoreable by construction. Wire tails are `[med-conf]` and may never fire anything.

---

## Immediate Catalysts *(source of truth = `docket/CATALYSTS.tsv`; this is the human twin and must not diverge in event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| ⏳ **Thu 9/17 1PM** | **10Y TIPS REOPENING `91282CRE3` $19B** (settles 9/30) — **bars frozen 9/9 (`742d4533e`), reproduced 08:2x** | ind <56.08 AND dlr >17.79 · cover BTC <2.20 · medians 66.94 / 10.64 / 2.40. **No `I'`; TIPS never count.** Real stop vs DFII10 2.62; a stop >2.438 = highest 10Y TIPS stop since 2008-10-08 (TA_WS, n=139). Confound stated pre-print: day-after-FOMC + Brent −7% ⇒ real-yield-UP tape. → `analysis/2026-09-17_PREPRINT_TIPS-R_91282CRE3_SEP-grade_F2-carrier.md` |
| **Thu 9/17 1:40 PM** | **7Y–10Y liquidity-support buyback op, cap $4B, 10 eligible 2033-11 → 2036-02** | **OUT of the F2 letter's scope** (not a stepped-up sector) — recorded as context, no packet to RED. Post-1:40 nominal 7–10Y tape contaminated. |
| 🔴 **Fri 9/18** | **FR2004 WEEKLY JOIN — WQ-157 leg ②** (PROME WQ 157 · DOCKET L271) | Join coupon auctions to the contemporaneous FR2004 long-end print (+ SOFR−IORB); base-rate `I'` + mechanism confirmation; **state the SBN2022/SBN2024 comparability verdict.** n ≤ 244. **The 9/15 `I'` fire waits on it.** |
| **Tue 9/22 · Wed 9/23 · Thu 9/24** | **2Y `91282CRP8` · 5Y `91282CRN3` · 7Y `91282CRM5`** month-end cluster (+ 2Y FRN-R 9/23, excluded from every bar); sizes at the 9/17 announcement | **`I'` bars RE-FROZEN 9/17 (venv, P15, strictly prior): 54.82 · 60.27 · 57.24 — UNCHANGED**; OLD 53.21/24.12 · 59.24/15.61 · 56.42/13.14; cover BTC <2.44 · <2.28 · <2.40. Counter re-arms at the 2Y. |
| 🔴 **Thu 9/24 1:40 PM** | **20Y–30Y buyback op ≥$4B — the FIRST in-scope F2 read of the carrier** | `buyback_f2.py --op 2026-09-24` → packet to RED same day → ledger. Fire = recent_share >50% (base rate 0/52). |
| **Thu 10/1** | Quarterly `I'` snapshot refresh + RED's boundary fixture + **define `VX-19`'s "disorderly"** · **10–20Y op (F2)** | `monitors/AUCTION_HEALTH.md` §3d rail · carrier |
| **10/6 · 10/7 · 10/8 · 10/15 · 10/21 · 10/22 · 10/26–29** | `VX-20` review · 3Y/10Y-R/**30Y-R + 20–30Y op (F2)** · 10–20Y op · 20Y-R · 5Y TIPS · month-end cluster | bars frozen at each announcement (10/1, 10/15, 10/22); F2 per op |
| **10/27 · Wed 11/4** | 20–30Y op (F2) · **QRA + 10–20Y op — F1 (ratchet) / F3 (long-coupon cut) resolve; sb0607 window ends** | carrier + `VX-BND-16` |
| **11/9 · 11/13 · 12/1 · 2027-01-25** | FHLB Q3 report (`REG-T-06` leg 3, `VX-18`) · FRBNY Q3 FX report · US-sov-CDS re-test · Norwegian MoF expert group (`VX-20` hard checkpoint) | as docketed |
| **— STANDING —** | MOF FX intervention · Warsh task force (end-2026) · FR2004 weekly · credit weekly · **F2 carrier (every boot)** | `FL-BND-11` · 2027 lane · `VX-04` · `VX-02/11` · `VX-16` |

**Recently resolved** → 9/10 30Y-R (clean) · 9/15 20Y-R (`I'` fire, marker) · **9/16 FOMC (graded, `KB-BND-293`)** · 9/11 hyperscaler share (**DECLINED** under its own second-miss rule, `KB-BND-297`) — rows rotated verbatim to `domain/sources/2026-09-17_CATALYSTS_rotated_fired-rows_9-10_to_9-16.md`.

---

## BOTTOM LINE

**[2026-09-17 Thu ~08:2x ET → PRE-PRINT — PROME WQ-184 L0 spawn `prome-ae`, DOCKET L404 + L401. Markets OPEN. TIPS-R prints 1:00 PM; this block is updated after the grade.]**
*(9/15 block rotated verbatim → `domain/sources/2026-09-17_STATUS_archive_rotated_9-15-blocks.md`, crc32 `1463914424`.)*

🔑 **THE FED CAME IN DOVISH AGAINST THE CURVE AND THE CURVE DID NOT MOVE — THAT IS THE 9/16 RESULT.** +25bp to 3.75–4.00, 12–0, no guidance sentence; **SEP median terminal 4.125** (16 of 18 see one more hike; 2028 median 3.9 pencils cuts). My pre-registered falsifier (*SEP terminal ≥~5.00 with the curve unchanged*) **did NOT trigger** — but the **dovish branch** of the same asymmetry read, for which I had predicted *"a large repricing"*, **was the branch tested, and the repricing did not come**: 5Y +3.3bp, 10Y +1.0, 30Y −1.5, breakevens −5bp, TIP −0.38%, TLT +0.21% (vendor; official cells ~16:15). **The curve is holding a policy path 60–85bp above the Fed's own median through the one event that could have re-anchored it ⇒ the priced path is a market view, not a guidance view — an inflation-risk / credibility spread living in the same real leg that fired the add-gate.** Working model, not truth; graded honestly in both halves (`KB-BND-293`).

🔴 **`DFII10` 2.62 [9/15] = +12bp through the add-gate for a FOURTH published session ⇒ `BND-29` TRUE (70% hit): the breach is PERSISTENT, and the named threat to its persistence (a dovish SEP) arrived and did nothing.** Still authorises NO add — the count is Will's (WQ-246), 7/16 NO-ADD, root rule #5. `$0`.

🟠 **1:00 PM — 10Y TIPS-R `91282CRE3` $19B, bars frozen 9/9 and reproduced this morning** (ind <56.08 AND dlr >17.79 · cover <2.20; no `I'`; never counts). A stop above 2.438 is the highest 10Y TIPS stop since Oct-2008. **Confound stated before the print: FOMC-day-after plus a 7% Brent drop is a real-yield-UP, breakeven-DOWN tape — a soft print has a non-structural explanation and will not be read as a demand hole.**

⬜ **F2 PER-OP CARRIER BUILT (L401)** — `monitors/buyback_f2.py` + `registry/f2_reads.tsv`, every boot. **Zero in-scope ops have run since 9/10** (9/15 was TIPS; today's is 7Y–10Y) ⇒ **zero arrears; the gap was structural.** Six in-scope reads remain, 9/24 → 11/4. Metric declared and base-rated (0/52); selftest 22/22; **not independently verified.**

🔴 **TOMORROW 9/18: the FR2004 join** — the kill leg is unevaluable and a live `I'` fire (9/15) sits behind it. **That is the desk's critical path, not a build task.** Also owed: `BND-25`/`BND-26` on the 9/16 H.15 cells; the hyperscaler share is **DECLINED** (`KB-BND-297`).

**Position: TLT puts HOLD, no add, `$0`. Composite 12/35, fifteenth consecutive. Downgrade counter 0. OPEN predictions: 3.** Pre-print record → `analysis/2026-09-17_PREPRINT_TIPS-R_91282CRE3_SEP-grade_F2-carrier.md`.
